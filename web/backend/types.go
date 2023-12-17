package main

type UUIDByNumber struct {
	UUID   string `json:"cardUuid"`
	Issuer int    `json:"issuer"`
}

type Metadata struct {
	Platform          string `json:"platform,omitempty"`
	Alias             string `json:"alias,omitempty"`
	AccountId         string `json:"accountId,omitempty"`
	X509PublicKeyHash string `json:"x509PublicKeyHash,omitempty"`
	X509PublicKey     string `json:"x509PublicKey,omitempty"`
	CardNumber        string `json:"cardNumber,omitempty"`
	CardIssuer        int    `json:"cardIssuer,omitempty"`
	FirstName         []int  `json:"firstName,omitempty"`
	LastName          []int  `json:"lastName,omitempty"`
}

type CurrencyBalance struct {
	Address        string `json:"address,omitempty"`
	AssetID        string `json:"assetId,omitempty"`
	WalletID       string `json:"walletId,omitempty"`
	StrBalance     string `json:"strBalance"`
	ReducedBalance string `json:"reducedBalance,omitempty"`
	Balance        int    `json:"balance,omitempty"`
}

type WalletBalance = []CurrencyBalance

type NetworkFee struct {
	NetworkFee   int    `json:"networkFee"`
	UnitPrice    int    `json:"unitPrice"`
	UnitQuantity int    `json:"unitQuantity"`
	UnitAssetId  string `json:"unitAssetId"`
}

type TransactionParticipant struct {
	External   bool   `json:"external,omitempty"`
	Address    string `json:"address"`
	AccountId  string `json:"accountId,omitempty"`
	InternalId string `json:"internalId,omitempty"`
	StrBalance string `json:"strBalance,omitempty"`
	Balance    int    `json:"balance,omitempty"`
}

type TransactionTemplate struct {
	NetworkFee         NetworkFee             `json:"networkFee"`
	TransactionId      string                 `json:"transactionId"`
	Asset              string                 `json:"asset"`
	TransactionGroupId string                 `json:"transactionGroupId"`
	Sender             TransactionParticipant `json:"sender"`
	Receiver           TransactionParticipant `json:"receiver"`
	Amount             int                    `json:"amount"`
	Memo               string                 `json:"memo,omitempty"`
}

type HexTransactionData struct {
	MetaData           bool   `json:"metaData"`
	NeedsSignature     bool   `json:"needsSignature"`
	SignedHex          string `json:"signedHex"`
	Idx                int    `json:"idx"`
	HexPayload         string `json:"hexPayload"`
	SignatureAlgorithm string `json:"signatureAlgorithm"`
}

type Transaction struct {
	StrAmount                 string `json:"strAmount"`
	StrFeeAmount              string `json:"strFeeAmount"`
	Direction                 string `json:"direction,omitempty"`
	Timestamp                 int64  `json:"timestamp"`
	Type                      string `json:"type,omitempty"`
	StatusCode                string `json:"statusCode"`
	NetworkFee                NetworkFee
	TransactionID             string `json:"transactionId"`
	Asset                     string `json:"asset"`
	InternalTransactionStatus string `json:"internalTransactionStatus"`
	HexTransactionData        []HexTransactionData
	TransactionGroupID        string `json:"transactionGroupId"`
	SubmitterID               string `json:"submitterId"`
	Sender                    TransactionParticipant
	Receiver                  TransactionParticipant
	Amount                    int64       `json:"amount"`
	InternalFee               interface{} `json:"internalFee,omitempty"`
	ExternalTransactionStatus string      `json:"externalTransactionStatus"`
	LinkedRawTransaction      string      `json:"linkedRawTransaction"`
	Memo                      string      `json:"memo,omitempty"`
	ExpiryTime                int64       `json:"expiryTime,omitempty"`
	TxFlag                    interface{} `json:"txFlag,omitempty"`
	PayloadTransform          string      `json:"payloadTransform"`
	CreatedTimestamp          int64       `json:"createdTimestamp"`
}
