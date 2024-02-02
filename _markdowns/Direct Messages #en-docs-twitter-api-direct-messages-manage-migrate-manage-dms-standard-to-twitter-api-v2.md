::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Both v1.1 and v2 versions of the Direct Messages endpoints provide
methods for creating Direct Message messages. This guide is intended to
help understand the differences and provide information for migrating to
v2.

A major difference between the two versions is that v1.1 supports only
one-to-one conversations, while v2 introduces support for group
conversations. One artifact of this is that v1.1 supports only \"message
created\" events, while v2 also supports events associated with
participants joining and leaving conversations. In fact, a fundamental
v2 update is establishing dm_conversations as a core API object. \

With v1.1. there are two endpoints for managing Direct Messages: \

With this v2 release, there are three POST methods for creating Direct
Messages: \

-   **POST /2/dm_conversations/with/:participant_id/messages** - Creates
    a one-to-one Direct Message. This method either adds the message to
    an existing one-to-one conversation or creates a new one. The [
    :participant_id ]{.code-inline} path parameter is the User ID of the
    account receiving the message.

-   **POST /2/dm_conversations** - Creates a new group conversation and
    adds a Direct Message to it. These requests require a list of
    conversation participants. Note that you can create multiple
    conversations with the same participant list. These requests will
    always return a new conversation ID.

-   **POST /2/dm_conversations/:dm_conversation_id/messages** - Creates
    a Direct Message and adds it to an existing conversation. The [
    :dm_conversation_id ]{.code-inline} path parameter is the ID of the
    conversation that the message will be added to.

An important detail is that conversation and event IDs are shared across
v1.1 and v2 versions of the Twitter Platform. This means both versions
can be used together. For example, the Direct Messages v1.1 endpoints
provide methods for returning a single event and for deleting events,
methods not yet available with v2. Since IDs are common across v1.1 and
v2, you can make v1.1 requests based on IDs provided by v2, or by
referencing conversation IDs displayed in conversation URLs on the
Twitter application. \

The following table compares fundamental aspects of the v1.1 and v2
manage Direct Messages endpoints. The Twitter API v2 characteristics
shared here are common to all of the Direct Message lookup endpoints. \
:::
:::

::: c01-rich-text-editor
::: is-table-default
+-----------------------+-----------------------+-----------------------+
| **Description**       | **Standard v1.1**     | **Twitter API v2**    |
+-----------------------+-----------------------+-----------------------+
| Host domain           | [                     | [                     |
|                       | ht                    | ht                    |
|                       | tps://api.twitter.com | tps://api.twitter.com |
|                       | ]{.code-inline}       | ]{.code-inline}       |
+-----------------------+-----------------------+-----------------------+
| Endpoint root path    | [/1.                  | [/2/dm_conve          |
|                       | 1/direct_messages](ht | rsations](https://api |
|                       | tps://api.twitter.com | .twitter.com/2/users/ |
|                       | /1.1/direct_messages) | :id/dm_conversations) |
|                       |                       |                       |
|                       |                       | Direct Messages       |
|                       |                       | conversations are     |
|                       |                       | introduced as a       |
|                       |                       | fundamental API       |
|                       |                       | object. \             |
|                       |                       |                       |
|                       |                       | These endpoints       |
|                       |                       | retrieve [            |
|                       |                       | MessageCreate         |
|                       |                       | ]{.code-inline} , [   |
|                       |                       | ParticipantsJoin      |
|                       |                       | ]{.code-inline} , and |
|                       |                       | [ ParticipantLeave    |
|                       |                       | ]{.code-inline}       |
|                       |                       | events.               |
+-----------------------+-----------------------+-----------------------+
| HTTP methods          | POST                  | POST                  |
| supported             |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Supports Group Direct |                       | ✔                     |
| Messages              |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Event types supported | [ message_create      | [ MessageCreate       |
|                       | ]{.code-inline}       | ]{.code-inline} , [   |
|                       |                       | ParticipantsJoin      |
|                       |                       | ]{.code-inline} , [   |
|                       |                       | ParticipantsLeave     |
|                       |                       | ]{.code-inline}       |
+-----------------------+-----------------------+-----------------------+
| [Authentication](/en  | OAuth 1.0a User       | OAuth 1.0a User       |
| /docs/authentication) | Context               | Context               |
|                       |                       |                       |
|                       |                       | OAuth 2 User Context  |
|                       |                       | (scopes: [ dm.read    |
|                       |                       | ]{.code-inline} , [   |
|                       |                       | dm.write              |
|                       |                       | ]{.code-inline} )     |
+-----------------------+-----------------------+-----------------------+
| Requires the use of   |                       | ✔                     |
| credentials from a    |                       |                       |
| [developer            |                       |                       |
| App](/en              |                       |                       |
| /docs/authentication) |                       |                       |
| associated with a     |                       |                       |
| Twitter API v2        |                       |                       |
| [Projec               |                       |                       |
| t](/en/docs/projects) |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Default request [rate | 1000 requests per     | 200 requests per 15   |
| limits](/en/docs/twi  | user per 24 hours\    | minutes per user      |
| tter-api/rate-limits) | 15000 requests per    |                       |
| \*\                   | app per 24 hours      | 1000 requests per     |
| \*All requests        |                       | user per 24 hours     |
| require user tokens   |                       |                       |
|                       |                       | 15000 requests per    |
|                       |                       | app per 24 hours      |
|                       |                       |                       |
|                       |                       | These rate limits are |
|                       |                       | shared across all     |
|                       |                       | dm_conversations POST |
|                       |                       | endpoints.            |
+-----------------------+-----------------------+-----------------------+
:::
:::

