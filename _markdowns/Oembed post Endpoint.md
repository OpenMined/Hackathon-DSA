
Graph API Reference v19.0: Oembed Post - Documentation - Meta for Developers











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
Graph API Versionv19.0Oembed Post
===========

Reading
-------

OembedPost


### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v19.0/oembed_post HTTP/1.1
Host: graph.facebook.com
```

```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/oembed_post',
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
    "/oembed_post",
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
    "/oembed_post",
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
                               initWithGraphPath:@"/oembed_post"
                                      parameters:params
                                      HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
If you want to learn how to use the Graph API, read our Using Graph API guide.### Parameters



| Parameter | Description |
| --- | --- |
| `maxwidth`int64 | Maximum width of returned post.
 |
| `omitscript`boolean | Default value: `false`If set to true, the returned embed HTML code will not include any javascript.
 |
| `sdklocale`string | sdklocale
 |
| `url`URI | The post's URL.
Required |
| `useiframe`boolean | Default value: `false`useiframe
 |

### Fields



| Field | Description |
| --- | --- |
| `author_name`string | The name of the Facebook user that owns the post.
Default |
| `author_url`string | A URL for the author/owner of the post.
Default |
| `height`int32 | The height in pixels required to display the HTML.
Default |
| `html`string | The HTML used to display the post.
Default |
| `provider_name`string | Name of the provider (Facebook).
Default |
| `provider_url`string | URL of the provider (Facebook).
Default |
| `type`string | The oEmbed resource type. See https://oembed.com/.
Default |
| `version`string | Always 1.0. See https://oembed.com/
Default |
| `width`int32 | The width in pixels required to display the HTML.
Default |

### Error Codes



| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |

Creating
--------

You can't perform this operation on this endpoint.Updating
--------

You can't perform this operation on this endpoint.Deleting
--------

You can't perform this operation on this endpoint.
































