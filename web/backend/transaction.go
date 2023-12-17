package main

import (
	"bytes"
	"fmt"
	"github.com/goccy/go-json"
	"io"
	"net/http"
)

func createTransaction(template *TransactionTemplate) bool {
	url := "https://api.ammer.io/wallet-proxy/api/v3/transactions/create/"
	templateJson, err := json.Marshal(template)
	if err != nil {
		return false
	}
	req, _ := http.NewRequest("POST", url, bytes.NewBuffer(templateJson))
	req.Header.Set("Content-Type", "application/json")
	res, _ := http.DefaultClient.Do(req)
	defer res.Body.Close()
	if res.StatusCode == http.StatusOK {
		return true
	}
	return false
}

func lookupTransaction(transactionId string, transactionGroupId string) (Transaction, error) {
	url := "https://api.ammer.io/wallet-proxy/api/v3/transactions/lookup"
	req, _ := http.NewRequest("GET", fmt.Sprintf("%s/%s/%s", url, transactionGroupId, transactionId), nil)
	req.Header.Add("accept", "application/json")
	res, _ := http.DefaultClient.Do(req)
	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

	var tx Transaction
	err := json.Unmarshal(body, &tx)
	if err != nil {
		return Transaction{}, err
	}
	return tx, nil
}
