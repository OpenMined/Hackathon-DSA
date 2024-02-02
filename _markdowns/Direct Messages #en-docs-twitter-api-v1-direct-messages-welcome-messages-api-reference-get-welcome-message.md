::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
Returns a Welcome Message by the given id.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/direct_messages/welcome_messages/show.json `

  -------------------------------------- -------------------------
  Response formats                       JSON
  Requires authentication?               Yes (user context only)
  Rate limited?                          Yes
  Requests / 15-min window (user auth)   15
  -------------------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

  ------------------- --------------------------------------------------------
  **id** (required)   The id of the Welcome Message that should be returned.
  ------------------- --------------------------------------------------------

## Example request using [Twurl](https://github.com/twitter/twurl) [¶](#example-request-using-twurl){.headerlink}

    twurl -X GET /1.1/direct_messages/welcome_messages/show.json?id=844385345234

## Example Response [¶](#example-response){.headerlink}

    {
      "welcome_message" : {
        "id": "844385345234",
        "created_timestamp": "1470182274821",
        "message_data": {
          "text": "Welcome!",
          "attachment": {
            "type": "media",
            "media": {
              ...
            }
          }
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
