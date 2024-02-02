
Thread - Graph API - Documentation - Meta for Developers












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
This document refers to an outdated version of Graph API. Please use the latest version.Graph API Versionv18.0Thread `/{thread-id}`
=====================

A Facebook Messages conversation thread. This endpoint is only accessible for users that are developers of the app making the request.

Pages should use the Conversation endpoint.

Reading
-------

Get a message thread.


### Permissions

* A Page access token requested by a person who can perform the `MODERATE` task on the Page.
* The `pages_messaging` permission
* The `pages_manage_metadata` permission
* The `pages_show_list` permission

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v19.0/{thread-id} HTTP/1.1
Host: graph.facebook.com
```

```
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
```

```
/* make the API call */
FB.api(
    "/{thread-id}",
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
    "/{thread-id}",
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
                               initWithGraphPath:@"/{thread-id}"
                                      parameters:params
                                      HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
### Fields



 
Name
 | 
Description
 | 
Type
 || `id` | The unique ID for this message thread. | `string` |
| `comments` | The messages in this thread. | `Message[]` |
| `to` | Profiles that are subscribed to the thread. | `Profile[]` |
| `unread` | The amount of messages that are unread by the session profile. | `integer` |
| `unseen` | The amount of messages that are unseen by the session profile. | `integer` |
| `updated_time` | When the thread was last updated. | `datetime` |
| `can_reply` | Can the page reply in the thread. | `boolean` |
| `linked_group` | ID of the Workplace group that the thread is linked to (Workplace only) | `string` |

### Edges



 
Name
 | 
Description
 || `messages` | List of individual messages in the thread. See Messages |

### Filtering Messages

The `messages` connection can be filtered to avoid pulling text that is part of thread warnings by the Messenger Apps. This is done via the `source` filter there only participants might be selected.


If this filter is not apply *admin text* (gray text appears in the thread by Messenger) will be retrieved as well.


#### Example

This call will retrieve the last 3 messages made only by the participants.



```

curl -i -X GET \
 "https://graph.facebook.com/v4.0/t_10155839492600149?fields=id,messages.source(PARTICIPANTS).limit(3)&access_token=<Access Token>"

```
Publishing
----------

You can't perform this operation on this endpoint.

Deleting
--------

You can't perform this operation on this endpoint.

Updating
--------

You can't perform this operation on this endpoint.




































 
