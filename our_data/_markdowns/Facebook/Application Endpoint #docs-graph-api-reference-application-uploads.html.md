Upload Service Provisioning API - Documentation - Meta for Developers

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
Graph API Versionv19.0Application Uploads
===================
Reading
-------
You can't perform this operation on this endpoint.Creating
--------
Create an upload session.

Upload session IDs returned by this endpoint can be used to upload large files, get the status of an upload session, or resume an interrupted session. See the Resumable Upload API document for complete usage instructions.

### Requirements

 Type | Description || Access Tokens | User or System User. The app user who granted the token must have an Administrator or Developer role on the app. |
| Permissions | None. |
You can make a POST request to `uploads` edge from the following paths: * `/{application_id}/uploads`
When posting to this edge, no Graph object will be created.### Parameters

| Parameter | Description |
| --- | --- |
| `file_length`int64 | The file length in bytes
 |
| `file_name`RegexParam | The name of the file to be uploaded
 |
| `file_type`RegexParam | The MIME type of the file to be uploaded
 |
| `session_type`enum {attachment} | Default value: `attachment`The type of upload session that is being requested by the app
 |
### Return Type
 Struct {`id`: string, }### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
Updating
--------
You can't perform this operation on this endpoint.Deleting
--------
You can't perform this operation on this endpoint.