Graph API Reference v19.0: Video Comments - Documentation - Meta for Developers

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
Graph API Versionv19.0Video Comments
==============
Reading
-------
Comments for this object

### New Page Experience
This endpoint is supported for New Page Experience.### Example
HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v19.0/{video-id}/comments HTTP/1.1
Host: graph.facebook.com
```
```
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
```
```
/* make the API call */
FB.api(
    "/{video-id}/comments",
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
    "/{video-id}/comments",
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
                               initWithGraphPath:@"/{video-id}/comments"
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
| `filter`enum{stream, toplevel} | Default value: `toplevel`SELF\_EXPLANATORY
 |
| `live_filter`enum{filter\_low\_quality, no\_filter} | Default value: `filter_low_quality`For comments on a Live streaming video, this determines whether low quality comments will be filtered out of the results (filtering is enabled by default). In all other circumstances this parameter is ignored.
 |
| `order`enum{chronological, reverse\_chronological} | Preferred ordering of the comments. Accepts chronological (oldest first) and reverse chronological (newest first). If the comments can be ranked, then the order will always be ranked regardless of this modifier. The best practice for querying comments on a Live video is to continually poll for comments in the reversechronological ordering mode.
 |
| `since`datetime | Lower bound of the time range to consider
 |
### Fields
Reading from this edge will return a JSON formatted result:

```
{
 "`data`": [],
 "`paging`": {},
 "`summary`": {}
}

```
#### `data`
A list of Comment nodes.#### `paging`
For more details about pagination, see the Graph API guide.#### `summary`
Aggregated information about the edge, such as counts. Specify the fields to fetch in the summary param (like `summary=order`).

| Field | Description |
| --- | --- |
| `order`enum | Order of returned comments
 |
| `total_count`unsigned int32 | Total number of people who commented
 |
| `can_comment`bool | Can the viewer comment
 |
### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 80001 | There have been too many calls to this Page account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 190 | Invalid OAuth 2.0 Access Token |
Creating
--------
You can make a POST request to `comments` edge from the following paths: * `/{video_id}/comments`
When posting to this edge, a Comment will be created.### Parameters

| Parameter | Description |
| --- | --- |
| `attachment_id`numeric string or integer | ID for a photo attachment to associate with this
 |
| `attachment_share_url`URL | Link to set the comment attachment to. Does not include the url in the message
 |
| `attachment_url`URL | Link to set the comment attachment to
 |
| `is_offline`boolean | Whether the comment was originally made while offline
 |
| `message`UTF-8 string | Same as the text param
Supports Emoji |
| `text`UTF-8 string | The text of the comment that allows emoji
Supports Emoji |
### Return Type
This endpoint supports read-after-write and will read the node represented by `id` in the return type. Struct {`id`: token with structure: Comment ID, }### Error Codes

| Error | Description |
| --- | --- |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 190 | Invalid OAuth 2.0 Access Token |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 1705 | There was an error during posting. |
| 459 | The session is invalid because the user has been checkpointed |
Updating
--------
You can't perform this operation on this endpoint.Deleting
--------
You can't perform this operation on this endpoint.