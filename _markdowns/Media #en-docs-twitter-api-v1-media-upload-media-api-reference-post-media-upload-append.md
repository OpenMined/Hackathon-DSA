::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
The ` APPEND ` command is used to upload a chunk (consecutive byte
range) of the media file. For example, a 3 MB file could be split into 3
chunks of size 1 MB, and uploaded using 3 ` APPEND ` command requests.
After the entire file is uploaded, the next step is to call the
[FINALIZE
command](/en/docs/media/upload-media/api-reference/post-media-upload-finalize)
.

There are a number of advantages of uploading a media file in small
chunks:

-   Improved reliability and success rates under low bandwidth network
    conditions
-   Uploads can be paused and resumed
-   File chunks can be retried individually
-   Ability to tune chunk sizes to match changing network conditions e.g
    on cellular clients

## Request [¶](#request){.headerlink}

Requests should be ` multipart/form-data ` POST format.

**Note:** The domain for this endpoint is **upload.twitter.com**

## Response [¶](#response){.headerlink}

A successful response returns HTTP 2xx.

## Resource URL [¶](#resource-url){.headerlink}

` https://upload.twitter.com/1.1/media/upload.json `

  -------------------------- -------------------------
  Response formats           JSON
  Requires authentication?   Yes (user context only)
  Rate limited?              Yes
  -------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

  --------------- ---------- ------------------------------------------------------------------------------------------------------------------------------------------------- --------------- ---------
  Name            Required   Description                                                                                                                                       Default Value   Example
  command         required   Must be set to ` APPEND ` (case sensitive).                                                                                                                       
  media_id        required   The ` media_id ` returned from the ` INIT ` command.                                                                                                              
  media           required   The raw binary file content being uploaded. It must be \<= 5 MB, and cannot be used with ` media_data ` .                                                         
  media_data      required   The base64-encoded chunk of media file. It must be \<= 5 MB and cannot be used with ` media ` . Use raw binary (media parameter) when possible.                   
  segment_index   required   An ordered index of file chunk. It must be between 0-999 inclusive. The first segment has index 0, second segment has index 1, and so on.                         
  --------------- ---------- ------------------------------------------------------------------------------------------------------------------------------------------------- --------------- ---------

## Example Request [¶](#example-request){.headerlink}

` POST https://upload.twitter.com/1.1/media/upload.json?command=APPEND&media_id=123&segment_index=2&media_data=123 `

## Example Result [¶](#example-result){.headerlink}

    // Successful response returns HTTP 2XX code without any content body.
:::
:::
:::
:::
:::
:::
:::
