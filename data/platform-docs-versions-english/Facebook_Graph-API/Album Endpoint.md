Album
=====

Represents an [Album](https://www.facebook.com/help/www/490693151131920/).

Reading
-------

Get [Fields](#fields) and [Edges](#edges) on an Album.

### Requirements

Requirements depend on the type of node that the Album is on.

| Requirement | User nodes | Page nodes | Group nodes |
| --- | --- | --- | --- |
| [Access Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens) | Any | Any | [User](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) |
| [Features](https://developers.facebook.com/docs/apps/review/feature) | None | To get public Page content of Pages you can not [perform a task](https://developers.facebook.com/docs/pages/overview#tasks) on, you will need [`Page Public Content Access`](https://developers.facebook.com/docs/apps/review/feature#reference-PAGES_ACCESS) | None |
| [Permissions](https://developers.facebook.com/docs/apps/review/login-permissions) | [`user_photos`](https://developers.facebook.com/docs/apps/review/login-permissions#user-photos) | Unpublished Pages:<br><br>* You must be able to [perform the `CREATE` task](https://developers.facebook.com/docs/pages/overview#tasks) on the Page<br>    <br>* [`pages_read_engagement`](https://developers.facebook.com/docs/pages/overview#tasks)<br>    <br><br>Published Pages:<br><br>* [`pages_read_engagement`](https://developers.facebook.com/docs/pages/overview#tasks) | None |
| [Group Roles](https://www.facebook.com/help/1686671141596230?helpref=about_content) | Not applicable | Not applicable | Admin |

### Requirements

Requirements depend on the type of node that the Album is on.

| Requirement | User nodes | Page nodes | Group nodes |
| --- | --- | --- | --- |
| [Access Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens) | Any | Any | [User](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) |
| [Features](https://developers.facebook.com/docs/apps/review/feature) | None | To get public Page content of Pages you can not [perform a task](https://developers.facebook.com/docs/pages/overview#tasks) on, you will need [`Page Public Content Access`](https://developers.facebook.com/docs/apps/review/feature#reference-PAGES_ACCESS) | None |
| [Permissions](https://developers.facebook.com/docs/apps/review/login-permissions) | [`user_photos`](https://developers.facebook.com/docs/apps/review/login-permissions#user-photos) | Unpublished Pages:<br><br>* You must be able to [perform the `CREATE` task](https://developers.facebook.com/docs/pages/overview#tasks) on the Page<br>    <br>* [`pages_read_engagement`](https://developers.facebook.com/docs/pages/overview#tasks)<br>    <br><br>Published Pages:<br><br>* [`pages_read_engagement`](https://developers.facebook.com/docs/pages/overview#tasks) | None |
| [Group Roles](https://www.facebook.com/help/1686671141596230?helpref=about_content) | Not applicable | Not applicable | Admin |

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Balbum-id%7D&version=v19.0)

    GET /v19.0/{album-id} HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{album-id}',
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
        "/{album-id}",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{album-id}",
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
                                   initWithGraphPath:@"/{album-id}"
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
| `id`<br><br>numeric string | The Album ID. |
| `backdated_time`<br><br>datetime | A user-specified time for when this object was created |
| `backdated_time_granularity`<br><br>enum | How accurate the backdated time is |
| `can_upload`<br><br>bool | Whether the app user can upload photos to this Album |
| `count`<br><br>unsigned int32 | The approximate number of [Photos](https://developers.facebook.com/docs/graph-api/reference/photo) and [Videos](https://developers.facebook.com/docs/graph-api/reference/video) in the Album. |
| `cover_photo`[](#)<br><br>[Photo](https://developers.facebook.com/docs/graph-api/reference/photo/) | Album cover photo id |
| `created_time`<br><br>datetime | The Album creation date and time.<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `description`<br><br>string | The Album description. |
| `event`[](#)<br><br>[Event](https://developers.facebook.com/docs/graph-api/reference/event/) | If this object has a place, the event associated with the place |
| `from`<br><br>User\|Page | The User who created the Album. |
| `link`<br><br>token with structure: URL | A link to this Album on Facebook. |
| `location`<br><br>string | The Album textual location. |
| `name`<br><br>string | The Album title.<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `place`<br><br>[Place](https://developers.facebook.com/docs/graph-api/reference/place/) | Place info |
| `privacy`<br><br>string | The Album privacy settings. |
| `type`<br><br>string | The Album type: album, app, cover, profile, mobile, normal, or wall |
| `updated_time`<br><br>datetime | The date and time the Album was last updated. |

### Edges

| Edge | Description |
| --- | --- |
| [`comments`](https://developers.facebook.com/docs/graph-api/reference/album/comments/) | Represents a collection of [Comments](https://developers.facebook.com/docs/graph-api/reference/comment) on the Album. |
| [`likes`](https://developers.facebook.com/docs/graph-api/reference/album/likes/) | A collection of [Profiles](https://developers.facebook.com/docs/graph-api/reference/profile) who like the Album. |
| [`photos`](https://developers.facebook.com/docs/graph-api/reference/album/photos/) | A collection of [Photos](https://developers.facebook.com/docs/graph-api/reference/photo) in the Album |
| [`picture`](https://developers.facebook.com/docs/graph-api/reference/album/picture/) | A link to the Album cover photo. |

### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 80001 | There have been too many calls to this Page account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |
| 100 | Invalid parameter |

Creating
--------

You can make a POST request to `albums` edge from the following paths:

* [`/{group_id}/albums`](https://developers.facebook.com/docs/graph-api/reference/group/albums/)

When posting to this edge, an [Album](https://developers.facebook.com/docs/graph-api/reference/album/) will be created.

### Parameters

| Parameter | Description |
| --- | --- |
| `contributors`<br><br>list<int> | Contributors to turn this into a shared album |
| `description`<br><br>UTF-8 string | Deprecated. Use the message param<br><br>DeprecatedSupports Emoji |
| `is_default`<br><br>boolean | Default value: `false`<br><br>`true` indicates that the request will create the application specific album |
| `location`<br><br>string | A text location of the Album for non-page locations |
| `make_shared_album`<br><br>boolean | Default value: `false`<br><br>Ensures the created Album is a shared Album |
| `message`<br><br>string | The Album's caption. This appears below the title of the album in the Album view |
| `name`<br><br>UTF-8 string | The title of the Album<br><br>Supports Emoji |
| `place`<br><br>place tag | The ID of a location page to tag the Album with |
| `privacy`<br><br>Privacy Parameter | The privacy of the Album |
| `tags`<br><br>list<int> | Deprecated<br><br>Deprecated |
| `visible`<br><br>string | Deprecated. Use privacy<br><br>Deprecated |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node represented by `id` in the return type.

Struct {

`id`: numeric string,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 200 | Permissions error |
| 190 | Invalid OAuth 2.0 Access Token |

Updating
--------

You can't perform this operation on this endpoint.

Deleting
--------

You can't perform this operation on this endpoint.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

Album Comments
==============

Reading
-------

Comments for this object

### New Page Experience

This endpoint is supported for [New Page Experience](https://developers.facebook.com/docs/pages/new-pages-experience/).

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Balbum-id%7D%2Fcomments&version=v19.0)

    GET /v19.0/{album-id}/comments HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{album-id}/comments',
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
        "/{album-id}/comments",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{album-id}/comments",
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
                                   initWithGraphPath:@"/{album-id}/comments"
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
| `filter`<br><br>enum{stream, toplevel} | Default value: `toplevel`<br><br>SELF\_EXPLANATORY |
| `live_filter`<br><br>enum{filter\_low\_quality, no\_filter} | Default value: `filter_low_quality`<br><br>For comments on a Live streaming video, this determines whether low quality comments will be filtered out of the results (filtering is enabled by default). In all other circumstances this parameter is ignored. |
| `order`<br><br>enum{chronological, reverse\_chronological} | Preferred ordering of the comments. Accepts chronological (oldest first) and reverse chronological (newest first). If the comments can be ranked, then the order will always be ranked regardless of this modifier. The best practice for querying comments on a Live video is to continually poll for comments in the reversechronological ordering mode. |
| `since`<br><br>datetime | Lower bound of the time range to consider |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {},
    "`summary`": {}
}

#### `data`

A list of [Comment](https://developers.facebook.com/docs/graph-api/reference/comment/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

#### `summary`

Aggregated information about the edge, such as counts. Specify the fields to fetch in the summary param (like `summary=order`).

| Field | Description |
| --- | --- |
| `order`<br><br>enum | Order of returned comments |
| `total_count`<br><br>unsigned int32 | Total number of people who commented |
| `can_comment`<br><br>bool | Can the viewer comment |

### Error Codes

| Error | Description |
| --- | --- |
| 80001 | There have been too many calls to this Page account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |
| 100 | Invalid parameter |
| 200 | Permissions error |

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

Album Likes
===========

Reading
-------

Likes for this object

### New Page Experience

This endpoint is supported for [New Page Experience](https://developers.facebook.com/docs/pages/new-pages-experience/).

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Balbum-id%7D%2Flikes&version=v19.0)

    GET /v19.0/{album-id}/likes HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{album-id}/likes',
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
        "/{album-id}/likes",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{album-id}/likes",
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
                                   initWithGraphPath:@"/{album-id}/likes"
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
    "`paging`": {},
    "`summary`": {}
}

#### `data`

A list of [Profile](https://developers.facebook.com/docs/graph-api/reference/profile/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

#### `summary`

Aggregated information about the edge, such as counts. Specify the fields to fetch in the summary param (like `summary=total_count`).

| Field | Description |
| --- | --- |
| `total_count`<br><br>unsigned int32 | Total number of likes |
| `can_like`<br><br>bool | Can the viewer like |
| `has_liked`<br><br>bool | Has the viewer liked |

### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 190 | Invalid OAuth 2.0 Access Token |
| 100 | Invalid parameter |

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

Album Photos
============

Represents a collection [Photos](https://developers.facebook.com/docs/graph-api/reference/photo) and [Videos](https://developers.facebook.com/docs/graph-api/reference/video) on an [Album](https://developers.facebook.com/docs/graph-api/reference/album).

Reading
-------

Get a list of [Photos](https://developers.facebook.com/docs/graph-api/reference/photo) on an [Album](https://developers.facebook.com/docs/graph-api/reference/album).

### New Page Experience

This endpoint is supported for [New Page Experience](https://developers.facebook.com/docs/pages/new-pages-experience/).

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Balbum-id%7D%2Fphotos&version=v19.0)

    GET /v19.0/{album-id}/photos HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{album-id}/photos',
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
        "/{album-id}/photos",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{album-id}/photos",
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
                                   initWithGraphPath:@"/{album-id}/photos"
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

A list of [Photo](https://developers.facebook.com/docs/graph-api/reference/photo/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 80001 | There have been too many calls to this Page account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |
| 100 | Invalid parameter |
| 190 | Invalid OAuth 2.0 Access Token |

Creating
--------

Animated photos are not supported, and a photo must be less than 10MB in size.

You can make a POST request to `photos` edge from the following paths:

* [`/{album_id}/photos`](https://developers.facebook.com/docs/graph-api/reference/album/photos/)

When posting to this edge, a [Photo](https://developers.facebook.com/docs/graph-api/reference/photo/) will be created.

### Parameters

| Parameter | Description |
| --- | --- |
| `aid`<br><br>string | Legacy album ID. Deprecated<br><br>Deprecated |
| `allow_spherical_photo`<br><br>boolean | Default value: `false`<br><br>Indicates that we should allow this photo to be treated as a spherical photo. This will not change the behavior unless the server is able to interpret the photo as spherical, such as via Photosphere XMP metadata. Regular non-spherical photos will still be treated as regular photos even if this parameter is true. |
| `alt_text_custom`<br><br>string | Accessible alternative description for an image |
| `android_key_hash`<br><br>string | Android key hash |
| `application_id`<br><br>non-empty string | iTunes App ID. This is used by the native Share dialog that's part of iOS |
| `attempt`<br><br>int64 | Default value: `0`<br><br>Number of attempts that have been made to upload this photo |
| `audience_exp`<br><br>boolean | Default value: `false`<br><br>Audience exp |
| `backdated_time`<br><br>datetime | A user-specified creation time for this photo |
| `backdated_time_granularity`<br><br>enum{year, month, day, hour, min, none} | Default value: `none`<br><br>Use only the part of the `backdated_time` parameter to the specified granularity |
| `caption`<br><br>UTF-8 string | The description of the photo<br><br>Supports Emoji |
| `composer_session_id`<br><br>string | Composer session ID |
| `direct_share_status`<br><br>int64 | The status to allow sponsor directly boost the post. |
| `feed_targeting`<br><br>feed target | Object that controls [News Feed targeting](https://www.facebook.com/help/352402648173466) for this post. Anyone in these groups will be more likely to see this post. People not in these groups will be less likely to see this post, but may still see it anyway. Any of the targeting fields shown here can be used, but none are required. `feed_targeting` applies to Pages only. |
| `geo_locations`<br><br>Object |     |
| `countries`<br><br>list<string> |     |
| `regions`<br><br>list<Object> |     |
| `key`<br><br>int64 |     |
| `cities`<br><br>list<Object> |     |
| `key`<br><br>int64 |     |
| `zips`<br><br>list<Object> |     |
| `key`<br><br>string |     |
| `locales`<br><br>list<string> | Values for targeted locales. Use `type` of `adlocale` to [find Targeting Options](https://developers.facebook.com/docs/marketing-api/targeting-search) and use the returned key to specify. |
| `age_min`<br><br>int64 | Must be `13` or higher. Default is 0. |
| `age_max`<br><br>int64 | Maximum age. |
| `genders`<br><br>list<int64> | Target specific genders. `1` targets all male viewers and `2` females. Default is to target both. |
| `college_years`<br><br>list<int64> | Array of integers. Represent graduation years from college. |
| `education_statuses`<br><br>list<int64> | Array of integers which represent current educational status. Use `1` for high school, `2` for undergraduate, and `3` for alum (or localized equivalents). |
| `interested_in`<br><br>list<int64> | Deprecated. Please see the [Graph API Changelog](https://developers.facebook.com/docs/graph-api/changelog/breaking-changes#2-7-2018) for more information.<br><br>Deprecated |
| `relationship_statuses`<br><br>list<int64> | Array of integers for targeting based on relationship status. Use `1` for single, `2` for 'in a relationship', `3` for married, and `4` for engaged. Default is all types. |
| `interests`<br><br>list<int64> | One or more IDs of pages to target fans of pages.Use `type` of `page` to get possible IDs as [find Targeting Options](https://developers.facebook.com/docs/marketing-api/targeting-search) and use the returned id to specify. |
| `filter_type`<br><br>int64 | Default value: `-1`<br><br>Unused? |
| `full_res_is_coming_later`<br><br>boolean | Default value: `false`<br><br>Full res is coming later |
| `initial_view_heading_override_degrees`<br><br>int64 | Manually specify the initial view heading in degrees from 0 to 360. This overrides any value present in the photo embedded metadata or provided in the spherical\_metadata parameter |
| `initial_view_pitch_override_degrees`<br><br>int64 | Manually specify the initial view pitch in degrees from -90 to 90. This overrides any value present in the photo embedded metadata or provided in the spherical\_metadata parameter |
| `initial_view_vertical_fov_override_degrees`<br><br>int64 | Manually specify the initial view vertical FOV in degrees from 60 to 120. This overrides any value present in the photo embedded metadata or provided in the spherical\_metadata parameter |
| `ios_bundle_id`<br><br>string | iOS Bundle ID |
| `is_explicit_location`<br><br>boolean | Is this an explicit location? |
| `is_explicit_place`<br><br>boolean | If set to `true`, the tag is a place, not a person |
| `manual_privacy`<br><br>boolean | Default value: `false`<br><br>Manual privacy |
| `message`<br><br>UTF-8 string | Deprecated. Please use the caption param instead.<br><br>DeprecatedSupports Emoji |
| `name`<br><br>UTF-8 string | Deprecated. Please use the caption param instead.<br><br>DeprecatedSupports Emoji |
| `no_story`<br><br>boolean | If set to `true`, this will suppress the News Feed story that is automatically generated on a profile when people upload a photo using your app. Useful for adding old photos where you may not want to generate a story |
| `offline_id`<br><br>int64 | Default value: `0`<br><br>Offline ID |
| `og_action_type_id`<br><br>numeric string or integer | The Open Graph action type |
| `og_icon_id`<br><br>numeric string or integer | The Open Graph icon |
| `og_object_id`<br><br>OG object ID or URL string | The Open Graph object ID |
| `og_phrase`<br><br>string | The Open Graph phrase |
| `og_set_profile_badge`<br><br>boolean | Default value: `false`<br><br>Flag to set if the post should create a profile badge |
| `og_suggestion_mechanism`<br><br>string | The Open Graph suggestion |
| `place`<br><br>place tag | Page ID of a place associated with the photo |
| `privacy`<br><br>Privacy Parameter | Determines the privacy settings of the photo. If not supplied, this defaults to the privacy level granted to the app in the Login dialog. This field cannot be used to set a more open privacy setting than the one granted |
| `profile_id`<br><br>int | Deprecated. Use `target_id` instead<br><br>Deprecated |
| `proxied_app_id`<br><br>numeric string or integer | Proxied app ID |
| `published`<br><br>boolean | Default value: `true`<br><br>Set to `false` if you don't want the photo to be published immediately |
| `qn`<br><br>string | Photos waterfall ID |
| `scheduled_publish_time`<br><br>int64 | Time at which an unpublished post should be published (Unix ISO-8601 format). Applies to Pages only |
| `spherical_metadata`<br><br>JSON object | A set of params describing an uploaded spherical photo. This field is not required; if it is not present we will try to generate spherical metadata from the metadata embedded in the image. If it is present, it takes precedence over any embedded metadata. Please click to the left to expand this list and see more information on each parameter. See also the Google Photo Sphere spec for more info on the meaning of the params: https://developers.google.com/streetview/spherical-metadata |
| `ProjectionType`<br><br>string | Accepted values include equirectangular (full spherical photo), cylindrical (panorama), and cubestrip (also known as cubemap, e.g. for synthetic or rendered content; stacked vertically with 6 faces).<br><br>Required |
| `CroppedAreaImageWidthPixels`<br><br>int64 | \--- In equirectangular projection: As described in Google Photo Sphere XMP Metadata spec.<br><br>\--- In cylindrical projection: Very similar to equirectangular. This value should be equal to the actual width of the image, and together with FullPanoWidthPixels, it describes the horizontal FOV of content of the image: HorizontalFOV = 360 \* CroppedAreaImageWidthPixels / FullPanoWidthPixels.<br><br>\--- In cubestrip projection: This has no relationship to the pixel dimensions of the image. It is simply a representation of the horizontal FOV of the content of the image. HorizontalFOV = CroppedAreaImageWidthPixels / PixelsPerDegree, where PixelsPerDegree is defined by FullPanoWidthPixels.<br><br>Required |
| `CroppedAreaImageHeightPixels`<br><br>int64 | \--- In equirectangular projection: As described in Google Photo Sphere XMP Metadata spec.<br><br>\--- In cylindrical projection: This value will NOT be equal to the actual height of the image. Instead, together with FullPanoHeightPixels, it describes the vertical FOV of the image: VerticalFOV = 180 \* CroppedAreaImageHeightPixels / FullPanoHeightPixels. In other words, this value is equal to the CroppedAreaImageHeightPixels value that this image would have, if it were projected into equirectangular format while maintaining the same FullPanoWidthPixels.<br><br>\--- In cubestrip projection: This has no relationship to the pixel dimensions of the image. It is simply a representation of the vertical FOV of the content of the image. VerticalFOV = CroppedAreaImageHeightPixels / PixelsPerDegree, where PixelsPerDegree is defined by FullPanoWidthPixels.<br><br>Required |
| `FullPanoWidthPixels`<br><br>int64 | \--- In equirectangular projection: As described in Google Photo Sphere XMP Metadata spec.<br><br>\--- In cylindrical projection: Very similar to equirectangular. This value defines a ratio of horizontal pixels to degrees in the space of the image, and in general the pixel to degree ratio in the scope of the metadata object. Concretely, PixelsPerDegree = FullPanoWidthPixels / 360. This is also equivalent to the circumference of the cylinder used to model this projection.<br><br>\--- In cubestrip projection: This value has no relationship to the pixel dimensions of the image. It only defines the pixel to degree ratio in the scope of the metadata object. It represents the number of pixels in 360 degrees, so pixels per degree is then given by: PixelsPerDegree = FullPanoWidthPixels / 360. As an example, if FullPanoWidthPixels were chosen to be 3600, we would have PixelsPerDegree = 3600 / 360 = 10. An image with a vertical field of view of 65 degrees would then have a CroppedAreaImageHeightPixels value of 65 \* 10 = 650.<br><br>Required |
| `FullPanoHeightPixels`<br><br>int64 | \--- In equirectangular projection: As described in Google Photo Sphere XMP Metadata spec.<br><br>\--- In cylindrical projection: This value is equal to the FullPanoHeightPixels value that this image would have, if it were projected into equirectangular format while maintaining the same FullPanoWidthPixels. It is always equal to FullPanoWidthPixels / 2.<br><br>\--- In cubestrip projection: This value has no relationship to the pixel dimensions of the image. It is a second, redundant representation of PixelsPerDegree. FullPanoHeightPixels = 180 \* PixelsPerDegree. It must be consistent with FullPanoWidthPixels: FullPanoHeightPixels = FullPanoWidthPixels / 2.<br><br>Required |
| `CroppedAreaLeftPixels`<br><br>int64 | Default value: `0`<br><br>\--- In equirectangular projection: As described in Google Photo Sphere XMP Metadata spec.<br><br>\--- In cylindrical projection: This value is equal to the CroppedAreaLeftPixels value that this image would have, if it were projected into equirectangular format while maintaining the same FullPanoWidthPixels. It is just a representation of the same angular offset that it represents in equirectangular projection in the Google Photo Sphere spec. Concretely, AngularOffsetFromLeftDegrees = CroppedAreaLeftPixels / PixelsPerDegree, where PixelsPerDegree is defined by FullPanoWidthPixels.<br><br>\--- In cubestrip projection: This value has no relationship to the pixel dimensions of the image. It is just a representation of the same angular offset that it represents in equirectangular projection in the Google Photo Sphere spec. AngularOffsetFromLeftDegrees = CroppedAreaLeftPixels / PixelsPerDegree, where PixelsPerDegree is defined by FullPanoWidthPixels. |
| `CroppedAreaTopPixels`<br><br>int64 | Default value: `0`<br><br>\--- In equirectangular projection: As described in Google Photo Sphere XMP Metadata spec.<br><br>\--- In cylindrical projection: This value is equal to the CroppedAreaTopPixels value that this image would have, if it were projected into equirectangular format while maintaining the same FullPanoWidthPixels. It is just a representation of the same angular offset that it represents in equirectangular projection in the Google Photo Sphere spec. Concretely, AngularOffsetFromTopDegrees = CroppedAreaTopPixels / PixelsPerDegree, where PixelsPerDegree is defined by FullPanoWidthPixels.<br><br>\--- In cubestrip projection: This value has no relationship to the pixel dimensions of the image. It is just a representation of the same angular offset that it represents in equirectangular projection in the Google Photo Sphere spec. AngularOffsetFromTopDegrees = CroppedAreaTopPixels / PixelsPerDegree, where PixelsPerDegree is defined by FullPanoWidthPixels. |
| `PoseHeadingDegrees`<br><br>float |     |
| `PosePitchDegrees`<br><br>float |     |
| `PoseRollDegrees`<br><br>float |     |
| `InitialViewHeadingDegrees`<br><br>float |     |
| `InitialViewPitchDegrees`<br><br>float |     |
| `InitialViewRollDegrees`<br><br>float | This is not currently supported |
| `InitialViewVerticalFOVDegrees`<br><br>float | This is deprecated. Please use InitialVerticalFOVDegrees. |
| `InitialVerticalFOVDegrees`<br><br>float | You can set the intial vertical FOV of the image. You can set either this field or InitialHorizontalFOVDegrees. |
| `InitialHorizontalFOVDegrees`<br><br>float | You can set the intial horizontal FOV of the image. You can set either this field or InitialVerticalFOVDegrees. |
| `PreProcessCropLeftPixels`<br><br>int64 |     |
| `PreProcessCropRightPixels`<br><br>int64 |     |
| `sponsor_id`<br><br>numeric string or integer | Facebook Page id that is tagged as sponsor in the photo post |
| `sponsor_relationship`<br><br>int64 | Sponsor Relationship, such as Presented By or Paid PartnershipWith |
| `tags`<br><br>list<Object> | Tags on this photo |
| `x`<br><br>float | The x-axis offset for the tag |
| `y`<br><br>float | The y-axis offset for the tag |
| `tag_uid`<br><br>int | The user\_id of the tagged person |
| `tag_text`<br><br>string | Text associated with the tag |
| `target_id`<br><br>int | Don't use this. Specifying a `target_id` allows you to post the photo to an object that's not the user in the access token. It only works when posting directly to the `/photos` endpoint. Instead of using this parameter you should be using the edge on an object directly, like `/page/photos`. |
| `targeting`<br><br>target | Allows you to target posts to specific audiences. Applies to Pages only |
| `geo_locations`<br><br>Object |     |
| `countries`<br><br>list<string> |     |
| `regions`<br><br>list<Object> |     |
| `key`<br><br>int64 |     |
| `cities`<br><br>list<Object> |     |
| `key`<br><br>int64 |     |
| `zips`<br><br>list<Object> |     |
| `key`<br><br>string |     |
| `locales`<br><br>list<string> |     |
| `excluded_countries`[](#)<br><br>list<string> |     |
| `excluded_regions`[](#)<br><br>list<int64> |     |
| `excluded_cities`[](#)<br><br>list<int64> |     |
| `excluded_zipcodes`[](#)<br><br>list<string> |     |
| `timezones`[](#)<br><br>list<int64> |     |
| `age_min`<br><br>enum {13, 15, 18, 21, 25} |     |
| `time_since_original_post`<br><br>int64 | Same as `backdated_time` but with a time delta instead of absolute time |
| `uid`<br><br>int | Deprecated |
| `unpublished_content_type`<br><br>enum {SCHEDULED, SCHEDULED\_RECURRING, DRAFT, ADS\_POST, INLINE\_CREATED, PUBLISHED, REVIEWABLE\_BRANDED\_CONTENT} | Content type of the unpublished content type |
| `url`<br><br>string | The URL of a photo that is already uploaded to the Internet. You must specify this or a file attachment |
| `user_selected_tags`<br><br>boolean | Default value: `false`<br><br>User selected tags |
| `vault_image_id`<br><br>numeric string or integer | A vault image ID to use for a photo. You can use only one of `url`, a file attachment, `vault_image_id`, or `sync_object_uuid` |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node represented by `id` in the return type.

Struct {

`id`: numeric string,

`post_id`: token with structure: Post ID,

}

### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 321 | Album is full |
| 100 | Invalid parameter |
| 220 | Album or albums not visible |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 120 | Invalid album id |

Updating
--------

You can't perform this operation on this endpoint.

Deleting
--------

You can't perform this operation on this endpoint.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

Album Picture
=============

Reading
-------

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Balbum-id%7D%2Fpicture&version=v19.0)

    GET /v19.0/{album-id}/picture HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{album-id}/picture',
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
        "/{album-id}/picture",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{album-id}/picture",
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
                                   initWithGraphPath:@"/{album-id}/picture"
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
| `redirect`<br><br>boolean | Default value: `true`<br><br>By default the picture edge will return a picture instead of a JSON response. If you want the picture edge to return JSON that describes the image set `redirect=0` when you make the request. |
| `type`<br><br>enum{thumbnail, small, album} | Default value: `album`<br><br>The size of this picture. It can be one of the following values: thumbnail, small, album. |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [ProfilePictureSource](https://developers.facebook.com/docs/graph-api/reference/profile-picture-source/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |

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