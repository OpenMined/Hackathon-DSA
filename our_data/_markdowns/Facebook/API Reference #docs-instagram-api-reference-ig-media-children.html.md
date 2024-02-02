Children - Instagram Platform - Documentation - Meta for Developers

Instagram Graph API* Overview
* Getting Started
* Guides
* Reference
* Changelog
Children
========

Represents a collection of IG Media objects on an album IG Media.

Creating
--------

This operation is not supported.

Reading
-------

### Getting Child Media Objects

`GET /{ig-media-id}/children`

Returns a list of IG Media objects on an album IG Media object.

#### Permissions

An access token from a User who created the album IG Media object, with the following permissions:

* `instagram_basic`
* `pages_read_engagement` or `pages_show_list`

If the token is from a User whose **Page role was granted via the Business Manager**, one of the following permissions is also required:

* `ads_management`
* `pages_read_engagement`
* `business_management`

#### Limitations

* Some fields, such as `permalink`, cannot be used on photos within albums (children).

#### Sample Request

```
GET graph.facebook.com
  /17896450804038745/children
```
#### Sample Response

```
{
  "data": [
    {
      "id": "17880997618081620"
    },
    {
      "id": "17871527143187462"
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