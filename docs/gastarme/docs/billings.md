## Billings - `/v1/billings/`


| Permission level  |   URL| Method  | Format   |  HTTP Status Code |
|---|---|---|---|---|
|  User |  `/v1/billings/` |   `GET`  |  `json` |  `200`|
|  User |  `/v1/billings/{id}/pay/` |  `PATCH` |  `json` |  `200`|


##PATCH
** Permission required **: User

- Add the bill id to the URL and **pay** to the resource as an action route: `/v1/billings/{1}/pay/`

#### Headers
|  Field | Content  |
|---|---|
|  Content-Type | application/json  |
|  Authorization | JWT `{token}` |

#### Request Content

|  Field | Type  | Required  |  Min Length |  Max Length |  Detail |
|---|---|---|---|---|---|
| `value` |  Decimal |  Yes | 3  | 12  | Value to be paid |


#### Response Content
|  Field | Type  |Detail   |
|---|---|---|
|  `id`|  Integer |  Bill id|
|  `expires_at`|  Timestamp |  Expiration date of the bill |
|  `value` | Decimal  |  Bill value that remains after the payment |
|  `credit_card` | Integer  |  Related credit card id |

#### Example

**Event**: User `PATCH` to `/v1/billings/1/pay/`  
**Header Content**:
```
Content-Type: application/
Authorization: JWT {token}
```
**Body Content**: 
```
{
	"value": "150.00"	
}
```

**HTTP Status Code**: `200`  
**Response Content**:
```
{
	"id": 1,
	"expires_at": "2018-11-20",
	"value": "450.00",
	"credit_card": 1
}
```


##RETRIEVE
** Permission required **: User

#### Headers
|  Field | Content  |
|---|---|
|  Content-Type | application/json  |
|  Authorization | JWT `{token}` |

#### Request Content

- Add the bill id to the URL: `/v1/billings/{1}/`


#### Response Content
|  Field | Type  |Detail   |
|---|---|---|
|  `id`|  Integer |  Bill id|
|  `expires_at`|  Timestamp |  Expiration date of the bill |
|  `value` | Decimal  |  Bill value |
|  `credit_card` | Integer  |  Related credit card id |


#### Example

**Event**: User `GET` to `/v1/billings/1/`  
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
	"expires_at": "2018-11-20",
	"value": "475.00",
	"credit_card": 1
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
| `expires_at__gte`  | Date  |  No |  Filter by minimum date of expiration (greater than or equal)|
| `expires_at__lte`  | Date  |  No |  Filter by maximum date of expiration (lesser than or equal)|

#### Response Content
|  Field | Type  |Detail   |
|---|---|---|
|  `id`|  Integer |  Bill id|
|  `expires_at`|  Timestamp |  Expiration date of the bill |
|  `value` | Decimal  |  Bill value |
|  `credit_card` | Integer  |  Related credit card id |

#### Example

**Event**: User `GET` to `/v1/billings/`  
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
			"expires_at": "2018-11-20",
			"value": "475.00",
			"credit_card": 1
		},
		{
			"id": 2,
			"expires_at": "2018-11-19",
			"value": "50.00",
			"credit_card": 2
		}
	]
}
```