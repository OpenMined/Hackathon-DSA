User Posts - Graph API - Documentation - Meta for Developers

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
This document refers to an outdated version of Graph API. Please use the latest version.Graph API Versionv18.0User Posts
==========

Represents a collection of Posts on a User.

Reading
-------

Get a list of Posts on a User.

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v19.0/{user-id}/posts HTTP/1.1
Host: graph.facebook.com
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{user-id}/posts',
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
    "/{user-id}/posts",
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
    "/{user-id}/posts",
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
                               initWithGraphPath:@"/{user-id}/posts"
                                      parameters:params
                                      HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
### Limitations

This endpoint will only returns Posts created on the app user's Timeline and Posts in which the app user has been tagged.

### Requirements

 Type of Requirement | Description || Access Tokens | User |
| Permissions | `user_posts` |
### Query String Parameters

 Name
  | 
 Description
  || `include_hidden`
boolean | Set to `true` to have results include hidden Posts. |
| `show_expired`
boolean | Set to `true` to have results include expired Posts. |
| `with`
enum {LOCATION} | Only return Posts that have set a location. |
### Response

Reading from this edge will return a JSON formatted result:

```
{
    "data": [],
    "paging": {}
}
```
`data`  
A list of Post nodes.

`paging`  
For more details about pagination, see the Graph API guide.

Creating
--------

This operation is not supported.

Updating
--------

This operation is not supported.

Deleting
--------

This operation is not supported.