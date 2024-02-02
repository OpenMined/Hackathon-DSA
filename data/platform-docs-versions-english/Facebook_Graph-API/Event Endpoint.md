Event
=====

[](#)

Represents an [Event](https://www.facebook.com/help/572885262883136/).

### Limitations

Access to Events on [Users](https://developers.facebook.com/docs/graph-api/reference/user) and [Pages](https://developers.facebook.com/docs/graph-api/reference/page) is only available to Facebook Marketing Partners.

[](#)

Reading
-------

Get fields and edges on an Event.

### Requirements

For Events on an [App](https://developers.facebook.com/docs/graph-api/reference/application):

* An App access token of an App that created the Event.

For Events on a [Group](https://developers.facebook.com/docs/graph-api/reference/group):

* A User access token of an Admin of the Event.
* The [Groups API](https://developers.facebook.com/docs/apps/review/feature#reference-GROUPS_ACCESS) feature.

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bevent-id%7D&version=v18.0)

    GET /v18.0/{event-id} HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{event-id}',
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
        "/{event-id}",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{event-id}",
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
                                   initWithGraphPath:@"/{event-id}"
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

| Field | Description |
| --- | --- |
| `id`<br><br>numeric string | The event ID |
| `attending_count`[](#)<br><br>int32 | Number of people attending the event |
| `can_guests_invite`<br><br>bool | Can guests invite friends. Requires an access token of an Admin of the Event |
| `category`[](#)<br><br>enum {CLASSIC\_LITERATURE, COMEDY, CRAFTS, DANCE, DRINKS, FITNESS\_AND\_WORKOUTS, FOODS, GAMES, GARDENING, HEALTH\_AND\_MEDICAL, HEALTHY\_LIVING\_AND\_SELF\_CARE, HOME\_AND\_GARDEN, MUSIC\_AND\_AUDIO, PARTIES, PROFESSIONAL\_NETWORKING, RELIGIONS, SHOPPING\_EVENT, SOCIAL\_ISSUES, SPORTS, THEATER, TV\_AND\_MOVIES, VISUAL\_ARTS} | The category of the event |
| `cover`<br><br>[CoverPhoto](https://developers.facebook.com/docs/graph-api/reference/cover-photo/) | Cover picture |
| `created_time`<br><br>datetime | created\_time |
| `declined_count`[](#)<br><br>int32 | Number of people who declined the event |
| `description`<br><br>string | Long-form description<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `discount_code_enabled`<br><br>bool | Is discount code enabled for this event |
| `end_time`<br><br>string | End time, if one has been set<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `event_times`<br><br>list<ChildEvent> | Array of times of a multi-instance event<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `guest_list_enabled`<br><br>bool | Can see guest list. Requires an access token of an Admin of the Event |
| `interested_count`[](#)<br><br>int32 | Number of people interested in the event |
| `is_canceled`<br><br>bool | Whether or not the event has been marked as canceled |
| `is_draft`<br><br>bool | Whether the event is in draft mode or published. Requires an access token of an Admin of the Event |
| `is_online`<br><br>bool | Whether the event is online or not. Required to pass the 'address' (city name) parameter for online events. |
| `is_page_owned`<br><br>bool | Whether the event is created by page or not |
| `maybe_count`[](#)<br><br>int32 | Number of people who maybe going to the event |
| `name`<br><br>string | Event name<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `noreply_count`[](#)<br><br>int32 | Number of people who did not reply to the event |
| `online_event_format`<br><br>enum {messenger\_room, third\_party, fb\_live, other, none} | Type of online event - Live, Link or Other |
| `online_event_third_party_url`<br><br>string | Third party streaming url associated with Link events |
| `owner` | The profile that created the event |
| `place`[](#)<br><br>[Place](https://developers.facebook.com/docs/graph-api/reference/place/) | Event Place information<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `scheduled_publish_time`<br><br>string | Time when event is scheduled to be published |
| `start_time`<br><br>string | Start time<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `ticket_uri`<br><br>string | The link users can visit to buy a ticket to this event |
| `ticket_uri_start_sales_time`<br><br>string | Time when tickets go on sale |
| `ticketing_privacy_uri`<br><br>string | URI to seller's privacy policy for ticket purchases |
| `ticketing_terms_uri`<br><br>string | URI to seller's terms of service for ticket purchases |
| `timezone`<br><br>enum | Timezone |
| `type`[](#)<br><br>enum {private, public, group, community, friends, work\_company} | The type of the event |
| `updated_time`<br><br>datetime | Last update time (ISO 8601 formatted) |

### Edges

| Edge | Description |
| --- | --- |
| [`roles`](https://developers.facebook.com/docs/graph-api/reference/event/roles/)[](#) | List of profiles having roles on the event. Requires an access token of an Admin of the Event |
| [`ticket_tiers`](https://developers.facebook.com/docs/graph-api/reference/event/ticket_tiers/)[](#) | List of ticket tiers. Requires an access token of an Admin of the Event |

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 458 | The session is invalid because the application is not installed |
| 190 | Invalid OAuth 2.0 Access Token |

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

Event Live Videos
=================

[](#)

Reading
-------

SELF\_EXPLANATORY

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bevent-id%7D%2Flive_videos&version=v18.0)

    GET /v18.0/{event-id}/live_videos HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{event-id}/live_videos',
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
        "/{event-id}/live_videos",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{event-id}/live_videos",
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
                                   initWithGraphPath:@"/{event-id}/live_videos"
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

A list of Null nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |

[](#)

Creating
--------

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

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Graph API Reference [`/{event-id}`](https://developers.facebook.com/docs/graph-api/reference/event/)`/photos`
=============================================================================================================

All the photos uploaded to an event's wall.

[](#)

Reading
-------

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bevent-id%7D%2Fphotos&version=v18.0)

    GET /v18.0/{event-id}/photos HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{event-id}/photos',
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
        "/{event-id}/photos",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{event-id}/photos",
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
                                   initWithGraphPath:@"/{event-id}/photos"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### Permissions

* A user access token is required.
    

### Fields

An array of [Photo objects](https://developers.facebook.com/docs/graph-api/reference/photo).

[](#)

Publishing
----------

There are two separate ways of publishing photos to Facebook:

1. Capture a photo via file upload as `multipart/form-data` then use the `source` parameter:

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK

    POST /v18.0/{event-id}/photos HTTP/1.1
    Host: graph.facebook.com
    
    source=%7Bimage-data%7D

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->post(
        '/{event-id}/photos',
        array (
          'source' => '{image-data}',
        ),
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
        "/{event-id}/photos",
        "POST",
        {
            "source": "{image-data}"
        },
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    Bundle params = new Bundle();
    params.putString("source", "{image-data}");
    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{event-id}/photos",
        params,
        HttpMethod.POST,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    NSDictionary *params = @{
      @"source": @"{image-data}",
    };
    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{event-id}/photos"
                                          parameters:params
                                          HTTPMethod:@"POST"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

1. Use a photo that is already on the internet by publishing using the `url` parameter:

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK

    POST /v18.0/{event-id}/photos HTTP/1.1
    Host: graph.facebook.com
    
    url=%7Bimage-url%7D

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->post(
        '/{event-id}/photos',
        array (
          'url' => '{image-url}',
        ),
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
        "/{event-id}/photos",
        "POST",
        {
            "url": "{image-url}"
        },
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    Bundle params = new Bundle();
    params.putString("url", "{image-url}");
    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{event-id}/photos",
        params,
        HttpMethod.POST,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    NSDictionary *params = @{
      @"url": @"{image-url}",
    };
    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{event-id}/photos"
                                          parameters:params
                                          HTTPMethod:@"POST"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### Permissions

* A user access token with `publish_actions` permission can be used to publish new photos.
    

### Fields

| Name | Description | Type |
| --- | --- | --- |
| `source` | The photo, [encoded as form data](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.w3.org%2FTR%2Fhtml401%2Finteract%2Fforms.html%23h-17.13.4.2&h=AT2XLG5u0eCe4pRBD1EUIClGZb4BXOBN2BXwNZsDpJM-dES7Hl-w067fDz9ZZJEwUhMshwdbzTDl8I98DDlhZawlL0F35oFAiNYhb8twx9WgYeTF3xocuP9YPDKnqj3MeVdBMqZmAfnEi6VKqm70aQ). Either this or `url` field is required, but both should not be used together. | [`multipart/form-data`](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.w3.org%2FTR%2Fhtml401%2Finteract%2Fforms.html%23h-17.13.4.2&h=AT3Rb9HVNeXUN22kYayApNmlWqGPGWzbAJ1FbsGFblLWzChr6opQWsHD61YTzQpF0hOR4ez-G5DJkudr6qv6ijU9_v1WR9Fb_k28WOqbJxKb3IV721dal5jCil8O35JSbtM6eAZZOyPlCIpSJkcinw) |
| `url` | The URL of a photo that is already uploaded to the internet. Either this or `source` is required, but both should not be used together. | `string` |
| `message` | The description of the photo, used as the accompanying status message in any feed story. | `string` |

### Response

If successful:

| Name | Description | Type |
| --- | --- | --- |
| `id` | The newly created photo ID | `string` |

[](#)

Deleting
--------

You can't delete using this edge, however you can [delete each photo using the /{photo-id} node](https://developers.facebook.com/docs/reference/api/photo/).

[](#)

Updating
--------

You can't update using this edge.

[](#)

[](#)

[`/{event-id}`](https://developers.facebook.com/docs/graph-api/reference/event/)`/picture`
==========================================================================================

An event's cover photo with profile picture dimensions.

[](#)

Reading
-------

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bevent-id%7D%2Fpicture&version=v18.0)

    GET /v18.0/{event-id}/picture HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{event-id}/picture',
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
        "/{event-id}/picture",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{event-id}/picture",
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
                                   initWithGraphPath:@"/{event-id}/picture"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### Permissions

* A user access token is required to retrieve the cover photo of any events visible to that person.
    

#### Modifiers

| Name | Description | Type |
| --- | --- | --- |
| `redirect` | The `picture` edge is a special case, as when requested, it will by default return the picture itself and not a JSON response. To return a JSON response, you need to set `redirect=false` as a request attribute. This is how to return the [fields below](#readfields). | `bool` |
| `type` | You can use this to get a pre-specified size of picture. | `enum{small, normal, large, square}` |

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK

    GET /v18.0/{event-id}/picture?redirect=0&type=normal HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{event-id}/picture?redirect=0&type=normal',
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
        "/{event-id}/picture",
        {
            "redirect": false,
            "type": "normal"
        },
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    Bundle params = new Bundle();
    params.putBoolean("redirect", false);
    params.putString("type", "normal");
    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{event-id}/picture",
        params,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    NSDictionary *params = @{
      @"redirect": @NO,
      @"type": @"normal",
    };
    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{event-id}/picture"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### Fields

| Parameter | Description | Type |
| --- | --- | --- |
| `url` | The URL of the profile photo. Only returned when `redirect` is `false`. | `string` |
| `is_silhouette` | Indicates if the photo hasn't been customised and is the default icon. Only returned when `redirect` is `false`. | `boolean` |

[](#)

Publishing
----------

You can't publish an event cover photo using the Graph API.

[](#)

Deleting
--------

You can't delete an event cover photo using the Graph API.

[](#)

[](#)

Event Roles
===========

[](#)

Reading
-------

EventRoles

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bevent-id%7D%2Froles&version=v18.0)

    GET /v18.0/{event-id}/roles HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{event-id}/roles',
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
        "/{event-id}/roles",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{event-id}/roles",
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
                                   initWithGraphPath:@"/{event-id}/roles"
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

A list of [Profile](https://developers.facebook.com/docs/graph-api/reference/profile/) nodes.

The following fields will be added to each node that is returned:

| Field | Description |
| --- | --- |
| `role_type`<br><br>enum | The type of the role of the profile on the event<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |

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

Event Ticket Tiers
==================

[](#)

Reading
-------

EventTicketTiers

Starting September 14, 2021, this endpoint will throw an error for version 12.0+ calls made by apps that lack the endpoint's required permissions. This change will apply to all versions on December 13, 2021.

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bevent-id%7D%2Fticket_tiers&version=v18.0)

    GET /v18.0/{event-id}/ticket_tiers HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{event-id}/ticket_tiers',
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
        "/{event-id}/ticket_tiers",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{event-id}/ticket_tiers",
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
                                   initWithGraphPath:@"/{event-id}/ticket_tiers"
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

A list of [EventTicketTier](https://developers.facebook.com/docs/graph-api/reference/event-ticket-tier/) nodes.

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