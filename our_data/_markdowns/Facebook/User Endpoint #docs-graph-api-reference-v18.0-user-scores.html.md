/user/scores - Graph API - Documentation - Meta for Developers

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
This document refers to an outdated version of Graph API. Please use the latest version.Graph API Versionv18.0As of April 4, 2018, this endpoint only returns an empty data set. Please see the changelog for more information.

`/{user-id}``/scores`
=====================
The scores this person has received from Facebook Games that they've played.
Reading
-------
HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v19.0/me/scores HTTP/1.1
Host: graph.facebook.com
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/me/scores',
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
    "/me/scores",
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
    "/me/scores",
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
                               initWithGraphPath:@"/me/scores"
                                      parameters:params
                                      HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
### Permissions
* An app access token can be used to see the scores that a person has received in that app.
* A user access token with `user_games_activity` permission is required to see all scores that person has received from other apps.
### Fields

Name
 | 
Description
 | 
Type
 || `user` | The person associated with the scores. | `User` |
| `score` | The actual score. | `int` |
| `application` | The app in which the score was achieved. | `App`. |
Publishing
----------
HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK
```
POST /v19.0/me/scores HTTP/1.1
Host: graph.facebook.com
score=3444
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->post(
    '/me/scores',
    array (
      'score' => '3444',
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
    "/me/scores",
    "POST",
    {
        "score": "3444"
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
params.putString("score", "3444");
/* make the API call */
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "/me/scores",
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
  @"score": @"3444",
};
/* make the API call */
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                               initWithGraphPath:@"/me/scores"
                                      parameters:params
                                      HTTPMethod:@"POST"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
### Permissions
As of April 24,2018, the `pubish_actions` permission has been removed. Please see the Breaking Changes Changelog for more details. To provide a way for your app users to share content to Facebook, we encourage you to use our Sharing products instead.
The **Scores API** is available only for apps that are categorized as Games and have already been granted the `publish_actions` permission in the past.
Please note that `publish_actions` will not be granted for new apps with the sole purpose of accessing this API.
* A user access token with `publish_actions` permission can be used to publish scores for that person.
* An app access token can be used if `publish_actions` permission was previously granted.
### Fields

Name
 | 
Description
 | 
Type
 || `score` | The score that you want to set for this person. | `int` |
### Response
If successful:

```
{
  "success": true
}
```
Otherwise a relevant error message will be returned.
Deleting
--------
You can delete the score this person has received from your app only.
HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK
```
DELETE /v19.0/me/scores HTTP/1.1
Host: graph.facebook.com
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->delete(
    '/me/scores',
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
FB.api(
    "/me/scores",
    "DELETE",
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
    "/me/scores",
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
                               initWithGraphPath:@"/me/scores"
                                      parameters:params
                                      HTTPMethod:@"DELETE"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
### Permissions
As of April 24,2018, the `pubish_actions` permission has been removed. Please see the Breaking Changes Changelog for more details.
The **Scores API** is available only for apps that are categorized as Games and have already been granted the `publish_actions` permission in the past.
Please note that `publish_actions` will not be granted for new apps with the sole purpose of accessing these APIs.
* A user access token with `publish_actions` permission can be used to delete scores (from this app) for that person.
* An app access token can be used if `publish_actions` permission was previously granted.
### Fields
No fields are required to delete.
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
You can update a person's score for your app by publishing a new score.