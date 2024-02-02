Graph API Reference v18.0: Live Video













DocsToolsSupportLog InGraph API* Overview
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
	+ Ads Archive
	+ Album
	+ App Link Host
	+ Application
	+ Branded Content Search
	+ CPASAdvertiser Partnership Recommendation
	+ Canvas
	+ Canvas Button
	+ Canvas Carousel
	+ Canvas Footer
	+ Canvas Header
	+ Canvas Photo
	+ Canvas Product List
	+ Canvas Product Set
	+ Canvas Text
	+ Canvas Video
	+ Collaborative Ads Directory
	+ Comment
	+ Commerce Merchant Settings
	+ Conversation
	+ Debug Token
	+ Event
	+ Games IAPProduct
	+ Group
	+ Group Doc
	+ Group Message
	+ Image Copyright
	+ Instagram Oembed
	+ Link
	+ Live Video
		- Blocked Users
		- Comments
		- Crosspost Shared Pages
		- Crossposted Broadcasts
		- Errors
		- Input Streams
		- Polls
		- Reactions
	+ Live Video Input Stream
	+ Mailing Address
	+ Media Fingerprint
	+ Message
	+ Milestone
	+ Object Comments
	+ Object Likes
	+ Object Private Replies
	+ Object Reactions
	+ Object Sharedposts
	+ Oembed Page
	+ Oembed Post
	+ Oembed Video
	+ Offline Conversion Data Set Upload
	+ Page
	+ Page Call To Action
	+ Page Post
	+ Page Upcoming Change
	+ Page/insights
	+ Payment
	+ Photo
	+ Place
	+ Place Tag
	+ Place Topic
	+ Post
	+ Profile
	+ Request
	+ Test User
	+ Thread
	+ URL
	+ User
	+ Video
	+ Video Copyright
	+ Video List
	+ Video Poll
	+ Video Poll Option
	+ Whats App Business Account
	+ Whats App Message Template
On This PageLive VideoReadingNew Page ExperienceExampleParametersFieldsEdgesError CodesCreatingParametersReturn TypeError CodesUpdatingParametersReturn TypeError CodesDeletingLimitationsParametersReturn TypeError CodesGraph API Versionv18.0Live Video
==========

Represents a live video broadcast. Refer to the Live Video API documentation for additional usage information.


Reading
-------

Get fields and edges on a LiveVideo.


Starting September 14, 2021, the following fields will throw an error for version 12.0+ calls made by apps that lack the endpoint's required permissions. This change will apply to all versions on December 13, 2021.


* `copyright`
### New Page Experience

