Live Video
==========

[](#)

Represents a live video broadcast. Refer to the [Live Video API](https://developers.facebook.com/docs/live-video-api) documentation for additional usage information.

[](#)

Reading
-------

Get fields and edges on a LiveVideo.

Starting September 14, 2021, the following fields will throw an error for version 12.0+ calls made by apps that lack the endpoint's required permissions. This change will apply to all versions on December 13, 2021.

* `copyright`
    

### New Page Experience

This endpoint is supported for [New Page Experience](https://developers.facebook.com/docs/pages/new-pages-experience/).

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Blive-video-id%7D&version=v18.0)

    GET /v18.0/{live-video-id} HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
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
    /* handle the result */

    /* make the API call */
    FB.api(
        "/{live-video-id}",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{live-video-id}",
        null,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{live-video-id}"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

| Parameter | Description |
| --- | --- |
| `target_token`<br><br>string | A target token recently returned by the speed test API |

### Fields

| Field | Description |
| --- | --- |
| `id`<br><br>numeric string | The live video ID. |
| `ad_break_config`<br><br>LiveVideoAdBreakConfig | The ad break configurations for clients implementing triggering an ad break ui. Contains ad break eligibility and constants to render the ui. In order to use this, the page hosting the broadcast needs to be whitelisted. |
| `ad_break_failure_reason`<br><br>enum | Ad Break failure reason |
| `broadcast_start_time`<br><br>datetime | The time the video was initially published |
| `copyright`<br><br>[VideoCopyright](https://developers.facebook.com/docs/graph-api/reference/video-copyright/) | The copyright information for the live video |
| `creation_time`<br><br>datetime | The creation time of the live video |
| `dash_ingest_url`<br><br>string | The dash ingest stream URL of the live video |
| `dash_preview_url`<br><br>string | Preview URL for dash player |
| `description`<br><br>string | The description of the live video |
| `embed_html`<br><br>iframe\_with\_src | The embed html of the live video<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `from`<br><br>User\|Page | The originator of the live video |
| `ingest_streams`<br><br>[list<LiveVideoInputStream>](https://developers.facebook.com/docs/graph-api/reference/live-video-input-stream/) | Individual ingest streams. |
| `is_manual_mode`<br><br>bool | Whether schedule live is in manual mode, in which live video will start manually instead of on schedled time |
| `is_reference_only`<br><br>bool | Whether the live video is exclusively used for copyright monitoring |
| `live_views`<br><br>unsigned int32 | The instant viewer count of the live video now |
| `overlay_url`<br><br>string | A URL used in conjunction with Facebook Live Producer to show overlays for this broadcast. In order to use this, the page hosting the broadcast needs to be whitelisted. |
| `permalink_url`<br><br>uri | The permalink URL of this video on Facebook. |
| `planned_start_time`<br><br>datetime | Planned start time for a live video |
| `recommended_encoder_settings`<br><br>LiveVideoRecommendedEncoderSettings | Recommended encoder settings for this live video. |
| `seconds_left`<br><br>int32 | Seconds left in the maximum possible duration for this live video |
| `secure_stream_url`<br><br>string | The secure stream url of the live video. Check with your encoder whether this is supported before adapting<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `status`<br><br>enum | The status of the LiveVideo.<br><br>A `LIVE_NOW` LiveVideo is one that will be published to the intended destination (Timeline, Group, Page, etc) upon receiving valid video data, or one that is already published and actively streaming.<br><br>An `UNPUBLISHED` LiveVideo is in preparation; it's not visible to other users, and it may be automatically deleted after several hours in this state.<br><br>A `SCHEDULED_UNPUBLISHED` LiveVideo is scheduled to go live at a future time.<br><br>A `SCHEDULED_LIVE` LiveVideo is one whose scheduled time has passed, yet the stream is not yet live. Either in the process of transitioning, or still waiting for a valid video stream.<br><br>(Consider using the `SCHEDULED` states to create a planned, future LiveVideo.)<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `stream_url`<br><br>string | The stream url of the live video<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `targeting`<br><br>LiveVideoTargeting | Targeting information for this live video |
| `title`<br><br>string | The title of the live video<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `video`<br><br>[Video](https://developers.facebook.com/docs/graph-api/reference/video/) | The inside video of the live video |

### Edges

| Edge | Description |
| --- | --- |
| [`blocked_users`](https://developers.facebook.com/docs/graph-api/reference/live-video/blocked_users/) | The users who are blocked from commenting on the live video |
| [`comments`](https://developers.facebook.com/docs/graph-api/reference/live-video/comments/) | Comments made on this |
| [`crosspost_shared_pages`](https://developers.facebook.com/docs/graph-api/reference/live-video/crosspost_shared_pages/) | Pages which are allowed to crosspost this live video. This field is only available on the original live video. |
| [`crossposted_broadcasts`](https://developers.facebook.com/docs/graph-api/reference/live-video/crossposted_broadcasts/) | Live videos which have been crossposted from this live video. This field is only available on the original live video. |
| [`errors`](https://developers.facebook.com/docs/graph-api/reference/live-video/errors/) | Errors that occurred during the live stream |
| [`polls`](https://developers.facebook.com/docs/graph-api/reference/live-video/polls/) | Polls configured for this broadcast |
| [`reactions`](https://developers.facebook.com/docs/graph-api/reference/live-video/reactions/)[](#) | People who reacted on this |

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 190 | Invalid OAuth 2.0 Access Token |
| 200 | Permissions error |

[](#)

Creating
--------

You can make a POST request to `live_videos` edge from the following paths:

* [`/{user_id}/live_videos`](https://developers.facebook.com/docs/graph-api/reference/user/live_videos/)

When posting to this edge, a [LiveVideo](https://developers.facebook.com/docs/graph-api/reference/live-video/) will be created.

### Parameters

| Parameter | Description |
| --- | --- |
| `content_tags`<br><br>list<numeric string> | Tags that describe the contents of the video. Use search endpoint with `type=adinterest` to get possible IDs.<br><br>                        Example:<br>                        ~~~~<br>                        /search?type=adinterest&q=couscous<br>                        ~~~~ |
| `description`<br><br>UTF-8 string | The description of the live video.<br><br>Supports Emoji |
| `donate_button_charity_id`<br><br>numeric string or integer | Specifies the ID of the charity for which a donate button will be added to the live video. |
| `enable_backup_ingest`<br><br>boolean | Set this to true to enable a backup ingest url. stop\_on\_delete\_stream defaults to false when set |
| `encoding_settings`<br><br>string | Identifier of the encoding settings group the broadcaster is using for this stream. This parameter is currently only in use for live-360 broadcasts. The value to be passed to this parameter is the value of the `identifier` key of the encoding settings preset. Encoding presets can be found by querying the `/broadcaster_encoding_settings` Graph API endpoint (`GET` query). |
| `event_params`<br><br>Live Video Event Parameter | Parameters specific to Live Online Event broadcast. If `start_time` (unix timecode) is set, LOE's start time will be updated. Also, `cover` (url) uploads an image to use as the cover photo for the event.<br><br>Example: { start\_time: 1641013200, cover: 'https://your.url/image.jpg', } |
| `fisheye_video_cropped`<br><br>boolean | Whether the single fisheye video is cropped or not |
| `front_z_rotation`<br><br>float | The front z rotation in degrees on the single fisheye video |
| `is_spherical`<br><br>boolean | Flag that denotes the broadcast is a 360 live broadcast. |
| `original_fov`<br><br>int64 | Original field of view of the camera |
| `privacy`<br><br>Privacy Parameter | Privacy for this live video. |
| `projection`<br><br>enum {EQUIRECTANGULAR, CUBEMAP, HALF\_EQUIRECTANGULAR} | Flag that denotes expected projection for 360 live streams. The default value is EQUIRECTANGULAR. |
| `published`<br><br>boolean | Set this to false to preview the stream before going live.<br><br>                        Deprecated. Prefer setting the status instead. |
| `schedule_custom_profile_image`<br><br>image | Custom image that will appear in the scheduled live story and lobby. |
| `spatial_audio_format`<br><br>enum {ambiX\_4} | Denotes the format of the spatial audio stream. When unspecified audio is presumed to be mono or stereo. |
| `status`<br><br>enum {UNPUBLISHED, LIVE\_NOW, SCHEDULED\_UNPUBLISHED, SCHEDULED\_LIVE, SCHEDULED\_CANCELED} | The status of the broadcast. A `LIVE_NOW` broadcast is currently live and visible to users. An `UNPUBLISHED` broadcast is in preparation; it's not visible to other users, and it may be automatically deleted after several hours in this state. (Consider using the `SCHEDULED` states to create a planned, future broadcast.) |
| `stereoscopic_mode`<br><br>enum {MONO, LEFT\_RIGHT, TOP\_BOTTOM} | Set this parameter to the stereoscopic mode for this video. |
| `stop_on_delete_stream`<br><br>boolean | Set this to true if stream should be stopped when deleteStream RTMP command received. |
| `title`<br><br>UTF-8 string | The title of the live video. Maximum 254 characters.<br><br>Supports Emoji |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node represented by `id` in the return type.

Struct {

`id`: numeric string,

`stream_url`: string,

`secure_stream_url`: string,

`stream_secondary_urls`: List \[

string

\],

`secure_stream_secondary_urls`: List \[

string

\],

`dash_ingest_url`: string,

`dash_ingest_secondary_urls`: List \[

string

\],

`event_id`: numeric string,

}

### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |
| 1005 | Fail to upload cover photo. |
| 1000 | Invalid time for an event. |

You can make a POST request to `live_videos` edge from the following paths:

* [`/{event_id}/live_videos`](https://developers.facebook.com/docs/graph-api/reference/event/live_videos/)

When posting to this edge, a [LiveVideo](https://developers.facebook.com/docs/graph-api/reference/live-video/) will be created.

### Parameters

| Parameter | Description |
| --- | --- |
| `content_tags`<br><br>list<numeric string> | Tags that describe the contents of the video. Use search endpoint with `type=adinterest` to get possible IDs.<br><br>                                    Example:<br>                                    ~~~~<br>                                    /search?type=adinterest&q=couscous<br>                                    ~~~~ |
| `description`<br><br>UTF-8 string | The description of the live video.<br><br>Supports Emoji |
| `enable_backup_ingest`<br><br>boolean | Set this to true to enable a backup ingest url. stop\_on\_delete\_stream defaults to false when set |
| `encoding_settings`<br><br>string | Identifier of the encoding settings group the broadcaster is using for this stream. This parameter is currently only in use for live-360 broadcasts. The value to be passed to this parameter is the value of the `identifier` key of the encoding settings preset. Encoding presets can be found by querying the `/broadcaster_encoding_settings` Graph API endpoint (`GET` query). |
| `event_params`<br><br>Live Video Event Parameter | Parameters specific to Live Online Event broadcast. If `start_time` (unix timecode) is set, LOE's start time will be updated. Also, `cover` (url) uploads an image to use as the cover photo for the event.<br><br>Example: { start\_time: 1641013200, cover: 'https://your.url/image.jpg', } |
| `fisheye_video_cropped`<br><br>boolean | Whether the single fisheye video is cropped or not |
| `front_z_rotation`<br><br>float | The front z rotation in degrees on the single fisheye video |
| `is_spherical`<br><br>boolean | Flag that denotes the broadcast is a 360 live broadcast. |
| `original_fov`<br><br>int64 | Original field of view of the camera |
| `privacy`<br><br>Privacy Parameter | Privacy for this live video. |
| `projection`<br><br>enum {EQUIRECTANGULAR, CUBEMAP, HALF\_EQUIRECTANGULAR} | Flag that denotes expected projection for 360 live streams. The default value is EQUIRECTANGULAR. |
| `published`<br><br>boolean | Set this to false to preview the stream before going live.<br><br>                                    Deprecated. Prefer setting the status instead. |
| `schedule_custom_profile_image`<br><br>image | Custom image that will appear in the scheduled live story and lobby. |
| `spatial_audio_format`<br><br>enum {ambiX\_4} | Denotes the format of the spatial audio stream. When unspecified audio is presumed to be mono or stereo. |
| `status`<br><br>enum {UNPUBLISHED, LIVE\_NOW, SCHEDULED\_UNPUBLISHED, SCHEDULED\_LIVE, SCHEDULED\_CANCELED} | The status of the broadcast. A `LIVE_NOW` broadcast is currently live and visible to users. An `UNPUBLISHED` broadcast is in preparation; it's not visible to other users, and it may be automatically deleted after several hours in this state. (Consider using the `SCHEDULED` states to create a planned, future broadcast.) |
| `stereoscopic_mode`<br><br>enum {MONO, LEFT\_RIGHT, TOP\_BOTTOM} | Set this parameter to the stereoscopic mode for this video. |
| `stop_on_delete_stream`<br><br>boolean | Set this to true if stream should be stopped when deleteStream RTMP command received. |
| `title`<br><br>UTF-8 string | The title of the live video. Maximum 254 characters.<br><br>Supports Emoji |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node represented by `id` in the return type.

Struct {

`id`: numeric string,

`stream_url`: string,

`secure_stream_url`: string,

`stream_secondary_urls`: List \[

string

\],

`secure_stream_secondary_urls`: List \[

string

\],

`dash_ingest_url`: string,

`dash_ingest_secondary_urls`: List \[

string

\],

`event_id`: numeric string,

}

### Error Codes

| Error | Description |
| --- | --- |
| 6000 | There was a problem uploading your video file. Please try again with another file. |

You can make a POST request to `live_videos` edge from the following paths:

* [`/{group_id}/live_videos`](https://developers.facebook.com/docs/graph-api/reference/group/live_videos/)

When posting to this edge, a [LiveVideo](https://developers.facebook.com/docs/graph-api/reference/live-video/) will be created.

### Parameters

| Parameter | Description |
| --- | --- |
| `content_tags`<br><br>list<numeric string> | Tags that describe the contents of the Live Video. Use search endpoint with `type=adinterest` to get possible IDs. For example: `/search?type=adinterest&q=couscous` |
| `description`<br><br>UTF-8 string | The description of the Live Video<br><br>Supports Emoji |
| `enable_backup_ingest`<br><br>boolean | Set this to true to enable a backup ingest url. stop\_on\_delete\_stream defaults to false when set |
| `encoding_settings`<br><br>string | Identifier of the encoding settings group. Currently only used for live-360 broadcasts. The value should be the `identifier` key of the encoding settings preset. Encoding presets can be found by querying the `GET /broadcaster_encoding_settings` endpoint |
| `event_params`<br><br>Live Video Event Parameter | Parameters specific to Live Online Event broadcast. If `start_time` (unix timecode) is set, LOE's start time will be updated. Also, `cover` (url) uploads an image to use as the cover photo for the event.<br><br>Example: { start\_time: 1641013200, cover: 'https://your.url/image.jpg', } |
| `fisheye_video_cropped`<br><br>boolean | Whether the single fisheye video is cropped or not |
| `front_z_rotation`<br><br>float | The front z rotation in degrees on the single fisheye video |
| `is_spherical`<br><br>boolean | Denotes if the broadcast is a 360 live broadcast |
| `original_fov`<br><br>int64 | Original field of view of the camera |
| `privacy`<br><br>Privacy Parameter | Privacy for this Live Video |
| `projection`<br><br>enum {EQUIRECTANGULAR, CUBEMAP, HALF\_EQUIRECTANGULAR} | Flag that denotes expected projection for 360 live streams. The default value is EQUIRECTANGULAR |
| `published`<br><br>boolean | Set this to false to preview the stream before going live. Deprecated. Set the status instead |
| `schedule_custom_profile_image`<br><br>image | Custom image that will appear in the scheduled live story and lobby |
| `spatial_audio_format`<br><br>enum {ambiX\_4} | Denotes the format of the spatial audio stream. When unspecified audio is presumed to be mono or stereo |
| `status`<br><br>enum {UNPUBLISHED, LIVE\_NOW, SCHEDULED\_UNPUBLISHED, SCHEDULED\_LIVE, SCHEDULED\_CANCELED} | The status of the broadcast. A `LIVE_NOW` broadcast is currently live and visible to users. An `UNPUBLISHED` broadcast is in preparation; it's not visible to other users, and it may be automatically deleted after several hours in this state. (Consider using the `SCHEDULED` states to create a planned, future broadcast.) |
| `stereoscopic_mode`<br><br>enum {MONO, LEFT\_RIGHT, TOP\_BOTTOM} | The stereoscopic mode for this video |
| `stop_on_delete_stream`<br><br>boolean | Set this to true if stream should be stopped when deleteStream RTMP command received |
| `title`<br><br>UTF-8 string | Title of the live video. Maximum 254 characters.<br><br>Supports Emoji |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node represented by `id` in the return type.

Struct {

`id`: numeric string,

`stream_url`: string,

`secure_stream_url`: string,

`stream_secondary_urls`: List \[

string

\],

`secure_stream_secondary_urls`: List \[

string

\],

`dash_ingest_url`: string,

`dash_ingest_secondary_urls`: List \[

string

\],

`event_id`: numeric string,

}

### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |
| 1005 | Fail to upload cover photo. |
| 1000 | Invalid time for an event. |

You can make a POST request to `live_videos` edge from the following paths:

* [`/{page_id}/live_videos`](https://developers.facebook.com/docs/graph-api/reference/page/live_videos/)

When posting to this edge, a [LiveVideo](https://developers.facebook.com/docs/graph-api/reference/live-video/) will be created.

### Parameters

| Parameter | Description |
| --- | --- |
| `content_tags`<br><br>list<numeric string> | Tags that describe the contents of the video. Use search endpoint with `type=adinterest` to get possible IDs.<br><br>                                                      Example:<br>                                                      ~~~~<br>                                                      /search?type=adinterest&q=couscous<br>                                                      ~~~~ |
| `crossposting_actions`<br><br>array<JSON object> | List of desired changes to crossposting for this broadcast. Each change must provide a `page_id` and `action`. Example:<br><br>\[ {page\_id: 1234, action: 'enable\_crossposting'}, {page\_id: 4567, action: 'enable\_crossposting\_and\_create\_post'} \]<br><br>Available action types:<br><br>* `enable_crossposting`: Enables crossposting for this broadcast with the Page if it is not currently enabled. No change if crossposting is already enabled with the Page for this broadcast.<br>* `disable_crossposting`: Disables crossposting for this broadcast with the Page if it is currently enabled. No change if crossposting is not already enabled with the Page for this broadcast.<br>* `enable_crossposting_and_create_post`: Same as `enable_crossposting`, but will also create a post as the Page. The post will be created even if crossposting is already enabled for the Page. This option is subject to your [live crossposting relationships](https://www.facebook.com/help/publisher/1385580858214929) and will fail for Pages without the required permission.<br><br>When used with a Live Online Event, this will apply to the event. |
| `page_id`<br><br>page ID | page\_id<br><br>Required |
| `action`<br><br>enum {ENABLE\_CROSSPOSTING, DISABLE\_CROSSPOSTING, ENABLE\_CROSSPOSTING\_AND\_CREATE\_POST} | action<br><br>Required |
| `custom_labels`<br><br>list<string> | Labels used to describe the video. Unlike content tags, custom labels are not published and only appear in insights data. |
| `description`<br><br>UTF-8 string | The description of the live video.<br><br>Supports Emoji |
| `donate_button_charity_id`<br><br>numeric string or integer | Specifies the ID of the charity for which a donate button will be added to the live video. |
| `enable_backup_ingest`<br><br>boolean | Set this to true to enable a backup ingest url. stop\_on\_delete\_stream defaults to false when set |
| `encoding_settings`<br><br>string | Identifier of the encoding settings group the broadcaster is using for this stream. This parameter is currently only in use for live-360 broadcasts. The value to be passed to this parameter is the value of the `identifier` key of the encoding settings preset. Encoding presets can be found by querying the `/broadcaster_encoding_settings` Graph API endpoint (`GET` query). |
| `event_params`<br><br>Live Video Event Parameter | Parameters specific to Live Online Event broadcast. If `start_time` (unix timecode) is set, LOE's start time will be updated. Also, `cover` (url) uploads an image to use as the cover photo for the event.<br><br>Example: { start\_time: 1641013200, cover: 'https://your.url/image.jpg', } |
| `fisheye_video_cropped`<br><br>boolean | Whether the single fisheye video is cropped or not |
| `front_z_rotation`<br><br>float | The front z rotation in degrees on the single fisheye video |
| `game_show`<br><br>JSON object | Configure this live stream to be a game show |
| `game_type`<br><br>enum {KNOCKOUT} | game\_type<br><br>Required |
| `is_spherical`<br><br>boolean | Flag that denotes the broadcast is a 360 live broadcast. |
| `original_fov`<br><br>int64 | Original field of view of the camera |
| `privacy`<br><br>Privacy Parameter | Privacy for this live video. |
| `product_items`<br><br>list<numeric string> | Products which will be shown with live videos. |
| `projection`<br><br>enum {EQUIRECTANGULAR, CUBEMAP, HALF\_EQUIRECTANGULAR} | Flag that denotes expected projection for 360 live streams. The default value is EQUIRECTANGULAR. |
| `published`<br><br>boolean | Set this to false to preview the stream before going live.<br><br>                                                      Deprecated. Prefer setting the status instead. |
| `schedule_custom_profile_image`<br><br>image | Custom image that will appear in the scheduled live story and lobby. |
| `spatial_audio_format`<br><br>enum {ambiX\_4} | Denotes the format of the spatial audio stream. When unspecified audio is presumed to be mono or stereo. |
| `status`<br><br>enum {UNPUBLISHED, LIVE\_NOW, SCHEDULED\_UNPUBLISHED, SCHEDULED\_LIVE, SCHEDULED\_CANCELED} | The status of the broadcast. A `LIVE_NOW` broadcast is currently live and visible to users. An `UNPUBLISHED` broadcast is in preparation; it's not visible to other users, and it may be automatically deleted after several hours in this state. (Consider using the `SCHEDULED` states to create a planned, future broadcast.) |
| `stereoscopic_mode`<br><br>enum {MONO, LEFT\_RIGHT, TOP\_BOTTOM} | Set this parameter to the stereoscopic mode for this video. |
| `stop_on_delete_stream`<br><br>boolean | Set this to true if stream should be stopped when deleteStream RTMP command received. |
| `targeting`<br><br>target | Object that [limits the audience](https://www.facebook.com/help/352402648173466) for this content. Anyone not in these demographics will not be able to view this content.<br><br>When used with a Live Online Event, this will apply to the event. |
| `geo_locations`<br><br>Object |     |
| `countries`<br><br>list<string> |     |
| `regions`<br><br>list<Object> |     |
| `key`<br><br>int64 |     |
| `cities`<br><br>list<Object> |     |
| `key`<br><br>int64 |     |
| `zips`<br><br>list<Object> |     |
| `key`<br><br>string |     |
| `locales`<br><br>list<string> |     |
| `excluded_countries`[](#)<br><br>list<string> |     |
| `excluded_regions`[](#)<br><br>list<int64> |     |
| `excluded_cities`[](#)<br><br>list<int64> |     |
| `excluded_zipcodes`[](#)<br><br>list<string> |     |
| `timezones`[](#)<br><br>list<int64> |     |
| `age_min`<br><br>enum {13, 15, 18, 21, 25} |     |
| `title`<br><br>UTF-8 string | The title of the live video. Maximum 254 characters.<br><br>Supports Emoji |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node represented by `id` in the return type.

Struct {

`id`: numeric string,

`stream_url`: string,

`secure_stream_url`: string,

`stream_secondary_urls`: List \[

string

\],

`secure_stream_secondary_urls`: List \[

string

\],

`dash_ingest_url`: string,

`dash_ingest_secondary_urls`: List \[

string

\],

`event_id`: numeric string,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 1005 | Fail to upload cover photo. |
| 1000 | Invalid time for an event. |
| 475 | You have been temporarily blocked from posting videos because you added videos containing content that may belong to someone else. |

[](#)

Updating
--------

You can update a [LiveVideo](https://developers.facebook.com/docs/graph-api/reference/live-video/) by making a POST request to [`/{live_video_id}`](https://developers.facebook.com/docs/graph-api/reference/live-video/).

### Parameters

| Parameter | Description |
| --- | --- |
| `allow_bm_crossposting`<br><br>boolean | If set to true, makes this live video available for crossposting by Pages in your Business Manager. |
| `content_tags`<br><br>list<numeric string> | Tags that describe the contents of the video. Use search endpoint with `type=adinterest` to get possible IDs. For example, `/search?type=adinterest&q=couscous`. |
| `cross_share_to_group_ids`<br><br>list<numeric string> | List of Groups by ID where the broadcast will be shared. The broadcast owner will require publishing permission to the groups in order to share. |
| `crossposting_actions`<br><br>array<JSON object> | List of desired changes to crossposting for this broadcast. Each change must provide a `page_id` and `action`. Example:<br>    <br>    <br>                [<br>                  {page_id: 1234, action: 'enable_crossposting'},<br>                  {page_id: 4567, action: 'enable_crossposting_and_create_post'}<br>                ]<br>    <br>    <br>            Available action types:<br>    <br>    <br>            - `enable_crossposting`: Enables crossposting for this broadcast with the Page if it is not currently enabled. No change if crossposting is already enabled with the Page for this broadcast.<br>            - `disable_crossposting`: Disables crossposting for this broadcast with the Page if it is currently enabled. No change if crossposting is not already enabled with the Page for this broadcast.<br>            - `enable_crossposting_and_create_post`: Same as `enable_crossposting`, but will also create a post as the Page. The post will be created even if crossposting is already enabled for the Page. This option is subject to your [live crossposting relationships](https://www.facebook.com/help/publisher/1385580858214929) and will fail for Pages without the required permission.<br>    <br>            When used with a Live Online Event, this will apply to the event. |
| `page_id`<br><br>page ID | page\_id<br><br>Required |
| `action`<br><br>enum {ENABLE\_CROSSPOSTING, DISABLE\_CROSSPOSTING, ENABLE\_CROSSPOSTING\_AND\_CREATE\_POST} | action<br><br>Required |
| `custom_labels`<br><br>list<string> | Labels used to describe the video. Unlike content tags, custom labels are not published and only appear in insights data. |
| `description`<br><br>UTF-8 string | The description of live video<br><br>Supports Emoji |
| `direct_share_status`<br><br>int64 | The status to allow sponsor directly boost the post. |
| `disturbing`<br><br>boolean | If true, autoplay will be disabled and live video will have a graphic content warning overlay |
| `donate_button_charity_id`<br><br>int64 | Specifies the ID of the charity for which a donate button will be added to the live video. If zero is passed, will remove the donate button on the video. |
| `embeddable`<br><br>boolean | If true, live video will be embeddable |
| `end_live_video`<br><br>boolean | If true, the live video will be ended. Only valid if the live video is still running |
| `event_params`<br><br>Live Video Event Parameter | Parameters specific to Live Online Event broadcast. If `start_time` (unix timecode) is set, LOE's start time will be updated. Also, `cover` (url) uploads an image to use as the cover photo for the event. Example: { start\_time: 1641013200, cover: 'https://your.url/image.jpg', } |
| `is_manual_mode`<br><br>boolean | Flag to indicate that the scheduled broadcast is switched to manual mode |
| `live_comment_moderation_setting`<br><br>list<enum {DEFAULT, FOLLOWER, SLOW, DISCUSSION, RESTRICTED, PROTECTED\_MODE, SUPPORTER, NO\_HYPERLINK, FOLLOWED, TAGGED}> | Set of comment moderation settings for the live video |
| `master_ingest_stream_id`<br><br>numeric string | Ingest stream to set to master and route viewers to. |
| `persistent_stream_key_status`<br><br>enum {ENABLE, DISABLE, REGENERATE} | Set the status of the persistent stream key for this live video |
| `place`<br><br>place tag | Location associated with the video, if any. |
| `planned_start_time`<br><br>datetime/timestamp | Planned start time for a scheduled live video |
| `privacy`<br><br>Privacy Parameter | The privacy setting of live video |
| `published`<br><br>boolean | Should the live video be published? Only valid if not yet published.<br><br>            Deprecated. Prefer setting the status instead. |
| `schedule_custom_profile_image`<br><br>image | Custom image that will appear in the scheduled live story and lobby. |
| `schedule_feed_background_image`<br><br>image | Custom background image that appears in the updated scheduled live story |
| `sponsor_id`<br><br>numeric string or integer | Facebook Page id that is tagged as sponsor in the video post |
| `sponsor_relationship`<br><br>int64 | Sponsor Relationship, such as Presented By or Paid PartnershipWith |
| `status`<br><br>enum {UNPUBLISHED, LIVE\_NOW, SCHEDULED\_UNPUBLISHED, SCHEDULED\_LIVE, SCHEDULED\_CANCELED} | The status of the LiveVideo.<br><br>A `LIVE_NOW` LiveVideo is one that will be published to the intended destination (Timeline, Group, Page, etc) upon receiving valid video data, or one that is already published and actively streaming.<br><br>An `UNPUBLISHED` LiveVideo is in preparation; it's not visible to other users, and it may be automatically deleted after several hours in this state.<br><br>A `SCHEDULED_UNPUBLISHED` LiveVideo is scheduled to go live at a future time.<br><br>A `SCHEDULED_LIVE` LiveVideo is one whose scheduled time has passed, yet the stream is not yet live. Either in the process of transitioning, or still waiting for a valid video stream.<br><br>(Consider using the `SCHEDULED` states to create a planned, future LiveVideo.) |
| `tags`<br><br>list<int> | Users tagged in the live video. |
| `targeting`<br><br>target | Object that [limits the audience](https://www.facebook.com/help/352402648173466) for this content. Anyone not in these demographics will not be able to view this content.<br><br>When used with a Live Online Event, this will apply to the event. |
| `geo_locations`<br><br>Object |     |
| `countries`<br><br>list<string> |     |
| `regions`<br><br>list<Object> |     |
| `key`<br><br>int64 |     |
| `cities`<br><br>list<Object> |     |
| `key`<br><br>int64 |     |
| `zips`<br><br>list<Object> |     |
| `key`<br><br>string |     |
| `locales`<br><br>list<string> |     |
| `excluded_countries`[](#)<br><br>list<string> |     |
| `excluded_regions`[](#)<br><br>list<int64> |     |
| `excluded_cities`[](#)<br><br>list<int64> |     |
| `excluded_zipcodes`[](#)<br><br>list<string> |     |
| `timezones`[](#)<br><br>list<int64> |     |
| `age_min`<br><br>enum {13, 15, 18, 21, 25} |     |
| `title`<br><br>UTF-8 string | The title of the live video.<br><br>Supports Emoji |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node represented by `id` in the return type.

Struct {

`id`: numeric string,

`persistent_stream_url`: string,

`backup_persistent_stream_url`: string,

}

### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |
| 1005 | Fail to upload cover photo. |

[](#)

Deleting
--------

You can delete a [LiveVideo](https://developers.facebook.com/docs/graph-api/reference/live-video/) by making a DELETE request to [`/{live_video_id}`](https://developers.facebook.com/docs/graph-api/reference/live-video/).

### Limitations

You cannot delete a LiveVideo on a [User](https://developers.facebook.com/docs/graph-api/reference/user) or [Group](https://developers.facebook.com/docs/graph-api/reference/group).

### Parameters

This endpoint doesn't have any parameters.

### Return Type

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

[](#)

Live Video Blocked Users
========================

[](#)

Reading
-------

List of users who are blocked from video broadcast

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Blive-video-id%7D%2Fblocked_users&version=v18.0)

    GET /v18.0/{live-video-id}/blocked_users HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{live-video-id}/blocked_users',
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

    /* make the API call */
    FB.api(
        "/{live-video-id}/blocked_users",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{live-video-id}/blocked_users",
        null,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{live-video-id}/blocked_users"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

| Parameter | Description |
| --- | --- |
| `uid`<br><br>numeric string or integer | IDs of users who are blocked from the video broadcast |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [User](https://developers.facebook.com/docs/graph-api/reference/user/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 210 | User not visible |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Live Video Comments
===================

[](#)

Reading
-------

Comments for this object

### New Page Experience

This endpoint is supported for [New Page Experience](https://developers.facebook.com/docs/pages/new-pages-experience/).

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Blive-video-id%7D%2Fcomments&version=v18.0)

    GET /v18.0/{live-video-id}/comments HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{live-video-id}/comments',
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

    /* make the API call */
    FB.api(
        "/{live-video-id}/comments",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{live-video-id}/comments",
        null,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{live-video-id}/comments"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

| Parameter | Description |
| --- | --- |
| `filter`<br><br>enum{stream, toplevel} | Default value: `toplevel`<br><br>SELF\_EXPLANATORY |
| `live_filter`<br><br>enum{filter\_low\_quality, no\_filter} | Default value: `filter_low_quality`<br><br>For comments on a Live streaming video, this determines whether low quality comments will be filtered out of the results (filtering is enabled by default). In all other circumstances this parameter is ignored. |
| `order`<br><br>enum{chronological, reverse\_chronological} | Preferred ordering of the comments. Accepts chronological (oldest first) and reverse chronological (newest first). If the comments can be ranked, then the order will always be ranked regardless of this modifier. The best practice for querying comments on a Live video is to continually poll for comments in the reversechronological ordering mode. |
| `since`<br><br>datetime | Lower bound of the time range to consider |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {},
    "`summary`": {}
}

#### `data`

A list of [Comment](https://developers.facebook.com/docs/graph-api/reference/comment/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

#### `summary`

Aggregated information about the edge, such as counts. Specify the fields to fetch in the summary param (like `summary=order`).

| Field | Description |
| --- | --- |
| `order`<br><br>enum | Order of returned comments |
| `total_count`<br><br>unsigned int32 | Total number of people who commented |
| `can_comment`<br><br>bool | Can the viewer comment |

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Live Video Crossposted Broadcasts
=================================

[](#)

Reading
-------

Live videos which have been crossposted from this live video. This field is only available on the original live video.

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Blive-video-id%7D%2Fcrossposted_broadcasts&version=v18.0)

    GET /v18.0/{live-video-id}/crossposted_broadcasts HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{live-video-id}/crossposted_broadcasts',
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

    /* make the API call */
    FB.api(
        "/{live-video-id}/crossposted_broadcasts",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{live-video-id}/crossposted_broadcasts",
        null,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{live-video-id}/crossposted_broadcasts"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

This endpoint doesn't have any parameters.

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [LiveVideo](https://developers.facebook.com/docs/graph-api/reference/live-video/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Live Video Errors
=================

[](#)

Reading
-------

LiveVideoErrors

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Blive-video-id%7D%2Ferrors&version=v18.0)

    GET /v18.0/{live-video-id}/errors HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{live-video-id}/errors',
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

    /* make the API call */
    FB.api(
        "/{live-video-id}/errors",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{live-video-id}/errors",
        null,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{live-video-id}/errors"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

This endpoint doesn't have any parameters.

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of LiveVideoError nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Live Video Input Streams
========================

[](#)

Reading
-------

You can't perform this operation on this endpoint.

[](#)

Creating
--------

You can make a POST request to `input_streams` edge from the following paths:

* [`/{live_video_id}/input_streams`](https://developers.facebook.com/docs/graph-api/reference/live-video/input_streams/)

When posting to this edge, a [LiveVideoInputStream](https://developers.facebook.com/docs/graph-api/reference/live-video-input-stream/) will be created.

### Parameters

This endpoint doesn't have any parameters.

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node represented by `id` in the return type.

Struct {

`id`: numeric string,

}

### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Live Video Polls
================

[](#)

Represents a collection of [VideoPolls](https://developers.facebook.com/docs/graph-api/reference/video-poll) on a [LiveVideo](https://developers.facebook.com/docs/graph-api/reference/live-video).

[](#)

Reading
-------

Gets a list of [VideoPolls](https://developers.facebook.com/docs/graph-api/reference/video-poll) on a [LiveVideo](https://developers.facebook.com/docs/graph-api/reference/live-video).

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Blive-video-id%7D%2Fpolls&version=v18.0)

    GET /v18.0/{live-video-id}/polls HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{live-video-id}/polls',
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

    /* make the API call */
    FB.api(
        "/{live-video-id}/polls",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{live-video-id}/polls",
        null,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{live-video-id}/polls"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

This endpoint doesn't have any parameters.

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [VideoPoll](https://developers.facebook.com/docs/graph-api/reference/video-poll/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

[](#)

Creating
--------

You can make a POST request to `polls` edge from the following paths:

* [`/{live_video_id}/polls`](https://developers.facebook.com/docs/graph-api/reference/live-video/polls/)

When posting to this edge, a [VideoPoll](https://developers.facebook.com/docs/graph-api/reference/video-poll/) will be created.

### Parameters

| Parameter | Description |
| --- | --- |
| `correct_option`<br><br>int64 | Number of the correct option (in order, starting from 1) |
| `options`<br><br>array<string> | Text options for users to select in order<br><br>Required |
| `question`<br><br>string | Question text<br><br>Required |
| `show_results`<br><br>boolean | True to show the results after voting, otherwise false |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node represented by `id` in the return type.

Struct {

`id`: numeric string,

`option_ids`: List \[

numeric string

\],

}

### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Live Video Reactions
====================

[](#)

Reading
-------

Reactions for this object

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Blive-video-id%7D%2Freactions&version=v18.0)

    GET /v18.0/{live-video-id}/reactions HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{live-video-id}/reactions',
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

    /* make the API call */
    FB.api(
        "/{live-video-id}/reactions",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{live-video-id}/reactions",
        null,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{live-video-id}/reactions"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

| Parameter | Description |
| --- | --- |
| `type`<br><br>enum {NONE, LIKE, LOVE, WOW, HAHA, SAD, ANGRY, THANKFUL, PRIDE, CARE, FIRE, HUNDRED} | Reaction type |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {},
    "`summary`": {}
}

#### `data`

A list of [Profile](https://developers.facebook.com/docs/graph-api/reference/profile/) nodes.

The following fields will be added to each node that is returned:

| Field | Description |
| --- | --- |
| `type`<br><br>enum {NONE, LIKE, LOVE, WOW, HAHA, SAD, ANGRY, THANKFUL, PRIDE, CARE, FIRE, HUNDRED} | The reaction type<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

#### `summary`

Aggregated information about the edge, such as counts. Specify the fields to fetch in the summary param (like `summary=total_count`).

| Field | Description |
| --- | --- |
| `total_count`<br><br>unsigned int32 | Total number of reactions |
| `viewer_reaction`<br><br>enum {NONE, LIKE, LOVE, WOW, HAHA, SAD, ANGRY, THANKFUL, PRIDE, CARE, FIRE, HUNDRED} | The viewer's reaction |

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)