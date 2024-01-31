Introduction

Introduction
------------

Direct Messages enable private conversations on Twitter. Direct Messages are one of the most popular features of Twitter, with a wide variety of use cases. These use cases range from group chats among friends to powering customer support for brands around the world. New v2 versions of Direct Messages endpoints will be introduced in stages, and this first stage includes fundamental endpoints for creating Direct Messages and listing Direct Message conversation events. For the first time, the Twitter API v2 supports _group_ conversations.

This initial release of Direct Messages lookup includes three GET methods:

* **GET /2/dm\_conversations/with/:participant\_id/dm\_events** \- Retrieves Direct Message events associated with a one-to-one conversation. The :participant\_id path parameter is the User ID of the account having the conversation with the authenticated user making this request. 
* **GET /2/dm\_conversations/:dm\_conversation\_id/dm\_events** - Retrieves Direct Message events associated with a specific conversation ID, as indicated by the :dm\_conversation\_id path parameter. 
* **GET /2/dm\_events** - Retrieves Direct Message events associated with a user, including both one-to-one and group conversations. Events from up to 30 days ago are available.  

Note that Direct Message event IDs are common across the v1.1 and v2 (as well as the Twitter App), so the v1.1 method to list a single event can be used along with these new v2 endpoints. Also note that the Enterprise and Premium Account Activity APIs support v2 one-to-one messages, but do not yet support group conversations.   

With this release, three event types are supported, and these endpoints support query parameters to filter on them:

* **MessageCreate** - A message has been created. 
* **ParticipantsJoin** - A new participant has joined a conversation. 
* **ParticipantsLeave** - A participant has left a conversation. 

There is a user rate limit of 300 requests per 15 minutes for the GET methods. This rate limit is shared across these GET endpoints.

