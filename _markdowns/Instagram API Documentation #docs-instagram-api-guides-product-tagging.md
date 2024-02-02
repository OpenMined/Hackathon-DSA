<div>

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
-   All [content publishing
    limitations](/docs/instagram-api/guides/content-publishing#limitations)
    apply to product tagging.
-   Product tagging is not supported for Stories and Live.
-   Product tagging is not supported for Instagram Creator accounts.
-   Accounts are limited to 25 tagged media posts within a 24 hour
    period. Carousel albums count as a single post.
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
-   Refer to each endpoint\'s reference document to determine which
    permissions, features, and
    [User](/docs/facebook-login/access-tokens/#usertokens) access tokens
    are required for each operation.
-   The Instagram Business account (IG User) that owns the IG Media (to
    be tagged) must have an approved [Instagram
    Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT0qoE3VZM94zqpzik-A1-wRBoWDtQSRpQUKwrBy9ef7y-y8XsQERaqDGgSJfAO3mWfyBY16uzUOPIixregwcRk3Qjj-xmuogqadgiUfOJvJT69UOfmUURe4jlX2T_b8SwpCTX6ctpnSeFAij3ardg)
    with a product catalog containing products. In-app and external
    Instagram Shop [checkout
    methods](https://www.facebook.com/business/help/449169642911614) are
    supported.
-   The app user must have an [admin
    role](https://www.facebook.com/business/help/442345745885606) on the
    [Business Manager](https://business.facebook.com/) that owns the
    Instagram Shop whose products are being used to tag media.
-   In order to request [App Review](/docs/app-review) approval for the
    [` instagram_shopping_tag_products `](/docs/permissions/reference/instagram_shopping_tag_products)
    and
    [` catalog_management `](/docs/permissions/reference/catalog_management)
    permissions, which are required by several product tagging
    endpoints, your app must be associated with a [verified
    business](/docs/development/release/business-verification) .
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
Request the ` shopping_product_tag_eligibility ` field on the [IG
User](/docs/instagram-api/reference/ig-user) endpoint to determine if
the Instagram Business account has set up an [Instagram
Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT21nwWiIas4YNl3oi3FqU2ZMnby9dkct6n3Y8lT5xRKBc7VNVoPwX8tvJB27DdWLzy7DWYVJHAxAeCbxSyKnxxq1MrepYseZzcR4NeHfLgowufaBRco5bB_Xzgdx_rRPRwbCXlcG0hGkEH8bdNPAA)
. Accounts that have not set up an Instagram Shop are ineligible for
product tagging.

``` {._5s-8 .prettyprint .lang-http .prettyprinted}
GET /{ig-user-id}?fields=shopping_product_tag_eligibility
```

Returns ` true ` if the Instagram Business account has been associated
with a [Business Manager\'s](https://business.facebook.com/) approved
Instagram Shop, otherwise returns ` false ` .

#### Sample Request

``` {._5s-8 .prettyprint .lang-curl .prettyprinted}
curl -i -X GET \ "https://graph.facebook.com/v18.0/90010177253934?fields=shopping_product_tag_eligibility&access_token=EAAOc..."
```

#### Sample Response

``` {._5s-8 .prettyprint .lang-json .prettyprinted}
{ "shopping_product_tag_eligibility": true, "id": "90010177253934"
}
```
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
Use the [IG User Available
Catalogs](/docs/instagram-api/reference/ig-user/available_catalogs)
endpoint to get the Instagram Business account\'s product catalog.

``` {._5s-8 .prettyprint .lang-http .prettyprinted}
GET /{ig-user-id}/available_catalogs
```

Returns an array of catalogs and their metadata. Responses can include
the following catalog fields:

-   ` catalog_id ` --- Catalog ID.
-   ` catalog_name ` --- Catalog name.
-   ` shop_name ` --- Shop name.
-   ` product_count ` --- Total number of products in the catalog.

#### Limitations

Collaborative catalogs such as shopping partner catalogs or affiliate
creator catalogs are not supported.

#### Sample Request

``` {._5s-8 .prettyprint .lang-curl .prettyprinted}
curl -i -X GET \ "https://graph.facebook.com/v18.0/90010177253934?fields=available_catalogs&access_token=EAAOc..."
```

#### Sample Response

``` {._5s-8 .prettyprint .lang-json .prettyprinted}
{ "available_catalogs": { "data": [ { "catalog_id": "960179311066902", "catalog_name": "Jay's Favorite Snacks", "shop_name": "Jay's Bespoke", "product_count": 11 } ] }, "id": "90010177253934"
}
```
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
Use the [IG User Catalog Product
Search](/docs/instagram-api/reference/ig-user/catalog_product_search)
endpoint to get a collection of products in the catalog that can be used
to tag media. Product variants are supported.

Although the API will not return an error when publishing a post tagged
with an unapproved product, the tag will not appear on the published
post until the product has been approved. Therefore, we recommend that
you only allow your app users to publish posts with tags whose products
have a ` review_status ` of ` approved ` . This field is returned for
each product by default when you get an app user\'s eligible products.

``` {._5s-8 .prettyprint .lang-http .prettyprinted}
GET /{ig-user-id}/catalog_product_search
```

#### Parameters

-   ` catalog_id ` --- **(required)** Catalog ID.
-   ` q ` --- A string to search for in each product\'s name, or a
    product\'s SKU number (the **Content ID** column in the catalog
    management interface). If no string is specified, all tag-eligible
    products will be returned.

Returns an object containing an array of tag-eligible products and their
metadata. Supports [cursor-based
pagination](/docs/graph-api/results#cursors) . Responses can include the
following product fields:

-   ` image_url ` --- Product image URL.
-   ` is_checkout_flow ` --- If ` true ` , product can be purchased
    directly in the Instagram app. If ` false ` , product must be
    purchased in the app user\'s app/website.
-   ` merchant_id ` --- Merchant ID.
-   ` product_id ` --- Product ID.
-   ` product_name ` --- Product name.
-   ` retailer_id ` --- Retailer ID.
-   ` review_status ` --- Review status. Values can be ` approved ` ,
    ` outdated ` , ` pending ` , ` rejected ` . An approved product can
    appear in the app user\'s [Instagram
    Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT0MV9YbV_4Y9TW40JAXiPB7fB6sVXXR5ah6SeYvVAIvlS-pnR28f0U2-v2tJM5oQgAAlkh7G55OA7ciJmIuAY5hHLMlBWO8TzKIupY0cuADPfbm7UHikcPGpJfuI0YdOj4u1MN8YPe75uujO8uY2Q)
    , but an approved status does not indicate product availability
    (e.g, the product could be out of stock). Only tags associated with
    products that have a ` review_status ` of ` approved ` can appear on
    published posts.
-   ` product_variants ` --- Product IDs ( ` product_id ` ) and variant
    names ( ` variant_name ` ) of [product
    variants](/docs/marketing-api/catalog/guides/product-variants) .

#### Sample Request

``` {._5s-8 .prettyprint .lang-curl .prettyprinted}
curl -i -X GET \ "https://graph.facebook.com/v18.0/90010177253934/catalog_product_search?catalog_id=960179311066902&q=gummy&access_token=EAAOc..."
```

#### Sample Response

``` {._5s-8 .prettyprint .lang-json .prettyprinted}
{ "data": [ { "product_id": 3231775643511089, "merchant_id": 90010177253934, "product_name": "Gummy Wombats", "image_url": "https://scont...", "retailer_id": "oh59p9vzei", "review_status": "approved", "is_checkout_flow": true, "product_variants": [ { "product_id": 5209223099160494 }, { "product_id": 7478222675582505, "variant_name": "Green Gummy Wombats" } ] } ]
}
```
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
Use the [IG User Media](/docs/instagram-api/reference/ig-user/media)
endpoint to create a media container for an
[image](/docs/instagram-api/reference/ig-user/media#create-photo-container)
or
[video](/docs/instagram-api/reference/ig-user/media#create-video-container)
. Alternatively, see [Create Tagged Media Container for
Reels](#post-media-reels) or [Carousels](#carousels) .

``` {._5s-8 .prettyprint .lang-http .prettyprinted}
POST /{ig-user-id}/media
```

#### Parameters

-   ` image_url ` --- ( **required** for images only) The path to the
    image. Your image must be on a public server.
-   ` user_tags ` --- (images only) An array of public usernames and x/y
    coordinates for any public Instagram users who you want to tag in
    the image. The array must be formatted in JSON and contain a
    ` username ` , ` x ` , and ` y ` property. For example,
    ` [{username:'natgeo',x:0.5,y:1.0}] ` . ` x ` and ` y ` values must
    be floats that originate from the top-left of the image, with a
    range of ` 0.0 ` -- ` 1.0 ` . Tagged users will receive a
    notification when the media is published.
-   ` video_url ` --- ( **required** for videos only) The path to the
    video. Your video must be on a public server.
-   ` thumb_offset ` --- (videos only) The location, in milliseconds, of
    the frame for the video\'s cover thumbnail image. The default value
    is ` 0 ` , which is the first frame of the video.
-   ` product_tags ` --- ( **required** ) An array of objects specifying
    the product tags to add to the image or video. You can specify up to
    20 tags for photo and video feed posts and up to 20 tags total per
    carousel post (up to 5 per carousel slide).
    -   The tags and product IDs must be unique.
    -   Tags for out-of-stock products are supported.
    -   Each object should have the following information:\
        -   ` product_id ` --- ( **required** ) Product ID.
        -   ` x ` --- (images only) A float that indicates percentage
            distance from left edge of the published media image. Value
            must be within ` 0.0 ` -- ` 1.0 ` range.
    -   ` y ` --- (images only) A float that indicates percentage
        distance from top edge of the pu blished media image. Value must
        be within ` 0.0 ` -- ` 1.0 ` range.

If the operation is successful the API returns a container ID which you
can use to [publish the container](#post-media-publish) .

#### Sample Request

``` {._5s-8 .prettyprint .lang-curl .prettyprinted}
curl -i -X POST \ "https://graph.facebook.com/v18.0/90010177253934/media?image_url=https%3A%2F%2Fupl...&location_id=7640348500&product_tags=%5B%0A%20%20%7B%0A%20%20%20%20product_id%3A'3231775643511089'%2C%0A%20%20%20%20x%3A%200.5%2C%0A%20%20%20%20y%3A%200.8%0A%20%20%7D%0A%5D&access_token=EAAOc..."
```

For reference, here is the HTML-decoded POST payload string:

``` {._5s-8 .prettyprint .lang-html .prettyprinted}
https://graph.facebook.com/v12.0/90010177253934/media?image_url=https://upl...&location_id=7640348500
&product_tags=[ { product_id:'3231775643511089', x: 0.5, y: 0.8 }
]&access_token=EAAOc...
```

#### Sample Response

``` {._5s-8 .prettyprint .lang-json .prettyprinted}
{ "id": "17969578066508312"
}
```
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
Use the [IG User Media](/docs/instagram-api/reference/ig-user/media)
endpoint to create a media container for Reels. Alternatively, see
[Create Tagged Media Container](#post-media) or [Carousels](#carousels)
.

``` {._5s-8 .prettyprint .lang-http .prettyprinted}
POST /{ig-user-id}/media
```

#### Parameters

-   ` media_type ` --- You must specify the media type ` REELS ` .
-   ` video_url ` --- The path to the video for the Reel. Your video
    must be on a public server. Your video must meet the [Reels
    Specifications](/docs/instagram-api/reference/ig-user/media#reel-specifications)
    .
-   ` thumb_offset ` --- The location, in milliseconds, of the frame for
    the video\'s cover thumbnail image. The default value is ` 0 ` ,
    which is the first frame of the video.
-   ` caption ` --- The caption for the Reel.
-   ` product_tags ` --- ( **required** ) An array of objects specifying
    the product tags to add to the Reel. You can specify up to 30 tags,
    and the tags and product IDs must be unique. Tags for out-of-stock
    products are supported. Each object should have the following
    information:\
    -   ` product_id ` --- ( **required** ) Product ID.
-   ` location_id ` --- The ID of a Page associated with a location that
    you want to tag the video with. For details, see [IG User Media
    Query String
    Parameters](/docs/instagram-api/reference/ig-user/media#query-string-parameters)
    .
-   ` share_to_feed ` --- ` true ` to request that the video appears on
    both the Feed and Reels tabs. ` false ` to request that the video
    appears only on the Reels tab.
-   ` access_token ` --- Your [User Access
    Token](/docs/facebook-login/guides/access-tokens) .

If the operation is successful the API returns a container ID which you
can use to [publish the container](#post-media-publish) .

#### Sample Request

``` {._5s-8 .prettyprint .lang-curl .prettyprinted}
curl -i -X POST \ "https://graph.facebook.com/v18.0/90010177253934/media?media_type=REELS&video_url=https://upl...&product_tags=%5B%0A%20%20%7B%0A%20%20%20%20product_id%3A'3231775643511089'%0A%20%20%7D%0A%5D&access_token=EAAOc..."
```

For reference, here is the HTML-decoded POST payload string:

``` {._5s-8 .prettyprint .lang-html .prettyprinted}
https://graph.facebook.com/v12.0/90010177253934/media?media_type=REELS&video_url=https://upl...
&product_tags=[ { product_id:'3231775643511089' }
]&access_token=EAAOc...
```

#### Sample Response

``` {._5s-8 .prettyprint .lang-json .prettyprinted}
{ "id": "17969578066508312"
}
```
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
Use the [IG User Media
Publish](/docs/instagram-api/reference/ig-user/media_publish) endpoint
to publish the tagged media container. You may publish up to 25 tagged
media containers on behalf of an app user within a 24 hour moving
period. If you are publishing a carousel, see [Carousels](#carousels) .
Only products that have a ` review_status ` of ` approved ` will appear
on published posts. If any of these products are out of stock, their
tags will still appear on the published post.

``` {._5s-8 .prettyprint .lang-http .prettyprinted}
POST /{ig-user-id}/media_publish
```

#### Parameters

-   ` creation_id ` --- ( **required** ) The carousel container ID.

If the operation is successful the API will return an IG Media ID.

#### Sample Request

``` {._5s-8 .prettyprint .lang-curl .prettyprinted}
curl -i -X POST \ "https://graph.facebook.com/v18.0/90010177253934/media_publish?creation_id=17969578066508312&access_token=EAAOc"
```

#### Sample Response

``` {._5s-8 .prettyprint .lang-json .prettyprinted}
{ "id": "90010778325754"
}
```
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
Use the [IG Media Product
Tags](/docs/instagram-api/reference/ig-media/product_tags#reading)
endpoint to get tags on published media.

``` {._5s-8 .prettyprint .lang-http .prettyprinted}
GET /{ig-media-id}/product_tags
```

Returns an array of product tags and their metadata on an [IG
Media](/docs/instagram-api/reference/ig-media/) . Responses can include
the following product tag fields:

-   ` product_id ` --- Product ID.
-   ` merchant_id ` --- Merchant ID.
-   ` name ` --- Product name.
-   ` price_string ` --- Product price.
-   ` image_url ` --- Product image URL.
-   ` review_status ` --- Indicates product tag eligibility status.
    Values can be:
-   ` approved ` --- Product is approved.
-   ` rejected ` --- Product was rejected.
-   ` pending ` --- Still undergoing review.
-   ` outdated ` --- Product was approved but has been edited and
    requires reapproval.
-   ` "" ` --- No review status.
-   ` no_review ` --- No review status.
-   ` is_checkout ` --- If ` true ` , product can be purchased directly
    through the Instagram app. If ` false ` , product can only be
    purchased on the merchant\'s website.
-   ` stripped_price_string ` --- Product short price string (price
    displayed in constrained spaces, such as ` $100 ` instead of
    ` 100 USD ` ).
-   ` string_sale_price_string ` --- Product sale price.
-   ` x ` --- A float that indicates percentage distance from left edge
    of media image. Value within ` 0.0 ` -- ` 1.0 ` range.
-   ` y ` --- A float that indicates percentage distance from top edge
    of media image. Value within ` 0.0 ` -- ` 1.0 ` range.

#### Sample Request

``` {._5s-8 .prettyprint .lang-curl .prettyprinted}
curl -i -X GET \ "https://graph.facebook.com/v18.0/90010778325754/product_tags?access_token=EAAOc..."
```

#### Sample Response

``` {._5s-8 .prettyprint .lang-json .prettyprinted}
{ "data": [ { "product_id": 3231775643511089, "merchant_id": 90010177253934, "name": "Gummy Wombats", "price_string": "$3.50", "image_url": "https://scont...", "review_status": "approved", "is_checkout": true, "stripped_price_string": "$3.50", "x": 0.5, "y": 0.80000001192093 } ]
}
```
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
Use the [IG Media Product
Tags](/docs/instagram-api/reference/ig-media/product_tags#creating)
endpoint to create or update tags on existing [IG
Media](/docs/instagram-api/reference/ig-media/) .

``` {._5s-8 .prettyprint .lang-http .prettyprinted}
POST /{ig-media-id}/product_tags
```

#### Parameters

-   ` updated_tags ` --- ( **required** ) An array of objects specifying
    which product tags to tag the image or video with (maximum of 5;
    tags and product IDs must be unique). Each object should have the
    following information:
-   ` product_id ` --- ( **required** ) Product ID. If the IG Media has
    not been tagged with this ID the tag will be added to the IG Media.
    If the media has already been tagged with this ID, the tag\'s
    display coordinates will be updated.
-   ` x ` --- (images only, **required** ) A float that indicates
    percentage distance from left edge of the published media image.
    Value must be within ` 0.0 ` -- ` 1.0 ` range.
-   ` y ` --- (images only, **required** ) A float that indicates
    percentage distance from top edge of the published media image.
    Value must be within ` 0.0 ` -- ` 1.0 ` range.

Tagging media is additive until the 5 tag limit has been reached. If the
targeted media has already been tagged by a product in the request, the
old tag\'s ` x ` and ` y ` values will be updated with their new values
(a new tag will not be added).

Returns ` true ` if able to update the product, otherwise returns
` false ` .

#### Sample Request

``` {._5s-8 .prettyprint .lang-curl .prettyprinted}
curl -i -X POST \ "https://graph.facebook.com/v18.0/90010778325754/product_tags?updated_tags=%5B%0A%20%20%7B%0A%20%20%20%20product_id%3A'3859448974125379'%2C%0A%20%20%20%20x%3A%200.5%2C%0A%20%20%20%20y%3A%200.8%0A%20%20%7D%0A%5D&access_token=EAAOc..."
```

For reference, here is the HTML-decoded POST payload string:

``` {._5s-8 .prettyprint .lang-html .prettyprinted}
https://graph.facebook.com/v12.0/90010778325754/product_tags?updated_tags=[ { product_id:'3859448974125379', x: 0.5, y: 0.8 }
]&access_token=EAAOc...
```

#### Sample Response

``` {._5s-8 .prettyprint .lang-json .prettyprinted}
{ "success": true
}
```
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
Use the [IG Media Product
Tags](/docs/instagram-api/reference/ig-media/product_tags#deleting)
endpoint to delete tags on a published [IG
Media](/docs/instagram-api/reference/ig-media/) including Reels.

``` {._5s-8 .prettyprint .lang-http .prettyprinted}
DELETE /{ig-media-id}/product_tags
```

#### Parameters

-   ` deleted_tags ` --- ( **required** ) An array containing the
    following information for each product tag to be deleted:
-   ` merchant_id ` --- ( **required** ) Merchant ID.
-   ` product_id ` --- ( **required** ) Product ID.

Returns ` true ` if tag deletion successful, otherwise returns ` false `
.

#### Sample Request

``` {._5s-8 .prettyprint .lang-curl .prettyprinted}
curl -i -X DELETE \ "https://graph.facebook.com/v18.0/90010778325754/product_tags?deleted_tags=%5B%0A%20%20%7B%0A%20%20%20%20product_id%3A'3859448974125379'%2C%0A%20%20%20%20merchant_id%3A'90010177253934'%0A%20%20%7D%0A%5D&access_token=EAAOc..."
```

For reference, here is the HTML-decoded POST payload string:

``` {._5s-8 .prettyprint .lang-html .prettyprinted}
https://graph.facebook.com/v12.0/90010778325754/product_tags?deleted_tags=[ { product_id:'3859448974125379', merchant_id:'90010177253934' }
]&access_token=EAAOc...
```

#### Sample Response

``` {._5s-8 .prettyprint .lang-json .prettyprinted}
{ "success": true
}
```
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
Use the [IG User Product
Appeal](/docs/instagram-api/reference/ig-user/product_appeal#creating)
endpoint it you want to provide a way for your app users to appeal
product
[rejections](https://www.facebook.com/help/instagram/1907693709488725)
(tags of rejected products will not appear on published posts). Although
not required, we do recommend that you provide a way for app users to
appeal rejections, or advise them to appeal rejections [using the
Business
Manager](https://www.facebook.com/business/help/494867298080532) .

``` {._5s-8 .prettyprint .lang-http .prettyprinted}
POST /{ig-user-id}/product_appeal
```

#### Parameters

-   ` appeal_reason ` --- ( **required** ) Explanation of why the
    product should be approved.
-   ` product_id ` --- ( **required** ) Product ID.

Returns ` true ` if we are able to receive your request, otherwise
returns ` false ` . Response does not indicate appeal outcome.

#### Sample Request

``` {._5s-8 .prettyprint .lang-curl .prettyprinted}
curl -i -X POST \ "https://graph.facebook.com/v18.0/90010177253934/product_appeal?appeal_reason=product%20is%20a%20toy%20and%20not%20a%20real%20weapon&product_id=4382881195057752&access_token=EAAOc..."
```

#### Sample Response

``` {._5s-8 .prettyprint .lang-json .prettyprinted}
{ "success": true
}
```
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
Use the [IG User Product
Appeal](/docs/instagram-api/reference/ig-user/product_appeal#reading)
endpoint to get the status of an appeal for a given
[rejected](https://www.facebook.com/help/instagram/1907693709488725)
product:

``` {._5s-8 .prettyprint .lang-http .prettyprinted}
GET /{ig-user-id}/product_appeal
```

#### Parameters

-   ` product_id ` --- ( **required** ) Product ID.

Returns appeal status metadata. Responses can include the following
appeal fields:

-   ` eligible_for_appeal ` --- Indicates if decision can be appealed
    (yes if ` true ` , no if ` false ` ).
-   ` product_id ` --- Product ID.
-   ` review_status ` --- Review status. Value can be:
-   ` approved ` --- Product is approved.
-   ` rejected ` --- Product was rejected.
-   ` pending ` --- Still undergoing review.
-   ` outdated ` --- Product was approved but has been edited and
    requires reapproval.
-   ` "" ` --- No review status.
-   ` no_review ` --- No review status.

#### Sample Request

``` {._5s-8 .prettyprint .lang-curl .prettyprinted}
curl -i -X GET \ "https://graph.facebook.com/v18.0/90010177253934/product_appeal?product_id=4029274203846188&access_token=EAAOc..."
```

#### Sample Response

``` {._5s-8 .prettyprint .lang-json .prettyprinted}
{ "data": [ { "product_id": 4029274203846188, "review_status": "approved", "eligible_for_appeal": false } ]
}
```
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
You can publish carousels (albums) containing up to 10 total tagged
images, videos, or a mix of the two. To do this, when performing step 1
of 3 of the [carousel
posts](/docs/instagram-api/guides/content-publishing#carousel-posts)
publishing process, simply create [tagged media
containers](#create-tagged-media-container) for each tagged image or
video that you want to appear in the album carousel and continue with
the carousel publishing processs as you normally would.

To get the IDs of IG Media in an album carousel, use the [IG Media
Children](/docs/instagram-api/reference/ig-media/children) endpoint.
:::
:::

</div>
