<div>

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
<div>

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
*Applies to v18.0+. Will apply to all versions on December 11, 2023.*

Duplicative and legacy Instagram insight metrics are being deprecated.
Please see documentation for the endpoints and [Instagram
Insights](/docs/instagram-api/guides/insights) for more information on
which metrics to use in their place.

The following endpoints and metrics are affected:

-   [` GET /{ig-user-id}/insights `](/docs/instagram-api/reference/ig-user/insights)
    -   ` AUDIENCE_GENDER_AGE `
    -   ` AUDIENCE_LOCALE `
    -   ` AUDIENCE_COUNTRY `
    -   ` AUDIENCE_CITY `
-   [` GET /{ig-media-id}/insights `](/docs/instagram-api/reference/ig-media/insights)
    -   ` CAROUSEL_ALBUM_IMPRESSIONS `
    -   ` CAROUSEL_ALBUM_REACH `
    -   ` CAROUSEL_ALBUM_ENGAGEMENT `
    -   ` CAROUSEL_ALBUM_SAVED `
    -   ` CAROUSEL_ALBUM_VIDEO_VIEWS `
    -   ` TAPS_FORWARD `
    -   ` TAPS_BACK `
    -   ` EXITS `
    -   ` ENGAGEMENT `

**Note:** ` total_interactions ` , which is listed as an alternative for
some of the deprecated metrics, is currently only available using
version 18.0 and does not work with older versions. When querying older
versions before Dec 11, 2023, please use the ` engagement ` metric.
` total_interactions ` , which is listed as an alternative for some of
the deprecated metrics, is currently only available using version 18.0
and does not work with older versions. When querying older versions
before Dec 11, 2023, please use the ` engagement ` metric.
:::
:::

</div>
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
*Applies to all versions.*

Instagram Product Tagging API for Reels is made available. You can tag
up to 30 products when publishing a reel.
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
<div>

*Applies to all versions.*

