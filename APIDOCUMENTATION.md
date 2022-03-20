# Users API documentation

This documentation contains the detailed documentation for Users API.

#### Contents

- [Overview](#1-overview)
- [Authentication](#2-authentication)
 - [Resources](#3-Resources)
  - [Users](#31-Users)
  - [Subsetting](#3.2-Subsetting)
  - [Register](#3.3-Register)
- [Testing](#4-testing)
- [Team](#5-team)

## 1. Overview

Users’s API is a JSON-based OAuth2 API. All requests are made to endpoints beginning:
`Resources/`

All requests are secure, i.e. `https`.

#### Developer agreement

Using Users’s API, you agree to our [terms of service](https://myusersapikata.herokuapp.com/).

## 2. Authentication

For you to consume or use the API,you must sign up and log in to acquire browser-based OAuth authentication access token. 

We recommend using self-issued access tokens. Browser-based authentication is supported **for existing integrations only**.

## 3. Resources

The API is RESTful and arranged around resources. All requests must be made with a token. All requests must be made using `https`.

Typically, the first request you make should be to acquire user details. This will confirm that your access token is valid, and give you a user id that you will need for subsequent requests.

### 3.1. Users

#### Getting the registered users' details
Returns details of the users who has permission to use the API. It returns 100 users at a time or per page by default. The maximum number of users per page is 100. The maximum number of pages is 100. The default number of users per page is 100. 

```
GET https://myusersapikata.herokuapp.com/users/
```

Example request:

```
GET /users/ HTTP/1.1
Host: https://myusersapikata.herokuapp.com
Authorization: Bearer 181d415f34379af07b2c11d144dfbe35d
Content-Type: application/json
Accept: application/json
Accept-Charset: utf-8
```

The response is a User object within a data envelope.

Example response:

```
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

{
"count": 100,
"message": "SUCCESS",
"status_code": 200,
"users": [
{
"email": "okothhassanjumca@gmail.com",
"name": "HASSAN JUMAs",
"user_id": 1
},
{
"email": "okothhassanjuma@gmail.com",
"name": "hassamn juma",
"user_id": 2
},
{
"email": "zbene2@desdev.cn",
"name": "Zebulon Bene",
"user_id": 3
},
{
"email": "ntite3@topsy.com",
"name": "Nichols Tite",
"user_id": 4
},
{
"email": "mballendine4@arstechnica.com",
"name": "Marcella Ballendine",
"user_id": 5
}
]
}
```

Where a User object is:

| Field      | Type   | Description                                     |
| -----------|--------|-------------------------------------------------|
| user_id    | string | A unique identifier for the user.               |
| name       | string | The user’s username on Users API.                  |
| email      | string | The user’s email on Users API.                      |


Possible errors:

| Error code           | Description                                     |
| ---------------------|-------------------------------------------------|
| 401 Unauthorized     | The `accessToken` is invalid or has been revoked. |
| 404 Not Found        | The `user_id` is invalid.                        |
| 500 Internal Server  | An error occurred while processing the request.  |


#### Getting the registered users' details by specifying the number of users to be returned per page  and the page number.
Returns details of users who has granted permission to use the API where n is the number of users to be returned per page.  The maximum number of users per page is 100. The default number of users per page is 100.

```
GET https://myusersapikata.herokuapp.com/users/<n>
```

Example request:

```
GET /users/ HTTP/1.1
Host: https://myusersapikata.herokuapp.com
Authorization: Bearer 181d415f34379af07b2c11d144dfbe35d
Content-Type: application/json
Accept: application/json
Accept-Charset: utf-8
```

The response is a User object within a data envelope.

Example response:

```
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

{
"count": 5,
"message": "SUCCESS",
"status_code": 200,
"users": [
{
"email": "okothhassanjumca@gmail.com",
"name": "HASSAN JUMAs",
"user_id": 1
},
{
"email": "okothhassanjuma@gmail.com",
"name": "hassamn juma",
"user_id": 2
},
{
"email": "zbene2@desdev.cn",
"name": "Zebulon Bene",
"user_id": 3
},
{
"email": "ntite3@topsy.com",
"name": "Nichols Tite",
"user_id": 4
},
{
"email": "mballendine4@arstechnica.com",
"name": "Marcella Ballendine",
"user_id": 5
}
]
}
```

Where a User object is:

| Field      | Type   | Description                                     |
| -----------|--------|-------------------------------------------------|
| user_id         | string | A unique identifier for the user.               |
| name       | string | The user’s username on Users API.                  |
| email      | string | The user’s email on Users API.                      |


Possible errors:

| Error code           | Description                                     |
| ---------------------|-------------------------------------------------|
| 401 Unauthorized     | The `accessToken` is invalid or has been revoked. |
| 404 Not Found        | The `user_id` is invalid.                        |
| 500 Internal Server  | An error occurred while processing the request.  |


#### Getting the registered users' details by specyfing the user name
Returns details of the users bearing the given name who has granted permission to use the API.If users share the same name, they will be returned and if the user name is not found, an empty array will be returned.

```
GET https://myusersapikata.herokuapp.com/users/<name>
```

Example request:

```
GET /users/ HTTP/1.1
Host: https://myusersapikata.herokuapp.com
Authorization: Bearer 181d415f34379af07b2c11d144dfbe35d
Content-Type: application/json
Accept: application/json
Accept-Charset: utf-8
```

The response is a User object within a data envelope.

Example response:

```
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

{
"count": 1,
"message": "SUCCESS",
"status_code": 200,
"users": [
{
"email": "okothhassanjuma@gmail.com",
"name": "hassamn juma",
"user_id": 2
}
]
}
```

Where a User object is:

| Field      | Type   | Description                                     |
| -----------|--------|-------------------------------------------------|
| user_id    | string | A unique identifier for the user.               |
| name       | string | The user’s username on Users API.                  |
| email      | string | The user’s email on Users API.                      |


Possible errors:

| Error code           | Description                                     |
| ---------------------|-------------------------------------------------|
| 401 Unauthorized     | The `accessToken` is invalid or has been revoked. |
| 404 Not Found        | The `user_id` is invalid.                        |
| 500 Internal Server  | An error occurred while processing the request.  |


#### Getting the registered users' details by specyfing the value of the user id or email
Returns details of the users who has permission to use the API. IT returns a single user whose id or email matches the given value. Users can not share the same id or email, so they will  return a single user.if the user id or email is not found, an empty array will be returned.

```

GET https://myusersapikata.herokuapp.com/user/<val>
```

Example request:

```
GET /user/ HTTP/1.1
Host: https://myusersapikata.herokuapp.com
Authorization: Bearer 181d415f34379af07b2c11d144dfbe35d
Content-Type: application/json
Accept: application/json
Accept-Charset: utf-8
```

The response is a User object within a data envelope.

Example response:

```

HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
{
"count": 1,
"message": "SUCCESS",
"status_code": 200,
"users": [
{
"email": "okothhassanjuma@gmail.com",
"name": "hassamn juma",
"user_id": 2
}
]
}
```

Where a User object is:

| Field      | Type   | Description                                     |
| -----------|--------|-------------------------------------------------|
| user_id    | string | A unique identifier for the user.               |
| name       | string | The user’s username on Users API.                  |
| email      | string | The user’s email on Users API.                      |


Possible errors:

| Error code           | Description                                     |
| ---------------------|-------------------------------------------------|
| 401 Unauthorized     | The `accessToken` is invalid or has been revoked. |
| 404 Not Found        | The `user_id` is invalid.                        |
| 500 Internal Server  | An error occurred while processing the request.  |




### 3.2. Subsetting


#### Subsetting users by per page

This endpoint returns a list of users by a given subset. The API endpoint exposes the users details. An example request looks like this:

```
GET https://myusersapikata.herokuapp.com/users/range/
```

In the response,  it returns  a list of users 100 per page. An empty array is returned if there are no users in the database. The response array is wrapped in a data envelope. This endpoint will return all details of the user, including the list of id, name and email.
```
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

{
"count": 100,
"message": "SUCCESS",
"status_code": 200,
"users": [
{
"email": "okothhassanjumca@gmail.com",
"name": "HASSAN JUMAs",
"user_id": 1
},
{
"email": "okothhassanjuma@gmail.com",
"name": "hassamn juma",
"user_id": 2
},
{
"email": "zbene2@desdev.cn",
"name": "Zebulon Bene",
"user_id": 3
},
{
"email": "ntite3@topsy.com",
"name": "Nichols Tite",
"user_id": 4
},
{
"email": "mballendine4@arstechnica.com",
"name": "Marcella Ballendine",
"user_id": 5
}, ............................
]
}
```
  
Where a User object is:

| Field      | Type   | Description                                     |
| -----------|--------|-------------------------------------------------|
| user_id         | string | A unique identifier for the user.               |
| name       | string | The user’s username on Users API.                  |
| email      | string | The user’s email on Users API.                      |


Possible errors:

| Error code           | Description                                                                           |
| ---------------------|---------------------------------------------------------------------------------------|
| 401 Unauthorized     | The `accessToken` is invalid, or has been revoked.                                    |
| 404 Not Found        | The `user_id` is invalid.                                                              |
| 500 Internal Server  | An error occurred while processing the request.                                         |


#### Subsetting users by id and a given count

This endpoint returns a list of contributors for a given publication. In other words, a list of  users who are registered. The API endpoint exposes the users details. An example request looks like this:

```
GET https://myusersapikata.herokuapp.com/users/range/<start>/<end>/
```

In the response,  it returns  a list of users from the start of the given index upto the the count of the given end. An empty array is returned if there are no users in the database. The response array is wrapped in a data envelope. This endpoint will return all details of the user, including the list of id, name and email.
```
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

{
"count": 8,
"message": "SUCCESS",
"status_code": 200,
"users": [
{
"email": "ntite3@topsy.com",
"name": "Nichols Tite",
"user_id": 4
},
{},
{},
{},
{},
{},
{},
{
"email": "cpagdena@deliciousdays.com",
"name": "Courtney Pagden",
"user_id": 11
}
]
}
```

Where a User object is:

| Field      | Type   | Description                                     |
| -----------|--------|-------------------------------------------------|
| user_id         | string | A unique identifier for the user.               |
| name       | string | The user’s username on Users API.                  |
| email      | string | The user’s email on Users API.                      |


Possible errors:

| Error code           | Description                                                                           |
| ---------------------|---------------------------------------------------------------------------------------|
| 401 Unauthorized     | The `accessToken` is invalid, or has been revoked.                                    |
| 401 Unauthorized     | The `accessToken` is invalid, or has been revoked.                                    |
| 404 Not Found        | The `user_id` is invalid.                                                              |
| 500 Internal Server  | An error occurred while processing the request.                                         |

### 3.3. Register a new user

#### Creating a user
Creates a user  and post the details in to the database. The request body is a JSON object with the following fields:
```
POST https://myusersapikata.herokuapp.com/register/
```


Example request:

```
POST /regiter HTTP/1.1
Host: https://myusersapikata.herokuapp.com
Authorization: Bearer 181d415f34379af07b2c11d144dfbe35d
Content-Type: application/json
Accept: application/json
Accept-Charset: utf-8

{
  "users":  {
      "user_id ": "11",
      "name": "Juma Hassan",
      "email": "jumahassan@gmail.com",

    }

}
```

With the following fields:


| Field      | Type   | Description                                     |
| -----------|--------|-------------------------------------------------|
| user_id         | string | A unique identifier for the user.               |
| name       | string | The user’s username on Users API.                  |
| email      | string | The user’s email on Users API.                      |


The response is a Post object within a data envelope. Example response:

```
HTTP/1.1 201 OK
Content-Type: application/json; charset=utf-8

{
  "users":  {
      "user_id ": "11",
      "name": "Juma Hassan",
      "email": "jumahassan@gmail.com",

    }

}
```

Where a user object is:

| Field      | Type   | Description                                     |
| -----------|--------|-------------------------------------------------|
| user_id    | string | A unique identifier for the user.               |
| name       | string | The user’s username on Users API.                  |
| email      | string | The user’s email on Users API.                      |

Possible errors:

| Error code           | Description                                                                                                          |
| ---------------------|----------------------------------------------------------------------------------------------------------------------|
| 400 Bad Request      | Required fields were invalid, not specified.                                                                         |
| 401 Unauthorized     | The access token is invalid or has been revoked.                                                                     |
| 409 Conflict         | The user already exists.                                                                                            | 


## 4. Testing
I don't have a sandbox environment yet. To test, please feel free to create a testing account. 

These endpoints will perform actions on production data on `myusersapikata.herokuapp.com`. **Please test with care.**

## 5. Team

[Hassan Juma ](https://github.com/HASSAN1A)

## [License](https://github.com/HASSAN1A/my_users_api/blob/main/LICENSE.md)

[MIT](https://github.com/HASSAN1A/my_users_api/main/LICENSE.md) © [Hassan Juma](https://github.com/HASSAN1A)
