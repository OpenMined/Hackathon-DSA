::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
Returns an array of numeric user ids the authenticating user is
blocking.

**Important** This method is cursored, meaning your app must make
multiple requests in order to receive all blocks correctly. See [Using
cursors to navigate collections](/en/docs/basics/cursoring) for more
details on how cursoring works.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/blocks/ids.json `

  -------------------------------------- -------------------------
  Response formats                       JSON
  Requires authentication?               Yes (user context only)
  Rate limited?                          Yes
  Requests / 15-min window (user auth)   15
  -------------------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

+-------------+-------------+-------------+-------------+-------------+
| st          | optional    | Many        |             | ` true `    |
| ringify_ids |             | programming |             |             |
|             |             | e           |             |             |
|             |             | nvironments |             |             |
|             |             | will not    |             |             |
|             |             | consume     |             |             |
|             |             | Twitter IDs |             |             |
|             |             | due to      |             |             |
|             |             | their size. |             |             |
|             |             | Provide     |             |             |
|             |             | this option |             |             |
|             |             | to have IDs |             |             |
|             |             | returned as |             |             |
|             |             | strings     |             |             |
|             |             | instead.    |             |             |
|             |             | Read more   |             |             |
|             |             | about       |             |             |
|             |             | [Twitter    |             |             |
|             |             | IDs](/en/do |             |             |
|             |             | cs/basics/t |             |             |
|             |             | witter-ids) |             |             |
|             |             | .           |             |             |
+-------------+-------------+-------------+-------------+-------------+
| cursor      | se          | Causes the  | ` -1 `      | ` 12893     |
|             | mi-optional | list of IDs |             | 764510938 ` |
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
|             |             | See [Using  |             |             |
|             |             | cursors to  |             |             |
|             |             | navigate    |             |             |
|             |             | collec      |             |             |
|             |             | tions](/en/ |             |             |
|             |             | docs/basics |             |             |
|             |             | /cursoring) |             |             |
|             |             | for more    |             |             |
|             |             | i           |             |             |
|             |             | nformation. |             |             |
+-------------+-------------+-------------+-------------+-------------+

## Example Request [¶](#example-request){.headerlink}

` GET https://api.twitter.com/1.1/blocks/ids.json?stringify_ids=true&cursor=-1 `

## Example Response [¶](#example-response){.headerlink}

    {
      "ids": [
        "123"
      ],
      "next_cursor": 0,
      "next_cursor_str": "0",
      "previous_cursor": 0,
      "previous_cursor_str": "0"
    }
:::
:::
:::
:::
:::
:::
:::
