Graph API Reference v18.0: Whats App Business Account Phone Numbers












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
On This PageWhats App Business Account Phone NumbersReadingRequirementsRequest SyntaxResponseSample RequestSample ResponseSample Request with FilteringSample Response 2ParametersFieldsError CodesCreatingRequirementsSample RequestSample ResponseParametersReturn TypeError CodesUpdatingGraph API Versionv18.0Whats App Business Account Phone Numbers
========================================

Represents a collection of business phone numbers associated with a WhatsApp Business Account (WABA).



 
 To find the ID of a WhatsApp Business Account, go to **Business Manager** > **Business Settings** > **Accounts** > **WhatsApp Business Accounts**. Find the account you want to use and click on it. A panel opens, with information about the account, including the ID.
  
For more information on how to use the API, see WhatsApp Business Management API.


Reading
-------

Get a list of phone numbers associated with a WhatsApp Business Account.


### Requirements




| Type | Description |
| --- | --- |
| Access Tokens | User or System User |
| Permissions | whatsapp\_business\_management
whatsapp\_business\_messaging |

### Request Syntax



```
GET https://graph.facebook.com/<API\_VERSION>/<WABA\_ID>/phone\_numbers
```
### Response


A list of WhatsApp Business Phone Number nodes and their default fields.


### Sample Request



```
curl \
'https://graph.facebook.com/v15.0/102289599326934/phone\_numbers' \
-H 'Authorization: Bearer EAAJi...'
```
### Sample Response



```
{
 "data" : [
 {
 "code\_verification\_status" : "VERIFIED",
 "display\_phone\_number" : "+1 555-555-5555",
 "id" : "106853218861309",
 "quality\_rating" : "GREEN",
 "verified\_name" : "Jaspers Market"
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
"https://graph.facebook.com/v18.0/102289599326934/phone\_numbers \
 ?fields=id,is\_official\_business\_account,display\_phone\_number,verified\_name \
 &filtering=[{'field':'account\_mode','operator':'EQUAL','value':'SANDBOX'}]" \
-H 'Authorization: Bearer EAAJi...'
```
### Sample Response 2



```
{ 
 "id" : "106853218861309", 
 "is\_official\_business\_account" : true,
 "display\_phone\_number" : "+1 555-555-5555", 
 "verified\_name" : "Jaspers Market"
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




| Type | Description |
| --- | --- |
| Access Tokens | User or System User. |
| Permissions | whatsapp\_business\_management
whatsapp\_business\_messaging |

### Sample Request


cURLAndroid SDKObjective-C
```
curl -i -X POST \
 "https://graph.facebook.com/LATEST-VERSION/WHATSAPP-BUSINESS-ACCOUNT-ID/phone\_numbers?
 cc=COUNTRY-CODE&
 phone\_number=PHONE-NUMBER&
 migrate\_phone\_number=true&
 access\_token=USER-ACCESS-TOKEN"
```

```
GraphRequest request = GraphRequest.newPostRequest(
 accessToken,
 "/WHATSAPP-BUSINESS-ACCOUNT-ID/phone\_numbers",
 new JSONObject("{\"cc\":\"COUNTRY-CODE\",\"phone\_number\":\"PHONE-NUMBER\",\"migrate\_phone\_number\":true}"),
 new GraphRequest.Callback() {
 @Override
 public void onCompleted(GraphResponse response) {
 // Insert your code here
 }
});
request.executeAsync();
```

```
FBSDKGraphRequest \*request = [[FBSDKGraphRequest alloc]
 initWithGraphPath:@"/WHATSAPP-BUSINESS-ACCOUNT-ID/phone\_numbers"
 parameters:@{ @"cc": @"COUNTRY-CODE",@"phone\_number": @"PHONE-NUMBER",@"migrate\_phone\_number": @"true",}
 HTTPMethod:@"POST"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection \*connection, id result, NSError \*error) {
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

You can't perform this operation on this endpoint.On This PageWhats App Business Account Phone NumbersReadingRequirementsRequest SyntaxResponseSample RequestSample ResponseSample Request with FilteringSample Response 2ParametersFieldsError CodesCreatingRequirementsSample RequestSample ResponseParametersReturn TypeError CodesUpdatingFollow Us* 
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