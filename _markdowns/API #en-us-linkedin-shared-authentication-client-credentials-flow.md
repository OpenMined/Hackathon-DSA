::: content
::: {.display-flex .justify-content-space-between .align-items-center .flex-wrap-wrap .page-metadata-container}
:::

If your application needs to access APIs that are not member specific,
use the Client Credential Flow. Your application **cannot** access these
APIs by default.

Learn more:

::: IMPORTANT
Important

2-legged OAuth authentication is not available for [Marketing
APIs](../../marketing/getting-started)
:::

## Step 1: Get Client ID and Client Secret

Each application is assigned a unique *Client ID* (Consumer key/API key)
and *Client Secret* . Please make a note of these values as they will be
integrated into your application config files. Your *Client Secret*
protects your application\'s security so be sure to keep it secure!

![Redirect URLS](../../media/oauth_values.png)

::: WARNING
Warning

Do not share your *Client Secret* value with anyone, and **do not** pass
it in the URL when making API calls, or URI query-string parameters, or
post in support forums, chat, etc.
:::

## Step 2: Generate an Access Token

To generate an access token, issue a HTTP POST against ` accessToken `
with a ` Content-Type ` header of ` x-www-form-urlencoded ` and the
following parameters in the request body:

``` lang-https
https://www.linkedin.com/oauth/v2/accessToken
```

  Parameter       Description                                                                Required
  --------------- -------------------------------------------------------------------------- ----------
  grant_type      The value of this field should always be ` client_credentials `            Yes
  client_id       The *Client ID* value generated when you registered your application       Yes
  client_secret   The *Client Secret* value generated when you registered your application   Yes

### Sample Request (Secure Approach)

``` lang-https
POST https://www.linkedin.com/oauth/v2/accessToken HTTP/1.1

Content-Type: application/x-www-form-urlencoded
grant_type=client_credentials
client_id={your_client_id}
client_secret={your_client_secret}
```

A successful access token request returns a [JSON](http://www.json.org/)
object containing the following fields:

-   ` access_token ` --- The access token for the application. This
    token must be kept secure.
-   ` expires_in ` --- Seconds until token expiration.
    -   The access token has a 30-minute lifespan and must be used
        immediately. You may request a new token once your current token
        expires.

### Sample Response

``` lang-json
{
    "access_token": "AQV8...",
    "expires_in": "1800"
}
```

For error details, refer the [API Error Details](#api-error-details)
section.

## Step 3: Make API Requests

Once you\'ve received an access token, you can make API requests by
including an *Authorization* header with your token in the HTTP call to
LinkedIn\'s API.

### Sample Request

``` lang-https
GET https://api.linkedin.com/v2/jobs HTTP/1.1

Connection: Keep-Alive
Authorization: Bearer {access_token}
```

## API Error Details

  HTTP STATUS CODE   ERROR MESSAGE                                                                    DESCRIPTION                                                                                  RESOLUTION
  ------------------ -------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------
  401                invalid_client_id \"Client authentication failed\"                               Client Authentication failed due to bad client credentials passed as part of the request.    Check whether the right **Client ID** , **Client Secret** are passed as part of the request.
  401                access_denied \"This application is not allowed to create application tokens\"   The developer application doesn't have enough permission to generate 2L application token.   Reach out to the LinkedIn Relationship Manager or Business Development team to get the necessary access.
  400                invalid_request \"A required parameter \"grant_type\" is missing\"               Grant type in the request is missing. It is a mandatory parameter.                           Add grant_type as ` client_credentials ` in the request.
  400                invalid_request \"A required parameter \"client_id\" is missing\"                Client ID in the request is missing. It is a mandatory parameter.                            Pass the Client ID of the developer application in request.
  400                invalid_request \"A required parameter \"client_secret\" is missing\"            Client Secret in the request is missing. It is a mandatory parameter.                        Pass the Client Secret of the developer application in the request.
  400                invalid_client_id \"The passed in client_id is invalid \"abcdefghijk\"\"         Invalid client ID is passed in the request.                                                  Pass the right client ID from the developer application.
:::
