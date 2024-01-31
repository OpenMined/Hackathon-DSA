This document refers to an outdated version of Graph API. Please [use the latest version.](https://developers.facebook.com/docs/graph-api/reference/v19.0/link)

Link `/{link-id}`
=================

A link shared on Facebook.

Reading
-------

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Blink-id%7D&version=v19.0)

    GET /v19.0/{link-id} HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{link-id}',
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
        "/{link-id}",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{link-id}",
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
                                   initWithGraphPath:@"/{link-id}"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### Permissions

* Any valid access token if the link is public
    

### Fields

| Name | Description | Type |
| --- | --- | --- |
| `id` | The link ID. | `string` |
| `created_time` | The time the message was published. | `datetime` |
| `description` | A description of the link (appears beneath the link caption). | `string` |
| `from` | The user that created the link. | [`User`](https://developers.facebook.com/docs/graph-api/reference/user) |
| `icon` | A URL to the link icon that Facebook displays in Feed. | `string` |
| `link` | The URL that was shared. | `string` |
| `message` | The optional message from the user about this link. | `string` |
| `name` | The name of the link. | `string` |
| `picture` | A URL to the thumbnail image used in the link post | `string` |
| `reactions`<br><br>  <br><br>Deprecated in v8.0+. | Reactions, LIKE, LOVE, WOW, HAHA, SORRY, ANGRY, NONE, to a link. | `string` |

Publishing
----------

Please use the [Sharing documentation](https://developers.facebook.com/docs/sharing/) to publish.

Updating
--------

You can't update a link using the Graph API.

Edges
-----

| Name | Description |
| --- | --- |
| [`/likes`](https://developers.facebook.com/docs/graph-api/reference/object/likes) | People who like this link. |
| [`/comments`](https://developers.facebook.com/docs/graph-api/reference/object/comments) | Comments on this link. |

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)