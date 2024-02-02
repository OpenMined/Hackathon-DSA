Overview

A media object represents a single photo, video or animated GIF. Media objects are used by many endpoints within the Twitter API, and may be included in Tweets, Direct Messages, user profiles, advertising creatives and elsewhere. Each media object may have multiple display or playback variants, with different resolutions or formats.  
 

Media types & size restrictions
-------------------------------

Size restrictions for uploading via API   

* Image 5 MB
* GIF 15 MB
* Video 512 MB (when using media\_category=amplify)

Creation
--------

Objects such as Tweets, Direct Messages, user profile pictures, hosted Ads cards, etc. can contain one or more media objects. These top-level objects are collectively known as entities. The relevant entity creation API (e.g. [POST statuses/update](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-statuses-update.html)) can be passed one or more media objects using a unique media\_id.

An entity which contains media object(s) can be created by following these steps:

1. Upload the media file(s) using either the recommended [chunked](https://developer.twitter.com/content/developer-twitter/en/docs/media/upload-media/uploading-media/chunked-media-upload) upload (images/GIF/video), or the older [simple](https://developer.twitter.com/en/docs/media/upload-media/api-reference/post-media-upload.html) upload (images only).
2. Receive a media\_id from step 1. This step may be repeated multiple times with different media if the entity allows multiple media\_id parameters to be passed in.
3. Create the entity by calling the appropriate endpoint, including the media\_id and other required parameters. For example, attach a media\_id to a Tweet using the [POST statuses/update](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-statuses-update.html) endpoint.

Retrieving
----------

Please refer to the [Media Object](https://developer.twitter.com/content/developer-twitter/en/docs/tweets/data-dictionary/overview/entities-object#media) in the Tweet data dictionary.

Media Best Practices

There are a few important concepts to understand when using the [POST media/upload](https://developer.twitter.com/en/docs/media/upload-media/uploading-media/media-best-practices) endpoint. Uploading media with OAuth can be a bit tricky, so we’ve outlined some things to keep in mind as well as a working sample of how to use this endpoint here.  

Keep in mind
------------

* Because the method uses multipart POST, [OAuth](https://developer.twitter.com/en/docs/basics/authentication/guides/creating-a-signature) is handled differently. POST or query string parameters are not used when calculating an OAuth signature basestring or signature. Only the `oauth_*` parameters are used.
* You may attach up to 4 photos, 1 animated GIF or 1 video in a Tweet.
* The image passed should be the raw binary of the image or binary base64 encoded, no need to otherwise encode or escape the contents as long as the Content-Type is set appropriately (when in doubt: `application/octet-stream`).
* When posting base64 encoded images, be sure to set the “Content-Transfer-Encoding: base64” on the image part of the message.
* Multi-part message boundaries must be on their own line and terminated by a CRLF.
* For working examples of how to POST using this endpoint, we recommend testing with [twurl](https://github.com/twitter/twurl). Also, take a look at the [Twitter Libraries](https://developer.twitter.com/en/docs/developer-utilities/twitter-libraries.html) available, including the [large-video-upload-python](https://github.com/twitterdev/large-video-upload-python) library.
* Use the `media_id_string` provided in the API response for Javascript and any other languages that cannot accurately represent a long integer.  
     

Media Categories
----------------

The Media Category parameter defines the use case of the media file to be uploaded, and can affect file size limits or other constraints enforced for media uploads. It’s important to use the correct media category when uploading media to avoid problems when trying to use the media. It is an optional value passed in the INIT request as part of the upload flow. If media category is not specified, the uploaded media is assumed to be a Tweet media (image, video, or GIF), depending on the content type.

The most common media categories are as follows:

* `tweet_image`
* `tweet_video`
* `tweet_gif`
* `dm_image`
* `dm_video`
* `dm_gif`
* `subtitles`

If you are an Ads API partner please refer to [these docs](https://developer.twitter.com/en/docs/ads/creatives/overview/promoted-video-overview) for more information on recommended media category for promoted video.  
  

Image specifications and recommendations
----------------------------------------

Image files must meet all of the following criteria:

* Supported image media types: JPG, PNG, GIF, WEBP
* Image size <= 5 MB, animated GIF size <= 15 MB

The file size limit above is enforced by the media upload endpoint. In addition, there is a separate product entity specific file size limit which is applied when calling the Tweet creation (or similar) endpoints with `media_id`. The file size limit and other constraints may vary depending on the `media_category` parameter.  
  

Animated GIF recommendations
----------------------------

A GIF may fail during Tweet creation even if it is within the file size limit. Adhere to the following constraints to improve success rates.

* Resolution should be <= 1280x1080 (width x height)
* Number of frames <= 350
* Number of pixels (width \* height \* num\_frames) <= 300 million
* File size <= 15Mb

In order to process larger GIFs, use the [chunked upload endpoint](https://developer.twitter.com/en/docs/media/upload-media/api-reference/post-media-upload-init.html) with the `media_category` parameter. This allows the server to process the GIF file asynchronously, which is a requirement for processing larger files. Pass `media_category=tweet_gif` to enable async upload behavior for Tweets with an animated GIF.  
 

Video specifications and recommendations
----------------------------------------

Please use the [Async Path](https://developer.twitter.com/en/docs/media/upload-media/uploading-media/chunked-media-upload) for media uploads.

**Recommended:**

* Recommended Video Codec: H264 High Profile
* Recommended Frame Rates: 30 FPS, 60 FPS
* Recommended Video Resolution: 1280x720 (landscape), 720x1280 (portrait), 720x720 (square)
* Recommended Minimum Video Bitrate: 5,000 kbps
* Recommended Minimum Audio Bitrate: 128 kbps
* Recommended Audio Codec: AAC LC
* Recommended Aspect Ratio: 16:9 (landscape or portrait), 1:1 (square)

**Advanced:**

* Frame rate must be 60 FPS or less
* Dimensions must be between 32x32 and 1280x1024
* File size must not exceed 512 mb
* Duration must be between 0.5 seconds and 140 seconds
* Aspect ratio must be between 1:3 and 3:1
* Must have 1:1 [pixel aspect ratio](https://en.wikipedia.org/wiki/Pixel_aspect_ratio)
* Only [YUV](https://en.wikipedia.org/wiki/YUV) 4:2:0 pixel format is supported
* Audio must be [AAC with Low Complexity profile](https://en.wikipedia.org/wiki/Advanced_Audio_Coding#Modular_encoding). High-Efficiency AAC is not supported
* Audio must be mono or stereo, not 5.1 or greater
* Must not have [open GOP](https://en.wikipedia.org/wiki/Group_of_pictures)
* Must use [progressive scan](https://en.wikipedia.org/wiki/Progressive_scan) 

**Additional Information:**

In the table below each row represents an upload recommendation, but is not a requirement. All uploads are processed for optimization across multiple platforms.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Orientation** | **Width** | **Height** | **Video Bitrate** | **Audio Bitrate** |
| Landscape | 1280 | 720 | 2048K | 128K |
| Landscape | 640 | 360 | 768K | 64K |
| Landscape | 320 | 180 | 256K | 64K |
| Portrait | 720 | 1280 | 2048K | 128K |
| Portrait | 360 | 640 | 768K | 64K |
| Portrait | 180 | 320 | 256K | 64K |
| Square | 720 | 720 | 2048K | 128K |
| Square | 480 | 480 | 768K | 64K |
| Square | 240 | 240 | 256K | 32K |

  
For an example of how to upload media, please see the [chunked media upload documentation](https://developer.twitter.com/content/developer-twitter/en/docs/media/upload-media/uploading-media/chunked-media-upload).  
 

Troubleshooting
---------------

For issues with the Media APIs, browse the [Media API category](https://twittercommunity.com/c/twitter-api/media-apis/34) in the developer forums for an answer.

Chunked media upload

Example of chunked video media/upload  

----------------------------------------

Using the [chunked POST media/upload](https://developer.twitter.com/en/docs/media/upload-media/api-reference/post-media-upload-init.html) endpoints requires an adjusted workflow from single image uploads. For video or chunked uploads, you must:

* Initialize the upload using the INIT command
* Upload each chunk of bytes using the APPEND command
* Complete the upload using the FINALIZE command

See the [large video upload sample](https://github.com/twitterdev/large-video-upload-python/) for an example written in Python.

Below is a working example using the command-line [twurl](https://github.com/twitter/twurl) utility. To see full headers of the requests and responses when using twurl, use the -t option to enable trace mode.

**INIT**

      `twurl -H upload.twitter.com "/1.1/media/upload.json" -d "command=INIT&media_type=video/mp4&total_bytes=4430752"`
    

      `{   "media_id": 601413451156586496,   "media_id_string": "601413451156586496",   "expires_after_secs": 3599 }`
    

**APPEND**  

      `twurl -H upload.twitter.com "/1.1/media/upload.json" -d "command=APPEND&media_id=601413451156586496&segment_index=0" --file /path/to/video.mp4 --file-field "media"`
    

HTTP 2XX will be returned with an empty response body on successful upload.  

**FINALIZE**

      `twurl -H upload.twitter.com "/1.1/media/upload.json" -d "command=FINALIZE&media_id=601413451156586496"`
    

      `{   "media_id": 601413451156586496,   "media_id_string": "601413451156586496",   "size": 4430752,   "expires_after_secs": 3600,   "video": {     "video_type": "video/mp4"   } }`
    

Troubleshooting  

------------------

For issues with the Media APIs:

* Browse the [Media API category](https://twittercommunity.com/c/twitter-api/media-apis/) in the developer forums.

POST media/upload (INIT)

post-media-upload-init

POST media/upload (INIT)
========================

Overview[¶](#overview "Permalink to this headline")
---------------------------------------------------

The `INIT` command request is used to initiate a file upload session. It returns a `media_id` which should be used to execute all subsequent requests. The next step after a successful return from INIT command is the [APPEND command](https://developer.twitter.com/en/docs/media/upload-media/api-reference/post-media-upload-append).

See the [Uploading media guide](https://developer.twitter.com/en/docs/media/upload-media/uploading-media/media-best-practices) for constraints and requirements on media files.

Request[¶](#request "Permalink to this headline")
-------------------------------------------------

Requests should be either `multipart/form-data` or `application/x-www-form-urlencoded` POST formats.

**Note:** The domain for this endpoint is **upload.twitter.com**

Response[¶](#response "Permalink to this headline")
---------------------------------------------------

The response provides a media identifier in the `media_id` (64-bit integer) and `media_id_string` (string) fields. Use the `media_id_string` provided in the API response from JavaScript and other languages that cannot accurately represent a long integer.

The entire file must be uploaded before `expires_after_secs` seconds.

The `additional_owners` field enables media to be uploaded media as user A and then used to create Tweets as user B.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://upload.twitter.com/1.1/media/upload.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| command | required | Must be set to `INIT` (case sensitive). |     |     |
| total\_bytes | required | The size of the media being uploaded in bytes. |     |     |
| media\_type | required | The MIME type of the media being uploaded. |     | `video/mp4` |
| media\_category | sometimes | A string enum value which identifies a media usecase. This identifier is used to enforce usecase specific constraints (e.g. file size, video duration) and enable advanced features. |     |     |
| additional\_owners | optional | A comma-separated list of user IDs to set as additional owners allowed to use the returned `media_id` in Tweets or Cards. Up to 100 additional owners may be specified. |     |     |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`POST https://upload.twitter.com/1.1/media/upload.json?command=INIT&total_bytes=10240&media_type=image/jpeg`

Example Result[¶](#example-result "Permalink to this headline")
---------------------------------------------------------------

    {
      "media_id": 710511363345354753,
      "media_id_string": "710511363345354753",
      "size": 11065,
      "expires_after_secs": 86400,
      "image": {
        "image_type": "image/jpeg",
        "w": 800,
        "h": 320
      }
    }

POST media/upload (APPEND)

post-media-upload-append

POST media/upload (APPEND)
==========================

Overview[¶](#overview "Permalink to this headline")
---------------------------------------------------

The `APPEND` command is used to upload a chunk (consecutive byte range) of the media file. For example, a 3 MB file could be split into 3 chunks of size 1 MB, and uploaded using 3 `APPEND` command requests. After the entire file is uploaded, the next step is to call the [FINALIZE command](https://developer.twitter.com/en/docs/media/upload-media/api-reference/post-media-upload-finalize).

There are a number of advantages of uploading a media file in small chunks:

* Improved reliability and success rates under low bandwidth network conditions
* Uploads can be paused and resumed
* File chunks can be retried individually
* Ability to tune chunk sizes to match changing network conditions e.g on cellular clients

Request[¶](#request "Permalink to this headline")
-------------------------------------------------

Requests should be `multipart/form-data` POST format.

**Note:** The domain for this endpoint is **upload.twitter.com**

Response[¶](#response "Permalink to this headline")
---------------------------------------------------

A successful response returns HTTP 2xx.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://upload.twitter.com/1.1/media/upload.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| command | required | Must be set to `APPEND` (case sensitive). |     |     |
| media\_id | required | The `media_id` returned from the `INIT` command. |     |     |
| media | required | The raw binary file content being uploaded. It must be <= 5 MB, and cannot be used with `media_data`. |     |     |
| media\_data | required | The base64-encoded chunk of media file. It must be <= 5 MB and cannot be used with `media`. Use raw binary (media parameter) when possible. |     |     |
| segment\_index | required | An ordered index of file chunk. It must be between 0-999 inclusive. The first segment has index 0, second segment has index 1, and so on. |     |     |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`POST https://upload.twitter.com/1.1/media/upload.json?command=APPEND&media_id=123&segment_index=2&media_data=123`

Example Result[¶](#example-result "Permalink to this headline")
---------------------------------------------------------------

    // Successful response returns HTTP 2XX code without any content body.

GET media/upload (STATUS)

get-media-upload-status

GET media/upload (STATUS)
=========================

Overview[¶](#overview "Permalink to this headline")
---------------------------------------------------

The `STATUS` command is used to periodically poll for updates of media processing operation. After the `STATUS` command response returns `succeeded`, you can move on to the next step which is usually create Tweet with media\_id.

Request[¶](#request "Permalink to this headline")
-------------------------------------------------

It should be a HTTP GET request with url params.

**Note:** The domain for this endpoint is **upload.twitter.com**

Response[¶](#response "Permalink to this headline")
---------------------------------------------------

The response body contains `processing_info` field which provides information about current state of media processing operation. It contains a `state` field which has transition flow: “pending” -> “in\_progress” -> \[“failed” | “succeeded”\]. You can not use the media\_id to create Tweet or other entities before the state field is set to “succeeded”.

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| command | required | Must be set to `STATUS` (case sensitive). |     |     |
| media\_id | required | The `media_id` returned from the `INIT` command. |     |     |

Example request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`GET https://upload.twitter.com/1.1/media/upload.json?command=STATUS&media_id=710511363345354753`

Example Result[¶](#example-result "Permalink to this headline")
---------------------------------------------------------------

    // Example of an in_progress response:
    
    {
      "media_id":710511363345354753,
      "media_id_string":"710511363345354753",
      "expires_after_secs":3595,
      "processing_info":{
        "state":"in_progress", // state transition flow is pending -> in_progress -> [failed|succeeded]
        "check_after_secs":10, // check for the update after 10 seconds
        "progress_percent":8 // Optional [0-100] int value. Please don't use it as a replacement of "state" field.
      }
    }
    
    // Example of a failed response:
    
    {
      "media_id":710511363345354753,
      "media_id_string":"710511363345354753",
      "processing_info":{
        "state":"failed",
        "progress_percent":12,
        "error":{
          "code":1,
          "name":"InvalidMedia",
          "message":"Unsupported video format"
        }
      }
    }
    
    // Example of a succeeded response:
    
    {
      "media_id":710511363345354753,
      "media_id_string":"710511363345354753",
      "expires_after_secs":3593,
      "video":{
        "video_type":"video/mp4"
      },
      "processing_info":{
        "state":"succeeded",
        "progress_percent":100,
      }
    }

POST media/upload (FINALIZE)

post-media-upload-finalize

POST media/upload (FINALIZE)
============================

Overview[¶](#overview "Permalink to this headline")
---------------------------------------------------

The `FINALIZE` command should be called after the entire media file is uploaded using `APPEND` commands. If and (only if) the response of the `FINALIZE` command contains a `processing_info` field, it may also be necessary to use a [STATUS command](https://developer.twitter.com/en/docs/media/upload-media/api-reference/get-media-upload-status) and wait for it to return success before proceeding to Tweet creation.

Request[¶](#request "Permalink to this headline")
-------------------------------------------------

Requests should be either `multipart/form-data` or `application/x-www-form-urlencoded` POST formats.

**Note:** The domain for this endpoint is **upload.twitter.com**

Response[¶](#response "Permalink to this headline")
---------------------------------------------------

The response provides a media identifier in the `media_id` (64-bit integer) and `media_id_string` (string) fields. Use the `media_id_string` provided in the API response from JavaScript and other languages that cannot accurately represent a long integer.

The returned mediaId is only valid for `expires_after_secs` seconds. Any attempt to use mediaId after this time period in other API calls will result in a Bad Request (HTTP 4xx) response.

If the response contains a `processing_info` field, then use the `STATUS` command to poll for the status of the `FINALIZE` operation. The async finalize approach is used for cases where media processing requires more time. In future, all video and animated GIF processing will only be supported using async finalize. This behavior is enabled if an upload session was [initialized](https://developer.twitter.com/en/docs/media/upload-media/api-reference/post-media-upload-init) with a media\_category parameter, and when then media type is either video or animated GIF.

If a `processing_info` field is NOT returned in the response, then `media_id` is ready for use in other API endpoints.

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| command | required | Must be set to `FINALIZE` (case sensitive). |     |     |
| media\_id | required | The `media_id` returned from the `INIT` command. |     |     |

Example request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`POST https://upload.twitter.com/1.1/media/upload.json?command=FINALIZE&media_id=710511363345354753`

Example Result[¶](#example-result "Permalink to this headline")
---------------------------------------------------------------

    // Example of sync FINALIZE response
    {
      "media_id": 710511363345354753,
      "media_id_string": "710511363345354753",
      "size": 11065,
      "expires_after_secs": 86400,
      "video": {
        "video_type": "video/mp4"
      }
    }
    
    // Example of async FINALIZE response which requires further STATUS command call(s)
    {
      "media_id": 710511363345354753,
      "media_id_string": "710511363345354753",
      "expires_after_secs": 86400,
      "size": 10240,
      "processing_info": {
        "state": "pending",
        "check_after_secs": 5 // check after 5 seconds for update using STATUS command
      }
    }

POST media/upload

post-media-upload

POST media/upload
=================

Overview[¶](#overview "Permalink to this headline")
---------------------------------------------------

Use this endpoint to upload images to Twitter.

This endpoint returns a `media_id` by default and can optionally return a `media_key` when a `media_category` is specified. These values are used by Twitter endpoints that accept images.

For example, a `media_id` value can be used to create a Tweet with an attached photo using the [POST statuses/update](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-statuses-update#post-statuses-update) endpoint.

All [Ads API endpoints](https://developer.twitter.com/en/docs/ads/) require a `media_key`. For example, a `media_key` value can be used to create a Draft Tweet with a photo using the [POST accounts/:account\_id/draft\_tweets](https://developer.twitter.com/en/docs/ads/creatives/api-reference/draft-tweets) endpoint.

Usage[¶](#usage "Permalink to this headline")
---------------------------------------------

This is a simple image upload endpoint with a limited set of features. The preferred alternative is the chunked upload endpoint which supports both images and videos, provides better reliability, allows resumption of file uploads, and other important features. In the future, new features will only be supported for the chunked upload endpoint.

* See the [Uploading media guide](https://developer.twitter.com/en/docs/media/upload-media/uploading-media/media-best-practices) for constraints and requirements on media files.
* See the [Uploading Media tutorial](https://developer.twitter.com/en/docs/tutorials/uploading-media) for step-by-step instructions on uploading an image.
* Use the [media metadata endpoint](https://developer.twitter.com/en/docs/media/upload-media/api-reference/post-media-metadata-create) to provide image alt text information.
* Ensure the POST is a `multipart/form-data` request. Either upload the raw binary (`media` parameter) of the file, or its base64-encoded contents (`media_data` parameter). Use raw binary when possible, because base64 encoding results in larger file sizes
* The response provides a media identifier in the `media_id` (64-bit integer) and `media_id_string` (string) fields. Use the `media_id_string` provided in the API response from JavaScript and other languages that cannot accurately represent a long integer.
* The returned `media_id` and `media_key` are only valid for `expires_after_secs` seconds. Any attempt to use either after this time period in other endpoints will result in an HTTP 4xx Bad Request.
* The `additional_owners` field enables media to be uploaded as user A and then used to create Tweets as user B.
* Please note that to upload videos or GIFs (`tweet_video`, `amplify_video`, and `tweet_gif`), you need to use the [chunked upload end-point](https://developer.twitter.com/en/docs/media/upload-media/api-reference/post-media-upload-init).

Request[¶](#request "Permalink to this headline")
-------------------------------------------------

Requests should be either `multipart/form-data` or `application/x-www-form-urlencoded` POST formats.

**Note:** The domain for this endpoint is **upload.twitter.com**

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://upload.twitter.com/1.1/media/upload.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

| Name | Required | Description | Default Value | Example |
| --- | --- | --- | --- | --- |
| media | required | The raw binary file content being uploaded. Cannot be used with `media_data`. |     |     |
| media\_category | optional | The category that represents how the media will be used. This field is required when using the media with the Ads APIPossible values: `amplify_video`, `tweet_gif`, `tweet_image`, and `tweet_video` |     |     |
| media\_data | required | The base64-encoded file content being uploaded. Cannot be used with `media`. |     |     |
| additional\_owners | optional | A comma-separated list of user IDs to set as additional owners allowed to use the returned `media_id` in Tweets or Cards. Up to 100 additional owners may be specified. |     |     |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`POST https://upload.twitter.com/1.1/media/upload.json?media_category=tweet_image`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
      "media_id": 710511363345354753,
      "media_id_string": "710511363345354753",
      "media_key": "3_710511363345354753",
      "size": 11065,
      "expires_after_secs": 86400,
      "image": {
        "image_type": "image/jpeg",
        "w": 800,
        "h": 320
      }
    }

POST media/metadata/create

post-media-metadata-create

POST media/metadata/create
==========================

Overview[¶](#overview "Permalink to this headline")
---------------------------------------------------

This endpoint can be used to provide additional information about the uploaded `media_id`. This feature is currently only supported for images and GIFs.

The request flow should be:

1. Upload media using either the [simple upload endpoint](https://developer.twitter.com/en/docs/media/upload-media/api-reference/post-media-upload) or the (preferred) [chunked upload endpoint](https://developer.twitter.com/en/docs/media/upload-media/api-reference/post-media-upload-init).
2. Call this endpoint to attach additional metadata such as image alt text.
3. Create Tweet with `media_id(s)` attached.

Request[¶](#request "Permalink to this headline")
-------------------------------------------------

Requests should be HTTP POST with a JSON content body, and Content-Type `application/json; charset=UTF-8` or `text/plain; charset=UTF-8`.

**Note:** The domain for this endpoint is **upload.twitter.com**

Response[¶](#response "Permalink to this headline")
---------------------------------------------------

A successful response returns HTTP 2xx.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://upload.twitter.com/1.1/media/metadata/create.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`POST https://upload.twitter.com/1.1/media/metadata/create.json`

    {
      "media_id":"692797692624265216",
      // image alt text metadata
      "alt_text": {
        "text":"dancing cat" // Must be <= 1000 chars
      }
    }

POST media/subtitles/delete

post-media-subtitles-delete

POST media/subtitles/delete
===========================

Overview
========

Use this endpoint to dissociate subtitles from a video and delete the subtitles. You can dissociate subtitles from a video before or after Tweeting.

Request
=======

Requests should be HTTP POST with a JSON content body, and Content-Type `application/json; charset=UTF-8`

**Note:** The domain for this endpoint is **upload.twitter.com**

Response Codes
==============

This endpoint returns the following HTTP responses:

|     |     |     |
| --- | --- | --- |
| Status | Text | Description |
| 200 | OK  | The request to create the subtitle was successful. |
| 400 | Bad Request | Generally, this response occurs due to the presence of invalid JSON in the request, or where the request failed to send any JSON payload. In this case this error could indicate an invalid subtitle file. |
| 403 | Unauthorized | HTTP authentication failed due to invalid credentials. Check your OAuth keys and tokens. |
| 404 | Not Found | The resource was not found at the URL to which the request was sent, likely because an incorrect media\_id |
| 500 | Internal Server Error | There was an error on Twitter's side. Retry your request using an exponential backoff pattern. |
| 503 | Service Unavailable | There was an error on Twitter's side. Retry your request using an exponential backoff pattern. |

Resource URL
============

`https://upload.twitter.com/1.1/media/subtitles/delete.json`

Resource Information
====================

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

Example Request
===============

    POST https://upload.twitter.com/1.1/media/subtitles/delete.json
    
      {
        "media_id":"692797692624265216",
        "media_category":"TweetVideo",
        "subtitle_info": {
          "subtitles": [
            "language_code":"EN", //The language code should be a BCP47 code (e.g. 'en", "sp")
          ]
        }
      }

POST media/subtitles/create

post-media-subtitles-create

POST media/subtitles/create
===========================

Overview
========

Use this endpoint to associate uploaded subtitles to an uploaded video. You can associate subtitles to video before or after Tweeting.

Request flow for associating subtitle to video before the video is Tweeted : 1. Upload video using the chunked upload endpoint and get the video media\_id. 2. Upload subtitle using the chunked upload endpoint with media category set to “Subtitles” and get the subtitle media\_id. 3. Call this endpoint to associate the subtitle to the video. 4. Create Tweet with the video media\_id.

Request flow for associating subtitle to video after the video is Tweeted : 1. Upload video using the chunked upload endpoint and get the video media\_id. 2. Create Tweet with the video media\_id. 3. Upload subtitle using the chunked upload endpoint with media category set to SUBTITLES and get the subtitle media\_id. 4. Call this endpoint to associate the subtitle to the video.

Request
=======

Requests should be HTTP POST with a JSON content body, and Content-Type `application/json; charset=UTF-8`

**Note:** The domain for this endpoint is **upload.twitter.com**

Response
========

This endpoint returns the following HTTP responses:

|     |     |     |
| --- | --- | --- |
| Status | Text | Description |
| 200 | OK  | The request to create the subtitle was successful. |
| 400 | Bad Request | Generally, this response occurs due to the presence of invalid JSON in the request, or where the request failed to send any JSON payload. In this case this error could indicate an invalid subtitle file. |
| 403 | Unauthorized | HTTP authentication failed due to invalid credentials. Check your OAuth keys and tokens. |
| 404 | Not Found | The resource was not found at the URL to which the request was sent, likely because an incorrect media\_id |
| 500 | Internal Server Error | There was an error on Twitter's side. Retry your request using an exponential backoff pattern. |
| 503 | Service Unavailable | There was an error on Twitter's side. Retry your request using an exponential backoff pattern. |

Resource URL
============

`https://upload.twitter.com/1.1/media/subtitles/create.json`

Resource Information
====================

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

Example Request
===============

    POST https://upload.twitter.com/1.1/media/subtitles/create.json
    
        {
          "media_id":"692797692624265216",
          "media_category":"TweetVideo",
          "subtitle_info": {
            "subtitles": [
              "media_id":"105195515189863968",
              "language_code":"EN", //The language code should be a BCP47 code (e.g. 'en", "sp"),
              "display_name":"English"
            ]
          }
        }

Example Result
==============

    // Successful response returns HTTP 2XX code without any content body.