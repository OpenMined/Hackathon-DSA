
Refresh Tokens with OAuth 2.0 - LinkedIn | Microsoft Learn

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

Refresh Tokens with OAuth 2.0
=============================

* Article
* 05/08/2023
* 6 contributors

Feedback

In this article
---------------

LinkedIn supports programmatic refresh tokens for all approved Marketing Developer Platform (MDP) partners.

Introduction
------------

Refresh tokens are used to get a new access token when your current access token expires. For more information, see the OAuth 2.0 RFC.

LinkedIn offers programmatic refresh tokens that are valid for a fixed length of time. By default, access tokens are valid for 60 days and programmatic refresh tokens are valid for a year. The member must reauthorize your application when refresh tokens expire.

When you use a refresh token to generate a new access token, the lifespan or Time To Live (TTL) of the refresh token remains the same as specified in the initial OAuth flow (365 days), and the new access token has a new TTL of 60 days.

For example, on:

* Day 1 - Your refresh token has a TTL of 365 days, and your access token has a TTL of 60 days.
* Day 59 - If you generate a new access token using the refresh token, the access token will have a TTL of 60 days and the refresh token will have a TTL of 306 days (365-59=306).
* Day 360- If you generate a new access token, your access token and refresh token will both expire in 5 days (365-360=5) and you must get your application reauthorized by the member using the authorization flow.

Note

Refresh Tokens are useful in minting new Access tokens and allow for seamless operations for extended periods of time. However, LinkedIn reserves the right to revoke Refresh Tokens or Access Tokens at any time due to technical or policy reasons. In such scenarios, the expectation from products leveraging Refresh Tokens is to fallback to the standard OAuth flow, and present the login screen to the end users.

### Step 1: Getting a Refresh Token

Use the Authorization Code Flow to get both a refresh token and access token. If your application is authorized for programmatic refresh tokens, the following fields are returned when you exchange the authorization code for an access token:

* `refresh_token` — Your refresh token for the application. This token must be kept secure.
* `refresh_token_expires_in` — The number of seconds remaining until the refresh token expires. Refresh tokens usually have a longer lifespan than access tokens.
* `scope` — URL-encoded, space-delimited list of member permissions your application has requested on behalf of the user.|

#### Sample Response

```
{
  "access_token": "AQXNnd2kXITHELmWblJigbHEuoFdfRhOwGA0QNnumBI8XOVSs0HtOHEU-wvaKrkMLfxxaB1O4poRg2svCWWgwhebQhqrETYlLikJJMgRAvH1ostjXd3DP3BtwzCGeTQ7K9vvAqfQK5iG_eyS-q-y8WNt2SnZKZumGaeUw_zKqtgCQavfEVCddKHcHLaLPGVUvjCH_KW0DJIdUMXd90kWqwuw3UKH27ki5raFDPuMyQXLYxkqq4mYU-IUuZRwq1pcrYp1Vv-ltbA_svUxGt_xeWeSxKkmgivY_DlT3jQylL44q36ybGBSbaFn-UU7zzio4EmOzdmm2tlGwG7dDeivdPDsGbj5ig",
  "expires_in": 86400,
  "refresh_token": "AQWAft_WjYZKwuWXLC5hQlghgTam-tuT8CvFej9-XxGyqeER_7jTr8HmjiGjqil13i7gMFjyDxh1g7C_G1gyTZmfcD0Bo2oEHofNAkr_76mSk84sppsGbygwW-5oLsb_OH_EXADPIFo0kppznrK55VMIBv_d7SINunt-7DtXCRAv0YnET5KroQOlmAhc1_HwW68EZniFw1YnB2dgDSxCkXnrfHYq7h63w0hjFXmgrdxeeAuOHBHnFFYHOWWjI8sLLenPy_EBrgYIitXsAkLUGvZXlCjAWl-W459feNjHZ0SIsyTVwzAQtl5lmw1ht08z5Du-RiQahQE0sv89eimHVg9VSNOaTvw",
  "refresh_token_expires_in": 525600,
  "scope":"r_basicprofile"
}
```

Note

Refresh tokens are approximately 500 characters long. We recommend that your application stack be made to handle tokens of at least 1000 characters to accommodate future expansion plans. This applies to access tokens as well as refresh tokens.

