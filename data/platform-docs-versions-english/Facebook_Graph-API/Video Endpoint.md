Video Captions
==============

[](#)

Reading
-------

VideoCaptions

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bvideo-id%7D%2Fcaptions&version=v18.0)

    GET /v18.0/{video-id}/captions HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{video-id}/captions',
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
        "/{video-id}/captions",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{video-id}/captions",
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
                                   initWithGraphPath:@"/{video-id}/captions"
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

A list of [VideoCaption](https://developers.facebook.com/docs/graph-api/reference/video-caption/) nodes.

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

### Permissions

To update a video's caption, you need one of the following:

* User is the owner of the video
    
* User has manage access on page that owns the video
    
* User has advertiser access on account that owns the video
    

### Limitations

The file size limit for video captions is 200K.  
  

You can update a [Video](https://developers.facebook.com/docs/graph-api/reference/video/) by making a POST request to [`/{video_id}/captions`](https://developers.facebook.com/docs/graph-api/reference/video/captions/).

### Parameters

| Parameter | Description |
| --- | --- |
| `captions_file`<br><br>file | Caption file in SRT (SubRip Text) format. File name must be in the format filename.locale.srt |
| `default_locale`<br><br>string | Specify which locale should be used as the default for the video. Can be set to 'none' |
| `locales_to_delete`<br><br>list<string> | Default value: `Vector`<br><br>locales of caption to delete |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node to which you POSTed.

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 482 | The captions files you selected contain locales that had been applied to video, please remove and try again. |
| 387 | There was a problem uploading your captions file. Please try again. |
| 386 | You uploaded a .SRT file with an incorrect file name. Please use this format: filename.en\_US.srt |
| 100 | Invalid parameter |
| 385 | The captions file you selected is in a format that we don't support. |

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Video Comments
==============

[](#)

Reading
-------

Comments for this object

### New Page Experience

This endpoint is supported for [New Page Experience](https://developers.facebook.com/docs/pages/new-pages-experience/).

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bvideo-id%7D%2Fcomments&version=v18.0)

    GET /v18.0/{video-id}/comments HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{video-id}/comments',
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
        "/{video-id}/comments",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{video-id}/comments",
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
                                   initWithGraphPath:@"/{video-id}/comments"
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
| 80001 | There have been too many calls to this Page account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 190 | Invalid OAuth 2.0 Access Token |

[](#)

Creating
--------

You can make a POST request to `comments` edge from the following paths:

* [`/{video_id}/comments`](https://developers.facebook.com/docs/graph-api/reference/video/comments/)

When posting to this edge, a [Comment](https://developers.facebook.com/docs/graph-api/reference/comment/) will be created.

### Parameters

| Parameter | Description |
| --- | --- |
| `attachment_id`<br><br>numeric string or integer | ID for a photo attachment to associate with this |
| `attachment_share_url`<br><br>URL | Link to set the comment attachment to. Does not include the url in the message |
| `attachment_url`<br><br>URL | Link to set the comment attachment to |
| `is_offline`<br><br>boolean | Whether the comment was originally made while offline |
| `message`<br><br>UTF-8 string | Same as the text param<br><br>Supports Emoji |
| `text`<br><br>UTF-8 string | The text of the comment that allows emoji<br><br>Supports Emoji |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node represented by `id` in the return type.

Struct {

`id`: token with structure: Comment ID,

}

### Error Codes

| Error | Description |
| --- | --- |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 190 | Invalid OAuth 2.0 Access Token |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 1705 | There was an error during posting. |
| 459 | The session is invalid because the user has been checkpointed |

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Video Crosspost Shared Pages
============================

[](#)

Reading
-------

VideoCrosspostSharedPages

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bvideo-id%7D%2Fcrosspost_shared_pages&version=v18.0)

    GET /v18.0/{video-id}/crosspost_shared_pages HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{video-id}/crosspost_shared_pages',
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
        "/{video-id}/crosspost_shared_pages",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{video-id}/crosspost_shared_pages",
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
                                   initWithGraphPath:@"/{video-id}/crosspost_shared_pages"
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

A list of [Page](https://developers.facebook.com/docs/graph-api/reference/page/) nodes.

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

Video Gaming Clip Create
========================

[](#)

Reading
-------

You can't perform this operation on this endpoint.

[](#)

Creating
--------

You can make a POST request to `gaming_clip_create` edge from the following paths:

* [`/{video_id}/gaming_clip_create`](https://developers.facebook.com/docs/graph-api/reference/video/gaming_clip_create/)

When posting to this edge, a [Video](https://developers.facebook.com/docs/graph-api/reference/video/) will be created.

### Parameters

| Parameter | Description |
| --- | --- |
| `duration_seconds`<br><br>float | Default value: `60`<br><br>The duration in seconds to create the clip. Should be a positive number. |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node to which you POSTed.

Struct {

`id`: numeric string,

}

### Error Codes

| Error | Description |
| --- | --- |
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

Video Likes
===========

[](#)

Reading
-------

Likes for this object

### New Page Experience

This endpoint is supported for [New Page Experience](https://developers.facebook.com/docs/pages/new-pages-experience/).

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bvideo-id%7D%2Flikes&version=v18.0)

    GET /v18.0/{video-id}/likes HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{video-id}/likes',
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
        "/{video-id}/likes",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{video-id}/likes",
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
                                   initWithGraphPath:@"/{video-id}/likes"
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
    "`paging`": {},
    "`summary`": {}
}

#### `data`

A list of [Profile](https://developers.facebook.com/docs/graph-api/reference/profile/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

#### `summary`

Aggregated information about the edge, such as counts. Specify the fields to fetch in the summary param (like `summary=total_count`).

| Field | Description |
| --- | --- |
| `total_count`<br><br>unsigned int32 | Total number of likes |
| `can_like`<br><br>bool | Can the viewer like |
| `has_liked`<br><br>bool | Has the viewer liked |

### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |
| 80001 | There have been too many calls to this Page account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |
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

Video Picture
=============

[](#)

Reading
-------

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bvideo-id%7D%2Fpicture&version=v18.0)

    GET /v18.0/{video-id}/picture HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{video-id}/picture',
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
        "/{video-id}/picture",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{video-id}/picture",
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
                                   initWithGraphPath:@"/{video-id}/picture"
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
| `redirect`<br><br>boolean | Default value: `true`<br><br>By default the picture edge will return a picture instead of a JSON response. If you want the picture edge to return JSON that describes the image set `redirect=0` when you make the request. |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [ProfilePictureSource](https://developers.facebook.com/docs/graph-api/reference/profile-picture-source/) nodes.

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

Video Poll Settings
===================

[](#)

Reading
-------

Poll Settings for Video

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bvideo-id%7D%2Fpoll_settings&version=v18.0)

    GET /v18.0/{video-id}/poll_settings HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{video-id}/poll_settings',
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
        "/{video-id}/poll_settings",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{video-id}/poll_settings",
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
                                   initWithGraphPath:@"/{video-id}/poll_settings"
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

A list of PollSettings nodes.

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

Video Polls
===========

[](#)

Reading
-------

Polls attached to this video

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bvideo-id%7D%2Fpolls&version=v18.0)

    GET /v18.0/{video-id}/polls HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{video-id}/polls',
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
        "/{video-id}/polls",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{video-id}/polls",
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
                                   initWithGraphPath:@"/{video-id}/polls"
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
| 210 | User not visible |

[](#)

Creating
--------

You can make a POST request to `polls` edge from the following paths:

* [`/{video_id}/polls`](https://developers.facebook.com/docs/graph-api/reference/video/polls/)

When posting to this edge, a [Video](https://developers.facebook.com/docs/graph-api/reference/video/) will be created.

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

Video Sponsor Tags
==================

[](#)

Reading
-------

VideoSponsorTags

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bvideo-id%7D%2Fsponsor_tags&version=v18.0)

    GET /v18.0/{video-id}/sponsor_tags HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{video-id}/sponsor_tags',
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
        "/{video-id}/sponsor_tags",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{video-id}/sponsor_tags",
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
                                   initWithGraphPath:@"/{video-id}/sponsor_tags"
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

A list of [Page](https://developers.facebook.com/docs/graph-api/reference/page/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
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

Video Tags
==========

[](#)

Reading
-------

VideoTags

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bvideo-id%7D%2Ftags&version=v18.0)

    GET /v18.0/{video-id}/tags HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{video-id}/tags',
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
        "/{video-id}/tags",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{video-id}/tags",
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
                                   initWithGraphPath:@"/{video-id}/tags"
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

A list of [TaggableSubject](https://developers.facebook.com/docs/graph-api/reference/taggable-subject/) nodes.

The following fields will be added to each node that is returned:

| Field | Description |
| --- | --- |
| `created_time`<br><br>datetime | The time the tag was created<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |

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

Video Thumbnails
================

[](#)

Represents a collection of [VideoThumbnails ![](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.2365-6/310307727_3347317042262105_1088877051262827250_n.png?_nc_cat=107&ccb=1-7&_nc_sid=e280be&_nc_ohc=831MNFLSQwkAX_NBYJc&_nc_ht=scontent-cdg4-2.xx&oh=00_AfBFzfp_r0uP87LWhIW9LbUGV2HepuPyhHSxWkm3ugn0Bg&oe=65CA3DE2)](https://developers.facebook.com/docs/graph-api/reference/video-thumbnail) on a [Video ![](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.2365-6/310307727_3347317042262105_1088877051262827250_n.png?_nc_cat=107&ccb=1-7&_nc_sid=e280be&_nc_ohc=831MNFLSQwkAX_NBYJc&_nc_ht=scontent-cdg4-2.xx&oh=00_AfBFzfp_r0uP87LWhIW9LbUGV2HepuPyhHSxWkm3ugn0Bg&oe=65CA3DE2)](https://developers.facebook.com/docs/graph-api/reference/video) 

[](#)

Reading
-------

Get a list of [VideoThumbnails](https://developers.facebook.com/docs/graph-api/reference/video-thumbnail/) on a [Video](https://developers.facebook.com/docs/graph-api/reference/video/).

### Requirements

| Type | Requirement |
| --- | --- |
| [Access Tokens ![](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.2365-6/310307727_3347317042262105_1088877051262827250_n.png?_nc_cat=107&ccb=1-7&_nc_sid=e280be&_nc_ohc=831MNFLSQwkAX_NBYJc&_nc_ht=scontent-cdg4-2.xx&oh=00_AfBFzfp_r0uP87LWhIW9LbUGV2HepuPyhHSxWkm3ugn0Bg&oe=65CA3DE2)](https://developers.facebook.com/docs/facebook-login/access-tokens) | App or Page |
| [Permissions ![](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.2365-6/310307727_3347317042262105_1088877051262827250_n.png?_nc_cat=107&ccb=1-7&_nc_sid=e280be&_nc_ohc=831MNFLSQwkAX_NBYJc&_nc_ht=scontent-cdg4-2.xx&oh=00_AfBFzfp_r0uP87LWhIW9LbUGV2HepuPyhHSxWkm3ugn0Bg&oe=65CA3DE2)](https://developers.facebook.com/docs/permissions/reference#p) | `pages_read_engagement`, `pages_show_list` |

### Examples

curl \-X GET "https://graph.facebook.com/**_`v18.0`_**/**_video-id_**/thumbnails?access\_token=**_page\_access\_token_**"

On success your app receives a list of VideoThumbnail objects for the video.

{
"id": "**_video-id-1_**",
"height": **_1280_**,
"scale": 1,
"uri": "**_url-for-video-1_**",
"width": **_720_**,
"is\_preferred": **_false_**
},
{
"id": "**_video-id-2_**",
"height": **_1280_**,
"scale": 1,
"uri": "**_url-for-video-2_**",
"width": **_720_**,
"is\_preferred": **_false_**
},
...

### Parameters

This endpoint doesn't have any parameters.

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [VideoThumbnail](https://developers.facebook.com/docs/graph-api/reference/video-thumbnail/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 190 | Invalid OAuth 2.0 Access Token |

[](#)

Creating
--------

You can make a POST request to `thumbnails` edge from the following paths:

* [`/{video_id}/thumbnails`](https://developers.facebook.com/docs/graph-api/reference/video/thumbnails/)

When posting to this edge, a [VideoThumbnail](https://developers.facebook.com/docs/graph-api/reference/video-thumbnail/) will be created.

### Limitations

* Maximum thumbnail file size 10MB.
* Thumbnails can only be created on [Videos](https://developers.facebook.com/docs/graph-api/reference/video/) that have been associated with a [Page](https://developers.facebook.com/docs/graph-api/reference/page/).
* We recommend that you use thumbnails with the same aspect ratio as the video.

### Requirements

| Type | Requirement |
| --- | --- |
| [Access Tokens ![](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.2365-6/310307727_3347317042262105_1088877051262827250_n.png?_nc_cat=107&ccb=1-7&_nc_sid=e280be&_nc_ohc=831MNFLSQwkAX_NBYJc&_nc_ht=scontent-cdg4-2.xx&oh=00_AfBFzfp_r0uP87LWhIW9LbUGV2HepuPyhHSxWkm3ugn0Bg&oe=65CA3DE2)](https://developers.facebook.com/docs/facebook-login/access-tokens) | App or Page |
| [Permissions ![](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.2365-6/310307727_3347317042262105_1088877051262827250_n.png?_nc_cat=107&ccb=1-7&_nc_sid=e280be&_nc_ohc=831MNFLSQwkAX_NBYJc&_nc_ht=scontent-cdg4-2.xx&oh=00_AfBFzfp_r0uP87LWhIW9LbUGV2HepuPyhHSxWkm3ugn0Bg&oe=65CA3DE2)](https://developers.facebook.com/docs/permissions/reference#p) | `pages_read_user_content`, `pages_manage_engagement`, `pages_show_list` |

### Examples

curl \-X POST "https://graph.facebook.com/**_`v18.0`_**/**_video-id_**/thumbnails
   ?access\_token=**_page\_access\_token_**
   &is\_preferred=**_true_**
   &source=@**_ThumbnailSample1.jpg_**"

On success your app receives a list of VideoThumbnail objects for the video.

{
  "success": **_true_**
}

### Parameters

| Parameter | Description |
| --- | --- |
| `is_preferred`<br><br>boolean | Default value: `false`<br><br>Set to `true` if this thumbnail is the preferred thumbnail to be shown for this video |
| `source`<br><br>image | The source for the thumbnail, an image file<br><br>Required |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node to which you POSTed.

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
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

Video Insights
==============

[](#)

Reading
-------

Get aggregated insight metrics for videos on a [Page](https://developers.facebook.com/docs/graph-api/reference/page). You can get metrics for Videos, Reels, and Ad Breaks. For the full list of metrics, see [Available Metrics](#metrics).

### Requirements

* The [pages\_manage\_engagement](https://developers.facebook.com/docs/permissions/reference/pages_manage_engagement) Permission.
* The [read\_insights](https://developers.facebook.com/docs/permissions/reference/read_insights) Permission.
* A Page access token requested by a person who is able to perform `ANALYZE` [Tasks](https://developers.facebook.com/docs/pages/overview#tasks) on a Page.
* Only Page admins can query earnings insights by using the API. Learn about [setting up user roles for a Page.](https://www.facebook.com/help/187316341316631)

### Limitations

* Insights for Videos on [Users](https://developers.facebook.com/docs/graph-api/reference/user) or [Groups](https://developers.facebook.com/docs/graph-api/reference/group) are not available.
* Data is only available for the past 2 years.
* A crossposted Video will have a unique video ID for each Page it was posted to.

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bvideo-id%7D%2Fvideo_insights&version=v18.0)

    GET /v18.0/{video-id}/video_insights HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{video-id}/video_insights',
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
        "/{video-id}/video_insights",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{video-id}/video_insights",
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
                                   initWithGraphPath:@"/{video-id}/video_insights"
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
| `metric`<br><br>list<A valid metric for an insights endpoint> | A list of [available metrics](#metrics) that you want to receive. |
| `period`<br><br>enum{day, week, days\_28, month, lifetime, total\_over\_range} | The aggregation period. |
| `since`<br><br>datetime/timestamp | Lower bound of the time range to consider. |
| `until`<br><br>datetime/timestamp | Upper bound of the time range to consider. |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [InsightsResult](https://developers.facebook.com/docs/graph-api/reference/insights-result/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |
| 80001 | There have been too many calls to this Page account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |

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

Available Metrics
-----------------

### Ad Breaks Metrics

The following metrics are available for the `metric` [parameter](#parameters) when you read aggregated insights for ad breaks.

| Name | Description | Values for `period` |
| --- | --- | --- |
| `total_video_ad_break_ad_cpm` | The average amount paid by advertisers for 1,000 impressions of their ads in your video, in U.S. cents. This number also includes the amount paid to Facebook. | day, lifetime |
| `total_video_ad_break_ad_impressions` | Number of times an ad was shown during your video's ad breaks. | day, lifetime |
| `total_video_ad_break_earnings` | An estimate of the amount you earned from ad breaks in your video, in U.S. cents, based on the number of impressions and CPM of ads shown. Actual payments may differ if there are content ownership claims or other adjustments. | day, lifetime |

### Reels Metrics

The following metrics are available for the `metric` [parameter](#parameters) when you read aggregated insights for a reel. For more information about Reels, see [Reels Developer Documentation](https://developers.facebook.com/docs/reels).

| Name | Description | Values for `period` |
| --- | --- | --- |
| `blue_reels_play_count` | The number of times your reel starts to play after an impression is already counted. This metric counts reels sessions with 1 millisecond or more of playback. This metric excludes replays. | lifetime |
| `post_impressions_unique` | The number of people who saw your reel at least once, whether or not the person played your reel. This metric is different from impressions, which includes multiple views of your reel by the same person. This metric is estimated. | lifetime |
| `post_video_avg_time_watched` | The average number of milliseconds your reel was played during a single instance of playing it, including time spent replaying your reel. Because this metric includes replays, the value can be greater than the total length of the reel. | lifetime |
| `post_video_likes_by_reaction_type` | The number of likes on your reel. | lifetime |
| `post_video_social_actions` | The number of comments on your reel and the number of times your reel was shared. | lifetime |
| `post_video_view_time` | The total number of milliseconds your reel played, including time spent replaying your reel. | lifetime |

### Video Metrics

The following metrics are available for the `metric` [parameter](#parameters) when you read aggregated insights for a video.

| Name | Description | Values for `period` |
| --- | --- | --- |
| `total_video_views` | The number of times your videos played for at least 3 seconds, or for nearly their total length if they're shorter than 3 seconds. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_views_unique` | The number of people who viewed your videos for at least 3 seconds, or for nearly their total length if they're shorter than 3 seconds. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_views_autoplayed` | The number of times your videos automatically played for at least 3 seconds, or for nearly their total length if they're shorter than 3 seconds. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_views_clicked_to_play` | The number of times your videos played for at least 3 seconds, or for nearly their total length if they're shorter than 3 seconds, after people clicked play. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_views_organic` | The number of times your videos played for at least 3 seconds, or for nearly their total length if they're shorter than 3 seconds, by organic reach. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_views_organic_unique` | The number of people who viewed your videos for at least 3 seconds, or for nearly their total length if they're shorter than 3 seconds, by organic reach. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_views_paid` | The number of times your promoted videos played for at least 3 seconds, or for nearly their total length if they're shorter than 3 seconds. For each [impression](https://www.facebook.com/business/help/675615482516035) of a video, we'll count video views separately and exclude any time spent replaying the video. | lifetime |
| `total_video_views_paid_unique` | The number of people who viewed your promoted videos for at least 3 seconds, or for nearly their total length if they're shorter than 3 seconds. For each [impression](https://www.facebook.com/business/help/675615482516035) of a video, we'll count video views separately and exclude any time spent replaying the video. | lifetime |
| `total_video_views_sound_on` | The number of times your videos played with sound on for at least 3 seconds, or for nearly their total length if they're shorter than 3 seconds. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_complete_views` | The number of times your videos played for 97%, or more, or its length. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_complete_views_unique` | The number of people who viewed your videos for 97%, or more, of its length. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_complete_views_auto_played` | The number of times your videos automatically played for 97%, or more, of its length. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_complete_views_clicked_to_play` | The number of times your videos played for 97%, or more, of its length, after people clicked play. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_complete_views_organic` | The number of times your videos played for 97%, or more, of its length, by organic reach. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_complete_views_organic_unique` | The number of people who viewed your videos for 97%, or more, of its length, by organic reach. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_complete_views_paid` | The number of times your promoted videos played for 97%, or more, of its length. For each [impression](https://www.facebook.com/business/help/675615482516035) of a video, we'll count video views separately and exclude any time spent replaying the video. | lifetime |
| `total_video_complete_views_paid_unique` | The number of people who viewed your promoted videos for 97%, or more, of its length. For each [impression](https://www.facebook.com/business/help/675615482516035) of a video, we'll count video views separately and exclude any time spent replaying the video. | lifetime |
| `total_video_10s_views` | The number of times your videos played for 10 seconds. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_10s_views_unique` | The number of people who viewed your videos for 10 seconds or more. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_10s_views_auto_played` | The number of times your videos automatically played for 10 seconds or more. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_10s_views_clicked_to_play` | The number of times your videos played for 10 seconds or more, after people clicked play. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_10s_views_organic` | The number of times your videos played for 10 seconds or more, by organic reach. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_10s_views_paid` | The number of times your promoted videos played for 10 seconds or more. For each [impression](https://www.facebook.com/business/help/675615482516035) of a video, we'll count video views separately and exclude any time spent replaying the video. | lifetime |
| `total_video_10s_views_sound_on` | The number of times your videos played with sound on for 10 seconds or more. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_15s_views` | The number of times your videos played for 15 seconds or more. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_60s_excludes_shorter_views` | The number of times your videos played for 60 seconds or more. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_retention_graph` | The number of times your videos played at each interval as a percentage of all views. Videos are divided into 40 equal intervals. Retention graphs may show more [impressions](https://www.facebook.com/business/help/675615482516035) later in the video than at the beginning. People might start the video in the middle, skip ahead, save, and rewatch it from that point, or other similar behaviors | lifetime |
| `total_video_retention_graph_autoplayed` | The number of times your videos automatically played at each interval as a percentage of all views. Videos are divided into 40 equal intervals. Retention graphs may show more [impressions](https://www.facebook.com/business/help/675615482516035) later in the video than at the beginning. People might start the video in the middle, skip ahead, save, and rewatch it from that point, or other similar behaviors. | lifetime |
| `total_video_retention_graph_clicked_to_play` | The number of times your videos played at each interval as a percentage of all views, after people clicked play. Videos are divided into 40 equal intervals. Retention graphs may show more [impressions](https://www.facebook.com/business/help/675615482516035) later in the video than at the beginning. People might start the video in the middle, skip ahead, save, and rewatch it from that point, or other similar behaviors. | lifetime |
| `total_video_avg_time_watched` | The average time, in milliseconds, people viewed your videos. | lifetime |
| `total_video_view_total_time` | The total time, in milliseconds, people viewed your videos. | lifetime |
| `total_video_view_total_time_organic` | The total time, in milliseconds, people viewed your videos, by organic reach. | lifetime |
| `total_video_view_total_time_paid` | The total time, in milliseconds, people viewed your promoted videos. | lifetime |
| `total_video_impressions` | The total number of [impressions](https://www.facebook.com/business/help/675615482516035) of your videos. | lifetime |
| `total_video_impressions_unique` | The total number of unique [impressions](https://www.facebook.com/business/help/675615482516035) of your videos. | lifetime |
| `total_video_impressions_paid_unique` | The total number of unique [impressions](https://www.facebook.com/business/help/675615482516035) or your promoted videos. | lifetime |
| `total_video_impressions_paid` | The total number of [impressions](https://www.facebook.com/business/help/675615482516035) of your promoted videos. | lifetime |
| `total_video_impressions_organic_unique` | The total number of unique [impressions](https://www.facebook.com/business/help/675615482516035) of your videos, by organic reach. | lifetime |
| `total_video_impressions_organic` | The total number of [impressions](https://www.facebook.com/business/help/675615482516035) of your videos, by organic reach. | lifetime |
| `total_video_impressions_viral_unique` | The total number of unique [impressions](https://www.facebook.com/business/help/675615482516035) of your videos in a friend's story. | lifetime |
| `total_video_impressions_viral` | The total number of [impressions](https://www.facebook.com/business/help/675615482516035) of your videos in a story generated by a friend. | lifetime |
| `total_video_impressions_fan_unique` | The total number of unique [impressions](https://www.facebook.com/business/help/675615482516035) of your videos for people who liked your Page. | lifetime |
| `total_video_impressions_fan` | The total number of [impressions](https://www.facebook.com/business/help/675615482516035) of your videos for people who liked your Page. | lifetime |
| `total_video_impressions_fan_paid_unique` | The total number of unique [impressions](https://www.facebook.com/business/help/675615482516035) of your promoted videos for people who liked your Page. | lifetime |
| `total_video_impressions_fan_paid` | The total number of [impressions](https://www.facebook.com/business/help/675615482516035) of your promoted video for people who liked your Page. | lifetime |
| `total_video_stories_by_action_type` | The total number of stories created about your Page's video, by action type; liking, commenting, sharing, etc. | lifetime |
| `total_video_reactions_by_type_total` | The total number of reactions to your Page's video, by type. | lifetime |
| `total_video_view_time_by_age_bucket_and_gender` | The total time, in milliseconds, your video has been viewed by Top Audiences; age and gender. | lifetime |
| `total_video_view_time_by_region_id` | The total time, in milliseconds, your Page's videos played for your Top 45 Locations; Region - Country. | lifetime |
| `total_video_views_by_distribution_type` | The number of times your videos played by distribution type; page\_owned and shared. | lifetime |
| `total_video_view_time_by_distribution_type` | The total time, in milliseconds, your Page's videos played by distribution type; page\_owned and shared. | lifetime |
| `total_video_view_total_time_live` | Total time (in ms) video has been viewed when it was broadcasted live. (Total Count). | lifetime |
| `total_video_views_by_country_id` | Lifetime video views by country. | lifetime |
| `total_video_views_live` | Number of people who viewed your video for 3 seconds or viewed to the end, when it was streamed live. | lifetime |
| `total_video_views_by_age_bucket_and_gender` | Lifetime video views by age bucket and gender. | lifetime |
| `total_video_views_gender_male` | Lifetime total number of times your videos played for at least 3 seconds, or for nearly their total length if they're shorter than 3 seconds by male viewers. | lifetime |
| `total_video_views_gender_female` | Lifetime total number of times your videos played for at least 3 seconds, or for nearly their total length if they're shorter than 3 seconds by female viewers. | lifetime |
| `total_video_views_live_clicked_to_play` | Lifetime total number of times people clicked to play your video and viewed it more than 3 seconds - while it was being streamed live. | lifetime |
| `total_video_views_gender_male_live` | Lifetime total number of times males viewed your video for more than 3 seconds while it was being streamed live. | lifetime |
| `total_video_views_live_autoplayed` | Lifetime total number of times your video started automatically playing and people viewed it for more than 3 seconds - while it was being streamed live. | lifetime |
| `total_video_views_gender_female_live` | Lifetime total number of times females viewed your video for more than 3 seconds while it was being streamed live. | lifetime |
| `has_total_video_views_by_publisher_platform_type` | Whether the video played for at least 3 seconds, or for nearly their total length if they're shorter than 3 seconds broken down by publisher platform type. | lifetime |
| `total_video_30s_views` | Total number of times your video was viewed for 30 seconds or 97% of the video if video is less than 30 seconds. (Total Count) | lifetime |

[](#)