::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
Returns a list of Welcome Message Rules.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/direct_messages/welcome_messages/rules/list.json `

  -------------------------------------- -------------------------
  Response formats                       JSON
  Requires authentication?               Yes (user context only)
  Rate limited?                          Yes
  Requests / 15-min window (user auth)   15
  -------------------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

  ----------------------- ---------------------------------------------------------------------------------------------------------------
  **count** (optional)    Number of welcome message rules to be returned. Max of 50. Default is 20.
  **cursor** (optional)   For paging through result sets greater than 1 page, use the "next_cursor" property from the previous request.
  ----------------------- ---------------------------------------------------------------------------------------------------------------

## Example request using [Twurl](https://github.com/twitter/twurl) [¶](#example-request-using-twurl){.headerlink}

    twurl -X GET "/1.1/direct_messages/welcome_messages/rules/list.json?count=2&cursor=MTIzNDU2Nzg"

## Example Responses [¶](#example-responses){.headerlink}

Welcome message rules are returned in the ` welcome_message_rules `
array. A ` next_cursor ` property will be returned if there are more
welcome message rules to be retrieved.

> **Note**
>
> To determine if there are more welcome message rules to retrieve,
> always look for the presence of a ` next_cursor ` . In rare cases the
> ` welcome_message_rules ` array may be empty.

    {
      "welcome_message_rules": [
        {
          "id": "9910934913490319",
          "created_timestamp": "1470182394258",
          "welcome_message_id": "844385345234"
        },
        {
          "id": "9910934913490431",
          "created_timestamp": "1470182394265",
          "welcome_message_id": "844385345238"
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
