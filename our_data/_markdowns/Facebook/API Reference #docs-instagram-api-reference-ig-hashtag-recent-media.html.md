Recent Media - Instagram Platform - Documentation - Meta for Developers

Instagram Graph API* Overview
* Getting Started
* Guides
* Reference
* Changelog
IG Hashtag Recent Media
=======================

Represents a collection of the most recently published photo and video IG Media objects that have been tagged with a hashtag.

**v10.0 and older calls until September 7, 2021:** The `like_count` field on an IG Media will return `0` if the media owner has hidden like counts on it.

**v11.0+ calls, and all versions on September 7, 2021:** If indirectly querying an IG Media through another endpoint or field expansion, the `like_count` field will be omitted from API responses if the media owner has hidden like counts on it. Directly querying the IG Media (which can only be done by the IG Media owner) will return the actual like count, however, even if like counts have been hidden.

Creating
--------

This operation is not supported.

Reading
-------

### Getting Hashtagged Media

`GET /{ig-hashtag-id}/recent_media?user_id={user-id}&fields={fields}`

Returns a list of the most recently published photo and video IG Media objects published with a specific hashtag.

#### Query String Parameters

* `{user_id}` (required) — The ID of the IG User performing the query.
* `{fields}` — A comma-separated list of fields you want returned. See Returnable Fields.

#### Limitations

* Only returns public photos and videos.
* Only returns media objects published within 24 hours of query execution.
* Will not return promoted/boosted/ads media.
* Responses are paginated with a maximum `limit` of 50 results per page.
* Responses will not always be in chronological order.
* You can query a maximum of 30 unique hashtags within a 7 day period.
* You cannot request the `username` field on returned media objects.
* This endpoint only returns an `after` cursor for paginated results; a `before` cursor will not be included. In addition, the `after` cursor value will always be the same for each page, but it can still be used to get the next page of results in the result set.

**Requirements**

 Type | Description || Features | `Instagram Public Content Access` |
| Permissions | `instagram_basic`
If the token is from a User whose Page role was granted via the Business Manager, one of the following permissions is also required: `ads_management`, `business_management`, or `read_pages_engagement`. |
| Tokens | A User access token of a Facebook User who has been approved for tasks on the connected Facebook Page. |
#### Response

An array of IG Media objects. Excess results will be paginated.

#### Returnable Fields

You can use the `fields` parameter to request the following fields on returned media objects:

* `caption`
* `children` (only returned for Album IG Media)
* `comments_count`
* `id`
* `like_count` (v10.0 and older calls: value will be `0` if the media owner has hidden like counts it. v11.0+ calls: field will be omitted if media owner has hidden like counts in it)
* `media_type`
* `media_url` (not returned for Album IG Media)
* `permalink`
* `timestamp` (only available on v7.0+)

#### Sample Request

```
GET graph.facebook.com/17873440459141021/recent_media
  ?user_id=17841405309211844
  &fields=id,media_type,comments_count,like_count
```
#### Sample Response

```
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
Updating
--------

This operation is not supported.

Deleting
--------

This operation is not supported.