Reels are now supported. To publish a video as a reel, set the
` media_type ` parameter to ` REELS ` when creating a [single media
post](/docs/instagram-api/guides/content-publishing#single-media-posts)
container. Refer to the
[` POST /ig-user/media endpoint `](/docs/instagram-api/reference/ig-user/media#creating)
reference to learn which parameters can be used with reels as well as
requirements for reels videos.

**Note:** Beginning November 9, 2023, the ` VIDEO ` value for
` media_type ` will no longer be supported. Use the ` REELS ` media type
to publish a video to your feed.

</div>
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
<div>

*Applies to all versions.*

You can now use the Instagram API to publish posts containing multiple
images and videos ( [carousel
posts](/docs/instagram-api/guides/content-publishing#carousel-posts) ).
Refer to the [Content
Publishing](https://developers.facebook.com/docs/instagram-api/guides/content-publishing)
guide for complete publishing steps.

If your app has already been approved for
[permissions](/docs/instagram-api/guides/content-publishing#permissions)
required for content publishing, it does not need to undergo [App
Review](/docs/app-review) again to take advantage of this functionality.

</div>
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
<div>

*Applies to all versions.*

You can now use the Instagram API to get live video IG Media being
broadcast by your app users, get comments on those videos, and use the
Instagram Messaging API to send private replies (direct messages) to the
comment authors. To support this functionality, the following changes
have been made:

-   a new [GET
    /ig-user/live_media](/docs/instagram-api/reference/ig-user/live_media#reading)
    edge can return live video [IG
    Media](/docs/instagram-api/reference/ig-media/) being broadcast by
    your app user at the time of the request
-   the ` media ` field on an [IG
    Comment](/docs/instagram-api/reference/ig-comment/) now returns and
    object containing both the ID ( ` id ` ) and published location (
    ` media_product_type ` ) of the media upon which the comment was
    made
-   a new
    [` live_comments `](/docs/graph-api/webhooks/reference/instagram/#live_comments)
    Instagram Webhooks field can send notifications containing live
    comments made on your app users\' live videos as they are being
    broadcast

Please refer to the [Instagram Messaging
API](/docs/messenger-platform/instagram) private replies documentation
to learn how to send [private
replies](/docs/messenger-platform/instagram/features/private-replies) to
users who have commented on your app users\' live video IG Media.

</div>
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
<div>

*Applies to all versions.*

Two new [fields](/docs/instagram-api/reference/ig-comment#fields) have
been added to [IG Comments](/docs/instagram-api/reference/ig-comment) :

-   ` from ` --- returns an object containing the
    [IGSID](/docs/messenger-platform/instagram/overview#igsid) ( ` id `
    ) and username ( ` username ` ) of the comment creator.
-   ` parent_id ` --- returns the ID of the parent IG Comment if this
    comment was created on another IG Comment (i.e. a reply to another
    comment).

#### Instagram Webhooks

*Applies to all versions.*

The ` comments ` Instagram webhooks
[field](/docs/graph-api/webhooks/reference/instagram/#comments) now
includes the following properties in the ` value ` field object:

-   ` from.id ` ---
    [IGSID](/docs/messenger-platform/instagram/overview#igsid) of the
    Instagram user who created the comment.
-   ` from.username ` --- Username of the Instagram user who created the
    comment
-   ` media.id ` --- ID of the IG Media upon which the comment was made.
-   ` media.media_product_type ` --- Surface (published location) of the
    IG Media upon which the comment was made.
-   ` parent_id ` --- ID of parent IG Comment if this comment was
    created on another IG Comment (i.e. a reply to another comment).

</div>
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
<div>

The following changes apply to Instagram TV videos created on or after
October 5, 2021. Instagram TV videos created before this date are exempt
from these changes.

-   the ` media_product_type `
    [field](/docs/instagram-api/reference/ig-media/#fields) will return
    ` FEED ` instead of ` IGTV `
-   the ` video_title `
    [field](/docs/instagram-api/reference/ig-media/#fields) will not be
    returned
-   [Instagram Webhooks](/docs/instagram-api/guides/webhooks)
    ` comments ` and ` mentions ` fields are now supported

On January 3, 2022, the changes above will apply to all API versions and
all Instagram TV videos, regardless of video creation date. This means
that starting January 3, 2022, apps using older API versions will be
able to query Instagram TV videos (read support was introduced in v10.0
and limited to v10.0+).

Starting with v14.0, the ` video_title ` field will no longer be
supported and the API will throw an error if the field is requested.

</div>
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
*Applies to v11.0+. Will apply to all versions September 7, 2021.*

If indirectly querying an [IG
Media](/docs/instagram-api/reference/ig-media) through another endpoint
or field expansion, the
[` like_count `](/docs/instagram-api/reference/ig-media#fields) field
will be omitted from API responses if the media owner has hidden like
counts on it. Directly querying the IG Media (which can only be done by
the IG Media owner) will return the actual like count, however, even if
like counts have been hidden.

\

#### Time-based Pagination

*Applies to v11.0+* .

Added
[` since `](/docs/instagram-api/reference/ig-media/#query-string-parameters)
and
[` until `](/docs/instagram-api/reference/ig-media/#query-string-parameters)
parameters to the
[` GET /{ig-user-id}/media `](/docs/instagram-api/reference/ig-media/#reading)
endpoint to support [time-based
pagination](/docs/graph-api/using-graph-api#time) .
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
<div>

If indirectly querying an IG Media through another endpoint, the
[like_count](/docs/instagram-api/reference/ig-media#fields) field will
now return ` 0 ` if the app user does not
[own](/docs/instagram-api/overview#authorization) the media and the
media owner has
[hidden](https://www.facebook.com/help/instagram/113355287252104) like
counts on it. Directly querying the IG Media, which can only be done by
the IG Media owner, will return the actual like count, even if the owner
has hidden like counts on the media.

</div>
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
<div>

Made a minor change to how we calculate the
[` online_followers `](/docs/instagram-api/reference/ig-user/insights#metrics-and-periods)
metric on IG Users.

</div>
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
<div>

Story [IG
Media](/docs/instagram-api/reference/ig-media/insights#metrics)
interactions performed by users in Japan are no longer included in some
` replies ` metric calculations:

-   For stories created by users in Japan, the ` replies ` metric will
    now return a value of ` 0 ` .
-   For stories created by users outside Japan, the ` replies ` metric
    will return the number of replies, but replies made by users in
    Japan will not be included in the calculation.

</div>
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
Fixed a minor bug with reach
[metrics](/docs/instagram-api/reference/ig-media/insights#metrics) on
story IG Media.
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}

-   The ` status ` field on an [IG
    Container](/docs/instagram-api/reference/ig-container) now returns
    an [error subcode](/docs/instagram-api/reference/error-codes) if the
    container\'s ` error_code ` field value is ` ERROR ` .
-   The [IG Media
    Insights](/docs/instagram-api/reference/ig-media/insights)
    ` video_views ` metric now supports albums and will return the sum
    of ` video_views ` on all videos in the album instead of ` 0 ` .
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
IGTV media is [now supported in
v10.0+](/blog/post/2021/03/15/igtv-media-mmetrics-instagram-graph-api/)
. This applies to all endpoints except those used for content publishing
and webhooks. To support this change, new ` media_product_type ` and
` video_title ` fields have been added to the [IG
Media](/docs/instagram-api/reference/ig-media) node. IGTV media must
have been shared to Instagram at the time of publish ( **Post a
Preview** or **Share Preview** to Feed enabled) in order to be
accessible via the API.
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
The Content Publishing beta has ended and all developers can now publish
media on Instagram Professional accounts. Refer to the [Content
Publishing](/docs/instagram-api/guides/content-publishing) guide for
usage details.
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
In compliance with the European Union\'s [ePrivacy
Directive](https://l.facebook.com/l.php?u=https%3A%2F%2Feur-lex.europa.eu%2Flegal-content%2FEN%2FTXT%2F%3Furi%3DCELEX%253A02002L0058-20091219&h=AT13E7YFWryPPoYL1_geokNynBd5lQ15OugVKAmqbi6B935kVqnFv634xzOCU7Cbc6HlXYzL0NHGCAtuGbzEiI7BwXXOYOlgvyunJI6BAgj0BMihTGkBas8Ap6G4C52eCzykvnUCwGloMyb-wUjASA)
, messaging-related Story [IG
Media](/docs/instagram-api/reference/ig-media) interactions performed by
users in the European Economic Area (EEA) after December 1, 2020, will
no longer be included in some metric calculations:

-   For Stories created by users in the EEA, the
    [` replies `](/docs/instagram-api/reference/ig-media/insights#metrics)
    metric will now return a value of ` 0 ` .
-   For Stories created by users outside the EEA, the
    [` replies `](/docs/instagram-api/reference/ig-media/insights#metrics)
    metric will return the number of replies, but replies made my users
    in the EEA will not be included in its calculation.

This change applies to all versions.
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
-   **IG User Insights** --- The
    [` follower_count `](/docs/instagram-api/reference/ig-user/insights)
    values now align more closely with their corresponding values
    displayed in the Instagram app. In addition,
    [` follower_count `](/docs/instagram-api/reference/ig-user/insights)
    now returns a maximum of 30 days of data instead of 2 years. This
    change applies to v9.0+ and will apply to all versions May 9, 2021.
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
-   **Insights** --- To align API behavior with Instagram app behavior,
    insights on [IG Users](/docs/instagram-api/reference/ig-user/) are
    now only available on IG Users that have 100 or more followers.
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
-   **Business Discovery** --- The [Business Discovery
    API](/docs/instagram-api/reference/ig-user/business_discovery) can
    now be used to get data about other Instagram Creator accounts.
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
-   **Webhooks** --- The ` story_insights ` field now requires the
    ` instagram_manage_insights ` permission instead of
    ` instagram_manage_comments ` .
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
-   **Hashtag Search API** --- You can now search for media tagged with
    specific hashtags by using our new [Hashtag Search
    API](/docs/instagram-api/guides/hashtag-search) . ` #spooky ` !
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
-   ` /{ig-media-id}/comments ` edge --- ` GET ` requests made using API
    version 3.1 or older will have results returned in chronological
    order. Requests made using version 3.2+ will have results returned
    in reverse chronological order.
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
-   ` /{ig-media-id} ` node --- You can now use field expansion to get
    the ` permalink ` field on media objects.
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
-   **Business Verification** --- In order to use the Instagram Graph
    API, all apps must undergo [Business
    Verification](/docs/apps/review) , which is part of the App Review
    process and now required for all Instagram Graph API endpoints. Apps
    previously reviewed before May 1st, 2018, have to be reviewed again,
    and have until August 1st, 2018 to do so, or lose access to the API.
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
-   ` /{ig-comment-id} ` node:

    -   Added a new ` username ` field.
    -   For ` GET ` requests, the ` user ` field will not be included in
        responses unless the User making the request owns the Comment;
        instead, we will return ` username ` for all commenters. This
        also applies to queries on Comments made through other APIs,
        such as the Mentions API.

-   ` /{ig-media-id} ` node:

    -   Added a new ` username ` field.
    -   For ` GET ` requests, the ` owner ` field will not be included
        in responses unless the User making the request owns the media
        object; instead, we will return ` username ` for all commenters.
        This also applies to queries on media objects made through other
        APIs, such as the Mentions API.
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
-   <div>

    **Insights API** --- Insights will now include ad activity generated
    through the API, Facebook ads interfaces, and Instagram\'s Promote
    feature. This affects the following metrics:

    </div>
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
-   **Content Publishing API** --- Beta partners can now use the
    ` /{ig-user-id}/media ` edge to tag
    [locations](/docs/instagram-api/guides/content-publishing#publish-with-locations)
    and public Instagram
    [users](/docs/instagram-api/guides/content-publishing#publish-with-tagged-users)
    when publishing photos.
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
-   **Public fields** --- The ` timestamp ` field on the
    ` /{ig-media-id} ` node is now a public field and can be returned
    via field expansion.
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
-   **Public fields** --- The ` /{ig-user-id} ` , ` /{ig-comment-id} ` ,
    and ` /{ig-media-id} ` nodes will now return all public fields when
    accessed through an edge via field expansion. Refer to each node\'s
    reference document to see which fields are public.
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
-   **Content Publishing API** --- Beta partners can now include
    hashtags when publishing photos via the ` /{ig-user-id}/media `
    edge. ` #crazywildebeest ` FTW!
:::
:::

</div>
