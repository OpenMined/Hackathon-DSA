URL - Graph API - Documentation - Meta for Developers

Graph API* Overview
* Get Started
* Batch Requests
* Debug Requests
* Handle Errors
* Field Expansion
* Secure Requests
* Resumable Upload API
* Changelog
* Features Reference
* Permissions Reference
* Reference
This document refers to an outdated version of Graph API. Please use the latest version.Graph API Versionv18.0URL `/?id={url}`
================
Represents a URL shared in a Post or in a Comment on a Post.

Refer to our News Tab Indexing API documentation for additional information.

Reading
-------

Get information about a URL that was shared in a Post or a Comment on a Post.

### Requirements

 Type | Description || Access Tokens | Any access token can be used to make this request. |
| Features | Not applicable. |
| Page Tasks | Not applicable. |
| Permissions | Not applicable. |
### Limitations

* Engagement values returned are not precise but do reflect user engagement with a URL.
* You are limited to 10 GET requests per URL, per app, per hour.

### Parameters

Include the following query string parameters to augment the request.

 Parameter | Description || `access_token`
Required*string* | An access token. |
| `fields`
*string* | A comma-separated list of fields you want to request. |
| `id`
*string* | The url to be shared. |
| `scopes`
*string* | A comma-separated list of scopes. |
### Fields

 Property Name
  | 
 Description
  | 
 Type
  || `app_links` | AppLinks data associated with this URL, if available. | `AppLinks` |
| `id` | The URL itself. | `string` |
| `engagement` | Counts of different ways people interacted with the URL Note that engagement values are intentionally not precise, but you can be confident they accurately reflect user engagement with a URL. | `object` |
| `comment_count` | Number of comments on the URL. | `int` |
| `comment_plugin_count` | Number of comments on the plugin gathered using the Comments Plugin on your site. | `int` |
| `reaction_count` | Number of reactions to the URL. | `int` |
| `share_count` | Number of times the URL was shared. | `int` |
| `og_object` | The Open Graph object that is canonically associated with this URL. | `OGObject` |
| `id` | ID of object. | `string` |
| `description` | The description of the object, if available. | `string` |
| `title` | The title of the object, if available. | `string` |
| `type` | The object type. | `og:type` |
| `updated_time` | When the object was last updated. | `datetime` |
### Examples

To get information about a URL published in a Post or Comment, send a `GET` request to `https://graph.facebook.com` with the `id` parameter set to the URL, any fields about the URL, and an access token requested from the User or Page who published the Post or Comment.

The follow example shows the engagement for the URL, https://www.facebook.com, that was shared by the User represented by the User access token.

*Formatted for readability.*
```
curl -i -X GET \
 "https://graph.facebook.com/{latest-graph-api-version}/
    ?id=https://www.facebook.com
    &fields=engagement
    &access_token={user-access-token}"
```
On success your app receives the following engagement counts for the URL that was shared:

```
{
  "engagement": {
    "reaction_count": 514919172,
    "comment_count": 68687082,
    "share_count": 975739682,
    "comment_plugin_count": 1641
  },
  "id": "https://www.facebook.com"
}
```
Creating
--------
You can't perform this operation on this endpoint.
Updating
--------
Update a URL.
### Requirements

 Type | Description || Access Tokens | Any access token can be used to make this request. |
| Features | Not applicable. |
| Page Tasks | Not applicable. |
| Permissions | Not applicable. |
### Examples

To update information about a URL published in a Post or Comment, send a `POST` request to `https://graph.facebook.com` with the `id` parameter set to the URL, the `scrape` parameter set to `true`, any `fields` about the URL, and an access token requested from the User or Page who published the Post or Comment.

The follow example updates the URL, https://www.facebook.com/my-update, that was shared by the User represented by the User access token.

*Formatted for readability.*
```
curl -i -X POST \
 "https://graph.facebook.com/{latest-graph-api-version}/
    ?id=https://www.facebook.com/my-update
    &scrape=true
    &access_token={user-access-token}"
```
On success your app receives the following engagement counts for the URL that was shared:

```
{
  "success": true
}  
```
### Query String Parameters
Include the following query string parameters to augment the request.

 Parameter | Description || `access_token`
Required*string* | An access token. |
| `fields`
*string* | A comma-separated list of fields you want to request. |
| `id`
Required*string* | The url to be updated. The url must be encoded so that it does not interfere with the `scrape` parameter. |
| `scrape`
Required*boolean* | Value must be `true`. |
#### Example Request

```
POST /{version}/?id={url}&scrape=true
Host: graph.facebook.com
```
#### Example Response

```
{
  "success": true
}
```
Deleting
--------
You can't perform this operation on this endpoint.