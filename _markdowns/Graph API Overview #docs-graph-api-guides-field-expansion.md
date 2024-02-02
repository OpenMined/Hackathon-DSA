Field Expansion - Graph API










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
On This PageField ExpansionLimiting ResultsNested RequestsField AliasesNext StepsField Expansion
===============


If you test the `GET /me/feed` query in the Graph API Explorer, you will noticed that the request returned many objects and paginated the results. This is common for most edges.


#### Example Response



```
{
 "data": [
 {
 "created\_time": "2021-04-30T01:37:07+0000",
 "message": "I’ll never forget it has a head.",
 "id": "10211998223264288\_10222340566616408"
 },
 ...
 {
 "created\_time": "2021-04-25T22:29:26+0000",
 "message": "Things you hear at my house: \"I accidentally made a cake.\"",
 "id": "10211998223264288\_10222314489524497"
 }
 ],
 "paging": {
 "previous": "https://graph.facebook.com/v11.0/USER-ID/feed?access\_token=ACCESS-TOKEN&pretty=0&\_\_previous=1&since=1627322627&until&\_\_paging\_token=enc\_AdB2fX...",
 "next": "https://graph.intern.facebook.com/v11.0/USER-ID/feed?access\_token=ACCESS-TOKEN&pretty=0&until=1619389766&since&\_\_paging\_token=enc\_AdAamX...&\_\_previous"
 }
}
```
Field expansion allows you not only to limit the number of objects returned but also perform nested requests.


Limiting Results
----------------


Limiting allows you to control the number of objects returned in each set of paginated results. To limit results, add a `.limit()` argument to any field or edge.


For example, performing a GET request on your `/feed` edge may return hundreds of Posts. You can limit the number of Posts returned for each page of results by doing this:



```
curl -i -X GET "https://graph.facebook.com/USER-ID?fields=feed.limit(3)&access\_token=ACCESS-TOKEN"
```
This returns all of the Posts on your User node, but limits the number of objects in each page of results to three. Notice that instead of specifying the Feed edge in the path URL (`/user/feed`), you specify it in the `fields` parameter (`?fields=feed`), which allows you to append the `.limit(3)` argument.


Here are the query results:



```
{
 "feed": {
 "data": [
 {
 "created\_time": "2021-12-12T01:24:21+0000",
 "message": "This picture of my grandson with Santa",
 "id": "POST-ID"
 },
 {
 "created\_time": "2021-12-11T23:40:17+0000",
 "message": ":)",
 "id": "POST-ID" 
 },
 {
 "created\_time": "2021-12-11T23:31:38+0000",
 "message": "Thought you might enjoy this.",
 "id": "POST-ID" 
 }
 ],
 "paging": {
 "previous": "https://graph.facebook.com/v8.0/USER-ID/feed?format=json&limit=3&since=1542820440&access\_token=ACCESS-TOKEN&\_\_paging\_token=enc\_AdC...&\_\_previous=1",
 "next": "https://graph.facebook.com/v8.0/USER-ID/feed?format=json&limit=3&access\_token=ACCESS-TOKEN&until=1542583212&\_\_paging\_token=enc\_AdD..."
 }
 },
 "id": "USER-ID"
}
```
As you can see, only three objects appear in this page of paginated results. However, the response included a `next` field and URL which you can use to fetch the next page.


Nested Requests
---------------


The field expansion feature of the Graph API allows you to effectively nest multiple graph queries into a single call. For example, in a single call, you can ask for the first N photos of the first K albums. The response maintains the data hierarchy so developers do not have to weave the data together on the client. This is different from the batch requests feature which allows you to make multiple, potentially unrelated, Graph API calls in a single request.


Here is the general format that field expansion takes:



```
GET graph.facebook.com/{node-id}?fields=LEVEL-ONE{LEVEL-TWO}
```
`LEVEL-ONE` in this case would be one or more (comma-separated) fields or edges from the parent node. 
`LEVEL-TWO` would be one or more (comma-separated) fields or edges from the first level node.


There is no limitation to the amount of nesting of levels that can occur here. You can also use a `.limit(n)` argument on each field or edge to restrict how many objects you want to get.


This is easier to understand by seeing it in action, so here's an example query that will retrieve up to five posts your published, with the text from each individual post.



```
GET graph.facebook.com/me?fields=posts.limit(5){message}
```
We can then extend this a bit more and for each post object, we get the text and privacy setting of each post. By default the `privacy` field returns an object that contains information about five key:value pairs, `allow`, `deny`, `description`, `friends`, and `value`. In this query we only want one returned, the `value` key:value pair.



```
GET graph.facebook.com/me?fields=posts.limit(5){message,privacy{value}}
```
Now we can extend it again by retrieving the name of each photo, the picture URL, and the people tagged:



```
GET graph.facebook.com
 /me?fields=albums.limit(5){name, photos.limit(2){name, picture, tags.limit(2)}},posts.limit(5)
```
Let's look at an example using cursor-based pagination:



```
GET graph.facebook.com
 /me?fields=albums.limit(5){name,photos.limit(2).after(MTAyMTE1OTQwNDc2MDAxNDkZD){name,picture,tags.limit(2)}},posts.limit(5)
```
You can see how field expansion can work across nodes, edges, and fields to return really complex data in a single request.


#### Limitations


* Certain resources, including most of Marketing API, are unable to utilize field expansion on some or all connections.


Field Aliases
-------------


Many nodes and edges allow you to provide aliases for fields by using the `as` parameter. This will return data using fields that you already have in your application logic.


For example, you can retrieve an image in two sizes and alias the returned object fields as `picture_small` and `picture_larger`:



```
me?fields=id,name,picture.width(100).height(100).as(picture\_small),picture.width(720).height(720).as(picture\_large)
```
On success, Graph API returns this result:



```
{
 "id": "993363923726",
 "name": "Benjamin Golub",
 "picture\_small": {
 "data": {
 "height": 100,
 "is\_silhouette": false,
 "url": "https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xft1/v/t1.0-1/p100x100/11700890\_10100330450676146\_2622493406845121288\_n.jpg?oh=82b9abe469c78486645783c9e70e8797&amp;oe=561D10AE&amp;\_\_gda\_\_=1444247939\_661c0f48363f1d1a7d42b6f836687a04",
 "width": 100
 }
 },
 "picture\_large": {
 "data": {
 "height": 720,
 "is\_silhouette": false,
 "url": "https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xft1/v/t1.0-1/11700890\_10100330450676146\_2622493406845121288\_n.jpg?oh=dd86551faa2de0cd6b359feb5665b0a5&amp;oe=561E0B46&amp;\_\_gda\_\_=1443979219\_f1abbbdfb0fb7dac361d7ae02b460638",
 "width": 720
 }
 }
}
```
Please note that not all nodes and edges support field aliasing. Endpoints that do not support aliasing will return an error. For example, the `User` node does not support aliasing, so if you tried to alias the `name` field as `my_name` you would receive an error like this:



```
{
 "error": {
 "message": "(#100) Unknown fields: my\_name.",
 "type": "OAuthException",
 "code": 100
 }
}
```
Next Steps
----------


* Learn about Paginated Results.


On This PageField ExpansionLimiting ResultsNested RequestsField AliasesNext StepsFollow Us* 
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