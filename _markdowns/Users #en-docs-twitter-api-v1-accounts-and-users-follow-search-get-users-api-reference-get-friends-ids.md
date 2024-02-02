<div>

::: c01-rich-text-editor
Returns a cursored collection of user IDs for every user the specified
user is following (otherwise known as their \"friends\").

At this time, results are ordered with the most recent following first
--- however, this ordering is subject to unannounced change and eventual
consistency issues. Results are given in groups of 5,000 user IDs and
multiple \"pages\" of results can be navigated through using the
` next_cursor ` value in subsequent requests. See [Using cursors to
navigate collections](/en/docs/basics/cursoring) for more information.

This method is especially powerful when used in conjunction with [GET
users /
lookup](/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-lookup)
, a method that allows you to convert user IDs into full [user
objects](/en/docs/tweets/data-dictionary/overview/user-object) in bulk.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/friends/ids.json `

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
| count       | optional    | Specifies   |             | ` 2048 `    |
|             |             | the number  |             |             |
|             |             | of IDs      |             |             |
|             |             | attempt     |             |             |
|             |             | retrieval   |             |             |
|             |             | of, up to a |             |             |
|             |             | maximum of  |             |             |
|             |             | 5,000 per   |             |             |
|             |             | distinct    |             |             |
|             |             | request.    |             |             |
|             |             | The value   |             |             |
|             |             | of          |             |             |
|             |             | ` count `   |             |             |
|             |             | is best     |             |             |
|             |             | thought of  |             |             |
|             |             | as a limit  |             |             |
|             |             | to the      |             |             |
|             |             | number of   |             |             |
|             |             | results to  |             |             |
|             |             | return.     |             |             |
|             |             | When using  |             |             |
|             |             | the count   |             |             |
|             |             | parameter   |             |             |
|             |             | with this   |             |             |
|             |             | method, it  |             |             |
|             |             | is wise to  |             |             |
|             |             | use a       |             |             |
|             |             | consistent  |             |             |
|             |             | count value |             |             |
|             |             | across all  |             |             |
|             |             | requests to |             |             |
|             |             | the same    |             |             |
|             |             | user\'s     |             |             |
|             |             | collection. |             |             |
|             |             | Usage of    |             |             |
|             |             | this        |             |             |
|             |             | parameter   |             |             |
|             |             | is          |             |             |
|             |             | encouraged  |             |             |
|             |             | in          |             |             |
|             |             | e           |             |             |
|             |             | nvironments |             |             |
|             |             | where all   |             |             |
|             |             | 5,000 IDs   |             |             |
|             |             | constitutes |             |             |
|             |             | too large   |             |             |
|             |             | of a        |             |             |
|             |             | response.   |             |             |
+-------------+-------------+-------------+-------------+-------------+

## Example Request [¶](#example-request){.headerlink}

    $ curl --request GET 
      --url 'https://api.twitter.com/1.1/friends/ids.json?screen_name=twitterdev' 
      --header 'authorization: Bearer <bearer>'

    $ curl --request GET 
      --url 'https://api.twitter.com/1.1/friends/ids.json?screen_name=twitterdev' 
      --header 'authorization: OAuth oauth_consumer_key="consumer-key-for-app", 
      oauth_nonce="generated-nonce", oauth_signature="generated-signature", 
      oauth_signature_method="HMAC-SHA1", oauth_timestamp="generated-timestamp", 
      oauth_version="1.0"'

    $ twurl /1.1/friends/ids.json?screen_name=twitterdev

## Example Response [¶](#example-response){.headerlink}

    {
      "previous_cursor": 0,
      "ids": [
        657693,
        183709371,
        7588892,
        38895958,
        22891211,
        9019482,
        14488353,
        11750202,
        12249,
        22915745,
        1249881,
        14927800,
        1523501,
        22548447,
        15062340,
        133031077,
        17874544,
        777925,
        4265731,
        27674040,
        26123649,
        9576402,
        821958,
        7852612,
        819797,
        1401881,
        8285392,
        9160152,
        795649,
        3191321,
        783214
      ],
      "previous_cursor_str": "0",
      "next_cursor": 0,
      "next_cursor_str": "0"
    }
:::

</div>
