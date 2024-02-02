Graph API Reference v18.0: User Ad Studies












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
		- Accounts
		- Ad Studies
		- Albums
		- Apprequestformerrecipients
		- Apprequests
		- Assigned Business Asset Groups
		- Assigned Pages
		- Assigned Product Catalogs
		- Business Users
		- Businesses
		- /user/checkins
		- Custom Labels
		- /user/family
		- Feed
		- /user/friends
		- Ids For Apps
		- Ids For Business
		- Ids For Pages
		- Likes
		- Live Videos
		- Music
		- Notifications
		- User Outbox
		- /user/payment\_transactions
		- Permissions
		- Photos
		- Picture
		- User Posts
		- /user/questions
		- Rich Media Documents
		- /user/scores
		- /user/subscribedto
		- /user/subscribers
		- Videos
	+ Video
	+ Video Copyright
	+ Video List
	+ Video Poll
	+ Video Poll Option
	+ Whats App Business Account
	+ Whats App Message Template
On This PageUser Ad StudiesReadingExampleParametersFieldsError CodesCreatingParametersReturn TypeError CodesUpdatingGraph API Versionv18.0User Ad Studies
===============

Reading
-------

UserAdStudies


### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v18.0/{user-id}/ad\_studies HTTP/1.1
Host: graph.facebook.com
```

```
/\* PHP SDK v5.0.0 \*/
/\* make the API call \*/
try {
 // Returns a `Facebook\FacebookResponse` object
 $response = $fb->get(
 '/{user-id}/ad\_studies',
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
 "/{user-id}/ad\_studies",
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
 "/{user-id}/ad\_studies",
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
 initWithGraphPath:@"/{user-id}/ad\_studies"
 parameters:params
 HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection \*connection,
 id result,
 NSError \*error) {
 // Handle the result
}];
```
If you want to learn how to use the Graph API, read our Using Graph API guide.### Parameters

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

A list of AdStudy nodes.#### `paging`

For more details about pagination, see the Graph API guide.#### `summary`

Aggregated information about the edge, such as counts. Specify the fields to fetch in the summary param (like `summary=total_count`).



| Field | Description |
| --- | --- |
| `total_count`unsigned int32 | Total number of lift studies for this person
 |

### Error Codes



| Error | Description |
| --- | --- |
| 270 | This Ads API request is not allowed for apps with development access level (Development access is by default for all apps, please request for upgrade). Make sure that the access token belongs to a user that is both admin of the app and admin of the ad account |
| 100 | Invalid parameter |

Creating
--------

You can make a POST request to `ad_studies` edge from the following paths: * `/{user_id}/ad_studies`

When posting to this edge, an AdStudy will be created.### Parameters



| Parameter | Description |
| --- | --- |
| `cells`list<Object> | A shape to describe the cells of the study
 |
| `description`string |  |
| `id`int64 |  |
| `name`string |  |
| `creation_template`enum {AUTOMATIC\_PLACEMENTS, BRAND\_AWARENESS, FACEBOOK, FACEBOOK\_AUDIENCE\_NETWORK, FACEBOOK\_INSTAGRAM, FACEBOOK\_NEWS\_FEED, FACEBOOK\_NEWS\_FEED\_IN\_STREAM\_VIDEO, IN\_STREAM\_VIDEO, INSTAGRAM, MOBILE\_OPTIMIZED\_VIDEO, PAGE\_POST\_ENGAGEMENT, REACH, TV\_COMMERCIAL, TV\_FACEBOOK, VIDEO\_VIEW\_OPTIMIZATION, LOW\_FREQUENCY, MEDIUM\_FREQUENCY, HIGH\_FREQUENCY} |  |
| `adaccounts`list<int64> |  |
| `adsets`list<numeric string or integer> |  |
| `campaigns`list<numeric string or integer> |  |
| `control_percentage`float with at most two digits after decimal point |  |
| `treatment_percentage`float with at most two digits after decimal point |  |
| `client_business`numeric string or integer | Business associated with study
 |
| `confidence_level`float | Confidence level used in power calculation and final report
 |
| `cooldown_start_time`integer | The beginning of the pre measurement cooldown period. This period ends when the study period starts.
 |
| `description`string | A brief description about the purpose of the study.
 |
| `end_time`integer | The time when the study period ends.
 |
| `name`string | The name of the study.
 |
| `objectives`list<Object> | A vector of objects describing the objectives assigned to this study
 |
| `id`numeric string or integer |  |
| `is_primary`boolean |  |
| `name`string |  |
| `type`enum {SALES, NONSALES, MAE, TELCO, FTL, MAI, PARTNER, BRANDLIFT, BRAND, MPC\_CONVERSION, CONVERSIONS} |  |
| `offsite_datasets`list<JSON or object-like arrays> |  |
| `id`numeric string or integer | Required |
| `event_names`list<string> |  |
| `adspixels`list<JSON or object-like arrays> |  |
| `id`numeric string or integer | Required |
| `event_names`list<string> |  |
| `customconversions`list<JSON or object-like arrays> |  |
| `id`numeric string or integer | Required |
| `event_names`list<string> |  |
| `applications`list<JSON or object-like arrays> |  |
| `id`numeric string or integer | Required |
| `event_names`list<string> |  |
| `offline_conversion_data_sets`list<JSON or object-like arrays> |  |
| `id`numeric string or integer | Required |
| `event_names`list<string> |  |
| `product_sets`list<JSON or object-like arrays> |  |
| `id`numeric string or integer | Required |
| `event_names`list<string> |  |
| `product_catalogs`list<JSON or object-like arrays> |  |
| `id`numeric string or integer | Required |
| `event_names`list<string> |  |
| `observation_end_time`integer | The end of the observation period for this study, this period starts when the study period ends.
 |
| `start_time`integer | The time when the study period starts.
 |
| `type`enum {LIFT, SPLIT\_TEST, CONTINUOUS\_LIFT\_CONFIG, GEO\_LIFT} | The type of ad study, either SPLIT\_TEST or LIFT.
 |
| `viewers`list<int> | The list of people who this study has been shared with.
 |

### Return Type

This endpoint supports read-after-write and will read the node represented by `id` in the return type. Struct {`id`: numeric string, `cell_ids`: List [numeric string], `objective_ids`: List [numeric string], }### Error Codes



| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |

Updating
--------

You can't perform this operation on this endpoint.Deleting
--------

You can't perform this operation on this endpoint.On This PageUser Ad StudiesReadingExampleParametersFieldsError CodesCreatingParametersReturn TypeError CodesUpdatingFollow Us* 
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