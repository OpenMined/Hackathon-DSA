App Link Host - Graph API - Documentation - Meta for Developers

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
This document refers to an outdated version of Graph API. Please use the latest version.Graph API Versionv18.0App Link Host `/app-link-host`
==============================
An individual app link host object created by an app. An app link host is a wrapper for a group of different app links.
Please see our main App Links documentation to learn more.
Reading
-------
HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK
```
GET /v19.0/{app-link-host-id} HTTP/1.1
Host: graph.facebook.com
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{app-link-host-id}',
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
    "/{app-link-host-id}",
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
    "/{app-link-host-id}",
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
                               initWithGraphPath:@"/{app-link-host-id}"
                                      parameters:params
                                      HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
### Permissions
* Any valid access token is required.
### Response

Name
 | 
Description
 | 
Type
 || `name` | A custom name for this app link host. | `string` |
| `canonical_url` | The App Link URL. | `string` |
Publishing
----------
Apps can create app link hosts using the `/app/app_link_hosts` edge.
Deleting
--------
Facebook apps can delete app links using this edge:
HTTPPHP SDKAndroid SDKiOS SDK
```
DELETE /v19.0/{app-link-host-id} HTTP/1.1
Host: graph.facebook.com
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->delete(
    '/{app-link-host-id}',
    array (),
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
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "/{app-link-host-id}",
    null,
    HttpMethod.DELETE,
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
                               initWithGraphPath:@"/{app-link-host-id}"
                                      parameters:params
                                      HTTPMethod:@"DELETE"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
### Permissions
* An app access token is required to delete app link hosts belonging to that app.
### Response
Returns `true` successful, otherwise an error message.
Updating
--------
Facebook apps can update app links using this edge:
PHP SDKHTTPAndroid SDKiOS SDK
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->post(
    '/{app-link-host-id}',
    array (
      'name' => 'Updated Name',
      'android' => '[]',
      'web' => '{"should_fallback": true}',
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
```
```
POST /v19.0/{app-link-host-id} HTTP/1.1
Host: graph.facebook.com
name=Updated+Name&android=%5B%5D&web=%7B%22should_fallback%22%3A+true%7D
```
```
Bundle params = new Bundle();
params.putString("name", "Updated Name");
params.putString("android", "[]");
params.putString("web", "{\"should_fallback\": true}");
/* make the API call */
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "/{app-link-host-id}",
    params,
    HttpMethod.POST,
    new GraphRequest.Callback() {
        public void onCompleted(GraphResponse response) {
            /* handle the result */
        }
    }
).executeAsync();
```
```
NSDictionary *params = @{
  @"name": @"Updated Name",
  @"android": @"[]",
  @"web": @"{\"should_fallback\": true}",
};
/* make the API call */
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                               initWithGraphPath:@"/{app-link-host-id}"
                                      parameters:params
                                      HTTPMethod:@"POST"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
### Permissions
* An app access token is required to update app link hosts belonging to that app.
### Fields

Name
 | 
Description
 | 
Type
 || `name` | A custom name for this app link host. | `string` |
### Response
Returns `true` successful, otherwise an error message.