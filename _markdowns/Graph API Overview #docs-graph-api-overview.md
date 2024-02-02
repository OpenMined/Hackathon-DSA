Overview - Graph API










DocsToolsSupportLog InGraph API* Overview
	+ Access Levels
	+ Facebook SDKs
	+ Paginated Results
	+ Rate Limits
	+ Versioning
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
On This PageOverviewHTTPHost URLAccess TokensNodesNode Metadata/meEdgesFieldsComplex ParametersPublishing, Updating, and DeletingRead-After-WriteWebhooksVersionsFacebook APIs, SDKs, and PlatformsNext StepsOverview
========


The Graph API is the primary way to get data into and out of the Facebook platform. It's an HTTP-based API that apps can use to programmatically query data, post new stories, manage ads, upload photos, and perform a wide variety of other tasks.


The Graph API is named after the idea of a "social graph" — a representation of the information on Facebook. It's composed of nodes, edges, and fields. Typically you use nodes to get data about a specific object, use edges to get collections of objects on a single object, and use fields to get data about a single object or each object in a collection. Throughout our documentation, we may refer to both a node and edge as an "endpoint". For example, "send a `GET` request to the User endpoint".


HTTP
----


All data transfers conform to HTTP/1.1, and all endpoints require HTTPS. Because the Graph API is HTTP-based, it works with any language that has an HTTP library, such as cURL and urllib. This means you can use the Graph API directly in your browser. For example, requesting this URL in your browser...


https://graph.facebook.com/facebook/picture?redirect=false


... is equivalent to performing this cURL request:



```
curl -i -X GET "https://graph.facebook.com/facebook/picture?redirect=false"
```
We have also enabled the `includeSubdomains` HSTS directive on `facebook.com`, but this should not adversely affect your Graph API calls.


Host URL
--------


Almost all requests are passed to the `graph.facebook.com` host URL. The single exception is video uploads, which use `graph-video.facebook.com`.


Access Tokens
-------------


Access tokens allow your app to access the Graph API. Almost all Graph API endpoints require an access token of some kind, so each time you access an endpoint, your request may require one. They typically perform two functions:


* They allow your app to access a User's information without requiring the User's password. For example, your app needs a User's email to perform a function. If the User agrees to allow your app to retrieve their email address from Facebook, the User will not need to enter their Facebook password for your app to get their email address.
* They allow us to identify your app, the User who is using your app, and the type of data the User has permitted your app to access.


Visit our access token documentation to learn more.


Nodes
-----


A node is an individual object with a unique ID. For example, there are many User node objects, each with a unique ID representing a person on Facebook. Pages, Groups, Posts, Photos, and Comments are just some of the nodes of the Facebook Social Graph.


The following cURL example represents a call to the User node.



```
curl -i -X GET \
 "https://graph.facebook.com/USER-ID?access\_token=ACCESS-TOKEN"
```
This request would return the following data by default, formatted using JSON:



```
{
 "name": "Your Name",
 "id": "YOUR-USER-ID"
}
```
### Node Metadata


You can get a list of all fields, including the field name, description, and data type, of a node object, such as a User, Page, or Photo. Send a `GET` request to an object ID and include the `metadata=1` parameter:



```
curl -i -X GET \
 "https://graph.facebook.com/USER-ID?
 metadata=1&access\_token=ACCESS-TOKEN"
```
The resulting JSON response will include the `metadata` property that lists all the supported fields for the given node:



```
{
 "name": "Jane Smith",
 "metadata": {
 "fields": [
 {
 "name": "id",
 "description": "The app user's App-Scoped User ID. This ID is unique to the app and cannot be used by other apps.",
 "type": "numeric string"
 },
 {
 "name": "age\_range",
 "description": "The age segment for this person expressed as a minimum and maximum age. For example, more than 18, less than 21.",
 "type": "agerange"
 },
 {
 "name": "birthday",
 "description": "The person's birthday. This is a fixed format string, like `MM/DD/YYYY`. However, people can control who can see the year they were born separately from the month and day so this string can be only the year (YYYY) or the month + day (MM/DD)",
 "type": "string"
 },
...
```
/me
---


The `/me` node is a special endpoint that translates to the object ID of the person or Page whose access token is currently being used to make the API calls. If you had a User access token, you could retrieve a User's name and ID by using:



```
curl -i -X GET \
 "https://graph.facebook.com/me?access\_token=ACCESS-TOKEN"
```
Edges
-----


An edge is a connection between two nodes. For example, a User node can have photos connected to it, and a Photo node can have comments connected to it. The following cURL example will return a list of photos a person has published to Facebook.



```
curl -i -X GET \
 "https://graph.facebook.com/USER-ID/photos?access\_token=ACCESS-TOKEN"
```
Each ID returned represents a Photo node and when it was uploaded to Facebook.



