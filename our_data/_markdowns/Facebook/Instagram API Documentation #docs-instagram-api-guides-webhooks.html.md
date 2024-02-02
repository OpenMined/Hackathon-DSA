Webhooks - Instagram Platform

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
On This PageSet Up Webhooks for InstagramReceive Live Webhook NotificationsLimitationsStep 1: Create an EndpointInstagram FieldsStep 2: Enable Page SubscriptionsEndpoint RequirementsCommon UsesCapture Story InsightsReply to Comment @MentionsGet the Comment's ContentsParse the Payload and RespondReply to Caption @MentionsGet the Caption's ContentsThe following content is from the Webhooks product documentation. Please refer to the Webhooks documentation if you are unfamiliar with Webhooks.

Set Up Webhooks for Instagram
=============================

Webhooks for Instagram allow you to receive real-time notifications whenever someone comments on the Media objects of your app users; @mentions your app users; or when Stories of your app users expire.

Receive Live Webhook Notifications
----------------------------------

To receive live webhook notifications, the following conditions must be satisfied:

* Your app must have **Instagram** webhooks configured and appropriate **fields** subscribed to in the App Dashboard.
* For Consumer apps, they must be in Live Mode.
* For Business apps, they must have permissions with an Advanced Access level. You can request Advanced Access for permissions as shown here:

If the app permissions don't have an access level of **Advanced Access**, the app doesn't receive webhook notifications.

* The app user must have granted your app appropriate permissions (instagram\_manage\_insights for Stories, instagram\_manage\_comments for Comments and @Mentions).
* The Page connected to the app user's account must have Page subscriptions enabled.
* The Business connected to the app user's Page must be **verified**.
* The owner of the Media object upon which the comment or @mention appears must not have set their account to private.

### Limitations

* Webhook notifications for Comments on albums don't include the album ID. Get the album ID by querying the Comment ID in the webhook and request its `media` field.
* Apps don't receive a webhook notifications if the Media where the comment or @mention appears was created by a private account.
* Story insights metrics with counts of less than 5 are returned as `-1`.
* Apps only receive webhook notifications for comments on live IG Media if the media is on broadcast.
* Reels are not supported.
* Your app must have successfully completed App Review (advanced access) to receive webhooks notifications for `comments` and `live_comments` webhooks fields.

Step 1: Create an Endpoint
--------------------------

Create an endpoint that accepts and processes webhooks. During the configuration, select the **Instagram Graph API** object, click **Set up**, and subscribe to one or more Instagram fields.

### Instagram Fields

| Field | Description | Permissions Required |
| --- | --- | --- |
| `comments` | Comments on an IG Media owned by your app's Instagram user.
The `ad_id` and `ad_title` will be returned in the media object when a person comments on a boosted Instagram post or Instagram ads post. This may result in duplicate webhook notifications.
 | * instagram\_manage\_comments
* pages\_manage\_metadata
* pages\_read\_engagement **or**
pages\_show\_list
 |
| `live_comments` | Comments on a live IG Media owned by your app's Instagram user. | * instagram\_manage\_comments
* pages\_manage\_metadata
* pages\_read\_engagement **or**
pages\_show\_list
 |
| `mentions` | @mentions for your app's Instagram user in a comment. | * instagram\_manage\_comments
* pages\_manage\_metadata
* pages\_read\_engagement **or**
pages\_show\_list
 |
| `story_insights` | Metrics describing interactions on a story. Sent 1 hour after the story expires. | * instagram\_manage\_insights
* pages\_manage\_metadata
* pages\_read\_engagement **or**
pages\_show\_list
 |
Step 2: Enable Page Subscriptions
---------------------------------

Your app must enable Page subscriptions on the Page connected to the app user's account by sending a `POST` request to the Page Subscribed Apps edge and subscribing to any Page field.

### Endpoint Requirements

* the app user's Page Access Token
* pages\_manage\_metadata

#### Request Syntax

```
POST /{page-id}/subscribed\_apps
 ?access\_token={access-token}
 &subscribed\_fields={fields}
```
#### Request Parameters

| 
 Value Placeholder
  | 
 Value Description
  |
| --- | --- |
| `{page_id}` | ID of the Page connected to the app user's account. |
| `{access_token}` | App user's Page access tToken. |
| `{fields}` | A Page field (example: `feed`). |
Your app does not receive notifications for changes to a field unless you configure Page subscriptions in the App Dashboard and subscribe to that field.

#### Sample Request

```
curl -i -X POST \
 "https://graph.facebook.com/v19.0/1755847768034402/subscribed\_apps?subscribed\_fields=feed&access\_token=EAAFB..."
```
##### Sample Response

```
{
 "success": true
}
```
Common Uses
-----------

