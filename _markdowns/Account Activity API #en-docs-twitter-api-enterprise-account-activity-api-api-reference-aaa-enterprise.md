



Enterprise Account Activity
API | Docs | Twitter Developer Platform 





































































































Enterprise Account Activity
API



aaa-enterprise

Enterprise Account Activity
API
===============================


POST
account\_activity/webhooks¶
--------------------------------


Registers a new webhook URL for the given application context. The
URL will be validated via CRC request before saving. In case the
validation failed, returns comprehensive error message to the
requester.


The number of allowed webhooks is determined by billing package.


### Resource URL¶


`https://api.twitter.com/1.1/account_activity/webhooks.json`


### Resource Information¶




|  |  |
| --- | --- |
| Response Format | JSON |
| Requires Authentication | Yes (user context - all consumer and access tokens) |
| Rate Limited | Yes |
| Requests / 15-min window (user auth) | 15 |
| Support for Tweet edits | All Tweet objects will include Tweet edit metadata describing the
Tweet's edit history. See the "Tweet
edits" fundamentals page for more details. |


### Parameters¶




|  |  |
| --- | --- |
| url (required) | Encoded URL for the callback endpoint. |


### Example Request¶



```
$ curl --request POST 
   --url 'https://api.twitter.com/1.1/account_activity/webhooks.json?url=https%3A%2F%2Fyour_domain.com%2Fwebhooks%2Ftwitter%2F0' 
   --header 'authorization: OAuth oauth_consumer_key="CONSUMER_KEY", oauth_nonce="GENERATED", oauth_signature="GENERATED", oauth_signature_method="HMAC-SHA1", oauth_timestamp="GENERATED", oauth_token="ACCESS_TOKEN", oauth_version="1.0"'
```

### HTTP Responses¶




| HTTP Code | Message |
| --- | --- |
| 200 | Webhook URL is registered to the provided application |
| 403 | There is an error with your request. See error messages section
below. |


### Example Response - Success¶


*HTTP 200*



```
{
  "id": "1234567890",
  "url": "https://your_domain.com/webhook/twitter/0",
  "valid": true,
  "created_at": "2016-06-02T23:54:02Z"
}
```

### Error Messages¶




| Code | Message |
| --- | --- |
| 214 | Webhook URL does not meet the requirements. |
| 214 | Too many resources already created. |
| 214 | Webhook URL does not meet the requirements. Invalid CRC token or
json response format. |
| 214 | High latency on CRC GET request. Your webhook should respond in less
than 3 seconds. |
| 214 | Non-200 response code during CRC GET request (i.e. 404, 500,
etc). |


*HTTP 403*



```
{
  "errors": [
    {
      "code": 214,
      "message": "Too many resources already created."
    }
  ]
}
```

GET account\_activity/webhooks¶
-------------------------------


Returns all URLs and their statuses for the given application.


We mark a URL as invalid if it fails the daily validation check. In
order to re-enable the URL, call the update endpoint.


### Resource URL¶


`https://api.twitter.com/1.1/account_activity/webhooks.json`


### Resource Information¶




|  |  |
| --- | --- |
| Response Format | JSON |
| Requires Authentication | Yes (application only - bearer token) |
| Rate Limited | Yes |
| Requests / 15-min window (application auth) | 15 |


### Example Request¶



```
$ curl --request GET 
 --url https://api.twitter.com/1.1/account_activity/webhooks.json 
 --header 'authorization: Bearer TOKEN'
```

### Example Response¶


*HTTP 200 OK*



```
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
```

### Error Messages¶




| Code | Message |
| --- | --- |
| 99 | You don’t have access to this resource. |


PUT
account\_activity/webhooks/:webhook\_id¶
--------------------------------------------


Triggers the challenge response check (CRC) for the given webhook's
URL. If the check is successful, returns 204 and reenables the webhook
by setting its status to `valid`.


### Resource URL¶


`https://api.twitter.com/1.1/account_activity/webhooks/:webhook_id.json`


### Resource Information¶




|  |  |
| --- | --- |
| Response Format | JSON |
| Requires Authentication | Yes (user context - all consumer and access tokens) |
| Rate Limited | Yes |
| Requests / 15-min window (user auth) | 15 |


### Parameters¶




