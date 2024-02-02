Object Likes - Graph API













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
	+ Whats App Message Template
On This Page/{object-id}/likesReadingNew Page ExperienceRequirementsLimitationsFieldsExample UsagePublishNew Page ExperiencePermissionsLimitationsFieldsResponseUpdatingDeletePermissionsLimitationsFieldsResponseGraph API Versionv18.0`/{object-id}/likes`
====================

This reference describes the `/likes` edge that is common to multiple Graph API nodes. The structure and operations are the same for each node. The following objects have a `/likes` edge:




|  |  |
| --- | --- |
| * Album
* Comment
* Page
* Photo
* User
* Video
 |  |

Reading
-------


Returns the list of people who liked this object. When reading likes on a Page or User object, this endpoint returns a list of pages liked by that Page or User.


Use the `likes` field of an object to get the number of likes.


We recommended that you use the `/object/reactions` endpoint to get like counts, if available.


### New Page Experience


The following objects `/likes` endpoint are supported for New Page Experience:




|  |  |
| --- | --- |
| * Album
* Comment
* Photo
* PagePost
 | * User
 |

### Requirements

* The same requirements required to view the object are required to view likes on that object.


### Limitations

* Only aggregated counts using `total_count` with the `summary` parameter are available for Post likes.
* The `like` reaction counts include both "like" and "care" reactions.
* `total_count` represents the approximate number of likes, however, the actual number returned might be different depending on privacy settings.
* The `GET /{group-post-id}/likes` and `GET /{post-id}/likes` endpoints are deprecated in v8.0+ and deprecated in all versions on Nov. 2, 2020.

### Fields



| 
Property Name
 | 
Description
 | 
Type
 |
| --- | --- | --- |
| `total_count` | Total number of User and Page likes on the object. To have this field returned, you must include the `summary=true` parameter and value in your request. | `int32` |

### Example Usage


**Sample Request**
```
curl -i -X GET "https://graph.facebook.com/{object-id}
 ?fields=likes.summary(true)
 &access\_token={access-token}"
```
#### Sample Response



```
 {
 "likes": {
 "data": [
 {
 "name": "Bill the Cat",
 "id": "155111347875779",
 "created\_time": "2017-06-18T18:21:04+0000"
 },
 {
 "name": "Calvin and Hobbes",
 "id": "257573197608192",
 "created\_time": "2017-06-18T18:21:02+0000"
 },
 {
 "name": "Berkeley Breathed's Bloom County",
 "id": "108793262484769",
 "created\_time": "2017-06-18T18:20:58+0000"
 }
 ],
 "paging": {
 "cursors": {
 "before": "Nzc0Njg0MTQ3OAZDZD",
 "after": "NTcxODc1ODk2NgZDZD"
 },
 "next": "https://graph.facebook.com/vX.X/me/likes?access\_token=user-access-token&pretty=0&summary=true&limit=25&after=NTcxODc1ODk2NgZDZD"
 },
 "summary": {
 "total\_count": 136
 }
 },
 "id": "user-id"
}
```
Publish
-------

Like an object.


### New Page Experience


The following objects `/likes` endpoint are supported for New Page Experience:




|  |  |
| --- | --- |
| * Album
* Comment
* PagePost
 |  |

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK
```
POST /v18.0/{object-id}/likes HTTP/1.1
Host: graph.facebook.com
```

```
/\* PHP SDK v5.0.0 \*/
/\* make the API call \*/
try {
 // Returns a `Facebook\FacebookResponse` object
 $response = $fb->post(
 '/{object-id}/likes',
 array (),
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
 "/{object-id}/likes",
 "POST",
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
 "/{object-id}/likes",
 null,
 HttpMethod.POST,
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
 initWithGraphPath:@"/{object-id}/likes"
 parameters:params
 HTTPMethod:@"POST"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection \*connection,
 id result,
 NSError \*error) {
 // Handle the result
}];
```
### Permissions

* A Page access token requested by a person who can perform the `CREATE_CONTENT` task on the Page
* The `pages_manage_engagement` permission

### Limitations

* The Page must also be able to like the object (whether via API or on Facebook.com).
* The object must not have already been liked by the Page.
* If the Page has already reacted to an object (wow, sad) then a like will succeed, but the reaction will not change.
* Liking a Page review is not supported.

### Fields

No fields are required to add likes.


### Response

On success, your app will receive the following response:



```
{
 "success": true
}
```
Updating
--------

You can't perform this operation on this endpoint.

Delete
------

Delete likes on Page objects using this endpoint.


HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK
```
DELETE /v18.0/{object-id}/likes HTTP/1.1
Host: graph.facebook.com
```

```
/\* PHP SDK v5.0.0 \*/
/\* make the API call \*/
try {
 // Returns a `Facebook\FacebookResponse` object
 $response = $fb->delete(
 '/{object-id}/likes',
 array (),
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
 "/{object-id}/likes",
 "DELETE",
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
 "/{object-id}/likes",
 null,
 HttpMethod.DELETE,
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
 initWithGraphPath:@"/{object-id}/likes"
 parameters:params
 HTTPMethod:@"DELETE"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection \*connection,
 id result,
 NSError \*error) {
 // Handle the result
}];
```
### Permissions

* A Page access token requested by a person who can perform the `MODERATE` task on the Page
* The `pages_manage_engagement` permission

### Limitations

* A User or Page can only delete their own `likes`.
* The object must have already been liked.
* Deleting a Page review like is not supported.

### Fields

There are no fields for this endpoint.


### Response

On success, your app will receive the following response:



```
{
 "success": true
}
```
On This Page/{object-id}/likesReadingNew Page ExperienceRequirementsLimitationsFieldsExample UsagePublishNew Page ExperiencePermissionsLimitationsFieldsResponseUpdatingDeletePermissionsLimitationsFieldsResponseFollow Us* 
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