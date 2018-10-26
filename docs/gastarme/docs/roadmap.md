## Where to start?
 1 - First of all, you'll need to create a [user](users.md)  
 2 - Once the user was created, you can obtain a [JWT Token](auth.md)  
 3 - Once authenticated, you must create a [wallet](wallets.md)  
 4 - With your wallet created, you'll be able to add [Credit Cards](creditcards.md) to it
 5 - With Credit Cards, you'll be able to make [purchases](purchases.md)  
 6 - Each purchase will generate a [bill](billings.md) that should be paid to restore your credit limit  

## Do i need to be authenticated?
Yes, for all the actions but user creation.

## How to i set my authentication?
Sending your `JWT` token on the `Authorization` header.

## What are the permission levels?

 **User** and **Superuser**. **Users** can create wallets, add credit cards, make purchases and pay bills while **Superusers** can list users and list and delete wallets.

## Example of a request

```
curl --request POST \
  --url http://0.0.0.0:8001/v1/wallets/1/creditcards/ \
  --header 'authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo4LCJ1c2VybmFtZSI6ImpvZGhhcW5hQGVtYWlsLmNvbSIsImV4cCI6MTU0MDUxNzQ2MSwiZW1haWwiOiJqb2RoYXFuYUBlbWFpbC5jb20iLCJvcmlnX2lhdCI6MTU0MDUxMzg2MX0.AucdOFhgPTybPe0-vG595yrY013mkV8oKWM2uBFAUc8' \
  --header 'content-type: application/json' \
  --data '{
  "wallet": 1,
	"cardholder_name": "JOHN DOE",
	"number": "4329721240311135",
	"cvv": "999",
	"expires_at": "2018-11-30",
	"monthly_billing_day": 19,
	"limit": "50.00"
}'
```
