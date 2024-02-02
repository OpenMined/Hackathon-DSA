::: {._4-u3 ._588p}
**` GET /{ig-user-id}?fields=mentioned_comment.comment_id `**

Returns data on an [IG
Comment](/docs/instagram-api/reference/ig-comment) in which an [IG
User](/docs/instagram-api/reference/ig-user) has been \@mentioned by
another Instagram user.

### Limitations

This endpoint will return an error if comments have been disabled on the
[IG Media](/docs/instagram-api/reference/ig-media) on which the [IG
User](/docs/instagram-api/reference/ig-user) has been \@mentioned.

### Requirements

### Request Syntax

``` {._5s-8 .prettyprint .lang-http}
GET https://graph.facebook.com/v18.0/{ig-user-id}
  ?fields=mentioned_comment.comment_id({comment-id}){{fields}}
  &access_token={access-token}
```

### Query String Parameters

::: _57-c
Parameter
:::
:::

Value

` {access_token} `\
**Required**\
*String*

The app user\'s User Access Token.

` {comment-id} `\
**Required**\
*String*

The ID of the IG Comment in which the IG User has been \@mentioned. The
ID is included in the [Webhook
notification](/docs/instagram-api/guides/webhooks#reply-comment-mention)
payload.

` {fields} `\
*Comma-separated list*

A comma-separated list of IG Comment [Fields](#fields) you want
returned. If omitted, default fields will be returned.

### Fields

::: _57-c
Field
:::

Description

` id `\
**Default**\
*String*

ID of the IG Comment.

` like_count `\
*String*

Number of times the IG Comment has been liked.

` media `\
*String*

ID of the IG Media on which the IG Comment was made. Use [Field
Expansion](#field-expansion) to get additional fields on the returned IG
Media entity.

` text `\
**Default**\
*String*

Text of the IG Comment.

` timestamp `\
**Default**\
*String*

IG Comment creation date formatted in ISO 8601.

### Response

### Sample Request

``` {._5s-8 .prettyprint .lang-curl}
curl -X GET \ 'https://graph.facebook.com/v18.0/17841405309211844?fields=mentioned_comment.comment_id(17873440459141021){timestamp,like_count,text,id}&access_token=IGQVJ...'
```

#### Sample Response

``` {._5s-8 .prettyprint .lang-json}
{
  "mentioned_comment": {
    "timestamp": "2017-05-03T16:09:08+0000",
    "like_count": 185,
    "text": "Shout out to @metricsaurus",
    "id": "17873440459141021"
  },
  "id": "17841405309211844"
}
```

### Field Expansion

You can expand the ` media ` field with a list of [IG
Media](/docs/instagram-api/reference/ig-media) fields to get additional
data on the IG Media entity on which the comment was made. For example:

``` {._5s-8 .prettyprint .lang-http}
media{id,media_url}
```

::: {._57yz ._57z1 ._3-8p}
::: _57y-
<div>

**v10.0 and older calls until September 7, 2021:** The
[` like_count `](/docs/instagram-api/reference/ig-media#fields) field on
an IG Media will return ` 0 ` if the media
[owner](/docs/instagram-api/overview#authorization) has
[hidden](https://www.facebook.com/help/instagram/113355287252104) like
counts on it.

**v11.0+ calls, and all versions on September 7, 2021:** If indirectly
querying an [IG Media](/docs/instagram-api/reference/ig-media) through
another endpoint or field expansion, the
[` like_count `](/docs/instagram-api/reference/ig-media#fields) field
will be omitted from API responses if the media owner has hidden like
counts on it. Directly querying the IG Media (which can only be done by
the IG Media owner) will return the actual like count, however, even if
like counts have been hidden.

</div>
:::
:::

#### Sample Field Expansion Request

``` {._5s-8 .prettyprint .lang-curl}
curl -X GET \ 'https://graph.facebook.com/v18.0/17841405309211844?fields=mentioned_comment.comment_id(17873440459141021){timestamp,like_count,text,media{id,media_url}}&access_token=IGQVJ...'
```

#### Sample Field Expansion Response

``` {._5s-8 .prettyprint .lang-json}
{
  "mentioned_comment": {
    "timestamp": "2017-05-03T16:09:08+0000",
    "like_count": 185,
    "text": "Shout out to @metricsaurus",
    "id": "17873440459141021",
    "media": {
      "id": "17895695668004550",
      "media_url": "https://scont..."
    }
  },
  "id": "17841405309211844"
}
```

### Pagination

If you are using field expansion to access an edge that supports
[cursor-based pagination](/docs/graph-api/using-graph-api#paging) , the
response will include ` before ` and ` after ` cursors if the response
contains multiple pages of data. Unlike standard cursor-based
pagination, however, the response will not include ` previous ` or
` next ` fields, so you will have to use the ` before ` and ` after `
cursors to construct ` previous ` and ` next ` query strings manually in
order to page through the returned data set.
