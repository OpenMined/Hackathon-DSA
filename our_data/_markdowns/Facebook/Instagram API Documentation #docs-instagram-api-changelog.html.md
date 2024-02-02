Changelog - Instagram Platform

DocsToolsSupportLog InInstagram Platform* Instagram Graph API
	+ Overview
	+ Getting Started
	+ Guides
	+ Reference
	+ Changelog
* Instagram Basic Display API
* Sharing to Feed
* Sharing to Stories
* oEmbed
* Embed Button
* Business Login for Instagram
On This PageChangelogSeptember 12, 2023November 9, 2022October 31stJune 28, 2022June 27, 2022June 20, 2022May 27, 2022March 15, 2022November 9, 2021October 20, 2021October 5, 2021June 8, 2021May 26, 2021May 4, 2021April 14, 2021April 12, 2021April 9, 2021March 16, 2021Januray 26, 2021December 2, 2020November 10, 2020May 5, 2020December 3, 2019August 13, 2019May 22, 2019May 9, 2019October 31, 2018October 23, 2018June 7, 2018May 1, 2018April 24, 2018April 23, 2018March 13, 2018March 8, 2018February 22, 2018February 8, 2018Changelog
=========

This changelog refers to changes made for the Instagram Graph API.

### Related Changelogs

* Graph API Changelog
* Messenger Platform Changelog (includes Instagram Messaging)
* Marketing API Changelog
September 12, 2023
------------------

#### Deprecation of Media and User Insights

*Applies to v18.0+. Will apply to all versions on December 11, 2023.*

Duplicative and legacy Instagram insight metrics are being deprecated. Please see documentation for the endpoints and Instagram Insights for more information on which metrics to use in their place.

The following endpoints and metrics are affected:

* `GET /{ig-user-id}/insights`
	+ `AUDIENCE_GENDER_AGE`
	+ `AUDIENCE_LOCALE`
	+ `AUDIENCE_COUNTRY`
	+ `AUDIENCE_CITY`
* `GET /{ig-media-id}/insights`
	+ `CAROUSEL_ALBUM_IMPRESSIONS`
	+ `CAROUSEL_ALBUM_REACH`
	+ `CAROUSEL_ALBUM_ENGAGEMENT`
	+ `CAROUSEL_ALBUM_SAVED`
	+ `CAROUSEL_ALBUM_VIDEO_VIEWS`
	+ `TAPS_FORWARD`
	+ `TAPS_BACK`
	+ `EXITS`
	+ `ENGAGEMENT`

**Note:** `total_interactions`, which is listed as an alternative for some of the deprecated metrics, is currently only available using version 18.0 and does not work with older versions. When querying older versions before Dec 11, 2023, please use the `engagement` metric.`total_interactions`, which is listed as an alternative for some of the deprecated metrics, is currently only available using version 18.0 and does not work with older versions. When querying older versions before Dec 11, 2023, please use the `engagement` metric.

November 9, 2022
----------------

#### Instagram Webhooks

*Applies to all versions.*

The `ad_id` and `ad_title` will be returned in the `media` object of the `comments` field's `value` object when a person comments on a boosted Instagram post or Instagram ads post.

October 31st
------------

#### Reels – Product Tags

*Applies to all versions.*

Instagram Product Tagging API for Reels is made available. You can tag up to 30 products when publishing a reel.

June 28, 2022
-------------

#### Reels

*Applies to all versions.*

Reels are now supported. To publish a video as a reel, set the `media_type` parameter to `REELS` when creating a single media post container. Refer to the `POST /ig-user/media endpoint` reference to learn which parameters can be used with reels as well as requirements for reels videos.

**Note:** Beginning November 9, 2023, the `VIDEO` value for `media_type` will no longer be supported. Use the `REELS` media type to publish a video to your feed.

June 27, 2022
-------------

#### Legacy Instagram API Documentation

*Applies to all versions.*

The Legacy Instagram API developer documentation has been removed and now redirects to the Instagram Platform developer documentation.

June 20, 2022
-------------

#### Product Tagging

*Applies to all versions.*

You can now create and manage Instagram Shopping Product Tags on an Instagram Business's published media. Refer to the Product Tagging guide to learn how.

May 27, 2022
------------

#### Product Variants

*Applies to all versions.*

For partners in the Product Tagging beta, all product variants that match a query's search criteria will now be returned when searching a catalog for products.

March 15, 2022
--------------

#### Carousel Posts

*Applies to all versions.*

You can now use the Instagram API to publish posts containing multiple images and videos (carousel posts). Refer to the Content Publishing guide for complete publishing steps.

If your app has already been approved for permissions required for content publishing, it does not need to undergo App Review again to take advantage of this functionality.

