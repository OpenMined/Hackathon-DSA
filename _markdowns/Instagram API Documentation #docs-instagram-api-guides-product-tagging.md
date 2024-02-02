Product Tagging - Instagram Platform











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
On This PageProduct TaggingLimitationsRequirementsEndpointsGet User EligibilityGet CatalogsGet Eligible ProductsCreate a Tagged Container for Images or VideosCreate a Tagged Container for ReelsPublish a Tagged Media ContainerGet Tags On MediaTag Existing MediaDelete TagsAppeal Product RejectionGet Appeal StatusCarouselsGet child media in a carouselProduct Tagging
===============


You can use the Instagram Graph API to create and manage Instagram Shopping Product Tags on an Instagram Business's IG Media.


**Note:** Beginning August 10, 2023, some businesses without checkout-enabled Shops will no longer be able to tag their products using the Content Publishing API. This will impact both API and native interfaces, and will remove tags to products from previous posts.Customers will still be able to tag products from Shops with checkout enabled on Facebook and Instagram. You can still refer to `shopping_product_tag_eligibility` field to check if an Instagram account is eligible to tag their products using Content Publishing API.


The general flow for tagging products is:


1. Check if the Instagram Business is eligible for product tagging.
2. If the Instagram Business is eligible, get its product catalogs.
3. Search each catalog for products that are eligible for tagging.
4. Create a tagged media container.
5. Publish the tagged media container.


Limitations
-----------


* All content publishing limitations apply to product tagging.
* Product tagging is not supported for Stories and Live.
* Product tagging is not supported for Instagram Creator accounts.
* Accounts are limited to 25 tagged media posts within a 24 hour period. Carousel albums count as a single post.


Requirements
------------


* Refer to each endpoint's reference document to determine which permissions, features, and User access tokens are required for each operation.
* The Instagram Business account (IG User) that owns the IG Media (to be tagged) must have an approved Instagram Shop with a product catalog containing products. In-app and external Instagram Shop checkout methods are supported.
* The app user must have an admin role on the Business Manager that owns the Instagram Shop whose products are being used to tag media.
* In order to request App Review approval for the `instagram_shopping_tag_products` and `catalog_management` permissions, which are required by several product tagging endpoints, your app must be associated with a verified business.


Endpoints
---------


* `GET /{ig-user-id}` — Check the app user's tagging eligibility.
* `GET /{ig-user-id}/available_catalogs` — Get a list of the app user's product catalogs.
* `GET /{ig-user-id}/catalog_product_search` — Get a list of tag eligible products in the app user's catalog.
* `POST /{ig-user-id}/media` — Create a tagged media container (step 1 of publishing process).
* `POST /{ig-user-id}/media_publish` — Publish a tagged media container (step 2 of publishing process).
* `GET /{ig-media-id}/product_tags` — Get tags on published IG Media.
* `DELETE /{ig-media-id}/product_tags` — Delete tags on published IG Media.
* `POST /{ig-media-id}/product_tags` — Create or update tags on published IG Media.
* `GET /{ig-user-id}/product_appeal` — Get product appeal information.
* `POST /{ig-user-id}/product_appeal` — Appeal a product rejection.
* `GET /{ig-media-id}/children` — Get a list of child IG Media in a carousel IG Media.


Get User Eligibility
--------------------


Request the `shopping_product_tag_eligibility` field on the IG User endpoint to determine if the Instagram Business account has set up an Instagram Shop. Accounts that have not set up an Instagram Shop are ineligible for product tagging.



```
GET /{ig-user-id}?fields=shopping\_product\_tag\_eligibility
```
Returns `true` if the Instagram Business account has been associated with a Business Manager's approved Instagram Shop, otherwise returns `false`.


#### Sample Request



```
curl -i -X GET \
 "https://graph.facebook.com/v18.0/90010177253934?fields=shopping\_product\_tag\_eligibility&access\_token=EAAOc..."
```
#### Sample Response



```
{
 "shopping\_product\_tag\_eligibility": true,
 "id": "90010177253934"
}
```
Get Catalogs
------------