```
 {
 "data": [
 {
 "created\_time": "2017-06-06T18:04:10+0000",
 "id": "1353272134728652"
 },
 {
 "created\_time": "2017-06-06T18:01:13+0000",
 "id": "1353269908062208"
 }
 ],
}
```
Fields
------


Fields are node properties. When you query a node, or an edge, it returns a set of fields by default, as the examples above show. However, you can specify which fields you want returned by using the `fields` parameter and listing each field. This overrides the defaults and returns only the fields you specify, and the ID of the object, which is always returned.


The following cURL request includes the `fields` parameter and the User's name, email, and profile picture.



```
curl -i -X GET \
 "https://graph.facebook.com/USER-ID?fields=id,name,email,picture&access\_token=ACCESS-TOKEN"
```
#### Data Returned



```
{
 "id": "USER-ID",
 "name": "EXAMPLE NAME",
 "email": "EXAMPLE@EMAIL.COM",
 "picture": {
 "data": {
 "height": 50,
 "is\_silhouette": false,
 "url": "URL-FOR-USER-PROFILE-PICTURE",
 "width": 50
 }
 }
}
```
### Complex Parameters


Most parameter types are straightforward primitives such as `bool`, `string` and `int`, but there are also `list` and `object` types that can be specified in the request.


The `list` type is specified in JSON syntax, for example: `["firstitem", "seconditem", "thirditem"]`


The `object` type is also specified in JSON syntax, for example: `{"firstkey": "firstvalue", "secondKey": 123}`


Publishing, Updating, and Deleting
----------------------------------


Visit our Facebook Sharing guide to learn how to publish to a User's Facebook or our Pages API documentation to publish to a Page's Facebook feed.


Some nodes allow you to update fields with `POST` operations. For example, you could update your `email` field like this:



```
curl -i -X POST \
 "https://graph.facebook.com/USER-ID?email=YOURNEW@EMAILADDRESS.COM&access\_token=ACCESS-TOKEN"
```
### Read-After-Write


For create and update endpoints, the Graph API can immediately read a successfully published or updated object and return any fields supported by the corresponding read endpoint.


By default, an ID of the object created or updated will be returned. To include more information in the response, include the `fields` parameter in your request and list the fields you want returned. For example, to publish the message “Hello” to a Page's feed, you could make the following request:



```
curl -i - X POST "https://graph.facebook.com/PAGE-ID/feed?message=Hello&
 fields=created\_time,from,id,message&access\_token=ACCESS-TOKEN"
```
*The above code example is formatted for readability.*This would return the specified fields as a JSON-formatted response, like this:



```
{
 "created\_time": "2017-04-06T22:04:21+0000",
 "from": {
 "name": "My Facebook Page",
 "id": "PAGE-ID"
 },
 "id": "POST\_ID",
 "message": "Hello",
}
```
Refer to each endpoint's reference documentation to see if it supports **read-after-write** and what fields are available.


#### Errors


If the read fails for any reason (for example, requesting a non-existent field), the Graph API will respond with a standard error response. Visit our Handling Errors guide for more information.


You can usually delete a node, such as a Post or Photo node, by performing a DELETE operation on the object ID:



```
curl -i -X DELETE \
 "https://graph.facebook.com/PHOTO-ID?access\_token=ACCESSS-TOKEN"
```
Usually you can only delete nodes that you created, but check each node's reference guide to see requirements for delete operations.


Webhooks
--------


You can be notified of changes to nodes or interactions with nodes by subscribing to webhooks. See Webhooks.


Versions
--------


The Graph API has multiple versions with quarterly releases. You can specify the version in your calls by adding "v" and the version number to the start of the request path. For example, here's a call to version 4.0:



```
curl -i -X GET \
 "https://graph.facebook.com/v4.0/USER-ID/photos
 ?access\_token=ACCESS-TOKEN"
```
If you do not include a version number we will default to the oldest available version, so it's recommended to include the version number in your requests.


You can read more about versions in our Versioning guide and learn about all available versions in the Graph API Changelog.


Facebook APIs, SDKs, and Platforms
----------------------------------


Connect interfaces and develop across platforms using Facebook's various APIs, SDKs, and platforms.


Next Steps
----------


**Get Started with Graph API** – Let's explore the Facebook Social Graph using the Graph Explorer tool and run a couple requests to get data.


On This PageOverviewHTTPHost URLAccess TokensNodesNode Metadata/meEdgesFieldsComplex ParametersPublishing, Updating, and DeletingRead-After-WriteWebhooksVersionsFacebook APIs, SDKs, and PlatformsNext StepsFollow Us* 
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