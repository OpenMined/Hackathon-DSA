Resumable Upload API - Graph API - Documentation - Meta for Developers

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
Resumable Upload API
====================

The Resumable Upload API allows you to upload large files to the Graph API and resume interrupted upload sessions without having to start over. Once uploaded, you can use an uploaded file's handle with other Graph API endpoints that support them.

Note that the Resumable Upload API is not the only way to upload files. Many nodes have an edge that supports uploading, but most do not have a way to handle large files or a way to resume an interrupted upload session.

References for endpoints that support uploaded file handles will indicate if the endpoints support handles returned by the Resumable Upload API.

Upload Steps
------------

Uploading a file is a two step process:

1. Use the Application Uploads endpoint to describe your file and create an upload session.
2. Use the returned upload session ID to initiate the upload process.

If successful, a file handle will be returned which you can then use with other endpoints that support file handles returned by the Resumable Upload API.

### Step 1: Create a Session

Send a `POST` request that describes your file to the Application Uploads endpoint (`{app-id}/uploads`) . Upon success an upload session ID will be returned that you can use in the next step to initiate the upload.

#### Request Syntax

```
POST https://graph.facebook.com/{api-version}/{app-id}/uploads
  &file_length={file-length}
  &file_type={file-type}
  &access_token={access-token}
```
Parameters Placeholders:

* `{api-version}` — The Graph API version.
* `{app-id}` — The application ID. The uploaded file that will be associated with this app. The app user must have an administrator or developer role on this app.
* `file-length` — The file's size, in bytes.
* `file-type` — The file's MIME type. Valid values are: `application/pdf`, `image/jpeg`, `image/jpg`, `image/png`, and `video/mp4`
* `{access-token}` — The app user's User Access Token.

Refer to the Application Uploads endpoint reference for a complete list of available query parameters and supported file types.

#### Response

```
{
  "id": "{id}"
}
```
Response property values:

* `{id}` — Upload session ID.

#### Sample Request

```
curl -X POST \
 "https://graph.facebook.com/v19.0/584544743160774/uploads?file_length=109981&file_type=image/png&access_token=EAAIT..."
```
#### Sample Response

```
{
    "id": "upload:MTphd..."
}
```
### Step 2: Initiate Upload

Initiate the upload session by sending a `POST` request to Graph API host address and append your upload session `{id}` along with the required headers indicated below. Upon success, a file handle, `{h}`, is returned that you can then use with any Graph API endpoints that support file handles returned by the Resumable Upload API.

If the upload session is taking longer than expected or has been interrupted, follow the steps described in the Interruptions section.

#### Request Syntax

```
POST https://graph.facebook.com/{api-version}/{upload-session-id}
  --header 'Authorization: OAuth {access-token}' 
  --header 'file_offset: 0'
  --data-binary @{file-name}
```
**Placeholder Values**

* `{api-version}` — Graph API version.
* `{upload-session-id}` — Upload session ID returned in step 1.
* `{access-token}` — App user's User Access Token. The app user must have a role on the app that was targeted in step 1.
* `{file-name}` — Name of the file to upload.

You must include the access token in the header or your request will fail.

#### Response

```
{
  "h": "{h}"
}
```
Response property values:

* `{h}` — The uploaded file's file handle

#### Sample Request

```
curl -X POST \
 "https://graph.facebook.com/v19.0/upload:MTphd..." \
 --header "Authorization: OAuth EAAIT..." \
 --header "file_offset: 0" \
 --data-binary @cats_are_jerks.png
```
#### Sample Response

```
{
    "h": "2:c2FtcGxl..."
}
```
Interruptions
-------------

If you have initiated an upload session but it is taking longer than expected or has been interrupted, send a `GET` request to Graph API host address and append your upload session ID. The API returns a `file_offset` value that you can use to resume the upload process from the point of interruption.

### Request Syntax

```
GET https://graph.facebook.com/{api-version}/{upload-session-id}
  ?access_token={access-token}
```
Placeholder values:

* `{api-version}` — Graph API version.
* `{upload-session-id}` — Upload session ID returned in Step 1: Create a Session.
* `{access-token}` — App user's User Access Token.

### Response

```
{
  "id": "{id}",
  "file_offset": {file-offset}
}
```
Response property values:

* `{id}` — The upload session ID that was queried.
* `{file-offset}` — An integer that indicates the number of bytes that have been successfully uploaded.

Capture the `file_offset` value and repeat Step 2: Initiate Upload, assigning the value to the corresponding `file_offset` header. This will resume the upload process from the point of interruption.

### Sample Request

```
curl -X GET \
 "https://graph.facebook.com/v19.0/upload:MTphd...&access_token=EAAIT..." \
```
### Sample Response

```
{
  "id": "upload:MTphd",
  "file_offset": 5238
}
```