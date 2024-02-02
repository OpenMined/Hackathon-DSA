Business Discovery - Instagram Platform

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
On This PageBusiness DiscoveryLimitationsEndpointsExamplesGetting an Account's Follower & Media CountGetting MediaGetting Basic Metrics on MediaBusiness Discovery
==================

You can use the Instagram Graph API to get basic metadata and metrics about other Instagram Business and Creator Accounts.

Limitations
-----------

Data about age-gated Instagram Business Accounts will not be returned.

Endpoints
---------

The API consists of the following endpoints. Refer to the endpoint's reference documentation for parameter and permission requirements.

* `GET /{ig-user-id}/business_discovery`

Examples
--------

### Getting an Account's Follower & Media Count

This sample query shows how to get the number of followers and number of published media objects on the Blue Bottle Coffee Instagram Business Account. Notice that business discovery queries are performed on the Instagram Business or Creator Account's ID (in this case, `17841405309211844`), not the username of the Instagram Business or Creator Account that you are attempting to get data about (`bluebottle` in this example).

#### Sample Request

```
curl -i -X GET \
 "https://graph.facebook.com/v3.2/17841405309211844?fields=business\_discovery.username(bluebottle){followers\_count,media\_count}&access\_token={access-token}"
```
#### Sample Response

```
{
 "business\_discovery": {
 "followers\_count": 267793,
 "media\_count": 1205,
 "id": "17841401441775531" // Blue Bottle's Instagram Account ID
 },
 "id": "17841405309211844" // ID of the Instagram account performing the query
}
```
### Getting Media

Since you can make nested requests by specifying an edge via the `fields` parameter, you can request the targeted Business or Creator Account's `media` edge to get all of its published media objects:

#### Sample Request

```
curl -i -X GET \
 "https://graph.facebook.com/v3.2/17841405309211844?fields=business\_discovery.username(bluebottle){followers\_count,media\_count,media}&access\_token={access-token}"
```
#### Sample Response

```
{
 "business\_discovery": {
 "followers\_count": 267793,
 "media\_count": 1205,
 "media": {
 "data": [
 {
 "id": "17858843269216389"
 },
 {
 "id": "17894036119131554"
 },
 {
 "id": "17894449363137701"
 },
 {
 "id": "17844278716241265"
 },
 ... // results truncated for brevity
 ],
 "id": "17841401441775531"
 },
 },
 "id": "17841405309211844"
}
```
### Getting Basic Metrics on Media

You can use both nested requests and field expansion to get public fields for a Business or Creator Account's media objects. Note that this does not grant you permission to access media objects directly — performing a `GET` on any returned IG Media will fail due to insufficient permissions.

For example, here's how to get the number of comments and likes for each of the media objects published by Blue Bottle Coffee:

#### Sample Request

```
curl -i -X GET \
 "https://graph.facebook.com/v3.2/17841405309211844?fields=business\_discovery.username(bluebottle){followers\_count,media\_count,media{comments\_count,like\_count}}&access\_token={access-token}"
```
#### Sample Response

```
{
 "business\_discovery": {
 "followers\_count": 267793,
 "media\_count": 1205,
 "media": {
 "data": [
 {
 "comments\_count": 50,
 "like\_count": 5841,
 "id": "17858843269216389"
 },
 {
 "comments\_count": 11,
 "like\_count": 2998,
 "id": "17894036119131554"
 },
 {
 "comments\_count": 28,
 "like\_count": 3644,
 "id": "17894449363137701"
 },
 {
 "comments\_count": 43,
 "like\_count": 4943,
 "id": "17844278716241265"
 },
 {
 "comments\_count": 60,
 "like\_count": 9347,
 "id": "17899363132086521"
 },
 {
 "comments\_count": 63,
 "like\_count": 6913,
 "id": "17893114378137541"
 },
 {
 "comments\_count": 16,
 "like\_count": 2791,
 "id": "17886057709171561"
 },
 {
 "comments\_count": 15,
 "like\_count": 3895,
 "id": "17856337633208377"
 },
 ],
 },
 "id": "17841401441775531"
 },
 "id": "17841405976406927"
}
```
On This PageBusiness DiscoveryLimitationsEndpointsExamplesGetting an Account's Follower & Media CountGetting MediaGetting Basic Metrics on MediaFollow Us* 
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