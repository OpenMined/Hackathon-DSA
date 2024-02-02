Replies - Instagram Platform - Documentation - Meta for Developers

Instagram Graph API* Overview
* Getting Started
* Guides
* Reference
* Changelog
IG Comment Replies
==================

Represents a collection of IG Comments on an IG Comment.

To create an IG Comment on an IG Media object, use the `POST /{ig-media-id}/comments` endpoint instead.

Creating
--------

### Replying to a Comment

`POST /{ig-comment-id}/replies?message={message}`

Creates an IG Comment on an IG Comment.

#### Query String Parameters

Query string parameters are optional unless indicated as required.

* `{message}` (required) — The text to be included in the comment.

#### Limitations

* You can only reply to top-level comments; replies to a reply will be added to the top-level comment.
* You cannot reply to hidden comments.
* You cannot reply to comments on a live video; use the Instagram Messaging API to send a private reply instead.

#### Permissions

A User access token from a User who created the comment, with the following permissions:

* `instagram_basic`
* `instagram_manage_comments`
* `pages_show_list`
* `page_read_engagement`

If the token is from a User whose **Page role was granted via the Business Manager**, one of the following permissions is also required:

* `ads_management`
* `pages_read_engagement`
* `business_management`

#### Sample Request

```
POST graph.facebook.com
  /17870913679156914/replies?message=*sniff*
```
#### Sample Response

```
{
  "id": "17873440459141021"
}
```
Reading
-------

### Getting All Replies (Comments) on a Comment

`GET /{ig-comment-id}/replies`

Returns a list of IG Comments on an IG Comment.

#### Limitations

You cannot get replies to a comment that has been deleted.

#### Permissions

An access token from a User who created the comment, with the following permissions:

* `instagram_basic`
* `pages_show_list`
* `page_read_engagement`

If the token is from a User whose **Page role was granted via the Business Manager**, one of the following permissions is also required:

* `ads_management`
* `pages_read_engagement`
* `business_management`

#### Sample Request

```
GET graph.facebook.com
  /17873440459141021/replies
```
#### Sample Response

```
{
  "data": [
    {
      "timestamp": "2017-08-31T16:53:49+0000",
      "text": "This is a great comment",
      "id": "17871618799146774"
    },
    {
      "timestamp": "2017-08-30T04:24:45+0000",
      "text": "It's me. Trust me.",
      "id": "17887288333072596"
    }
  ]
}
```
Updating
--------

This operation is not supported.

Deleting
--------

This operation is not supported.