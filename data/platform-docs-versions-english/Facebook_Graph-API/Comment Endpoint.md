This document refers to an outdated version of Graph API. Please [use the latest version.](https://developers.facebook.com/docs/graph-api/reference/v19.0/comment)

Comment `/{comment-id}`
=======================

A `comment` can be made on various types of content on Facebook. Most Graph API nodes have a `/comments` edge that lists all the comments on that object. The `/{comment-id}` node returns a single `comment`.

Reading
-------

### New Page Experience

This API is supported for New Page Experience.

### Permissions

* **General** - To read a comment, you generally need the same permissions as required for viewing the object that the comment was added to.
    
* **Replies** - If this is a comment that is a reply to another comment, the permissions required apply to the object that the parent comment was added to.
    
* **Page owned Comments and Replies** — For any comments or replies owned by (on) a Page, you must use a Page access token if you want User information to be included in the response.
    

The Page Post comment ID format, `{page-id}_{post_id}_{comment-id}`, has been deprecated. Use the `{pagepost-id}_{comment-id}` format instead.

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bcomment-id%7D&version=v19.0)

    GET /v19.0/{comment-id} HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{comment-id}',
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
        "/{comment-id}",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{comment-id}",
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
                                   initWithGraphPath:@"/{comment-id}"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### Fields

