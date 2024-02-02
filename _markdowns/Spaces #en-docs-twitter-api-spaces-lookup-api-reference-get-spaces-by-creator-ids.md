::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Returns live or scheduled Spaces created by the specified user IDs. Up
to 100 comma-separated IDs can be looked up using this endpoint.

### Endpoint URL

` https://api.twitter.com/2/spaces/by/creator_ids `

+-----------------------------------+-----------------------------------+
| Authentication methods\           | [OAuth 2.0 Authorization Code     |
| supported by this endpoint        | with                              |
|                                   | PKCE](/en/docs/authenticat        |
|                                   | ion/oauth-2-0/authorization-code) |
|                                   |                                   |
|                                   | [OAuth 2.0                        |
|                                   | App-only](/en/docs/authentic      |
|                                   | ation/oauth-2-0/application-only) |
|                                   |                                   |
|                                   | This is not an auth method but a  |
|                                   | shared rate limit between user    |
|                                   | and application-only              |
+-----------------------------------+-----------------------------------+
| [Rate                             | User rate limit (User context):   |
| limit](/en/docs/rate-limits)      | 300 requests per 15-minute window |
|                                   | per each authenticated user       |
|                                   |                                   |
|                                   | App rate limit                    |
|                                   | (Application-only): 300 requests  |
|                                   | per 15-minute window shared among |
|                                   | all users of your app             |
|                                   |                                   |
|                                   | Shared rate limit: 1 per second   |
|                                   | among all users of your app       |
+-----------------------------------+-----------------------------------+

+-----------------------+-----------------------+-----------------------+
| Name                  | Type                  | Description           |
+-----------------------+-----------------------+-----------------------+
| ` user_ids `\         | string                | A comma separated     |
| [Required]{.small}    |                       | list of user IDs (up  |
|                       |                       | to 100).              |
+-----------------------+-----------------------+-----------------------+
| ` expansions `\       | enum (                | [Ex                   |
| [Optional]{.small}    | ` invited_user_ids `  | pansions](/en/docs/tw |
|                       | , ` speaker_ids ` ,   | itter-api/expansions) |
|                       | ` creator_id ` ,      | enable you to request |
|                       | ` host_ids ` ,        | additional data       |
|                       | ` topics_ids ` )      | objects that relate   |
|                       |                       | to the originally     |
|                       |                       | returned Space.       |
|                       |                       | Submit a list of      |
|                       |                       | desired expansions in |
|                       |                       | a comma-separated     |
|                       |                       | list. The ID that     |
|                       |                       | represents the        |
|                       |                       | expanded data object  |
|                       |                       | will be included      |
|                       |                       | directly in the Space |
|                       |                       | data object, but the  |
|                       |                       | expanded object       |
|                       |                       | metadata will be      |
|                       |                       | returned within the   |
|                       |                       | ` includes ` response |
|                       |                       | object, and will also |
|                       |                       | include the ID so     |
|                       |                       | that you can match    |
|                       |                       | this data object to   |
|                       |                       | the original Space    |
|                       |                       | object. The following |
|                       |                       | data objects can be   |
|                       |                       | expanded using this   |
|                       |                       | parameter:            |
|                       |                       |                       |
|                       |                       | -   The Spaces        |
|                       |                       |     creator\'s user   |
|                       |                       |     object            |
|                       |                       | -   The user objects  |
|                       |                       |     of any Space      |
|                       |                       |     co-host           |
|                       |                       | -   Any mentioned     |
|                       |                       |     users' object     |
|                       |                       | -   Any speaker\'s    |
|                       |                       |     user object       |
+-----------------------+-----------------------+-----------------------+
| ` space.fields `\     | enum ( ` host_ids ` , | This                  |
| [Optional]{.small}    | ` created_at ` ,      | [fields](/en/doc      |
|                       | ` creator_id ` ,      | s/twitter-api/fields) |
|                       | ` id ` , ` lang ` ,   | parameter enables you |
|                       | ` invited_user_ids `  | to select which       |
|                       | ,                     | specific [Space       |
|                       | ` participant_count ` | f                     |
|                       | , ` speaker_ids ` ,   | ields](/en/docs/twitt |
|                       | ` started_at ` ,      | er-api/data-dictionar |
|                       | ` ended_at ` ,        | y/object-model/space) |
|                       | ` subscriber_count `  | will deliver in each  |
|                       | , ` topic_ids ` ,     | returned Space.       |
|                       | ` state ` , ` title ` | Specify the desired   |
|                       | , ` updated_at ` ,    | fields in a           |
|                       | ` scheduled_start ` , | comma-separated list. |
|                       | ` is_ticketed ` )     |                       |
+-----------------------+-----------------------+-----------------------+
| ` topic.fields `\     | enum ( ` id ` ,       | This                  |
| [Optional]{.small}    | ` name ` ,            | [fields](/en/doc      |
|                       | ` description ` )     | s/twitter-api/fields) |
|                       |                       | parameter enables you |
|                       |                       | to select which       |
|                       |                       | specific topic        |
|                       |                       | metadata in each      |
|                       |                       | returned Space topic  |
|                       |                       | object, if the        |
|                       |                       | creator of the Space  |
|                       |                       | set one or more       |
|                       |                       | topics. Specify the   |
|                       |                       | desired fields in a   |
|                       |                       | comma-separated list. |
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
|                       | ` public_metrics ` ,  | returned Space.       |
|                       | ` url ` ,             | Specify the desired   |
|                       | ` username ` ,        | fields in a           |
|                       | ` verified ` ,        | comma-separated list  |
|                       | ` verified_type ` ,   | without spaces        |
|                       | ` withheld ` )        | between commas and    |
|                       |                       | fields. While the     |
|                       |                       | user ID will be       |
|                       |                       | located in the        |
|                       |                       | original Space        |
|                       |                       | object, you will find |
|                       |                       | this ID and all       |
|                       |                       | additional user       |
|                       |                       | fields in the         |
|                       |                       | ` includes ` data     |
|                       |                       | object.               |
+-----------------------+-----------------------+-----------------------+
:::
:::

