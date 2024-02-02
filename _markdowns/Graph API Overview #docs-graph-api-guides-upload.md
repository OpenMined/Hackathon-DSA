::: {._4-u3 ._588p}
Uploading a file is a two step process:

1.  Use the [Application
    Uploads](/docs/graph-api/reference/application/uploads/) endpoint to
    describe your file and create an upload session.
2.  Use the returned upload session ID to initiate the upload process.

If successful, a file handle will be returned which you can then use
with other endpoints that support file handles returned by the Resumable
Upload API.

### Step 1: Create a Session {#step-1--create-a-session}

Send a ` POST ` request that describes your file to the [Application
Uploads](/docs/graph-api/reference/application/uploads/) endpoint (
` {app-id}/uploads ` ) . Upon success an upload session ID will be
returned that you can use in the next step to initiate the upload.

#### Request Syntax

``` {._5s-8 .prettyprint .lang-http .prettyprinted}
POST https://graph.facebook.com/{api-version}/{app-id}/uploads &file_length={file-length} &file_type={file-type} &access_token={access-token}
```

Parameters Placeholders:

-   ` {api-version} ` --- The Graph API version.
-   ` {app-id} ` --- The application ID. The uploaded file that will be
    associated with this app. The app user must have an administrator or
    developer role on this app.
-   ` file-length ` --- The file\'s size, in bytes.
-   ` file-type ` --- The file\'s MIME type. Valid values are:
    ` application/pdf ` , ` image/jpeg ` , ` image/jpg ` , ` image/png `
    , and ` video/mp4 `
-   ` {access-token} ` --- The app user\'s User Access Token.

Refer to the [Application
Uploads](docs/graph-api/reference/application/uploads/) endpoint
reference for a complete list of available query parameters and
supported file types.

#### Response

``` {._5s-8 .prettyprint .lang-json .prettyprinted}
{ "id": "{id}"
}
```

Response property values:

-   ` {id} ` --- Upload session ID.

#### Sample Request

``` {._5s-8 .prettyprint .lang-curl .prettyprinted}
curl -X POST \ "https://graph.facebook.com/v18.0/584544743160774/uploads?file_length=109981&file_type=image/png&access_token=EAAIT..."
```

#### Sample Response

``` {._5s-8 .prettyprint .lang-json .prettyprinted}
{ "id": "upload:MTphd..."
}
```

### Step 2: Initiate Upload {#step-2--initiate-upload}

Initiate the upload session by sending a ` POST ` request to Graph API
host address and append your upload session ` {id} ` along with the
required headers indicated below. Upon success, a file handle, ` {h} ` ,
is returned that you can then use with any Graph API endpoints that
support file handles returned by the Resumable Upload API.

If the upload session is taking longer than expected or has been
interrupted, follow the steps described in the
[Interruptions](#interruptions) section.

#### Request Syntax

``` {._5s-8 .prettyprint .lang-http .prettyprinted}
POST https://graph.facebook.com/{api-version}/{upload-session-id} --header 'Authorization: OAuth {access-token}' --header 'file_offset: 0' --data-binary @{file-name}
```

**Placeholder Values**

-   ` {api-version} ` --- Graph API version.
-   ` {upload-session-id} ` --- Upload session ID returned in step 1.
-   ` {access-token} ` --- App user\'s User Access Token. The app user
    must have a role on the app that was targeted in step 1.
-   ` {file-name} ` --- Name of the file to upload.

You must include the access token in the header or your request will
fail.

#### Response

``` {._5s-8 .prettyprint .lang-json .prettyprinted}
{ "h": "{h}"
}
```

Response property values:

-   ` {h} ` --- The uploaded file\'s file handle

#### Sample Request

``` {._5s-8 .prettyprint .lang-curl .prettyprinted}
curl -X POST \ "https://graph.facebook.com/v18.0/upload:MTphd..." \ --header "Authorization: OAuth EAAIT..." \ --header "file_offset: 0" \ --data-binary @cats_are_jerks.png
```

#### Sample Response

``` {._5s-8 .prettyprint .lang-json .prettyprinted}
{ "h": "2:c2FtcGxl..."
}
```
:::
