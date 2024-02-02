/event/photos - Documentation - Meta for Developers

/event/photosThis document refers to an outdated version of Graph API. Please use the latest version.Graph API Versionv18.0Graph API Reference `/{event-id}``/photos`
==========================================
All the photos uploaded to an event's wall.
Reading
-------
HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v19.0/{event-id}/photos HTTP/1.1
Host: graph.facebook.com
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{event-id}/photos',
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
    "/{event-id}/photos",
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
    "/{event-id}/photos",
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
                               initWithGraphPath:@"/{event-id}/photos"
                                      parameters:params
                                      HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
### Permissions
* A user access token is required.
### Fields
An array of Photo objects.
Publishing
----------
There are two separate ways of publishing photos to Facebook:
1. Capture a photo via file upload as `multipart/form-data` then use the `source` parameter:
HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK
```
POST /v19.0/{event-id}/photos HTTP/1.1
Host: graph.facebook.com
source=%7Bimage-data%7D
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->post(
    '/{event-id}/photos',
    array (
      'source' => '{image-data}',
    ),
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
    "/{event-id}/photos",
    "POST",
    {
        "source": "{image-data}"
    },
    function (response) {
      if (response && !response.error) {
        /* handle the result */
      }
    }
);
```
```
Bundle params = new Bundle();
params.putString("source", "{image-data}");
/* make the API call */
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "/{event-id}/photos",
    params,
    HttpMethod.POST,
    new GraphRequest.Callback() {
        public void onCompleted(GraphResponse response) {
            /* handle the result */
        }
    }
).executeAsync();
```
```
NSDictionary *params = @{
  @"source": @"{image-data}",
};
/* make the API call */
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                               initWithGraphPath:@"/{event-id}/photos"
                                      parameters:params
                                      HTTPMethod:@"POST"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
1. Use a photo that is already on the internet by publishing using the `url` parameter:
HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK
```
POST /v19.0/{event-id}/photos HTTP/1.1
Host: graph.facebook.com
url=%7Bimage-url%7D
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->post(
    '/{event-id}/photos',
    array (
      'url' => '{image-url}',
    ),
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
    "/{event-id}/photos",
    "POST",
    {
        "url": "{image-url}"
    },
    function (response) {
      if (response && !response.error) {
        /* handle the result */
      }
    }
);
```
```
Bundle params = new Bundle();
params.putString("url", "{image-url}");
/* make the API call */
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "/{event-id}/photos",
    params,
    HttpMethod.POST,
    new GraphRequest.Callback() {
        public void onCompleted(GraphResponse response) {
            /* handle the result */
        }
    }
).executeAsync();
```
```
NSDictionary *params = @{
  @"url": @"{image-url}",
};
/* make the API call */
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                               initWithGraphPath:@"/{event-id}/photos"
                                      parameters:params
                                      HTTPMethod:@"POST"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
### Permissions
* A user access token with `publish_actions` permission can be used to publish new photos.
### Fields

Name
 | 
Description
 | 
Type
 || `source` | The photo, encoded as form data. Either this or `url` field is required, but both should not be used together. | `multipart/form-data` |
| `url` | The URL of a photo that is already uploaded to the internet. Either this or `source` is required, but both should not be used together. | `string` |
| `message` | The description of the photo, used as the accompanying status message in any feed story. | `string` |
### Response
If successful:

Name
 | 
Description
 | 
Type
 || `id` | The newly created photo ID | `string` |
Deleting
--------
You can't delete using this edge, however you can delete each photo using the /{photo-id} node.
Updating
--------
You can't update using this edge.