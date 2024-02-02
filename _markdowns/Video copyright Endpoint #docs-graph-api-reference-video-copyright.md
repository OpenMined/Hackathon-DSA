
Graph API Reference v19.0: Video Copyright - Documentation - Meta for Developers











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
Graph API Versionv19.0Video Copyright
===============

Reading
-------

A video copyright


### New Page Experience

This endpoint is supported for New Page Experience.### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v19.0/{video-copyright-id} HTTP/1.1
Host: graph.facebook.com
```

```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{video-copyright-id}',
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
    "/{video-copyright-id}",
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
    "/{video-copyright-id}",
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
                               initWithGraphPath:@"/{video-copyright-id}"
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
| `id`numeric string | The video copyright ID
Default |
| `content_category`enum | The content category of the reference file.
Default |
| `copyright_content_id`numeric string | The copyright content ID
Default |
| `creator`User | The account that created the copyright
Default |
| `excluded_ownership_segments`list<VideoCopyrightSegment> | The list of audio and video segments excluded from copyright monitoring. This includes both self-defined excluded segments as well as system generated excluded segments.
 |
| `in_conflict`bool | Whether the video copyright is in active conflict with another rights owner's video copyright.
Default |
| `monitoring_status`enum | Whether the video is monitored successfully for copyright. The status could be NOT\_EXAMINED, COPYRIGHTED, and ERROR.
Default |
| `monitoring_type`enum | Whether the video is monitored for VIDEO, AUDIO, or VIDEO\_AND\_AUDIO
Default |
| `ownership_countries`VideoCopyrightGeoGate | Two string arrays of ISO 3166 format country codes. `included_countries` are where the owner owns the rights to the content. `excluded_countries` are where the owner does not own the rights to the content. When both lists are empty, rights ownership is worldwide.
Default |
| `reference_file`CopyrightReferenceContainer | The reference file
Default |
| `reference_file_disabled`bool | Whether the reference file is disabled.
Default |
| `reference_file_disabled_by_ops`bool | Whether the reference file has been disabled by ops.
Default |
| `reference_owner_id`string | The ID of the reference video owner
Default |
| `rule_ids`list<VideoCopyrightRule> | A list of matching rules applied to the copyrighted content
Default |
| `tags`list<string> | The tags/keywords associated with the copyright
 |
| `whitelisted_ids`list<numeric string> | A list of page IDs or user IDs, who are allowed to use the copyrighted content.
Default |

### Edges



| Edge | Description |
| --- | --- |
| `update_records` | Update records of the copyright
 |

### Error Codes



| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

Creating
--------

You can't perform this operation on this endpoint.Updating
--------

You can update a VideoCopyright by making a POST request to `/{video_copyright_id}`.### Parameters



| Parameter | Description |
| --- | --- |
| `append_excluded_ownership_segments`boolean | If true, append the excluded ownership segments instead of replacing them
 |
| `attribution_id`numeric string or integer | The ID of the attribution to be displayed for valid monitored videos matching this content.
 |
| `content_category`enum {episode, movie, web} | The content category of the copyrighted reference file.
 |
| `excluded_ownership_countries`list<UTF-8 encoded string> | A string array of ISO 3166 format country codes, where the owner does not own the rights to the content
 |
| `excluded_ownership_segments`list<Video Match Segment> | An array of match segments to exclude from the matching algorithm. System generated excluded segments may not be replaced.
 |
| `start_time_in_sec`float | Required |
| `media_type`enum {VIDEO\_AND\_AUDIO, VIDEO\_ONLY, AUDIO\_ONLY} | Required |
| `duration_in_sec`float | Required |
| `segment_source`enum {PUBLISHER\_DEFINED, PAUSE\_LIVE\_MONITORING, LABEL\_MUTED, PUBLISHER\_MUTED, MUSIC\_RESTRICTION\_MUTED\_STILL\_VIDEO, MUSIC\_RESTRICTION\_MUTED\_MULTI\_TRACK, AUDIO\_LIBRARY\_USAGE, MELODY, INELIGIBLE\_CONTENT} | Default value: `PUBLISHER_DEFINED` |
| `is_reference_disabled`boolean | If true, stop creating matches for the reference file.
 |
| `monitoring_type`enum {VIDEO\_AND\_AUDIO, VIDEO\_ONLY, AUDIO\_ONLY} | Setting to indicate whether the content has copyright ownership on video, audio, or both.
 |
| `ownership_countries`list<UTF-8 encoded string> | A string array of ISO 3166 format country codes, where the owner owns the rights to the content
 |
| `rule_id`numeric string or integer | A copyright policy to be applied to the copyrighted content.
 |
| `whitelisted_ids`list<numeric string> | A list of page IDs or user IDs, who are allowed to use the copyrighted content.
 |
| `whitelisted_ig_user_ids`list<numeric string> | A list of Instagram user IDs who are allowed to use the copyrighted content.
 |

### Return Type

This endpoint supports read-after-write and will read the node to which you POSTed. Struct {`success`: bool, }### Error Codes



| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

Deleting
--------

You can't perform this operation on this endpoint.
































