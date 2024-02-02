
LinkedIn 2-Legged OAuth Flow - LinkedIn | Microsoft Learn

Skip to main content

This browser is no longer supported.

Upgrade to Microsoft Edge to take advantage of the latest features, security updates, and technical support.

Download Microsoft Edge
More info about Internet Explorer and Microsoft Edge

Table of contents 

Exit focus mode

Read in English

Save

Table of contents
Read in English

Save
Edit

Print

Twitter
LinkedIn
Facebook
Email

Table of contents

Client Credential Flow (2-legged OAuth)
=======================================

* Article
* 05/08/2023
* 8 contributors

Feedback

In this article
---------------

If your application needs to access APIs that are not member specific, use the Client Credential Flow. Your application **cannot** access these APIs by default.

Learn more:

* LinkedIn Developer Enterprise products and permission requests.
* LinkedIn Developers Platform knowledge base.

Important

2-legged OAuth authentication is not available for Marketing APIs

Note

**Generate a Token Manually Using the Developer Portal** 
The LinkedIn Developer Portal has a token generator for manually creating tokens. Visit the LinkedIn Developer Portal Token Generator or follow the steps outlined in Developer Portal Tools.

Step 1: Get Client ID and Client Secret
---------------------------------------

* Getting started? Create a new application on the Developer Portal.
* Existing application? Go to My apps to modify your app settings.

Each application is assigned a unique *Client ID* (Consumer key/API key) and *Client Secret*. Please make a note of these values as they will be integrated into your application config files. Your *Client Secret* protects your application's security so be sure to keep it secure!

Warning

Do not share your *Client Secret* value with anyone, and **do not** pass it in the URL when making API calls, or URI query-string parameters, or post in support forums, chat, etc.

Step 2: Generate an Access Token
--------------------------------

To generate an access token, issue a HTTP POST against `accessToken` with a `Content-Type` header of `x-www-form-urlencoded` and the following parameters in the request body:

```
https://www.linkedin.com/oauth/v2/accessToken
```

| Parameter | Description | Required |
| --- | --- | --- |
| grant\_type | The value of this field should always be `client_credentials` | Yes |
| client\_id | The *Client ID* value generated when you registered your application | Yes |
| client\_secret | The *Client Secret* value generated when you registered your application | Yes |

* View the Best Practices for Secure Applications page for more security info.

### Sample Request (Secure Approach)

```
POST https://www.linkedin.com/oauth/v2/accessToken HTTP/1.1
Content-Type: application/x-www-form-urlencoded
grant_type=client_credentials
client_id={your_client_id}
client_secret={your_client_secret}
```
A successful access token request returns a JSON object containing the following fields:

* `access_token` — The access token for the application. This token must be kept secure.
* `expires_in` — Seconds until token expiration.
	+ The access token has a 30-minute lifespan and must be used immediately. You may request a new token once your current token expires.

### Sample Response

```
{
    "access_token": "AQV8...",
    "expires_in": "1800"
}
```
For error details, refer the API Error Details section.

Step 3: Make API Requests
-------------------------

Once you've received an access token, you can make API requests by including an *Authorization* header with your token in the HTTP call to LinkedIn's API.

### Sample Request

```
GET https://api.linkedin.com/v2/jobs HTTP/1.1
Connection: Keep-Alive
Authorization: Bearer {access_token}
```
API Error Details
-----------------

| HTTP STATUS CODE | ERROR MESSAGE | DESCRIPTION | RESOLUTION |
| --- | --- | --- | --- |
| 401 | invalid\_client\_id "Client authentication failed" | Client Authentication failed due to bad client credentials passed as part of the request. | Check whether the right **Client ID**, **Client Secret** are passed as part of the request. |
| 401 | access\_denied "This application is not allowed to create application tokens" | The developer application doesn’t have enough permission to generate 2L application token. | Reach out to the LinkedIn Relationship Manager or Business Development team to get the necessary access. |
| 400 | invalid\_request "A required parameter "grant\_type" is missing" | Grant type in the request is missing. It is a mandatory parameter. | Add grant\_type as `client_credentials` in the request. |
| 400 | invalid\_request "A required parameter "client\_id" is missing" | Client ID in the request is missing. It is a mandatory parameter. | Pass the Client ID of the developer application in request. |
| 400 | invalid\_request "A required parameter "client\_secret" is missing" | Client Secret in the request is missing. It is a mandatory parameter. | Pass the Client Secret of the developer application in the request. |
| 400 | invalid\_client\_id "The passed in client\_id is invalid "abcdefghijk"" | Invalid client ID is passed in the request. | Pass the right client ID from the developer application. |

---

Feedback
--------

Was this page helpful?

Yes

No

Provide product feedback

Feedback
--------

Submit and view feedback for

This product
This page

View all page feedback

---

Additional resources
--------------------

California Consumer Privacy Act (CCPA) Opt-Out Icon

Your Privacy Choices

Theme

* Light
* Dark
* High contrast

* 
* Previous Versions
* Blog
* Contribute
* Privacy
* Terms of Use
* Trademarks
* © Microsoft 2024

Additional resources
--------------------

### In this article

California Consumer Privacy Act (CCPA) Opt-Out Icon

Your Privacy Choices

Theme

* Light
* Dark
* High contrast

* 
* Previous Versions
* Blog
* Contribute
* Privacy
* Terms of Use
* Trademarks
* © Microsoft 2024