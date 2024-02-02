Graph API Reference v19.0: Whats App Message Template - Documentation - Meta for Developers

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
Graph API Versionv19.0WhatsApp Message Template
=========================
Represents a specific message template. Make the API call to the message template ID.  
 To find a message template ID, call `https://graph.facebook.com/`v19.0`/{whatsapp-business-account-ID}/message_templates`.

For more information on how to use the API, see WhatsApp Business Management API.

Reading
-------
Retrieves information about the message template

### Example

Requirements

* whatsapp\_business\_management permission
* whatsapp\_business\_messaging permission
* public\_profile permission
* WHATSAPP MESSAGE TEMPLATE ID
* USER ACCESS TOKEN

Request

cURLAndroid SDKObjective-C
```
curl -i -X GET \
 "https://graph.facebook.com/LATEST-VERSION/WHATS-APP-MESSAGE-TEMPLATE-ID?access_token=USER-ACCESS-TOKEN"
```
```
GraphRequest request = GraphRequest.newGraphPathRequest(
  accessToken,
  "/WHATS-APP-MESSAGE-TEMPLATE-ID",
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
    initWithGraphPath:@"/WHATS-APP-MESSAGE-TEMPLATE-ID"
           parameters:nil
           HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection, id result, NSError *error) {
    // Insert your code here
}];
```
Response

```
{
  "name": "shiptest",
  "components": [
    {
      "type": "BODY",
      "text": "testing"
    }
  ],
  "language": "en_US",
  "status": "REJECTED",
  "category": "TRANSACTIONAL",
  "id": "WHATS-APP-MESSAGE-TEMPLATE-ID"
}
```
### Parameters
This endpoint doesn't have any parameters.### Fields

| Field | Description |
| --- | --- |
| `id`numeric string | ID
 |
| `category`enum | The category type of the message template
Default |
| `components`list<WhatsAppBusinessHSMWhatsAppHSMComponentGet> | An array of JSON objects describing the message template components.
Default |
| `cta_url_link_tracking_opted_out`bool | Optional boolean field for opting out/in of link tracking at template level
 |
| `language`string | The language (and locale) of the element translation
Default |
| `message_send_ttl_seconds`integer | 
Template message delivery retry time-to-live (TTL) override value. If unable to deliver the template message to the WhatsApp user, we will periodically retry for this period of time. If we are unable to deliver the message for this period of time, the message will be dropped.
Only allowed for authentication message templates. See Time-To-Live.
Default |
| `name`string | The message template name
Default |
| `previous_category`enum | Previous category of the template. See Template Categories.
Default |
| `quality_score`WhatsAppBusinessHSMWhatsAppBusinessHSMQualityScoreShape | Quality score of the HSM
 |
| `rejected_reason`enum | The reason the message template was rejected
enum {ABUSIVE\_CONTENT, INVALID\_FORMAT, NONE, PROMOTIONAL, TAG\_CONTENT\_MISMATCH, SCAM}
 |
| `status`enum | The status of the message template
enum {APPROVED, IN\_APPEAL, PENDING, REJECTED, PENDING\_DELETION, DELETED, DISABLED, PAUSED, LIMIT\_EXCEEDED}
Default |
| `sub_category`enum | Sub category of the template
Default |
### Edges

| Edge | Description |
| --- | --- |
| `compare` | compare
 |
### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 80008 | There have been too many calls to this WhatsApp Business account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |
Creating
--------
You can make a POST request to `message_templates` edge from the following paths: * `/{whats_app_business_account_id}/message_templates`
When posting to this edge, a WhatsAppMessageTemplate will be created.### Parameters

| Parameter | Description |
| --- | --- |
| `allow_category_change`boolean | Set to `true` to allow us to assign a category based on our template guidelines and the template's contents. This can prevent the template `status` from immediately being set to `REJECTED` upon creation due to miscategorization.
If omitted, template will not be auto-assigned a category and its status may be set to `REJECTED` if determined to be miscategorized.
See Template Categories.
 |
