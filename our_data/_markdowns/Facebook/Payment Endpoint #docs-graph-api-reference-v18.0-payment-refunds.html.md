Payment Refunds - Graph API - Documentation - Meta for Developers

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
This document refers to an outdated version of Graph API. Please use the latest version.Graph API Versionv18.0`/{payment-id}``/refunds`
=========================
Used to issue any payment refunds.
Reading
-------
You can't read this edge.
Publishing
----------
You can use this edge to initiate refunds:
HTTPPHP SDKAndroid SDKiOS SDK
```
POST /v19.0/{payment-id}/refunds HTTP/1.1
Host: graph.facebook.com
currency=EUR&amount=1.00
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->post(
    '/{payment-id}/refunds',
    array (
      'currency' => 'EUR',
      'amount' => '1.00',
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
params.putString("currency", "EUR");
params.putString("amount", "1.00");
/* make the API call */
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "/{payment-id}/refunds",
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
  @"currency": @"EUR",
  @"amount": @"1.00",
};
/* make the API call */
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                               initWithGraphPath:@"/{payment-id}/refunds"
                                      parameters:params
                                      HTTPMethod:@"POST"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
### Permissions
* An app access token is required to issue any refunds for that app.
### Fields

Name
 | 
Description
 | 
Type
 || `currency` | The three-letter ISO code of the currency in which the refund amount is specified; it must be the same as the currency in which the original purchase was denominated. This is required. | `string` |
| `amount` | The amount to refund. This is required. It must be less than or equal to the `refundable_amount` field on the parent Payment object. | `string` |
| `reason` | The reason you are refunding this order. | `enum{MALICIOUS_FRAUD, FRIENDLY_FRAUD, CUSTOMER_SERVICE}` |
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