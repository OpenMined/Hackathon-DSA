Graph API Reference v19.0: Canvas Text - Documentation - Meta for Developers

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
Graph API Versionv19.0Canvas Text
===========
Reading
-------
Text element of the canvas

### Example
PHP Business SDKcURL
```
use FacebookAds\Api;
use FacebookAds\Http\RequestInterface;
$params = array(
  'fields' => array(
    'id',
    'name',
    'rich_text',
  ),
);
$data = Api::instance()->call(
  '/' . <CANVAS_TEXT_ID>,
  RequestInterface::METHOD_GET,
  $params)->getContent();
```
```
curl -G \
  --data-urlencode 'fields=[ 
    "id", 
    "name", 
    "rich_text" 
  ]' \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v2.11/<CANVAS_TEXT_ID>
```
### Parameters
This endpoint doesn't have any parameters.### Fields

| Field | Description |
| --- | --- |
| `id`numeric string | The id of the element
 |
| `background_color`string | The color of the background for the element
 |
| `bottom_padding`numeric string | The padding below the element
 |
| `element_group_key`string | The element group key to bundle multiple elements in editing
 |
| `element_type`enum | The type of the element
Default |
| `font_family`string | The font family
 |
| `font_size`numeric string | The size of the font for the text
 |
| `line_height`numeric string | The line height of the text
 |
| `name`string | The name of the element
Default |
| `rich_text`CanvasRichText | The text content of the element
 |
| `text_alignment`enum | The alignment of the text
 |
| `text_color`string | The color of the text
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
You can't perform this operation on this endpoint.Deleting
--------
You can delete a CanvasText by making a DELETE request to `/{canvas_text_id}`.### Parameters
This endpoint doesn't have any parameters.### Return Type
 Struct {`success`: bool, }### Error Codes

| Error | Description |
| --- | --- |
| 210 | User not visible |