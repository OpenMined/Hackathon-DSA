Graph API Reference v19.0: User Live Videos - Documentation - Meta for Developers

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
Graph API Versionv19.0User Live Videos
================
Represents a collection of LiveVideos on a User.

Reading
-------
Get a collection of LiveVideos on a User.

### New Page Experience
This endpoint is supported for New Page Experience.### Example
HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v19.0/{user-id}/live_videos HTTP/1.1
Host: graph.facebook.com
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{user-id}/live_videos',
    '{access-token}'
  );
} catch(Facebook\Exceptions\FacebookResponseException $e) {
  echo 'Graph returned an error: ' . $e->getMessage();
  exit;
} catch(Facebook\Exceptions\FacebookSDKException $e) {
  echo 'Facebook SDK returned an error: ' . $e->getMessage();
  exit;
}
$graphNode = $response->getGraphNode();
/* handle the result */
```
```
/* make the API call */
FB.api(
    "/{user-id}/live_videos",
    function (response) {
      if (response && !response.error) {
        /* handle the result */
      }
    }
);
```
```
/* make the API call */
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "/{user-id}/live_videos",
    null,
    HttpMethod.GET,
    new GraphRequest.Callback() {
        public void onCompleted(GraphResponse response) {
            /* handle the result */
        }
    }
).executeAsync();
```
```
/* make the API call */
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                               initWithGraphPath:@"/{user-id}/live_videos"
                                      parameters:params
                                      HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
If you want to learn how to use the Graph API, read our Using Graph API guide.### Parameters

| Parameter | Description |
| --- | --- |
| `broadcast_status`list<enum {UNPUBLISHED, LIVE, LIVE\_STOPPED, PROCESSING, VOD, SCHEDULED\_UNPUBLISHED, SCHEDULED\_LIVE, SCHEDULED\_EXPIRED, SCHEDULED\_CANCELED}> | Allows you to specify what kind of live videos return. No value returns all status types
 |
| `source`enum{target, owner} | Default value: `target`Specifies what the source of the videos should be. 'target' gets videos broadcasted onto the user's timeline, 'owner' gets videos made by the user
 |
### Fields
Reading from this edge will return a JSON formatted result:

```
{
 "`data`": [],
 "`paging`": {}
}

```
#### `data`
A list of LiveVideo nodes.#### `paging`
For more details about pagination, see the Graph API guide.### Error Codes

| Error | Description |
| --- | --- |
| 190 | Invalid OAuth 2.0 Access Token |
| 100 | Invalid parameter |
| 200 | Permissions error |
Creating
--------
You can make a POST request to `live_videos` edge from the following paths: * `/{user_id}/live_videos`
When posting to this edge, a LiveVideo will be created.Scheduling is deprecated. Calls to the `POST /ID/live-video` endpoint with the `planned_start_time` parameter will return an error. To schedule a live video, use the `event_params` parameter.

### Parameters

| Parameter | Description |
| --- | --- |
| `content_tags`list<numeric string> | Tags that describe the contents of the video. Use search endpoint with `type=adinterest` to get possible IDs.
```
                    Example:
                    ~~~~
                    /search?type=adinterest&q=couscous
                    ~~~~
```
 |
| `description`UTF-8 string | The description of the live video.
Supports Emoji |
| `donate_button_charity_id`numeric string or integer | Specifies the ID of the charity for which a donate button will be added to the live video.
 |
| `enable_backup_ingest`boolean | Set this to true to enable a backup ingest url. stop\_on\_delete\_stream defaults to false when set
 |
| `encoding_settings`string | Identifier of the encoding settings group the broadcaster is using for this stream. This parameter is currently only in use for live-360 broadcasts. The value to be passed to this parameter is the value of the `identifier` key of the encoding settings preset. Encoding presets can be found by querying the `/broadcaster_encoding_settings` Graph API endpoint (`GET` query).
 |
| `event_params`Live Video Event Parameter | Parameters specific to Live Online Event broadcast. If `start_time` (unix timecode) is set, LOE's start time will be updated. Also, `cover` (url) uploads an image to use as the cover photo for the event.
Example:
{
 start\_time: 1641013200,
 cover: 'https://your.url/image.jpg',
}
 |
| `fisheye_video_cropped`boolean | Whether the single fisheye video is cropped or not
 |
| `front_z_rotation`float | The front z rotation in degrees on the single fisheye video
 |
| `is_spherical`boolean | Flag that denotes the broadcast is a 360 live broadcast.
 |
| `original_fov`int64 | Original field of view of the camera
 |
| `privacy`Privacy Parameter | Privacy for this live video.
 |
| `projection`enum {EQUIRECTANGULAR, CUBEMAP, HALF\_EQUIRECTANGULAR} | Flag that denotes expected projection for 360 live streams. The default value is EQUIRECTANGULAR.
 |
| `published`boolean | Set this to false to preview the stream before going live.
```
                    Deprecated. Prefer setting the status instead.
```
 |
| `schedule_custom_profile_image`image | Custom image that will appear in the scheduled live story and lobby.
 |
| `spatial_audio_format`enum {ambiX\_4} | Denotes the format of the spatial audio stream. When unspecified audio is presumed to be mono or stereo.
 |
| `status`enum {UNPUBLISHED, LIVE\_NOW, SCHEDULED\_UNPUBLISHED, SCHEDULED\_LIVE, SCHEDULED\_CANCELED} | The status of the broadcast. A `LIVE_NOW` broadcast is currently live and visible to users. An `UNPUBLISHED` broadcast is in preparation; it's not visible to other users, and it may be automatically deleted after several hours in this state. (Consider using the `SCHEDULED` states to create a planned, future broadcast.)
 |
| `stereoscopic_mode`enum {MONO, LEFT\_RIGHT, TOP\_BOTTOM} | Set this parameter to the stereoscopic mode for this video.
 |
| `stop_on_delete_stream`boolean | Set this to true if stream should be stopped when
 deleteStream RTMP command received.
 |
| `title`UTF-8 string | The title of the live video. Maximum 254 characters.
Supports Emoji |
### Return Type
This endpoint supports read-after-write and will read the node represented by `id` in the return type. Struct {`id`: numeric string, `stream_url`: string, `secure_stream_url`: string, `stream_secondary_urls`: List [string], `secure_stream_secondary_urls`: List [string], `dash_ingest_url`: string, `dash_ingest_secondary_urls`: List [string], `event_id`: numeric string, }### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |
| 1005 | Fail to upload cover photo. |
| 1000 | Invalid time for an event. |
Updating
--------
You can't perform this operation on this endpoint.Deleting
--------
You can't perform this operation on this endpoint.