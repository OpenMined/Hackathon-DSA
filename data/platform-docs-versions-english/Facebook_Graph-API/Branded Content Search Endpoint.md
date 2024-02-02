Branded Content Search
======================

Reading
-------

Returns branded content based on your search. By default we only return content that is currently available on Facebook or Instagram, and content that was created on or after August 17, 2023.

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=branded_content_search&version=v19.0)

    GET /v19.0/branded_content_search HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/branded_content_search',
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
        "/branded_content_search",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/branded_content_search",
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
                                   initWithGraphPath:@"/branded_content_search"
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
| `creation_date_max`<br><br>string | Search for branded content posted after the date (inclusive) you provide. The date format should be YYYY-mm-dd.<br><br>Required |
| `creation_date_min`<br><br>string | Search for branded content posted before the date (inclusive) you provide. The date format should be YYYY-mm-dd.<br><br>Required |
| `ig_username`<br><br>string | Search for an Instagram account that posted branded content or was a brand partner. Your search must include this parameter or page\_url. |
| `page_url`<br><br>URI | Search for a Facebook Page that posted branded content or was a brand partner. Your search must include this parameter or ig\_username. |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [BrandedContentSearch](https://developers.facebook.com/docs/graph-api/reference/branded-content-search/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

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