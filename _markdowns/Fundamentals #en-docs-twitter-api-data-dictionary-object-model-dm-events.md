::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Direct Message (DM) conversations are made up of events. The Twitter API
v2 currently supports three event types: MessageCreate,
ParticipantsJoin, and ParticipantsLeave.

DM event objects are returned by the [Direct Message
lookup](/en/docs/twitter-api/direct-messages/lookup/introduction)
endpoints, and a MessageCreate event is created when Direct Messages are
successfully created with the [Manage Direct
Messages](/en/docs/twitter-api/direct-messages/manage/introduction)
endpoints.

When requesting DM events, there are three default event object
attributes, or fields, included: [ id ]{.code-inline} , [ event_type
]{.code-inline} , and [ text ]{.code-inline} . To receive additional
event fields, use the [fields](/en/docs/twitter-api/fields) parameter [
dm_event.fields ]{.code-inline} to select others. Other available event
fields include the following: [ dm_conversation_id ]{.code-inline} , [
created_at ]{.code-inline} , [ sender_id ]{.code-inline} , [ attachments
]{.code-inline} , [ participant_ids ]{.code-inline} , and [
referenced_tweets ]{.code-inline} .

Several of these fields provide the IDs of other Twitter objects related
to the Direct Message event:

-   [ sender_id ]{.code-inline} - The ID of the account that sent the
    message, or who invited a participant to a group conversation
-   [ partricipants_ids ]{.code-inline} - An array of account IDs. For
    ParticipantsJoin and ParticipantsLeave events this array will
    contain a single ID of the account that created the event
-   [ attachments ]{.code-inline} - Provides media IDs for content that
    has been uploaded to Twitter by the sender
-   [ referenced_tweets ]{.code-inline} - If a Tweet URL is found in the
    text field, the ID of that Tweet is included in the response

The [ sender_id ]{.code-inline} , [ participant_ids ]{.code-inline} , [
referenced_tweets.id, ]{.code-inline} and [ attachments.media_keys
]{.code-inline} [expansions](/en/docs/twitter-api/expansions) are
available to expand on these Twitter object IDs.
:::
:::

