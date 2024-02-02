Graph API Reference v19.0: User Albums - Documentation - Meta for Developers

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
Graph API Versionv19.0User Albums
===========
Albums for a Facebook User.
Reading
-------
UserAlbums

### Permissions
* A user access token is required with the `user_photos` permission to view a person's albums.
This API can only be used to read albums of the person who created the access token. It can't be used to read the albums of friends or non-friends.
### Example
HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v19.0/{user-id}/albums HTTP/1.1
Host: graph.facebook.com
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{user-id}/albums',
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
    "/{user-id}/albums",
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
    "/{user-id}/albums",
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
                               initWithGraphPath:@"/{user-id}/albums"
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
A list of Album nodes.#### `paging`
For more details about pagination, see the Graph API guide.### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 459 | The session is invalid because the user has been checkpointed |
| 190 | Invalid OAuth 2.0 Access Token |
Creating
--------
You can't perform this operation on this endpoint.Updating
--------
You can't perform this operation on this endpoint.Deleting
--------
You can't perform this operation on this endpoint.