Content Publishing - Instagram Platform

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
On This PageContent PublishingRequirementsAccess TokensPermissionsPublic ServerPage Publishing AuthorizationLimitationsRate LimitEndpointsSingle Media PostsCarousel PostsReels PostsStory PostsCollaborator TagsLocation TagsProduct TagsUser TagsTroubleshootingErrorsContent Publishing
==================

You can use the Instagram Graph API to publish single images, videos, reels (i.e., single media posts), or posts containing multiple images and videos (carousel posts) on Instagram Professional accounts.

Beginning July 1, 2023, all single feed videos published through the Instagram Content Publishing API will be shared as reels.

Requirements
------------

### Access Tokens

All requests must include the app user's User access token.

### Permissions

Publishing relies on a combination of the following permissions. The exact combination depends on which endpoints your app uses. Refer to our endpoint references to determine which permissions each endpoint requires.

* ads\_management
* business\_management
* instagram\_basic
* instagram\_content\_publish
* pages\_read\_engagement

If your app will be used by app users who do not have a role on your app or a role in a Business that has claimed your app, you must request approval for each permission via App Review before non-role app users can grant them to your app.

### Public Server

We cURL media used in publishing attempts so the media must be hosted on a publicly accessible server at the time of the attempt.

### Page Publishing Authorization

Instagram Professional accounts connected to a Page that requires Page Publishing Authorization (PPA) cannot be published to until PPA has been completed.

It's possible that an app user may be able to perform Tasks on a Page that initially does not require PPA but later requires it. In this scenario, the app user would not be able to publish content to their Instagram Professional account until completing PPA. Since there's no way for you to determine if an app user's Page requires PPA, we recommend that you advise app users to preemptively complete PPA.

### Limitations

* JPEG is the only image format supported. Extended JPEG formats such as MPO and JPS are not supported.
* Shopping tags are not supported.
* Branded content tags are not supported.
* Filters are not supported.
* Publishing to Instagram TV is not supported.

For additional limitations, refer to each endpoint's reference.

### Rate Limit

Instagram accounts are limited to 50 API-published posts within a 24-hour moving period. Carousels count as a single post. This limit is enforced on the `POST /{ig-user-id}/media_publish` endpoint when attempting to publish a media container. We recommend that your app also enforce the publishing rate limit, especially if your app allows app users to schedule posts to be published in the future.

To check an Instagram Professional account's current rate limit usage, query the `GET /{ig-user-id}/content_publishing_limit` endpoint.

Endpoints
---------

The API consists of the following endpoints. Refer to each endpoint's reference document for usage requirements.

* `POST /{ig-user-id}/media` — upload media and create media containers.
* `POST /{ig-user-id}/media_publish` — publish uploaded media using their media containers.
* `GET /{ig-container-id}?fields=status_code` — check media container publishing eligibility and status.
* `GET /{ig-user-id}/content_publishing_limit` — check app user's current publishing rate limit usage.

Single Media Posts
------------------

Publishing single image, video, story or reel is a two-step process:

1. Use the `POST /{ig-user-id}/media` endpoint to create a container from an image or video hosted on your public server.
2. Use the `POST /{ig-user-id}/media_publish` endpoint to publish the container.

Step 1 of 2: Create Container
Let's say you have an image at...

```
https://www.example.com/images/bronz-fonz.jpg
```
... that you want to publish with the hashtag "#BronzFonz" as its caption. Send a request to the `POST /{ig-user-id}/media` endpoint:

#### Sample Request

```
POST https://graph.facebook.com/v19.0/17841400008460056/media
 ?image\_url=https://www.example.com/images/bronz-fonz.jpg
 &caption=#BronzFonz
```
This returns a container ID for the image.

#### Sample Response

```
{
 "id": "17889455560051444" // IG Container ID
}
```
Step 2 of 2: Publish Container
Use the `POST /{ig-user-id}/media_publish` endpoint to publish the container ID returned in the previous step.

#### Sample Request

```
POST https://graph.facebook.com/v19.0/17841400008460056/media\_publish
 ?creation\_id=17889455560051444
```
#### Sample Response

```
{
 "id": "17920238422030506" // IG Media ID
}
```
Carousel Posts
--------------

You may publish up to 10 images, videos, or a mix of the two in a single post (a carousel post). Publishing carousels is a three step process:

