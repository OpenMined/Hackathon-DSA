This document refers to an outdated version of Graph API. Please [use the latest version.](https://developers.facebook.com/docs/graph-api/reference/v19.0/thread)

Thread `/{thread-id}`
=====================

A Facebook Messages conversation thread. This endpoint is only accessible for users that are developers of the app making the request.

Pages should use the [Conversation endpoint](https://developers.facebook.com/docs/graph-api/reference/conversation/).

Reading
-------

Get a message thread.

### Permissions

* A Page access token requested by a person who can perform the [`MODERATE` task](https://developers.facebook.com/docs/pages/overview/permissions-features#tasks) on the Page.
    
* The [`pages_messaging` permission](https://developers.facebook.com/docs/permissions/reference/pages_messaging)
    
* The [`pages_manage_metadata` permission](https://developers.facebook.com/docs/permissions/reference/pages_manage_metadata)
    
* The [`pages_show_list` permission](https://developers.facebook.com/docs/permissions/reference/pages_show_list)
    

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bthread-id%7D&version=v19.0)

    GET /v19.0/{thread-id} HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{thread-id}',
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
        "/{thread-id}",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{thread-id}",
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
                                   initWithGraphPath:@"/{thread-id}"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### Fields

| Name | Description | Type |
| --- | --- | --- |
| `id` | The unique ID for this message thread. | `string` |
| `comments` | The messages in this thread. | [`Message[]`](https://developers.facebook.com/docs/graph-api/reference/message/) |
| `to` | Profiles that are subscribed to the thread. | [`Profile[]`](https://developers.facebook.com/docs/graph-api/reference/profile/) |
| `unread` | The amount of messages that are unread by the session profile. | `integer` |
| `unseen` | The amount of messages that are unseen by the session profile. | `integer` |
| `updated_time` | When the thread was last updated. | `datetime` |
| `can_reply` | Can the page reply in the thread. | `boolean` |
| `linked_group` | ID of the Workplace group that the thread is linked to (Workplace only) | `string` |

### Edges

| Name | Description |
| --- | --- |
| `messages` | List of individual messages in the thread. See [Messages](https://developers.facebook.com/docs/graph-api/reference/message) |

### Filtering Messages

The `messages` connection can be filtered to avoid pulling text that is part of thread warnings by the Messenger Apps. This is done via the `source` filter there only participants might be selected.

If this filter is not apply _admin text_ (gray text appears in the thread by Messenger) will be retrieved as well.

#### Example

This call will retrieve the last 3 messages made only by the participants.

curl -i -X GET \\
 "https://graph.facebook.com/v4.0/t\_10155839492600149?fields=id,messages.source(PARTICIPANTS).limit(3)&access\_token=<Access Token>"

Publishing
----------

You can't perform this operation on this endpoint.

Deleting
--------

You can't perform this operation on this endpoint.

Updating
--------

You can't perform this operation on this endpoint.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)