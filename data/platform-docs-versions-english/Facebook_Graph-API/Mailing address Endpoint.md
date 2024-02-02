Mailing Address
===============

A mailing address

Reading
-------

A mailing address object

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bmailing-address-id%7D&version=v19.0)

    GET /v19.0/{mailing-address-id} HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{mailing-address-id}',
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
        "/{mailing-address-id}",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{mailing-address-id}",
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
                                   initWithGraphPath:@"/{mailing-address-id}"
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
| `id`<br><br>numeric string | The mailing address ID |
| `city`<br><br>string | Address city name<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `city_page`<br><br>[Page](https://developers.facebook.com/docs/graph-api/reference/page/) | Page representing the address city |
| `country`<br><br>string | Country of the address<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `postal_code`<br><br>string | Postal code of the address<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `region`<br><br>string | Region or state of the address<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `street1`<br><br>string | Street address<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `street2`<br><br>string | Second part of the street address - apt, suite, etc<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |

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