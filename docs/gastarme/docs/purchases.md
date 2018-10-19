## Purchases - `/v1/purchases/`


| Permission level  |   URL| Method  | Format   |  HTTP Status Code |
|---|---|---|---|---|
|  User |  `/v1/purchases/` |   `POST`|  `json` |  `201`, `400` |


##CREATE
** Permission required **: User

#### Request Content

|  Field | Type  | Required  |  Min Length |  Max Length |  Detail |
|---|---|---|---|---|---|
| `wallet` |  Integer |  Yes |  1 |  32 |  Related wallet id |
| `value` |  Decimal |  Yes | 3  | 12  | Purchase value  |


#### Response Content
|  Field | Type  |Detail   |
|---|---|---|
|  `wallet`|  Integer |  Related wallet id|
|  `credit_limit` | Decimal  |  Purchase value |
|  `made_at`|  Timestamp |  Date and time of the purchase |

#### Example

**Event**: User `POST` to `/v1/purchases/`  
**Request Content**: 
```
{
	"wallet": 1,
	"value": "150.00"	
}
```

**HTTP Status Code**: `201`  
**Response Content**:
```
{
	"id": 3,
	"value": "150.00",
	"made_at": "2018-10-18T10:53:52.204568-03:00",
	"wallet": 1
}
```

#### Validations
**HTTP Status Code**: `400`  

| Content  | Detail  |
|---|---|
| `wallet`: Wallet does not belong to current user  | You must user your own wallet |
| `wallet`: Must first have credit cards  | In order to make a purchase, you mus first have credit cards |
| `value`: Must be greater than 0  | The purchase value must be greater than 0 |
| `value`: Value exceeds your credit available  | The purchase value exceeds the credit limit of your wallett |
