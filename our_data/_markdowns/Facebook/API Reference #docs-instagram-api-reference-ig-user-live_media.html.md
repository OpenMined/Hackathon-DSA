Live Media - Instagram Platform - Documentation - Meta for Developers

Instagram Graph API* Overview
* Getting Started
* Guides
* Reference
* Changelog
IG User Live Media
==================

Represents a collection of live video IG Media on an IG User.

Creating
--------

This operation is not supported.

Reading
-------

**`GET /{ig-user-id}/live_media`**

Get a collection of live video IG Media on an IG User.

### Limitations

Only live video IG Media being broadcast at the time of the request will be returned.

### Time-based Pagination

This endpoint supports time-based pagination. Include `since` and `until` query-string paramaters with Unix timestamp or `strtotime` data values to define a time range.

### Requirements

 Type | Requirement || Access Tokens | User |
| Permissions | `instagram_basic`
`instagram_read_engagement`
`pages_read_engagement`
If the app user was granted a role via the Business Manager on the Page connected to the targeted IG User, you will also need one of:
`ads_management`
`business_management` |
### Request Syntax

```
GET https://graph.facebook.com/{api-version}/{ig-user-id}/live_media
  ?access_token={access-token}
```
### Path Parameters

 Placeholder | Value || `{api-version}`
*String* | API version. |
| `{ig-user-id}`
**Required**
*String* | App user's app-scoped user ID. |
### Query String Parameters

 Key | Value || `access_token`
**Required**
*String* | App user's User access token. |
| `fields`
*Comma-separated list* | Comma-separated list of IG Media fields you want returned for each live IG Media in the result set. |
| `since`
*timestamp* | A Unix timestamp or `strtotime` data value that points to the start of a range of time-based data. See time-based pagination. |
| `until`
*timestamp* | A Unix timestamp or `strtotime` data value that points to the end of a range of time-based data. See time-based pagination. |
### Response

A JSON-formatted object containing the data you requested.

```
{
  "data": [],
  "paging": {}
}
```
#### Response Contents

 Property | Value || `data` | An array of IG Media on an IG User. |
| `paging` | An object containing paging cursors and next/previous data set retrievial URLs. |
### cURL Example

#### Request

```
curl -X GET \
  'https://graph.facebook.com/v19.0/17841405822304914/live_media?fields=id,media_type,media_product_type,owner,username,comments&access_token=IGQVJ...'
```
#### Response

```
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
Updating
--------

This operation is not supported.

Deleting
--------

This operation is not supported.