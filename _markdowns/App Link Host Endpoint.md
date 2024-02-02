<div>

::: _xmu
``` {#u_0_v_D6 ._5gt1 .prettyprint}
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->post(
    '/{app-link-host-id}',
    array (
      'name' => 'Updated Name',
      'android' => '[]',
      'web' => '{"should_fallback": true}',
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

``` {#u_0_w_ju ._5gt1 .prettyprint}
POST /v19.0/{app-link-host-id} HTTP/1.1
Host: graph.facebook.com

name=Updated+Name&android=%5B%5D&web=%7B%22should_fallback%22%3A+true%7D
```

``` {#u_0_x_ZM ._5gt1 .prettyprint}
Bundle params = new Bundle();
params.putString("name", "Updated Name");
params.putString("android", "[]");
params.putString("web", "{\"should_fallback\": true}");
/* make the API call */
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "/{app-link-host-id}",
    params,
    HttpMethod.POST,
    new GraphRequest.Callback() {
        public void onCompleted(GraphResponse response) {
            /* handle the result */
        }
    }
).executeAsync();
```

``` {#u_0_y_NQ ._5gt1 .prettyprint}
NSDictionary *params = @{
  @"name": @"Updated Name",
  @"android": @"[]",
  @"web": @"{\"should_fallback\": true}",
};
/* make the API call */
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                               initWithGraphPath:@"/{app-link-host-id}"
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
