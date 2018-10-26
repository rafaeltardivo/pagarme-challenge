## Purchases - `/v1/purchases/`


| Permission level  |   URL| Method  | Format   |  HTTP Status Code |
|---|---|---|---|---|
|  User |  `/v1/purchases/` |   `POST`|  `json` |  `201`, `400` |


##CREATE
** Permission required **: User

#### Headers
|  Field | Content  |
|---|---|
|  Content-Type | application/json  |
|  Authorization | JWT `{token}` |

#### Request Content

|  Field | Type  | Required  |  Min Length |  Max Length |  Detail |
|---|---|---|---|---|---|
| `wallet` |  Integer |  Yes |  1 |  32 |  Related wallet id |
| `value` |  Decimal |  Yes | 3  | 12  | Purchase value  |


#### Response Content
|  Field | Type  |Detail   |
|---|---|---|
|  `id`|  Integer |  Created purchase id|
|  `payments`|  List |  A collection of payments|
|  `wallet`|  Integer |  Related wallet id|
|  `credit_limit` | Decimal  |  Purchase value |
|  `made_at`|  Timestamp |  Date and time of the purchase |

#### Example

**Event**: User `POST` to `/v1/purchases/`  
**Header Content**:
```
Content-Type: application/
Authorization: JWT {token}
```
**Body Content**: 
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
	"id": 2,
	"payments": [
		{
			"value": "150.00",
			"credit_card": 1
		}
	],
	"value": "150.00",
	"made_at": "2018-10-19T13:08:47.846428",
	"wallet": 1
}
```

#### Validations
**HTTP Status Code**: `400`  

| Field  | Content  |  Detail |
|---|---|---|
| `wallet`  | Wallet does not belong to current user. |  You must user your own wallet |
| `wallet`  | Must first have credit cards. |  In order to make a purchase, you mus first have credit cards |
| `email`|  This field is required. | The payload must contain a valid email address  |
| `email` | Enter a valid email address.  | The email must have between 6 and 100 characters  |


##RETRIEVE
** Permission required **: User

#### Headers
|  Field | Content  |
|---|---|
|  Content-Type | application/json  |
|  Authorization | JWT `{token}` |

#### Request Content
 - Add the purchase id to the URL: `/v1/purchases/{1}/`

#### Response Content
|  Field | Type  |Detail   |
|---|---|---|
|  `id`|  Integer |  Created purchase id|
|  `payments`|  List |  A collection of payments|
|  `wallet`|  Integer |  Related wallet id|
|  `credit_limit` | Decimal  |  Purchase value |
|  `made_at`|  Timestamp |  Date and time of the purchase |

#### Example

**Event**: User `GET` to `/v1/wallets/1/`  
**Header Content**:
```
Content-Type: application/
Authorization: JWT {token}
```
**Body Content**:  None


**HTTP Status Code**: `200`  
**Response Content**:
```
{
	"id": 1,
	"payments": [
		{
			"value": "150.00",
			"credit_card": 1
		}
	],
	"value": "150.00",
	"made_at": "2018-10-19T13:08:47.846428",
	"wallet": 1
}
```

##LIST
** Permission required **: User

#### Headers
|  Field | Content  |
|---|---|
|  Content-Type | application/json  |
|  Authorization | JWT `{token}` |

#### Request Content
 - None

#### Filters

| Field  | Type  | Required  | Detail  |
|---|---|---|---|
| `made_at__gte`  | Date  |  No |  Filter by minimum date of purchase (greater than or equal)|
| `made_at__lte`  | Date  |  No |  Filter by maximum date of purchase (lesser than or equal)|

#### Response Content
|  Field | Type  |Detail   |
|---|---|---|
|  `id`|  Integer |  Created purchase id|
|  `payments`|  List |  A collection of payments|
|  `wallet`|  Integer |  Related wallet id|
|  `credit_limit` | Decimal  |  Purchase value |
|  `made_at`|  Timestamp |  Date and time of the purchase |

#### Example

**Event**: User `GET` to `/v1/purchases/`  
**Header Content**:
```
Content-Type: application/
Authorization: JWT {token}
```
**Body Content**:  None


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
			"payments": [
				{
					"value": "200.00",
					"credit_card": 1
				}
			],
			"value": "200.00",
			"made_at": "2018-10-19T11:01:51.621101",
			"wallet": 1
		},
		{
			"id": 2,
			"payments": [
				{
					"value": "150.00",
					"credit_card": 1
				}
			],
			"value": "150.00",
			"made_at": "2018-10-19T13:08:47.846428",
			"wallet": 1
		}
	]
}
```