Graph API Reference v19.0: Games IAPProduct - Documentation - Meta for Developers

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
Graph API Versionv19.0Games IAPProduct
================
Reading
-------
An in-app-purchaseable product

### Example
HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v19.0/{games-iap-product-id} HTTP/1.1
Host: graph.facebook.com
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{games-iap-product-id}',
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
    "/{games-iap-product-id}",
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
    "/{games-iap-product-id}",
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
                               initWithGraphPath:@"/{games-iap-product-id}"
                                      parameters:params
                                      HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
If you want to learn how to use the Graph API, read our Using Graph API guide.### Parameters
This endpoint doesn't have any parameters.### Fields

| Field | Description |
| --- | --- |
| `id`numeric string | The id of the object
 |
| `description`string | Description of the product (e.g. "Used as in-app currency")
Default |
| `image_uri`string | The associated image of the product for the Facebook Pay dialog
Default |
| `local_price_amount_cents`integer | Local price of the product in 1/100ths of the major unit of currency (e.g. 1 JPY -> 100, 1.23 USD -> 123)
Default |
| `local_price_formatted`string | Human-readable local price of the product (e.g. "$1.23")
Default |
| `price`string | Human-readable price of the product (e.g. "$1.23")
Default |
| `price_amount_cents`unsigned int32 | Price of the product in 1/100ths of the major unit of currency (e.g. 1 JPY -> 100, 1.23 USD -> 123)
Default |
| `price_currency_code`string | Currency code of price (e.g. "JPY", "USD")
Default |
| `product_id`string | Identifier for the product (e.g. "gold\_bar")
Default |
| `product_type`enum | Type of the product (e.g. managed)
Default |
| `subscription_term`enum | The subscription renewal length of time if ProductType is SUBSCRIPTION
Default |
| `title`string | Title of the product displayed to the user (e.g. "Gold Bar")
Default |
### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
Creating
--------
You can't perform this operation on this endpoint.Updating
--------
You can't perform this operation on this endpoint.Deleting
--------
You can't perform this operation on this endpoint.