Members - Graph API - Documentation - Meta for Developers

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
This document refers to an outdated version of Graph API. Please use the latest version.Graph API Versionv18.0This edge was deprecated on April 4th, 2018, and can no longer be used.

Members
=======
The members of a Group.
Reading
-------
HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v19.0/{group-id}/members HTTP/1.1
Host: graph.facebook.com
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{group-id}/members',
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
    "/{group-id}/members",
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
    "/{group-id}/members",
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
                               initWithGraphPath:@"/{group-id}/members"
                                      parameters:params
                                      HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
### Permissions
A User access token of an Admin of the Group with the following permissions:
* `user_managed_groups`
### Fields
A list of User objects and one additional field:

Name
 | 
Description
 | 
Type
 || `administrator` | Whether or not the person is a group admin. | `boolean` |
Creating
--------
This operation is not supported.
Updating
--------
This operation is not supported.
Deleting
--------
This operation is not supported.