::: c01-rich-text-editor
::: is-table-default
The following tables compare the v2 POST methods with version v1.1. Note
that these v2 offerings expand the available capabilities by supporting
group conversations.

##  **Create a new one-to-one Direct Message**  

Path: POST /2/dm_conversations/with/:participant_id/messages
:::
:::

::: c01-rich-text-editor
::: is-table-default
+-----------------------+-----------------------+-----------------------+
| **Description**       | **Standard v1.1**     | **Twitter API v2**    |
+-----------------------+-----------------------+-----------------------+
| Endpoint path         | POST                  | POST                  |
|                       | direc                 | /2/dm_c               |
|                       | t_messages/events/new | onversations/with/:pa |
|                       | (message_create)      | rticipant_id/messages |
+-----------------------+-----------------------+-----------------------+
| Default request [rate | 1000 requests per     | 200 requests per 15   |
| limits](/en/docs/twi  | user per 24 hours\    | minutes per user      |
| tter-api/rate-limits) | 15000 requests per    |                       |
|                       | app per 24 hours      | 1000 requests per     |
|                       |                       | user per 24 hours     |
|                       |                       |                       |
|                       |                       | 15000 requests per    |
|                       |                       | app per 24 hours      |
|                       |                       |                       |
|                       |                       | These rate limits are |
|                       |                       | shared across all     |
|                       |                       | dm_conversations POST |
|                       |                       | endpoints.            |
+-----------------------+-----------------------+-----------------------+
| Supports group Direct |                       | ✔                     |
| Messages              |                       |                       |
+-----------------------+-----------------------+-----------------------+
:::
:::

::: c01-rich-text-editor
::: is-table-default
**Create a new Direct Message group conversation and add a message to
it**\

Path: POST /2/dm_conversations
:::
:::

::: c01-rich-text-editor
::: is-table-default
+-----------------------+-----------------------+-----------------------+
| **Description**       | **Standard v1.1**     | **Twitter API v2**    |
+-----------------------+-----------------------+-----------------------+
| Endpoint path         | Not supported         | POST                  |
|                       |                       | /2/dm_conversations   |
+-----------------------+-----------------------+-----------------------+
| Default request [rate |                       | 200 requests per 15   |
| limits](/en/docs/twi  |                       | minutes per user      |
| tter-api/rate-limits) |                       |                       |
|                       |                       | 1000 requests per     |
|                       |                       | user per 24 hours     |
|                       |                       |                       |
|                       |                       | 15000 requests per    |
|                       |                       | app per 24 hours      |
|                       |                       |                       |
|                       |                       | These rate limits are |
|                       |                       | shared across all     |
|                       |                       | dm_conversations POST |
|                       |                       | endpoints.            |
+-----------------------+-----------------------+-----------------------+
| Supports group Direct |                       | ✔                     |
| Messages              |                       |                       |
+-----------------------+-----------------------+-----------------------+
:::
:::

::: c01-rich-text-editor
::: is-table-default
**Add a Direct Message to an existing conversation by ID**\

Path: POST /2/dm_conversations/:dm_conversation_id/messages
:::
:::

::: c01-rich-text-editor
::: is-table-default
+-----------------------+-----------------------+-----------------------+
| **Description**       | **Standard v1.1**     | **Twitter API v2**    |
+-----------------------+-----------------------+-----------------------+
| Endpoint path         | Not supported         | POST                  |
|                       |                       | /2/dm_                |
|                       |                       | conversations/:dm_con |
|                       |                       | versation_id/messages |
+-----------------------+-----------------------+-----------------------+
| Default request [rate |                       | 200 requests per 15   |
| limits](/en/docs/twi  |                       | minutes per user      |
| tter-api/rate-limits) |                       |                       |
|                       |                       | 1000 requests per     |
|                       |                       | user per 24 hours     |
|                       |                       |                       |
|                       |                       | 15000 requests per    |
|                       |                       | app per 24 hours      |
|                       |                       |                       |
|                       |                       | These rate limits are |
|                       |                       | shared across all     |
|                       |                       | dm_conversations POST |
|                       |                       | endpoints.            |
+-----------------------+-----------------------+-----------------------+
| Supports group Direct |                       | ✔                     |
| Messages              |                       |                       |
+-----------------------+-----------------------+-----------------------+
:::
:::
:::
