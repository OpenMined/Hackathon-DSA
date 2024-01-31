Group
=====

A Facebook [Group](https://www.facebook.com/help/1629740080681586).

[](#)

Reading
-------

Returns information about a single Group object. To get a list of Groups a User administers, use the [`/user/groups`](https://developers.facebook.com/docs/graph-api/reference/user/groups/) edge instead.

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bgroup-id%7D&version=v18.0)

    GET /v18.0/{group-id} HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{group-id}',
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
        "/{group-id}",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{group-id}",
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
                                   initWithGraphPath:@"/{group-id}"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### Permissions

* `groups_access_member_info` — Enables your app to receive member-related data on group content.
* `publish_to_groups` — Enables your app to post content into a group on behalf of a user.

**For Public and Closed Groups**

A User access token

**For Secret Groups**

A User access token for an Admin of the Group

**Caveats**

* Fields that return User information will not be included in any responses unless the request is made using an access token of an Admin of the Group.
    

### Fields

| Property Name | Description | Type |
| --- | --- | --- |
| `id` | The Group ID | `string` |
| `cover` | Information about the Group's cover photo. | `CoverPhoto` |
| `id` | ID of the [Photo](https://developers.facebook.com/docs/reference/api/photo/) that represents this cover photo. | `string` |
| `source` | URL to the [Photo](https://developers.facebook.com/docs/reference/api/photo/) that represents this cover photo. | `string` |
| `offset_y` | The vertical offset in pixels of the photo from the bottom. | `int` |
| `offset_x` | The horizontal offset in pixels of the photo from the left. | `int` |
| `description` | A brief description of the Group. | `string` |
| `email` | The email address to upload content to the Group. Only current members of the Group can use this. | `string` |
| `icon` | The URL for the Group's icon. | `string` |
| `member_count` | The number of members in the Group. | `int` |
| `member_request_count` | The number of pending member requests. Requires an access token of an Admin of the Group.we The count is only returned when the number of pending member requests is over 50. | `int` |
| `name` | The name of the Group. | `string` |
| `owner` | _Deprecated in v9.0+. Will be deprecated in all versions February 9, 2021._ | `User` \| `Page` |
| `parent` | The parent of this Group, if it exists. | `Group` \| `Page` |
| `permissions` | The permissions a User has granted for an app installed in the Group. | `string` |
| `privacy` | The privacy setting of the Group. Possible values are `CLOSED`, `OPEN`, and `SECRET`. Requires an access token of an Admin of the Group. | `string` |
| `updated_time` | The last time the Group was updated (includes changes Group properties, Posts, and Comments). Requires an access token of an Admin of the Group. | `datetime` |

[](#)

Creating
--------

This operation is not supported.

[](#)

Updating
--------

This operation is not supported.

[](#)

Deleting
--------

This operation is not supported.

[](#)

Edges
-----

| Name | Description |
| --- | --- |
| [`/admins`](https://developers.facebook.com/docs/graph-api/reference/group/admins) | _This edge was deprecated on April 4th, 2018._ |
| [`/albums`](https://developers.facebook.com/docs/graph-api/reference/group/albums) | Photo albums owned by the Group. |
| [`/docs`](https://developers.facebook.com/docs/graph-api/reference/group/docs) | Documents owned by the Group. |
| [`/events`](https://developers.facebook.com/docs/graph-api/reference/group/events) | Events owned by the Group. |
| [`/feed`](https://developers.facebook.com/docs/graph-api/reference/group/feed) | Feed of Posts owned by the Group. |
| [`/files`](https://developers.facebook.com/docs/graph-api/reference/group/files) | Files owned by the Group. |
| [`/live_videos`](https://developers.facebook.com/docs/graph-api/reference/live-video/) | Live Videos owned by the Group. |
| [`/members`](https://developers.facebook.com/docs/graph-api/reference/group/members/) | _This edge was deprecated on April 4th, 2018._ |
| [`/photos`](https://developers.facebook.com/docs/graph-api/reference/group/photos) | Photos owned by the Group. |
| [`/videos`](https://developers.facebook.com/docs/graph-api/reference/group/videos) | Videos owned by the Group. |

[](#)

[](#)

This edge was deprecated on April 4th, 2018, and can no longer be used.

Admins
======

The Admins of a Group.

[](#)

Reading
-------

An Admin of the Group can get a list of other Group Admins.

HTTPPHP SDKAndroid SDKiOS SDK

    GET /v18.0/{group-id}/admins HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{group-id}/admins',
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
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{group-id}/admins",
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
                                   initWithGraphPath:@"/{group-id}/admins"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### Permissions

A User access token of an Admin of the Group.

[](#)

Creating
--------

This operation is not supported.

[](#)

Deleting
--------

This operation is not supported.

[](#)

Updating
--------

This operation is not supported.

[](#)

[](#)

Group Albums
============

The photo albums created for a Group.

[](#)

Reading
-------

Returns an array of [Albums](https://developers.facebook.com/docs/reference/api/album/) on the Group.

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bgroup-id%7D%2Falbums&version=v18.0)

    GET /v18.0/{group-id}/albums HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{group-id}/albums',
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
        "/{group-id}/albums",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{group-id}/albums",
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
                                   initWithGraphPath:@"/{group-id}/albums"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### Requirements

| Requirement | Description |
| --- | --- |
| [App Review](https://developers.facebook.com/docs/apps/review) | Your app must be approved for the [Groups API](https://developers.facebook.com/docs/groups-api/) feature. |
| [App Installation](https://developers.facebook.com/docs/groups-api#app-installation) | The app must be installed on the Group. |
| [Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens) | A User access token. |

### Fields

When requesting the following Album fields through field expansion, only Users who granted your app the `groups_access_member_info` permission will be included:

* `from`
* `likes`
* `reaction`

[](#)

Publishing
----------

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK

    POST /v18.0/{group-id}/albums HTTP/1.1
    Host: graph.facebook.com
    
    name=%7Balbum-name%7D&message=%7Balbum-description%7D&privacy=%7Bprivacy-settings%7D

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->post(
        '/{group-id}/albums',
        array (
          'name' => '{album-name}',
          'message' => '{album-description}',
          'privacy' => '{privacy-settings}',
        ),
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
        "/{group-id}/albums",
        "POST",
        {
            "name": "{album-name}",
            "message": "{album-description}",
            "privacy": "{privacy-settings}"
        },
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    Bundle params = new Bundle();
    params.putString("name", "{album-name}");
    params.putString("message", "{album-description}");
    params.putString("privacy", "{privacy-settings}");
    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{group-id}/albums",
        params,
        HttpMethod.POST,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    NSDictionary *params = @{
      @"name": @"{album-name}",
      @"message": @"{album-description}",
      @"privacy": @"{privacy-settings}",
    };
    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{group-id}/albums"
                                          parameters:params
                                          HTTPMethod:@"POST"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### Requirements

| Type of Requirement | Description |
| --- | --- |
| [App Review](https://developers.facebook.com/docs/apps/review) | Your app must be approved for the following login permissions and features: (Click to expand) |
| Login permissions | `publish_to_groups` |
| Features | [Groups API](https://developers.facebook.com/docs/groups-api/) |
| [App Installation](https://developers.facebook.com/docs/groups-api#app-installation) | The app must be installed on the Group. |
| [Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens) | A User access token for a user who is a member of the Group where the app is installed. |
| [Permissions](https://developers.facebook.com/docs/facebook-login/permissions/) | The user must grant your app this permission:<br><br>`publish_to_groups` |

### Fields

| Parameter | Description | Type |
| --- | --- | --- |
| `name` | The name given to the album. This field is required. | `string` |
| `message` | The description of the album, which will show up in Feed as the status message. | `string` |

#### Response

| Name | Description | Type |
| --- | --- | --- |
| id  | The ID of the newly created album. | `string` |

[](#)

Deleting
--------

This operation is not supported.

[](#)

Updating
--------

This operation is not supported.

[](#)

[](#)

Group Docs
==========

The documents owned by a Group.

[](#)

Reading
-------

Returns a list of [Group Docs](https://developers.facebook.com/docs/graph-api/reference/groupdoc).

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bgroup-id%7D%2Fdocs&version=v18.0)

    GET /v18.0/{group-id}/docs HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{group-id}/docs',
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
        "/{group-id}/docs",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{group-id}/docs",
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
                                   initWithGraphPath:@"/{group-id}/docs"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### Requirements

| Type | Description |
| --- | --- |
| [App Review](https://developers.facebook.com/docs/apps/review) | Your app must be approved for the [Groups API](https://developers.facebook.com/docs/groups-api/) feature. |
| [App Installation](https://developers.facebook.com/docs/groups-api#app-installation) | The app must be installed on the Group. |
| [Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens) | A User access token. |

[](#)

Creating
--------

This operation is not supported.

[](#)

Updating
--------

This operation is not supported.

[](#)

Deleting
--------

This operation is not supported.

[](#)

[](#)

Group Feed
==========

Posts owned by a Group, including status updates and links.

[](#)

Reading
-------

Returns an array of [Posts](https://developers.facebook.com/docs/reference/api/post) on the Group.

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bgroup-id%7D%2Ffeed&version=v18.0)

    GET /v18.0/{group-id}/feed HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{group-id}/feed',
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
        "/{group-id}/feed",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{group-id}/feed",
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
                                   initWithGraphPath:@"/{group-id}/feed"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### Requirements

| Type of Requirement | Description |
| --- | --- |
| [App Review](https://developers.facebook.com/docs/apps/review) | Your app must be approved for the [Groups API](https://developers.facebook.com/docs/groups-api/) feature. |
| [App Installation](https://developers.facebook.com/docs/groups-api#app-installation) | The app must be installed on the Group. |
| [Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens) | A User access token or a Page access token. |

### Notes

* The `since` and `until` params apply on the `updated_time` field.
    

[](#)

Publishing
----------

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK

    POST /v18.0/{group-id}/feed HTTP/1.1
    Host: graph.facebook.com
    
    message=This+is+a+test+message

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->post(
        '/{group-id}/feed',
        array (
          'message' => 'This is a test message',
        ),
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
        "/{group-id}/feed",
        "POST",
        {
            "message": "This is a test message"
        },
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    Bundle params = new Bundle();
    params.putString("message", "This is a test message");
    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{group-id}/feed",
        params,
        HttpMethod.POST,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    NSDictionary *params = @{
      @"message": @"This is a test message",
    };
    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{group-id}/feed"
                                          parameters:params
                                          HTTPMethod:@"POST"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### Requirements

| Type of Requirement | Description |
| --- | --- |
| [App Review](https://developers.facebook.com/docs/apps/review) | Your app must be approved for the following login permissions and features: (Click to expand) |
| Login permissions | `publish_to_groups` |
| Features | [Groups API](https://developers.facebook.com/docs/groups-api/) |
| [App Installation](https://developers.facebook.com/docs/groups-api#app-installation) | The app must be installed on the Group. |
| [Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens) | A User access token of a member of the Group. |
| [Permissions](https://developers.facebook.com/docs/facebook-login/permissions/) | The user must grant your app the following permissions:<br><br>`publish_to_groups` |

### Fields

| Name | Type | Description |
| --- | --- | --- |
| `message` | `string` | The main body of the post, otherwise called the status message. Either `link` or `message` must be supplied. |
| `link` | `string` | The URL of a link to attach to the post. Either `link` or `message` must be supplied. Additional fields associated with `link` are shown below. |

### Response

If successful, you will receive a response with the following information. In addition, this endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/overview#read-after-write) and can immediately return any fields returned by [read](https://developers.facebook.com/docs/graph-api/reference/group/feed#read) operations.

| Name | Description | Type |
| --- | --- | --- |
| `id` | The newly created post ID | `string` |

[](#)

Updating
--------

This operation is not supported.

[](#)

Deleting
--------

This operation is not supported.

[](#)

[](#)

Group Events
============

All events that belong to a group.

[](#)

Reading
-------

Returns a list of [Facebook Events](https://developers.facebook.com/docs/graph-api/reference/event).

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bgroup-id%7D%2Fevents&version=v18.0)

    GET /v18.0/{group-id}/events HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{group-id}/events',
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
        "/{group-id}/events",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{group-id}/events",
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
                                   initWithGraphPath:@"/{group-id}/events"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### Requirements

| Type of Requirement | Description |
| --- | --- |
| [App Review](https://developers.facebook.com/docs/apps/review) | Your app must be approved for the [Groups API](https://developers.facebook.com/docs/groups-api/) feature. |
| [App Installation](https://developers.facebook.com/docs/groups-api#app-installation) | The app must be installed on the Group. |
| [Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens) | A User access token. |

### Fields

By default, this will only return events within the last two weeks. Use the [`until` or `since` parameters](https://developers.facebook.com/docs/graph-api/using-graph-api#paging) to modify this range.

[](#)

Publishing
----------

This operation is not supported.

[](#)

Deleting
--------

This operation is not supported.

[](#)

Updating
--------

This operation is not supported.

[](#)

[](#)

Group Files
===========

The files uploaded to this group.

[](#)

Reading
-------

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bgroup-id%7D%2Ffiles&version=v18.0)

    GET /v18.0/{group-id}/files HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{group-id}/files',
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
        "/{group-id}/files",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{group-id}/files",
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
                                   initWithGraphPath:@"/{group-id}/files"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### Requirements

| Type of Requirement | Description |
| --- | --- |
| [App Review](https://developers.facebook.com/docs/apps/review) | Your app must be approved for the [Groups API](https://developers.facebook.com/docs/groups-api/) feature. |
| [App Installation](https://developers.facebook.com/docs/groups-api#app-installation) | The app must be installed on the Group. |
| [Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens) | A User access token. |

### Fields

| Name | Description | Type |
| --- | --- | --- |
| `download_link` | URL to download the file. | `string` |
| `group` | The Group the file is uploaded to (the same Group as in the request). | [`Group`](https://developers.facebook.com/docs/graph-api/reference/group) |
| `id` | The ID of the file. Note that you cannot request each file individually by its ID, only through this edge. | `string` |
| `message` | The text included with the file post. | `string` |
| `updated_time` | The last time the file was changed. | `datetime` |

[](#)

Publishing
----------

This operation is not supported.

[](#)

Deleting
--------

This operation is not supported.

[](#)

Updating
--------

This operation is not supported.

[](#)

[](#)

This edge was deprecated on April 4th, 2018, and can no longer be used.

Members
=======

The members of a Group.

[](#)

Reading
-------

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bgroup-id%7D%2Fmembers&version=v18.0)

    GET /v18.0/{group-id}/members HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{group-id}/members',
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
        "/{group-id}/members",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{group-id}/members",
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
                                   initWithGraphPath:@"/{group-id}/members"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### Permissions

A User access token of an Admin of the Group with the following permissions:

* `user_managed_groups`
    

### Fields

A list of [User objects](https://developers.facebook.com/docs/graph-api/reference/user/) and one additional field:

| Name | Description | Type |
| --- | --- | --- |
| `administrator` | Whether or not the person is a group admin. | `boolean` |

[](#)

Creating
--------

This operation is not supported.

[](#)

Updating
--------

This operation is not supported.

[](#)

Deleting
--------

This operation is not supported.

[](#)

[](#)

[`/{group-id}`](https://developers.facebook.com/docs/graph-api/reference/group/)`/opted_in_members`
===================================================================================================

This edge allows you to get a list of Users on the Group who have chosen to share their publicly available profile information with apps installed on the Group.

[](#)

Creating
--------

This operation is not supported.

[](#)

Reading
-------

Returns a list of Users. These are the Group members who have granted the app permission to access their public information.

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bgroup-id%7D%2Fopted_in_members&version=v18.0)

    GET /v18.0/{group-id}/opted_in_members HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{group-id}/opted_in_members',
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
        "/{group-id}/opted_in_members",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{group-id}/opted_in_members",
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
                                   initWithGraphPath:@"/{group-id}/opted_in_members"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### Permissions

* A User or a Page access token of an admin of the Group.
    
* The app must be installed in the Group.
    

### Fields

Returns a list of [User](https://developers.facebook.com/docs/graph-api/reference/user/) nodes.

[](#)

Publishing
----------

This operation is not supported.

[](#)

Deleting
--------

This operation is not supported.

[](#)

Updating
--------

This operation is not supported.

[](#)

[](#)

Group Photos
============

[](#)

Reading
-------

You can't perform this operation on this endpoint.

[](#)

Creating
--------

Animated photos are not supported, and a photo must be less than 10MB in size.

You can make a POST request to `photos` edge from the following paths:

* [`/{group_id}/photos`](https://developers.facebook.com/docs/graph-api/reference/group/photos/)

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
| `direct_share_status`<br><br>int64 | The status to allow sponsor directly boost the post |
| `feed_targeting`<br><br>feed target | Object that controls [Feed targeting](https://www.facebook.com/help/352402648173466) for this post. Anyone in these groups will be more likely to see this post. People not in these groups will be less likely to see this post, but may still see it anyway. Any of the targeting fields shown here can be used, but none are required. `feed_targeting` applies to Pages only |
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
| `filter_type`<br><br>int64 | Default value: `-1`<br><br>Filter type |
| `full_res_is_coming_later`<br><br>boolean | Default value: `false`<br><br>Full res is coming later |
| `initial_view_heading_override_degrees`<br><br>int64 | Manually specify the initial view heading in degrees from 0 to 360. This overrides any value present in the photo embedded metadata or provided in the spherical\_metadata parameter |
| `initial_view_pitch_override_degrees`<br><br>int64 | Manually specify the initial view pitch in degrees from -90 to 90. This overrides any value present in the photo embedded metadata or provided in the spherical\_metadata parameter |
| `initial_view_vertical_fov_override_degrees`<br><br>int64 | Manually specify the initial view vertical FOV in degrees from 60 to 120. This overrides any value present in the photo embedded metadata or provided in the spherical\_metadata parameter |
| `ios_bundle_id`<br><br>string | iOS Bundle ID |
| `is_explicit_location`<br><br>boolean | Is an explicit location |
| `is_explicit_place`<br><br>boolean | If set to `true`, the tag is a place, not a person |
| `manual_privacy`<br><br>boolean | Default value: `false`<br><br>Manual privacy |
| `message`<br><br>UTF-8 string | Deprecated. Please use the caption param instead<br><br>DeprecatedSupports Emoji |
| `name`<br><br>UTF-8 string | Deprecated. Please use the caption param instead<br><br>DeprecatedSupports Emoji |
| `no_story`<br><br>boolean | If set to `true`, this will suppress the Feed story that is automatically generated on a profile when people upload a photo using your app. Useful for adding old photos where you may not want to generate a story |
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
| `target_id`<br><br>int | Do not use. Specifying a `target_id` allows you to post the photo to an object that's not the user in the access token. It only works when posting directly to the `/photos` endpoint. Instead of using this parameter you should be using the edge on an object directly, like `/page/photos` |
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
| 100 | Invalid parameter |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 190 | Invalid OAuth 2.0 Access Token |
| 120 | Invalid album id |
| 324 | Missing or invalid image file |

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Group Videos
============

[Videos](https://developers.facebook.com/docs/reference/api/video/) owned by a Facebook Group.

[](#)

Reading
-------

Returns an array of [Video](https://developers.facebook.com/docs/reference/api/video/) objects.

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bgroup-id%7D%2Fvideos&version=v18.0)

    GET /v18.0/{group-id}/videos HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{group-id}/videos',
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
        "/{group-id}/videos",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{group-id}/videos",
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
                                   initWithGraphPath:@"/{group-id}/videos"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### Requirements

| Type of Requirement | Description |
| --- | --- |
| [App Review](https://developers.facebook.com/docs/apps/review) | Your app must be approved for the [Groups API](https://developers.facebook.com/docs/groups-api/) feature. |
| [App Installation](https://developers.facebook.com/docs/groups-api#app-installation) | The app must be installed on the Group. |
| [Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens) | A User access token. |

[](#)

Creating
--------

This operation is not supported.

To publish videos to User timelines, Groups, or Pages, please use the [Sharing Dialog](https://developers.facebook.com/docs/sharing).

[](#)

Updating
--------

This operation is not supported.

[](#)

Deleting
--------

This operation is not supported.

[](#)

[](#)