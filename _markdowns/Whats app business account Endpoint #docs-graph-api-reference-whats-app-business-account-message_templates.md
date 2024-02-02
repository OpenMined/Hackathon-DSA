Graph API Reference v18.0: Whats App Business Account Message Templates












DocsToolsSupportLog InGraph API* Overview
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
	+ Ads Archive
	+ Album
	+ App Link Host
	+ Application
	+ Branded Content Search
	+ CPASAdvertiser Partnership Recommendation
	+ Canvas
	+ Canvas Button
	+ Canvas Carousel
	+ Canvas Footer
	+ Canvas Header
	+ Canvas Photo
	+ Canvas Product List
	+ Canvas Product Set
	+ Canvas Text
	+ Canvas Video
	+ Collaborative Ads Directory
	+ Comment
	+ Commerce Merchant Settings
	+ Conversation
	+ Debug Token
	+ Event
	+ Games IAPProduct
	+ Group
	+ Group Doc
	+ Group Message
	+ Image Copyright
	+ Instagram Oembed
	+ Link
	+ Live Video
	+ Live Video Input Stream
	+ Mailing Address
	+ Media Fingerprint
	+ Message
	+ Milestone
	+ Object Comments
	+ Object Likes
	+ Object Private Replies
	+ Object Reactions
	+ Object Sharedposts
	+ Oembed Page
	+ Oembed Post
	+ Oembed Video
	+ Offline Conversion Data Set Upload
	+ Page
	+ Page Call To Action
	+ Page Post
	+ Page Upcoming Change
	+ Page/insights
	+ Payment
	+ Photo
	+ Place
	+ Place Tag
	+ Place Topic
	+ Post
	+ Profile
	+ Request
	+ Test User
	+ Thread
	+ URL
	+ User
	+ Video
	+ Video Copyright
	+ Video List
	+ Video Poll
	+ Video Poll Option
	+ Whats App Business Account
		- Assigned Users
		- Conversation Analytics
		- Dcc Config
		- Message Template Previews
		- Message Templates
		- Phone Numbers
		- Product Catalogs
		- Subscribed Apps
		- Template Performance Metrics
		- Upsert Message Templates
	+ Whats App Message Template
On This PageWhats App Business Account Message TemplatesReadingRequirementsRequest SyntaxPath ParametersResponseSample RequestSample ResponseParametersFieldsError CodesCreatingRequirementsRequest SyntaxPath ParametersPost BodyResponseSample RequestSample ResponseParametersReturn TypeError CodesUpdatingDeletingRequirementsRequest SyntaxPath ParametersResponseSample RequestSample ResponseParametersReturn TypeError CodesGraph API Versionv18.0Whats App Business Account Message Templates
============================================

Represents a collection of templates on a WhatsApp Business Account. See Templates.


Reading
-------

Get a list of templates on a WhatsApp Business Account.


### Requirements




| Type | Description |
| --- | --- |
| Access Tokens | User or System User |
| Permissions | whatsapp\_business\_management |

### Request Syntax



```
GET /<WHATSAPP\_BUSINESS\_ACCOUNT\_ID>/message\_templates
 ?category=<CATEGORY>,
 &content=<CONTENT>,
 &language=<LANGUAGE>,
 &name=<NAME>,
 &name\_or\_content=<NAME\_OR\_CONTENT>,
 &quality\_score=<QUALITY\_SCORE>,
 &status=<STATUS>
```
### Path Parameters




| Placeholder | Value |
| --- | --- |
| `<WHATSAPP_BUSINESS_ACCOUNT_ID>` | WhatsApp Business Account ID. |

### Response


A list of WhatsApp Message Template nodes.


### Sample Request



```
curl 'https://graph.facebook.com/v16.0/102290129340398/message\_templates?category=utility' \
-H 'Authorization: Bearer EAAJB...'
```
### Sample Response



