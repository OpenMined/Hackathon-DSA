Insights - Instagram Platform

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
On This PageInsightsLimitationsUTCEndpointsExamplesGetting Account MetricsGetting Media MetricsInsights
========

You can use the Instagram Graph API to get social interaction metrics for IG Users and their IG Media objects. Amounts for each metric are calculated upon API request.

Due to privacy rules, messaging-related Story IG Media interactions performed by users in some regions will no longer be included in some metric calculations. These regions include: Europe starting December 1, 2020 and Japan starting April 14, 2021.

* For Stories created by users in affected regions, the `replies` metric will now return a value of `0`.
* For Stories created by users outside affected regions, the `replies` metric will return the number of replies, but replies made by users in affected regions will not be included in the calculation.

Limitations
-----------

* Some metrics are not available on IG Users with fewer than 100 followers.
* The API only reports organic interaction metrics; interactions on ads containing a media object are not counted.
* Metrics data is stored for 2 years.
* You can only get insights for a single user at a time.
* You cannot get insights for Facebook Pages.
* Stories insights are only available for 24 hours, even if the stories are archived or highlighted. If you want to get the latest insights for a story before it expires, set up a Webhook for the `Instagram` topic and subscribe to the `story_insights` field.
* Insights on album child IG Media is not supported.
* If insights data you are requesting does not exist or is currently unavailable the API will return an empty data set instead of `0` for individual metrics.

UTC
---

Timestamps in API responses use UTC with zero offset and are formatted using ISO-8601. For example: `2019-04-05T07:56:32+0000`

Endpoints
---------

The API consists of the following endpoints:

* `GET /{ig-media-id}/insights` — gets metrics on a media object
* `GET /{ig-user-id}/insights` — gets metrics on an Instagram Business Account or Instagram Creator account.

Refer to each endpoint's reference documentation for available metrics, parameters, and permission requirements.

Examples
--------

### Getting Account Metrics

To get metrics on an Instagram Business or Creator Account, query the `GET /{ig-user-id}/insights` edge and specify the metrics you want returned.

#### Sample Request

```
GET graph.facebook.com/17841405822304914/insights
 ?metric=impressions,reach,profile\_views
 &period=day
```
#### Sample Response

```
{
 "data": [
 {
 "name": "impressions",
 "period": "day",
 "values": [
 {
 "value": 32,
 "end\_time": "2018-01-11T08:00:00+0000"
 },
 {
 "value": 32,
 "end\_time": "2018-01-12T08:00:00+0000"
 }
 ],
 "title": "Impressions",
 "description": "Total number of times the Business Account's media objects have been viewed",
 "id": "instagram\_business\_account\_id/insights/impressions/day"
 },
 {
 "name": "reach",
 "period": "day",
 "values": [
 {
 "value": 12,
 "end\_time": "2018-01-11T08:00:00+0000"
 },
 {
 "value": 12,
 "end\_time": "2018-01-12T08:00:00+0000"
 }
 ],
 "title": "Reach",
 "description": "Total number of times the Business Account's media objects have been uniquely viewed",
 "id": "instagram\_business\_account\_id/insights/reach/day"
 },
 {
 "name": "profile\_views",
 "period": "day",
 "values": [
 {
 "value": 15,
 "end\_time": "2018-01-11T08:00:00+0000"
 },
 {
 "value": 15,
 "end\_time": "2018-01-12T08:00:00+0000"
 }
 ],
 "title": "Profile Views",
 "description": "Total number of users who have viewed the Business Account's profile within the specified period",
 "id": "instagram\_business\_account\_id/insights/profile\_views/day"
 }
 ]
}
```
### Getting Media Metrics

To get metrics on a media object, query the `GET /{ig-media-id}/insights` edge and specify the metrics you want returned.

#### Sample Request

```
GET graph.facebook.com/{media-id}/insights
 ?metric=engagement,impressions,reach
```
#### Sample Response

```
{
 "data": [
 {
 "name": "engagement",
 "period": "lifetime",
 "values": [
 {
 "value": 8
 }
 ],
 "title": "Engagement",
 "description": "Total number of likes and comments on the media object",
 "id": "media\_id/insights/engagement/lifetime"
 },
 {
 "name": "impressions",
 "period": "lifetime",
 "values": [
 {
 "value": 13
 }
 ],
 "title": "Impressions",
 "description": "Total number of times the media object has been seen",
 "id": "media\_id/insights/impressions/lifetime"
 },
 {
 "name": "reach",
 "period": "lifetime",
 "values": [
 {
 "value": 13
 }
 ],
 "title": "Reach",
 "description": "Total number of unique accounts that have seen the media object",
 "id": "media\_id/insights/reach/lifetime"
 }
 ]
}
```
On This PageInsightsLimitationsUTCEndpointsExamplesGetting Account MetricsGetting Media MetricsFollow Us* 
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