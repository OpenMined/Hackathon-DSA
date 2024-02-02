Graph API Reference v19.0: Whats App Business Account Assigned Users - Documentation - Meta for Developers

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
Graph API Versionv19.0Whats App Business Account Assigned Users
=========================================
Represents users assigned to a specific WhatsApp Business Account (WABA).  

 To find the ID of a WhatsApp Business Account, go to **Business Manager** > **Business Settings** > **Accounts** > **WhatsApp Business Accounts**. Find the account you want to use and click on it. A panel opens, with information about the account, including the ID.
Reading
-------
Returns the WhatsApp Business Account's assigned users.

### Example

Requirements

* whatsapp\_business\_management permission
* whatsapp\_business\_messaging permission
* public\_profile permission
* BUSINESS ID (also referred to as BUSINESS MANAGER ID in Business Settings)
* WhatsApp Business Account (WABA) ID
* USER ACCESS TOKEN

Request

cURLAndroid SDKObjective-C
```
curl -i -X GET \
 "https://graph.facebook.com/LATEST-VERSION/WHATSAPP-BUSINESS-ACCOUNT-ID/assigned_users?
        business=BUSINESS-ID&
        access_token=USER-ACCESS-TOKEN"
```
```
GraphRequest request = GraphRequest.newGraphPathRequest(
  accessToken,
  "/WHATSAPP-BUSINESS-ACCOUNT-ID/assigned_users",
  new GraphRequest.Callback() {
    @Override
    public void onCompleted(GraphResponse response) {
      // Insert your code here
    }
});
Bundle parameters = new Bundle();
parameters.putString("business", "BUSINESS-ID");
request.setParameters(parameters);
request.executeAsync();
```
```
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
    initWithGraphPath:@"/WHATSAPP-BUSINESS-ACCOUNT-ID/assigned_users"
           parameters:@{ @"business": @"BUSINESS-ID",}
           HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection, id result, NSError *error) {
    // Insert your code here
}];
```
Response

```
{
  "data": [
    {
      "id": "ASSIGNED-USER-ID",
      "name": " ",
      "tasks": [
        "MANAGE"
      ]
    }
  ],
  "paging": {
    "cursors": {
      "before": "BEFORE-CURSOR",
      "after": "AFTER-CURSOR"
    }
  }
}
```
### Parameters

| Parameter | Description |
| --- | --- |
| `business`business id ID | business
Required |
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
A list of AssignedUser nodes.The following fields will be added to each node that is returned:

| Field | Description |
| --- | --- |
| `tasks`list<string> | Tasks the user has on the WABA
Default |
#### `paging`
For more details about pagination, see the Graph API guide.#### `summary`
Aggregated information about the edge, such as counts. Specify the fields to fetch in the summary param (like `summary=total_count`).

| Field | Description |
| --- | --- |
| `total_count`unsigned int32 | Total count
 |
### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
Creating
--------
You can't perform this operation on this endpoint.Updating
--------
You can update a WhatsAppBusinessAccount by making a POST request to `/{whats_app_business_account_id}/assigned_users`.### Parameters

| Parameter | Description |
| --- | --- |
| `tasks`array<enum {MANAGE, DEVELOP, MANAGE\_TEMPLATES, MANAGE\_PHONE, VIEW\_COST, MANAGE\_EXTENSIONS, VIEW\_PHONE\_ASSETS, MANAGE\_PHONE\_ASSETS, VIEW\_TEMPLATES}> | Permissions on WhatsApp Business Account
Required |
| `user`UID | Business user ID
Required |
### Return Type
This endpoint supports read-after-write and will read the node to which you POSTed. Struct {`success`: bool, }### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
Deleting
--------
You can dissociate a WhatsAppBusinessAccount from a WhatsAppBusinessAccount by making a DELETE request to `/{whats_app_business_account_id}/assigned_users`.### Parameters

| Parameter | Description |
| --- | --- |
| `user`UID | Business user ID
Required |
### Return Type
 Struct {`success`: bool, }### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |