Albums - Graph API - Documentation - Meta for Developers

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
This document refers to an outdated version of Graph API. Please use the latest version.Graph API Versionv18.0Group Albums
============
The photo albums created for a Group.
Reading
-------
Returns an array of Albums on the Group.

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v19.0/{group-id}/albums HTTP/1.1
Host: graph.facebook.com
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{group-id}/albums',
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
    "/{group-id}/albums",
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
    "/{group-id}/albums",
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
                               initWithGraphPath:@"/{group-id}/albums"
                                      parameters:params
                                      HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
### Requirements

 Requirement | Description || App Review | Your app must be approved for the Groups API feature. |
| App Installation | The app must be installed on the Group. |
| Tokens | A User access token. |
### Fields
When requesting the following Album fields through field expansion, only Users who granted your app the `groups_access_member_info` permission will be included: 
 * `from`
* `likes`
* `reaction`

Publishing
----------
HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK
```
POST /v19.0/{group-id}/albums HTTP/1.1
Host: graph.facebook.com
name=%7Balbum-name%7D&message=%7Balbum-description%7D&privacy=%7Bprivacy-settings%7D
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->post(
    '/{group-id}/albums',
    array (
      'name' => '{album-name}',
      'message' => '{album-description}',
      'privacy' => '{privacy-settings}',
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
    "/{group-id}/albums",
    "POST",
    {
        "name": "{album-name}",
        "message": "{album-description}",
        "privacy": "{privacy-settings}"
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
params.putString("name", "{album-name}");
params.putString("message", "{album-description}");
params.putString("privacy", "{privacy-settings}");
/* make the API call */
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "/{group-id}/albums",
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
  @"name": @"{album-name}",
  @"message": @"{album-description}",
  @"privacy": @"{privacy-settings}",
};
/* make the API call */
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                               initWithGraphPath:@"/{group-id}/albums"
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
| Tokens | A User access token for a user who is a member of the Group where the app is installed. |
| Permissions | The user must grant your app this permission:
`publish_to_groups` |
### Fields

Parameter
 | 
Description
 | 
Type
 || `name` | The name given to the album. This field is required. | `string` |
| `message` | The description of the album, which will show up in Feed as the status message. | `string` |
#### Response

Name
 | 
Description
 | 
Type
 || id | The ID of the newly created album. | `string` |
Deleting
--------
This operation is not supported.
Updating
--------
This operation is not supported.