|  |  |
| --- | --- |
| webhook\_id (required) | Webhook ID. Defined in resource path. |


### Example Request¶



```
$ curl --request PUT 
 --url https://api.twitter.com/1.1/account_activity/webhooks/:WEBHOOK_ID.json 
 --header 'authorization: OAuth oauth_consumer_key="CONSUMER_KEY", oauth_nonce="GENERATED", oauth_signature="GENERATED", oauth_signature_method="HMAC-SHA1", oauth_timestamp="GENERATED", oauth_token="ACCESS_TOKEN", oauth_version="1.0"'
```

### Response¶


*HTTP 204 OK*



```
{ }
```

### Error Messages¶




| Code | Message |
| --- | --- |
| 34 | Webhook does not exist or is associated with a different twitter
application. |
| 214 | Webhook URL does not meet the requirements. |
| 214 | Webhook URL does not meet the requirements. Invalid CRC token or
json response format. |
| 214 | High latency on CRC GET request. Your webhook should respond in less
than 3 seconds. |
| 214 | Non-200 response code during CRC GET request (i.e. 404, 500,
etc). |


POST
account\_activity/webhooks/:webhook\_id/subscriptions/all¶
---------------------------------------------------------------


Subscribes the provided application to all events for the provided
user context for all message types. After activation, all events for the
requesting user will be sent to the application’s webhook via POST
request.


Subscriptions are currently limited based on your account
configuration. If you have a need to add more subscriptions, please
contact your account manager.


### Resource URL¶


`https://api.twitter.com/1.1/account_activity/webhooks/:webhook_id/subscriptions/all.json`


### Resource Information¶




