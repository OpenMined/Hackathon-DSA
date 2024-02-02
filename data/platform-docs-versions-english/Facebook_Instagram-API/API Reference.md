Reference
=========

The Instagram API consists of nodes (objects), edges (collections) on those nodes, and fields (object properties). Nodes and Root Edges (edges that are not on a node) are listed below.

Nodes
-----

| Node | Actions |
| --- | --- |
| [IG Comment](https://developers.facebook.com/docs/instagram-api/reference/ig-comment/) | Represents an Instagram comment. |
| [IG Container](https://developers.facebook.com/docs/instagram-api/reference/ig-container/) | Represents a media container for publishing an Instagram post. |
| [IG Hashtag](https://developers.facebook.com/docs/instagram-api/reference/ig-hashtag/) | Represents an Instagram hashtag. |
| [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media/) | Represents an Instagram photo, video, story, or album. |
| [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user/) | Represents an Instagram Business Account or Instagram Creator Account. |
| [Page](https://developers.facebook.com/docs/instagram-api/reference/page/) | Represents a Facebook Page. |

Root Edges
----------

| Root Edge | Actions |
| --- | --- |
| [ig\_hashtag\_search](https://developers.facebook.com/docs/instagram-api/reference/ig-hashtag-search) | Gets the ID of an [IG Hashtag](https://developers.facebook.com/docs/instagram-api/reference/ig-hashtag). |

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

Error Codes
===========

This page describes the error messages that can be returned by the Instragram Graph API. The sample response below shows an example of code `3600` and subcode `2207004` with the subsequent error codes defined.

### Sample Response

{
  "error": 
    {
      "message": "The image size is too large.",
      "type": "OAuthException",
      "code": 36000,
      "error\_subcode": 2207004,
      "is\_transient": false,
      "error\_user\_title": "Image size too large",
      "error\_user\_msg": "The image is too large to download. It should be less than 8 MiB.",
      "fbtrace\_id": "A6LJylpZRKw2xKLFsAP-cJh"
   }
 }

### Error Codes Defined

| HTTP Status Code | Code | Subcode | User Message | Recommended Solution |
| --- | --- | --- | --- | --- |
| `400` | `-2` | `2207003` | `It takes too long to download the media.` | A timeout occured while downloading the media. Try again. |
| `400` | `-2` | `2207020` | `The media you are trying to access has expired. Please try to upload again.` | Generate a new container ID and use it to try again. |
| `400` | `-1` | `2207001` |     | Instagram server error. Try again. |
| `400` | `-1` | `2207032` | `Create media fail, please try to re-create media` | Failed to create a media container. Try again. |
| `400` | `-1` | `2207053` | `unknown upload error` | An unknown error occured during upload. Generate a new container and use it to try again. This should only affect video uploads. |
| `400` | `1` | `2207057` | `Thumbnail offset must be greater than or equal to 0 and less than video duration, i.e.` {video-length} | The thumbnail offset you entered is out of bounds for the video duration. Add the right offset in milliseconds. |
| `400` | `4` | `2207051` | `We restrict certain activity to protect our community. Tell us if you think we made a mistake.` | The publishing action is suspected to be spam. We restrict certain activity to protect our community. Let us know if you can determine that the publishing actions is not spam. |
| `400` | `9` | `2207042` | `You reached maximum number of posts that is allowed to be published by Content Publishing API.` | The app user has reached their daily publishing limit. Advise the app's user to try again the following day. |
| `400` | `24` | `2207006` | `The media with` {media-id} `cannot be found` | Possible permission error due to missing permission or expired token. Generate a new container and use it to try again. |
| `400` | `24` | `2207008` | `The media builder with creation id =` {creation-id} `does not exist or has been expired.` | Temporary error publishing a container. Try again 1–2 times in the next 30 seconds to 2 minutes. If unsuccessful, generate a new container ID and use it to try again. |
| `400` | `25` | `2207050` | `The Instagram account is restricted.` | The app user's Instagram Professional account is inactive, checkpointed, or restricted. Advise the app user to sign in to the Instagram app and complete any actions the app requires to re-enable their account. |
| `400` | `100` | `2207023` | `The media type` {media-type} `is unknown.` | The media type entered is not one of the [expected media types](https://developers.facebook.com/docs/instagram-api/reference/ig-media#fields). Please enter the correct one. |
| `400` | `100` | `2207028` | `Your post won't work as a carousel. Carousels need at least 2 photos/videos and no more than 10 photos/videos.` | Try again using an acceptable number of photos/videos. |
| `400` | `100` | `2207035` | `Product tag positions should not be specified for video media.` | Videos do not support X/Y coordinates. Disallow X/Y coordinates with videos. |
| `400` | `100` | `2207036` | `Product tag positions are required for photo media.` | Image product tags must include X/Y coordinates. Require X/Y coordinates for images. |
| `400` | `100` | `2207037` | `We couldn't add all of your product tags. The product ID may be incorrect, the product may be deleted, or you may not have permission to tag the product.` | One or more of the products being used to tag the item is invalid (deleted, rejected, app user lacks permission, product ID is invalid, etc.). Get the app user's catalogs and eligible products again and allow the app user to only use those product IDs when tagging. |
| `400` | `100` | `2207040` | `Cannot use more than` {max-tag-count} `tags per created media.` | The app user exceeded the maximum number (20) of @ tags. Advise user to use fewer @ tags. |
| `400` | `352` | `2207026` | `The video format is not supported. Please check spec for supported` {video} `format` | Unsupported video format. Advise the app user to upload an MOV or MP4 (MPEG-4 Part 14). See [Video Specifications](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media#video-specifications). |
| `400` | `9004` | `2207052` | `The media could not be fetched from this uri:` {uri} | The media could not be fetched from the supplied URI. Advise the app user to make sure the URI is valid and publicly available. |
| `400` | `9007` | `2207027` | `The media is not ready for publishing, please wait for a moment` | [Check the container status](https://developers.facebook.com/docs/instagram-api/reference/ig-container#fields) and publish when its status is `FINISHED`. |
| `400` | `36000` | `2207004` | `The image is too large to download. It should be less than` {size}`.` | Image exceeded maximum file size of 8MiB. Advise the user to try again with a smaller image. |
| `400` | `36001` | `2207005` | `The image format` {current-image-format} `is not supported. Supported formats are:` {format}`.` | Possible permission error due to missing permission or expired token. Generate a new container and use it to try again. |
| `400` | `36003` | `2207009` | `The submitted image with aspect ratio` {submitted-ratio} `cannot be published. Please submit an image with a valid aspect ratio.` | The image's aspect ratio does not fall within our acceptable range. Advise the app user to try again with an image that falls withing a 4:5 to 1.91:1 range. |
| `400` | `36004` | `2207010` | `The submitted image's caption was` {submitted-caption-length} `characters long. The maximum number of characters permitted for a caption is` {maximum-caption-length}. `Please submit media with a shorter caption.` | The user exceeded the maximum amount of characters for a caption. Advise user to use a shorter caption. Maximum 2,200 characters, 30 hashtags, and 20 @ tags. |

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

IG Comment
==========

Represents a comment on an [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media).

Creating
--------

This operation is not supported.

Reading
-------

**`GET /{ig-comment-id}?fields={fields}`**

Get [fields](#fields) and [edges](#edges) on an IG Comment.

### Limitations

* Requests cannot be performed on comments discovered through the [Mentions API](https://developers.facebook.com/docs/instagram-api/guides/mentions) unless the request is made by the comment owner. Instead, use the [Mentioned Comment](https://developers.facebook.com/docs/instagram-api/reference/ig-user/mentioned_comment) node.
* Comments on age-gated media are not returned.
* Comments created by IG Users who have been restricted by the app user will not be returned unless the IG Users are unrestricted and the Comments are approved.
* Comments on live video IG Media can only be read while the IG Media upon which the comment was created is being broadcast.

### Requirements

| Type | Requirement |
| --- | --- |
| [Access Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens/) | [User](https://developers.facebook.com/docs/facebook-login/access-tokens/#usertokens) |
| [Permissions](https://developers.facebook.com/docs/permissions/reference) | [`instagram_basic`](https://developers.facebook.com/docs/permissions/reference/instagram_basic)  <br>[`pages_read_engagement`](https://developers.facebook.com/docs/permissions/reference/pages_show_list)  <br>[`pages_show_list`](https://developers.facebook.com/docs/permissions/reference/pages_show_list)<br><br>  <br><br>If the app user was granted a role via the Business Manager on the [Page](https://developers.facebook.com/docs/instagram-api/overview#pages) connected to the targeted IG User, you will also need one of:<br><br>  <br><br>[`ads_management`](https://developers.facebook.com/docs/permissions/reference/ads_management)  <br>[`business_management`](https://developers.facebook.com/docs/permissions/reference/business_management) |

### Request Syntax

GET https://graph.facebook.com/{api-version}/{ig-comment-id}
  ?fields={fields}
  &access\_token={access-token}

### Path Parameters

| Placeholder | Value |
| --- | --- |
| `{api-version}` | API [version](https://developers.facebook.com/docs/graph-api/guides/versioning). |
| `{ig-comment-id}` | **Required.** IG Comment ID. |

### Query String Parameters

| Key | Placeholder | Value |
| --- | --- | --- |
| `access_token` | `{access-token}` | **Required.** App user's [User](https://developers.facebook.com/docs/facebook-login/access-tokens/#usertokens) access token. |
| `fields` | `{fields}` | Comma-separated list of IG Comment [fields](#fields) you want returned for each IG Comment in the result set. |

### Fields

| Field Name | Description |
| --- | --- |
| `from` | An object containing:<br><br>  <br><br>* `id` — [IGSID](https://developers.facebook.com/docs/messenger-platform/instagram/overview#igsid) of the Instagram user who created the IG Comment.<br>* `username` — Username of the Instagram user who created the IG Comment. |
| `hidden` | Indicates if comment has been hidden (`true`) or not (`false`). |
| `id` | IG Comment ID. |
| `like_count` | Number of likes on the IG Comment. |
| `media` | An object containing:<br><br>  <br><br>* `id` — ID of the [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media/) upon which the IG Comment was made.<br>* `media_product_type` — Published surface of the [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media/) (i.e. where the IG Media appears) upon which the IG Comment was made. |
| `parent_id` | ID of the parent IG Comment if this comment was created on another IG Comment (i.e. a reply to another comment. |
| `replies` | A list of replies (IG Comments) made on the IG Comment. |
| `text` | IG Comment text. |
| `timestamp` | ISO 8601 formatted timestamp indicating when IG Comment was created.<br><br>  <br><br>Example: `2017-05-19T23:27:28+0000`. |
| `user` | ID of IG User who created the IG Comment. Only returned if the app user created the IG Comment, otherwise `username` will be returned instead. |
| `username` | Username of Instagram user who created the IG Comment. |

### Edges

| Edge | Description |
| --- | --- |
| [`replies`](https://developers.facebook.com/docs/instagram-api/reference/ig-comment/replies) | Get a list of IG Comments on the IG Comment; Create an IG Comment on an IG Comment. |

### Response

A JSON-formatted object containing default and requested [fields](#fields) and [edges](#edges).

{
  "{field}":"{value}",
  ...
}

### cURL Example

#### Request

curl -i -X GET \\
 "https://graph.facebook.com/`v18.0`/17881770991003328?fields=hidden%2Cmedia%2Ctimestamp&access\_token=EAAOc..."

#### Response

{
  "hidden": false,
  "media": {
    "id": "17856134461174448"
  },
  "timestamp": "2017-05-19T23:27:28+0000",
  "id": "17881770991003328"
}

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

A User [access token](https://developers.facebook.com/docs/instagram-api/overview#authentication) from a Facebook User who created the comment, with the following permissions:

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

POST graph.facebook.com
  /17873440459141021?hide=true

#### Sample Response

{
  "success": true
}

Deleting
--------

### Deleting a Comment

`DELETE /{ig-comment-id}`

#### Permissions

A User [access token](https://developers.facebook.com/docs/instagram-api/overview#authentication) from a User who created the comment, with the following permissions:

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

DELETE graph.facebook.com
  /17873440459141021

#### Sample Response

{
  "success": true
}

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

IG Comment Replies
==================

Represents a collection of [IG Comments](https://developers.facebook.com/docs/instagram-api/reference/ig-comment) on an [IG Comment](https://developers.facebook.com/docs/instagram-api/reference/ig-comment).

To create an [IG Comment](https://developers.facebook.com/docs/instagram-api/reference/ig-comment) on an [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object, use the [`POST /{ig-media-id}/comments`](https://developers.facebook.com/docs/instagram-api/reference/ig-media/comments) endpoint instead.

Creating
--------

### Replying to a Comment

`POST /{ig-comment-id}/replies?message={message}`

Creates an [IG Comment](https://developers.facebook.com/docs/instagram-api/reference/ig-comment) on an [IG Comment](https://developers.facebook.com/docs/instagram-api/reference/ig-comment).

#### Query String Parameters

Query string parameters are optional unless indicated as required.

* `{message}` (required) — The text to be included in the comment.

#### Limitations

* You can only reply to top-level comments; replies to a reply will be added to the top-level comment.
* You cannot reply to hidden comments.
* You cannot reply to comments on a live video; use the [Instagram Messaging API](https://developers.facebook.com/docs/messenger-platform/instagram) to send a [private reply](https://developers.facebook.com/docs/messenger-platform/instagram/features/private-replies) instead.

#### Permissions

A User [access token](https://developers.facebook.com/docs/instagram-api/overview#authentication) from a User who created the comment, with the following permissions:

* `instagram_basic`
* `instagram_manage_comments`
* `pages_show_list`
* `page_read_engagement`

If the token is from a User whose **Page role was granted via the Business Manager**, one of the following permissions is also required:

* `ads_management`
* `pages_read_engagement`
* `business_management`

#### Sample Request

POST graph.facebook.com
  /17870913679156914/replies?message=\*sniff\*

#### Sample Response

{
  "id": "17873440459141021"
}

Reading
-------

### Getting All Replies (Comments) on a Comment

`GET /{ig-comment-id}/replies`

Returns a list of [IG Comments](https://developers.facebook.com/docs/instagram-api/reference/ig-comment) on an [IG Comment](https://developers.facebook.com/docs/instagram-api/reference/ig-comment).

#### Limitations

You cannot get replies to a comment that has been deleted.

#### Permissions

An [access token](https://developers.facebook.com/docs/facebook-login/access-tokens) from a User who created the comment, with the following permissions:

* `instagram_basic`
* `pages_show_list`
* `page_read_engagement`

If the token is from a User whose **Page role was granted via the Business Manager**, one of the following permissions is also required:

* `ads_management`
* `pages_read_engagement`
* `business_management`

#### Sample Request

GET graph.facebook.com
  /17873440459141021/replies

#### Sample Response

{
  "data": \[
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
  \]
}

Updating
--------

This operation is not supported.

Deleting
--------

This operation is not supported.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

IG Container
============

Represents a media container for publishing an Instagram post. Refer to the [Content Publishing](https://developers.facebook.com/docs/instagram-api/guides/content-publishing) guide for complete publishing steps.

Creating
--------

This operation is not supported.

Reading
-------

**`GET /{instagram-container-id}`**

Get [fields](#fields) and [edges](#edges) on an IG Container.

### Requirements

| Type | Description |
| --- | --- |
| [Access Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) | [User](https://developers.facebook.com/docs/facebook-login/access-tokens/#usertokens) |
| [Permissions](https://developers.facebook.com/docs/apps/review/login-permissions) | [`instagram_basic`](https://developers.facebook.com/docs/facebook-login/permissions#reference-instagram_basic)  <br>[`instagram_content_publish`](https://developers.facebook.com/docs/permissions/reference/instagram_content_publish)  <br>[`pages_read_engagement`](https://developers.facebook.com/docs/permissions/reference/pages_read_engagement)<br><br>  <br><br>If the app user was granted a role on the Page via the Business Manager, one of the following permissions is also required:<br><br>  <br><br>[`ads_management`](https://developers.facebook.com/docs/permissions/reference/ads_management)  <br>[`business_management`](https://developers.facebook.com/docs/permissions/reference/business_management) |

### Request Syntax

GET https://graph.facebook.com/{instagram-container-id}
  ?fields={fields}
  &access\_token={access-token}

### Query String Parameters

| Parameter | Value |
| --- | --- |
| `access_token`  <br>**Required**  <br>_String_ | The app user's [User](https://developers.facebook.com/docs/facebook-login/access-tokens/#usertokens) access token. |
| `fields`  <br>_Comma-separated list_ | A comma-separated list of [fields](#fields) and [edges](#edges) you want returned. If omitted, default fields will be returned. |

### Fields

| Field Name | Description |
| --- | --- |
| `copyright_check_status` | Used to determine if an uploaded video is violating copyright. Key-values pairs return include:<br><br>* `matches_found` set to one of the following:<br>    * `true` – the video is violating copyright<br>    * `false` – the video is not violating copyright<br>* `status` set to one of the following:<br>    * `completed` – the detection process has finished<br>    * `error` – an error occurred during the detection process<br>    * `in_progress` – the detection process is ongoing<br>    * `not_started` – the detection process has not started |
| `id` | Instagram Container ID, represented in code examples as `{instagram-container-id}` |
| `status` | Publishing status. If `status_code` is `ERROR`, this value will be an [error subcode](https://developers.facebook.com/docs/instagram-api/reference/error-codes). |
| `status_code` | The container's publishing status. Possible values:<br><br>  <br><br>* `EXPIRED` — The container was not published within 24 hours and has expired.<br>* `ERROR` — The container failed to complete the publishing process.<br>* `FINISHED` — The container and its media object are ready to be published.<br>* `IN_PROGRESS` — The container is still in the publishing process.<br>* `PUBLISHED` — The container's media object has been published. |

### Edges

There are no edges on this node.

### Response

A JSON-formatted object containing default and requested [fields](#fields).

{
  "{field}":"{value}",
  ...
}

### Sample Request

curl -X GET \\
  'https://graph.facebook.com/17889615691921648?fields=status\_code&access\_token=IGQVJ...'

### Sample Response

{
  "status\_code": "FINISHED",
  "id": "17889615691921648"
}

Updating
--------

This operation is not supported.

Deleting
--------

This operation is not supported.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

IG Hashtag Search
=================

This root edge allows you to get [IG Hashtag](https://developers.facebook.com/docs/instagram-api/reference/ig-hashtag) IDs.

Creating
--------

This operation is not supported.

Reading
-------

### Getting a Hashtag ID

`GET /ig_hashtag_search?user_id={user-id}&q={q}`

Returns the ID of an [IG Hashtag](https://developers.facebook.com/docs/instagram-api/reference/ig-hashtag). IDs are both static and global (i.e, the ID for `#bluebottle` will always be `17843857450040591` for all apps and all app users).

#### Query String Parameters

* `{user_id}` (required) — The ID of the [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) performing the request.
* `{q}` (required) — The hashtag name to query.

#### Limitations

* You can query a maximum of 30 unique hashtags [within a 7 day period](https://developers.facebook.com/docs/instagram-api/reference/ig-user/recently_searched_hashtags).
* The API will return a generic error for any queries that include hashtags that we have deemed sensitive or offensive.

**Requirements**

| Type | Description |
| --- | --- |
| [Features](https://developers.facebook.com/docs/apps/review/feature) | [`Instagram Public Content Access`](https://developers.facebook.com/docs/apps/review/feature#reference-INSTAGRAM_PUBLIC_CONTENT_ACCESS) |
| [Permissions](https://developers.facebook.com/docs/apps/review/login-permissions) | [`instagram_basic`](https://developers.facebook.com/docs/facebook-login/permissions#reference-instagram_basic)<br><br>  <br><br>If the token is from a User whose Page role was granted via the Business Manager, one of the following permissions is also required: `ads_management`, `business_management`, or `pages_read_engagement`. |
| [Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) | A User access token of a Facebook User who has been [approved for tasks on the connected Facebook Page](https://developers.facebook.com/docs/instagram-api/overview#access-tokens). |

#### Sample Request

curl -X GET \\
 "https://graph.facebook.com/`v18.0`/ig\_hashtag\_search?user\_id=17841405309211844&q=bluebottle&access\_token={access-token}"

#### Sample Response

{
    "data": \[
        {
            "id": "17843857450040591"
        }
    \]
}

Updating
--------

This operation is not supported.

Deleting
--------

This operation is not supported.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

IG Hashtag
==========

Represents an Instagram hashtag.

Creating
--------

This operation is not supported.

Reading
-------

**`GET /{ig-hashtag-id}`**

Returns [Fields](#fields) and [Edges](#edges) on an IG Hashtag.

### Limitations

You can query a maximum of 30 unique hashtags [within a 7 day period](https://developers.facebook.com/docs/instagram-api/reference/ig-user/recently_searched_hashtags).

### Requirements

| Type | Description |
| --- | --- |
| [Features](https://developers.facebook.com/docs/apps/review/feature) | [`Instagram Public Content Access`](https://developers.facebook.com/docs/apps/review/feature#reference-INSTAGRAM_PUBLIC_CONTENT_ACCESS) |
| [Permissions](https://developers.facebook.com/docs/apps/review/login-permissions) | [`instagram_basic`](https://developers.facebook.com/docs/facebook-login/permissions#reference-instagram_basic)<br><br>  <br><br>If the token is from a User whose Page role was granted via the Business Manager, one of the following permissions is also required: `ads_management`, `business_management`, or [`pages_read_engagement`](https://developers.facebook.com/docs/pages/overview#permissions). |
| [Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) | The app user's [User](https://developers.facebook.com/docs/facebook-login/access-tokens/#usertokens) access token. |

### Request Syntax

GET https://graph.facebook.com/{ig-hashtag-id}
  ?fields={fields}
  &access\_token={access-token}

### Query String Parameters

Include the following query string parameters to augment the request.

| Key | Value |
| --- | --- |
| `access_token`  <br>**Required**  <br>_String_ | The app user's [Instagram User Access Token](https://developers.facebook.com/docs/instagram-basic-display-api/overview#instagram-user-access-tokens). |
| `fields`  <br>_Comma-separated list_ | A comma-separated list of [Fields](#fields) and [Edges](#edges) you want returned. If omitted, default fields will be returned. |

### Fields

You can use the `fields` query string parameter to request the following Fields on an IG Hashtag.

| Field Name | Description |
| --- | --- |
| `id` | The hashtag's ID (included by default). IDs are static and global. |
| `name` | The hashtag's name, without the leading hash symbol. |

### Edges

You can request the following edges as path parameters or by using the `fields` query string parameter.

| Edge | Description |
| --- | --- |
| [`recent_media`](https://developers.facebook.com/docs/instagram-api/reference/ig-hashtag/recent-media#reading) | Get a list of the most recently published photo and video [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) objects published with a specific hashtag. |
| [`top_media`](https://developers.facebook.com/docs/instagram-api/reference/ig-hashtag/top-media#reading) | Returns the most popular photo and video [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) objects that have been tagged with the hashtag. |

### Response

A JSON-formatted object containing default and requested [Fields](#fields).

{
  "{field}":"{value}",
  ...
}

### Sample Request

GET https://graph.facebook.com/17841593698074073
  ?fields=id,name
  &access\_token=EAADd...

### Sample Response

{
  "id": "17841593698074073",
  "name": "coke"
}

Updating
--------

This operation is not supported.

Deleting
--------

This operation is not supported.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

IG Hashtag Recent Media
=======================

Represents a collection of the most recently published photo and video [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) objects that have been tagged with a hashtag.

**v10.0 and older calls until September 7, 2021:** The [`like_count`](https://developers.facebook.com/docs/instagram-api/reference/ig-media#fields) field on an IG Media will return `0` if the media [owner](https://developers.facebook.com/docs/instagram-api/overview#authorization) has [hidden](https://www.facebook.com/help/instagram/113355287252104) like counts on it.

**v11.0+ calls, and all versions on September 7, 2021:** If indirectly querying an [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) through another endpoint or field expansion, the [`like_count`](https://developers.facebook.com/docs/instagram-api/reference/ig-media#fields) field will be omitted from API responses if the media owner has hidden like counts on it. Directly querying the IG Media (which can only be done by the IG Media owner) will return the actual like count, however, even if like counts have been hidden.

Creating
--------

This operation is not supported.

Reading
-------

### Getting Hashtagged Media

`GET /{ig-hashtag-id}/recent_media?user_id={user-id}&fields={fields}`

Returns a list of the most recently published photo and video [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) objects published with a specific hashtag.

#### Query String Parameters

* `{user_id}` (required) — The ID of the [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) performing the query.
* `{fields}` — A comma-separated list of fields you want returned. See [Returnable Fields](#returnable-fields).

#### Limitations

* Only returns public photos and videos.
* Only returns media objects published within 24 hours of query execution.
* Will not return promoted/boosted/ads media.
* Responses are paginated with a maximum `limit` of 50 results per page.
* Responses will not always be in chronological order.
* You can query a maximum of 30 unique hashtags [within a 7 day period](https://developers.facebook.com/docs/instagram-api/reference/ig-user/recently_searched_hashtags).
* You cannot request the `username` field on returned media objects.
* Responses will not include any personally identifiable information.
* This endpoint only returns an `after` cursor for paginated results; a `before` cursor will not be included. In addition, the `after` cursor value will always be the same for each page, but it can still be used to get the next page of results in the result set.

**Requirements**

| Type | Description |
| --- | --- |
| [Features](https://developers.facebook.com/docs/apps/review/feature) | [`Instagram Public Content Access`](https://developers.facebook.com/docs/apps/review/feature#reference-INSTAGRAM_PUBLIC_CONTENT_ACCESS) |
| [Permissions](https://developers.facebook.com/docs/apps/review/login-permissions) | [`instagram_basic`](https://developers.facebook.com/docs/facebook-login/permissions#reference-instagram_basic)<br><br>  <br><br>If the token is from a User whose Page role was granted via the Business Manager, one of the following permissions is also required: `ads_management`, `business_management`, or `read_pages_engagement`. |
| [Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens) | A User access token of a Facebook User who has been [approved for tasks on the connected Facebook Page](https://developers.facebook.com/docs/instagram-api/overview#authentication). |

#### Response

An array of [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) objects. Excess results will be paginated.

#### Returnable Fields

You can use the `fields` parameter to request the following fields on returned media objects:

* `caption`
* `children` (only returned for Album [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media))
* `comments_count`
* `id`
* `like_count` (v10.0 and older calls: value will be `0` if the media owner has [hidden](https://www.facebook.com/help/instagram/113355287252104) like counts it. v11.0+ calls: field will be omitted if media owner has hidden like counts in it)
* `media_type`
* `media_url` (not returned for Album [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media))
* `permalink`
* `timestamp` (only available on v7.0+)

#### Sample Request

GET graph.facebook.com/17873440459141021/recent\_media
  ?user\_id=17841405309211844
  &fields=id,media\_type,comments\_count,like\_count

#### Sample Response

{
  "data": \[
    {
      "id": "17880997618081620",
      "media\_type": "IMAGE",
      "comments\_count": 84,
      "like\_count": 177
    },
    {
      "id": "17871527143187462"
      "media\_type": "IMAGE",
      "comments\_count": 24,
      "like\_count": 57
    },
    {       
      "id": "17896450804038745"
      "media\_type": "IMAGE",
      "comments\_count": 19,
      "like\_count": 36
    }
  \],
  "paging":
    {
      "cursors":
        {
          "after": "NTAyYmE4..."
        },
      "next": "https://graph.facebook.com/..."
    }
}

Updating
--------

This operation is not supported.

Deleting
--------

This operation is not supported.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

IG Hashtag Top Media
====================

Represents a collection of the most popular photo and video [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) objects that have been tagged with a hashtag.

Popularity is determined by a mix of views and viewer interaction using the same methodology that determines the top posts when [searching for a hashtag](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.instagram.com%2Fexplore%2Ftags%2Fhalloween%2F&h=AT2Fug9fJSffIoihZqmAS4FJxi97jSL5BA1-gSBmw6Wdsxg4Wpcx6ur_MVtPTDtn4HmGwjHa61Q_gslq4vmoQycA0hBeC0hij9AuyiBkdbLn4ip98Itdk6ioXB5UmxOWDxHWpcV9ablo9q29) on [www.instagram.com](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.instagram.com%2F&h=AT1Rmeo_7upk1LHofFfGPFLqvFY2-CMvIwCoNxSPWtOg50czvbLts9sCdeElNNVc67WO16bz64Hx4DRUO4X1PWTo--jC0ehhRYJjuzBcgm9tfuiXlG3VlZBTEoNm_YW5eh7PRZmd5cN0Cex-).

**v10.0 and older calls until September 7, 2021:** The [`like_count`](https://developers.facebook.com/docs/instagram-api/reference/ig-media#fields) field on an IG Media will return `0` if the media [owner](https://developers.facebook.com/docs/instagram-api/overview#authorization) has [hidden](https://www.facebook.com/help/instagram/113355287252104) like counts on it.

**v11.0+ calls, and all versions on September 7, 2021:** If indirectly querying an [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) through another endpoint or field expansion, the [`like_count`](https://developers.facebook.com/docs/instagram-api/reference/ig-media#fields) field will be omitted from API responses if the media owner has hidden like counts on it. Directly querying the IG Media (which can only be done by the IG Media owner) will return the actual like count, however, even if like counts have been hidden.

Creating
--------

This operation is not supported.

Reading
-------

### Getting the Most Popular Hashtagged Media

`GET /{ig-hashtag-id}/top_media?user_id={user-id}&fields={fields}`

Returns the most popular photo and video [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) objects that have been tagged with the hashtag.

#### Query String Parameters

* `{user_id}` (required) — The ID of the Instagram Business or Creator Account performing the query.
* `{fields}` — A comma-separated list of fields you want returned. See [Returnable Fields](#returnable-fields).

#### Limitations

* This edge only returns public photos and videos.
* Will not return promoted/boosted/ads media.
* Responses are paginated with a maximum `limit` of 50 results per page.
* You can query a maximum of 30 unique hashtags [within a 7 day period](https://developers.facebook.com/docs/instagram-api/reference/ig-user/recently_searched_hashtags).
* You cannot request the `username` field on returned media objects.
* Responses will not include any personally identifiable information.
* This endpoint only returns an `after` cursor for paginated results; a `before` cursor will not be included. In addition, the `after` cursor value will always be the same for each page, but it can still be used to get the next page of results in the result set.

**Requirements**

| Type | Description |
| --- | --- |
| [Features](https://developers.facebook.com/docs/apps/review/feature) | [`Instagram Public Content Access`](https://developers.facebook.com/docs/apps/review/feature#reference-INSTAGRAM_PUBLIC_CONTENT_ACCESS) |
| [Permissions](https://developers.facebook.com/docs/apps/review/login-permissions) | [`instagram_basic`](https://developers.facebook.com/docs/facebook-login/permissions#reference-instagram_basic)<br><br>  <br><br>If the token is from a User whose Page role was granted via the Business Manager, one of the following permissions is also required: `ads_management`, `business_management`, or `pages_read_engagement`. |
| [Tokens](https://developers.facebook.com/docs/instagram-api/overview#access-tokens) | A User access token of a Facebook User who has been [approved for tasks on the connected Facebook Page](https://developers.facebook.com/docs/instagram-api/overview#access-tokens). |

#### Response

An array of [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) objects. Excess results will be paginated.

#### Returnable Fields

You can use the `fields` parameter to request the following fields on returned media objects:

* `caption`
* `children` (only returned for Album [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media))
* `comments_count`
* `id`
* `like_count` (v10.0 and older calls: value will be `0` if the media owner has [hidden](https://www.facebook.com/help/instagram/113355287252104) like counts it. v11.0+ calls: field will be omitted if media owner has hidden like counts in it.)
* `media_type`
* `media_url` (not returned for Album [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media))
* `permalink`
* `timestamp` (only available on v7.0+)

#### Sample Request

GET graph.facebook.com/17873440459141021/top\_media
  ?user\_id=17841405309211844
  &fields=id,media\_type,comments\_count,like\_count

#### Sample Response

{
  "data": \[
    {
      "id": "17880997618081620",
      "media\_type": "IMAGE",
      "comments\_count": 84,
      "like\_count": 177
    },
    {
      "id": "17871527143187462"
      "media\_type": "IMAGE",
      "comments\_count": 24,
      "like\_count": 57
    },
    {       
      "id": "17896450804038745"
      "media\_type": "IMAGE",
      "comments\_count": 19,
      "like\_count": 36
    },
    ... // Results truncated for clarity
  \],
  "paging":
    {
      "cursors":
        {
          "after": "NTAyYmE4..."
        },
      "next": "https://graph.facebook.com/..."
    }
}

Updating
--------

This operation is not supported.

Deleting
--------

This operation is not supported.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

IG Media
========

Represents an Instagram album, photo, or video (uploaded video, live video, video created with the Instagram TV app, reel, or story).

Creating
--------

This operation is not supported.

Reading
-------

**`GET /{ig-media-id}`**

Gets [fields](#fields) and [edges](#edges) on IG media.

### Limitations

* Fields that return aggregated values don't include ads-driven data. For example, `comments_count` counts comments on a photo, but not comments on ads that contain that photo.
* Captions don't include the `@` symbol unless the app user is also able to perform Admin-equivalent [tasks](https://developers.facebook.com/docs/pages/overview#tasks) on the app.
* Some fields, such as `permalink`, cannot be used on photos within albums (children).
* Instagram TV media must be shared to Instagram at the time of publish (**Post a Preview** or **Share Preview to Feed** enabled) in order to be accessible via the API.
* Live video IG Media can only be read while they are being broadcast.

### Requirements

| Type | Description |
| --- | --- |
| [Access Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) | [User](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens). |
| [Permissions](https://developers.facebook.com/docs/apps/review/login-permissions) | [`instagram_basic`](https://developers.facebook.com/docs/permissions/reference/instagram_basic)  <br>[`pages_read_engagement`](https://developers.facebook.com/docs/permissions/reference/pages_read_engagement)  <br>[`pages_show_list`](https://developers.facebook.com/docs/permissions/reference/pages_show_list)<br><br>  <br><br>If the app user was granted a role on the Page via the Business Manager, you also need one of the following:<br><br>  <br><br>[`ads_management`](https://developers.facebook.com/docs/permissions/reference/ads_management)  <br>[`business_management`](https://developers.facebook.com/docs/permissions/reference/business_management) |

### Request Syntax

GET https://graph.facebook.com/{api-version}/{ig-media-id}
  ?fields={fields}
  &access\_token={access-token}

### Path Parameters

| Placeholder | Value |
| --- | --- |
| `{api-version}` | API [version](https://developers.facebook.com/docs/graph-api/guides/versioning). |
| `{ig-media-id}` | **Required.** IG Media ID. |

### Query String Parameters

| Key | Placeholder | Value |
| --- | --- | --- |
| `access_token` | `{access-token}` | **Required.** App user's [user access token](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens). |
| `fields` | `{fields}` | Comma-separated list of [fields](#fields) you want returned. |

### Fields

Public fields can be read via field expansion.

FieldDescription

`caption`  
Public

Caption. Excludes album children. The `@` symbol is excluded, unless the app user can perform admin-equivalent [tasks](https://developers.facebook.com/docs/pages/overview#tasks) on the Facebook Page connected to the Instagram account used to create the caption.

`comments_count`  
Public

Count of comments on the media. Excludes comments on album child media and the media's caption. Includes replies on comments.

`copyright_check_information.status`

Returns `status` and `matches_found` objects

| status objects | Description |
| --- | --- |
| `status` | * `completed` – the detection process has finished<br>* `error` – an error occurred during the detection process<br>* `in_progress` – the detection process is ongoing<br>* `not_started` – the detection process has not started |
| `matches_found` | Set to one of the following:<br><br>* `false` if the video **does not violate** copyright,<br>* `true` if the video **does violate** copyright |

If a video **is violating copyright**, the `copyright_matches` is returned with an array of objects about the copyrighted material, when the violation is occurring in the video, and the actions take to mitigate the violation.

| copyright\_matches objects | Description |
| --- | --- |
| `author` | the author of the copyrighted video |
| `content_title` | the name of the copyrighted video |
| `matched_segments` | An array of objects with the following key-value pairs: \* `duration_in_seconds` – the number of seconds the content violates copyright \* `segment_type` – either `AUDIO` or `VIDEO` \* `start_time_in_seconds` – set to the start time of the video |
| `owner_copyright_policy` | Objects returned include:<br><br>* `name` – The name for the copyright owners' policy<br>* `actions` – An array of `action` objects with the mitigations steps taken defined by the copyright owner's policy. May include different mitigations steps for different locations.<br>    <br>    * `action` – The mitigation action taken against the video violating copyright. Different mitigation steps can be taken for different countries. Can be one of the following values:<br>        * `BLOCK` – The video is blocked from the audiences listed in the `geos` array<br>        * `MUTE` - The video is muted for audiences listed in the `geos` array |

`id`  
Public

Media ID.

`ig_id`  
Public

Instagram media ID. Used with Legacy Instagram API, now deprecated. Use `id` instead.

`is_comment_enabled`

Indicates if comments are enabled or disabled. Excludes album children.

`is_shared_to_feed`  
Public

For Reels only. When `true`, indicates that the reel can appear in both the **Feed** and **Reels** tabs. When `false`, indicates that the reel can only appear in the **Reels** tab.

Neither value determines whether the reel actually appears in the **Reels** tab because the reel may not meet eligibilty requirements or may not be selected by our algorithm. See [reel specifications](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media#reel-specifications) for eligibility critera.

`like_count`

Count of likes on the media, including replies on comments. Excludes likes on album child media and likes on promoted posts created from the media.

  

If queried indirectly through another endpoint or field expansion:

  

* **v10.0 and older calls:** The value is `0` if the media owner has [hidden](https://www.facebook.com/help/instagram/113355287252104) like counts.
* **v11.0+ calls:** The `like_count` field is omitted if the media owner has hidden like counts.

`media_product_type`  
Public

Surface where the media is published. Can be `AD`, `FEED`, `STORY` or `REELS`.

`media_type`  
Public

Media type. Can be `CAROUSEL_ALBUM`, `IMAGE`, or `VIDEO`.

`media_url`  
Public

The URL for the media.

The `media_url` field is omitted from responses if the media contains copyrighted material or has been flagged for a copyright violation. Examples of copyrighted material can include audio on reels.

`owner`  
Public

Instagram user ID who created the media. Only returned if the app user making the query also created the media; otherwise, `username` field is returned instead.

`permalink`  
Public

Permanent URL to the media.

`shortcode`  
Public

Shortcode to the media.

`thumbnail_url`  
Public

Media thumbnail URL. Only available on `VIDEO` media.

`timestamp`  
Public

[ISO 8601](https://l.facebook.com/l.php?u=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FISO_8601&h=AT1Wb-YmtAiffvxoGN81YWKGtsp4OqFfe7yTMnr4yFEvZSxT6joBmwp6Jbmjw66FoAOeIub4gkWnF0sQ3zFfelvYiMHElyFvKOmsUWIGgn-g4fLrBsGq_Bv6zbe5AaRVrRfVOiFsA0MPK7qxuiKOKPVvnYNhXQ)\-formatted creation date in UTC (default is UTC ±00:00).

`username`  
Public

Username of user who created the media.

`video_title`  
Public

Deprecated. Omitted from response.

### Edges

Public edges can be returned through field expansion.

| Edge | Description |
| --- | --- |
| [`children`](https://developers.facebook.com/docs/instagram-api/reference/ig-media/children)  <br>Public. | Represents a collection of [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) objects on an album [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media). |
| [`collaborators`](https://developers.facebook.com/docs/instagram-api/reference/ig-media/collaborators) | Represents a list of users who are added as collaborators on an [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object. |
| [`comments`](https://developers.facebook.com/docs/instagram-api/reference/ig-media/comments) | Represents a collection of [IG Comments](https://developers.facebook.com/docs/instagram-api/reference/ig-comment) on an [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object. |
| [`insights`](https://developers.facebook.com/docs/instagram-api/reference/ig-media/insights) | Represents social interaction metrics on an [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object. |

### cURL Example

#### Request

curl -X GET \\
  'https://graph.facebook.com/`v18.0`/17895695668004550?fields=id,media\_type,media\_url,owner,timestamp&access\_token=IGQVJ...'

#### Response

{
  "id": "17918920912340654",
  "media\_type": "IMAGE",
  "media\_url": "https://sconten...",
  "owner": {
    "id": "17841405309211844"
  },
  "timestamp": "2019-09-26T22:36:43+0000"
}

Updating
--------

**`POST /{ig-media-id}`**

Enable or disable comments on an IG Media.

### Limitations

Live video IG Media not supported.

### Requirements

| Type | Description |
| --- | --- |
| [Access Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) | [User](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens). |
| [Permissions](https://developers.facebook.com/docs/apps/review/login-permissions) | [`instagram_basic`](https://developers.facebook.com/docs/permissions/reference/instagram_basic)  <br>[`instagram_manage_comments`](https://developers.facebook.com/docs/permissions/reference/instagram_manage_comments)  <br>[`pages_show_list`](https://developers.facebook.com/docs/permissions/reference/pages_show_list)<br><br>  <br><br>If the app user was granted a role on the Page via the Business Manager, you also need one of the following:<br><br>  <br><br>[`ads_management`](https://developers.facebook.com/docs/permissions/reference/ads_management)  <br>[`business_management`](https://developers.facebook.com/docs/permissions/reference/business_management) |

### Request Syntax

POST https://graph.facebook.com/{api-version}/{ig-media-id}
  ?comment\_enabled={comment-enabled}
  &access\_token={access-token}

### Path Parameters

| Placeholder | Value |
| --- | --- |
| `{api-version}` | API [version](https://developers.facebook.com/docs/graph-api/guides/versioning). |
| `{ig-media-id}` | **Required.** IG Media ID. |

### Query String Parameters

| Key | Placeholder | Value |
| --- | --- | --- |
| `access_token` | `{access-token}` | **Required.** App user's [user access token](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens). |
| `comment_enabled` | `{comment-enabled}` | **Required.** Set to `true` to enable comments or `false` to disable comments. |

### cURL Example

#### Request

curl -i -X POST \\
 "https://graph.facebook.com/`v18.0`/17918920912340654?comment\_enabled=true&access\_token=EAAOc..."

#### Response

{
  "success": true
}

Deleting
--------

This operation is not supported.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

Children
========

Represents a collection of [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) objects on an album [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media).

Creating
--------

This operation is not supported.

Reading
-------

### Getting Child Media Objects

`GET /{ig-media-id}/children`

Returns a list of [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) objects on an album [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object.

#### Permissions

An [access token](https://developers.facebook.com/docs/instagram-api/overview#authentication) from a User who created the album [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object, with the following permissions:

* `instagram_basic`
* `pages_read_engagement` or `pages_show_list`

If the token is from a User whose **Page role was granted via the Business Manager**, one of the following permissions is also required:

* `ads_management`
* `pages_read_engagement`
* `business_management`

#### Limitations

* Some fields, such as `permalink`, cannot be used on photos within albums (children).

#### Sample Request

GET graph.facebook.com
  /17896450804038745/children

#### Sample Response

{
  "data": \[
    {
      "id": "17880997618081620"
    },
    {
      "id": "17871527143187462"
    }
  \]
}

Updating
--------

This operation is not supported.

Deleting
--------

This operation is not supported.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

Collaborators
=============

Represents a list of users who are added as collaborators on an IG Media object.

Creating
--------

This operation is not supported.

Reading
-------

Get a list of Instagram users as collaborators and their invitation status on an IG Media object.

**`GET /{ig-media-id}`**

### Limitations

* Up to 3 Instagram accounts can be added as collaborators
* Only IG users who have enabled collaborator tagging will be returned in the response
* Collaborators tagging supports Feed image, Reels and Carousel, Stories is not supported

### Requirements

| Type | Description |
| --- | --- |
| [Access Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) | [User](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) – User must have created the IG Media object |
| [Permissions](https://developers.facebook.com/docs/permissions) | [`instagram_basic`](https://developers.facebook.com/docs/permissions/reference/instagram_basic)  <br>[`pages_read_engagement`](https://developers.facebook.com/docs/permissions/reference/pages_read_engagement)  <br>[`pages_show_list`](https://developers.facebook.com/docs/permissions/reference/pages_show_list)<br><br>  <br><br>If the app user was granted a role on the Page via the Business Manager, you also need one of the following:<br><br>  <br><br>[`ads_management`](https://developers.facebook.com/docs/permissions/reference/ads_management)  <br>[`business_management`](https://developers.facebook.com/docs/permissions/reference/business_management) |

### Request syntax

GET https://graph.facebook.com/{appi-version}/{ig-media-id}/collaborators

### Sample Response

{
  "data": \[
    {
      "id": "90010775360791",
      "username": "realtest1",
      "invite\_status": "Accpeted"
    },
    {
      "id": "17841449208283139",
      "username": "realtest2",
      "invite\_status": "Pending"
    },
    {
      "id": "90011117049518",
      "username": "realtest3",
      "invite\_status": "Declined"
    }
  \]
}

### Path Parameters

| Placeholder | Value |
| --- | --- |
| `{api-version}` | API [version](https://developers.facebook.com/docs/graph-api/guides/versioning). |
| `{ig-user-id}` | **Required.** IG User ID. |

### Query String Parameters

| Key | Placeholder | Value |
| --- | --- | --- |
| `access_token` | `{access-token}` | **Required.** App user's [User](https://developers.facebook.com/docs/facebook-login/access-tokens/#usertokens) access token. |

### Response fields

| Field Name | Description |
| --- | --- |
| `id` | The App-scoped ID for the Instagram account of the potential collaborator |
| `invite_status` | The status for the invitation sent to a potential collaborator. Can be one of the following:<br><br>* `Accepted`<br>* `Declined`<br>* `Pending` |
| `username` | Instagram profile username for the potential collaborator |

Updating
--------

This operation is not supported.

Deleting
--------

This operation is not supported.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

Comments
========

Represents a collection of [IG Comments](https://developers.facebook.com/docs/instagram-api/reference/ig-comment) on an [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object.

### Non-Organic Comments

Comments on Ads containing IG Media (i.e. non-organic comments) are of a different type and are not supported. To get non-organic comments, use the [Marketing API](https://developers.facebook.com/docs/marketing-api/) and request the Ad's `effective_instagram_story_id`. You can then query the returned ID's `/comments` edge to get a collection of non-organic [Instagram Comments](https://developers.facebook.com/docs/graph-api/reference/instagram-comment/). Refer to the Marketing API's [Post Moderation](https://developers.facebook.com/docs/instagram/ads-api/guides/post-moderation) guide for more information.

Creating
--------

### Creating a Comment on a Media Object

`POST /{ig-media-id}/comments?message={message}`

Creates an [IG Comment](https://developers.facebook.com/docs/instagram-api/reference/ig-comment) on an [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object.

#### Limitations

Comments on live video IG Media are not supported.

#### Query String Parameters

Query string parameters are optional unless indicated as required.

* `{message}` (required) — The text to be included in the comment.

#### Permissions

An [access token](https://developers.facebook.com/docs/instagram-api/overview#authentication) from a User who created the [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object, with the following permissions:

* `instagram_basic`
* `instagram_manage_comments`
* `pages_show_list`
* `pages_read_engagement`

If the token is from a User whose **Page role was granted via the Business Manager**, one of the following permissions is also required:

* `ads_management`
* `pages_read_engagement`
* `business_management`

#### Sample Request

POST graph.facebook.com
  /17895695668004550/comments?message=This%20is%20awesome!

#### Sample Response

{
  "id": "17870913679156914"
}

Reading
-------

### Getting Comments on a Media Object

`GET /{ig-media-id}/comments`

Returns a list of [IG Comments](https://developers.facebook.com/docs/instagram-api/reference/ig-comment) on an [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object.

#### Limitations

* Requests made using API version 3.1 or older will have results returned in chronological order. Requests made using version 3.2+ will have results returned in reverse chronological order.
* Returns only top-level comments. Replies to comments are not included unless you use field expansion to request the `replies` field.
* Returns a maximum of 50 comments per query.

#### Permissions

An [access token](https://developers.facebook.com/docs/instagram-api/overview#authentication) from a User who created the [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object, with the following permissions:

* `instagram_basic`
* `pages_show_list`
* `pages_read_engagement`

If the token is from a User whose **Page role was granted via the Business Manager**, one of the following permissions is also required:

* `ads_management`
* `pages_read_engagement`
* `business_management`

#### Sample Request

GET graph.facebook.com
  /17895695668004550/comments

#### Sample Response

{
  "data": \[
    {
      "timestamp": "2017-08-31T19:16:02+0000",
      "text": "This is awesome!",
      "id": "17870913679156914"
    },
    {
      "timestamp": "2017-08-31T18:10:30+0000",
      "text": "\*Sniff\*",
      "id": "17873440459141021"
    }
  \]
}

Updating
--------

This operation is not supported.

Deleting
--------

This operation is not supported.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

IG Media Insights
=================

Represents social interaction metrics on an [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object.

Creating
--------

This operation is not supported.

Reading
-------

**`GET /{ig-media-id}/insights`**

Get insights data on an [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object.

### Limitations

* Insights data is not available for any media within an album [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media).
* Story media metrics are only available for 24 hours, even if the stories are archived or highlighted. To get the latest insights for a story before it expires, set up a [Webhook](https://developers.facebook.com/docs/instagram-api/guides/webhooks) for the `Instagram` topic and subscribe to the `story_insights` field.
* Story media metrics with values less than 5 return an error code `10` with the message `(#10) Not enough viewers for the media to show insights`.
* For Stories created by users in Europe and Japan, the `replies` metric now returns a value of `0`.
* For Stories, replies made by users in Europe and Japan are not included in `replies` calculations.
* If insights data you are requesting does not exist or is currently unavailable, the API returns an empty data set instead of `0` for individual metrics.
* Data used to calculate metrics can be delayed up to 48 hours.

### Requirements

| Type | Description |
| --- | --- |
| [Access Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) | [User](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) |
| [Permissions](https://developers.facebook.com/docs/apps/review/login-permissions) | [`instagram_basic`](https://developers.facebook.com/docs/facebook-login/permissions#reference-instagram_basic)  <br>[`instagram_manage_insights`](https://developers.facebook.com/docs/facebook-login/permissions#reference-instagram_manage_insights)  <br>[`pages_read_engagement`](https://developers.facebook.com/docs/facebook-login/permissions#reference-pages_read_engagement)  <br>[`pages_show_list`](https://developers.facebook.com/docs/facebook-login/permissions#reference-pages_show_list)<br><br>  <br><br>If the app user was granted a role on the Page via the Business Manager, you will also need one of:<br><br>  <br><br>[`ads_management`](https://developers.facebook.com/docs/permissions/reference/ads_management)  <br>[`business_management`](https://developers.facebook.com/docs/permissions/reference/business_management) |

### Request Syntax

GET https://graph.facebook.com/{api-version}/{ig-media-id}/insights
  ?metric={metric}
  &access\_token={access-token}

### Path Parameters

| Placeholder | Value |
| --- | --- |
| `{api-version}` | API [version](https://developers.facebook.com/docs/graph-api/guides/versioning). |
| `{ig-media-id}` | **Required.** IG Media ID. |

### Query String Parameters

| Parameter | Value |
| --- | --- |
| `{access-token}`<br><br>Type: string | **Required**. App user's [User access token](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens). |
| `{metric}`<br><br>Type: Comma-separated list | **Required**. Comma-separated list of [Metrics](#metrics) you want returned. |

### Metrics

Some of these metrics are deprecated for v18.0. They will be deprecated for all versions beginning Dec 11, 2023. Please use the alternative metrics listed.

`total_interactions`, which is listed as an alternative for some of the deprecated metrics, is currently only available using version 18.0 and does not work with older versions. When querying older versions before Dec 11, 2023, please use the `engagement` metric.

See the [Changelog](https://developers.facebook.com/docs/instagram-api/changelog) for more information.

#### Album Metrics

| Metric | Description |
| --- | --- |
| `carousel_album_engagement`  <br>_Deprecated for v18.0+_ | Total number of likes and [IG Comments](https://developers.facebook.com/docs/instagram-api/reference/ig-comment) on the album [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object.  <br>**Alternative metric:** `total_interactions` |
| `carousel_album_impressions`  <br>_Deprecated for v18.0+_ | Total number of times the album [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object has been seen.  <br>**Alternative metrics:** `impressions` |
| `carousel_album_reach`  <br>_Deprecated for v18.0+_ | Total number of unique Instagram accounts that have seen the album [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object.  <br>**Alternative metric:** `reach` |
| `carousel_album_saved`  <br>_Deprecated for v18.0+_ | Total number of unique Instagram accounts that have saved the album [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object.  <br>**Alternative metric:** `saved` |
| `carousel_album_video_views`  <br>_Deprecated for v18.0+_ | Total number of unique Instagram accounts that have viewed video [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) within the album.  <br>**Alternative metric:** `video_views` |

#### Photo and Video Metrics

Metrics on media within an album are not supported. Get metrics on the album instead.

| Metric | Description |
| --- | --- |
| `engagement`  <br>_Deprecated for v18.0+_ | Sum of [`likes_count`](https://developers.facebook.com/docs/instagram-api/reference/ig-media#fields), [`comment_count`](https://developers.facebook.com/docs/instagram-api/reference/ig-media#fields), and [`saved`](#metrics) counts on the [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media).  <br>**Alternative metric:** `total_interactions`  <br>**Note:** You may see different results. `engagement` includes likes, comments and saves count while `total_interactions` includes likes, comments, saved and shares count. |
| `impressions` | Total number of times the [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object has been seen. |
| `reach` | Total number of unique Instagram accounts that have seen the [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object. |
| `saved` | Total number of unique Instagram accounts that have saved the [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object. |
| `video_views` | Total number of times the video [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) has been seen. For album IG Media, the number of times all videos within the album have been seen. |

#### Reels Metrics

| Metric | Description |
| --- | --- |
| `comments` | Number of comments on the reel. Metric [in development](https://business.facebook.com/business/help/metrics-labeling). |
| `ig_reels_avg_watch_time` | The average amount of time spent playing the reel. Metric [in development](https://business.facebook.com/business/help/metrics-labeling). |
| `ig_reels_video_view_total_time` | The total amount of time the reel was played, including any time spent replaying the reel. Metric [in development](https://business.facebook.com/business/help/metrics-labeling). |
| `likes` | Number of likes on the reel. Metric [in development](https://business.facebook.com/business/help/metrics-labeling). |
| `plays` | Number of times the reels starts to play after an impression is already counted. This is defined as video sessions with 1 ms or more of playback and excludes replays. Metric [in development](https://business.facebook.com/business/help/metrics-labeling). |
| `reach` | Number of unique accounts that have seen the reel at least once. Reach is different from impressions, which can include multiple views of a reel by the same account. Metric is [estimated](https://business.facebook.com/business/help/metrics-labeling) and [in development](https://business.facebook.com/business/help/metrics-labeling). |
| `saved` | Number of saves of the reel. Metric [in development](https://business.facebook.com/business/help/metrics-labeling). |
| `shares` | Number of shares of the reel. Metric [in development](https://business.facebook.com/business/help/metrics-labeling). |
| `total_interactions` | Number of likes, saves, comments, and shares on the reel, minus the number of unlikes, unsaves, and deleted comments. Metric [in development](https://business.facebook.com/business/help/metrics-labeling). |

#### Story Metrics

| Metric | Description |
| --- | --- |
| `exits`  <br>_Deprecated for v18.0+_ | Total number of times someone exited the story [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object.  <br>**Alternative metric:** `navigation`  <br>**Breakdown:** `story_navigation_action_type` |
| `impressions` | Total number of times the story [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object has been seen. |
| `reach` | Total number of unique Instagram accounts that have seen the story [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object. |
| `replies` | Total number of replies ([IG Comments](https://developers.facebook.com/docs/instagram-api/reference/ig-comment)) on the story [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object. Value does not include replies made by users in some regions. These regions include: Europe starting December 1, 2020 and Japan starting April 14, 2021. If the Story was created by a user in one of these regions, returns a value of `0`. |
| `taps_forward`  <br>_Deprecated for v18.0+_ | Total number of taps to see this story [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object's next photo or video.  <br>**Alternative metric:** `navigation`  <br>**Breakdown:** `story_navigation_action_type` |
| `taps_back`  <br>_Deprecated for v18.0+_ | Total number of taps to see this story [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object's previous photo or video.  <br>**Alternative metric:** `navigation`  <br>**Breakdown:** `story_navigation_action_type` |

#### Sample Request

curl -X GET \\
  'https://graph.facebook.com/`v18.0`/17895695668004550/insights?metric=impressions,reach&access\_token=IGQVJ...'

#### Sample Response

{
  "data": \[
    {
      "name": "impressions",
      "period": "lifetime",
      "values": \[
        {
          "value": 264
        }
      \],
      "title": "Impressions",
      "description": "Total number of times the media object has been seen",
      "id": "17855590849148465/insights/impressions/lifetime"
    },
    {
      "name": "reach",
      "period": "lifetime",
      "values": \[
        {
          "value": 103
        }
      \],
      "title": "Reach",
      "description": "Total number of unique accounts that have seen the media object",
      "id": "17855590849148465/insights/reach/lifetime"
    }
  \]
}

New Metrics
-----------

The metrics listed below are new and will gradually be made available to all developers. These metrics will eventually replace the legacy metrics listed above. If you see this message you are able to use the new metrics described below.

### Request Syntax

GET https://graph.facebook.com/{api-version}/{ig-media-id}/insights
  ?metric={metric}
  &breakdown={breakdown}
  &access\_token={access-token}

### Path Parameters

| Placeholder | Value |
| --- | --- |
| `{api-version}` | API [version](https://developers.facebook.com/docs/graph-api/guides/versioning). |
| `{ig-media-id}` | **Required.** [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) ID. |

### Query String Parameters

| Key | Placeholder | Value |
| --- | --- | --- |
| `access_token` | `{access-token}` | **Required.** The app user's [User](https://developers.facebook.com/docs/facebook-login/guides/access-tokens#usertokens) access token. |
| `breakdown` | `{breakdown}` | Designates how to break down result set into subsets. See [Breakdown](#breakdown). |
| `metric` | `{metric}` | **Required.** Comma-separated list of [Metrics](#metrics) you want returned. |

### Breakdown

You can also specify one or more breakdowns, and the results will be broken down into smaller sets based on the specified breakdown. Values can be:

* `action_type` — Only compatible with the profile\_activity metric. Break down results by profile UI component that viewers tapped or clicked after viewing the app user's profile. Response values can be:
    * `BIO_LINK_CLICKED`
    * `CALL`
    * `DIRECTION`
    * `EMAIL`
    * `OTHER`
    * `TEXT`
* `story_navigation_action_type` — Break down results by navigation action taken by the viewer upon viewing the media.
    * `TAP_BACK`
    * `TAP_EXIT`
    * `TAP_FORWARD`
    * `SWIPE_FORWARD`

Refer to the [Metrics](#metrics) table to determine which metrics support breakdowns and which breakdowns they support. If you request a metric that doesn't support breakdowns, the API will return an error ("`An unknown error has occurred.`"), so be careful if requesting multiple metrics in a single query.

### Metrics

#### Post Metrics

The following metrics are available on image and video IG Media published as a Post. Album carousels and IGTV are not supported.

| Metric | Breakdown | Description |
| --- | --- | --- |
| `comments` | n/a | The number of comments on your post. |
| `follows` | n/a | The number of accounts that started following you. |
| `likes` | n/a | The number of likes on your post. |
| `profile_activity` | `action_type` | The number of actions people take when they visit your profile after engaging with your post. |
| `profile_visits` | n/a | The number of times your profile was visited. |
| `shares` | n/a | The number of shares of your post. |
| `total_interactions` | n/a | The number of likes, saves, comments and shares on your post minus the number of unlikes, unsaves and deleted comments. |

#### Story Metrics

The following metrics are available on IG Media published as a Story.

| Metric | Breakdown | Description |
| --- | --- | --- |
| `follows` | n/a | This is how many accounts started following you. |
| `navigation` | `story_navigation_action_type` | This is the total number of actions taken from your story. These are made up of metrics like exited, forward, back and next story. |
| `profile_activity` | `action_type` | The number of actions people take when they visit your profile after engaging with your story. |
| `profile_visits` | n/a | The number of times your profile was visited. |
| `shares` | n/a | The number of shares of your story. |
| `total_interactions` | n/a | The number of replies and shares for your story. |

### Response

A JSON object containing the results of your query. Results can include the following data, based on your query specifications:

{
  "data": \[
    {
      "name": "{name}",
      "period": "{period}",
      "values": \[
        {
          "value": {value}
        }
      \],
      "title": "{title}",
      "description": "{description}",
      "total\_value": {
        "value":{value},
        "breakdowns": \[
          {
            "dimension\_keys": \[
              "{dimension-key-1}",
              "{dimension-key-2}"
              ...
            \],
            "results": \[
              {
                "dimension\_values": \[
                  "dimension-value-1",
                  "dimension-value-2"
                  ...
                \],
                "value": {value}
              },
              ...
            \]
          }
        \]
      },
      "id": "{id}"
    }
  \]
}

### Response Contents

| Property | Value Type | Description |
| --- | --- | --- |
| `data` | Array | An array containing an object describing your request results. |
| `name` | String | [Metric](#metrics) name. |
| `period` | String | Period requested. Period is automatically set to `lifetime` in the request and cannot be changed, so this value will always be `lifetime`. |
| `values` | Array | An array containing an object describing requested [metric](#metrics) values. |
| `value` | Integer | For `data.values.value`, sum of requested [metric](#metrics) values.<br><br>  <br><br>For `data.total_value.value`, sum of requested [breakdown](#breakdown) values.<br><br>  <br><br>For `data.total_value.breakdowns.results.value`, sum of [breakdown](#breakdown) set values. |
| `title` | String | [Metric](#metrics) title. |
| `description` | String | [Metric](#metrics) description. |
| `id` | String | A string describing the query's path parameters. |
| `total_value` | Object | Object describing requested [breakdown](#breakdown) values (if breakdowns were requested). |
| `breakdowns` | Array | An array of objects describing the [breakdowns](#breakdown) requested and their results. |
| `dimension_keys` | Array | Array of strings describing [breakdowns](#breakdown) requested. |
| `results` | Array | An array of objects describing each [breakdown](#breakdown) set. |
| `dimension_values` | String | An array of strings describing [breakdown](#breakdown) set values. Values can be mapped to `dimension_keys`. |
| `paging` | Object | An object containing URLs used to request the next set of results. See [Paginated Results](https://developers.facebook.com/docs/instagram-api/reference/ig-media/docs/graph-api/results) for more information. |
| `previous` | String | URL to retrieve the previous page of results. See [Paginated Results](https://developers.facebook.com/docs/instagram-api/reference/ig-media/docs/graph-api/results) for more information. |
| `next` | String | URL to retrieve the next page of results. See [Paginated Results](https://developers.facebook.com/docs/instagram-api/reference/ig-media/docs/graph-api/results) for more information. |

### Sample Post Metric Request

curl -i -X GET \\
 "https://graph.facebook.com/`v18.0`/17932174733377207/insights?metric=profile\_activity&breakdown=action\_type&access\_token=EAAOc..."

### Sample Post Metric Response

{
  "data": \[
    {
      "name": "profile\_activity",
      "period": "lifetime",
      "values": \[
        {
          "value": 4
        }
      \],
      "title": "Profile activity",
      "description": "\[IG Insights\] This header is the name of a metric that appears on an educational info sheet for a particular post, story, video or promotion. This metric is the sum of all profile actions people take when they engage with this content.",
      "total\_value": {
        "value": 4,
        "breakdowns": \[
          {
            "dimension\_keys": \[
              "action\_type"
            \],
            "results": \[
              {
                "dimension\_values": \[
                  "email"
                \],
                "value": 1
              },
              {
                "dimension\_values": \[
                  "text"
                \],
                "value": 1
              },
              {
                "dimension\_values": \[
                  "direction"
                \],
                "value": 1
              },
              {
                "dimension\_values": \[
                  "bio\_link\_clicked"
                \],
                "value": 1
              }
            \]
          }
        \]
      },
      "id": "17932174733377207/insights/profile\_activity/lifetime"
    }
  \]
}

### Sample Story Metric Request

curl -i -X GET \\
 "https://graph.facebook.com/`v18.0`/17969782069736348/insights?metric=navigation&breakdown=story\_navigation\_action\_type&access\_token=EAAOc..."

### Sample Story Metric Response

{
  "data": \[
    {
      "name": "navigation",
      "period": "lifetime",
      "values": \[
        {
          "value": 25
        }
      \],
      "title": "Navigation",
      "description": "This is the total number of actions taken from your story. These are made up of metrics like exited, forward, back and next story.",
      "total\_value": {
        "value": 25,
        "breakdowns": \[
          {
            "dimension\_keys": \[
              "story\_navigation\_action\_type"
            \],
            "results": \[
              {
                "dimension\_values": \[
                  "tap\_forward"
                \],
                "value": 19
              },
              {
                "dimension\_values": \[
                  "tap\_back"
                \],
                "value": 4
              },
              {
                "dimension\_values": \[
                  "tap\_exit"
                \],
                "value": 1
              },
              {
                "dimension\_values": \[
                  "swipe\_forward"
                \],
                "value": 1
              }
            \]
          }
        \]
      },
      "id": "17969782069736348/insights/navigation/lifetime"
    }
  \]
}

Updating
--------

This operation is not supported.

Deleting
--------

This operation is not supported.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

IG Media Product Tags
=====================

Represents product tags on an [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media). See [Product Tagging](https://developers.facebook.com/docs/instagram-api/guides/product-tagging) guide for complete usage details.

Creating
--------

**`POST /{ig-media-id}/product_tags`**

Create or update product tags on an existing [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media).

### Limitations

* Instagram Creator accounts are not supported.
* Stories, Instagram TV, Live, and Mentions are not supported.
* Tagging media is additive until the 5 tag limit has been reached. If the targeted media has already been tagged by a product in the request, the old tag's `x` and `y` values will be updated with their new values (a new tag will not be added).

### Requirements

| Type | Requirement |
| --- | --- |
| [Access Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens/) | [User](https://developers.facebook.com/docs/facebook-login/access-tokens/#usertokens) |
| [Business Roles](https://www.facebook.com/business/help/442345745885606) | The app user must have an admin role on the [Business Manager](https://business.facebook.com/) that owns the IG User's [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322&h=AT1GgNey-1JfUCCuiLd0jrmBHvpHu02_Q_au1MUfCA6raN8ot1FQ4T7Nwus-Yxg2KvZbQXIaZNmFSO0hgmRpOg4rsh5mUNztbx9d5cwQ0z55dy6aj0C-F3W1l5-qIvyUb4JeVMBek9vX9_ee). |
| [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT138dnHtFGwotXoO8YIY8IOWIZOLMqMPQ27RtaFX0M3iU2EVXuv8zgSgSci6hzMsnnFcfoVUdo39KVmkAsKG-oS3bWaiWvRFT19Oyee2N6bgDHC2NtpEU0G9QcbUqwhJrp5zBNGD7VZW5qP) | The IG User that owns the IG Media must have an approved [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT0wwIMn9TvaHCCeU4P0TfyQq4x-LXoJgdcf7UhbXvJ6MWjuwv7EHxGnBuVLfvHMHecqk7fkWZWawtO1pfalf0CgumRxwaOupSTc-YLqkfu-sr_qKOf0AaVKs8LHpAHgmDkxdfZBuy5aGqQv) with a product catalog containing products. |
| [Permissions](https://developers.facebook.com/docs/permissions/reference) | [`catalog_management`](https://developers.facebook.com/docs/permissions/reference/catalog_management)  <br>[`instagram_basic`](https://developers.facebook.com/docs/permissions/reference/instagram_basic)  <br>[`instagram_shopping_tag_products`](https://developers.facebook.com/docs/permissions/reference/instagram_shopping_tag_products)  <br>[`pages_show_list`](https://developers.facebook.com/docs/permissions/reference/pages_show_list)<br><br>  <br><br>If the app user was granted a role via the Business Manager on the [Page](https://developers.facebook.com/docs/instagram-api/overview#pages) connected to the targeted IG User, you will also need one of:<br><br>  <br><br>[`ads_management`](https://developers.facebook.com/docs/permissions/reference/ads_management)  <br>[`business_management`](https://developers.facebook.com/docs/permissions/reference/business_management) |

### Request Syntax

POST https://graph.facebook.com/{api-version}/{ig-media-id}/product\_tags
  ?updated\_tags={updated-tags}
  &access\_token={access-token}

### Path Parameters

| Placeholder | Value |
| --- | --- |
| `{api-version}` | API [version](https://developers.facebook.com/docs/instagram-basic-display-api/overview#versions). |
| `{ig-media-id}` | **Required.** IG Media ID. |

### Query String Parameters

| Key | Placeholder | Value |
| --- | --- | --- |
| `access_token` | `{access-token}` | **Required.** App user's [User](https://developers.facebook.com/docs/facebook-login/access-tokens/#usertokens) access token. |
| `updated_tags` | `{updated-tags}` | **Required. Applies only to images and videos**. An array of objects specifying which product tags to tag the image or video with (maximum of 5; tags and product IDs must be unique). Each object should have the following information:<br><br>  <br><br>* `product_id` — **Required.** Product ID.<br>* `x` — **Images only.** An optional float that indicates percentage distance from left edge of the published media image. Value must be within `0.0`–`1.0` range.<br>* `y` — **Images only.** An optional float that indicates percentage distance from top edge of the published media image. Value must be within `0.0`–`1.0` range.<br><br>For example:<br><br>  <br><br>`[{product_id:'3231775643511089',x:0.5,y:0.8}]` |

### Response

An object indicating success or failure.

{
  "success": {success}
}

#### Response Contents

| Property | Value |
| --- | --- |
| `success` | Returns `true` if able to update the [IG Media's](https://developers.facebook.com/docs/instagram-api/reference/ig-media) product tags, otherwise returns `false`. |

### cURL Example

#### Request

curl -i -X POST \\
 "https://graph.facebook.com/`v18.0`/90010778325754/product\_tags?updated\_tags=%5B%0A%20%20%7B%0A%20%20%20%20product\_id%3A'3859448974125379'%2C%0A%20%20%20%20x%3A%200.5%2C%0A%20%20%20%20y%3A%200.8%0A%20%20%7D%0A%5D&access\_token=EAAOc..."

For reference, here is the HTML-decoded POST payload string:

https://graph.facebook.com/`v18.0`/90010778325754/product\_tags?updated\_tags=\[
  {
    product\_id:'3859448974125379',
    x: 0.5,
    y: 0.8
  }
\]&access\_token=EAAOc...

#### Response

{
  "success": true
}

Reading
-------

**`GET /{ig-media-id}/product_tags`**

Get a collection of product tags on an [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media). See the [Product Tagging](https://developers.facebook.com/docs/instagram-api/guides/product-tagging) guide for complete product tagging steps.

### Limitations

* Instagram Creator accounts are not supported.
* Stories, Instagram TV, Reels, Live, and Mentions are not supported.

### Requirements

| Type | Requirement |
| --- | --- |
| [Access Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens/) | [User](https://developers.facebook.com/docs/facebook-login/access-tokens/#usertokens) |
| [Business Roles](https://www.facebook.com/business/help/442345745885606) | The app user must have an admin role on the [Business Manager](https://business.facebook.com/) that owns the IG User's [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322&h=AT1rEZAyM7zCWl5oPs8qYCrpuQDkKppRONYBHFJay3cKx611DwwKVPoBZOWrJu77vVE-7CMnW6L34U_fBdM1o97x2oNJMOzy4jn501Swar7DLSt8nua-KdAtuv1uNJFa5eIk3Glfa_on9XDPtzEc9X-qa5X4LA). |
| [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT0_cyu9sORFFwCXju_cQXCkgTqbrXCesBxoqjI098ozOzz5_QkhSFUHmnLuUlGTjyN2S3Yi3UEWLTnHVMVFbd5NLKjqk-bXnNWHjQLesrmAX2zW8C6jqq1BCvJtahn0QR-B12l72OYj7PLE) | The IG User that owns the IG Media must have an approved [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT08UaTJqLRBjXGlE_Yf85j1NJ_vI5dDCXuMIwfyEnCu1FLz3gMA8y4rHchdsBgqw0rbbgvKk9cgO6yOhiv0NYs8PGcWRzFx6DRZ2pFLCjpYNYmQaBqMaU7ABHqHUhYD8ii8jEkx-KkpB1pp) with a product catalog containing products. |
| [Permissions](https://developers.facebook.com/docs/permissions/reference) | [`catalog_management`](https://developers.facebook.com/docs/permissions/reference/catalog_management)  <br>[`instagram_basic`](https://developers.facebook.com/docs/permissions/reference/instagram_basic)  <br>[`instagram_shopping_tag_products`](https://developers.facebook.com/docs/permissions/reference/instagram_shopping_tag_products)  <br>[`pages_show_list`](https://developers.facebook.com/docs/permissions/reference/pages_show_list)<br><br>  <br><br>If the app user was granted a role via the Business Manager on the [Page](https://developers.facebook.com/docs/instagram-api/overview#pages) connected to the targeted IG User, you will also need one of:<br><br>  <br><br>[`ads_management`](https://developers.facebook.com/docs/permissions/reference/ads_management)  <br>[`business_management`](https://developers.facebook.com/docs/permissions/reference/business_management) |

### Request Syntax

GET https://graph.facebook.com/{api-version}/{ig-media-id}/product\_tags
  ?access\_token={access-token}

### Path Parameters

| Placeholder | Value |
| --- | --- |
| `{api-version}` | API [version](https://developers.facebook.com/docs/instagram-basic-display-api/overview#versions). |
| `{ig-media-id}` | **Required.** IG Media ID. |

### Query String Parameters

| Key | Placeholder | Value |
| --- | --- | --- |
| `access_token` | `{access-token}` | **Required.** App user's [User](https://developers.facebook.com/docs/facebook-login/access-tokens/#usertokens) access token. |

### Response

A JSON-formatted object containing an array of product tags on an IG Media. Responses can include the following product tag fields:

{
  "data": \[
    {
      "product\_id": {product-id},
      "merchant\_id": {merchant-id},
      "name": "{name}",
      "price\_string": "{price-string}",
      "image\_url": "{image-url}",
      "review\_status": "{review-status}",
      "is\_checkout": {is-checkout},
      "stripped\_price\_string": "{stripped-price-string}",
      "string\_sale\_price\_string": "{string-sale-price-string}",
      "x": {x},
      "y": {y}
    }
  \]
}

#### Response Contents

| Property | Value |
| --- | --- |
| `product_id` | Product ID. |
| `merchant_id` | Merchant ID. |
| `name` | Product name. |
| `price_string` | Price string. |
| `image_url` | Product image URL. |
| `review_status` | Product review status. Values can be:<br><br>  <br><br>* `approved` — Product is approved.<br>* `rejected` — Product was rejected<br>* `pending` — Still undergoing review.<br>* `outdated` — Product was approved but has been edited and requires reapproval.<br>* `""` — No review status. |
| `is_checkout` | If `true`, product can be purchased directly through the Instagram app. If `false`, product can only be purchased on the merchant's website. |
| `stripped_price_string` | Product short price string (price displayed in constrained spaces, such as `$100` instead of `100 USD`). |
| `string_sale_price_string` | Product sale price. |
| `x` | A float that indicates percentage distance from left edge of media image. Value within `0.0`–`1.0` range. |
| `y` | A float that indicates percentage distance from top edge of media image. Value within `0.0`–`1.0` range. |

### cURL Example

#### Request

curl -i -X GET \\
 "https://graph.facebook.com/`v18.0`/90010778325754/product\_tags?access\_token=EAAOc..."

#### Response

{
  "data": \[
    {
      "product\_id": 3231775643511089,
      "merchant\_id": 90010177253934,
      "name": "Gummy Bears",
      "price\_string": "$3.50",
      "image\_url": "https://scont...",
      "review\_status": "approved",
      "is\_checkout": true,
      "stripped\_price\_string": "$3.50",
      "stripped\_sale\_price\_string": "$3",
      "x": 0.5,
      "y": 0.80000001192093
    }
  \]
}

Updating
--------

See [Creating](#creating).

Deleting
--------

**`DELETE /{ig-media-id}/product_tags`**

Delete product tags on an existing [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media).

### Limitations

* Instagram Creator accounts are not supported.
* Stories, Instagram TV, Reels, Live, and Mentions are not supported.

### Requirements

| Type | Requirement |
| --- | --- |
| [Access Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens/) | [User](https://developers.facebook.com/docs/facebook-login/access-tokens/#usertokens) |
| [Business Roles](https://www.facebook.com/business/help/442345745885606) | The app user must have an admin role on the [Business Manager](https://business.facebook.com/) that owns the IG User's [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322&h=AT1LKcr8EdSIpjXsaQ3jBneB__KJLKaW3CNa2E2jtYT2r6A7OyiH4__-WERJBaAQvkcguObcxBMKSpOv-vk-oDsoGj3EvBEpYmaiKP7y3aDyqjophqC9FRAVxYFRL2o0kkuUsBx7gNSEWzFh5Uzf3hmmVjxHig). |
| [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT2HXe7yl5DK3oY5ts4cb_bCgVI0i_S08Pa-VU7twdSNq5_Ck0ebcKEtdr_tz47wSzFPIpBQ_19UBOdcw5gJqjxtdeANfsaYt9SFu_3FbgGqwh1o-rZVf39Cuhxbdd8-IjVyW3KhXONxItSA) | The IG User that owns the IG Media must have an approved [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT2CpTGd35e7kFok6J6H0Z5GvGMq6xUqksCckzREFl7dOQFm-s0izSmVvNSQF5nNS5sySeq5OmqAYse9Ae75r7CQVRHcjD3f0shQWGBcaiwEPASOu8jGBS_Dc9yTGe9qDQgygVc7twBJiCGY) with a product catalog containing products. |
| [Permissions](https://developers.facebook.com/docs/permissions/reference) | [`catalog_management`](https://developers.facebook.com/docs/permissions/reference/catalog_management)  <br>[`instagram_basic`](https://developers.facebook.com/docs/permissions/reference/instagram_basic)  <br>[`instagram_shopping_tag_products`](https://developers.facebook.com/docs/permissions/reference/instagram_shopping_tag_products)  <br>[`pages_show_list`](https://developers.facebook.com/docs/permissions/reference/pages_show_list)<br><br>  <br><br>If the app user was granted a role via the Business Manager on the [Page](https://developers.facebook.com/docs/instagram-api/overview#pages) connected to the targeted IG User, you will also need one of:<br><br>  <br><br>[`ads_management`](https://developers.facebook.com/docs/permissions/reference/ads_management)  <br>[`business_management`](https://developers.facebook.com/docs/permissions/reference/business_management) |

### Request Syntax

DELETE https://graph.facebook.com/{api-version}/{ig-media-id}/product\_tags
  ?deleted\_tags={deleted-tags}
  &access\_token={access-token}

### Path Parameters

| Placeholder | Value |
| --- | --- |
| `{api-version}` | API [version](https://developers.facebook.com/docs/instagram-basic-display-api/overview#versions). |
| `{ig-media-id}` | **Required.** IG Media ID. |

### Query String Parameters

| Key | Placeholder | Value |
| --- | --- | --- |
| `access_token` | `{access-token}` | **Required.** App user's [User](https://developers.facebook.com/docs/facebook-login/access-tokens/#usertokens) access token. |
| `deleted_tags` | `{deleted-tags}` | **Required.** An array containing the following information for each product tag to be deleted<br><br>  <br><br>* `merchant_id` — **Required.** Merchant ID.<br>* `product_id` — **Required.** Product ID. |

### Response

An object indicating success or failure.

{
  "success": {success}
}

#### Response Contents

| Property | Value |
| --- | --- |
| `success` | Returns `true` if able to delete the specified product tags on the [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media), otherwise returns `false`. |

### cURL Example

#### Request

curl -i -X DELETE \\
  "https://graph.facebook.com/`v18.0`/90010778325754/product\_tags?deleted\_tags=%5B%0A%20%20%7B%0A%20%20%20%20product\_id%3A'3859448974125379'%2C%0A%20%20%20%20merchant\_id%3A'90010177253934'%0A%20%20%7D%0A%5D&access\_token=EAAOc..."

For reference, here is the HTML-decoded POST payload string:

https://graph.facebook.com/v12.0/90010778325754/product\_tags?deleted\_tags=\[
  {
    product\_id:'3859448974125379',
    merchant\_id:'90010177253934'
  }
\]&access\_token=EAAOc...

#### Response

{
  "success": true
}

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

IG User
=======

Represents an [Instagram Business Account](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F502981923235522&h=AT24nIIIt6NM9ANQSdD9lADwOviWIF73vg3bhGrs0k1WdkEBWCBYaU9gRiEW9dhdh2v_Kupv8F3L49HLDR7ui1M_7DO6ZkwCt2-SGPtM0hwQ-LU3QCgHNT-QcB8B-d4J508_--lK7VtuR-fHU9Xi1VC3Bj7cSw) or an [Instagram Creator Account](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1158274571010880&h=AT2lvRfLEeizHGXkDygRdMRcPGN-Gl_u-OvqJDUICIGVdNT6OM9XPFHZC_4qdvk69BTCr73FwilyxL-npRIKbKp0FkgYRtfeVz88Dz6WkRqbWpOl70izbdB56QJTMgyWnovyNr0xnJ3vyKe4).

Creating
--------

This operation is not supported.

Reading
-------

**`GET /{ig-user-id}`**

Get fields and edges on an Instagram Business or Creator Account.

### Requirements

| Type | Description |
| --- | --- |
| [Access Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) | [User](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens). |
| [Business Roles](https://www.facebook.com/business/help/442345745885606) | If you are requesting the `shopping_product_tag_eligibility` field for [product tagging](https://developers.facebook.com/docs/instagram-api/guides/product-tagging), the app user must have an admin role on the [Business Manager](https://business.facebook.com/) that owns the IG User's [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322&h=AT0pTIalEgnyzpvxq9FUfZpb-p2Qsdd3SR2_lEAo_WrMt0W3itJXTicBgZ7R0AdTh_dOwmWEMkw7XW8ggpTNVqH3N-PXUwumKtFHqczJNSUIEadHE0oefkK78Zz45ufzeHyNb_EQ1C7-ikkf). |
| [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT1_Iz5ZE7ylJakBv1JWTl07HE_Ptg9RCxIyXIi8-dlZBL7BZVUKhlcU7F7OqoAUHTZ7_4xcCLCxZ1cvvPzq0LlWUIouhFFuMKB9AkpcVDqOvoynES2s_hwwf6KavecfbzYQui8-J1pT_7la) | If you are requesting the `shopping_product_tag_eligibility` field for [product tagging](https://developers.facebook.com/docs/instagram-api/guides/product-tagging), the IG User must have an approved [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT0sRLslEqXDbc2f_UijZVLJ4J7ywUBtIR4b2u0_1tJYh_1C5VwBEVAwr-1MWDwhmcylx-UsL0SB6G7cUPcsTr3f5zwuwkYe4OP4C7vxJD6ScLzSXjX6Znt8g_oKzS1-pYJt55vCZ_fJbe08) with a product catalog containing products. |
| [Permissions](https://developers.facebook.com/docs/apps/review/login-permissions) | [`instagram_basic`](https://developers.facebook.com/docs/permissions/reference/instagram_basic)  <br>[`pages_read_engagement`](https://developers.facebook.com/docs/permissions/reference/pages_read_engagement)  <br>[`pages_show_list`](https://developers.facebook.com/docs/permissions/reference/pages_show_list)<br><br>  <br><br>If the app user was granted a role on the Page via the Business Manager, you also need one of the following:<br><br>  <br><br>[`ads_management`](https://developers.facebook.com/docs/permissions/reference/ads_management)  <br>[`business_management`](https://developers.facebook.com/docs/permissions/reference/business_management)<br><br>  <br><br>If you are requesting the `shopping_product_tag_eligibility` field for [product tagging](https://developers.facebook.com/docs/instagram-api/guides/product-tagging), you will also need:<br><br>  <br><br>[`catalog_management`](https://developers.facebook.com/docs/permissions/reference/catalog_management)  <br>[`instagram_shopping_tag_products`](https://developers.facebook.com/docs/permissions/reference/instagram_shopping_tag_products) |

### Request Syntax

GET https://graph.facebook.com/{api-version}/{ig-user-id}
  ?fields={fields}
  &access\_token={access-token}

### Path Parameters

| Placeholder | Value |
| --- | --- |
| `{api-version}` | API [version](https://developers.facebook.com/docs/graph-api/guides/versioning). |
| `{ig-user-id}` | **Required.** IG User ID. |

### Query String Parameters

| Key | Placeholder | Value |
| --- | --- | --- |
| `access_token` | `{access-token}` | **Required.** App user's [User](https://developers.facebook.com/docs/facebook-login/access-tokens/#usertokens) access token. |
| `fields` | `{fields}` | Comma-separated list of IG User [fields](#fields) you want returned for each IG User in the result set. |

### Fields

Public fields can be returned by an edge using field expansion.

| Field Name | Description |
| --- | --- |
| `biography`  <br>Public | Profile bio text. |
| `id`  <br>Public | App-scoped User ID. |
| `ig_id` | Instagram User ID. Used with Legacy Instagram API, now deprecated. Use `id` instead. |
| `followers_count`  <br>Public | Total number of Instagram users following the user. |
| `follows_count` | Total number of Instagram users the user follows. |
| `media_count`  <br>Public | Total number of [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) published on the user. |
| `name` | Profile name. |
| `profile_picture_url` | Profile picture URL. |
| `shopping_product_tag_eligibility` | Returns `true` if the app user has set up an [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT0jX3E0PMRG44gUWEUTT9uJ9XAo2eoSUocnJmLveGSJ9hDpVy4uJiF-8Oi2RavQGtZUGUaNCJ8ojcDHkq3WyBL2vN4kBXGkYuOGESrxbVZd96YeFsazyjUPwz9DTedBYRnP86oBYjfNEUd5) and is therefore eligible for product tagging, otherwise returns `false`. |
| `username`  <br>Public | Profile username. |
| `website`  <br>Public | Single profile website URL. |

### Edges

| Edge | Description |
| --- | --- |
| [`business_discovery`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/business_discovery) | Get data about other Instagram Business or Instagram Creator [IG Users](https://developers.facebook.com/docs/instagram-api/reference/ig-user). |
| [`content_publishing_limit`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/content_publishing_limit) | Represents an [IG User's](https://developers.facebook.com/docs/instagram-api/reference/ig-user) current [content publishing](https://developers.facebook.com/docs/instagram-api/guides/content-publishing) usage. |
| [`insights`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/insights) | Represents social interaction metrics on an [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user). |
| [`live_media`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/live_media) | Represents a collection of live video [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) on an [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user). |
| [`media`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media) | Represents a collection of [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) on an [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user). |
| [`media_publish`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media_publish) | Publish an [IG Container](https://developers.facebook.com/docs/instagram-api/reference/ig-container) on an Instagram Business [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user). |
| [`mentions`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/mentions) | Create an [IG Comment](https://developers.facebook.com/docs/instagram-api/reference/ig-comment) on an IG Comment or captioned [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) that an [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) has been @mentioned in by another Instagram user. |
| [`mentioned_comment`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/mentioned_comment) | Get data on an [IG Comment](https://developers.facebook.com/docs/instagram-api/reference/ig-comment) in which an [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) has been @mentioned by another Instagram user. |
| [`mentioned_media`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/mentioned_media) | Get data on an [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) in which an [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) has been @mentioned in a caption by another Instagram user. |
| [`recently_searched_hashtags`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/recently_searched_hashtags) | Get [IG Hashtags](https://developers.facebook.com/docs/instagram-api/reference/ig-hashtag) that an [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) has searched for within the last 7 days. |
| [`stories`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/stories) | Represents a collection of story [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) objects on an [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user). |
| [`tags`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/tags) | Represents a collection of [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) in which an [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) has been tagged by another Instagram user. |

### Response

A JSON-formatted object containing default and requested [fields](#fields) and [edges](#edges).

{
  "{field}":"{value}",
  ...
}

### cURL Example

#### Request

curl -X GET \\
  'https://graph.facebook.com/`v18.0`/17841405822304914?fields=biography%2Cid%2Cusername%2Cwebsite&access\_token=EAACwX...'

#### Response

{
  "biography": "Dino data crunching app",
  "id": "17841405822304914",
  "username": "metricsaurus",
  "website": "http://www.metricsaurus.com/"
}

Updating
--------

This operation is not supported.

Deleting
--------

This operation is not supported.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

IG User Available Catalogs
==========================

Represents a collection of product catalogs in an [IG User's](https://developers.facebook.com/docs/instagram-api/reference/ig-user) [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT2OYgz_XTBZ4JnkL7VOZDs3nvm0XgcIFqDFlhi3U53StZkkAPZca5qUG8porwNRgP8FDZjR18IU6ucriOpR1gEav6njXCr8osLaSogJrLCn48JOYaBofZzcGoJqP_3EVF0HM-5LKS5WWjzn). See [Product Tagging](https://developers.facebook.com/docs/instagram-api/guides/product-tagging) guide for complete usage details.

Creating
--------

This operation is not supported.

Reading
-------

**`GET /{ig-user-id}/available_catalogs`**

Get the product catalog in an [IG User's](https://developers.facebook.com/docs/instagram-api/reference/ig-user) [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT2jYKMX-vriDz2pMelUquOYyW5bkK-dMNR5nQ-i4I0GEdpNfUbplVd71c7OEgruJwvRIZuFzTyUsJ0kIPYaIjqaNeO6lXghHu5xABuRFzFAb9YmF-6O0XAtySl8pFlP4RvmpZEHRS5GgINo).

### Limitations

* Instagram Creator accounts are not supported.
* Stories, Instagram TV, Reels, Live, and Mentions are not supported.
* Only returns data on a single catalog because Instagram Shops are limited to a single catalog.
* Collaborative catalogs (shopping partner or affiliate creator catalogs) are not supported.

### Requirements

| Type | Requirement |
| --- | --- |
| [Access Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens/) | [User](https://developers.facebook.com/docs/facebook-login/access-tokens/#usertokens) |
| [Business Roles](https://www.facebook.com/business/help/442345745885606) | The app user must have an admin role on the [Business Manager](https://business.facebook.com/) that owns the IG User's [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322&h=AT3zbkRIT5UXPgJwyiuJfLSxVoxkPViEFBvHwVKpBr8Jf-S5zmMOtZHRP2vOwGMk6qroUYZ3lZCUBtVxsUzEko81RHl3ubFKe-0AIWeyg96d37yeG8SpuAoidm9Wc6NADVs_xE9v0QNTLkdj). |
| [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT06KPYTEJGpegdzFydHDCKMzy04fQ_I3-OgvWKTVLV5UdCt7BbIdqTQAQoYUDVTzUuvQ-L7-ZGkZhhTlurcjwZrR3pbn5GiyPVEAIkIRaWHl1fo9jus-vzxZ3LW7w8UeduqJWcNWC0HbkD1q2MgdiJCTjiBSg) | The IG User must have an approved [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT012JUqzilVdEgXqY7_5KDS2HimIoeWboUaT_kE0FwUIQa2S-dViKkIZCLiboYms3v6ob-3_aaQR2Rv6ZIk57vo9Zf2_ikNFPIQXUcpKfwWIp3II0hlI3pedVgPqOmnGAroCeXMBQGweyT4) with a product catalog containing products. |
| [Permissions](https://developers.facebook.com/docs/permissions/reference) | [`catalog_management`](https://developers.facebook.com/docs/permissions/reference/catalog_management)  <br>[`instagram_basic`](https://developers.facebook.com/docs/permissions/reference/instagram_basic)  <br>[`instagram_shopping_tag_products`](https://developers.facebook.com/docs/permissions/reference/instagram_shopping_tag_products)  <br>[`pages_show_list`](https://developers.facebook.com/docs/permissions/reference/pages_show_list)<br><br>  <br><br>If the app user was granted a role via the Business Manager on the [Page](https://developers.facebook.com/docs/instagram-api/overview#pages) connected to the targeted IG User, you will also need one of:<br><br>  <br><br>[`ads_management`](https://developers.facebook.com/docs/permissions/reference/ads_management)  <br>[`business_management`](https://developers.facebook.com/docs/permissions/reference/business_management) |

### Request Syntax

GET https://graph.facebook.com/{api-version}/{ig-user-id}/available\_catalogs
  ?fields={fields}
  &access\_token={access-token}

### Path Parameters

| Placeholder | Value |
| --- | --- |
| `{api-version}` | API [version](https://developers.facebook.com/docs/instagram-basic-display-api/overview#versions). |
| `{ig-user-id}` | **Required.** App user's app-scoped user ID. |

### Query String Parameters

| Key | Placeholder | Value |
| --- | --- | --- |
| `access_token` | `{access-token}` | **Required.** App user's [User](https://developers.facebook.com/docs/facebook-login/access-tokens/#usertokens) access token. |
| `fields` | `{fields}` | Comma-separated list of catalog [fields](#fields) you want returned for each catalog in the result set. |

### Response

A JSON-formatted object containing the data you requested.

{
  "data": \[
    {
      "catalog\_id": "{catalog-id}",
      "catalog\_name": "{catalog-name}",
      "shop\_name": "{shop-name}",
      "product\_count": {product-count}
    }
  \]
}

#### Response Contents

| Property | Value |
| --- | --- |
| `catalog_id` | Catalog ID. |
| `catalog_name` | Catalog name. |
| `shop_name` | Shop name. |
| `product_count` | Number of products in catalog. Includes all products regardless of review status. |

### cURL Example

#### Request

curl -i -X GET \\
 "https://graph.facebook.com/`v18.0`/90010177253934/available\_catalogs?access\_token=EAAOc..."

#### Response

{
  "data": \[
    {
      "catalog\_id": "960179311066902",
      "catalog\_name": "Jay's Favorite Snacks",
      "shop\_name": "Jay's Bespoke",
      "product\_count": 11
    }
  \]
}

Updating
--------

This operation is not supported.

Deleting
--------

This operation is not supported.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

IG User Business Discovery
==========================

Allows you to get data about other Instagram Business or Creator [IG Users](https://developers.facebook.com/docs/instagram-api/reference/ig-user).

Creating
--------

This operation is not supported.

Reading
-------

**`GET /{ig-user-id}?fields=business_discovery.username({username})`**

Returns data about another Instagram Business or Creator [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user). Perform this request on the Instagram Business or Creator [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) who is making the query, and identify the targeted business with the `username` parameter.

### Limitations

Data about age-gated Instagram Business [IG Users](https://developers.facebook.com/docs/instagram-api/reference/ig-user) will not be returned.

### Query String Parameters

* `{username}` (required) — The username of the Instagram Business or Creator [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) you want to get data about.

### Permissions

A Facebook User [access token](https://developers.facebook.com/docs/instagram-api/overview#authentication) with the following permissions:

* `instagram_basic`
* `instagram_manage_insights`
* `pages_read_engagement` or `pages_show_list`

If the token is from a User whose **Page role was granted via the Business Manager**, one of the following permissions is also required:

* `ads_management`
* `pages_read_engagement`
* `business_management`

### Field Expansion

You can use field expansion get public fields on the targeted [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user). Refer to the [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) reference for a list of public fields.

### Sample Request with Field Expansion

Getting data about the Instagram Business [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) "Blue Bottle Coffee" and using field expansion to request its followers and media counts.

GET graph.facebook.com
  /17841405309211844
    ?fields=business\_discovery.username(bluebottle){followers\_count,media\_count}

### Sample Response

{
  "business\_discovery": {
    "followers\_count": 267788,
    "media\_count": 1205,
    "id": "17841401441775531"
  },
  "id": "17841405309211844"
}

### Accessing Edges with Field Expansion

You can also use field expansion to access the `/media` edge on the targeted [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) and specify the fields and metrics that should be returned for each [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object. Refer to the [Media node reference](https://developers.facebook.com/docs/instagram-api/reference/ig-media) for a list of public fields.

**v10.0 and older calls until September 7, 2021:** The [`like_count`](https://developers.facebook.com/docs/instagram-api/reference/ig-media#fields) field on an IG Media will return `0` if the media [owner](https://developers.facebook.com/docs/instagram-api/overview#authorization) has [hidden](https://www.facebook.com/help/instagram/113355287252104) like counts on it.

**v11.0+ calls, and all versions on September 7, 2021:** If indirectly querying an [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) through another endpoint or field expansion, the [`like_count`](https://developers.facebook.com/docs/instagram-api/reference/ig-media#fields) field will be omitted from API responses if the media owner has hidden like counts on it. Directly querying the IG Media (which can only be done by the IG Media owner) will return the actual like count, however, even if like counts have been hidden.

### Sample Request with Edge

GET graph.facebook.com
  /17841405309211844
    ?fields=business\_discovery.username(bluebottle){followers\_count,media\_count,media}

### Sample Response with Edge

{
  "business\_discovery": {
    "followers\_count": 267788,
    "media\_count": 1205,
    "media": {
      "data": \[
        {
          "id": "17858843269216389"
        },
        {
          "id": "17894036119131554"
        },
        {
          "id": "17894449363137701"
        },
        {
          "id": "17844278716241265"
        },
        {
          "id": "17911489846004508"
        }
      \],
    },
    "id": "17841401441775531"
  },
  "id": "17841405309211844"
}

### Pagination

The `/media` edge supports [cursor-based pagination](https://developers.facebook.com/docs/graph-api/using-graph-api#paging), so when accessing it via field expansion, the response will include `before` and `after` cursors if the response contains multiple pages of data. Unlike standard cursor-based pagination, however, the response will not include `previous` or `next` fields, so you will have to use the `before` and `after` cursors to construct `previous` and `next` query strings manually in order to page through the returned data set.

### Sample Request

GET graph.facebook.com
  /17841405309211844
    ?fields=business\_discovery.username(bluebottle){media{comments\_count,like\_count}}

### Sample Response

{
  "business\_discovery": {
    "media": {
      "data": \[
        {
          "comments\_count": 50,
          "like\_count": 5837,
          "id": "17858843269216389"
        },
        {
          "comments\_count": 11,
          "like\_count": 2997,
          "id": "17894036119131554"
        },
        {
          "comments\_count": 28,
          "like\_count": 3643,
          "id": "17894449363137701"
        },
        {
          "comments\_count": 43,
          "like\_count": 4943,
          "id": "17844278716241265"
        },
     \],
   },
   "id": "17841401441775531"
  },
  "id": "17841405976406927"
}

Updating
--------

This operation is not supported.

Deleting
--------

This operation is not supported.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

IG User Catalog Product Search
==============================

Represents products and product variants that match a given search string in an [IG User's](https://developers.facebook.com/docs/instagram-api/reference/ig-user) [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT0AC54TfJ-oQieA9xPaEy4BHjqDss_TaDC_66s4_qetLIKTfGOcDXYn7X3eaNQfWhF1i5XbFgGk_b_v9lwid_WvNgCUSyTjCVWHE6EyfN-KDE_5CuKNvJclafEVYm3EjpC7VnUT-1xaBFpj) product catalog. See [Product Tagging](https://developers.facebook.com/docs/instagram-api/guides/product-tagging) guide for complete usage details.

Creating
--------

This operation is not supported.

Reading
-------

**`GET /{ig-user-id}/catalog_product_search`**

Get a collection of products that match a given search string within the targeted [IG User's](https://developers.facebook.com/docs/instagram-api/reference/ig-user) [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT0TrqR5PwLy78Cd-Ti8VIHI8s7p8gdTgF6h2ix8FHuXsPC0NCQhaXwRkKWuT06-jIDDRVUMWfqr6JO94NHcbRldH3ek9-r8Xnw-y3tbYX4lkez8ehXAyhUM6sJ7D9nJO96j-2a7XP52VOCT) catalog.

### Limitations

* Instagram Creator accounts are not supported.
* Stories, Instagram TV, Reels, Live, and Mentions are not supported.
* Products with a `review_status` of `rejected` will be returned, however, IG Media cannot be tagged with rejected products.
* Although the API will not return an error when publishing a post tagged with an unapproved product, the tag will not appear on the published post until the product has been approved. Therefore, we recommend that you only allow your app users to publish posts with tags whose products have a `review_status` of `approved`. This field is returned for each product by default when you get an app user's eligible products.

### Requirements

| Type | Requirement |
| --- | --- |
| [Access Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens/) | [User](https://developers.facebook.com/docs/facebook-login/access-tokens/#usertokens) |
| [Business Roles](https://www.facebook.com/business/help/442345745885606) | The app user must have an admin role on the [Business Manager](https://business.facebook.com/) that owns the IG User's [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322&h=AT0pXTBBoRJoFeS2QvVGXGsc8y99ApgfiWu4P8g52t4SpCN8RnmONqImTp8R87bicpfyw929daC07mgr-mwWEWK5gqBUIM_n4UWtI-ItxHBw4BX-2dwq4qRZwmqhGHkWjC3d5yE5l_pNdWM_). |
| [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT1WaeYMJSw8d41ugqMHSdbGKWY4FbR0stxPn0BzVt1qu4uMQkdmeZkPUL4pHQr43Mscrojm2w5-R0j3w_gJLFT4mfN9oESvBHeBg-k_WBEYSQA2_pFzWGM6yD-kGmcWkveTmAqMxadL1rFp) | The IG User must have an approved [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT2sFYbt51lrWAXfnAMVu2uO8lXVJ_bgH12O_RmUW4MEE5h5od_04z8ADNlXEpoEvJ1DZ6tlszUoYbQ-kl-8HO1_DZBy5F2Y1rXaJrhwc58GnuK4tIzOXT5p-_jc80T8hiIsnQjC995UeqoK) with a product catalog containing products. |
| [Permissions](https://developers.facebook.com/docs/permissions/reference) | [`catalog_management`](https://developers.facebook.com/docs/permissions/reference/catalog_management)  <br>[`instagram_basic`](https://developers.facebook.com/docs/permissions/reference/instagram_basic)  <br>[`instagram_shopping_tag_products`](https://developers.facebook.com/docs/permissions/reference/instagram_shopping_tag_products)  <br>[`pages_show_list`](https://developers.facebook.com/docs/permissions/reference/pages_show_list)<br><br>  <br><br>If the app user was granted a role via the Business Manager on the [Page](https://developers.facebook.com/docs/instagram-api/overview#pages) connected to the targeted IG User, you will also need one of:<br><br>  <br><br>[`ads_management`](https://developers.facebook.com/docs/permissions/reference/ads_management)  <br>[`business_management`](https://developers.facebook.com/docs/permissions/reference/business_management) |

### Request Syntax

GET https://graph.facebook.com/{api-version}/{ig-user-id}/catalog\_product\_search
  ?catalog\_id={catalog-id}
  &q={q}
  &access\_token={access-token}

### Path Parameters

| Placeholder | Value |
| --- | --- |
| `{api-version}` | API [version](https://developers.facebook.com/docs/instagram-basic-display-api/overview#versions). |
| `{ig-user-id}` | **Required.** App user's app-scoped user ID. |

### Query String Parameters

| Key | Placeholder | Value |
| --- | --- | --- |
| `access_token` | `{access-token}` | **Required.** App user's [User](https://developers.facebook.com/docs/facebook-login/access-tokens/#usertokens) access token. |
| `catalog_id` | `{catalog-id}` | **Required.** ID of catalog to search. |
| `q` | `{q}` | A string to search for in each product's name or SKU number (SKU numbers can be added in the **Content ID** column in the catalog management interface). If no string is specified, all tag-eligible products will be returned. |

### Response

A JSON-formatted object containing an array of tag-eligible products and their metadata. Supports [cursor-based pagination](https://developers.facebook.com/docs/graph-api/results#cursors).

{
  "data": \[
    {
      "product\_id": {product-id},
      "merchant\_id": {merchant-id},
      "product\_name": "{product-name}",
      "image\_url": "{image-url}",
      "retailer\_id": "{retailer-id}",
      "review\_status": "{review-status}",
      "is\_checkout\_flow": {is-checkout-flow}
    }
  \]
}

#### Response Contents

| Property | Value |
| --- | --- |
| `product_id` | Product ID. |
| `merchant_id` | Merchant ID. |
| `product_name` | Product name. |
| `image_url` | Product image URL. |
| `retailer_id` | Retailer ID. |
| `review_status` | Review status. Values can be `approved`, `outdated`, `pending`, `rejected`. An approved product can appear in the app user's [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT0ULcRbXC4LSgbako41rUdZcvu76zxyk05IjlAgzosO15CgEsZPv6iVks73_kpmhnrWAfIc8hYYnEvlNY8Q42aENWC1vRWMKGtaK2eGu8QebIehTVuVhb4Bg5s1-qito9f3X8Yac_9qBeRo), but an approved status does not indicate product availability (e.g, the product could be out of stock). Only tags associated with products that have a `review_status` of `approved` can appear on published posts. |
| `is_checkout_flow` | If `true`, product can be purchased directly in the Instagram app. If `false`, product must be purchased in the app user's app/website. |
| `product_variants` | Product IDs (`product_id`) and variant names (`variant_name`) of [product variants](https://developers.facebook.com/docs/marketing-api/catalog/guides/product-variants). |

### cURL Example

#### Request

curl -i -X GET \\
 "https://graph.facebook.com/`v18.0`/90010177253934/catalog\_product\_search?catalog\_id=960179311066902&q=gummy&access\_token=EAAOc"

#### Response

{
  "data": \[
    {
      "product\_id": 3231775643511089,
      "merchant\_id": 90010177253934,
      "product\_name": "Gummy Wombats",
      "image\_url": "https://scont...",
      "retailer\_id": "oh59p9vzei",
      "review\_status": "approved",
      "is\_checkout\_flow": true,
      "product\_variants": \[
            {
              "product\_id": 5209223099160494
            },
            {
              "product\_id": 7478222675582505,
              "variant\_name": "Green Gummy Wombats"
            }
          \]
    }
  \]
}

Updating
--------

This operation is not supported.

Deleting
--------

This operation is not supported.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

IG User Content Publishing Limit
================================

Represents an [IG User's](https://developers.facebook.com/docs/instagram-api/reference/ig-user) current [content publishing](https://developers.facebook.com/docs/instagram-api/guides/content-publishing) usage.

Creating
--------

This operation is not supported.

Reading
-------

**`GET /{ig-user-id}/content_publishing_limit`**

Get the number of times an [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) has published and [IG Container](https://developers.facebook.com/docs/instagram-api/reference/ig-container) within a given time period. Refer to the [Content Publishing](https://developers.facebook.com/docs/instagram-api/guides/content-publishing) guide for complete publishing steps.

### Requirements

| Type | Requirement |
| --- | --- |
| [Access Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens/) | [User](https://developers.facebook.com/docs/facebook-login/access-tokens/#usertokens) |
| [Permissions](https://developers.facebook.com/docs/permissions/reference) | [`instagram_basic`](https://developers.facebook.com/docs/permissions/reference/instagram_basic)  <br>[`instagram_content_publish`](https://developers.facebook.com/docs/permissions/reference/instagram_content_publish)  <br>[`pages_read_engagement`](https://developers.facebook.com/docs/permissions/reference/pages_read_engagement)<br><br>  <br><br>If the app user was granted a role via the Business Manager on the [Page](https://developers.facebook.com/docs/instagram-api/overview#pages) connected to the targeted IG User, you will also need one of:<br><br>  <br><br>[`ads_management`](https://developers.facebook.com/docs/permissions/reference/ads_management)  <br>[`business_management`](https://developers.facebook.com/docs/permissions/reference/business_management) |

### Request Syntax

GET https://graph.facebook.com/v9.0/{ig-user-id}/content\_publishing\_limit
  ?fields={fields}
  &since={since}
  &access\_token={access-token}

### Query String Parameters

| Placeholder | Value Description |
| --- | --- |
| `{access-token}`  <br>**Required**  <br>_String_ | The app user's User Access Token. |
| `{fields}`  <br>_Comma-separated list_ | A comma-separated list of [fields](#fields) you want returned. If omitted, the `quota_usage` field will be returned by default. |
| `{since}`  <br>_Unix timestamp_ | A Unix timestamp no older than 24 hours. |

### Fields

| Field | Value Description |
| --- | --- |
| `config`  <br>_Object_ | Returns these values:<br><br>* `quota_total` — The maximum number of [IG Containers](https://developers.facebook.com/docs/instagram-api/reference/ig-container) the app user can publish within the `quota_duration` time period (currently `50`).<br>* `quota_duration` — The period of time in seconds against which the `quota_total` is calculated (currently `86400` seconds, or 24 hours). |
| `quota_usage`  <br>_Comma-separated list_ | The number of times the app user has published an [IG Container](https://developers.facebook.com/docs/instagram-api/reference/ig-container) since the time specified in the `since` query string parameter. If the `since` parameter is omitted, this value will be the number of times the app user has published a container within the last 24 hours. This field is returned by default if the `fields` query string parameter is omitted from the query. |

### Sample Request

curl -X GET \\
  'https://graph.facebook.com/`v18.0`/17841405822304914/content\_publishing\_limit?fields=quota\_usage,rate\_limit\_settings&since=1609969714&access\_token=IGQVJ...'

### Sample Response

{
  "data": \[
    {
      "quota\_usage": 2,
      "config": {
        "quota\_total": 50,
        "quota\_duration": 86400
      }
    }
  \]
}

Updating
--------

This operation is not supported.

Deleting
--------

This operation is not supported.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

Instagram User Insights
=======================

Represents social interaction metrics on an [Instagram User](https://developers.facebook.com/docs/instagram-api/reference/ig-user).

Creating
--------

This operation is not supported.

Reading
-------

**`GET /{ig-user-id}/insights`**

Returns insights on an [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user).

### Limitations

* `follower_count`, `online_followers`, and all `audience_*` metrics are not available on IG Users with fewer than 100 followers.
* Insights data for the `online_followers` metric is only available for the last 30 days.
* If insights data you are requesting does not exist or is currently unavailable, the API will return an empty data set instead of `0` for individual metrics.
* Demographic metrics only return the top 45 performers (e.g., for `audience_city`, up to 45 cities with the highest number of followers can be returned).
* Only viewers for whom we have demographic data are used in demographic metric calculations.
* Summing demographic metric values may result in a value less than the follower count (see previous bullet point).
* `audience_*` [metrics](#metrics-and-periods) do not support `since` and `until` [range](#range) parameters.
* Data used to calculate metrics may be delayed up to 48 hours.

### Requirements

| Type | Description |
| --- | --- |
| [Access Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) | [User](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) |
| [Permissions](https://developers.facebook.com/docs/apps/review/login-permissions) | [`instagram_basic`](https://developers.facebook.com/docs/facebook-login/permissions#reference-instagram_basic)  <br>[`instagram_manage_insights`](https://developers.facebook.com/docs/facebook-login/permissions#reference-instagram_manage_insights)  <br>[`pages_read_engagement`](https://developers.facebook.com/docs/facebook-login/permissions#reference-pages_read_engagement)  <br>[`pages_show_list`](https://developers.facebook.com/docs/facebook-login/permissions#reference-pages_show_list)<br><br>  <br><br>If the app user was granted a role on the Page via the Business Manager, you will also need one of:<br><br>  <br><br>[`ads_management`](https://developers.facebook.com/docs/permissions/reference/ads_management)  <br>[`business_management`](https://developers.facebook.com/docs/permissions/reference/business_management) |

### Request Syntax

GET https://graph.facebook.com/{api-version}/{ig-user-id}/insights
  ?metric={metric}
  &period={period}
  &since={since}
  &until={until}
  &access\_token={access-token}

### Path Parameters

| Placeholder | Value |
| --- | --- |
| `{api-version}` | API [version](https://developers.facebook.com/docs/graph-api/guides/versioning). |
| `{ig-user-id}` | **Required.** IG User ID. |

### Query String Parameters

| Parameter | Value |
| --- | --- |
| `{access-token}`  <br>**Required**  <br>_String_ | The app user's User Access Token. |
| `{metric}`  <br>**Required**  <br>_Comma-separated list_ | A comma-separated list of [Metrics](#metrics-and-periods) you want returned. If requesting multiple metrics, they must all have the same compatible [Period](#metrics-and-periods). |
| `{period}`  <br>**Required**  <br>_String_ | A [Period](#metrics-and-periods) that is compatible with the metrics you are requesting. |
| `{since}`  <br>_Unix timestamp_ | Used in conjunction with `{until}` to define a [Range](#range). If you omit `since` and `until`, the API defaults to a 2 day range: yesterday through today.<br><br>  <br><br>**Note**: The pagination cursors (`previous` and `next`) fetch the next time window of results, not the next batch of results within the current time window. |
| `{until}`  <br>_Unix timestamp_ | Used in conjunction with `{since}` to define a [Range](#range). If you omit `since` and `until`, the API defaults to a 2 day range: yesterday through today.<br><br>  <br><br>**Note**: The pagination cursors (`previous` and `next`) fetch the next time window of results, not the next batch of results within the current time window. |

### Metrics and Periods

Some of these metrics are deprecated for v18.0. They will be deprecated for all versions beginning Dec 11, 2023. Please use the alternative metrics listed. See the [Changelog](https://developers.facebook.com/docs/instagram-api/changelog) for more information.

Metrics that support `lifetime` periods will have results returned in an array of 24 hour periods, with periods ending on UTC−07:00. `audience_*` metrics do not support `since` and `until` [range](#range) parameters.

| Metric | Compatible Period | Description |
| --- | --- | --- |
| `audience_city`  <br>_Deprecated for v18.0+_ | `lifetime` | Cities of followers for whom we have demographic data.<br><br>  <br><br>* Does not include current day's data.<br>* Not available on IG Users with fewer than 100 followers.<br>* Only top 45 cities with highest values returned.<br>* Does not support `since` and `until` parameters.<br>* Response does not include the `end_time` JSON property.<br><br>**Alternative metric:** `follower_demographics`  <br>**Breakdown:** `city` |
| `audience_country`  <br>_Deprecated for v18.0+_ | `lifetime` | Countries of followers for whom we have demographic data.<br><br>  <br><br>* Does not include current day's data.<br>* Not available on IG Users with fewer than 100 followers.<br>* Only top 45 countries with highest values returned.<br>* Does not support `since` and `until` parameters.<br>* Response does not include the `end_time` JSON property.<br><br>**Alternative metric:** `follower_demographics`  <br>**Breakdown:** `country` |
| `audience_gender_age`  <br>_Deprecated for v18.0+_ | `lifetime` | The gender and age distribution of followers for whom we have demographic data. Possible values: `M` (male), `F` (female), `U` (Uncategorised).<br><br>  <br><br>* Does not include current day's data.<br>* Not available on IG Users with fewer than 100 followers.<br>* Does not support `since` and `until` parameters.<br>* Response does not include the `end_time` JSON property.<br><br>**Alternative metric:** `follower_demographics`  <br>**Breakdown:** `age`, `gender` |
| `audience_locale`  <br>_Deprecated for v18.0+_ | `lifetime` | **Note:** This metric is no longer supported.<br><br>  <br><br>Locales by country codes of followers for whom we have demographic data.<br><br>  <br><br>* Does not include current day's data.<br>* Not available on IG Users with fewer than 100 followers.<br>* Only top 45 locales with highest values returned.<br>* Does not support `since` and `until` parameters.<br>* Response does not include the `end_time` JSON property.<br><br>**Alternative metric:** N/A |
| `email_contacts` | `day` | Total number of taps on the email link in the [IG User's](https://developers.facebook.com/docs/instagram-api/reference/ig-user) profile. |
| `follower_count` | `day` | Total number of new followers each day within the specified range. Returns a maximum of 30 days worth of data. Not available on IG Users with fewer than 100 followers. |
| `get_directions_clicks` | `day` | Total number of taps on the directions link in the [IG User's](https://developers.facebook.com/docs/instagram-api/reference/ig-user) profile. |
| `impressions` | `day`, `week`, `days_28` | Total number of times the [IG User's](https://developers.facebook.com/docs/instagram-api/reference/ig-user) [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) have been viewed. Includes ad activity generated through the API, Facebook ads interfaces, and the Promote feature. Does not include profile views. |
| `online_followers` | `lifetime` | Total number of the [IG User's](https://developers.facebook.com/docs/instagram-api/reference/ig-user) followers who were online during the specified range. Not available on IG Users with fewer than 100 followers. |
| `phone_call_clicks` | `day` | Total number of taps on the call link in the [IG User's](https://developers.facebook.com/docs/instagram-api/reference/ig-user) profile. |
| `profile_views` | `day` | Total number of users who have viewed the [IG User's](https://developers.facebook.com/docs/instagram-api/reference/ig-user) profile within the specified period. |
| `reach` | `day`, `week`, `days_28` | Total number of unique users who have viewed at least one of the [IG User's](https://developers.facebook.com/docs/instagram-api/reference/ig-user) [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media). Repeat views and views across different IG Media owned by the IG User by the same user are only counted as a single view. Includes ad activity generated through the API, Facebook ads interfaces, and the Promote feature. |
| `text_message_clicks` | `day` | Total number of taps on the text message link in the [IG User's](https://developers.facebook.com/docs/instagram-api/reference/ig-user) profile. |
| `website_clicks` | `day` | Total number of taps on the website link in the [IG User's](https://developers.facebook.com/docs/instagram-api/reference/ig-user) profile. |

### Range

This edge supports [time-based pagination](https://developers.facebook.com/docs/graph-api/results#time), so you can include the `since` and `until` parameters with Unix timestamps to define a _range_. For example, to get 28 days worth of impressions — _every day for the last 10 days_ — you could generate Unix timestamps for _10 days ago_ and _today_, assign them to the `since` and `until` parameters, and include them in your request:

metric=impressions&period=days\_28&since=1501545600&until=1502493720

The `since` and `until` parameters are inclusive, so if your range includes a day that hasn't ended (i.e, today), subsequent queries throughout the day may return increased values. If you do not include the `since` and `until` parameters, the API will default to a 2 day range: yesterday through today.

### Sample Request

curl -X GET \\
  'https://graph.facebook.com/`v18.0`/17841405822304914/insights?metric=impressions,reach,profile\_views&period=day&access\_token=IGQVJ...'

### Sample Response

{
  "data": \[
    {
      "name": "impressions",
      "period": "day",
      "values": \[
        {
          "value": 4,
          "end\_time": "2017-05-04T07:00:00+0000"
        },
        {
          "value": 66,
          "end\_time": "2017-05-05T07:00:00+0000"
        }
      \],
      "title": "Impressions",
      "description": "Total number of times this profile has been seen",
      "id": "17841400008460056/insights/impressions/day"
    },
    {
      "name": "reach",
      "period": "day",
      "values": \[
        {
          "value": 3,
          "end\_time": "2017-05-04T07:00:00+0000"
        },
        {
          "value": 36,
          "end\_time": "2017-05-05T07:00:00+0000"
        }
      \],
      "title": "Reach",
      "description": "Total number of unique accounts that have seen this profile",
      "id": "17841400008460056/insights/reach/day"
    },
    {
      "name": "profile\_views",
      "period": "day",
      "values": \[
        {
          "value": 0,
          "end\_time": "2017-05-04T07:00:00+0000"
        },
        {
          "value": 2,
          "end\_time": "2017-05-05T07:00:00+0000"
        }
      \],
      "title": "Profile Views",
      "description": "Total number of unique accounts that have viewed this profile within the specified period",
      "id": "17841400008460056/insights/profile\_views/day"
    }
  \]
}

Notice that the [sample request](#sample-request) above did not include the `since` and `until` parameters, so the API returned data for a default range of 2 days. Each day is identified by an ISO 8601 formatted UTC timestamp with zero offset, which has been assigned to an `end_time` property.

The `end_time` property indicates a data set's lookback cutoff date; data older than this value is not included in the data set's calculation.

Updating
--------

This operation is not supported.

Deleting
--------

This operation is not supported.

New Metrics
-----------

The metrics listed below are new and will gradually be made available to all developers. These metrics will eventually replace the legacy metrics listed above. If you see this message you are able to use the new metrics described below.

### Request Syntax

GET https://graph.facebook.com/{api-version}/{ig-user-id}/insights
  ?metric={metric}
  &period={period}
  &timeframe={timeframe}
  &metric\_type={metric-type}
  &breakdown={breakdown}
  &since={since}
  &until={until}
  &access\_token={access-token}

### Path Parameters

| Placeholder | Value |
| --- | --- |
| `{api-version}` | API [version](https://developers.facebook.com/docs/graph-api/guides/versioning). |
| `{ig-user-id}` | **Required.** [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) ID. |

### Query String Parameters

| Key | Placeholder | Value |
| --- | --- | --- |
| `access_token` | `{access-token}` | **Required.** The app user's [User](https://developers.facebook.com/docs/facebook-login/guides/access-tokens#usertokens) access token. |
| `breakdown` | `{breakdown}` | Designates how to break down result set into subsets. See [Breakdown](#breakdown). |
| `metric` | `{metric}` | **Required.** Comma-separated list of [Metrics](#metrics) you want returned. |
| `metric_type` | `{metric-type}` | Designates if you want the responses aggregated by time period or as a simple total. See [Metric Type](#metric-type). |
| `period` | `{period}` | **Required.** [Period](#period) aggregation. |
| `since` | `{since}` | Unix timestamp indicating start of range. See [Range](#range-2). |
| `timeframe` | `{timeframe}` | **Required for demographics-related metrics.** Designates how far to look back for data. See [Timeframe](#timeframe). |
| `until` | `{until}` | Unix timestamp indicating end of range. See [Range](#range-2). |

### Breakdown

If you request `metric_type=total_value`, you can also specify one or more breakdowns, and the results will be broken down into smaller sets based on the specified breakdown. Values can be:

* `contact_button_type` — Break down results by profile UI component that viewers tapped or clicked. Response values can be:
    * `BOOK_NOW`
    * `CALL`
    * `DIRECTION`
    * `EMAIL`
    * `INSTANT_EXPERIENCE`
    * `TEXT`
    * `UNDEFINED`
* `follow_type` — Break down results by followers or non-followers. Response values can be:
    * `FOLLOWER`
    * `NON_FOLLOWER`
    * `UNKNOWN`
* `media_product_type` — Break down results by the surface where viewers viewed or interacted with the app user's media. Response values can be:
    * `AD`
    * `FEED`
    * `REELS`
    * `STORY`

Refer to the [Metrics](#metrics) table to determine which metrics are compatible with a breakdown. If you request a metric that doesn't support a breakdown, the API will return an error (`"An unknown error has occurred."`), so be careful if requesting multiple metrics in a single query.

If you request `metric_type=time_series`, breakdowns will not be included in the response.

### Metric Type

You can designate how you want results aggregated, either by time period or as a simple total (with breakdowns, if requested). Values can be:

* `time_series` — Tells the API to aggregate results by time period. See [Period](#period).
* `total_value` — Tells the API to return results as a simple total. If breakdowns are included in the request, the result set will be further broken down by the specific breakdowns. See [Breakdown](#breakdown).

### Period

Tells the API which time frame to use when aggregating results. Only compatible with interaction-related metrics.

### Timeframe

Tells the API how far to look back for data when requesting demographic-related metrics. This value overrides the `since` and `until` parameters.

### Range

Assign UNIX timestamps to the `since` and `until` parameters to define a range. The API will only include data created within this range (inclusive). If you do not include these parameters, the API will look back 24 hours.

For demographics-related metrics, the `timeframe` parameter overrides these values. See [Timeframe](#timeframe).

### Metrics

#### Interaction Metrics

  

| Metric | Period | Timeframe | Breakdown | Metric Type | Description |
| --- | --- | --- | --- | --- | --- |
| `impressions` | `day` | n/a | n/a | `total_value`, `time_series` | The number of times your posts, stories, reels, videos and live videos were on screen, including in ads. |
| `reach` | `day` | n/a | `media_product_type`, `follow_type` | `total_value`, `time_series` | The number of unique accounts that have seen your content, at least once, including in ads. Content includes posts, stories, reels, videos and live videos. Reach is different from impressions, which may include multiple views of your content by the same accounts.<br><br>  <br><br>This metric is estimated and [in development](https://business.facebook.com/business/help/metrics-labeling). |
| `total_interactions` | `day` | n/a | `media_product_type` | `total_value` | The total number of post interactions, story interactions, reels interactions, video interactions and live video interactions, including any interactions on boosted content. |
| `accounts_engaged` | `day` | n/a | n/a | `total_value` | The number of accounts that have interacted with your content, including in ads. Content includes posts, stories, reels, videos and live videos. Interactions can include actions such as likes, saves, comments, shares or replies.<br><br>  <br><br>This metric is estimated and [in development](https://business.facebook.com/business/help/metrics-labeling). |
| `likes` | `day` | n/a | `media_product_type` | `total_value` | The number of likes on your posts, reels, and videos. |
| `comments` | `day` | n/a | `media_product_type` | `total_value` | The number of comments on your posts, reels, videos and live videos.<br><br>  <br><br>This metric is [in development](https://business.facebook.com/business/help/metrics-labeling). |
| `saved` | `day` | n/a | `media_product_type` | `total_value` | The number of saves of your posts, reels, and videos. |
| `shares` | `day` | n/a | `media_product_type` | `total_value` | The number of shares of your posts, stories, reels, videos and live videos. |
| `replies` | `day` | n/a | n/a | `total_value` | The number of replies you received from your story, including text replies and quick reaction replies. |
| `follows_and_unfollows` | `day` | n/a | `follow_type` | `total_value` | The number of accounts that followed you and the number of accounts that unfollowed you or left Instagram in the selected time period.<br><br>  <br><br>Not returned if the IG User has less than 100 followers. |
| `profile_links_taps` | `day` | n/a | `contact_button_type` | `total_value` | The number of taps on your business address, call button, email button and text button. |
| `website_clicks` | `day` | n/a | n/a | `total_value` | The number of times the link to your website was tapped. |
| `profile_views` | `day` | n/a | n/a | `total_value` | The number of times your profile was visited. |

#### Demographic Metrics

  

| Metric | Period | Timeframe | Breakdown | Metric Type | Description |
| --- | --- | --- | --- | --- | --- |
| `engaged_audience_demographics` | `lifetime` | One of:<br><br>  <br><br>`last_14_days`, `last_30_days`, `last_90_days`, `prev_month`, `this_month`, `this_week` | `age`,  <br>`city`,  <br>`country`,  <br>`gender` | `total_value` | The demographic characteristics of the engaged audience, including countries, cities and gender distribution.<br><br>  <br><br>Does not support `since` or `until`. See [Range](#range-2) for more information.<br><br>  <br><br>Not returned if the IG User has less than 100 followers. |
| `reached_audience_demographics` | `lifetime` | One of:<br><br>  <br><br>`last_14_days`, `last_30_days`, `last_90_days`, `prev_month`, `this_month`, `this_week` | `age`,  <br>`city`,  <br>`country`,  <br>`gender` | `total_value` | The demographic characteristics of the reached audience, including countries, cities and gender distribution.<br><br>  <br><br>Does not support `since` or `until`. See [Range](#range-2) for more information.<br><br>  <br><br>Not returned if the IG User has less than 100 followers. |
| `follower_demographics` | `lifetime` | One of:<br><br>  <br><br>`last_14_days`, `last_30_days`, `last_90_days`, `prev_month`, `this_month`, `this_week` | `age`,  <br>`city`,  <br>`country`,  <br>`gender` | `total_value` | The demographic characteristics of followers, including countries, cities and gender distribution.<br><br>  <br><br>Does not support `since` or `until`. See [Range](#range-2) for more information.<br><br>  <br><br>Not returned if the IG User has less than 100 followers. |

### Response

A JSON object containing the results of your query. Results can include the following data, based on your query specifications:

{
  "data": \[
    {
      "name": "{data}",
      "period": "{period}",
      "title": "{title}",
      "description": "{description}",
      "total\_value": {
        "value": {value},
        "breakdowns": \[
          {
            "dimension\_keys": \[
              "{key-1}",
              "{key-2",
              ...
            \],
            "results": \[
              {
                "dimension\_values": \[
                  "{value-1}",
                  "{value-2}",
                  ...
                \],
                "value": {value},
                "end\_time": "{end-time}"
              },
              ...
            \]
          }
        \]
      },
      "id": "{id}"
    }
  \],
  "paging": {
    "previous": "{previous}",
    "next": "{next}"
  }
}

### Response Contents

| Property | Value Type | Description |
| --- | --- | --- |
| `breakdowns` | Array | An array of objects describing the [breakdowns](#breakdown) requested and their results.<br><br>  <br><br>Only returned if `metric_type=total_values` is requested. |
| `data` | Array | An array of objects describing your results. |
| `description` | String | [Metric](#metrics) description. |
| `dimension_keys` | Array | An array of strings describing [breakdowns](#breakdown) requested in the query. Can be used as keys corresponding to values in individual breakdown sets.<br><br>  <br><br>Only returned if `metric_type=total_values` is requested. |
| `dimension_values` | Array | An array of strings describing [breakdown](#breakdown) set values. Values can be mapped to `dimension_keys`.<br><br>  <br><br>Only returned if `metric_type=total_values` is requested. |
| `end_time` | String | ISO 8601 timestamp with time and offset. For example: `2022-08-01T07:00:00+0000` |
| `id` | String | A string describing the query's path parameters. |
| `name` | String | [Metric](#metrics) requested. |
| `next` | String | URL to retrieve the next page of results. See [Paginated Results](https://developers.facebook.com/docs/graph-api/results) for more information. |
| `paging` | Object | An object containing URLs used to request the next set of results. See [Paginated Results](https://developers.facebook.com/docs/graph-api/results) for more information. |
| `period` | String | [Period](#period) requested. |
| `previous` | String | URL to retrieve the previous page of results. See [Paginated Results](https://developers.facebook.com/docs/graph-api/results) for more information. |
| `results` | Array | An array of objects describing each [breakdown](#breakdown) set.<br><br>  <br><br>Only returned if `metric_type=total_values` is requested. |
| `title` | String | [Metric](#metrics) title. |
| `total_value` | Object | Object describing requested [breakdown](#breakdown) values (if breakdowns were requested). |
| `value` | Integer | For `data.total_value.value`, sum of requested [metric](#metrics) values.<br><br>  <br><br>For `data.total_value.breakdowns.results.value`, sum of [breakdown](#breakdown) set values. Only returned if `metric_type=total_values` is requested. |

### Sample Interaction Metric Request

curl -i -X GET \\
  "https://graph.facebook.com/`v18.0`/17841405822304914/insights?metric=reach&period=day&breakdown=media\_product\_type&metric\_type=total\_value&since=1658991600&access\_token=EAAOc..."

### Sample Interaction Metric Response

{
  "data": \[
    {
      "name": "reach",
      "period": "day",
      "title": "Accounts reached",
      "description": "The number of unique accounts that have seen your content, at least once, including in ads. Content includes posts, stories, reels, videos and live videos. Reach is different from impressions, which may include multiple views of your content by the same accounts. This metric is estimated and in development.",
      "total\_value": {
        "value": 224,
        "breakdowns": \[
          {
            "dimension\_keys": \[
              "media\_product\_type"
            \],
            "results": \[
              {
                "dimension\_values": \[
                  "CAROUSEL\_CONTAINER"
                \],
                "value": 100
              },
              {
                "dimension\_values": \[
                  "POST"
                \],
                "value": 124
              }
            \]
          }
        \]
      },
      "id": "17841405309211844/insights/reach/day"
    }
  \],
  "paging": {
    "previous": "https://graph.face...",
    "next": "https://graph.face..."
  }

### Sample Demographic Metric Request

curl -i -X GET \\
  "https://graph.facebook.com/`v18.0`/17841405822304914/insights?metric=engaged\_audience\_demographics&period=lifetime&timeframe=last\_90\_days&breakdowns=country&metric\_type=total\_value&access\_token=EAAOc..."

### Sample Demographic Metric Response

{
  "data": \[
    {
      "name": "engaged\_audience\_demographics",
      "period": "lifetime",
      "title": "Engaged audience demographics",
      "description": "The demographic characteristics of the engaged audience, including countries, cities and gender distribution.",
      "total\_value": {
        "breakdowns": \[
          {
            "dimension\_keys": \[
              "timeframe",
              "country"
            \],
            "results": \[
              {
                "dimension\_values": \[
                  "LAST\_90\_DAYS",
                  "AR"
                \],
                "value": 1
              },
              {
                "dimension\_values": \[
                  "LAST\_90\_DAYS",
                  "RU"
                \],
                "value": 1
              },
              {
                "dimension\_values": \[
                  "LAST\_90\_DAYS",
                  "MA"
                \],
                "value": 1
              },
              {
                "dimension\_values": \[
                  "LAST\_90\_DAYS",
                  "LA"
                \],
                "value": 1
              },
              {
                "dimension\_values": \[
                  "LAST\_90\_DAYS",
                  "IQ"
                \],
                "value": 2
              },
              {
                "dimension\_values": \[
                  "LAST\_90\_DAYS",
                  "MX"
                \],
                "value": 1
              },
              {
                "dimension\_values": \[
                  "LAST\_90\_DAYS",
                  "FR"
                \],
                "value": 1
              },
              {
                "dimension\_values": \[
                  "LAST\_90\_DAYS",
                  "ES"
                \],
                "value": 3
              },
              {
                "dimension\_values": \[
                  "LAST\_90\_DAYS",
                  "NL"
                \],
                "value": 1
              },
              {
                "dimension\_values": \[
                  "LAST\_90\_DAYS",
                  "TR"
                \],
                "value": 1
              },
              {
                "dimension\_values": \[
                  "LAST\_90\_DAYS",
                  "US"
                \],
                "value": 7
              }
            \]
          }
        \]
      },
      "id": "17841401130346306/insights/engaged\_audience\_demographics/lifetime"
    }
  \]
}

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

IG User Live Media
==================

Represents a collection of live video [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) on an [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user).

Creating
--------

This operation is not supported.

Reading
-------

**`GET /{ig-user-id}/live_media`**

Get a collection of live video [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) on an [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user).

### Limitations

Only live video IG Media being broadcast at the time of the request will be returned.

### Time-based Pagination

This endpoint supports [time-based pagination](https://developers.facebook.com/docs/graph-api/using-graph-api#time). Include `since` and `until` query-string paramaters with Unix timestamp or `strtotime` data values to define a time range.

### Requirements

| Type | Requirement |
| --- | --- |
| [Access Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens/) | [User](https://developers.facebook.com/docs/facebook-login/access-tokens/#usertokens) |
| [Permissions](https://developers.facebook.com/docs/permissions/reference) | [`instagram_basic`](https://developers.facebook.com/docs/permissions/reference/instagram_basic)  <br>[`instagram_read_engagement`](https://developers.facebook.com/docs/permissions/reference/instagram_read_engagement)  <br>[`pages_read_engagement`](https://developers.facebook.com/docs/permissions/reference/pages_show_list)<br><br>  <br><br>If the app user was granted a role via the Business Manager on the [Page](https://developers.facebook.com/docs/instagram-api/overview#pages) connected to the targeted IG User, you will also need one of:<br><br>  <br><br>[`ads_management`](https://developers.facebook.com/docs/permissions/reference/ads_management)  <br>[`business_management`](https://developers.facebook.com/docs/permissions/reference/business_management) |

### Request Syntax

GET https://graph.facebook.com/{api-version}/{ig-user-id}/live\_media
  ?access\_token={access-token}

### Path Parameters

| Placeholder | Value |
| --- | --- |
| `{api-version}`  <br>_String_ | API [version](https://developers.facebook.com/docs/instagram-basic-display-api/overview#versions). |
| `{ig-user-id}`  <br>**Required**  <br>_String_ | App user's app-scoped user ID. |

### Query String Parameters

| Key | Value |
| --- | --- |
| `access_token`  <br>**Required**  <br>_String_ | App user's [User](https://developers.facebook.com/docs/facebook-login/access-tokens/#usertokens) access token. |
| `fields`  <br>_Comma-separated list_ | Comma-separated list of IG Media [fields](https://developers.facebook.com/docs/instagram-api/reference/ig-media#fields) you want returned for each live IG Media in the result set. |
| `since`  <br>_timestamp_ | A Unix timestamp or `strtotime` data value that points to the start of a range of time-based data. See [time-based pagination](https://developers.facebook.com/docs/graph-api/using-graph-api#time). |
| `until`  <br>_timestamp_ | A Unix timestamp or `strtotime` data value that points to the end of a range of time-based data. See [time-based pagination](https://developers.facebook.com/docs/graph-api/using-graph-api#time). |

### Response

A JSON-formatted object containing the data you requested.

{
  "data": \[\],
  "paging": {}
}

#### Response Contents

| Property | Value |
| --- | --- |
| `data` | An array of [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) on an [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user). |
| `paging` | An object containing [paging](https://developers.facebook.com/docs/graph-api/using-graph-api#paging) cursors and next/previous data set retrievial URLs. |

### cURL Example

#### Request

curl -X GET \\
  'https://graph.facebook.com/`v18.0`/17841405822304914/live\_media?fields=id,media\_type,media\_product\_type,owner,username,comments&access\_token=IGQVJ...'

#### Response

{
   "id":"90010498116233",
   "media\_type":"BROADCAST",
   "media\_product\_type":"LIVE",
   "owner":{
      "id":"17841405822304914"
   },
   "username":"jayposiris",
   "comments":{
      "data":\[
        {
            "hidden": false,
            "id": "17907364514064687",
            "like\_count": 0,
            "media": {
                "id": "17892642502701087"
            },
            "text": "@jayposiris",
            "timestamp": "2021-08-17T21:23:07+0000",
            "username": "bztest0316\_11",
            "from": {
                "id": "5895605157123796",
                "username": "bztest0316\_11"
            }
        }
      \]
   }
}

Updating
--------

This operation is not supported.

Deleting
--------

This operation is not supported.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

IG User Media
=============

Represents a collection of [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) objects on an [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user).

Beginning November 9, 2023, the `VIDEO` value for `media_type` will no longer be supported. Use the `REELS` media type to publish a video to your feed.

Creating
--------

**`POST /{ig-user-id}/media`**

* Create an image, carousel, story or reel [IG Container](https://developers.facebook.com/docs/instagram-api/reference/ig-container) for use in the post publishing process. See the [Content Publishing](https://developers.facebook.com/docs/instagram-api/guides/content-publishing) guide for complete publishing steps.

### Limitations

#### General Limitations

* Containers expire after 24 hours.
* If the [Page](https://developers.facebook.com/docs/instagram-api/overview#pages) connected to the targeted Instagram Professional account requires [Page Publishing Authorization](https://www.facebook.com/business/m/one-sheeters/page-publishing-authorization) (PPA), PPA must be completed or the request will fail.
* If the Page connected to the targeted Instagram Professional account requires two-factor authentication, the Facebook User must also have performed two-factor authentication or the request will fail.
* Publishing to Instagram TV is not supported.

#### Reels Limitations

* Reels cannot appear in album carousels.
* Account privacy settings are respected upon publish. For example, if **Allow remixing** is enabled, published reels will have remixing enabled upon publish but remixing can be disabled on published reels manually through the Instagram app.
* Music tagging is only available for original audio.

#### Story Limitations

* Stories expire after 24 hours.
* Support either video URL or Reels URL but not both.
* Publishing stickers (i.e., link, poll, location) is not supported.

### Requirements

| Type | Description |
| --- | --- |
| [Access Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) | [User](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) |
| [Business Roles](https://www.facebook.com/business/help/442345745885606) | If creating containers for [product tagging](https://developers.facebook.com/docs/instagram-api/guides/product-tagging), the app user must have an admin role on the [Business Manager](https://business.facebook.com/) that owns the IG User's [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322&h=AT1W29Aj-0FOc8DdQwaKZ_Ys6yCUJcia5o7l2_DcWAEVGYkePs64NePiXBmLBMPql-olrhmf6dTS5n_S7DD95QOgtBklOXjv3v5K1IGrC6yEXkkDEcGwrunOdjQHs5W_RjVL0R3_jH14OeUh). |
| [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT1o66yS2UY95AVulx3T88k90p8-yCcuodwOJDfjUnIcVKT3o9sp5SMrZugbiDoXiyELN-HQywDbtGs3NF7iFFL4Up2tazWos4oByCE6EMqfzTJs_FkCOHUrlHYlC7lw6EciSaxa33IUc5C4) | If creating containers for [product tagging](https://developers.facebook.com/docs/instagram-api/guides/product-tagging), the IG User must have an approved [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT3RX58iA6K1Vlxc9N4TgMiigm-6LXedS61TJJdW2DwbG4XvSq2nPOTQVGTDNASDao5cHf8JUyratlNdnc6IUz39X71qI2MrjV7PlnxR3Ini9g5pD4d6s7JJlkFhcQRaPzU49N294lAagzjG) with a product catalog containing products. |
| [Permissions](https://developers.facebook.com/docs/apps/review/login-permissions) | [`instagram_basic`](https://developers.facebook.com/docs/facebook-login/permissions#reference-instagram_basic)  <br>[`instagram_content_publish`](https://developers.facebook.com/docs/permissions/reference/instagram_content_publish)  <br>[`pages_read_engagement`](https://developers.facebook.com/docs/facebook-login/permissions#reference-pages_read_engagement) or [`pages_show_list`](https://developers.facebook.com/docs/facebook-login/permissions#reference-pages_show_list)<br><br>  <br><br>If the app user was granted a role on the Page via the Business Manager, you will also need one of:<br><br>  <br><br>[`ads_management`](https://developers.facebook.com/docs/permissions/reference/ads_management)  <br>[`business_management`](https://developers.facebook.com/docs/permissions/reference/business_management)<br><br>  <br><br>If creating containers for [product tagging](https://developers.facebook.com/docs/instagram-api/guides/product-tagging), you will also need:<br><br>  <br><br>[`catalog_management`](https://developers.facebook.com/docs/permissions/reference/catalog_management)  <br>[`instagram_shopping_tag_products`](https://developers.facebook.com/docs/permissions/reference/instagram_shopping_tag_products) |
| [Tasks](https://developers.facebook.com/docs/instagram-api/overview#tasks) | The app user whose token is used in the request must be able to perform `MANAGE` or `CREATE_CONTENT` tasks on the [Page](https://developers.facebook.com/docs/instagram-api/overview#pages) connected to the targeted Instagram account. |

### Image Specifications

* Format: JPEG
* File size: 8 MB maximum.
* Aspect ratio: Must be within a 4:5 to 1.91:1 range
* Minimum width: 320 (will be scaled up to the minimum if necessary)
* Maximum width: 1440 (will be scaled down to the maximum if necessary)
* Height: Varies, depending on width and aspect ratio
* Color Space: sRGB. Images using other color spaces will have their color spaces converted to sRGB.

### Reel Specifications

The following are the specifications for Reels:

* Container: MOV or MP4 (MPEG-4 Part 14), no edit lists, moov atom at the front of the file.
    
* Audio codec: AAC, 48khz sample rate maximum, 1 or 2 channels (mono or stereo).
    
* Video codec: HEVC or H264, progressive scan, closed GOP, 4:2:0 chroma subsampling.
    
* Frame rate: 23-60 FPS.
    
* Picture size:
    
    * Maximum columns (horizontal pixels): 1920
        
    * Required aspect ratio is between 0.01:1 and 10:1 but we recommend 9:16 to avoid cropping or blank space.
        
    
* Video bitrate: VBR, 25Mbps maximum
    
* Audio bitrate: 128kbps
    
* Duration: 15 mins maximum, 3 seconds minimum
    
* File size: 1GB maximum
    

The following are the specifications for a Reels cover photo:

* Format: JPEG
    
* File size: 8MB maximum
    
* Color Space: sRGB. Images that use other color spaces will be converted to sRGB.
    
* Aspect ratio: We recommend 9:16 to avoid cropping or blank space. If the aspect ratio of the original image is not 9:16, we crop the image and use the middle most 9:16 rectangle as the cover photo for the reel. If you share a reel to your feed, we crop the image and use the middle most 1:1 square as the cover photo for your feed post.
    

### Story Image Specifications

* Format: JPEG
* File size: 8 MB maximum.
* Aspect ratio: We recommended 9:16 to avoid cropping or blank space
* Color Space: sRGB. Images using other color spaces will have their color spaces converted to sRGB

### Story Video Specifications

* Container: MOV or MP4 (MPEG-4 Part 14), no edit lists, moov atom at the front of the file.
    
* Audio codec: AAC, 48khz sample rate maximum, 1 or 2 channels (mono or stereo).
    
* Video codec: HEVC or H264, progressive scan, closed GOP, 4:2:0 chroma subsampling.
    
* Frame rate: 23-60 FPS.
    
* Picture size:
    
    * Maximum columns (horizontal pixels): 1920
        
    * Required aspect ratio is between 0.1:1 and 10:1 but we recommend 9:16 to avoid cropping or blank space
        
    
* Video bitrate: VBR, 25Mbps maximum
    
* Audio bitrate: 128kbps
    
* Duration: 60 seconds maximum, 3 seconds minimum
    
* File size: 100MB maximum
    

### Request Syntax

#### Image Containers

POST https://graph.facebook.com/{api-version}/{ig-user-id}/media
  ?image\_url={image-url}
  &is\_carousel\_item={is-carousel-item}
  &caption={caption}
  &location\_id={location-id}
  &user\_tags={user-tags}
  &product\_tags={product-tags}
  &access\_token={access-token}

#### Reel Containers

POST https://graph.facebook.com/{api-version}/{ig-user-id}/media
?media\_type=REELS
&video\_url={reel-url}
&caption={caption}
&share\_to\_feed={share-to-feed}
&collaborators={collaborator-usernames}
&cover\_url={cover-url}
&audio\_name={audio-name}
&user\_tags={user-tags}
&location\_id={location-id}
&thumb\_offset={thumb-offset}
&share\_to\_feed={share-to-feed}
&access\_token={access-token}

#### Carousel Containers

Carousel containers only. To create carousel item containers, create image or video containers instead (reels are not supported). See [Carousel Posts](https://developers.facebook.com/docs/instagram-api/guides/content-publishing#carousel-posts) for complete publishing steps.

POST https://graph.facebook.com/{api-version}/{ig-user-id}/media
?media\_type=CAROUSEL
&caption={caption}
&share\_to\_feed={share-to-feed}
&collaborators={collaborator-usernames}
&location\_id={location-id}
&product\_tags={product-tags}
&children={children}
&access\_token={access-token}

### Image Story Containers

POST https://graph.facebook.com/{api-version}/{ig-user-id}/media
  ?image\_url={image-url}
  &media\_type=STORIES
  &access\_token={access-token}

### Video Story Containers

POST https://graph.facebook.com/{api-version}/{ig-user-id}/media
  ?video\_url={video-url}
  &media\_type=STORIES
  &access\_token={access-token}

### Path Parameters

| Placeholder | Value |
| --- | --- |
| `{api-version}` | API [version](https://developers.facebook.com/docs/graph-api/guides/versioning). |
| `{ig-user-id}`  <br>Required | App user's app-scoped user ID. |

### Query String Parameters

| Key | Placeholder | Description |
| --- | --- | --- |
| `access_token` | `{access-token}` | Required. App user's [User](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) access token. |
| `audio_name` | `{audio-name}` | **For Reels only.** Name of the audio of your Reels media. You can only rename once, either while creating a reel or after from the audio page. |
| `caption` | `{caption}` | A caption for the image, video, or carousel. Can include hashtags (example: `#crazywildebeest`) and usernames of Instagram users (example: `@natgeo`). @Mentioned Instagram users receive a notification when the container is published. Maximum 2200 characters, 30 hashtags, and 20 @ tags.<br><br>  <br><br>**Not supported on images or videos in carousels**. |
| `collaborators` | `{caption}` | For Feed image, Reels and Carousels only. A list of up to 3 instagram usernames as collaborators on an ig media.<br><br>  <br><br>**Not supported for Stories.** |
| `children` | `{children}` | **Required for carousels. Applies only to carousels**. An array of up to 10 container IDs of each image and video that should appear in the published carousel. Carousels can have up to 10 total images, vidoes, or a mix of the two. |
| `cover_url` | `{cover-url}` | For Reels only. The path to an image to use as the cover image for the Reels tab. We will cURL the image using the URL that you specify so the image must be on a public server. If you specify both `cover_url` and `thumb_offset`, we use `cover_url` and ignore `thumb_offset`. The image must conform to the [specifications for a Reels cover photo](#reels-specs). |
| `image_url` | `{image-url}` | For images only and required for images. The path to the image. We will cURL the image using the URL that you specify so the image must be on a public server. |
| `is_carousel_item` | `{is-carousel-item}` | **Applies only to images and video**. Set to `true`. Indicates image or video appears in a carousel. |
| `location_id` | `{location-id}` | The ID of a [Page](https://developers.facebook.com/docs/graph-api/reference/page) associated with a location that you want to tag the image or video with.<br><br>  <br><br>Use the [Pages Search API](https://developers.facebook.com/docs/pages/searching) to search for [Pages](https://developers.facebook.com/docs/graph-api/reference/page) whose names match a search string, then parse the results to identify any Pages that have been created for a physical location. Include the `location` field in your query and verify that the Page you want to use has location data. Attempting to create a container using a Page that has no location data will fail with coded exception `INSTAGRAM_PLATFORM_API__INVALID_LOCATION_ID`.<br><br>  <br><br>**Not supported on images or videos in carousels**. |
| `media_type` | `{media-type}` | **Required for carousels, stories, and reels.** Indicates container is for a carousel, story or reel. Value can be:<br><br>* `CAROUSEL`<br>* `REELS`<br>* `STORIES` |
| `product_tags` | `{product-tags}` | **Required for product tagging. Applies only to images and videos**. An array of objects specifying which product tags to tag the image or video with (maximum of 5; tags and product IDs must be unique). Each object should have the following information:<br><br>  <br><br>* `product_id` — **Required.** Product ID.<br>* `x` — **Images only.** An optional float that indicates percentage distance from left edge of the published media image. Value must be within `0.0`–`1.0` range.<br>* `y` — **Images only.** An optional float that indicates percentage distance from top edge of the published media image. Value must be within `0.0`–`1.0` range.<br><br>For example:<br><br>  <br><br>`[{product_id:'3231775643511089',x: 0.5,y: 0.8}]` |
| `share_to_feed` | `{share-to-feed}` | For Reels only. When `true`, indicates that the reel can appear in both the **Feed** and **Reels** tabs. When `false`, indicates the reel can only appear in the **Reels** tab.<br><br>Neither value determines whether the reel actually appears in the **Reels** tab because the reel may not meet eligibilty requirements or may not be selected by our algorithm. See [reel specifications](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media#reel-specifications) for eligibility critera. |
| `thumb_offset` | `{thumb-offset}` | For videos and reels. Location, in milliseconds, of the video or reel frame to be used as the cover thumbnail image. The default value is `0`, which is the first frame of the video or reel. For reels, if you specify both `cover_url` and `thumb_offset`, we use `cover_url` and ignore `thumb_offset`. |
| `user_tags` | `{user-tags}` | **Required for user tagging. Applies to images and videos.** An array of public usernames and `x`/`y` coordinates for any public Instagram users who you want to tag in the image. Each object should have the following information:<br><br>* `usernames` — **Required.** Public usernames.<br>* `x` — **Images only.** An optional float that indicates percentage distance from left edge of the published media image. Value must be within `0.0`–`1.0` range.<br>* `y` — **Images only.** An optional float that indicates percentage distance from top edge of the published media image. Value must be within `0.0`–`1.0` range. |
| `video_url` | `{video-url}` | **Required for videos and reels. Applies only to videos and reels.** Path to the video. We cURL the video using the passed-in URL, so it must be on a public server. |

### Response

A JSON-formatted object containing an [IG Container](https://developers.facebook.com/docs/instagram-api/reference/ig-container) ID which you can use to [publish](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media_publish) the container.

Video uploads are asynchronous, so receiving a container ID does not guarantee that the upload was successful. To verify that a video has been uploaded, request the [`status_code`](https://developers.facebook.com/docs/instagram-api/reference/ig-container#fields) field on the IG Container. If its value is `FINISHED`, the video was uploaded successfully.

{
  "id":"{ig-container-id}"
}

### Sample Request

POST graph.facebook.com/17841400008460056/media
  ?image\_url=https//www.example.com/images/bronzed-fonzes.jpg
  &caption=#BronzedFonzes!
  &collaborators= \[‘username1’,’username2’\]
  &user\_tags=\[
    {
      username:'kevinhart4real',
      x: 0.5,
      y: 0.8
    },
    {
      username:'therock',
      x: 0.3,
      y: 0.2
    }
  \]

### Sample Response

{
  "id": "17889455560051444"
}

Reading
-------

**`GET /{ig-user-id}/media`**

Get all [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) on an [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user).

### Limitations

* Returns a maximum of 10K of the most recently created media.
* Story IG Media not supported, use the [`GET /{ig-user-id}/stories`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/stories) endpoint instead.

### Requirements

| Type | Description |
| --- | --- |
| [Access Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) | [User](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) |
| [Permissions](https://developers.facebook.com/docs/apps/review/login-permissions) | [`instagram_basic`](https://developers.facebook.com/docs/facebook-login/permissions#reference-instagram_basic)  <br>[`pages_read_engagement`](https://developers.facebook.com/docs/facebook-login/permissions#reference-pages_read_engagement) or [`pages_show_list`](https://developers.facebook.com/docs/facebook-login/permissions#reference-pages_show_list)<br><br>  <br><br>If the app user was granted a role on the Page via the Business Manager, you will also need one of:<br><br>  <br><br>[`ads_management`](https://developers.facebook.com/docs/permissions/reference/ads_management)  <br>[`business_management`](https://developers.facebook.com/docs/permissions/reference/business_management) |

### Time-based Pagination

This endpoint supports [time-based pagination](https://developers.facebook.com/docs/graph-api/results#time). Include `since` and `until` query-string parameters with Unix timestamp or `strtotime` data values to define a time range.

### Sample Request

GET graph.facebook.com/17841405822304914/media

### Sample Response

{
  "data": \[
    {
      "id": "17895695668004550"
    },
    {
      "id": "17899305451014820"
    },
    {
      "id": "17896450804038745"
    },
    {
      "id": "17881042411086627"
    },
    {
      "id": "17869102915168123"
    }
  \]
}

Updating
--------

This operation is not supported.

Deleting
--------

This operation is not supported.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

IG User Media Publish
=====================

Publish an [IG Container](https://developers.facebook.com/docs/instagram-api/reference/ig-container) on an Instagram Business [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user). Refer to the [Content Publishing](https://developers.facebook.com/docs/instagram-api/guides/content-publishing) guide for complete publishing steps.

Creating
--------

**`POST /{ig-user-id}/media_publish`**

Publish an [IG Container](https://developers.facebook.com/docs/instagram-api/reference/ig-container) object on an Instagram Business [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user).

### Limitations

* Instagram accounts are limited to 25 API-published posts within a 24 hour moving period.
* If the [Page](https://developers.facebook.com/docs/instagram-api/overview#pages) connected to the targeted Instagram Business account requires [Page Publishing Authorization](https://www.facebook.com/business/m/one-sheeters/page-publishing-authorization) (PPA), PPA must be completed or the request will fail.
* If the Page connected to the targeted Instagram Business account requires two-factor authentication, the Facebook User must also have performed two-factor authentication or the request will fail.
* Publishing to Instagram TV is not supported.

### Requirements

| Type | Description |
| --- | --- |
| [Access Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) | [User](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) |
| [Business Roles](https://www.facebook.com/business/help/442345745885606) | If publishing containers for [product tagging](https://developers.facebook.com/docs/instagram-api/guides/product-tagging), the app user must have an admin role on the [Business Manager](https://business.facebook.com/) that owns the IG User's [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322&h=AT1rJVCFEiavGpZxcYued2SkwsYEiUTmOqfsFckgWzq4L6EU6EeFtmMFL2kL-kuNfNxd6ImNtzW_5plZeKKNv6ZMmkKT1xxisSb274IW-vzbmV89iv233Mlpc4qTqCgTbibVGgv7QZ_GyV2K). |
| [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT0eu9NEAb2X0zuI31hDko9oFvT19828XwXeRcn-0_xPo1IKuErkrBH08I7FJ-0BujwNhasFwolyzCZaZ3Jgn_HalW9sWZvns_3qp3XzS-4bNKsVk5ElNDX4NnBKR7g5ObIb92B0g_3D2lsp) | If publishing containers for [product tagging](https://developers.facebook.com/docs/instagram-api/guides/product-tagging), the IG User must have an approved [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT0oydNpzHZIW0ZBCJxVkvb7PiguAN5IqHYxu9OR3YOB3KlcWCS1dZYy5OxeMp7Zho4cUNM25AB0Xzobv9zwcnsbze8F-whaewoBHaKWylK7Wxv-wFmsJRsk-85txCi1gLk126dyqgpvFmlX) with a product catalog containing products. |
| [Permissions](https://developers.facebook.com/docs/apps/review/login-permissions) | [`instagram_basic`](https://developers.facebook.com/docs/facebook-login/permissions#reference-instagram_basic)  <br>[`instagram_content_publish`](https://developers.facebook.com/docs/permissions/reference/instagram_content_publish)  <br>[`pages_read_engagement`](https://developers.facebook.com/docs/facebook-login/permissions#reference-pages_read_engagement) or [`pages_show_list`](https://developers.facebook.com/docs/facebook-login/permissions#reference-pages_show_list)<br><br>  <br><br>If the app user was granted a role on the Page via the Business Manager, you will also need one of:<br><br>  <br><br>[`ads_management`](https://developers.facebook.com/docs/permissions/reference/ads_management)  <br>[`business_management`](https://developers.facebook.com/docs/permissions/reference/business_management)<br><br>  <br><br>If publishing containers for [product tagging](https://developers.facebook.com/docs/instagram-api/guides/product-tagging), you will also need:<br><br>  <br><br>[`catalog_management`](https://developers.facebook.com/docs/permissions/reference/catalog_management)  <br>[`instagram_shopping_tag_products`](https://developers.facebook.com/docs/permissions/reference/instagram_shopping_tag_products) |
| [Tasks](https://developers.facebook.com/docs/instagram-api/overview#tasks) | The app user whose token is used in the request must be able to perform `MANAGE` or `CREATE_CONTENT` tasks on the [Page](https://developers.facebook.com/docs/instagram-api/overview#pages) connected to the targeted Instagram account. |

### Request Syntax

POST https://graph.facebook.com/{api-version}/{ig-user-id}/media\_publish
  ?creation\_id={creation-id}
  &access\_token={access-token}

### Path Parameters

| Placeholder | Value |
| --- | --- |
| `{api-version}`  <br>_String_ | API [version](https://developers.facebook.com/docs/graph-api/guides/versioning). |
| `{ig-user-id}`  <br>**Required**  <br>_String_ | App user's app-scoped user ID. |

### Query String Parameters

| Key | Placeholder | Description |
| --- | --- | --- |
| `access_token`<br><br>Required | `{access-token}` | The app user's [User](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) access token. |
| `creation_id`<br><br>Required | `{creation-id}` | The ID of the [IG Container](https://developers.facebook.com/docs/instagram-api/reference/ig-container) to be published. |

### Sample Request

POST graph.facebook.com
  /17841405822304914/media\_publish
    ?creation\_id=17889455560051444

### Sample Response

{
  "id": "17920238422030506"
}

Reading
-------

This operation is not supported.

Updating
--------

This operation is not supported.

Deleting
--------

This operation is not supported.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

IG User Mentions
================

This edge allows you to create an [IG Comment](https://developers.facebook.com/docs/instagram-api/reference/ig-comment) on an [IG Comment](https://developers.facebook.com/docs/instagram-api/reference/ig-comment) or captioned [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object that an [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) has been @mentioned in by another Instagram user.

Creating
--------

### Replying to a Captioned IG Media Object

`POST /{ig-user-id}/mentions?media_id={media_id}&message={message}`

Creates an [IG Comment](https://developers.facebook.com/docs/instagram-api/reference/ig-comment) on an [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object in which an [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) has been @mentioned in a caption.

#### Limitations

* Mentions on Stories are not supported.
* Commenting on photos in which you were tagged is not supported.
* Webhooks will not be sent if the Media upon which the comment or @mention appears was created by an account that is set to private.

#### Query String Parameters

Query string parameters are optional unless indicated as required.

* `{media_id}` (required) — the media ID contained in the [Webhook notification](https://developers.facebook.com/docs/instagram-api/guides/webhooks#reply-caption-mention) payload
* `{message}` (required) — text to include in the commment

#### Permissions

A Facebook User [access token](https://developers.facebook.com/docs/instagram-api/overview#authentication) with the following permissions:

* `instagram_basic`
* `instagram_manage_comments`
* `pages_read_engagement`
* `pages_show_list`

If the token is from a User whose **Page role was granted via the Business Manager**, one of the following permissions is also required:

* `ads_management`
* `pages_read_engagement`
* `business_management`

#### Sample cURL Request

curl -i -X POST \\
 -d "media\_id=17920112008063024" \\
 -d "message=Thanks%20for%20the%20dinosaur!" \\
 -d "access\_token=a-valid-access-token-goes-here" \\
 "https://graph.facebook.com/17841405309211844/mentions"

#### Sample Response

{
  "id": "17846319838228163"
}

### Replying to a Comment

`POST /{ig-user-id}/mentions?media_id={media_id}&comment_id={comment_id}&message={message}`

Creates an [IG Comment](https://developers.facebook.com/docs/instagram-api/reference/ig-comment) on an [IG Comment](https://developers.facebook.com/docs/instagram-api/reference/ig-comment) in which an [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) has been @mentioned.

#### Limitations

* Mentions on Stories are not supported.
* Commenting on photos in which you were tagged is not supported.
* Webhooks will not be sent if the Media upon which the comment or @mention appears was created by an account that is set to private.

#### Query String Parameters

Query string parameters are optional unless indicated as required.

* `{comment_id}` (required) — the comment ID contained in the [Webhook notification](https://developers.facebook.com/docs/instagram-api/guides/webhooks#reply-comment-mention) payload
* `{media_id}` (required) — the media ID contained in the [Webhook notification](https://developers.facebook.com/docs/instagram-api/guides/webhooks#reply-caption-mention) payload
* `{message}` (required) — text to include in the commment

#### Permissions

A Facebook User [access token](https://developers.facebook.com/docs/instagram-api/overview#authentication) with the following permissions:

* `instagram_basic`
* `instagram_manage_comments`
* `pages_read_engagement`
* `pages_show_list`

If the token is from a User whose **Page role was granted via the Business Manager**, one of the following permissions is also required:

* `ads_management`
* `pages_read_engagement`
* `business_management`

#### Parameters

* `comment_id` (required)
* `media_id` (required)
* `message`

#### Sample cURL Request

curl -i -X POST \\
 -d "media\_id=17920112008063024" \\
 -d "comment\_id=17918718562020960" \\
 -d "message=Hope%20you%20enjoy%20your%20new%20T-Rex!" \\
 -d "access\_token=a-valid-access-token-goes-here" \\
 "https://graph.facebook.com/17841405309211844/mentions"

#### Sample Response

{
  "id": "17846319838254687"
}

Reading
-------

This operation is not supported.

Updating
--------

This operation is not supported.

Deleting
--------

This operation is not supported.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

IG User Mentioned Comment
=========================

Returns data on an [IG Comment](https://developers.facebook.com/docs/instagram-api/reference/ig-comment) in which an [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) has been @mentioned by another Instagram user.

Creating
--------

This operation is not supported.

Reading
-------

**`GET /{ig-user-id}?fields=mentioned_comment.comment_id`**

Returns data on an [IG Comment](https://developers.facebook.com/docs/instagram-api/reference/ig-comment) in which an [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) has been @mentioned by another Instagram user.

### Limitations

This endpoint will return an error if comments have been disabled on the [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) on which the [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) has been @mentioned.

### Requirements

| Type | Description |
| --- | --- |
| [Access Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) | [User](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) |
| [Permissions](https://developers.facebook.com/docs/apps/review/login-permissions) | [`instagram_basic`](https://developers.facebook.com/docs/permissions/reference/instagram_basic)  <br>[`instagram_manage_comments`](https://developers.facebook.com/docs/permissions/reference/instagram_manage_comments)  <br>[`pages_read_engagement`](https://developers.facebook.com/docs/permissions/reference/pages_read_engagement)  <br>[`pages_show_list`](https://developers.facebook.com/docs/permissions/reference/pages_show_list)<br><br>  <br><br>If the app user was granted a role on the Page via the Business Manager, you will also need one of:<br><br>  <br><br>[`ads_management`](https://developers.facebook.com/docs/permissions/reference/ads_management)  <br>[`business_management`](https://developers.facebook.com/docs/permissions/reference/business_management) |
| [Tasks](https://developers.facebook.com/docs/instagram-api/overview#tasks) | `MANAGE`, `CREATE_CONTENT`, or `MODERATE` |

### Request Syntax

GET https://graph.facebook.com/`v18.0`/{ig-user-id}
  ?fields=mentioned\_comment.comment\_id({comment-id}){{fields}}
  &access\_token={access-token}

### Query String Parameters

| Parameter | Value |
| --- | --- |
| `{access_token}`  <br>**Required**  <br>_String_ | The app user's User Access Token. |
| `{comment-id}`  <br>**Required**  <br>_String_ | The ID of the IG Comment in which the IG User has been @mentioned. The ID is included in the [Webhook notification](https://developers.facebook.com/docs/instagram-api/guides/webhooks#reply-comment-mention) payload. |
| `{fields}`  <br>_Comma-separated list_ | A comma-separated list of IG Comment [Fields](#fields) you want returned. If omitted, default fields will be returned. |

### Fields

| Field | Description |
| --- | --- |
| `id`  <br>**Default**  <br>_String_ | ID of the IG Comment. |
| `like_count`  <br>_String_ | Number of times the IG Comment has been liked. |
| `media`  <br>_String_ | ID of the IG Media on which the IG Comment was made. Use [Field Expansion](#field-expansion) to get additional fields on the returned IG Media entity. |
| `text`  <br>**Default**  <br>_String_ | Text of the IG Comment. |
| `timestamp`  <br>**Default**  <br>_String_ | IG Comment creation date formatted in ISO 8601. |

### Response

### Sample Request

curl -X GET \\
  'https://graph.facebook.com/`v18.0`/17841405309211844?fields=mentioned\_comment.comment\_id(17873440459141021){timestamp,like\_count,text,id}&access\_token=IGQVJ...'

#### Sample Response

{
  "mentioned\_comment": {
    "timestamp": "2017-05-03T16:09:08+0000",
    "like\_count": 185,
    "text": "Shout out to @metricsaurus",
    "id": "17873440459141021"
  },
  "id": "17841405309211844"
}

### Field Expansion

You can expand the `media` field with a list of [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) fields to get additional data on the IG Media entity on which the comment was made. For example:

media{id,media\_url}

**v10.0 and older calls until September 7, 2021:** The [`like_count`](https://developers.facebook.com/docs/instagram-api/reference/ig-media#fields) field on an IG Media will return `0` if the media [owner](https://developers.facebook.com/docs/instagram-api/overview#authorization) has [hidden](https://www.facebook.com/help/instagram/113355287252104) like counts on it.

**v11.0+ calls, and all versions on September 7, 2021:** If indirectly querying an [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) through another endpoint or field expansion, the [`like_count`](https://developers.facebook.com/docs/instagram-api/reference/ig-media#fields) field will be omitted from API responses if the media owner has hidden like counts on it. Directly querying the IG Media (which can only be done by the IG Media owner) will return the actual like count, however, even if like counts have been hidden.

#### Sample Field Expansion Request

curl -X GET \\
  'https://graph.facebook.com/`v18.0`/17841405309211844?fields=mentioned\_comment.comment\_id(17873440459141021){timestamp,like\_count,text,media{id,media\_url}}&access\_token=IGQVJ...'

#### Sample Field Expansion Response

{
  "mentioned\_comment": {
    "timestamp": "2017-05-03T16:09:08+0000",
    "like\_count": 185,
    "text": "Shout out to @metricsaurus",
    "id": "17873440459141021",
    "media": {
      "id": "17895695668004550",
      "media\_url": "https://scont..."
    }
  },
  "id": "17841405309211844"
}

### Pagination

If you are using field expansion to access an edge that supports [cursor-based pagination](https://developers.facebook.com/docs/graph-api/using-graph-api#paging), the response will include `before` and `after` cursors if the response contains multiple pages of data. Unlike standard cursor-based pagination, however, the response will not include `previous` or `next` fields, so you will have to use the `before` and `after` cursors to construct `previous` and `next` query strings manually in order to page through the returned data set.

Updating
--------

This operation is not supported.

Deleting
--------

This operation is not supported.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

Mentioned Media
===============

Returns data on an [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) in which an [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) has been @mentioned in a caption by another Instagram user.

Creating
--------

This operation is not supported.

Reading
-------

**`GET /{ig-user-id}?fields=mentioned_media.media_id`**

Returns data on an [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) in which an [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) has been @mentioned in a caption by another Instagram user.

### Limitations

* Mentions on Stories are not supported.
* Commenting on photos in which you were tagged is not supported.
* Webhooks will not be sent if the Media upon which the comment or @mention appears was created by an account that is set to private.

### Requirements

| Type | Description |
| --- | --- |
| [Access Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) | [User](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) |
| [Permissions](https://developers.facebook.com/docs/apps/review/login-permissions) | [`instagram_basic`](https://developers.facebook.com/docs/permissions/reference/instagram_basic)  <br>[`instagram_manage_comments`](https://developers.facebook.com/docs/permissions/reference/instagram_manage_comments)  <br>[`pages_read_engagement`](https://developers.facebook.com/docs/permissions/reference/pages_read_engagement)  <br>[`pages_show_list`](https://developers.facebook.com/docs/permissions/reference/pages_show_list)<br><br>  <br><br>If the app user was granted a role on the Page via the Business Manager, you will also need one of:<br><br>  <br><br>[`ads_management`](https://developers.facebook.com/docs/permissions/reference/ads_management)  <br>[`business_management`](https://developers.facebook.com/docs/permissions/reference/business_management) |
| [Tasks](https://developers.facebook.com/docs/instagram-api/overview#tasks) | `MANAGE`, `CREATE_CONTENT`, or `MODERATE` |

### Request Syntax

GET https://graph.facebook.com/`v18.0`/{ig-user-id}
  ?fields=mentioned\_media.media\_id({media-id}){{fields}}
  &access\_token={access-token}

### Query String Parameters

| Parameter | Value |
| --- | --- |
| `{access_token}`  <br>**Required**  <br>_String_ | The app user's User Access Token. |
| `{fields}`  <br>_Comma-separated list_ | A comma-separated list of IG Media [Fields](#fields) you want returned. If omitted, default Fields will be returned. |
| `{media-id}`  <br>**Required**  <br>_String_ | The ID of the IG Media in which the IG User has been @mentioned in a caption. The ID is included in the [Webhook notification](https://developers.facebook.com/docs/instagram-api/guides/webhooks#reply-comment-mention) payload. |

### Fields

| Field | Description |
| --- | --- |
| `caption`  <br>_String_ | The caption text. Captions that @mention an IG User will not include the `@` symbol unless the app user created the IG Media object upon which the caption was made. |
| `comments`  <br>_Object_ | A list of IG Comments on the IG Media. If using Field Expansion to get the comment text, text that @mentions an IG User will not include the `@` symbol unless the app user created the IG Media object upon which the caption was made. |
| `comments_count`  <br>_String_ | Number of IG Comments on the IG Media. |
| `id`  <br>**Default**  <br>_String_ | ID of the IG Media. |
| `like_count`  <br>_String_ | Count of likes on the media. Excludes likes on album child media and likes on promoted posts created from the media. Includes replies on comments.<br><br>  <br><br>* **v10.0 and older calls:** value will be `0` if the media owner has [hidden](https://www.facebook.com/help/instagram/113355287252104) like counts it.<br>* **v11.0+ calls:** field will be omitted if media owner has hidden like counts in it Value will be `0` if the media owner has [hidden](https://www.facebook.com/help/instagram/113355287252104) like counts it. |
| `media_type`  <br>_String_ | The IG Media's type: `CAROUSEL_ALBUM`, `IMAGE`, `STORY`, or `VIDEO`. |
| `media_url`  <br>_String_ | URL of the published IG Media. |
| `owner`  <br>_String_ | ID of the IG User who created the IG Media. Only returned if the app user created the IG Media object, otherwise the `username` field will be returned instead. |
| `timestamp`  <br>_String_ | Creation date of IG Media formatted in ISO 8601. |
| `username`  <br>_String_ | Username of the IG User who created the IG Media. |

### Sample Request

curl -X GET \\
  'https://graph.facebook.com/`v18.0`/17841405309211844?fields=mentioned\_media.media\_id(17873440459141021){caption,media\_type}&access\_token=IGQVJ...'

### Sample Response

{
  "mentioned\_media": {
    "caption": "metricsaurus headquarters!",
    "media\_type": "IMAGE",
    "id": "17873440459141021"
  },
  "id": "17841405309211844"
}

Note that in the sample above, the API has stripped out the leading `@` symbol from the original caption (@metricsaurus headquarters!) because the app user did not create the caption.

### Pagination

If you are using field expansion to access an edge that supports [cursor-based pagination](https://developers.facebook.com/docs/graph-api/using-graph-api#paging), the response will include `before` and `after` cursors if the response contains multiple pages of data. Unlike standard cursor-based pagination, however, the response will not include `previous` or `next` fields, so you will have to use the `before` and `after` cursors to construct `previous` and `next` query strings manually in order to page through the returned data set.

Updating
--------

This operation is not supported.

Deleting
--------

This operation is not supported.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

IG User Product Appeal
======================

Represents a rejected product's appeal status. See [Product Tagging](https://developers.facebook.com/docs/instagram-api/guides/product-tagging) guide for complete usage details.

Creating
--------

**`POST /{ig-user-id}/product_appeal`**

Appeal a rejected product.

### Limitations

* Instagram Creator accounts are not supported.
* Stories, Instagram TV, Reels, Live, and Mentions are not supported.

### Requirements

| Type | Requirement |
| --- | --- |
| [Access Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens/) | [User](https://developers.facebook.com/docs/facebook-login/access-tokens/#usertokens) |
| [Business Roles](https://www.facebook.com/business/help/442345745885606) | The app user must have an admin role on the [Business Manager](https://business.facebook.com/) that owns the IG User's [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322&h=AT19cPTf4a_hGTX6P46kAKqX3Burs9zXi1Ut-e2wiXYmGWJej89WtAw_rRYMkUqaKqD-2XskNj2zbBApV1W8ZSp5RPT1K6j9OgvsLLRIJBNGB98s3ttlobdbD_-ukRsyuMISaED8tsxcUb1W). |
| [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT12fqyWHHYCzxSnV8plgsesRWqCzJixwxYi0QSMNr5Wb0krDP3mpR92yvUmIyyIQIcZvG8KcrERsHTBd1SCDcfhx82oIZ-rderYe6Kj5PlNxZJe1sBYVoyCvIrdtLZDC3bjKc5ZdddVK-TO) | The IG User must have an approved [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT18k9kOahoUk4cdYkCYiLRh-mD-ax02o1kQkAwzzDQLeLJHkze9S9pbYmjIvD8aEAYNodWmfO0pHRAXapyXghwrJK82mvEdz8dnrkZ78qx5d0MtbD-sbFConZaQvw-FEnSqown3W0LiShO7) with a product catalog containing products. |
| [Permissions](https://developers.facebook.com/docs/permissions/reference) | [`catalog_management`](https://developers.facebook.com/docs/permissions/reference/catalog_management)  <br>[`instagram_basic`](https://developers.facebook.com/docs/permissions/reference/instagram_basic)  <br>[`instagram_shopping_tag_products`](https://developers.facebook.com/docs/permissions/reference/instagram_shopping_tag_products)  <br>[`pages_show_list`](https://developers.facebook.com/docs/permissions/reference/pages_show_list)<br><br>  <br><br>If the app user was granted a role via the Business Manager on the [Page](https://developers.facebook.com/docs/instagram-api/overview#pages) connected to the targeted IG User, you will also need one of:<br><br>  <br><br>[`ads_management`](https://developers.facebook.com/docs/permissions/reference/ads_management)  <br>[`business_management`](https://developers.facebook.com/docs/permissions/reference/business_management) |

### Request Syntax

POST https://graph.facebook.com/{api-version}/{ig-user-id}/product\_appeal
  ?appeal\_reason={appeal-reason}
  &product\_id={product-id}
  &access\_token={access-token}

### Path Parameters

| Placeholder | Value |
| --- | --- |
| `{api-version}` | API [version](https://developers.facebook.com/docs/instagram-basic-display-api/overview#versions). |
| `{ig-user-id}` | **Required.** App user's app-scoped user ID. |

### Query String Parameters

| Key | Placeholder | Value |
| --- | --- | --- |
| `access_token` | `{access-token}` | **Required.** App user's [User](https://developers.facebook.com/docs/facebook-login/access-tokens/#usertokens) access token. |
| `appeal_reason` | `{appeal-reason}` | **Required.** Explanation of why the product should be approved. |
| `product_id` | `{product-id}` | **Required.** Product ID. |

### Response

An object indicating success or failure. Response does not indicate appeal outcome.

{
  "success": {success}
}

#### Response Contents

| Property | Value |
| --- | --- |
| `success` | Indicates if API accepted request (`true`) or did not accept request (`false`). Response does not indicate appeal outcome. |

### cURL Example

#### Request

curl -i -X POST \\
 "https://graph.facebook.com/`v18.0`/90010177253934/product\_appeal?appeal\_reason=product%20is%20a%20toy%20and%20not%20a%20real%20weapon&product\_id=4382881195057752&access\_token=EAAOc..."

#### Response

{
  "success": true
}

Reading
-------

**`GET /{ig-user-id}/product_appeal`**

Get appeal status of a rejected product.

### Limitations

* Instagram Creator accounts are not supported.
* Stories, Instagram TV, Reels, Live, and Mentions are not supported.

### Requirements

| Type | Requirement |
| --- | --- |
| [Access Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens/) | [User](https://developers.facebook.com/docs/facebook-login/access-tokens/#usertokens) |
| [Business Roles](https://www.facebook.com/business/help/442345745885606) | The app user must have an admin role on the [Business Manager](https://business.facebook.com/) that owns the IG User's [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322&h=AT2JHruDamfaitQDu7xOnGgL19BYq2MUGTgu7VdCsv-Kw-jEm04AikUwcoZxO3GFwBWJTv1kDCNOAkWYIHfaUmDYWkp6zIglYAzYIvNM6l9uSr_TwV7RDhbi7PyOEuT5mouSOfrFcrfYy_JX). |
| [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT3mq6lKIhQHDfABWn5B8F0A5YAO4CkHLYGpdKSxuOmj6Uj7uBg1mkSDadisxztiHaMd1lkIpMTYIhj0zo9e71uly6kmch3ynu7VJ8SXx_vEQw567H6obIF7h-U_MuCzPkrKv3o4HqzEVbTs) | The IG User must have an approved [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT0GioGyG4rzsTJLB5ewuLqZRdjls7hkeGCLNGZUYlaGj9-By9fG0og_Cql12jr2NfbANlaCetHlu8Tj8g7QqR3gsxhS17Vt3AuTq2Sbn8EqzRaPgBoP1QJ1VBUKKLLWWAgvB9eH_MasDH_8) with a product catalog containing products. |
| [Permissions](https://developers.facebook.com/docs/permissions/reference) | [`catalog_management`](https://developers.facebook.com/docs/permissions/reference/catalog_management)  <br>[`instagram_basic`](https://developers.facebook.com/docs/permissions/reference/instagram_basic)  <br>[`instagram_shopping_tag_products`](https://developers.facebook.com/docs/permissions/reference/instagram_shopping_tag_products)  <br>[`pages_show_list`](https://developers.facebook.com/docs/permissions/reference/pages_show_list)<br><br>  <br><br>If the app user was granted a role via the Business Manager on the [Page](https://developers.facebook.com/docs/instagram-api/overview#pages) connected to the targeted IG User, you will also need one of:<br><br>  <br><br>[`ads_management`](https://developers.facebook.com/docs/permissions/reference/ads_management)  <br>[`business_management`](https://developers.facebook.com/docs/permissions/reference/business_management) |

### Request Syntax

GET https://graph.facebook.com/{api-version}/{ig-user-id}/product\_appeal
  ?product\_id={product-id}
  &access\_token={access-token}

### Path Parameters

| Placeholder | Value |
| --- | --- |
| `{api-version}` | API [version](https://developers.facebook.com/docs/instagram-basic-display-api/overview#versions). |
| `{ig-user-id}` | **Required.** App user's app-scoped user ID. |

### Query String Parameters

| Key | Placeholder | Value |
| --- | --- | --- |
| `access_token` | `{access-token}` | **Required.** App user's [User](https://developers.facebook.com/docs/facebook-login/access-tokens/#usertokens) access token. |
| `product_id` | `{product-id}` | **Required.** Product ID. |

### Response

A JSON-formatted object containing an array of appeal status metadata.

{
  "data": \[
    {
      "eligible\_for\_appeal": {eligible-for-appeal},
      "product\_id": {product-id},
      "review\_status": "{review-status}"
    }
  \]
}

#### Response Contents

| Property | Value |
| --- | --- |
| `eligible_for_appeal` | Indicates if decision can be appealed (yes if `true`, no if `false`). |
| `product_id` | Product ID. |
| `review_status` | Review status. Value can be:<br><br>  <br><br>* `approved` — Product is approved.<br>* `rejected` — Product was rejected<br>* `pending` — Still undergoing review.<br>* `outdated` — Product was approved but has been edited and requires reapproval.<br>* `""` — No review status.<br>* `no_review` — No review status. |

### cURL Example

#### Request

curl -i -X GET \\
 "https://graph.facebook.com/`v18.0`/90010177253934/product\_appeal?product\_id=4029274203846188&access\_token=EAAOc..."

#### Response

{
  "data": \[
    {
      "product\_id": 4029274203846188,
      "review\_status": "approved",
      "eligible\_for\_appeal": false
    }
  \]
}

Updating
--------

This operation is not supported.

Deleting
--------

This operation is not supported.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

Recently Searched Hashtags
==========================

This edge allows you to determine the [IG Hashtags](https://developers.facebook.com/docs/instagram-api/reference/ig-hashtag) that an [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) has queried for within the last 7 days.

Reading
-------

`GET /{ig-user-id}/recently_searched_hashtags`

Get the hashtags that an [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) has queried using the [IG Hashtags](https://developers.facebook.com/docs/instagram-api/reference/ig-hashtag) endpoint within the last 7 days.

IG Users can query a maximum of 30 unique hashtags within a rolling, 7 day period. A queried hashtag will count against that user's limit as soon as it is queried. Subsequent queries on that hashtag within 7 days of the initial query will not count against the user's limit.

**Limitations**

* Emojis in hashtag queries are not supported.
* The API returns 25 results per page by default, but you can use the `limit` parameter to get up to 30 per page (`limit=30`).

#### Requirements

| Type | Description |
| --- | --- |
| [Features](https://developers.facebook.com/docs/apps/review/feature) | [`Instagram Public Content Access`](https://developers.facebook.com/docs/apps/review/feature#reference-INSTAGRAM_PUBLIC_CONTENT_ACCESS) |
| [Permissions](https://developers.facebook.com/docs/apps/review/login-permissions) | [`instagram_basic`](https://developers.facebook.com/docs/facebook-login/permissions#reference-instagram_basic)<br><br>  <br><br>If the token is from a User whose Page role was granted via the Business Manager, one of the following permissions is also required: `ads_management`, `business_management`, or `pages_read_engagement`. |
| [Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens) | A Facebook User [access token](https://developers.facebook.com/docs/instagram-api/overview#authentication). |

#### Sample Request

GET graph.facebook.com/17841405309211844/recently\_searched\_hashtags?limit=30

#### Sample Response

{
  "data": \[
    {
      "id": "17841562906103814"
    },
    {
      "id": "17841563587120501"
    }
  \]
}

Creating
--------

This operation is not supported.

Updating
--------

This operation is not supported.

Deleting
--------

This operation is not supported.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

Stories
=======

Represents a collection of story [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) objects on an [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user).

Creating
--------

For creating Stories Media, refer to the [Instagram User Media](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media) documentation.

Reading
-------

### Getting Stories

`GET /{ig-user-id}/stories`

Returns a list of story [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) objects on an [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user).

#### Limitations

* Responses will not include Live Video stories.
* Stories are only available for 24 hours.
* New stories created when a user reshares a story will not be returned.

#### Permissions

A Facebook User [access token](https://developers.facebook.com/docs/instagram-api/overview#authentication) with the following permissions:

* `instagram_basic`
* `instagram_manage_insights`
* `pages_read_engagement`
* `pages_show_list`

If the token is from a User whose **Page role was granted via the Business Manager**, one of the following permissions is also required:

* `ads_management`
* `pages_read_engagement`
* `business_management`

#### Sample Request

GET graph.facebook.com
  /17841405822304914/stories

#### Sample Response

{
  "data": \[
    {
      "id": "17861937508009798"
    },
    {
      "id": "17862253585030136"
    },
    {
      "id": "17856428680064034"
    },
    {
      "id": "17862537148046301"
    },
    {
      "id": "17852121721080875"
    },
    {
      "id": "17862694123018235"
    }
  \]
}

Updating
--------

This operation is not supported.

Deleting
--------

This operation is not supported.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

Tags
====

Represents a collection of [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) objects in which an [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) has been tagged by another Instagram user.

Creating
--------

This operation is not supported.

Reading
-------

**`GET /{ig-user-id}/tags`**

Returns a list of [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) objects in which an [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) has been tagged by another Instagram user.

### Limitations

Private [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) objects will not be returned.

### Requirements

| Type | Description |
| --- | --- |
| [Access Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens) | [User](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) |
| [Features](https://developers.facebook.com/docs/apps/review/feature) | Not applicable. |
| [Permissions](https://developers.facebook.com/docs/apps/review/login-permissions) | [`instagram_basic`](https://developers.facebook.com/docs/facebook-login/permissions#reference-instagram_basic)  <br>[`instagram_manage_comments`](https://developers.facebook.com/docs/facebook-login/permissions#reference-instagram_manage_comments)  <br>[`pages_read_engagement`](https://developers.facebook.com/docs/pages/overview#permissions)<br><br>[`pages_show_list`](https://developers.facebook.com/docs/pages/overview#permissions)<br><br>  <br><br>If the token is from a User whose Page role was granted via the Business Manager, one of the following permissions is also required: [`ads_management`](https://developers.facebook.com/docs/facebook-login/permissions#reference-ads_management), [`business_management`](https://developers.facebook.com/docs/facebook-login/permissions#reference-business_management), or [`pages_read_engagement`](https://developers.facebook.com/docs/pages/overview#permissions). |
| [Tasks](https://developers.facebook.com/docs/instagram-api/overview#tasks) | The app user must be able to perform appropriate Tasks on the Page based on the Permissions requested by the app. |

### Request Syntax

GET https://graph.facebook.com/{ig-user-id}/tags
  ?fields={fields}
  &access\_token={access-token}

### Query String Parameters

Include the following query string parameters to augment the request.

| Key | Value |
| --- | --- |
| `access_token`  <br>**Required**  <br>_String_ | The app user's [Instagram User Access Token](https://developers.facebook.com/docs/instagram-basic-display-api/overview#instagram-user-access-tokens). |
| `fields`  <br>_Comma-separated list_ | A comma-separated list of [Fields](#fields) and [Edges](#edges) you want included in the response. If omitted, default fields will be returned. |

### Fields

Use the `fields` query string parameter to specify fields you want included on any returned [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media#read) objects.

**v10.0 and older calls until September 7, 2021:** The [`like_count`](https://developers.facebook.com/docs/instagram-api/reference/ig-media#fields) field on an IG Media will return `0` if the media [owner](https://developers.facebook.com/docs/instagram-api/overview#authorization) has [hidden](https://www.facebook.com/help/instagram/113355287252104) like counts on it.

**v11.0+ calls, and all versions on September 7, 2021:** If indirectly querying an [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) through another endpoint or field expansion, the [`like_count`](https://developers.facebook.com/docs/instagram-api/reference/ig-media#fields) field will be omitted from API responses if the media owner has hidden like counts on it. Directly querying the IG Media (which can only be done by the IG Media owner) will return the actual like count, however, even if like counts have been hidden.

### Edges

Use the `fields` query string parameter to specify Edges you want included on any returned [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media#read) objects.

### Response

A JSON-formatted object containing [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) objects.

{
  "{field}":"{value}",
  ...
}

### Pagination

This edge supports [cursor-based pagination](https://developers.facebook.com/docs/graph-api/using-graph-api#paging) so the response will include `before` and `after` cursors if the response contains multiple pages of data. Unlike standard cursor-based pagination, however, the response will not include `previous` or `next` fields, so you will have to use the `before` and `after` cursors to construct `previous` and `next` query strings manually in order to page through the returned data set.

### Sample Request

GET graph.facebook.com/17841405822304914/tags
    ?fields=id,username
    &access\_token=EAADd...

### Sample Response

{
  "data": \[
    {
      "id": "18038...",
      "username": "keldo..."
    },
    {
      "id": "17930...",
      "username": "ashla..."
    },
    {
      "id": "17931...",
      "username": "jaypo..."
    }
  \]
}

Updating
--------

This operation is not supported.

Deleting
--------

This operation is not supported.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

Page
====

Represents a Facebook Page.

This node allows you to:

* get the [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) connected to a Facebook Page.

Creating
--------

This operation is not supported.

Reading
-------

### Getting a Page's IG User

`GET /{page-id}?fields=instagram_business_account`

Returns the [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) connected to the Facebook Page.

#### Permissions

A Facebook User [access token](https://developers.facebook.com/docs/instagram-api/overview#authentication) with the following permissions:

* `instagram_basic`
* `pages_show_list`

If the token is from a User whose **Page role was granted via the Business Manager**, one of the following permissions is also required:

* `ads_management`
* `pages_read_engagement`
* `business_management`

#### Sample Request

GET graph.facebook.com
  /134895793791914?fields=instagram\_business\_account

#### Sample Response

{
  "instagram\_business\_account": {
    "id": "17841405822304914"
  },
  "id": "134895793791914"
}

Updating
--------

This operation is not supported.

Deleting
--------

This operation is not supported.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)