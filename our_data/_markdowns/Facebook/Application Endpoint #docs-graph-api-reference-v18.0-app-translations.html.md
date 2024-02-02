Translations - Graph API - Documentation - Meta for Developers

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
This document refers to an outdated version of Graph API. Please use the latest version.Graph API Versionv18.0`/{app-id}``/translations`
==========================
The strings from this app that were translated using our translations tools.
Reading
-------
HTTPPHP SDKAndroid SDKiOS SDK
```
GET /v19.0/{app-id}/translations?locale=fr_FR HTTP/1.1
Host: graph.facebook.com
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{app-id}/translations?locale=fr_FR',
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
Bundle params = new Bundle();
params.putString("locale", "fr_FR");
/* make the API call */
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "/{app-id}/translations",
    params,
    HttpMethod.GET,
    new GraphRequest.Callback() {
        public void onCompleted(GraphResponse response) {
            /* handle the result */
        }
    }
).executeAsync();
```
```
NSDictionary *params = @{
  @"locale": @"fr_FR",
};
/* make the API call */
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                               initWithGraphPath:@"/{app-id}/translations"
                                      parameters:params
                                      HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
### Permissions
* An app access token is required to return translations for that app.
### Modifiers

Name
 | 
Description
 | 
Type
 || `locale` | Specifies which locale of language to request. This is a required parameter when reading this edge. | `enum{`locale`}` |
### Fields

Name
 | 
Description
 | 
Type
 || `id` | A unique ID for each individual string. | `string` |
| `translation` | The translated string. | `string` |
| `approval_status` | The approval status of the string. | `enum{auto-approved, approved, unapproved}` |
| `native_string` | The original string that was translated. | `string` |
| `description` | The provided description of the string. | `string` |
Publishing
----------
You can specify new strings to be translated for your app using this edge:
HTTPPHP SDKAndroid SDKiOS SDK
```
POST /v19.0/{app-id}/translations HTTP/1.1
Host: graph.facebook.com
native_strings=%5B%7B%22text%22%3A%22Test+String%22%2C+%22description%22%3A+%22This+is+a+test+string+for+an+app.%22%7D%5D
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->post(
    '/{app-id}/translations',
    array (
      'native_strings' => '[{"text":"Test String", "description": "This is a test string for an app."}]',
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
Bundle params = new Bundle();
params.putString("native_strings", "[{\"text\":\"Test String\", \"description\": \"This is a test string for an app.\"}]");
/* make the API call */
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "/{app-id}/translations",
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
  @"native_strings": @"[{\"text\":\"Test String\", \"description\": \"This is a test string for an app.\"}]",
};
/* make the API call */
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                               initWithGraphPath:@"/{app-id}/translations"
                                      parameters:params
                                      HTTPMethod:@"POST"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
### Permissions
* An app access token is required to add new translation strings for that app.
### Fields

Name
 | 
Description
 | 
Type
 || Vector | Vector | Vector |
#### Response
If successful, you will receive a plain response of the number of strings that were added, otherwise an error message.
Deleting
--------
You can delete translation strings using this operation:
HTTPPHP SDKAndroid SDKiOS SDK
```
DELETE /v19.0/{app-id}/translations HTTP/1.1
Host: graph.facebook.com
native_hashes=%5B%27hash1%27%2C+%27hash2%27%5D
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->delete(
    '/{app-id}/translations',
    array (
      'native_hashes' => '[\'hash1\', \'hash2\']',
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
Bundle params = new Bundle();
params.putString("native_hashes", "['hash1', 'hash2']");
/* make the API call */
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "/{app-id}/translations",
    params,
    HttpMethod.DELETE,
    new GraphRequest.Callback() {
        public void onCompleted(GraphResponse response) {
            /* handle the result */
        }
    }
).executeAsync();
```
```
NSDictionary *params = @{
  @"native_hashes": @"['hash1', 'hash2']",
};
/* make the API call */
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                               initWithGraphPath:@"/{app-id}/translations"
                                      parameters:params
                                      HTTPMethod:@"DELETE"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
### Permissions
* An app access token is required to delete translation strings from that app.
### Fields

Name
 | 
Description
 | 
Type
 || `native_hashes` | An array of hashes for each translation string. The hash is a unique identifier for each string, and can be retrieved using the `translation` FQL table. | `string[]` |
#### Response
If successful, you will receive a plain response of the number of strings that were deleted, otherwise an error message.