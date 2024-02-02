Graph API Reference v19.0: Whats App Business Account - Documentation - Meta for Developers

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
Graph API Versionv19.0WhatsApp Business Account
=========================
Represents a specific WhatsApp Business Account (WABA). Make the API call to the WABA ID.  

 To find the ID of a WhatsApp Business Account, go to **Business Manager** > **Business Settings** > **Accounts** > **WhatsApp Business Accounts**. Find the account you want to use and click on it. A panel opens, with information about the account, including the ID.
For more information on how to use the API, see WhatsApp Business Management API.

The following API calls are subject to Business Use Case Rate Limits:

* `GET`, `POST`, and `DELETE` calls to `/{whats-app-business-account-id}/assigned_users`
* `GET` calls to `/{whats-app-business-account-id}`

Reading
-------
Returns the account information of a WhatsApp Business Account

### Example

Requirements

* whatsapp\_business\_management permission
* whatsapp\_business\_messaging permission
* public\_profile permission
* WhatsApp Business Account (WABA) ID
* USER ACCESS TOKEN

Request

cURLAndroid SDKObjective-C
```
curl -i -X GET \
 "https://graph.facebook.com/LATEST-VERSION/WHATSAPP-BUSINESS-ACCOUNT-ID?access_token=USER-ACCESS-TOKEN"
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
request.executeAsync();
```
```
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
    initWithGraphPath:@"/WHATSAPP-BUSINESS-ACCOUNT-ID"
           parameters:nil
           HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection, id result, NSError *error) {
    // Insert your code here
}];
```
Response

```
{
  "id": "WHATSAPP-BUSINESS-ACCOUNT-ID",
  "name": "Test WhatsApp Business Account",
  "timezone_id": "1",
  "message_template_namespace": "MESSAGE-TEMPLATE-NAMESPACE"
}
```
### Parameters
This endpoint doesn't have any parameters.### Fields

| Field | Description |
| --- | --- |
| `id`numeric string | ID of the WhatApp Business Account.
Default |
| `account_review_status`enum | Status from account review process.
 |
| `analytics`WABAAnalytics | Used to designate which analytics metrics you want returned. See Analytics.
 |
| `business_verification_status`enum | Current status of business verification of Meta Business Account which owns this WhatsApp Business Account
 |
| `country`string | country of the WhatsApp Business Account's owning Meta Business account
 |
| `currency`string | The currency in which the payment transactions for the WhatsApp Business Account will be processed
Default |
| `is_enabled_for_insights`bool | If `true`, indicates the WhatsApp Business Account enabled template analytics. See Analytics.
 |
| `message_template_namespace`string | Namespace string for the message templates that belong to the WhatsApp Business Account
Default |
| `name`string | User-friendly name to differentiate WhatsApp Business Accounts
Default |
| `on_behalf_of_business_info`WABAOnBehalfOfComputedInfo | The "on behalf of" information for the WhatsApp Business Account
 |
| `ownership_type`enum | Ownership type of the WhatsApp Business Account
 |
| `primary_funding_id`numeric string | Primary funding ID for the WhatsApp Business Account paid service
 |
| `purchase_order_number`string | The purchase order number supplied by the business for payment management purposes
 |
| `timezone_id`string | The timezone of the WhatsApp Business Account
Default |
### Edges

| Edge | Description |
| --- | --- |
| `conversation_analytics` | Analytics data of the WhatsApp Business Account with conversation based pricing
 |
| `dcc_config` | Returns a list of DCC configs
 |
| `message_template_previews` | Retrieves a preview of a message template based on the provided configuration
 |
| `message_templates` | Message templates that belong to the WhatsApp Business Account
 |
| `phone_numbers` | The phone numbers that belong to the WhatsApp Business Account
 |
| `product_catalogs` | product\_catalogs
 |
| `subscribed_apps` | List of apps that are subscribed to webhooks updates for this WABA
 |
| `template_performance_metrics` | template\_performance\_metrics
 |
### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 131009 | Parameter value is not valid |
| 200 | Permissions error |
| 80008 | There have been too many calls to this WhatsApp Business account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |
| 131031 | Business Account locked |
| 131000 | Something went wrong |
Creating
--------
You can't perform this operation on this endpoint.Updating
--------
You can update a WhatsAppBusinessAccount by making a POST request to `/{whats_app_business_account_id}/assigned_users`.### Parameters

| Parameter | Description |
| --- | --- |
| `tasks`array<enum {MANAGE, DEVELOP, MANAGE\_TEMPLATES, MANAGE\_PHONE, VIEW\_COST, MANAGE\_EXTENSIONS, VIEW\_PHONE\_ASSETS, MANAGE\_PHONE\_ASSETS, VIEW\_TEMPLATES}> | Permissions on WhatsApp Business Account
Required |
| `user`UID | Business user ID
Required |
### Return Type
This endpoint supports read-after-write and will read the node to which you POSTed. Struct {`success`: bool, }### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
Deleting
--------
You can dissociate a WhatsAppBusinessAccount from a WhatsAppBusinessAccount by making a DELETE request to `/{whats_app_business_account_id}/assigned_users`.### Parameters

| Parameter | Description |
| --- | --- |
| `user`UID | Business user ID
Required |
### Return Type
 Struct {`success`: bool, }### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
Supported values
----------------

### Currencies

Supported values for currency codes can be found in currencies.

### Time Zones

Supported values for time zones can be found in timezone ids.