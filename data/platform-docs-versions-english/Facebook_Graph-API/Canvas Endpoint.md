Canvas
======

[](#)

Reading
-------

A canvas document

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bcanvas-id%7D&version=v18.0)

    GET /v18.0/{canvas-id} HTTP/1.1
    Host: graph.facebook.com

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

    /* make the API call */
    FB.api(
        "/{canvas-id}",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

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

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

This endpoint doesn't have any parameters.

### Fields

| Field | Description |
| --- | --- |
| `id`<br><br>numeric string | ID of the canvas |
| `background_color`<br><br>string | Background color of the canvas |
| `body_elements`[](#)<br><br>list<CanvasPhoto\|CanvasHeader\|CanvasVideo\|CanvasText\|CanvasCarousel\|CanvasButton\|CanvasFooter\|CanvasStoreLocator\|CanvasProductList\|CanvasProductSet> | Body element nodes for the canvas |
| `business_id`<br><br>numeric string | The business id for the canvas product set element |
| `canvas_link`<br><br>string | The canvas link for the canvas |
| `collection_hero_image`<br><br>[Photo](https://developers.facebook.com/docs/graph-api/reference/photo/) | First element as photo inside canvas to use as hero media for canvas collection |
| `collection_hero_video`<br><br>[Video](https://developers.facebook.com/docs/graph-api/reference/video/) | First element as video inside canvas to use as hero media for canvas collection |
| `collection_thumbnails`<br><br>list<CanvasCollectionThumbnail> | Canvas elements that can be used as thumbnails for canvas collections |
| `element_payload`<br><br>string | Payload that contains all element |
| `elements`<br><br>list<RichMediaElement> | Body element nodes for the canvas |
| `fb_body_elements`<br><br>list<CanvasPhoto\|CanvasHeader\|CanvasVideo\|CanvasText\|CanvasCarousel\|CanvasButton\|CanvasFooter\|CanvasStoreLocator\|CanvasProductList\|CanvasProductSet\|CanvasDynamicProductSet\|CanvasTemplateVideo\|CanvasDynamicPhoto> | Body element nodes for the canvas, used by FB internal apps and includes elements who's API is not public yet |
| `is_hidden`<br><br>bool | The canvas is hidden or not |
| `is_published`<br><br>bool | Publish status of the canvas |
| `last_editor`<br><br>[User](https://developers.facebook.com/docs/graph-api/reference/user/) | User who last edited this canvas |
| `linked_documents`<br><br>[list<Canvas>](https://developers.facebook.com/docs/graph-api/reference/canvas/) | The canvas documents that are reachable via buttons/links in this document |
| `name`<br><br>string | Name used to label the canvas<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `owner`<br><br>[Page](https://developers.facebook.com/docs/graph-api/reference/page/) | Page that owns this canvas |
| `property_list`<br><br>list<string> | List of properties for this canvas |
| `store_url`<br><br>string | The associated app store URL for the canvas |
| `style_list`<br><br>list<enum> | Canvas level style attributes |
| `tags`<br><br>list<string> | Tags associated with Canvas |
| `ui_property_list`<br><br>list<string> | List of UI properties to set when viewing this canvas from creation tools |
| `unused_body_elements`<br><br>list<CanvasPhoto\|CanvasHeader\|CanvasVideo\|CanvasText\|CanvasCarousel\|CanvasButton\|CanvasFooter\|CanvasStoreLocator\|CanvasProductList\|CanvasProductSet> | Body element nodes that belong to the canvas but are not used |
| `update_time`<br><br>int32 | Last updated time of the canvas |
| `use_retailer_item_ids`<br><br>bool | HACK: Flag for whether or not the ad creative that uses this Canvas should use retailer\_item\_ids or not |

### Edges

| Edge | Description |
| --- | --- |
| [`preview`](https://developers.facebook.com/docs/graph-api/reference/canvas/preview/) | Get preview HTML embed element |
| [`previews`](https://developers.facebook.com/docs/graph-api/reference/canvas/previews/)[](#) | Get preview notifications for the canvas |

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 80001 | There have been too many calls to this Page account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can update a [Canvas](https://developers.facebook.com/docs/graph-api/reference/canvas/) by making a POST request to [`/{canvas_id}`](https://developers.facebook.com/docs/graph-api/reference/canvas/).

### Parameters

| Parameter | Description |
| --- | --- |
| `background_color`<br><br>string | Background color of the canvas |
| `body_element_ids`<br><br>list<numeric string or integer> | A list of canvas element ids |
| `enable_swipe_to_open`<br><br>boolean | Field used to mark if swipe to open is enabled |
| `is_hidden`<br><br>boolean | Field used to hide a (published) canvas |
| `is_published`<br><br>boolean | Field used to mark the publish state of the canvas |
| `name`<br><br>string | Field used to label the canvas |
| `source_template_id`[](#)<br><br>numeric string or integer | ID of EntRichMediaDocumentTemplate that the Canvas document is created from |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node to which you POSTed.

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Canvas Preview
==============

[](#)

Reading
-------

CanvasPreview

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bcanvas-id%7D%2Fpreview&version=v18.0)

    GET /v18.0/{canvas-id}/preview HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{canvas-id}/preview',
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

    /* make the API call */
    FB.api(
        "/{canvas-id}/preview",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{canvas-id}/preview",
        null,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{canvas-id}/preview"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

This endpoint doesn't have any parameters.

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of CanvasPreview nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Canvas Previews
===============

[](#)

Reading
-------

Sends a Canvas preview notification to specified page admin ids.

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bcanvas-id%7D%2Fpreviews&version=v18.0)

    GET /v18.0/{canvas-id}/previews HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{canvas-id}/previews',
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

    /* make the API call */
    FB.api(
        "/{canvas-id}/previews",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{canvas-id}/previews",
        null,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{canvas-id}/previews"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

| Parameter | Description |
| --- | --- |
| `user_ids`<br><br>list<int> | SELF\_EXPLANATORY |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of TextWithEntities nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Canvas Button
=============

[](#)

Reading
-------

A button inside the canvas

### Example

PHP Business SDKcURL

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

    curl -G \
      --data-urlencode 'fields=[ 
        "action", 
        "id", 
        "name", 
        "rich_text" 
      ]' \
      -d 'access_token=<ACCESS_TOKEN>' \
      https://graph.facebook.com/v2.11/<CANVAS_BUTTON_ID>

### Parameters

This endpoint doesn't have any parameters.

### Fields

| Field | Description |
| --- | --- |
| `id`<br><br>numeric string | The id of the element |
| `action`<br><br>CanvasOpenURLAction | The action associated with the button |
| `background_color`<br><br>string | Color of the button background |
| `bottom_padding`<br><br>numeric string | The padding below the element |
| `button_color`<br><br>string | Color of the button |
| `button_style`<br><br>enum | The style of the button |
| `deep_link`<br><br>string | Deep link destination only for mobile apps (used for mobile install or engagement ads, and app link is supported) |
| `element_group_key`<br><br>string | The element group key to bundle multiple elements in editing |
| `element_type`<br><br>enum | The type of the element<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `font_family`<br><br>string | The font family |
| `font_size`<br><br>numeric string | The size of the font for the text |
| `line_height`<br><br>numeric string | The line height of the text |
| `name`<br><br>string | The name of the element<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `rich_text`<br><br>[CanvasRichText](https://developers.facebook.com/docs/graph-api/reference/canvas-rich-text/) | The text inside the button |
| `text_alignment`<br><br>enum | The alignment of the text |
| `text_color`<br><br>string | The color of the text |
| `top_padding`<br><br>numeric string | The padding above the element |

### Error Codes

| Error | Description |
| --- | --- |
| 80001 | There have been too many calls to this Page account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Canvas Carousel
===============

[](#)

Reading
-------

A carousel inside a canvas

### Example

PHP Business SDKcURL

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
      '/' . <CANVAS_CAROUSEL_ID>,
      RequestInterface::METHOD_GET,
      $params)->getContent();

    curl -G \
      --data-urlencode 'fields=[ 
        "child_elements", 
        "id", 
        "name" 
      ]' \
      -d 'access_token=<ACCESS_TOKEN>' \
      https://graph.facebook.com/v2.11/<CANVAS_CAROUSEL_ID>

### Parameters

This endpoint doesn't have any parameters.

### Fields

| Field | Description |
| --- | --- |
| `id`<br><br>numeric string | The id of the element |
| `bottom_padding`<br><br>numeric string | The padding below the element |
| `child_elements`<br><br>list<CanvasPhoto\|CanvasDynamicPhoto> | The child elements of the carousel |
| `element_group_key`<br><br>string | The element group key to bundle multiple elements in editing |
| `element_type`<br><br>enum | The type of the element<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `name`<br><br>string | The name of the element<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `style`<br><br>enum | The presentation style of the carousel |
| `top_padding`<br><br>numeric string | The padding above the element |

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Canvas Footer
=============

[](#)

Reading
-------

A footer of the canvas

### Example

PHP Business SDKcURL

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

    curl -G \
      --data-urlencode 'fields=[ 
        "child_elements", 
        "id", 
        "name" 
      ]' \
      -d 'access_token=<ACCESS_TOKEN>' \
      https://graph.facebook.com/v2.11/<CANVAS_FOOTER_ID>

### Parameters

This endpoint doesn't have any parameters.

### Fields

| Field | Description |
| --- | --- |
| `id`<br><br>numeric string | The id of the element |
| `background_color`<br><br>string | Background color of the button |
| `bottom_padding`<br><br>numeric string | The padding below the element |
| `child_elements`<br><br>list<CanvasButton> | The child elements inside a footer |
| `element_group_key`<br><br>string | The element group key to bundle multiple elements in editing |
| `element_type`<br><br>enum | The type of the element<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `name`<br><br>string | The name of the element<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `top_padding`<br><br>numeric string | The padding above the element |

### Error Codes

| Error | Description |
| --- | --- |
| 80001 | There have been too many calls to this Page account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can delete a [CanvasFooter](https://developers.facebook.com/docs/graph-api/reference/canvas-footer/) by making a DELETE request to [`/{canvas_footer_id}`](https://developers.facebook.com/docs/graph-api/reference/canvas-footer/).

### Parameters

This endpoint doesn't have any parameters.

### Return Type

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

[](#)

Canvas Product List
===================

[](#)

**Only E-commerce and travel hotel vertical catalogs are currently supported.**

[](#)

Reading
-------

A product list inside the canvas

  

Select a product catalog and then manually provide the product ID, name and color variations to promote in a collection's ad creative. Use this option if you or your advertiser does not want to set-up a product set from a catalog feed. This option makes creating of ads from product catalog simpler. **Note that we do not save selected products as a product set for later reuse.**

Use this option to select which item colors you want to show in an ad and control the order products appear. **Because this is a manual ordering, we do not dynamically rank or display products based on popularity or relevancy to each viewer.**

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bcanvas-product-list-id%7D&version=v18.0)

    GET /v18.0/{canvas-product-list-id} HTTP/1.1
    Host: graph.facebook.com

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

    /* make the API call */
    FB.api(
        "/{canvas-product-list-id}",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

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

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

This endpoint doesn't have any parameters.

### Fields

| Field | Description |
| --- | --- |
| `id`<br><br>numeric string | The id of the element |
| `bottom_padding`<br><br>numeric string | The padding below the element |
| `element_group_key`<br><br>string | The element group key to bundle multiple elements in editing |
| `element_type`<br><br>enum | The type of the element<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `item_description`<br><br>string | A token to represent which field from the product to show in the product description |
| `item_headline`<br><br>string | A token to represent which field from the product to show in the product headline |
| `name`<br><br>string | The name of the element<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `product_id_list`<br><br>list<integer> | A list of product ids inside the canvas |
| `top_padding`<br><br>numeric string | The padding above the element |

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

Provide a list of products for the element. This must include more than four IDs. IDs must be from Dynamic Ads product catalog or Dynamic Ads for Travel, hotel catalog.

`curl \ -F 'bottom_padding=8' \ -F 'name=Product List Name' \ -F 'product_id_list=[product_id_1, product_id_2, product_id_3, product_id_4]' \ -F 'item_headline=See more at {{product.url}}' \ -F 'item_description={{product.current_price}}' \ -F 'top_padding=24' \ -F 'access_token=TOKEN' \ https://graph.facebook.com/VERSION/CANVAS_ELEMENT_PRODUCT_LIST_ID`  
  

You can update a [CanvasProductList](https://developers.facebook.com/docs/graph-api/reference/canvas-product-list/) by making a POST request to [`/{canvas_product_list_id}`](https://developers.facebook.com/docs/graph-api/reference/canvas-product-list/).

### Parameters

| Parameter | Description |
| --- | --- |
| `bottom_padding`<br><br>float | The padding below the product list |
| `item_description`<br><br>string | A token to represent which field from the product to show in the product description |
| `item_headline`<br><br>string | A token to represent which field from the product to show in the product headline |
| `name`<br><br>string | Name of the product list element |
| `product_id_list`<br><br>list<int64> | A list of product ids inside the canvas<br><br>Required |
| `top_padding`<br><br>float | The padding above the product list |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node to which you POSTed.

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

[](#)

Deleting
--------

You can delete a [CanvasProductList](https://developers.facebook.com/docs/graph-api/reference/canvas-product-list/) by making a DELETE request to [`/{canvas_product_list_id}`](https://developers.facebook.com/docs/graph-api/reference/canvas-product-list/).

### Parameters

This endpoint doesn't have any parameters.

### Return Type

Struct {

`success`: bool,

}

[](#)

Canvas Product Set
==================

[](#)

Reading
-------

A product set inside the canvas

Starting September 14, 2021, the following fields will throw an error for version 12.0+ calls made by apps that lack the endpoint's required permissions. This change will apply to all versions on December 13, 2021.

* `storefront_settings`
    

### Example

PHP Business SDKcURL

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

    curl -G \
      --data-urlencode 'fields=[ 
        "id", 
        "name", 
        "product_set_id" 
      ]' \
      -d 'access_token=<ACCESS_TOKEN>' \
      https://graph.facebook.com/v2.11/<CANVAS_PRODUCT_SET_ID>

### Parameters

This endpoint doesn't have any parameters.

### Fields

| Field | Description |
| --- | --- |
| `id`<br><br>numeric string | The id of the element |
| `bottom_padding`<br><br>numeric string | The padding below the element |
| `element_group_key`<br><br>string | The element group key to bundle multiple elements in editing |
| `element_type`<br><br>enum | The type of the element<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `image_overlay_spec`[](#)<br><br>[AdCreativeLinkDataImageOverlaySpec](https://developers.facebook.com/docs/marketing-api/reference/ad-creative-link-data-image-overlay-spec/) | How to render overlays over a product item |
| `item_description`<br><br>string | A token to represent which field from the product to show in the product description |
| `item_headline`<br><br>string | A token to represent which field from the product to show in the product headline |
| `max_products`<br><br>unsigned int32 | Maximum number of products to show |
| `name`<br><br>string | The name of the element<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `product_set_id`<br><br>numeric string | The product set id which contains a subset of products within a product catalog |
| `retailer_item_ids`<br><br>list<string> | An array of items that should be shown first in the product set element. If this is not set then products will be dynamically chosen |
| `show_in_feed`<br><br>bool | A flag that products should be shown in feed unit |
| `top_padding`<br><br>numeric string | The padding above the element |

### Error Codes

| Error | Description |
| --- | --- |
| 80001 | There have been too many calls to this Page account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |
| 100 | Invalid parameter |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

### Create a Collection Ads Product Set

To create a product set used in Collection ads from a set of products in Dynamic Ads:

`curl -F 'canvas_product_set={ "bottom_padding": 8, "max_items": 50, "name": "Collection Product Set Name", "product_set_id": "PRODUCT_SET_ID", "show_in_feed": true, "item_headline": "See more at {{product.brand | titleize}}", "item_description": "{{product.price}}", "retailer_item_ids": [ "RETAILER_ID_1", "RETAILER_ID_2", "RETAILER_ID_3", "RETAILER_ID_4", ], "top_padding": 24 }' \ -F 'access_token=ACCESS_TOKEN' \ https://graph.facebook.com/VERSION/PAGE_ID/canvas_elements`

[](#)

Canvas Text
===========

[](#)

Reading
-------

Text element of the canvas

### Example

PHP Business SDKcURL

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

    curl -G \
      --data-urlencode 'fields=[ 
        "id", 
        "name", 
        "rich_text" 
      ]' \
      -d 'access_token=<ACCESS_TOKEN>' \
      https://graph.facebook.com/v2.11/<CANVAS_TEXT_ID>

### Parameters

This endpoint doesn't have any parameters.

### Fields

| Field | Description |
| --- | --- |
| `id`<br><br>numeric string | The id of the element |
| `background_color`<br><br>string | The color of the background for the element |
| `bottom_padding`<br><br>numeric string | The padding below the element |
| `element_group_key`<br><br>string | The element group key to bundle multiple elements in editing |
| `element_type`<br><br>enum | The type of the element<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `font_family`<br><br>string | The font family |
| `font_size`<br><br>numeric string | The size of the font for the text |
| `line_height`<br><br>numeric string | The line height of the text |
| `name`<br><br>string | The name of the element<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `rich_text`<br><br>[CanvasRichText](https://developers.facebook.com/docs/graph-api/reference/canvas-rich-text/) | The text content of the element |
| `text_alignment`<br><br>enum | The alignment of the text |
| `text_color`<br><br>string | The color of the text |
| `top_padding`<br><br>numeric string | The padding above the element |

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can delete a [CanvasText](https://developers.facebook.com/docs/graph-api/reference/canvas-text/) by making a DELETE request to [`/{canvas_text_id}`](https://developers.facebook.com/docs/graph-api/reference/canvas-text/).

### Parameters

This endpoint doesn't have any parameters.

### Return Type

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 210 | User not visible |

[](#)

Canvas Video
============

[](#)

Reading
-------

A video inside canvas

### Example

PHP Business SDKcURL

    use FacebookAds\Api;
    use FacebookAds\Http\RequestInterface;
    
    $params = array(
      'fields' => array(
        'id',
        'name',
        'video',
      ),
    );
    
    $data = Api::instance()->call(
      '/' . <CANVAS_VIDEO_ID>,
      RequestInterface::METHOD_GET,
      $params)->getContent();

    curl -G \
      --data-urlencode 'fields=[ 
        "id", 
        "name", 
        "video" 
      ]' \
      -d 'access_token=<ACCESS_TOKEN>' \
      https://graph.facebook.com/v2.11/<CANVAS_VIDEO_ID>

### Parameters

This endpoint doesn't have any parameters.

### Fields

| Field | Description |
| --- | --- |
| `id`<br><br>numeric string | The id of the element |
| `bottom_padding`<br><br>numeric string | The padding below the element |
| `element_group_key`<br><br>string | The element group key to bundle multiple elements in editing |
| `element_type`<br><br>enum | The type of the element<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `name`<br><br>string | The name of the element<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `style`<br><br>enum | The presentation style of the video |
| `top_padding`<br><br>numeric string | The padding above the element |
| `video`<br><br>[Video](https://developers.facebook.com/docs/graph-api/reference/video/) | The facebook video node |

### Error Codes

| Error | Description |
| --- | --- |
| 80001 | There have been too many calls to this Page account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can delete a [CanvasVideo](https://developers.facebook.com/docs/graph-api/reference/canvas-video/) by making a DELETE request to [`/{canvas_video_id}`](https://developers.facebook.com/docs/graph-api/reference/canvas-video/).

### Parameters

This endpoint doesn't have any parameters.

### Return Type

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 210 | User not visible |

[](#)