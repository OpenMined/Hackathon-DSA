Batch Requests - Graph API










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
On This PageBatch RequestsBatch RequestComplex Batch RequestsErrorsTimeoutsBatch calls with JSONPUsing Multiple Access TokensUpload Binary DataBatch Requests
==============


Send a single HTTP request that contains multiple Facebook Graph API calls. Independent operations are processed in parallel while dependent operations are processed sequentially. Once all operations are complete, a consolidated response is passed back to you and the HTTP connection is closed.


The ordering of responses correspond with the ordering of operations in the request. You should process responses accordingly to determine which operations were successful and which should be retried in a subsequent operation.


### Limitations


* Batch requests are limited to 50 requests per batch. Each call within the batch is counted separately for the purposes of calculating API call limits and resource limits. For example, a batch of 10 API calls will count as 10 calls and each call within the batch contributes to CPU resource limits in the same manner. Please see our Rate Limiting Guide for more information.
* Batch requests cannot include multiple Adsets under the same Campaign. Learn more about batching Marketing API requests.


Batch Request
-------------


A batch request takes a JSON object consisting of an array of your requests. It returns an array of logical HTTP responses represented as JSON arrays. Each response has a status code, an optional headers array, and an optional body (which is a JSON encoded string).


To make a batched request, send a `POST` request to an endpoint where the `batch` parameter is your JSON object.



```
POST /ENDPOINT?batch=[JSON-OBJECT]
```
**Sample Batch Request**


In this example, we are getting information about two Pages that our app manages.


*Formatted for readability.*
```
curl -i -X POST 'https://graph.facebook.com/me?batch= 
 [
 {
 "method":"GET",
 "relative\_url":"PAGE-A-ID"
 }, 
 {
 "method":"GET",
 "relative\_url":"PAGE-B-ID"
 }
 ]
 &include\_headers=false // Included to remove header information
 &access\_token=ACCESS-TOKEN'
```
Once all operations are complete, a response is sent with the result of each operation. Because the headers returned can sometimes be much larger than the actual API response, you might want to remove them for efficiency. To include header information, remove the `include_headers` parameter or set it to `true`.


**Sample Response**


The body field contains a string encoded JSON object:



```
[
 {
 "code": 200,
 "body": "{
 \"name\": \"Page A Name\",
 \"id\": \"PAGE-A-ID\"
 }"
 },
 {
 "code": 200,
 "body": "{
 \"name\": \"Page B Name\",
 \"id\": \"PAGE-B-ID\"
 }"
 }
]
```
Complex Batch Requests
----------------------


It is possible to combine operations that would normally use different HTTP methods into a single batch request. While `GET` and `DELETE` operations can only have a `relative_url` and a `method` field, `POST` and `PUT` operations may contain an optional `body` field. The body should be formatted as a raw HTTP POST string, similar to a URL query string.


**Sample Request**


The following example publishes a post to a Page we manage and have publish permissions and then the Page's feed in a single operation:



```
curl "https://graph.facebook.com/PAGE-ID?batch=
 [
 { 
 "method":"POST",
 "relative\_url":"PAGE-ID/feed",
 "body":"message=Test status update"
 },
 { 
 "method":"GET",
 "relative\_url":"PAGE-ID/feed"
 }
 ]
 &access\_token=ACCESS-TOKEN"
```
The output of this call would be:



```
[
 { "code": 200,
 "headers": [
 { "name":"Content-Type", 
 "value":"text/javascript; charset=UTF-8"}
 ],
 "body":"{\"id\":\"…\"}"
 },
 { "code": 200,
 "headers": [
 { "name":"Content-Type", 
 "value":"text/javascript; charset=UTF-8"
 },
 { "name":"ETag", 
 "value": "…"
 }
 ],
 "body": "{\"data\": [{…}]}
 }
]
```
The following example creates a new ad for a campaign, and then gets the details of the newly created object. Note the **URLEncoding** for the body param:



