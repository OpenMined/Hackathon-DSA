::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
Deletes a custom profile that was created with [POST
custom_profiles/new.json](/en/docs/direct-messages/custom-profiles/api-reference/new-profile)
.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/custom_profiles/destroy.json `

  --------------------------------------- -------------------------
  Response formats                        JSON
  Requires authentication?                Yes (user context only)
  Rate limited?                           Yes
  Requests / 24 hour window (user auth)   Yes (1000 / 1 day)
  --------------------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

  ------------------- -------------------------------------------------
  **id** (required)   The string ID of the custom profile to destroy.
  ------------------- -------------------------------------------------

## Example request using [Twurl](https://github.com/twitter/twurl) [¶](#example-request-using-twurl){.headerlink}

    twurl -X DELETE /1.1/custom_profiles/destroy.json?id=100001

## Example Response [¶](#example-response){.headerlink}

Calling this multiple times on a valid id will return a 204 response
code.

    HTTP 204 with empty body
:::
:::
:::
:::
:::
:::
:::