| `category`enum {UTILITY, MARKETING, AUTHENTICATION} | Template category. See Template Categories.
Required |
| `components`array<JSON object> | Array of components that make up the template. See Template Components.
For types `HEADER`, `BODY`, `FOOTER`, `text` is required.
Required |
| `type`enum {HEADER, BODY, FOOTER, BUTTONS, CAROUSEL, LIMITED\_TIME\_OFFER} | Component type.
Required |
| `format`enum {TEXT, IMAGE, DOCUMENT, VIDEO, LOCATION} | Component format.
 |
| `text`string | **Required for components with type `HEADER`,`BODY`, or `FOOTER`.**
Component text.
 |
| `buttons`array<JSON object> | Button components to be used in the template.
 |
| `type`enum {QUICK\_REPLY, URL, PHONE\_NUMBER, OTP, MPM, CATALOG, VOICE\_CALL} | Button type.
Required |
| `text`string | Button text.
 |
| `url`URI | url
 |
| `phone_number`phone number string | phone\_number
 |
| `example`array<string> | example
 |
| `flow_id`int64 | flow\_id
 |
| `zero_tap_terms_accepted`boolean | zero\_tap\_terms\_accepted
 |
| `example`JSON object | Placeholder examples. Templates will not be approved without examples.
 |
| `header_text`array<string> | header\_text
 |
| `body_text`array<array<string>> | body\_text
 |
| `header_handle`array<string> | header\_handle
 |
| `language`string | Template location and locale code.
Required |
| `name`string | Template name.
Required |
| `sub_category`enum {CUSTOM, ORDER\_DETAILS, ORDER\_STATUS} | Sub category of the template
 |
### Return Type
This endpoint supports read-after-write and will read the node to which you POSTed. Struct {`id`: numeric string, `status`: enum, `category`: enum, }### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 80008 | There have been too many calls to this WhatsApp Business account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |
| 192 | Invalid phone number |
| 200 | Permissions error |
| 200002 | HSM Template creation failed |
Updating
--------
You can update a WhatsAppMessageTemplate by making a POST request to `/{whats_app_message_template_id}`.### Parameters

| Parameter | Description |
| --- | --- |
| `category`enum {UTILITY, MARKETING, AUTHENTICATION} | category
 |
| `components`array<JSON object> | The array containing all the content of the message template
 |
| `type`enum {HEADER, BODY, FOOTER, BUTTONS, CAROUSEL, LIMITED\_TIME\_OFFER} | Component type.
Required |
| `format`enum {TEXT, IMAGE, DOCUMENT, VIDEO, LOCATION} | Component format.
 |
| `text`string | **Required for components with type `HEADER`,`BODY`, or `FOOTER`.**
Component text.
 |
| `buttons`array<JSON object> | Button components to be used in the template.
 |
| `type`enum {QUICK\_REPLY, URL, PHONE\_NUMBER, OTP, MPM, CATALOG, VOICE\_CALL} | Button type.
Required |
| `text`string | Button text.
 |
| `url`URI | url
 |
| `phone_number`phone number string | phone\_number
 |
| `flow_id`int64 | flow\_id
 |
| `zero_tap_terms_accepted`boolean | zero\_tap\_terms\_accepted
 |
| `message_send_ttl_seconds`int64 | 
Template message delivery retry time-to-live (TTL) override value. If unable to deliver the template message to the WhatsApp user, we will periodically retry for this period of time. If we are unable to deliver the message for this period of time, the message will be dropped.
Only allowed for authentication message templates. See Time-To-Live.
 |
### Return Type
This endpoint supports read-after-write and will read the node to which you POSTed. Struct {`success`: bool, }### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 80012 | There have been too many calls to this message template. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |
| 192 | Invalid phone number |
Deleting
--------
You can dissociate a WhatsAppMessageTemplate from a WhatsAppBusinessAccount by making a DELETE request to `/{whats_app_business_account_id}/message_templates`.### Parameters

| Parameter | Description |
| --- | --- |
| `hsm_id`whatsapp business hsm ID | ID of template to be deleted. Required if deleting a template by ID.
 |
| `name`string | Name of template to be deleted.
Required |
### Return Type
 Struct {`success`: bool, }### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
WhatsApp Business Platform 
 |
 Cloud API
 |
 On-Premises API
 |
 Business Management API