
Request - Graph API - Documentation - Meta for Developers












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
This document refers to an outdated version of Graph API. Please use the latest version.Graph API Versionv18.0Request `/{request-id}`
=======================

An individual game request received by someone, sent by an app or by another person.

### Related Guides

* Game Requests
* `/{user-id}/apprequests`
Reading
-------

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v19.0/{request-id} HTTP/1.1
Host: graph.facebook.com
```

```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{request-id}',
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
    "/{request-id}",
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
    "/{request-id}",
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
                               initWithGraphPath:@"/{request-id}"
                                      parameters:params
                                      HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
### Permissions

* A user access token is required if you are requesting using only the Request object ID, and want to know about the recipient of the request. The request must have been sent to the person whose access token you are using.
* An app access token can be used when you are requesting using the concatenated Request object ID and user ID string, or when you are only using the request object ID, but do not need to know recipient info. See the Requests docs for more info on this ID.

### Fields



 
Name
 | 
Description
 | 
Type
 || `id` | The request object ID. | `string` |
| `application` | App associated with the request. | `App` |
| `to` | The recipient of the request. | `User` |
| `from` | The sender associated with the request. This is only included for user to user requests. | `User` |
| `message` | A string describing the request. | `string` |
| `created_time` | Timestamp when the request was created. | `datetime` |

Publishing
----------

You can't publish using this endpoint.

Requests are published via the Game Request Dialog. If your app is a **Game** you can publish app requests using the `/{user-id}/apprequests` edge.

Deleting
--------

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK
```
DELETE /v19.0/{request-id} HTTP/1.1
Host: graph.facebook.com
```

```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->delete(
    '/{request-id}',
    array (),
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
    "/{request-id}",
    "DELETE",
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
    "/{request-id}",
    null,
    HttpMethod.DELETE,
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
                               initWithGraphPath:@"/{request-id}"
                                      parameters:params
                                      HTTPMethod:@"DELETE"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
### Permissions

* A user access token is required if you are using only the Request object ID. The request must also have been sent to the person whose access token you are using.
* An app access token can be used when you are using the concatenated Request object ID and user ID string.

### Fields

No fields are needed to delete.

### Response

If successful:


```
{
  "success": true
}
```
Otherwise a relevant error message will be returned.

Updating
--------

You can't update using this endpoint.




































 
