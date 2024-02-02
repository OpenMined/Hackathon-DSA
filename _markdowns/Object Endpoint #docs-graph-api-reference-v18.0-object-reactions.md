Object Reactions - Graph API












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
On This PageObject ReactionsReadingNew Page ExperienceRequirementsSample RequestParametersFieldsError CodesCreatingGraph API Versionv18.0Object Reactions
================


This reference describes the `/reactions` edge that is common to multiple Graph API nodes. The structure and operations are the same for each node. The following objects have a `/reactions` edge:




|  |  |
| --- | --- |
| * Comment
* PagePost
* Post
 |  |

Reading
-------


Get reactions on an object.


View Insights for more information on Page and Post reactions.


### New Page Experience


This endpoint is supported for New Page Experience.


### Requirements


**Marketing Apps**


* `ads_management`
* `pages_read_engagement`
* `pages_show_list`


**Page Management Apps**


* `pages_show_list`


### Sample Request


The following example is a `GET` request made by a User who has reacted to their own object.


cURLAndroid SDKObjective-CJava SDKPHP SDK
```
curl -i -X GET \
 "https://graph.facebook.com/your-post-id/reactions?access\_token=your-user-access-token"
```

```
GraphRequest request = GraphRequest.newGraphPathRequest(
 accessToken,
 "/your-post-id/reactions",
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
 initWithGraphPath:@"/your-post-id/reactions"
 parameters:nil
 HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection \*connection, id result, NSError \*error) {
 // Insert your code here
}];
```

```
FB.api(
 '/your-post-id/reactions',
 'GET',
 {},
 function(response) {
 // Insert your code here
 }
);
```

```
try {
 // Returns a `FacebookFacebookResponse` object
 $response = $fb->get(
 '/your-post-id/reactions',
 '{access-token}'
 );
} catch(FacebookExceptionsFacebookResponseException $e) {
 echo 'Graph returned an error: ' . $e->getMessage();
 exit;
} catch(FacebookExceptionsFacebookSDKException $e) {
 echo 'Facebook SDK returned an error: ' . $e->getMessage();
 exit;
}
$graphNode = $response->getGraphNode();
```
#### The JSON Response



```
{
 "data": [
 {
 "id": "your-user-id",
 "name": "Your Name",
 "type": "HAHA"
 }
 ],
 "paging": {
 "cursors": {
 "before": "QVFIUk5YbXFFbG8yVWVOa2w0ZAGhmSUNKMkZAZAOXZARbzJOMHM0TUFtZAnhJbWdPdkF4OURUTHJrQjFqQ2RQZAVN1UGxSVU5FWURENnE4OUFPeXFreU1jV09pdFJR",
 "after": "QVFIUkpsWVRkcVl6SlhsdWlrcGdudl8xVEhwVEJ5ZA3FXdG90bTRxam13NmJDUGpQVnB5ZA29lMG9FVmFaeU1BLW1hc2oZD"
 }
 }
}
```
If the User or Page has not reacted to the object being queried, `data` will be empty.


The following example is a `GET` request for the total reactions to an object.


cURLAndroid SDKObjective-CJava SDKPHP SDK
```
curl -i -X GET \
 "https://graph.facebook.com/your-post-id
 ?fields=reactions.summary(total\_count)
 &access\_token=your-access-token"
```

```
GraphRequest request = GraphRequest.newGraphPathRequest(
 accessToken,
 "/your-post-id",
 new GraphRequest.Callback() {
 @Override
 public void onCompleted(GraphResponse response) {
 // Insert your code here
 }
});

Bundle parameters = new Bundle();
parameters.putString("fields", "reactions.summary(total\_count)");
request.setParameters(parameters);
request.executeAsync();
```

```
FBSDKGraphRequest \*request = [[FBSDKGraphRequest alloc]
 initWithGraphPath:@"/your-post-id"
 parameters:@{ @"fields": @"reactions.summary(total\_count)",}
 HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection \*connection, id result, NSError \*error) {
 // Insert your code here
}];
```

```
FB.api(
 '/your-post-id',
 'GET',
 {"fields":"reactions.summary(total\_count)"},
 function(response) {
 // Insert your code here
 }
);
```

```
try {
 // Returns a `FacebookFacebookResponse` object
 $response = $fb->get(
 '/your-post-id',
 '{access-token}'
 );
} catch(FacebookExceptionsFacebookResponseException $e) {
 echo 'Graph returned an error: ' . $e->getMessage();
 exit;
} catch(FacebookExceptionsFacebookSDKException $e) {
 echo 'Facebook SDK returned an error: ' . $e->getMessage();
 exit;
}
$graphNode = $response->getGraphNode();
```
The JSON Response if the User or Page has reacted to their own object.