::: c01-rich-text-editor
::: is-table-default
+-----------------------+-----------------------+-----------------------+
| Name                  | Type                  | Description           |
+-----------------------+-----------------------+-----------------------+
| ` id `\               | string                | Unique identifier of  |
| [Default]{.small}     |                       | this Space.           |
+-----------------------+-----------------------+-----------------------+
| ` host_ids `          | array                 | An array containing   |
|                       |                       | the user ID of each   |
|                       |                       | Space co-host. These  |
|                       |                       | IDs are returned as   |
|                       |                       | strings in order to   |
|                       |                       | avoid complications   |
|                       |                       | with languages and    |
|                       |                       | tools that cannot     |
|                       |                       | handle large          |
|                       |                       | integers.             |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` sp                  |
|                       |                       | ace.fields=host_ids ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
|                       |                       |                       |
|                       |                       | You can obtain the    |
|                       |                       | expanded object in    |
|                       |                       | ` includes.users ` by |
|                       |                       | adding                |
|                       |                       | `                     |
|                       |                       | expansions=host_ids ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` created_at `        | date (ISO 8601)       | Creation date and     |
|                       |                       | time of this Space.   |
|                       |                       | For scheduled Spaces, |
|                       |                       | this indicates the    |
|                       |                       | time the Space was    |
|                       |                       | created, not the time |
|                       |                       | when the Space will   |
|                       |                       | start.                |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` spac                |
|                       |                       | e.fields=created_at ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` creator_id `        | string                | The user ID of the    |
|                       |                       | account that created  |
|                       |                       | this Space. This ID   |
|                       |                       | is returned as a      |
|                       |                       | string in order to    |
|                       |                       | avoid complications   |
|                       |                       | with languages and    |
|                       |                       | tools that cannot     |
|                       |                       | handle large          |
|                       |                       | integers.             |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` spac                |
|                       |                       | e.fields=creator_id ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
|                       |                       |                       |
|                       |                       | You can obtain the    |
|                       |                       | expanded object in    |
|                       |                       | ` includes.users ` by |
|                       |                       | adding                |
|                       |                       | ` ex                  |
|                       |                       | pansions=creator_id ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` ended_at `          | date (ISO 8601)       | End date and time of  |
|                       |                       | this Space. This      |
|                       |                       | field will be only    |
|                       |                       | present for Spaces in |
|                       |                       | the ` ended ` state.  |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` sp                  |
|                       |                       | ace.fields=ended_at ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` lang `              | string                | Main language of the  |
|                       |                       | Space's creator, as   |
|                       |                       | inferred by Twitter   |
|                       |                       | (this may differ from |
|                       |                       | the language spoken   |
|                       |                       | in the Space).        |
|                       |                       | Returned as a BCP 47  |
|                       |                       | language tag.         |
|                       |                       | Supported values:     |
|                       |                       |                       |
|                       |                       | -   Arabic ` (ar) `   |
|                       |                       | -   Armenian ` (hy) ` |
|                       |                       | -   Chinese ` (zh) `  |
|                       |                       | -   Danish ` (da) `   |
|                       |                       | -   English ` (en) `  |
|                       |                       | -   Finnish ` (fi) `  |
|                       |                       | -   French ` (fr) `   |
|                       |                       | -   German ` (de) `   |
|                       |                       | -   Hindi ` (hi) `    |
|                       |                       | -   Hebrew ` (iw) `   |
|                       |                       | -   Indonesian        |
|                       |                       |     ` (in) `          |
|                       |                       | -   Italian ` (it) `  |
|                       |                       | -   Japanese ` (ja) ` |
|                       |                       | -   Kazakh ` (kk) `   |
|                       |                       | -   Korean ` (ko) `   |
|                       |                       | -   Norwegian         |
|                       |                       |     ` (no) `          |
|                       |                       | -   Polish ` (pl) `   |
|                       |                       | -   Portuguese        |
|                       |                       |     ` (pt) `          |
|                       |                       | -   Romanian ` (ro) ` |
|                       |                       | -   Russian ` (ru) `  |
|                       |                       | -   Spanish ` (es) `  |
|                       |                       | -   Swedish ` (sv) `  |
|                       |                       | -   Turkish ` (tr) `  |
|                       |                       | -   Ukranian ` (uk) ` |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` space.fields=lang ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` is_ticketed `       | boolean               | Indicates if this is  |
|                       |                       | a ticketed Space.     |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` space               |
|                       |                       | .fields=is_ticketed ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` invited_user_ids `  | array                 | The list of user IDs  |
|                       |                       | that can              |
|                       |                       | automatically join as |
|                       |                       | Speakers. Usually,    |
|                       |                       | users in this list    |
|                       |                       | are invited to speak  |
|                       |                       | via the Invite user   |
|                       |                       | option and have a     |
|                       |                       | Speaker role when the |
|                       |                       | Space starts. These   |
|                       |                       | IDs are returned as   |
|                       |                       | strings in order to   |
|                       |                       | avoid complications   |
|                       |                       | with languages and    |
|                       |                       | tools that cannot     |
|                       |                       | handle large          |
|                       |                       | integers.             |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` space.fiel          |
|                       |                       | ds=invited_user_ids ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
|                       |                       |                       |
|                       |                       | You can obtain the    |
|                       |                       | expanded object in    |
|                       |                       | ` includes.users ` by |
|                       |                       | adding                |
|                       |                       | ` expansio            |
|                       |                       | ns=invited_user_ids ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` participant_count ` | integer               | The current number of |
|                       |                       | users in the Space,   |
|                       |                       | including Hosts and   |
|                       |                       | Speakers.             |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` space.field         |
|                       |                       | s=participant_count ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` scheduled_start `   | date (ISO 8601)       | Indicates the         |
|                       |                       | scheduled start time  |
|                       |                       | of a Space. This      |
|                       |                       | field is returned     |
|                       |                       | only if the Space has |
|                       |                       | been scheduled; in    |
|                       |                       | other words, if the   |
|                       |                       | field is returned, it |
|                       |                       | means the Space is a  |
|                       |                       | scheduled Space.      |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` space.fie           |
|                       |                       | lds=scheduled_start ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` speaker_ids `       | array                 | The list of users who |
|                       |                       | were speaking at any  |
|                       |                       | point during the      |
|                       |                       | Space. This list      |
|                       |                       | contains all the      |
|                       |                       | users in              |
|                       |                       | ` invited_user_ids `  |
|                       |                       | in addition to any    |
|                       |                       | user who requested to |
|                       |                       | speak and was allowed |
|                       |                       | via the Add speaker   |
|                       |                       | option. These IDs are |
|                       |                       | returned as strings   |
|                       |                       | in order to avoid     |
|                       |                       | complications with    |
|                       |                       | languages and tools   |
|                       |                       | that cannot handle    |
|                       |                       | large integers.These  |
|                       |                       | IDs are returned as   |
|                       |                       | strings in order to   |
|                       |                       | avoid complications   |
|                       |                       | with languages and    |
|                       |                       | tools that cannot     |
|                       |                       | handle large          |
|                       |                       | integers.             |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` space               |
|                       |                       | .fields=speaker_ids ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
|                       |                       |                       |
|                       |                       | You can obtain the    |
|                       |                       | expanded object in    |
|                       |                       | ` includes.users ` by |
|                       |                       | adding                |
|                       |                       | ` exp                 |
|                       |                       | ansions=speaker_ids ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` started_at `        | date (ISO 8601)       | The start date and    |
|                       |                       | time of the Space.    |
|                       |                       | Only available if the |
|                       |                       | space has started.    |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` spac                |
|                       |                       | e.fields=started_at ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` state `\            | enum ( ` live ` ,     | Indicates whether the |
| [Default]{.small}     | ` scheduled ` )       | Space is scheduled    |
|                       |                       | and hasn't started    |
|                       |                       | yet ( ` scheduled ` ) |
|                       |                       | or if it's in         |
|                       |                       | progress ( ` live `   |
|                       |                       | ).                    |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | `                     |
|                       |                       |  space.fields=state ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` subscriber_count `  | integer               | Indicates the number  |
|                       |                       | of people who set a   |
|                       |                       | remainder to this     |
|                       |                       | Space. This field can |
|                       |                       | only be requested if  |
|                       |                       | your app is authentic |
|                       |                       | the request using the |
|                       |                       | Access Token of the   |
|                       |                       | creator of the Space. |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` space.fiel          |
|                       |                       | ds=subscriber_count ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` topic_ids `         | string                | A list of the Space   |
|                       |                       | topic IDs, if set by  |
|                       |                       | the creator of the    |
|                       |                       | Space.                |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` spa                 |
|                       |                       | ce.fields=topic_ids ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` topics.id `         | string                | The ID of the Space   |
|                       |                       | topic.                |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` top                 |
|                       |                       | ic.fields=topics.id ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
|                       |                       |                       |
|                       |                       | You can obtain the    |
|                       |                       | expanded object in    |
|                       |                       | ` includes.topics `   |
|                       |                       | by adding             |
|                       |                       | ` expansions=topics ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` topics.id `         | string                | The ID of the Space   |
|                       |                       | topic.                |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` top                 |
|                       |                       | ic.fields=topics.id ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
|                       |                       |                       |
|                       |                       | You can obtain the    |
|                       |                       | expanded object in    |
|                       |                       | ` includes.topics `   |
|                       |                       | by adding             |
|                       |                       | ` expansions=topics ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` topics.name `       | string                | The name of the Space |
|                       |                       | topic.                |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` topic               |
|                       |                       | .fields=topics.name ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
|                       |                       |                       |
|                       |                       | You can obtain the    |
|                       |                       | expanded object in    |
|                       |                       | ` includes.topics `   |
|                       |                       | by adding             |
|                       |                       | ` expansions=topics ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` topics.name `       | string                | A full text           |
|                       |                       | description of the    |
|                       |                       | Space topic.          |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` topic               |
|                       |                       | .fields=topics.name ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
|                       |                       |                       |
|                       |                       | You can obtain the    |
|                       |                       | expanded object in    |
|                       |                       | ` includes.topics `   |
|                       |                       | by adding             |
|                       |                       | ` expansions=topics ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` title `             | string                | The title of this     |
|                       |                       | Space as specified by |
|                       |                       | the creator.          |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | `                     |
|                       |                       |  space.fields=title ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` updated_at `        | date (ISO 8601)       | The timestamp of the  |
|                       |                       | last update to any of |
|                       |                       | this Space\'s         |
|                       |                       | metadata, such as the |
|                       |                       | title or scheduled    |
|                       |                       | time.                 |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` spac                |
|                       |                       | e.fields=updated_at ` |
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
