Group - Graph API - Documentation - Meta for Developers

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
This document refers to an outdated version of Graph API. Please use the latest version.Graph API Versionv18.0Group
=====
A Facebook Group.
Reading
-------
Returns information about a single Group object. To get a list of Groups a User administers, use the `/user/groups` edge instead.
HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v19.0/{group-id} HTTP/1.1
Host: graph.facebook.com
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{group-id}',
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
    "/{group-id}",
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
    "/{group-id}",
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
                               initWithGraphPath:@"/{group-id}"
                                      parameters:params
                                      HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
### Permissions
* `groups_access_member_info` — Enables your app to receive member-related data on group content.
* `publish_to_groups` — Enables your app to post content into a group on behalf of a user.

**For Public and Closed Groups**
A User access token
**For Secret Groups**
A User access token for an Admin of the Group
**Caveats**
* Fields that return User information will not be included in any responses unless the request is made using an access token of an Admin of the Group.
### Fields

Property Name
 | 
Description
 | 
Type
 || `id` | The Group ID | `string` |
| `cover` | Information about the Group's cover photo. | `CoverPhoto` |
| `id` | ID of the Photo that represents this cover photo. | `string` |
| `source` | URL to the Photo that represents this cover photo. | `string` |
| `offset_y` | The vertical offset in pixels of the photo from the bottom. | `int` |
| `offset_x` | The horizontal offset in pixels of the photo from the left. | `int` |
| `description` | A brief description of the Group. | `string` |
| `email` | The email address to upload content to the Group. Only current members of the Group can use this. | `string` |
| `icon` | The URL for the Group's icon. | `string` |
| `member_count` | The number of members in the Group. | `int` |
| `member_request_count` | The number of pending member requests. Requires an access token of an Admin of the Group.we The count is only returned when the number of pending member requests is over 50. | `int` |
| `name` | The name of the Group. | `string` |
| `owner` | *Deprecated in v9.0+. Will be deprecated in all versions February 9, 2021.* | `User` | `Page` |
| `parent` | The parent of this Group, if it exists. | `Group` | `Page` |
| `permissions` | The permissions a User has granted for an app installed in the Group. | `string` |
| `privacy` | The privacy setting of the Group. Possible values are `CLOSED`, `OPEN`, and `SECRET`. Requires an access token of an Admin of the Group. | `string` |
| `updated_time` | The last time the Group was updated (includes changes Group properties, Posts, and Comments). Requires an access token of an Admin of the Group. | `datetime` |
Creating
--------
This operation is not supported.
Updating
--------
This operation is not supported.
Deleting
--------
This operation is not supported.
Edges
-----

Name
 | 
Description
 || `/admins` | *This edge was deprecated on April 4th, 2018.* |
| `/albums` | Photo albums owned by the Group. |
| `/docs` | Documents owned by the Group. |
| `/events` | Events owned by the Group. |
| `/feed` | Feed of Posts owned by the Group. |
| `/files` | Files owned by the Group. |
| `/live_videos` | Live Videos owned by the Group. |
| `/members` | *This edge was deprecated on April 4th, 2018.* |
| `/photos` | Photos owned by the Group. |
| `/videos` | Videos owned by the Group. |