`/{place-tag-id}`
=================

An instance of a person being tagged at a place in a photo, video, post, status or link.

Reading
-------

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bplace-tag-id%7D&version=v19.0)

    GET /v19.0/{place-tag-id} HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{place-tag-id}',
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
        "/{place-tag-id}",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{place-tag-id}",
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
                                   initWithGraphPath:@"/{place-tag-id}"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### Permissions

* A user access token with `user_tagged_places` permission is required to see any tags involving that person.
    

### Fields

| Name | Description | Type |
| --- | --- | --- |
| `id` | The ID of this place tag. | `string` |
| `created_time` | When the tag was created. | `datetime` |
| `place` | The Facebook Page representing the place. | [`Page`](https://developers.facebook.com/docs/graph-api/reference/page/) |

Publishing
----------

Use the [`/{user-id}/feed`](https://developers.facebook.com/docs/graph-api/reference/user/feed/) edge to create posts with place tagging.

Deleting
--------

You can't delete place tags, however if the original content that created the tag is removed, the place tag will also be removed.

Updating
--------

You can't update using this node.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)