1. Use the `POST /{ig-user-id}/media` endpoint to create individual item containers for each image and video that will appear in the carousel.
2. Use the `POST /{ig-user-id}/media` endpoint again to create a single carousel container for the items.
3. Use the `POST /{ig-user-id}/media_publish` endpoint to publish the carousel container.

Carousel posts count as a single post against the account's rate limit.

Limitations
* Carousels cannot be boosted.
* Carousels are limited to 10 images, videos, or a mix of the two.
* Carousel images are all cropped based on the first image in the carousel, with the default being a 1:1 aspect ratio.

Step 1 of 3: Create item container
Use the `POST /{ig-user-id}/media` endpoint to create an item container for the image or video that will appear in a carousel. Carousels may have up to 10 total images, videos, or a mix of the two.

```
POST /{ig-user-id}/media
```
#### Parameters

The following parameters are **required**. Refer to the `POST /{ig-user-id}/media` endpoint reference for additional supported parameters.

* `is_carousel_item` — Set to `true`. Indicates image or video will appear in a carousel.
* `image_url` — (images only) The path to the image. We will cURL your image using the passed in URL so it must be on a public server.
* `media_type` — (videos only) Set to `VIDEO`. Indicates media is a video.
* `video_url` — (videos only) Path to the video. We will cURL your video using the passed in URL so it must be on a public server.

If the operation is successful, the API will return an item container ID which can be used when creating the carousel container.

Repeat this process for each image or video that should appear in the carousel.

#### Sample Request

```
curl -i -X POST \
"https://graph.facebook.com/v19.0/90010177253934/media?image\_url=https%3A%2F%2Fsol...&is\_carousel\_item=true&access\_token=EAAOc..."
```
#### Sample Response

```
{
 "id": "17899506308402767"
}
```
Step 2 of 3: Create carousel container
Use the `POST /{ig-user-id}/media` endpoint to create a carousel container.

```
POST /{ig-user-id}/media
```
#### Parameters

The following parameters are **required**. Refer to the `POST /{ig-user-id}/media` endpoint reference for additional supported parameters.

* `media_type` — Set to `CAROUSEL`. Indicates container is for a carousel.
* `children` — An array of up to 10 container IDs of each image and video that should appear in the published carousel. Carousels can have up to 10 total images, videos, or a mix of the two.

#### Sample Request

```
curl -i -X POST \
"https://graph.facebook.com/v19.0/90010177253934/media?caption=Fruit%20candies&media\_type=CAROUSEL&children=17899506308402767%2C18193870522147812%2C17853844403701904&access\_token=EAAOc..."
```
#### Sample Response

```
{
 "id": "18000748627392977"
}
```
Step 3 of 3: Publish carousel container
Use the `POST /{ig-user-id}/media_publish` endpoint to publish a carousel container (a carousel post). Accounts are limited to 50 published posts within a 24-hour period. Publishing a carousel counts as a single post.

```
POST /{ig-user-id}/media\_publish
```
#### Parameters

The following parameters are required.

* `creation_id` — The carousel container ID.

If the operation is successful the API will return a carousel album IG Media ID.

#### Sample Request

```
curl -i -X POST \
"https://graph.facebook.com/v19.0/90010177253934/media\_publish?creation\_id=18000748627392977&access\_token=EAAOc..."
```
#### Sample Response

```
{
 "id": "90010778390276"
}
```
Reels Posts
-----------

Reels are short-form videos that are eligible to appear in the **Reels** tab of the Instagram app if they meet certain specifications and are selected by our algorithm. To publish a reel, follow the steps for publishing a single media post and include the `media_type=REELS` parameter along with the path to the video using the `video_url` parameter.

Reels are not a new media type, even though you set `media_type=REELS` when you publish a reel. If you publish a reel and then request its `media_type` field, the value returned is `VIDEO`. To determine if a published video has been designated as a reel, request its `media_product_type` field instead.

You can use the code sample on GitHub (insta\_reels\_publishing\_api\_sample) to learn how to publish Reels to Instagram.

To make it more convenient for developers, Meta has published the full set of Graph API calls for Instagram Reels on the Postman API Platform. For more information, see Postman Collections for Facebook Reels and Instagram Reels.

For more information about Reels, see Reels Developer Documentation.

