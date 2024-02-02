Files - Graph API - Documentation - Meta for Developers

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
This document refers to an outdated version of Graph API. Please use the latest version.Graph API Versionv18.0Group Files
===========
The files uploaded to this group.
Reading
-------
HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v19.0/{group-id}/files HTTP/1.1
Host: graph.facebook.com
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{group-id}/files',
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
    "/{group-id}/files",
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
    "/{group-id}/files",
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
                               initWithGraphPath:@"/{group-id}/files"
                                      parameters:params
                                      HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
### Requirements

 Type of Requirement | Description || App Review | Your app must be approved for the Groups API feature. |
| App Installation | The app must be installed on the Group. |
| Tokens | A User access token. |
### Fields

Name
 | 
Description
 | 
Type
 || `download_link` | URL to download the file. | `string` |
| `group` | The Group the file is uploaded to (the same Group as in the request). | `Group` |
| `id` | The ID of the file. Note that you cannot request each file individually by its ID, only through this edge. | `string` |
| `message` | The text included with the file post. | `string` |
| `updated_time` | The last time the file was changed. | `datetime` |
Publishing
----------
This operation is not supported.
Deleting
--------
This operation is not supported.
Updating
--------
This operation is not supported.