Use the IG User Available Catalogs endpoint to get the Instagram Business account's product catalog.



```
GET /{ig-user-id}/available\_catalogs
```
Returns an array of catalogs and their metadata. Responses can include the following catalog fields:


* `catalog_id` — Catalog ID.
* `catalog_name` — Catalog name.
* `shop_name` — Shop name.
* `product_count` — Total number of products in the catalog.


#### Limitations


Collaborative catalogs such as shopping partner catalogs or affiliate creator catalogs are not supported.


#### Sample Request



```
curl -i -X GET \
 "https://graph.facebook.com/v18.0/90010177253934?fields=available\_catalogs&access\_token=EAAOc..."
```
#### Sample Response



```
{
 "available\_catalogs": {
 "data": [
 {
 "catalog\_id": "960179311066902",
 "catalog\_name": "Jay's Favorite Snacks",
 "shop\_name": "Jay's Bespoke",
 "product\_count": 11
 }
 ]
 },
 "id": "90010177253934"
}
```
Get Eligible Products
---------------------


Use the IG User Catalog Product Search endpoint to get a collection of products in the catalog that can be used to tag media. Product variants are supported.


Although the API will not return an error when publishing a post tagged with an unapproved product, the tag will not appear on the published post until the product has been approved. Therefore, we recommend that you only allow your app users to publish posts with tags whose products have a `review_status` of `approved`. This field is returned for each product by default when you get an app user's eligible products.



```
GET /{ig-user-id}/catalog\_product\_search
```
#### Parameters


* `catalog_id` — **(required)** Catalog ID.
* `q` — A string to search for in each product's name, or a product's SKU number (the **Content ID** column in the catalog management interface). If no string is specified, all tag-eligible products will be returned.


Returns an object containing an array of tag-eligible products and their metadata. Supports cursor-based pagination. Responses can include the following product fields:


* `image_url` — Product image URL.
* `is_checkout_flow` — If `true`, product can be purchased directly in the Instagram app. If `false`, product must be purchased in the app user's app/website.
* `merchant_id` — Merchant ID.
* `product_id` — Product ID.
* `product_name` — Product name.
* `retailer_id` — Retailer ID.
* `review_status` — Review status. Values can be `approved`, `outdated`, `pending`, `rejected`. An approved product can appear in the app user's Instagram Shop, but an approved status does not indicate product availability (e.g, the product could be out of stock). Only tags associated with products that have a `review_status` of `approved` can appear on published posts.
* `product_variants` — Product IDs (`product_id`) and variant names (`variant_name`) of product variants.


#### Sample Request



```
curl -i -X GET \
 "https://graph.facebook.com/v18.0/90010177253934/catalog\_product\_search?catalog\_id=960179311066902&q=gummy&access\_token=EAAOc..."
```
#### Sample Response



```
{
 "data": [
 {
 "product\_id": 3231775643511089,
 "merchant\_id": 90010177253934,
 "product\_name": "Gummy Wombats",
 "image\_url": "https://scont...",
 "retailer\_id": "oh59p9vzei",
 "review\_status": "approved",
 "is\_checkout\_flow": true,
 "product\_variants": [
 {
 "product\_id": 5209223099160494
 },
 {
 "product\_id": 7478222675582505,
 "variant\_name": "Green Gummy Wombats"
 }
 ]
 }
 ]
}
```
Create a Tagged Container for Images or Videos
----------------------------------------------


Use the IG User Media endpoint to create a media container for an image or video. Alternatively, see Create Tagged Media Container for Reels or Carousels.



```
POST /{ig-user-id}/media
```
#### Parameters


