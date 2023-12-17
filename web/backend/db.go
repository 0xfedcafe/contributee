package main

import (
	"encoding/json"
	"fmt"
	"go.etcd.io/bbolt"
	"strconv"
)

func addUser(db *bbolt.DB, user User) error {
	return db.Update(func(tx *bbolt.Tx) error {
		userBucket := tx.Bucket([]byte("User"))
		if userBucket == nil {
			return fmt.Errorf("bucket not found")
		}

		userBytes, err := json.Marshal(user)
		if err != nil {
			return err
		}

		return userBucket.Put([]byte(user.CardNumber), userBytes)
	})
}

func addSessionToken(db *bbolt.DB, sessionToken SessionToken) error {
	return db.Update(func(tx *bbolt.Tx) error {
		userBucket := tx.Bucket([]byte("SessionToken"))
		if userBucket == nil {
			return fmt.Errorf("bucket not found")
		}

		sessionTokenBytes, err := json.Marshal(sessionToken)
		if err != nil {
			return err
		}

		return userBucket.Put([]byte(sessionToken.Token), sessionTokenBytes)
	})
}

func addFunding(db *bbolt.DB, funding Funding) error {
	return db.Update(func(tx *bbolt.Tx) error {
		fundingBucket := tx.Bucket([]byte("Funding"))
		if fundingBucket == nil {
			return fmt.Errorf("bucket not found")
		}

		fundingBytes, err := json.Marshal(funding)
		if err != nil {
			return err
		}

		return fundingBucket.Put([]byte(strconv.Itoa(funding.FundingID)), fundingBytes)
	})
}

func addDonation(db *bbolt.DB, donation Donation) error {
	return db.Update(func(tx *bbolt.Tx) error {
		donationBucket := tx.Bucket([]byte("Donation"))
		if donationBucket == nil {
			return fmt.Errorf("bucket not found")
		}

		donationBytes, err := json.Marshal(donation)
		if err != nil {
			return err
		}

		return donationBucket.Put([]byte(strconv.Itoa(donation.DonationID)), donationBytes)
	})
}

func addExchange(db *bbolt.DB, exchange Exchange) error {
	return db.Update(func(tx *bbolt.Tx) error {
		exchangeBucket := tx.Bucket([]byte("Exchange"))
		if exchangeBucket == nil {
			return fmt.Errorf("bucket not found")
		}

		exchangeBytes, err := json.Marshal(exchange)
		if err != nil {
			return err
		}

		return exchangeBucket.Put([]byte(strconv.Itoa(exchange.ExchangeID)), exchangeBytes)
	})
}

func extractAllExchanges(db *bbolt.DB) ([]Exchange, error) {
	var exchanges []Exchange

	err := db.View(func(tx *bbolt.Tx) error {
		exchangeBucket := tx.Bucket([]byte("Exchange"))
		if exchangeBucket == nil {
			return fmt.Errorf("bucket not found")
		}

		return exchangeBucket.ForEach(func(k, v []byte) error {
			var exchange Exchange
			if err := json.Unmarshal(v, &exchange); err != nil {
				return err
			}

			exchanges = append(exchanges, exchange)
			return nil
		})
	})

	if err != nil {
		return nil, err
	}

	return exchanges, nil
}

func extractFundingByID(db *bbolt.DB, fundingID int) (*Funding, error) {
	var funding *Funding

	err := db.View(func(tx *bbolt.Tx) error {
		fundingBucket := tx.Bucket([]byte("Funding"))
		if fundingBucket == nil {
			return fmt.Errorf("bucket not found")
		}

		fundingBytes := fundingBucket.Get([]byte(strconv.Itoa(fundingID)))
		if fundingBytes == nil {
			return fmt.Errorf("funding not found")
		}

		if err := json.Unmarshal(fundingBytes, &funding); err != nil {
			return err
		}

		return nil
	})

	if err != nil {
		return nil, err
	}

	return funding, nil
}

func loginUser(db *bbolt.DB, cardNumber string, token string) error {
	return db.Update(func(tx *bbolt.Tx) error {
		userBucket := tx.Bucket([]byte("User"))
		if userBucket == nil {
			return fmt.Errorf("bucket not found")
		}

		userBytes := userBucket.Get([]byte(cardNumber))
		if userBytes == nil {
			return fmt.Errorf("user not found")
		}

		var user User
		if err := json.Unmarshal(userBytes, &user); err != nil {
			return err
		}

		userBytes, err := json.Marshal(user)
		if err != nil {
			return err
		}

		return userBucket.Put([]byte(cardNumber), userBytes)
	})
}

func getSessionTokens(db *bbolt.DB, cardNumber string) ([]string, error) {
	var tokens []string
	err := db.View(func(tx *bbolt.Tx) error {
		sessionTokenBucket := tx.Bucket([]byte("SessionToken"))
		if sessionTokenBucket == nil {
			return fmt.Errorf("bucket not found")
		}
		sessionTokenBytes := sessionTokenBucket.Get([]byte(cardNumber))
		if sessionTokenBytes == nil {
			return fmt.Errorf("user not found")
		}

		var sessionToken SessionToken
		if err := json.Unmarshal(userBytes, &user); err != nil {
			return err
		}
	})
	return tokens, err
}

func initDB(db *bbolt.DB) error {
	err := db.Update(func(tx *bbolt.Tx) error {
		_, err := tx.CreateBucketIfNotExists([]byte("Funding"))
		if err != nil {
			return err
		}

		_, err = tx.CreateBucketIfNotExists([]byte("User"))
		if err != nil {
			return err
		}

		_, err = tx.CreateBucketIfNotExists([]byte("RequestFund"))
		if err != nil {
			return err
		}

		_, err = tx.CreateBucketIfNotExists([]byte("Donation"))
		if err != nil {
			return err
		}

		_, err = tx.CreateBucketIfNotExists([]byte("Exchange"))
		if err != nil {
			return err
		}

		_, err = tx.CreateBucketIfNotExists([]byte("SessionToken"))
		if err != nil {
			return err
		}

		return nil
	})

	if err != nil {
		return err
	}

	return nil
}
