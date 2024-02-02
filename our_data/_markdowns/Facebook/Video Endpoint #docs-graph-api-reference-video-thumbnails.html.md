Graph API, Video Thumbnails - Documentation - Meta for Developers

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
Graph API Versionv19.0Video Thumbnails
================

 Represents a collection of
 VideoThumbnails
 on a 
 Video
Reading
-------
Get a list of VideoThumbnails on a Video.

### Requirements

 Type | Requirement || Access Tokens | App or Page |
| Permissions | `pages_read_engagement`, `pages_show_list` |
### Examples

```
curl -X GET "https://graph.facebook.com/***`v19.0`***/***video-id***/thumbnails?access_token=***page\_access\_token***"
```
On success your app receives a list of VideoThumbnail objects for the video.

```
{
"id": "***video-id-1***",
"height": ***1280***,
"scale": 1,
"uri": "***url-for-video-1***",
"width": ***720***,
"is_preferred": ***false***
},
{
"id": "***video-id-2***",
"height": ***1280***,
"scale": 1,
"uri": "***url-for-video-2***",
"width": ***720***,
"is_preferred": ***false***
},
...
```
### Parameters
This endpoint doesn't have any parameters.### Fields
Reading from this edge will return a JSON formatted result:

```
{
 "`data`": [],
 "`paging`": {}
}

```
#### `data`
A list of VideoThumbnail nodes.#### `paging`
For more details about pagination, see the Graph API guide.### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 190 | Invalid OAuth 2.0 Access Token |
Creating
--------
You can make a POST request to `thumbnails` edge from the following paths: * `/{video_id}/thumbnails`
When posting to this edge, a VideoThumbnail will be created.### Limitations

* Maximum thumbnail file size 10MB.
* Thumbnails can only be created on Videos that have been associated with a Page.
* We recommend that you use thumbnails with the same aspect ratio as the video.

### Requirements

 Type | Requirement || Access Tokens | App or Page |
| Permissions | `pages_read_user_content`, `pages_manage_engagement`, `pages_show_list` |
### Examples

```
curl -X POST "https://graph.facebook.com/***`v19.0`***/***video-id***/thumbnails
   ?access_token=***page\_access\_token***
   &is_preferred=***true***
   &source=@***ThumbnailSample1.jpg***"
```
On success your app receives a list of VideoThumbnail objects for the video.

```
{
  "success": ***true***
}
```
### Parameters

| Parameter | Description |
| --- | --- |
| `is_preferred`boolean | Default value: `false`Set to `true` if this thumbnail is the preferred thumbnail to be shown for this video
 |
| `source`image | The source for the thumbnail, an image file
Required |
### Return Type
This endpoint supports read-after-write and will read the node to which you POSTed. Struct {`success`: bool, }### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
Updating
--------
You can't perform this operation on this endpoint.Deleting
--------
You can't perform this operation on this endpoint.