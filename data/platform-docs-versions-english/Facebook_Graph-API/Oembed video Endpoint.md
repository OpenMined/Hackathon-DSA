Oembed Video
============

Reading
-------

OembedVideo

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=oembed_video&version=v19.0)

    GET /v19.0/oembed_video HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/oembed_video',
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
        "/oembed_video",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/oembed_video",
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
                                   initWithGraphPath:@"/oembed_video"
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
| `maxwidth`<br><br>int64 | maxwidth |
| `omitscript`<br><br>boolean | Default value: `false`<br><br>omitscript |
| `sdklocale`<br><br>string | sdklocale |
| `url`<br><br>URI | url<br><br>Required |
| `useiframe`<br><br>boolean | Default value: `false`<br><br>useiframe |

### Fields

| Field | Description |
| --- | --- |
| `author_name`<br><br>string | author\_name<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `author_url`<br><br>string | author\_url<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `height`<br><br>int32 | height<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `html`<br><br>string | html<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `provider_name`<br><br>string | provider\_name<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `provider_url`<br><br>string | provider\_url<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `type`<br><br>string | type<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `version`<br><br>string | version<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `width`<br><br>int32 | width<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |

### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
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