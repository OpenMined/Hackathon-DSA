Graph API Reference v19.0: Whats App Business Account Message Templates - Documentation - Meta for Developers

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
Graph API Versionv19.0Whats App Business Account Message Templates
============================================
Represents a collection of templates on a WhatsApp Business Account. See Templates.

Reading
-------
Get a list of templates on a WhatsApp Business Account.

### Requirements

 Type | Description || Access Tokens | User or System User |
| Permissions | whatsapp\_business\_management |
### Request Syntax

```
GET /<WHATSAPP_BUSINESS_ACCOUNT_ID>/message_templates
  ?category=<CATEGORY>,
  &content=<CONTENT>,
  &language=<LANGUAGE>,
  &name=<NAME>,
  &name_or_content=<NAME_OR_CONTENT>,
  &quality_score=<QUALITY_SCORE>,
  &status=<STATUS>
```
### Path Parameters

 Placeholder | Value || `<WHATSAPP_BUSINESS_ACCOUNT_ID>` | WhatsApp Business Account ID. |
### Response

A list of WhatsApp Message Template nodes.

### Sample Request

```
curl 'https://graph.facebook.com/v16.0/102290129340398/message_templates?category=utility' \
-H 'Authorization: Bearer EAAJB...'
```
### Sample Response

```
{
  "data": [
    {
      "name": "order_delivery_update",
      "components": [
        {
          "type": "HEADER",
          "format": "LOCATION"
        },
        {
          "type": "BODY",
          "text": "Good news {{1}}! Your order #{{2}} is on its way to the location above. Thank you for your order!",
          "example": {
            "body_text": [
              [
                "Mark",
                "566701"
              ]
            ]
          }
        },
        {
          "type": "FOOTER",
          "text": "To stop receiving delivery updates, tap the button below."
        },
        {
          "type": "BUTTONS",
          "buttons": [
            {
              "type": "QUICK_REPLY",
              "text": "Stop Delivery Updates"
            }
          ]
        }
      ],
      "language": "en_US",
      "status": "APPROVED",
      "category": "UTILITY",
      "id": "1667192013751005"
    },
    ...
  ],
  "paging": {
    "cursors": {
      "before": "MAZDZD",
      "after": "MjQZD"
    }
  }
}
```
### Parameters

| Parameter | Description |
| --- | --- |
| `category`array<enum {ACCOUNT\_UPDATE, PAYMENT\_UPDATE, PERSONAL\_FINANCE\_UPDATE, SHIPPING\_UPDATE, RESERVATION\_UPDATE, ISSUE\_RESOLUTION, APPOINTMENT\_UPDATE, TRANSPORTATION\_UPDATE, TICKET\_UPDATE, ALERT\_UPDATE, AUTO\_REPLY, TRANSACTIONAL, OTP, UTILITY, MARKETING, AUTHENTICATION}> | The category for a template
 |
| `content`string | The content for a template
 |
| `language`array<string> | A list of supported languages that are available for each template
 |
| `name`string | The name for a message template
 |
| `name_or_content`string | Returns a list of message templates where the value for `name` or `content` match this value
 |
| `quality_score`array<enum {GREEN, YELLOW, RED, UNKNOWN}> | The quality score for a template
 |
| `status`array<enum {APPROVED, IN\_APPEAL, PENDING, REJECTED, PENDING\_DELETION, DELETED, DISABLED, PAUSED, LIMIT\_EXCEEDED}> | The review status for a template
 |
### Fields
Reading from this edge will return a JSON formatted result:

```
{
 "`data`": [],
 "`paging`": {},
 "`summary`": {}
}

```
#### `data`
A list of WhatsAppBusinessHSM nodes.#### `paging`
For more details about pagination, see the Graph API guide.#### `summary`
Aggregated information about the edge, such as counts. Specify the fields to fetch in the summary param (like `summary=total_count`).

| Field | Description |
| --- | --- |
| `total_count`unsigned int32 | The total number of message templates that belong to a WhatsApp Business Account
 |
| `message_template_count`int32 | The current number of message templates that belong to the WhatsApp Business Account
 |
| `message_template_limit`int32 | The maximum number of message templates that can belong to a WhatsApp Business Account
 |
| `are_translations_complete`bool | The status for template translations
 |
### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 80008 | There have been too many calls to this WhatsApp Business account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |
Creating
--------
You can make a POST request to `message_templates` edge from the following paths: * `/{whats_app_business_account_id}/message_templates`
When posting to this edge, a WhatsAppMessageTemplate will be created.### Requirements

 Type | Description || Access Tokens | User or System User |
| Permissions | whatsapp\_business\_management |
### Request Syntax

```
POST /<WHATSAPP_BUSINESS_ACCOUNT_ID>/message_templates
```
### Path Parameters

 Placeholder | Value || `<WHATSAPP_BUSINESS_ACCOUNT_ID>` | ID of the WhatsApp Business Account to create the template on. |
### Post Body

See Parameters for property descriptions.

```
{
  "allow_category_change": <ALLOW_CATEGORY_CHANGE>,
  "name": "<NAME>",
  "language": "<LANGUAGE>",
  "category": "<CATEGORY>",
  "components": [<COMPONENTS>]
}
```
### Response

See Return Type.

### Sample Request

```
curl 'https://graph.facebook.com/v19.0/102290129340398/message_templates' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer EAAJB...' \
-d '
{
  "name": "seasonal_promotion",
  "language": "en",
  "category": "MARKETING",
  "components": [
    {
      "type": "HEADER",
      "format": "TEXT",
      "text": "Our {{1}} is on!",
      "example": {
        "header_text": [
          "Summer Sale"
        ]
      }
    },
    {
      "type": "BODY",
      "text": "Shop now through {{1}} and use code {{2}} to get {{3}} off of all merchandise.",
      "example": {
        "body_text": [
          [
            "the end of August","25OFF","25%"
          ]
        ]
      }
    },
    {
      "type": "FOOTER",
      "text": "Use the buttons below to manage your marketing subscriptions"
    },
    {
      "type":"BUTTONS",
      "buttons": [
        {
          "type": "QUICK_REPLY",
          "text": "Unsubcribe from Promos"
        },
        {
          "type":"QUICK_REPLY",
          "text": "Unsubscribe from All"
        }
      ]
    }
  ]
}'
```
### Sample Response

```
{
    "id": "594425479261596",
    "status": "PENDING",
    "category": "MARKETING"
}
```
### Parameters

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
You can't perform this operation on this endpoint.Deleting
--------
You can dissociate a WhatsAppMessageTemplate from a WhatsAppBusinessAccount by making a DELETE request to `/{whats_app_business_account_id}/message_templates`.### Requirements

 Type | Description || Access Tokens | User or System User |
| Permissions | whatsapp\_business\_management |
### Request Syntax

```
DELETE /<WHATSAPP_BUSINESS_ACCOUNT_ID>/message_templates
```
### Path Parameters

 Placeholder | Value || `<WHATSAPP_BUSINESS_ACCOUNT_ID>` | ID of the WhatsApp Business Account that owns the template. |
### Response

See Return Type.

### Sample Request

```
curl -X DELETE 'https://graph.facebook.com/v19.0/102290129340398/message_templates?name=order_confirmation' \
-H 'Authorization: Bearer EAAJB...'
```
### Sample Response

```
{
  "success": true
}
```
### Parameters

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