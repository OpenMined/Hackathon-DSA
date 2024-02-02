Graph API Reference v19.0: Canvas - Documentation - Meta for Developers

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
Graph API Versionv19.0Canvas
======
Reading
-------
A canvas document

### Example
HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v19.0/{canvas-id} HTTP/1.1
Host: graph.facebook.com
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{canvas-id}',
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
    "/{canvas-id}",
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
    "/{canvas-id}",
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
                               initWithGraphPath:@"/{canvas-id}"
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
| `id`numeric string | ID of the canvas
 |
| `background_color`string | Background color of the canvas
 |
| `body_elements`list<CanvasPhoto|CanvasHeader|CanvasVideo|CanvasText|CanvasCarousel|CanvasButton|CanvasFooter|CanvasStoreLocator|CanvasProductList|CanvasProductSet> | Body element nodes for the canvas
 |
| `business_id`numeric string | The business id for the canvas product set element
 |
| `canvas_link`string | The canvas link for the canvas
 |
| `collection_hero_image`Photo | First element as photo inside canvas to use as hero media for canvas collection
 |
| `collection_hero_video`Video | First element as video inside canvas to use as hero media for canvas collection
 |
| `collection_thumbnails`list<CanvasCollectionThumbnail> | Canvas elements that can be used as thumbnails for canvas collections
 |
| `element_payload`string | Payload that contains all element
 |
| `elements`list<RichMediaElement> | Body element nodes for the canvas
 |
| `fb_body_elements`list<CanvasPhoto|CanvasHeader|CanvasVideo|CanvasText|CanvasCarousel|CanvasButton|CanvasFooter|CanvasStoreLocator|CanvasProductList|CanvasProductSet|CanvasDynamicProductSet|CanvasTemplateVideo|CanvasDynamicPhoto> | Body element nodes for the canvas, used by FB internal apps and includes elements who's API is not public yet
 |
| `is_hidden`bool | The canvas is hidden or not
 |
| `is_published`bool | Publish status of the canvas
 |
| `last_editor`User | User who last edited this canvas
 |
| `linked_documents`list<Canvas> | The canvas documents that are reachable via buttons/links in this document
 |
| `name`string | Name used to label the canvas
Default |
| `owner`Page | Page that owns this canvas
 |
| `property_list`list<string> | List of properties for this canvas
 |
| `store_url`string | The associated app store URL for the canvas
 |
| `style_list`list<enum> | Canvas level style attributes
 |
| `tags`list<string> | Tags associated with Canvas
 |
| `ui_property_list`list<string> | List of UI properties to set when viewing this canvas from creation tools
 |
| `unused_body_elements`list<CanvasPhoto|CanvasHeader|CanvasVideo|CanvasText|CanvasCarousel|CanvasButton|CanvasFooter|CanvasStoreLocator|CanvasProductList|CanvasProductSet> | Body element nodes that belong to the canvas but are not used
 |
| `update_time`int32 | Last updated time of the canvas
 |
| `use_retailer_item_ids`bool | HACK: Flag for whether or not the ad creative that uses this Canvas should use retailer\_item\_ids or not
 |
### Edges

| Edge | Description |
| --- | --- |
| `preview` | Get preview HTML embed element
 |
| `previews` | Get preview notifications for the canvas
 |
### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 80001 | There have been too many calls to this Page account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
Creating
--------
You can't perform this operation on this endpoint.Updating
--------
You can update a Canvas by making a POST request to `/{canvas_id}`.### Parameters

| Parameter | Description |
| --- | --- |
| `background_color`string | Background color of the canvas
 |
| `body_element_ids`list<numeric string or integer> | A list of canvas element ids
 |
| `enable_swipe_to_open`boolean | Field used to mark if swipe to open is enabled
 |
| `is_hidden`boolean | Field used to hide a (published) canvas
 |
| `is_published`boolean | Field used to mark the publish state of the canvas
 |
| `name`string | Field used to label the canvas
 |
| `source_template_id`numeric string or integer | ID of EntRichMediaDocumentTemplate that the Canvas document is created from
 |
### Return Type
This endpoint supports read-after-write and will read the node to which you POSTed. Struct {`success`: bool, }### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
Deleting
--------
You can't perform this operation on this endpoint.