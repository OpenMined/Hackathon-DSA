::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
Creates a new custom profile. The returned ID should be used with when
publishing a new message with [POST
direct_messages/events/new](/en/docs/direct-messages/sending-and-receiving/api-reference/new-event)
.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/custom_profiles/new.json `

  --------------------------------------- -------------------------
  Response formats                        JSON
  Requires authentication?                Yes (user context only)
  Rate limited?                           Yes
  Requests / 24 hour window (user auth)   Yes (1000 / 1 day)
  --------------------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

  -------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **name** (required)              The string ID of of the custom profile. 48 characters max length.
  **avatar.media.id** (required)   The string ID of the media to associate with the profile. See [Uploading Media](/en/docs/media/upload-media/overview) for further details on generating a media ID.
  -------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Example Request [¶](#example-request){.headerlink}

    {
      "custom_profile": {
        "name": "Jon C, Partner Engineer",
        "avatar": {
            "media": {
               "id": "1234"
           }
        }
    }

### Example request using [Twurl](https://github.com/twitter/twurl) [¶](#example-request-using-twurl){.headerlink}

    twurl -A 'Content-type: application/json' /1.1/custom_profiles/new.json -d ' { "custom_profile": { "name": "Jon C, Partner Engineer", "avatar": { "media": { "id": "1234" } } }'

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
