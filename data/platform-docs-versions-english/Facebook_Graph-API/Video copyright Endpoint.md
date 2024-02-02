Video Copyright
===============

Reading
-------

A video copyright

### New Page Experience

This endpoint is supported for [New Page Experience](https://developers.facebook.com/docs/pages/new-pages-experience/).

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bvideo-copyright-id%7D&version=v19.0)

    GET /v19.0/{video-copyright-id} HTTP/1.1
    Host: graph.facebook.com

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

    /* make the API call */
    FB.api(
        "/{video-copyright-id}",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

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

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

This endpoint doesn't have any parameters.

### Fields

| Field | Description |
| --- | --- |
| `id`<br><br>numeric string | The video copyright ID<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `content_category`<br><br>enum | The content category of the reference file.<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `copyright_content_id`<br><br>numeric string | The copyright content ID<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `creator`<br><br>[User](https://developers.facebook.com/docs/graph-api/reference/user/) | The account that created the copyright<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `excluded_ownership_segments`<br><br>list<VideoCopyrightSegment> | The list of audio and video segments excluded from copyright monitoring. This includes both self-defined excluded segments as well as system generated excluded segments. |
| `in_conflict`<br><br>bool | Whether the video copyright is in active conflict with another rights owner's video copyright.<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `monitoring_status`<br><br>enum | Whether the video is monitored successfully for copyright. The status could be NOT\_EXAMINED, COPYRIGHTED, and ERROR.<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `monitoring_type`<br><br>enum | Whether the video is monitored for VIDEO, AUDIO, or VIDEO\_AND\_AUDIO<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `ownership_countries`<br><br>VideoCopyrightGeoGate | Two string arrays of [ISO 3166 format country codes](http://l.facebook.com/l.php?u=http%3A%2F%2Fwww.iso.org%2Fiso%2Fcountry_codes%2Fiso_3166_code_lists%2Fcountry_names_and_code_elements.htm&h=AT34BBT04GKgPV9PpsrTct7Xb2nSO4EfUGKCbIrSQaZGIEqjOmypM9ODRWWi8MZZoZEsW2IktjemteZ0RrRXysp2T3T1qr6fjE2EZ8yHCBFMV6MQqlRDDtV1bltTB3ngtD6dRW8khOL_Lq6P). `included_countries` are where the owner owns the rights to the content. `excluded_countries` are where the owner does not own the rights to the content. When both lists are empty, rights ownership is worldwide.<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `reference_file`<br><br>CopyrightReferenceContainer | The reference file<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `reference_file_disabled`<br><br>bool | Whether the reference file is disabled.<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `reference_file_disabled_by_ops`<br><br>bool | Whether the reference file has been disabled by ops.<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `reference_owner_id`<br><br>string | The ID of the reference video owner<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `rule_ids`<br><br>[list<VideoCopyrightRule>](https://developers.facebook.com/docs/graph-api/reference/video-copyright-rule/) | A list of matching rules applied to the copyrighted content<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `tags`<br><br>list<string> | The tags/keywords associated with the copyright |
| `whitelisted_ids`<br><br>list<numeric string> | A list of page IDs or user IDs, who are allowed to use the copyrighted content.<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |

### Edges

| Edge | Description |
| --- | --- |
| [`update_records`](https://developers.facebook.com/docs/graph-api/reference/video-copyright/update_records/) | Update records of the copyright |

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

Creating
--------

You can't perform this operation on this endpoint.

Updating
--------

You can update a [VideoCopyright](https://developers.facebook.com/docs/graph-api/reference/video-copyright/) by making a POST request to [`/{video_copyright_id}`](https://developers.facebook.com/docs/graph-api/reference/video-copyright/).

### Parameters

| Parameter | Description |
| --- | --- |
| `append_excluded_ownership_segments`<br><br>boolean | If true, append the excluded ownership segments instead of replacing them |
| `attribution_id`<br><br>numeric string or integer | The ID of the attribution to be displayed for valid monitored videos matching this content. |
| `content_category`<br><br>enum {episode, movie, web} | The content category of the copyrighted reference file. |
| `excluded_ownership_countries`<br><br>list<UTF-8 encoded string> | A string array of [ISO 3166 format country codes](http://l.facebook.com/l.php?u=http%3A%2F%2Fwww.iso.org%2Fiso%2Fcountry_codes%2Fiso_3166_code_lists%2Fcountry_names_and_code_elements.htm&h=AT1iBQr5mxbp2Cd1k9dFB9Cgl3fUBUWjE_ehJVRV0BkMc6-BgfLGuNDe1r1thMIwLqpe3NePQaF85OsG3bu-QuwrsVrztbxL3liuUYZEt6FdDmXW4ox3CkTFgnKETbCG0S9iNZ1rbFOFhYXV), where the owner does not own the rights to the content |
| `excluded_ownership_segments`<br><br>list<Video Match Segment> | An array of match segments to exclude from the matching algorithm. System generated excluded segments may not be replaced. |
| `start_time_in_sec`<br><br>float | Required |
| `media_type`<br><br>enum {VIDEO\_AND\_AUDIO, VIDEO\_ONLY, AUDIO\_ONLY} | Required |
| `duration_in_sec`<br><br>float | Required |
| `segment_source`<br><br>enum {PUBLISHER\_DEFINED, PAUSE\_LIVE\_MONITORING, LABEL\_MUTED, PUBLISHER\_MUTED, MUSIC\_RESTRICTION\_MUTED\_STILL\_VIDEO, MUSIC\_RESTRICTION\_MUTED\_MULTI\_TRACK, AUDIO\_LIBRARY\_USAGE, MELODY, INELIGIBLE\_CONTENT} | Default value: `PUBLISHER_DEFINED` |
| `is_reference_disabled`<br><br>boolean | If true, stop creating matches for the reference file. |
| `monitoring_type`<br><br>enum {VIDEO\_AND\_AUDIO, VIDEO\_ONLY, AUDIO\_ONLY} | Setting to indicate whether the content has copyright ownership on video, audio, or both. |
| `ownership_countries`<br><br>list<UTF-8 encoded string> | A string array of [ISO 3166 format country codes](http://l.facebook.com/l.php?u=http%3A%2F%2Fwww.iso.org%2Fiso%2Fcountry_codes%2Fiso_3166_code_lists%2Fcountry_names_and_code_elements.htm&h=AT125Dbs33srvNIvePjs2SjkhJky4gWFlvwQ4aqsqlwYTozaH7bQWtXj9WCkxlKdZDgaV1csU7NLAKONPszYJrNP83t5hdolZaprVxGVshUCluoJX0n2mFhyrcmtS5HNxHcGXrq6JlU_5eBK), where the owner owns the rights to the content |
| `rule_id`<br><br>numeric string or integer | A copyright policy to be applied to the copyrighted content. |
| `whitelisted_ids`<br><br>list<numeric string> | A list of page IDs or user IDs, who are allowed to use the copyrighted content. |
| `whitelisted_ig_user_ids`<br><br>list<numeric string> | A list of Instagram user IDs who are allowed to use the copyrighted content. |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node to which you POSTed.

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

Deleting
--------

You can't perform this operation on this endpoint.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

Video Copyright Update Records
==============================

Reading
-------

Update history records for on video reference files

Starting September 14, 2021, this endpoint will throw an error for version 12.0+ calls made by apps that lack the endpoint's required permissions. This change will apply to all versions on December 13, 2021.

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bvideo-copyright-id%7D%2Fupdate_records&version=v19.0)

    GET /v19.0/{video-copyright-id}/update_records HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{video-copyright-id}/update_records',
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

    /* make the API call */
    FB.api(
        "/{video-copyright-id}/update_records",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{video-copyright-id}/update_records",
        null,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{video-copyright-id}/update_records"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

This endpoint doesn't have any parameters.

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of MediaCopyrightUpdateRecord nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

Creating
--------

You can't perform this operation on this endpoint.

Updating
--------

You can't perform this operation on this endpoint.

Deleting
--------

You can't perform this operation on this endpoint.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)