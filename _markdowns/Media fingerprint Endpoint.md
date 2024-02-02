
Graph API Reference v19.0: Media Fingerprint - Documentation - Meta for Developers











Graph API* Overview
* Get Started
* Batch Requests
* Debug Requests
* Handle Errors
* Field Expansion
* Secure Requests
* Resumable Upload API
* Changelog
* Features Reference
* Permissions Reference
* Reference
Graph API Versionv19.0Media Fingerprint
=================

Reading
-------

Media fingerprint


### New Page Experience

This endpoint is supported for New Page Experience.### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v19.0/{media-fingerprint-id} HTTP/1.1
Host: graph.facebook.com
```

```
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
```

```
/* make the API call */
FB.api(
    "/{media-fingerprint-id}",
    function (response) {
      if (response && !response.error) {
        /* handle the result */
      }
    }
);
```

```
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
```

```
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
```
If you want to learn how to use the Graph API, read our Using Graph API guide.### Parameters

This endpoint doesn't have any parameters.### Fields



| Field | Description |
| --- | --- |
| `id`numeric string | Media fingerprint ID
Default |
| `duration_in_sec`float | The length of the fingerprinted content, in seconds
Default |
| `fingerprint_content_type`enum | Media fingerprint content type
Default |
| `metadata`FingerprintMetadata | The metadata associated with the fingerprinted content
 |
| `title`string | The title of the fingerprinted content
 |
| `universal_content_id`string | A unique code user can use to manage fingerprint. For example: International Standard Recording Code for songtracks. This is for your own use; Facebook will not use this data.
 |

### Error Codes



| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

Creating
--------

You can't perform this operation on this endpoint.Updating
--------

You can update a MediaFingerprint by making a POST request to `/{media_fingerprint_id}`.### Parameters



| Parameter | Description |
| --- | --- |
| `metadata`array | The fingerprint metadata, for example:
 metadata={'episode':'newEpisodeVal','season':'newSeasonVal'}
 |
| `album`string | Album name of a songtrack. This is a required metadata field for SONGTRACK content type.
 |
| `artist`string | Artist name of a songtrack. This is a required metadata field for SONGTRACK content type.
 |
| `episode`string | Episode name of an episode. This is a required metadata field for EPISODE content type.
 |
| `season`string | Season name of an episode. This is a required metadata field for EPISODE content type.
 |
| `description`string | Description of fingerprint. This is a required metadata field for MOVIE and OTHER content type.
 |
| `source`file | The source of the new fingerprint file to update. Example: @myDirectory/myFile.mp4.rdm
 |
| `title`string | The title of the media content
 |
| `universal_content_id`string | A unique code user can use to manage fingerprint. For example: International Standard Recording Code for songtracks. This is for your own use; Facebook will not use this data.
 |

### Return Type

This endpoint supports read-after-write and will read the node to which you POSTed. Struct {`success`: bool, }### Error Codes



| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

Deleting
--------

You can't perform this operation on this endpoint.
