::: c01-rich-text-editor
::: is-table-default
+-----------------+-----------------+-----------------+-----------------+
| **Field value** | **Type**        | **Description** | **How it can be |
|                 |                 |                 | used**          |
+-----------------+-----------------+-----------------+-----------------+
| id (default)    | string          | The unique      | Use this to     |
|                 |                 | identifier of   | p               |
|                 |                 | the event.      | rogrammatically |
|                 |                 |                 | retrieve a      |
|                 |                 | [ \"id\":       | specific        |
|                 |                 | \"105011        | conversation    |
|                 |                 | 8621198921728\" | event           |
|                 |                 | ]{.code-inline} | (available with |
|                 |                 |                 | v1.1            |
|                 |                 |                 | endpoints).     |
+-----------------+-----------------+-----------------+-----------------+
| event_type      | string          | Describes the   | When retrieving |
| (default)       |                 | type of event.  | a               |
|                 |                 | Three types are | conversation\'s |
|                 |                 | currently       | history,        |
|                 |                 | supported:      | understanding   |
|                 |                 |                 | when messages   |
|                 |                 | -               | were created,   |
|                 |                 |   MessageCreate | and for group   |
|                 |                 |                 | conversations,  |
|                 |                 | -   P           | understanding   |
|                 |                 | articipantsJoin | when            |
|                 |                 |                 | participants    |
|                 |                 | -   Pa          | joined and      |
|                 |                 | rticipantsLeave | left. All GET   |
|                 |                 |                 | methods support |
|                 |                 | [               | filtering on    |
|                 |                 | \"event_type\": | specific event  |
|                 |                 | \"              | types with the  |
|                 |                 | MessageCreate\" | [ event_type=   |
|                 |                 | ]{.code-inline} | query           |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 | parameter. .    |
+-----------------+-----------------+-----------------+-----------------+
| text (default)  | string          | The actual      | With chatbots,  |
|                 |                 | UTF-8 text of   | this can be     |
|                 |                 | the Direct      | used to analyze |
|                 |                 | Message.        | message         |
|                 |                 |                 | contents and    |
|                 |                 | [ \"text\":     | determining     |
|                 |                 | \"Hello, just   | automated       |
|                 |                 | you!\"          | responses.      |
|                 |                 | ]{.code-inline} | Could be used   |
|                 |                 |                 | to build        |
|                 |                 |                 | conversation    |
|                 |                 |                 | search          |
|                 |                 |                 | features.       |
+-----------------+-----------------+-----------------+-----------------+
| sender_id       | string          | ID of the User  | Retrieve the    |
|                 |                 | creating the    | User object of  |
|                 |                 | event. To       | who created the |
|                 |                 | expand this     | MessageCreate   |
|                 |                 | object in the   | or              |
|                 |                 | response,       | P               |
|                 |                 | include [       | articipantsJoin |
|                 |                 | sender_id       | event.          |
|                 |                 | ]{.code-inline} |                 |
|                 |                 | as an           |                 |
|                 |                 | expansion  and  |                 |
|                 |                 | use the [       |                 |
|                 |                 | user.fields     |                 |
|                 |                 | ]{.code-inline} |                 |
|                 |                 | query parameter |                 |
|                 |                 | to specify User |                 |
|                 |                 | object          |                 |
|                 |                 | attributes of   |                 |
|                 |                 | interest.       |                 |
|                 |                 |                 |                 |
|                 |                 | [               |                 |
|                 |                 | \"sender_id\":  |                 |
|                 |                 | \"90694         |                 |
|                 |                 | 8460078698496\" |                 |
|                 |                 | ]{.code-inline} |                 |
+-----------------+-----------------+-----------------+-----------------+
| participant_id  | array (of       | IDs of the      | Used to         |
|                 | strings)        | participants    | retrieve User   |
|                 |                 | joining and     | objects for     |
|                 |                 | leaving a group | participants    |
|                 |                 | conversation.   | joining and     |
|                 |                 | Also used when  | leaving group   |
|                 |                 | creating new    | conversations.  |
|                 |                 | group           |                 |
|                 |                 | conversations.  |                 |
|                 |                 | To expand this  |                 |
|                 |                 | object in the   |                 |
|                 |                 | response,       |                 |
|                 |                 | include [       |                 |
|                 |                 | participant_ids |                 |
|                 |                 | ]{.code-inline} |                 |
|                 |                 | as an expansion |                 |
|                 |                 | and use the [   |                 |
|                 |                 | user.fields     |                 |
|                 |                 | ]{.code-inline} |                 |
|                 |                 | query parameter |                 |
|                 |                 | to specify User |                 |
|                 |                 | object          |                 |
|                 |                 | attributes of   |                 |
|                 |                 | interest.       |                 |
|                 |                 |                 |                 |
|                 |                 | [               |                 |
|                 |                 | \"par           |                 |
|                 |                 | ticipant_ids\": |                 |
|                 |                 | \[              |                 |
|                 |                 | ]{.code-inline} |                 |
|                 |                 |                 |                 |
|                 |                 | [               |                 |
|                 |                 | \"90694         |                 |
|                 |                 | 8460078698496\" |                 |
|                 |                 | ]{.code-inline} |                 |
|                 |                 |                 |                 |
|                 |                 | [ \]            |                 |
|                 |                 | ]{.code-inline} |                 |
+-----------------+-----------------+-----------------+-----------------+
| dm_             | string          | The unique      | Use this to     |
| conversation_id |                 | identifier of   | p               |
|                 |                 | the             | rogrammatically |
|                 |                 | conversation    | retrieve events |
|                 |                 | the event is    | from a          |
|                 |                 | apart of.       | conversation,   |
|                 |                 |                 | and add Direct  |
|                 |                 | [               | Messages to it. |
|                 |                 | \"dm_con        |                 |
|                 |                 | versation_id\": |                 |
|                 |                 | \"158498        |                 |
|                 |                 | 8213961031680\" |                 |
|                 |                 | ]{.code-inline} |                 |
+-----------------+-----------------+-----------------+-----------------+
| created_at      | date (ISO 8601) | Creation time   | This field can  |
|                 |                 | (UTC) of the    | be used to      |
|                 |                 | Tweet.          | understand when |
|                 |                 |                 | a Direct        |
|                 |                 | [               | Message was     |
|                 |                 | \"created_at\": | created or when |
|                 |                 | \"2019-06-04T   | conversation    |
|                 |                 | 23:12:08.000Z\" | participants    |
|                 |                 | ]{.code-inline} | joined or left. |
+-----------------+-----------------+-----------------+-----------------+
| re              | array           | ID for any      | When Direct     |
| ferenced_tweets |                 | Tweet mentioned | Messages        |
|                 |                 | in the Direct   | reference a     |
|                 |                 | Message text.   | Tweet, these    |
|                 |                 | To expand this  | IDs can be used |
|                 |                 | object in the   | to lookup the   |
|                 |                 | response,       | Tweet\'s        |
|                 |                 | include [       | details.        |
|                 |                 | refer           |                 |
|                 |                 | enced_tweets.id |                 |
|                 |                 | ]{.code-inline} |                 |
|                 |                 | as an expansion |                 |
|                 |                 | and use the [   |                 |
|                 |                 | tweet.fields    |                 |
|                 |                 | ]{.code-inline} |                 |
|                 |                 | query parameter |                 |
|                 |                 | to specify      |                 |
|                 |                 | Tweet object    |                 |
|                 |                 | attributes of   |                 |
|                 |                 | interest.       |                 |
|                 |                 |                 |                 |
|                 |                 | [               |                 |
|                 |                 | \"refer         |                 |
|                 |                 | enced_tweets\": |                 |
|                 |                 | \[              |                 |
|                 |                 | ]{.code-inline} |                 |
|                 |                 |                 |                 |
|                 |                 | [ {             |                 |
|                 |                 | ]{.code-inline} |                 |
|                 |                 |                 |                 |
|                 |                 | [ \"id\":       |                 |
|                 |                 | \"157886        |                 |
|                 |                 | 8150510456833\" |                 |
|                 |                 | ]{.code-inline} |                 |
|                 |                 |                 |                 |
|                 |                 | [ }             |                 |
|                 |                 | ]{.code-inline} |                 |
|                 |                 |                 |                 |
|                 |                 | [ \]            |                 |
|                 |                 | ]{.code-inline} |                 |
+-----------------+-----------------+-----------------+-----------------+
| attachments     | object          | For Direct      | Understanding   |
|                 |                 | Messages with   | the media       |
|                 |                 | attached Media, | objects         |
|                 |                 | provides the    | attached to     |
|                 |                 | media key of    | Direct          |
|                 |                 | the uploaded    | Messages.       |
|                 |                 | content (photo, |                 |
|                 |                 | video, or GIF.  |                 |
|                 |                 | To expand this  |                 |
|                 |                 | object in the   |                 |
|                 |                 | response,       |                 |
|                 |                 | include [       |                 |
|                 |                 | attachm         |                 |
|                 |                 | ents.media_keys |                 |
|                 |                 | ]{.code-inline} |                 |
|                 |                 | as an expansion |                 |
|                 |                 | and use the [   |                 |
|                 |                 | media.fields    |                 |
|                 |                 | ]{.code-inline} |                 |
|                 |                 | query parameter |                 |
|                 |                 | to specify      |                 |
|                 |                 | media object    |                 |
|                 |                 | attributes of   |                 |
|                 |                 | interest.       |                 |
|                 |                 | Currently, one  |                 |
|                 |                 | attachment is   |                 |
|                 |                 | supported.      |                 |
|                 |                 |                 |                 |
|                 |                 | [               |                 |
|                 |                 | \               |                 |
|                 |                 | "attachments\": |                 |
|                 |                 | {               |                 |
|                 |                 | ]{.code-inline} |                 |
|                 |                 |                 |                 |
|                 |                 | [               |                 |
|                 |                 | \"media_keys\": |                 |
|                 |                 | \[              |                 |
|                 |                 | ]{.code-inline} |                 |
|                 |                 |                 |                 |
|                 |                 | [               |                 |
|                 |                 | \"3_113604      |                 |
|                 |                 | 8009270239232\" |                 |
|                 |                 | ]{.code-inline} |                 |
|                 |                 |                 |                 |
|                 |                 | [ \]            |                 |
|                 |                 | ]{.code-inline} |                 |
|                 |                 |                 |                 |
|                 |                 | [ }             |                 |
|                 |                 | ]{.code-inline} |                 |
+-----------------+-----------------+-----------------+-----------------+
:::
:::

::: c01-rich-text-editor
::: is-table-default
For this example, we will build a request that retrieves events
associated with a one-to-one conversation. This request will return
fundamental Direct Message event fields, along with additional fields
for referenced Tweets and their authors. Let\'s build a query that asks
for:

-   Fundamental event attributes such as when it was created and what
    conversation it is part of (dm_conversation).
-   The account ID and description of who sent the Direct Message.
-   The text of any referenced Tweet, and when it was posted.
-   The account ID and description of any referenced Tweet author.

To return those attributes, your request query would include the
following:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 ?dm_event.fields=id,sender_id,text,created_at,dm_conversation_id&expansions=sender_id,referenced_tweets.id&tweet.fields=created_at,text,author_id&user.fields=description
    
```
:::
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 curl --request GET 'https://api.twitter.com/2/dm_conversations/with/:participant_id/dm_events?tweet.fields=created_at,text,author_id&user.fields=description&expansions=sender_id,participant_ids,referenced_tweets.id&dm_event.fields=id,sender_id,text,participant_ids,created_at,' 
    --header 'Authorization: Bearer $BEARER_TOKEN'
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
Be sure to replace [ \$BEARER_TOKEN ]{.code-inline} with your own
generated [Bearer
Token](/en/docs/authentication/oauth-2-0/bearer-tokens) .

### Sample Response
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {
    "data": [{
            "id": "1585047616894574596",
            "sender_id": "944480690",
            "text": "Hello, just you!",
            "created_at": "2022-10-25T23:16:15.000Z",
            "event_type": "MessageCreate",
            "dm_conversation_id": "944480690-906948460078698496"
        },
        {
            "id": "1581048670673260549",
            "sender_id": "944480690",
            "text": "Simple Tweet link: https://t.co/IYFbRIdXHg",
            "referenced_tweets": [{
                "id": "1578900353814519810"
            }],
            "created_at": "2022-10-14T22:25:52.000Z",
            "event_type": "MessageCreate",
            "dm_conversation_id": "944480690-906948460078698496"
        },
        {
            "id": "1580705121553420292",
            "sender_id": "944480690",
            "text": "Adding a new 1-to-1 Direct Message.",
            "created_at": "2022-10-13T23:40:43.000Z",
            "event_type": "MessageCreate",
            "dm_conversation_id": "944480690-906948460078698496"
        }
    ],
    "includes": {
        "users": [{
                "name": "API Demos",
                "description": "Hosting TwitterDev integrations... @TwitterDev #DevRel",
                "id": "944480690",
                "username": "FloodSocial"
            },
            {
                "name": "the SnowBot",
                "description": "Home of the @TwitterDev SnowBot... Serving snow reports, snow photos, and snow research links... Chatbot is currently being remodeled for Twitter APIv2.",
                "id": "906948460078698496",
                "username": "SnowBotDev"
            }
        ],
        "tweets": [{
                "text": "Feeling kind of bad that I didn’t wish everybody a happy new Colorado Water Year…\n\nHappy Water Year to all my Colorado friends and colleagues, new and old… \n\nMay this be a generous water year, although not too generous…",
                "id": "1578900353814519810",
                "created_at": "2022-10-09T00:09:13.000Z",
                "author_id": "944480690",
                "edit_history_tweet_ids": [
                    "1578900353814519810"
                ]
            }
        ]
    },
    "meta": {
        "result_count": 3,
        "next_token": "18LAA581J5II7LA00C00ZZZZ",
        "previous_token": "1BLC45G1H8CAL5DG0G00ZZZZ"
    }
}

    
```
:::
:::
:::
:::
