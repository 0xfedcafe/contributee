package main

type UUIDByNumber struct {
	UUID   string `json:"cardUuid"`
	Issuer int    `json:"issuer"`
}

type Metadata struct {
	Platform          string `json:"platform,omitempty"`
	Alias             string `json:"alias,omitempty"`
	AccountId         string `json:"accountId"`
	X509PublicKeyHash string `json:"x509PublicKeyHash"`
	X509PublicKey     string `json:"x509PublicKey"`
	CardNumber        string `json:"cardNumber"`
	CardIssuer        int    `json:"cardIssuer"`
	FirstName         []int  `json:"firstName,omitempty"`
	LastName          []int  `json:"lastName,omitempty"`
}
