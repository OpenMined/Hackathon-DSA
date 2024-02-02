::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
A media object represents a single photo, video or animated GIF. Media
objects are used by many endpoints within the Twitter API, and may be
included in Tweets, Direct Messages, user profiles, advertising
creatives and elsewhere. Each media object may have multiple display or
playback variants, with different resolutions or formats.\

## Media types & size restrictions

Size restrictions for uploading via API\

-   Image 5 MB
-   GIF 15 MB
-   Video 512 MB (when using [ media_category=amplify ]{.code-inline} )

## Creation

Objects such as Tweets, Direct Messages, user profile pictures, hosted
Ads cards, etc. can contain one or more media objects. These top-level
objects are collectively known as entities. The relevant entity creation
API (e.g. [POST
statuses/update](/en/docs/tweets/post-and-engage/api-reference/post-statuses-update.html)
) can be passed one or more media objects using a unique media_id.

An entity which contains media object(s) can be created by following
these steps:

1.  Upload the media file(s) using either the recommended
    [chunked](/content/developer-twitter/en/docs/media/upload-media/uploading-media/chunked-media-upload)
    upload (images/GIF/video), or the older
    [simple](/en/docs/media/upload-media/api-reference/post-media-upload.html)
    upload (images only).
2.  Receive a media_id from step 1. This step may be repeated multiple
    times with different media if the entity allows
    multiple media_id parameters to be passed in.
3.  Create the entity by calling the appropriate endpoint, including
    the media_id and other required parameters. For example, attach
    a media_id to a Tweet using the [POST
    statuses/update](/en/docs/tweets/post-and-engage/api-reference/post-statuses-update.html)
    endpoint.

## Retrieving

Please refer to the [Media
Object](/content/developer-twitter/en/docs/tweets/data-dictionary/overview/entities-object#media)
in the Tweet data dictionary.
:::
:::
:::
:::
:::
:::
:::
:::
