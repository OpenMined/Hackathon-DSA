Graph API User Accounts - Documentation - Meta for Developers

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
Graph API Versionv19.0User Accounts
=============
The Facebook Pages that a person owns or is able to perform tasks on.
Reading
-------
Pages the User has a role on

### Permissions
A Page access token for a User with a role (other than Live Contributor) on the Page and the following permissions:
* The `pages_show_list` permission
* To access accounts using a `business_id` or for a user who owns any business Pages, the app must be approved for the `business_management` permission.
**Note:** In order for a Page to be returned, the User must also grant the app running the query the `pages_show_list` permissions for that Page.
### Limitations
* **It does not return pages that you are connected with through a business. To retrieve pages that you are connected with via businesses, the  `business_management` permission is required**
### New Page Experience
This endpoint is supported for New Page Experience.### Example
HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKcURLGraph API Explorer
```
GET /v19.0/{user-id}/accounts HTTP/1.1
Host: graph.facebook.com
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{user-id}/accounts',
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
    "/{user-id}/accounts",
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
    "/{user-id}/accounts",
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
                               initWithGraphPath:@"/{user-id}/accounts"
                                      parameters:params
                                      HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
```
curl -X GET -G \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v19.0/{user-id}/accounts
```
If you want to learn how to use the Graph API, read our Using Graph API guide.### Parameters

| Parameter | Description |
| --- | --- |
| `is_place`boolean | If specified,filter pages based on whetherthey are places or not
 |
| `is_promotable`boolean | If specified, filter pages based on whether they can be promoted or not
 |
### Fields
Reading from this edge will return a JSON formatted result:

```
{
 "`data`": [],
 "`paging`": {},
 "`summary`": {}
}

```
#### `data`
A list of Page nodes.The following fields will be added to each node that is returned:

| Field | Description |
| --- | --- |
| `tasks`list<enum> | The User's tasks assigned to the Page.
Default |
#### `paging`
For more details about pagination, see the Graph API guide.#### `summary`
Aggregated information about the edge, such as counts. Specify the fields to fetch in the summary param (like `summary=total_count`).

| Field | Description |
| --- | --- |
| `total_count`int32 | Total number of objects on this edge
Default |
### Error Codes

| Error | Description |
| --- | --- |
| 459 | The session is invalid because the user has been checkpointed |
| 190 | Invalid OAuth 2.0 Access Token |
| 200 | Permissions error |
| 100 | Invalid parameter |
| 80001 | There have been too many calls to this Page account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |
| 80002 | There have been too many calls to this Instagram account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |
| 110 | Invalid user id |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 210 | User not visible |
Creating
--------
This API lets you create Facebook pages.
### Permissions
* A User access token with `pages_manage_metadata`  and `pages_show_list` permissions.
* The `category_enum` parameter with a Page Category.
* Other requirements vary depending on the type of page you are creating but may require the following parameters: `name`, `about`, `picture`, and `cover_photo`.
**Note:** When setting the locale, at least one, `city_id`, `location`, or `coordinates`, is required. Caveats:
* `city_id` and `location` can not be used together
* `city_id` and `coordinates` can be used together however the coordinates must be within the city selected
* `location` and `coordinates` can be used together however the coordinates must be within the location selected
### Limitations
* You can only create a Page as a test user or if your app has been allowlisted by your Facebook representative.

---
You can make a POST request to `accounts` edge from the following paths: * `/{user_id}/accounts`
When posting to this edge, no Graph object will be created.### Parameters

| Parameter | Description |
| --- | --- |
| `about`UTF-8 encoded string | Short description
 |
| `address`UTF-8 encoded string | Address
 |
| `category_enum`string | Page category (enum). See Pages Categories API docs.
 |
| `category_list`list<numeric string> | List of categories
 |
| `city_id`city id | City ID
 |
| `coordinates`JSON-encoded coordinate list | Coordinates
 |
| `cover_photo`Object | Cover photo
 |
| `url`URL | Required |
| `offset_y`integer | Default value: `50` |
| `offset_x`integer | Default value: `50` |
| `focus_y`float |  |
| `focus_x`float |  |
| `zoom_scale_x`float |  |
| `zoom_scale_y`float |  |
| `no_feed_story`boolean | Default value: `false` |
| `no_notification`boolean | Default value: `false` |
| `description`UTF-8 encoded string | Description
 |
| `ignore_coordinate_warnings`boolean | If ignore warnings generated in coordination validation (bool)
 |
| `location`Object | This defines the location for this page. This is required if `location_page_id` is not specified, or if the Page referenced by the `location_page_id` doesn't have a valid value for the field. The dictionary must include the keys either `city_id` or all of `city`, `state`, and `country` (but `state` is optional if the address is not in the U.S.).
 |
| `city`string |  |
| `state`string |  |
| `country`string |  |
| `name`UTF-8 encoded string | Page name
Required |
| `phone`UTF-8 encoded string | Phone
 |
| `picture`URL | Profile picture
 |
| `website`URL | Website
 |
| `zip`string | Zipcode
 |
### Return Type
This endpoint supports read-after-write and will read the node represented by `id` in the return type. Struct {`id`: numeric string, }### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 152 | Invalid page type |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 190 | Invalid OAuth 2.0 Access Token |
| 3950 | The system creation is throttled. |
Updating
--------
You can't perform this operation on this endpoint.Deleting
--------
You can't perform this operation on this endpoint.