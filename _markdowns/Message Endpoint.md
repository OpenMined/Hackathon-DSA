
Message - Graph API - Documentation - Meta for Developers












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
This document refers to an outdated version of Graph API. Please use the latest version.Graph API Versionv18.0Message
=======

An individual message in a Messenger or Instagram Messaging conversation.

To get the message ID use the conversation endpoint or Webhooks to retrieve the individual message IDs.

Reading
-------

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v19.0/{message-id} HTTP/1.1
Host: graph.facebook.com
```

```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{message-id}',
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
    "/{message-id}",
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
    "/{message-id}",
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
                               initWithGraphPath:@"/{message-id}"
                                      parameters:params
                                      HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
### Requirements



 Type | Description || App Review | Required to access data for people who do not have a role on your app, such as a developer, tester or admin |
| Features | Not applicable |
| Tokens |  A Page access token from a person who can perform the `MODERATE` or `MESSAGING` task on the Page being queried or linked to the Instagram Professional account. |
| Permissions | The `pages_messaging` and `pages_manage_metadata` permissionsThe `instagram_basic` and `instagram_manage_messaging` permissions are also required for Instagram Messaging |

### Limitations


**For Instagram Messaging**


* Only Instagram Professional accounts with a linked Facebook Page can access this endpoint.
* When querying this endpoint, all messages for this conversation will be returned. However, you will only be able to query data for the 20 most recent messages in the conversation. If a message is not within the 20 most recent, an error will be returned stating that the message has been deleted.

### Fields

If a field has no data, it will not be returned in the JSON response.




 Name | Description || `attachments.data`
*array*`file_url` `generic_template``id``image_data` `name` `video_data`  | Media, such as an image, video, or file CDN URL, attached to the message.
The URL for the file attached to the messageThe URL for the image attached to the message. Can include the following key:value pairs:

|  |  |
| --- | --- |
| * `cta`: object with `title`, `type`, `url`
* `medial_url`: string, URL for the image
 | * `subtitle`: string, in pixels
* `title`: string,
 |

 The ID for the attachmentThe URL for the image attached to the message. Can include the following key:value pairs:

|  |  |
| --- | --- |
| * `animated_gif_preview_url`: string, URL for preview for the GIF
* `animated_gif_url`: string, URL for the GIF
* `height`: int, in pixels
* `max_height`: int, in pixels
* `max_width`: int, in pixels
 | * `preview_url`: string, Preview for the URL
* `render_as_sticker`: bool, true or false
* `url`: string, URL for the image
* `width`: int, in pixels
 |

The name for the attachementThe URL for the video attached to the message |
| `created_time`
*datetime* | The time the message was created |
| `from`
*object*`id``email` `name` `username`  | Information about who sent the message. Can be a person, Page, or Instagram Professional account
 The ID can be an Instagram-scoped ID or Page-scoped ID for a person or Page ID or Instagram Professional account ID for your business.The email for a person or Facebook Page. *Page messaging only*The name for a person or Facebook Page. *Page messaging only*The username for a person on Instagram or your Instagram Professional account. *Instagram Messaging only*
```
"from": {
    "username": "INSTAGRAM-USERNAME",
    "id": "ID"
  }
```
 |
| `id`
*string* | The ID for a message |
| `is_unsupported`
*boolean* | Only returned when `true`; a message contains unsupported content. |
| `message`
*string* | Text content for the message. If no text is part of the message, this will be empty. |
| `reactions`
*array*`data` *array*`reaction` *emoji*`users` *array of objects*`id` `username`  | The types of reactions the message has received with a list of all the people who reacted with that reaction type.An array of reaction objectsThe reaction emoji typeA list of people who have reacted to the message The ID can be an Instagram-scoped ID for a person on Instagram or Instagram Professional account ID for your business.The username for a person on Instagram or your Instagram Professional account. *Instagram Messaging only*
```
"reactions":
  {
    "reaction": "❤️",
    "users" : [
      {
        "username": "INSTAGRAM-USERNAME",
        "id": "ID", 
      },
    ]
  }
```
 |
| `shares`
*array* | Media shares, such as a post or product template, included in the message. Please note, for the shares object you need to request the sub-fields also in order to retrieve the data.

```
"shares": {
  "data": [{
    "template": {
      "payload":{
        "product": {
           "elements":{     //Can contain multiple products if applicable
             "data": [
              {
                "id" : "PRODUCT-ID",    // 0 if business can't see this product
                "retailer_id": "ID-ASSIGNED-BY-THE-RETAILER", 
                "image_url" : "IMAGE-URL", 
                "name" : "PRODUCT-NAME",
                "price" : "$10"
              },
            ],
          }
        }
      }
    }
  }]
}   
```
 |
| `story`
*array* | The link and ID for a story. Only mentions and replyies are supported.

```
StoryReply: 
{
    "link": "CDN-URL",
    "id": "STORY-ID"
}

StoryMention: 
{
    "link": "CDN-URL",
    "id": "STORY-ID"
}
```
 |
| `tags`
*object* | A `data` array containing names for tags indicating the message folder and source of the message.* For Facebook Pages, `name` can be `inbox`, `read`, `source:chat`,
 |
| `to`
*object*`data` *array*`id``email` `name` `username`  | Information about who received the message
 The ID can be an Instagram-scoped ID or Page-scoped ID for a person or Page ID or Instagram Professional account ID for your business.The email for a person or Facebook Page. *Page messaging only*The name for a person or Facebook Page. *Page messaging only*The username for a person on Instagram or your Instagram Professional account. *Instagram Messaging only*
```
"to": {
  "data": [
    { 
      "username": "INSTAGRAM-USERNAME", 
      "id": "ID" 
    }
  ]
}
```
 |

Edges
-----



 
Name
 | 
Description
 || `/attachments` | Files attached to a message. |
| `/shares` | Shared items, including links, photos, videos, stickers and products. |

Create
------


You can't perform this operation on this endpoint.


Update
------


You can't perform this operation on this endpoint.


Delete
------


You can't perform this operation on this endpoint.





































 
