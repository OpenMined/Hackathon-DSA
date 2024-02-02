::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
Returns a collection of numeric IDs for every user who has a pending
request to follow the authenticating user.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/friendships/incoming.json `

  -------------------------------------- -------------------------
  Response formats                       JSON
  Requires authentication?               Yes (user context only)
  Rate limited?                          Yes
  Requests / 15-min window (user auth)   15
  -------------------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

+-------------+-------------+-------------+-------------+-------------+
| cursor      | se          | Causes the  |             | ` 12893     |
|             | mi-optional | list of     |             | 764510938 ` |
|             |             | connections |             |             |
|             |             | to be       |             |             |
|             |             | broken into |             |             |
|             |             | pages of no |             |             |
|             |             | more than   |             |             |
|             |             | 5000 IDs at |             |             |
|             |             | a time. The |             |             |
|             |             | number of   |             |             |
|             |             | IDs         |             |             |
|             |             | returned is |             |             |
|             |             | not         |             |             |
|             |             | guaranteed  |             |             |
|             |             | to be 5000  |             |             |
|             |             | as          |             |             |
|             |             | suspended   |             |             |
|             |             | users are   |             |             |
|             |             | filtered    |             |             |
|             |             | out after   |             |             |
|             |             | connections |             |             |
|             |             | are         |             |             |
|             |             | queried. If |             |             |
|             |             | no cursor   |             |             |
|             |             | is          |             |             |
|             |             | provided, a |             |             |
|             |             | value of    |             |             |
|             |             | ` -1 ` will |             |             |
|             |             | be assumed, |             |             |
|             |             | which is    |             |             |
|             |             | the first   |             |             |
|             |             | \"page.\"   |             |             |
|             |             |             |             |             |
|             |             | The         |             |             |
|             |             | response    |             |             |
|             |             | from the    |             |             |
|             |             | API will    |             |             |
|             |             | include a   |             |             |
|             |             | ` previo    |             |             |
|             |             | us_cursor ` |             |             |
|             |             | and         |             |             |
|             |             | ` ne        |             |             |
|             |             | xt_cursor ` |             |             |
|             |             | to allow    |             |             |
|             |             | paging back |             |             |
|             |             | and forth.  |             |             |
+-------------+-------------+-------------+-------------+-------------+
| st          | optional    | Many        |             | ` true `    |
| ringify_ids |             | programming |             |             |
|             |             | e           |             |             |
|             |             | nvironments |             |             |
|             |             | will not    |             |             |
|             |             | consume our |             |             |
|             |             | Tweet ids   |             |             |
|             |             | due to      |             |             |
|             |             | their size. |             |             |
|             |             | Provide     |             |             |
|             |             | this option |             |             |
|             |             | to have ids |             |             |
|             |             | returned as |             |             |
|             |             | strings     |             |             |
|             |             | instead.    |             |             |
+-------------+-------------+-------------+-------------+-------------+

## Example Request [¶](#example-request){.headerlink}

` GET https://api.twitter.com/1.1/friendships/incoming.json `

## Example Response [¶](#example-response){.headerlink}

    {
      "previous_cursor": 0,
      "ids": [6253282],
      "previous_cursor_str": "0",
      "next_cursor": 0,
      "next_cursor_str": "0"
    }
:::
:::
:::
:::
:::
:::
:::
