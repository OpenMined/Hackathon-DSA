Comment Moderation - Instagram Platform











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
On This PageComment ModerationEndpointsExamplesGetting & Replying to CommentsComment Moderation
==================


You can use the Instagram Graph API to get comments, reply to comments, delete comments, hide/unhide comments, and disable/enable comments on IG Media owned by your app users.


You can use the Instagram Messaging API to send private replies (direct messages) to users who have commented on your app users' live video IG Media. Refer to the Instagram Messaging's private replies documentation to learn how.


Endpoints
---------


The API consists of the following endpoints. Refer to each endpoint's reference documentation for parameter and permission requirements.


* `GET /{ig-media-id}/comments` — Get comments on an IG Media.
* `GET /{ig-comment-id}/replies` — Get replies on an IG Comment.
* `POST /{ig-comment-id}/replies` — Reply to an IG Comment.
* `POST /{ig-comment-id}` — Hide/unhide an IG Comment.
* `POST /{ig-media-id}` — Disable/enable comments on an IG Media.
* `DELETE /{ig-comment-id}` — Delete an IG Comment.


Examples
--------


### Getting & Replying to Comments


You can get all of the comments on a media object, analyze and filter the returned data set against specific criteria, then reply to any comments that match your criteria.


First, query the `GET /{ig-media-id}/comments` endpoint to get all of the comments and their IDs on the media object:


#### Sample Request



```
GET graph.facebook.com
 /17895695668004550/comments
```
#### Sample Response



```
{
 "data": [
 {
 "timestamp": "2017-08-31T18:10:30+0000",
 "text": "I love this!",
 "id": "17873440459141021"
 },
 {
 "timestamp": "2017-08-31T19:16:02+0000",
 "text": "This is awesome!",
 "id": "17870913679156914"
 },
 ... // results truncated for brevity
 ]
}
```
Next, parse the returned results for comments that match whatever criteria you are using and use the matching comments to reply in the comment thread to the Instagram users who made the comments:


#### Sample Request



```
POST graph.facebook.com
 /17870913679156914/replies?message=Thanks%20for%20sharing!
```
#### Sample Response



```
{
 "id": "17873440459141029"
}
```
If you have a lot of comments that you want to reply to, you could batch the replies into a single request.


On This PageComment ModerationEndpointsExamplesGetting & Replying to CommentsFollow Us* 
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