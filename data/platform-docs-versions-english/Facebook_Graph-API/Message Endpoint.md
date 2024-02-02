This document refers to an outdated version of Graph API. Please [use the latest version.](https://developers.facebook.com/docs/graph-api/reference/v19.0/message)

Message
=======

An individual message in a Messenger or Instagram Messaging conversation.

To get the message ID use the [conversation endpoint](https://developers.facebook.com/docs/graph-api/reference/conversation) or [Webhooks](https://developers.facebook.com/docs/graph-api/webhooks/) to retrieve the individual message IDs.

Reading
-------

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bmessage-id%7D&version=v19.0)

    GET /v19.0/{message-id} HTTP/1.1
    Host: graph.facebook.com

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

    /* make the API call */
    FB.api(
        "/{message-id}",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

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

### Requirements

| Type | Description |
| --- | --- |
| [App Review](https://developers.facebook.com/docs/apps/review) | Required to access data for people who do not have a role on your app, such as a developer, tester or admin |
| Features | Not applicable |
| Tokens | A [Page access token](https://developers.facebook.com/docs/facebook-login/access-tokens/#pagetokens) from a person who can perform the [`MODERATE` or `MESSAGING` task](https://developers.facebook.com/docs/pages/overview-1#tasks) on the Page being queried or linked to the Instagram Professional account. |
| Permissions | The [`pages_messaging` and `pages_manage_metadata` permissions](https://developers.facebook.com/docs/permissions/reference)<br><br>The [`instagram_basic` and `instagram_manage_messaging` permissions](https://developers.facebook.com/docs/permissions/reference) are also required for Instagram Messaging |

### Limitations

**For Instagram Messaging**

* Only Instagram Professional accounts with a linked Facebook Page can access this endpoint.
    
* When querying this endpoint, all messages for this conversation will be returned. However, you will only be able to query data for the 20 most recent messages in the conversation. If a message is not within the 20 most recent, an error will be returned stating that the message has been deleted.
    

### Fields

If a field has no data, it will not be returned in the JSON response.

NameDescription

`attachments.data`

_array_

`file_url`

`generic_template`

`id`

`image_data`

`name`

`video_data`

Media, such as an image, video, or file CDN URL, attached to the message.

  

The URL for the file attached to the message

The URL for the image attached to the message. Can include the following key:value pairs:

|     |     |
| --- | --- |
| * `cta`: object with `title`, `type`, `url`<br>* `medial_url`: string, URL for the image | * `subtitle`: string, in pixels<br>* `title`: string, |

The ID for the attachment

The URL for the image attached to the message. Can include the following key:value pairs:

|     |     |
| --- | --- |
| * `animated_gif_preview_url`: string, URL for preview for the GIF<br>* `animated_gif_url`: string, URL for the GIF<br>* `height`: int, in pixels<br>* `max_height`: int, in pixels<br>* `max_width`: int, in pixels | * `preview_url`: string, Preview for the URL<br>* `render_as_sticker`: bool, true or false<br>* `url`: string, URL for the image<br>* `width`: int, in pixels |

The name for the attachement

The URL for the video attached to the message

`created_time`

_datetime_

The time the message was created

`from`

_object_

`id`

`email`

`name`

`username`

Information about who sent the message. Can be a person, Page, or Instagram Professional account

The ID can be an Instagram-scoped ID or Page-scoped ID for a person or Page ID or Instagram Professional account ID for your business.

The email for a person or Facebook Page. _Page messaging only_

The name for a person or Facebook Page. _Page messaging only_

The username for a person on Instagram or your Instagram Professional account. _Instagram Messaging only_

"from": {
    "username": "INSTAGRAM-USERNAME",
    "id": "ID"
  }

`id`

_string_

The ID for a message

`is_unsupported`

_boolean_

Only returned when `true`; a message contains unsupported content.

`message`

_string_

Text content for the message. If no text is part of the message, this will be empty.

`reactions`

_array_

`data` _array_

`reaction` _emoji_

`users` _array of objects_

`id`

  

`username`

The types of reactions the message has received with a list of all the people who reacted with that reaction type.

An array of reaction objects

The reaction emoji type

A list of people who have reacted to the message

  

The ID can be an Instagram-scoped ID for a person on Instagram or Instagram Professional account ID for your business.

The username for a person on Instagram or your Instagram Professional account. _Instagram Messaging only_

"reactions":
  {
    "reaction": "❤️",
    "users" : \[
      {
        "username": "INSTAGRAM-USERNAME",
        "id": "ID", 
      },
    \]
  }

`shares`

_array_

Media shares, such as a post or product template, included in the message. Please note, for the shares object you need to request the sub-fields also in order to retrieve the data.

"shares": {
  "data": \[{
    "template": {
      "payload":{
        "product": {
           "elements":{     //Can contain multiple products if applicable
             "data": \[
              {
                "id" : "PRODUCT-ID",    // 0 if business can't see this product
                "retailer\_id": "ID-ASSIGNED-BY-THE-RETAILER", 
                "image\_url" : "IMAGE-URL", 
                "name" : "PRODUCT-NAME",
                "price" : "$10"
              },
            \],
          }
        }
      }
    }
  }\]
}   

`story`

_array_

The link and ID for a story. Only mentions and replyies are supported.

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

`tags`

_object_

A `data` array containing names for tags indicating the message folder and source of the message.

* For Facebook Pages, `name` can be `inbox`, `read`, `source:chat`,

`to`

_object_

`data` _array_

`id`

`email`

`name`

`username`

Information about who received the message

  
  

The ID can be an Instagram-scoped ID or Page-scoped ID for a person or Page ID or Instagram Professional account ID for your business.

The email for a person or Facebook Page. _Page messaging only_

The name for a person or Facebook Page. _Page messaging only_

The username for a person on Instagram or your Instagram Professional account. _Instagram Messaging only_

"to": {
  "data": \[
    { 
      "username": "INSTAGRAM-USERNAME", 
      "id": "ID" 
    }
  \]
}

Edges
-----

| Name | Description |
| --- | --- |
| [`/attachments`](https://developers.facebook.com/docs/graph-api/reference/message/attachments) | Files attached to a message. |
| [`/shares`](https://developers.facebook.com/docs/graph-api/reference/message/shares/) | Shared items, including links, photos, videos, stickers and products. |

Create
------

You can't perform this operation on this endpoint.

Update
------

You can't perform this operation on this endpoint.

Delete
------

You can't perform this operation on this endpoint.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)