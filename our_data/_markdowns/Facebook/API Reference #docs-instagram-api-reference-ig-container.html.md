IG Container - Instagram Platform - Documentation - Meta for Developers

Instagram Platform* Instagram Graph API
* Instagram Basic Display API
* Sharing to Feed
* Sharing to Stories
* oEmbed
* Embed Button
* Business Login for Instagram
IG Container
============

Represents a media container for publishing an Instagram post. Refer to the Content Publishing guide for complete publishing steps.

Creating
--------

This operation is not supported.

Reading
-------

**`GET /{instagram-container-id}`**

Get fields and edges on an IG Container.

### Requirements

 Type | Description || Access Tokens | User |
| Permissions | `instagram_basic`
`instagram_content_publish`
`pages_read_engagement`
If the app user was granted a role on the Page via the Business Manager, one of the following permissions is also required:
`ads_management`
`business_management` |
### Request Syntax

```
GET https://graph.facebook.com/{instagram-container-id}
  ?fields={fields}
  &access_token={access-token}
```
### Query String Parameters

 Parameter | Value || `access_token`
**Required**
*String* | The app user's User access token. |
| `fields`
*Comma-separated list* | A comma-separated list of fields and edges you want returned. If omitted, default fields will be returned. |
### Fields

 Field Name | Description || `copyright_check_status` | Used to determine if an uploaded video is violating copyright. Key-values pairs return include:* `matches_found` set to one of the following:
	+ `true` – the video is violating copyright
	+ `false` – the video is not violating copyright
* `status` set to one of the following:
	+ `completed` – the detection process has finished
	+ `error` – an error occurred during the detection process
	+ `in_progress` – the detection process is ongoing
	+ `not_started` – the detection process has not started
 |
| `id` | Instagram Container ID, represented in code examples as `{instagram-container-id}` |
| `status` | Publishing status. If `status_code` is `ERROR`, this value will be an error subcode. |
| `status_code` | The container's publishing status. Possible values:
* `EXPIRED` — The container was not published within 24 hours and has expired.
* `ERROR` — The container failed to complete the publishing process.
* `FINISHED` — The container and its media object are ready to be published.
* `IN_PROGRESS` — The container is still in the publishing process.
* `PUBLISHED` — The container's media object has been published.
 |
### Edges

There are no edges on this node.

### Response

A JSON-formatted object containing default and requested fields.

```
{
  "{field}":"{value}",
  ...
}
```
### Sample Request

```
curl -X GET \
  'https://graph.facebook.com/17889615691921648?fields=status_code&access_token=IGQVJ...'
```
### Sample Response

```
{
  "status_code": "FINISHED",
  "id": "17889615691921648"
}
```
Updating
--------

This operation is not supported.

Deleting
--------

This operation is not supported.