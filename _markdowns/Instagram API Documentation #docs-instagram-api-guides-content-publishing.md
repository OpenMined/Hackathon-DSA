<div>

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
You can use the Instagram Graph API to publish single images, videos,
reels (i.e., single media posts), or posts containing multiple images
and videos (carousel posts) on Instagram Professional accounts.

::: {._57yz ._57z1 ._3-8p}
::: _57y-
Beginning July 1, 2023, all single feed videos published through the
Instagram Content Publishing API will be shared as reels.
:::
:::

## Requirements

### Access Tokens

All requests must include the app user\'s
[User](/docs/facebook-login/access-tokens/#usertokens) access token.

### Permissions

Publishing relies on a combination of the following permissions. The
exact combination depends on which [endpoints](#endpoints) your app
uses. Refer to our [endpoint](#endpoints) references to determine which
permissions each endpoint requires.

If your app will be used by app users who do not have a
[role](/docs/development/build-and-test/app-roles) on your app or a role
in a
[Business](https://www.facebook.com/business/help/442345745885606?id=180505742745347)
that has claimed your app, you must request approval for each permission
via [App Review](/docs/app-review) before non-role app users can grant
them to your app.

### Public Server

We cURL media used in publishing attempts so the media must be hosted on
a publicly accessible server at the time of the attempt.

### Page Publishing Authorization

Instagram Professional accounts connected to a
[Page](/docs/instagram-api/overview#pages) that requires [Page
Publishing
Authorization](https://www.facebook.com/business/m/one-sheeters/page-publishing-authorization)
(PPA) cannot be published to until PPA has been completed.

It\'s possible that an app user may be able to perform
[Tasks](/docs/instagram-api/overview#tasks) on a Page that initially
does not require PPA but later requires it. In this scenario, the app
user would not be able to publish content to their Instagram
Professional account until completing PPA. Since there\'s no way for you
to determine if an app user\'s Page requires PPA, we recommend that you
advise app users to preemptively complete PPA.

### Limitations

-   JPEG is the only image format supported. Extended JPEG formats such
    as MPO and JPS are not supported.
-   Shopping tags are not supported.
-   Branded content tags are not supported.
-   Filters are not supported.
-   Publishing to Instagram TV is not supported.

For additional limitations, refer to each [endpoint\'s](#endpoints)
reference.

### Rate Limit

Instagram accounts are limited to 50 API-published posts within a
24-hour moving period. Carousels count as a single post. This limit is
enforced on the
[` POST /{ig-user-id}/media_publish `](/docs/instagram-api/reference/ig-user/media_publish)
endpoint when attempting to publish a media container. We recommend that
your app also enforce the publishing rate limit, especially if your app
allows app users to schedule posts to be published in the future.

To check an Instagram Professional account\'s current rate limit usage,
query the
[` GET /{ig-user-id}/content_publishing_limit `](/docs/instagram-api/reference/ig-user/content_publishing_limit)
endpoint.
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
Publishing single image, video, story or reel is a two-step process:

Step 1 of 2: Create Container

Let\'s say you have an image at\...

``` {._5s-8 .prettyprint .lang-html .prettyprinted}
https://www.example.com/images/bronz-fonz.jpg
```

\... that you want to publish with the hashtag \"#BronzFonz\" as its
caption. Send a request to the
[` POST /{ig-user-id}/media `](/docs/instagram-api/reference/ig-user/media#creating)
endpoint:

#### Sample Request

``` {._5s-8 .prettyprint .lang-curl .prettyprinted}
POST https://graph.facebook.com/v18.0/17841400008460056/media ?image_url=https://www.example.com/images/bronz-fonz.jpg &caption=#BronzFonz
```

This returns a container ID for the image.

#### Sample Response

``` {._5s-8 .prettyprint .lang-code .prettyprinted}
{ "id": "17889455560051444" // IG Container ID
}
```

Step 2 of 2: Publish Container

Use the ` POST /{ig-user-id}/media_publish ` endpoint to publish the
container ID returned in the previous step.

#### Sample Request

``` {._5s-8 .prettyprint .lang-html .prettyprinted}
POST https://graph.facebook.com/v18.0/17841400008460056/media_publish ?creation_id=17889455560051444
```

#### Sample Response

``` {._5s-8 .prettyprint .lang-code .prettyprinted}
{ "id": "17920238422030506" // IG Media ID
}
```
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
You may publish up to 10 images, videos, or a mix of the two in a single
post (a carousel post). Publishing carousels is a three step process:

Carousel posts count as a single post against the account\'s [rate
limit](#rate-limit) .

Limitations

-   Carousels cannot be boosted.
-   Carousels are limited to 10 images, videos, or a mix of the two.
-   Carousel images are all cropped based on the first image in the
    carousel, with the default being a 1:1 aspect ratio.

Step 1 of 3: Create item container

Use the
[` POST /{ig-user-id}/media `](/docs/instagram-api/reference/ig-user/media#creating)
endpoint to create an item container for the image or video that will
appear in a carousel. Carousels may have up to 10 total images, videos,
or a mix of the two.

``` {._5s-8 .prettyprint .lang-http .prettyprinted}
POST /{ig-user-id}/media
```

#### Parameters

The following parameters are **required** . Refer to the
[` POST /{ig-user-id}/media `](/docs/instagram-api/reference/ig-user/media#creating)
endpoint reference for additional supported parameters.

-   ` is_carousel_item ` --- Set to ` true ` . Indicates image or video
    will appear in a carousel.
-   ` image_url ` --- (images only) The path to the image. We will cURL
    your image using the passed in URL so it must be on a public server.
-   ` media_type ` --- (videos only) Set to ` VIDEO ` . Indicates media
    is a video.
-   ` video_url ` --- (videos only) Path to the video. We will cURL your
    video using the passed in URL so it must be on a public server.

If the operation is successful, the API will return an item container ID
which can be used when creating the carousel container.

Repeat this process for each image or video that should appear in the
carousel.

#### Sample Request

``` {._5s-8 .prettyprint .lang-curl .prettyprinted}
curl -i -X POST \ "https://graph.facebook.com/v18.0/90010177253934/media?image_url=https%3A%2F%2Fsol...&is_carousel_item=true&access_token=EAAOc..."
```

#### Sample Response

``` {._5s-8 .prettyprint .lang-json .prettyprinted}
{ "id": "17899506308402767"
}
```

Step 2 of 3: Create carousel container

Use the
[` POST /{ig-user-id}/media `](/docs/instagram-api/reference/ig-user/media#creating)
endpoint to create a carousel container.

``` {._5s-8 .prettyprint .lang-http .prettyprinted}
POST /{ig-user-id}/media
```

#### Parameters

The following parameters are **required** . Refer to the
[` POST /{ig-user-id}/media `](/docs/instagram-api/reference/ig-user/media#creating)
endpoint reference for additional supported parameters.

-   ` media_type ` --- Set to ` CAROUSEL ` . Indicates container is for
    a carousel.
-   ` children ` --- An array of up to 10 container IDs of each image
    and video that should appear in the published carousel. Carousels
    can have up to 10 total images, videos, or a mix of the two.

#### Sample Request

``` {._5s-8 .prettyprint .lang-curl .prettyprinted}
curl -i -X POST \ "https://graph.facebook.com/v18.0/90010177253934/media?caption=Fruit%20candies&media_type=CAROUSEL&children=17899506308402767%2C18193870522147812%2C17853844403701904&access_token=EAAOc..."
```

#### Sample Response

``` {._5s-8 .prettyprint .lang-code .prettyprinted}
{ "id": "18000748627392977"
}
```

Step 3 of 3: Publish carousel container

Use the
[` POST /{ig-user-id}/media_publish `](/docs/instagram-api/reference/ig-user/media_publish#creating)
endpoint to publish a carousel container (a carousel post). Accounts are
limited to 50 published posts within a 24-hour period. Publishing a
carousel counts as a single post.

``` {._5s-8 .prettyprint .lang-http .prettyprinted}
POST /{ig-user-id}/media_publish
```

#### Parameters

The following parameters are required.

-   ` creation_id ` --- The carousel container ID.

If the operation is successful the API will return a carousel album [IG
Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media)
ID.

#### Sample Request

``` {._5s-8 .prettyprint .lang-curl .prettyprinted}
curl -i -X POST \ "https://graph.facebook.com/v18.0/90010177253934/media_publish?creation_id=18000748627392977&access_token=EAAOc..."
```

#### Sample Response

``` {._5s-8 .prettyprint .lang-code .prettyprinted}
{ "id": "90010778390276"
}
```
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
Reels are short-form videos that are eligible to appear in the **Reels**
tab of the Instagram app if they meet certain
[specifications](/docs/instagram-api/reference/ig-user/media#reel-specifications)
and are selected by our algorithm. To publish a reel, follow the steps
for publishing a [single media post](#single-media-posts) and include
the ` media_type=REELS ` parameter along with the path to the video
using the ` video_url ` parameter.

Reels are not a new media type, even though you set ` media_type=REELS `
when you publish a reel. If you publish a reel and then request its
` media_type ` field, the value returned is ` VIDEO ` . To determine if
a published video has been designated as a reel, request its
` media_product_type ` field instead.

You can use the [code sample on GitHub
(insta_reels_publishing_api_sample)](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffbsamples%2Freels_publishing_apis%2Ftree%2Fmain%2Finsta_reels_publishing_api_sample&h=AT1iZheD6FZrTLkD8_OI8dviVeZAUQyFA1w8AcPp9M3yB8smwwgLCihBK-2-yDUwO5yCqs9e24n1C_xbI7prbdrVC7UdsCDxOcdzDOW14pMGjqjSA6j8QLHuzJe84nswRJ8CR4B9BF8IEs_b1wdqaQ)
to learn how to publish Reels to Instagram.

To make it more convenient for developers, Meta has published the full
set of Graph API calls for Instagram Reels on the Postman API Platform.
For more information, see [Postman Collections for Facebook Reels and
Instagram Reels](/docs/reels/postman) .

For more information about Reels, see [Reels Developer
Documentation](/docs/reels) .
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
::: {._57yz ._57z0 ._3-8p}
::: _57y-
Only business accounts can publish stories with the Content Publising
API at this time.
:::
:::

Stories are videos and images that are posted as IG stories on
Instagram. To publish a story, follow the same steps for publishing a
single media post and include the ` media_type=STORIES ` parameter along
with the path to the image/video using the ` image_url ` or
` video_url ` parameter.

**Note:** Stories are not a new media type even though you are setting
` media_type=STORIES ` when publishing a story. If you publish a story
and then request its ` media_type ` field, the value will be returned as
` IMAGE/VIDEO ` . To determine if a published image/video has been
designated as a story, request its ` media_product_type ` field instead.
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
You can add public Instagram users in an image, carousel and reel as a
collaborators and they will receive an invite to be a collaborator for
that particular media. To tag users in an image, follow the Single Media
Posts steps above, but when creating the media container, include the
collaborators parameter and an array of strings indicating the Instagram
usernames of users whom you want to invite as a collaborator on the
media.

#### Sample Requeset

``` {._5s-8 .prettyprint .lang-curl .prettyprinted}
POST graph.facebook.com/17841400008460056/media
?image_url=https://www.example.com/images/bronzed-fonzes.jpg
&caption=#BronzedFonzes!
&collaborators= [‘username1’,’username2’]
```

#### Notes

-   The collaborators value must be an array of strings.
-   You can only tag users with public Instagram accounts.
-   No more than 3 collaborators can be added to a media.
-   Collaborators cannot be added to Story media.
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
You can use the [Pages Search API
![](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.2365-6/310307727_3347317042262105_1088877051262827250_n.png?_nc_cat=107&ccb=1-7&_nc_sid=e280be&_nc_ohc=0iqM6GOMcgMAX-Sufh2&_nc_ht=scontent-cdg4-2.xx&oh=00_AfBhUHzPDjdzkuY0wzYMWRnR31Z8YvejaG8Y6FlqaccnFQ&oe=65C36E22){.img
width="10px"
srcset="https://scontent-cdg4-2.xx.fbcdn.net/v/t39.2365-6/310307727_3347317042262105_1088877051262827250_n.png?_nc_cat=107&ccb=1-7&_nc_sid=e280be&_nc_ohc=0iqM6GOMcgMAX-Sufh2&_nc_ht=scontent-cdg4-2.xx&oh=00_AfBhUHzPDjdzkuY0wzYMWRnR31Z8YvejaG8Y6FlqaccnFQ&oe=65C36E22"}](/docs/pages/searching)
, be sure to include the \`location\` field in your query, to search for
Pages whose names match a search string. Then, parse the results to
identify any Pages that have been created for a physical location. If
you include a Page\'s ID when publishing an image or video, it will be
tagged with the location associated with that Page.

#### Limitations

To be eligible for tagging, a Page must have latitude and longitude
location data.

Verify that the Page you want to use has latitude and longitude data in
the response. Attempting to create a container using a Page that has no
location data will fail with coded exception
` INSTAGRAM_PLATFORM_API__INVALID_LOCATION_ID ` .

Once you have the Page ID, assign it to the ` location_id ` parameter
when publishing [single media](#single-media-posts) or
[carousel](#carousel-posts) item containers.
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
You can tag public Instagram users in an image and they will receive a
notification that they have been tagged.

To tag users in an image, follow the [Single Media
Posts](#single-media-posts) steps above, but when creating the media
container, include the ` user_tags ` parameter and an array of objects
indicating the Instagram users in the image as well as their x/y
coordinates within the image itself.

#### Sample Request

``` {._5s-8 .prettyprint .lang-html .prettyprinted}
POST graph.facebook.com/17841400008460056/media ?image_url=https://www.example.com/images/bronzed-fonzes.jpg &caption=#BronzedFonzes! &user_tags= [ { username:'kevinhart4real', x: 0.5, y: 0.8 }, { username:'therock', x: 0.3, y: 0.2 } ]
```

This returns a container ID which you then publish using the [IG User
Media
Publish](/docs/instagram-api/reference/ig-user/media_publish#creating)
endpoint.

#### Notes

-   The ` user_tags ` value must be an array of objects formatted with
    JSON.
-   You can only tag users with public Instagram accounts.
-   The object must contain all three properties ( ` username ` , ` x `
    , and ` y ` ) for each user.
-   ` x ` and ` y ` values must be ` float ` numbers that originate from
    the top-left of the image, with a range of ` 0.0 ` -- ` 1.0 ` .
-   User tags can be used with images in carousels.
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
If you are able to create a container for a video but the
[` POST /{ig-user-id}/media_publish `](/docs/instagram-api/reference/ig-user/media_publish#creating)
endpoint does not return the published media ID, you can get the
container\'s publishing status by querying the
` GET /{ig-container-id}?fields=status_code ` endpoint. This endpoint
will return one of the following:

-   ` EXPIRED ` --- The container was not published within 24 hours and
    has expired.
-   ` ERROR ` --- The container failed to complete the publishing
    process.
-   ` FINISHED ` --- The container and its media object are ready to be
    published.
-   ` IN_PROGRESS ` --- The container is still in the publishing
    process.
-   ` PUBLISHED ` --- The container\'s media object has been published.

We recommend querying a container\'s status once per minute, for no more
than 5 minutes.
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
See the [Error Codes](/docs/instagram-api/reference/error-codes)
reference.
:::
:::

</div>
