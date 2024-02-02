
Graph API Reference v19.0: Instagram Oembed - Documentation - Meta for Developers











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
Graph API Versionv19.0Instagram Oembed
================

Reading
-------

InstagramOembed


### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v19.0/instagram_oembed HTTP/1.1
Host: graph.facebook.com
```

```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/instagram_oembed',
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
    "/instagram_oembed",
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
    "/instagram_oembed",
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
                               initWithGraphPath:@"/instagram_oembed"
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
| `hidecaption`boolean | If set to true, the embed code hides the caption. Defaults to false if parameter is not included in request.
 |
| `maxwidth`int64 | Maximum width of returned media. Must be between 320 and 658. Note that the maxheight parameter is not supported. This is because the embed code is responsive and its height varies depending on its width and length of the caption.
 |
| `omitscript`boolean | If set to true, the returned embed HTML code will not include any javascript.
 |
| `url`URI | The post's URL.
Required |

### Fields



| Field | Description |
| --- | --- |
| `author_name`string | The name of the Instagram user that owns the post.
Default |
| `html`string | The HTML used to display the post.
Default |
| `provider_name`string | Name of the provider (Instagram)
Default |
| `provider_url`string | URL of the provider (Instagram)
Default |
| `thumbnail_height`int32 | The height of the thumbnail.
Default |
| `thumbnail_url`string | A url for the post's raw image asset. It must respect the 'maxwidth' parameter from the request. Prefer using the HTML field instead. However, you may use this field if loading the embed code is not an option. If you embed an Instagram image this way, you must provide clear attribution next to the image, including attribution to the original author and to Instagram, and a link to the Instagram media page.
Default |
| `thumbnail_width`int32 | The width of the thumbnail.
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
































