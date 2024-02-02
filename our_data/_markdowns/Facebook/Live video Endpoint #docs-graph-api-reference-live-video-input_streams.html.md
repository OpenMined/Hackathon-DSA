Graph API Reference v19.0: Live Video Input Streams - Documentation - Meta for Developers

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
Graph API Versionv19.0Live Video Input Streams
========================
Reading
-------
You can't perform this operation on this endpoint.Creating
--------
You can make a POST request to `input_streams` edge from the following paths: * `/{live_video_id}/input_streams`
When posting to this edge, a LiveVideoInputStream will be created.### Parameters
This endpoint doesn't have any parameters.### Return Type
This endpoint supports read-after-write and will read the node represented by `id` in the return type. Struct {`id`: numeric string, }### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
Updating
--------
You can't perform this operation on this endpoint.Deleting
--------
You can't perform this operation on this endpoint.