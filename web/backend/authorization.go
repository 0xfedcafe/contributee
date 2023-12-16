package main

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"github.com/goccy/go-json"
	"io"
	"net/http"
)

func getUUIDbyCardNumber(cardNumber string) (UUIDByNumber, error) {
	fmt.Println(cardNumber)

	url := "https://api.ammer.io/wallet-proxy/api/cardUuidByNumber/"
	req, _ := http.NewRequest("GET", fmt.Sprintf("%s/%s", url, cardNumber), nil)
	res, _ := http.DefaultClient.Do(req)
	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

	var p UUIDByNumber
	err := json.Unmarshal(body, &p)
	if err != nil {
		return UUIDByNumber{}, err
	}

	return p, nil
}

func authorizeHandler(c *gin.Context) {
	cardNumber := c.PostForm("card_number")

	p, err := getUUIDbyCardNumber(cardNumber)

	if err != nil {
		c.Status(500)
	}

	m, err := getMetadata(p.UUID)

	pub := m.X509PublicKey
	fmt.Println(pub)
	if err != nil {
		c.Status(500)
	}

	//fmt.Println(metadata)
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
