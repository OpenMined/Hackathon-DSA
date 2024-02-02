Paginated Results - Graph API










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
On This PagePaginated ResultsTraversing Paged ResultsCursor-based PaginationTime-based PaginationOffset-based PaginationNext StepsPaginated Results
=================


We cover the basics of Graph API terminology and structure in the Graph API overview. This document goes into more detail about the results from your API requests.


Traversing Paged Results
------------------------


When making an API request to a node or edge, you usually don't receive all of the results of that request in a single response. This is because some responses could contain thousands of objects so most responses are paginated by default.


### Cursor-based Pagination


Cursor-based pagination is the most efficient method of paging and should always be used when possible. A cursor refers to a random string of characters which marks a specific item in a list of data. The cursor will always point to the item, however it will be invalidated if the item is deleted or removed. Therefore, your app shouldn't store cursors or assume that they will be valid in the future.


When reading an edge that supports cursor pagination, you see the following JSON response:



```
{
 "data": [
 ... Endpoint data is here
 ],
 "paging": {
 "cursors": {
 "after": "MTAxNTExOTQ1MjAwNzI5NDE=",
 "before": "NDMyNzQyODI3OTQw"
 },
 "previous": "https://graph.facebook.com/{your-user-id}/albums?limit=25&before=NDMyNzQyODI3OTQw"
 "next": "https://graph.facebook.com/{your-user-id}/albums?limit=25&after=MTAxNTExOTQ1MjAwNzI5NDE="
 }
}
```
A cursor-paginated edge supports the following parameters:


* `before` : This is the cursor that points to the start of the page of data that has been returned.
* `after` : This is the cursor that points to the end of the page of data that has been returned.
* `limit` : This is the maximum number of objects that *may* be returned. A query may return fewer than the value of `limit` due to filtering. Do not depend on the number of results being fewer than the `limit` value to indicate that your query reached the end of the list of data, use the absence of `next` instead as described below. For example, if you set `limit` to 10 and 9 results are returned, there may be more data available, but one item was removed due to privacy filtering. Some edges may also have a maximum on the `limit` value for performance reasons. In all cases, the API returns the correct pagination links.
* `next` : The Graph API endpoint that will return the next page of data. If not included, this is the last page of data. Due to how pagination works with visibility and privacy, it is possible that a page may be empty but contain a `next` paging link. Stop paging when the `next` link no longer appears.
* `previous` : The Graph API endpoint that will return the previous page of data. If not included, this is the first page of data.


Don't store cursors. Cursors can quickly become invalid if items are added or deleted.


### Time-based Pagination


Time pagination is used to navigate through results data using Unix timestamps which point to specific times in a list of data.


When using an endpoint that uses time-based pagination, you see the following JSON response:



```
{
 "data": [
 ... Endpoint data is here
 ],
 "paging": {
 "previous": "https://graph.facebook.com/{your-user-id}/feed?limit=25&since=1364849754",
 "next": "https://graph.facebook.com/{your-user-id}/feed?limit=25&until=1364587774"
 }
}
```
A time-paginated edge supports the following parameters:


* `until` : A Unix timestamp or `strtotime` data value that points to the end of the range of time-based data.
* `since` : A Unix timestamp or `strtotime` data value that points to the start of the range of time-based data.
* `limit` : This is the maximum number of objects that *may* be returned. A query may return fewer than the value of `limit` due to filtering. Do not depend on the number of results being fewer than the `limit` value to indicate your query reached the end of the list of data, use the absence of `next` instead as described below. For example, if you set `limit` to 10 and 9 results are returned, there may be more data available, but one item was removed due to privacy filtering. Some edges may also have a maximum on the `limit` value for performance reasons. In all cases, the API returns the correct pagination links.
* `next` : The Graph API endpoint that will return the next page of data.
* `previous` : The Graph API endpoint that will return the previous page of data.


For consistent results, specify both `since` and `until` parameters. Also, it is recommended that the time difference is a maximum of 6 months.


### Offset-based Pagination


Offset pagination can be used when you do not care about chronology and just want a specific number of objects returned. Only use this if the edge does not support cursor or time-based pagination.


An offset-paginated edge supports the following parameters:


* `offset` : This offsets the start of each page by the number specified.
* `limit` : This is the maximum number of objects that *may* be returned. A query may return fewer than the value of `limit` due to filtering. Do not depend on the number of results being fewer than the `limit` value to indicate that your query reached the end of the list of data, use the absence of `next` instead as described below. For example, if you set `limit` to 10 and 9 results are returned, there may be more data available, but one item was removed due to privacy filtering. Some edges may also have a maximum on the `limit` value for performance reasons. In all cases, the API returns the correct pagination links.
* `next` : The Graph API endpoint that will return the next page of data. If not included, this is the last page of data. Due to how pagination works with visibility and privacy, it is possible that a page may be empty but contain a `next` paging link. Stop paging when the `next` link no longer appears.
* `previous` : The Graph API endpoint that will return the previous page of data. If not included, this is the first page of data.


Note that if new objects are added to the list of items being paged, the contents of each offset-based page will change.


Offset based pagination is not supported for all API calls. To get consistent results, we recommend you to paginate using the previous/next links we return in the response.


For objects that have many items returned, such as comments which can number in the tens of thousands, you may encounter limits while paging. The API will return an error when your app has reached the cursor limit:


```
{
 "error": {
 "message": "(#100) The After Cursor specified exceeds the max limit supported by this endpoint",
 "type": "OAuthException",
 "code": 100
 }
}
```
Next Steps
----------


Now that you are more familiar with the Graph API visit our Graph Explorer Tool Guide to explore the Graph without writing code, Common Uses to view the most common tasks performed, and the SDKs available.


On This PagePaginated ResultsTraversing Paged ResultsCursor-based PaginationTime-based PaginationOffset-based PaginationNext StepsFollow Us* 
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