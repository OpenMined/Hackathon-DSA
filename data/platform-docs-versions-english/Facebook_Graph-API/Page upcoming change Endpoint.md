Page Upcoming Change
====================

Reading
-------

Notification of page upcoming changes.

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bpage-upcoming-change-id%7D&version=v19.0)

    GET /v19.0/{page-upcoming-change-id} HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{page-upcoming-change-id}',
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
        "/{page-upcoming-change-id}",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{page-upcoming-change-id}",
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
                                   initWithGraphPath:@"/{page-upcoming-change-id}"
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
| `id`<br><br>numeric string | The ID of the upcoming change |
| `change_type`<br><br>enum | The type of the upcoming change<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `effective_time`<br><br>datetime | The time when the upcoming change will become effective<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `page`<br><br>[Page](https://developers.facebook.com/docs/graph-api/reference/page/) | The associated page of this upcoming change<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `proposal`<br><br>[PageChangeProposal](https://developers.facebook.com/docs/graph-api/reference/page-change-proposal/) | The proposal associated with the change, only valid when change\_type is knowledge\_proposal<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `timer_status`<br><br>enum | The status of the timer associated with this change<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |

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