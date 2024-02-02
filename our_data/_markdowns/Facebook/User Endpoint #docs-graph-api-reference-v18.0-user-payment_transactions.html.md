/user/payment\_transactions - Graph API - Documentation - Meta for Developers

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
This document refers to an outdated version of Graph API. Please use the latest version.Graph API Versionv18.0`/{user-id}``/payment_transactions`
===================================
The Facebook Payments orders this person placed with an app.
Reading
-------
HTTPPHP SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v19.0/me/payment_transactions HTTP/1.1
Host: graph.facebook.com
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/me/payment_transactions',
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
    "/me/payment_transactions",
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
                               initWithGraphPath:@"/me/payment_transactions"
                                      parameters:params
                                      HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
### Permissions
* An app access token is required to view any transactions made using that app.
### Fields
An array of Payment objects.
Publishing
----------
You can't publish using this edge. Please see the Payments docs for details on how to integrate this into your ap.
Deleting
--------
You can't delete using this edge.
Updating
--------
You can't update using this edge.