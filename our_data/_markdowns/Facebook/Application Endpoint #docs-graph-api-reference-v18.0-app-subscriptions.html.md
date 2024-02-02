Subscriptions - Graph API - Documentation - Meta for Developers

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
This document refers to an outdated version of Graph API. Please use the latest version.Graph API Versionv18.0`/{app-id}``/subscriptions`
===========================
This edge allows you to configure webhooks subscriptions on an app.

Reading
-------
HTTPPHP SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v19.0/{app-id}/subscriptions HTTP/1.1
Host: graph.facebook.com
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{app-id}/subscriptions',
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
    "/{app-id}/subscriptions",
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
                               initWithGraphPath:@"/{app-id}/subscriptions"
                                      parameters:params
                                      HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
### Permissions
* An app access token is required to return subscriptions for that app.
### Fields

Name
 | 
Description
 | 
Type
 || `object` | Indicates the object type that this subscription applies to. | `enum{user, page, permissions, payments}` |
| `callback_url` | The URL that will receive the `POST` request when an update is triggered. | `string` |
| `fields` | The set of fields in this `object` that are subscribed to. | `string[]` |
| `active` | Indicates whether or not the subscription is active. | `bool` |
Creating
--------

You can create new Webhooks subscriptions using this edge:

HTTPPHP SDKAndroid SDKiOS SDK
```
POST /v19.0/{app-id}/subscriptions HTTP/1.1
Host: graph.facebook.com
object=page&callback_url=http%3A%2F%2Fexample.com%2Fcallback%2F&fields=about%2C+picture&include_values=true&verify_token=thisisaverifystring
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->post(
    '/{app-id}/subscriptions',
    array (
      'object' => 'page',
      'callback_url' => 'http://example.com/callback/',
      'fields' => 'about, picture',
      'include_values' => 'true',
      'verify_token' => 'thisisaverifystring',
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
params.putString("object", "page");
params.putString("callback_url", "http://example.com/callback/");
params.putString("fields", "about, picture");
params.putString("include_values", "true");
params.putString("verify_token", "thisisaverifystring");
/* make the API call */
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "/{app-id}/subscriptions",
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
  @"object": @"page",
  @"callback_url": @"http://example.com/callback/",
  @"fields": @"about, picture",
  @"include_values": @"true",
  @"verify_token": @"thisisaverifystring",
};
/* make the API call */
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                               initWithGraphPath:@"/{app-id}/subscriptions"
                                      parameters:params
                                      HTTPMethod:@"POST"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
Making a POST request with the `callback_url`, `verify_token`, and `object` fields will reactivate the subscription.
### Limitations

* Webhooks for Instagram is not supported. Instagram webhooks must be configured using the App Dashboard.
* Webhooks for WhatsApp is not supported. WhatsApp webhooks must be configured using the App Dashboard.

### Permissions
* An app access token is required to add new subscriptions for that app.
* Subscriptions for the object type `user` will only be valid for users who have installed the app.
* Subscriptions for the object type `page` will only be valid for Pages that have installed the app. You can install the app for a Page using the /{page-id}/subscribed\_apps edge.
* The app used to subscribe should be set up to receive Webhooks updates.
### Fields

Name
 | 
Description
 | 
Type
 || `object` | Indicates the object type that this subscription applies to. | `enum{user, page, permissions, payments}` |
| `callback_url` | The URL that will receive the `POST` request when an update is triggered, and a `GET` request when attempting this publish operation. See our guide to constructing a callback URL page. | `string` |
| `fields` | One or more of the set of valid fields in this `object` to subscribe to. | `string[]` |
| `include_values` | Indicates if change notifications should include the new values. | `bool` |
| `verify_token` | An arbitrary string that can be used to confirm to your server that the request is valid. | `string` |
### Response
If your callback URL is valid and the subscription is successful:

```
{
  "success": true
}
```
Otherwise a relevant error message will be returned.
Deleting
--------
You can delete all or per-object subscriptions using this operation:
HTTPPHP SDKAndroid SDKiOS SDK
```
DELETE /v19.0/{app-id}/subscriptions HTTP/1.1
Host: graph.facebook.com
object=page
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->delete(
    '/{app-id}/subscriptions',
    array (
      'object' => 'page',
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
params.putString("object", "page");
/* make the API call */
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "/{app-id}/subscriptions",
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
  @"object": @"page",
};
/* make the API call */
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                               initWithGraphPath:@"/{app-id}/subscriptions"
                                      parameters:params
                                      HTTPMethod:@"DELETE"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
You can delete specific fields from your subscription by including a `fields` param.
### Permissions
* An app access token is required to delete subscriptions for that app.
### Fields

Name
 | 
Description
 | 
Type
 || `object` | A specific object type to remove subscriptions for. If this optional field is not included, all subscriptions for this app will be removed. | `enum{user, page, permissions, payments}` |
| `fields` | One or more of the set of valid fields in this `object` to subscribe to. | `string[]` |
### Response
If successful:

```
{
  "success": true
}
```
Otherwise a relevant error message will be returned.
Updating
--------
You can perform updates on this edge by performing a publish operation with new values. This will amend the susbcription for the given topic without overwriting existing fields.