This endpoint is supported for New Page Experience.### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v18.0/{live-video-id} HTTP/1.1
Host: graph.facebook.com
```

```
/\* PHP SDK v5.0.0 \*/
/\* make the API call \*/
try {
 // Returns a `Facebook\FacebookResponse` object
 $response = $fb->get(
 '/{live-video-id}',
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
/\* handle the result \*/
```

```
/\* make the API call \*/
FB.api(
 "/{live-video-id}",
 function (response) {
 if (response && !response.error) {
 /\* handle the result \*/
 }
 }
);
```

```
/\* make the API call \*/
new GraphRequest(
 AccessToken.getCurrentAccessToken(),
 "/{live-video-id}",
 null,
 HttpMethod.GET,
 new GraphRequest.Callback() {
 public void onCompleted(GraphResponse response) {
 /\* handle the result \*/
 }
 }
).executeAsync();
```

```
/\* make the API call \*/
FBSDKGraphRequest \*request = [[FBSDKGraphRequest alloc]
 initWithGraphPath:@"/{live-video-id}"
 parameters:params
 HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection \*connection,
 id result,
 NSError \*error) {
 // Handle the result
}];
```
If you want to learn how to use the Graph API, read our Using Graph API guide.### Parameters



| Parameter | Description |
| --- | --- |
| `target_token`string | A target token recently returned by the speed test API
 |

### Fields



| Field | Description |
| --- | --- |
| `id`numeric string | The live video ID.
 |
| `ad_break_config`LiveVideoAdBreakConfig | The ad break configurations for clients implementing triggering an ad break ui. Contains ad break eligibility and constants to render the ui. In order to use this, the page hosting the broadcast needs to be whitelisted.
 |
| `ad_break_failure_reason`enum | Ad Break failure reason
 |
| `broadcast_start_time`datetime | The time the video was initially published
 |
| `copyright`VideoCopyright | The copyright information for the live video
 |
| `creation_time`datetime | The creation time of the live video
 |
| `dash_ingest_url`string | The dash ingest stream URL of the live video
 |
| `dash_preview_url`string | Preview URL for dash player
 |
| `description`string | The description of the live video
 |
| `embed_html`iframe\_with\_src | The embed html of the live video
Default |
| `from`User|Page | The originator of the live video
 |
| `ingest_streams`list<LiveVideoInputStream> | Individual ingest streams.
 |
| `is_manual_mode`bool | Whether schedule live is in manual mode, in which live video will start manually instead of on schedled time
 |
| `is_reference_only`bool | Whether the live video is exclusively used for copyright monitoring
 |
| `live_views`unsigned int32 | The instant viewer count of the live video now
 |
| `overlay_url`string | A URL used in conjunction with Facebook Live Producer to show overlays for this broadcast. In order to use this, the page hosting the broadcast needs to be whitelisted.
 |
| `permalink_url`uri | The permalink URL of this video on Facebook.
 |
| `planned_start_time`datetime | Planned start time for a live video
 |
| `recommended_encoder_settings`LiveVideoRecommendedEncoderSettings | Recommended encoder settings for this live video.
 |
| `seconds_left`int32 | Seconds left in the maximum possible duration for this live video
 |
| `secure_stream_url`string | The secure stream url of the live video. Check with your encoder whether this is supported before adapting
Default |
| `status`enum | The status of the LiveVideo.
A `LIVE_NOW` LiveVideo is one that will be published to the intended destination (Timeline, Group, Page, etc) upon receiving valid video data, or one that is already published and actively streaming.
An `UNPUBLISHED` LiveVideo is in preparation; it's not visible to other users, and it may be automatically deleted after several hours in this state.
A `SCHEDULED_UNPUBLISHED` LiveVideo is scheduled to go live at a future time.
A `SCHEDULED_LIVE` LiveVideo is one whose scheduled time has passed, yet the stream is not yet live. Either in the process of transitioning, or still waiting for a valid video stream.
(Consider using the `SCHEDULED` states to create a planned, future LiveVideo.)
Default |
| `stream_url`string | The stream url of the live video
Default |
| `targeting`LiveVideoTargeting | Targeting information for this live video
 |
| `title`string | The title of the live video
Default |
| `video`Video | The inside video of the live video
 |

### Edges



| Edge | Description |
| --- | --- |
| `blocked_users` | The users who are blocked from commenting on the live video
 |
| `comments` | Comments made on this
 |
| `crosspost_shared_pages` | Pages which are allowed to crosspost this live video. This field is only available on the original live video.
 |
| `crossposted_broadcasts` | Live videos which have been crossposted from this live video. This field is only available on the original live video.
 |
| `errors` | Errors that occurred during the live stream
 |
| `polls` | Polls configured for this broadcast
 |
| `reactions` | People who reacted on this
 |

### Error Codes



| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 190 | Invalid OAuth 2.0 Access Token |
| 200 | Permissions error |

Creating
--------

You can make a POST request to `live_videos` edge from the following paths: * `/{user_id}/live_videos`

When posting to this edge, a LiveVideo will be created.### Parameters



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

You can make a POST request to `live_videos` edge from the following paths: * `/{event_id}/live_videos`

When posting to this edge, a LiveVideo will be created.### Parameters



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
| 6000 | There was a problem uploading your video file. Please try again with another file. |

You can make a POST request to `live_videos` edge from the following paths: * `/{group_id}/live_videos`

When posting to this edge, a LiveVideo will be created.### Parameters



| Parameter | Description |
| --- | --- |
| `content_tags`list<numeric string> | Tags that describe the contents of the Live Video. Use search endpoint with `type=adinterest` to get possible IDs. For example: `/search?type=adinterest&q=couscous`
 |
| `description`UTF-8 string | The description of the Live Video
Supports Emoji |
| `enable_backup_ingest`boolean | Set this to true to enable a backup ingest url. stop\_on\_delete\_stream defaults to false when set
 |
| `encoding_settings`string | Identifier of the encoding settings group. Currently only used for live-360 broadcasts. The value should be the `identifier` key of the encoding settings preset. Encoding presets can be found by querying the `GET /broadcaster_encoding_settings` endpoint
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
| `is_spherical`boolean | Denotes if the broadcast is a 360 live broadcast
 |
| `original_fov`int64 | Original field of view of the camera
 |
| `privacy`Privacy Parameter | Privacy for this Live Video
 |
| `projection`enum {EQUIRECTANGULAR, CUBEMAP, HALF\_EQUIRECTANGULAR} | Flag that denotes expected projection for 360 live streams. The default value is EQUIRECTANGULAR
 |
| `published`boolean | Set this to false to preview the stream before going live. Deprecated. Set the status instead
 |
| `schedule_custom_profile_image`image | Custom image that will appear in the scheduled live story and lobby
 |
| `spatial_audio_format`enum {ambiX\_4} | Denotes the format of the spatial audio stream. When unspecified audio is presumed to be mono or stereo
 |
| `status`enum {UNPUBLISHED, LIVE\_NOW, SCHEDULED\_UNPUBLISHED, SCHEDULED\_LIVE, SCHEDULED\_CANCELED} | The status of the broadcast. A `LIVE_NOW` broadcast is currently live and visible to users. An `UNPUBLISHED` broadcast is in preparation; it's not visible to other users, and it may be automatically deleted after several hours in this state. (Consider using the `SCHEDULED` states to create a planned, future broadcast.)
 |
| `stereoscopic_mode`enum {MONO, LEFT\_RIGHT, TOP\_BOTTOM} | The stereoscopic mode for this video
 |
| `stop_on_delete_stream`boolean | Set this to true if stream should be stopped when deleteStream RTMP command received
 |
| `title`UTF-8 string | Title of the live video. Maximum 254 characters.
Supports Emoji |

### Return Type

This endpoint supports read-after-write and will read the node represented by `id` in the return type. Struct {`id`: numeric string, `stream_url`: string, `secure_stream_url`: string, `stream_secondary_urls`: List [string], `secure_stream_secondary_urls`: List [string], `dash_ingest_url`: string, `dash_ingest_secondary_urls`: List [string], `event_id`: numeric string, }### Error Codes



| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |
| 1005 | Fail to upload cover photo. |
| 1000 | Invalid time for an event. |

You can make a POST request to `live_videos` edge from the following paths: * `/{page_id}/live_videos`

When posting to this edge, a LiveVideo will be created.### Parameters



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
| `crossposting_actions`array<JSON object> | List of desired changes to crossposting for this broadcast. Each change must provide a `page_id` and `action`. Example:
[
 {page\_id: 1234, action: 'enable\_crossposting'},
 {page\_id: 4567, action: 'enable\_crossposting\_and\_create\_post'}
]
Available action types:
* `enable_crossposting`: Enables crossposting for this broadcast with the Page if it is not currently enabled. No change if crossposting is already enabled with the Page for this broadcast.
* `disable_crossposting`: Disables crossposting for this broadcast with the Page if it is currently enabled. No change if crossposting is not already enabled with the Page for this broadcast.
* `enable_crossposting_and_create_post`: Same as `enable_crossposting`, but will also create a post as the Page. The post will be created even if crossposting is already enabled for the Page. This option is subject to your live crossposting relationships and will fail for Pages without the required permission.


When used with a Live Online Event, this will apply to the event.
 |
| `page_id`page ID | page\_id
Required |
| `action`enum {ENABLE\_CROSSPOSTING, DISABLE\_CROSSPOSTING, ENABLE\_CROSSPOSTING\_AND\_CREATE\_POST} | action
Required |
| `custom_labels`list<string> | Labels used to describe the video. Unlike content tags, custom labels are not published and only appear in insights data.
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
| `game_show`JSON object | Configure this live stream to be a game show
 |
| `game_type`enum {KNOCKOUT} | game\_type
Required |
| `is_spherical`boolean | Flag that denotes the broadcast is a 360 live broadcast.
 |
| `original_fov`int64 | Original field of view of the camera
 |
| `privacy`Privacy Parameter | Privacy for this live video.
 |
| `product_items`list<numeric string> | Products which will be shown with live videos.
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
| `targeting`target | Object that limits the audience for this content. Anyone not in these demographics will not be able to view this content.
When used with a Live Online Event, this will apply to the event.
 |
| `geo_locations`Object |  |
| `countries`list<string> |  |
| `regions`list<Object> |  |
| `key`int64 |  |
| `cities`list<Object> |  |
| `key`int64 |  |
| `zips`list<Object> |  |
| `key`string |  |
| `locales`list<string> |  |
| `excluded_countries`list<string> |  |
| `excluded_regions`list<int64> |  |
| `excluded_cities`list<int64> |  |
| `excluded_zipcodes`list<string> |  |
| `timezones`list<int64> |  |
| `age_min`enum {13, 15, 18, 21, 25} |  |
| `title`UTF-8 string | The title of the live video. Maximum 254 characters.
Supports Emoji |

### Return Type

This endpoint supports read-after-write and will read the node represented by `id` in the return type. Struct {`id`: numeric string, `stream_url`: string, `secure_stream_url`: string, `stream_secondary_urls`: List [string], `secure_stream_secondary_urls`: List [string], `dash_ingest_url`: string, `dash_ingest_secondary_urls`: List [string], `event_id`: numeric string, }### Error Codes



| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 1005 | Fail to upload cover photo. |
| 1000 | Invalid time for an event. |
| 475 | You have been temporarily blocked from posting videos because you added videos containing content that may belong to someone else. |

Updating
--------

You can update a LiveVideo by making a POST request to `/{live_video_id}`.### Parameters



| Parameter | Description |
| --- | --- |
| `allow_bm_crossposting`boolean | If set to true, makes this live video available for crossposting by Pages in your Business Manager.
 |
| `content_tags`list<numeric string> | Tags that describe the contents of the video. Use search endpoint with `type=adinterest` to get possible IDs. For example, `/search?type=adinterest&q=couscous`.
 |
| `cross_share_to_group_ids`list<numeric string> | List of Groups by ID where the broadcast will be shared. The broadcast owner will require publishing permission to the groups in order to share.
 |
| `crossposting_actions`array<JSON object> | 
```
 List of desired changes to crossposting for this broadcast. Each change must provide a `page\_id` and `action`. Example:


 [
 {page\_id: 1234, action: 'enable\_crossposting'},
 {page\_id: 4567, action: 'enable\_crossposting\_and\_create\_post'}
 ]


 Available action types:


 - `enable\_crossposting`: Enables crossposting for this broadcast with the Page if it is not currently enabled. No change if crossposting is already enabled with the Page for this broadcast.
 - `disable\_crossposting`: Disables crossposting for this broadcast with the Page if it is currently enabled. No change if crossposting is not already enabled with the Page for this broadcast.
 - `enable\_crossposting\_and\_create\_post`: Same as `enable\_crossposting`, but will also create a post as the Page. The post will be created even if crossposting is already enabled for the Page. This option is subject to your [live crossposting relationships](https://www.facebook.com/help/publisher/1385580858214929) and will fail for Pages without the required permission.

 When used with a Live Online Event, this will apply to the event.
```

 |
| `page_id`page ID | page\_id
Required |
| `action`enum {ENABLE\_CROSSPOSTING, DISABLE\_CROSSPOSTING, ENABLE\_CROSSPOSTING\_AND\_CREATE\_POST} | action
Required |
| `custom_labels`list<string> | Labels used to describe the video. Unlike content tags, custom labels are not published and only appear in insights data.
 |
| `description`UTF-8 string | The description of live video
Supports Emoji |
| `direct_share_status`int64 | The status to allow sponsor directly boost the post.
 |
| `disturbing`boolean | If true, autoplay will be disabled and live video will have a graphic content warning overlay
 |
| `donate_button_charity_id`int64 | Specifies the ID of the charity for which a donate button will be added to the live video. If zero is passed, will remove the donate button on the video.
 |
| `embeddable`boolean | If true, live video will be embeddable
 |
| `end_live_video`boolean | If true, the live video will be ended. Only valid if the live video is still running
 |
| `event_params`Live Video Event Parameter | Parameters specific to Live Online Event broadcast. If `start_time` (unix timecode) is set, LOE's start time will be updated. Also, `cover` (url) uploads an image to use as the cover photo for the event.
Example:
{
 start\_time: 1641013200,
 cover: 'https://your.url/image.jpg',
}
 |
| `is_manual_mode`boolean | Flag to indicate that the scheduled broadcast is switched to manual mode
 |
| `live_comment_moderation_setting`list<enum {DEFAULT, FOLLOWER, SLOW, DISCUSSION, RESTRICTED, PROTECTED\_MODE, SUPPORTER, NO\_HYPERLINK, FOLLOWED, TAGGED}> | Set of comment moderation settings for the live video
 |
| `master_ingest_stream_id`numeric string | Ingest stream to set to master and route viewers to.
 |
| `persistent_stream_key_status`enum {ENABLE, DISABLE, REGENERATE} | Set the status of the persistent stream key for this live video
 |
| `place`place tag | Location associated with the video, if any.
 |
| `planned_start_time`datetime/timestamp | Planned start time for a scheduled live video
 |
| `privacy`Privacy Parameter | The privacy setting of live video
 |
| `published`boolean | Should the live video be published? Only valid if not yet published.

```
 Deprecated. Prefer setting the status instead.
```

 |
| `schedule_custom_profile_image`image | Custom image that will appear in the scheduled live story and lobby.
 |
| `schedule_feed_background_image`image | Custom background image that appears in the updated scheduled live story
 |
| `sponsor_id`numeric string or integer | Facebook Page id that is tagged as sponsor in the video post
 |
| `sponsor_relationship`int64 | Sponsor Relationship, such as Presented By or Paid PartnershipWith
 |
| `status`enum {UNPUBLISHED, LIVE\_NOW, SCHEDULED\_UNPUBLISHED, SCHEDULED\_LIVE, SCHEDULED\_CANCELED} | The status of the LiveVideo.
A `LIVE_NOW` LiveVideo is one that will be published to the intended destination (Timeline, Group, Page, etc) upon receiving valid video data, or one that is already published and actively streaming.
An `UNPUBLISHED` LiveVideo is in preparation; it's not visible to other users, and it may be automatically deleted after several hours in this state.
A `SCHEDULED_UNPUBLISHED` LiveVideo is scheduled to go live at a future time.
A `SCHEDULED_LIVE` LiveVideo is one whose scheduled time has passed, yet the stream is not yet live. Either in the process of transitioning, or still waiting for a valid video stream.
(Consider using the `SCHEDULED` states to create a planned, future LiveVideo.)
 |
| `tags`list<int> | Users tagged in the live video.
 |
| `targeting`target | Object that limits the audience for this content. Anyone not in these demographics will not be able to view this content.
When used with a Live Online Event, this will apply to the event.
 |
| `geo_locations`Object |  |
| `countries`list<string> |  |
| `regions`list<Object> |  |
| `key`int64 |  |
| `cities`list<Object> |  |
| `key`int64 |  |
| `zips`list<Object> |  |
| `key`string |  |
| `locales`list<string> |  |
| `excluded_countries`list<string> |  |
| `excluded_regions`list<int64> |  |
| `excluded_cities`list<int64> |  |
| `excluded_zipcodes`list<string> |  |
| `timezones`list<int64> |  |
| `age_min`enum {13, 15, 18, 21, 25} |  |
| `title`UTF-8 string | The title of the live video.
Supports Emoji |

### Return Type

This endpoint supports read-after-write and will read the node represented by `id` in the return type. Struct {`id`: numeric string, `persistent_stream_url`: string, `backup_persistent_stream_url`: string, }### Error Codes



| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |
| 1005 | Fail to upload cover photo. |

Deleting
--------

You can delete a LiveVideo by making a DELETE request to `/{live_video_id}`.### Limitations


You cannot delete a LiveVideo on a User or Group.


### Parameters

This endpoint doesn't have any parameters.### Return Type

 Struct {`success`: bool, }### Error Codes



| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

On This PageLive VideoReadingNew Page ExperienceExampleParametersFieldsEdgesError CodesCreatingParametersReturn TypeError CodesUpdatingParametersReturn TypeError CodesDeletingLimitationsParametersReturn TypeError CodesFollow Us* 
#### Products

* Artificial Intelligence
* AR/VR
* Business Tools
* Gaming
* Open Source
* Publishing
* Social Integrations
* Social Presence
#### Programs

* ThreatExchange
#### Support

* Developer Support
* Bugs
* Platform Status
* Report a Platform Data Incident
* Facebook for Developers Community Group
* Sitemap
#### News

* Blog
* Success Stories
* Videos
* Meta for Developers Page
#### Terms and Policies

* Platform Initiatives Hub
* Platform Terms
* Developer Policies
* European Commission Commitments
Follow Us* 
 © 2024 Meta * About
* Create Ad
* Careers
* Privacy Policy
* Cookies
* Terms
English (US)Bahasa IndonesiaDeutschEspañolEspañol (España)Français (France)ItalianoPortuguês (Brasil)Tiếng ViệtРусскийالعربيةภาษาไทย한국어中文(香港)中文(台灣)中文(简体)日本語English (US)





































Allow the use of cookies from Facebook on this browser?We use cookies and similar technologies to help:Provide and improve content on Meta ProductsProvide a safer experience by using information we receive from cookies on and off FacebookProvide and improve Meta Products for people who have an accountFor advertising and measurement services off of Meta Products, analytics, and to provide certain features and improve our services for you, we use tools from other companies on Facebook. These companies also use cookies.You can allow the use of all cookies, just essential cookies or you can choose more options below. You can learn more about cookies and how we use them, and review or change your choice at any time in our Cookie Policy.Essential cookiesThese cookies are required to use Meta Products. They’re necessary for these sites to work as intended.Optional cookies

Cookies from other companiesWe use tools from other companies for advertising and measurement services off of Meta Products, analytics, and to provide certain features and improve our services for you. These companies also use cookies.More informationIf you allow these cookies:

* We’ll be able to better personalize ads for you off of Meta Products, and measure their performance
* Features on our products will not be affected
* Other companies will receive information about you by using cookies

If you don’t allow these cookies:

* We won’t use cookies from other companies to help personalize ads for you off of Meta Products, or to measure their performance
* Some features on our products may not work

Other ways you can control your information

Manage your ad experience in Accounts CenterIf you have a Facebook account, you can manage how different data is used to personalize ads with these tools.

Ad settings

To show you better ads, we use data that advertisers and other partners provide us about your activity off Meta Company Products, including websites and apps. You can control whether we use this data to show you ads in your ad settings.

The Meta Audience Network is a way for advertisers to show you ads in apps and websites off the Meta Company Products. One of the ways Audience Network shows relevant ads is by using your ad preferences to determine which ads you may be interested in seeing. You can control this in your ad settings.

Ad preferences

In Ad preferences, you can choose whether we show you ads and make choices about the information used to show you ads.

Off-Facebook activity

You can review your off-Facebook activity, which is a summary of activity that businesses and organizations share with us about your interactions with them, such as visiting their apps or websites. They use our Business Tools, such as Facebook Login or Meta Pixel, to share this information with us. This helps us do things such as give you a more personalized experience on Meta Products. Learn more about off-Facebook activity, how we use it, and how you can manage it.

More information about online advertisingYou can opt out of seeing online interest-based ads from Meta and other participating companies through the Digital Advertising Alliance in the US, the Digital Advertising Alliance of Canada in Canada or the European Interactive Digital Advertising Alliance in Europe, or through your mobile device settings, if you are using Android, iOS 13 or an earlier version of iOS. Please note that ad blockers and tools that restrict our cookie use may interfere with these controls.

The advertising companies we work with generally use cookies and similar technologies as part of their services. To learn more about how advertisers generally use cookies and the choices they offer, you can review the following resources:

* Digital Advertising Alliance
* Digital Advertising Alliance of Canada
* European Interactive Digital Advertising Alliance
Controlling cookies with browser settingsYour browser or device may offer settings that allow you to choose whether browser cookies are set and to delete them. These controls vary by browser, and manufacturers may change both the settings they make available and how they work at any time. As of 5 October 2020, you may find additional information about the controls offered by popular browsers at the links below. Certain parts of Meta Products may not work properly if you have disabled browser cookies. Please be aware that these controls are distinct from the controls that Facebook offers.

* Google Chrome
* Internet Explorer
* Firefox
* Safari
* Safari Mobile
* Opera
Only allow essential cookiesAllow essential and optional cookies