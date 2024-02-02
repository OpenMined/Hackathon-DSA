Graph API Reference v18.0: Application Accounts












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
		- Accounts
		- Application Achievements
		- Activities
		- Ad Placement Groups
		- Adnetworkanalytics Results
		- Aem Attribution
		- Aem Conversion Configs
		- Aem Conversion Filter
		- Agencies
		- App Event Types
		- App Indexing
		- App Installed Groups
		- Appassets
		- Assets
		- Button Auto Detection Device Selection
		- Cloudbridge Settings
		- Codeless Event Mappings
		- Da Checks
		- Events
		- Page/insights
		- Ios Skadnetwork Conversion Config
		- Mmp Auditing
		- Mobile Sdk Gk
		- Model Asset
		- Monetized Digital Store Objects
		- Object Types
		- Objects
		- Page Activities
		- Payment Currencies
		- Permissions
		- Picture
		- Products
		- Purchases
		- Roles
		- Scores
		- Static Resources
		- Subscribed Domains
		- Subscribed Domains Phishing
		- Subscriptions
		- Translations
		- Uploads
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
	+ Whats App Message Template
On This PageApplication AccountsReadingRequirementsExampleParametersFieldsError CodesCreatingRequirementsParametersReturn TypeError CodesUpdatingDeletingRequirementsLimitationsParametersReturn TypeError CodesGraph API Versionv18.0Application Accounts
====================

Represents a collection of test users on an app.


Reading
-------

Get a list of test users on an app.


### Requirements




| Type | Requirement |
| --- | --- |
| Access Tokens | App |
| Permissions | None |

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v18.0/{application-id}/accounts HTTP/1.1
Host: graph.facebook.com
```

```
/\* PHP SDK v5.0.0 \*/
/\* make the API call \*/
try {
 // Returns a `Facebook\FacebookResponse` object
 $response = $fb->get(
 '/{application-id}/accounts',
 '{access-token}'
 );
} catch(Facebook\Exceptions\FacebookResponseException $e) {
 echo 'Graph returned an error: ' . $e->getMessage();
 exit;
} catch(Facebook\Exceptions\FacebookSDKException $e) {
 echo 'Facebook SDK returned an error: ' . $e->getMessage();
 exit;
}
$graphNode = $response->getGraphNode();
/\* handle the result \*/
```

```
/\* make the API call \*/
FB.api(
 "/{application-id}/accounts",
 function (response) {
 if (response && !response.error) {
 /\* handle the result \*/
 }
 }
);
```

```
/\* make the API call \*/
new GraphRequest(
 AccessToken.getCurrentAccessToken(),
 "/{application-id}/accounts",
 null,
 HttpMethod.GET,
 new GraphRequest.Callback() {
 public void onCompleted(GraphResponse response) {
 /\* handle the result \*/
 }
 }
).executeAsync();
```

```
/\* make the API call \*/
FBSDKGraphRequest \*request = [[FBSDKGraphRequest alloc]
 initWithGraphPath:@"/{application-id}/accounts"
 parameters:params
 HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection \*connection,
 id result,
 NSError \*error) {
 // Handle the result
}];
```
If you want to learn how to use the Graph API, read our Using Graph API guide.### Parameters



| Parameter | Description |
| --- | --- |
| `type`enum{test-users} | The type of user requested
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

A list of TestAccount nodes.The following fields will be added to each node that is returned:



| Field | Description |
| --- | --- |
| `access_token`string | An access token that can be used to make API calls on behalf of this user
Default |

#### `paging`

For more details about pagination, see the Graph API guide.### Error Codes



| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |

Creating
--------

You can make a POST request to `accounts` edge from the following paths: * `/{application_id}/accounts`

When posting to this edge, a TestAccount will be created.  
Upon successful creation, a `login_url` and `access_token` will be returned. You can use the login URL to log in as the test user. Login URLs expire once they are used, or after one hour if they are unused. An access token will only be returned if the `installed` parameter was set to `true` at the time of the query.


You can also use this edge to associate an existing test user with a different app by using the `owner_acces_token` parameter.


### Requirements




| Type | Requirement |
| --- | --- |
| Access Tokens | App |
| Permissions | None |

### Parameters



| Parameter | Description |
| --- | --- |
| `installed`boolean | Automatically installs the app for the test user once it is created or associated
 |
| `minor`boolean | Is this test user a minor
 |
| `name`string | The name for the test user. When left blank, a random name will be automatically generated
 |
| `owner_access_token`string | When associating existing test users with other apps, this is the app access token of any app that is already associated with the test user. The `{app-id}` in the publishing request in this case should be the app that will is the target to associate with the test user. The API request should also be signed with the app access token of that target app. Required when associating test users, but should not be used when creating new test users
 |
| `permissions`List<Permission> | Default value: `Set`List of permissions that are automatically granted for the app when it is created or associated
 |
| `type`enum{test-users} | Type
 |
| `uid`int | ID of an existing test user to associate with another app. Required when associating test users, but should not be used when creating new test users
 |

### Return Type

This endpoint supports read-after-write and will read the node represented by `id` in the return type. Struct {`id`: numeric string, `access_token`: string, `login_url`: string, `email`: string, `password`: string, }### Error Codes



| Error | Description |
| --- | --- |
| 2900 | Too many test accounts |

Updating
--------

You can't perform this operation on this endpoint.Deleting
--------

You can dissociate a TestAccount from an Application by making a DELETE request to `/{application_id}/accounts`.### Requirements




| Type | Requirement |
| --- | --- |
| Access Tokens | App |
| Permissions | None |

### Limitations


At least one test user must be associated with an app. Attempting to perform this operation on an app's sole test user will result in error code `2902`.


### Parameters



| Parameter | Description |
| --- | --- |
| `type`enum {TEST\_USERS} | Account type
 |
| `uid`UID | Account UID
Required |

### Return Type

 Struct {`success`: bool, }### Error Codes



| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 2902 | Cannot remove test account from this app |

On This PageApplication AccountsReadingRequirementsExampleParametersFieldsError CodesCreatingRequirementsParametersReturn TypeError CodesUpdatingDeletingRequirementsLimitationsParametersReturn TypeError CodesFollow Us* 
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