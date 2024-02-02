::: {._4-u3 ._588p}
**` GET /{ig-user-id}/tags `**

Returns a list of [IG Media](/docs/instagram-api/reference/ig-media)
objects in which an [IG User](/docs/instagram-api/reference/ig-user) has
been tagged by another Instagram user.

### Limitations

Private [IG Media](/docs/instagram-api/reference/ig-media) objects will
not be returned.

### Requirements

### Request Syntax

``` {._5s-8 .prettyprint .lang-code}
GET https://graph.facebook.com/{ig-user-id}/tags
  ?fields={fields}
  &access_token={access-token}
```

### Query String Parameters

Include the following query string parameters to augment the request.

::: _57-c
Key
:::
:::

Value

` access_token `\
**Required**\
*String*

The app user\'s [Instagram User Access
Token](/docs/instagram-basic-display-api/overview#instagram-user-access-tokens)
.

` fields `\
*Comma-separated list*

A comma-separated list of [Fields](#fields) and [Edges](#edges) you want
included in the response. If omitted, default fields will be returned.

### Fields

Use the ` fields ` query string parameter to specify fields you want
included on any returned [IG
Media](/docs/instagram-api/reference/ig-media#read) objects.

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

### Edges

Use the ` fields ` query string parameter to specify Edges you want
included on any returned [IG
Media](/docs/instagram-api/reference/ig-media#read) objects.

### Response

A JSON-formatted object containing [IG
Media](/docs/instagram-api/reference/ig-media) objects.

``` {._5s-8 .prettyprint .lang-json}
{
  "{field}":"{value}",
  ...
}
```

### Pagination

This edge supports [cursor-based
pagination](/docs/graph-api/using-graph-api#paging) so the response will
include ` before ` and ` after ` cursors if the response contains
multiple pages of data. Unlike standard cursor-based pagination,
however, the response will not include ` previous ` or ` next ` fields,
so you will have to use the ` before ` and ` after ` cursors to
construct ` previous ` and ` next ` query strings manually in order to
page through the returned data set.

### Sample Request

``` {._5s-8 .prettyprint .lang-code}
GET graph.facebook.com/17841405822304914/tags
    ?fields=id,username
    &access_token=EAADd...
```

### Sample Response

``` {._5s-8 .prettyprint .lang-code}
{
  "data": [
    {
      "id": "18038...",
      "username": "keldo..."
    },
    {
      "id": "17930...",
      "username": "ashla..."
    },
    {
      "id": "17931...",
      "username": "jaypo..."
    }
  ]
}
```
