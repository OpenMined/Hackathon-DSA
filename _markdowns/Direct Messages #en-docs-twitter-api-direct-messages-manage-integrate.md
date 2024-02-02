::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
The Direct Messages endpoints v2 introduce conversations and
conversation events as core Twitter API objects, and makes a distinction
between one-to-one and group conversations. One-to-one conversations
always have two, and only two, participants, while group conversations
can have two or more and memberships that can change.

This page contains information on several tools and key concepts that
you should be aware of as you integrate the Manage Direct Messages
endpoints into your system. We've broken the page into two sections:

## Key Concepts

### []{#direct-message-conversations} Direct Message conversations

All Direct Messages are part of a Direct Message conversation. These
conversations can be one-to-one conversations or group conversations.
This launch provides the foundational endpoints needed to create Direct
Messages and retrieve events associated with Direct Message
conversations. All conversations have a unique dm_conversation_id, and
the events that make up that conversation all have a unique dm_event_id.

The Manage Direct Message endpoints provide three POST methods for
creating new messages and adding them to conversations:
:::
:::

::: c01-rich-text-editor
-   **POST /2/dm_conversations/with/:participant_id/messages** - Creates
    a one-to-one Direct Message. This method either adds the message to
    an existing one-to-one conversation or creates a new one. The
    :participant_id path parameter is the User ID of the account
    receiving the message.\
    Here is an example JSON request body for sending a one-to-one Direct
    Message:
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {
   "text": "Hello just you. This will appear as a new conversation if we have never messaged, or will be added to our existing thread. "
}

    
```
:::
:::
:::

::: c01-rich-text-editor
-   **POST /2/dm_conversations**  - Creates a new group conversation and
    adds a Direct Message to it. These requests require a list of
    conversation participants. Note that you can create multiple
    conversations with the same participant list. These requests will
    always return a new conversation ID.\
    Below is an example JSON request body for creating a new group
    conversation and adding a Direct Message. Note that this requires a
    [ \"conversation_type\" ]{.code-inline} field and that must be set
    to \"Group\" (case sensitive).
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {
   "message": {"text": "Hello to just you two, this is a new group conversation."},
   "participant_ids": ["944480690","906948460078698496"],
   "conversation_type": "Group"       
}

    
```
:::
:::
:::

::: c01-rich-text-editor
-   **POST /2/dm_conversations/:dm_conversation_id/messages** - Creates
    a Direct Message and adds it to an existing conversation. The [
    :dm_conversation_id ]{.code-inline} path parameter is the ID of the
    conversation that the message will be added to. This method can be
    used to add a message to both one-to-one and group conversations.\
    Here is an example JSON request body for sending Direct Message to
    both one-to-one and group conversations:
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {
   "text": "Here is a new message."
}

    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
These POST methods support attaching a single piece of media. POST
request bodies must include either or both the \"text\" and
\"attachments\" fields. The \"text\" attribute is required if the
\"attachments\" field is not included, and the \"attachments\" field is
required if the \"text\" field is not included. See the next section for
more information.

For more information see the [Manage Direct Messages API
References](/en/docs/twitter-api/direct-messages/manage/api-reference) .
\

### []{#shared-conversation-and-event-ids} Shared conversation and event IDs across v1.1 and v2

An important concept is that conversation and event IDs are shared
across v1.1 and v2 versions of the Twitter Platform. This means both
versions can be used together.

For example, the Direct Messages v1.1 endpoints provide methods for
returning a single event and for deleting events. These methods are not
yet available with v2. Since IDs are common across v1.1 and v2, you can
make v1.1 requests based on IDs provided by v2, or by referencing
conversation IDs displayed in conversation URLs on the Twitter
application. \

### []{#including-media-attachments-and-referencing-tweets} Including media attachments and referencing Tweets

The Manage Direct Message endpoints all support attaching one piece of
media (photo, video, or GIF). Attaching media requires a media ID
generated by the v1.1 [Upload
media](/en/docs/twitter-api/v1/media/upload-media/overview) endpoint.
The authenticated user posting the Direct Message must have also
uploaded the media. Once uploaded, media is available for 24 hours for
including with the message. \

