::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
Returns an array of numeric user ids the authenticating user has muted.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/mutes/users/ids.json `

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
| cursor      | optional    | Causes the  | ` -1 `      | ` 2 `       |
|             |             | list of IDs |             |             |
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
|             |             | out. If no  |             |             |
|             |             | cursor is   |             |             |
|             |             | provided, a |             |             |
|             |             | value of -1 |             |             |
|             |             | will be     |             |             |
|             |             | assumed,    |             |             |
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

` GET https://api.twitter.com/1.1/mutes/users/ids.json?cursor=-1 `

## Example Response [¶](#example-response){.headerlink}

    {
      "ids": [
        1228026486,
        54931584
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
