Graph API Reference v19.0: Canvas Product Set - Documentation - Meta for Developers

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
Graph API Versionv19.0Canvas Product Set
==================
Reading
-------
A product set inside the canvas

Starting September 14, 2021, the following fields will throw an error for version 12.0+ calls made by apps that lack the endpoint's required permissions. This change will apply to all versions on December 13, 2021.

* `storefront_settings`
### Example
PHP Business SDKcURL
```
use FacebookAds\Api;
use FacebookAds\Http\RequestInterface;
$params = array(
  'fields' => array(
    'id',
    'name',
    'product_set_id',
  ),
);
$data = Api::instance()->call(
  '/' . <CANVAS_PRODUCT_SET_ID>,
  RequestInterface::METHOD_GET,
  $params)->getContent();
```
```
curl -G \
  --data-urlencode 'fields=[ 
    "id", 
    "name", 
    "product_set_id" 
  ]' \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v2.11/<CANVAS_PRODUCT_SET_ID>
```
### Parameters
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
| `image_overlay_spec`AdCreativeLinkDataImageOverlaySpec | How to render overlays over a product item
 |
| `item_description`string | A token to represent which field from the product to show in the product description
 |
| `item_headline`string | A token to represent which field from the product to show in the product headline
 |
| `max_products`unsigned int32 | Maximum number of products to show
 |
| `name`string | The name of the element
Default |
| `product_set_id`numeric string | The product set id which contains a subset of products within a product catalog
 |
| `retailer_item_ids`list<string> | An array of items that should be shown first in the product set element. If this is not set then products will be dynamically chosen
 |
| `show_in_feed`bool | A flag that products should be shown in feed unit
 |
| `top_padding`numeric string | The padding above the element
 |
### Error Codes

| Error | Description |
| --- | --- |
| 80001 | There have been too many calls to this Page account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |
| 100 | Invalid parameter |
Creating
--------
You can't perform this operation on this endpoint.Updating
--------
You can't perform this operation on this endpoint.Deleting
--------
You can't perform this operation on this endpoint.### Create a Collection Ads Product Set
To create a product set used in Collection ads from a set of products in Dynamic Ads:

`curl
 -F 'canvas_product_set={ 
 "bottom_padding": 8, 
 "max_items": 50, 
 "name": "Collection Product Set Name", 
 "product_set_id": "PRODUCT_SET_ID",
 "show_in_feed": true,
 "item_headline": "See more at {{product.brand | titleize}}",
 "item_description": "{{product.price}}",
 "retailer_item_ids": [
 "RETAILER_ID_1", 
 "RETAILER_ID_2", 
 "RETAILER_ID_3", 
 "RETAILER_ID_4",
 ], 
 "top_padding": 24 
 }' \
 -F 'access_token=ACCESS_TOKEN' \
 https://graph.facebook.com/VERSION/PAGE_ID/canvas_elements`