Graph API Reference v19.0: Whats App Business Account Conversation Analytics - Documentation - Meta for Developers

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
Graph API Versionv19.0Whats App Business Account Conversation Analytics
=================================================
Reading
-------
Enables one to retrieve the conversation based pricing analytics data for this WhatsApp Business Account

### Example

Requirements

* whatsapp\_business\_management permission
* whatsapp\_business\_messaging permission
* public\_profile permission
* WHATSAPP BUSINESS ACCOUNT ID
* USER ACCESS TOKEN

Request

*Formatted for readability.*

cURLAndroid SDKObjective-C
```
curl -i -X GET \ 
"https://graph.facebook.com/LATEST-VERSION/WHATSAPP-BUSINESS-ACCOUNT-ID?fields=conversation_analytics.start(1651698000).end(1652302800).granularity(DAILY).phone_numbers(PHONE-NUMBER).country_codes().metric_types().conversation_types().conversation_directions().dimensions(CONVERSATION_DIRECTIONCONVERSATION_TYPECOUNTRYPHONE)&
access_token=USER-ACCESS-TOKEN"
```
```
GraphRequest request = GraphRequest.newGraphPathRequest(
  accessToken,
  "/WHATSAPP-BUSINESS-ACCOUNT-ID",
  new GraphRequest.Callback() {
    @Override
    public void onCompleted(GraphResponse response) {
      // Insert your code here
    }
});
Bundle parameters = new Bundle();
parameters.putString("fields", "conversation_analytics.start(1651698000).end(1652302800).granularity(DAILY).phone_numbers(["PHONE-NUMBER "]).country_codes([]).metric_types([]).conversation_types([]).conversation_directions([]).dimensions(["CONVERSATION_DIRECTION","CONVERSATION_TYPE","COUNTRY","PHONE"])");
request.setParameters(parameters);
request.executeAsync();
```
```
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
    initWithGraphPath:@"/WHATSAPP-BUSINESS-ACCOUNT-ID"
           parameters:@{ @"fields": @"conversation_analytics.start(1651698000).end(1652302800).granularity(DAILY).phone_numbers(["PHONE-NUMBER"]).country_codes([]).metric_types([]).conversation_types([]).conversation_directions([]).dimensions(["CONVERSATION_DIRECTION","CONVERSATION_TYPE","COUNTRY","PHONE"])",}
           HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection, id result, NSError *error) {
    // Insert your code here
}];
```
Response

```
{
  "conversation_analytics": {
    "data": [
      {
        "data_points": [
          {
            "start": 1651698000,
            "end": 1651784400,
            "conversation": 281,
            "phone_number": "PHONE-NUMBER",
            "country": "US",
            "conversation_type": "FREE_TIER",
            "conversation_direction": "BUSINESS_INITIATED",
            "cost": 0
          },
          {
            "start": 1652130000,
            "end": 1652216400,
            "conversation": 631,
            "phone_number": "PHONE-NUMBER",
            "country": "US",
            "conversation_type": "FREE_TIER",
            "conversation_direction": "BUSINESS_INITIATED",
            "cost": 0
          }
        ]
      }
    ]
  },
  "id": "WHATSAPP-BUSINESS-ACCOUNT-ID"
}
```
### Parameters

| Parameter | Description |
| --- | --- |
| `conversation_categories`array<enum {UNKNOWN, MARKETING, UTILITY, AUTHENTICATION, SERVICE, MARKETING\_OPTIMIZED\_DELIVERY}> | Default value: `[]`list of conversation categories
 |
| `conversation_directions`array<enum {UNKNOWN, BUSINESS\_INITIATED, USER\_INITIATED}> | Default value: `[]`list of conversation directions
 |
| `conversation_types`array<enum {UNKNOWN, REGULAR, FREE\_ENTRY\_POINT, FREE\_TIER}> | Default value: `[]`list of conversation types
 |
| `country_codes`array<string> | Default value: `[]`list of country codes
 |
| `dimensions`array<enum {UNKNOWN, PHONE, COUNTRY, CONVERSATION\_TYPE, CONVERSATION\_DIRECTION, CONVERSATION\_CATEGORY}> | Default value: `[]`list of breakdown dimensions
 |
| `end`int64 | end time
Required |
| `granularity`enum {HALF\_HOUR, DAILY, MONTHLY} | data granularity
Required |
| `metric_types`array<enum {UNKNOWN, CONVERSATION, COST}> | Default value: `[]`list of metric types
 |
| `phone_numbers`array<string> | Default value: `[]`list of phone numbers
 |
| `start`int64 | start time
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
A list of WABAConversationAnalytics nodes.#### `paging`
For more details about pagination, see the Graph API guide.### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 131009 | Parameter value is not valid |
Creating
--------
You can't perform this operation on this endpoint.Updating
--------
You can't perform this operation on this endpoint.Deleting
--------
You can't perform this operation on this endpoint.