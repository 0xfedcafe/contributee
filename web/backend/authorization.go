package main

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"github.com/goccy/go-json"
	"github.com/google/uuid"
	"io"
	"net/http"
)

func getUUIDbyCardNumber(cardNumber string) (*UUIDByNumber, error) {
	fmt.Println(cardNumber)

	url := "https://api.ammer.io/wallet-proxy/api/cardUuidByNumber/"
	req, _ := http.NewRequest("GET", fmt.Sprintf("%s/%s", url, cardNumber), nil)
	res, _ := http.DefaultClient.Do(req)
	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

	var p *UUIDByNumber
	err := json.Unmarshal(body, &p)
	if err != nil {
		return &UUIDByNumber{}, err
	}

	return p, nil
}

//

func (env *Env) loginHandler(c *gin.Context) {
	cardNumber := c.PostForm("card_number")
	p, err := getUUIDbyCardNumber(cardNumber)

	loginToken := uuid.New().String()
	c.Data(http.StatusOK, "application/json", []byte(fmt.Sprintf(`{"key":"%s"}`, loginToken)))
	return

	if err != nil {
		c.Status(500)
		return
	}

	wb, err := getWalletBalance(p.UUID)
	if err != nil {
		c.Status(500)
		return
	}
	fmt.Println(wb)
	var walletID string
	var address string
	for _, currency := range wb {
		if currency.AssetID == TumAuthTokenUUID {
			walletID = currency.WalletID
			address = currency.Address
		}
	}
	transactionId := uuid.New().String()
	transactionGroupId := uuid.New().String()
	template := &TransactionTemplate{
		NetworkFee: NetworkFee{
			NetworkFee:   0,
			UnitPrice:    0,
			UnitQuantity: 100000,
			UnitAssetId:  TumAuthTokenUUID,
		},
		TransactionId:      transactionId,
		Asset:              TumAuthTokenUUID,
		TransactionGroupId: transactionGroupId,
		Sender: TransactionParticipant{
			Address:    address,
			InternalId: walletID,
		},
		Receiver: TransactionParticipant{
			Address: address,
		},
		Amount: 0,
		Memo:   "login",
	}

	fmt.Println(walletID, address)
	getTemplate := createTransaction(template)
	if !getTemplate {
		c.Status(500)
		return
	}

	connectionId := uuid.New().String()

	mtx.Lock()
	pendingTransactions[transactionId] = &PendingTransaction{nil, connectionId, p.UUID}
	mtx.Unlock()

	kk := make(chan bool)
	res := make(chan bool)
	go func() {
		kk <- setupSseListener(connectionId, sseHandler)
	}()
	go func() {
		res <- addSseTargetAccount(connectionId, p.UUID)
	}()

	if !<-kk || !<-res || pendingTransactions[transactionId].Transaction.ExternalTransactionStatus != "FINALIZED" {
		c.Status(500)
		return
	}

	//err = loginUser(env.db, cardNumber)
	if err != nil {
		c.Status(500)
		return
	}

	mtx.Lock()
	pendingTransactions[transactionId] = nil
	mtx.Unlock()
	//loginToken := uuid.New().String()

	//b, err := getWalletBalance(p.UUID)

	//fmt.Println(b)

	c.Data(http.StatusOK, "application/json", []byte(fmt.Sprintf(`{"key":"%s"}`, loginToken)))

}

func getMetadata(UUID string) (*Metadata, error) {

	url := "https://api.ammer.io/wallet-proxy/metadata/metadata/"
	req, _ := http.NewRequest("GET", fmt.Sprintf("%s/%s", url, UUID), nil)
	req.Header.Add("accept", "application/json")
	res, _ := http.DefaultClient.Do(req)
	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	var m *Metadata

	err := json.Unmarshal(body, &m)

	fmt.Println(m)

	if err != nil {
		return nil, err
	}

	return m, nil
}

func getWalletBalance(UUID string) (WalletBalance, error) {
	url := fmt.Sprintf("https://api.ammer.io/wallet-proxy/api/v3/balance/balances/assets/%s", UUID)

	req, err := http.NewRequest("GET", url, nil)

	req.Header.Add("accept", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	var wb WalletBalance

	err = json.Unmarshal(body, &wb)
	if err != nil {
		return WalletBalance{}, nil
	}

	fmt.Println(wb)
	return wb, nil
}

//
