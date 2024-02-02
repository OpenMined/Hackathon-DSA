::: content
::: {.display-flex .justify-content-space-between .align-items-center .flex-wrap-wrap .page-metadata-container}
:::

The token inspector tool enables developers to check the Time to Live
(TTL) and status (active/expired) for all tokens (including Enterprise
tokens.) For [Authorization Code Flow](authorization-code-flow)
(3-legged OAuth) tokens, permission scopes will be displayed. You can
fetch access token data using the ` /introspectToken ` endpoint or the
[Token Inspector
Tool](https://www.linkedin.com/developers/tools/oauth/token-inspector)
in the UI.

### API Details

``` lang-https
POST https://www.linkedin.com/oauth/v2/introspectToken

Content-Type: application/x-www-form-urlencoded
```

#### Sample Request

::: {#tabpanel_1_http .section}
``` lang-http
POST https://www.linkedin.com/oauth/v2/introspectToken
```
:::

::: {#tabpanel_1_curl .section}
``` lang-curl
curl --location --request POST 'https://www.linkedin.com/oauth/v2/introspectToken' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'client_id=<Application Client ID>' \
--data-urlencode 'client_secret=<Application Client Secret>' \
--data-urlencode 'token=<Token Value>'
```
:::

  Field           Type     Description
  --------------- -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  client_id       string   Required. Application client id
  client_secret   string   Required. Application client secret
  token           string   Required. The string value of the token returned using [Client Credential Flow](client-credentials-flow) (2-legged OAuth), [Authorization Code Flow](authorization-code-flow) (3-legged OAuth), or ` Enterprise_User ` (Enterprise OAuth Flow).

``` lang-json
{
    "active": true,
    "client_id": "xxxxxxxx",
    "authorized_at": 1493055596,
    "created_at": 1493055596,
    "status": "active",
    "expires_at": 1497497620,
    "scope": "r_liteprofile,r_emailaddress,w_member_social",
    "auth_type": "_see note below_" 
}
```

::: NOTE
Note

Possible ` auth-type ` values returned are: \"auth_type\": \"2L\"
\"auth_type\": \"3L\"

\"auth_type\": \"Enterprise_User\"
:::

  --------------------------------------------------------------------------------
  Field                   Type                    Description
  ----------------------- ----------------------- --------------------------------
  active                  boolean                 Required. Boolean indicator of
                                                  whether or not the returned
                                                  token is currently active

  status                  string                  Optional. An enum string with
                                                  values:\
                                                  ` revoked ` - Token has been
                                                  revoked\
                                                  ` expired ` - Token has expired
                                                  due to the \"expires_at\" TTL\
                                                  ` active ` - Token is active

  scope                   string                  Optional. A string containing a
                                                  comma-separated list of scopes
                                                  associated with this token.\
                                                  Returned only for token obtained
                                                  via [Authorization Code
                                                  Flow](authorization-code-flow)
                                                  (3-legged OAuth)

  client_id               string                  Optional. Optional. Application
                                                  Client ID

  created_at              long                    Optional. Epoch time in seconds,
                                                  indicating when this token was
                                                  originally issued

  expires_at              long                    Optional. Epoch time in seconds,
                                                  indicating when this token will
                                                  expire

  authorized_at           long                    Optional. Epoch time in seconds,
                                                  indicating when the token was
                                                  authorized

  auth_type               string                  Optional. String with values:\
                                                  ` 3L ` - 3-legged member token\
                                                  ` 2L ` - 2-legged application
                                                  token\
                                                  ` Enterprise_User ` - Enterprise
                                                  member token
  --------------------------------------------------------------------------------

The response will vary depending on the status of the token and its
authenticity.

  Status Code   Description
  ------------- ------------------------------------
  200           Success
  400           Invalid ` client id ` or ` token `
  401           Invalid ` client secret `

::: NOTE
Note

If the credentials are valid but do not match the client information in
the token, you will receive a successful response (status 200 OK),
however with ` "active": false, ` in the response body.
:::
:::