|  |  |
| --- | --- |
| Response Format | JSON |
| Requires Authentication | Yes (3-legged OAuth - Whitelisted consumer key and subscribing
user's access token) |
| Rate Limited | Yes |
| Requests / 15-min window (user auth) | 500 |


### Parameters¶




|  |  |
| --- | --- |
| webhook\_id (required) | Webhook ID. Defined in resource path. |


### Example Request¶



```
$ curl --request POST 
 --url https://api.twitter.com/1.1/account_activity/webhooks/:WEBHOOK_ID/subscriptions/all.json 
 --header 'authorization: OAuth oauth_consumer_key="WHITELISTED_CONSUMER_KEY", oauth_nonce="GENERATED", oauth_signature="GENERATED", oauth_signature_method="HMAC-SHA1", oauth_timestamp="GENERATED", oauth_token="SUBSCRIBING_USER'S_ACCESS_TOKEN", oauth_version="1.0"'
```

### Example Response - Success¶


*HTTP 204 NO CONTENT*



```
{}
```

### Error Messages¶




| Code | Message |
| --- | --- |
| 34 | Webhook does not exist or is associated with a different twitter
application. |
| 348 | Client application is not permitted to access this user's webhook
subscriptions. |


GET
account\_activity/subscriptions/count¶
------------------------------------------


Returns the count of subscriptions that are currently active on your
account. Note that the /count endpoint requires application-only OAuth,
so that you should make requests using a bearer token instead of user
context.


### Resource URL¶


`https://api.twitter.com/1.1/account_activity/subscriptions/count.json`


### Resource Information¶




|  |  |
| --- | --- |
| Response Format | HTTP response code |
| Requires Authentication | Yes (application only - bearer token) |
| Rate Limited | Yes |
| Requests / 15-min window (application auth) | 15 |


### HTTP Response Codes¶




|  |  |
| --- | --- |
| Code | Message |
| 200 | Success. A count of subscriptions for the requested webhook will be
returned. |
| 401 | Your application does not have permission to view subscriptions for
the specified webhook. |


### Example Request¶



```
$ curl --request GET 
 --url https://api.twitter.com/1.1/account_activity/subscriptions/count.json 
 --header 'authorization: Bearer TOKEN'
```

### Example Response - Success¶


*HTTP 200*



```
{
  "account_name":"my-account",
  "subscriptions_count_all":"1",
  "subscriptions_count_direct_messages":"0",
  "provisioned_count":"50"
}
```

### Error Messages¶




| Code | Message |
| --- | --- |
| 32 | Could not authenticate you. |


*HTTP 401*



```
{
  "errors": [
    {
       "code": 32,
      "message": "Could not authenticate you."
    }
  ]
}
```

GET
account\_activity/webhooks/:webhook\_id/subscriptions/all¶
--------------------------------------------------------------


Provides a way to determine if a webhook configuration is subscribed
to the provided user’s events. If the provided user context has an
active subscription with provided application, returns 204 OK. If the
response code is not 204, then the user does not have an active
subscription. See HTTP Response code and error messages below for
details.


### Resource URL¶


`https://api.twitter.com/1.1/account_activity/webhooks/:webhook_id/subscriptions/all.json`


### Resource Information¶




|  |  |
| --- | --- |
| Response Format | JSON |
| Requires Authentication | Yes (3-legged OAuth - Whitelisted consumer key and subscribing
user's access token) |
| Rate Limited | Yes |
| Requests / 15-min window (user auth) | 500 |


### Parameters¶




|  |  |
| --- | --- |
| webhook\_id (required) | Webhook ID. Defined in resource path. |


### Example Request¶



```
$ curl --request GET 
 --url https://api.twitter.com/1.1/account_activity/webhooks/:WEBHOOK_ID/subscriptions/all.json 
 --header 'authorization: OAuth oauth_consumer_key="WHITELISTED_CONSUMER_KEY", oauth_nonce="GENERATED", oauth_signature="GENERATED", oauth_signature_method="HMAC-SHA1", oauth_timestamp="GENERATED", oauth_token="SUBSCRIBING_USER'S_ACCESS_TOKEN", oauth_version="1.0"'
```

### Example Response - Success¶


*HTTP 204 NO CONTENT*



```
{ }
```

GET
account\_activity/webhooks/:webhook\_id/subscriptions/all/list¶
-------------------------------------------------------------------


Returns a list of the current All Activity type subscriptions for the
specified webhook. Note that the /list endpoint requires
application-only OAuth, so requests should be made using a bearer token
instead of user context.


### Resource URL¶


`https://api.twitter.com/1.1/account_activity/webhooks/:webhook_id/subscriptions/all/list.json`


### Resource Information¶




|  |  |
| --- | --- |
| Response Format | HTTP response code |
| Requires Authentication | Yes (application only - bearer token) |
| Rate Limited | Yes |
| Requests / 15-min window (application auth) | 50 |


### Parameters¶




|  |  |
| --- | --- |
| webhook\_id (required) | Webhook ID. Defined in resource path. |


### HTTP Response Codes¶




| Code | Message |
| --- | --- |
| 200 | Success. A list of subscriptions for the requested webhook will be
returned. |
| 401 | Your application does not have permission to view subscriptions for
the specified webhook. |


### Example Request¶



```
$ curl --request GET 
 --url https://api.twitter.com/1.1/account_activity/webhooks/:WEBHOOK_ID/subscriptions/all/list.json 
 --header 'authorization: Bearer TOKEN'
```

### Example Response - Success¶


*HTTP 200*



```
{
  "webhook_id": "1234567890",
  "webhook_url": "https://your_domain.com/webhook/twitter/0",
  "application_id": "11231812",
  "subscriptions": [{
    "user_id": "20212306"
  }]
}
```

### Error Messages¶




| Code | Message |
| --- | --- |
| 32 | Could not authenticate you. |


*HTTP 401*



```
{
  "errors": [
    {
       "code": 32,
      "message": "Could not authenticate you."
    }
  ]
}
```

DELETE
account\_activity/webhooks/:webhook\_id¶
-----------------------------------------------


Removes the webhook from the provided application's configuration.
The webhook ID can be accessed by making a call to GET
/1.1/account\_activity/webhooks.


### Resource URL¶


`https://api.twitter.com/1.1/account_activity/webhooks/:webhook_id.json`


### Resource Information¶




|  |  |
| --- | --- |
| Response Format | JSON |
| Requires Authentication | Yes (user context - all consumer and access tokens) |
| Rate Limited | Yes |
| Requests / 15-min window (user auth) | 15 |


### Parameters¶




|  |  |
| --- | --- |
| webhook\_id (required) | Webhook ID. Defined in resource path. |


### Example Request¶



```
$ curl --request DELETE 
 --url https://api.twitter.com/1.1/account_activity/webhooks/:WEBHOOK_ID.json 
 --header 'authorization: OAuth oauth_consumer_key="CONSUMER_KEY", oauth_nonce="GENERATED", oauth_signature="GENERATED", oauth_signature_method="HMAC-SHA1", oauth_timestamp="GENERATED", oauth_token="ACCESS_TOKEN", oauth_version="1.0"'
```

### Response¶


*HTTP 204 OK*



```
{ }
```

DELETE
account\_activity/webhooks/:webhook\_id/subscriptions/all
(DEPRECATED)¶
------------------------------------------------------------------------------


Deactivates subscription(s) for the provided user context and
application. After deactivation, all events for the requesting user will
no longer be sent to the webhook URL.


### Resource URL¶


`https://api.twitter.com/1.1/account_activity/webhooks/:webhook_id/subscriptions/all.json`


### Resource Information¶




|  |  |
| --- | --- |
| Response Format | JSON |
| Requires Authentication | Yes (3-legged OAuth - Whitelisted consumer key and subscribed user's
access token) |
| Rate Limited | Yes |
| Requests / 15-min window (user auth) | 500 |


### Parameters¶




|  |  |
| --- | --- |
| webhook\_id (required) | Webhook ID. Defined in resource path. |


### Example Request¶



```
$ curl --request DELETE 
 --url https://api.twitter.com/1.1/account_activity/webhooks/:WEBHOOK_ID/subscriptions/all.json 
 --header 'authorization: OAuth oauth_consumer_key="WHITELISTED_CONSUMER_KEY", oauth_nonce="GENERATED", oauth_signature="GENERATED", oauth_signature_method="HMAC-SHA1", oauth_timestamp="GENERATED", oauth_token="SUBSCRIBED_USER'S_ACCESS_TOKEN", oauth_version="1.0"'

Example Request
```



---



```
{ }
```

DELETE
/account\_activity/webhooks/:webhook\_id/subscriptions/:user\_id/all.json¶
---------------------------------------------------------------------------------


Deactivates subscription for the specified webhook and user id. After
deactivation, all events for the requesting user will no longer be sent
to the webhook URL. Note, that this endpoint requires application-only
OAuth, so requests should be made using a bearer token instead of user
context.


### Resource URL¶


`https://api.twitter.com/1.1/account_activity/webhooks/:webhook_id/subscriptions/:user_id/all.json`


### Resource Information¶




|  |  |
| --- | --- |
| Response Format | JSON |
| Requires Authentication | Yes (application only - bearer token) |
| Rate Limited | Yes |
| Requests / 15-min window | 500 |


### Example Request¶



```
$ curl --request DELETE 
 --url https://api.twitter.com/1.1/account_activity/webhooks/:webhook_id/subscriptions/:user_id/all.json 
 --header 'authorization: Bearer TOKEN'

```

### Response¶


*HTTP 204 NO CONTENT*


### Error Messages¶




| Code | Message |
| --- | --- |
| 404 | Sorry, that page does not exist. - This often occurs when the
specified user id is not actually subscribed. |



















Developer policy and terms


Follow @XDevelopers


Subscribe to developer news












#### 
 X platform


* X.com
* Status
* Accessibility
* Embed a post
* Privacy Center
* Transparency Center
* Download the X app




#### 
 X Corp.


* About the company
* Company news
* Brand toolkit
* Jobs and internships
* Investors




#### 
 Help


* Help Center
* Using X
* X for creators
* Ads Help Center
* Managing your account
* Email Preference Center
* Rules and policies
* Contact us




#### 
 Developer resources


* Developer home
* Documentation
* Forums
* Communities
* Developer blog
* Engineering blog
* Developer terms




#### 
 Business resources


* Advertise
* X for business
* Resources and guides
* X for marketers
* Marketing insights
* Brand inspiration
* X Ads Academy









 © 2024 X Corp.
 


Cookies


Privacy


Terms and conditions






















**Did someone say … cookies?**  
  


 X and its partners use cookies to provide you with a better, safer and
 faster service and to support our business. Some cookies are necessary to use
 our services, improve our services, and make sure they work properly.
 Show more about your choices.


 




* Accept all cookies
* Refuse non-essential cookies















