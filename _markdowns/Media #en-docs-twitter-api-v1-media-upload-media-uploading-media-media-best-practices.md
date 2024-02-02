::: is-table-default
There are a few important concepts to understand when using the [POST
media/upload](/en/docs/media/upload-media/uploading-media/media-best-practices)
endpoint. Uploading media with OAuth can be a bit tricky, so we've
outlined some things to keep in mind as well as a working sample of how
to use this endpoint here.\

## Keep in mind

-   Because the method uses multipart POST,
    [OAuth](/en/docs/basics/authentication/guides/creating-a-signature)
    is handled differently. POST or query string parameters are not used
    when calculating an OAuth signature basestring or signature. Only
    the ` oauth_* ` parameters are used.
-   You may attach up to 4 photos, 1 animated GIF or 1 video in a Tweet.
-   The image passed should be the raw binary of the image or binary
    base64 encoded, no need to otherwise encode or escape the contents
    as long as the Content-Type is set appropriately (when in doubt:
    ` application/octet-stream ` ).
-   When posting base64 encoded images, be sure to set the
    "Content-Transfer-Encoding: base64" on the image part of the
    message.
-   Multi-part message boundaries must be on their own line and
    terminated by a CRLF.
-   For working examples of how to POST using this endpoint, we
    recommend testing with [twurl](https://github.com/twitter/twurl) .
    Also, take a look at the [Twitter
    Libraries](/en/docs/developer-utilities/twitter-libraries.html)
    available, including the
    [large-video-upload-python](https://github.com/twitterdev/large-video-upload-python)
    library.
-   Use the ` media_id_string ` provided in the API response for
    Javascript and any other languages that cannot accurately represent
    a long integer.\

## Media Categories

The Media Category parameter defines the use case of the media file to
be uploaded, and can affect file size limits or other constraints
enforced for media uploads. It's important to use the correct media
category when uploading media to avoid problems when trying to use the
media. It is an optional value passed in the INIT request as part of the
upload flow. If media category is not specified, the uploaded media is
assumed to be a Tweet media (image, video, or GIF), depending on the
content type.

The most common media categories are as follows:

-   ` tweet_image `
-   ` tweet_video `
-   ` tweet_gif `
-   ` dm_image `
-   ` dm_video `
-   ` dm_gif `
-   ` subtitles `

If you are an Ads API partner please refer to [these
docs](/en/docs/ads/creatives/overview/promoted-video-overview) for more
information on recommended media category for promoted video.

## Image specifications and recommendations

Image files must meet all of the following criteria:

-   Supported image media types: JPG, PNG, GIF, WEBP
-   Image size \<= 5 MB, animated GIF size \<= 15 MB

The file size limit above is enforced by the media upload endpoint. In
addition, there is a separate product entity specific file size limit
which is applied when calling the Tweet creation (or similar) endpoints
with ` media_id ` . The file size limit and other constraints may vary
depending on the ` media_category ` parameter.

## Animated GIF recommendations

A GIF may fail during Tweet creation even if it is within the file size
limit. Adhere to the following constraints to improve success rates.

-   Resolution should be \<= 1280x1080 (width x height)
-   Number of frames \<= 350
-   Number of pixels (width \* height \* num_frames) \<= 300 million
-   File size \<= 15Mb

In order to process larger GIFs, use the [chunked upload
endpoint](/en/docs/media/upload-media/api-reference/post-media-upload-init.html)
with the ` media_category ` parameter. This allows the server to process
the GIF file asynchronously, which is a requirement for processing
larger files. Pass ` media_category=tweet_gif ` to enable async upload
behavior for Tweets with an animated GIF.\

## Video specifications and recommendations

Please use the [Async
Path](/en/docs/media/upload-media/uploading-media/chunked-media-upload)
for media uploads.

**Recommended:**

-   Recommended Video Codec: H264 High Profile
-   Recommended Frame Rates: 30 FPS, 60 FPS
-   Recommended Video Resolution: 1280x720 (landscape), 720x1280
    (portrait), 720x720 (square)
-   Recommended Minimum Video Bitrate: 5,000 kbps
-   Recommended Minimum Audio Bitrate: 128 kbps
-   Recommended Audio Codec: AAC LC
-   Recommended Aspect Ratio: 16:9 (landscape or portrait), 1:1 (square)

**Advanced:**

-   Frame rate must be 60 FPS or less
-   Dimensions must be between 32x32 and 1280x1024
-   File size must not exceed 512 mb
-   Duration must be between 0.5 seconds and 140 seconds
-   Aspect ratio must be between 1:3 and 3:1
-   Must have 1:1 [pixel aspect
    ratio](https://en.wikipedia.org/wiki/Pixel_aspect_ratio)
-   Only [YUV](https://en.wikipedia.org/wiki/YUV) 4:2:0 pixel format is
    supported
-   Audio must be [AAC with Low Complexity
    profile](https://en.wikipedia.org/wiki/Advanced_Audio_Coding#Modular_encoding)
    . High-Efficiency AAC is not supported
-   Audio must be mono or stereo, not 5.1 or greater
-   Must not have [open
    GOP](https://en.wikipedia.org/wiki/Group_of_pictures)
-   Must use [progressive scan\
    ](https://en.wikipedia.org/wiki/Progressive_scan)

**Additional Information:**

In the table below each row represents an upload recommendation, but is
not a requirement. All uploads are processed for optimization across
multiple platforms.

  ----------------- ----------- ------------ ------------------- -------------------
  **Orientation**   **Width**   **Height**   **Video Bitrate**   **Audio Bitrate**
  Landscape         1280        720          2048K               128K
  Landscape         640         360          768K                64K
  Landscape         320         180          256K                64K
  Portrait          720         1280         2048K               128K
  Portrait          360         640          768K                64K
  Portrait          180         320          256K                64K
  Square            720         720          2048K               128K
  Square            480         480          768K                64K
  Square            240         240          256K                32K
  ----------------- ----------- ------------ ------------------- -------------------

\
For an example of how to upload media, please see the [chunked media
upload
documentation](/content/developer-twitter/en/docs/media/upload-media/uploading-media/chunked-media-upload)
.\

## Troubleshooting

For issues with the Media APIs, browse the [Media API
category](https://twittercommunity.com/c/twitter-api/media-apis/34) in
the developer forums for an answer.
:::
