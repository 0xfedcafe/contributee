package main

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"io"
	"net/http"
)

func authorizeHandler(c *gin.Context) {
	cardNumber := c.PostForm("card_number")
	fmt.Println(cardNumber)

	url := "https://api.ammer.io/wallet-proxy/api/cardUuidByNumber/cardNumber"
	req, _ := http.NewRequest("GET", fmt.Sprintf("%s%s", url, cardNumber), nil)
	res, _ := http.DefaultClient.Do(req)
	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

	getPublicKey(body)
}

func getPublicKey(UUID string) {
	url := "https://api.ammer.io/wallet-proxy/metadata/metadata/cardId"
	req, _ := http.NewRequest("GET", fmt.Sprintf("%s/%s", url, UUID), nil)
	req.Header.Add("accept", "application/json")
	res, _ := http.DefaultClient.Do(req)
	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)
	fmt.Println(body)
}

//
