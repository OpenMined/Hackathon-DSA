Object Likes - Graph API - Documentation - Meta for Developers

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
This document refers to an outdated version of Graph API. Please use the latest version.Graph API Versionv18.0`/{object-id}/likes`
====================
This reference describes the `/likes` edge that is common to multiple Graph API nodes. The structure and operations are the same for each node. The following objects have a `/likes` edge:

|  |  |
| --- | --- |
| * Album
* Comment
* Page
* Photo
* User
* Video
 |  |
Reading
-------

Returns the list of people who liked this object. When reading likes on a Page or User object, this endpoint returns a list of pages liked by that Page or User.

Use the `likes` field of an object to get the number of likes.

We recommended that you use the `/object/reactions` endpoint to get like counts, if available.

### New Page Experience

The following objects `/likes` endpoint are supported for New Page Experience:

|  |  |
| --- | --- |
| * Album
* Comment
* Photo
* PagePost
 | * User
 |
### Requirements
* The same requirements required to view the object are required to view likes on that object.

### Limitations
* Only aggregated counts using `total_count` with the `summary` parameter are available for Post likes.
* The `like` reaction counts include both "like" and "care" reactions.
* `total_count` represents the approximate number of likes, however, the actual number returned might be different depending on privacy settings.
* The `GET /{group-post-id}/likes` and `GET /{post-id}/likes` endpoints are deprecated in v8.0+ and deprecated in all versions on Nov. 2, 2020.
### Fields

Property Name
 | 
Description
 | 
Type
 || `total_count` | Total number of User and Page likes on the object. To have this field returned, you must include the `summary=true` parameter and value in your request. | `int32` |
### Example Usage

**Sample Request**
```
curl -i -X GET "https://graph.facebook.com/{object-id}
  ?fields=likes.summary(true)
  &access_token={access-token}"
```
#### Sample Response

```
  {
  "likes": {
    "data": [
      {
        "name": "Bill the Cat",
        "id": "155111347875779",
        "created_time": "2017-06-18T18:21:04+0000"
      },
      {
        "name": "Calvin and Hobbes",
        "id": "257573197608192",
        "created_time": "2017-06-18T18:21:02+0000"
      },
      {
        "name": "Berkeley Breathed's Bloom County",
        "id": "108793262484769",
        "created_time": "2017-06-18T18:20:58+0000"
      }
    ],
    "paging": {
      "cursors": {
        "before": "Nzc0Njg0MTQ3OAZDZD",
        "after": "NTcxODc1ODk2NgZDZD"
      },
      "next": "https://graph.facebook.com/vX.X/me/likes?access_token=user-access-token&pretty=0&summary=true&limit=25&after=NTcxODc1ODk2NgZDZD"
    },
    "summary": {
      "total_count": 136
    }
  },
  "id": "user-id"
}
```
Publish
-------
Like an object.

### New Page Experience

The following objects `/likes` endpoint are supported for New Page Experience:

|  |  |
| --- | --- |
| * Album
* Comment
* PagePost
 |  |
HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK
```
POST /v19.0/{object-id}/likes HTTP/1.1
Host: graph.facebook.com
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->post(
    '/{object-id}/likes',
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
    "/{object-id}/likes",
    "POST",
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
    "/{object-id}/likes",
    null,
    HttpMethod.POST,
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
                               initWithGraphPath:@"/{object-id}/likes"
                                      parameters:params
                                      HTTPMethod:@"POST"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
### Permissions
* A Page access token requested by a person who can perform the `CREATE_CONTENT` task on the Page
* The `pages_manage_engagement` permission
### Limitations
* The Page must also be able to like the object (whether via API or on Facebook.com).
* The object must not have already been liked by the Page.
* If the Page has already reacted to an object (wow, sad) then a like will succeed, but the reaction will not change.
* Liking a Page review is not supported.
### Fields
No fields are required to add likes.

### Response
On success, your app will receive the following response:

```
{
  "success": true
}
```
Updating
--------
You can't perform this operation on this endpoint.
Delete
------
Delete likes on Page objects using this endpoint.

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK
```
DELETE /v19.0/{object-id}/likes HTTP/1.1
Host: graph.facebook.com
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->delete(
    '/{object-id}/likes',
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
    "/{object-id}/likes",
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
    "/{object-id}/likes",
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
                               initWithGraphPath:@"/{object-id}/likes"
                                      parameters:params
                                      HTTPMethod:@"DELETE"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
### Permissions
* A Page access token requested by a person who can perform the `MODERATE` task on the Page
* The `pages_manage_engagement` permission
### Limitations
* A User or Page can only delete their own `likes`.
* The object must have already been liked.
* Deleting a Page review like is not supported.
### Fields
There are no fields for this endpoint.

### Response
On success, your app will receive the following response:

```
{
  "success": true
}
```