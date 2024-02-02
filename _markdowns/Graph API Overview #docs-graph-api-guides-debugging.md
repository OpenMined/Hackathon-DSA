Debug Requests - Graph API











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
On This PageDebug RequestsGraph API Debug ModeDetermining Version used by API RequestsDebug Info for Reporting BugsDebug Requests
==============


Graph API Debug Mode
--------------------


When Debug Mode is enabled, Graph API response may contain additional fields that explain potential issues with the request.


To enable debug mode, use the `debug` query string parameter. For example:


cURLAndroid SDKObjective-CJava SDKPHP SDK
```
curl -i -X GET \
 "https://graph.facebook.com/{user-id}
 ?fields=friends
 &debug=all
 &access\_token={your-access-token}"
```

```
GraphRequest request = GraphRequest.newMeRequest(
 accessToken,
 new GraphRequest.GraphJSONObjectCallback() {
 @Override
 public void onCompleted(JSONObject object, GraphResponse response) {
 // Insert your code here
 }
});

Bundle parameters = new Bundle();
parameters.putString("fields", "friends");
parameters.putString("debug", "all");
request.setParameters(parameters);
request.executeAsync();
```

```
FBSDKGraphRequest \*request = [[FBSDKGraphRequest alloc]
 initWithGraphPath:@"/{user-id}"
 parameters:@{ @"fields": @"friends",@"debug": @"all",}
 HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection \*connection, id result, NSError \*error) {
 // Insert your code here
}];
```

```
FB.api(
 '/{user-id}',
 'GET',
 {"fields":"friends","debug":"all"},
 function(response) {
 // Insert your code here
 }
);
```

```
try {
 // Returns a `FacebookFacebookResponse` object
 $response = $fb->get(
 '/{user-id}',
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
If `user_friends` permission was not granted, this produces the following response:



```
{
 "data": [
 ], 
 "\_\_debug\_\_": {
 "messages": [
 {
 "message": "Field friends is only accessible on User object, if user\_friends permission is granted by the user", 
 "type": "warning"
 }, 
 {
 "link": "https://developers.facebook.com/docs/apps/changelog#v2\_0", 
 "message": "Only friends who have installed the app are returned in versions greater or equal to v2.0.", 
 "type": "info"
 }
 ]
 }
}
```
The `debug` parameter value can be set to "all" or to a minimal requested severity level that corresponds to `type` of the message:




| 
Debug Param Value
 | 
What Will Be Returned
 |
| --- | --- |
| all | All available debug messages. |
| info | Debug messages with type *info* and *warning*. |
| warning | Only debug messages with type *warning*. |

Debug information, when available, is returned as a JSON object under the `__debug__` key in the `messages` array. Every element of this array is a JSON object that contains the following fields:




| 
Field
 | 
Datatype
 | 
Description
 |
| --- | --- | --- |
| message | String | The message. |
| type | String | The message severity. |
| link | String | [Optional] A URL pointing to related information. |

You can also use Debug Mode with Graph API Explorer.


### Determining Version used by API Requests


When you're building an app and making Graph API requests, you might find it useful to determine what API version you're getting a response from. For example, if you're making calls without a version specified, the API version that responds may not be known to you.


The Graph API supplies a request header with any response called `facebook-api-version` that indicates the exact version of the API that generated the response. For example, a Graph API call that generates a request with v2.0 produces the following HTTP header:



```
facebook-api-version:v2.0
```
This `facebook-api-version` header allows you to determine whether API calls are being returned from the version that you expect.


### Debug Info for Reporting Bugs


When reporting a bug in the Graph API, we include some additional request headers to send with your bug report to help us pinpoint and reproduce your issue. These request headers are `X-FB-Debug`, `x-fb-rev`, and `X-FB-Trace-ID`.


On This PageDebug RequestsGraph API Debug ModeDetermining Version used by API RequestsDebug Info for Reporting BugsFollow Us* 
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