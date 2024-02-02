Graph API Reference v18.0: Whats App Business Account












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
On This PageWhatsApp Business AccountReadingExampleParametersFieldsEdgesError CodesCreatingUpdatingParametersReturn TypeError CodesDeletingParametersReturn TypeError CodesSupported valuesCurrenciesTime ZonesGraph API Versionv18.0WhatsApp Business Account
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
 "https://graph.facebook.com/LATEST-VERSION/WHATSAPP-BUSINESS-ACCOUNT-ID?access\_token=USER-ACCESS-TOKEN"
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
FBSDKGraphRequest \*request = [[FBSDKGraphRequest alloc]
 initWithGraphPath:@"/WHATSAPP-BUSINESS-ACCOUNT-ID"
 parameters:nil
 HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection \*connection, id result, NSError \*error) {
 // Insert your code here
}];
```
Response



```
{
 "id": "WHATSAPP-BUSINESS-ACCOUNT-ID",
 "name": "Test WhatsApp Business Account",
 "timezone\_id": "1",
 "message\_template\_namespace": "MESSAGE-TEMPLATE-NAMESPACE"
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


On This PageWhatsApp Business AccountReadingExampleParametersFieldsEdgesError CodesCreatingUpdatingParametersReturn TypeError CodesDeletingParametersReturn TypeError CodesSupported valuesCurrenciesTime ZonesFollow Us* 
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