```
{
 "reactions": {
 "data": [
 {
 "id": "your-user-id",
 "name": "Your Name",
 "type": "HAHA"
 }
 ],
 "paging": {
 "cursors": {
 "before": "QVFIUk5YbXFFbG8yVWVOa2w0ZAGhmSUNKMkZAZAOXZARbzJOMHM0TUFtZAnhJbWdPdkF4OURUTHJrQjFqQ2RQZAVN1UGxSVU5FWURENnE4OUFPeXFreU1jV09pdFJR",
 "after": "QVFIUkpsWVRkcVl6SlhsdWlrcGdudl8xVEhwVEJ5ZA3FXdG90bTRxam13NmJDUGpQVnB5ZA29lMG9FVmFaeU1BLW1hc2oZD"
 }
 },
 "summary": {
 "total\_count": 28
 }
 },
 "id": "your-post-id"
}
```
The JSON Response if the User or Page has **not** reacted to their own object.



```
{
 "reactions": {
 "data": [
 ],
 "paging": {
 "cursors": {
 "before": "QVFIUk5YbXFFbG8yVWVOa2w0ZAGhmSUNKMkZAZAOXZARbzJOMHM0TUFtZAnhJbWdPdkF4OURUTHJrQjFqQ2RQZAVN1UGxSVU5FWURENnE4OUFPeXFreU1jV09pdFJR",
 "after": "QVFIUkpsWVRkcVl6SlhsdWlrcGdudl8xVEhwVEJ5ZA3FXdG90bTRxam13NmJDUGpQVnB5ZA29lMG9FVmFaeU1BLW1hc2oZD"
 }
 },
 "summary": {
 "total\_count": 28
 }
 },
 "id": "your-post-id"
}
```
A User or Page can only query their own reactions. Other Users' or Pages' reactions are unavailable due to privacy concerns.


The "like" reaction counts include both "like" and "care" reactions.


### Parameters




| Name | Description |
| --- | --- |
| `type`
enum {NONE, LIKE, LOVE, WOW, HAHA, SORRY, ANGRY} | The type of reaction a Page or User marked an object. |

### Fields


Reading from this edge will return a JSON formatted result



```
{
 "data": [],
 "paging": {},
 "summary": {}
}
```
`data`


The Profile of the Page or User running the query, if the object being queried was reacted to by the Page or User, and a list of reaction types:




| Field | Description |
| --- | --- |
| `type`
enum {NONE, LIKE, LOVE, WOW, HAHA, SORRY, ANGRY} | The type of reaction a Page or User marked an object. |

For reactions on Posts, this edge does not return a Profile except for the current user, if read with a user access token.


#### View the count of an individual reaction


cURLAndroid SDKObjective-CJava SDKPHP SDK
```
curl -i -X GET \
 "https://graph.facebook.com/your-object-id
 ?fields=reactions.type(LOVE).limit(0).summary(total\_count)
 &access\_token=your-access-token"
```

```
GraphRequest request = GraphRequest.newGraphPathRequest(
 accessToken,
 "/your-object-id",
 new GraphRequest.Callback() {
 @Override
 public void onCompleted(GraphResponse response) {
 // Insert your code here
 }
});

Bundle parameters = new Bundle();
parameters.putString("fields", "reactions.type(LOVE).limit(0).summary(total\_count)");
request.setParameters(parameters);
request.executeAsync();
```

```
FBSDKGraphRequest \*request = [[FBSDKGraphRequest alloc]
 initWithGraphPath:@"/your-object-id"
 parameters:@{ @"fields": @"reactions.type(LOVE).limit(0).summary(total\_count)",}
 HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection \*connection, id result, NSError \*error) {
 // Insert your code here
}];
```

```
FB.api(
 '/your-object-id',
 'GET',
 {"fields":"reactions.type(LOVE).limit(0).summary(total\_count)"},
 function(response) {
 // Insert your code here
 }
);
```

```
try {
 // Returns a `FacebookFacebookResponse` object
 $response = $fb->get(
 '/your-object-id',
 '{access-token}'
 );
} catch(FacebookExceptionsFacebookResponseException $e) {
 echo 'Graph returned an error: ' . $e->getMessage();
 exit;
} catch(FacebookExceptionsFacebookSDKException $e) {
 echo 'Facebook SDK returned an error: ' . $e->getMessage();
 exit;
}
$graphNode = $response->getGraphNode();
```
#### Example JSON Returned



```
{
 "reactions": {
 "data": [
 ],
 "summary": {
 "total\_count": 3498
 }
 },
 "id": "your-object-id"
}
```
`paging`


For more details about pagination, see the Graph API's paging documentation. Adding `limit(0)` to `reactions` will remove `paging` from the output.


`summary`


Aggregated information about the edge, such as counts. Specify the fields to fetch in the summary param (like `summary=total_count`).




| Field | Description |
| --- | --- |
| `total_count`
unsigned int32 | Total number of reactions |
| `viewer_reaction`
enum {NONE, LIKE, LOVE, WOW, HAHA, SORRY, ANGRY} | The type of reaction a Page or User marked an object. |

### Error Codes




| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

Creating
--------


This operation is not supported.


Updating
--------


This operation is not supported.


Deleting
--------


This operation is not supported.


On This PageObject ReactionsReadingNew Page ExperienceRequirementsSample RequestParametersFieldsError CodesCreatingFollow Us* 
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