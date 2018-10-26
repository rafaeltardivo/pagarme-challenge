## Wallets - `/v1/wallets/`


| Permission level  |   URL| Method  | Format   |  HTTP Status Code |
|---|---|---|---|---|
|  User |  `/v1/wallets/` |   `POST`, `GET`|  `json` |  `200`, `201`, `400` |
|  Superuser |  `/v1/wallets/` | `GET`, `DELETE` |  `json` |  `200`, `204` |

##CREATE
** Permission required **: User

#### Headers
|  Field | Content  |
|---|---|
|  Content-Type | application/json  |
|  Authorization | JWT `{token}` |

#### Request Content

 - No content

#### Response Content
|  Field | Type  |Detail   |
|---|---|---|
|  `id`|  Integer |  Wallet's id |
|  `credit_limit` | Decimal  |  Wallet's limit |
|  `credit_available`|  Decimal |  Current available credit |
|  `created_at`|  Timestamp |  Date and time fo the creation |

#### Example

**Event**: User `POST` to `/v1/wallets/`  
**Header Content**:
```
Content-Type: application/
Authorization: JWT {token}
```
**Body Content**: `None`

**HTTP Status Code**: `201`  
**Response Content**:
```
{
	"id": 1,
	"credit_limit": "0.00",
	"credit_available": "0.00",
	"created_at": "2018-10-14T11:17:26.702134"
}
```

#### Validations
**HTTP Status Code**: `400`  

| Content  | Detail  |
|---|---|
| `user`: Already has a wallet.  | Every user must have only one wallet |


##RETRIEVE
** Permission required **: User

#### Headers
|  Field | Content  |
|---|---|
|  Content-Type | application/json  |
|  Authorization | JWT `{token}` |

#### Request Content
 - Add the wallet id to the URL: `/v1/wallets/{wallet_id}/`

#### Response Content
|  Field | Type  |Detail   |
|---|---|---|
|  `id`|  Integer |  Wallet's id |
|  `credit_limit` | Decimal  |  Wallet's limit |
|  `credit_available`|  Decimal |  Current available credit |
|  `created_at`|  Timestamp |  Date and time fo the creation |

#### Example

**Event**: User `GET` to `/v1/wallets/1/`  
**Header Content**:
```
Content-Type: application/
Authorization: JWT {token}
```
**Body Content**: `None`

**HTTP Status Code**: `200`  
**Response Content**:
```
{
	"id": 1,
	"credit_limit": "0.00",
	"credit_available": "0.00",
	"created_at": "2018-10-14T11:18:26.702134
}
```

##LIST
** Permission required **: Superuser

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
| `user`  | Integer  |  No |  Filter by user id |
| `id` |  Integer | No  |  Filter by id |

#### Response Content
|  Field | Type  |Detail   |
|---|---|---|
|  `id`|  Integer |  Wallet's id |
|  `credit_limit` | Decimal  |  Wallet's limit |
|  `credit_available`|  Decimal |  Current available credit |
|  `created_at`|  Timestamp |  Date and time fo the creation |

#### Example

**Event**: User `GET` to `/v1/wallets/`  
**Header Content**:
```
Content-Type: application/
Authorization: JWT {token}
```
**Body Content**: `None`

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
			"credit_limit": "0.00",
			"credit_available": "0.00",
			"created_at": "2018-10-15T17:10:29.481854",
			"user": 9
		},
		{
			"id": 2,
			"credit_limit": "0.00",
			"credit_available": "0.00",
			"created_at": "2018-10-15T17:44:03.746431",
			"user": 10
		}
	]
}
```

##DELETE
** Permission required **: Superuser

#### Headers
|  Field | Content  |
|---|---|
|  Content-Type | application/json  |
|  Authorization | JWT `{token}` |

#### Request Content
- Add the wallet id to the URL: `/v1/wallets/{wallet_id}/`

#### Example

**Event**: User `DELETE` to `/v1/wallets/1/`  
**Header Content**:
```
Content-Type: application/
Authorization: JWT {token}
```
**Body Content**: `None`

**HTTP Status Code**: `204`  
**Response Content**: `None`

