Video Poll
==========

Reading
-------

Embedded video poll

### Feature Permissions

| Name | Description |
| --- | --- |
| Live video API | This [feature permission](https://developers.facebook.com/docs/videos/live-video-api/) may be required. |

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bvideo-poll-id%7D&version=v19.0)

    GET /v19.0/{video-poll-id} HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{video-poll-id}',
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
        "/{video-poll-id}",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{video-poll-id}",
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
                                   initWithGraphPath:@"/{video-poll-id}"
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
| `id`<br><br>numeric string | The poll ID<br><br>[Core](https://developers.facebook.com/docs/apps/versions/#coreextended)[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `question`<br><br>string | The poll question text |
| `show_results`<br><br>bool | True if this is a Live poll and voting is open and the results show after voting |
| `status`<br><br>enum {closed, voting\_open, results\_open} | Live poll status |

### Edges

| Edge | Description |
| --- | --- |
| [`poll_options`](https://developers.facebook.com/docs/graph-api/reference/video-poll/poll_options/) | Options available on this poll |

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

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

Updating
--------

You can update a [VideoPoll](https://developers.facebook.com/docs/graph-api/reference/video-poll/) by making a POST request to [`/{video_poll_id}`](https://developers.facebook.com/docs/graph-api/reference/video-poll/).

### Parameters

| Parameter | Description |
| --- | --- |
| `action`<br><br>enum {ATTACH\_TO\_VIDEO, CLOSE, SHOW\_VOTING, SHOW\_RESULTS, DELETE\_POLL} | Change state for the poll<br><br>Required |
| `show_results`<br><br>boolean | True if the viewer sees results after voting, false if they do not |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node represented by `id` in the return type.

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

Deleting
--------

You can't perform this operation on this endpoint.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

Video Poll Poll Options
=======================

Reading
-------

Options available for this poll

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bvideo-poll-id%7D%2Fpoll_options&version=v19.0)

    GET /v19.0/{video-poll-id}/poll_options HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{video-poll-id}/poll_options',
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
        "/{video-poll-id}/poll_options",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{video-poll-id}/poll_options",
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
                                   initWithGraphPath:@"/{video-poll-id}/poll_options"
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

A list of [VideoPollOption](https://developers.facebook.com/docs/graph-api/reference/video-poll-option/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

Creating
--------

You can't perform this operation on this endpoint.

Updating
--------

You can't perform this operation on this endpoint.

Deleting
--------

You can't perform this operation on this endpoint.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

Video Poll Option
=================

Reading
-------

Represents a single poll option that may be selected by the user

### Feature Permissions

| Name | Description |
| --- | --- |
| `Live Video API` | This is a required [feature permission](https://developers.facebook.com/docs/apps/review/feature/) |

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bvideo-poll-option-id%7D&version=v19.0)

    GET /v19.0/{video-poll-option-id} HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{video-poll-option-id}',
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
        "/{video-poll-option-id}",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{video-poll-option-id}",
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
                                   initWithGraphPath:@"/{video-poll-option-id}"
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
| `id`<br><br>numeric string | Poll option ID<br><br>[Core](https://developers.facebook.com/docs/apps/versions/#coreextended) |
| `is_correct`<br><br>bool | True if this answer is considered correct, otherwise false |
| `order`<br><br>int32 | Options appear in increasing numerical order within a poll |
| `text`<br><br>string | Text to display to the user for this option<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `total_votes`<br><br>int32 | Total number of votes for this option |

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

Creating
--------

You can't perform this operation on this endpoint.

Updating
--------

You can't perform this operation on this endpoint.

Deleting
--------

You can't perform this operation on this endpoint.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)