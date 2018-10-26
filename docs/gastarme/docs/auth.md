## Authentication - `/v1/auth/jwt/`


| Permission level  |   URL| Method  | Format   |  HTTP Status Code |
|---|---|---|---|---|
|  Anonymous |  `/v1/auth/jwt/`|   `POST`|  `json` |  `200`, `400` |


### OBTAIN
** Permission required **: None

#### Headers
|  Field | Content  |
|---|---|
|  Content-Type | application/json  |

#### Request Content

|  Field |  Type |  Required |  Detail |
|---|---|---|---|
| `email`  | Email field  | Yes  |  User's email |
| `password`  |  String | Yes  |  User's password |


#### Response Content
|  Field | Type  |Detail   |
|---|---|---|
|  `type` | String  |  `JWT` |
|  `token`|  String | Token |
|  `expires_in`|  Integer | Seconds remaining for the token to expire |

#### Example

**Event**: Anonymous `POST` to `/v1/auth/jwt/obtain/`  
**Header Content**:
```
Content-Type: application/json
```
**Body Content**: 
```
{
	"email": "jonhdoeqa@email.com",
	"password": "1234ABCD"
}

```
**HTTP Status Code**: `200`  
**Response Content**:
```
{
	"type": "JWT",
	"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImpvaG4uZG9lQGVtYWlsLmNvbSIsImV4cCI6MTUzOTc0MTI5NiwiZW1haWwiOiJqb2huLmRvZUBlbWFpbC5jb20iLCJvcmlnX2lhdCI6MTUzOTczNzY5Nn0.cq9TRU0lPKY1-A_miNEqtOE6Kgi9Fx0Av1JlNu1Nq84",
	"expires_in": 3600
}
```

#### Validations
**HTTP Status Code**: `400`  

| Field  | Content  |  Detail |
|---|---|---|
| `email`  |  This field is required. | The payload must contain an email |
| `password`| This field is required. | The payload must contain a password  |

### REFRESH
** Permission required **: None

#### Headers
|  Field | Content  |
|---|---|
|  Content-Type | application/json  |

#### Request Content

|  Field |  Type |  Required |  Detail |
|---|---|---|---|
| `token`  | String | Yes  |  User's token  |


#### Response Content
|  Field | Type  |Detail   |
|---|---|---|
|  `type` | String  |  `JWT` |
|  `token`|  String | Token |
|  `expires_in`|  Integer | Seconds remaining for the token to expire |

#### Example

**Event**: Anonymous `POST` to `/v1/auth/jwt/refresh/`  
**Header Content**:
```
Content-Type: application/json
```
**Body Content**: 
```
{
	"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImpvaG4uZG9lQGVtYWlsLmNvbSIsImV4cCI6MTUzOTc0MTI5NiwiZW1haWwiOiJqb2huLmRvZUBlbWFpbC5jb20iLCJvcmlnX2lhdCI6MTUzOTczNzY5Nn0.cq9TRU0lPKY1-A_miNEqtOE6Kgi9Fx0Av1JlNu1Nq84"
}

```
**HTTP Status Code**: `200`  
**Response Content**:
```
{
	"type": "JWT",
	"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImpvaG4uZG9lQGVtYWlsLmNvbSIsImV4cCI6MTUzOTc0MTI5NiwiZW1haWwiOiJqb2huLmRvZUBlbWFpbC5jb20iLCJvcmlnX2lhdCI6MTUzOTczNzY5Nn0.cq9TRU0lPKY1-A_miNEqtOE6Kgi9Fx0Av1JlNu1Nq84",
	"expires_in": 3600
}
```

#### Validations
**HTTP Status Code**: `400`  

| Field  | Content  |  Detail |
|---|---|---|
| `non_field_errors`  |  Error decoding signature. |  The token is invalid |
| `non_field_errors`|  Signature has expired. | The token has expired  |