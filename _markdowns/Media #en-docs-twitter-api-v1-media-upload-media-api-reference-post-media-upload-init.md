::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
The ` INIT ` command request is used to initiate a file upload session.
It returns a ` media_id ` which should be used to execute all subsequent
requests. The next step after a successful return from INIT command is
the [APPEND
command](/en/docs/media/upload-media/api-reference/post-media-upload-append)
.

See the [Uploading media
guide](/en/docs/media/upload-media/uploading-media/media-best-practices)
for constraints and requirements on media files.

## Request [¶](#request){.headerlink}

Requests should be either ` multipart/form-data ` or
` application/x-www-form-urlencoded ` POST formats.

**Note:** The domain for this endpoint is **upload.twitter.com**

## Response [¶](#response){.headerlink}

The response provides a media identifier in the ` media_id ` (64-bit
integer) and ` media_id_string ` (string) fields. Use the
` media_id_string ` provided in the API response from JavaScript and
other languages that cannot accurately represent a long integer.

The entire file must be uploaded before ` expires_after_secs ` seconds.

The ` additional_owners ` field enables media to be uploaded media as
user A and then used to create Tweets as user B.

## Resource URL [¶](#resource-url){.headerlink}

` https://upload.twitter.com/1.1/media/upload.json `

  -------------------------- -------------------------
  Response formats           JSON
  Requires authentication?   Yes (user context only)
  Rate limited?              Yes
  -------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

  ------------------- ----------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------- ---------------
  Name                Required    Description                                                                                                                                                                            Default Value   Example
  command             required    Must be set to ` INIT ` (case sensitive).                                                                                                                                                              
  total_bytes         required    The size of the media being uploaded in bytes.                                                                                                                                                         
  media_type          required    The MIME type of the media being uploaded.                                                                                                                                                             ` video/mp4 `
  media_category      sometimes   A string enum value which identifies a media usecase. This identifier is used to enforce usecase specific constraints (e.g. file size, video duration) and enable advanced features.                   
  additional_owners   optional    A comma-separated list of user IDs to set as additional owners allowed to use the returned ` media_id ` in Tweets or Cards. Up to 100 additional owners may be specified.                              
  ------------------- ----------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------- ---------------

## Example Request [¶](#example-request){.headerlink}

` POST https://upload.twitter.com/1.1/media/upload.json?command=INIT&total_bytes=10240&media_type=image/jpeg `

## Example Result [¶](#example-result){.headerlink}

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
:::
:::
:::
:::
:::
:::
:::
