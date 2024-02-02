Hashtag Search - Instagram Platform











DocsToolsSupportLog InInstagram Platform* Instagram Graph API
	+ Overview
	+ Getting Started
	+ Guides
		- Business Discovery
		- Content Publishing
		- Comment Moderation
		- Copyright Detection
		- Hashtag Search
		- Insights
		- Mentions
		- Product Tagging
		- Webhooks
	+ Reference
	+ Changelog
* Instagram Basic Display API
* Sharing to Feed
* Sharing to Stories
* oEmbed
* Embed Button
* Business Login for Instagram
On This PageHashtag SearchLimitationsRequirementsEndpointsCommon UsesGetting Media Tagged With A HashtagHashtag Search
==============


Find public IG Media that has been tagged with specific hashtags.


Limitations
-----------


* You can query a maximum of 30 unique hashtags on behalf of an Instagram Business or Creator Account within a rolling, 7 day period. Once you query a hashtag, it will count against this limit for 7 days. Subsequent queries on the same hashtag within this time frame will not count against your limit, and will not reset its initial query 7 day timer.
* Personally identifiable information will not be included in responses.
* You cannot comment on hashtagged media objects discovered through the API.
* Hashtags on Stories are not supported.
* Emojis in hashtag queries are not supported.
* The API will return a generic error for any requests that include hashtags that we have deemed sensitive or offensive.


Requirements
------------


In order to use this API, you must undergo App Review and request approval for:


* the `Instagram Public Content Access` feature
* the `instagram_basic` permission


Endpoints
---------


The Hashtag Search API consists of the following nodes and edges:


* `GET /ig_hashtag_search` — to get a specific hashtag's node ID
* `GET /{ig-hashtag-id}` — to get data about a hashtag
* `GET /{ig-hashtag-id}/top_media` — to get the most popular photos and videos that have a specific hashtag
* `GET /{ig-hashtag-id}/recent_media` — to get the most recently published photos and videos that have a specific hashtag
* `GET /{ig-user-id}/recently_searched_hashtags` — to determine the unique hashtags an Instagram Business or Creator Account has searched for in the current week


Refer to each endpoint's reference documentation for supported fields, parameters, and usage requirements.


Common Uses
-----------


### Getting Media Tagged With A Hashtag


To get all of the photos and videos that have a specific hashtag, first use the `/ig_hashtag_search` endpoint and include the hashtag and ID of the Instagram Business or Creator Account making the query. For example, if the query is being made on behalf of the Instagram Business Account with the ID `17841405309211844`, you could get the ID for the "#coke" hashtag by performing the following query:



```
GET graph.facebook.com/ig\_hashtag\_search
 ?user\_id=17841405309211844
 &q=coke
```
This will return the ID for the “#Coke” hashtag node:



```
{
 "id" : "17873440459141021"
}
```
Now that you have the hashtag ID (`17873440459141021`), you can query its `/top_media` or `/recent_media` edge and include the Business Account ID to get a collection of media objects that have the “#coke” hashtag. For example:



```
GET graph.facebook.com/17873440459141021/recent\_media
 ?user\_id=17841405309211844
```
This would return a response that looks like this:



```
{
 "data": [
 {
 "id": "17880997618081620"
 },
 {
 "id": "17871527143187462"
 },
 { 
 "id": "17896450804038745" 
 }
 ]
}
```
On This PageHashtag SearchLimitationsRequirementsEndpointsCommon UsesGetting Media Tagged With A HashtagFollow Us* 
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