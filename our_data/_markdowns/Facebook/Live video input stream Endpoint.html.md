Graph API Reference v19.0: Live Video Input Stream - Documentation - Meta for Developers

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
Graph API Versionv19.0Live Video Input Stream
=======================
Represents a live video broadcast ingest stream.

Reading
-------
An ingest stream for a live video

### Example
HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v19.0/{live-video-input-stream-id} HTTP/1.1
Host: graph.facebook.com
```
```
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
```
```
/* make the API call */
FB.api(
    "/{live-video-input-stream-id}",
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
    "/{live-video-input-stream-id}",
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
                               initWithGraphPath:@"/{live-video-input-stream-id}"
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
| `target_token`string | A target token recently returned by the speed test API
 |
### Fields

| Field | Description |
| --- | --- |
| `id`numeric string | The ID of the input stream
 |
| `dash_ingest_url`string | The dash ingest stream URL of this stream
Default |
| `dash_preview_url`string | Preview URL for input to use with dash player
Default |
| `is_master`bool | Set to true if this is input is being served to viewers
Default |
| `secure_stream_url`string | The RTMPS URL for this stream
Default |
| `stream_health`LiveVideoStreamHealth | Parameters indicating the input stream health
Default |
| `stream_id`numeric string | 0-indexed ID for this ingest stream
Default |
| `stream_url`string | The ingest RTMP URL for this stream
Default |
### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
Creating
--------
You can make a POST request to `input_streams` edge from the following paths: * `/{live_video_id}/input_streams`
When posting to this edge, a LiveVideoInputStream will be created.### Parameters
This endpoint doesn't have any parameters.### Return Type
This endpoint supports read-after-write and will read the node represented by `id` in the return type. Struct {`id`: numeric string, }### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
Updating
--------
You can't perform this operation on this endpoint.Deleting
--------
You can't perform this operation on this endpoint.