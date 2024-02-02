Graph API Reference v19.0: Application Accounts - Documentation - Meta for Developers

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
Graph API Versionv19.0Application Accounts
====================
Represents a collection of test users on an app.

Reading
-------
Get a list of test users on an app.

### Requirements

 Type | Requirement || Access Tokens | App |
| Permissions | None |
### Example
HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v19.0/{application-id}/accounts HTTP/1.1
Host: graph.facebook.com
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{application-id}/accounts',
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
    "/{application-id}/accounts",
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
    "/{application-id}/accounts",
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
                               initWithGraphPath:@"/{application-id}/accounts"
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
| `type`enum{test-users} | The type of user requested
 |
### Fields
Reading from this edge will return a JSON formatted result:

```
{
 "`data`": [],
 "`paging`": {}
}

```
#### `data`
A list of TestAccount nodes.The following fields will be added to each node that is returned:

| Field | Description |
| --- | --- |
| `access_token`string | An access token that can be used to make API calls on behalf of this user
Default |
#### `paging`
For more details about pagination, see the Graph API guide.### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |
Creating
--------
You can make a POST request to `accounts` edge from the following paths: * `/{application_id}/accounts`
When posting to this edge, a TestAccount will be created.  
Upon successful creation, a `login_url` and `access_token` will be returned. You can use the login URL to log in as the test user. Login URLs expire once they are used, or after one hour if they are unused. An access token will only be returned if the `installed` parameter was set to `true` at the time of the query.

You can also use this edge to associate an existing test user with a different app by using the `owner_acces_token` parameter.

### Requirements

 Type | Requirement || Access Tokens | App |
| Permissions | None |
### Parameters

| Parameter | Description |
| --- | --- |
| `installed`boolean | Automatically installs the app for the test user once it is created or associated
 |
| `minor`boolean | Is this test user a minor
 |
| `name`string | The name for the test user. When left blank, a random name will be automatically generated
 |
| `owner_access_token`string | When associating existing test users with other apps, this is the app access token of any app that is already associated with the test user. The `{app-id}` in the publishing request in this case should be the app that will is the target to associate with the test user. The API request should also be signed with the app access token of that target app. Required when associating test users, but should not be used when creating new test users
 |
| `permissions`List<Permission> | Default value: `Set`List of permissions that are automatically granted for the app when it is created or associated
 |
| `type`enum{test-users} | Type
 |
| `uid`int | ID of an existing test user to associate with another app. Required when associating test users, but should not be used when creating new test users
 |
### Return Type
This endpoint supports read-after-write and will read the node represented by `id` in the return type. Struct {`id`: numeric string, `access_token`: string, `login_url`: string, `email`: string, `password`: string, }### Error Codes

| Error | Description |
| --- | --- |
| 2900 | Too many test accounts |
Updating
--------
You can't perform this operation on this endpoint.Deleting
--------
You can dissociate a TestAccount from an Application by making a DELETE request to `/{application_id}/accounts`.### Requirements

 Type | Requirement || Access Tokens | App |
| Permissions | None |
### Limitations

At least one test user must be associated with an app. Attempting to perform this operation on an app's sole test user will result in error code `2902`.

### Parameters

| Parameter | Description |
| --- | --- |
| `type`enum {TEST\_USERS} | Account type
 |
| `uid`UID | Account UID
Required |
### Return Type
 Struct {`success`: bool, }### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 2902 | Cannot remove test account from this app |