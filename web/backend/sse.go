package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"github.com/r3labs/sse/v2"
	"net/http"
	"sync"
)

var pendingTransactions = make(map[string]*PendingTransaction)
var mtx sync.Mutex

func setupSseListener(connectionId string, handler func(msg *sse.Event)) bool {
	client := sse.NewClient(fmt.Sprintf("https://api.ammer.io/push/notifications/v2/stream/subscribe/%s", connectionId))
	err := client.Subscribe("transaction", handler)
	if err != nil {
		return false
	}
	return true
}

func addSseTargetAccount(connectionId string, cardUUID string) bool {
	element := Element{
		AccountID: cardUUID,
		Start:     -1,
		Offset:    1,
	}
	elements := []Element{element}
	body, err := json.Marshal(map[string][]Element{
		"elements": elements,
	})
	if err != nil {
		return false
	}
	url := "https://api.ammer.io/push/notifications/v2/stream/submitRequest"
	req, _ := http.NewRequest("POST", fmt.Sprintf("%s/%s", url, connectionId), bytes.NewBuffer(body))
	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("Accept", "application/json")
	res, err := http.DefaultClient.Do(req)
	if err != nil {
		return false
	}
	defer res.Body.Close()
	return res.StatusCode == http.StatusOK
}

func sseHandler(msg *sse.Event) {
	var t *Transaction
	fmt.Println(string(msg.Data))
	err := json.Unmarshal(msg.Data, &t)
	if err != nil {
		fmt.Println(fmt.Sprintf("error in SSE: %s", err.Error()))
		return
	}
	//mtx.Lock()

	if pendingTransactions[t.TransactionID] == nil {
		//mtx.Unlock()
		return
	}
	p := pendingTransactions[t.TransactionID]
	p.Transaction = t

	//mtx.Unlock()
}

//
