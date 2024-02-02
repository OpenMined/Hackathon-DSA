<div>

::: _xmu
``` {#u_0_a_4I ._5gt1 .prettyprint}
POST /v19.0/{test-user-id} HTTP/1.1
Host: graph.facebook.com

password=newpassword&name=Newname+Smith
```

``` {#u_0_b_8k ._5gt1 .prettyprint}
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->post(
    '/{test-user-id}',
    array (
      'password' => 'newpassword',
      'name' => 'Newname Smith',
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

``` {#u_0_c_Ac ._5gt1 .prettyprint}
Bundle params = new Bundle();
params.putString("password", "newpassword");
params.putString("name", "Newname Smith");
/* make the API call */
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "/{test-user-id}",
    params,
    HttpMethod.POST,
    new GraphRequest.Callback() {
        public void onCompleted(GraphResponse response) {
            /* handle the result */
        }
    }
).executeAsync();
```

``` {#u_0_d_jf ._5gt1 .prettyprint}
NSDictionary *params = @{
  @"password": @"newpassword",
  @"name": @"Newname Smith",
};
/* make the API call */
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                               initWithGraphPath:@"/{test-user-id}"
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
