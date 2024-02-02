::: {._4-u3 ._588p}
Returns the list of people who liked this object. When reading likes on
a Page or User object, this endpoint returns a list of pages liked by
that Page or User.

Use the ` likes ` field of an object to get the number of likes.

### New Page Experience

The following objects ` /likes ` endpoint are supported for New Page
Experience:

+-----------------------------------+-----------------------------------+
| -   [Album]                       |                                   |
| (/docs/graph-api/reference/album) |                                   |
| -   [Comment](/                   |                                   |
| docs/graph-api/reference/comment) |                                   |
| -   [Photo]                       |                                   |
| (/docs/graph-api/reference/photo) |                                   |
| -   [PagePost](/d                 |                                   |
| ocs/graph-api/reference/pagepost) |                                   |
+-----------------------------------+-----------------------------------+

### Requirements {#readperms}

-   The same requirements required to view the object are required to
    view likes on that object.

### Limitations

-   Only aggregated counts using ` total_count ` with the ` summary `
    parameter are available for Post likes.

-   The ` like ` reaction counts include both \"like\" and \"care\"
    reactions.

-   ` total_count ` represents the approximate number of likes, however,
    the actual number returned might be different depending on privacy
    settings.

-   The ` GET /{group-post-id}/likes ` and ` GET /{post-id}/likes `
    endpoints are deprecated in v8.0+ and deprecated in all versions on
    Nov. 2, 2020.

### Fields {#readfields}

::: _57-c
  Property Name     Description                                                                                                                                                  Type
  ----------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------ -----------
  ` total_count `   Total number of User and Page likes on the object. To have this field returned, you must include the ` summary=true ` parameter and value in your request.   ` int32 `
:::

### Example Usage

**Sample Request**

``` {._5s-8 .prettyprint .lang-code .prettyprinted}
curl -i -X GET "https://graph.facebook.com/{object-id} ?fields=likes.summary(true) &access_token={access-token}"
```

#### Sample Response

``` {._5s-8 .prettyprint .lang-code .prettyprinted}
 { "likes": { "data": [ { "name": "Bill the Cat", "id": "155111347875779", "created_time": "2017-06-18T18:21:04+0000" }, { "name": "Calvin and Hobbes", "id": "257573197608192", "created_time": "2017-06-18T18:21:02+0000" }, { "name": "Berkeley Breathed's Bloom County", "id": "108793262484769", "created_time": "2017-06-18T18:20:58+0000" } ], "paging": { "cursors": { "before": "Nzc0Njg0MTQ3OAZDZD", "after": "NTcxODc1ODk2NgZDZD" }, "next": "https://graph.facebook.com/vX.X/me/likes?access_token=user-access-token&pretty=0&summary=true&limit=25&after=NTcxODc1ODk2NgZDZD" }, "summary": { "total_count": 136 } }, "id": "user-id"
}
```
:::
