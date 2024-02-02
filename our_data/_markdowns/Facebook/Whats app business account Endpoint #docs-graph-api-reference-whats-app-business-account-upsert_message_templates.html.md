Graph API Reference v19.0: Whats App Business Account Upsert Message Templates - Documentation - Meta for Developers

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
Graph API Versionv19.0Whats App Business Account Upsert Message Templates
===================================================
Reading
-------
You can't perform this operation on this endpoint.Creating
--------
You can make a POST request to `upsert_message_templates` edge from the following paths: * `/{whats_app_business_account_id}/upsert_message_templates`
When posting to this edge, no Graph object will be created.### Parameters

| Parameter | Description |
| --- | --- |
| `category`enum {AUTHENTICATION} | Template category. See Template Categories.
Required |
| `components`array<JSON object> | Array of components that make up the template. See Template Components.
Required |
| `type`enum {HEADER, BODY, FOOTER, BUTTONS, CAROUSEL, LIMITED\_TIME\_OFFER} | type
Required |
| `add_security_recommendation`boolean | Set to true if you want the template to include the string, For your security, do not share this code. Set to false to exclude the string.
 |
| `code_expiration_minutes`int64 | Indicates number of minutes the password or code is valid.
If omitted, the code expiration warning will not be displayed in the delivered message.
Minimum 1, maximum 90.
 |
| `buttons`array<JSON object> | Button components to be used in the template.
 |
| `type`enum {OTP} | type
Required |
| `otp_type`enum {COPY\_CODE, ONE\_TAP, ZERO\_TAP} | Indicates button type. Set to COPY\_CODE if you want the template to use a copy code button, or ONE\_TAP to have it use a one-tap autofill button.
 |
| `package_name`string | One-tap buttons only.
Your Android app's package name.
 |
| `signature_hash`string | One-tap buttons only.
Your app signing key hash.
 |
| `languages`array<string> | array of Template location and locale code.
Required |
| `name`string | Template name.
Required |
### Return Type
This endpoint supports read-after-write and will read the node to which you POSTed. Struct {`data`: List [ Struct {`id`: numeric string, `status`: enum, `language`: string, }], }Updating
--------
You can't perform this operation on this endpoint.Deleting
--------
You can't perform this operation on this endpoint.