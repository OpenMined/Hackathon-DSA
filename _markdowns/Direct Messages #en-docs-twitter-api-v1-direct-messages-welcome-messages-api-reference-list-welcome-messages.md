::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
Returns a list of Welcome Messages.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/direct_messages/welcome_messages/list.json `

  -------------------------------------- -------------------------
  Response formats                       JSON
  Requires authentication?               Yes (user context only)
  Rate limited?                          Yes
  Requests / 15-min window (user auth)   15
  -------------------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

  ----------------------- ---------------------------------------------------------------------------------------------------------------
  **count** (optional)    Number of welcome messages to be returned. Max of 50. Default is 20.
  **cursor** (optional)   For paging through result sets greater than 1 page, use the "next_cursor" property from the previous request.
  ----------------------- ---------------------------------------------------------------------------------------------------------------

## Example request using [Twurl](https://github.com/twitter/twurl) [¶](#example-request-using-twurl){.headerlink}

    twurl -X GET "/1.1/direct_messages/welcome_messages/list.json?count=2&cursor=MTIzNDU2Nzg"

## Example Response [¶](#example-response){.headerlink}

Welcome Messages are returned in the ` welcome_messages ` array. A
` next_cursor ` property will be returned if there are more welcome
messages to be retrieved.

> **Note**
>
> To determine if there are more welcome messages to retrieve, always
> look for the presence of a ` next_cursor ` . In rare cases the
> ` welcome_messages ` array may be empty.

    {
      "welcome_messages": [
        {
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
        },
        {
          "id": "844385345238",
          "created_timestamp": "1470182275399",
          "message_data": {
            "text": "Welcome Again!",
            "attachment": {
              "type": "media",
              "media": {
                ...
              }
            }
          }
        }
      ],
      "next_cursor": "NDUzNDUzNDY3Nzc3"
    }
:::
:::
:::
:::
:::
:::
:::