November 9, 2021
----------------

#### Live Videos

*Applies to all versions.*

You can now use the Instagram API to get live video IG Media being broadcast by your app users, get comments on those videos, and use the Instagram Messaging API to send private replies (direct messages) to the comment authors. To support this functionality, the following changes have been made:

* a new GET /ig-user/live\_media edge can return live video IG Media being broadcast by your app user at the time of the request
* the `media` field on an IG Comment now returns and object containing both the ID (`id`) and published location (`media_product_type`) of the media upon which the comment was made
* a new `live_comments` Instagram Webhooks field can send notifications containing live comments made on your app users' live videos as they are being broadcast

Please refer to the Instagram Messaging API private replies documentation to learn how to send private replies to users who have commented on your app users' live video IG Media.

October 20, 2021
----------------

#### IG Comments

*Applies to all versions.*

Two new fields have been added to IG Comments:

* `from` — returns an object containing the IGSID (`id`) and username (`username`) of the comment creator.
* `parent_id` — returns the ID of the parent IG Comment if this comment was created on another IG Comment (i.e. a reply to another comment).

#### Instagram Webhooks

*Applies to all versions.*

The `comments` Instagram webhooks field now includes the following properties in the `value` field object:

* `from.id` — IGSID of the Instagram user who created the comment.
* `from.username` — Username of the Instagram user who created the comment
* `media.id` — ID of the IG Media upon which the comment was made.
* `media.media_product_type` — Surface (published location) of the IG Media upon which the comment was made.
* `parent_id` — ID of parent IG Comment if this comment was created on another IG Comment (i.e. a reply to another comment).

October 5, 2021
---------------

The following changes apply to Instagram TV videos created on or after October 5, 2021. Instagram TV videos created before this date are exempt from these changes.

* the `media_product_type` field will return `FEED` instead of `IGTV`
* the `video_title` field will not be returned
* Instagram Webhooks `comments` and `mentions` fields are now supported

On January 3, 2022, the changes above will apply to all API versions and all Instagram TV videos, regardless of video creation date. This means that starting January 3, 2022, apps using older API versions will be able to query Instagram TV videos (read support was introduced in v10.0 and limited to v10.0+).

Starting with v14.0, the `video_title` field will no longer be supported and the API will throw an error if the field is requested.

June 8, 2021
------------

#### Like Counts

*Applies to v11.0+. Will apply to all versions September 7, 2021.*

If indirectly querying an IG Media through another endpoint or field expansion, the `like_count` field will be omitted from API responses if the media owner has hidden like counts on it. Directly querying the IG Media (which can only be done by the IG Media owner) will return the actual like count, however, even if like counts have been hidden.

#### Time-based Pagination

*Applies to v11.0+*.

Added `since` and `until` parameters to the `GET /{ig-user-id}/media` endpoint to support time-based pagination.

May 26, 2021
------------

If indirectly querying an IG Media through another endpoint, the like\_count field will now return `0` if the app user does not own the media and the media owner has hidden like counts on it. Directly querying the IG Media, which can only be done by the IG Media owner, will return the actual like count, even if the owner has hidden like counts on the media.

May 4, 2021
-----------

Made a minor change to how we calculate the `online_followers` metric on IG Users.

April 14, 2021
--------------

Story IG Media interactions performed by users in Japan are no longer included in some `replies` metric calculations:

* For stories created by users in Japan, the `replies` metric will now return a value of `0`.
* For stories created by users outside Japan, the `replies` metric will return the number of replies, but replies made by users in Japan will not be included in the calculation.

April 12, 2021
--------------

Fixed a minor bug with reach metrics on story IG Media.

April 9, 2021
-------------

* The `status` field on an IG Container now returns an error subcode if the container's `error_code` field value is `ERROR`.
* The IG Media Insights `video_views` metric now supports albums and will return the sum of `video_views` on all videos in the album instead of `0`.

March 16, 2021
--------------

IGTV media is now supported in v10.0+. This applies to all endpoints except those used for content publishing and webhooks. To support this change, new `media_product_type` and `video_title` fields have been added to the IG Media node. IGTV media must have been shared to Instagram at the time of publish (**Post a Preview** or **Share Preview** to Feed enabled) in order to be accessible via the API.

Januray 26, 2021
----------------

The Content Publishing beta has ended and all developers can now publish media on Instagram Professional accounts. Refer to the Content Publishing guide for usage details.

December 2, 2020
----------------

In compliance with the European Union's ePrivacy Directive, messaging-related Story IG Media interactions performed by users in the European Economic Area (EEA) after December 1, 2020, will no longer be included in some metric calculations:

