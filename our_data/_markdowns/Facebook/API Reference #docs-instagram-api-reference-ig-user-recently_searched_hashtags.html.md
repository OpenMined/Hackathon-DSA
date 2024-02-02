Recently Searched Hashtags - Instagram Platform - Documentation - Meta for Developers

Instagram Graph API* Overview
* Getting Started
* Guides
* Reference
* Changelog
Recently Searched Hashtags
==========================

This edge allows you to determine the IG Hashtags that an IG User has queried for within the last 7 days.

Reading
-------

`GET /{ig-user-id}/recently_searched_hashtags`

Get the hashtags that an IG User has queried using the IG Hashtags endpoint within the last 7 days.

IG Users can query a maximum of 30 unique hashtags within a rolling, 7 day period. A queried hashtag will count against that user's limit as soon as it is queried. Subsequent queries on that hashtag within 7 days of the initial query will not count against the user's limit.

**Limitations**

* Emojis in hashtag queries are not supported.
* The API returns 25 results per page by default, but you can use the `limit` parameter to get up to 30 per page (`limit=30`).

#### Requirements

 Type | Description || Features | `Instagram Public Content Access` |
| Permissions | `instagram_basic`
If the token is from a User whose Page role was granted via the Business Manager, one of the following permissions is also required: `ads_management`, `business_management`, or `pages_read_engagement`. |
| Tokens | A Facebook User access token. |
#### Sample Request

```
GET graph.facebook.com/17841405309211844/recently_searched_hashtags?limit=30
```
#### Sample Response

```
{
  "data": [
    {
      "id": "17841562906103814"
    },
    {
      "id": "17841563587120501"
    }
  ]
}
```
Creating
--------

This operation is not supported.

Updating
--------

This operation is not supported.

Deleting
--------

This operation is not supported.