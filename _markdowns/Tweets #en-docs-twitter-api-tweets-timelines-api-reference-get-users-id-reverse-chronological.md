::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Allows you to retrieve a collection of the most recent Tweets and
Retweets posted by you and users you follow. This endpoint can return
every Tweet created on a timeline over the last 7 days as well as the
most recent 800 regardless of creation date.

### Endpoint URL

` https://api.twitter.com/2/users/:id/timelines/reverse_chronological `

  ----------------------- ----------------------- ---------------------------------------------------------------
  Name                    Type                    Description

  ` id `\                 string                  Unique identifier of the user that is requesting their
  [Required]{.small}                              chronological home timeline. User ID can be referenced using
                                                  the
                                                  [user/lookup](/en/docs/twitter-api/users/lookup/introduction)
                                                  endpoint. More information on Twitter IDs is
                                                  [here](/en/docs/twitter-ids) .
  ----------------------- ----------------------- ---------------------------------------------------------------

+-----------------------+-----------------------+-----------------------+
| Name                  | Type                  | Description           |
+-----------------------+-----------------------+-----------------------+
| ` end_time `\         | date (ISO 8601)       | YYYY-MM-DDTHH:mm:ssZ  |
| [Optional]{.small}    |                       | (ISO 8601/RFC 3339).  |
|                       |                       | The new UTC timestamp |
|                       |                       | from which the Tweets |
|                       |                       | will be provided.     |
|                       |                       | Timestamp is in       |
|                       |                       | second granularity    |
|                       |                       | and is inclusive (for |
|                       |                       | example, 12:00:01     |
|                       |                       | includes the first    |
|                       |                       | second of the         |
|                       |                       | minute).              |
|                       |                       |                       |
|                       |                       | Please note that this |
|                       |                       | parameter does not    |
|                       |                       | support a millisecond |
|                       |                       | value.                |
+-----------------------+-----------------------+-----------------------+
| ` exclude `\          | enum ( ` retweets ` , | Comma-separated list  |
| [Optional]{.small}    | ` replies ` )         | of the types of       |
|                       |                       | Tweets to exclude     |
|                       |                       | from the response.    |
+-----------------------+-----------------------+-----------------------+
| ` expansions `\       | enum (                | [Ex                   |
| [Optional]{.small}    | ` a                   | pansions](/en/docs/tw |
|                       | ttachments.poll_ids ` | itter-api/expansions) |
|                       | ,                     | enable you to request |
|                       | ` att                 | additional data       |
|                       | achments.media_keys ` | objects that relate   |
|                       | , ` author_id ` ,     | to the originally     |
|                       | ` edi                 | returned Tweets.      |
|                       | t_history_tweet_ids ` | Submit a list of      |
|                       | ,                     | desired expansions in |
|                       | ` entitie             | a comma-separated     |
|                       | s.mentions.username ` | list without spaces.  |
|                       | , ` geo.place_id ` ,  | The ID that           |
|                       | `                     | represents the        |
|                       | in_reply_to_user_id ` | expanded data object  |
|                       | ,                     | will be included      |
|                       | ` r                   | directly in the Tweet |
|                       | eferenced_tweets.id ` | data object, but the  |
|                       | ,                     | expanded object       |
|                       | ` referenced_         | metadata will be      |
|                       | tweets.id.author_id ` | returned within the   |
|                       | )                     | ` includes ` response |
|                       |                       | object, and will also |
|                       |                       | include the ID so     |
|                       |                       | that you can match    |
|                       |                       | this data object to   |
|                       |                       | the original Tweet    |
|                       |                       | object. The following |
|                       |                       | data objects can be   |
|                       |                       | expanded using this   |
|                       |                       | parameter:            |
|                       |                       |                       |
|                       |                       | -   The Tweet         |
|                       |                       |     author\'s user    |
|                       |                       |     object            |
|                       |                       | -   The user object   |
|                       |                       |     of the Tweet's    |
|                       |                       |     author that the   |
|                       |                       |     original Tweet is |
|                       |                       |     responding to     |
|                       |                       | -   Any mentioned     |
|                       |                       |     users' object     |
|                       |                       | -   Any referenced    |
|                       |                       |     Tweets' author's  |
|                       |                       |     user object       |
|                       |                       | -   Attached media's  |
|                       |                       |     object            |
|                       |                       | -   Attached poll's   |
|                       |                       |     object            |
|                       |                       | -   Attached place's  |
|                       |                       |     object            |
|                       |                       | -   Any referenced    |
|                       |                       |     Tweets' object    |
|                       |                       |     (this includes    |
|                       |                       |     Tweet objects for |
|                       |                       |     previous versions |
|                       |                       |     of an edited      |
|                       |                       |     Tweet).           |
+-----------------------+-----------------------+-----------------------+
| ` max_results `\      | integer               | Specifies the number  |
| [Optional]{.small}    |                       | of Tweets to try and  |
|                       |                       | retrieve, up to a     |
|                       |                       | maximum of 100 per    |
|                       |                       | distinct request. By  |
|                       |                       | default, 100 results  |
|                       |                       | are returned if this  |
|                       |                       | parameter is not      |
|                       |                       | supplied. The minimum |
|                       |                       | permitted value is 1. |
|                       |                       | It is possible to     |
|                       |                       | receive less than the |
|                       |                       | ` max_results ` per   |
|                       |                       | request throughout    |
|                       |                       | the pagination        |
|                       |                       | process.              |
+-----------------------+-----------------------+-----------------------+
| ` media.fields `\     | enum (                | This                  |
| [Optional]{.small}    | ` duration_ms ` ,     | [fields](/en/doc      |
|                       | ` height ` ,          | s/twitter-api/fields) |
|                       | ` media_key ` ,       | parameter enables you |
|                       | ` preview_image_url ` | to select which       |
|                       | , ` type ` , ` url `  | specific [media       |
|                       | , ` width ` ,         | f                     |
|                       | ` public_metrics ` ,  | ields](/en/docs/twitt |
|                       | `                     | er-api/data-dictionar |
|                       |  non_public_metrics ` | y/object-model/media) |
|                       | , ` organic_metrics ` | will deliver in each  |
|                       | ,                     | returned Tweet.       |
|                       | ` promoted_metrics `  | Specify the desired   |
|                       | , ` alt_text ` ,      | fields in a           |
|                       | ` variants ` )        | comma-separated list  |
|                       |                       | without spaces        |
|                       |                       | between commas and    |
|                       |                       | fields. The Tweet     |
|                       |                       | will only return      |
|                       |                       | media fields if the   |
|                       |                       | Tweet contains media  |
|                       |                       | and if you\'ve also   |
|                       |                       | included the          |
|                       |                       | ` expansions=att      |
|                       |                       | achments.media_keys ` |
|                       |                       | query parameter in    |
|                       |                       | your request. While   |
|                       |                       | the media ID will be  |
|                       |                       | located in the Tweet  |
|                       |                       | object, you will find |
|                       |                       | this ID and all       |
|                       |                       | additional media      |
|                       |                       | fields in the         |
|                       |                       | ` includes ` data     |
|                       |                       | object.               |
+-----------------------+-----------------------+-----------------------+
| ` pagination_token `\ | string                | This parameter is     |
| [Optional]{.small}    |                       | used to move forwards |
|                       |                       | or backwards through  |
|                       |                       | \'pages\' of results, |
|                       |                       | based on the value of |
|                       |                       | the ` next_token ` or |
|                       |                       | ` previous_token ` in |
|                       |                       | the response. The     |
|                       |                       | value used with the   |
|                       |                       | parameter is pulled   |
|                       |                       | directly from the     |
|                       |                       | response provided by  |
|                       |                       | the API, and should   |
|                       |                       | not be modified.      |
+-----------------------+-----------------------+-----------------------+
| ` place.fields `\     | enum (                | This                  |
| [Optional]{.small}    | ` contained_within `  | [fields](/en/doc      |
|                       | , ` country ` ,       | s/twitter-api/fields) |
|                       | ` country_code ` ,    | parameter enables you |
|                       | ` full_name ` ,       | to select which       |
|                       | ` geo ` , ` id ` ,    | specific [place       |
|                       | ` name ` ,            | f                     |
|                       | ` place_type ` )      | ields](/en/docs/twitt |
|                       |                       | er-api/data-dictionar |
|                       |                       | y/object-model/place) |
|                       |                       | will deliver in each  |
|                       |                       | returned Tweet.       |
|                       |                       | Specify the desired   |
|                       |                       | fields in a           |
|                       |                       | comma-separated list  |
|                       |                       | without spaces        |
|                       |                       | between commas and    |
|                       |                       | fields. The Tweet     |
|                       |                       | will only return      |
|                       |                       | place fields if the   |
|                       |                       | Tweet contains a      |
|                       |                       | place and if you\'ve  |
|                       |                       | also included the     |
|                       |                       | ` expa                |
|                       |                       | nsions=geo.place_id ` |
|                       |                       | query parameter in    |
|                       |                       | your request. While   |
|                       |                       | the place ID will be  |
|                       |                       | located in the Tweet  |
|                       |                       | object, you will find |
|                       |                       | this ID and all       |
|                       |                       | additional place      |
|                       |                       | fields in the         |
|                       |                       | ` includes ` data     |
|                       |                       | object.               |
+-----------------------+-----------------------+-----------------------+
| ` poll.fields `\      | enum (                | This                  |
| [Optional]{.small}    | ` duration_minutes `  | [fields](/en/doc      |
|                       | , ` end_datetime ` ,  | s/twitter-api/fields) |
|                       | ` id ` , ` options `  | parameter enables you |
|                       | , ` voting_status ` ) | to select which       |
|                       |                       | specific [poll        |
|                       |                       | fields](/en/docs/twit |
|                       |                       | ter-api/data-dictiona |
|                       |                       | ry/object-model/poll) |
|                       |                       | will deliver in each  |
|                       |                       | returned Tweet.       |
|                       |                       | Specify the desired   |
|                       |                       | fields in a           |
|                       |                       | comma-separated list  |
|                       |                       | without spaces        |
|                       |                       | between commas and    |
|                       |                       | fields. The Tweet     |
|                       |                       | will only return poll |
|                       |                       | fields if the Tweet   |
|                       |                       | contains a poll and   |
|                       |                       | if you\'ve also       |
|                       |                       | included the          |
|                       |                       | ` expansions=a        |
|                       |                       | ttachments.poll_ids ` |
|                       |                       | query parameter in    |
|                       |                       | your request. While   |
|                       |                       | the poll ID will be   |
|                       |                       | located in the Tweet  |
|                       |                       | object, you will find |
|                       |                       | this ID and all       |
|                       |                       | additional poll       |
|                       |                       | fields in the         |
|                       |                       | ` includes ` data     |
|                       |                       | object.               |
+-----------------------+-----------------------+-----------------------+
| ` since_id `\         | string                | Returns results with  |
| [Optional]{.small}    |                       | a Tweet ID greater    |
|                       |                       | than (that is, more   |
|                       |                       | recent than) the      |
|                       |                       | specified \'since\'   |
|                       |                       | Tweet ID. There are   |
|                       |                       | limits to the number  |
|                       |                       | of Tweets that can be |
|                       |                       | accessed through the  |
|                       |                       | API. If the limit of  |
|                       |                       | Tweets has occurred   |
|                       |                       | since the             |
|                       |                       | ` since_id ` , the    |
|                       |                       | ` since_id ` will be  |
|                       |                       | forced to the oldest  |
|                       |                       | ID available. More    |
|                       |                       | information on        |
|                       |                       | Twitter IDs is        |
|                       |                       | [here](               |
|                       |                       | /en/docs/twitter-ids) |
|                       |                       | .                     |
+-----------------------+-----------------------+-----------------------+
| ` start_time `\       | date (ISO 8601)       | YYYY-MM-DDTHH:mm:ssZ  |
| [Optional]{.small}    |                       | (ISO 8601/RFC 3339).  |
|                       |                       | The oldest UTC        |
|                       |                       | timestamp from which  |
|                       |                       | the Tweets will be    |
|                       |                       | provided. Timestamp   |
|                       |                       | is in second          |
|                       |                       | granularity and is    |
|                       |                       | inclusive (for        |
|                       |                       | example, 12:00:01     |
|                       |                       | includes the first    |
|                       |                       | second of the         |
|                       |                       | minute).              |
|                       |                       |                       |
|                       |                       | Please note that this |
|                       |                       | parameter does not    |
|                       |                       | support a millisecond |
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
|                       | `                     | will deliver in each  |
|                       | in_reply_to_user_id ` | returned Tweet        |
|                       | , ` lang ` ,          | object. Specify the   |
|                       | `                     | desired fields in a   |
|                       |  non_public_metrics ` | comma-separated list  |
|                       | , ` public_metrics `  | without spaces        |
|                       | , ` organic_metrics ` | between commas and    |
|                       | ,                     | fields. You can also  |
|                       | ` promoted_metrics `  | pass the              |
|                       | ,                     | ` expansions=r        |
|                       | `                     | eferenced_tweets.id ` |
|                       |  possibly_sensitive ` | expansion to return   |
|                       | ,                     | the specified fields  |
|                       | ` referenced_tweets ` | for both the original |
|                       | , ` reply_settings `  | Tweet and any         |
|                       | , ` source ` ,        | included referenced   |
|                       | ` text ` ,            | Tweets. The requested |
|                       | ` withheld ` )        | Tweet fields will     |
|                       |                       | display in both the   |
|                       |                       | original Tweet data   |
|                       |                       | object, as well as in |
|                       |                       | the referenced Tweet  |
|                       |                       | expanded data object  |
|                       |                       | that will be located  |
|                       |                       | in the ` includes `   |
|                       |                       | data object.          |
+-----------------------+-----------------------+-----------------------+
| ` until_id `\         | string                | Returns results with  |
| [Optional]{.small}    |                       | a Tweet ID less than  |
|                       |                       | (that is, older than) |
|                       |                       | the specified         |
|                       |                       | \'until\' Tweet ID.   |
|                       |                       | There are limits to   |
|                       |                       | the number of Tweets  |
|                       |                       | that can be accessed  |
|                       |                       | through the API. If   |
|                       |                       | the limit of Tweets   |
|                       |                       | has occurred since    |
|                       |                       | the ` until_id ` ,    |
|                       |                       | the ` until_id ` will |
|                       |                       | be forced to the most |
|                       |                       | recent ID available.  |
|                       |                       | More information on   |
|                       |                       | Twitter IDs is        |
|                       |                       | [here](               |
|                       |                       | /en/docs/twitter-ids) |
|                       |                       | .                     |
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
|                       | , ` protected ` ,     | will deliver in each  |
|                       | ` public_metrics ` ,  | returned Tweet.       |
|                       | ` url ` ,             | Specify the desired   |
|                       | ` username ` ,        | fields in a           |
|                       | ` verified ` ,        | comma-separated list  |
|                       | ` verified_type ` ,   | without spaces        |
|                       | ` withheld ` )        | between commas and    |
|                       |                       | fields. While the     |
|                       |                       | user ID will be       |
|                       |                       | located in the        |
|                       |                       | original Tweet        |
|                       |                       | object, you will find |
|                       |                       | this ID and all       |
|                       |                       | additional user       |
|                       |                       | fields in the         |
|                       |                       | ` includes ` data     |
|                       |                       | object. You must also |
|                       |                       | pass one of the user  |
|                       |                       | expansions to return  |
|                       |                       | the desired user      |
|                       |                       | fields:               |
|                       |                       |                       |
|                       |                       | -   ` e               |
|                       |                       | xpansions=author_id ` |
|                       |                       | -                     |
|                       |                       |  ` expansions=entitie |
|                       |                       | s.mentions.username ` |
|                       |                       | -   ` expansions=     |
|                       |                       | in_reply_to_user_id ` |
|                       |                       | -   ` e               |
|                       |                       | xpansions=referenced_ |
|                       |                       | tweets.id.author_id ` |
+-----------------------+-----------------------+-----------------------+
:::
:::

