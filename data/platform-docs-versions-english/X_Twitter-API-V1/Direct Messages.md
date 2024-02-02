Direct Message API features

Please note:

We've recently released the following endpoints within the [Twitter API v2](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api).

| v1.1 endpoints | Corresponding v2 endpoints |     |
| --- | --- | --- |
| [GET direct\_messages/events/list](https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/sending-and-receiving/api-reference/list-events) | Direct Messages [lookup](https://developer.twitter.com/en/docs/twitter-api/direct-messages/lookup/introduction) | [Migration guide](https://developer.twitter.com/en/docs/twitter-api/direct-messages/lookup/migrate) |
| [POST direct\_mesages/events/new](https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/sending-and-receiving/api-reference/new-event) | [Manage](https://developer.twitter.com/en/docs/twitter-api/direct-messages/manage/introduction) Direct Messages | [Migration guide](https://developer.twitter.com/en/docs/twitter-api/direct-messages/manage/migrate) |

Please use the migration guides to see what has changed between the standard v1.1 and v2 versions.

These API features enable developers to build better-personalized customer experiences at scale as well as other innovative interactions. To help create more engaging customer service, marketing, and user engagement experiences in Direct Messages we’re providing developers access to endpoints to start conversations with a welcome message, publish messages with quick replies and media, and more.

* [Sending and receiving events](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving "Sending and receiving events")Send and receive Direct Messages.
* [Welcome Messages](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/welcome-messages "Welcome Messages")Create messages that display for specific scenarios.
* [Message Attachments](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/message-attachments "Message Attachments")Attach videos, images and GIFs.
* [Quick Replies](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/quick-replies "Quick Replies")Prompt users for structured replies with a menu of options.
* [Buttons](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/buttons "Buttons")Add buttons to link to websites, deep link to apps or other parts of Twitter.
* [Conversation management](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/conversation-management "Conversation management")Properties to help manage the conversation between multiple applications.
* [Custom profiles](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/custom-profiles "Custom profiles")Display a custom profile image and name in a Direct Message.
* [Customer feedback cards](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/customer-feedback "Customer feedback cards")Prompt users for NPS and CSAT feedback.

Overview

Please note:

We've recently released the following endpoints within the [Twitter API v2](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api).

| v1.1 endpoints | Corresponding v2 endpoints |     |
| --- | --- | --- |
| [GET direct\_messages/events/list](https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/sending-and-receiving/api-reference/list-events) | Direct Messages [lookup](https://developer.twitter.com/en/docs/twitter-api/direct-messages/lookup/introduction) | [Migration guide](https://developer.twitter.com/en/docs/twitter-api/direct-messages/lookup/migrate) |
| [POST direct\_mesages/events/new](https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/sending-and-receiving/api-reference/new-event) | [Manage](https://developer.twitter.com/en/docs/twitter-api/direct-messages/manage/introduction) Direct Messages | [Migration guide](https://developer.twitter.com/en/docs/twitter-api/direct-messages/manage/migrate) |

Please use the migration guides to see what has changed between the standard v1.1 and v2 versions.

Sending message events  

-------------------------

To send a new Direct Message use [POST direct\_messages/events/new (message\_create)](https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/api-reference/new-event). Optionally, you may also attach [Quick Replies](https://developer.twitter.com/en/docs/direct-messages/quick-replies) or [media](https://developer.twitter.com/en/docs/direct-messages/message-attachments/guides/attaching-media) (image, GIF or video).

Receiving messages events
-------------------------

* You can retrieve Direct Messages from up to the past 30 days with [GET direct\_messages/events/list](https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/api-reference/list-events).
* Consuming Direct Messages in real-time can be accomplished via webhooks with the [Account Activity API](https://developer.twitter.com/en/docs/accounts-and-users/subscribe-account-activity/overview).

Message Create Object

Message Create Object
=====================

Direct Message Event objects are returned by [GET direct\_messages/events/list](https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/api-reference/list-events), [GET direct\_messages/events/show](https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/api-reference/get-event) and can be consumed in real-time using the [Account Activity API](https://developer.twitter.com/en/docs/accounts-and-users/subscribe-account-activity/overview). Direct Messages have the type of message\_create.

      `{   "type": "message_create",   "id": "1234858592",   "created_timestamp": "1392078023603",   "initiated_via": {     "tweet_id": "123456",     "welcome_message_id": "456789"   },   "message_create": {     "target": {       "recipient_id": "1234858592"     },     "sender_id": "3805104374",     "source_app_id": "268278",     "message_data": {       "text": "Blue Bird",       "entities": {         "hashtags": [],         "symbols": [],         "urls": [],         "user_mentions": [],       },       "quick_reply_response": {         "type": "options",         "metadata": "external_id_2"       },       "attachment": {         "type": "media",         "media": {          ...         }       }     }   } }`
    

Top level event object
----------------------

|     |     |
| --- | --- |
| Property | Description |
| type | The type of event. For Direct Messages type will be message\_create. |
| id  | The ID of the direct message event. |
| created\_timestamp | Epoch timestamp of when the Direct Message event was created. |
| initiated\_via.tweet\_id | The ID of the Tweet with Direct Message Prompt the conversation was initiated from if one was used. |
| initiated\_via.welcome\_message\_id | The ID of the Welcome Message immediatley preceding the conversation if one was used. |

message\_create object
----------------------

|     |     |
| --- | --- |
| message\_create.target.recipient\_id | The ID of the user receiving the message. |
| message\_create.sender\_id | The ID of the user sending the message. |
| message\_create.source\_app\_id | The ID of the application used to create the event. App details are available in the apps object in JSON payloads containing message\_create events. |
| message\_create.message\_data | A message\_data object. |

message\_data object  

-----------------------

|     |     |
| --- | --- |
| message\_data.text | The Direct Message text. |
| message\_data.entities | A Twitter [entities](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/entities-object) object. |
| message\_data.quick\_reply\_response | A [Quick Reply](https://developer.twitter.com/en/docs/direct-messages/quick-replies/overview) response object. |
| message\_data.attachment | An [attachment](https://developer.twitter.com/en/docs/direct-messages/message-attachments/overview) object (media) |

Direct Message migration guide

Direct Message migration guide
------------------------------

**On September 17th, 2018 we retired the legacy Direct Message endpoints.  
If you had been using those endpoints, please make sure to migrate over to the new Direct Message endpoints or the Account Activity API.**

**Please review [this announcment](https://twittercommunity.com/t/details-and-what-to-expect-from-the-api-deprecations-this-week-on-august-16-2018/110746) to learn more.**

This guide is designed to help you migrate from legacy Direct Message REST APIs to their enhanced replacements which have graduated from beta. Below you will find a summary of the changes, a new features list, and key differences and considerations to help with the transition. The new Direct Message endpoints are available now to all developers. For guidance in migrating from User Streams or Site Streams, see the [migration guide to Account Activity API](https://developer.twitter.com/content/developer-twitter/en/docs/accounts-and-users/subscribe-account-activity/migration/us-ss-migration-guide).

* [Summary of changes](#summary)
* [New features](#features)
* [Sending Direct Messages](#sending)
* [Receiving Direct Messages](#receiving)
* [Deleting Direct Messages](#deleting) 

### Summary of changes

If you are still using the following DM endpoints, you will have to migrate to the newer endpoints. 

| Deprecated endpoint | New migration alternative |
| --- | --- |
| [POST direct\_messages/new](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/new-message) | [POST direct\_messages/events/new](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/new-event) |
| [GET direct\_messages/show](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/get-message) | [GET direct\_messages/events/show](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/get-event) |
| [GET direct\_messages](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/get-messages) | [GET direct\_messages/events/list](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/list-events) |
| [GET direct\_messages/sent](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/get-sent-message) | [GET direct\_messages/events/list](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/list-events) |
| [POST direct\_messages/destroy](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/delete-message) | [DELETE direct\_messages/events/destroy](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/delete-message-event "GET direct_messages/events/list") |

### New features

The new Direct Message API endpoints support a number of new capabilities and provide improved access to previous Direct Messages. New features include:

* Support for media attachments (image, GIF, and video).
* Ability to prompt users for structured replies with a predefined options list.
* Up to 30 days of access to past Direct Messages.

For a full list of new Direct Message features and additional new API endpoints refer to the [technical documentation](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/overview).  
 

### Differences & migration considerations

The new API endpoints behave very differently from their previous counterparts. Simply updating the endpoint URLs will result in errors in your application. Consider the following when updating your application for the migration.

#### New Direct Message object

The first thing you are likely to notice is the new object structure of Direct Messages. This new Message Create object structure has been introduced to support new capabilities like [Quick Replies](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/quick-replies) and [Attachments](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/message-attachments). The new object also contains a smaller condensed user object. Your application will need to be updated to account for this new object structure when parsing and potentially in data models or storage. For descriptions of each property see the [full documentation on the Message Create Object](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/guides/message-create-object).  

**Example message create object**  

    {
      "type": "message_create",
      "id": "1234858592",
      "created_timestamp": "1392078023603",
      "initiated_via": {
        "tweet_id": "123456",
        "welcome_message_id": "456789"
      },
      "message_create": {
        "target": {
          "recipient_id": "1234858592"
        },
        "sender_id": "3805104374",
        "source_app_id": "268278",
        "message_data": {
          "text": "Blue Bird",
          "entities": {
            "hashtags": [],
            "symbols": [],
            "urls": [],
            "user_mentions": [],
          },
          "quick_reply_response": {
            "type": "options",
            "metadata": "external_id_2"
          },
          "attachment": {
            "type": "media",
            "media": {
             ...
            }
          }
        }
      }

#### Summary

* Entirely new Direct Message object structure.
* Condensed user object.
* New information provided (quick reply responses, attachments, etc).  
      
    

### Sending Direct Messages

[POST direct\_messages/events/new](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/new-event) is a direct replacement for sending Direct Messages. The most significant difference with this endpoint is that all information is now sent as JSON in the POST request body as opposed to individual POST params.

**Example Twurl request**  

twurl -A 'Content-type: application/json' -X POST /1.1/direct\_messages/events/new.json -d '{"event": {"type": "message\_create", "message\_create": {"target": {"recipient\_id": "4534871"}, "message\_data": {"text": "Hello World!"}}}}'

Note in the above request that the content-type is set to application/json as opposed to application/x-www-form-urlencoded. Additionally, if you are constructing the OAuth 1.0a signature, note that the JSON body is not included in the generation of the signature. Most OAuth libraries already account for this. If you are using [twurl](https://github.com/twitter/twurl), ensure you are using at least version 0.9.3.  

#### Summary

* Message is defined in JSON POST body
* Content-type header must be set to application/json
* JSON body is not included in the generation of the OAuth signature.  
     

### Retrieving Direct Messages

Retrieving past Direct Message is now accomplished with a single API endpoint: [GET direct\_messages/events/list](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/list-events). The significant difference with this new endpoint is that it now returns both sent and received messages in reverse chronological order. This may make it easier to rebuild a conversation. However, if you are only looking for sent or received messages you will need to post-process the response by referring to the sender\_id property.

Pagination is now based on a cursor value rather an ID of a Direct Message. A cursor property is returned with each response. [GET direct\_messages/events/list](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/list-events) will return up to 30 days of past messages, regardless of how many messages exist within the past 30 days. When a cursor is not returned, there are no more messages to be returned. The method for accessing individual Direct Messages with [GET direct\_messages/events/show](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/get-event) remains the same, although the Direct Message object returned has a different structure as described previously.

Finally, real-time access to Direct Messages will now be accomplished via webhook with the [Account Activity API](https://developer.twitter.com/content/developer-twitter/en/docs/accounts-and-users/subscribe-account-activity/overview). For guidance in migrating from User Streams or Site Streams, see the migration guide to Account Activity API for more information.

#### Summary

* Sent and Received messages are now returned on the same endpoint.
* Up to 30 days of messages returned.
* Cursor based pagination.
* Real-time access to Direct Message via webhook.  
     

### Deleting Direct Messages

Direct Messages can now be deleted with DELETE direct\_messages/events/destroy. The interface is largely the same requiring the ID of the message to delete. The key differences is the endpoint now requires a DELETE request instead of a POST request.  
  
How deleted Direct Messages are reflected in official Twitter clients remains the same. Direct Messages are only removed from the interface of the user context provided. Other members of the conversation can still access the Direct Message.

#### Summary

* Deleting a Direct Message requires the ID.
* New endpoint requires a DELETE request.
* How deleted Direct Messages are reflected in official Twitter clients remains unchanged.

**Questions about migrating to the new Direct Message endpoints?  
**Post your question to the developer community forum on [twittercommunity.com](https://twittercommunity.com/tags/c/rest-api/rest-api-v1-1/directmessages).

Next Steps
----------

*     Download our Direct Message Migration Guide (below)

Direct Messages[Direct Message - Migration Guide
--------------------------------](https://cdn.cms-twdigitalassets.com/content/dam/developer-twitter/pdfs-and-files/DM%20-%20Migration%20Guide.pdf)

[Download PDF](https://cdn.cms-twdigitalassets.com/content/dam/developer-twitter/pdfs-and-files/DM%20-%20Migration%20Guide.pdf)

POST direct\_messages/events/new (message\_create)

new-event

POST direct\_messages/events/new (message\_create)
==================================================

Publishes a new `message_create` event resulting in a Direct Message sent to a specified user from the authenticating user. Returns an event if successful. Supports publishing Direct Messages with optional Quick Reply and media attachment. Replaces behavior currently provided by [POST direct\_messages/new](https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/api-reference/new-message).

Requires a JSON POST body and `Content-Type` header to be set to `application/json`. Setting `Content-Length` may also be required if it is not automatically.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/direct_messages/events/new.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Content-Type | application/json |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 24-hour window | 1000 per user; 15000 per app |

Direct Message Rate Limiting[¶](#direct-message-rate-limiting "Permalink to this headline")
-------------------------------------------------------------------------------------------

When a message is received from a user you may send up to 5 messages in response within a 24 hour window. Each message received resets the 24 hour window and the 5 allotted messages. Sending a 6th message within a 24 hour window or sending a message outside of a 24 hour window will count towards rate-limiting. This behavior only applies when using the POST direct\_messages/events/new endpoint.

Event Object[¶](#event-object "Permalink to this headline")
-----------------------------------------------------------

|     |     |
| --- | --- |
| **type** (required) | The type of event you are posting. For Direct Messages, use `message_create` |
| **message\_create.target.recipient\_id** (required) | The ID of the user who should receive the direct message. |
| **message\_create.message\_data** (required) | The `Message Data Object` defining the content to deliver to the reciepient. |

Message Data Object[¶](#message-data-object "Permalink to this headline")
-------------------------------------------------------------------------

|     |     |
| --- | --- |
| **text** (required) | The text of your Direct Message. URL encode as necessary. Max length of 10,000 characters. Max length of 9,990 characters if used as a [Welcome Message](https://developer.twitter.com/en/docs/direct-messages/welcome-messages/api-reference/new-welcome-message). |
| **quick\_reply.type** (optional) | The Quick Reply type to present to the user (example requests below):<br><br>* **options** - Array of `Options` objects (20 max). |
| **attachment.type** (optional) | The attachment type. Can be media or location. |
| **attachment.media.id** (optional) | A media id to associate with the message. A Direct Message may only reference a single media\_id. See [Uploading Media](https://developer.twitter.com/en/docs/direct-messages/message-attachments/guides/attaching-media) for further details on uploading media. |

**Note**

See [Attaching Media to Direct Messages](https://developer.twitter.com/en/docs/direct-messages/message-attachments/guides/attaching-media) for details on including an image, GIF or video in Direct Messages.

### Example request[¶](#example-request "Permalink to this headline")

    curl --request POST 
    --url https://api.twitter.com/1.1/direct_messages/events/new.json 
    --header 'authorization: OAuth oauth_consumer_key="YOUR_CONSUMER_KEY", oauth_nonce="AUTO_GENERATED_NONCE", oauth_signature="AUTO_GENERATED_SIGNATURE", oauth_signature_method="HMAC-SHA1", oauth_timestamp="AUTO_GENERATED_TIMESTAMP", oauth_token="USERS_ACCESS_TOKEN", oauth_version="1.0"' 
    --header 'content-type: application/json' 
    --data '{"event": {"type": "message_create", "message_create": {"target": {"recipient_id": "RECIPIENT_USER_ID"}, "message_data": {"text": "Hello World!"}}}}'

    twurl -A 'Content-type: application/json' -X POST /1.1/direct_messages/events/new.json -d '{"event": {"type": "message_create", "message_create": {"target": {"recipient_id": "RECIPIENT_USER_ID"}, "message_data": {"text": "Hello World!"}}}}'

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
    "event": {
      "type": "message_create",
      "message_create": {
        "target": {
          "recipient_id": "RECIPIENT_USER_ID"
        },
        "message_data": {
          "text": "Hello World!",
        }
      }
    }
    }

**Note**

See [media/entity](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/entities-object1) documentation for details on returned media object properties.

GET direct\_messages/events/show

get-event

GET direct\_messages/events/show
================================

Returns a single Direct Message event by the given id.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/direct_messages/events/show.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 15  |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |
| --- | --- |
| **id** (required) | The id of the Direct Message event that should be returned. |

Example request using [Twurl](https://github.com/twitter/twurl)[¶](#example-request-using-twurl "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------

    twurl -X GET /1.1/direct_messages/events/show.json?id=110

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
      "event": 
        "id": "110", 
        "created_timestamp": "5300",
        "type": "message_create",
        "message_create": {
          ...
        }
      }
    }

GET direct\_messages/events/list

list-events

GET direct\_messages/events/list
================================

Returns all Direct Message events (both sent _and_ received) within the last 30 days. Sorted in reverse-chronological order.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/direct_messages/events/list.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 15/user |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |
| --- | --- |
| **count** (optional) | Max number of events to be returned. 20 default. 50 max. |
| **cursor** (optional) | For paging through result sets greater than 1 page, use the “next\_cursor” property from the previous request. |

Example request using [Twurl](https://github.com/twitter/twurl)[¶](#example-request-using-twurl "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------

    twurl -X GET /1.1/direct_messages/events/list.json

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

Events are returned in the `events` array. A `next_cursor` property will be returned if there are more events to be retrieved.

> **Note**
> 
> To determine if there are more event to retrieve, always look for the presence of a `next_cursor`. In rare cases the `events` array may be empty.

    {
      "next_cursor": "AB345dkfC",
      "events": [
        { "id": "110", "created_timestamp": "5300", ... },
        { "id": "109", "created_timestamp": "5200", ... },
        { "id": "108", "created_timestamp": "5200", ... },
        { "id": "107", "created_timestamp": "5200", ... },
        { "id": "106", "created_timestamp": "5100", ... },
        { "id": "105", "created_timestamp": "5100", ... },
        ...
      ]
    }

DELETE direct\_messages/events/destroy

delete-message-event

DELETE direct\_messages/events/destroy
======================================

Deletes the direct message specified in the required ID parameter. The authenticating user must be the recipient of the specified direct message. Direct Messages are only removed from the interface of the user context provided. Other members of the conversation can still access the Direct Messages. A successful delete will return a 204 http response code with no body content.

**Important**: This method requires an access token with RWD (read, write & direct message) permissions.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/direct_messages/events/destroy.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | 204 - No Content |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |
| --- | --- |
| **id** (required) | The id of the Direct Message event that should be deleted. |

Example request using [Twurl](https://github.com/twitter/twurl)[¶](#example-request-using-twurl "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------

    twurl -X DELETE "/1.1/direct_messages/events/destroy.json?id=938178981337088004"

Overview

Welcome Messages provide the ability to display a message to people who are entering a Direct Message conversation. Welcome messages can be customized for different referral paths. For example, users who click on Direct Message links in a Tweet or if a user enters a Direct Message view for the first time with no prior context. Welcome Messages can contain any content that a Direct Message would, including media, Quick Replies, and more.

Welcome Messages can be presented to users in two ways:

* [Deeplinking to a Welcome Message](https://developer.twitter.com/en/docs/direct-messages/welcome-messages/guides/deeplinking-to-welcome-message)  
    Create a URL that can be used anywhere to link a user to a specific message in the Direct Message view.
* [Setting a Default Welcome Message](https://developer.twitter.com/en/docs/direct-messages/welcome-messages/guides/setting-default-welcome-message)  
    Set the default message a user will see when they enter the Direct Message view.

Setting a default Welcome Message

Setting a Default Welcome Message
=================================

Without a default Welcome Message, users are presented with an empty Direct Message conversation view or the state of the previous conversation.  A Welcome Message may be set to default so that it is presented to the user when a Welcome Message deeplink is not used. Use a default Welcome Message to provide context to users including what services are provided, when they can receive response or provide Quick Reply options to start an automated conversation flow. All features available to Direct Messages can be used in a default Welcome Message.

When a Welcome Message is set as default, it will be presented to the user in the following scenarios:

* Direct Message compose view opened for the first time.
* Direct Message compose view opened for the first time since leaving a conversation.
* Direct Message compose view opened after no message activity for 7 days.

**Note:** Specifying a Welcome Message in a [deeplink](https://developer.twitter.com/en/docs/direct-messages/welcome-messages/guides/deeplinking-to-welcome-message) will always override the default Welcome Message. Deeplinking without a defined Welcome Message will follow default Welcome Message behavior defined above.

To set a default Welcome Message:

1. Create a new Welcome Message with [POST direct\_messages/welcome\_messages/new](https://developer.twitter.com/en/docs/direct-messages/welcome-messages/api-reference/new-welcome-message). Take note of the returned Welcome Message ID.
2. Create a new Welcome Message Rule using the Welcome Message ID with [POST direct\_messages/welcome\_messages/rules/new](https://developer.twitter.com/en/docs/direct-messages/welcome-messages/api-reference/new-welcome-message-rule).  
    

**Note:** Although an account can have many Welcome Messages, an account may only have a single “default” Welcome Message and only a single rule. If you have previously created a rule, you must [delete](https://developer.twitter.com/en/docs/direct-messages/welcome-messages/api-reference/delete-welcome-message-rule) the current rule before creating a new one. See [POST direct\_messages/welcome\_messages/rules/new](https://developer.twitter.com/en/docs/direct-messages/welcome-messages/api-reference/new-welcome-message-rule) documentation for more information regarding the future of rules.

Deeplinking to a Welcome Message

Deeplinking to a Welcome Message
================================

Every Welcome Message can be deeplinked to. When a user follows the deeplink, the Direct Message compose view will be opened with the specified Welcome Message presented. Deeplinks can be used anywhere from a website, an app, a Tweet or even another Direct Message conversation.

To create a Welcome Message deeplink:

1. Create a new Welcome Message with [POST direct\_messages/welcome\_messages/new](https://developer.twitter.com/en/docs/direct-messages/welcome-messages/api-reference/new-welcome-message). Take note of the returned Welcome Message ID.  
    
2. Construct a Direct Message deeplink with the recipient\_id and welcome\_message\_id query string parameters defined.  
    

Example Direct Message Deeplink:  

https://twitter.com/messages/compose?recipient\_id= 3805104374&welcome\_message\_id=12345

**Note:** You can create as many Welcome Messages as you require and all Welcome Messages can be deeplinked to.

Deeplinking from a Tweet   

----------------------------

By simply including the Direct Message deeplink URL at the end of a Tweet, your can append a "Send a private message" button to the bottom of the Tweet. Read more about using Direct Message deeplinks in Tweets in [this blog post](https://blog.twitter.com/marketing/en_us/a/2016/best-practices-using-direct-messages-for-customer-service-0.html).

Using a [Direct Message Card](https://blog.twitter.com/2017/drive-discovery-of-bots-other-personalized-customer-experiences-in-direct-messages), businesses can capture people’s attention with engaging image or video creatives, and include up to four fully customizable call-to-action buttons. Each call-to-action button can deeplink to a unique Welcome Message. The Direct Message Card is currently available in limited beta to Twitter advertisers. Contact your Twitter representative for more information.  

Deeplinking from a Website  

-----------------------------

Direct Message deeplinks may also be used to deeplink from a website or other external source like a mobile app. For more details on deeplinking to Welcome Messages from a website, see [Message Button](https://dev.twitter.com/web/message-button) documentation.

DELETE direct\_messages/welcome\_messages/destroy

delete-welcome-message

DELETE direct\_messages/welcome\_messages/destroy
=================================================

Deletes a Welcome Message by the given id.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/direct_messages/welcome_messages/destroy.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | 204 - No Content |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |
| --- | --- |
| **id** (required) | The id of the Welcome Message that should be deleted. |

Example request using [Twurl](https://github.com/twitter/twurl)[¶](#example-request-using-twurl "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------

    twurl -X DELETE /1.1/direct_messages/welcome_messages/destroy.json?id=844385345234

DELETE direct\_messages/welcome\_messages/rules/destroy

delete-welcome-message-rule

DELETE direct\_messages/welcome\_messages/rules/destroy
=======================================================

Deletes a Welcome Message Rule by the given id.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/direct_messages/welcome_messages/rules/destroy.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | 204 - No Content |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |
| --- | --- |
| **id** (required) | The id of the Welcome Message Rule that should be deleted. |

Example request using [Twurl](https://github.com/twitter/twurl)[¶](#example-request-using-twurl "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------

    twurl -X DELETE /1.1/direct_messages/welcome_messages/rules/destroy.json?id=9910934913490319

GET direct\_messages/welcome\_messages/show

get-welcome-message

GET direct\_messages/welcome\_messages/show
===========================================

Returns a Welcome Message by the given id.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/direct_messages/welcome_messages/show.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 15  |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |
| --- | --- |
| **id** (required) | The id of the Welcome Message that should be returned. |

Example request using [Twurl](https://github.com/twitter/twurl)[¶](#example-request-using-twurl "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------

    twurl -X GET /1.1/direct_messages/welcome_messages/show.json?id=844385345234

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
      "welcome_message" : {
        "id": "844385345234",
        "created_timestamp": "1470182274821",
        "message_data": {
          "text": "Welcome!",
          "attachment": {
            "type": "media",
            "media": {
              ...
            }
          }
        }
      }
    }

GET direct\_messages/welcome\_messages/rules/show

get-welcome-message-rule

GET direct\_messages/welcome\_messages/rules/show
=================================================

Returns a Welcome Message Rule by the given id.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/direct_messages/welcome_messages/rules/show.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 15  |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |
| --- | --- |
| **id** (required) | The id of the Welcome Message Rule that should be returned. |

Example request using [Twurl](https://github.com/twitter/twurl)[¶](#example-request-using-twurl "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------

    twurl -X GET /1.1/direct_messages/welcome_messages/rules/show.json?id=9910934913490319

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
      "welcome_message_rule" : {
        "id": "9910934913490319",
        "created_timestamp": "1470182394258",
        "welcome_message_id": "844385345234"
      }
    }

GET direct\_messages/welcome\_messages/rules/list

list-welcome-message-rules

GET direct\_messages/welcome\_messages/rules/list
=================================================

Returns a list of Welcome Message Rules.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/direct_messages/welcome_messages/rules/list.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 15  |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |
| --- | --- |
| **count** (optional) | Number of welcome message rules to be returned. Max of 50. Default is 20. |
| **cursor** (optional) | For paging through result sets greater than 1 page, use the “next\_cursor” property from the previous request. |

Example request using [Twurl](https://github.com/twitter/twurl)[¶](#example-request-using-twurl "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------

    twurl -X GET "/1.1/direct_messages/welcome_messages/rules/list.json?count=2&cursor=MTIzNDU2Nzg"

Example Responses[¶](#example-responses "Permalink to this headline")
---------------------------------------------------------------------

Welcome message rules are returned in the `welcome_message_rules` array. A `next_cursor` property will be returned if there are more welcome message rules to be retrieved.

> **Note**
> 
> To determine if there are more welcome message rules to retrieve, always look for the presence of a `next_cursor`. In rare cases the `welcome_message_rules` array may be empty.

    {
      "welcome_message_rules": [
        {
          "id": "9910934913490319",
          "created_timestamp": "1470182394258",
          "welcome_message_id": "844385345234"
        },
        {
          "id": "9910934913490431",
          "created_timestamp": "1470182394265",
          "welcome_message_id": "844385345238"
        }
      ],
      "next_cursor": "NDUzNDUzNDY3Nzc3"
    }

GET direct\_messages/welcome\_messages/list

list-welcome-messages

GET direct\_messages/welcome\_messages/list
===========================================

Returns a list of Welcome Messages.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/direct_messages/welcome_messages/list.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 15  |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |
| --- | --- |
| **count** (optional) | Number of welcome messages to be returned. Max of 50. Default is 20. |
| **cursor** (optional) | For paging through result sets greater than 1 page, use the “next\_cursor” property from the previous request. |

Example request using [Twurl](https://github.com/twitter/twurl)[¶](#example-request-using-twurl "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------

    twurl -X GET "/1.1/direct_messages/welcome_messages/list.json?count=2&cursor=MTIzNDU2Nzg"

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

Welcome Messages are returned in the `welcome_messages` array. A `next_cursor` property will be returned if there are more welcome messages to be retrieved.

> **Note**
> 
> To determine if there are more welcome messages to retrieve, always look for the presence of a `next_cursor`. In rare cases the `welcome_messages` array may be empty.

    {
      "welcome_messages": [
        {
          "id": "844385345234",
          "created_timestamp": "1470182274821",
          "message_data": {
            "text": "Welcome!",
            "attachment": {
              "type": "media",
              "media": {
                ...
              }
            }
          }
        },
        {
          "id": "844385345238",
          "created_timestamp": "1470182275399",
          "message_data": {
            "text": "Welcome Again!",
            "attachment": {
              "type": "media",
              "media": {
                ...
              }
            }
          }
        }
      ],
      "next_cursor": "NDUzNDUzNDY3Nzc3"
    }

POST direct\_messages/welcome\_messages/new

new-welcome-message

POST direct\_messages/welcome\_messages/new
===========================================

Creates a new Welcome Message that will be stored and sent in the future from the authenticating user in defined circumstances. Returns the message template if successful. Supports publishing with the same elements as Direct Messages (e.g. Quick Replies, media attachments).

Requires a JSON POST body and `Content-Type` header to be set to `application/json`. Setting `Content-Length` may also be required if it is not automatically.

See the [Welcome Messages overview](https://developer.twitter.com/en/docs/direct-messages/welcome-messages/overview) to learn how to work with Welcome Messages.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/direct_messages/welcome_messages/new.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Content-Type | application/json |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

Welcome Message Object[¶](#welcome-message-object "Permalink to this headline")
-------------------------------------------------------------------------------

|     |     |
| --- | --- |
| **message\_data** (required) | The `Message Data Object` defining the content of the message template. See [POST direct\_messages/events/new (message\_create)](https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/api-reference/new-event) for Message Data object details. |
| **name** (optional) | A human readable name for the Welcome Message. This is not displayed to the user. Max length of 100 alpha numeric characters including hyphens, underscores, spaces, hashes and at signs. |

> **Note**
> 
> See [Attaching Media to Direct Messages](https://developer.twitter.com/en/docs/direct-messages/message-attachments/guides/attaching-media) for details on including an image, GIF or video in Direct Messages.

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

    {
      "welcome_message" : {
        "name": "simple_welcome-message 01",
        "message_data": {
          "text": "Welcome!",
          "attachment": {
            "type": "media",
            "media": {
              "id": "48909183894931"
            }
          }
        }
      }
    }

### Example request using [Twurl](https://github.com/twitter/twurl)[¶](#example-request-using-twurl "Permalink to this headline")

    twurl -A 'Content-type: application/json' /1.1/direct_messages/welcome_messages/new.json -d '{"name": "simple_welcome-message 01", "welcome_message": {"message_data": {"text": "Welcome!", "attachment": {"type": "media", "media": {"id": "48909183894931"}}}}}'

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
      "welcome_message" : {
        "id": "844385345234",
        "created_timestamp": "1470182274821",
        "message_data": {
          "text": "Welcome!",
          "attachment": {
            "type": "media",
            "media": {
              ...
            }
          }
        }
      }
      "name": "simple_welcome-message 01"
    }

POST direct\_messages/welcome\_messages/rules/new

new-welcome-message-rule

POST direct\_messages/welcome\_messages/rules/new
=================================================

Creates a new Welcome Message Rule that determines which Welcome Message will be shown in a given conversation. Returns the created rule if successful.

Requires a JSON POST body and `Content-Type` header to be set to `application/json`. Setting `Content-Length` may also be required if it is not automatically.

Additional rule configurations are forthcoming. For the initial beta release, the most recently created Rule will always take precedence, and the assigned Welcome Message will be displayed in the conversation.

See the [Welcome Messages overview](https://developer.twitter.com/en/docs/direct-messages/welcome-messages/overview) to learn how to work with Welcome Messages.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/direct_messages/welcome_messages/rules/new.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Content-Type | application/json |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

Welcome Message Rule Object[¶](#welcome-message-rule-object "Permalink to this headline")
-----------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| **welcome\_message\_id** (required) | The ID of the Welcome Message that will be sent when this Rule is triggered. |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

    {
      "welcome_message_rule": {
        "welcome_message_id": "844385345234"
      }
    }

### Example request using [Twurl](https://github.com/twitter/twurl)[¶](#example-request-using-twurl "Permalink to this headline")

    twurl -A 'Content-type: application/json' -X POST /1.1/direct_messages/welcome_messages/rules/new.json -d '{"welcome_message_rule": {"welcome_message_id": "844385345234"}}'

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
      "welcome_message_rule" : {
        "id": "9910934913490319",
        "created_timestamp": "1470182394258",
        "welcome_message_id": "844385345234"
      }
    }

PUT direct\_messages/welcome\_messages/update

update-welcome-message

PUT direct\_messages/welcome\_messages/update
=============================================

Updates a Welcome Message by the given ID. Updates to the `welcome_message` object are atomic. For example, if the Welcome Message currently has `quick_reply` defined and you only provde `text`, the `quick_reply` object will be removed from the Welcome Message.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/direct_messages/welcome_messages/update.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |
| --- | --- |
| **id** (required) | The id of the Welcome Message that should be updated. |

Example request using [Twurl](https://github.com/twitter/twurl)[¶](#example-request-using-twurl "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------

    twurl -A 'Content-type: application/json' -X PUT '/1.1/direct_messages/welcome_messages/update.json?id=4893198399134' -d ‘
    {
      "message_data":{
        "text": "Welcome!"
      }
    }

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
      "name": "Generic Welcome 01"
      "welcome_message": {
        "id": "4893198399134",
        "created_timestamp": "154903045",
        "message_data": {
          "text": "Welcome!"
        }
      },
      "apps": {
        "8829219": {
          "id": "8829219",
          "name": "Furni",
          "url": "https://developer.twitter.com"
        }
      }
    }

Overview

Overview
--------

Media may be attached and retrieved for Direct Messages through authenticated calls with app-user authorization.

Direct Messages with an image will contain a media object with relevant details, check our Twitter data objects dictionary for more details [here](https://developer.twitter.com/content/developer-twitter/en/docs/tweets/data-dictionary/overview/entities-object#media).  
 

### Uploading and attaching media (images, GIFs, video) to a Direct Message.

[Media for Direct Messages upload & attachment guide](https://developer.twitter.com/en/docs/direct-messages/message-attachments/guides/attaching-media) 

### Retrieving Direct Message media

For media in Direct Messages `media_url` is the same https URL as `media_url_https` and must be accessed by signing a request with the user’s access token using OAuth 1.0A.

It is not possible to directly embed these images in a web page.

[Media in Direct Messages retrieval guide](https://developer.twitter.com/en/docs/direct-messages/message-attachments/guides/retrieving-media)

Attaching media

Attaching media
---------------

[POST direct\_messages/events/new](https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/api-reference/new-event.html) supports media attachments of type image, GIF and video. The process is similar to attaching media to Tweets:

1. Chunk upload the image, GIF or video.
2. Send Direct Message with media attachment.

It is possible to attach the same media asset to multiple Direct Messages. However, you must get users’ express consent to set media as “shared,” and must provide them with clear notice that “shared” media will be viewable by anyone with the media’s URL. See the documented process below for how to set media to "shared."

**Note:** Media for use with Direct Messages should be uploaded using the asynchronous chunked upload process described on this page.  
 

### 1\. Chunk upload media

* Chunk upload the media file starting with [POST media/upload (INIT)](https://developer.twitter.com/en/docs/media/upload-media/api-reference/post-media-upload-init.html).
* Set the media\_category to dm\_image, dm\_gif or dm\_video appropriately.
* If reusing the media asset across multiple Direct Messages, you must set shared to true during the initial upload.
* If attaching a media asset to a Welcome Message, you must set shared to true during the initial upload.
* Uploaded media can only be shared across Direct Messages created by the same user.
* See [Uploading Media](https://developer.twitter.com/en/docs/media/upload-media/uploading-media/chunked-media-upload.html) for subsequent [APPEND](https://developer.twitter.com/en/docs/media/upload-media/api-reference/post-media-upload-append.html) and [FINALIZE](https://developer.twitter.com/en/docs/media/upload-media/api-reference/post-media-upload-finalize.html) steps.
* The returned media ID will be used when sending the Direct Message. If you did not set shared to true the media ID can only be used in a single Direct Message.

Once a media ID is generated, it must be attached to a Direct Message within 24 hours.

#### Parameters

|     |     |
| --- | --- |
| **media\_category  <br>**(required) | The media category: dm\_image, dm\_gif, dm\_video |
| **shared** | Set to true if media asset will be reused for multiple Direct Messages. Default is false. |

See [POST media/upload (INIT)](https://developer.twitter.com/en/docs/media/upload-media/api-reference/post-media-upload-init.html) documentation for all parameters and full details.  
 

### 2\. Send Direct Message with media attachment

* Define an attachment object in the message\_data object in the Direct Message event json body.
* Set attachment type property to media.
* Set the media.id property to the media ID returned in the previous chunk upload process.  
     

#### Parameters

|     |     |
| --- | --- |
| **attachment.type  <br>**(required) | Must be set to media. |
| **attachment.media.id  <br>**(required) | A media ID to associate with the message. A Direct Message may only reference a single media id. |

See [POST direct\_messages/events/new](https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/api-reference/new-event.html) documentation for all parameters and full details.

Attaching location

Attaching location
==================

Locations can be attached to Direct Messages created with [POST direct\_messages/events/new](https://dev.twitter.com/rest/reference/post/direct_messages/events/new). The location is defined as an attachement object with longitue and latitude coordinates or a Twitter place.  

Example message with shared coordinate attachment
-------------------------------------------------

      `{   "event": {     "type": "message_create",     "message_create": {       "target": {         "recipient_id": "844385345234"       },       "message_data": {         "text": "Here's my location",         "attachment": {           "type": "location",           "location": {             "type": "shared_coordinate",             "shared_coordinate": {               "coordinates": {                 "type": "Point",                 "coordinates": [-122.443893, 37.771718]               }             }           }         }       }     }   } }`
    

Example message with shared place attachment
--------------------------------------------

      `{   "event": {     "type": "message_create",       "message_create": {         "target": {           "recipient_id": "844385345234"         },         "message_data": {           "text": "Here's my location",           "attachment": {             "type": "location",             "location": {               "type": "shared_place",               "shared_place": {                 "place": {                   "id": "123456"                 }               }             }           }         }       }     }   } }`
    

**Note:** Not all place IDs are discoverable with [GET geo/search](https://developer.twitter.com/en/docs/geo/places-near-location/api-reference/get-geo-search.html). To retrieve all available details for a place ID you may also use [GET geo/id/:place\_id](https://developer.twitter.com/en/docs/twitter-api/v1/geo/place-information/api-reference/get-geo-id-place_id).

Retrieving media

Retrieving media
----------------

Media in direct messages must be retrieved via an authenticated app-user GET request.  It is advised that applications store user's access tokens to use for direct message media retrieval.

For media in direct messages, `media_url` is the same https URL as `media_url_https` and must be accessed by signing a request with the user’s access token using OAuth 1.0A.

You can no longer access media via an authenticated www.twitter.com session. We cannot prescribe how you should update your integration if you are affected by this change. However, here is one implementation path to address this that we endorse:

* Make sure you’re storing a user’s Twitter access token, if you’re not already
* Set up an endpoint to make OAuth requests to Twitter to retrieve DM images on behalf of the user using the user’s Twitter access token:
    * The endpoint should be a GET endpoint
    * The endpoint must be authenticated
    * The endpoint must deny all cross-origin requests
    * The endpoint must only be used for making requests to retrieve DM images, and must deny requests to other Twitter APIs  
         

Example request:

      `curl --request GET \    --url https://ton.twitter.com/1.1/ton/data/dm/1034828552951160836/1034828533812486145/oP5p359h.jpg \    --header 'authorization: OAuth  oauth_consumer_key="6NxxxxxxCS",  oauth_nonce="Sbxxxxxx2G",  oauth_signature="637xxxxxxM%3D",  oauth_signature_method="HMAC-SHA1",  oauth_timestamp="1535557741",  oauth_token="600-SQxxxxxxcqIF",  oauth_version="1.0"'`
    

  
If you display images in a web interface, the URL from the newly created endpoint could be used in a <img> tag to display to users of your products.

Example:

      `<img src="fetch_dm_image?url=https://ton.twitter.com/i/ton/data/dm/xx.jpg">`

Overview

Messages published with [POST direct\_messages/events/new (message\_create)](https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/api-reference/new-event) can have an attached Quick Reply to request stuctured input from a user.

[Quick Reply Options API reference](https://developer.twitter.com/en/docs/direct-messages/quick-replies/api-reference/options)List of up to 20 predefined options presented for a user to choose from.

Quick Reply attachment metadata will not be accessible via legacy REST and Streaming endpoints. Only text values will be delivered in the legacy Direct Message JSON format.

Options Quick Reply

options

Options Quick Reply
===================

List of up to 20 predefined options presented for a user to choose from. For use with [POST direct\_messages/events/new (message\_create)](https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/api-reference/new-event).

Quick Reply Object[¶](#quick-reply-object "Permalink to this headline")
-----------------------------------------------------------------------

|     |     |
| --- | --- |
| **quick\_reply.type** (required) | Must be set to `options` |
| **quick\_reply.option** (required) | An array of `options` objects. |

Option Object[¶](#option-object "Permalink to this headline")
-------------------------------------------------------------

|     |     |
| --- | --- |
| **label** (required) | The text label displayed on the button face. Label text is returned as the user's message response. String, max length of 36 characters including spaces. Values with URLs are not allowed and will return an error. |
| **description** (optional) | Optional description text displayed under label text. All options must have this property defined if property is present in any option. Text is auto-wrapped and will display on a max of two lines and supports `n` for controlling line breaks. Description text is not include in the user's message response. String, max length of 72 characters including spaces. |
| **metadata** (optional) | Metadata that will be sent back in the webhook request. String, max length of 1,000 characters including spaces. |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

Although not required, if one option defines the `description`, then all `options` must contain the `description`.

    {
      "event": {
        "type": "message_create",
        "message_create": {
          "target": {
            "recipient_id": "844385345234"
          },
          "message_data": {
            "text": "What's your favorite type of bird?",
            "quick_reply": {
              "type": "options",
              "options": [
                {
                  "label": "Red Bird",
                  "description": "A description about the red bird.",
                  "metadata": "external_id_1"
                },
                {
                  "label": "Blue Bird",
                  "description": "A description about the blue bird.",
                  "metadata": "external_id_2"
                },
                {
                  "label": "Black Bird",
                  "description": "A description about the black bird.",
                  "metadata": "external_id_3"
                },
                {
                  "label": "White Bird",
                  "description": "A description about the white bird.",
                  "metadata": "external_id_4"
                }
              ]
            }
          }
        }
      }
    }

Example User Response[¶](#example-user-response "Permalink to this headline")
-----------------------------------------------------------------------------

The `type` and `metadata` will be present in the `quick_reply_response` object. The `label` for the chosen option is sent as the message `text`.

    {
      "event": {
        "type": "message_create",
        "id": "1234858592",
        "created_timestamp": "1392078023603",
        "message_create": {
          "target": {
            "recipient_id": "1234858592"
          },
          "sender_id": "3805104374",
          "message_data": {
            "text": "Blue Bird",
            "entities": {
              "hashtags": [],
              "symbols": [],
              "urls": [],
              "user_mentions": []
            },
            "quick_reply_response": {
              "type": "options",
              "metadata": "external_id_2"
            }
          }
        }
      }
    }

Overview

Buttons enable developers to add up to three call-to-action (CTA) buttons to any Direct Message or Welcome Message. These buttons can be used to open any URL from the Direct Message compose view. The text labels displayed on the buttons can be fully customized.

This feature is intended to make it easier for users to complete actions outside of Direct Messages, whether in a webview or in another part of the Twitter app. For instance, buttons can be used to:

* **Open a webview** to interact with a mobile web page that is better suited for completing an action than completing that action in messaging. For example, completing a credit card purchase or interacting with a side-by-side comparison of different products.
    
* **Compose a Tweet** at the end of a Direct Message interaction. For example, to tell others about a bot or share a coupon publicly. This can be accomplished by using the Tweet [web intents URL scheme](https://dev.twitter.com/web/intents).
    
* **Follow a user** account at the end of a Direct Message interaction. For example, as a final request from a business at the end of a customer service interaction. This can be accomplished using the Follow [web intents URL scheme](https://dev.twitter.com/web/intents).
    
* **Send a Direct Message** to a different account. For example, to direct a user from a marketing-related bot to a separate dedicated customer service @username to get help from a person. This can be accomplished using the Direct Message URL deep link scheme. Example below.
    
    https://twitter.com/messages/compose?recipient\_id=3805104374

Buttons

buttons

Buttons
=======

Buttons enable developers to add up to three call-to-action (CTA) buttons to any Direct Message or Welcome Message. These buttons can be used to open any URL from the Direct Message compose view. The text labels displayed on the buttons can be fully customized.

  
  

This feature is intended to make it easier for users to complete actions outside of Direct Messages, whether in a webview or in another part of the Twitter app. For instance, buttons can be used to:

* **Open a webview** to interact with a mobile web page that is better suited for completing an action than completing that action in messaging. For example, completing a credit card purchase or interacting with a side-by-side comparison of different products.
    
* **Compose a Tweet** at the end of a Direct Message interaction. For example, to tell others about a bot or share a coupon publicly. This can be accomplished by using the Tweet [web intents URL scheme](https://dev.twitter.com/web/intents).
    
* **Follow a user** account at the end of a Direct Message interaction. For example, as a final request from a business at the end of a customer service interaction. This can be accomplished using the Follow [web intents URL scheme](https://dev.twitter.com/web/intents).
    
* **Send a Direct Message** to a different account. For example, to direct a user from a marketing-related bot to a separate dedicated customer service @username to get help from a person. This can be accomplished using the Direct Message URL deep link scheme. Example below.
    
        https://twitter.com/messages/compose?recipient_id=3805104374
    

CTAs Object[¶](#ctas-object "Permalink to this headline")
---------------------------------------------------------

Buttons can be added to a Direct Message by defining a `ctas` array of 1-3 objects.

|     |     |
| --- | --- |
| **type** (required) | Defines the type of button to display. Currently must be set to `web_url`. |
| **label** (required) | The text that will be displayed to the user on each button. Max string length of 36 characters. |
| **url** (required) | A valid http or https target URL of the button. |
| **tco\_url** (read only) | The t.co version of the URL will be returned in a POST response and on the read path (GET requests) only. |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

    {
      "event": {
        "type": "message_create",
        "message_create": {
          "target": {
            "recipient_id": "844385345234"
          },
          "message_data": {
            "text": "Flight SF8020 from San Francisco to Montreal is ahead of schedule and will land in approximately 15 minutes. Can we help with anything else?",
            "ctas": [
              {
                "type": "web_url",
                "label": "See flight details",
                "url": "https://www.myairline.domain/see-flight-details"
              },
              {
                "type": "web_url",
                "label": "Map it",
                "url": "https://www.myairline.domain/map-it"
              },
              {
                "type": "web_url",
                "label": "Visit MyAirline.domain",
                "url": "https://www.myairline.domain/"
              }
            ]
          }
        }
      }
    }

Example Read Response[¶](#example-read-response "Permalink to this headline")
-----------------------------------------------------------------------------

The following JSON payload is an example of what will be received using an [Account Activity webhook](https://developer.twitter.com/en/docs/accounts-and-users/subscribe-account-activity/overview.html) or GET request like [GET direct\_messages/events/list](https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/api-reference/list-events). Notice the addition of the t.co short URL representation of the full URLs.

    {
      "event": {
        "type": "message_create",
        "message_create": {
          "target": {
            "recipient_id": "844385345234"
          },
          "message_data": {
            "text": "Flight SF8020 from San Francisco to Montreal is ahead of schedule and will land in approximately 15 minutes. Can we help with anything else?",
            "ctas": [
              {
                "type": "web_url",
                "label": "See flight details",
                "tco_url": "https://t.co/foo1",
                "url": "https://www.myairline.domain/see-flight-details"
              },
              {
                "type": "web_url",
                "label": "Map it",
                "tco_url": "https://t.co/foo2",
                "url": "https://www.myairline.domain/map-it"
              },
              {
                "type": "web_url",
                "label": "Visit MyAirline.domain",
                "tco_url": "https://t.co/foo3",
                "url": "https://www.myairline.domain/"
              }
            ]
          }
        }
      }
    }

Overview

Send typing indicators or read receipts that are displayed in the Direct Message conversation view to let users know that their messages are being processed.  
  

* [Typing indicators](https://developer.twitter.com/en/docs/direct-messages/typing-indicator-and-read-receipts/api-reference/new-typing-indicator)  
    A visual aniamtion in the Direct Message view notifying the recipient that the user is typing or thinking.
* [Read receipts](https://developer.twitter.com/en/docs/direct-messages/typing-indicator-and-read-receipts/api-reference/new-read-receipt)  
    A subtle visual notification in the Direct Message view notifying the recipient that the user has read or seen the last message.

POST direct\_messages/mark\_read

new-read-receipt

POST direct\_messages/mark\_read
================================

Marks a message as read in the recipient’s Direct Message conversation view with the sender.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/direct_messages/mark_read.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Content-Type | application/json |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 1000 / 15 minutes |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |
| --- | --- |
| **last\_read\_event\_id** (required) | The message ID of the most recent message to be marked read. All messages before it will be marked read as well. |
| **recipient\_id** (required) | The user ID of the user the message is from. |

Example request using [Twurl](https://github.com/twitter/twurl)[¶](#example-request-using-twurl "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------

    twurl -X POST /1.1/direct_messages/mark_read.json -d "last_read_event_id=8754578330382663743" -d "recipient_id=3805104374" 

HTTP Response Codes[¶](#http-response-codes "Permalink to this headline")
-------------------------------------------------------------------------

Response contains no body.

| Code | Message |
| --- | --- |
| 204 | Read receipt successfully sent. |
| 400 | Missing or invalid parameter(s) included in request. |

Webhook Event[¶](#webhook-event "Permalink to this headline")
-------------------------------------------------------------

If using the [Account Activity API](https://developer.twitter.com/en/docs/accounts-and-users/subscribe-account-activity/overview), the following JSON payload will be sent to your webhook for all subscribed users.

    {
      "direct_message_mark_read_events": [
        {
          "created_timestamp": "1288834974657",
          "sender_id": "2244994945",
          "last_read_event_id": "877260925346103299",
          "target": {
            "recipient_id": "3805104374"
          }
        }
      ],
      "users": {
        // hydrated user objects
      }
    }

POST direct\_messages/indicate\_typing

new-typing-indicator

POST direct\_messages/indicate\_typing
======================================

Displays a visual typing indicator in the recipient’s Direct Message conversation view with the sender. Each request triggers a typing indicator animation with a duration of ~3 seconds.

Usage[¶](#usage "Permalink to this headline")
---------------------------------------------

A rudimentary approach would be to invoke an API request on every keypress or input event, however the application may quickly hit rate limits. A more sophisticated approach is to capture input events, but limit API requests to a specified interval based on the behavior of your users and the rate limit specified below.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/direct_messages/indicate_typing.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Content-Type | application/json |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 1000 / 15 minutes |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |
| --- | --- |
| **recipient\_id** (required) | The user ID of the user to receive the typing indicator. |

Example request using [Twurl](https://github.com/twitter/twurl)[¶](#example-request-using-twurl "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------

    twurl -X POST /1.1/direct_messages/indicate_typing.json -d "recipient_id=3805104374"

HTTP Response Codes[¶](#http-response-codes "Permalink to this headline")
-------------------------------------------------------------------------

Response contains no body.

| Code | Message |
| --- | --- |
| 204 | Typing indicator successfully sent. |
| 400 | Missing or invalid parameter(s) included in request. |

Webhook Event[¶](#webhook-event "Permalink to this headline")
-------------------------------------------------------------

**Coming Soon:** If using the [Account Activity API](https://developer.twitter.com/en/docs/accounts-and-users/subscribe-account-activity/overview), the following JSON payload will be sent to your webhook for all subscribed users.

    {
      "direct_message_indicate_typing_events": [
        {
          "created_timestamp":"1288834974657",
          "sender_id":"2244994945",
          "target":{
            "recipient_id":"3805104374"
          }
        }
      ],
      "users": {
        // hydrated user objects
      }
    }

Overview

When creating an app to manage Direct Messages, having context of where the user came from or what application was responsible for sending the message can be important information for managing the conversation. Having this context can help improve analytics or determine the next action your app should take. To provide this context the following is available in Direct Message event objects when applicable.

Event properties
----------------

Message create event properties for conversation management.

* [initiated\_via](https://developer.twitter.com/en/docs/direct-messages/conversation-management/guides/initiated-via)  
    Provides the Twitter entity (Tweet or Welcome Message) that preceded the Direct Message in conversation.
* [source\_app](https://developer.twitter.com/en/docs/direct-messages/conversation-management/guides/source-app)  
    Provides information about the Twitter app the authenticating account used to send the Direct Message.

initiated\_via

When users communicate with businesses through Direct Messages, they may be guided by [Welcome Messages](https://dev.twitter.com/rest/direct-messages/direct-messages/welcome-messages) or led to a private conversation via a Direct Message deeplink. In these cases, it can be important for developers to know if another object preceded the DM in conversation. For example, Initiated Via helps a customer service agent see the full conversation history or enable a bot developer to perform A/B testing of different welcome messages.

The initiated\_via object in the Direct Message event object indicates the ID of the Twitter entity that directly preceded the DM in the sender’s context. Currently tweet\_id and welcome\_message\_id may be included. The initiated\_via object is only present if a Twitter entity directly preceded the DM.

initiated\_via object
---------------------

|     |     |
| --- | --- |
| initiated\_via.tweet\_id | The ID of the Tweet with Direct Message Prompt the event was initiated from if one was used. |
| initiated\_via.welcome\_message\_id | The ID of the Welcome Message immediately preceding the event if one was used. |

**Note:** Direct Messages are never referenced as an entity type under the “initiated\_via” object. Developers should continue to rely on IDs for ordering Direct Message events.

Example Direct Message Event
----------------------------

The following Direct Message event was preceded by a Direct Message prompt from a Tweet or a Welcome Message was presented to the user.  

      `{   "type": "message_create",   "id": "1234858592",   "created_timestamp": "1392078023603",   "initiated_via": {     "tweet_id": "123456",     "welcome_message_id": "456789"   },   "message_create": {     "target": {       "recipient_id": "1234858592"     },     "sender_id": "3805104374",     "source_app_id": "268278",     "message_data": {       "text": "Blue Bird",       "entities": {         "hashtags": [],         "symbols": [],         "urls": [],         "user_mentions": [],       },       "quick_reply_response": {         "type": "options",         "metadata": "external_id_2"       },       "attachment": {         "type": "media",         "media": {          ...         }       }     }   } }`

source\_app

source\_app
===========

Some Twitter accounts may make use of more than one application to send Direct Messages — such as when a human social care app is used alongside a separate bot app to manage the same account. In these cases, it can be helpful for developers to know which app was used to send a given message.

The new source\_app object will return this information for all DMs sent by an account. This object is included in the JSON payload for webhooks and REST endpoints. It is relevant on the read path only — Twitter automatically adds this information based on the app authentication used to post a DM. This value will not be returned in the response for POST events/new.json.

**Note:** This same pattern exists with Tweets with the source property, however the JSON structure is different. Please also note that this object will not be included for DMs received by an authenticating user and is only included for DMs sent by the authenticating user.

source\_app object
------------------

|     |     |
| --- | --- |
| id  | The ID of the Twitter app used by the authenticating user to send the DM. |
| name | The name of the Twitter app used by the authenticating user to send the DM. |
| url | The URL of the Twitter app used by the authenticating user to send the DM. |

Example for GET direct\_messages/events/list
--------------------------------------------

      `{   "event": {     "type": "message_create",     "id": "854103000570187779",     "created_timestamp": "1492468998459",     "message_create": {       "target": {         "recipient_id": "3340250004"       },       "sender_id": "51378538",       "source_app_id": "268278",       "message_data": {         "text": "Hello",         "entities": {           "hashtags": [],           "symbols": [],           "user_mentions": [],           "urls": []         }       }     }   }   "apps": {     "268278": {       "id": "268278",       "name": "Twitter Web Client",       "url": "http://twitter.com"     }   } }`
    

Example for GET direct\_messages/events/show
--------------------------------------------

      `{   "events": [     {       "type": "message_create",       "id": "854103000570187779",       "created_timestamp": "1492468998459",       "message_create": {         "target": {           "recipient_id": "3340250004"         },         "sender_id": "51378538",         "source_app_id": "268278",         "message_data": {           "text": "Hello",           "entities": {             "hashtags": [],             "symbols": [],             "user_mentions": [],             "urls": []           }         }       }     },     {       "type": "message_create",       "id": "867807494898188291",       "created_timestamp": "1495736404524",       "message_create": {         "target": {           "recipient_id": "3340250004"         },         "sender_id": "51378538",         "source_app_id": "9206597",         "message_data": {           "text": "World",           "entities": {             "hashtags": [],             "symbols": [],             "user_mentions": [],             "urls": []           }         }       }     },   ],   "apps": {     "9206597": {       "id": "9206597",       "name": "BeeToSeaBiz TestApp Awesome",       "url": "https://twitter.com/beetoseabiz"     },     "268278": {       "id": "268278",       "name": "Twitter Web Client",       "url": "http://twitter.com"     }   } }`

Overview

Custom profiles allow a Direct Message author to present a different identity than that of the Twitter account being used. For example, brands may want customer service agents posting under a single Twitter account to use their own name and photo. A custom profile may also be used to attach a unique identity to a message authored by an automated application or bot so that users clearly understand they are talking to a bot.

To use the custom profiles feature:
-----------------------------------

1. Posting accounts must be Verified and on an allowlist to use this feature.
2. Create a custom profile with a name and photo using the API.
3. Attach a custom profile ID to new Direct Message POST requests. Valid custom profiles will override the default avatar.

Send a Direct Message with custom profile

attach-profile

Send a Direct Message with custom profile
=========================================

To attach a custom profile to a Direct Message add a `event.custom_profile_id` parameter to the [POST direct\_messages/events/new.json](https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/api-reference/new-event) request.

_Note:_ See [full documentation](https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/api-reference/new-event) for all properties. Custom profiles can also be used with [welcome messages](https://developer.twitter.com/en/docs/direct-messages/welcome-messages/overview).

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |
| --- | --- |
| **event.custom\_profile\_id** | The string ID of the custom profile to attach to the Direct Message. |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

    {
      "event": {
        "type": "message_create",
        "message_create": {
          "target": {
            "recipient_id": "844385345234"
          },
          "message_data": {
            "text": "Hi, my name is Jon. How can I help?",
          },
          "custom_profile_id": "100001"
        }
      }
    }

### Example request using [Twurl](https://github.com/twitter/twurl)[¶](#example-request-using-twurl "Permalink to this headline")

    twurl -A 'Content-type: application/json' -X POST /1.1/direct_messages/events/new.json -d ' { "event": { "type": "message_create", "message_create": { "target": { "recipient_id": "844385345234" }, "message_data": { "text": "Hi, my name is Jon. How can I help?", }, "custom_profile_id": "100001" } } }'

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
      "event": {
        "type": "message_create",
        "message_create": {
          "target": {
            "recipient_id": "844385345234"
          },
          "sender_id": "1241124",
          "message_data": {
            "text": "Hi, my name is Jon. How can I help?",
          },
          "custom_profile_id":  "100001"
        }
      }
    }

DELETE custom\_profiles/destroy.json

delete-profile

DELETE custom\_profiles/destroy.json
====================================

Deletes a custom profile that was created with [POST custom\_profiles/new.json](https://developer.twitter.com/en/docs/direct-messages/custom-profiles/api-reference/new-profile).

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/custom_profiles/destroy.json`

Resource information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 24 hour window (user auth) | Yes (1000 / 1 day) |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |
| --- | --- |
| **id** (required) | The string ID of the custom profile to destroy. |

Example request using [Twurl](https://github.com/twitter/twurl)[¶](#example-request-using-twurl "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------

    twurl -X DELETE /1.1/custom_profiles/destroy.json?id=100001

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

Calling this multiple times on a valid id will return a 204 response code.

    HTTP 204 with empty body

GET custom\_profiles/:id

get-profile

GET custom\_profiles/:id
========================

Returns a custom profile that was created with [POST custom\_profiles/new.json](https://developer.twitter.com/en/docs/direct-messages/custom-profiles/api-reference/new-profile).

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/custom_profiles/:id.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 24 hour window (user auth) | Yes (180 / 15 min) |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |
| --- | --- |
| **id** (required) | The string ID of the custom profile that should be returned. Provided in resource URL. |

Example request using [Twurl](https://github.com/twitter/twurl)[¶](#example-request-using-twurl "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------

    twurl -X GET /1.1/custom_profiles/100001

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
      "custom_profile": {
        "id": "100001",
        "created_timestamp": "1479767168196",
        "name": "Jon C, Partner Engineer",
        "avatar": {
            "media": {
               "url": "https://pbs.twimg.com/media/Cr7HZpvVYAAYZIX.jpg"
           }
        }
    }

POST custom\_profiles/new.json

new-profile

POST custom\_profiles/new.json
==============================

Creates a new custom profile. The returned ID should be used with when publishing a new message with [POST direct\_messages/events/new](https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/api-reference/new-event).

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/custom_profiles/new.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 24 hour window (user auth) | Yes (1000 / 1 day) |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |
| --- | --- |
| **name** (required) | The string ID of of the custom profile. 48 characters max length. |
| **avatar.media.id** (required) | The string ID of the media to associate with the profile. See [Uploading Media](https://developer.twitter.com/en/docs/media/upload-media/overview) for further details on generating a media ID. |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

    {
      "custom_profile": {
        "name": "Jon C, Partner Engineer",
        "avatar": {
            "media": {
               "id": "1234"
           }
        }
    }

### Example request using [Twurl](https://github.com/twitter/twurl)[¶](#example-request-using-twurl "Permalink to this headline")

    twurl -A 'Content-type: application/json' /1.1/custom_profiles/new.json -d ' { "custom_profile": { "name": "Jon C, Partner Engineer", "avatar": { "media": { "id": "1234" } } }'

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
      "custom_profile": {
        "id": "100001",
        "created_timestamp": "1479767168196",
        "name": "Jon C, Partner Engineer",
        "avatar": {
            "media": {
               "url": "https://pbs.twimg.com/media/Cr7HZpvVYAAYZIX.jpg"
           }
        }
    }

GET custom\_profiles/list

get-profile-list

GET custom\_profiles/list
=========================

Retrieves all custom profiles for the authenticated account. Default page size is 20.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/custom_profiles/list.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 24 hour window (user auth) | Yes (180 / 15 min) |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |
| --- | --- |
| **count** (optional) | Number of custom profile objects to be returned. Max of 50. Default is 20. |
| **cursor** (optional) | For paging through result sets greater than 1 page. Use the `next_cursor` property returned from the previous request. |

_Note:_ In rare cases a response may contain an empty custom profile object with `next_cursor` defined. The presence of a `next_cursor` property in the response indicates there are more custom profiles to retrieve.

Example request using [Twurl](https://github.com/twitter/twurl)[¶](#example-request-using-twurl "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------

    twurl -X GET /1.1/custom_profiles/list.json?count=2&cursor=MTIzNDU2Nzg

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
      "custom_profiles": [
        {
          "id": "100001",
          "created_timestamp": "1479767168196",
          "name": "Carol",
          "avatar": {
            "media": {
              "url": "https://pbs.twimg.com/some_img/987654321/ABC?format=jpg&name=normal"
            }
          }
        },
        {
          "id": "100002",
          "created_timestamp": "1479767168197",
          "name": "Andy",
          "avatar": {
            "media": {
              "url": "https://pbs.twimg.com/some_img/56565656/DEF?format=jpg&name=normal"
            }
          }
        }
     ],
     "next_cursor": "NDUzNDUzNDY3Nzc3"
    }

Overview

Enterprise

Product & development guidance
------------------------------

Collecting structured feedback about customer interactions is a useful part of the customer service experience, providing quantitative measures of service quality and effectiveness that benefits both people and businesses. By asking for feedback in context and shortly after the interaction is complete, people are more likely to provide a response and more likely to provide feedback that reflects their interaction. This feature supports the programmatic creation and delivery of feedback prompts that allow someone to submit responses to feedback surveys after a conversation in Direct Messages.

* Feedback should ideally be built into your product so it can be kicked off automatically, not manually. The goal is to remove potential bias in results and to give a sense of trust to the user (for more honest feedback) that the agent who handled the interaction is not reading the results.
* Feedback results should be delivered to the business via your product. We've built our APIs with an assumption that you could create a dashboard or file download to provide reports to managers. Twitter is not planning to provide an interface for businesses to retrieve results directly from Twitter.
* Feedback results should ideally not be surfaced directly to an agent, and instead, be surfaced in supervisor reports or in an asynchronous way such that an agent doesn’t see the feedback and change their interaction demeanor or behavior.  
    
* Initially, Feedback can only be requested along with a Direct Message. Make sure to check the user object can\_dm to see if you have the ability to send Feedback before hitting the POST endpoint. (Particularly relevant if sending a Feedback prompt after a public interaction.)  
    
* A Direct Message must be sent before prompting a user for Feedback. When brands are considering the Direct Message text preceding the Feedback prompt, make sure it makes sense in the case that the Feedback experience does not render (web client, old clients, 3rd party clients, etc).
* Scores and text can be submitted independently and will likely have different timestamps. A score may be submitted without a text comment ever being completed. Both scores and text are immutable once submitted.
* Code should be tolerant of n ­number of updates per Feedback object. It should not assume a max of three possible updates. You should always rely on the most recent “updated\_at” timestamp.
* An empty next\_cursor value indicates you have reached the end of the result set. You should make no assumption about empty/partial page returned in "events" array as a signal that there is no more data to be fetched.

* * *

  
Access & authentication
--------------------------

Customer feedback cards only display to users in the iOS or Android Twitter apps. They do not display on twitter.com, mobile.twitter.com, TweekDeck, or 3rd-party Twitter apps, even if a feedback request is sent. 

Customer feedback cards are only available to Twitter enterprise data customers.

* Your client app ID and a @username must each be added to an allowlist to get app ­level access to the API.
* Authentication is 3-­legged OAuth currently used with the Twitter public API.
* We must additionally add the @username to an allowlist for any accounts you wish to send Feedback requests FROM (either your customer’s handles or your own if used for testing purposes).

GET feedback/show/:id.json

show

GET feedback/show/:id.json
==========================

Returns a single Feedback response for the specified ID in the URL.

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15 min window (user auth) | 180 |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |
| --- | --- |
| **feedback\_id** (required) | Required in path. |

Response Values[¶](#response-values "Permalink to this headline")
-----------------------------------------------------------------

|     |     |
| --- | --- |
| **score** | The user provided score response. 1­5 if type is CSAT. 0­10 if type is NPS. |
| **text** | The user provided text response. |

Example Result[¶](#example-result "Permalink to this headline")
---------------------------------------------------------------

    {
      "created_at": "SatDec1517:58:20+00002015",
      "updated_at": "SatDec1517:59:22+00002015",
      "id": "123456789"
      "text": "Thankyouforbeingaloyalcustomer!",
      "media_id_str": 12345,
      "response": {
        "score": {
          "created_at": "SatDec1518:59:22+00002015",
          "value": 1
        },
        "text": {
          "created_at": "SatDec1518:59:52+00002015",
          "value": "I<3thisbiz"
        }
      }
    }

Note

Response object will only be present if data is available.

GET feedback/events.json

events

GET feedback/events.json
========================

Returns Feedback creation and response events that occur in a specified time period. Please note that the max to\_time is 24 hours prior to the current time.

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15 min window (user auth) | 1,000 |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |
| --- | --- |
| **from\_time** (required) | Required on the 1st page. Epoch timestamp in milliseconds. Example: 1451936737470<br><br>The range is inclusive. |
| **to\_time** (required) | Required on the 1st page. Epoch timestamp in milliseconds. Example: 1451936737470<br><br>The range is inclusive. The max to\_time is 24 hours before current time. Requests for more recent data via this endpoint will receive an error. |
| **count** (required) | Max number of results returned. Default and max is 100. |
| **cursor** (optiona) | For paging through results. Required for paging through result sets greater than 1 page.<br><br>An empty value indicates you have reached the end of the result set. |

Response Values[¶](#response-values "Permalink to this headline")
-----------------------------------------------------------------

|     |     |
| --- | --- |
| **events** | An array of events. |
| **event\_type** | Possible values: feedback.created, feedback.updated |
| **next\_cursor** | Values are unique to a given from\_time/to\_time range. |

Example Result[¶](#example-result "Permalink to this headline")
---------------------------------------------------------------

    {
      "events":[
        {
          "event_type": "feedback.updated",
          "created_at": "SatDec1517:58:22+00002015",
          "feedback": {
            "created_at": "SatDec1517:58:20+00002015",
            "updated_at": "SatDec1517:59:22+00002015",
            "id": "123456789",
            ...
          }
        },
        {
          "event_type": "feedback.created",
          "created_at": "SatDec1517:59:22+00002015",
          "feedback":{
            "created_at": "SatDec1517:59:22+00002015",
            "updated_at": "SatDec1517:59:22+00002015",
            "id": "123456799",
            ...
          }
        }
      ],
      "next_cursor": "10011"
    }

POST feedback/create.json

create

POST feedback/create.json
=========================

Sends Feedback prompt along with a Direct Message (DM) to a specified user. The DM message is required. Sending Feedback inherits the Direct Message restrictions and behavior from [POST direct\_messages/events/new](https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/api-reference/new-event).

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 24 hour window (user auth) | 1,000 and 1 per recipient |

**Note**

Handles can be added to an allowlist to receive more than 1 new feedback request per 24 hours. Please send a list of @handles to your account manager.

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |
| --- | --- |
| **type** (required) | The Feedback type. Possible values: csat, nps (case sensitive) |
| **to\_user\_id** (required) | The ID of the user who should receive the Feedback prompt in a direct message. |
| **message** (required) | The Direct Message text used to introduce the Feedback prompt. |
| **privacy\_url** (required) | The URL to the sender’s hosted privacy policy. The sender is the business owner of the @username. |
| **external\_id** (optional) | An open field to track case IDs, conversation IDs, etc with a max length of 256 characters. |
| **question\_variant\_id** (optional) | The ID of the relative question variant text that will override the default text. See NPS Question Variants and CSAT Question Variants sections. Default value is 0 if not provided. |
| **display\_name** (optional) | Overrides the display name in the question text only (i.e. "How likely are you to recommend <display\_name> to a friend?" Max length of 20 characters.)<br><br>Confirmation messaging uses the default Twitter display name from the business’ profile. |
| **test** (optional) | Boolean value. Default is false. If true, we will exclude this feedback from analytics / aggregations.<br><br>This value should be used for any testing activity. |

Example Result[¶](#example-result "Permalink to this headline")
---------------------------------------------------------------

    {
      "created_at":"SatDec1517:58:20+00002015",
      "updated_at":"SatDec1517:59:22+00002015",
      "id":"123456789",
      "type":"nps",
      "test":false,
      "dm_id":"8989898989",
      "from_user_id":"1212121212121",
      "to_user_id":"343434343434",
      "privacy_url":"https://my­business.domain/privacy",
      "external_id":"ticket_5555",
      "question_variant_id":"3",
      "display_name":"MyBusinessName"
    }

NPS Question Variants[¶](#nps-question-variants "Permalink to this headline")
-----------------------------------------------------------------------------

| ID  | Text |
| --- | --- |
| 0   | What is your overall satisfaction with <display\_name>? |
| 1   | How satisfied are you with <display\_name>? |
| 2   | Overall, how satisfied were you with your recent <display\_name> experience? |
| 3   | How would you rate the overall experience with <display\_name>? |
| 4   | How would you rate your overall experience with <display\_name>? |
| 5   | How would you rate your experience so far with <display\_name>? |

CSAT Question Variants[¶](#csat-question-variants "Permalink to this headline")
-------------------------------------------------------------------------------

| ID  | Text |
| --- | --- |
| 0   | What is your overall satisfaction with <display\_name>? |
| 1   | How satisfied are you with <display\_name>? |
| 2   | Overall, how satisfied were you with your recent <display\_name> experience? |
| 3   | How would you rate the overall experience with <display\_name>? |
| 4   | How would you rate your overall experience with <display\_name>? |
| 5   | How would you rate your experience so far with <display\_name>? |
| 6   | How would you rate your experience on Twitter with <display\_name>? |
| 7   | Were you satisfied with your recent experience with <display\_name>? |
| 8   | How well does <display\_name> meet your expectations? |
| 9   | How would you rate your guest experience with <display\_name>? |
| 10  | How would you rate your service experience with <display\_name>? |
| 11  | How would you rate your recent service experience with <display\_name>? |
| 12  | How would you rate the service you received from <display\_name>? |
| 13  | Were you satisfied with the result of your interaction with <display\_name>? |
| 14  | How would you rate the ability to resolve your issue with <display\_name>? |
| 15  | How would you rate the response time from <display\_name>? |
| 16  | How would you rate the speed of service from <display\_name>? |
| 17  | How would you rate the time to resolution with <display\_name>? |
| 18  | How would you rate the time to resolve your issue with <display\_name>? |
| 19  | How would you rate the speed of resolution with <display\_name>? |
| 20  | How would you rate the <display\_name> advisor's expertise? |
| 21  | How satisfied were you with the <display\_name> agent who helped you? |
| 22  | How satisfied were you with the <display\_name> specialist who helped you? |
| 23  | How satisfied were you with the <display\_name> representative who helped you? |
| 24  | How would you rate your recent banking experience with <display\_name>? |
| 25  | How would you rate the overall event experience at <display\_name>? |
| 26  | How would you rate your bill pay experience with <display\_name>? |
| 27  | How would you rate your purchase experience with <display\_name>? |
| 28  | How would you rate your shopping experience with <display\_name>? |
| 29  | How would you rate your delivery experience with <display\_name>? |
| 30  | How would you rate your rental experience with <display\_name>? |
| 31  | How would you rate your recent <display\_name> store visit? |
| 32  | How would you rate your recent <display\_name> hotel stay? |
| 33  | How would you rate your recent flight with <display\_name>? |
| 34  | How would you rate your recent ride with <display\_name>? |
| 35  | How would you rate your recent trip with <display\_name>? |
| 36  | How would you rate your recent visit to <display\_name>? |
| 37  | How would you rate your recent meal at <display\_name>? |