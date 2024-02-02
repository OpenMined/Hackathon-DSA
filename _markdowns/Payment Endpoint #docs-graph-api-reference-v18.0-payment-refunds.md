<div>

::: _xmu
``` {#u_0_a_7C ._5gt1 .prettyprint}
POST /v19.0/{payment-id}/refunds HTTP/1.1
Host: graph.facebook.com

currency=EUR&amount=1.00
```

``` {#u_0_b_sN ._5gt1 .prettyprint}
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

``` {#u_0_c_hF ._5gt1 .prettyprint}
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

``` {#u_0_d_p+ ._5gt1 .prettyprint}
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
:::

</div>
