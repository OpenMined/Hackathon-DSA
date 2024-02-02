<div>

::: c01-rich-text-editor
Returns a collection of numeric IDs for every protected user for whom
the authenticating user has a pending follow request.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/friendships/outgoing `

  -------------------------------------- -------------------------
  Response formats                       JSON
  Requires authentication?               Yes (user context only)
  Rate limited?                          Yes
  Requests / 15-min window (user auth)   15
  -------------------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

+-------------+-------------+-------------+-------------+-------------+
| cursor      | se          | Causes the  | ` -1 `      | ` 12893     |
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
| st          | optional    | Some        | ` false `   | ` true `    |
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
|             |             | More about  |             |             |
|             |             | [Twitter    |             |             |
|             |             | IDs](/en/do |             |             |
|             |             | cs/basics/t |             |             |
|             |             | witter-ids) |             |             |
|             |             | .           |             |             |
+-------------+-------------+-------------+-------------+-------------+

## Example Request [¶](#example-request){.headerlink}

` GET https://api.twitter.com/1.1/friendships/outgoing.json `

## Example Response [¶](#example-response){.headerlink}

    {
      "previous_cursor": 0,
      "ids": [
        51937528,
        124856868,
        213246307,
        89356977,
        121177351,
        113338333,
        59520091,
        46451699,
        98223312,
        18172433,
        32210115,
        36851055,
        81269257
      ],
      "previous_cursor_str": "0",
      "next_cursor": 0,
      "next_cursor_str": "0"
    }
:::

</div>
