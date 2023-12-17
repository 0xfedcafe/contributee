package main

import (
	"github.com/gin-gonic/gin"
	"go.etcd.io/bbolt"
	"log"
)

func main() {
	db, err := bbolt.Open("my.db", 0666, nil)
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

	if err := initDB(db); err != nil {
		return
	}

	r := gin.Default()
	env := &Env{db: db}
	r.POST("/authorize", env.authorizeHandler)
	err = r.Run()

	if err != nil {
		return
	} // listen and serve on 0.0.0.0:8080 (for windows "localhost:8080")
}
