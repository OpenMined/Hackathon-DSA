Graph API Reference v19.0: Whats App Message Template Compare - Documentation - Meta for Developers

Graph API* Overview
* Get Started
* Batch Requests
* Debug Requests
* Handle Errors
* Field Expansion
* Secure Requests
* Resumable Upload API
* Changelog
* Features Reference
* Permissions Reference
* Reference
Graph API Versionv19.0Whats App Message Template Compare
==================================
Compare template send counts and block ratios. See Template Comparison.

Reading
-------
Compare the WhatsApp message template's send count and block ratio to another WhatsApp message template's send count and block ratio.

### Requirements

 Type | Description || Access Tokens | User or System User |
| Permissions | business\_management |
### Limitations

* Only two templates can be compared at a time.
* Templates must have been sent at least 1,000 times in the queries specified timeframe.
* Timeframes are limited to 7, 30, 60 and 90 day lookbacks from the time of the request.

### Request Syntax

```
GET /<WHATSAPP_MESSAGE_TEMPLATE_ID>/compare
  ?template_ids=[<TEMPLATE_IDS]
  &start=<START>
  &end=<END>
```
### Response

```
{
  "data": [
    {
      "metric": "BLOCK_RATE",
      "type": "RELATIVE",
      "order_by_relative_metric": [<ORDER_BY_RELATIVE_METRIC>]
    },
    {
      "metric": "MESSAGE_SENDS",
      "type": "NUMBER_VALUES",
      "number_values": [<NUMBER_VALUES>]
    },
    {
      "metric": "TOP_BLOCK_REASON",
      "type": "STRING_VALUES",
      "string_values": [<STRING_VALUES>]
    }
  ]
}
```
### Sample Request

```
curl -X GET 'https://graph.facebook.com/v19.0/5289179717853347/compare?template_ids=[1533406637136032]&start=1674844791182&end=1674845395982' \
-H 'Authorization: Bearer EAAJB...'
```
### Sample Response

```
{
  "data": [
    {
      "metric": "BLOCK_RATE",
      "type": "RELATIVE",
      "order_by_relative_metric": [
        "1533406637136032",
        "5289179717853347"
      ]
    },
    {
      "metric": "MESSAGE_SENDS",
      "type": "NUMBER_VALUES",
      "number_values": [
        {
          "key": "5289179717853347",
          "value": 1273
        },
        {
          "key": "1533406637136032",
          "value": 1042
        }
      ]
    },
    {
      "metric": "TOP_BLOCK_REASON",
      "type": "STRING_VALUES",
      "string_values": [
        {
          "key": "5289179717853347",
          "value": "UNKNOWN_BLOCK_REASON"
        },
        {
          "key": "1533406637136032",
          "value": "UNKNOWN_BLOCK_REASON"
        }
      ]
    }
  ]
}
```
### Example
HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v19.0/{whats-app-message-template-id}/compare HTTP/1.1
Host: graph.facebook.com
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{whats-app-message-template-id}/compare',
    '{access-token}'
  );
} catch(Facebook\Exceptions\FacebookResponseException $e) {
  echo 'Graph returned an error: ' . $e->getMessage();
  exit;
} catch(Facebook\Exceptions\FacebookSDKException $e) {
  echo 'Facebook SDK returned an error: ' . $e->getMessage();
  exit;
}
$graphNode = $response->getGraphNode();
/* handle the result */
```
```
/* make the API call */
FB.api(
    "/{whats-app-message-template-id}/compare",
    function (response) {
      if (response && !response.error) {
        /* handle the result */
      }
    }
);
```
```
/* make the API call */
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "/{whats-app-message-template-id}/compare",
    null,
    HttpMethod.GET,
    new GraphRequest.Callback() {
        public void onCompleted(GraphResponse response) {
            /* handle the result */
        }
    }
).executeAsync();
```
```
/* make the API call */
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                               initWithGraphPath:@"/{whats-app-message-template-id}/compare"
                                      parameters:params
                                      HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
If you want to learn how to use the Graph API, read our Using Graph API guide.### Parameters

| Parameter | Description |
| --- | --- |
| `end`datetime/timestamp | UNIX timestamp indicating end of timeframe. Timeframes are limited to 7, 30, 60 and 90 day lookbacks from the time of the request. To define a timeframe, set your end date to the current time as a UNIX timestamp, then subtract the number of days for your desired timeframe, in seconds, from that value:
Required |
| `start`datetime/timestamp | UNIX timestamp indicating start of timeframe. Timeframes are limited to 7, 30, 60 and 90 day lookbacks from the time of the request. To define a timeframe, set your end date to the current time as a UNIX timestamp, then subtract the number of days for your desired timeframe, in seconds, from that value:
Required |
| `template_ids`array<EntWhatsAppBusinessHSM ID> | ID of the WhatsApp Message Template to compare the target to.
Required |
### Fields
Reading from this edge will return a JSON formatted result:

```
{
 "`data`": [],
 "`paging`": {}
}

```
#### `data`
A list of WhatsAppBusinessHSMComparison nodes.#### `paging`
For more details about pagination, see the Graph API guide.### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
Creating
--------
You can't perform this operation on this endpoint.Updating
--------
You can't perform this operation on this endpoint.Deleting
--------
You can't perform this operation on this endpoint.