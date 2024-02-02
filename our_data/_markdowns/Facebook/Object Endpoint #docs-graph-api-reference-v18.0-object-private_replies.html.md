Object Private Replies - Graph API - Documentation - Meta for Developers

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
This document refers to an outdated version of Graph API. Please use the latest version.Graph API Versionv18.0`/{object-id}/private_replies`
==============================
#### Legacy Private Replies are deprecated for v5.0+

On October 29, 2019 we announced that this endpoint is now deprecated. Please use the new Private Replies

As part of the V3.3 changes the `read_page_mailboxes` permission was deprecated. Use `pages_messaging` permission to access this endpoint.
The `read_page_mailboxes` permission will stop working after June 30 2020

This edge is the **Legacy Private Replies** allows Pages to reply to Post Comments and Visitor Posts with a plain text only message. It can be used with the following nodes:

* `Comment`
* `Post`
Please note that a comment or post may only be replied to once.
Reading
-------
You can't read using this edge.
Publishing
----------
To reply with a private Message:
HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK
```
POST /v19.0/{object-id}/private_replies HTTP/1.1
Host: graph.facebook.com
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->post(
    '/{object-id}/private_replies',
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
    "/{object-id}/private_replies",
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
    "/{object-id}/private_replies",
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
                               initWithGraphPath:@"/{object-id}/private_replies"
                                      parameters:params
                                      HTTPMethod:@"POST"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
Private replies to posts or comments are allowed within 7 days of the creation date of the user post or comment.
Permissions
-----------

This edge requires a Page access token with the following permissions:

* `pages_messaging`

Apps with Standard Access can only send and receive messages from people who have a role on your app. Additionally Pages in `unpublished` status will only be allowed to message people with a role on the Page.

### Fields

Parameter
 | 
Description
 | 
Type
 || `id` | The ID of the Page Comment or Visitor Post that you are replying to. | `string` |
| `message` | The text of the reply. **This field is required**. | `string` |
### Response
If successful, you will receive a response with the following fields. In addition, this endpoint supports read-after-write and can immediately read the node represented by `id` in the return type.

Field
 | 
Description
 | 
Type
 || id | The ID of the newly created Message. | `string` |
Deleting
--------
You can't delete using this edge.
Updating
--------
You can't update using this edge.