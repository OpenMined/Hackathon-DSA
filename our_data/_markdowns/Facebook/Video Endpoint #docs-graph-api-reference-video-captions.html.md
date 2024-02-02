Graph API, Video Captions - Documentation - Meta for Developers

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
Graph API Versionv19.0Video Captions
==============
Reading
-------
VideoCaptions

### Example
HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v19.0/{video-id}/captions HTTP/1.1
Host: graph.facebook.com
```
```
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
```
```
/* make the API call */
FB.api(
    "/{video-id}/captions",
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
    "/{video-id}/captions",
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
                               initWithGraphPath:@"/{video-id}/captions"
                                      parameters:params
                                      HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
If you want to learn how to use the Graph API, read our Using Graph API guide.### Parameters
This endpoint doesn't have any parameters.### Fields
Reading from this edge will return a JSON formatted result:

```
{
 "`data`": [],
 "`paging`": {}
}

```
#### `data`
A list of VideoCaption nodes.#### `paging`
For more details about pagination, see the Graph API guide.### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
Creating
--------
You can't perform this operation on this endpoint.Updating
--------
### Permissions
To update a video's caption, you need one of the following:
* User is the owner of the video
* User has manage access on page that owns the video
* User has advertiser access on account that owns the video
### Limitations
The file size limit for video captions is 200K.

You can update a Video by making a POST request to `/{video_id}/captions`.### Parameters

| Parameter | Description |
| --- | --- |
| `captions_file`file | Caption file in SRT (SubRip Text) format. File name must be in the format filename.locale.srt
 |
| `default_locale`string | Specify which locale should be used as the default for the video. Can be set to 'none'
 |
| `locales_to_delete`list<string> | Default value: `Vector`locales of caption to delete
 |
### Return Type
This endpoint supports read-after-write and will read the node to which you POSTed. Struct {`success`: bool, }### Error Codes

| Error | Description |
| --- | --- |
| 482 | The captions files you selected contain locales that had been applied to video, please remove and try again. |
| 387 | There was a problem uploading your captions file. Please try again. |
| 386 | You uploaded a .SRT file with an incorrect file name. Please use this format: filename.en\_US.srt |
| 100 | Invalid parameter |
| 385 | The captions file you selected is in a format that we don't support. |
Deleting
--------
You can't perform this operation on this endpoint.