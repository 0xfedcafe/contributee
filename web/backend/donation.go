package main

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"github.com/yeqown/go-qrcode/v2"
	"github.com/yeqown/go-qrcode/writer/standard"
	"net/http"
	"path/filepath"
	"strings"
)

func donationHandler(c *gin.Context) {
	wr := c.PostForm("wallet")
	qrc, err := qrcode.New(wr)
	if err != nil {
		fmt.Printf("could not generate QRCode: %v", err)
		return
	}

	w, err := standard.New("qr.jpeg", standard.WithHalftone("./test2.png"),
		standard.WithQRWidth(25))
	if err != nil {
		fmt.Printf("standard.New failed: %v", err)
		return
	}

	// save file
	if err = qrc.Save(w); err != nil {
		fmt.Printf("could not save image: %v", err)
	}
	c.String(200, "Wow")
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
