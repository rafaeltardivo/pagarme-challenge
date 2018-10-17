## Users - `/v1/users/`


| Permission level  |   URL| Method  | Format   |  HTTP Status Code |
|---|---|---|---|---|
|  Anonymous |  `/v1/users/` |   `POST`|  `json` |  `201`, `400` |


### CREATE
** Permission required **: None
#### Request Content

|  Field | Type  | Required  |  Min Length |  Max Length |  Detail |
|---|---|---|---|---|---|
|  `name` |  String |  Yes |  8 |  100 |  User's name |
| `email` |  Email Field |  Yes | 8  | 100  | User's email  |
| `password` |  String |  Yes | 8  | 128  | User's password  |

#### Response Content
|  Field | Type  |Detail   |
|---|---|---|
|  `name` | String  |  User's name |
|  `email`|  Email Field |  User's email |

#### Example

**Event**: Anonymous `POST` to `/v1/users/`  
**Request Content**: 
```
{
	"name": "John Doe",
	"email": "jonhdoeqa@email.com",
	"password": "1234ABCD"
}

```
**HTTP Status Code**: `201`  
**Response Content**:
```
{
	"name": "John Doe",
	"email": "jonhdoeqa@email.com"
}
```

#### Validations
**HTTP Status Code**: `400`  

| Content  | Detail  |
|---|---|
| `email`: User with this email already exists.  | Email is unique |
| `email`: This field is required. |  The payload must contain an email |
| `email`: Enter a valid email address.. |  The payload must contain a valid email address|
| `email`: Ensure this field has no more than 100 characters. |  The email must contain maximum 100 characters |
| `name`: This field is required. |  The payload must contain a name |
| `name`: Must contain at least 8 characters. |  The name must contain at least 8 characters |
| `name`: Ensure this field has no more than 100 characters. |  The name must contain maximum 100 characters |
| `password`: This field is required. |  The payload must contain a password |
| `password`: This password is too common. |  The password must be more complex |
| `password`: This password is too short. It must contain at least 8 characters.|  The password must contain at least 8 characters |
| `password`: This password is entirely numeric.|  The password must contain letters and numbers. |
| `password`: Ensure this field has no more than 128 characters. |  The email must contain maximum 128 characters |
