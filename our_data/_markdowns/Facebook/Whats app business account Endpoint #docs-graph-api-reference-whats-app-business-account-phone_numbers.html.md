Graph API Reference v19.0: Whats App Business Account Phone Numbers - Documentation - Meta for Developers

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
Graph API Versionv19.0Whats App Business Account Phone Numbers
========================================
Represents a collection of business phone numbers associated with a WhatsApp Business Account (WABA).

 To find the ID of a WhatsApp Business Account, go to **Business Manager** > **Business Settings** > **Accounts** > **WhatsApp Business Accounts**. Find the account you want to use and click on it. A panel opens, with information about the account, including the ID.
For more information on how to use the API, see WhatsApp Business Management API.

Reading
-------
Get a list of phone numbers associated with a WhatsApp Business Account.

### Requirements

 Type | Description || Access Tokens | User or System User |
| Permissions | whatsapp\_business\_management
whatsapp\_business\_messaging |
### Request Syntax

```
GET https://graph.facebook.com/<API_VERSION>/<WABA_ID>/phone_numbers
```
### Response

A list of WhatsApp Business Phone Number nodes and their default fields.

### Sample Request

```
curl \
'https://graph.facebook.com/v15.0/102289599326934/phone_numbers' \
-H 'Authorization: Bearer EAAJi...'
```
### Sample Response

```
{
  "data" : [
    {
      "code_verification_status" : "VERIFIED",
      "display_phone_number" : "+1 555-555-5555",
      "id" : "106853218861309",
      "quality_rating" : "GREEN",
      "verified_name" : "Jaspers Market"
    }
  ],
  "paging" : {
    "cursors" : {
      "after" : "QVFIU...",
      "before" : "QVFIU..."
    }
  }
}
```
### Sample Request with Filtering

See Filtering Phone Numbers.

```
curl GET \
"https://graph.facebook.com/v19.0/102289599326934/phone_numbers \
 ?fields=id,is_official_business_account,display_phone_number,verified_name \
 &filtering=[{'field':'account_mode','operator':'EQUAL','value':'SANDBOX'}]" \
-H 'Authorization: Bearer EAAJi...'
```
### Sample Response 2

```
{   
   "id" : "106853218861309", 
   "is_official_business_account" : true,
   "display_phone_number" : "+1 555-555-5555",      
   "verified_name" : "Jaspers Market"
}
```
### Parameters
This endpoint doesn't have any parameters.### Fields
Reading from this edge will return a JSON formatted result:

```
{
 "`data`": [],
 "`paging`": {},
 "`summary`": {}
}

```
#### `data`
A list of WhatsAppBusinessAccountToNumberCurrentStatus nodes.#### `paging`
For more details about pagination, see the Graph API guide.#### `summary`
Aggregated information about the edge, such as counts. Specify the fields to fetch in the summary param (like `summary=total_count`).

| Field | Description |
| --- | --- |
| `total_count`unsigned int32 | The current number of phone numbers that belong to a WhatsApp Business Account
 |
### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 80008 | There have been too many calls to this WhatsApp Business account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |
Creating
--------

 Create a business phone number on a WhatsApp Business Account.
 ### Requirements

 Type | Description || Access Tokens | User or System User. |
| Permissions | whatsapp\_business\_management
whatsapp\_business\_messaging |
### Sample Request

cURLAndroid SDKObjective-C
```
curl -i -X POST \
 "https://graph.facebook.com/LATEST-VERSION/WHATSAPP-BUSINESS-ACCOUNT-ID/phone_numbers?
  cc=COUNTRY-CODE&
  phone_number=PHONE-NUMBER&
  migrate_phone_number=true&
  access_token=USER-ACCESS-TOKEN"
```
```
GraphRequest request = GraphRequest.newPostRequest(
  accessToken,
  "/WHATSAPP-BUSINESS-ACCOUNT-ID/phone_numbers",
  new JSONObject("{\"cc\":\"COUNTRY-CODE\",\"phone_number\":\"PHONE-NUMBER\",\"migrate_phone_number\":true}"),
  new GraphRequest.Callback() {
    @Override
    public void onCompleted(GraphResponse response) {
      // Insert your code here
    }
});
request.executeAsync();
```
```
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
    initWithGraphPath:@"/WHATSAPP-BUSINESS-ACCOUNT-ID/phone_numbers"
           parameters:@{ @"cc": @"COUNTRY-CODE",@"phone_number": @"PHONE-NUMBER",@"migrate_phone_number": @"true",}
           HTTPMethod:@"POST"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection, id result, NSError *error) {
    // Insert your code here
}];
```
### Sample Response

```
{
  "id": "POST-ID"
}
```
You can make a POST request to `phone_numbers` edge from the following paths: * `/{whats_app_business_account_id}/phone_numbers`
When posting to this edge, a WhatsAppBusinessPhoneNumber will be created.### Parameters

| Parameter | Description |
| --- | --- |
| `cc`string | Country dial code of the phone number (for example, `1`).
 |
| `migrate_phone_number`boolean | Set to `true` to migrate a registered WhatsApp Business Phone Number from one WhatsApp Business Account to another.
 |
| `phone_number`string | Phone number without the country code or plus symbol (`+`).
 |
| `preverified_id`string | Preverified ID related to this phone number
 |
| `verified_name`string | Name of the business as it appears in the WhatsApp app or WhatsApp Business app profile.
 |
### Return Type
This endpoint supports read-after-write and will read the node represented by `id` in the return type. Struct {`id`: numeric string, }### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
Updating
--------
You can't perform this operation on this endpoint.Deleting
--------
You can't perform this operation on this endpoint.