::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
This endpoint can be used to provide additional information about the
uploaded ` media_id ` . This feature is currently only supported for
images and GIFs.

The request flow should be:

## Request [¶](#request){.headerlink}

Requests should be HTTP POST with a JSON content body, and Content-Type
` application/json; charset=UTF-8 ` or ` text/plain; charset=UTF-8 ` .

**Note:** The domain for this endpoint is **upload.twitter.com**

## Response [¶](#response){.headerlink}

A successful response returns HTTP 2xx.

## Resource URL [¶](#resource-url){.headerlink}

` https://upload.twitter.com/1.1/media/metadata/create.json `

  -------------------------- -------------------------
  Response formats           JSON
  Requires authentication?   Yes (user context only)
  Rate limited?              Yes
  -------------------------- -------------------------

## Example Request [¶](#example-request){.headerlink}

` POST https://upload.twitter.com/1.1/media/metadata/create.json `

    {
      "media_id":"692797692624265216",
      // image alt text metadata
      "alt_text": {
        "text":"dancing cat" // Must be <= 1000 chars
      }
    }
:::
:::
:::
:::
:::
:::
:::