```
{
 "data": [
 {
 "name": "order\_delivery\_update",
 "components": [
 {
 "type": "HEADER",
 "format": "LOCATION"
 },
 {
 "type": "BODY",
 "text": "Good news {{1}}! Your order #{{2}} is on its way to the location above. Thank you for your order!",
 "example": {
 "body\_text": [
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
 "type": "QUICK\_REPLY",
 "text": "Stop Delivery Updates"
 }
 ]
 }
 ],
 "language": "en\_US",
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




| Type | Description |
| --- | --- |
| Access Tokens | User or System User |
| Permissions | whatsapp\_business\_management |

### Request Syntax



```
POST /<WHATSAPP\_BUSINESS\_ACCOUNT\_ID>/message\_templates
```
### Path Parameters




| Placeholder | Value |
| --- | --- |
| `<WHATSAPP_BUSINESS_ACCOUNT_ID>` | ID of the WhatsApp Business Account to create the template on. |

### Post Body


See Parameters for property descriptions.



```
{
 "allow\_category\_change": <ALLOW\_CATEGORY\_CHANGE>,
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
curl 'https://graph.facebook.com/v18.0/102290129340398/message\_templates' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer EAAJB...' \
-d '
{
 "name": "seasonal\_promotion",
 "language": "en",
 "category": "MARKETING",
 "components": [
 {
 "type": "HEADER",
 "format": "TEXT",
 "text": "Our {{1}} is on!",
 "example": {
 "header\_text": [
 "Summer Sale"
 ]
 }
 },
 {
 "type": "BODY",
 "text": "Shop now through {{1}} and use code {{2}} to get {{3}} off of all merchandise.",
 "example": {
 "body\_text": [
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
 "type": "QUICK\_REPLY",
 "text": "Unsubcribe from Promos"
 },
 {
 "type":"QUICK\_REPLY",
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




| Type | Description |
| --- | --- |
| Access Tokens | User or System User |
| Permissions | whatsapp\_business\_management |

### Request Syntax



```
DELETE /<WHATSAPP\_BUSINESS\_ACCOUNT\_ID>/message\_templates
```
### Path Parameters




| Placeholder | Value |
| --- | --- |
| `<WHATSAPP_BUSINESS_ACCOUNT_ID>` | ID of the WhatsApp Business Account that owns the template. |

### Response


See Return Type.


### Sample Request



```
curl -X DELETE 'https://graph.facebook.com/v18.0/102290129340398/message\_templates?name=order\_confirmation' \
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
 Business Management APIOn This PageWhats App Business Account Message TemplatesReadingRequirementsRequest SyntaxPath ParametersResponseSample RequestSample ResponseParametersFieldsError CodesCreatingRequirementsRequest SyntaxPath ParametersPost BodyResponseSample RequestSample ResponseParametersReturn TypeError CodesUpdatingDeletingRequirementsRequest SyntaxPath ParametersResponseSample RequestSample ResponseParametersReturn TypeError CodesFollow Us* 
#### Products

* Artificial Intelligence
* AR/VR
* Business Tools
* Gaming
* Open Source
* Publishing
* Social Integrations
* Social Presence
#### Programs

* ThreatExchange
#### Support

* Developer Support
* Bugs
* Platform Status
* Report a Platform Data Incident
* Facebook for Developers Community Group
* Sitemap
#### News

* Blog
* Success Stories
* Videos
* Meta for Developers Page
#### Terms and Policies

* Platform Initiatives Hub
* Platform Terms
* Developer Policies
* European Commission Commitments
Follow Us* 
 © 2024 Meta * About
* Create Ad
* Careers
* Privacy Policy
* Cookies
* Terms
English (US)Bahasa IndonesiaDeutschEspañolEspañol (España)Français (France)ItalianoPortuguês (Brasil)Tiếng ViệtРусскийالعربيةภาษาไทย한국어中文(香港)中文(台灣)中文(简体)日本語English (US)




































Allow the use of cookies from Facebook on this browser?We use cookies and similar technologies to help:Provide and improve content on Meta ProductsProvide a safer experience by using information we receive from cookies on and off FacebookProvide and improve Meta Products for people who have an accountFor advertising and measurement services off of Meta Products, analytics, and to provide certain features and improve our services for you, we use tools from other companies on Facebook. These companies also use cookies.You can allow the use of all cookies, just essential cookies or you can choose more options below. You can learn more about cookies and how we use them, and review or change your choice at any time in our Cookie Policy.Essential cookiesThese cookies are required to use Meta Products. They’re necessary for these sites to work as intended.Optional cookies

Cookies from other companiesWe use tools from other companies for advertising and measurement services off of Meta Products, analytics, and to provide certain features and improve our services for you. These companies also use cookies.More informationIf you allow these cookies:

* We’ll be able to better personalize ads for you off of Meta Products, and measure their performance
* Features on our products will not be affected
* Other companies will receive information about you by using cookies

If you don’t allow these cookies:

* We won’t use cookies from other companies to help personalize ads for you off of Meta Products, or to measure their performance
* Some features on our products may not work

Other ways you can control your information

Manage your ad experience in Accounts CenterIf you have a Facebook account, you can manage how different data is used to personalize ads with these tools.

Ad settings

To show you better ads, we use data that advertisers and other partners provide us about your activity off Meta Company Products, including websites and apps. You can control whether we use this data to show you ads in your ad settings.

The Meta Audience Network is a way for advertisers to show you ads in apps and websites off the Meta Company Products. One of the ways Audience Network shows relevant ads is by using your ad preferences to determine which ads you may be interested in seeing. You can control this in your ad settings.

Ad preferences

In Ad preferences, you can choose whether we show you ads and make choices about the information used to show you ads.

Off-Facebook activity

You can review your off-Facebook activity, which is a summary of activity that businesses and organizations share with us about your interactions with them, such as visiting their apps or websites. They use our Business Tools, such as Facebook Login or Meta Pixel, to share this information with us. This helps us do things such as give you a more personalized experience on Meta Products. Learn more about off-Facebook activity, how we use it, and how you can manage it.

More information about online advertisingYou can opt out of seeing online interest-based ads from Meta and other participating companies through the Digital Advertising Alliance in the US, the Digital Advertising Alliance of Canada in Canada or the European Interactive Digital Advertising Alliance in Europe, or through your mobile device settings, if you are using Android, iOS 13 or an earlier version of iOS. Please note that ad blockers and tools that restrict our cookie use may interfere with these controls.

The advertising companies we work with generally use cookies and similar technologies as part of their services. To learn more about how advertisers generally use cookies and the choices they offer, you can review the following resources:

* Digital Advertising Alliance
* Digital Advertising Alliance of Canada
* European Interactive Digital Advertising Alliance
Controlling cookies with browser settingsYour browser or device may offer settings that allow you to choose whether browser cookies are set and to delete them. These controls vary by browser, and manufacturers may change both the settings they make available and how they work at any time. As of 5 October 2020, you may find additional information about the controls offered by popular browsers at the links below. Certain parts of Meta Products may not work properly if you have disabled browser cookies. Please be aware that these controls are distinct from the controls that Facebook offers.

* Google Chrome
* Internet Explorer
* Firefox
* Safari
* Safari Mobile
* Opera
Only allow essential cookiesAllow essential and optional cookies