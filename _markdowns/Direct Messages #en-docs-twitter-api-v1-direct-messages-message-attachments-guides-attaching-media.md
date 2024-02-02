::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
[POST
direct_messages/events/new](/en/docs/direct-messages/sending-and-receiving/api-reference/new-event.html)
supports media attachments of type image, GIF and video. The process is
similar to attaching media to Tweets:

1.  Chunk upload the image, GIF or video.
2.  Send Direct Message with media attachment.

It is possible to attach the same media asset to multiple Direct
Messages. However, you must get users' express consent to set media as
"shared," and must provide them with clear notice that "shared" media
will be viewable by anyone with the media's URL. See the documented
process below for how to set media to \"shared.\"

**Note:** Media for use with Direct Messages should be uploaded using
the asynchronous chunked upload process described on this page.\

### 1. Chunk upload media

-   Chunk upload the media file starting with [POST media/upload
    (INIT)](/en/docs/media/upload-media/api-reference/post-media-upload-init.html)
    .
-   Set the [ media_category ]{.code-inline} to [ dm_image
    ]{.code-inline} , [ dm_gif ]{.code-inline} or [ dm_video
    ]{.code-inline} appropriately.
-   If reusing the media asset across multiple Direct Messages, you must
    set [ shared ]{.code-inline} to [ true ]{.code-inline} during the
    initial upload.
-   If attaching a media asset to a Welcome Message, you must
    set shared to true during the initial upload.
-   Uploaded media can only be shared across Direct Messages created by
    the same user.
-   See [Uploading
    Media](/en/docs/media/upload-media/uploading-media/chunked-media-upload.html)
    for subsequent
    [APPEND](/en/docs/media/upload-media/api-reference/post-media-upload-append.html)
    and
    [FINALIZE](/en/docs/media/upload-media/api-reference/post-media-upload-finalize.html)
    steps.
-   The returned media ID will be used when sending the Direct Message.
    If you did not set shared to true the media ID can only be used in a
    single Direct Message.

Once a media ID is generated, it must be attached to a Direct Message
within 24 hours.

#### Parameters

  ----------------------------------- -----------------------------------
  **media_category\                   The media category: [ dm_image
  ** (required)                       ]{.code-inline} , [ dm_gif
                                      ]{.code-inline} , [ dm_video
                                      ]{.code-inline}

  **shared**                          Set to [ true ]{.code-inline} if
                                      media asset will be reused for
                                      multiple Direct Messages. Default
                                      is [ false ]{.code-inline} .
  ----------------------------------- -----------------------------------

See [POST media/upload
(INIT)](/en/docs/media/upload-media/api-reference/post-media-upload-init.html)
documentation for all parameters and full details.\

### 2. Send Direct Message with media attachment

-   Define an attachment object in the message_data object in the Direct
    Message event json body.
-   Set attachment type property to [ media ]{.code-inline} .
-   Set the [ media.id ]{.code-inline} property to the media ID returned
    in the previous chunk upload process.\

#### Parameters

  ----------------------------------- -----------------------------------
  **attachment.type\                  Must be set to [ media
  ** (required)                       ]{.code-inline} .

  **attachment.media.id\              A media ID to associate with the
  ** (required)                       message. A Direct Message may only
                                      reference a single media id.
  ----------------------------------- -----------------------------------

See [POST
direct_messages/events/new](/en/docs/direct-messages/sending-and-receiving/api-reference/new-event.html)
documentation for all parameters and full details.
:::
:::
:::
:::
:::
:::
:::
:::
