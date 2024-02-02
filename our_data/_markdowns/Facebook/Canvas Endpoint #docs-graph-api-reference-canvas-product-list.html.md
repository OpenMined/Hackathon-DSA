Graph API Reference v19.0: Canvas Product List - Documentation - Meta for Developers

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
Graph API Versionv19.0Canvas Product List
===================
**Only E-commerce and travel hotel vertical catalogs are currently supported.**Reading
-------
A product list inside the canvas

Select a product catalog and then manually provide the product ID, name and color variations to promote in a collection's ad creative. Use this option if you or your advertiser does not want to set-up a product set from a catalog feed. This option makes creating of ads from product catalog simpler. **Note that we do not save selected products as a product set for later reuse.**
Use this option to select which item colors you want to show in an ad and control the order products appear. **Because this is a manual ordering, we do not dynamically rank or display products based on popularity or relevancy to each viewer.**
### Example
HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v19.0/{canvas-product-list-id} HTTP/1.1
Host: graph.facebook.com
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{canvas-product-list-id}',
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
    "/{canvas-product-list-id}",
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
    "/{canvas-product-list-id}",
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
                               initWithGraphPath:@"/{canvas-product-list-id}"
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
| `id`numeric string | The id of the element
 |
| `bottom_padding`numeric string | The padding below the element
 |
| `element_group_key`string | The element group key to bundle multiple elements in editing
 |
| `element_type`enum | The type of the element
Default |
| `item_description`string | A token to represent which field from the product to show in the product description
 |
| `item_headline`string | A token to represent which field from the product to show in the product headline
 |
| `name`string | The name of the element
Default |
| `product_id_list`list<integer> | A list of product ids inside the canvas
 |
| `top_padding`numeric string | The padding above the element
 |
### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
Creating
--------
You can't perform this operation on this endpoint.Updating
--------
Provide a list of products for the element. This must include more than four IDs. IDs must be from Dynamic Ads product catalog or Dynamic Ads for Travel, hotel catalog.
`curl \
 -F 'bottom_padding=8' \
 -F 'name=Product List Name' \
 -F 'product_id_list=[product_id_1, product_id_2, product_id_3, product_id_4]' \
 -F 'item_headline=See more at {{product.url}}' \
 -F 'item_description={{product.current_price}}' \
 -F 'top_padding=24' \
 -F 'access_token=TOKEN' \
 https://graph.facebook.com/VERSION/CANVAS_ELEMENT_PRODUCT_LIST_ID`   
You can update a CanvasProductList by making a POST request to `/{canvas_product_list_id}`.### Parameters

| Parameter | Description |
| --- | --- |
| `bottom_padding`float | The padding below the product list
 |
| `item_description`string | A token to represent which field from the product to show in the product description
 |
| `item_headline`string | A token to represent which field from the product to show in the product headline
 |
| `name`string | Name of the product list element
 |
| `product_id_list`list<int64> | A list of product ids inside the canvas
Required |
| `top_padding`float | The padding above the product list
 |
### Return Type
This endpoint supports read-after-write and will read the node to which you POSTed. Struct {`success`: bool, }### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
Deleting
--------
You can delete a CanvasProductList by making a DELETE request to `/{canvas_product_list_id}`.### Parameters
This endpoint doesn't have any parameters.### Return Type
 Struct {`success`: bool, }