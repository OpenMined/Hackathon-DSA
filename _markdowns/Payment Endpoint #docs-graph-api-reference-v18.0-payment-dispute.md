
Payment Dispute - Graph API - Documentation - Meta for Developers












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
This document refers to an outdated version of Graph API. Please use the latest version.Graph API Versionv18.0`/{payment-id}``/dispute`
=========================

Used to settle any payment disputes.

Reading
-------

You can't read this edge, use the `disputes` field on the parent Payment object.

Publishing
----------

You can use this edge to settle disputes:

HTTPPHP SDKAndroid SDKiOS SDK
```
POST /v19.0/{payment-id}/dispute HTTP/1.1
Host: graph.facebook.com

reason=DENIED_REFUND
```

```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->post(
    '/{payment-id}/dispute',
    array (
      'reason' => 'DENIED_REFUND',
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
params.putString("reason", "DENIED_REFUND");
/* make the API call */
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "/{payment-id}/dispute",
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
  @"reason": @"DENIED_REFUND",
};
/* make the API call */
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                               initWithGraphPath:@"/{payment-id}/dispute"
                                      parameters:params
                                      HTTPMethod:@"POST"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
### Permissions

* An app access token is required to settle any disputes for that app.
* If the payment has not been disputed yet, the call will return an error.

### Fields



 
Name
 | 
Description
 | 
Type
 || `reason` | The reason you are settling this dispute. This is required. | `enum{GRANTED_REPLACEMENT_ITEM, DENIED_REFUND, BANNED_USER}` |

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

You can't delete using this edge.




































 
