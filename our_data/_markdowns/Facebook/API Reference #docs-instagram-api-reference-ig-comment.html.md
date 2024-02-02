IG Comment - Instagram Platform - Documentation - Meta for Developers

Instagram Platform* Instagram Graph API
* Instagram Basic Display API
* Sharing to Feed
* Sharing to Stories
* oEmbed
* Embed Button
* Business Login for Instagram
IG Comment
==========

Represents a comment on an IG Media.

Creating
--------

This operation is not supported.

Reading
-------

**`GET /{ig-comment-id}?fields={fields}`**

Get fields and edges on an IG Comment.

### Limitations

* Requests cannot be performed on comments discovered through the Mentions API unless the request is made by the comment owner. Instead, use the Mentioned Comment node.
* Comments on age-gated media are not returned.
* Comments created by IG Users who have been restricted by the app user will not be returned unless the IG Users are unrestricted and the Comments are approved.
* Comments on live video IG Media can only be read while the IG Media upon which the comment was created is being broadcast.

### Requirements

 Type | Requirement || Access Tokens | User |
| Permissions | `instagram_basic`
`pages_read_engagement`
`pages_show_list`
If the app user was granted a role via the Business Manager on the Page connected to the targeted IG User, you will also need one of:
`ads_management`
`business_management` |
### Request Syntax

```
GET https://graph.facebook.com/{api-version}/{ig-comment-id}
  ?fields={fields}
  &access_token={access-token}
```
### Path Parameters

 Placeholder | Value || `{api-version}` | API version. |
| `{ig-comment-id}` | **Required.** IG Comment ID. |
### Query String Parameters

 Key | Placeholder | Value || `access_token` | `{access-token}` | **Required.** App user's User access token. |
| `fields` | `{fields}` | Comma-separated list of IG Comment fields you want returned for each IG Comment in the result set. |
### Fields

 Field Name | Description || `from` | An object containing:
* `id` — IGSID of the Instagram user who created the IG Comment.
* `username` — Username of the Instagram user who created the IG Comment.
 |
| `hidden` | Indicates if comment has been hidden (`true`) or not (`false`). |
| `id` | IG Comment ID. |
| `like_count` | Number of likes on the IG Comment. |
| `media` | An object containing:
* `id` — ID of the IG Media upon which the IG Comment was made.
* `media_product_type` — Published surface of the IG Media (i.e. where the IG Media appears) upon which the IG Comment was made.
 |
| `parent_id` | ID of the parent IG Comment if this comment was created on another IG Comment (i.e. a reply to another comment. |
| `replies` | A list of replies (IG Comments) made on the IG Comment. |
| `text` | IG Comment text. |
| `timestamp` | ISO 8601 formatted timestamp indicating when IG Comment was created.
Example: `2017-05-19T23:27:28+0000`. |
| `user` | ID of IG User who created the IG Comment. Only returned if the app user created the IG Comment, otherwise `username` will be returned instead. |
| `username` | Username of Instagram user who created the IG Comment. |
### Edges

 Edge | Description || `replies` | Get a list of IG Comments on the IG Comment; Create an IG Comment on an IG Comment. |
### Response

A JSON-formatted object containing default and requested fields and edges.

```
{
  "{field}":"{value}",
  ...
}
```
### cURL Example

#### Request

```
curl -i -X GET \
 "https://graph.facebook.com/v19.0/17881770991003328?fields=hidden%2Cmedia%2Ctimestamp&access_token=EAAOc..."
```
#### Response

```
{
  "hidden": false,
  "media": {
    "id": "17856134461174448"
  },
  "timestamp": "2017-05-19T23:27:28+0000",
  "id": "17881770991003328"
}
```
Updating
--------

### Hiding/Unhiding a Comment

`POST /{ig-comment-id}?hide={hide}`

#### Query String Parameters

* `{hide}` (required) — Set to `true` to hide the comment, or `false` to show the comment.

#### Limitations

* Comments made by media object owners on their own media objects will always be displayed, even if the comments have been set to `hide=true`.
* Comments on live video IG Media are not supported.

#### Permissions

A User access token from a Facebook User who created the comment, with the following permissions:

* `instagram_basic`
* `instagram_manage_comments`
* `pages_show_list`
* `pages_read_engagement`

If the token is from a User whose **Page role was granted via the Business Manager**, one of the following permissions is also required:

* `ads_management`
* `pages_read_engagement`
* `business_management`

#### Sample Request

Hiding a comment:

```
POST graph.facebook.com
  /17873440459141021?hide=true
```
#### Sample Response

```
{
  "success": true
}
```
Deleting
--------

### Deleting a Comment

`DELETE /{ig-comment-id}`

#### Permissions

A User access token from a User who created the comment, with the following permissions:

* `instagram_basic`
* `instagram_manage_comments`

If the token is from a User whose **Page role was granted via the Business Manager**, one of the following permissions is also required:

* `ads_management`
* `pages_read_engagement`
* `business_management`

#### Limitations

* A comment can only be deleted by the owner of the object upon which the comment was made, even if the user attempting to delete the comment is the comment's author.
* Comments on live video IG Media are not supported.

#### Sample Request

```
DELETE graph.facebook.com
  /17873440459141021
```
#### Sample Response

```
{
  "success": true
}
```