::: {._4-u3 ._588p}
` GET /{ig-hashtag-id}/recent_media?user_id={user-id}&fields={fields} `

Returns a list of the most recently published photo and video [IG
Media](/docs/instagram-api/reference/ig-media) objects published with a
specific hashtag.

#### Query String Parameters

-   ` {user_id} ` (required) --- The ID of the [IG
    User](/docs/instagram-api/reference/ig-user) performing the query.
-   ` {fields} ` --- A comma-separated list of fields you want returned.
    See [Returnable Fields](#returnable-fields) .

```{=html}
<!-- -->
```
-   Only returns public photos and videos.
-   Only returns media objects published within 24 hours of query
    execution.
-   Will not return promoted/boosted/ads media.
-   Responses are paginated with a maximum ` limit ` of 50 results per
    page.
-   Responses will not always be in chronological order.
-   You can query a maximum of 30 unique hashtags [within a 7 day
    period](/docs/instagram-api/reference/ig-user/recently_searched_hashtags)
    .
-   You cannot request the ` username ` field on returned media objects.
-   Responses will not include any personally identifiable information.
-   This endpoint only returns an ` after ` cursor for paginated
    results; a ` before ` cursor will not be included. In addition, the
    ` after ` cursor value will always be the same for each page, but it
    can still be used to get the next page of results in the result set.

**Requirements**

An array of [IG Media](/docs/instagram-api/reference/ig-media) objects.
Excess results will be paginated.

#### Returnable Fields

You can use the ` fields ` parameter to request the following fields on
returned media objects:

-   ` caption `
-   ` children ` (only returned for Album [IG
    Media](/docs/instagram-api/reference/ig-media) )
-   ` comments_count `
-   ` id `
-   ` like_count ` (v10.0 and older calls: value will be ` 0 ` if the
    media owner has
    [hidden](https://www.facebook.com/help/instagram/113355287252104)
    like counts it. v11.0+ calls: field will be omitted if media owner
    has hidden like counts in it)
-   ` media_type `
-   ` media_url ` (not returned for Album [IG
    Media](/docs/instagram-api/reference/ig-media) )
-   ` permalink `
-   ` timestamp ` (only available on v7.0+)

#### Sample Request

``` {._5s-8 .prettyprint .lang-code}
GET graph.facebook.com/17873440459141021/recent_media
  ?user_id=17841405309211844
  &fields=id,media_type,comments_count,like_count
```

#### Sample Response

``` {._5s-8 .prettyprint .lang-code}
{
  "data": [
    {
      "id": "17880997618081620",
      "media_type": "IMAGE",
      "comments_count": 84,
      "like_count": 177
    },
    {
      "id": "17871527143187462"
      "media_type": "IMAGE",
      "comments_count": 24,
      "like_count": 57
    },
    {       
      "id": "17896450804038745"
      "media_type": "IMAGE",
      "comments_count": 19,
      "like_count": 36
    }
  ],
  "paging":
    {
      "cursors":
        {
          "after": "NTAyYmE4..."
        },
      "next": "https://graph.facebook.com/..."
    }
}
```
:::
