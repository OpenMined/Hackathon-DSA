This document refers to an outdated version of Graph API. Please [use the latest version.](https://developers.facebook.com/docs/graph-api/reference/v19.0/url)

URL `/?id={url}`
================

Represents a URL shared in a Post or in a Comment on a Post.

Refer to our [News Tab Indexing API](https://developers.facebook.com/docs/news-tab-indexing) documentation for additional information.

Reading
-------

Get information about a URL that was shared in a Post or a Comment on a Post.

### Requirements

| Type | Description |
| --- | --- |
| [Access Tokens](#) | Any access token can be used to make this request. |
| [Features](#) | Not applicable. |
| [Page Tasks](#) | Not applicable. |
| [Permissions](#) | Not applicable. |

### Limitations

* Engagement values returned are not precise but do reflect user engagement with a URL.
* You are limited to 10 GET requests per URL, per app, per hour.

### Parameters

Include the following query string parameters to augment the request.

| Parameter | Description |
| --- | --- |
| `access_token`<br><br>Required<br><br>_string_ | An [access token](#). |
| `fields`<br><br>_string_ | A comma-separated list of fields you want to request. |
| `id`<br><br>_string_ | The url to be shared. |
| `scopes`<br><br>_string_ | A comma-separated list of scopes. |

### Fields

| Property Name | Description | Type |
| --- | --- | --- |
| `app_links` | AppLinks data associated with this URL, if available. | `AppLinks` |
| `id` | The URL itself. | `string` |
| `engagement` | Counts of different ways people interacted with the URL Note that engagement values are intentionally not precise, but you can be confident they accurately reflect user engagement with a URL. | `object` |
| `comment_count` | Number of comments on the URL. | `int` |
| `comment_plugin_count` | Number of comments on the plugin gathered using the [Comments Plugin](https://developers.facebook.com/docs/plugins/comments/) on your site. | `int` |
| `reaction_count` | Number of reactions to the URL. | `int` |
| `share_count` | Number of times the URL was shared. | `int` |
| `og_object` | The [Open Graph object](https://developers.facebook.com/docs/opengraph/using-objects#selfhosted-canonical) that is canonically associated with this URL. | `OGObject` |
| `id` | ID of object. | `string` |
| `description` | The description of the object, if available. | `string` |
| `title` | The title of the object, if available. | `string` |
| `type` | The object type. | [`og:type`](https://developers.facebook.com/docs/opengraph/creating-custom-stories#objecttypes) |
| `updated_time` | When the object was last updated. | `datetime` |

### Examples

To get information about a URL published in a Post or Comment, send a `GET` request to `https://graph.facebook.com` with the `id` parameter set to the URL, any fields about the URL, and an access token requested from the User or Page who published the Post or Comment.

The follow example shows the engagement for the URL, https://www.facebook.com, that was shared by the User represented by the User access token.

_Formatted for readability._

curl -i -X GET \\
 "https://graph.facebook.com/{latest-graph-api-version}/
    ?id=https://www.facebook.com
    &fields=engagement
    &access\_token={user-access-token}"

On success your app receives the following engagement counts for the URL that was shared:

{
  "engagement": {
    "reaction\_count": 514919172,
    "comment\_count": 68687082,
    "share\_count": 975739682,
    "comment\_plugin\_count": 1641
  },
  "id": "https://www.facebook.com"
}

Creating
--------

You can't perform this operation on this endpoint.

Updating
--------

Update a URL.

### Requirements

| Type | Description |
| --- | --- |
| [Access Tokens](#) | Any access token can be used to make this request. |
| [Features](#) | Not applicable. |
| [Page Tasks](#) | Not applicable. |
| [Permissions](#) | Not applicable. |

### Examples

To update information about a URL published in a Post or Comment, send a `POST` request to `https://graph.facebook.com` with the `id` parameter set to the URL, the `scrape` parameter set to `true`, any `fields` about the URL, and an access token requested from the User or Page who published the Post or Comment.

The follow example updates the URL, https://www.facebook.com/my-update, that was shared by the User represented by the User access token.

_Formatted for readability._

curl -i -X POST \\
 "https://graph.facebook.com/{latest-graph-api-version}/
    ?id=https://www.facebook.com/my-update
    &scrape=true
    &access\_token={user-access-token}"

On success your app receives the following engagement counts for the URL that was shared:

{
  "success": true
}  

### Query String Parameters

Include the following query string parameters to augment the request.

| Parameter | Description |
| --- | --- |
| `access_token`<br><br>Required<br><br>_string_ | An [access token](#). |
| `fields`<br><br>_string_ | A comma-separated list of fields you want to request. |
| `id`<br><br>Required<br><br>_string_ | The url to be updated. The url must be [encoded](https://l.facebook.com/l.php?u=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FPercent-encoding&h=AT1gY4BblbIBuCB3dip-SeD_C-_61lJJG2vzlzcv3kcLes15aVBxnxKposQncImqGkirzgOyk1DHhESM_MU3AXVeKTtE0mUpcc67xvcQBk6DRIdxEMak2weeOGtaiUgHUmIKvOeoYvphCQJP) so that it does not interfere with the `scrape` parameter. |
| `scrape`<br><br>Required<br><br>_boolean_ | Value must be `true`. |

#### Example Request

POST /{version}/?id={url}&scrape=true
Host: graph.facebook.com

#### Example Response

{
  "success": true
}

Deleting
--------

You can't perform this operation on this endpoint.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)