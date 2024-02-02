::: {._4-u3 ._588p}
You can edit a comment by using the following endpoint:

::: _5z09
::: _xmu
``` {#u_0_y_7Z ._5gt1 .prettyprint}
POST /v19.0/{comment-id} HTTP/1.1
Host: graph.facebook.com

message=This+is+a+test+comment
```

``` {#u_0_z_P0 ._5gt1 .prettyprint}
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
```

``` {#u_0_10_hA ._5gt1 .prettyprint}
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
```

``` {#u_0_11_/i ._5gt1 .prettyprint}
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
```

``` {#u_0_12_S+ ._5gt1 .prettyprint}
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
```
:::
:::

### New Page Experience

This API is supported for New Page Experience.

-   A Page access token requested by a person who can perform the
    \`MODERATE\` task on the Page

-   The ` pages_read_engagement ` permission

-   The ` pages_manage_engagement ` permission

### Hiding Comments {#hiding}

You can hide most comments on Posts with the following exceptions:

-   comments made by the Page
-   comments made by the Page\'s admins
-   comments made by the Page on a User\'s Post. The Post is owned by
    the User.
-   comments made by any User on another User\'s Post to the Page. The
    Post is owned by the User.
-   comments made by an Event creator. The Post is owned by the Event
    creator.
-   comments made by a Facebook Group. The Post is owned by the Group.
-   comments made by anyone on a review

One of ` attachment_url ` , ` attachment_id ` , ` message ` , or
` attachment_share_url ` must be provided when updating.

You must include either a message or an attachment. An attachment can be
either a ` url ` , an ` attachment_id ` , or an ` attachment_share_url `
. You may include an ` id ` and a ` url ` together. If you include an
` attachment_share_url ` , you must not include the others.

When updating you must include any values that were on the original
content. If you do not include one of them it will be removed from the
content after the update. For example, if you update a comment that has
an image that was specified via ` attachment_url ` and you don\'t
include it in the update the image will be removed.

Updating supports the fields listed on the [publishing section of the
` /object/comments `](/docs/graph-api/reference/object/comments#publish)
. This includes the ` attachment_url ` , ` attachment_id ` , ` message `
and ` source ` . Please see that document for details on those fields.

Updating also supports the ` is_hidden ` field, documented here.

::: _57-c
Name
:::
:::

Description

Type

` is_hidden `

Whether this comment is hidden or visible. The original poster can still
see the comment, along with the page admin and anyone else tagged in the
comment

` boolean `

If successful, you will receive a response with the following
information. In addition, this endpoint supports
[read-after-write](/docs/graph-api/using-graph-api#read-after-write) and
can immediately return any fields returned by
[read](/docs/graph-api/reference/comment#read) operations.

``` {._5s-8 .prettyprint .lang-code}
{
  "success": true
}
```

If unsuccessful, a relevant error message will be returned.
