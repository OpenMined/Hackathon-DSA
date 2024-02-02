::: {._4-u3 ._588p}
**` GET /{ig-user-id}?fields=mentioned_media.media_id `**

Returns data on an [IG Media](/docs/instagram-api/reference/ig-media) in
which an [IG User](/docs/instagram-api/reference/ig-user) has been
\@mentioned in a caption by another Instagram user.

### Limitations

-   Mentions on Stories are not supported.
-   Commenting on photos in which you were tagged is not supported.
-   Webhooks will not be sent if the Media upon which the comment or
    \@mention appears was created by an account that is set to private.

### Requirements

### Request Syntax

``` {._5s-8 .prettyprint .lang-http}
GET https://graph.facebook.com/v18.0/{ig-user-id}
  ?fields=mentioned_media.media_id({media-id}){{fields}}
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

` {fields} `\
*Comma-separated list*

A comma-separated list of IG Media [Fields](#fields) you want returned.
If omitted, default Fields will be returned.

` {media-id} `\
**Required**\
*String*

The ID of the IG Media in which the IG User has been \@mentioned in a
caption. The ID is included in the [Webhook
notification](/docs/instagram-api/guides/webhooks#reply-comment-mention)
payload.

### Fields

::: _57-c
Field
:::

Description

` caption `\
*String*

The caption text. Captions that \@mention an IG User will not include
the ` @ ` symbol unless the app user created the IG Media object upon
which the caption was made.

` comments `\
*Object*

A list of IG Comments on the IG Media. If using Field Expansion to get
the comment text, text that \@mentions an IG User will not include the
` @ ` symbol unless the app user created the IG Media object upon which
the caption was made.

` comments_count `\
*String*

Number of IG Comments on the IG Media.

` id `\
**Default**\
*String*

ID of the IG Media.

` like_count `\
*String*

Count of likes on the media. Excludes likes on album child media and
likes on promoted posts created from the media. Includes replies on
comments.

\

-   **v10.0 and older calls:** value will be ` 0 ` if the media owner
    has
    [hidden](https://www.facebook.com/help/instagram/113355287252104)
    like counts it.
-   **v11.0+ calls:** field will be omitted if media owner has hidden
    like counts in it Value will be ` 0 ` if the media owner has
    [hidden](https://www.facebook.com/help/instagram/113355287252104)
    like counts it.

` media_type `\
*String*

The IG Media\'s type: ` CAROUSEL_ALBUM ` , ` IMAGE ` , ` STORY ` , or
` VIDEO ` .

` media_url `\
*String*

URL of the published IG Media.

` owner `\
*String*

ID of the IG User who created the IG Media. Only returned if the app
user created the IG Media object, otherwise the ` username ` field will
be returned instead.

` timestamp `\
*String*

Creation date of IG Media formatted in ISO 8601.

` username `\
*String*

Username of the IG User who created the IG Media.

### Sample Request

``` {._5s-8 .prettyprint .lang-curl}
curl -X GET \ 'https://graph.facebook.com/v18.0/17841405309211844?fields=mentioned_media.media_id(17873440459141021){caption,media_type}&access_token=IGQVJ...'
```

### Sample Response

``` {._5s-8 .prettyprint .lang-json}
{
  "mentioned_media": {
    "caption": "metricsaurus headquarters!",
    "media_type": "IMAGE",
    "id": "17873440459141021"
  },
  "id": "17841405309211844"
}
```

Note that in the sample above, the API has stripped out the leading
` @ ` symbol from the original caption (@metricsaurus headquarters!)
because the app user did not create the caption.

### Pagination

If you are using field expansion to access an edge that supports
[cursor-based pagination](/docs/graph-api/using-graph-api#paging) , the
response will include ` before ` and ` after ` cursors if the response
contains multiple pages of data. Unlike standard cursor-based
pagination, however, the response will not include ` previous ` or
` next ` fields, so you will have to use the ` before ` and ` after `
cursors to construct ` previous ` and ` next ` query strings manually in
order to page through the returned data set.
