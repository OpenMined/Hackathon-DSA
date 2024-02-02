`/{object-id}/comments`
=======================

This reference describes the `/comments` edge that is common to multiple Graph API nodes. The structure and operations are the same for each node. The following objects have a `/comments` edge:

|     |     |     |
| --- | --- | --- |
| * [Album](https://developers.facebook.com/docs/graph-api/reference/album/)<br>    <br>* [Comment](https://developers.facebook.com/docs/graph-api/reference/comment/)<br>    <br>* [Event](https://developers.facebook.com/docs/graph-api/reference/event/)<br>    <br>* [Link](https://developers.facebook.com/docs/graph-api/reference/link/) | * [Live Video](https://developers.facebook.com/docs/graph-api/reference/live-video/)<br>    <br>* [Photo](https://developers.facebook.com/docs/graph-api/reference/photo/)<br>    <br>* [Post](https://developers.facebook.com/docs/graph-api/reference/post/) | * [Thread](https://developers.facebook.com/docs/graph-api/reference/thread/)<br>    <br>* [User](https://developers.facebook.com/docs/graph-api/reference/user/)<br>    <br>* [Video](https://developers.facebook.com/docs/graph-api/reference/video/) |

It is possible for comment objects to have a `/comments` edge, which is called _comment replies_. The structure is the same for these, but attention should be paid to the [modifiers](#readmodifiers) for these edges.

[](#)

Reading
-------

Returns a comment on an object.

The `id` field for the `/PAGEPOST-ID/comments` endpoint will no longer be returned for apps using the [Page Public Content Access feature](https://developers.facebook.com/docs/pages/overview/permissions-features#features). To access the comment IDs for a Page post you must be able to perform the [MODERATE task](https://developers.facebook.com/docs/pages/overview/permissions-features#tasks) on the Page being queried. This change is in effect for v11.0+ and will be implement for all versions on September, 7, 2021.

### New Page Experience

The following objects `/comments` endpoint are supported for New Page Experience:

|     |     |
| --- | --- |
| * Album<br>* Comment<br>* Link<br>* Page | * PagePost<br>* Photo<br>* Post<br>* PostComment |

### Permissions

* The same permissions required to view the parent object are required to view comments on that object.

### Limitations

* Other users' profile information and comments will not be returned when accessing user posts, photos, albums, videos, likes, and reactions unless authorized by those users.
    
* Comments returned in a query are based on default filtering. To get all comments that can be returned depending on your permissions, set the `filter` parameter to `stream` or use the `order` field.
    
* A [new Page](https://www.facebook.com/business/help/2752670058165459?id=418112142508425) can comment as the Page on new Pages or classic Pages. However, a classic Page can not comment on a new Page.
    
* For the following nodes, the `/comments` endpoint returns empty data if you read it with a [User access token](https://developers.facebook.com/docs/facebook-login/access-tokens):
    
    * [Album](https://developers.facebook.com/docs/graph-api/reference/album/)
        
    * [Photo](https://developers.facebook.com/docs/graph-api/reference/photo/)
        
    * [Post](https://developers.facebook.com/docs/graph-api/reference/post/)
        
    * [Video](https://developers.facebook.com/docs/graph-api/reference/video/)
        
    
* The `id` field for the [`/PAGEPOST-ID/comments` endpoint](https://developers.facebook.com/docs/graph-api/reference/pagepost/) will no longer be returned for apps using the [Page Public Content Access feature](https://developers.facebook.com/docs/pages/overview/permissions-features#features). To access the comment IDs for a Page post you must be able to perform the [MODERATE task](https://developers.facebook.com/docs/pages/overview/permissions-features#tasks) on the Page being queried.
    
* For objects that have tens of thousands of comments, you may encounter limits while [paging](https://developers.facebook.com/docs/graph-api/using-graph-api#paging). Learn more about paging in our [Using the Graph API Guide](https://developers.facebook.com/docs/graph-api/using-graph-api).
    

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bobject-id%7D%2Fcomments&version=v18.0)

    GET /v18.0/{object-id}/comments HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{object-id}/comments',
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
        "/{object-id}/comments",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{object-id}/comments",
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
                                   initWithGraphPath:@"/{object-id}/comments"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### Parameters

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK

    GET /v18.0/{object-id}/comments?summary=1&filter=toplevel HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{object-id}/comments?summary=1&filter=toplevel',
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
        "/{object-id}/comments",
        {
            "summary": true,
            "filter": "toplevel"
        },
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    Bundle params = new Bundle();
    params.putBoolean("summary", true);
    params.putString("filter", "toplevel");
    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{object-id}/comments",
        params,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    NSDictionary *params = @{
      @"summary": @YES,
      @"filter": @"toplevel",
    };
    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{object-id}/comments"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

| Parameter | Description |
| --- | --- |
| `summary`<br><br>_bool_ | A summary of metadata about the comments on the object. Importantly this metadata includes `order` which indicates how the comments are being sorted. |
| `filter`<br><br>_enum { toplevel, stream }_ | If a person can reply to a comment, you can filter comments based on top level comments, comments that are made directly on the post, or the chronological order of all comments.<br><br>* `toplevel` - This is the default. It returns all top-level comments in chronological order, as ordered on Facebook. This filter is useful for displaying comments in the same structure as they appear on Facebook.<br>* `stream` - All-level comments in `chronological` order. This filter is useful for comment moderation tools where it is helpful to see a chronological list of all comments. |

### Fields

An array of [Comment objects](https://developers.facebook.com/docs/graph-api/reference/comment/) in addition to the following fields when `summary` is `true` in the request.

| Field | Description |
| --- | --- |
| `order`<br><br>_enum { chronological, reverse\_chronological }_ | Order in which comments were returned.<br><br>* `chronological`: Comments sorted by the oldest comments first.<br>* `reverse_chronological`: Comments sorted by the newest comments first. |
| `total_count`<br><br>_int32_ | The count of comments on this node. It is important to note that this value changes depending on the `filter` being used (where comment replies are available):<br><br>* if `filter` is `stream` then `total_count` will be a count of all comments (including replies) on the node.<br>* if `filter` is `toplevel` then `total_count` will be a count of all top-level comments on the node.<br><br>Note: `total_count` can be greater than or equal to the actual number of comments returned due to comment privacy or deletion. |

[](#)

Publishing
----------

Publish new comments to any object.

### New Page Experience

The following objects `/comments` endpoint are supported for New Page Experience:

|     |     |
| --- | --- |
| * Comments<br>* PagePosts<br>* Photo<br>* Post | * PostComment<br>* Video |

### Permissions

* A Page access token requested by a person who can perform the `MODERATE` task on the Page
    
* The `pages_manage_engagement` permission
    

Note, the `can_comment` field on individual [comment objects](https://developers.facebook.com/docs/graph-api/reference/comment/) indicates whether it is possible to reply to that comment.

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK

    POST /v18.0/{object-id}/comments HTTP/1.1
    Host: graph.facebook.com
    
    message=This+is+a+test+comment

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->post(
        '/{object-id}/comments',
        array (
          'message' => 'This is a test comment',
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
        "/{object-id}/comments",
        "POST",
        {
            "message": "This is a test comment"
        },
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    Bundle params = new Bundle();
    params.putString("message", "This is a test comment");
    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{object-id}/comments",
        params,
        HttpMethod.POST,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    NSDictionary *params = @{
      @"message": @"This is a test comment",
    };
    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{object-id}/comments"
                                          parameters:params
                                          HTTPMethod:@"POST"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### Fields

| Name | Description |
| --- | --- |
| `attachment_id`<br><br>_string_ | An optional ID of a unpublished photo (see `no_story` field in [`/{user-id}/photos`](https://developers.facebook.com/docs/graph-api/reference/user/photos/#publish)) uploaded to Facebook to include as a photo comment. One of `attachment_id`, `attachment_share_url`, `attachment_url`, `message`, or `source` must be provided when publishing. |
| `attachment_share_url`<br><br>_string_ | The URL of a GIF to include as a animated GIF comment. One of `attachment_id`, `attachment_share_url`, `attachment_url`, `message`, or `source` must be provided when publishing. |
| `attachment_url`<br><br>_string_ | The URL of an image to include as a photo comment. One of `attachment_id`, `attachment_share_url`, `attachment_url`, `message`, or `source` must be provided when publishing. |
| `source`<br><br>_[multipart/form-data](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.w3.org%2FTR%2Fhtml401%2Finteract%2Fforms.html%23h-17.13.4.2&h=AT1B_welIoHVZ_yCIjRGO_mTq55r0_1w5ocMHXx4ZpCyULkGJXrC7qP3EeIktScqVbnInKiftqSwhHkpipWPNurdpUqlPoRuQPkaRbL5rkcVomRXSP_7drlzDgWPKihGHOOe34mg9IaAGPTCYpyVBEXMYaDM0w6S5u8)_ | A photo, encoded as form data, to use as a photo comment. One of `attachment_id`, `attachment_share_url`, `attachment_url`, `message`, or `source` must be provided when publishing. |
| `message`<br><br>_string_ | The comment text. One of `attachment_id`, `attachment_share_url`, `attachment_url`, `message`, or `source` must be provided when publishing.<br><br>Mention other Facebook Pages in your `message` text using the following syntax:<br><br>`@[page-id]`<br><br>Usage of [this feature is subject to review](https://developers.facebook.com/docs/apps/review/feature#reference-MENTIONING). |

### Return Type

If successful, you will receive a JSON response with the newly created comment ID. In addition, this endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/using-graph-api#read-after-write) and can immediately return any fields returned by [read](https://developers.facebook.com/docs/graph-api/reference/object/comments#read) operations.

{
  "id": "{comment-id}"
}

[](#)

Updating
--------

You can't update using this edge.

[](#)

Deleting
--------

You can't delete using this edge.

Delete individual comments using the [/comment-id endpoint](https://developers.facebook.com/docs/graph-api/reference/comment/).

[](#)

[](#)

`/{object-id}/likes`
====================

This reference describes the `/likes` edge that is common to multiple Graph API nodes. The structure and operations are the same for each node. The following objects have a `/likes` edge:

|     |     |
| --- | --- |
| * [Album](https://developers.facebook.com/docs/graph-api/reference/album)<br>* [Comment](https://developers.facebook.com/docs/graph-api/reference/comment)<br>* [Page](https://developers.facebook.com/docs/graph-api/reference/page)<br>* [Photo](https://developers.facebook.com/docs/graph-api/reference/photo)<br>* [User](https://developers.facebook.com/docs/graph-api/reference/user)<br>* [Video](https://developers.facebook.com/docs/graph-api/reference/video) |     |

[](#)

Reading
-------

Returns the list of people who liked this object. When reading likes on a Page or User object, this endpoint returns a list of pages liked by that Page or User.

Use the `likes` field of an object to get the number of likes.

We recommended that you use the [`/object/reactions` endpoint](https://developers.facebook.com/docs/graph-api/reference/object/reactions) to get like counts, if available.

### New Page Experience

The following objects `/likes` endpoint are supported for New Page Experience:

|     |     |
| --- | --- |
| * [Album](https://developers.facebook.com/docs/graph-api/reference/album)<br>* [Comment](https://developers.facebook.com/docs/graph-api/reference/comment)<br>* [Photo](https://developers.facebook.com/docs/graph-api/reference/photo)<br>* [PagePost](https://developers.facebook.com/docs/graph-api/reference/pagepost) | * User |

### Requirements

* The same requirements required to view the object are required to view likes on that object.

### Limitations

* Only aggregated counts using `total_count` with the `summary` parameter are available for Post likes.
    
* The `like` reaction counts include both "like" and "care" reactions.
    
* `total_count` represents the approximate number of likes, however, the actual number returned might be different depending on privacy settings.
    
* The `GET /{group-post-id}/likes` and `GET /{post-id}/likes` endpoints are deprecated in v8.0+ and deprecated in all versions on Nov. 2, 2020.
    

### Fields

| Property Name | Description | Type |
| --- | --- | --- |
| `total_count` | Total number of User and Page likes on the object. To have this field returned, you must include the `summary=true` parameter and value in your request. | `int32` |

### Example Usage

**Sample Request**

curl \-i \-X GET "https://graph.facebook.com/{object-id}
  ?fields=likes.summary(true)
  &access\_token={access-token}"

#### Sample Response

  {
  "likes": {
    "data": \[
      {
        "name": "Bill the Cat",
        "id": "155111347875779",
        "created\_time": "2017-06-18T18:21:04+0000"
      },
      {
        "name": "Calvin and Hobbes",
        "id": "257573197608192",
        "created\_time": "2017-06-18T18:21:02+0000"
      },
      {
        "name": "Berkeley Breathed's Bloom County",
        "id": "108793262484769",
        "created\_time": "2017-06-18T18:20:58+0000"
      }
    \],
    "paging": {
      "cursors": {
        "before": "Nzc0Njg0MTQ3OAZDZD",
        "after": "NTcxODc1ODk2NgZDZD"
      },
      "next": "https://graph.facebook.com/vX.X/me/likes?access\_token=user-access-token&pretty=0&summary=true&limit=25&after=NTcxODc1ODk2NgZDZD"
    },
    "summary": {
      "total\_count": 136
    }
  },
  "id": "user-id"
}

[](#)

Publish
-------

Like an object.

### New Page Experience

The following objects `/likes` endpoint are supported for New Page Experience:

|     |     |
| --- | --- |
| * [Album](https://developers.facebook.com/docs/graph-api/reference/album)<br>* [Comment](https://developers.facebook.com/docs/graph-api/reference/comment)<br>* PagePost |     |

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK

    POST /v18.0/{object-id}/likes HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->post(
        '/{object-id}/likes',
        array (),
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
        "/{object-id}/likes",
        "POST",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{object-id}/likes",
        null,
        HttpMethod.POST,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{object-id}/likes"
                                          parameters:params
                                          HTTPMethod:@"POST"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### Permissions

* A Page access token requested by a person who can perform the [`CREATE_CONTENT` task](https://developers.facebook.com/docs/pages/overview-1#tasks) on the Page
    
* The `pages_manage_engagement` permission
    

### Limitations

* The Page must also be able to like the object (whether via API or on Facebook.com).
    
* The object must not have already been liked by the Page.
    
* If the Page has already reacted to an object (wow, sad) then a like will succeed, but the reaction will not change.
    
* Liking a Page review is not supported.
    

### Fields

No fields are required to add likes.

### Response

On success, your app will receive the following response:

{
  "success": true
}

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Delete
------

Delete likes on Page objects using this endpoint.

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK

    DELETE /v18.0/{object-id}/likes HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->delete(
        '/{object-id}/likes',
        array (),
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
        "/{object-id}/likes",
        "DELETE",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{object-id}/likes",
        null,
        HttpMethod.DELETE,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{object-id}/likes"
                                          parameters:params
                                          HTTPMethod:@"DELETE"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### Permissions

* A Page access token requested by a person who can perform the [`MODERATE` task](https://developers.facebook.com/docs/pages/overview-1#tasks) on the Page
    
* The `pages_manage_engagement` permission
    

### Limitations

* A User or Page can only delete their own `likes`.
    
* The object must have already been liked.
    
* Deleting a Page review like is not supported.
    

### Fields

There are no fields for this endpoint.

### Response

On success, your app will receive the following response:

{
  "success": true
}

[](#)

[](#)

`/{object-id}/private_replies`
==============================

#### Legacy Private Replies are deprecated for v5.0+

On October 29, 2019 we announced that this endpoint is now deprecated. Please use the new [Private Replies](https://developers.facebook.com/docs/messenger-platform/discovery/private-replies)

As part of the V3.3 changes the `read_page_mailboxes` permission was deprecated. Use `pages_messaging` permission to access this endpoint. The `read_page_mailboxes` permission will stop working after June 30 2020

This edge is the **Legacy Private Replies** allows Pages to reply to Post Comments and Visitor Posts with a plain text only message. It can be used with the following nodes:

* [`Comment`](https://developers.facebook.com/docs/graph-api/reference/comment)
    
* [`Post`](https://developers.facebook.com/docs/graph-api/reference/post)
    

Please note that a comment or post may only be replied to once.

[](#)

Reading
-------

You can't read using this edge.

[](#)

Publishing
----------

To reply with a private Message:

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK

    POST /v18.0/{object-id}/private_replies HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->post(
        '/{object-id}/private_replies',
        array (),
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
        "/{object-id}/private_replies",
        "POST",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{object-id}/private_replies",
        null,
        HttpMethod.POST,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{object-id}/private_replies"
                                          parameters:params
                                          HTTPMethod:@"POST"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

Private replies to posts or comments are allowed within 7 days of the creation date of the user post or comment.

Permissions
-----------

This edge requires a Page access token with the following permissions:

* `pages_messaging`

Apps with Standard Access can only send and receive messages from people who have a role on your app. Additionally Pages in `unpublished` status will only be allowed to message people with a role on the Page.

### Fields

| Parameter | Description | Type |
| --- | --- | --- |
| `id` | The ID of the Page Comment or Visitor Post that you are replying to. | `string` |
| `message` | The text of the reply. **This field is required**. | `string` |

### Response

If successful, you will receive a response with the following fields. In addition, this endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/using-graph-api#read-after-write) and can immediately read the node represented by `id` in the return type.

| Field | Description | Type |
| --- | --- | --- |
| id  | The ID of the newly created Message. | `string` |

[](#)

Deleting
--------

You can't delete using this edge.

[](#)

Updating
--------

You can't update using this edge.

[](#)

[](#)

Object Reactions
================

This reference describes the `/reactions` edge that is common to multiple Graph API nodes. The structure and operations are the same for each node. The following objects have a `/reactions` edge:

|     |     |
| --- | --- |
| * [Comment](https://developers.facebook.com/docs/graph-api/reference/comment)<br>* [PagePost](https://developers.facebook.com/docs/graph-api/reference/pagepost)<br>* [Post](https://developers.facebook.com/docs/graph-api/reference/post) |     |

[](#)

Reading
-------

Get reactions on an object.

View [Insights](https://developers.facebook.com/docs/graph-api/reference/insights#availmetrics) for more information on Page and Post reactions.

### New Page Experience

This endpoint is supported for New Page Experience.

### Requirements

**Marketing Apps**

* `ads_management`
* `pages_read_engagement`
* `pages_show_list`

**Page Management Apps**

* `pages_show_list`

### Sample Request

The following example is a `GET` request made by a User who has reacted to their own object.

cURLAndroid SDKObjective-CJava SDKPHP SDK

    curl -i -X GET \
     "https://graph.facebook.com/your-post-id/reactions?access_token=your-user-access-token"

    GraphRequest request = GraphRequest.newGraphPathRequest(
      accessToken,
      "/your-post-id/reactions",
      new GraphRequest.Callback() {
        @Override
        public void onCompleted(GraphResponse response) {
          // Insert your code here
        }
    });
    
    request.executeAsync();

    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
        initWithGraphPath:@"/your-post-id/reactions"
               parameters:nil
               HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection, id result, NSError *error) {
        // Insert your code here
    }];

    FB.api(
      '/your-post-id/reactions',
      'GET',
      {},
      function(response) {
          // Insert your code here
      }
    );

    try {
      // Returns a `FacebookFacebookResponse` object
      $response = $fb->get(
        '/your-post-id/reactions',
        '{access-token}'
      );
    } catch(FacebookExceptionsFacebookResponseException $e) {
      echo 'Graph returned an error: ' . $e->getMessage();
      exit;
    } catch(FacebookExceptionsFacebookSDKException $e) {
      echo 'Facebook SDK returned an error: ' . $e->getMessage();
      exit;
    }
    $graphNode = $response->getGraphNode();

#### The JSON Response

{
  "data": \[
    {
      "id": "your-user-id",
      "name": "Your Name",
      "type": "HAHA"
    }
  \],
  "paging": {
    "cursors": {
      "before": "QVFIUk5YbXFFbG8yVWVOa2w0ZAGhmSUNKMkZAZAOXZARbzJOMHM0TUFtZAnhJbWdPdkF4OURUTHJrQjFqQ2RQZAVN1UGxSVU5FWURENnE4OUFPeXFreU1jV09pdFJR",
      "after": "QVFIUkpsWVRkcVl6SlhsdWlrcGdudl8xVEhwVEJ5ZA3FXdG90bTRxam13NmJDUGpQVnB5ZA29lMG9FVmFaeU1BLW1hc2oZD"
    }
  }
}

If the User or Page has not reacted to the object being queried, `data` will be empty.

The following example is a `GET` request for the total reactions to an object.

cURLAndroid SDKObjective-CJava SDKPHP SDK

    curl -i -X GET \
     "https://graph.facebook.com/your-post-id
       ?fields=reactions.summary(total_count)
       &access_token=your-access-token"

    GraphRequest request = GraphRequest.newGraphPathRequest(
      accessToken,
      "/your-post-id",
      new GraphRequest.Callback() {
        @Override
        public void onCompleted(GraphResponse response) {
          // Insert your code here
        }
    });
    
    Bundle parameters = new Bundle();
    parameters.putString("fields", "reactions.summary(total_count)");
    request.setParameters(parameters);
    request.executeAsync();

    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
        initWithGraphPath:@"/your-post-id"
               parameters:@{ @"fields": @"reactions.summary(total_count)",}
               HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection, id result, NSError *error) {
        // Insert your code here
    }];

    FB.api(
      '/your-post-id',
      'GET',
      {"fields":"reactions.summary(total_count)"},
      function(response) {
          // Insert your code here
      }
    );

    try {
      // Returns a `FacebookFacebookResponse` object
      $response = $fb->get(
        '/your-post-id',
        '{access-token}'
      );
    } catch(FacebookExceptionsFacebookResponseException $e) {
      echo 'Graph returned an error: ' . $e->getMessage();
      exit;
    } catch(FacebookExceptionsFacebookSDKException $e) {
      echo 'Facebook SDK returned an error: ' . $e->getMessage();
      exit;
    }
    $graphNode = $response->getGraphNode();

The JSON Response if the User or Page has reacted to their own object.

{
  "reactions": {
    "data": \[
      {
        "id": "your-user-id",
        "name": "Your Name",
        "type": "HAHA"
      }
    \],
    "paging": {
      "cursors": {
        "before": "QVFIUk5YbXFFbG8yVWVOa2w0ZAGhmSUNKMkZAZAOXZARbzJOMHM0TUFtZAnhJbWdPdkF4OURUTHJrQjFqQ2RQZAVN1UGxSVU5FWURENnE4OUFPeXFreU1jV09pdFJR",
        "after": "QVFIUkpsWVRkcVl6SlhsdWlrcGdudl8xVEhwVEJ5ZA3FXdG90bTRxam13NmJDUGpQVnB5ZA29lMG9FVmFaeU1BLW1hc2oZD"
      }
    },
    "summary": {
      "total\_count": 28
    }
  },
  "id": "your-post-id"
}

The JSON Response if the User or Page has **not** reacted to their own object.

{
  "reactions": {
    "data": \[
    \],
    "paging": {
      "cursors": {
        "before": "QVFIUk5YbXFFbG8yVWVOa2w0ZAGhmSUNKMkZAZAOXZARbzJOMHM0TUFtZAnhJbWdPdkF4OURUTHJrQjFqQ2RQZAVN1UGxSVU5FWURENnE4OUFPeXFreU1jV09pdFJR",
        "after": "QVFIUkpsWVRkcVl6SlhsdWlrcGdudl8xVEhwVEJ5ZA3FXdG90bTRxam13NmJDUGpQVnB5ZA29lMG9FVmFaeU1BLW1hc2oZD"
      }
    },
    "summary": {
      "total\_count": 28
    }
  },
  "id": "your-post-id"
}

A User or Page can only query their own reactions. Other Users' or Pages' reactions are unavailable due to privacy concerns.

The "like" reaction counts include both "like" and "care" reactions.

### Parameters

| Name | Description |
| --- | --- |
| `type`<br><br>enum {NONE, LIKE, LOVE, WOW, HAHA, SORRY, ANGRY} | The type of reaction a Page or User marked an object. |

### Fields

Reading from this edge will return a JSON formatted result

{
    "data": \[\],
    "paging": {},
    "summary": {}
}

`data`

The [Profile](https://developers.facebook.com/docs/graph-api/reference/profile/) of the Page or User running the query, if the object being queried was reacted to by the Page or User, and a list of reaction types:

| Field | Description |
| --- | --- |
| `type`<br><br>enum {NONE, LIKE, LOVE, WOW, HAHA, SORRY, ANGRY} | The type of reaction a Page or User marked an object. |

For reactions on Posts, this edge does not return a Profile except for the current user, if read with a user access token.

#### View the count of an individual reaction

cURLAndroid SDKObjective-CJava SDKPHP SDK

    curl -i -X GET \
     "https://graph.facebook.com/your-object-id
       ?fields=reactions.type(LOVE).limit(0).summary(total_count)
       &access_token=your-access-token"

    GraphRequest request = GraphRequest.newGraphPathRequest(
      accessToken,
      "/your-object-id",
      new GraphRequest.Callback() {
        @Override
        public void onCompleted(GraphResponse response) {
          // Insert your code here
        }
    });
    
    Bundle parameters = new Bundle();
    parameters.putString("fields", "reactions.type(LOVE).limit(0).summary(total_count)");
    request.setParameters(parameters);
    request.executeAsync();

    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
        initWithGraphPath:@"/your-object-id"
               parameters:@{ @"fields": @"reactions.type(LOVE).limit(0).summary(total_count)",}
               HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection, id result, NSError *error) {
        // Insert your code here
    }];

    FB.api(
      '/your-object-id',
      'GET',
      {"fields":"reactions.type(LOVE).limit(0).summary(total_count)"},
      function(response) {
          // Insert your code here
      }
    );

    try {
      // Returns a `FacebookFacebookResponse` object
      $response = $fb->get(
        '/your-object-id',
        '{access-token}'
      );
    } catch(FacebookExceptionsFacebookResponseException $e) {
      echo 'Graph returned an error: ' . $e->getMessage();
      exit;
    } catch(FacebookExceptionsFacebookSDKException $e) {
      echo 'Facebook SDK returned an error: ' . $e->getMessage();
      exit;
    }
    $graphNode = $response->getGraphNode();

#### Example JSON Returned

{
  "reactions": {
    "data": \[
    \],
    "summary": {
      "total\_count": 3498
    }
  },
  "id": "your-object-id"
}

`paging`

For more details about pagination, see the Graph API's [paging documentation](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging). Adding `limit(0)` to `reactions` will remove `paging` from the output.

`summary`

Aggregated information about the edge, such as counts. Specify the fields to fetch in the summary param (like `summary=total_count`).

| Field | Description |
| --- | --- |
| `total_count`<br><br>unsigned int32 | Total number of reactions |
| `viewer_reaction`<br><br>enum {NONE, LIKE, LOVE, WOW, HAHA, SORRY, ANGRY} | The type of reaction a Page or User marked an object. |

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

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

`/{object-id}/sharedposts`
==========================

This reference describes the `/sharedposts` edge that is common to multiple Graph API nodes. The structure and operations are the same for each node. The following objects have a `sharedposts` edge:

* PagePost
    
* Post
    
* User
    

[](#)

Reading
-------

#### Permissions

* A user access token with `user_posts` permission, for someone who is able to view the post after privacy settings are taken into account. A post will be returned if either (a) the app created the post or (b) the creator of the post has granted `user_posts` permission to the app.
    

#### Feature Permissions

| Name | Description |
| --- | --- |
| Page Public Content Access | This is a required [feature permission](https://developers.facebook.com/docs/apps/review/feature/#reference-PAGES_ACCESS). |

#### Limitations

* The `/{album-id}/sharedposts` is not available.
* The `GET /{photo-id}/sharedposts` endpoint is deprecated in v8.0+.

#### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bobject-id%7D%2Fsharedposts&version=v18.0)

    GET /v18.0/{object-id}/sharedposts HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{object-id}/sharedposts',
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
        "/{object-id}/sharedposts",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{object-id}/sharedposts",
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
                                   initWithGraphPath:@"/{object-id}/sharedposts"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

#### Fields

A list of [Post objects](https://developers.facebook.com/docs/graph-api/reference/post) representing each of the shares.

[](#)

Publishing
----------

You cannot publish shares of an object using the Graph API.

[](#)

Deleting
--------

You cannot delete shares of an object using the Graph API.

[](#)

[](#)