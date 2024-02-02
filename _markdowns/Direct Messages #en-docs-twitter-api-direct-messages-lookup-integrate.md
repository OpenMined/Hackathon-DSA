::: is-table-default
The Direct Messages endpoints v2 introduce conversations and
conversation events as core Twitter API objects, and make a distinction
between 1-1 and group conversations. 1-1 conversations always have two,
and only two, participants, while group conversations can have two or
more and memberships that can change.

This page contains information on several tools and key concepts that
you should be aware of as you integrate the Direct Messages lookup
endpoints into your system. We've broken the page into two sections:

### Key Concepts

### []{#direct-message-conversations} Direct Message conversations

All Direct Messages are part of a Direct Message conversation. These
conversations can be one-to-one conversations or group conversations.
This launch provides the foundational endpoints needed to create Direct
Messages and retrieve events associated with Direct Message
conversations. All conversations have a unique [ dm_conversation_id
]{.code-inline} , and the events that make up that conversation all have
a unique [ dm_event_id ]{.code-inline} .

The Direct Message lookup endpoints provide methods for retrieving
events associated with conversations. These GET endpoints are used to
retrieve the messages that make up a conversation, and for group
conversations, can be used to understand who has joined and left group
conversations. \

This initial release of Direct Messages lookup includes three GET
methods:

-   **GET /2/dm_conversations/with/:participant_id/dm_events** -
    Retrieves Direct Message events associated with a one-to-one
    conversation. The [ :participant_id ]{.code-inline} path parameter
    is the numeric User ID of the account having the conversation with
    the authenticated user making this request.

-   **GET /2/dm_conversations/:dm_conversation_id/dm_events** -
    Retrieves Direct Message events associated with a specific
    conversation ID, as indicated by the [ :dm_conversation_id
    ]{.code-inline} path parameter. Both one-to-one and group
    conversations IDs are supported.

-   **GET /2/dm_events** - Retrieves Direct Message events associated
    with the authenticating user, including both one-to-one and group
    conversations. Events from up to 30 days ago are available.

These GET endpoints all support retrieving [ dm_events ]{.code-inline}
by event type with an [ event_types ]{.code-inline} request query
parameters. Currently, there are three conversation event types
supported: \

-   **MessageCreate** - Created when a new Direct Message is created.
    This event object can include the time and text of the message,
    along with the account ID of who sent the message, and the
    conversation and event IDs.

-   **ParticipantsJoin** - Created when a new participant joins a group
    conversation. This [ dm_event ]{.code-inline} object includes the ID
    of the participant joining, along with the created_at time and the
    sender_id of the \'invite\' event.

-   **ParticipantsLeave** - Created when a participant leaves a
    conversation.This event object includes the ID of the participant
    leaving, along with the time of the event.

For more information see the [Direct Messages lookup API
References](/en/docs/twitter-api/direct-messages/lookup/api-reference) .

### []{#shared-conversation-and-event-ids} Shared conversation and event IDs across v1.1 and v2

An important concept is that conversation and event IDs are shared
across v1.1 and v2 versions of the Twitter Platform. This means both
versions can be used together. For example, the Direct Messages v1.1
endpoints provide methods for returning a single event and for deleting
events, methods not yet available with v2. Since IDs are common across
v1.1 and v2, you can make v1.1 requests based on IDs provided by v2, or
by referencing conversation IDs displayed in conversation URLs on the
Twitter application.

### []{#direct-message-event-fields-and-expansions} Direct Message event fields and expansions

The Twitter API v2 allows users to select exactly which data they want
to return from the API using a set of tools called fields and
expansions. For example, Direct Message lookup endpoints support the
following [ dm_events ]{.code-inline} fields:

-   [ id ]{.code-inline} , [ event_type ]{.code-inline} , and [ text
    ]{.code-inline} are the defaults for [ MessageCreate ]{.code-inline}
    events.

-   [ id ]{.code-inline} , [ event_type ]{.code-inline} , and [
    participant_ids ]{.code-inline} are the defaults for [
    ParticipantsJoin ]{.code-inline} and [ ParticipantsLeave
    ]{.code-inline} events.

-   [ dm_conversation_id ]{.code-inline} and [ created_at
    ]{.code-inline} are available for all events.

-   [ attachments ]{.code-inline} and [ referenced_tweets
    ]{.code-inline} are available for [ MessageCreate ]{.code-inline}
    events.

-   [ sender_id ]{.code-inline} is available for [ MessageCreate
    ]{.code-inline} and [ ParticipantsJoin ]{.code-inline} events.

-   [ participant_ids ]{.code-inline} is available for [
    ParticipantsJoin ]{.code-inline} and [ ParticipantsLeave
    ]{.code-inline} events.

In addition, the Direct Message lookup endpoints support the following
[expansions](/en/docs/twitter-api/expansions) : \

-   [ sender_id ]{.code-inline} - Expands the User object associated
    with who sent the message or who invited someone to the
    conversation.

-   [ referenced_tweets.id ]{.code-inline} - Expands the Tweet object if
    the Direct Message text includes a link to a Tweet.

-   [ attachments.media_keys ]{.code-inline} - Expands the Media object
    if the Direct Message includes a media attachment.

-   [ participant_ids ]{.code-inline} - Expands the User object
    associated with who joined or left a group conversation.

Since expansion include Tweets, Users, and Media objects, you can also
use the [ tweet.fields ]{.code-inline} , [ user.fields ]{.code-inline} ,
and [ media.fields ]{.code-inline} request query parameters. See our
guide on how to [use fields and
expansions](/en/docs/twitter-api/data-dictionary/using-fields-and-expansions)
for more information. \

### []{#conversation-event-types} Conversation event types

Below are example JSON objects for Direct Message the [ MessageCreate
]{.code-inline} , [ ParticipantsJoin ]{.code-inline} , and [
ParticipantsLeave ]{.code-inline} event types. \

Available [ dm_event ]{.code-inline} object fields: [ id ]{.code-inline}
, [ text ]{.code-inline} , [ event_type ]{.code-inline} , [
dm_conversation_id ]{.code-inline} , [ created_at ]{.code-inline} , [
sender_id ]{.code-inline} , [ attachments ]{.code-inline} , [
referenced_tweets ]{.code-inline} , [ participant_ids ]{.code-inline} .
See the the Fields and Expansion section for more details on selecting
these fields in your requests. \

Example [ MessageCreate ]{.code-inline} event:

With all the [ dm_event ]{.code-inline} fields specified, here is the
response for a simple text Direct Message:
:::
