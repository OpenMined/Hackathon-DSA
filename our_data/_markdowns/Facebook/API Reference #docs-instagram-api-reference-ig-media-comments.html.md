Comments - Instagram Platform - Documentation - Meta for Developers

Instagram Graph API* Overview
* Getting Started
* Guides
* Reference
* Changelog
Comments
========

Represents a collection of IG Comments on an IG Media object.

### Non-Organic Comments

Comments on Ads containing IG Media (i.e. non-organic comments) are of a different type and are not supported. To get non-organic comments, use the Marketing API and request the Ad's `effective_instagram_story_id`. You can then query the returned ID's `/comments` edge to get a collection of non-organic Instagram Comments. Refer to the Marketing API's Post Moderation guide for more information.

Creating
--------

### Creating a Comment on a Media Object

`POST /{ig-media-id}/comments?message={message}`

Creates an IG Comment on an IG Media object.

#### Limitations

Comments on live video IG Media are not supported.

#### Query String Parameters

Query string parameters are optional unless indicated as required.

* `{message}` (required) — The text to be included in the comment.

#### Permissions

An access token from a User who created the IG Media object, with the following permissions:

* `instagram_basic`
* `instagram_manage_comments`
* `pages_show_list`
* `pages_read_engagement`

If the token is from a User whose **Page role was granted via the Business Manager**, one of the following permissions is also required:

* `ads_management`
* `pages_read_engagement`
* `business_management`

#### Sample Request

```
POST graph.facebook.com
  /17895695668004550/comments?message=This%20is%20awesome!
```
#### Sample Response

```
{
  "id": "17870913679156914"
}
```
Reading
-------

### Getting Comments on a Media Object

`GET /{ig-media-id}/comments`

Returns a list of IG Comments on an IG Media object.

#### Limitations

* Requests made using API version 3.1 or older will have results returned in chronological order. Requests made using version 3.2+ will have results returned in reverse chronological order.
* Returns only top-level comments. Replies to comments are not included unless you use field expansion to request the `replies` field.
* Returns a maximum of 50 comments per query.

#### Permissions

An access token from a User who created the IG Media object, with the following permissions:

* `instagram_basic`
* `pages_show_list`
* `pages_read_engagement`

If the token is from a User whose **Page role was granted via the Business Manager**, one of the following permissions is also required:

* `ads_management`
* `pages_read_engagement`
* `business_management`

#### Sample Request

```
GET graph.facebook.com
  /17895695668004550/comments
```
#### Sample Response

```
{
  "data": [
    {
      "timestamp": "2017-08-31T19:16:02+0000",
      "text": "This is awesome!",
      "id": "17870913679156914"
    },
    {
      "timestamp": "2017-08-31T18:10:30+0000",
      "text": "*Sniff*",
      "id": "17873440459141021"
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