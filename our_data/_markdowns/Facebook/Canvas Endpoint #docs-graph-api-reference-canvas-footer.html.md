Graph API Reference v19.0: Canvas Footer - Documentation - Meta for Developers

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
Graph API Versionv19.0Canvas Footer
=============
Reading
-------
A footer of the canvas

### Example
PHP Business SDKcURL
```
use FacebookAds\Api;
use FacebookAds\Http\RequestInterface;
$params = array(
  'fields' => array(
    'child_elements',
    'id',
    'name',
  ),
);
$data = Api::instance()->call(
  '/' . <CANVAS_FOOTER_ID>,
  RequestInterface::METHOD_GET,
  $params)->getContent();
```
```
curl -G \
  --data-urlencode 'fields=[ 
    "child_elements", 
    "id", 
    "name" 
  ]' \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v2.11/<CANVAS_FOOTER_ID>
```
### Parameters
This endpoint doesn't have any parameters.### Fields

| Field | Description |
| --- | --- |
| `id`numeric string | The id of the element
 |
| `background_color`string | Background color of the button
 |
| `bottom_padding`numeric string | The padding below the element
 |
| `child_elements`list<CanvasButton> | The child elements inside a footer
 |
| `element_group_key`string | The element group key to bundle multiple elements in editing
 |
| `element_type`enum | The type of the element
Default |
| `name`string | The name of the element
Default |
| `top_padding`numeric string | The padding above the element
 |
### Error Codes

| Error | Description |
| --- | --- |
| 80001 | There have been too many calls to this Page account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |
Creating
--------
You can't perform this operation on this endpoint.Updating
--------
You can't perform this operation on this endpoint.Deleting
--------
You can delete a CanvasFooter by making a DELETE request to `/{canvas_footer_id}`.### Parameters
This endpoint doesn't have any parameters.### Return Type
 Struct {`success`: bool, }### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |