Graph API Reference v19.0: Application Assets - Documentation - Meta for Developers

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
Graph API Versionv19.0Application Assets
==================
Reading
-------
You can't perform this operation on this endpoint.Creating
--------
You can make a POST request to `assets` edge from the following paths: * `/{application_id}/assets`
When posting to this edge, no Graph object will be created.### Parameters

| Parameter | Description |
| --- | --- |
| `asset`file | The asset file to upload
Required |
| `comment`string | Optional comment describing the asset
 |
| `type`string | Type of the asset, e.g. SWF, JS, BUNDLE, UNITY\_WEBGL, GAMES\_DESKTOP, PRIVACY\_POLICY, TOS
Required |
### Return Type
This endpoint supports read-after-write and will read the node to which you POSTed. Struct {`success`: bool, }### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
Updating
--------
You can't perform this operation on this endpoint.Deleting
--------
You can't perform this operation on this endpoint.