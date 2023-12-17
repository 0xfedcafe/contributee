package main

type Funding struct {
	FundingID      int    `json:"fundingID"`
	UserCardNumber string `json:"userCardNumber"`
	Description    string `json:"description"`
	Timestamp      string `json:"timestamp"`
	Picture        []byte `json:"picture"`
}

type User struct {
	CardNumber     string `json:"cardNumber"`
	LoggedIn       bool   `json:"loggedIn"`
	LoginTimestamp string `json:"loginTimestamp"`
}

type Donation struct {
	DonationID     int     `json:"donationID"`
	UserCardNumber string  `json:"userCardNumber"`
	FundingID      int     `json:"fundingID"`
	CurrencyID     int     `json:"currencyID"`
	Amount         float64 `json:"amount"`
}

type Exchange struct {
	ExchangeID     int     `json:"exchangeID"`
	FromCurrency   string  `json:"fromCurrency"`
	ToCurrency     string  `json:"toCurrency"`
	Rate           float64 `json:"rate"`
	UserCardNumber string  `json:"userCardNumber"`
}

type Currency struct {
	CurrencyID int    `json:"currencyID"`
	Ticker     string `json:"ticker"`
	Name       string `json:"name"`
}
