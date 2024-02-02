
Group Doc - Graph API - Documentation - Meta for Developers












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
This document refers to an outdated version of Graph API. Please use the latest version.Graph API Versionv18.0Group Doc `/{group-doc-id}`
===========================

Represents a doc within a Facebook group. The `/{group-doc-id}` node returns a single doc.

Reading
-------

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v19.0/{group-doc-id} HTTP/1.1
Host: graph.facebook.com
```

```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{group-doc-id}',
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
    "/{group-doc-id}",
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
    "/{group-doc-id}",
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
                               initWithGraphPath:@"/{group-doc-id}"
                                      parameters:params
                                      HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
### Permissions

* Any valid access token if the group is public (i.e. the group's privacy setting is `OPEN`)

### Fields



 
Property Name
 | 
Description
 | 
Type
 || `id` | The group doc ID. | `string` |
| `from` | The profile that created this doc. | `User``|``Page` |
| `subject` | The title of the doc. | `string` |
| `message` | The body of the doc. This string will contain HTML for any formatting in the doc, and will be HTML encoded. | `string` |
| `icon` | The URL for the doc's icon | `string` |
| `created_time` | When the doc was created. | `datetime` |
| `updated_time` | The last time the doc was changed. | `datetime` |
| `revision` | An ID representing the current doc revision. | `int` |
| `can_edit` | Whether the session user can edit this doc. | `boolean` |
| `can_delete` | Whether the session user can delete this doc (on Facebook.com). | `boolean` |
| `embedded_urls` | URLs for document embeds | `[string]` |

Publishing
----------

You cannot create docs via the Graph API.

Deleting
--------

You cannot delete docs via the Graph API.

Updating
--------

You cannot update docs via the Graph API.




































 