Since you are making requests on behalf of a user with Direct Message v2 endpoints, you must authenticate with either [OAuth 1.0a User Context](https://developer-staging.twitter.com/en/docs/authentication/oauth-1-0a) or [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code), using Access Tokens associated with users that have authorized your Twitter App. To generate these Access Tokens with OAuth 1.0a, you can use the [3-legged OAuth flow](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens). To generate user Access Tokens with OAuth 2.0, you can use the [Authorization Code with PKCE grant flow](https://developer.twitter.com/en/docs/authentication/oauth-2-0/user-access-token).

**Account setup**

To access these endpoints, you will need:

* An approved [developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info).
* To authenticate using the keys and tokens from a [developer App](https://developer.twitter.com/en/docs/apps) that is located within a [Project](https://developer.twitter.com/en/docs/projects). 

Learn more about getting access to the Twitter API v2 endpoints in our [getting started guide](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api).

[Quick start](https://developer.twitter.com/en/docs/twitter-api/direct-messages/lookup/quick-start)

[Sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code)

[Run in Postman](https://t.co/twitter-api-postman)

[Try with API Explorer](https://developer.twitter.com/apitools/api?endpoint=/2/tweets&method=get)

Supporting resources
--------------------

[Learn how to use Postman to make requests](https://developer.twitter.com/en/docs/tutorials/postman-getting-started "Learn how to use Postman to make requests")

[Troubleshoot an error](https://developer.twitter.com/en/support/twitter-api "Troubleshoot an error")

[Visit the API reference page for this endpoint](https://developer.twitter.com/en/docs/twitter-api/direct-messages/lookup/api-reference "Visit the API reference page for this endpoint")

Relevant tutorials
------------------

[Measure Tweet performance](https://developer.twitter.com/en/docs/tutorials/measure-tweet-performance "Measure Tweet performance")

Quick start

Getting started with the manage Direct Message endpoints
--------------------------------------------------------

This quick start guide will help you make your first request to the Direct Message endpoints using Postman, a tool for managing and making HTTP requests. To learn more about our Postman collections, please visit our [Using Postman](https://developer.twitter.com/en/docs/tools-and-libraries/using-postman) guide.

Please visit our [Twitter API v2 sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code) GitHub repository if you want to review Python-based examples. In addition, the official [Twitter Developer Platform software development kits (SDKs)](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview) will be updated to support these Direct Message endpoints.  

### Prerequisites

To complete this guide, you will need to have a set of [keys and tokens](https://developer.twitter.com/en/docs/authentication) to authenticate your request. You can generate these keys and tokens by following these steps:

* [Sign up for a developer account](https://developer.twitter.com/en/apply-for-access) and receive approval.
* Create a [Project](https://developer.twitter.com/en/docs/projects) and an associated [developer App](https://developer.twitter.com/en/docs/apps) in the developer portal.
* Navigate to your App's “Keys and tokens” page to generate the required credentials. Make sure to save all credentials in a secure location.

### Steps to building Direct Message lookup requests

In this example, in one request, we'll create a new group conversation and add our first message to it. We'll then add a second message to the created conversation.

#### Step one: Start with a tool or library

To begin working with the manage Direct Message endpoints we are going to use the Postman tool to simplify the process. A TwitterDev-authored collection of example Twitter API v2 requests will be used to explore six endpoints used to create new Direct Messages and to list Direct Message conversation events.

While most of the collection is pre-filled, there are a few details that you'll need to provide that are based on the Twitter App created to host these API requests. First, let's get the collection loaded/updated.

To load Twitter API v2 Postman collection into your environment, please click on the following button:

[Add Twitter API v2 to Postman](https://t.co/twitter-api-postman)

  
  
Once you have the Twitter API v2 collection loaded in Postman, navigate to the “Manage Direct Messages” folder. This folder's Authorization tab has been pre-filled where possible. You will need to update a few settings to share your Twitter App's authentication details.

This folder also contains three endpoints for creating new Direct Messages. Note that there is also a "Direct Message lookup" folder with three available endpoints for retrieving Direct Message conversation events, including sending and receiving messages, and when conversation participants join and leave.

Since creating group conversations is a new feature of the Twitter API v2, this example will focus on that. We will be working with the "New group DM and conversation" example. We will use this request to create a Direct Message group conversation.

The next step is to authenticate with the endpoint.

####   
Step two: Authenticate your request

To properly make a request to the Twitter API, you need to verify that you have permission to do so. To make a successful request to this endpoint, we will be using [OAuth 2.0 Authorization Code Flow with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code). You can generate an access token within Postman. 

With Postman you can set the authentication method at the folder level or at the request level. Here we will be configuring the authentication details at the folder level. Navigate to the "Mange Direct Messages" folder, select the "Authorization" tab and confirm that the Type to set to “OAuth 2.0”, and "Add auth data to" is set to "Request Headers." In the "Current Token" section, make sure the "header Prefix" is set to Bearer.  

To configure and generate a new token:

1. Create a Token Name, such as "DM lookup."
    
2. Confirm that **Grant Type** is set to Authorization Code (with PKCE).
    
3. Set your **Callback URL**. You will want to update your Callback URL to exactly match the Callback URL associated with your application in the [v2 Dev Portal](https://developer.twitter.com/en/portal/dashboard). With the Twitter App used with this example, the Callback URL is set to - [https://www.example.com.](https://www.example.com/) (Note that since this must match exactly, [https://example.com](https://example.com/) would not work.) 
    
4. Confirm that **Auth URL** is set to [https://twitter.com/i/oauth2/authorize](https://twitter.com/i/oauth2/authorize)
    
5. Confirm that **Access Token URL** is set to [https://api.twitter.com/2/oauth2/token.](https://api.twitter.com/2/oauth2/token)**Client ID** \- Copy and paste OAuth 2.0 client ID from the Developer Portal  
    **Client Secret** - You will need this only if you are using an App type that is a confidential client. If so, copy and paste the OAuth 2.0 Client Secret from the Developer Portal. 
    
6. Confirm that **Scope** is set to dm.read dm.write tweet.read users.read.
    
7. Confirm that **State** is set to “state.”
    
8. Confirm that **Client Authentication** is set to Send as Basic Auth header.
    
9. Click where it says “Get New Access Token”, click "Authorize app" as part of the "Sign-in with Twitter" process.
    
10. Click the "Proceed" button and then the "Use Token" to generate a token. 
    
11. Click on the "Save" button to save these configuration details.
    

You may get a message that you are not logged into Twitter. If you get this error, you will need to log in to the Twitter account that you are trying to post on behalf of inside of Postman.

Now that these OAuth 2.0 details have been set at the folder level, navigate to each of the examples and their "Authorization" tab and confirm that they have their Type set to "Inherit auth from parent." 

Note that this token will expire soon, and you'll need to regenerate it by clicking on the "Get New Access Token" button. Clicking that will trigger the "Sign-in with Twitter" process and generate a fresh token to make requests with.

#### Step three: Retrieve Direct Messages conversation events

When retrieving Direct Message conversation events with this endpoint, you need to specify a conversation ID. The conversation ID is part of the endpoint path: https://api.twitter.com/2/dm\_conversations/:dm\_conversation\_id/dm\_events

In Postman, navigate to the “Params” tab and enter the ID of the conversation you want to retrieve events for in the "Path Variables" section.

The setting would be:

|     |     |
| --- | --- |
| **Key** | **Value** |
| `dm_conversation_id` | `1228393702244134912` |

With this conversation specified, the resulting path becomes https://api.twitter.com/2/dm\_conversations/1582103724607971328/dm\_events

If you click the "Send" button you will receive the default Direct Message object fields in your response: id,  text, and event\_type. There will also be a "meta" object with the number of results, along with pagination tokens used for retrieving more events if available.

      `{    "data": [        {            "event_type": "MessageCreate",            "id": "1580705921830768647",            "text": "hello to you two, this is a new group conversation."        }    ],    "meta": {        "result_count": 1,        "next_token": "18LAA5FFPEKJA52G0G00ZZZZ",        "previous_token": "1BLC45FFPEKJA52G0S00ZZZZ"    } }`
    

If you would like to receive additional fields, you will have to specify those fields in your request with the [field](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/fields) and/or [expansion](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/expansions) parameters.

For this exercise, we will request additional sets of fields of the dm\_event object:  

1. The default Direct Message object fields, id, text, and event\_type.
    
2. Additional Direct Message object fields: dm\_conversation\_id, created\_at, sender\_id, attachments, participant\_ids, referenced\_tweets
    

In Postman, navigate to the "Params" tab and add the following key:value pair to the "Query Params" table:

|     |     |
| --- | --- |
| Key | Value |
| dm\_event.fields | dm\_conversation\_id,created\_at,sender\_id,attachments,participant\_ids,referenced\_tweets |

|     |     |     |
| --- | --- | --- |
|     |     |     |
|     |     |     |

You should now see the following URL next to the "Send" button:

https://api.twitter.com/2/dm\_conversations/:dm\_conversation\_id/dm\_events?dm\_event.fields=id,text,event\_type,dm\_conversation\_id,created\_at,sender\_id,attachments,participant\_ids,referenced\_tweets

#### Step four: Make your request and review your response

Once you have everything set up, hit the "Send" button again, and you will receive a response similar to the below response. Note that this response includes all the available dm\_event fields.

      `{    "data": [        {            "text": "hello to you two, this is a new group conversation.",            "id": "1580705921830768647",            "dm_conversation_id": "1580705921830768643",            "event_type": "MessageCreate",            "sender_id": "17200003",            "created_at": "2022-10-13T23:43:54.000Z"        }    ],    "meta": {        "result_count": 1,        "next_token": "18LAA5FFPEKJA52G0G00ZZZZ",        "previous_token": "1BLC45FFPEKJA52G0S00ZZZZ"    } }`
    

Next steps
----------

[API Reference](https://developer.twitter.com/en/docs/twitter-api/direct-messages/lookup/api-reference "API Reference")

[Get support](https://developer.twitter.com/en/support/twitter-api "Get support")

[Sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code "Sample code")

Integrate

Integration guide
-----------------

The Direct Messages endpoints v2 introduce conversations and conversation events as core Twitter API objects, and make a distinction between 1-1 and group conversations. 1-1 conversations always have two, and only two, participants, while group conversations can have two or more and memberships that can change.   

This page contains information on several tools and key concepts that you should be aware of as you integrate the Direct Messages lookup endpoints into your system. We’ve broken the page into two sections:

* Key Concepts
    * [Direct Message conversations](#direct-message-conversations)
    * [Shared conversation and event IDs across v1.1 and v2](#shared-conversation-and-event-ids)
    * [Direct Message event fields and expansions](#direct-message-event-fields-and-expansions)
    * [Conversation event types](#conversation-event-types)
    * [Authentication](#authentication)
    * [Developer portal, Projects, and Apps](#developer-portal-projects-and-apps)
    * [Rate limits](#rate-limits)
    * [Pagination](#pagination)
* [Helpful tools](#helpful-tools)

### Key Concepts

### Direct Message conversations

All Direct Messages are part of a Direct Message conversation. These conversations can be one-to-one conversations or group conversations. This launch provides the foundational endpoints needed to create Direct Messages and retrieve events associated with Direct Message conversations. All conversations have a unique dm\_conversation\_id, and the events that make up that conversation all have a unique dm\_event\_id.  

The Direct Message lookup endpoints provide methods for retrieving events associated with conversations. These GET endpoints are used to retrieve the messages that make up a conversation, and for group conversations, can be used to understand who has joined and left group conversations.  

This initial release of Direct Messages lookup includes three GET methods:

* **GET /2/dm\_conversations/with/:participant\_id/dm\_events** - Retrieves Direct Message events associated with a one-to-one conversation. The :participant\_id path parameter is the numeric User ID of the account having the conversation with the authenticated user making this request.  
    
* **GET /2/dm\_conversations/:dm\_conversation\_id/dm\_events** - Retrieves Direct Message events associated with a specific conversation ID, as indicated by the :dm\_conversation\_id path parameter. Both one-to-one and group conversations IDs are supported.  
    
* **GET /2/dm\_events** - Retrieves Direct Message events associated with the authenticating user, including both one-to-one and group conversations. Events from up to 30 days ago are available.  
    

These GET endpoints all support retrieving dm\_events by event type with an event\_types request query parameters. Currently, there are three conversation event types supported:  

* **MessageCreate** - Created when a new Direct Message is created. This event object can include the time and text of the message, along with the account ID of who sent the message, and the conversation and event IDs. 
    
* **ParticipantsJoin** - Created when a new participant joins a group conversation. This dm\_event object includes the ID of the participant joining, along with the created\_at time and the sender\_id of the 'invite' event. 
    
* **ParticipantsLeave** - Created when a participant leaves a conversation.This event object includes the ID of the participant leaving, along with the time of the event. 
    

For more information see the [Direct Messages lookup API References](https://developer.twitter.com/en/docs/twitter-api/direct-messages/lookup/api-reference).

### Shared conversation and event IDs across v1.1 and v2

An important concept is that conversation and event IDs are shared across v1.1 and v2 versions of the Twitter Platform. This means both versions can be used together. For example, the Direct Messages v1.1 endpoints provide methods for returning a single event and for deleting events, methods not yet available with v2. Since IDs are common across v1.1 and v2, you can make v1.1 requests based on IDs provided by v2, or by referencing conversation IDs displayed in conversation URLs on the Twitter application.  

### Direct Message event fields and expansions

The Twitter API v2 allows users to select exactly which data they want to return from the API using a set of tools called fields and expansions. For example, Direct Message lookup endpoints support the following dm\_events fields: 

* id, event\_type, and text are the defaults for MessageCreate events. 
    
* id, event\_type, and participant\_ids are the defaults for ParticipantsJoin and ParticipantsLeave events.
    
* dm\_conversation\_id and created\_at are available for all events.
    
* attachments and referenced\_tweets are available for MessageCreate events. 
    
* sender\_id is available for MessageCreate and ParticipantsJoin events. 
    
* participant\_ids is available for ParticipantsJoin and ParticipantsLeave events. 
    

In addition, the Direct Message lookup endpoints support the following [expansions](https://developer.twitter.com/en/docs/twitter-api/expansions):  

* sender\_id - Expands the User object associated with who sent the message or who invited someone to the conversation. 
    
* referenced\_tweets.id - Expands the Tweet object if the Direct Message text includes a link to a Tweet. 
    
* attachments.media\_keys - Expands the Media object if the Direct Message includes a media attachment. 
    
* participant\_ids - Expands the User object associated with who joined or left a group conversation.
    

Since expansion include Tweets, Users, and Media objects, you can also use the tweet.fields, user.fields, and media.fields request query parameters. See our guide on how to [use fields and expansions](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/using-fields-and-expansions) for more information.  

### Conversation event types

Below are example JSON objects for Direct Message the MessageCreate, ParticipantsJoin, and ParticipantsLeave event types.   

Available dm\_event object fields: id, text, event\_type, dm\_conversation\_id, created\_at, sender\_id, attachments, referenced\_tweets, participant\_ids. See the the Fields and Expansion section for more details on selecting these fields in your requests.   

Example MessageCreate event: 

With all the dm\_event fields specified, here is the response for a simple text Direct Message: 

      `{     "text": "Hi everyone.",     "sender_id": "944480690",     "dm_conversation_id": "1578398451921985538",     "id": "1582838499983564806",     "event_type": "MessageCreate",     "created_at": "2022-10-19T20:58:00.000Z" }`
    

Example ParticipantsJoin event:

With all the dm\_event fields specified, here is the response for a participant joining a conversation:

      `{     "participant_ids": [         "944480690"     ],     "sender_id": "17200003",     "dm_conversation_id": "1578398451921985538",     "id": "1582835469712138240",     "event_type": "ParticipantsJoin",     "created_at": "2022-10-19T20:45:58.000Z" }`
    

Example ParticipantsLeave event:

With all the dm\_event fields specified, here is the response for a participant leaving a conversation:

      `{     "participant_ids": [         "944480690"     ],     "dm_conversation_id": "1578398451921985538",     "id": "1582838535115067392",     "event_type": "ParticipantsLeave",     "created_at": "2022-10-19T20:58:09.000Z"     }`
    

### Authentication

All Twitter API v2 endpoints require for you to authenticate your requests with a set of credentials, also known as keys and tokens. All Direct Messages are private and require user authorization to access them. 

These Direct Message endpoints require the use of [OAuth 2.0 Authorization Flow with PKCE](https://developer.twitter.com/en/docs/twitter-api/tweets/manage-tweets/integrate#authentication) or [1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a), which means that you must use a set of API keys and user Access Tokens to make a successful request. The Access Tokens must be associated with the user that you are requesting on behalf of. If you want to generate a set of Access Tokens for another user, they must authorize or authenticate your App using the [3-legged OAuth flow](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens).

Please note that OAuth user-context can be tricky to use. If you are not familiar with this authentication method, we recommend using a [library](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries) or a tool like Postman to properly authenticate your requests. 

[OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code) allows for greater control over an application’s scope, and authorization flows across multiple devices. OAuth 2.0 allows you to pick specific fine-grained scopes which give you specific permissions on behalf of a user. The Direct Messages lookup endpoints require these scopes:  dm.read, tweet.read, user.read

To enable OAuth 2.0 in your App, you must enable it in your’s App’s authentication settings found in the App settings section of the developer portal.

### Developer portal, Projects, and developer Apps

To retrieve a set of authentication credentials that will work with the Twitter API v2 endpoints, you must have an approved developer account, set up a Project within that account, and create a developer App within that Project. You can then find your keys and tokens within your developer App. 

### Rate limits

Everyday many thousands of developers make requests to the Twitter API. To help manage the sheer volume of these requests, rate limits are placed on each endpoint that limits the number of requests that you can make on behalf of your app or on behalf of an authenticated user. 

The Direct Message lookup endpoints are rate limited at the user-level, meaning that the authenticated user that you are making the request on behalf of can only make a certain number of requests with your Twitter App. There is a user rate limit of 300 requests per 15 minutes for the GET methods. These rate limits are shared across the GET endpoints.   

### Pagination

These endpoints utilize pagination so that responses are returned quickly. In cases where there are more results than what can be sent in a single response (up to 100 events) you will need to paginate. Use the max\_results parameter to identify how many results will return per page, and the pagination\_token parameter to return the next page of results. You can learn more by reviewing our [pagination guide](https://developer.twitter.com/en/docs/twitter-api/pagination).  

Helpful tools
-------------

Here are some helpful tools we encourage you to explore as you work with the Direct Messages lookup endpoints: 

****Postman**  
**

Postman is a great tool that you can use to test out an endpoint. Each Postman request includes every path and body parameter to help you quickly understand what is available to you. To learn more about our Postman collections, please visit our [Using Postman](https://developer.twitter.com/en/docs/tutorials/postman-getting-started) page. 

****Code samples**  
**

Python sample code for the v2 Direct Messages endpoints is available in our Twitter API v2 sample code GitHub repository. The "Manage-Direct-Messages" folder contains examples for the POST methods, and the "Direct-Messages-lookup" folder contains examples for the GET methods.

****TwitterDev Software Development Kits (SDKs)**  
**

These [libraries](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview) are being updated for the v2 Direct Messages endpoints and should be ready soon:  

* [Twitter API Java SDK](https://github.com/twitterdev/twitter-api-java-sdk) - Official Java SDK for the Twitter API v2
* [Twitter API TypeScript/JavaScript SDK](https://github.com/twitterdev/twitter-api-typescript-sdk) - Official TS/JS SDK for the Twitter API v2

**Third-party libraries**  

There is a growing number of [third-party libraries](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/v2#community-libraries) developed by our community. These libraries are designed to help you get started, and several are expected to support v2 Direct Messages endpoints soon. You can find a library that works with the v2 endpoints by looking for the proper version tag.

Next steps
----------

[Visit the API reference page for this endpoint](https://developer.twitter.com/en/docs/twitter-api/direct-messages/lookup/api-reference "Visit the API reference page for this endpoint")

Standard v1.1 compared to Twitter API v2

Comparing v1.1 and v2 Direct Message event lookup endpoints
-----------------------------------------------------------

Both v1.1 and v2 versions of the Direct Messages endpoints provide methods for looking up Direct Message events. This guide is intended to help understand the differences and provide information for migrating to v2. 

A major difference between the two versions is that v1.1 supports only one-to-one conversations, while v2 introduces support for group conversations. One artifact of this is that v1.1 supports only "message created" events, while v2 also supports events associated with participants joining and leaving conversations. In fact, a fundamental v2 update is establishing dm\_conversations as a core API object.     

With v1.1. there are two endpoints for retrieving Direct Messages (again, new messages are the only event type supported with v1.1):  

* [GET direct\_messages/events/show](https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/sending-and-receiving/api-reference/get-event) - Retrieves a single event by ID. 
    
* [GET direct\_messages/events/list](https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/sending-and-receiving/api-reference/list-events) - Retrieves up to 30 days of one-to-one Direct Messages sent and received by the authenticated user. Note that this method is not able to retrieve messages from group conversations. 
    

With this v2 release, there are three GET methods for retrieving Direct Message conversation events:   

* **GET /2/dm\_conversations/with/:participant\_id/dm\_events** - Retrieves Direct Message events associated with a one-to-one conversation. The :participant\_id path parameter is the User ID of the account having the conversation with the authenticated user making this request. 
    
* **GET /2/dm\_conversations/:dm\_conversation\_id/dm\_events** - Retrieves Direct Message events associated with a specific conversation ID, as indicated by the :dm\_conversation\_id path parameter. This method supports both one-to-one and group conversations. 
    
* **GET /2/dm\_events** - Retrieves Direct Message events associated with a user, including both one-to-one and group conversations. Events from up to 30 days ago are available.  
    

An important detail is that conversation and event IDs are shared across v1.1 and v2 versions of the Twitter Platform. This means both versions can be used together. For example, the Direct Messages v1.1 endpoints provide methods for returning a single event and for deleting events, methods not yet available with v2. Since IDs are common across v1.1 and v2, you can make v1.1 requests based on IDs provided by v2, or by referencing conversation IDs displayed in conversation URLs on the Twitter application.

The following table compares fundamental aspects of the v1.1 and v2 Direct Message event lookup endpoints. The Twitter API v2 characteristics shared here are common to all of the Direct Message lookup endpoints.

|     |     |     |
| --- | --- | --- |
| **Description** | **Standard v1.1** | **Twitter API v2** |
| Host domain | https://api.twitter.com | https://api.twitter.com |
| Endpoint root path | [/1.1/direct\_messages](https://api.twitter.com/1.1/direct_messages) | [/2/dm\_conversations](https://api.twitter.com/2/users/:id/dm_conversations)<br><br>Direct Messages conversations are introduced as a fundamental API object.   <br><br>These endpoints retrieve MessageCreate, ParticipantsJoin, and ParticipantLeave events. |
| HTTP methods supported | GET | GET |
| Supports Group Direct Messages |     | ✔   |
| Event types supported | message\_create | MessageCreate, ParticipantsJoin, ParticipantsLeave |
| [Authentication](https://developer.twitter.com/en/docs/authentication) | OAuth 1.0a User Context | OAuth 1.0a User Context<br><br>OAuth 2 User Context (scopes: dm.read, tweet.read, user.read) |
| Requires the use of credentials from a [developer App](https://developer.twitter.com/en/docs/authentication) associated with a Twitter API v2 [Project](https://developer.twitter.com/en/docs/projects) |     | ✔   |
| Default request [rate limits](https://developer.twitter.com/en/docs/twitter-api/rate-limits)\*  <br>\*All requests require user tokens |     | GET requests: 300 requests per 15 mins<br><br>Rate limit is applied across all three endpoints |

The following tables compare the v2 GET methods with version v1.1. Note that these v2 offerings expand the available capabilities by supporting group conversations. 

**Get all messages in a specific one-to-one conversation**   

--------------------------------------------------------------

Path: GET /2/dm\_conversations/with/:participant\_id/dm\_events

|     |     |     |
| --- | --- | --- |
| **Description** | **Standard v1.1** | **Twitter API v2** |
| Endpoint path | GET <br><br>/1.1/direct\_messages/events/list | GET /2/dm\_conversations/with/:participant\_id/dm\_events |
| How much event history is available | 30 days | No limit |
| Default request [rate limits](https://developer.twitter.com/en/docs/twitter-api/rate-limits) | 15 requests per 15 minutes | 300 requests per 15 minutes  <br>Rate limit is applied across all three GET endpoints |

**Get all messages by conversation ID**   

Path: GET /2/dm\_conversations/:dm\_conversation\_id/dm\_events

|     |     |     |
| --- | --- | --- |
| **Description** | **Standard v1.1** | **Twitter API v2** |
| Endpoint path | Not supported. V1.1 can return messages from one-to-one conversations only and there is no support for retrieving events by conversation IDs. | GET /2/dm\_conversations/:dm\_conversation\_id/dm\_events |
| How much event history is available | 30 days | No limit |
| Supports group conversations |     | ✔   |
| Default request [rate limits](https://developer.twitter.com/en/docs/twitter-api/rate-limits) | 15 requests per 15 minutes | 300 requests per 15 minutes  <br>Rate limit is applied across all three GET endpoints |
|     |     |

**Get all events across an authenticated user's conversations, both one-to-one and group conversations**  

Path: GET /2/dm\_events

|     |     |     |
| --- | --- | --- |
| **Description** | **Standard v1.1** | **Twitter API v2** |
| Endpoint path | GET /1.1/direct\_messages/events/list  <br>  <br>V1.1 can return messages from one-to-one conversations only. | GET /2/dm\_events |
| How much event history is available | 30 days | 30 days |
| Supports group conversations |     | ✔   |
| Default request [rate limits](https://developer.twitter.com/en/docs/twitter-api/rate-limits) | 15 requests per 15 minutes | 300 requests per 15 minutes  <br>Rate limit is applied across all three GET endpoints |
|     |     |

Next steps
----------

[Quick start guide](https://developer.twitter.com/en/docs-vnext/twitter-api/tweets/lookup/quick-start "Quick start guide")

[API reference](https://developer.twitter.com/en/docs-vnext/twitter-api/tweets/lookup/api-reference/get-tweets "API reference")

[Sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code "Sample code")

API reference

API reference index
-------------------

For the complete API reference, select an endpoint from the list:

|     |     |
| --- | --- |
| **Get all messages in a 1-1 conversation** | [GET /2/dm\_conversations/with/:user\_id/dm\_events](https://developer.twitter.com/en/docs/twitter-api/direct-messages/lookup/api-reference/get-dm_conversations-with-participant_id-dm_events) |
| **Get all messages in a specific conversation (both group and 1-1 conversations)** | [GET /2/dm\_conversations/:dm\_conversation\_id/dm\_events](https://developer.twitter.com/en/docs/twitter-api/direct-messages/lookup/api-reference/get-dm_conversations-dm_conversation_id-dm_events) |
| **Get all messages across a user's DM conversations (both sent and received, group and 1-1 conversations)** | [GET /2/dm\_events](https://developer.twitter.com/en/docs/twitter-api/direct-messages/lookup/api-reference/get-dm_events) |

GET /2/dm\_events

GET /2/dm\_events
=================

Returns a list of Direct Messages for the authenticated user, both sent and received. Direct Message events are returned in reverse chronological order. Supports retrieving events from the previous 30 days.

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Try a live request ❯](https://oauth-playground.glitch.me/?id=getDmEvents) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Fdm_events&method=get) 

### Endpoint URL

`https://api.twitter.com/2/dm_events`  
  

### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code "This method allows an authorized app to act on behalf of the user, as the user. It is typically used to access or post public information for a specific user, and it us useful when your app needs to be aware of the relationship between a user and what this endpoint returns. Click to learn how to authenticate with OAuth 2.0 Authorization Code with PKCE.") |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | User rate limit (User context): 300 requests per 15-minute window per each authenticated user |

### OAuth 2.0 scopes required by this endpoint

|     |
| --- |
| `dm.read`<br><br>`tweet.read`<br><br>`user.read` |
| [Learn more about OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/twitter-api/oauth2) |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| `dm_event.fields`  <br> Optional | enum (`id`, `text`, `event_type`, `created_at`, `dm_conversation_id`, `sender_id`, `participant_ids`, `referenced_tweets`, `attachments`) | Extra fields to include in the event payload. `id`, and `event_type` are returned by default. The `text` value isn't included for `ParticipantsJoin` and `PartcipantsLeave` events. |
| `event_types`  <br> Optional | enum (`MessageCreate`, `ParticipantsJoin`, `ParticipantsLeave`) | The type of Direct Message event to return. If not included, all types are returned. |
| `expansions`  <br> Optional | enum (`attachments.media_keys`, `referenced_tweets.id`, `sender_id`, `participant_ids`) | [Expansions](https://developer.twitter.com/en/docs/twitter-api/expansions) enable you to request additional data objects that relate to the returned Direct Message conversation events. Submit a list of desired expansions in a comma-separated list without spaces. The IDs that represents the expanded data objects will be included directly in the event data object, and the expanded object metadata will be returned within the `includes` response object.  <br>  <br>The following data objects can be expanded using this parameter:  <br><br>* The user object for the message sender.<br>* Attached media's object.<br>* Any referenced Tweet's object.<br>* The user object for who is joining or leaving group conversations. |
| `max_results`  <br> Optional | number | The maximum number of results to be returned in a page. Must be between 1 and 100. The default is 100. |
| `media.fields`  <br> Optional | enum (`duration_ms`, `height`, `media_key`, `preview_image_url`, `type`, `url`, `width`, `public_metrics`, `alt_text`, `variants`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [media fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/media) will be delivered in Direct Message 'MessageCreate' events.  <br>  <br>Specify the desired fields in a comma-separated list without spaces between commas and fields. While the media ID will be located in the event object, you will find this ID and all additional media fields in the `includes` data object.  <br>  <br>The event object will only include media fields if the Direct Message contains media and if you've also included the `expansions=attachments.media_keys` query parameter in your request. |
| `pagination_token`  <br> Optional | string | Contains either the `next_token` or `previous_token` value. |
| `tweet.fields`  <br> Optional | enum (`attachments`, `author_id`, `context_annotations`, `conversation_id`, `created_at`, `edit_controls`, `entities`, `geo`, `id`, `in_reply_to_user_id`, `lang`, `public_metrics`, `possibly_sensitive`, `referenced_tweets`, `reply_settings`, `source`, `text`, `withheld`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [Tweet fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) will be delivered in each returned Direct Message 'MessageCreate' event object that contains a Tweet reference.  <br>  <br>Specify the desired fields in a comma-separated list without spaces between commas and fields. While the Tweet ID will be in the event object, you will find this ID and all additional Tweet fields in the ``includes data object.      The event object will include Tweet fields only if the Direct Message references a Tweet and the `expansions=referenced_tweet.id` query parameter is included in the request.`` |
| `user.fields`  <br> Optional | enum (`created_at`, `description`, `entities`, `id`, `location`, `most_recent_tweet_id`, `name`, `pinned_tweet_id`, `profile_image_url`, `protected`, `public_metrics`, `url`, `username`, `verified`, `withheld`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [user fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) will be delivered for Direct Message conversation events that reference a sender or participant ID.  <br>  <br>Specify the desired fields in a comma-separated list without spaces between commas and fields.  <br>  <br>While the user ID will be located in the event object, you will find this ID and all additional user fields in the `includes` data object.  <br>  <br>You must also pass one of the user-based expansions to return the desired user fields:  <br><br>* `expansions=sender_id`<br>* `expansions=participants_id` |

  
  

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [cURL (default fields)](#tab0)
* [cURL (optional fields)](#tab1)

cURL (default fields)

cURL (optional fields)

      `curl "https://api.twitter.com/2/dm_events" -H "Authorization: Bearer $ACCESS_TOKEN" -H "Authorization: Bearer $ACCESS_TOKEN"`
    

      `curl "https://api.twitter.com/2/dm_events?dm_event.fields=id,text,event_type,dm_conversation_id,created_at,sender_id,attachments,participant_ids,referenced_tweets" -H "Authorization: Bearer $ACCESS_TOKEN"`
    

### Example responses

* [Default fields](#tab0)
* [Optional fields](#tab1)

Default fields

Optional fields

      `{   "data": [     {       "event_type": "MessageCreate",       "id": "1346889436626259968",       "text": "Hello just you..."     }   ] }`
    

      `{   "data": [     {       "id": "1585321444547837956",       "text": "Another photo https://t.co/J5KotyeIyd",       "event_type": "MessageCreate",       "dm_conversation_id": "1585094756761149440",       "created_at": "2022-10-26T17:24:21.000Z",       "sender_id": "906948460078698496"     }   ] }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | string | The `id` of the Direct Message event. |
| `text` | string | The text included in the Direct Message. |
| `event_type` | string | The type of event. |
| `created_at` | date (ISO 8601) | The `timestamp` of the Direct Message event creation. |
| `sender_id` | string | The `id` of the user who sent the Direct Message. |
| `dm_conversation_id` | string | The `id` of the Direct Message to which the event belongs. |
| `attachments` | object | The attached urls and media information for expansion. E.g. Media, Tweet, Card |
| `attachments.media_keys` | array | List of unique identifiers of media attached to a Direct Message. These identifiers use the same media key format as those returned by the [Media Library](https://developer.twitter.com/en/docs/ads/creatives/guides/media-library).  <br>  <br>You can obtain the expanded object in `includes.media` by adding `expansions=attachments.media_keys` in the request's query parameter. |
| `referenced_tweets` | array | Expansion of a "shared" Tweet in the Direct Message. If the parent Tweet is a Retweet, a Retweet with comment (also known as Quoted Tweet) or a Reply, it will include the related Tweet referenced to by its parent. |
| `referenced_tweets.id` | string | The `id` of a "shared" Tweet in the Direct Message.  <br>  <br>You can obtain the expanded object in `includes.tweets` by adding `expansions=referenced_tweets.id` in the request's query parameter. |
| `media.fields` | enum (`duration_ms`, `height`, `media_key`, `preview_image_url`, `type`, `url`, `width`, `public_metrics`, `non_public_metrics`, `organic_metrics`, `promoted_metrics`, `alt_text`, `variants`) | Expansion of included media with its own fields. E.g. url, size, etc. When including the `expansions=attachments.media_keys` parameter, this includes a list of images, videos, and GIFs included in Tweets in the form of [media objects](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/media) with their default fields and any additional fields requested using the `media.fields` parameter, assuming there is a media attachment present in the returned Tweet(s).  <br>  <br>You can obtain the expanded object in `includes.media` by adding `expansions=media.fields` in the request's query parameter. |
| `user.fields` | string | The Expansion of user object via `sender_id`.  <br>  <br>You can obtain the expanded object in `includes.users` by adding `expansions=user.fields` in the request's query parameter. |
| `meta` | object | This object contains information about the number of messages returned in the current request and pagination details. |
| `meta.next_token` | string | A value that encodes the next 'page' of results that can be requested, via the `pagination_token` request parameter. |
| `meta.previous_token` | string | A value that encodes the previous 'page' of results that can be requested, via the `pagination_token` request parameter. |
| `meta.result_count` | number | The number of results in the current page. |
| `errors` | object | Contains details about errors in a request for messages in a specified conversation. |

GET /2/dm\_conversations/with/:participant\_id/dm\_events

GET /2/dm\_conversations/with/:participant\_id/dm\_events
=========================================================

Returns a list of Direct Messages (DM) events within a 1-1 conversation with the user specified in the `participant_id` path parameter. Messages are returned in reverse chronological order.

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Try a live request ❯](https://oauth-playground.glitch.me/?id=getDmConversationsWithParticipantIdDmEvents) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Fdm_conversations%2Fwith%2F%7Bparticipant_id%7D%2Fdm_events&method=get) 

### Endpoint URL

`https://api.twitter.com/2/dm_conversations/with/:participant_id/dm_events`  
  

### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code "This method allows an authorized app to act on behalf of the user, as the user. It is typically used to access or post public information for a specific user, and it us useful when your app needs to be aware of the relationship between a user and what this endpoint returns. Click to learn how to authenticate with OAuth 2.0 Authorization Code with PKCE.") |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | User rate limit (User context): 300 requests per 15-minute window per each authenticated user |

### OAuth 2.0 scopes required by this endpoint

|     |
| --- |
| `dm.read`<br><br>`tweet.read`<br><br>`user.read` |
| [Learn more about OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/twitter-api/oauth2) |

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `participant_id`  <br> Required | string | The `participant_id` of the user that the authenicating user is having a 1-1 conversation with. |

  
  

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| `dm_event.fields`  <br> Optional | enum (`id`, `text`, `event_type`, `created_at`, `dm_conversation_id`, `sender_id`, `participant_ids`, `referenced_tweets`, `attachments`) | Extra fields to include in the event payload. `id`, and `event_type` are returned by default. The `text` value isn't included for `ParticipantsJoin` and `PartcipantsLeave` events. |
| `event_types`  <br> Optional | enum (`MessageCreate`, `ParticipantsJoin`, `ParticipantsLeave`) | The type of Direct Message event to returm. In the context of one-to-one conversations, only `MessageCreate` is relevant. |
| `expansions`  <br> Optional | enum (`attachments.media_keys`, `referenced_tweets.id`, `sender_id`, `participant_ids`) | [Expansions](https://developer.twitter.com/en/docs/twitter-api/expansions) enable you to request additional data objects that relate to the returned Direct Message conversation events. Submit a list of desired expansions in a comma-separated list without spaces. The IDs that represents the expanded data objects will be included directly in the event data object, and the expanded object metadata will be returned within the `includes` response object.  <br>  <br>The following data objects can be expanded using this parameter:  <br><br>* The user object for the message sender.<br>* Attached media's object.<br>* Any referenced Tweet's object.<br>* The user object for who is joining or leaving group conversations. |
| `max_results`  <br> Optional | number | The maximum number of results to be returned in a page. Must be between 1 and 100. The default is 100. |
| `media.fields`  <br> Optional | enum (`duration_ms`, `height`, `media_key`, `preview_image_url`, `type`, `url`, `width`, `public_metrics`, `alt_text`, `variants`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [media fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/media) will be delivered in Direct Message 'MessageCreate' events.  <br>  <br>Specify the desired fields in a comma-separated list without spaces between commas and fields. While the media ID will be located in the event object, you will find this ID and all additional media fields in the `includes` data object.  <br>  <br>The event object will only include media fields if the Direct Message contains media and if you've also included the `expansions=attachments.media_keys` query parameter in your request. |
| `pagination_token`  <br> Optional | string | Contains either the `next_token` or `previous_token` value. |
| `tweet.fields`  <br> Optional | enum (`attachments`, `author_id`, `context_annotations`, `conversation_id`, `created_at`, `edit_controls`, `entities`, `geo`, `id`, `in_reply_to_user_id`, `lang`, `public_metrics`, `possibly_sensitive`, `referenced_tweets`, `reply_settings`, `source`, `text`, `withheld`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [Tweet fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) will be delivered in each returned Direct Message 'MessageCreate' event object that contains a Tweet reference.  <br>  <br>Specify the desired fields in a comma-separated list without spaces between commas and fields. While the Tweet ID will be in the event object, you will find this ID and all additional Tweet fields in the ``includes data object.      The event object will include Tweet fields only if the Direct Message references a Tweet and the `expansions=referenced_tweet.id` query parameter is included in the request.`` |
| `user.fields`  <br> Optional | enum (`created_at`, `description`, `entities`, `id`, `location`, `most_recent_tweet_id`, `name`, `pinned_tweet_id`, `profile_image_url`, `protected`, `public_metrics`, `url`, `username`, `verified`, `withheld`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [user fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) will be delivered for Direct Message conversation events that reference a sender or participant ID.  <br>  <br>Specify the desired fields in a comma-separated list without spaces between commas and fields.  <br>  <br>While the user ID will be located in the event object, you will find this ID and all additional user fields in the `includes` data object.  <br>  <br>You must also pass one of the user-based expansions to return the desired user fields:  <br><br>* `expansions=sender_id`<br>* `expansions=participants_id` |

  
  

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [cURL (default fields)](#tab0)
* [cURL (optional fields)](#tab1)

cURL (default fields)

cURL (optional fields)

      `curl "https://api.twitter.com/2/dm_conversations/with/:participant_id/dm_events" -H "Authorization: Bearer $ACCESS_TOKEN"`
    

      `curl "https://api.twitter.com/2/dm_conversations/with/:participant_id/dm_events?dm_event.fields=id,text,event_type,dm_conversation_id,created_at,sender_id,attachments,participant_ids,referenced_tweets" -H "Authorization: Bearer $ACCESS_TOKEN"`
    

### Example responses

* [Default fields](#tab0)
* [Optional fields](#tab1)

Default fields

Optional fields

      `{   "data": [     {       "event_type": "MessageCreate",       "id": "1346889436626259968",       "text": "Hello just you..."     }   ] }`
    

      `{   "data": [     {       "id": "1585321444547837956",       "text": "Another photo https://t.co/J5KotyeIyd",       "event_type": "MessageCreate",       "dm_conversation_id": "1585094756761149440",       "created_at": "2022-10-26T17:24:21.000Z",       "sender_id": "906948460078698496"     }   ] }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | string | The `id` of the Direct Message event. |
| `text` | string | The text included in the Direct Message. |
| `event_type` | string | The type of event. Possible values include MessageCreate, ParticipantsJoin, ParticipantsLeave. |
| `created_at` | date (ISO 8601) | The `timestamp` of the Direct Message event creation. |
| `sender_id` | string | The `id` of the user who sent the Direct Message. |
| `dm_conversation_id` | string | The `id` of the conversation the Direct Message belongs to. |
| `attachments` | object | The attached urls and media information for expansion. E.g. Media, Tweet, Card |
| `attachments.media_keys` | array | List of unique identifiers of media attached to a direct message. These identifiers use the same media key format as those returned by the [Media Library](https://developer.twitter.com/en/docs/ads/creatives/guides/media-library).  <br>  <br>You can obtain the expanded object in `includes.media` by adding `expansions=attachments.media_keys` in the request's query parameter. |
| `referenced_tweets` | array | Expansion of a "shared" Tweet in the Direct Message. If the parent Tweet is a Retweet, a Retweet with comment (also known as Quoted Tweet) or a Reply, it will include the related Tweet referenced to by its parent. |
| `referenced_tweets.id` | string | The `id` of a "shared" Tweet in the Direct Message.  <br>  <br>You can obtain the expanded object in `includes.tweets` by adding `expansions=referenced_tweets.id` in the request's query parameter. |
| `media.fields` | enum (`duration_ms`, `height`, `media_key`, `preview_image_url`, `type`, `url`, `width`, `public_metrics`, `non_public_metrics`, `organic_metrics`, `promoted_metrics`, `alt_text`, `variants`) | Expansion of included media with its own fields. E.g. url, size, etc. When including the `expansions=attachments.media_keys` parameter, this includes a list of images, videos, and GIFs included in Tweets in the form of [media objects](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/media) with their default fields and any additional fields requested using the `media.fields` parameter, assuming there is a media attachment present in the returned Tweet(s).  <br>  <br>You can obtain the expanded object in `includes.media` by adding `expansions=media.fields` in the request's query parameter. |
| `user.fields` | string | The Expansion of user object via `sender_id`.  <br>  <br>You can obtain the expanded object in `includes.users` by adding `expansions=user.fields` in the request's query parameter. |
| `meta` | object | This object contains information about the number of messages returned in the current request and pagination details. |
| `meta.next_token` | string | A value that encodes the next 'page' of results that can be requested, via the `pagination_token` request parameter. |
| `meta.previous_token` | string | A value that encodes the previous 'page' of results that can be requested, via the `pagination_token` request parameter. |
| `meta.result_count` | number | The number of results in the current page. |
| `errors` | object | Contains details about errors in a request for messages in a specified conversation. |

GET /2/dm\_conversations/:dm\_conversation\_id/dm\_events

GET /2/dm\_conversations/:dm\_conversation\_id/dm\_events
=========================================================

Returns a list of Direct Messages within a conversation specified in the `dm_conversation_id` path parameter. Messages are returned in reverse chronological order.

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Try a live request ❯](https://oauth-playground.glitch.me/?id=getDmConversationsIdDmEvents) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Fdm_conversations%2F%7Bdm_conversation_id%7D%2Fdm_events&method=get) 

### Endpoint URL

`https://api.twitter.com/2/dm_conversations/:dm_conversation_id/dm_events`  
  

### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code "This method allows an authorized app to act on behalf of the user, as the user. It is typically used to access or post public information for a specific user, and it us useful when your app needs to be aware of the relationship between a user and what this endpoint returns. Click to learn how to authenticate with OAuth 2.0 Authorization Code with PKCE.") |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | User rate limit (User context): 300 requests per 15-minute window per each authenticated user |

### OAuth 2.0 scopes required by this endpoint

|     |
| --- |
| `dm.read`<br><br>`tweet.read`<br><br>`user.read` |
| [Learn more about OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/twitter-api/oauth2) |

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `dm_conversation_id`  <br> Required | string | The `id` of the Direct Message conversation for which events are being retrieved. |

  
  

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| `dm_event.fields`  <br> Optional | enum (`id`, `text`, `event_type`, `created_at`, `dm_conversation_id`, `sender_id`, `participant_ids`, `referenced_tweets`, `attachments`) | Extra fields to include in the event payload. `id`, and `event_type` are returned by default. The `text` value isn't included for `ParticipantsJoin` and `PartcipantsLeave` events. |
| `event_types`  <br> Optional | enum (`MessageCreate`, `ParticipantsJoin`, `ParticipantsLeave`) | The type of Direct Message event to returm. If not included, all types are returned. |
| `expansions`  <br> Optional | enum (`attachments.media_keys`, `referenced_tweets.id`, `sender_id`, `participant_ids`) | [Expansions](https://developer.twitter.com/en/docs/twitter-api/expansions) enable you to request additional data objects that relate to the returned Direct Message conversation events. Submit a list of desired expansions in a comma-separated list without spaces. The IDs that represents the expanded data objects will be included directly in the event data object, and the expanded object metadata will be returned within the `includes` response object.  <br>  <br>The following data objects can be expanded using this parameter:  <br><br>* The user object for the message sender.<br>* Attached media's object.<br>* Any referenced Tweet's object.<br>* The user object for who is joining or leaving group conversations. |
| `max_results`  <br> Optional | number | The maximum number of results to be returned in a page. Must be between 1 and 100. The default is 100. |
| `media.fields`  <br> Optional | enum (`duration_ms`, `height`, `media_key`, `preview_image_url`, `type`, `url`, `width`, `public_metrics`, `alt_text`, `variants`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [media fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/media) will be delivered in Direct Message 'MessageCreate' events.  <br>  <br>Specify the desired fields in a comma-separated list without spaces between commas and fields. While the media ID will be located in the event object, you will find this ID and all additional media fields in the `includes` data object.  <br>  <br>The event object will only include media fields if the Direct Message contains media and if you've also included the `expansions=attachments.media_keys` query parameter in your request. |
| `pagination_token`  <br> Optional | string | Contains either the `next_token` or `previous_token` value. |
| `tweet.fields`  <br> Optional | enum (`attachments`, `author_id`, `context_annotations`, `conversation_id`, `created_at`, `edit_controls`, `entities`, `geo`, `id`, `in_reply_to_user_id`, `lang`, `public_metrics`, `possibly_sensitive`, `referenced_tweets`, `reply_settings`, `source`, `text`, `withheld`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [Tweet fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) will be delivered in each returned Direct Message 'MessageCreate' event object that contains a Tweet reference.  <br>  <br>Specify the desired fields in a comma-separated list without spaces between commas and fields. While the Tweet ID will be in the event object, you will find this ID and all additional Tweet fields in the ``includes data object.      The event object will include Tweet fields only if the Direct Message references a Tweet and the `expansions=referenced_tweet.id` query parameter is included in the request.`` |
| `user.fields`  <br> Optional | enum (`created_at`, `description`, `entities`, `id`, `location`, `most_recent_tweet_id`, `name`, `pinned_tweet_id`, `profile_image_url`, `protected`, `public_metrics`, `url`, `username`, `verified`, `withheld`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [user fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) will be delivered for Direct Message conversation events that reference a sender or participant ID.  <br>  <br>Specify the desired fields in a comma-separated list without spaces between commas and fields.  <br>  <br>While the user ID will be located in the event object, you will find this ID and all additional user fields in the `includes` data object.  <br>  <br>You must also pass one of the user-based expansions to return the desired user fields:  <br><br>* `expansions=sender_id`<br>* `expansions=participants_id` |

  
  

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [cURL (default fields)](#tab0)
* [cURL (optional fields)](#tab1)

cURL (default fields)

cURL (optional fields)

      `curl "https://api.twitter.com/2/dm_conversations/:dm_conversation_id/dm_events" -H "Authorization: Bearer $ACCESS_TOKEN" -H "Authorization: Bearer $ACCESS_TOKEN"`
    

      `curl "https://api.twitter.com/2/dm_conversations/:dm_conversation_id/dm_events?dm_event.fields=id,text,event_type,dm_conversation_id,created_at,sender_id,attachments,participant_ids,referenced_tweets" -H Authorization: Bearer $ACCESS_TOKEN"`
    

### Example responses

* [Default fields](#tab0)
* [Optional fields](#tab1)

Default fields

Optional fields

      `{   "data": [     {       "event_type": "MessageCreate",       "id": "1346889436626259968",       "text": "Hello just you..."     }   ] }`
    

      `{   "data": [     {       "id": "1585321444547837956",       "text": "Another photo https://t.co/J5KotyeIyd",       "event_type": "MessageCreate",       "dm_conversation_id": "1585094756761149440",       "created_at": "2022-10-26T17:24:21.000Z",       "sender_id": "906948460078698496"     }   ] }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | string | The `id` of the Direct Message event. |
| `text` | string | The text included in the Direct Message. |
| `event_type` | string | The type of event. Possible values include MessageCreate, ParticipantsJoin, ParticipantsLeave. |
| `created_at` | date (ISO 8601) | The `timestamp` of the Direct Message event creation. |
| `sender_id` | string | The `id` of the user who sent the Direct Message. |
| `dm_conversation_id` | string | The `id` of the conversation the Direct Message belongs to. |
| `attachments` | object | The attached urls and media information for expansion. E.g. Media, Tweet, Card |
| `attachments.media_keys` | array | List of unique identifiers of media attached to a direct message. These identifiers use the same media key format as those returned by the [Media Library](https://developer.twitter.com/en/docs/ads/creatives/guides/media-library).  <br>  <br>You can obtain the expanded object in `includes.media` by adding `expansions=attachments.media_keys` in the request's query parameter. |
| `referenced_tweets` | array | Expansion of a "shared" Tweet in the Direct Message. If the parent Tweet is a Retweet, a Retweet with comment (also known as Quoted Tweet) or a Reply, it will include the related Tweet referenced to by its parent. |
| `referenced_tweets.id` | string | The `id` of a "shared" Tweet in the Direct Message.  <br>  <br>You can obtain the expanded object in `includes.tweets` by adding `expansions=referenced_tweets.id` in the request's query parameter. |
| `media.fields` | enum (`duration_ms`, `height`, `media_key`, `preview_image_url`, `type`, `url`, `width`, `public_metrics`, `non_public_metrics`, `organic_metrics`, `promoted_metrics`, `alt_text`, `variants`) | Expansion of included media with its own fields. E.g. url, size, etc. When including the `expansions=attachments.media_keys` parameter, this includes a list of images, videos, and GIFs included in Tweets in the form of [media objects](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/media) with their default fields and any additional fields requested using the `media.fields` parameter, assuming there is a media attachment present in the returned Tweet(s).  <br>  <br>You can obtain the expanded object in `includes.media` by adding `expansions=media.fields` in the request's query parameter. |
| `user.fields` | string | The Expansion of user object via `sender_id`.  <br>  <br>You can obtain the expanded object in `includes.users` by adding `expansions=user.fields` in the request's query parameter. |
| `meta` | object | This object contains information about the number of messages returned in the current request and pagination details. |
| `meta.next_token` | string | A value that encodes the next 'page' of results that can be requested, via the `pagination_token` request parameter. |
| `meta.previous_token` | string | A value that encodes the previous 'page' of results that can be requested, via the `pagination_token` request parameter. |
| `meta.result_count` | number | The number of results in the current page. |
| `errors` | object | Contains details about errors in a request for messages in a specified conversation. |

Introduction

Introduction
------------

Direct Messages enable private conversations on Twitter. Direct Messages are one of the most popular features of Twitter, with a wide variety of use cases. These use cases range from group chats among friends, to powering customer support for brands around the world. New v2 versions of Direct Messages endpoints will be introduced in stages, and this first stage includes fundamental endpoints for creating Direct Messages and listing Direct Message conversation events. For the first time, the Twitter API v2 supports _group_ conversations.

This initial release of Manage Direct Messages includes three POST methods for creating Direct Messages:

* **POST /2/dm\_conversations/with/:participant\_id/messages** - Creates a one-to-one Direct Message. This method either creates a new 1-1 conversation or retrieves the current conversation and adds the Direct Message to it. The :participant\_idpath parameter is the User ID of the account receiving the message. 
* **POST /2/dm\_conversations** - Creates a new group conversation and adds a Direct Message to it. These requests require a list of conversation participants. Note that you can create multiple conversations with the same participant list. These requests will always return a new conversation ID. 
* **POST /2/dm\_conversations/:dm\_conversation\_id/messages** - Creates a Direct Message and adds it to an existing conversation. The :dm\_conversation\_id path parameter is the ID of the conversation that the message will be added to. 

Note that Direct Message event IDs are common across the v1.1 and v2 (as well as the Twitter App), so the v1.1 methods to hide/delete Direct Messages can be used along with this new v2 endpoint. Also note that the Enterprise and Premium Account Activity APIs support v2 one-to-one messages, but do not yet support group conversations.     

There is a user rate limit of 200 requests per 15 minutes for the POST method. There is also a rate limit of 1000 requests per 24 hours per user. Additionally, there is a rate limit of 15000 requests per 24 hours. Note that these rate limits are shared across these POST endpoints.

Since you are making requests on behalf of a user with the manage Tweets endpoints, you must authenticate with either [OAuth 1.0a User Context](https://developer-staging.twitter.com/en/docs/authentication/oauth-1-0a) or [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code), and use a user Access Tokens associated with a user that has authorized your App. To generate this user Access Token with OAuth 1.0a, you can use the [3-legged OAuth flow](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens). To generate a user Access Token with OAuth 2.0, you can use the [Authorization Code with PKCE grant flow](https://developer.twitter.com/en/docs/authentication/oauth-2-0/user-access-token).  

**Account setup**

To access these endpoints, you will need:

* An approved [developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info).
* To authenticate using the keys and tokens from a [developer App](https://developer.twitter.com/en/docs/apps) that is located within a [Project](https://developer.twitter.com/en/docs/projects). 

Learn more about getting access to the Twitter API v2 endpoints in our [getting started guide](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api).

[Quick start](https://developer.twitter.com/en/docs/twitter-api/direct-messages/manage/quick-start)

[Sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code)

[Run in Postman](https://t.co/twitter-api-postman)

[Try with API Explorer](https://developer.twitter.com/apitools/api?endpoint=/2/tweets&method=post)

Supporting resources
--------------------

[Learn how to use Postman](https://developer.twitter.com/en/docs/tutorials/postman-getting-started "Learn how to use Postman")

[Troubleshoot an error](https://developer.twitter.com/en/support/twitter-api "Troubleshoot an error")

[API Reference](https://developer.twitter.com/en/docs/twitter-api/direct-messages/manage/api-reference "API Reference")

Quick start

Getting started with the manage Direct Message endpoints
--------------------------------------------------------

This quick start guide will help you make your first request to the Direct Message endpoints using Postman, a tool for managing and making HTTP requests. To learn more about our Postman collections, please visit our [Using Postman](https://developer.twitter.com/en/docs/tools-and-libraries/using-postman) guide,

Please visit our [Twitter API v2 sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code) GitHub repository if you want to review Python-based examples. In addition, the official [Twitter Developer Platform software development kits (SDKs)](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview) will be updated to support these Direct Message endpoints.  

### Prerequisites

To complete this guide, you will need to have a set of [keys and tokens](https://developer.twitter.com/en/docs/authentication) to authenticate your request. You can generate these keys and tokens by following these steps:

* [Sign up for a developer account](https://developer.twitter.com/en/apply-for-access) and receive approval.
* Create a [Project](https://developer.twitter.com/en/docs/projects) and an associated [developer App](https://developer.twitter.com/en/docs/apps) in the developer portal.
* Navigate to your App's “Keys and tokens” page to generate the required credentials. Make sure to save all credentials in a secure location.

### Steps to building manage Direct Message requests

In this example, in one request, we'll create a new group conversation and add our first message to it. We'll then add a second message to the created conversation.

#### Step one: Start with a tool or library

To begin working with the manage Direct Message endpoints, we are going to use the Postman tool to simplify the process. A TwitterDev-authored collection of example Twitter API v2 requests will be used to explore six endpoints used to create new Direct Messages and to list Direct Message conversation events.

While most of the collection is pre-filled, there are a few details that you'll need to provide that are based on the Twitter App created to host these API requests. First, let's get the collection loaded/updated.

To load the Twitter API v2 Postman collection into your environment, please click on the following button:

[Add Twitter API v2 to Postman](https://t.co/twitter-api-postman)

Once you have the Twitter API v2 collection loaded in Postman, navigate to the “Manage Direct Messages” folder. This folder's Authorization tab has been pre-filled where possible, and you can update a few settings to share your Twitter App's authentication details. This folder also contains three endpoints for creating new Direct Messages. Note that there is also a "Direct Message lookup" folder with three available endpoints for retrieving Direct Message conversation events, including sending and receiving messages, and when conversation participants join and leave.. 

Since creating group conversations is an exciting new feature of the Twitter API v2, this example will focus on that. We will be working with the "New group DM and conversation" example. We will use this request to create a Direct Message group conversation.

The next step is to authenticate with the endpoint.

**Step two: Authenticate your request**  

To properly make a request to the Twitter API, you need to verify that you have permission to do so. To make a successful request to this endpoint, we will be using [OAuth 2.0 Authorization Code Flow with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code). You can generate an access token within Postman. 

With Postman you can set the authentication method at the folder level or at the request level. Here we will be configuring the authentication details at the folder level.

Navigate to the "Manage Direct Messages" folder, select the "Authorization" tab and confirm that the Type to set to “OAuth 2.0,” and "Add auth data to" is set to "Request Headers." In the "Current Token" section, make sure the "header Prefix" is set to Bearer.  

To configure and generate a new token:

1. Create a Token Name, such as "Manage DMs."
    
2. Confirm that **Grant Type** is set to Authorization Code (with PKCE).
    
3. Set your **Callback URL**. You will want to update your Callback URL to exactly match the Callback URL associated with your application in the [v2 Dev Portal](https://developer.twitter.com/en/portal/dashboard). With the Twitter App used with this example, the Callback URL is set to - [_https://www.example.com_.](https://www.example.com/) (Note that since this must match exactly, [_https://example.com_](https://example.com/) would not work.) 
    
4. Confirm that **Auth URL** is set to [https://twitter.com/i/oauth2/authorize](https://twitter.com/i/oauth2/authorize).
    
5. Confirm that **Access Token URL** is set to [https://api.twitter.com/2/oauth2/token.](https://api.twitter.com/2/oauth2/token)**Client ID** - Copy and paste OAuth 2.0 client ID from the Developer Portal  
    **Client Secret** - You will need this only if you are using an App type that is a confidential client. If so, copy and paste the OAuth 2.0 Client Secret from the Developer Portal. 
    
6. Confirm that **Scope** is set to dm.read, dm.write, tweet.read, and users.read.
    
7. Confirm that **State** is set to “state.”
    
8. Confirm that **Client Authentication** is set to Send as Basic Auth header.
    
9. Click where it says **Get New Access Token**, click "Authorize app" as part of the "Sign-in with Twitter" process.
    
10. Click the "Proceed" button and then the "Use Token" to generate a token. 
    
11. Click on the "Save" button to save these configuration details.
    

You may get a message that you are not logged into Twitter. If you get this error, you will need to log in to the Twitter account you are trying to post on behalf of inside of Postman.

Now that these OAuth 2.0 details have been set at the folder level, navigate to each of the examples and their "Authorization" tab and confirm that they have their Type set to "Inherit auth from parent." 

Note that this token will expire soon, and you'll need to regenerate it by clicking on the "Get New Access Token" button. Clicking that will trigger the "Sign-in with Twitter" process and generate a fresh token to make requests with.

#### Step three: Specify the Direct Message conversation participants and message contents

Navigate to the “Body” tab and make updates to the example JSON object. Set the participant\_ids attribute to the accounts you want to send the Direct Message to.

      `{    "message": {"text": "Hello to just you two, this is a new group conversation."},    "participant_ids": ["944480690","906948460078698496"],    "conversation_type": "Group"        }`
    

#### Step four: Make your request and review the response

Once you have everything set up, hit the "Send" button, and you will receive a similar response to the example response below. A reminder that if your token has expired since you created it above, you can return to the folder's Authorization tab and click on the "Get New Access Token" to create a fresh token.

      `{    "data": {        "dm_conversation_id": "1582103724607971328",        "dm_event_id": "1582103724607971332"    } }`
    

If the returned response "data" object contains a dm\_conversation\_id and an dm\_event\_id, you have successfully created a new Direct Message conversation. To start looking up events associated with this conversation, head over to the Direct Message lookup Quick start guide.

#### Step five: Add another message to that group conversation

Now select the "Add DM to conversation" example, and select the "Params" tab. Under "Path Variables" , update the dm\_conversation\_id to the ID of the conversation you created above.

|     |     |
| --- | --- |
| **Key** | **Value** |
| dm\_conversation\_id | 1582103724607971328 |

Using this conversation ID, the request path will resolve to: https://api.twitter.com/2/dm\_conversations/1582103724607971328/messages

Also, update the "Body" tab with request JSON containing the message text you want to send: 

      `{    "text": "Adding a new message to our group conversation..." }`
    

Once you have everything set up, hit the "Send" button, and you will receive a similar response to the following example response:

      `{    "data": {        "dm_conversation_id": "1582103724607971328",        "dm_event_id": "1582106224379559940"    } }`
    

Next steps
----------

[API Reference](https://developer.twitter.com/en/docs/twitter-api/direct-messages/manage/api-reference "API Reference")

[Get support](https://developer.twitter.com/en/support/twitter-api "Get support")

[Sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code "Sample code")

Integrate

Integration guide
-----------------

The Direct Messages endpoints v2 introduce conversations and conversation events as core Twitter API objects, and makes a distinction between one-to-one and group conversations. One-to-one conversations always have two, and only two, participants, while group conversations can have two or more and memberships that can change.   

This page contains information on several tools and key concepts that you should be aware of as you integrate the Manage Direct Messages endpoints into your system. We’ve broken the page into two sections:

* Key Concepts
    * [Direct Message conversations](#direct-message-conversations)  
        
    * [Shared conversation and event IDs across v1.1 and v2](#shared-conversation-and-event-ids)
    * [Including media attachments and referencing Tweets](#including-media-attachments-and-referencing-tweets)
    * [Authentication](#authentication)  
        
    * [Developer portal, Projects, and developer Apps](#developer-portal-projects-and-developer-apps)  
        
    * [Rate limits](#rate-limits)  
        
* [Helpful tools](#helpful-tools)

Key Concepts
------------

### Direct Message conversations

All Direct Messages are part of a Direct Message conversation. These conversations can be one-to-one conversations or group conversations. This launch provides the foundational endpoints needed to create Direct Messages and retrieve events associated with Direct Message conversations. All conversations have a unique dm\_conversation\_id, and the events that make up that conversation all have a unique dm\_event\_id.  

The Manage Direct Message endpoints provide three POST methods for creating new messages and adding them to conversations:

* **POST /2/dm\_conversations/with/:participant\_id/messages** - Creates a one-to-one Direct Message. This method either adds the message to an existing one-to-one conversation or creates a new one. The :participant\_id path parameter is the User ID of the account receiving the message.   
    Here is an example JSON request body for sending a one-to-one Direct Message:
    

      `{    "text": "Hello just you. This will appear as a new conversation if we have never messaged, or will be added to our existing thread. " }`
    

* **POST /2/dm\_conversations** - Creates a new group conversation and adds a Direct Message to it. These requests require a list of conversation participants. Note that you can create multiple conversations with the same participant list. These requests will always return a new conversation ID. Below is an example JSON request body for creating a new group conversation and adding a Direct Message. Note that this requires a "conversation\_type" field and that must be set to "Group" (case sensitive).

      `{    "message": {"text": "Hello to just you two, this is a new group conversation."},    "participant_ids": ["944480690","906948460078698496"],    "conversation_type": "Group"        }`
    

* **POST /2/dm\_conversations/:dm\_conversation\_id/messages** \- Creates a Direct Message and adds it to an existing conversation. The :dm\_conversation\_id path parameter is the ID of the conversation that the message will be added to. This method can be used to add a message to both one-to-one and group conversations.  
    Here is an example JSON request body for sending Direct Message to both one-to-one and group conversations:
    

      `{    "text": "Here is a new message." }`
    

These POST methods support attaching a single piece of media. POST request bodies must include either or both the "text" and "attachments" fields. The "text" attribute is required if the "attachments" field is not included, and the "attachments" field is required if the "text" field is not included. See the next section for more information.

For more information see the [Manage Direct Messages API References](https://developer.twitter.com/en/docs/twitter-api/direct-messages/manage/api-reference).   

### Shared conversation and event IDs across v1.1 and v2

An important concept is that conversation and event IDs are shared across v1.1 and v2 versions of the Twitter Platform. This means both versions can be used together.

For example, the Direct Messages v1.1 endpoints provide methods for returning a single event and for deleting events. These methods are not yet available with v2. Since IDs are common across v1.1 and v2, you can make v1.1 requests based on IDs provided by v2, or by referencing conversation IDs displayed in conversation URLs on the Twitter application.    

### Including media attachments and referencing Tweets

The Manage Direct Message endpoints all support attaching one piece of media (photo, video, or GIF). Attaching media requires a media ID generated by the v1.1 [Upload media](https://developer.twitter.com/en/docs/twitter-api/v1/media/upload-media/overview) endpoint. The authenticated user posting the Direct Message must have also uploaded the media. Once uploaded, media is available for 24 hours for including with the message.   

To illustrate how to include media, the following is an example JSON request body:

      `{  "text": "Here's a photo...",  "attachments": [{"media_id": "1583157113245011970}] }`
    

The resulting MessageCreate event will include the following metadata:

      `{     "attachments": {         "media_keys": [             "5_1583157113245011970"         ]     } }`
    

Tweets can also be included by including the Tweet URL in the message text. To illustrate how to include Tweets in messages, the following is an example JSON request body:

      `{  "text": "Here's the Tweet I has talking about: https://twitter.com/SnowBotDev/status/1580559079470145536" }`
    

The resulting MessageCreate event will include the following metadata:

      `{     "referenced_tweets": [         {             "id": "1580559079470145536"         }     ] }`
    

### Authentication

All Twitter API v2 endpoints require for you to authenticate your requests with a set of credentials, also known as keys and tokens. All Direct Messages are private and require user authorization to access them. 

These Direct Message endpoints require the use of [OAuth 2.0 Authorization Flow with PKCE](https://developer.twitter.com/en/docs/twitter-api/tweets/manage-tweets/integrate#authentication) or [1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a), which means that you must use a set of API keys and user Access Tokens to make a successful request. The Access Tokens must be associated with the user that you are requesting on behalf of. If you want to generate a set of Access Tokens for another user, they must authorize or authenticate your App using the [3-legged OAuth flow](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens).

Please note that OAuth user-context can be tricky to use. If you are not familiar with this authentication method, we recommend using a [library](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries) or a tool like Postman to properly authenticate your requests. 

[OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code) allows for greater control over an application’s scope and authorization flows across multiple devices. OAuth 2.0 allows you to pick specific fine-grained scopes, which give you specific permissions on behalf of a user. The Direct Messages lookup endpoints require these scopes:  dm.write, dm.read, tweet.read, user.read.

To enable OAuth 2.0 in your App, you must enable it in your App’s authentication settings found in the App settings section of the developer portal.

### Developer portal, Projects, and developer Apps

To retrieve a set of authentication credentials that will work with the Twitter API v2 endpoints, you must have an approved developer account, set up a Project within that account, and create a developer App within that Project. You can then find your keys and tokens within your developer App. 

### Rate limits

Everyday many thousands of developers make requests to the Twitter API. To help manage the sheer volume of these requests, rate limits are placed on each endpoint that limits the number of requests that you can make on behalf of your app or on behalf of an authenticated user.   

The Manage Direct Message endpoints are rate limited at both the per-user and Twitter App levels. This means that the authenticated user that you are making the request on behalf of can only send a certain number of messages with your Twitter App. In addition, there is a daily limit on how many Direct Messages can be sent by your Twitter App.   

There is a user rate limit of 200 requests/messages per 15 minutes for the POST methods. Users are also limited to 1000 Direct Messages per 24 hours. In addition, Twitter Apps have a limit of 15000 messages per 24 hours. These rate limits are shared across the POST endpoints. 

Helpful tools
-------------

Here are some helpful tools we encourage you to explore as you work with the Direct Messages lookup endpoints: 

****Postman**  
**

Postman is a great tool that you can use to test out an endpoint. Each Postman request includes every path and body parameter to help you quickly understand what is available to you. To learn more about our Postman collections, please visit our [Using Postman](https://developer.twitter.com/en/docs/tutorials/postman-getting-started) page. 

****Code samples**  
**

Python sample code for the v2 Direct Messages endpoints is available in our Twitter API v2 sample code GitHub repository. The "Manage-Direct-Messages" folder contains examples for the POST methods, and the "Direct-Messages-lookup" folder contains examples for the GET methods.

****TwitterDev Software Development Kits (SDKs)**  
**

These [libraries](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview) are being updated for the v2 Direct Messages endpoints and should be ready soon:  

* [Twitter API Java SDK](https://github.com/twitterdev/twitter-api-java-sdk) - Official Java SDK for the Twitter API v2
* [Twitter API TypeScript/JavaScript SDK](https://github.com/twitterdev/twitter-api-typescript-sdk) - Official TS/JS SDK for the Twitter API v2

**Third-party libraries**  

There is a growing number of [third-party libraries](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/v2#community-libraries) developed by our community. These libraries are designed to help you get started, and several are expected to support v2 Direct Messages endpoints soon. You can find a library that works with the v2 endpoints by looking for the proper version tag.

Next steps
----------

[API reference](https://developer.twitter.com/en/docs/twitter-api/direct-messages/manage/api-reference "API reference")

Manage Direct Messages standard to Twitter API v2

Comparing v1.1 and v2 Manage Direct Message endpoints
-----------------------------------------------------

Both v1.1 and v2 versions of the Direct Messages endpoints provide methods for creating Direct Message messages. This guide is intended to help understand the differences and provide information for migrating to v2. 

A major difference between the two versions is that v1.1 supports only one-to-one conversations, while v2 introduces support for group conversations. One artifact of this is that v1.1 supports only "message created" events, while v2 also supports events associated with participants joining and leaving conversations. In fact, a fundamental v2 update is establishing dm\_conversations as a core API object.     

With v1.1. there are two endpoints for managing Direct Messages:  

* [POST direct\_messages/events/new](https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/sending-and-receiving/api-reference/new-event) \- Creates a one-to-one Direct Message. This v1.1 endpoint can only create one-to-one messages, and does not support group messages.  
    
* [DELETE direct\_messages/events/destroy](https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/sending-and-receiving/api-reference/delete-message-event) - Deletes a one-to-one message from the view of the authenticating user. 
    

With this v2 release, there are three POST methods for creating Direct Messages:   

* **POST /2/dm\_conversations/with/:participant\_id/messages** - Creates a one-to-one Direct Message. This method either adds the message to an existing one-to-one conversation or creates a new one. The :participant\_id path parameter is the User ID of the account receiving the message. 
    
* **POST /2/dm\_conversations** - Creates a new group conversation and adds a Direct Message to it. These requests require a list of conversation participants. Note that you can create multiple conversations with the same participant list. These requests will always return a new conversation ID. 
    
* **POST /2/dm\_conversations/:dm\_conversation\_id/messages** - Creates a Direct Message and adds it to an existing conversation. The :dm\_conversation\_id path parameter is the ID of the conversation that the message will be added to. 
    

An important detail is that conversation and event IDs are shared across v1.1 and v2 versions of the Twitter Platform. This means both versions can be used together. For example, the Direct Messages v1.1 endpoints provide methods for returning a single event and for deleting events, methods not yet available with v2. Since IDs are common across v1.1 and v2, you can make v1.1 requests based on IDs provided by v2, or by referencing conversation IDs displayed in conversation URLs on the Twitter application.  

The following table compares fundamental aspects of the v1.1 and v2 manage Direct Messages endpoints. The Twitter API v2 characteristics shared here are common to all of the Direct Message lookup endpoints.  

|     |     |     |
| --- | --- | --- |
| **Description** | **Standard v1.1** | **Twitter API v2** |
| Host domain | https://api.twitter.com | https://api.twitter.com |
| Endpoint root path | [/1.1/direct\_messages](https://api.twitter.com/1.1/direct_messages) | [/2/dm\_conversations](https://api.twitter.com/2/users/:id/dm_conversations)<br><br>Direct Messages conversations are introduced as a fundamental API object.   <br><br>These endpoints retrieve MessageCreate, ParticipantsJoin, and ParticipantLeave events. |
| HTTP methods supported | POST | POST |
| Supports Group Direct Messages |     | ✔   |
| Event types supported | message\_create | MessageCreate, ParticipantsJoin, ParticipantsLeave |
| [Authentication](https://developer.twitter.com/en/docs/authentication) | OAuth 1.0a User Context | OAuth 1.0a User Context<br><br>OAuth 2 User Context (scopes: dm.read, dm.write) |
| Requires the use of credentials from a [developer App](https://developer.twitter.com/en/docs/authentication) associated with a Twitter API v2 [Project](https://developer.twitter.com/en/docs/projects) |     | ✔   |
| Default request [rate limits](https://developer.twitter.com/en/docs/twitter-api/rate-limits)\*  <br>\*All requests require user tokens | 1000 requests per user per 24 hours  <br>15000 requests per app per 24 hours | 200 requests per 15 minutes per user<br><br>1000 requests per user per 24 hours<br><br>15000 requests per app per 24 hours<br><br>These rate limits are shared across all dm\_conversations POST endpoints. |

The following tables compare the v2 POST methods with version v1.1. Note that these v2 offerings expand the available capabilities by supporting group conversations. 

**Create a new one-to-one Direct Message**  

---------------------------------------------

Path: POST /2/dm\_conversations/with/:participant\_id/messages

|     |     |     |
| --- | --- | --- |
| **Description** | **Standard v1.1** | **Twitter API v2** |
| Endpoint path | POST direct\_messages/events/new (message\_create) | POST /2/dm\_conversations/with/:participant\_id/messages |
| Default request [rate limits](https://developer.twitter.com/en/docs/twitter-api/rate-limits) | 1000 requests per user per 24 hours  <br>15000 requests per app per 24 hours | 200 requests per 15 minutes per user<br><br>1000 requests per user per 24 hours<br><br>15000 requests per app per 24 hours<br><br>These rate limits are shared across all dm\_conversations POST endpoints. |
| Supports group Direct Messages |     | ✔   |

**Create a new Direct Message group conversation and add a message to it**  

Path: POST /2/dm\_conversations

|     |     |     |
| --- | --- | --- |
| **Description** | **Standard v1.1** | **Twitter API v2** |
| Endpoint path | Not supported | POST /2/dm\_conversations |
| Default request [rate limits](https://developer.twitter.com/en/docs/twitter-api/rate-limits) |     | 200 requests per 15 minutes per user<br><br>1000 requests per user per 24 hours<br><br>15000 requests per app per 24 hours<br><br>These rate limits are shared across all dm\_conversations POST endpoints. |
| Supports group Direct Messages |     | ✔   |

**Add a Direct Message to an existing conversation by ID**  

Path: POST /2/dm\_conversations/:dm\_conversation\_id/messages

|     |     |     |
| --- | --- | --- |
| **Description** | **Standard v1.1** | **Twitter API v2** |
| Endpoint path | Not supported | POST /2/dm\_conversations/:dm\_conversation\_id/messages |
| Default request [rate limits](https://developer.twitter.com/en/docs/twitter-api/rate-limits) |     | 200 requests per 15 minutes per user<br><br>1000 requests per user per 24 hours<br><br>15000 requests per app per 24 hours<br><br>These rate limits are shared across all dm\_conversations POST endpoints. |
| Supports group Direct Messages |     | ✔   |

Next steps
----------

[API reference](https://developer.twitter.com/en/docs/twitter-api/direct-messages/manage "API reference")

API reference

API reference index
-------------------

For the complete API reference, select an endpoint from the list:  
  

### Manage Direct Messages

|     |     |     |
| --- | --- | --- |
| **Create a message in a 1-1 conversation with the participant** | [POST /2/dm\_conversations/with/:participant\_id/messages](https://developer.twitter.com/en/docs/twitter-api/direct-messages/manage/api-reference/post-dm_conversations-with-participant_id-messages) |     |
| **Create a group conversation and add a DM to it** | [POST /2/dm\_conversations/](https://developer.twitter.com/en/docs/twitter-api/direct-messages/manage/api-reference/post-dm_conversations) |     |
| **Adding a DM to an existing conversation (for both group and 1-1)** | [POST /2/dm\_conversations/:dm\_conversation\_id/messages](https://developer.twitter.com/en/docs/twitter-api/direct-messages/manage/api-reference/post-dm_conversations-dm_conversation_id-messages) |     |

POST /2/dm\_conversations/:dm\_conversation\_id/messages

POST /2/dm\_conversations/:dm\_conversation\_id/messages
========================================================

Creates a Direct Message on behalf of an authenticated user, and adds it to the specified conversation.

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Try a live request ❯](https://oauth-playground.glitch.me/?id=dmConversationByIdEventIdCreate) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Fdm_conversations%2F%7Bdm_conversation_id%7D%2Fmessages&method=post) 

### Endpoint URL

`https://api.twitter.com/2/dm_conversations/:dm_conversation_id/messages`  
  

### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 2.0 App-only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only "Use this method to obtain information in the context of an unauthenticated public user. This method is for developers that just need read-only access to public information. Click to learn how to obtain an OAuth 2.0 App Access Token.")<br><br>[OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code "This method allows an authorized app to act on behalf of the user, as the user. It is typically used to access or post public information for a specific user, and it us useful when your app needs to be aware of the relationship between a user and what this endpoint returns. Click to learn how to authenticate with OAuth 2.0 Authorization Code with PKCE.")<br><br>[OAuth 1.0a](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) is also available for this endpoint. |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | User rate limit (User context): 200 requests per 15-minute window per each authenticated user<br><br>App rate limit (Application-only): 15000 requests per 24-hour window shared among all users of your app |

### OAuth 2.0 scopes required by this endpoint

|     |
| --- |
| `dm.write`<br><br>`dm.read`<br><br>`tweet.read`<br><br>`users.read` |
| [Learn more about OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/twitter-api/oauth2) |

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `dm_conversation_id`  <br> Required | string | The `dm_conversation_id` of the conversation to add the Direct Message to. Supports both 1-1 and group conversations. |

  
  

### JSON body parameters

| Name | Type | Description |
| --- | --- | --- |
| `attachments`  <br> Optional | array | A single Media ID being attached to the Direct Message. This field is required if `text` is not present. For this launch, only 1 attachment is supported.  <br>  <br>Example: `{"text": "Sending a DM with media!", "attachments": [{"media_id": "1455952740635586573"}]` |
| `text`  <br> Optional | string | Text of the Direct Message being created. This field is required if `attachments` is not present. Text messages support up to 10,000 characters.  <br>  <br>Example: `{"text": "Hello just you conversation participants!""}` |

  
  

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [cURL](#tab0)

cURL

      `curl -X POST "https://api.twitter.com/2/dm_conversations/:dm_conversation_id/messages" -d '{"text": "Adding a Direct Message to a conversation by referencing the conversation ID. This method supports both one-to-one and group conversations."}' -H "Authorization: Bearer $ACCESS_TOKEN"`
    

### Example responses

* [Successful response](#tab0)

Successful response

      `{   "dm_conversation_id": "1346889436626259968",   "dm_event_id": "128341038123" }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `dm_conversation_id` | string | Contains the `id` of the Direct Message conversation the Direct Message was added to. |
| `dm_event_id` | string | Contains the `id` of the event created by this request. |

POST /2/dm\_conversations/with/:participant\_id/messages

POST /2/dm\_conversations/with/:participant\_id/messages
========================================================

Creates a one-to-one Direct Message and adds it to the one-to-one conversation. This method either creates a new one-to-one conversation or retrieves the current conversation and adds the Direct Message to it.

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Try a live request ❯](https://oauth-playground.glitch.me/?id=dmConversationWithUserEventIdCreate) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Fdm_conversations%2Fwith%2F%7Bparticipant_id%7D%2Fmessages&method=post) 

### Endpoint URL

`https://api.twitter.com/2/dm_conversations/with/:participant_id/messages`  
  

### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 1.0a](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) is also available for this endpoint.<br><br>[OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code "This method allows an authorized app to act on behalf of the user, as the user. It is typically used to access or post public information for a specific user, and it us useful when your app needs to be aware of the relationship between a user and what this endpoint returns. Click to learn how to authenticate with OAuth 2.0 Authorization Code with PKCE.")<br><br>[OAuth 2.0 App-only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only "Use this method to obtain information in the context of an unauthenticated public user. This method is for developers that just need read-only access to public information. Click to learn how to obtain an OAuth 2.0 App Access Token.") |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | User rate limit (User context): 200 requests per 15-minute window per each authenticated user<br><br>App rate limit (Application-only): 15000 requests per 24-hour window shared among all users of your app |

### OAuth 2.0 scopes required by this endpoint

|     |
| --- |
| `dm.write`<br><br>`dm.read`<br><br>`tweet.read`<br><br>`users.read` |
| [Learn more about OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/twitter-api/oauth2) |

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `participant_id`  <br> Required | string | The User ID of the account this one-to-one Direct Message is to be sent to. |

  
  

### JSON body parameters

| Name | Type | Description |
| --- | --- | --- |
| `attachments`  <br> Optional | array | A single Media ID being attached to the Direct Message. This field is required if `text` is not present. For this launch, only 1 attachment is supported.  <br>  <br>Example: `{"text": "Sending a DM with media!", "attachments": [{"media_id": "1455952740635586573"}]` |
| `text`  <br> Optional | string | Text of the Direct Message being created. This field is required if `attachments` is not present. Text messages support up to 10,000 characters.  <br>  <br>Example: `{"text": "Hello just you"}` |

  
  

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [cURL](#tab0)

cURL

      `curl -X POST "https://api.twitter.com/2/dm_conversations/with/:participant_id/messages" -d '{"text": "This is a one-to-one Direct Message with an attachment","attachments": [{"media_id": "1455952740635586573"}]}' -H "Authorization: Bearer $ACCESS_TOKEN"`
    

### Example responses

* [Successful response](#tab0)

Successful response

      `{   "dm_conversation_id": "1346889436626259968",   "dm_event_id": "128341038123" }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `dm_conversation_id` | string | Contains the `id` of the Direct Message conversation the Direct Message was added to. |
| `dm_event_id` | string | Contains the `id` of the event created by this request. |

POST /2/dm\_conversations

POST /2/dm\_conversations
=========================

Creates a new group conversation and adds a Direct Message to it on behalf of an authenticated user.

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Try a live request ❯](https://oauth-playground.glitch.me/?id=dmConversationIdCreate) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Fdm_conversations&method=post) 

### Endpoint URL

`https://api.twitter.com/2/dm_conversations`  
  

### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 1.0a](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) is also available for this endpoint.<br><br>[OAuth 2.0 App-only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only "Use this method to obtain information in the context of an unauthenticated public user. This method is for developers that just need read-only access to public information. Click to learn how to obtain an OAuth 2.0 App Access Token.")<br><br>[OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code "This method allows an authorized app to act on behalf of the user, as the user. It is typically used to access or post public information for a specific user, and it us useful when your app needs to be aware of the relationship between a user and what this endpoint returns. Click to learn how to authenticate with OAuth 2.0 Authorization Code with PKCE.") |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | User rate limit (User context): 200 requests per 15-minute window per each authenticated user<br><br>App rate limit (Application-only): 15000 requests per 24-hour window shared among all users of your app |

### OAuth 2.0 scopes required by this endpoint

|     |
| --- |
| `dm.write`<br><br>`dm.read`<br><br>`tweet.read`<br><br>`users.read` |
| [Learn more about OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/twitter-api/oauth2) |

### JSON body parameters

| Name | Type | Description |
| --- | --- | --- |
| `conversation_type`  <br> Required | string | The `conversation_type` attribute must be set to "Group" (case sensitive).  <br>  <br>Example: `{"conversation_type": "Group"}` |
| `message`  <br> Required | object | A JSON object that contains either or both the `text` and `attachments` parameters.  <br>  <br>Example: `{"message": {text": "Hello just you conversation participants!"}}` |
| `participant_ids`  <br> Required | array | An array of User IDs that the conversation is created with. Conversations can have up to 50 participants.  <br>  <br>Example: `{"participant_ids": ["944480690","906948460078698496"]}` |
| `message.attachments`  <br> Optional | array | A single Media ID being attached to the Direct Message. This field is required if `message.text` is not present. For this launch, only 1 attachment is supported.  <br>  <br>Example: `{"message": {"text": "Sending a DM with media!", "attachments": [{"media_id": "1455952740635586573"}]}` |
| `message.text`  <br> Optional | string | Text of the Direct Message being created. This field is required if `message.attachments` is not present. Text messages support up to 10,000 characters.  <br>  <br>Example: `{"message": {"text": "Hello just you conversation participants!"}}` |

  
  

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [cURL](#tab0)

cURL

      `curl -X POST "https://api.twitter.com/2/dm_conversations" -d '{"conversation_type":"Group", "participant_ids": ["944480690", "906948460078698496"],"message": {"text": "Hello to you two, this is a new group conversation"}}' -H "Authorization: Bearer $ACCESS_TOKEN"`
    

### Example responses

* [Successful response](#tab0)

Successful response

      `{   "dm_conversation_id": "1346889436626259968",   "dm_event_id": "128341038123" }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `dm_conversation_id` | string | Contains `id` of the DM conversation. |
| `dm_event_id` | string | Contains `id` of the event sent in this conversation. |