::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
Returns a single Direct Message event by the given id.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/direct_messages/events/show.json `

  -------------------------------------- -------------------------
  Response formats                       JSON
  Requires authentication?               Yes (user context only)
  Rate limited?                          Yes
  Requests / 15-min window (user auth)   15
  -------------------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

  ------------------- -------------------------------------------------------------
  **id** (required)   The id of the Direct Message event that should be returned.
  ------------------- -------------------------------------------------------------

## Example request using [Twurl](https://github.com/twitter/twurl) [¶](#example-request-using-twurl){.headerlink}

    twurl -X GET /1.1/direct_messages/events/show.json?id=110

## Example Response [¶](#example-response){.headerlink}

    {
      "event": 
        "id": "110", 
        "created_timestamp": "5300",
        "type": "message_create",
        "message_create": {
          ...
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
