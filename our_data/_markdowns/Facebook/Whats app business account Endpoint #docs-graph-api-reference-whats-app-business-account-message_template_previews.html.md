Graph API Reference v19.0: Whats App Business Account Message Template Previews - Documentation - Meta for Developers

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
Graph API Versionv19.0Whats App Business Account Message Template Previews
====================================================
Represents a collection of WhatsApp authentication template previews. See Authentication Templates for additional information about authentication templates.

Reading
-------
Get previews of authentication template text in various language, based on parameters include in the request.

### Requirements

 Type | Description || Access Tokens | User or System User |
| Permissions | whatsapp\_business\_management |
### Request Syntax

```
GET /<WHATSAPP_BUSINESS_ACCOUNT_ID>/message_template_previews
  ?category=AUTHENTICATION,
  &language=<LANGUAGE>,
  &add_security_recommendation=<ADD_SECURITY_RECOMMENDATION>,
  &code_expiration_minutes=<CODE_EXPIRATION_MINUTES>,
  &button_types=<BUTTON_TYPES>
```
### Response

A list of WhatsApp Business Account Message Template Preview nodes.

### Sample Request

```
curl 'https://graph.facebook.com/v19.0/102290129340398/message_template_previews?category=AUTHENTICATION&languages=en_US%2Ces_ES&add_security_recommendation=true&code_expiration_minutes=10&button_types=OTP' \
-H 'Authorization: Bearer EAAJB...'
```
### Sample Response

```
{
  "data": [
    {
      "body": "*{{1}}* is your verification code. For your security, do not share this code.",
      "buttons": [
        {
          "autofill_text": "Autofill",
          "text": "Copy code"
        }
      ],
      "footer": "This code expires in 10 minutes.",
      "language": "en_US"
    },
    {
      "body": "Tu código de verificación es *{{1}}*. Por tu seguridad, no lo compartas.",
      "buttons": [
        {
          "autofill_text": "Autocompletar",
          "text": "Copiar código"
        }
      ],
      "footer": "Este código caduca en 10 minutos.",
      "language": "es_ES"
    }
  ]
}
```
### Parameters

| Parameter | Description |
| --- | --- |
| `add_security_recommendation`boolean | Default value: `false`
Set to `true` if you want the security recommendation body string included in the response.
If omitted, the security recommendation string will not be included.
 |
| `button_types`array<enum {OTP}> | Default value: `[]`
Comma-separated list of strings indicating button type.
If included, the response will include the button text for each button in the response.
For authentication templates, this value must be `OTP`.
 |
| `category`enum {AUTHENTICATION} | The category of the message template. Set to `AUTHENTICATION` for authentication templates.
Required |
| `code_expiration_minutes`int64 | For authentication templates, set to an integer if you want the code expiration footer string included in the response.
If omitted, the code expiration footer string will not be included.
Value indicates number of minutes until code expires.
Minimum `1`, maximum `90`.
 |
| `languages`array<string> | Default value: `["af","sq","ar","az","bn","bg","ca","zh_CN","zh_HK","zh_TW","hr","cs","da","nl","en","en_GB","en_US","et","fil","fi","fr","ka","de","el","gu","ha","he","hi","hu","id","ga","it","ja","kn","kk","ko","ky_KG","lo","lv","lt","mk","ml","ms","mr","nb","fa","pl","pt_BR","pt_PT","pa","ro","ru","rw_RW","sr","sk","sl","es","es_AR","es_ES","es_MX","sw","sv","ta","te","th","tr","uk","ur","uz","vi","zu"]`
Comma-separated list of language and locale codes of language versions you want returned.
If omitted, versions of all supported languages will be returned.
 |
### Fields
Reading from this edge will return a JSON formatted result:

```
{
 "`data`": [],
 "`paging`": {}
}

```
#### `data`
A list of WhatsAppBusinessAccountMessageTemplatePreview nodes.#### `paging`
For more details about pagination, see the Graph API guide.Creating
--------
You can't perform this operation on this endpoint.Updating
--------
You can't perform this operation on this endpoint.Deleting
--------
You can't perform this operation on this endpoint.