::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
Returns a cursored collection of user objects for every user the
specified user is following (otherwise known as their \"friends\").

At this time, results are ordered with the most recent following first
--- however, this ordering is subject to unannounced change and eventual
consistency issues. Results are given in groups of 20 users and multiple
\"pages\" of results can be navigated through using the ` next_cursor `
value in subsequent requests. See [Using cursors to navigate
collections](/en/docs/basics/cursoring) for more information.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/friends/list.json `

  -------------------------------------- ------
  Response formats                       JSON
  Requires authentication?               Yes
  Rate limited?                          Yes
  Requests / 15-min window (user auth)   15
  Requests / 15-min window (app auth)    15
  -------------------------------------- ------

## Parameters [¶](#parameters){.headerlink}

+-------------+-------------+-------------+-------------+-------------+
| user_id     | optional    | The ID of   |             | ` 12345 `   |
|             |             | the user    |             |             |
|             |             | for whom to |             |             |
|             |             | return      |             |             |
|             |             | results.    |             |             |
+-------------+-------------+-------------+-------------+-------------+
| screen_name | optional    | The screen  |             | ` noradio ` |
|             |             | name of the |             |             |
|             |             | user for    |             |             |
|             |             | whom to     |             |             |
|             |             | return      |             |             |
|             |             | results.    |             |             |
+-------------+-------------+-------------+-------------+-------------+
| cursor      | se          | Causes the  | ` -1 `      | ` 12893     |
|             | mi-optional | results to  |             | 764510938 ` |
|             |             | be broken   |             |             |
|             |             | into pages. |             |             |
|             |             | If no       |             |             |
|             |             | cursor is   |             |             |
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
| count       | optional    | The number  | ` 20 `      | ` 42 `      |
|             |             | of users to |             |             |
|             |             | return per  |             |             |
|             |             | page, up to |             |             |
|             |             | a maximum   |             |             |
|             |             | of 200.     |             |             |
+-------------+-------------+-------------+-------------+-------------+
| skip_status | optional    | When set to | ` false `   | ` false `   |
|             |             | either      |             |             |
|             |             | ` true ` ,  |             |             |
|             |             | ` t ` or    |             |             |
|             |             | ` 1 `       |             |             |
|             |             | statuses    |             |             |
|             |             | will not be |             |             |
|             |             | included in |             |             |
|             |             | the         |             |             |
|             |             | returned    |             |             |
|             |             | user        |             |             |
|             |             | objects.    |             |             |
+-------------+-------------+-------------+-------------+-------------+
| include_us  | optional    | The user    | ` true `    | ` false `   |
| er_entities |             | object      |             |             |
|             |             | `           |             |             |
|             |             |  entities ` |             |             |
|             |             | node will   |             |             |
|             |             | not be      |             |             |
|             |             | included    |             |             |
|             |             | when set to |             |             |
|             |             | ` false ` . |             |             |
+-------------+-------------+-------------+-------------+-------------+

## Example Request [¶](#example-request){.headerlink}

` GET https://api.twitter.com/1.1/friends/list.json?cursor=-1&screen_name=twitterapi&skip_status=true&include_user_entities=false `

## Example Response [¶](#example-response){.headerlink}

    {
    "users": [
          {user-object},
          {user-object},
          {user-object}
      ],
      "previous_cursor": 0,
      "previous_cursor_str": "0",
      "next_cursor": 1333504313713126852,
      "next_cursor_str": "1333504313713126852"
    }

For more detail, see the [user-object
definition](/en/docs/tweets/data-dictionary/overview/user-object) .
:::
:::
:::
:::
:::
:::
:::
