package main

import (
	"github.com/gin-gonic/gin"
	"net/http"
	"path/filepath"
	"strings"
)

func donationHandler(c *gin.Context) {

}

func uploadFileHandler(c *gin.Context) {
	form, err := c.MultipartForm()
	if err != nil {
		c.String(http.StatusBadRequest, "get form err: %s", err.Error())
		return
	}

	files := form.File["files"]
	for _, file := range files {
		filename := filepath.Base(file.Filename)
		buff := make([]byte, 512)
		f, err := file.Open()
		if err != nil {
			c.String(http.StatusBadRequest, "upload file err: %s", err.Error())
			return
		}

		if _, err = f.Read(buff); err != nil {
			c.String(http.StatusBadRequest, "upload file err: %s", err.Error())
			return
		}

		if !strings.HasPrefix(http.DetectContentType(buff), "image/") {
			c.String(http.StatusBadRequest, "don't hack me 😭")
			return
		}

		if err := c.SaveUploadedFile(file, filename); err != nil {
			c.String(http.StatusBadRequest, "upload file err: %s", err.Error())
			return
		}
		f.Close()
	}

}
