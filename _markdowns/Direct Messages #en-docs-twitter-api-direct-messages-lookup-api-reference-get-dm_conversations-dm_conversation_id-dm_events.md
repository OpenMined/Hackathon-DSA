::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Returns a list of Direct Messages within a conversation specified in the
` dm_conversation_id ` path parameter. Messages are returned in reverse
chronological order.

### Endpoint URL

` https://api.twitter.com/2/dm_conversations/:dm_conversation_id/dm_events `

  ------------------------- ----------------------- -----------------------
  Name                      Type                    Description

  ` dm_conversation_id `\   string                  The ` id ` of the
  [Required]{.small}                                Direct Message
                                                    conversation for which
                                                    events are being
                                                    retrieved.
  ------------------------- ----------------------- -----------------------

+-----------------------+-----------------------+-----------------------+
| Name                  | Type                  | Description           |
+-----------------------+-----------------------+-----------------------+
| ` dm_event.fields `\  | enum ( ` id ` ,       | Extra fields to       |
| [Optional]{.small}    | ` text ` ,            | include in the event  |
|                       | ` event_type ` ,      | payload. ` id ` , and |
|                       | ` created_at ` ,      | ` event_type ` are    |
|                       | `                     | returned by default.  |
|                       |  dm_conversation_id ` | The ` text ` value    |
|                       | , ` sender_id ` ,     | isn\'t included for   |
|                       | ` participant_ids ` , | ` ParticipantsJoin `  |
|                       | ` referenced_tweets ` | and                   |
|                       | , ` attachments ` )   | ` PartcipantsLeave `  |
|                       |                       | events.               |
+-----------------------+-----------------------+-----------------------+
| ` event_types `\      | enum (                | The type of Direct    |
| [Optional]{.small}    | ` MessageCreate ` ,   | Message event to      |
|                       | ` ParticipantsJoin `  | returm. If not        |
|                       | ,                     | included, all types   |
|                       | ` ParticipantsLeave ` | are returned.         |
|                       | )                     |                       |
+-----------------------+-----------------------+-----------------------+
| ` expansions `\       | enum (                | [Ex                   |
| [Optional]{.small}    | ` att                 | pansions](/en/docs/tw |
|                       | achments.media_keys ` | itter-api/expansions) |
|                       | ,                     | enable you to request |
|                       | ` r                   | additional data       |
|                       | eferenced_tweets.id ` | objects that relate   |
|                       | , ` sender_id ` ,     | to the returned       |
|                       | ` participant_ids ` ) | Direct Message        |
|                       |                       | conversation events.  |
|                       |                       | Submit a list of      |
|                       |                       | desired expansions in |
|                       |                       | a comma-separated     |
|                       |                       | list without spaces.  |
|                       |                       | The IDs that          |
|                       |                       | represents the        |
|                       |                       | expanded data objects |
|                       |                       | will be included      |
|                       |                       | directly in the event |
|                       |                       | data object, and the  |
|                       |                       | expanded object       |
|                       |                       | metadata will be      |
|                       |                       | returned within the   |
|                       |                       | ` includes ` response |
|                       |                       | object. The following |
|                       |                       | data objects can be   |
|                       |                       | expanded using this   |
|                       |                       | parameter:            |
|                       |                       |                       |
|                       |                       | -   The user object   |
|                       |                       |     for the message   |
|                       |                       |     sender.           |
|                       |                       | -   Attached media\'s |
|                       |                       |     object.           |
|                       |                       | -   Any referenced    |
|                       |                       |     Tweet\'s object.  |
|                       |                       | -   The user object   |
|                       |                       |     for who is        |
|                       |                       |     joining or        |
|                       |                       |     leaving group     |
|                       |                       |     conversations.    |
+-----------------------+-----------------------+-----------------------+
| ` max_results `\      | number                | The maximum number of |
| [Optional]{.small}    |                       | results to be         |
|                       |                       | returned in a page.   |
|                       |                       | Must be between 1 and |
|                       |                       | 100. The default is   |
|                       |                       | 100.                  |
+-----------------------+-----------------------+-----------------------+
| ` media.fields `\     | enum (                | This                  |
| [Optional]{.small}    | ` duration_ms ` ,     | [fields](/en/doc      |
|                       | ` height ` ,          | s/twitter-api/fields) |
|                       | ` media_key ` ,       | parameter enables you |
|                       | ` preview_image_url ` | to select which       |
|                       | , ` type ` , ` url `  | specific [media       |
|                       | , ` width ` ,         | f                     |
|                       | ` public_metrics ` ,  | ields](/en/docs/twitt |
|                       | ` alt_text ` ,        | er-api/data-dictionar |
|                       | ` variants ` )        | y/object-model/media) |
|                       |                       | will be delivered in  |
|                       |                       | Direct Message        |
|                       |                       | \'MessageCreate\'     |
|                       |                       | events.               |
|                       |                       |                       |
|                       |                       | Specify the desired   |
|                       |                       | fields in a           |
|                       |                       | comma-separated list  |
|                       |                       | without spaces        |
|                       |                       | between commas and    |
|                       |                       | fields. While the     |
|                       |                       | media ID will be      |
|                       |                       | located in the event  |
|                       |                       | object, you will find |
|                       |                       | this ID and all       |
|                       |                       | additional media      |
|                       |                       | fields in the         |
|                       |                       | ` includes ` data     |
|                       |                       | object.               |
|                       |                       |                       |
|                       |                       | The event object will |
|                       |                       | only include media    |
|                       |                       | fields if the Direct  |
|                       |                       | Message contains      |
|                       |                       | media and if you\'ve  |
|                       |                       | also included the     |
|                       |                       | ` expansions=att      |
|                       |                       | achments.media_keys ` |
|                       |                       | query parameter in    |
|                       |                       | your request.         |
+-----------------------+-----------------------+-----------------------+
| ` pagination_token `\ | string                | Contains either the   |
| [Optional]{.small}    |                       | ` next_token ` or     |
|                       |                       | ` previous_token `    |
|                       |                       | value.                |
+-----------------------+-----------------------+-----------------------+
| ` tweet.fields `\     | enum (                | This                  |
| [Optional]{.small}    | ` attachments ` ,     | [fields](/en/doc      |
|                       | ` author_id ` ,       | s/twitter-api/fields) |
|                       | `                     | parameter enables you |
|                       | context_annotations ` | to select which       |
|                       | , ` conversation_id ` | specific [Tweet       |
|                       | , ` created_at ` ,    | f                     |
|                       | ` edit_controls ` ,   | ields](/en/docs/twitt |
|                       | ` entities ` ,        | er-api/data-dictionar |
|                       | ` geo ` , ` id ` ,    | y/object-model/tweet) |
|                       | `                     | will be delivered in  |
|                       | in_reply_to_user_id ` | each returned Direct  |
|                       | , ` lang ` ,          | Message               |
|                       | ` public_metrics ` ,  | \'MessageCreate\'     |
|                       | `                     | event object that     |
|                       |  possibly_sensitive ` | contains a Tweet      |
|                       | ,                     | reference.            |
|                       | ` referenced_tweets ` |                       |
|                       | , ` reply_settings `  | Specify the desired   |
|                       | , ` source ` ,        | fields in a           |
|                       | ` text ` ,            | comma-separated list  |
|                       | ` withheld ` )        | without spaces        |
|                       |                       | between commas and    |
|                       |                       | fields. While the     |
|                       |                       | Tweet ID will be in   |
|                       |                       | the event object, you |
|                       |                       | will find this ID and |
|                       |                       | all additional Tweet  |
|                       |                       | fields in the         |
|                       |                       | ` in                  |
|                       |                       | cludes data object. ` |
|                       |                       |                       |
|                       |                       | The event object will |
|                       |                       | include Tweet fields  |
|                       |                       | only if the Direct    |
|                       |                       | Message references a  |
|                       |                       | Tweet and the         |
|                       |                       | ` expansions=         |
|                       |                       | referenced_tweet.id ` |
|                       |                       | query parameter is    |
|                       |                       | included in the       |
|                       |                       | request.              |
+-----------------------+-----------------------+-----------------------+
| ` user.fields `\      | enum ( ` created_at ` | This                  |
| [Optional]{.small}    | , ` description ` ,   | [fields](/en/doc      |
|                       | ` entities ` , ` id ` | s/twitter-api/fields) |
|                       | , ` location ` ,      | parameter enables you |
|                       | ` m                   | to select which       |
|                       | ost_recent_tweet_id ` | specific [user        |
|                       | , ` name ` ,          | fields](/en/docs/twit |
|                       | ` pinned_tweet_id ` , | ter-api/data-dictiona |
|                       | ` profile_image_url ` | ry/object-model/user) |
|                       | , ` protected ` ,     | will be delivered for |
|                       | ` public_metrics ` ,  | Direct Message        |
|                       | ` url ` ,             | conversation events   |
|                       | ` username ` ,        | that reference a      |
|                       | ` verified ` ,        | sender or participant |
|                       | ` withheld ` )        | ID. Specify the       |
|                       |                       | desired fields in a   |
|                       |                       | comma-separated list  |
|                       |                       | without spaces        |
|                       |                       | between commas and    |
|                       |                       | fields.               |
|                       |                       |                       |
|                       |                       | While the user ID     |
|                       |                       | will be located in    |
|                       |                       | the event object, you |
|                       |                       | will find this ID and |
|                       |                       | all additional user   |
|                       |                       | fields in the         |
|                       |                       | ` includes ` data     |
|                       |                       | object.               |
|                       |                       |                       |
|                       |                       | You must also pass    |
|                       |                       | one of the user-based |
|                       |                       | expansions to return  |
|                       |                       | the desired user      |
|                       |                       | fields:               |
|                       |                       |                       |
|                       |                       | -   ` e               |
|                       |                       | xpansions=sender_id ` |
|                       |                       | -   ` expansi         |
|                       |                       | ons=participants_id ` |
+-----------------------+-----------------------+-----------------------+
:::
:::

