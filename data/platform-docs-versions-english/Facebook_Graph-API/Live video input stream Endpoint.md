Live Video Input Stream
=======================

Represents a live video broadcast ingest stream.

Reading
-------

An ingest stream for a live video

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Blive-video-input-stream-id%7D&version=v19.0)

    GET /v19.0/{live-video-input-stream-id} HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{live-video-input-stream-id}',
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
        "/{live-video-input-stream-id}",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{live-video-input-stream-id}",
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
                                   initWithGraphPath:@"/{live-video-input-stream-id}"
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
| `id`<br><br>numeric string | The ID of the input stream |
| `dash_ingest_url`<br><br>string | The dash ingest stream URL of this stream<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `dash_preview_url`<br><br>string | Preview URL for input to use with dash player<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `is_master`<br><br>bool | Set to true if this is input is being served to viewers<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `secure_stream_url`<br><br>string | The RTMPS URL for this stream<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `stream_health`<br><br>LiveVideoStreamHealth | Parameters indicating the input stream health<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `stream_id`<br><br>numeric string | 0-indexed ID for this ingest stream<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `stream_url`<br><br>string | The ingest RTMP URL for this stream<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

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

Updating
--------

You can't perform this operation on this endpoint.

Deleting
--------

You can't perform this operation on this endpoint.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)