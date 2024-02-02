Object Comments - Graph API - Documentation - Meta for Developers

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
This document refers to an outdated version of Graph API. Please use the latest version.Graph API Versionv18.0`/{object-id}/comments`
=======================
This reference describes the `/comments` edge that is common to multiple Graph API nodes. The structure and operations are the same for each node. The following objects have a `/comments` edge:

|  |  |  |
| --- | --- | --- |
| * Album
* Comment
* Event
* Link
 | * Live Video
* Photo
* Post
 | * Thread
* User
* Video
 |
It is possible for comment objects to have a `/comments` edge, which is called *comment replies*. The structure is the same for these, but attention should be paid to the modifiers for these edges.
Reading
-------
Returns a comment on an object.

The `id` field for the `/PAGEPOST-ID/comments` endpoint will no longer be returned for apps using the Page Public Content Access feature. To access the comment IDs for a Page post you must be able to perform the MODERATE task on the Page being queried. This change is in effect for v11.0+ and will be implement for all versions on September, 7, 2021.
###  New Page Experience
The following objects `/comments` endpoint are supported for New Page Experience:

|  |  |
| --- | --- |
| * Album
* Comment
* Link
* Page
 | * PagePost
* Photo
* Post
* PostComment
 |
### Permissions
* The same permissions required to view the parent object are required to view comments on that object.

### Limitations
* Other users' profile information and comments will not be returned when accessing user posts, photos, albums, videos, likes, and reactions unless authorized by those users.
* Comments returned in a query are based on default filtering. To get all comments that can be returned depending on your permissions, set the `filter` parameter to `stream` or use the `order` field.
* A new Page can comment as the Page on new Pages or classic Pages. However, a classic Page can not comment on a new Page.
* For the following nodes, the `/comments` endpoint returns empty data if you read it with a User access token:
	+ Album
	+ Photo
	+ Post
	+ Video
* The `id` field for the `/PAGEPOST-ID/comments` endpoint will no longer be returned for apps using the Page Public Content Access feature. To access the comment IDs for a Page post you must be able to perform the MODERATE task on the Page being queried.
* For objects that have tens of thousands of comments, you may encounter limits while paging. Learn more about paging in our Using the Graph API Guide.
### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v19.0/{object-id}/comments HTTP/1.1
Host: graph.facebook.com
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{object-id}/comments',
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
    "/{object-id}/comments",
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
    "/{object-id}/comments",
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
                               initWithGraphPath:@"/{object-id}/comments"
                                      parameters:params
                                      HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
### Parameters
HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK
```
GET /v19.0/{object-id}/comments?summary=1&filter=toplevel HTTP/1.1
Host: graph.facebook.com
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{object-id}/comments?summary=1&filter=toplevel',
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
    "/{object-id}/comments",
    {
        "summary": true,
        "filter": "toplevel"
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
params.putBoolean("summary", true);
params.putString("filter", "toplevel");
/* make the API call */
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "/{object-id}/comments",
    params,
    HttpMethod.GET,
    new GraphRequest.Callback() {
        public void onCompleted(GraphResponse response) {
            /* handle the result */
        }
    }
).executeAsync();
```
```
NSDictionary *params = @{
  @"summary": @YES,
  @"filter": @"toplevel",
};
/* make the API call */
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                               initWithGraphPath:@"/{object-id}/comments"
                                      parameters:params
                                      HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```

  Parameter  |  Description  || `summary`
*bool* | A summary of metadata about the comments on the object. Importantly this metadata includes `order` which indicates how the comments are being sorted. |
| `filter`
*enum { toplevel, stream }* | If a person can reply to a comment, you can filter comments based on top level comments, comments that are made directly on the post, or the chronological order of all comments.* `toplevel` - This is the default. It returns all top-level comments in chronological order, as ordered on Facebook. This filter is useful for displaying comments in the same structure as they appear on Facebook.
* `stream` - All-level comments in `chronological` order. This filter is useful for comment moderation tools where it is helpful to see a chronological list of all comments.
 |
### Fields
An array of Comment objects in addition to the following fields when `summary` is `true` in the request.

  Field  |  Description  || `order`
*enum { chronological, reverse\_chronological }* | Order in which comments were returned.* `chronological`: Comments sorted by the oldest comments first.
* `reverse_chronological`: Comments sorted by the newest comments first.
 |
| `total_count`
*int32* | The count of comments on this node. It is important to note that this value changes depending on the `filter` being used (where comment replies are available):* if `filter` is `stream` then `total_count` will be a count of all comments (including replies) on the node.
* if `filter` is `toplevel` then `total_count` will be a count of all top-level comments on the node.
Note: `total_count` can be greater than or equal to the actual number of comments returned due to comment privacy or deletion. |
Publishing
----------
Publish new comments to any object.

###  New Page Experience
The following objects `/comments` endpoint are supported for New Page Experience:

|  |  |
| --- | --- |
| * Comments
* PagePosts
* Photo
* Post
 | * PostComment
* Video
 |
### Permissions
* A Page access token requested by a person who can perform the `MODERATE` task on the Page
* The `pages_manage_engagement` permission
Note, the `can_comment` field on individual comment objects indicates whether it is possible to reply to that comment.
### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK
```
POST /v19.0/{object-id}/comments HTTP/1.1
Host: graph.facebook.com
message=This+is+a+test+comment
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->post(
    '/{object-id}/comments',
    array (
      'message' => 'This is a test comment',
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
    "/{object-id}/comments",
    "POST",
    {
        "message": "This is a test comment"
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
params.putString("message", "This is a test comment");
/* make the API call */
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "/{object-id}/comments",
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
  @"message": @"This is a test comment",
};
/* make the API call */
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                               initWithGraphPath:@"/{object-id}/comments"
                                      parameters:params
                                      HTTPMethod:@"POST"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
### Fields

  Name  |  Description  || `attachment_id`
*string* | An optional ID of a unpublished photo (see `no_story` field in `/{user-id}/photos`) uploaded to Facebook to include as a photo comment. One of `attachment_id`, `attachment_share_url`, `attachment_url`, `message`, or `source` must be provided when publishing. |
| `attachment_share_url`
*string* | The URL of a GIF to include as a animated GIF comment. One of `attachment_id`, `attachment_share_url`, `attachment_url`, `message`, or `source` must be provided when publishing. |
| `attachment_url`
*string* | The URL of an image to include as a photo comment. One of `attachment_id`, `attachment_share_url`, `attachment_url`, `message`, or `source` must be provided when publishing. |
| `source`
*multipart/form-data* | A photo, encoded as form data, to use as a photo comment. One of `attachment_id`, `attachment_share_url`, `attachment_url`, `message`, or `source` must be provided when publishing. |
| `message`
*string* | The comment text. One of `attachment_id`, `attachment_share_url`, `attachment_url`, `message`, or `source` must be provided when publishing.Mention other Facebook Pages in your `message` text using the following syntax: `@[page-id]` Usage of this feature is subject to review. |
### Return Type
If successful, you will receive a JSON response with the newly created comment ID. In addition, this endpoint supports read-after-write and can immediately return any fields returned by read operations.

```
{
  "id": "{comment-id}"
}
```
Updating
--------
You can't update using this edge.
Deleting
--------
You can't delete using this edge.
Delete individual comments using the /comment-id endpoint.