::: c01-rich-text-editor
::: is-table-default
+-----------------------+-----------------------+-----------------------+
| Name                  | Type                  | Description           |
+-----------------------+-----------------------+-----------------------+
| ` id `                | string                | The ` id ` of the     |
|                       |                       | Direct Message event. |
+-----------------------+-----------------------+-----------------------+
| ` text `              | string                | The text included in  |
|                       |                       | the Direct Message.   |
+-----------------------+-----------------------+-----------------------+
| ` event_type `        | string                | The type of event.    |
|                       |                       | Possible values       |
|                       |                       | include               |
|                       |                       | MessageCreate,        |
|                       |                       | ParticipantsJoin,     |
|                       |                       | ParticipantsLeave.    |
+-----------------------+-----------------------+-----------------------+
| ` created_at `        | date (ISO 8601)       | The ` timestamp ` of  |
|                       |                       | the Direct Message    |
|                       |                       | event creation.       |
+-----------------------+-----------------------+-----------------------+
| ` sender_id `         | string                | The ` id ` of the     |
|                       |                       | user who sent the     |
|                       |                       | Direct Message.       |
+-----------------------+-----------------------+-----------------------+
| `                     | string                | The ` id ` of the     |
|  dm_conversation_id ` |                       | conversation the      |
|                       |                       | Direct Message        |
|                       |                       | belongs to.           |
+-----------------------+-----------------------+-----------------------+
| ` attachments `       | object                | The attached urls and |
|                       |                       | media information for |
|                       |                       | expansion. E.g.       |
|                       |                       | Media, Tweet, Card    |
+-----------------------+-----------------------+-----------------------+
| ` att                 | array                 | List of unique        |
| achments.media_keys ` |                       | identifiers of media  |
|                       |                       | attached to a direct  |
|                       |                       | message. These        |
|                       |                       | identifiers use the   |
|                       |                       | same media key format |
|                       |                       | as those returned by  |
|                       |                       | the [Media            |
|                       |                       | Library](/e           |
|                       |                       | n/docs/ads/creatives/ |
|                       |                       | guides/media-library) |
|                       |                       | .                     |
|                       |                       |                       |
|                       |                       | You can obtain the    |
|                       |                       | expanded object in    |
|                       |                       | ` includes.media ` by |
|                       |                       | adding                |
|                       |                       | ` expansions=att      |
|                       |                       | achments.media_keys ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` referenced_tweets ` | array                 | Expansion of a        |
|                       |                       | \"shared\" Tweet in   |
|                       |                       | the Direct Message.   |
|                       |                       | If the parent Tweet   |
|                       |                       | is a Retweet, a       |
|                       |                       | Retweet with comment  |
|                       |                       | (also known as Quoted |
|                       |                       | Tweet) or a Reply, it |
|                       |                       | will include the      |
|                       |                       | related Tweet         |
|                       |                       | referenced to by its  |
|                       |                       | parent.               |
+-----------------------+-----------------------+-----------------------+
| ` r                   | string                | The ` id ` of a       |
| eferenced_tweets.id ` |                       | \"shared\" Tweet in   |
|                       |                       | the Direct Message.   |
|                       |                       |                       |
|                       |                       | You can obtain the    |
|                       |                       | expanded object in    |
|                       |                       | ` includes.tweets `   |
|                       |                       | by adding             |
|                       |                       | ` expansions=r        |
|                       |                       | eferenced_tweets.id ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` media.fields `      | enum (                | Expansion of included |
|                       | ` duration_ms ` ,     | media with its own    |
|                       | ` height ` ,          | fields. E.g. url,     |
|                       | ` media_key ` ,       | size, etc. When       |
|                       | ` preview_image_url ` | including the         |
|                       | , ` type ` , ` url `  | ` expansions=att      |
|                       | , ` width ` ,         | achments.media_keys ` |
|                       | ` public_metrics ` ,  | parameter, this       |
|                       | `                     | includes a list of    |
|                       |  non_public_metrics ` | images, videos, and   |
|                       | , ` organic_metrics ` | GIFs included in      |
|                       | ,                     | Tweets in the form of |
|                       | ` promoted_metrics `  | [media                |
|                       | , ` alt_text ` ,      | ob                    |
|                       | ` variants ` )        | jects](/en/docs/twitt |
|                       |                       | er-api/data-dictionar |
|                       |                       | y/object-model/media) |
|                       |                       | with their default    |
|                       |                       | fields and any        |
|                       |                       | additional fields     |
|                       |                       | requested using the   |
|                       |                       | ` media.fields `      |
|                       |                       | parameter, assuming   |
|                       |                       | there is a media      |
|                       |                       | attachment present in |
|                       |                       | the returned          |
|                       |                       | Tweet(s).             |
|                       |                       |                       |
|                       |                       | You can obtain the    |
|                       |                       | expanded object in    |
|                       |                       | ` includes.media ` by |
|                       |                       | adding                |
|                       |                       | ` expa                |
|                       |                       | nsions=media.fields ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` user.fields `       | string                | The Expansion of user |
|                       |                       | object via            |
|                       |                       | ` sender_id ` .       |
|                       |                       |                       |
|                       |                       | You can obtain the    |
|                       |                       | expanded object in    |
|                       |                       | ` includes.users ` by |
|                       |                       | adding                |
|                       |                       | ` exp                 |
|                       |                       | ansions=user.fields ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` meta `              | object                | This object contains  |
|                       |                       | information about the |
|                       |                       | number of messages    |
|                       |                       | returned in the       |
|                       |                       | current request and   |
|                       |                       | pagination details.   |
+-----------------------+-----------------------+-----------------------+
| ` meta.next_token `   | string                | A value that encodes  |
|                       |                       | the next \'page\' of  |
|                       |                       | results that can be   |
|                       |                       | requested, via the    |
|                       |                       | ` pagination_token `  |
|                       |                       | request parameter.    |
+-----------------------+-----------------------+-----------------------+
| `                     | string                | A value that encodes  |
| meta.previous_token ` |                       | the previous \'page\' |
|                       |                       | of results that can   |
|                       |                       | be requested, via the |
|                       |                       | ` pagination_token `  |
|                       |                       | request parameter.    |
+-----------------------+-----------------------+-----------------------+
| ` meta.result_count ` | number                | The number of results |
|                       |                       | in the current page.  |
+-----------------------+-----------------------+-----------------------+
| ` errors `            | object                | Contains details      |
|                       |                       | about errors in a     |
|                       |                       | request for messages  |
|                       |                       | in a specified        |
|                       |                       | conversation.         |
+-----------------------+-----------------------+-----------------------+
:::
:::
:::
