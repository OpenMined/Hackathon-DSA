Graph API Reference v19.0: Album - Documentation - Meta for Developers

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
Graph API Versionv19.0Album
=====
Represents an Album.

Reading
-------
Get Fields and Edges on an Album.

### Requirements

Requirements depend on the type of node that the Album is on.

 Requirement | User nodes | Page nodes | Group nodes || Access Tokens | Any
 | Any
 | User
 |
| Features | None
 | To get public Page content of Pages you can not perform a task on, you will need `Page Public Content Access` | None
 |
| Permissions | `user_photos` | Unpublished Pages:* You must be able to perform the `CREATE` task on the Page
* `pages_read_engagement`
Published Pages:* `pages_read_engagement`
 | None |
| Group Roles | Not applicable | Not applicable | Admin |
### Requirements

Requirements depend on the type of node that the Album is on.

 Requirement | User nodes | Page nodes | Group nodes || Access Tokens | Any
 | Any
 | User
 |
| Features | None
 | To get public Page content of Pages you can not perform a task on, you will need `Page Public Content Access` | None
 |
| Permissions | `user_photos` | Unpublished Pages:* You must be able to perform the `CREATE` task on the Page
* `pages_read_engagement`
Published Pages:* `pages_read_engagement`
 | None |
| Group Roles | Not applicable | Not applicable | Admin |
### Example
HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v19.0/{album-id} HTTP/1.1
Host: graph.facebook.com
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{album-id}',
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
    "/{album-id}",
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
    "/{album-id}",
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
                               initWithGraphPath:@"/{album-id}"
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
| `id`numeric string | The Album ID.
 |
| `backdated_time`datetime | A user-specified time for when this object was created
 |
| `backdated_time_granularity`enum | How accurate the backdated time is
 |
| `can_upload`bool | Whether the app user can upload photos to this Album
 |
| `count`unsigned int32 | The approximate number of Photos and Videos in the Album.
 |
| `cover_photo`Photo | Album cover photo id
 |
| `created_time`datetime | The Album creation date and time.
Default |
| `description`string | The Album description.
 |
| `event`Event | If this object has a place, the event associated with the place
 |
| `from`User|Page | The User who created the Album.
 |
| `link`token with structure: URL | A link to this Album on Facebook.
 |
| `location`string | The Album textual location.
 |
| `name`string | The Album title.
Default |
| `place`Place | Place info
 |
| `privacy`string | The Album privacy settings.
 |
| `type`string | The Album type: album, app, cover, profile, mobile, normal, or wall
 |
| `updated_time`datetime | The date and time the Album was last updated.
 |
### Edges

| Edge | Description |
| --- | --- |
| `comments` | Represents a collection of Comments on the Album.
 |
| `likes` | A collection of Profiles who like the Album.
 |
| `photos` | A collection of Photos in the Album
 |
| `picture` | A link to the Album cover photo.
 |
### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 80001 | There have been too many calls to this Page account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |
| 100 | Invalid parameter |
Creating
--------
You can make a POST request to `albums` edge from the following paths: * `/{group_id}/albums`
When posting to this edge, an Album will be created.### Parameters

| Parameter | Description |
| --- | --- |
| `contributors`list<int> | Contributors to turn this into a shared album
 |
| `description`UTF-8 string | Deprecated. Use the message param
DeprecatedSupports Emoji |
| `is_default`boolean | Default value: `false``true` indicates that the request will create the application specific album
 |
| `location`string | A text location of the Album for non-page locations
 |
| `make_shared_album`boolean | Default value: `false`Ensures the created Album is a shared Album
 |
| `message`string | The Album's caption. This appears below the title of the album in the Album view
 |
| `name`UTF-8 string | The title of the Album
Supports Emoji |
| `place`place tag | The ID of a location page to tag the Album with
 |
| `privacy`Privacy Parameter | The privacy of the Album
 |
| `tags`list<int> | Deprecated
Deprecated |
| `visible`string | Deprecated. Use privacy
Deprecated |
### Return Type
This endpoint supports read-after-write and will read the node represented by `id` in the return type. Struct {`id`: numeric string, }### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 200 | Permissions error |
| 190 | Invalid OAuth 2.0 Access Token |
Updating
--------
You can't perform this operation on this endpoint.Deleting
--------
You can't perform this operation on this endpoint.