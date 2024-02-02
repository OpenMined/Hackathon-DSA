CPASAdvertiser Partnership Recommendation
=========================================

Reading
-------

Returns a recommendation of a single retailer for a specific brand. This endpoint returns a retailer-brand pair and an advertiser who can advertise on behalf of the producer.

This endpoint is mainly for Facebook’s Marketing Partners using [Collaborative Ads](https://developers.facebook.com/docs/marketing-api/collaborative-ads).

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bcpas-advertiser-partnership-recommendation-id%7D&version=v19.0)

    GET /v19.0/{cpas-advertiser-partnership-recommendation-id} HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{cpas-advertiser-partnership-recommendation-id}',
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
        "/{cpas-advertiser-partnership-recommendation-id}",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{cpas-advertiser-partnership-recommendation-id}",
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
                                   initWithGraphPath:@"/{cpas-advertiser-partnership-recommendation-id}"
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
| `id`<br><br>numeric string | ID of the recommendation object. |
| `advertiser_business_id`<br><br>numeric string | Recommended advertiser for this partnership. |
| `brand_business_id`<br><br>numeric string | Recommended brand for this partnership. |
| `brands`<br><br>list<string> | Brands that can be advertised for in this partnership. |
| `countries`<br><br>list<string> | Countries in which the partnership could run ads. |
| `merchant_business_id`<br><br>numeric string | Recommended retailer for this partnership. |
| `merchant_categories`<br><br>list<string> | Categories associated with the retailer's products. |
| `status`<br><br>enum | Current status of this recommendation based on actions taken on it. |
| `status_reason`<br><br>enum | Reason why this recommendation has its current status. |

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