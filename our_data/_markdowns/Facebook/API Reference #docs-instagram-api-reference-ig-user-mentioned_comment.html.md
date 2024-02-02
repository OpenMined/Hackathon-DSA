Mentioned Comment - Instagram Platform - Documentation - Meta for Developers

Instagram Graph API* Overview
* Getting Started
* Guides
* Reference
* Changelog
IG User Mentioned Comment
=========================

Returns data on an IG Comment in which an IG User has been @mentioned by another Instagram user.

Creating
--------

This operation is not supported.

Reading
-------

**`GET /{ig-user-id}?fields=mentioned_comment.comment_id`**

Returns data on an IG Comment in which an IG User has been @mentioned by another Instagram user.

### Limitations

This endpoint will return an error if comments have been disabled on the IG Media on which the IG User has been @mentioned.

### Requirements

 Type
  | 
 Description
  || Access Tokens | User |
| Permissions | `instagram_basic`
`instagram_manage_comments`
`pages_read_engagement`
`pages_show_list`
If the app user was granted a role on the Page via the Business Manager, you will also need one of:
`ads_management`
`business_management` |
| Tasks | `MANAGE`, `CREATE_CONTENT`, or `MODERATE` |
### Request Syntax

```
GET https://graph.facebook.com/v19.0/{ig-user-id}
  ?fields=mentioned_comment.comment_id({comment-id}){{fields}}
  &access_token={access-token}
```
### Query String Parameters

 Parameter | Value || `{access_token}`
**Required**
*String* | The app user's User Access Token. |
| `{comment-id}`
**Required**
*String* | The ID of the IG Comment in which the IG User has been @mentioned. The ID is included in the Webhook notification payload. |
| `{fields}`
*Comma-separated list* | A comma-separated list of IG Comment Fields you want returned. If omitted, default fields will be returned. |
### Fields

 Field | Description || `id`
**Default**
*String* | ID of the IG Comment. |
| `like_count`
*String* | Number of times the IG Comment has been liked. |
| `media`
*String* | ID of the IG Media on which the IG Comment was made. Use Field Expansion to get additional fields on the returned IG Media entity. |
| `text`
**Default**
*String* | Text of the IG Comment. |
| `timestamp`
**Default**
*String* | IG Comment creation date formatted in ISO 8601. |
### Response

### Sample Request

```
curl -X GET \
  'https://graph.facebook.com/v19.0/17841405309211844?fields=mentioned_comment.comment_id(17873440459141021){timestamp,like_count,text,id}&access_token=IGQVJ...'
```
#### Sample Response

```
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

You can expand the `media` field with a list of IG Media fields to get additional data on the IG Media entity on which the comment was made. For example:

```
media{id,media_url}
```
**v10.0 and older calls until September 7, 2021:** The `like_count` field on an IG Media will return `0` if the media owner has hidden like counts on it.

**v11.0+ calls, and all versions on September 7, 2021:** If indirectly querying an IG Media through another endpoint or field expansion, the `like_count` field will be omitted from API responses if the media owner has hidden like counts on it. Directly querying the IG Media (which can only be done by the IG Media owner) will return the actual like count, however, even if like counts have been hidden.

#### Sample Field Expansion Request

```
curl -X GET \
  'https://graph.facebook.com/v19.0/17841405309211844?fields=mentioned_comment.comment_id(17873440459141021){timestamp,like_count,text,media{id,media_url}}&access_token=IGQVJ...'
```
#### Sample Field Expansion Response

```
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

If you are using field expansion to access an edge that supports cursor-based pagination, the response will include `before` and `after` cursors if the response contains multiple pages of data. Unlike standard cursor-based pagination, however, the response will not include `previous` or `next` fields, so you will have to use the `before` and `after` cursors to construct `previous` and `next` query strings manually in order to page through the returned data set.

Updating
--------

This operation is not supported.

Deleting
--------

This operation is not supported.