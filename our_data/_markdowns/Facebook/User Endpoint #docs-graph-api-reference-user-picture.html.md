Graph API Reference v19.0: User Picture - Documentation - Meta for Developers

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
Graph API Versionv19.0User Picture
============
A User's profile image.

Querying a User ID (UID) now requires an access token. Refer to the requirements table to determine which token type to include in UID-based requests.

Reading
-------

 Get the app user's profile image.
 ### Requirements

 Type | Requirement || Access Tokens | If querying an App-Scoped User ID:* None
If querying a User ID:* User or Page access token for Facebook Login authenticated requests
* App access token for server-side requests
* Client access token for mobile or web client-side requests
If querying a Page-Scoped User ID:* Page
 |
| Permissions | None |
### Notes

* Supports App-Scoped User IDs (ASID), User IDs (UID), and Page-Scoped User IDs (PSID).
* By default this edge will return a `302` redirect to the image. To get data about the image, include the `redirect=false` query string parameter.
* Profile picture URLs returned by this edge will expire.
* Tokenless requests on ASIDs made by apps that are inactive or that have not completed Data Use Checkup will receive an error code in response.

### Limitations

* Apps in Development mode that make tokenless requests on ASIDs will receive a silhouette image in response.
* Apps in Development mode that make requests with a Client token will receive a silhouette image in response.

### Example
HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v19.0/{user-id}/picture HTTP/1.1
Host: graph.facebook.com
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{user-id}/picture',
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
    "/{user-id}/picture",
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
    "/{user-id}/picture",
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
                               initWithGraphPath:@"/{user-id}/picture"
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
| `height`integer | The height of this picture in pixels.
 |
| `redirect`boolean | Default value: `true`By default the picture edge will return a picture instead of a JSON response. If you want the picture edge to return JSON that describes the image set `redirect=0` when you make the request.
 |
| `type`enum{small, normal, album, large, square} | The size of this picture. It can be one of the following values: small, normal, large, square.
 |
| `width`integer | The width of this picture in pixels.
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
A single ProfilePictureSource node.#### `paging`
For more details about pagination, see the Graph API guide.### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 190 | Invalid OAuth 2.0 Access Token |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 459 | The session is invalid because the user has been checkpointed |
Creating
--------
You can't perform this operation on this endpoint.Updating
--------
You can't perform this operation on this endpoint.Deleting
--------
You can't perform this operation on this endpoint.