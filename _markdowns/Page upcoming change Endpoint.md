
Graph API Reference v19.0: Page Upcoming Change - Documentation - Meta for Developers











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
Graph API Versionv19.0Page Upcoming Change
====================

Reading
-------

Notification of page upcoming changes.


### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v19.0/{page-upcoming-change-id} HTTP/1.1
Host: graph.facebook.com
```

```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{page-upcoming-change-id}',
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
    "/{page-upcoming-change-id}",
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
    "/{page-upcoming-change-id}",
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
                               initWithGraphPath:@"/{page-upcoming-change-id}"
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



| Field | Description |
| --- | --- |
| `id`numeric string | The ID of the upcoming change
 |
| `change_type`enum | The type of the upcoming change
Default |
| `effective_time`datetime | The time when the upcoming change will become effective
Default |
| `page`Page | The associated page of this upcoming change
Default |
| `proposal`PageChangeProposal | The proposal associated with the change, only valid when change\_type is knowledge\_proposal
Default |
| `timer_status`enum | The status of the timer associated with this change
Default |

### Error Codes



| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

Creating
--------

You can't perform this operation on this endpoint.Updating
--------

You can't perform this operation on this endpoint.Deleting
--------

You can't perform this operation on this endpoint.
































