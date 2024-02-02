Static Resources - Graph API - Documentation - Meta for Developers

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
This document refers to an outdated version of Graph API. Please use the latest version.Graph API Versionv18.0This endpoint is deprecated as of April 4, 2018. Please see the changelog for more information.

`/{app-id}``/staticresources`
=============================
Usage statistics for any static resources used by a Facebook Canvas app.
Reading
-------
HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v19.0/{app-id}/staticresources HTTP/1.1
Host: graph.facebook.com
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{app-id}/staticresources',
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
    "/{app-id}/staticresources",
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
    "/{app-id}/staticresources",
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
                               initWithGraphPath:@"/{app-id}/staticresources"
                                      parameters:params
                                      HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
### Permissions
* A user access token for an admin of the app.
### Fields

Name
 | 
Description
 | 
Type
 || `usage_stats` | Static resource URLs with the fractions of page loads that used each resource. | `array` |
| `prefetched_resources` | Static resource URLs that are currently being flushed early for users who are using the app. | `array` |
| `https` | An object containing `usage_stats` and `prefetched_resources` again, only showing resources accessed via HTTPS. | `object` |
Publishing
----------
You can't publish using this edge.
Deleting
--------
You can't delete using this edge.
Related Topics
--------------
* Resource Prefetching via Facebook SDK for JavaScript