### Capture Story Insights

If you subscribe to the `story_insights` field, we send your endpoint a webhook notification containing user interaction metrics on a story, after the story has expired.

#### Sample Story Insights Payload

```
[
 {
 "entry": [
 {
 "changes": [
 {
 "field": "story\_insights",
 "value": {
 "media\_id": "18023345989012587",
 "exits": 1,
 "replies": 0,
 "reach": 17,
 "taps\_forward": 12,
 "taps\_back": 0,
 "impressions": 28
 }
 }
 ],
 "id": "17841405309211844", // Instagram Business or Creator Account ID
 "time": 1547687043
 }
 ],
 "object": "instagram"
 }
]
```
### Reply to Comment @Mentions

If you subscribe to the `mentions` field, we send your endpoint a webhook notification whenever an Instagram user @mentions an Instagram Business or Creator Account in a comment or caption.

For example, here's a sample comment webhook notification payload sent for an Instagram Business Account (`17841405726653026`):

#### Sample Comment @Mention Payload

```
[
 {
 "entry": [
 {
 "changes": [
 {
 "field": "mentions",
 "value": {
 "comment\_id": "17894227972186120",
 "media\_id": "17918195224117851"
 }
 }
 ],
 "id": "17841405726653026",
 "time": 1520622968
 }
 ],
 "object": "instagram"
 }
]
```
### Get the Comment's Contents

To get the comment's contents, use the `comment_id` property to query the `GET /{ig-user-id}/mentioned_comment` edge:

#### Sample Query

```
GET https://graph.facebook.com/17841405726653026
 ?fields=mentioned\_comment.comment\_id(17894227972186120)
```
#### Sample Response

```
{
 "mentioned\_comment": {
 "timestamp": "2018-03-20T00:05:29+0000",
 "text": "@bluebottle challenge?",
 "id": "17894227972186120"
 },
 "id": "17841405726653026"
}
```
### Parse the Payload and Respond

When you get the response, parse the payload for the `text` property to determine if you want to respond to the comment. To respond, use the webhook notification payload's `caption_id` and `media_id` property values to query the `POST /{ig-user-id}/mentions` endpoint:

#### Sample Query

```
curl -i -X POST \
 -d "comment\_id=17894227972186120" \
 -d "media\_id=17918195224117851" \
 -d "message=Challenge%20accepted!" \
 -d "access\_token={access-token}" \
 "https://graph.facebook.com/17841405726653026/mentions"
```
#### Sample Response

```
{
 "id": "17911496353086895"
}
```
### Reply to Caption @Mentions

If you subscribe to the `mentions` field, we send your endpoint a webhook notification whenever a user @mentions an Instagram Business or Creator Account in a comment or caption on a media object not owned by the Business or Creator.

For example, here's a sample caption @mention webhook notification sent for an Instagram Business Account (`17841405726653026`):

#### Sample Caption @Mention Webhook Notification

```
[
 {
 "entry": [
 {
 "changes": [
 {
 "field": "mentions",
 "value": {
 "media\_id": "17918195224117851"
 }
 }
 ],
 "id": "17841405726653026",
 "time": 1520622968
 }
 ],
 "object": "instagram"
 }
]
```
### Get the Caption's Contents

To get the caption's contents, use the `media_id` property to query the `GET /{ig-user-id}/mentioned_media` edge:

#### Sample Query

```
GET https://graph.facebook.com/17841405726653026
 ?fields=mentioned\_media.media\_id(17918195224117851){caption,media\_type}
```
#### Sample Response

```
{
 "mentioned\_media": {
 "caption": "@bluebottle There can be only one!",
 "media\_type": "IMAGE",
 "id": "17918195224117851"
 },
 "id": "17841405726653026"
}
```
### Parse the Payload and Respond

When you get the response, parse the payload for the `caption` property to determine if you want to respond to the comment. To respond, use the webhook `media_id` property to query the `POST /{ig-user-id}/mentions` edge:

#### Sample Query

```
curl -i -X POST \
 -d "media\_id=17918195224117851" \
 -d "message=MacLeod%20agrees!" \
 -d "access\_token={access-token}" \
 "https://graph.facebook.com/17841405726653026/mentions"
```
#### Sample Response

```
{
 "id": "17911496353086895"
}
```
On This PageSet Up Webhooks for InstagramReceive Live Webhook NotificationsLimitationsStep 1: Create an EndpointInstagram FieldsStep 2: Enable Page SubscriptionsEndpoint RequirementsCommon UsesCapture Story InsightsReply to Comment @MentionsGet the Comment's ContentsParse the Payload and RespondReply to Caption @MentionsGet the Caption's ContentsFollow Us* 
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