package main

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"github.com/goccy/go-json"
	"io"
	"net/http"
)

func authorizeHandler(c *gin.Context) {
	cardNumber := c.PostForm("card_number")
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
		c.Status(500)
	}

	fmt.Println(p.UUID)

	_, err = getPublicKey(p.UUID)
	if err != nil {
		c.Status(500)
	}

	//fmt.Println(metadata)
}

func getPublicKey(UUID string) (*Metadata, error) {

	url := "https://api.ammer.io/wallet-proxy/metadata/metadata/"
	req, _ := http.NewRequest("GET", fmt.Sprintf("%s/%s", url, UUID), nil)
	req.Header.Add("accept", "application/json")
	res, _ := http.DefaultClient.Do(req)
	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	var m *Metadata //&Metadata{}

	err := json.Unmarshal(body, &m)

	fmt.Println(m)

	if err != nil {
		return nil, err
	}

	return m, nil
}

//