* `image_url` — (**required** for images only) The path to the image. Your image must be on a public server.
* `user_tags` — (images only) An array of public usernames and x/y coordinates for any public Instagram users who you want to tag in the image. The array must be formatted in JSON and contain a `username`, `x`, and `y` property. For example, `[{username:'natgeo',x:0.5,y:1.0}]`. `x` and `y` values must be floats that originate from the top-left of the image, with a range of `0.0`–`1.0`. Tagged users will receive a notification when the media is published.
* `video_url` — (**required** for videos only) The path to the video. Your video must be on a public server.
* `thumb_offset` — (videos only) The location, in milliseconds, of the frame for the video's cover thumbnail image. The default value is `0`, which is the first frame of the video.
* `product_tags` — (**required**) An array of objects specifying the product tags to add to the image or video. You can specify up to 20 tags for photo and video feed posts and up to 20 tags total per carousel post (up to 5 per carousel slide).
	+ The tags and product IDs must be unique.
	+ Tags for out-of-stock products are supported.
	+ Each object should have the following information:  
	
		- `product_id` — (**required**) Product ID.
		- `x` — (images only) A float that indicates percentage distance from left edge of the published media image. Value must be within `0.0`–`1.0` range.
	+ `y` — (images only) A float that indicates percentage distance from top edge of the pu blished media image. Value must be within `0.0`–`1.0` range.


If the operation is successful the API returns a container ID which you can use to publish the container.


#### Sample Request



```
curl -i -X POST \
 "https://graph.facebook.com/v18.0/90010177253934/media?image\_url=https%3A%2F%2Fupl...&location\_id=7640348500&product\_tags=%5B%0A%20%20%7B%0A%20%20%20%20product\_id%3A'3231775643511089'%2C%0A%20%20%20%20x%3A%200.5%2C%0A%20%20%20%20y%3A%200.8%0A%20%20%7D%0A%5D&access\_token=EAAOc..."
```
For reference, here is the HTML-decoded POST payload string:



```
https://graph.facebook.com/v12.0/90010177253934/media?image\_url=https://upl...&location\_id=7640348500
&product\_tags=[
 {
 product\_id:'3231775643511089',
 x: 0.5,
 y: 0.8
 }
]&access\_token=EAAOc...
```
#### Sample Response



```
{
 "id": "17969578066508312"
}
```
Create a Tagged Container for Reels
-----------------------------------


Use the IG User Media endpoint to create a media container for Reels. Alternatively, see Create Tagged Media Container or Carousels.



```
POST /{ig-user-id}/media
```
#### Parameters


* `media_type` — You must specify the media type `REELS`.
* `video_url` — The path to the video for the Reel. Your video must be on a public server. Your video must meet the Reels Specifications.
* `thumb_offset` — The location, in milliseconds, of the frame for the video's cover thumbnail image. The default value is `0`, which is the first frame of the video.
* `caption` — The caption for the Reel.
* `product_tags` — (**required**) An array of objects specifying the product tags to add to the Reel. You can specify up to 30 tags, and the tags and product IDs must be unique. Tags for out-of-stock products are supported. Each object should have the following information:  

	+ `product_id` — (**required**) Product ID.
* `location_id` — The ID of a Page associated with a location that you want to tag the video with. For details, see IG User Media Query String Parameters.
* `share_to_feed` — `true` to request that the video appears on both the Feed and Reels tabs. `false` to request that the video appears only on the Reels tab.
* `access_token` — Your User Access Token.


If the operation is successful the API returns a container ID which you can use to publish the container.


#### Sample Request



```
curl -i -X POST \
 "https://graph.facebook.com/v18.0/90010177253934/media?media\_type=REELS&video\_url=https://upl...&product\_tags=%5B%0A%20%20%7B%0A%20%20%20%20product\_id%3A'3231775643511089'%0A%20%20%7D%0A%5D&access\_token=EAAOc..."
```
For reference, here is the HTML-decoded POST payload string:



```
https://graph.facebook.com/v12.0/90010177253934/media?media\_type=REELS&video\_url=https://upl...
&product\_tags=[
 {
 product\_id:'3231775643511089'
 }
]&access\_token=EAAOc...
```
#### Sample Response



```
{
 "id": "17969578066508312"
}
```
Publish a Tagged Media Container
--------------------------------


Use the IG User Media Publish endpoint to publish the tagged media container. You may publish up to 25 tagged media containers on behalf of an app user within a 24 hour moving period. If you are publishing a carousel, see Carousels. Only products that have a `review_status` of `approved` will appear on published posts. If any of these products are out of stock, their tags will still appear on the published post.



