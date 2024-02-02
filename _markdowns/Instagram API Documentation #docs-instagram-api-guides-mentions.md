Mentions - Instagram Platform











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
On This PageMentionsLimitationsEndpointsWebhooksExamplesListening for and Replying to Comment @MentionsListening for and Replying to Caption @MentionsMentions
========


Identify captions, comments, and IG Media in which an Instagram Business or Creator's alias has been tagged or @mentioned.


Limitations
-----------


* Mentions on Stories are not supported.
* Commenting on photos in which you were tagged is not supported.
* Webhooks will not be sent if the Media upon which the comment or @mention appears was created by an account that is set to private.


Endpoints
---------


The API consists of the following endpoints:


* `GET /{ig-user-id}/tags` — to get the media objects in which a Business or Creator Account has been tagged
* `GET /{ig-user-id}?fields=mentioned_comment` — to get data about a comment that an Business or Creator Account has been @mentioned in
* `GET /{ig-user-id}?fields=mentioned_media` — to get data about a media object on which a Business or Creator Account has been @mentioned in a caption
* `POST /{ig-user-id}/mentions` — to reply to a comment or media object caption that a Business or Creator Account has been @mentioned in by another Instagram user


Refer to each endpoint reference document for usage instructions.


Webhooks
--------


Subscribe to the `mentions` field to recieve Instagram Webhooks notifications whenever an Instagram user mentions an Instagram Business or Creator Account. Note that we do not store Webhooks notification data, so if you set up a Webhook that listens for mentions, you should store any received data if you plan on using it later.


Examples
--------


### Listening for and Replying to Comment @Mentions


You can listen for comment @mentions and reply to any that meet your criteria:


1. Set up an Instagram webhook that's subscribed to the `mentions` field.
2. Set up a script that can parse the Webhooks notifications and identify comment IDs.
3. Use the IDs to query the `GET /{ig-user-id}/mentioned_comment` endpoint to get more information about each comment.
4. Analyze the returned results to identify any comments that meet your criteria.
5. Use the `POST /{ig-user-id}/mentions` endpoint to reply to those comments.


The reply will appear as a sub-thread comment on the comment in which the Business or Creator Account was mentioned.


### Listening for and Replying to Caption @Mentions


You can listen for caption @mentions and reply to any that meet your criteria:


1. Set up an Instagram webhook that's subscribed to the `mentions` field.
2. Set up a script that can parse the Webhooks notifications and identify media IDs.
3. Use the IDs to query the `GET /{ig-user-id}/mentioned_media` endpoint to get more information about each media object.
4. Analyze the returned results to identify media objects with captions that meet your criteria.
5. Use the `POST /{ig-user-id}/mentions` endpoint to comment on those media objects.


On This PageMentionsLimitationsEndpointsWebhooksExamplesListening for and Replying to Comment @MentionsListening for and Replying to Caption @MentionsFollow Us* 
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