```
curl \
-F 'access\_token=...' \
-F 'batch=[
 {
 "method":"POST",
 "name":"create-ad",
 "relative\_url":"11077200629332/ads",
 "body":"ads=%5B%7B%22name%22%3A%22test\_ad%22%2C%22billing\_entity\_id%22%3A111200774273%7D%5D"
 }, 
 {
 "method":"GET",
 "relative\_url":"?ids={result=create-ad:$.data.\*.id}"
 }
]' \
https://graph.facebook.com
```
The following example adds multiple pages to a Business Manager:



```
curl \
-F 'access\_token=<ACCESS\_TOKEN>' \
-F 'batch=[
 {
 "method":"POST",
 "name":"test1",
 "relative\_url":"<BUSINESS\_ID>/owned\_pages",
 "body":"page\_id=<PAGE\_ID\_1>"
 }, 
 {
 "method":"POST",
 "name":"test2",
 "relative\_url":"<BUSINESS\_ID>/owned\_pages",
 "body":"page\_id=<PAGE\_ID\_2>"
 }, 
 {
 "method":"POST",
 "name":"test3",
 "relative\_url":"<BUSINESS\_ID>/owned\_pages",
 "body":"page\_id=<PAGE\_ID\_3>"
 }, 
]' \
"https://graph.facebook.com/v12.0"
```
Where:


* `<ACCESS_TOKEN>` is an access token with the `business_management` permission.
* `<BUSINESS_ID>` is the ID of the Business Manager to which the pages should be claimed.
* `<PAGE_ID_n>` are the Page IDs to be claimed.


Errors
------


Its possible that one of your requested operations may throw an error. This could be because, for example, you don't have permission to perform the requested operation. The response is similiar to the standard Graph API, but encapsulated in the batch response syntax:



```
[
 { "code": 403,
 "headers": [
 {"name":"WWW-Authenticate", "value":"OAuth…"},
 {"name":"Content-Type", "value":"text/javascript; charset=UTF-8"} ],
 "body": "{\"error\":{\"type\":\"OAuthException\", … }}"
 }
]
```
Other requests within the batch should still complete successfully and will be returned, as normal, with a `200` status code.


Timeouts
--------


Large or complex batches may timeout if it takes too long to complete all the requests within the batch. In such a circumstance, the result is a partially-completed batch. In a partially-completed batch, requests that are completed successful will return the normal output with the `200` status code. Responses for requests that are not successful will be `null`. You can retry any unsuccessful request.


Batch calls with JSONP
----------------------


The Batch API supports JSONP, just like the rest of the Graph API - the JSONP callback function is specified using the `callback` query string or form post parameter.


Using Multiple Access Tokens
----------------------------


Individual requests of a single batch request can specify its own access tokens as a query string or form post parameter. In that case the top level access token is considered a fallback token and is used if an individual request has not explicitly specified an access token.


This may be useful when you want to query the API using several different User or Page access tokens, or if some of your calls need to be made using an app access token.


You must include an access token as a top level parameter, even when all individual requests contain their own tokens.


Upload Binary Data
------------------


You can upload multiple binary items as part of a batch call. In order to do this, you need to add all the binary items as multipart/mime attachments to your request, and need each operation to reference its binary items using the `attached_files` property in the operation. The `attached_files` property can take a comma separated list of attachment names in its value.


The following example shows how to upload 2 photos in a single batch call:



```
curl 
 -F 'access\_token=…' \
 -F 'batch=[{"method":"POST","relative\_url":"me/photos","body":"message=My cat photo","attached\_files":"file1"},{"method":"POST","relative\_url":"me/photos","body":"message=My dog photo","attached\_files":"file2"},]' \
 -F 'file1=@cat.gif' \
 -F 'file2=@dog.jpg' \
 https://graph.facebook.com
```


 

 -->
On This PageBatch RequestsBatch RequestComplex Batch RequestsErrorsTimeoutsBatch calls with JSONPUsing Multiple Access TokensUpload Binary DataFollow Us* 
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