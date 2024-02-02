
Direct Message migration guide | Docs | Twitter Developer Platform 

Direct Message migration guide

Direct Message migration guide
------------------------------

**On September 17th, 2018 we retired the legacy Direct Message endpoints.  
If you had been using those endpoints, please make sure to migrate over to the new Direct Message endpoints or the Account Activity API.**

**Please review this announcment to learn more.**

This guide is designed to help you migrate from legacy Direct Message REST APIs to their enhanced replacements which have graduated from beta. Below you will find a summary of the changes, a new features list, and key differences and considerations to help with the transition. The new Direct Message endpoints are available now to all developers. For guidance in migrating from User Streams or Site Streams, see the migration guide to Account Activity API.

* Summary of changes
* New features
* Sending Direct Messages
* Receiving Direct Messages
* Deleting Direct Messages

### Summary of changes

If you are still using the following DM endpoints, you will have to migrate to the newer endpoints. 

| Deprecated endpoint | New migration alternative |
| --- | --- |
| POST direct\_messages/new | POST direct\_messages/events/new |
| GET direct\_messages/show | GET direct\_messages/events/show |
| GET direct\_messages | GET direct\_messages/events/list |
| GET direct\_messages/sent | GET direct\_messages/events/list |
| POST direct\_messages/destroy | DELETE direct\_messages/events/destroy |

### New features

The new Direct Message API endpoints support a number of new capabilities and provide improved access to previous Direct Messages. New features include:

* Support for media attachments (image, GIF, and video).
* Ability to prompt users for structured replies with a predefined options list.
* Up to 30 days of access to past Direct Messages.

For a full list of new Direct Message features and additional new API endpoints refer to the technical documentation.  

### Differences & migration considerations

The new API endpoints behave very differently from their previous counterparts. Simply updating the endpoint URLs will result in errors in your application. Consider the following when updating your application for the migration.

#### New Direct Message object

The first thing you are likely to notice is the new object structure of Direct Messages. This new Message Create object structure has been introduced to support new capabilities like Quick Replies and Attachments. The new object also contains a smaller condensed user object. Your application will need to be updated to account for this new object structure when parsing and potentially in data models or storage. For descriptions of each property see the full documentation on the Message Create Object.  

**Example message create object**  

```
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
```

#### Summary

* Entirely new Direct Message object structure.
* Condensed user object.
* New information provided (quick reply responses, attachments, etc).

### Sending Direct Messages

POST direct\_messages/events/new is a direct replacement for sending Direct Messages. The most significant difference with this endpoint is that all information is now sent as JSON in the POST request body as opposed to individual POST params.

**Example Twurl request**  

```
twurl -A 'Content-type: application/json' -X POST /1.1/direct_messages/events/new.json -d '{"event": {"type": "message_create", "message_create": {"target": {"recipient_id": "4534871"}, "message_data": {"text": "Hello World!"}}}}'
```

Note in the above request that the content-type is set to application/json as opposed to application/x-www-form-urlencoded. Additionally, if you are constructing the OAuth 1.0a signature, note that the JSON body is not included in the generation of the signature. Most OAuth libraries already account for this. If you are using twurl, ensure you are using at least version 0.9.3.  

#### Summary

* Message is defined in JSON POST body
* Content-type header must be set to application/json
* JSON body is not included in the generation of the OAuth signature.

### Retrieving Direct Messages

Retrieving past Direct Message is now accomplished with a single API endpoint: GET direct\_messages/events/list. The significant difference with this new endpoint is that it now returns both sent and received messages in reverse chronological order. This may make it easier to rebuild a conversation. However, if you are only looking for sent or received messages you will need to post-process the response by referring to the sender\_id property.

Pagination is now based on a cursor value rather an ID of a Direct Message. A cursor property is returned with each response. GET direct\_messages/events/list will return up to 30 days of past messages, regardless of how many messages exist within the past 30 days. When a cursor is not returned, there are no more messages to be returned. The method for accessing individual Direct Messages with GET direct\_messages/events/show remains the same, although the Direct Message object returned has a different structure as described previously.

Finally, real-time access to Direct Messages will now be accomplished via webhook with the Account Activity API. For guidance in migrating from User Streams or Site Streams, see the migration guide to Account Activity API for more information.

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

**Questions about migrating to the new Direct Message endpoints?**Post your question to the developer community forum on twittercommunity.com.

Next Steps
----------

* Download our Direct Message Migration Guide (below)

Direct Messages
Direct Message - Migration Guide
--------------------------------

Download PDF

Developer policy and terms

Follow @XDevelopers

Subscribe to developer news

#### 
 X platform

* X.com
* Status
* Accessibility
* Embed a post
* Privacy Center
* Transparency Center
* Download the X app

#### 
 X Corp.

* About the company
* Company news
* Brand toolkit
* Jobs and internships
* Investors

#### 
 Help

* Help Center
* Using X
* X for creators
* Ads Help Center
* Managing your account
* Email Preference Center
* Rules and policies
* Contact us

#### 
 Developer resources

* Developer home
* Documentation
* Forums
* Communities
* Developer blog
* Engineering blog
* Developer terms

#### 
 Business resources

* Advertise
* X for business
* Resources and guides
* X for marketers
* Marketing insights
* Brand inspiration
* X Ads Academy

 © 2024 X Corp.

Cookies

Privacy

Terms and conditions

**Did someone say … cookies?**  

 X and its partners use cookies to provide you with a better, safer and
 faster service and to support our business. Some cookies are necessary to use
 our services, improve our services, and make sure they work properly.
 Show more about your choices.

* Accept all cookies
* Refuse non-essential cookies