| Property Name | Description | Type |
| --- | --- | --- |
| `id` | The comment ID | `string` |
| `attachment` | Link, video, sticker, or photo attached to the comment | [`StoryAttachment`](https://developers.facebook.com/docs/graph-api/reference/story-attachment/) |
| `can_comment` | Whether the viewer can reply to this comment | `bool` |
| `can_remove` | Whether the viewer can remove this comment | `bool` |
| `can_hide` | Whether the viewer can hide this comment. Only visible to a page admin | `boolean` |
| `can_like` | Whether the viewer can like this comment | `boolean` |
| `can_reply_privately` | Whether the viewer can send a private reply to this comment (Page viewers only) | `boolean` |
| `comment_count` | Number of replies to this comment | `int32` |
| `created_time` | The time this comment was made | `datetime` |
| `from` | The person that made this comment | [`User`](https://developers.facebook.com/docs/graph-api/reference/user/) |
| `like_count` | Number of times this comment was liked | `int32` |
| `message` | The comment text | `string` |
| `message_tags` | An array of Profiles tagged in `message`. | `object[]` |
| `id` | ID of the profile that was tagged. | `string` |
| `name` | The text used in the tag. | `string` |
| `type` | Indicates which type of profile is tagged. | `enum{user, page, group}` |
| `offset` | Where the first character of the tagged text is in the `message`, measured in [unicode code points](https://l.facebook.com/l.php?u=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FCode_point&h=AT2i8B_IOTq8ETraR8BzN2rp1fTWAe9ir3N3-dtmpqbi-0L4USxjZq6UUEV4z6ARsn4ziBFfQOSRp1wzV_MwYCeS-0TujP3nBMOwnETl4tJS11G-gGiZL_iqxQc5uqf2L-_AnQXrLDvHFQgA). | `integer` |
| `length` | How many [unicode code points](https://l.facebook.com/l.php?u=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FCode_point&h=AT3MqiYezls_pJ-vHYozYSAK9XAVwr7dI0nffhmpAMou_IBkpaCkH-pNp99-BXf1E5cQAZRWRvvFDEYhEGrcaRAuL6hk4-eATYt7-sRCY34ml2khGei5yLhoSzeGqAjBMsn0o2XxrOi2h7OC) this tag consists of, after the offset. | `integer` |
| `object` | The comment on a post that contains a photo or video, including those in dynamic posts. Otherwise, this is empty. | `Object` |
| `parent` | For comment replies, this the comment that this is a reply to. | [`Comment`](https://developers.facebook.com/docs/graph-api/reference/comment) |
| `private_reply_conversation` | For comments with private replies, gets conversation between the Page and author of the comment (Page viewers only) | [`Conversation`](https://developers.facebook.com/docs/graph-api/reference/conversation) |
| `user_likes` | Whether the viewer has liked this comment. | `bool` |

Publishing
----------

You can publish comments by using the [`/comments`](https://developers.facebook.com/docs/graph-api/reference/object/comments/) edge when it is present on a node.

Deleting
--------

You can delete a comment by using the following endpoint:

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK

    DELETE /v19.0/{comment-id} HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->delete(
        '/{comment-id}',
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
        "/{comment-id}",
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
        "/{comment-id}",
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
                                   initWithGraphPath:@"/{comment-id}"
                                          parameters:params
                                          HTTPMethod:@"DELETE"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### New Page Experience

This API is supported for New Page Experience.

### Requirements

To delete a comment posted by a Page, you will need:

* A Page access token requested by a person who can perform the \`MODERATE\` task on the Page
    
* The `pages_read_engagement` permission
    
* The `pages_manage_engagement` permission
    

To delete a comment posted by a User or another Page, you will need:

* A Page access token requested by a person who can perform the \`MODERATE\` task on the Page
    
* The `pages_manage_engagement` permission
    
* The `pages_read_user_content` permission
    

#### Limitations

Reviews are not Page posts, so comments on reviews can not be removed by a Page.

### Response

If successful:

{
  "success": true
}

Otherwise a relevant error message will be returned.

Updating
--------

You can edit a comment by using the following endpoint:

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK

    POST /v19.0/{comment-id} HTTP/1.1
    Host: graph.facebook.com
    
    message=This+is+a+test+comment

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->post(
        '/{comment-id}',
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
        "/{comment-id}",
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
        "/{comment-id}",
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
                                   initWithGraphPath:@"/{comment-id}"
                                          parameters:params
                                          HTTPMethod:@"POST"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### New Page Experience

This API is supported for New Page Experience.

### Permissions

* A Page access token requested by a person who can perform the \`MODERATE\` task on the Page
    
* The `pages_read_engagement` permission
    
* The `pages_manage_engagement` permission
    

### Hiding Comments

You can hide most comments on Posts with the following exceptions:

* comments made by the Page
* comments made by the Page's admins
* comments made by the Page on a User's Post. The Post is owned by the User.
* comments made by any User on another User's Post to the Page. The Post is owned by the User.
* comments made by an Event creator. The Post is owned by the Event creator.
* comments made by a Facebook Group. The Post is owned by the Group.
* comments made by anyone on a review

### Fields

One of `attachment_url`, `attachment_id`, `message`, or `attachment_share_url` must be provided when updating.

You must include either a message or an attachment. An attachment can be either a `url`, an `attachment_id`, or an `attachment_share_url`. You may include an `id` and a `url` together. If you include an `attachment_share_url`, you must not include the others.

When updating you must include any values that were on the original content. If you do not include one of them it will be removed from the content after the update. For example, if you update a comment that has an image that was specified via `attachment_url` and you don't include it in the update the image will be removed.

Updating supports the fields listed on the [publishing section of the `/object/comments`](https://developers.facebook.com/docs/graph-api/reference/object/comments#publish). This includes the `attachment_url`, `attachment_id`, `message` and `source`. Please see that document for details on those fields.

Updating also supports the `is_hidden` field, documented here.

| Name | Description | Type |
| --- | --- | --- |
| `is_hidden` | Whether this comment is hidden or visible. The original poster can still see the comment, along with the page admin and anyone else tagged in the comment | `boolean` |

### Response

If successful, you will receive a response with the following information. In addition, this endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/using-graph-api#read-after-write) and can immediately return any fields returned by [read](https://developers.facebook.com/docs/graph-api/reference/comment#read) operations.

{
  "success": true
}

If unsuccessful, a relevant error message will be returned.

Edges
-----

| Property Name | Description | Type |
| --- | --- | --- |
| [`/comments`](https://developers.facebook.com/docs/graph-api/reference/object/comments) | Comments that reply to this comment. | `Edge<Comment>` |
| [`/likes`](https://developers.facebook.com/docs/graph-api/reference/object/likes) | People who like this comment. | `Edge<Profile>` |
| [`/reactions`](https://developers.facebook.com/docs/graph-api/reference/object/reactions) | People who have reacted to this post. | `Edge<Reaction>` |
| [`/private_replies`](https://developers.facebook.com/docs/graph-api/reference/object/private_replies) | Used to send private message reply to this comment (Page viewers only). | `Edge<Message>` |

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)