To illustrate how to include media, the following is an example JSON
request body:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {
 "text": "Here's a photo...",
 "attachments": [{"media_id": "1583157113245011970}]
}

    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
The resulting MessageCreate event will include the following metadata:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {
    "attachments": {
        "media_keys": [
            "5_1583157113245011970"
        ]
    }
}

    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
Tweets can also be included by including the Tweet URL in the message
text. To illustrate how to include Tweets in messages, the following is
an example JSON request body:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {
 "text": "Here's the Tweet I has talking about: https://twitter.com/SnowBotDev/status/1580559079470145536"
}

    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
The resulting MessageCreate event will include the following metadata:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {
    "referenced_tweets": [
        {
            "id": "1580559079470145536"
        }
    ]
}

    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
All Twitter API v2 endpoints require for you to authenticate your
requests with a set of credentials, also known as keys and tokens. All
Direct Messages are private and require user authorization to access
them.

These Direct Message endpoints require the use of [OAuth 2.0
Authorization Flow with
PKCE](/en/docs/twitter-api/tweets/manage-tweets/integrate#authentication)
or [1.0a User Context](/en/docs/authentication/oauth-1-0a) , which means
that you must use a set of API keys and user Access Tokens to make a
successful request. The Access Tokens must be associated with the user
that you are requesting on behalf of. If you want to generate a set of
Access Tokens for another user, they must authorize or authenticate your
App using the [3-legged OAuth
flow](/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens) .

Please note that OAuth user-context can be tricky to use. If you are not
familiar with this authentication method, we recommend using a
[library](/en/docs/twitter-api/tools-and-libraries) or a tool like
Postman to properly authenticate your requests.

[OAuth 2.0 Authorization Code with
PKCE](/en/docs/authentication/oauth-2-0/authorization-code) allows for
greater control over an application's scope and authorization flows
across multiple devices. OAuth 2.0 allows you to pick specific
fine-grained scopes, which give you specific permissions on behalf of a
user. The Direct Messages lookup endpoints require these scopes: [
dm.write ]{.code-inline} , [ dm.read ]{.code-inline} , [ tweet.read
]{.code-inline} , [ user.read ]{.code-inline} .

To enable OAuth 2.0 in your App, you must enable it in your App's
authentication settings found in the App settings section of the
developer portal.

### []{#developer-portal-projects-and-developer-apps} Developer portal, Projects, and developer Apps

To retrieve a set of authentication credentials that will work with the
Twitter API v2 endpoints, you must have an approved developer account,
set up a Project within that account, and create a developer App within
that Project. You can then find your keys and tokens within your
developer App.

### []{#rate-limits} Rate limits

Everyday many thousands of developers make requests to the Twitter API.
To help manage the sheer volume of these requests, rate limits are
placed on each endpoint that limits the number of requests that you can
make on behalf of your app or on behalf of an authenticated user. \

The Manage Direct Message endpoints are rate limited at both the
per-user and Twitter App levels. This means that the authenticated user
that you are making the request on behalf of can only send a certain
number of messages with your Twitter App. In addition, there is a daily
limit on how many Direct Messages can be sent by your Twitter App. \

There is a user rate limit of 200 requests/messages per 15 minutes for
the POST methods. Users are also limited to 1000 Direct Messages per 24
hours. In addition, Twitter Apps have a limit of 15000 messages per 24
hours. These rate limits are shared across the POST endpoints.

## []{#helpful-tools} Helpful tools

Here are some helpful tools we encourage you to explore as you work with
the Direct Messages lookup endpoints:

** **Postman** \
**

Postman is a great tool that you can use to test out an endpoint. Each
Postman request includes every path and body parameter to help you
quickly understand what is available to you. To learn more about our
Postman collections, please visit our [Using
Postman](https://developer.twitter.com/en/docs/tutorials/postman-getting-started)
page.

** **Code samples** \
**

Python sample code for the v2 Direct Messages endpoints is available in
our Twitter API v2 sample code GitHub repository. The
\"Manage-Direct-Messages\" folder contains examples for the POST
methods, and the \"Direct-Messages-lookup\" folder contains examples for
the GET methods.

** **TwitterDev Software Development Kits (SDKs)** \
**

These
[libraries](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)
are being updated for the v2 Direct Messages endpoints and should be
ready soon: \

**Third-party libraries** \

There is a growing number of [third-party
libraries](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/v2#community-libraries)
developed by our community. These libraries are designed to help you get
started, and several are expected to support v2 Direct Messages
endpoints soon. You can find a library that works with the v2 endpoints
by looking for the proper version tag.
:::
:::
:::