Story Posts
-----------

Only business accounts can publish stories with the Content Publising API at this time.

Stories are videos and images that are posted as IG stories on Instagram. To publish a story, follow the same steps for publishing a single media post and include the `media_type=STORIES` parameter along with the path to the image/video using the `image_url` or `video_url` parameter.

**Note:** Stories are not a new media type even though you are setting `media_type=STORIES` when publishing a story. If you publish a story and then request its `media_type` field, the value will be returned as `IMAGE/VIDEO`. To determine if a published image/video has been designated as a story, request its `media_product_type` field instead.

Collaborator Tags
-----------------

You can add public Instagram users in an image, carousel and reel as a collaborators and they will receive an invite to be a collaborator for that particular media.
To tag users in an image, follow the Single Media Posts steps above, but when creating the media container, include the collaborators parameter and an array of strings indicating the Instagram usernames of users whom you want to invite as a collaborator on the media.

#### Sample Requeset

```
POST graph.facebook.com/17841400008460056/media
?image\_url=https://www.example.com/images/bronzed-fonzes.jpg
&caption=#BronzedFonzes!
&collaborators= [‘username1’,’username2’]
```
#### Notes

* The collaborators value must be an array of strings.
* You can only tag users with public Instagram accounts.
* No more than 3 collaborators can be added to a media.
* Collaborators cannot be added to Story media.

Location Tags
-------------

You can use the Pages Search API, be sure to include the `location` field in your query, to search for Pages whose names match a search string. Then, parse the results to identify any Pages that have been created for a physical location. If you include a Page's ID when publishing an image or video, it will be tagged with the location associated with that Page.
#### Limitations

To be eligible for tagging, a Page must have latitude and longitude location data.

Verify that the Page you want to use has latitude and longitude data in the response. Attempting to create a container using a Page that has no location data will fail with coded exception `INSTAGRAM_PLATFORM_API__INVALID_LOCATION_ID`.

Once you have the Page ID, assign it to the `location_id` parameter when publishing single media or carousel item containers.

Product Tags
------------

You can publish both single media posts and carousel posts tagged with Instagram Shopping products. Refer to the Product Tagging guide to learn how.

User Tags
---------

You can tag public Instagram users in an image and they will receive a notification that they have been tagged.

To tag users in an image, follow the Single Media Posts steps above, but when creating the media container, include the `user_tags` parameter and an array of objects indicating the Instagram users in the image as well as their x/y coordinates within the image itself.

#### Sample Request

```
POST graph.facebook.com/17841400008460056/media
 ?image\_url=https://www.example.com/images/bronzed-fonzes.jpg
 &caption=#BronzedFonzes!
 &user\_tags=
 [
 {
 username:'kevinhart4real',
 x: 0.5,
 y: 0.8
 },
 {
 username:'therock',
 x: 0.3,
 y: 0.2
 }
 ]
```
This returns a container ID which you then publish using the IG User Media Publish endpoint.

#### Notes

* The `user_tags` value must be an array of objects formatted with JSON.
* You can only tag users with public Instagram accounts.
* The object must contain all three properties (`username`, `x`, and `y`) for each user.
* `x` and `y` values must be `float` numbers that originate from the top-left of the image, with a range of `0.0`–`1.0`.
* User tags can be used with images in carousels.

Troubleshooting
---------------

If you are able to create a container for a video but the `POST /{ig-user-id}/media_publish` endpoint does not return the published media ID, you can get the container's publishing status by querying the `GET /{ig-container-id}?fields=status_code` endpoint. This endpoint will return one of the following:

* `EXPIRED` — The container was not published within 24 hours and has expired.
* `ERROR` — The container failed to complete the publishing process.
* `FINISHED` — The container and its media object are ready to be published.
* `IN_PROGRESS` — The container is still in the publishing process.
* `PUBLISHED` — The container's media object has been published.

We recommend querying a container's status once per minute, for no more than 5 minutes.

Errors
------

See the Error Codes reference.

On This PageContent PublishingRequirementsAccess TokensPermissionsPublic ServerPage Publishing AuthorizationLimitationsRate LimitEndpointsSingle Media PostsCarousel PostsReels PostsStory PostsCollaborator TagsLocation TagsProduct TagsUser TagsTroubleshootingErrorsFollow Us* 
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