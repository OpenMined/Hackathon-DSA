Registers a new webhook URL for the given application context. The URL
will be validated via CRC request before saving. In case the validation
failed, returns comprehensive error message to the requester.

The number of allowed webhooks is determined by billing package.

### Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/account_activity/webhooks.json `

  -------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Response Format                        JSON
  Requires Authentication                Yes (user context - all consumer and access tokens)
  Rate Limited                           Yes
  Requests / 15-min window (user auth)   15
  Support for Tweet edits                All Tweet objects will include Tweet edit metadata describing the Tweet\'s edit history. See the [\"Tweet edits\" fundamentals](https://developer.twitter.com/en/docs/twitter-api/enterprise/tweet-edits) page for more details.
  -------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Parameters [¶](#parameters){.headerlink}

  ---------------- ----------------------------------------
  url (required)   Encoded URL for the callback endpoint.
  ---------------- ----------------------------------------

### Example Request [¶](#example-request){.headerlink}

    $ curl --request POST 
       --url 'https://api.twitter.com/1.1/account_activity/webhooks.json?url=https%3A%2F%2Fyour_domain.com%2Fwebhooks%2Ftwitter%2F0' 
       --header 'authorization: OAuth oauth_consumer_key="CONSUMER_KEY", oauth_nonce="GENERATED", oauth_signature="GENERATED", oauth_signature_method="HMAC-SHA1", oauth_timestamp="GENERATED", oauth_token="ACCESS_TOKEN", oauth_version="1.0"'

### HTTP Responses [¶](#http-responses){.headerlink}

  ----- ------------------------------------------------------------------------
  200   Webhook URL is registered to the provided application
  403   There is an error with your request. See error messages section below.
  ----- ------------------------------------------------------------------------

### Example Response - Success [¶](#example-response-success){.headerlink} {#example-response-success}

*HTTP 200*

    {
      "id": "1234567890",
      "url": "https://your_domain.com/webhook/twitter/0",
      "valid": true,
      "created_at": "2016-06-02T23:54:02Z"
    }

### Error Messages [¶](#error-messages){.headerlink}

  ----- ----------------------------------------------------------------------------------------
  214   Webhook URL does not meet the requirements.
  214   Too many resources already created.
  214   Webhook URL does not meet the requirements. Invalid CRC token or json response format.
  214   High latency on CRC GET request. Your webhook should respond in less than 3 seconds.
  214   Non-200 response code during CRC GET request (i.e. 404, 500, etc).
  ----- ----------------------------------------------------------------------------------------

*HTTP 403*

    {
      "errors": [
        {
          "code": 214,
          "message": "Too many resources already created."
        }
      ]
    }

## GET account_activity/webhooks [¶](#get-account-activity-webhooks){.headerlink} {#get-account-activity-webhooks}

Returns all URLs and their statuses for the given application.

We mark a URL as invalid if it fails the daily validation check. In
order to re-enable the URL, call the update endpoint.

### Resource URL [¶](#resource-url){.headerlink} {#resource-url}

` https://api.twitter.com/1.1/account_activity/webhooks.json `

  --------------------------------------------- ---------------------------------------
  Response Format                               JSON
  Requires Authentication                       Yes (application only - bearer token)
  Rate Limited                                  Yes
  Requests / 15-min window (application auth)   15
  --------------------------------------------- ---------------------------------------

### Example Request [¶](#example-request){.headerlink} {#example-request}

    $ curl --request GET 
     --url https://api.twitter.com/1.1/account_activity/webhooks.json 
     --header 'authorization: Bearer TOKEN'

### Example Response [¶](#example-response){.headerlink}

*HTTP 200 OK*

    [
      {
        "id": "1234567890",
        "url": "https://your_domain.com/webhook/twitter/0",
        "valid": true,
        "created_at": "2016-06-02T23:54:02Z"
      }
      {
        "id": "2468013579",
        "url": "https://your_domain2.com/webhook/twitter/0",
        "valid": true,
        "created_at": "2016-06-04T22:31:29Z"
      }
    ]

### Error Messages [¶](#error-messages){.headerlink} {#error-messages}

  ---- -----------------------------------------
  99   You don't have access to this resource.
  ---- -----------------------------------------

## PUT account_activity/webhooks/:webhook_id [¶](#put-account-activity-webhooks-webhook-id){.headerlink} {#put-account-activity-webhooks-webhook-id}

Triggers the challenge response check (CRC) for the given webhook\'s
URL. If the check is successful, returns 204 and reenables the webhook
by setting its status to ` valid ` .

### Resource URL [¶](#resource-url){.headerlink} {#resource-url}

` https://api.twitter.com/1.1/account_activity/webhooks/:webhook_id.json `

  -------------------------------------- -----------------------------------------------------
  Response Format                        JSON
  Requires Authentication                Yes (user context - all consumer and access tokens)
  Rate Limited                           Yes
  Requests / 15-min window (user auth)   15
  -------------------------------------- -----------------------------------------------------

### Parameters [¶](#parameters){.headerlink} {#parameters}

  ----------------------- ---------------------------------------
  webhook_id (required)   Webhook ID. Defined in resource path.
  ----------------------- ---------------------------------------

### Example Request [¶](#example-request){.headerlink} {#example-request}

    $ curl --request PUT 
     --url https://api.twitter.com/1.1/account_activity/webhooks/:WEBHOOK_ID.json 
     --header 'authorization: OAuth oauth_consumer_key="CONSUMER_KEY", oauth_nonce="GENERATED", oauth_signature="GENERATED", oauth_signature_method="HMAC-SHA1", oauth_timestamp="GENERATED", oauth_token="ACCESS_TOKEN", oauth_version="1.0"'

### Response [¶](#response){.headerlink}

*HTTP 204 OK*

    { }

### Error Messages [¶](#error-messages){.headerlink} {#error-messages}

  ----- ----------------------------------------------------------------------------------------
  34    Webhook does not exist or is associated with a different twitter application.
  214   Webhook URL does not meet the requirements.
  214   Webhook URL does not meet the requirements. Invalid CRC token or json response format.
  214   High latency on CRC GET request. Your webhook should respond in less than 3 seconds.
  214   Non-200 response code during CRC GET request (i.e. 404, 500, etc).
  ----- ----------------------------------------------------------------------------------------

## POST account_activity/webhooks/:webhook_id/subscriptions/all [¶](#post-account-activity-webhooks-webhook-id-subscriptions-all){.headerlink} {#post-account-activity-webhooks-webhook-id-subscriptions-all}

Subscribes the provided application to all events for the provided user
context for all message types. After activation, all events for the
requesting user will be sent to the application's webhook via POST
request.

Subscriptions are currently limited based on your account configuration.
If you have a need to add more subscriptions, please contact your
account manager.

### Resource URL [¶](#resource-url){.headerlink} {#resource-url}

` https://api.twitter.com/1.1/account_activity/webhooks/:webhook_id/subscriptions/all.json `

  -------------------------------------- --------------------------------------------------------------------------------------
  Response Format                        JSON
  Requires Authentication                Yes (3-legged OAuth - Whitelisted consumer key and subscribing user\'s access token)
  Rate Limited                           Yes
  Requests / 15-min window (user auth)   500
  -------------------------------------- --------------------------------------------------------------------------------------

### Parameters [¶](#parameters){.headerlink} {#parameters}

  ----------------------- ---------------------------------------
  webhook_id (required)   Webhook ID. Defined in resource path.
  ----------------------- ---------------------------------------

### Example Request [¶](#example-request){.headerlink} {#example-request}

    $ curl --request POST 
     --url https://api.twitter.com/1.1/account_activity/webhooks/:WEBHOOK_ID/subscriptions/all.json 
     --header 'authorization: OAuth oauth_consumer_key="WHITELISTED_CONSUMER_KEY", oauth_nonce="GENERATED", oauth_signature="GENERATED", oauth_signature_method="HMAC-SHA1", oauth_timestamp="GENERATED", oauth_token="SUBSCRIBING_USER'S_ACCESS_TOKEN", oauth_version="1.0"'

### Example Response - Success [¶](#example-response-success){.headerlink} {#example-response-success}

*HTTP 204 NO CONTENT*

    {}

### Error Messages [¶](#error-messages){.headerlink} {#error-messages}

  ----- -----------------------------------------------------------------------------------
  34    Webhook does not exist or is associated with a different twitter application.
  348   Client application is not permitted to access this user\'s webhook subscriptions.
  ----- -----------------------------------------------------------------------------------

Returns the count of subscriptions that are currently active on your
account. Note that the /count endpoint requires application-only OAuth,
so that you should make requests using a bearer token instead of user
context.

### Resource URL [¶](#resource-url){.headerlink} {#resource-url}

` https://api.twitter.com/1.1/account_activity/subscriptions/count.json `

  --------------------------------------------- ---------------------------------------
  Response Format                               HTTP response code
  Requires Authentication                       Yes (application only - bearer token)
  Rate Limited                                  Yes
  Requests / 15-min window (application auth)   15
  --------------------------------------------- ---------------------------------------

### HTTP Response Codes [¶](#http-response-codes){.headerlink}

  ------ --------------------------------------------------------------------------------------------
  Code   Message
  200    Success. A count of subscriptions for the requested webhook will be returned.
  401    Your application does not have permission to view subscriptions for the specified webhook.
  ------ --------------------------------------------------------------------------------------------

### Example Request [¶](#example-request){.headerlink} {#example-request}

    $ curl --request GET 
     --url https://api.twitter.com/1.1/account_activity/subscriptions/count.json 
     --header 'authorization: Bearer TOKEN'

### Example Response - Success [¶](#example-response-success){.headerlink} {#example-response-success}

*HTTP 200*

    {
      "account_name":"my-account",
      "subscriptions_count_all":"1",
      "subscriptions_count_direct_messages":"0",
      "provisioned_count":"50"
    }

### Error Messages [¶](#error-messages){.headerlink} {#error-messages}

  ---- -----------------------------
  32   Could not authenticate you.
  ---- -----------------------------

*HTTP 401*

    {
      "errors": [
        {
           "code": 32,
          "message": "Could not authenticate you."
        }
      ]
    }

Provides a way to determine if a webhook configuration is subscribed to
the provided user's events. If the provided user context has an active
subscription with provided application, returns 204 OK. If the response
code is not 204, then the user does not have an active subscription. See
HTTP Response code and error messages below for details.

### Resource URL [¶](#resource-url){.headerlink} {#resource-url}

` https://api.twitter.com/1.1/account_activity/webhooks/:webhook_id/subscriptions/all.json `

  -------------------------------------- --------------------------------------------------------------------------------------
  Response Format                        JSON
  Requires Authentication                Yes (3-legged OAuth - Whitelisted consumer key and subscribing user\'s access token)
  Rate Limited                           Yes
  Requests / 15-min window (user auth)   500
  -------------------------------------- --------------------------------------------------------------------------------------

### Parameters [¶](#parameters){.headerlink} {#parameters}

  ----------------------- ---------------------------------------
  webhook_id (required)   Webhook ID. Defined in resource path.
  ----------------------- ---------------------------------------

### Example Request [¶](#example-request){.headerlink} {#example-request}

    $ curl --request GET 
     --url https://api.twitter.com/1.1/account_activity/webhooks/:WEBHOOK_ID/subscriptions/all.json 
     --header 'authorization: OAuth oauth_consumer_key="WHITELISTED_CONSUMER_KEY", oauth_nonce="GENERATED", oauth_signature="GENERATED", oauth_signature_method="HMAC-SHA1", oauth_timestamp="GENERATED", oauth_token="SUBSCRIBING_USER'S_ACCESS_TOKEN", oauth_version="1.0"'

### Example Response - Success [¶](#example-response-success){.headerlink} {#example-response-success}

*HTTP 204 NO CONTENT*

    { }

Returns a list of the current All Activity type subscriptions for the
specified webhook. Note that the /list endpoint requires
application-only OAuth, so requests should be made using a bearer token
instead of user context.

### Resource URL [¶](#resource-url){.headerlink} {#resource-url}

` https://api.twitter.com/1.1/account_activity/webhooks/:webhook_id/subscriptions/all/list.json `

  --------------------------------------------- ---------------------------------------
  Response Format                               HTTP response code
  Requires Authentication                       Yes (application only - bearer token)
  Rate Limited                                  Yes
  Requests / 15-min window (application auth)   50
  --------------------------------------------- ---------------------------------------

### Parameters [¶](#parameters){.headerlink} {#parameters}

  ----------------------- ---------------------------------------
  webhook_id (required)   Webhook ID. Defined in resource path.
  ----------------------- ---------------------------------------

### HTTP Response Codes [¶](#http-response-codes){.headerlink} {#http-response-codes}

  ----- --------------------------------------------------------------------------------------------
  200   Success. A list of subscriptions for the requested webhook will be returned.
  401   Your application does not have permission to view subscriptions for the specified webhook.
  ----- --------------------------------------------------------------------------------------------

### Example Request [¶](#example-request){.headerlink} {#example-request}

    $ curl --request GET 
     --url https://api.twitter.com/1.1/account_activity/webhooks/:WEBHOOK_ID/subscriptions/all/list.json 
     --header 'authorization: Bearer TOKEN'

### Example Response - Success [¶](#example-response-success){.headerlink} {#example-response-success}

*HTTP 200*

    {
      "webhook_id": "1234567890",
      "webhook_url": "https://your_domain.com/webhook/twitter/0",
      "application_id": "11231812",
      "subscriptions": [{
        "user_id": "20212306"
      }]
    }

### Error Messages [¶](#error-messages){.headerlink} {#error-messages}

  ---- -----------------------------
  32   Could not authenticate you.
  ---- -----------------------------

*HTTP 401*

    {
      "errors": [
        {
           "code": 32,
          "message": "Could not authenticate you."
        }
      ]
    }

## DELETE account_activity/webhooks/:webhook_id [¶](#delete-account-activity-webhooks-webhook-id){.headerlink} {#delete-account-activity-webhooks-webhook-id}

Removes the webhook from the provided application\'s configuration. The
webhook ID can be accessed by making a call to GET
/1.1/account_activity/webhooks.

### Resource URL [¶](#resource-url){.headerlink} {#resource-url}

` https://api.twitter.com/1.1/account_activity/webhooks/:webhook_id.json `

  -------------------------------------- -----------------------------------------------------
  Response Format                        JSON
  Requires Authentication                Yes (user context - all consumer and access tokens)
  Rate Limited                           Yes
  Requests / 15-min window (user auth)   15
  -------------------------------------- -----------------------------------------------------

### Parameters [¶](#parameters){.headerlink} {#parameters}

  ----------------------- ---------------------------------------
  webhook_id (required)   Webhook ID. Defined in resource path.
  ----------------------- ---------------------------------------

### Example Request [¶](#example-request){.headerlink} {#example-request}

    $ curl --request DELETE 
     --url https://api.twitter.com/1.1/account_activity/webhooks/:WEBHOOK_ID.json 
     --header 'authorization: OAuth oauth_consumer_key="CONSUMER_KEY", oauth_nonce="GENERATED", oauth_signature="GENERATED", oauth_signature_method="HMAC-SHA1", oauth_timestamp="GENERATED", oauth_token="ACCESS_TOKEN", oauth_version="1.0"'

### Response [¶](#response){.headerlink} {#response}

*HTTP 204 OK*

    { }

Deactivates subscription(s) for the provided user context and
application. After deactivation, all events for the requesting user will
no longer be sent to the webhook URL.

### Resource URL [¶](#resource-url){.headerlink} {#resource-url}

` https://api.twitter.com/1.1/account_activity/webhooks/:webhook_id/subscriptions/all.json `

  -------------------------------------- -------------------------------------------------------------------------------------
  Response Format                        JSON
  Requires Authentication                Yes (3-legged OAuth - Whitelisted consumer key and subscribed user\'s access token)
  Rate Limited                           Yes
  Requests / 15-min window (user auth)   500
  -------------------------------------- -------------------------------------------------------------------------------------

### Parameters [¶](#parameters){.headerlink} {#parameters}

  ----------------------- ---------------------------------------
  webhook_id (required)   Webhook ID. Defined in resource path.
  ----------------------- ---------------------------------------

### Example Request [¶](#example-request){.headerlink} {#example-request}

    $ curl --request DELETE 
     --url https://api.twitter.com/1.1/account_activity/webhooks/:WEBHOOK_ID/subscriptions/all.json 
     --header 'authorization: OAuth oauth_consumer_key="WHITELISTED_CONSUMER_KEY", oauth_nonce="GENERATED", oauth_signature="GENERATED", oauth_signature_method="HMAC-SHA1", oauth_timestamp="GENERATED", oauth_token="SUBSCRIBED_USER'S_ACCESS_TOKEN", oauth_version="1.0"'

    Example Request

    { }

Deactivates subscription for the specified webhook and user id. After
deactivation, all events for the requesting user will no longer be sent
to the webhook URL. Note, that this endpoint requires application-only
OAuth, so requests should be made using a bearer token instead of user
context.

### Resource URL [¶](#resource-url){.headerlink} {#resource-url}

` https://api.twitter.com/1.1/account_activity/webhooks/:webhook_id/subscriptions/:user_id/all.json `

  -------------------------- ---------------------------------------
  Response Format            JSON
  Requires Authentication    Yes (application only - bearer token)
  Rate Limited               Yes
  Requests / 15-min window   500
  -------------------------- ---------------------------------------

### Example Request [¶](#example-request){.headerlink} {#example-request}

    $ curl --request DELETE 
     --url https://api.twitter.com/1.1/account_activity/webhooks/:webhook_id/subscriptions/:user_id/all.json 
     --header 'authorization: Bearer TOKEN'

### Response [¶](#response){.headerlink} {#response}

*HTTP 204 NO CONTENT*

### Error Messages [¶](#error-messages){.headerlink} {#error-messages}

  ----- -------------------------------------------------------------------------------------------------------------
  404   Sorry, that page does not exist. - This often occurs when the specified user id is not actually subscribed.
  ----- -------------------------------------------------------------------------------------------------------------
