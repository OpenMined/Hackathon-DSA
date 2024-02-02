Graph API Reference v19.0: Canvas Button - Documentation - Meta for Developers

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
Graph API Versionv19.0Canvas Button
=============
Reading
-------
A button inside the canvas

### Example
PHP Business SDKcURL
```
use FacebookAds\Api;
use FacebookAds\Http\RequestInterface;
$params = array(
  'fields' => array(
    'action',
    'id',
    'name',
    'rich_text',
  ),
);
$data = Api::instance()->call(
  '/' . <CANVAS_BUTTON_ID>,
  RequestInterface::METHOD_GET,
  $params)->getContent();
```
```
curl -G \
  --data-urlencode 'fields=[ 
    "action", 
    "id", 
    "name", 
    "rich_text" 
  ]' \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v2.11/<CANVAS_BUTTON_ID>
```
### Parameters
This endpoint doesn't have any parameters.### Fields

| Field | Description |
| --- | --- |
| `id`numeric string | The id of the element
 |
| `action`CanvasOpenURLAction | The action associated with the button
 |
| `background_color`string | Color of the button background
 |
| `bottom_padding`numeric string | The padding below the element
 |
| `button_color`string | Color of the button
 |
| `button_style`enum | The style of the button
 |
| `deep_link`string | Deep link destination only for mobile apps
 (used for mobile install or engagement ads, and app link is supported)
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
| `rich_text`CanvasRichText | The text inside the button
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
| 80001 | There have been too many calls to this Page account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |
Creating
--------
You can't perform this operation on this endpoint.Updating
--------
You can't perform this operation on this endpoint.Deleting
--------
You can't perform this operation on this endpoint.