Object Comments - Graph API













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
On This Page/{object-id}/commentsReadingNew Page ExperiencePermissionsLimitationsExampleParametersFieldsPublishingNew Page ExperiencePermissionsExampleFieldsReturn TypeUpdatingDeletingGraph API Versionv18.0`/{object-id}/comments`
=======================

This reference describes the `/comments` edge that is common to multiple Graph API nodes. The structure and operations are the same for each node. The following objects have a `/comments` edge:



|  |  |  |
| --- | --- | --- |
| * Album
* Comment
* Event
* Link
 | * Live Video
* Photo
* Post
 | * Thread
* User
* Video
 |

It is possible for comment objects to have a `/comments` edge, which is called *comment replies*. The structure is the same for these, but attention should be paid to the modifiers for these edges.

Reading
-------

Returns a comment on an object.


The `id` field for the `/PAGEPOST-ID/comments` endpoint will no longer be returned for apps using the Page Public Content Access feature. To access the comment IDs for a Page post you must be able to perform the MODERATE task on the Page being queried. This change is in effect for v11.0+ and will be implement for all versions on September, 7, 2021.

###  New Page Experience

The following objects `/comments` endpoint are supported for New Page Experience:



|  |  |
| --- | --- |
| * Album
* Comment
* Link
* Page
 | * PagePost
* Photo
* Post
* PostComment
 |

### Permissions

* The same permissions required to view the parent object are required to view comments on that object.


### Limitations

* Other users' profile information and comments will not be returned when accessing user posts, photos, albums, videos, likes, and reactions unless authorized by those users.
* Comments returned in a query are based on default filtering. To get all comments that can be returned depending on your permissions, set the `filter` parameter to `stream` or use the `order` field.
* A new Page can comment as the Page on new Pages or classic Pages. However, a classic Page can not comment on a new Page.
* For the following nodes, the `/comments` endpoint returns empty data if you read it with a User access token:
 
	+ Album
	+ Photo
	+ Post
	+ Video
* The `id` field for the `/PAGEPOST-ID/comments` endpoint will no longer be returned for apps using the Page Public Content Access feature. To access the comment IDs for a Page post you must be able to perform the MODERATE task on the Page being queried.
* For objects that have tens of thousands of comments, you may encounter limits while paging. Learn more about paging in our Using the Graph API Guide.

### Example


HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v18.0/{object-id}/comments HTTP/1.1
Host: graph.facebook.com
```

```
/\* PHP SDK v5.0.0 \*/
/\* make the API call \*/
try {
 // Returns a `Facebook\FacebookResponse` object
 $response = $fb->get(
 '/{object-id}/comments',
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
 "/{object-id}/comments",
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
 "/{object-id}/comments",
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
 initWithGraphPath:@"/{object-id}/comments"
 parameters:params
 HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection \*connection,
 id result,
 NSError \*error) {
 // Handle the result
}];
```
### Parameters

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK
```
GET /v18.0/{object-id}/comments?summary=1&filter=toplevel HTTP/1.1
Host: graph.facebook.com
```

```
/\* PHP SDK v5.0.0 \*/
/\* make the API call \*/
try {
 // Returns a `Facebook\FacebookResponse` object
 $response = $fb->get(
 '/{object-id}/comments?summary=1&filter=toplevel',
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
 "/{object-id}/comments",
 {
 "summary": true,
 "filter": "toplevel"
 },
 function (response) {
 if (response && !response.error) {
 /\* handle the result \*/
 }
 }
);
```

```
Bundle params = new Bundle();
params.putBoolean("summary", true);
params.putString("filter", "toplevel");
/\* make the API call \*/
new GraphRequest(
 AccessToken.getCurrentAccessToken(),
 "/{object-id}/comments",
 params,
 HttpMethod.GET,
 new GraphRequest.Callback() {
 public void onCompleted(GraphResponse response) {
 /\* handle the result \*/
 }
 }
).executeAsync();
```

```
NSDictionary \*params = @{
 @"summary": @YES,
 @"filter": @"toplevel",
};
/\* make the API call \*/
FBSDKGraphRequest \*request = [[FBSDKGraphRequest alloc]
 initWithGraphPath:@"/{object-id}/comments"
 parameters:params
 HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection \*connection,
 id result,
 NSError \*error) {
 // Handle the result
}];
```


|  Parameter  |  Description  |
| --- | --- |
| `summary`
*bool* | A summary of metadata about the comments on the object. Importantly this metadata includes `order` which indicates how the comments are being sorted. |
| `filter`
*enum { toplevel, stream }* | If a person can reply to a comment, you can filter comments based on top level comments, comments that are made directly on the post, or the chronological order of all comments.* `toplevel` - This is the default. It returns all top-level comments in chronological order, as ordered on Facebook. This filter is useful for displaying comments in the same structure as they appear on Facebook.
* `stream` - All-level comments in `chronological` order. This filter is useful for comment moderation tools where it is helpful to see a chronological list of all comments.
 |

### Fields

An array of Comment objects in addition to the following fields when `summary` is `true` in the request.



|  Field  |  Description  |
| --- | --- |
| `order`
*enum { chronological, reverse\_chronological }* | Order in which comments were returned.* `chronological`: Comments sorted by the oldest comments first.
* `reverse_chronological`: Comments sorted by the newest comments first.
 |
| `total_count`
*int32* | The count of comments on this node. It is important to note that this value changes depending on the `filter` being used (where comment replies are available):* if `filter` is `stream` then `total_count` will be a count of all comments (including replies) on the node.
* if `filter` is `toplevel` then `total_count` will be a count of all top-level comments on the node.

Note: `total_count` can be greater than or equal to the actual number of comments returned due to comment privacy or deletion. |

Publishing
----------

Publish new comments to any object.


###  New Page Experience

The following objects `/comments` endpoint are supported for New Page Experience:



|  |  |
| --- | --- |
| * Comments
* PagePosts
* Photo
* Post
 | * PostComment
* Video
 |

### Permissions

* A Page access token requested by a person who can perform the `MODERATE` task on the Page
* The `pages_manage_engagement` permission

Note, the `can_comment` field on individual comment objects indicates whether it is possible to reply to that comment.

### Example


HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK
```
POST /v18.0/{object-id}/comments HTTP/1.1
Host: graph.facebook.com