### Step 2: Exchanging a Refresh Token for a New Access Token

You can exchange the refresh token for a new access token by making the following HTTP POST request with a `Content-Type` header of `x-www-form-urlencoded` and the following parameters in the request body:

```
https://www.linkedin.com/oauth/v2/accessToken
```

| Parameter | Description | Required |
| --- | --- | --- |
| grant\_type | The value of this field should always be refresh\_token. | Yes |
| refresh\_token | The refresh token from Step 1. | Yes |
| client\_id | The Client ID value generated when you registered your application. | Yes |
| client\_secret | The Client Secret value generated when you registered your application. | Yes |

#### Sample Request

```
POST https://www.linkedin.com/oauth/v2/accessToken
Content-Type: application/x-www-form-urlencoded
grant_type=refresh_token&refresh_token=AQQOMeCIQMa6-zjU-02w8EJW67wPVk3hjJE5x1lZhU013LihKD8i1DpvaAl2jnuP8F1uXMgkm8nzjPfnaJR_kQNOxsLRLZWnAMzHMm81S0yQlkBYicw&client_id=861hhm46p48to2&client_secret=gPecS7yqHkyyShvR
```
A successful request returns a new access token with a new expiration time and the refresh token.

```
{
  "access_token": "BBBB2kXITHELmWblJigbHEuoFdfRhOwGA0QNnumBI8XOVSs0HtOHEU-wvaKrkMLfxxaB1O4poRg2svCWWgwhebQhqrETYlLikJJMgRAvH1ostjXd3DP3BtwzCGeTQ7K9vvAqfQK5iG_eyS-q-y8WNt2SnZKZumGaeUw_zKqtgCQavfEVCddKHcHLaLPGVUvjCH_KW0DJIdUMXd90kWqwuw3UKH27ki5raFDPuMyQXLYxkqq4mYU-IUuZRwq1pcrYp1Vv-ltbA_svUxGt_xeWeSxKkmgivY_DlT3jQylL44q36ybGBSbaFn-UU7zzio4EmOzdmm2tlGwG7dDeivdPDsGbj5ig",
  "expires_in": 86400,
  "refresh_token": "AQWAft_WjYZKwuWXLC5hQlghgTam-tuT8CvFej9-XxGyqeER_7jTr8HmjiGjqil13i7gMFjyDxh1g7C_G1gyTZmfcD0Bo2oEHofNAkr_76mSk84sppsGbygwW-5oLsb_OH_EXADPIFo0kppznrK55VMIBv_d7SINunt-7DtXCRAv0YnET5KroQOlmAhc1_HwW68EZniFw1YnB2dgDSxCkXnrfHYq7h63w0hjFXmgrdxeeAuOHBHnFFYHOWWjI8sLenPy_EBrgYIitXsAkLUGvZXlCjAWl-W459feNjHZ0SIsyTVwzAQtl5lmw1ht08z5Du-RiQahQE0sv89eimHVg9VSNOaTvw",
  "refresh_token_expires_in": 439200,
  "scope":"r_basicprofile"
}
```
#### API Error Details

| HTTP STATUS CODE | ERROR MESSAGE | ERROR DESCRIPTION | RESOLUTION |
| --- | --- | --- | --- |
| 400 | invalid\_request "The provided authorization grant or refresh token is invalid, expired or revoked" | Invalid or expired or revoked refresh token is sent as part of the request. | Refresh Token expired or revoked or invalid, hence reauthenticate the member to generate the new refresh token. |
| 400 | invalid\_request "A required parameter "redirect\_uri" is missing" | Redirect\_URI in the request is missing. It is mandatory parameter. | Pass the Redirect\_URI in the request to route user back to correct landing page. |
| 400 | invalid\_request "A required parameter "grant\_type" is missing" | Grant type in the request is missing. It is mandatory parameter. | Add grant\_type as "refresh\_token" in the request. |
| 400 | invalid\_request "A required parameter "client\_id" is missing" | Client ID in the request is missing. It is mandatory parameter. | Pass the client id of the app in request. |
| 400 | invalid\_request "A required parameter "refresh\_token" is missing" | Refresh Token in the request is missing. It is mandatory parameter. | Pass the stored Refresh Token received as part of initial access token call. |

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