```
POST /{ig-user-id}/media\_publish
```
#### Parameters


* `creation_id` — (**required**) The carousel container ID.


If the operation is successful the API will return an IG Media ID.


#### Sample Request



```
curl -i -X POST \
 "https://graph.facebook.com/v18.0/90010177253934/media\_publish?creation\_id=17969578066508312&access\_token=EAAOc"
```
#### Sample Response



```
{
 "id": "90010778325754"
}
```
Get Tags On Media
-----------------


Use the IG Media Product Tags endpoint to get tags on published media.



```
GET /{ig-media-id}/product\_tags
```
Returns an array of product tags and their metadata on an IG Media. Responses can include the following product tag fields:


* `product_id` — Product ID.
* `merchant_id` — Merchant ID.
* `name` — Product name.
* `price_string` — Product price.
* `image_url` — Product image URL.
* `review_status` — Indicates product tag eligibility status. Values can be:
* `approved` — Product is approved.
* `rejected` — Product was rejected.
* `pending` — Still undergoing review.
* `outdated` — Product was approved but has been edited and requires reapproval.
* `""` — No review status.
* `no_review` — No review status.
* `is_checkout` — If `true`, product can be purchased directly through the Instagram app. If `false`, product can only be purchased on the merchant's website.
* `stripped_price_string` — Product short price string (price displayed in constrained spaces, such as `$100` instead of `100 USD`).
* `string_sale_price_string` — Product sale price.
* `x` — A float that indicates percentage distance from left edge of media image. Value within `0.0`–`1.0` range.
* `y` — A float that indicates percentage distance from top edge of media image. Value within `0.0`–`1.0` range.


#### Sample Request



```
curl -i -X GET \
 "https://graph.facebook.com/v18.0/90010778325754/product\_tags?access\_token=EAAOc..."
```
#### Sample Response



```
{
 "data": [
 {
 "product\_id": 3231775643511089,
 "merchant\_id": 90010177253934,
 "name": "Gummy Wombats",
 "price\_string": "$3.50",
 "image\_url": "https://scont...",
 "review\_status": "approved",
 "is\_checkout": true,
 "stripped\_price\_string": "$3.50",
 "x": 0.5,
 "y": 0.80000001192093
 }
 ]
}
```
Tag Existing Media
------------------


Use the IG Media Product Tags endpoint to create or update tags on existing IG Media.



```
POST /{ig-media-id}/product\_tags
```
#### Parameters


* `updated_tags` — (**required**) An array of objects specifying which product tags to tag the image or video with (maximum of 5; tags and product IDs must be unique). Each object should have the following information:
* `product_id` — (**required**) Product ID. If the IG Media has not been tagged with this ID the tag will be added to the IG Media. If the media has already been tagged with this ID, the tag's display coordinates will be updated.
* `x` — (images only, **required**) A float that indicates percentage distance from left edge of the published media image. Value must be within `0.0`–`1.0` range.
* `y` — (images only, **required**) A float that indicates percentage distance from top edge of the published media image. Value must be within `0.0`–`1.0` range.


Tagging media is additive until the 5 tag limit has been reached. If the targeted media has already been tagged by a product in the request, the old tag's `x` and `y` values will be updated with their new values (a new tag will not be added).


Returns `true` if able to update the product, otherwise returns `false`.


#### Sample Request



```
curl -i -X POST \
 "https://graph.facebook.com/v18.0/90010778325754/product\_tags?updated\_tags=%5B%0A%20%20%7B%0A%20%20%20%20product\_id%3A'3859448974125379'%2C%0A%20%20%20%20x%3A%200.5%2C%0A%20%20%20%20y%3A%200.8%0A%20%20%7D%0A%5D&access\_token=EAAOc..."
```
For reference, here is the HTML-decoded POST payload string:



```
https://graph.facebook.com/v12.0/90010778325754/product\_tags?updated\_tags=[
 {
 product\_id:'3859448974125379',
 x: 0.5,
 y: 0.8
 }
]&access\_token=EAAOc...
```
#### Sample Response



