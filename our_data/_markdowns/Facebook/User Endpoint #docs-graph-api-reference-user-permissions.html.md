Graph API User, Permissions - Documentation - Meta for Developers

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
Graph API Versionv19.0User permissions
Returns a list of granted and declined permissions.

---
### Revoking Permissions
Apps can let people revoke permissions that were previously granted. For example, your app could have a settings page that lets someone disable publishing to Facebook. That settings page could also revoke the `publish_actions` permission at the same time.
You can revoke a specific permission by making a call to a Graph API endpoint:

```
DELETE /{user-id}/permissions/{permission-name}
```
This request must be made with a user access token or an app access token for the current app. If the request is successful, you will receive a response of `true`.
Reading
-------
### Example
HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v19.0/{user-id}/permissions HTTP/1.1
Host: graph.facebook.com
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{user-id}/permissions',
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
    "/{user-id}/permissions",
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
    "/{user-id}/permissions",
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
                               initWithGraphPath:@"/{user-id}/permissions"
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
| `permission`string | Permission name
 |
| `status`enum{granted, declined, expired} | Permission status
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
A list of Permission nodes.#### `paging`
For more details about pagination, see the Graph API guide.### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |
| 459 | The session is invalid because the user has been checkpointed |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 190 | Invalid OAuth 2.0 Access Token |
Creating
--------
You can't perform this operation on this endpoint.Updating
--------
You can't perform this operation on this endpoint.Deleting
--------
You can dissociate a Permission from a User by making a DELETE request to `/{user_id}/permissions`.### Parameters

| Parameter | Description |
| --- | --- |
| `permission`string | permission which wanted to be remove
 |
### Return Type
 Struct {`success`: bool, }### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 240 | Desktop applications cannot call this function for other users |