::: c01-rich-text-editor
::: is-table-default
+-----------------------+-----------------------+-----------------------+
| Name                  | Type                  | Description           |
+-----------------------+-----------------------+-----------------------+
| ` id `\               | string                | Unique identifier of  |
| [Default]{.small}     |                       | this Tweet. This is   |
|                       |                       | returned as a string  |
|                       |                       | in order to avoid     |
|                       |                       | complications with    |
|                       |                       | languages and tools   |
|                       |                       | that cannot handle    |
|                       |                       | large integers. More  |
|                       |                       | information on        |
|                       |                       | Twitter IDs is        |
|                       |                       | [here](               |
|                       |                       | /en/docs/twitter-ids) |
|                       |                       | .                     |
+-----------------------+-----------------------+-----------------------+
| ` text `\             | string                | The content of the    |
| [Default]{.small}     |                       | Tweet.                |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` tweet.fields=text ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` created_at `        | date (ISO 8601)       | Creation time of the  |
|                       |                       | Tweet. For example:   |
|                       |                       | ` 2020-               |
|                       |                       | 12-10T20:00:10.000Z ` |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` twee                |
|                       |                       | t.fields=created_at ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` author_id `         | string                | Unique identifier of  |
|                       |                       | this user. This is    |
|                       |                       | returned as a string  |
|                       |                       | in order to avoid     |
|                       |                       | complications with    |
|                       |                       | languages and tools   |
|                       |                       | that cannot handle    |
|                       |                       | large integers.       |
|                       |                       |                       |
|                       |                       | You can obtain the    |
|                       |                       | expanded object in    |
|                       |                       | ` includes.users ` by |
|                       |                       | adding                |
|                       |                       | ` e                   |
|                       |                       | xpansions=author_id ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` edit                | array                 | Unique identifiers    |
| _history_tweet_ids `\ |                       | indicating all        |
| [Default]{.small}     |                       | versions of an edited |
|                       |                       | Tweet. For Tweets     |
|                       |                       | with no edits, there  |
|                       |                       | will be one ID. For   |
|                       |                       | Tweets with an edit   |
|                       |                       | history, there will   |
|                       |                       | be multiple IDs,      |
|                       |                       | arranged in ascending |
|                       |                       | order reflecting the  |
|                       |                       | order of edit, with   |
|                       |                       | the most recent       |
|                       |                       | version in the last   |
|                       |                       | position of the       |
|                       |                       | array.                |
+-----------------------+-----------------------+-----------------------+
| ` edit_controls `     | object                | Indicates if a Tweet  |
|                       |                       | is eligible for edit, |
|                       |                       | how long it is        |
|                       |                       | editable for, and the |
|                       |                       | number of remaining   |
|                       |                       | edits.                |
|                       |                       |                       |
|                       |                       | The                   |
|                       |                       | ` is_edit_eligible `  |
|                       |                       | field indicates if a  |
|                       |                       | Tweet was eligible    |
|                       |                       | for edit when         |
|                       |                       | published. This field |
|                       |                       | is not dynamic and    |
|                       |                       | won\'t toggle from    |
|                       |                       | True to False when a  |
|                       |                       | Tweet reaches its     |
|                       |                       | editable time limit,  |
|                       |                       | or maximum number of  |
|                       |                       | edits. The following  |
|                       |                       | Tweet features will   |
|                       |                       | cause this field to   |
|                       |                       | be false:             |
|                       |                       |                       |
|                       |                       | -   Tweet is promoted |
|                       |                       | -   Tweet has a poll  |
|                       |                       | -   Tweet is a        |
|                       |                       |     non-self-thread   |
|                       |                       |     reply             |
|                       |                       | -   Tweet is a        |
|                       |                       |     Retweet (note     |
|                       |                       |     that Quote Tweets |
|                       |                       |     are eligible for  |
|                       |                       |     edit)             |
|                       |                       | -   Tweet is nullcast |
|                       |                       | -   Community Tweet   |
|                       |                       | -   Superfollow Tweet |
|                       |                       | -   Collaborative     |
|                       |                       |     Tweet             |
|                       |                       |                       |
|                       |                       | ` { "edit_contr       |
|                       |                       | ols": { "is_edit_elig |
|                       |                       | ible": true, "editabl |
|                       |                       | e_until": "2022-08-21 |
|                       |                       |  09:35:20.311", "edit |
|                       |                       | s_remaining": 4 } } ` |
|                       |                       | Editable Tweets can   |
|                       |                       | be edited for the     |
|                       |                       | first 30 minutes      |
|                       |                       | after creation and    |
|                       |                       | can be edited up to   |
|                       |                       | five times.           |
+-----------------------+-----------------------+-----------------------+
| ` conversation_id `   | string                | The Tweet ID of the   |
|                       |                       | original Tweet of the |
|                       |                       | conversation (which   |
|                       |                       | includes direct       |
|                       |                       | replies, replies of   |
|                       |                       | replies).             |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` tweet.fie           |
|                       |                       | lds=conversation_id ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` note_tweet `        | object                | Information about     |
|                       |                       | Tweets with more than |
|                       |                       | 280 characters.       |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` twee                |
|                       |                       | t.fields=note_tweet ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| `                     | string                | If this Tweet is a    |
| in_reply_to_user_id ` |                       | Reply, indicates the  |
|                       |                       | user ID of the parent |
|                       |                       | Tweet\'s author. This |
|                       |                       | is returned as a      |
|                       |                       | string in order to    |
|                       |                       | avoid complications   |
|                       |                       | with languages and    |
|                       |                       | tools that cannot     |
|                       |                       | handle large          |
|                       |                       | integers.             |
|                       |                       |                       |
|                       |                       | You can obtain the    |
|                       |                       | expanded object in    |
|                       |                       | ` includes.users ` by |
|                       |                       | adding                |
|                       |                       | ` expansions=         |
|                       |                       | in_reply_to_user_id ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` referenced_tweets ` | array                 | A list of Tweets this |
|                       |                       | Tweet refers to. For  |
|                       |                       | example, if the       |
|                       |                       | parent Tweet is a     |
|                       |                       | Retweet, a Retweet    |
|                       |                       | with comment (also    |
|                       |                       | known as Quoted       |
|                       |                       | Tweet) or a Reply, it |
|                       |                       | will include the      |
|                       |                       | related Tweet         |
|                       |                       | referenced to by its  |
|                       |                       | parent.               |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` tweet.field         |
|                       |                       | s=referenced_tweets ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` ref                 | enum ( ` retweeted `  | Indicates the type of |
| erenced_tweets.type ` | , ` quoted ` ,        | relationship between  |
|                       | ` replied_to ` )      | this Tweet and the    |
|                       |                       | Tweet returned in the |
|                       |                       | response:             |
|                       |                       | ` retweeted ` (this   |
|                       |                       | Tweet is a Retweet),  |
|                       |                       | ` quoted ` (a Retweet |
|                       |                       | with comment, also    |
|                       |                       | known as Quoted       |
|                       |                       | Tweet), or            |
|                       |                       | ` replied_to ` (this  |
|                       |                       | Tweet is a reply).    |
+-----------------------+-----------------------+-----------------------+
| ` r                   | string                | The unique identifier |
| eferenced_tweets.id ` |                       | of the referenced     |
|                       |                       | Tweet.                |
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
| ` attachments `       | object                | Specifies the type of |
|                       |                       | attachments (if any)  |
|                       |                       | present in this       |
|                       |                       | Tweet.                |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` tweet               |
|                       |                       | .fields=attachments ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` att                 | array                 | List of unique        |
| achments.media_keys ` |                       | identifiers of media  |
|                       |                       | attached to this      |
|                       |                       | Tweet. These          |
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
| ` a                   | array                 | List of unique        |
| ttachments.poll_ids ` |                       | identifiers of polls  |
|                       |                       | present in the Tweets |
|                       |                       | returned. These are   |
|                       |                       | returned as a string  |
|                       |                       | in order to avoid     |
|                       |                       | complications with    |
|                       |                       | languages and tools   |
|                       |                       | that cannot handle    |
|                       |                       | large integers.       |
|                       |                       |                       |
|                       |                       | You can obtain the    |
|                       |                       | expanded object in    |
|                       |                       | ` includes.polls ` by |
|                       |                       | adding                |
|                       |                       | ` expansions=at       |
|                       |                       | tachments.polls_ids ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` geo `               | object                | Contains details      |
|                       |                       | about the location    |
|                       |                       | tagged by the user in |
|                       |                       | this Tweet, if they   |
|                       |                       | specified one.        |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` tweet.fields=geo `  |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` geo.coordinates `   | object                | Contains details      |
|                       |                       | about the coordinates |
|                       |                       | of the location       |
|                       |                       | tagged by the user in |
|                       |                       | this Tweet, if they   |
|                       |                       | specified one.        |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` tweet.fie           |
|                       |                       | lds=geo.coordinates ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` g                   | string                | Describes the type of |
| eo.coordinates.type ` |                       | coordinate. The only  |
|                       |                       | value supported at    |
|                       |                       | present is ` Point `  |
|                       |                       | .                     |
+-----------------------+-----------------------+-----------------------+
| ` geo.coor            | array                 | A pair of decimal     |
| dinates.coordinates ` |                       | values representing   |
|                       |                       | the precise location  |
|                       |                       | of the user           |
|                       |                       | (latitude,            |
|                       |                       | longitude). This      |
|                       |                       | value will be         |
|                       |                       | ` null ` unless the   |
|                       |                       | user explicitly       |
|                       |                       | shared their precise  |
|                       |                       | location.             |
+-----------------------+-----------------------+-----------------------+
| ` geo.place_id `      | string                | The unique identifier |
|                       |                       | of the place, if this |
|                       |                       | is a point of         |
|                       |                       | interest tagged in    |
|                       |                       | the Tweet.            |
|                       |                       |                       |
|                       |                       | You can obtain the    |
|                       |                       | expanded object in    |
|                       |                       | ` includes.places `   |
|                       |                       | by adding             |
|                       |                       | ` expa                |
|                       |                       | nsions=geo.place_id ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| `                     | array                 | Contains context      |
| context_annotations ` |                       | annotations for the   |
|                       |                       | Tweet.                |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` tweet.fields=       |
|                       |                       | context_annotations ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` context             | object                | Contains elements     |
| _annotations.domain ` |                       | which identify        |
|                       |                       | detailed information  |
|                       |                       | regarding the domain  |
|                       |                       | classification based  |
|                       |                       | on Tweet text.        |
+-----------------------+-----------------------+-----------------------+
| ` context_an          | string                | Contains the numeric  |
| notations.domain.id ` |                       | value of the domain.  |
+-----------------------+-----------------------+-----------------------+
| ` context_anno        | string                | Domain name based on  |
| tations.domain.name ` |                       | the Tweet text.       |
+-----------------------+-----------------------+-----------------------+
| ` context_annotations | string                | Long form description |
| .domain.description ` |                       | of domain             |
|                       |                       | classification.       |
+-----------------------+-----------------------+-----------------------+
| ` context             | object                | Contains elements     |
| _annotations.entity ` |                       | which identify        |
|                       |                       | detailed information  |
|                       |                       | regarding the domain  |
|                       |                       | classification bases  |
|                       |                       | on Tweet text.        |
+-----------------------+-----------------------+-----------------------+
| ` context_an          | string                | Unique value which    |
| notations.entity.id ` |                       | correlates to an      |
|                       |                       | explicitly mentioned  |
|                       |                       | Person, Place,        |
|                       |                       | Product or            |
|                       |                       | Organization.         |
+-----------------------+-----------------------+-----------------------+
| ` context_anno        | string                | Name or reference of  |
| tations.entity.name ` |                       | entity referenced in  |
|                       |                       | the Tweet.            |
+-----------------------+-----------------------+-----------------------+
| ` context_annotations | string                | Additional            |
| .entity.description ` |                       | information regarding |
|                       |                       | referenced entity.    |
+-----------------------+-----------------------+-----------------------+
| ` entities `          | object                | Contains details      |
|                       |                       | about text that has a |
|                       |                       | special meaning in a  |
|                       |                       | Tweet.                |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` tw                  |
|                       |                       | eet.fields=entities ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` e                   | array                 | Contains details      |
| ntities.annotations ` |                       | about annotations     |
|                       |                       | relative to the text  |
|                       |                       | within a Tweet.       |
+-----------------------+-----------------------+-----------------------+
| ` entitie             | integer               | The start position    |
| s.annotations.start ` |                       | (zero-based) of the   |
|                       |                       | text used to annotate |
|                       |                       | the Tweet. All start  |
|                       |                       | indices are           |
|                       |                       | inclusive.            |
+-----------------------+-----------------------+-----------------------+
| ` entit               | integer               | The end position      |
| ies.annotations.end ` |                       | (zero based) of the   |
|                       |                       | text used to annotate |
|                       |                       | the Tweet. While all  |
|                       |                       | other end indices are |
|                       |                       | exclusive, this one   |
|                       |                       | is inclusive.         |
+-----------------------+-----------------------+-----------------------+
| ` entities.anno       | number                | The confidence score  |
| tations.probability ` |                       | for the annotation as |
|                       |                       | it correlates to the  |
|                       |                       | Tweet text.           |
+-----------------------+-----------------------+-----------------------+
| ` entiti              | string                | The description of    |
| es.annotations.type ` |                       | the type of entity    |
|                       |                       | identified when the   |
|                       |                       | Tweet text was        |
|                       |                       | interpreted.          |
+-----------------------+-----------------------+-----------------------+
| ` entities.annotati   | string                | The text used to      |
| ons.normalized_text ` |                       | determine the         |
|                       |                       | annotation type.      |
+-----------------------+-----------------------+-----------------------+
| ` entities.urls `     | array                 | Contains details      |
|                       |                       | about text recognized |
|                       |                       | as a URL.             |
+-----------------------+-----------------------+-----------------------+
| `                     | integer               | The start position    |
| entities.urls.start ` |                       | (zero-based) of the   |
|                       |                       | recognized URL within |
|                       |                       | the Tweet. All start  |
|                       |                       | indices are           |
|                       |                       | inclusive.            |
+-----------------------+-----------------------+-----------------------+
| ` entities.urls.end ` | integer               | The end position      |
|                       |                       | (zero-based) of the   |
|                       |                       | recognized URL within |
|                       |                       | the Tweet. This end   |
|                       |                       | index is exclusive.   |
+-----------------------+-----------------------+-----------------------+
| ` entities.urls.url ` | string                | The URL in the format |
|                       |                       | tweeted by the user.  |
+-----------------------+-----------------------+-----------------------+
| ` entitie             | string                | The fully resolved    |
| s.urls.expanded_url ` |                       | URL.                  |
+-----------------------+-----------------------+-----------------------+
| ` entiti              | string                | The URL as displayed  |
| es.urls.display_url ` |                       | in the Twitter        |
|                       |                       | client.               |
+-----------------------+-----------------------+-----------------------+
| ` entiti              | string                | The full destination  |
| es.urls.unwound_url ` |                       | URL.                  |
+-----------------------+-----------------------+-----------------------+
| ` entities.hashtags ` | array                 | Contains details      |
|                       |                       | about text recognized |
|                       |                       | as a Hashtag.         |
+-----------------------+-----------------------+-----------------------+
| ` enti                | integer               | The start position    |
| ties.hashtags.start ` |                       | (zero-based) of the   |
|                       |                       | recognized Hashtag    |
|                       |                       | within the Tweet. All |
|                       |                       | start indices are     |
|                       |                       | inclusive.            |
+-----------------------+-----------------------+-----------------------+
| ` en                  | integer               | The end position      |
| tities.hashtags.end ` |                       | (zero-based) of the   |
|                       |                       | recognized Hashtag    |
|                       |                       | within the Tweet.     |
|                       |                       | This end index is     |
|                       |                       | exclusive.            |
+-----------------------+-----------------------+-----------------------+
| ` en                  | string                | The text of the       |
| tities.hashtags.tag ` |                       | Hashtag.              |
+-----------------------+-----------------------+-----------------------+
| ` entities.mentions ` | array                 | Contains details      |
|                       |                       | about text recognized |
|                       |                       | as a user mention.    |
+-----------------------+-----------------------+-----------------------+
| ` enti                | integer               | The start position    |
| ties.mentions.start ` |                       | (zero-based) of the   |
|                       |                       | recognized user       |
|                       |                       | mention within the    |
|                       |                       | Tweet. All start      |
|                       |                       | indices are           |
|                       |                       | inclusive.            |
+-----------------------+-----------------------+-----------------------+
| ` en                  | integer               | The end position      |
| tities.mentions.end ` |                       | (zero-based) of the   |
|                       |                       | recognized user       |
|                       |                       | mention within the    |
|                       |                       | Tweet. This end index |
|                       |                       | is exclusive.         |
+-----------------------+-----------------------+-----------------------+
| ` entitie             | string                | The part of text      |
| s.mentions.username ` |                       | recognized as a user  |
|                       |                       | mention.              |
|                       |                       |                       |
|                       |                       | You can obtain the    |
|                       |                       | expanded object in    |
|                       |                       | ` includes.users ` by |
|                       |                       | adding                |
|                       |                       | ` expansions=entitie  |
|                       |                       | s.mentions.username ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` entities.cashtags ` | array                 | Contains details      |
|                       |                       | about text recognized |
|                       |                       | as a Cashtag.         |
+-----------------------+-----------------------+-----------------------+
| ` enti                | integer               | The start position    |
| ties.cashtags.start ` |                       | (zero-based) of the   |
|                       |                       | recognized Cashtag    |
|                       |                       | within the Tweet. All |
|                       |                       | start indices are     |
|                       |                       | inclusive.            |
+-----------------------+-----------------------+-----------------------+
| ` en                  | integer               | The end position      |
| tities.cashtags.end ` |                       | (zero-based) of the   |
|                       |                       | recognized Cashtag    |
|                       |                       | within the Tweet.     |
|                       |                       | This end index is     |
|                       |                       | exclusive.            |
+-----------------------+-----------------------+-----------------------+
| ` en                  | string                | The text of the       |
| tities.cashtags.tag ` |                       | Cashtag.              |
+-----------------------+-----------------------+-----------------------+
| ` withheld `          | object                | Contains withholding  |
|                       |                       | details for [withheld |
|                       |                       | content](https://he   |
|                       |                       | lp.twitter.com/en/rul |
|                       |                       | es-and-policies/tweet |
|                       |                       | -withheld-by-country) |
|                       |                       | .                     |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` tw                  |
|                       |                       | eet.fields=withheld ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| `                     | boolean               | Indicates if the      |
|  withheld.copyright ` |                       | content is being      |
|                       |                       | withheld for on the   |
|                       |                       | basis of copyright    |
|                       |                       | infringement.         |
+-----------------------+-----------------------+-----------------------+
| ` wit                 | array                 | Provides a list of    |
| hheld.country_codes ` |                       | countries where this  |
|                       |                       | content is not        |
|                       |                       | available.            |
+-----------------------+-----------------------+-----------------------+
| ` withheld.scope `    | enum ( ` tweet ` ,    | Indicates whether the |
|                       | ` user ` )            | content being         |
|                       |                       | withheld is a Tweet   |
|                       |                       | or a user.            |
+-----------------------+-----------------------+-----------------------+
| ` note_tweet `        | object                | Information for       |
|                       |                       | Tweets longer than    |
|                       |                       | 280 characters.       |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` twee                |
|                       |                       | t.fields=note_tweet ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` note_tweet.text `   | string                | The text for Tweets   |
|                       |                       | longer than 280       |
|                       |                       | characters.           |
+-----------------------+-----------------------+-----------------------+
| `                     | object                | Contains details      |
| note_tweet.entities ` |                       | about text that has a |
|                       |                       | special meaning in a  |
|                       |                       | Tweet.                |
+-----------------------+-----------------------+-----------------------+
| ` note_               | array                 | Contains details      |
| tweet.entities.urls ` |                       | about text recognized |
|                       |                       | as a URL.             |
+-----------------------+-----------------------+-----------------------+
| ` note_twee           | array                 | Contains details      |
| t.entities.mentions ` |                       | about text recognized |
|                       |                       | as a user mention.    |
+-----------------------+-----------------------+-----------------------+
| ` note_twee           | array                 | Contains details      |
| t.entities.hashtags ` |                       | about text recognized |
|                       |                       | as a Hashtag.         |
+-----------------------+-----------------------+-----------------------+
| ` note_twee           | array                 | Contains details      |
| t.entities.cashtags ` |                       | about text recognized |
|                       |                       | as a Cashtag.         |
+-----------------------+-----------------------+-----------------------+
| ` public_metrics `    | object                | Engagement metrics    |
|                       |                       | for the Tweet at the  |
|                       |                       | time of the request.  |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` tweet.fi            |
|                       |                       | elds=public_metrics ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` public_me           | integer               | Number of times this  |
| trics.retweet_count ` |                       | Tweet has been        |
|                       |                       | Retweeted.            |
+-----------------------+-----------------------+-----------------------+
| ` public_             | integer               | Number of Replies of  |
| metrics.reply_count ` |                       | this Tweet.           |
+-----------------------+-----------------------+-----------------------+
| ` public              | integer               | Number of Likes of    |
| _metrics.like_count ` |                       | this Tweet.           |
+-----------------------+-----------------------+-----------------------+
| ` public_             | integer               | Number of times this  |
| metrics.quote_count ` |                       | Tweet has been        |
|                       |                       | Retweeted with a      |
|                       |                       | comment (also known   |
|                       |                       | as Quote).            |
+-----------------------+-----------------------+-----------------------+
| ` public_metri        | integer               | Number of times this  |
| cs.impression_count ` |                       | Tweet has been        |
|                       |                       | viewed.               |
+-----------------------+-----------------------+-----------------------+
| ` public_met          | integer               | Number of times this  |
| rics.bookmark_count ` |                       | Tweet has been        |
|                       |                       | bookmarked.           |
+-----------------------+-----------------------+-----------------------+
| `                     | object                | Non-public engagement |
|  non_public_metrics ` |                       | metrics for the Tweet |
|                       |                       | at the time of the    |
|                       |                       | request. This is a    |
|                       |                       | private metric and    |
|                       |                       | requires the use of   |
|                       |                       | OAuth 2.0 User        |
|                       |                       | Context               |
|                       |                       | authentication. This  |
|                       |                       | metric is only        |
|                       |                       | available for Tweets  |
|                       |                       | created by the        |
|                       |                       | authenticating user   |
|                       |                       | in the last 30 days.  |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` tweet.fields        |
|                       |                       | =non_public_metrics ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` non_public_metri    | integer               | Number of times the   |
| cs.impression_count ` |                       | Tweet has been        |
|                       |                       | viewed. This requires |
|                       |                       | the use of OAuth 2.0  |
|                       |                       | User Context          |
|                       |                       | authentication. This  |
|                       |                       | metric is only        |
|                       |                       | available for Tweets  |
|                       |                       | created by the        |
|                       |                       | authenticating user   |
|                       |                       | in the last 30 days.  |
+-----------------------+-----------------------+-----------------------+
| ` non_public_metr     | integer               | Number of times a     |
| ics.url_link_clicks ` |                       | user clicks on a URL  |
|                       |                       | link or URL preview   |
|                       |                       | card in a Tweet. This |
|                       |                       | is a private metric,  |
|                       |                       | and requires the use  |
|                       |                       | of OAuth 2.0 User     |
|                       |                       | Context               |
|                       |                       | authentication. This  |
|                       |                       | metric is only        |
|                       |                       | available for Tweets  |
|                       |                       | created by the        |
|                       |                       | authenticating user   |
|                       |                       | in the last 30 days.  |
+-----------------------+-----------------------+-----------------------+
| ` non_public_metrics. | integer               | Number of times a     |
| user_profile_clicks ` |                       | user clicks the       |
|                       |                       | following portions of |
|                       |                       | a Tweet - display     |
|                       |                       | name, user name,      |
|                       |                       | profile picture. This |
|                       |                       | is a private metric,  |
|                       |                       | and requires the use  |
|                       |                       | of OAuth 2.0 User     |
|                       |                       | Context               |
|                       |                       | authentication. This  |
|                       |                       | metric is only        |
|                       |                       | available for Tweets  |
|                       |                       | created by the        |
|                       |                       | authenticating user   |
|                       |                       | in the last 30 days.  |
+-----------------------+-----------------------+-----------------------+
| ` organic_metrics `   | object                | Organic engagement    |
|                       |                       | metrics for the Tweet |
|                       |                       | at the time of the    |
|                       |                       | request. Requires     |
|                       |                       | user context          |
|                       |                       | authentication. This  |
|                       |                       | metric is only        |
|                       |                       | available for Tweets  |
|                       |                       | created by the        |
|                       |                       | authenticating user   |
|                       |                       | in the last 30 days.  |
+-----------------------+-----------------------+-----------------------+
| ` organic_metri       | integer               | Number of times the   |
| cs.impression_count ` |                       | Tweet has been viewed |
|                       |                       | organically. This is  |
|                       |                       | a private metric, and |
|                       |                       | requires the use of   |
|                       |                       | OAuth 2.0 User        |
|                       |                       | Context               |
|                       |                       | authentication. This  |
|                       |                       | metric is only        |
|                       |                       | available for Tweets  |
|                       |                       | created by the        |
|                       |                       | authenticating user   |
|                       |                       | in the last 30 days.  |
+-----------------------+-----------------------+-----------------------+
| ` organic_metr        | integer               | Number of times a     |
| ics.url_link_clicks ` |                       | user clicks on a URL  |
|                       |                       | link or URL preview   |
|                       |                       | card in a Tweet       |
|                       |                       | organically. This is  |
|                       |                       | a private metric, and |
|                       |                       | requires the use of   |
|                       |                       | OAuth 2.0 User        |
|                       |                       | Context               |
|                       |                       | authentication. This  |
|                       |                       | metric is only        |
|                       |                       | available for Tweets  |
|                       |                       | created by the        |
|                       |                       | authenticating user   |
|                       |                       | in the last 30 days.  |
+-----------------------+-----------------------+-----------------------+
| ` organic_metrics.    | integer               | Number of times a     |
| user_profile_clicks ` |                       | user clicks the       |
|                       |                       | following portions of |
|                       |                       | a Tweet organically - |
|                       |                       | display name, user    |
|                       |                       | name, profile         |
|                       |                       | picture. This is a    |
|                       |                       | private metric, and   |
|                       |                       | requires the use of   |
|                       |                       | OAuth 2.0 User        |
|                       |                       | Context               |
|                       |                       | authentication. This  |
|                       |                       | metric is only        |
|                       |                       | available for Tweets  |
|                       |                       | created by the        |
|                       |                       | authenticating user   |
|                       |                       | in the last 30 days.  |
+-----------------------+-----------------------+-----------------------+
| ` organic_me          | integer               | Number of times the   |
| trics.retweet_count ` |                       | Tweet has been        |
|                       |                       | Retweeted             |
|                       |                       | organically. This     |
|                       |                       | metric is only        |
|                       |                       | available for Tweets  |
|                       |                       | created by the        |
|                       |                       | authenticating user   |
|                       |                       | in the last 30 days.  |
+-----------------------+-----------------------+-----------------------+
| ` organic_            | integer               | Number of replies the |
| metrics.reply_count ` |                       | Tweet has received    |
|                       |                       | organically. This     |
|                       |                       | metric is only        |
|                       |                       | available for Tweets  |
|                       |                       | created by the        |
|                       |                       | authenticating user   |
|                       |                       | in the last 30 days.  |
+-----------------------+-----------------------+-----------------------+
| ` organic             | integer               | Number of likes the   |
| _metrics.like_count ` |                       | Tweet has received    |
|                       |                       | organically. This     |
|                       |                       | metric is only        |
|                       |                       | available for Tweets  |
|                       |                       | created by the        |
|                       |                       | authenticating user   |
|                       |                       | in the last 30 days.  |
+-----------------------+-----------------------+-----------------------+
| ` promoted_metrics `  | object                | Engagement metrics    |
|                       |                       | for the Tweet at the  |
|                       |                       | time of the request   |
|                       |                       | in a promoted         |
|                       |                       | context. Requires     |
|                       |                       | user context          |
|                       |                       | authentication. This  |
|                       |                       | metric is only        |
|                       |                       | available for Tweets  |
|                       |                       | created by the        |
|                       |                       | authenticating user   |
|                       |                       | in the last 30 days.  |
+-----------------------+-----------------------+-----------------------+
| ` promoted_metri      | integer               | Number of times the   |
| cs.impression_count ` |                       | Tweet has been viewed |
|                       |                       | when that Tweet is    |
|                       |                       | being promoted. This  |
|                       |                       | is a private metric,  |
|                       |                       | and requires the use  |
|                       |                       | of OAuth 2.0 User     |
|                       |                       | Context               |
|                       |                       | authentication. This  |
|                       |                       | metric is only        |
|                       |                       | available for Tweets  |
|                       |                       | created by the        |
|                       |                       | authenticating user   |
|                       |                       | in the last 30 days.  |
+-----------------------+-----------------------+-----------------------+
| ` promoted_metr       | integer               | Number of times a     |
| ics.url_link_clicks ` |                       | user clicks on a URL  |
|                       |                       | link or URL preview   |
|                       |                       | card in a Tweet when  |
|                       |                       | it is being promoted. |
|                       |                       | This is a private     |
|                       |                       | metric, and requires  |
|                       |                       | the use of OAuth 2.0  |
|                       |                       | User Context          |
|                       |                       | authentication. This  |
|                       |                       | metric is only        |
|                       |                       | available for Tweets  |
|                       |                       | created by the        |
|                       |                       | authenticating user   |
|                       |                       | in the last 30 days.  |
+-----------------------+-----------------------+-----------------------+
| ` promoted_metrics.   | integer               | Number of times a     |
| user_profile_clicks ` |                       | user clicks the       |
|                       |                       | following portions of |
|                       |                       | a Tweet when it is    |
|                       |                       | being promoted -      |
|                       |                       | display name, user    |
|                       |                       | name, profile         |
|                       |                       | picture. This is a    |
|                       |                       | private metric, and   |
|                       |                       | requires the use of   |
|                       |                       | OAuth 2.0 User        |
|                       |                       | Context               |
|                       |                       | authentication. This  |
|                       |                       | metric is only        |
|                       |                       | available for Tweets  |
|                       |                       | created by the        |
|                       |                       | authenticating user   |
|                       |                       | in the last 30 days.  |
+-----------------------+-----------------------+-----------------------+
| ` promoted_me         | integer               | Number of times this  |
| trics.retweet_count ` |                       | Tweet has been        |
|                       |                       | Retweeted when that   |
|                       |                       | Tweet is being        |
|                       |                       | promoted. This metric |
|                       |                       | is only available for |
|                       |                       | Tweets created by the |
|                       |                       | authenticating user   |
|                       |                       | in the last 30 days.  |
+-----------------------+-----------------------+-----------------------+
| ` promoted_           | integer               | Number of Replies to  |
| metrics.reply_count ` |                       | this Tweet when that  |
|                       |                       | Tweet is being        |
|                       |                       | promoted. This metric |
|                       |                       | is only available for |
|                       |                       | Tweets created by the |
|                       |                       | authenticating user   |
|                       |                       | in the last 30 days.  |
+-----------------------+-----------------------+-----------------------+
| ` promoted            | integer               | Number of Likes of    |
| _metrics.like_count ` |                       | this Tweet when that  |
|                       |                       | Tweet is being        |
|                       |                       | promoted.             |
+-----------------------+-----------------------+-----------------------+
| `                     | boolean               | Indicates if this     |
|  possibly_sensitive ` |                       | Tweet contains URLs   |
|                       |                       | marked as sensitive,  |
|                       |                       | for example content   |
|                       |                       | suitable for mature   |
|                       |                       | audiences.            |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` tweet.fields        |
|                       |                       | =possibly_sensitive ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` lang `              | string                | Language of the       |
|                       |                       | Tweet, if detected by |
|                       |                       | Twitter. Returned as  |
|                       |                       | a BCP47 language tag. |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` tweet.fields=lang ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` reply_settings `    | string                | Shows who can reply   |
|                       |                       | to this Tweet. Fields |
|                       |                       | returned are          |
|                       |                       | ` everyone ` ,        |
|                       |                       | ` mentionedUsers ` ,  |
|                       |                       | and ` following ` .   |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` tweet.fi            |
|                       |                       | elds=reply_settings ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` source `            | string                | The name of the app   |
|                       |                       | the user Tweeted      |
|                       |                       | from.                 |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | `                     |
|                       |                       | tweet.fields=source ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` includes `          | object                | If you include an     |
|                       |                       | ` `[`expan            |
|                       |                       | sion`](/en/docs/twitt |
|                       |                       | er-api/expansions)` ` |
|                       |                       | parameter, the        |
|                       |                       | referenced objects    |
|                       |                       | will be returned if   |
|                       |                       | available.            |
+-----------------------+-----------------------+-----------------------+
| ` includes.tweets `   | array                 | When including the    |
|                       |                       | ` expansions=r        |
|                       |                       | eferenced_tweets.id ` |
|                       |                       | parameter, this       |
|                       |                       | includes a list of    |
|                       |                       | referenced Retweets,  |
|                       |                       | Quoted Tweets, or     |
|                       |                       | replies in the form   |
|                       |                       | of [Tweet             |
|                       |                       | ob                    |
|                       |                       | jects](/en/docs/twitt |
|                       |                       | er-api/data-dictionar |
|                       |                       | y/object-model/tweet) |
|                       |                       | with their default    |
|                       |                       | fields and any        |
|                       |                       | additional fields     |
|                       |                       | requested using the   |
|                       |                       | ` tweet.fields `      |
|                       |                       | parameter, assuming   |
|                       |                       | there is a referenced |
|                       |                       | Tweet present in the  |
|                       |                       | returned Tweet(s).    |
+-----------------------+-----------------------+-----------------------+
| ` includes.users `    | array                 | When including the    |
|                       |                       | ` e                   |
|                       |                       | xpansions=author_id ` |
|                       |                       | parameter, this       |
|                       |                       | includes a list of    |
|                       |                       | referenced Tweet      |
|                       |                       | authors in the form   |
|                       |                       | of [user              |
|                       |                       | o                     |
|                       |                       | bjects](/en/docs/twit |
|                       |                       | ter-api/data-dictiona |
|                       |                       | ry/object-model/user) |
|                       |                       | with their default    |
|                       |                       | fields and any        |
|                       |                       | additional fields     |
|                       |                       | requested using the   |
|                       |                       | ` user.fields `       |
|                       |                       | parameter.            |
+-----------------------+-----------------------+-----------------------+
| ` includes.places `   | array                 | When including the    |
|                       |                       | ` expa                |
|                       |                       | nsions=geo.place_id ` |
|                       |                       | parameter, this       |
|                       |                       | includes a list of    |
|                       |                       | referenced places in  |
|                       |                       | Tweets in the form of |
|                       |                       | [place                |
|                       |                       | ob                    |
|                       |                       | jects](/en/docs/twitt |
|                       |                       | er-api/data-dictionar |
|                       |                       | y/object-model/place) |
|                       |                       | with their default    |
|                       |                       | fields and any        |
|                       |                       | additional fields     |
|                       |                       | requested using the   |
|                       |                       | ` place.fields `      |
|                       |                       | parameter, assuming   |
|                       |                       | there is a place      |
|                       |                       | present in the        |
|                       |                       | returned Tweet(s).    |
+-----------------------+-----------------------+-----------------------+
| ` includes.media `    | array                 | When including the    |
|                       |                       | ` expansions=att      |
|                       |                       | achments.media_keys ` |
|                       |                       | parameter, this       |
|                       |                       | includes a list of    |
|                       |                       | images, videos, and   |
|                       |                       | GIFs included in      |
|                       |                       | Tweets in the form of |
|                       |                       | [media                |
|                       |                       | ob                    |
|                       |                       | jects](/en/docs/twitt |
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
+-----------------------+-----------------------+-----------------------+
| ` includes.polls `    | string                | When including the    |
|                       |                       | ` expansions=a        |
|                       |                       | ttachments.poll_ids ` |
|                       |                       | parameter, this       |
|                       |                       | includes a list of    |
|                       |                       | polls that are        |
|                       |                       | attached to Tweets in |
|                       |                       | the form of [poll     |
|                       |                       | o                     |
|                       |                       | bjects](/en/docs/twit |
|                       |                       | ter-api/data-dictiona |
|                       |                       | ry/object-model/poll) |
|                       |                       | with their default    |
|                       |                       | fields and any        |
|                       |                       | additional fields     |
|                       |                       | requested using the   |
|                       |                       | ` poll.fields `       |
|                       |                       | parameter, assuming   |
|                       |                       | there is a poll       |
|                       |                       | present in the        |
|                       |                       | returned Tweet(s).    |
+-----------------------+-----------------------+-----------------------+
| ` meta `\             | object                | This object contains  |
| [Default]{.small}     |                       | information about the |
|                       |                       | number of users       |
|                       |                       | returned in the       |
|                       |                       | current request and   |
|                       |                       | pagination details.   |
+-----------------------+-----------------------+-----------------------+
| ` meta.count `\       | integer               | The number of Tweet   |
| [Default]{.small}     |                       | results returned in   |
|                       |                       | the response.         |
+-----------------------+-----------------------+-----------------------+
| ` meta.newest_id `\   | string                | The Tweet ID of the   |
| [Default]{.small}     |                       | most recent Tweet     |
|                       |                       | returned in the       |
|                       |                       | response.             |
+-----------------------+-----------------------+-----------------------+
| ` meta.oldest_id `\   | string                | The Tweet ID of the   |
| [Default]{.small}     |                       | oldest Tweet returned |
|                       |                       | in the response.      |
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
| ` errors `            | object                | Contains details      |
|                       |                       | about errors that     |
|                       |                       | affected any of the   |
|                       |                       | requested Tweets. See |
|                       |                       | [Status codes and     |
|                       |                       | error                 |
|                       |                       | messages](/en/        |
|                       |                       | support/twitter-api/e |
|                       |                       | rror-troubleshooting) |
|                       |                       | for more details.     |
+-----------------------+-----------------------+-----------------------+
:::
:::
:::
