
Milestone - Graph API - Documentation - Meta for Developers












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
This document refers to an outdated version of Graph API. Please use the latest version.Graph API Versionv18.0Milestone `/{milestone-id}`
===========================

This represents a milestone on a Facebook Page.

### Related Guides

* Adding Milestones to Pages using the Graph API
Reading
-------

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v19.0/{milestone-id} HTTP/1.1
Host: graph.facebook.com
```

```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{milestone-id}',
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
    "/{milestone-id}",
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
    "/{milestone-id}",
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
                               initWithGraphPath:@"/{milestone-id}"
                                      parameters:params
                                      HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
### Permissions

To view publicly shared milestones of any Page, you will need:


* A valid app or user access token
* The Public Page Content Access feature

To view milestones of Pages you manage, you will need:


* A Page access token
* The `pages_read_engagement` permission

### Fields



 
Name
 | 
Description
 | 
Type
 || `id` | The ID of a milestone event | `string` |
| `title` | The title of the milestone | `string` |
| `from` | The Page that posted the milestone. | `Page` |
| `description` | The description of the milestone | `string` |
| `created_time` | The creation time of the milestone | `datetime` |
| `updated_time` | The update time of the milestone | `datetime` |
| `start_time` | The start time of the milestone | `datetime` |
| `end_time` | The end time of the milestone. Page milestones have the same start and end time | `datetime` |

Creating
--------

You can't perform this operation on this endpoint.


Use the `/{page-id}/milestones` endpoint to create new milestones for a Page.

Deleting
--------

### Permissions

To delete a milestone of Pages you manage, you will need:


* A Page access token
* The `pages_manage_posts` permission

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK
```
DELETE /v19.0/{milestone-id} HTTP/1.1
Host: graph.facebook.com
```

```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->delete(
    '/{milestone-id}',
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
    "/{milestone-id}",
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
    "/{milestone-id}",
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
                               initWithGraphPath:@"/{milestone-id}"
                                      parameters:params
                                      HTTPMethod:@"DELETE"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
### Fields

No fields necessary to delete.

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

### Permissions

You can't perform this operation on this endpoint.


Edges
-----



 
Name
 | 
Description
 || `/likes` | A list of the likes. |
| `/comments` | A list of the comments. |




































 