* For Stories created by users in the EEA, the `replies` metric will now return a value of `0`.
* For Stories created by users outside the EEA, the `replies` metric will return the number of replies, but replies made my users in the EEA will not be included in its calculation.

This change applies to all versions.

November 10, 2020
-----------------

* **IG User Insights** — The `follower_count` values now align more closely with their corresponding values displayed in the Instagram app. In addition, `follower_count` now returns a maximum of 30 days of data instead of 2 years. This change applies to v9.0+ and will apply to all versions May 9, 2021.

May 5, 2020
-----------

* **Hashtag Search** — *This change applies to v7.0+* — You can now request the `timestamp` field on IG Media returned by `GET /{ig-hashtag-id}/top_media` and `GET /{ig-hashtag-id}/recent_media` Hashtag Search queries. For example: `GET /{ig-hashtag-id}/top_media?fields=timestamp`.

December 3, 2019
----------------

* **Insights** — To align API behavior with Instagram app behavior, insights on IG Users are now only available on IG Users that have 100 or more followers.

August 13, 2019
---------------

* **Business Discovery** — The Business Discovery API can now be used to get data about other Instagram Creator accounts.

May 22, 2019
------------

* **Instagram Creator Accounts** — The API now supports Instagram Creator Accounts, with two exceptions. (1) The Content Publishing API cannot be used by Instagram Creators, and (2) the Business Discovery API can be used by Creators but can only target Businesses.

May 9, 2019
-----------

* **Webhooks** — The `story_insights` field now requires the `instagram_manage_insights` permission instead of `instagram_manage_comments`.

October 31, 2018
----------------

* **Hashtag Search API** — You can now search for media tagged with specific hashtags by using our new Hashtag Search API. `#spooky`!

October 23, 2018
----------------

* `/{ig-media-id}/comments` edge — `GET` requests made using API version 3.1 or older will have results returned in chronological order. Requests made using version 3.2+ will have results returned in reverse chronological order.

June 7, 2018
------------

* `/{ig-media-id}` node — You can now use field expansion to get the `permalink` field on media objects.

May 1, 2018
-----------

* **Business Verification** — In order to use the Instagram Graph API, all apps must undergo Business Verification, which is part of the App Review process and now required for all Instagram Graph API endpoints. Apps previously reviewed before May 1st, 2018, have to be reviewed again, and have until August 1st, 2018 to do so, or lose access to the API.

April 24, 2018
--------------

* `/{ig-comment-id}` node:
	+ Added a new `username` field.
	+ For `GET` requests, the `user` field will not be included in responses unless the User making the request owns the Comment; instead, we will return `username` for all commenters. This also applies to queries on Comments made through other APIs, such as the Mentions API.
* `/{ig-media-id}` node:
	+ Added a new `username` field.
	+ For `GET` requests, the `owner` field will not be included in responses unless the User making the request owns the media object; instead, we will return `username` for all commenters. This also applies to queries on media objects made through other APIs, such as the Mentions API.
April 23, 2018
--------------

* **Insights API** — Insights will now include ad activity generated through the API, Facebook ads interfaces, and Instagram's Promote feature. This affects the following metrics:

	+ `impressions`
	+ `reach`
March 13, 2018
--------------

* **Content Publishing API** — Beta partners can now use the `/{ig-user-id}/media` edge to tag locations and public Instagram users when publishing photos.

March 8, 2018
-------------

* **Public fields** — The `timestamp` field on the `/{ig-media-id}` node is now a public field and can be returned via field expansion.

February 22, 2018
-----------------

* **Public fields** — The `/{ig-user-id}`, `/{ig-comment-id}`, and `/{ig-media-id}` nodes will now return all public fields when accessed through an edge via field expansion. Refer to each node's reference document to see which fields are public.

February 8, 2018
----------------

* **Content Publishing API** — Beta partners can now include hashtags when publishing photos via the `/{ig-user-id}/media` edge. `#crazywildebeest` FTW!

On This PageChangelogSeptember 12, 2023November 9, 2022October 31stJune 28, 2022June 27, 2022June 20, 2022May 27, 2022March 15, 2022November 9, 2021October 20, 2021October 5, 2021June 8, 2021May 26, 2021May 4, 2021April 14, 2021April 12, 2021April 9, 2021March 16, 2021Januray 26, 2021December 2, 2020November 10, 2020May 5, 2020December 3, 2019August 13, 2019May 22, 2019May 9, 2019October 31, 2018October 23, 2018June 7, 2018May 1, 2018April 24, 2018April 23, 2018March 13, 2018March 8, 2018February 22, 2018February 8, 2018Follow Us* 
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