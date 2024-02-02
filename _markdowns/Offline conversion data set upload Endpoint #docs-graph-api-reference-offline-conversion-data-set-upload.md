
Graph API Reference v19.0: Offline Conversion Data Set Upload - Documentation - Meta for Developers











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
Graph API Versionv19.0Offline Conversion Data Set Upload
==================================

Reading
-------

A subset of Offline Event Data Set


### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v19.0/{offline-conversion-data-set-upload-id} HTTP/1.1
Host: graph.facebook.com
```

```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{offline-conversion-data-set-upload-id}',
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
    "/{offline-conversion-data-set-upload-id}",
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
    "/{offline-conversion-data-set-upload-id}",
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
                               initWithGraphPath:@"/{offline-conversion-data-set-upload-id}"
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
| `id`numeric string | ID of the data set upload
Default |
| `api_calls`int32 | Api calls stat from RTCS
 |
| `creation_time`int32 | Time of the creation of this upload tag
 |
| `duplicate_entries`int32 | Duplicate entries stat
 |
| `event_stats`string | Event stats
 |
| `event_time_max`integer | Latest entry timestamp
 |
| `event_time_min`integer | First entry timestamp
 |
| `first_upload_time`int32 | Time of the first upload to this upload tag
 |
| `is_excluded_for_lift`bool | The flag to determine if the upload data should be excluded from Lift
Default |
| `last_upload_time`int32 | Time of the most recent upload to this upload tag
 |
| `match_rate_approx`int32 | Approximate match rate percentage for the entries in this upload
 |
| `matched_entries`int32 | Matched entries stat
 |
| `upload_tag`string | The name by which uploads are grouped in this data set
Default |
| `valid_entries`int32 | Valid entries stat
 |

### Edges



| Edge | Description |
| --- | --- |
| `progress` | Upload progress, returns a list of progress ranges that were previously uploaded
 |
| `pull_sessions` | pull\_sessions
 |

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
































