This document refers to an outdated version of Graph API. Please [use the latest version.](https://developers.facebook.com/docs/graph-api/reference/v19.0/conversation)

Conversation `/{conversation-id}`
=================================

A Messenger conversation between a person and a Facebook Page or an Instagram Professional Account.

Reading
-------

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bconversation-id%7D&version=v19.0)

    GET /v19.0/{conversation-id} HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{conversation-id}',
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
        "/{conversation-id}",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{conversation-id}",
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
                                   initWithGraphPath:@"/{conversation-id}"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### Permissions

* A Page access token requested by a person who can perform the [`MESSAGING` task](https://developers.facebook.com/docs/pages/overview-1#tasks) on the Page being queried
    
* The [`pages_messaging` permission](https://developers.facebook.com/docs/apps/review/login-permissions#reference-pages_messaging)
    
* The [`pages_manage_metadata` permission](https://developers.facebook.com/docs/apps/review/login-permissions#reference-pages_manage_metadata)
    

For Instagram Messaging, you will also need:

* The [`instagram_basic` permission](https://developers.facebook.com/docs/apps/review/login-permissions#reference-instagram_basic)
    
* The [`instagram_manage_messages` permission](https://developers.facebook.com/docs/apps/review/login-permissions#reference-instagram_manage_messages)
    

### Limitations

* When querying this endpoint for Instagram Messaging, all messages for the conversation will be returned. However, you will only be able to query data for the 20 most recent messages in the conversation. If a message is not within the 20 most recent, an error will be returned stating that the message has been deleted.
    

### Fields

| Name | Description |
| --- | --- |
| `id`<br><br>_string_ | The ID for the conversation |
| `messages`<br><br>_string_ | Messages within the conversation |
| `participants`<br><br>_object_<br><br>`id`<br><br>  <br><br>`email`<br><br>_Page messaging only_<br><br>`name`<br><br>_Page messaging only_<br><br>`username`<br><br>_Instagram Messaging only_ | Participants in the conversation<br><br>  <br><br>Instagram-Scoped ID or Page-scoped ID for a person or Instagram ID for your Instagram Professional account or the Page ID.<br><br>Email for the person or Page<br><br>  <br><br>Name for the person or Page<br><br>  <br><br>Instagram username for a person or your Instagram Profession account |
| `updated_time`<br><br>_datetime_ | The time when the last message was added to the conversation |

To get information about a specific message within a conversation, send a request to the [Message endpoint](https://developers.facebook.com/docs/graph-api/reference/message).

Publishing
----------

You can't publish using this edge.

Use the [Messenger Platform](https://developers.facebook.com/docs/messenger-platform/reference/send-api/) to send [Templates](https://developers.facebook.com/docs/messenger-platform/send-messages/templates), [Quick Replies](https://developers.facebook.com/docs/messenger-platform/send-messages/quick-replies), and more.

Deleting
--------

You can't delete using this edge.

Updating
--------

You can't update using this edge.

Edges
-----

| Name | Description | Used to Publish |
| --- | --- | --- |
| [`/messages`](https://developers.facebook.com/docs/graph-api/reference/conversation/messages/) | List of all messages in the conversation | Replies (by Pages only) |

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

This document refers to an outdated version of Graph API. Please [use the latest version.](https://developers.facebook.com/docs/graph-api/reference/v19.0/conversation/messages)

Graph API Reference [`/{conversation-id}`](https://developers.facebook.com/docs/graph-api/reference/conversation/)`/messages`
=============================================================================================================================

The messages in a conversation between a person and a Facebook Page or Instagram Professional account.

Reading
-------

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bconversation-id%7D%2Fmessages&version=v19.0)

    GET /v19.0/{conversation-id}/messages HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{conversation-id}/messages',
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
        "/{conversation-id}/messages",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{conversation-id}/messages",
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
                                   initWithGraphPath:@"/{conversation-id}/messages"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### Permissions

* A Page access token requested by a person who can perform the `MESSAGING` task on the Page
    
* The `[pages_messaging](https://developers.facebook.com/docs/apps/review/login-permissions#reference-pages_messaging)` permission
    
* For Instagram Messaging, the `instagram_manage_messages` permission is also required
    

### Fields

Returns an array of [Message objects](https://developers.facebook.com/docs/graph-api/reference/message) with additional fields:

| Name | Description | Type |
| --- | --- | --- |
| Vector | Vector |

Send a message
--------------

You cannot send a message to this enpoint. Use [Send API](https://developers.facebook.com/docs/messenger-platform/reference/send-api/) instead.

Delete
------

You cannot delete this endpoint.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)