```
{
 "success": true
}
```
Delete Tags
-----------


Use the IG Media Product Tags endpoint to delete tags on a published IG Media including Reels.



```
DELETE /{ig-media-id}/product\_tags
```
#### Parameters


* `deleted_tags` — (**required**) An array containing the following information for each product tag to be deleted:
* `merchant_id` — (**required**) Merchant ID.
* `product_id` — (**required**) Product ID.


Returns `true` if tag deletion successful, otherwise returns `false`.


#### Sample Request



```
curl -i -X DELETE \
 "https://graph.facebook.com/v18.0/90010778325754/product\_tags?deleted\_tags=%5B%0A%20%20%7B%0A%20%20%20%20product\_id%3A'3859448974125379'%2C%0A%20%20%20%20merchant\_id%3A'90010177253934'%0A%20%20%7D%0A%5D&access\_token=EAAOc..."
```
For reference, here is the HTML-decoded POST payload string:



```
https://graph.facebook.com/v12.0/90010778325754/product\_tags?deleted\_tags=[
 {
 product\_id:'3859448974125379',
 merchant\_id:'90010177253934'
 }
]&access\_token=EAAOc...
```
#### Sample Response



```
{
 "success": true
}
```
Appeal Product Rejection
------------------------


Use the IG User Product Appeal endpoint it you want to provide a way for your app users to appeal product rejections (tags of rejected products will not appear on published posts). Although not required, we do recommend that you provide a way for app users to appeal rejections, or advise them to appeal rejections using the Business Manager.



```
POST /{ig-user-id}/product\_appeal
```
#### Parameters


* `appeal_reason` — (**required**) Explanation of why the product should be approved.
* `product_id` — (**required**) Product ID.


Returns `true` if we are able to receive your request, otherwise returns `false`. Response does not indicate appeal outcome.


#### Sample Request



```
curl -i -X POST \

"https://graph.facebook.com/v18.0/90010177253934/product\_appeal?appeal\_reason=product%20is%20a%20toy%20and%20not%20a%20real%20weapon&product\_id=4382881195057752&access\_token=EAAOc..."
```
#### Sample Response



```
{
 "success": true
}
```
Get Appeal Status
-----------------


Use the IG User Product Appeal endpoint to get the status of an appeal for a given rejected product:



```
GET /{ig-user-id}/product\_appeal
```
#### Parameters


* `product_id` — (**required**) Product ID.


Returns appeal status metadata. Responses can include the following appeal fields:


* `eligible_for_appeal` — Indicates if decision can be appealed (yes if `true`, no if `false`).
* `product_id` — Product ID.
* `review_status` — Review status. Value can be:
* `approved` — Product is approved.
* `rejected` — Product was rejected.
* `pending` — Still undergoing review.
* `outdated` — Product was approved but has been edited and requires reapproval.
* `""` — No review status.
* `no_review` — No review status.


#### Sample Request



```
curl -i -X GET \
 "https://graph.facebook.com/v18.0/90010177253934/product\_appeal?product\_id=4029274203846188&access\_token=EAAOc..."
```
#### Sample Response



```
{
 "data": [
 {
 "product\_id": 4029274203846188,
 "review\_status": "approved",
 "eligible\_for\_appeal": false
 }
 ]
}
```
Carousels
---------


You can publish carousels (albums) containing up to 10 total tagged images, videos, or a mix of the two. To do this, when performing step 1 of 3 of the carousel posts publishing process, simply create tagged media containers for each tagged image or video that you want to appear in the album carousel and continue with the carousel publishing processs as you normally would.


### Get child media in a carousel


To get the IDs of IG Media in an album carousel, use the IG Media Children endpoint.


On This PageProduct TaggingLimitationsRequirementsEndpointsGet User EligibilityGet CatalogsGet Eligible ProductsCreate a Tagged Container for Images or VideosCreate a Tagged Container for ReelsPublish a Tagged Media ContainerGet Tags On MediaTag Existing MediaDelete TagsAppeal Product RejectionGet Appeal StatusCarouselsGet child media in a carouselFollow Us* 
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