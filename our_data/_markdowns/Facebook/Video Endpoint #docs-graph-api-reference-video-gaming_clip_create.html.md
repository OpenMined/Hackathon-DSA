Graph API Reference v19.0: Video Gaming Clip Create - Documentation - Meta for Developers

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
Graph API Versionv19.0Video Gaming Clip Create
========================
Reading
-------
You can't perform this operation on this endpoint.Creating
--------
You can make a POST request to `gaming_clip_create` edge from the following paths: * `/{video_id}/gaming_clip_create`
When posting to this edge, a Video will be created.### Parameters

| Parameter | Description |
| --- | --- |
| `duration_seconds`float | Default value: `60`The duration in seconds to create the clip. Should be a positive number.
 |
### Return Type
This endpoint supports read-after-write and will read the node to which you POSTed. Struct {`id`: numeric string, }### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
Updating
--------
You can't perform this operation on this endpoint.Deleting
--------
You can't perform this operation on this endpoint.