Games IAPProduct
================

Reading
-------

An in-app-purchaseable product

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bgames-iap-product-id%7D&version=v19.0)

    GET /v19.0/{games-iap-product-id} HTTP/1.1
    Host: graph.facebook.com

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

    /* make the API call */
    FB.api(
        "/{games-iap-product-id}",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

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

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

This endpoint doesn't have any parameters.

### Fields

| Field | Description |
| --- | --- |
| `id`<br><br>numeric string | The id of the object |
| `description`<br><br>string | Description of the product (e.g. "Used as in-app currency")<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `image_uri`<br><br>string | The associated image of the product for the Facebook Pay dialog<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `local_price_amount_cents`<br><br>integer | Local price of the product in 1/100ths of the major unit of currency (e.g. 1 JPY -> 100, 1.23 USD -> 123)<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `local_price_formatted`<br><br>string | Human-readable local price of the product (e.g. "$1.23")<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `price`<br><br>string | Human-readable price of the product (e.g. "$1.23")<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `price_amount_cents`<br><br>unsigned int32 | Price of the product in 1/100ths of the major unit of currency (e.g. 1 JPY -> 100, 1.23 USD -> 123)<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `price_currency_code`<br><br>string | Currency code of price (e.g. "JPY", "USD")<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `product_id`<br><br>string | Identifier for the product (e.g. "gold\_bar")<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `product_type`<br><br>enum | Type of the product (e.g. managed)<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `subscription_term`<br><br>enum | The subscription renewal length of time if ProductType is SUBSCRIPTION<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `title`<br><br>string | Title of the product displayed to the user (e.g. "Gold Bar")<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

Creating
--------

You can't perform this operation on this endpoint.

Updating
--------

You can't perform this operation on this endpoint.

Deleting
--------

You can't perform this operation on this endpoint.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)