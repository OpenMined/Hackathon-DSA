::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Both v1.1 and v2 versions of the Direct Messages endpoints provide
methods for looking up Direct Message events. This guide is intended to
help understand the differences and provide information for migrating to
v2.

A major difference between the two versions is that v1.1 supports only
one-to-one conversations, while v2 introduces support for group
conversations. One artifact of this is that v1.1 supports only \"message
created\" events, while v2 also supports events associated with
participants joining and leaving conversations. In fact, a fundamental
v2 update is establishing dm_conversations as a core API object. \

With v1.1. there are two endpoints for retrieving Direct Messages
(again, new messages are the only event type supported with v1.1): \

With this v2 release, there are three GET methods for retrieving Direct
Message conversation events: \

-   **GET /2/dm_conversations/with/:participant_id/dm_events** -
    Retrieves Direct Message events associated with a one-to-one
    conversation. The :participant_id path parameter is the User ID of
    the account having the conversation with the authenticated user
    making this request.

-   **GET /2/dm_conversations/:dm_conversation_id/dm_events** -
    Retrieves Direct Message events associated with a specific
    conversation ID, as indicated by the :dm_conversation_id path
    parameter. This method supports both one-to-one and group
    conversations.

-   **GET /2/dm_events** - Retrieves Direct Message events associated
    with a user, including both one-to-one and group conversations.
    Events from up to 30 days ago are available.

An important detail is that conversation and event IDs are shared across
v1.1 and v2 versions of the Twitter Platform. This means both versions
can be used together. For example, the Direct Messages v1.1 endpoints
provide methods for returning a single event and for deleting events,
methods not yet available with v2. Since IDs are common across v1.1 and
v2, you can make v1.1 requests based on IDs provided by v2, or by
referencing conversation IDs displayed in conversation URLs on the
Twitter application.

The following table compares fundamental aspects of the v1.1 and v2
Direct Message event lookup endpoints. The Twitter API v2
characteristics shared here are common to all of the Direct Message
lookup endpoints.
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
| HTTP methods          | GET                   | GET                   |
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
|                       |                       | tweet.read            |
|                       |                       | ]{.code-inline} , [   |
|                       |                       | user.read             |
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
| Default request [rate |                       | GET requests: 300     |
| limits](/en/docs/twi  |                       | requests per 15 mins  |
| tter-api/rate-limits) |                       |                       |
| \*\                   |                       | Rate limit is applied |
| \*All requests        |                       | across all three      |
| require user tokens   |                       | endpoints             |
+-----------------------+-----------------------+-----------------------+
:::
:::

::: c01-rich-text-editor
::: is-table-default
The following tables compare the v2 GET methods with version v1.1. Note
that these v2 offerings expand the available capabilities by supporting
group conversations.

##  **Get all messages in a specific one-to-one conversation**  

Path: GET /2/dm_conversations/with/:participant_id/dm_events
:::
:::

::: c01-rich-text-editor
::: is-table-default
+-----------------------+-----------------------+-----------------------+
| **Description**       | **Standard v1.1**     | **Twitter API v2**    |
+-----------------------+-----------------------+-----------------------+
| Endpoint path         | GET                   | GET                   |
|                       |                       | /2/dm_co              |
|                       | /1.1/direct           | nversations/with/:par |
|                       | _messages/events/list | ticipant_id/dm_events |
+-----------------------+-----------------------+-----------------------+
| How much event        | 30 days               | No limit              |
| history is available  |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Default request [rate | 15 requests per 15    | 300 requests per 15   |
| limits](/en/docs/twi  | minutes               | minutes\              |
| tter-api/rate-limits) |                       | Rate limit is applied |
|                       |                       | across all three GET  |
|                       |                       | endpoints             |
+-----------------------+-----------------------+-----------------------+
:::
:::

::: c01-rich-text-editor
::: is-table-default
**Get all messages by conversation ID**\

Path: GET /2/dm_conversations/:dm_conversation_id/dm_events
:::
:::

::: c01-rich-text-editor
::: is-table-default
+-----------------------+-----------------------+-----------------------+
| **Description**       | **Standard v1.1**     | **Twitter API v2**    |
+-----------------------+-----------------------+-----------------------+
| Endpoint path         | Not supported. V1.1   | GET                   |
|                       | can return messages   | /2/dm_c               |
|                       | from one-to-one       | onversations/:dm_conv |
|                       | conversations only    | ersation_id/dm_events |
|                       | and there is no       |                       |
|                       | support for           |                       |
|                       | retrieving events by  |                       |
|                       | conversation IDs.     |                       |
+-----------------------+-----------------------+-----------------------+
| How much event        | 30 days               | No limit              |
| history is available  |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Supports group        |                       | ✔                     |
| conversations         |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Default request [rate | 15 requests per 15    | 300 requests per 15   |
| limits](/en/docs/twi  | minutes               | minutes\              |
| tter-api/rate-limits) |                       | Rate limit is applied |
|                       |                       | across all three GET  |
|                       |                       | endpoints             |
+-----------------------+-----------------------+-----------------------+
|                       |                       |                       |
+-----------------------+-----------------------+-----------------------+
:::
:::

::: c01-rich-text-editor
::: is-table-default
**Get all events across an authenticated user\'s conversations, both
one-to-one and group conversations**\

Path: GET /2/dm_events
:::
:::

::: c01-rich-text-editor
::: is-table-default
+-----------------------+-----------------------+-----------------------+
| **Description**       | **Standard v1.1**     | **Twitter API v2**    |
+-----------------------+-----------------------+-----------------------+
| Endpoint path         | GET                   | GET /2/dm_events      |
|                       | /1.1/direct           |                       |
|                       | _messages/events/list |                       |
|                       |                       |                       |
|                       | V1.1 can return       |                       |
|                       | messages from         |                       |
|                       | one-to-one            |                       |
|                       | conversations only.   |                       |
+-----------------------+-----------------------+-----------------------+
| How much event        | 30 days               | 30 days               |
| history is available  |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Supports group        |                       | ✔                     |
| conversations         |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Default request [rate | 15 requests per 15    | 300 requests per 15   |
| limits](/en/docs/twi  | minutes               | minutes\              |
| tter-api/rate-limits) |                       | Rate limit is applied |
|                       |                       | across all three GET  |
|                       |                       | endpoints             |
+-----------------------+-----------------------+-----------------------+
|                       |                       |                       |
+-----------------------+-----------------------+-----------------------+
:::
:::
:::
