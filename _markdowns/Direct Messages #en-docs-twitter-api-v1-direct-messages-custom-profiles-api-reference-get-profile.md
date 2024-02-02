::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
Returns a custom profile that was created with [POST
custom_profiles/new.json](/en/docs/direct-messages/custom-profiles/api-reference/new-profile)
.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/custom_profiles/:id.json `

  --------------------------------------- -------------------------
  Response formats                        JSON
  Requires authentication?                Yes (user context only)
  Rate limited?                           Yes
  Requests / 24 hour window (user auth)   Yes (180 / 15 min)
  --------------------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

  ------------------- ----------------------------------------------------------------------------------------
  **id** (required)   The string ID of the custom profile that should be returned. Provided in resource URL.
  ------------------- ----------------------------------------------------------------------------------------

## Example request using [Twurl](https://github.com/twitter/twurl) [¶](#example-request-using-twurl){.headerlink}

    twurl -X GET /1.1/custom_profiles/100001

## Example Response [¶](#example-response){.headerlink}

    {
      "custom_profile": {
        "id": "100001",
        "created_timestamp": "1479767168196",
        "name": "Jon C, Partner Engineer",
        "avatar": {
            "media": {
               "url": "https://pbs.twimg.com/media/Cr7HZpvVYAAYZIX.jpg"
           }
        }
    }
:::
:::
:::
:::
:::
:::
:::
