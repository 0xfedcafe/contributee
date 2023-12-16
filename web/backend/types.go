package main

type UUIDByNumber struct {
	UUID   string `json:"cardUuid"`
	Issuer int    `json:"issuer"`
}

type Metadata struct {
	Platform          *string `json:"platform,omitempty"`
	Alias             *string `json:"alias,omitempty"`
	AccountId         string  `json:"accountId,omitempty"`
	X509PublicKeyHash string  `json:"x509PublicKeyHash,omitempty"`
	X509PublicKey     string  `json:"x509PublicKey,omitempty"`
	CardNumber        string  `json:"cardNumber,omitempty"`
	CardIssuer        int     `json:"cardIssuer,omitempty"`
	FirstName         []int   `json:"firstName,omitempty"`
	LastName          []int   `json:"lastName,omitempty"`
}
