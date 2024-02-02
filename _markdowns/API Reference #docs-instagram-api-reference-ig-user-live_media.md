::: {._4-u3 ._588p}
**` GET /{ig-user-id}/live_media `**

Get a collection of live video [IG
Media](/docs/instagram-api/reference/ig-media) on an [IG
User](/docs/instagram-api/reference/ig-user) .

### Limitations

Only live video IG Media being broadcast at the time of the request will
be returned.

### Time-based Pagination

This endpoint supports [time-based
pagination](/docs/graph-api/using-graph-api#time) . Include ` since `
and ` until ` query-string paramaters with Unix timestamp or
` strtotime ` data values to define a time range.

### Requirements

### Request Syntax

``` {._5s-8 .prettyprint .lang-code}
GET https://graph.facebook.com/{api-version}/{ig-user-id}/live_media
  ?access_token={access-token}
```

### Path Parameters

::: _57-c
Placeholder
:::
:::

Value

` {api-version} `\
*String*

API [version](/docs/instagram-basic-display-api/overview#versions) .

` {ig-user-id} `\
**Required**\
*String*

App user\'s app-scoped user ID.

### Query String Parameters

::: _57-c
Key
:::

Value

` access_token `\
**Required**\
*String*

App user\'s [User](/docs/facebook-login/access-tokens/#usertokens)
access token.

` fields `\
*Comma-separated list*

Comma-separated list of IG Media
[fields](/docs/instagram-api/reference/ig-media#fields) you want
returned for each live IG Media in the result set.

` since `\
*timestamp*

A Unix timestamp or ` strtotime ` data value that points to the start of
a range of time-based data. See [time-based
pagination](/docs/graph-api/using-graph-api#time) .

` until `\
*timestamp*

A Unix timestamp or ` strtotime ` data value that points to the end of a
range of time-based data. See [time-based
pagination](/docs/graph-api/using-graph-api#time) .

### Response

A JSON-formatted object containing the data you requested.

``` {._5s-8 .prettyprint .lang-json}
{
  "data": [],
  "paging": {}
}
```

#### Response Contents

::: _57-c
Property
:::

Value

` data `

An array of [IG Media](/docs/instagram-api/reference/ig-media) on an [IG
User](/docs/instagram-api/reference/ig-user) .

` paging `

An object containing [paging](/docs/graph-api/using-graph-api#paging)
cursors and next/previous data set retrievial URLs.

### cURL Example

#### Request

``` {._5s-8 .prettyprint .lang-curl}
curl -X GET \ 'https://graph.facebook.com/v18.0/17841405822304914/live_media?fields=id,media_type,media_product_type,owner,username,comments&access_token=IGQVJ...'
```

#### Response

``` {._5s-8 .prettyprint .lang-json}
{
   "id":"90010498116233",
   "media_type":"BROADCAST",
   "media_product_type":"LIVE",
   "owner":{
      "id":"17841405822304914"
   },
   "username":"jayposiris",
   "comments":{
      "data":[
        {
            "hidden": false,
            "id": "17907364514064687",
            "like_count": 0,
            "media": {
                "id": "17892642502701087"
            },
            "text": "@jayposiris",
            "timestamp": "2021-08-17T21:23:07+0000",
            "username": "bztest0316_11",
            "from": {
                "id": "5895605157123796",
                "username": "bztest0316_11"
            }
        }
      ]
   }
}
```
