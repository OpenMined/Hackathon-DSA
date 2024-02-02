Graph API Reference: User Videos - Documentation - Meta for Developers

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
Graph API Versionv19.0User Videos
===========
Reading
-------
GET GraphUserVideosEdge

### Example
HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v19.0/{user-id}/videos HTTP/1.1
Host: graph.facebook.com
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{user-id}/videos',
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
    "/{user-id}/videos",
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
    "/{user-id}/videos",
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
                               initWithGraphPath:@"/{user-id}/videos"
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
| `type`enum {TAGGED, UPLOADED} | Default value: `"TAGGED"`Allows you to query which type of videos to return
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
A list of Video nodes.#### `paging`
For more details about pagination, see the Graph API guide.### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 190 | Invalid OAuth 2.0 Access Token |
Creating
--------
You can make a POST request to `videos` edge from the following paths: * `/{user_id}/videos`
When posting to this edge, a Video will be created.### Parameters

| Parameter | Description |
| --- | --- |
| `audio_story_wave_animation_handle`string | Everstore handle of wave animation used to burn audio story video
 |
| `content_category`enum {BEAUTY\_FASHION, BUSINESS, CARS\_TRUCKS, COMEDY, CUTE\_ANIMALS, ENTERTAINMENT, FAMILY, FOOD\_HEALTH, HOME, LIFESTYLE, MUSIC, NEWS, POLITICS, SCIENCE, SPORTS, TECHNOLOGY, VIDEO\_GAMING, OTHER} | Content category of this video.
 |
| `description`UTF-8 string | 
```
                                                              The text describing a post that may be shown in a story about it.
                                                              It may include rich text information, such as entities and emojis.
```
Supports Emoji |
| `direct_share_status`int64 | The status to allow sponsor directly boost the post.
 |
| `embeddable`boolean | Whether the video is embeddable.
 |
| `end_offset`int64 | end\_offset
 |
| `file_size`int64 | The size of the entire video file in bytes.
 |
| `file_url`string | Accessible URL of a video file. Cannot be used with `upload_phase`.
 |
| `fisheye_video_cropped`boolean | Whether the single fisheye video is cropped or not
 |
| `fov`int64 | 360 video only: Vertical field of view
 |
| `front_z_rotation`float | The front z rotation in degrees on the single fisheye video
 |
| `guide`list<list<int64>> | 360 video only: Guide keyframes data. An array of keyframes, each of which is an array of 3 or 4 elements in the following order: [video timestamp (seconds), pitch (degrees, -90 ~ 90), yaw (degrees, -180 ~ 180), field of view (degrees, 40 ~ 90, optional)], ordered by video timestamp in strictly ascending order.
 |
| `guide_enabled`boolean | 360 video only: Whether Guide is active.
 |
| `initial_heading`int64 | 360 video only: Horizontal camera perspective to display when the video begins.
 |
| `initial_pitch`int64 | 360 video only: Vertical camera perspective to display when the video begins.
 |
| `is_voice_clip`boolean | is\_voice\_clip, used to indicate that if a video is used as audio record
 |
| `no_story`boolean | Default value: `false`If set to `true`, this will suppress feed and timeline story.
 |
| `original_fov`int64 | Original field of view of the source camera
 |
| `original_projection_type`enum {equirectangular, cubemap, half\_equirectangular} | 360 video only: The original projection type of the 360 video being uploaded.
 |
| `posting_to_redspace`enum {enabled, disabled} | Whether the post should appear in RedSpace.
 |
| `privacy`Privacy Parameter | Determines the privacy settings of the video. If not supplied, this defaults to the privacy level granted to the app in the Login Dialog. This field cannot be used to set a more open privacy setting than the one granted.
 |
| `prompt_id`string | The prompt id in prompts or purple rain that generated this post
 |
| `prompt_tracking_string`string | The prompt tracking string associated with this video post
 |
| `react_mode_metadata`JSON-encoded string | This metadata is required for clip reacts feature
 |
| `referenced_sticker_id`numeric string or integer | Sticker id of the sticker in the post
 |
| `replace_video_id`numeric string or integer | The video id your uploaded video about to replace
 |
| `slideshow_spec`JSON object | Specification of a list of images that are used to generate video.
 |
| `images_urls`list<URL> | A 3-7 element array of the URLs of the images. Required.
Required |
| `duration_ms`integer | The duration in milliseconds of each image. Default value is 1000.
 |
| `transition_ms`integer | The duration in milliseconds of the crossfade transition between images.
 Default value is 1000.
 |
| `reordering_opt_in`boolean | Default value: `false` |
| `music_variations_opt_in`boolean | Default value: `false` |
| `source`string | The video, encoded as form data. This field is required.
 |
| `spherical`boolean | Default value: `false`Set if the video was recorded in 360 format.
 |
| `sponsor_id`numeric string or integer | Facebook Page id that is tagged as sponsor in the video post
 |
| `start_offset`int64 | Start byte position of the file chunk.
 |
| `swap_mode`enum {replace} | Type of replacing video request
 |
| `title`UTF-8 string | The title of the video
Supports Emoji |
| `transcode_setting_properties`string | Properties used in computing transcode settings for the video
 |
| `unpublished_content_type`enum {SCHEDULED, SCHEDULED\_RECURRING, DRAFT, ADS\_POST, INLINE\_CREATED, PUBLISHED, REVIEWABLE\_BRANDED\_CONTENT} | Type of unpublished content, such as scheduled, draft or ads\_post.
 |
| `upload_phase`enum {start, transfer, finish, cancel} | Type of chunked upload request.
 |
| `upload_session_id`numeric string or integer | ID of the chunked upload session.
 |
| `video_file_chunk`string | The video file chunk, encoded as form data. This field is required during `transfer` upload phase.
 |
| `video_id_original`string | video\_id\_original
 |
### Return Type
 Struct {`id`: numeric string, `upload_session_id`: numeric string, `video_id`: numeric string, `start_offset`: numeric string, `end_offset`: numeric string, `success`: bool, `skip_upload`: bool, `upload_domain`: string, `region_hint`: string, `xpv_asset_id`: numeric string, `is_xpv_single_prod`: bool, `transcode_bit_rate_bps`: numeric string, `transcode_dimension`: numeric string, `should_expand_to_transcode_dimension`: bool, `action_id`: string, `gop_size_seconds`: numeric string, `target_video_codec`: string, `target_hdr`: string, `maximum_frame_rate`: numeric string, }### Error Codes

| Error | Description |
| --- | --- |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 200 | Permissions error |
| 100 | Invalid parameter |
| 6000 | There was a problem uploading your video file. Please try again with another file. |
| 6001 | There was a problem uploading your video. Please try again. |
| 459 | The session is invalid because the user has been checkpointed |
| 190 | Invalid OAuth 2.0 Access Token |
| 194 | Missing at least one required parameter |
| 210 | User not visible |
Updating
--------
You can't perform this operation on this endpoint.Deleting
--------
You can't perform this operation on this endpoint.