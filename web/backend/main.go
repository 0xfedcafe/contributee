package main

import (
	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()
	r.POST("/authorize", authorizeHandler)
	r.POST("/submit_vote", donationHandler)
	r.POST("/upload", uploadFileHandler)
	err := r.Run()

	if err != nil {
		return
	} // listen and serve on 0.0.0.0:8080 (for windows "localhost:8080")
}
