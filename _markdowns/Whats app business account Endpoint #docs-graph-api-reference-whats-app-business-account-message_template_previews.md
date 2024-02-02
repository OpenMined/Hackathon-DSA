Graph API Reference v18.0: Whats App Business Account Message Template Previews












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
On This PageWhats App Business Account Message Template PreviewsReadingRequirementsRequest SyntaxResponseSample RequestSample ResponseParametersFieldsCreatingGraph API Versionv18.0Whats App Business Account Message Template Previews
====================================================

Represents a collection of WhatsApp authentication template previews. See Authentication Templates for additional information about authentication templates.


Reading
-------

Get previews of authentication template text in various language, based on parameters include in the request.


### Requirements




| Type | Description |
| --- | --- |
| Access Tokens | User or System User |
| Permissions | whatsapp\_business\_management |

### Request Syntax



```
GET /<WHATSAPP\_BUSINESS\_ACCOUNT\_ID>/message\_template\_previews
 ?category=AUTHENTICATION,
 &language=<LANGUAGE>,
 &add\_security\_recommendation=<ADD\_SECURITY\_RECOMMENDATION>,
 &code\_expiration\_minutes=<CODE\_EXPIRATION\_MINUTES>,
 &button\_types=<BUTTON\_TYPES>
```
### Response


A list of WhatsApp Business Account Message Template Preview nodes.


### Sample Request



```
curl 'https://graph.facebook.com/v18.0/102290129340398/message\_template\_previews?category=AUTHENTICATION&languages=en\_US%2Ces\_ES&add\_security\_recommendation=true&code\_expiration\_minutes=10&button\_types=OTP' \
-H 'Authorization: Bearer EAAJB...'
```
### Sample Response



```
{
 "data": [
 {
 "body": "\*{{1}}\* is your verification code. For your security, do not share this code.",
 "buttons": [
 {
 "autofill\_text": "Autofill",
 "text": "Copy code"
 }
 ],
 "footer": "This code expires in 10 minutes.",
 "language": "en\_US"
 },
 {
 "body": "Tu código de verificación es \*{{1}}\*. Por tu seguridad, no lo compartas.",
 "buttons": [
 {
 "autofill\_text": "Autocompletar",
 "text": "Copiar código"
 }
 ],
 "footer": "Este código caduca en 10 minutos.",
 "language": "es\_ES"
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

You can't perform this operation on this endpoint.On This PageWhats App Business Account Message Template PreviewsReadingRequirementsRequest SyntaxResponseSample RequestSample ResponseParametersFieldsCreatingFollow Us* 
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