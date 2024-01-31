Group Message
=============

[](#)

Reading
-------

GroupMessage

### New Page Experience

This endpoint is supported for [New Page Experience](https://developers.facebook.com/docs/pages/new-pages-experience/).

### Feature Permissions

| Name | Description |
| --- | --- |
| Groups API | This [feature permission](https://developers.facebook.com/docs/graph-api/reference/group/) may be required. |

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bgroup-message-id%7D&version=v18.0)

    GET /v18.0/{group-message-id} HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{group-message-id}',
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
        "/{group-message-id}",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{group-message-id}",
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
                                   initWithGraphPath:@"/{group-message-id}"
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
| `id`<br><br>token with structure: Post ID | id  |
| `actions`<br><br>list | actions |
| `admin_creator`<br><br>BusinessUser\|User\|Application | admin\_creator |
| `allowed_advertising_objectives`<br><br>list<string> | allowed\_advertising\_objectives |
| `application`<br><br>[Application](https://developers.facebook.com/docs/graph-api/reference/application/) | application |
| `backdated_time`<br><br>datetime | backdated\_time |
| `call_to_action`<br><br>struct with keys: type, value | call\_to\_action |
| `can_reply_privately`<br><br>bool | can\_reply\_privately |
| `caption`<br><br>string | caption |
| `child_attachments`<br><br>list | child\_attachments |
| `comments_mirroring_domain`<br><br>string | comments\_mirroring\_domain |
| `coordinates`<br><br>struct with keys: checkin\_id, author\_uid, page\_id, target\_id, target\_href, coords, tagged\_uids, timestamp, message, target\_type | coordinates |
| `created_time`<br><br>datetime | created\_time<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `description`<br><br>string | description |
| `event`[](#)<br><br>[Event](https://developers.facebook.com/docs/graph-api/reference/event/) | event |
| `expanded_height`<br><br>unsigned int32 | expanded\_height |
| `expanded_width`<br><br>unsigned int32 | expanded\_width |
| `feed_targeting`<br><br>struct with keys: country, cities, regions, genders, age\_min, age\_max, education\_statuses, college\_years, relationship\_statuses, interests, interested\_in, user\_adclusters, locales, countries, geo\_locations, work\_positions, work\_employers, education\_majors, education\_schools, family\_statuses, life\_events, industries, politics, ethnic\_affinity, generation, fan\_of, relevant\_until\_ts | feed\_targeting |
| `from`<br><br>User\|Page | from |
| `full_picture`<br><br>string | full\_picture |
| `height`<br><br>unsigned int32 | height |
| `icon`<br><br>string | icon |
| `is_app_share`<br><br>bool | is\_app\_share |
| `is_eligible_for_promotion`<br><br>bool | is\_eligible\_for\_promotion |
| `is_expired`<br><br>bool | is\_expired |
| `is_hidden`<br><br>bool | is\_hidden |
| `is_inline_created`<br><br>bool | is\_inline\_created |
| `is_popular`<br><br>bool | is\_popular |
| `is_published`<br><br>bool | is\_published |
| `is_spherical`<br><br>bool | is\_spherical |
| `link`<br><br>uri | link |
| `message`<br><br>string | message<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `message_tags`<br><br>list | message\_tags |
| `multi_share_end_card`<br><br>bool | multi\_share\_end\_card |
| `multi_share_optimized`<br><br>bool | multi\_share\_optimized |
| `name`<br><br>string | name |
| `object_id`<br><br>string | object\_id |
| `parent_id`<br><br>token with structure: Post ID | parent\_id |
| `permalink_url`<br><br>uri | permalink\_url |
| `place`<br><br>[Place](https://developers.facebook.com/docs/graph-api/reference/place/) | place |
| `privacy`<br><br>[Privacy](https://developers.facebook.com/docs/graph-api/reference/privacy/) | privacy |
| `promotable_id`[](#)<br><br>token with structure: Post ID | promotable\_id |
| `properties`<br><br>list | properties |
| `scheduled_publish_time`<br><br>float | scheduled\_publish\_time |
| `shares`<br><br>struct with keys: count | shares |
| `source`<br><br>string | source |
| `status_type`<br><br>string | status\_type |
| `story`<br><br>string | story<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `story_tags`<br><br>list | story\_tags |
| `subscribed`<br><br>bool | subscribed |
| `target`[](#)<br><br>[Profile](https://developers.facebook.com/docs/graph-api/reference/profile/) | target |
| `targeting`<br><br>struct with keys: country, cities, regions, zips, genders, college\_networks, work\_networks, age\_min, age\_max, education\_statuses, college\_years, college\_majors, political\_views, relationship\_statuses, interests, keywords, interested\_in, user\_clusters, user\_clusters2, user\_clusters3, user\_adclusters, excluded\_user\_adclusters, custom\_audiences, excluded\_custom\_audiences, locales, radius, connections, excluded\_connections, friends\_of\_connections, countries, excluded\_user\_clusters, adgroup\_id, user\_event, qrt\_versions, page\_types, user\_os, user\_device, action\_spec, action\_spec\_friend, action\_spec\_excluded, geo\_locations, excluded\_geo\_locations, targeted\_entities, conjunctive\_user\_adclusters, wireless\_carrier, site\_category, work\_positions, work\_employers, education\_majors, education\_schools, family\_statuses, life\_events, behaviors, travel\_status, industries, politics, markets, income, net\_worth, home\_type, home\_ownership, home\_value, ethnic\_affinity, generation, household\_composition, moms, office\_type, interest\_clusters\_expansion, dynamic\_audience\_ids, product\_audience\_specs, excluded\_product\_audience\_specs, exclusions, flexible\_spec, engagement\_specs, excluded\_engagement\_specs | targeting |
| `timeline_visibility`<br><br>string | timeline\_visibility |
| `type`<br><br>string | type |
| `updated_time`<br><br>datetime | updated\_time |
| `via`<br><br>User\|Page | via |
| `width`<br><br>unsigned int32 | width |

### Edges

| Edge | Description |
| --- | --- |
| [`attachments`](https://developers.facebook.com/docs/graph-api/reference/group-message/attachments/)[](#) | attachments |
| [`comments`](https://developers.facebook.com/docs/graph-api/reference/group-message/comments/) | comments |
| [`dynamic_posts`](https://developers.facebook.com/docs/graph-api/reference/group-message/dynamic_posts/) | dynamic\_posts |
| [`insights`](https://developers.facebook.com/docs/graph-api/reference/group-message/insights/) | insights |
| [`reactions`](https://developers.facebook.com/docs/graph-api/reference/group-message/reactions/)[](#) | reactions |
| [`sharedposts`](https://developers.facebook.com/docs/graph-api/reference/group-message/sharedposts/) | sharedposts |
| [`sponsor_tags`](https://developers.facebook.com/docs/graph-api/reference/group-message/sponsor_tags/) | sponsor\_tags |
| [`to`](https://developers.facebook.com/docs/graph-api/reference/group-message/to/) | to  |

### Error Codes

| Error | Description |
| --- | --- |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 200 | Permissions error |
| 100 | Invalid parameter |
| 190 | Invalid OAuth 2.0 Access Token |
| 2500 | Error parsing graph query |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Group Message Attachments
=========================

[](#)

Reading
-------

You can't perform this operation on this endpoint.

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Group Message Dynamic Posts
===========================

[](#)

Reading
-------

You can't perform this operation on this endpoint.

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Group Message Insights
======================

[](#)

Reading
-------

PostInsights

### New Page Experience

This endpoint is supported for [New Page Experience](https://developers.facebook.com/docs/pages/new-pages-experience/).

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bgroup-message-id%7D%2Finsights&version=v18.0)

    GET /v18.0/{group-message-id}/insights HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{group-message-id}/insights',
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
        "/{group-message-id}/insights",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{group-message-id}/insights",
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
                                   initWithGraphPath:@"/{group-message-id}/insights"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

| Parameter | Description |
| --- | --- |
| `date_preset`<br><br>enum{today, yesterday, this\_month, last\_month, this\_quarter, maximum, data\_maximum, last\_3d, last\_7d, last\_14d, last\_28d, last\_30d, last\_90d, last\_week\_mon\_sun, last\_week\_sun\_sat, last\_quarter, last\_year, this\_week\_mon\_today, this\_week\_sun\_today, this\_year} | date\_preset |
| `metric`<br><br>list<A valid metric for an insights endpoint> | metric |
| `period`<br><br>enum{day, week, days\_28, month, lifetime, total\_over\_range} | period |
| `since`<br><br>datetime | since |
| `until`<br><br>datetime | until |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [InsightsResult](https://developers.facebook.com/docs/graph-api/reference/insights-result/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Group Message Reactions
=======================

[](#)

Reading
-------

You can't perform this operation on this endpoint.

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Group Message Sharedposts
=========================

[](#)

Reading
-------

You can't perform this operation on this endpoint.

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Group Message To
================

[](#)

Reading
-------

PostTo

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bgroup-message-id%7D%2Fto&version=v18.0)

    GET /v18.0/{group-message-id}/to HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{group-message-id}/to',
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
        "/{group-message-id}/to",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{group-message-id}/to",
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
                                   initWithGraphPath:@"/{group-message-id}/to"
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

A list of [Profile](https://developers.facebook.com/docs/graph-api/reference/profile/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)