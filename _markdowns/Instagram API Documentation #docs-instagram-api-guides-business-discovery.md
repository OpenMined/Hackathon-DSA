::: {._4-u3 ._588p}
This sample query shows how to get the number of followers and number of
published media objects on the [Blue Bottle
Coffee](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.instagram.com%2Fbluebottle%2F&h=AT2jbnIX5izMz6Ye8R5ytg6noryJYvWvV7-XQoxcgEfDHPbwFONod2hJNKUQPHwlhr5KDjLM-zMro_bPxC_RB_D-8piBYkwm30isnP2S8ZSEqo6qj8hpbuwXlTC2pWtaP3v4K8Mc0SaMl1v_3ct6Dw)
Instagram Business Account. Notice that business discovery queries are
performed on the Instagram Business or Creator Account\'s ID (in this
case, ` 17841405309211844 ` ), not the username of the Instagram
Business or Creator Account that you are attempting to get data about (
` bluebottle ` in this example).

#### Sample Request

``` {._5s-8 .prettyprint .lang-curl .prettyprinted}
curl -i -X GET \ "https://graph.facebook.com/v3.2/17841405309211844?fields=business_discovery.username(bluebottle){followers_count,media_count}&access_token={access-token}"
```

#### Sample Response

``` {._5s-8 .prettyprint .lang-json .prettyprinted}
{ "business_discovery": { "followers_count": 267793, "media_count": 1205, "id": "17841401441775531" // Blue Bottle's Instagram Account ID }, "id": "17841405309211844" // ID of the Instagram account performing the query
}
```

Since you can make nested requests by specifying an edge via the
` fields ` parameter, you can request the targeted Business or Creator
Account\'s ` media ` edge to get all of its published media objects:

#### Sample Request

``` {._5s-8 .prettyprint .lang-curl .prettyprinted}
curl -i -X GET \ "https://graph.facebook.com/v3.2/17841405309211844?fields=business_discovery.username(bluebottle){followers_count,media_count,media}&access_token={access-token}"
```

#### Sample Response

``` {._5s-8 .prettyprint .lang-json .prettyprinted}
{ "business_discovery": { "followers_count": 267793, "media_count": 1205, "media": { "data": [ { "id": "17858843269216389" }, { "id": "17894036119131554" }, { "id": "17894449363137701" }, { "id": "17844278716241265" }, ... // results truncated for brevity ], "id": "17841401441775531" }, }, "id": "17841405309211844"
}
```

You can use both nested requests and field expansion to get public
fields for a Business or Creator Account\'s media objects. Note that
this does not grant you permission to access media objects directly ---
performing a ` GET ` on any returned [IG
Media](/docs/instagram-api/reference/ig-media) will fail due to
insufficient permissions.

For example, here\'s how to get the number of comments and likes for
each of the media objects published by Blue Bottle Coffee:

#### Sample Request

``` {._5s-8 .prettyprint .lang-curl .prettyprinted}
curl -i -X GET \ "https://graph.facebook.com/v3.2/17841405309211844?fields=business_discovery.username(bluebottle){followers_count,media_count,media{comments_count,like_count}}&access_token={access-token}"
```

#### Sample Response

``` {._5s-8 .prettyprint .lang-code .prettyprinted}
{ "business_discovery": { "followers_count": 267793, "media_count": 1205, "media": { "data": [ { "comments_count": 50, "like_count": 5841, "id": "17858843269216389" }, { "comments_count": 11, "like_count": 2998, "id": "17894036119131554" }, { "comments_count": 28, "like_count": 3644, "id": "17894449363137701" }, { "comments_count": 43, "like_count": 4943, "id": "17844278716241265" }, { "comments_count": 60, "like_count": 9347, "id": "17899363132086521" }, { "comments_count": 63, "like_count": 6913, "id": "17893114378137541" }, { "comments_count": 16, "like_count": 2791, "id": "17886057709171561" }, { "comments_count": 15, "like_count": 3895, "id": "17856337633208377" }, ], }, "id": "17841401441775531" }, "id": "17841405976406927"
}
```
:::