message=This+is+a+test+comment
```

```
/\* PHP SDK v5.0.0 \*/
/\* make the API call \*/
try {
 // Returns a `Facebook\FacebookResponse` object
 $response = $fb->post(
 '/{object-id}/comments',
 array (
 'message' => 'This is a test comment',
 ),
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
 "/{object-id}/comments",
 "POST",
 {
 "message": "This is a test comment"
 },
 function (response) {
 if (response && !response.error) {
 /\* handle the result \*/
 }
 }
);
```

```
Bundle params = new Bundle();
params.putString("message", "This is a test comment");
/\* make the API call \*/
new GraphRequest(
 AccessToken.getCurrentAccessToken(),
 "/{object-id}/comments",
 params,
 HttpMethod.POST,
 new GraphRequest.Callback() {
 public void onCompleted(GraphResponse response) {
 /\* handle the result \*/
 }
 }
).executeAsync();
```

```
NSDictionary \*params = @{
 @"message": @"This is a test comment",
};
/\* make the API call \*/
FBSDKGraphRequest \*request = [[FBSDKGraphRequest alloc]
 initWithGraphPath:@"/{object-id}/comments"
 parameters:params
 HTTPMethod:@"POST"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection \*connection,
 id result,
 NSError \*error) {
 // Handle the result
}];
```
### Fields



|  Name  |  Description  |
| --- | --- |
| `attachment_id`
*string* | An optional ID of a unpublished photo (see `no_story` field in `/{user-id}/photos`) uploaded to Facebook to include as a photo comment. One of `attachment_id`, `attachment_share_url`, `attachment_url`, `message`, or `source` must be provided when publishing. |
| `attachment_share_url`
*string* | The URL of a GIF to include as a animated GIF comment. One of `attachment_id`, `attachment_share_url`, `attachment_url`, `message`, or `source` must be provided when publishing. |
| `attachment_url`
*string* | The URL of an image to include as a photo comment. One of `attachment_id`, `attachment_share_url`, `attachment_url`, `message`, or `source` must be provided when publishing. |
| `source`
*multipart/form-data* | A photo, encoded as form data, to use as a photo comment. One of `attachment_id`, `attachment_share_url`, `attachment_url`, `message`, or `source` must be provided when publishing. |
| `message`
*string* | The comment text. One of `attachment_id`, `attachment_share_url`, `attachment_url`, `message`, or `source` must be provided when publishing.Mention other Facebook Pages in your `message` text using the following syntax: `@[page-id]` Usage of this feature is subject to review. |

### Return Type

If successful, you will receive a JSON response with the newly created comment ID. In addition, this endpoint supports read-after-write and can immediately return any fields returned by read operations.


```
{
 "id": "{comment-id}"
}
```
Updating
--------

You can't update using this edge.

Deleting
--------

You can't delete using this edge.

Delete individual comments using the /comment-id endpoint.

On This Page/{object-id}/commentsReadingNew Page ExperiencePermissionsLimitationsExampleParametersFieldsPublishingNew Page ExperiencePermissionsExampleFieldsReturn TypeUpdatingDeletingFollow Us* 
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