::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
Use this endpoint to dissociate subtitles from a video and delete the
subtitles. You can dissociate subtitles from a video before or after
Tweeting.

## Request

Requests should be HTTP POST with a JSON content body, and Content-Type
` application/json; charset=UTF-8 `

**Note:** The domain for this endpoint is **upload.twitter.com**

## Response Codes

This endpoint returns the following HTTP responses:

  -------- ----------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Status   Text                    Description
  200      OK                      The request to create the subtitle was successful.
  400      Bad Request             Generally, this response occurs due to the presence of invalid JSON in the request, or where the request failed to send any JSON payload. In this case this error could indicate an invalid subtitle file.
  403      Unauthorized            HTTP authentication failed due to invalid credentials. Check your OAuth keys and tokens.
  404      Not Found               The resource was not found at the URL to which the request was sent, likely because an incorrect media_id
  500      Internal Server Error   There was an error on Twitter\'s side. Retry your request using an exponential backoff pattern.
  503      Service Unavailable     There was an error on Twitter\'s side. Retry your request using an exponential backoff pattern.
  -------- ----------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Resource URL

` https://upload.twitter.com/1.1/media/subtitles/delete.json `

  -------------------------- -------------------------
  Response formats           JSON
  Requires authentication?   Yes (user context only)
  Rate limited?              Yes
  -------------------------- -------------------------

## Example Request

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
:::
:::
:::
:::
:::
:::
:::
