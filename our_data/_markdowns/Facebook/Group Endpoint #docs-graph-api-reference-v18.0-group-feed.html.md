Feed - Graph API - Documentation - Meta for Developers

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
This document refers to an outdated version of Graph API. Please use the latest version.Graph API Versionv18.0Group Feed
==========
Posts owned by a Group, including status updates and links.

Reading
-------
Returns an array of Posts on the Group.
HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v19.0/{group-id}/feed HTTP/1.1
Host: graph.facebook.com
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{group-id}/feed',
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
    "/{group-id}/feed",
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
    "/{group-id}/feed",
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
                               initWithGraphPath:@"/{group-id}/feed"
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
| Tokens | A User access token or a Page access token. |
### Notes
* The `since` and `until` params apply on the `updated_time` field.
Publishing
----------
HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK
```
POST /v19.0/{group-id}/feed HTTP/1.1
Host: graph.facebook.com
message=This+is+a+test+message
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->post(
    '/{group-id}/feed',
    array (
      'message' => 'This is a test message',
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
/* make the API call */
FB.api(
    "/{group-id}/feed",
    "POST",
    {
        "message": "This is a test message"
    },
    function (response) {
      if (response && !response.error) {
        /* handle the result */
      }
    }
);
```
```
Bundle params = new Bundle();
params.putString("message", "This is a test message");
/* make the API call */
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "/{group-id}/feed",
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
  @"message": @"This is a test message",
};
/* make the API call */
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                               initWithGraphPath:@"/{group-id}/feed"
                                      parameters:params
                                      HTTPMethod:@"POST"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
### Requirements

 Type of Requirement | Description || App Review | Your app must be approved for the following login permissions and features: (Click to expand) |
| Login permissions | `publish_to_groups` |
| Features | Groups API |
| App Installation | The app must be installed on the Group. |
| Tokens | A User access token of a member of the Group. |
| Permissions | The user must grant your app the following permissions:`publish_to_groups` |
### Fields

 Name | Type | Description || `message` | `string` | The main body of the post, otherwise called the status message. Either `link` or `message` must be supplied. |
| `link` | `string` | The URL of a link to attach to the post. Either `link` or `message` must be supplied. Additional fields associated with `link` are shown below. |
### Response
If successful, you will receive a response with the following information. In addition, this endpoint supports read-after-write and can immediately return any fields returned by read operations.

Name
 | 
Description
 | 
Type
 || `id` | The newly created post ID | `string` |
Updating
--------
This operation is not supported.
Deleting
--------
This operation is not supported.