::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
Updates a Welcome Message by the given ID. Updates to the
` welcome_message ` object are atomic. For example, if the Welcome
Message currently has ` quick_reply ` defined and you only provde
` text ` , the ` quick_reply ` object will be removed from the Welcome
Message.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/direct_messages/welcome_messages/update.json `

  -------------------------- -------------------------
  Response formats           JSON
  Requires authentication?   Yes (user context only)
  Rate limited?              Yes
  -------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

  ------------------- -------------------------------------------------------
  **id** (required)   The id of the Welcome Message that should be updated.
  ------------------- -------------------------------------------------------

## Example request using [Twurl](https://github.com/twitter/twurl) [¶](#example-request-using-twurl){.headerlink}

    twurl -A 'Content-type: application/json' -X PUT '/1.1/direct_messages/welcome_messages/update.json?id=4893198399134' -d ‘
    {
      "message_data":{
        "text": "Welcome!"
      }
    }

## Example Response [¶](#example-response){.headerlink}

    {
      "name": "Generic Welcome 01"
      "welcome_message": {
        "id": "4893198399134",
        "created_timestamp": "154903045",
        "message_data": {
          "text": "Welcome!"
        }
      },
      "apps": {
        "8829219": {
          "id": "8829219",
          "name": "Furni",
          "url": "https://developer.twitter.com"
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
