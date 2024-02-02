::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
Retrieves all custom profiles for the authenticated account. Default
page size is 20.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/custom_profiles/list.json `

  --------------------------------------- -------------------------
  Response formats                        JSON
  Requires authentication?                Yes (user context only)
  Rate limited?                           Yes
  Requests / 24 hour window (user auth)   Yes (180 / 15 min)
  --------------------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

  ----------------------- --------------------------------------------------------------------------------------------------------------------------
  **count** (optional)    Number of custom profile objects to be returned. Max of 50. Default is 20.
  **cursor** (optional)   For paging through result sets greater than 1 page. Use the ` next_cursor ` property returned from the previous request.
  ----------------------- --------------------------------------------------------------------------------------------------------------------------

*Note:* In rare cases a response may contain an empty custom profile
object with ` next_cursor ` defined. The presence of a ` next_cursor `
property in the response indicates there are more custom profiles to
retrieve.

## Example request using [Twurl](https://github.com/twitter/twurl) [¶](#example-request-using-twurl){.headerlink}

    twurl -X GET /1.1/custom_profiles/list.json?count=2&cursor=MTIzNDU2Nzg

## Example Response [¶](#example-response){.headerlink}

    {
      "custom_profiles": [
        {
          "id": "100001",
          "created_timestamp": "1479767168196",
          "name": "Carol",
          "avatar": {
            "media": {
              "url": "https://pbs.twimg.com/some_img/987654321/ABC?format=jpg&name=normal"
            }
          }
        },
        {
          "id": "100002",
          "created_timestamp": "1479767168197",
          "name": "Andy",
          "avatar": {
            "media": {
              "url": "https://pbs.twimg.com/some_img/56565656/DEF?format=jpg&name=normal"
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
