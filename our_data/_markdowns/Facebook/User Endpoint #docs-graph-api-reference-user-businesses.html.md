Graph API Reference v19.0: User Businesses - Documentation - Meta for Developers

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
Graph API Versionv19.0User Businesses
===============
Reading
-------
UserBusinesses

### Example
HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v19.0/{user-id}/businesses HTTP/1.1
Host: graph.facebook.com
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{user-id}/businesses',
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
    "/{user-id}/businesses",
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
    "/{user-id}/businesses",
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
                               initWithGraphPath:@"/{user-id}/businesses"
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
Reading from this edge will return a JSON formatted result:

```
{
 "`data`": [],
 "`paging`": {}
}

```
#### `data`
A list of Business nodes.The following fields will be added to each node that is returned:

| Field | Description |
| --- | --- |
| `permitted_roles`list<string> | Roles the user has on the business
 |
#### `paging`
For more details about pagination, see the Graph API guide.### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 110 | Invalid user id |
| 190 | Invalid OAuth 2.0 Access Token |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
Creating
--------
You can make a POST request to `businesses` edge from the following paths: * `/{user_id}/businesses`
When posting to this edge, a Business will be created.### Parameters

| Parameter | Description |
| --- | --- |
| `child_business_external_id`string | child\_business\_external\_id
 |
| `email`string | The business email of the business admin
 |
| `name`string | Username
Required |
| `primary_page`page ID | Primary Page ID
 |
| `sales_rep_email`string | Sales Rep email address
 |
| `survey_business_type`enum {AGENCY, ADVERTISER, APP\_DEVELOPER, PUBLISHER} | Business Type
 |
| `survey_num_assets`int64 | Number of Assets in the business
 |
| `survey_num_people`int64 | Number of People that will work on the business
 |
| `timezone_id`int64 | Timezone ID
 |
| `vertical`enum {NOT\_SET, ADVERTISING, AUTOMOTIVE, CONSUMER\_PACKAGED\_GOODS, ECOMMERCE, EDUCATION, ENERGY\_AND\_UTILITIES, ENTERTAINMENT\_AND\_MEDIA, FINANCIAL\_SERVICES, GAMING, GOVERNMENT\_AND\_POLITICS, MARKETING, ORGANIZATIONS\_AND\_ASSOCIATIONS, PROFESSIONAL\_SERVICES, RETAIL, TECHNOLOGY, TELECOM, TRAVEL, NON\_PROFIT, RESTAURANT, HEALTH, LUXURY, OTHER} | Vertical ID
Required |
### Return Type
This endpoint supports read-after-write and will read the node represented by `id` in the return type. Struct {`id`: numeric string, }### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 42000 | This Page can't be added because it's already linked to an Instagram business profile. To add this Page to Business Manager, go to Instagram and convert to a personal account or change the Page linked to your business profile. |
| 3918 | The Facebook Page you've tried to add is already owned by another Business Manager. You can still request access to this Page, but your request will need to be approved by the Business Manager that owns it. |
| 3974 | The name you chose for this Business Manager is not valid. Try a different name. |
| 3947 | You are trying to create a Business Manager with the same name as one you are already a part of. Please pick a different name. |
| 3913 | It doesn't look like you have permission to create a new Business Manager. |
| 3912 | There was a technical issue and the changes you made to your Business Manager weren't saved. Please try again. |
| 3973 | The name you chose for this Business Manager is not valid. Please choose another. |
| 3998 | You must be an admin of the primary Page to create a business using that page. |
Updating
--------
You can't perform this operation on this endpoint.Deleting
--------
You can dissociate a Business from a User by making a DELETE request to `/{user_id}/businesses`.### Parameters

| Parameter | Description |
| --- | --- |
| `business`numeric string or integer | Business ID
 |
### Return Type
 Struct {`success`: bool, }### Error Codes

| Error | Description |
| --- | --- |
| 3914 | It looks like you're trying to remove the last admin from this Business Manager. At least one admin is required in Business Manager. |
| 100 | Invalid parameter |
| 190 | Invalid OAuth 2.0 Access Token |