## Credit Cards - `/v1/wallets/{wallet_id}/creditcards/`


| Permission level  |   URL| Method  | Format   |  HTTP Status Code |
|---|---|---|---|---|
|  User |  `/v1/wallets/{wallet_id}/creditcards/` |   `POST`, `GET`, `DELETE`|  `json` |  `200`, `201`, `204`, `400` |

##CREATE
** Permission required **: User

#### Request Content
|  Field | Type  | Required  |  Min Length |  Max Length |  Detail |
|---|---|---|---|---|---|
| `wallet` |  Integer |  Yes |  1 |  32 |  Related wallet id |
| `number` |  String |  Yes |  16 |  16 |  Card number |
| `cardholder_name` |  String |  Yes | 8  | 26  | Card holder  |
| `cvv` |  String |  Yes | 3  | 3  | Card verification value  |
| `expires_at` |  Date |  Yes | 10  | 10  | Card expiration date  |
| `monthly_billing_day` |  Integer |  Yes | 1  | 2  | Card monthly billing date  |
| `limit` |  Decimal |  Yes | 3  | 12  | Card credit limit  |

#### Response Content
|  Field | Type  |Detail   |
|---|---|---|
| `wallet` |  Integer | Related wallet id |
| `number` |  String | Card number |
| `cardholder_name` | String |  Card holder  |
| `cvv` |  String | Card verification value  |
| `expires_at` |  Date | Card expiration date  |
| `monthly_billing_day` | Date | Card monthly billing date  |
| `limit` |  Decimal | Card credit limit  |

#### Example

**Event**: User `POST` to `/v1/wallets/1/creditcards/`  
**Request Content**:
```
{
  	"wallet": 1,
	"cardholder_name": "TEST USER ONE",
	"number": "4729333012967719",
	"cvv": "999",
	"expires_at": "2022-10-30",
	"monthly_billing_day": 9,
	"limit": "900.00"
}
```

**HTTP Status Code**: `201`  
**Response Content**:
```
{
	"id": 1,
	"number": "4729333012967719",
	"cardholder_name": "TEST USER ONE",
	"cvv": "999",
	"expires_at": "2022-10-30",
	"monthly_billing_day": 9,
	"limit": "900.00",
	"wallet": 1
}
```

#### Validations
**HTTP Status Code**: `400`  

| Content  | Detail  |
|---|---|
| `number`: This field is required.  | The payload must contain a number |
| `number`: Must contain 16 digits.  | The card number must contain 16 digits |
| `number`: Must contain only numbers.  | The number must contain only numbers |
| `number`: Ensure this field has no more than 16 characters. |  The number must contain maximum 16 characters |
| `cardholder_name`: This field is required.  | The payload must contain a cardholder_name |
| `cardholder_name`: Must be letters and/or spaces.  | The cardholder_name must contain only letters and spaces |
| `cardholder_name`: Ensure this field has no more than 26 characters. |  The number must contain maximum 26 characters |
| `cardholder_name`: Must contain at least 7 characters. |  The number must contain at least 7 characters. |
| `cvv`: This field is required.  | The payload must contain a cvv |
| `cvv`: Must contain 3 digits.  | The cvv must contain 3 digits |
| `cvv`: Must contain only numbers.  | The cvv must contain only numbers |
| `cvv`: Ensure this field has no more than 3 characters. |  The number must contain maximum 3 characters |
| `expires_at`: This field is required.  | The payload must contain a expires_at |
| `expires_at`: Card already expired.  | The card is already expired |
| `monthly_billing_day`: This field is required.  | The payload must contain a monthly_billing_day |
| `monthly_billing_day`: Must be between days 1 and 20.  | The monthly_billing_day must be between days 1 and 20 |
| `limit`: This field is required.  | The payload must contain a limit |
| `limit`: Must be greater than 0.  | The limit must be greater than 0 |
| `wallet`: This field is required.  | The payload must contain a limit |
| `wallet`: Wallet does not belong to current user.  | The user can only add cards to his own wallets |


##RETRIEVE
** Permission required **: User
#### Request Content
 - Add the wallet  and the creditcard id to the URL: `/v1/wallets/{wallet_id}/creditcards/{creditcard_id}/`

#### Response Content
|  Field | Type  |Detail   |
|---|---|---|
| `wallet` |  Integer | Related wallet id |
| `number` |  String | Card number |
| `cardholder_name` | String |  Card holder  |
| `cvv` |  String | Card verification value  |
| `expires_at` |  Date | Card expiration date  |
| `monthly_billing_day` | Date | Card monthly billing date  |
| `limit` |  Decimal | Card credit limit  |



#### Example

**Event**: User `GET` to `/v1/wallets/1/creditcards/1/`  
**Request Content**: `None`

**HTTP Status Code**: `200`  
**Response Content**:
```
{
	"id": 1,
	"number": "4729333012967724",
	"cardholder_name": "JOHN DOE",
	"cvv": "999",
	"expires_at": "2018-11-30",
	"monthly_billing_day": 19,
	"limit": "100.00",
	"wallet": 1
}
```

##LIST
** Permission required **: User
#### Request Content
 - None

#### Filters

| Field  | Type  | Required  | Detail  |
|---|---|---|---|
| `expires_at_min`  | Date  |  No |  Filter by minimum date of expiration |
| `expires_at_max`  | Date  |  No |  Filter by maximum date of expiration |
| `limit_min` |  Decimal | No  |  Filter by minimum limit |
| `limit_max` |  Decimal | No  |  Filter by maximum limit |

#### Response Content
|  Field | Type  |Detail   |
|---|---|---|
| `wallet` |  Integer | Related wallet id |
| `number` |  String | Card number |
| `cardholder_name` | String |  Card holder  |
| `cvv` |  String | Card verification value  |
| `expires_at` |  Date | Card expiration date  |
| `monthly_billing_day` | Date | Card monthly billing date  |
| `limit` |  Decimal | Card credit limit |

#### Example

**Event**: User `GET` to `/v1/wallets/1/creditcards/`  
**Request Content**: `None`

**HTTP Status Code**: `200`  
**Response Content**:
```
{
	"count": 2,
	"next": null,
	"previous": null,
	"results": [
		{
			"id": 1,
			"number": "4729333012967724",
			"cardholder_name": "JOHN DOE",
			"cvv": "999",
			"expires_at": "2018-11-30",
			"monthly_billing_day": 19,
			"limit": "100.00",
			"wallet": 1
		},
		{
			"id": 2,
			"number": "4729333012967784",
			"cardholder_name": "JOHN DOE",
			"cvv": "999",
			"expires_at": "2018-11-30",
			"monthly_billing_day": 19,
			"limit": "100.00",
			"wallet": 1
		},
	]
}
```

##DELETE
** Permission required **: User
#### Request Content
- Add the wallet id to the URL: `/v1/wallets/{wallet_id}/creditcards/{creditcard_id}/`


#### Example

**Event**: User `DELETE` to `/v1/wallets/1/creditcards/1/`  
**Request Content**: `None`

**HTTP Status Code**: `204`  
**Response Content**: `None`

