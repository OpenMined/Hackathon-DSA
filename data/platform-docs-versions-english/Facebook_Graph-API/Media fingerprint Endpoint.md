Media Fingerprint
=================

Reading
-------

Media fingerprint

### New Page Experience

This endpoint is supported for [New Page Experience](https://developers.facebook.com/docs/pages/new-pages-experience/).

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bmedia-fingerprint-id%7D&version=v19.0)

    GET /v19.0/{media-fingerprint-id} HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{media-fingerprint-id}',
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
        "/{media-fingerprint-id}",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{media-fingerprint-id}",
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
                                   initWithGraphPath:@"/{media-fingerprint-id}"
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
| `id`<br><br>numeric string | Media fingerprint ID<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `duration_in_sec`<br><br>float | The length of the fingerprinted content, in seconds<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `fingerprint_content_type`<br><br>enum | Media fingerprint content type<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `metadata`<br><br>FingerprintMetadata | The metadata associated with the fingerprinted content |
| `title`<br><br>string | The title of the fingerprinted content |
| `universal_content_id`<br><br>string | A unique code user can use to manage fingerprint. For example: International Standard Recording Code for songtracks. This is for your own use; Facebook will not use this data. |

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

Creating
--------

You can't perform this operation on this endpoint.

Updating
--------

You can update a [MediaFingerprint](https://developers.facebook.com/docs/graph-api/reference/media-fingerprint/) by making a POST request to [`/{media_fingerprint_id}`](https://developers.facebook.com/docs/graph-api/reference/media-fingerprint/).

### Parameters

| Parameter | Description |
| --- | --- |
| `metadata`<br><br>array | The fingerprint metadata, for example: metadata={'episode':'newEpisodeVal','season':'newSeasonVal'} |
| `album`<br><br>string | Album name of a songtrack. This is a required metadata field for SONGTRACK content type. |
| `artist`<br><br>string | Artist name of a songtrack. This is a required metadata field for SONGTRACK content type. |
| `episode`<br><br>string | Episode name of an episode. This is a required metadata field for EPISODE content type. |
| `season`<br><br>string | Season name of an episode. This is a required metadata field for EPISODE content type. |
| `description`<br><br>string | Description of fingerprint. This is a required metadata field for MOVIE and OTHER content type. |
| `source`<br><br>file | The source of the new fingerprint file to update. Example: @myDirectory/myFile.mp4.rdm |
| `title`<br><br>string | The title of the media content |
| `universal_content_id`<br><br>string | A unique code user can use to manage fingerprint. For example: International Standard Recording Code for songtracks. This is for your own use; Facebook will not use this data. |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node to which you POSTed.

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

Deleting
--------

You can't perform this operation on this endpoint.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)