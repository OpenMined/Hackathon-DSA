::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Returns a list of Tweets from the specified List.

### Endpoint URL

` https://api.twitter.com/2/lists/:id/tweets `

  ----------------------- ----------------------- -----------------------
  Name                    Type                    Description

  ` id `\                 string                  The ID of the List
  [Required]{.small}                              whose Tweets you would
                                                  like to retrieve.
  ----------------------- ----------------------- -----------------------

  ----------------------- ------------------------------------ ------------------------------------------------------------------
  Name                    Type                                 Description

  ` expansions `\         enum ( ` attachments.poll_ids ` ,    [Expansions](/en/docs/twitter-api/expansions) enable you to
  [Optional]{.small}      ` attachments.media_keys ` ,         request additional data objects that relate to the originally
                          ` author_id ` ,                      returned users. The ID that represents the expanded data object
                          ` edit_history_tweet_ids ` ,         will be included directly in the user data object, but the
                          ` entities.mentions.username ` ,     expanded object metadata will be returned within the ` includes `
                          ` geo.place_id ` ,                   response object, and will also include the ID so that you can
                          ` in_reply_to_user_id ` ,            match this data object to the original Tweet object. At this time,
                          ` referenced_tweets.id ` ,           the only expansion available to endpoints that primarily return
                          ` referenced_tweets.id.author_id ` ) user objects is ` expansions=pinned_tweet_id ` . You will find the
                                                               expanded Tweet data object living in the ` includes ` response
                                                               object.

  ` max_results `\        integer                              The maximum number of results to be returned per page. This can be
  [Optional]{.small}                                           a number between 1 and 100. By default, each page will return 100
                                                               results.

  ` media.fields `\       enum ( ` duration_ms ` , ` height `  This [fields](/en/docs/twitter-api/fields) parameter enables you
  [Optional]{.small}      , ` media_key ` ,                    to select which specific [media
                          ` preview_image_url ` , ` type ` ,   fields](/en/docs/twitter-api/data-dictionary/object-model/media)
                          ` url ` , ` width ` ,                will deliver in each returned Tweet. Specify the desired fields in
                          ` public_metrics ` ,                 a comma-separated list without spaces between commas and fields.
                          ` non_public_metrics ` ,             The Tweet will only return media fields if the Tweet contains
                          ` organic_metrics ` ,                media and if you\'ve also included the
                          ` promoted_metrics ` , ` alt_text `  ` expansions=attachments.media_keys ` query parameter in your
                          , ` variants ` )                     request. While the media ID will be located in the Tweet object,
                                                               you will find this ID and all additional media fields in the
                                                               ` includes ` data object.

  ` pagination_token `\   string                               Used to request the next page of results if all results weren\'t
  [Optional]{.small}                                           returned with the latest request, or to go back to the previous
                                                               page of results. To return the next page, pass the next_token
                                                               returned in your previous response. To go back one page, pass the
                                                               previous_token returned in your previous response.

  ` place.fields `\       enum ( ` contained_within ` ,        This [fields](/en/docs/twitter-api/fields) parameter enables you
  [Optional]{.small}      ` country ` , ` country_code ` ,     to select which specific [place
                          ` full_name ` , ` geo ` , ` id ` ,   fields](/en/docs/twitter-api/data-dictionary/object-model/place)
                          ` name ` , ` place_type ` )          will deliver in each returned Tweet. Specify the desired fields in
                                                               a comma-separated list without spaces between commas and fields.
                                                               The Tweet will only return place fields if the Tweet contains a
                                                               place and if you\'ve also included the ` expansions=geo.place_id `
                                                               query parameter in your request. While the place ID will be
                                                               located in the Tweet object, you will find this ID and all
                                                               additional place fields in the ` includes ` data object.

  ` poll.fields `\        enum ( ` duration_minutes ` ,        This [fields](/en/docs/twitter-api/fields) parameter enables you
  [Optional]{.small}      ` end_datetime ` , ` id ` ,          to select which specific [poll
                          ` options ` , ` voting_status ` )    fields](/en/docs/twitter-api/data-dictionary/object-model/poll)
                                                               will deliver in each returned Tweet. Specify the desired fields in
                                                               a comma-separated list without spaces between commas and fields.
                                                               The Tweet will only return poll fields if the Tweet contains a
                                                               poll and if you\'ve also included the
                                                               ` expansions=attachments.poll_ids ` query parameter in your
                                                               request. While the poll ID will be located in the Tweet object,
                                                               you will find this ID and all additional poll fields in the
                                                               ` includes ` data object.

  ` tweet.fields `\       enum ( ` attachments ` ,             This [fields](/en/docs/twitter-api/fields) parameter enables you
  [Optional]{.small}      ` author_id ` ,                      to select which specific [Tweet
                          ` context_annotations ` ,            fields](/en/docs/twitter-api/data-dictionary/object-model/tweet)
                          ` conversation_id ` , ` created_at ` will deliver in each returned pinned Tweet. Specify the desired
                          , ` edit_controls ` , ` entities ` , fields in a comma-separated list without spaces between commas and
                          ` geo ` , ` id ` ,                   fields. The Tweet fields will only return if the user has a pinned
                          ` in_reply_to_user_id ` , ` lang ` , Tweet and if you\'ve also included the
                          ` non_public_metrics ` ,             ` expansions=pinned_tweet_id ` query parameter in your request.
                          ` public_metrics ` ,                 While the referenced Tweet ID will be located in the original
                          ` organic_metrics ` ,                Tweet object, you will find this ID and all additional Tweet
                          ` promoted_metrics ` ,               fields in the ` includes ` data object.
                          ` possibly_sensitive ` ,             
                          ` referenced_tweets ` ,              
                          ` reply_settings ` , ` source ` ,    
                          ` text ` , ` withheld ` )            

  ` user.fields `\        enum ( ` created_at ` ,              This [fields](/en/docs/twitter-api/fields) parameter enables you
  [Optional]{.small}      ` description ` , ` entities ` ,     to select which specific [user
                          ` id ` , ` location ` ,              fields](/en/docs/twitter-api/data-dictionary/object-model/user)
                          ` most_recent_tweet_id ` , ` name `  will deliver with the users object. Specify the desired fields in
                          , ` pinned_tweet_id ` ,              a comma-separated list without spaces between commas and fields.
                          ` profile_image_url ` ,              These specified user fields will display directly in the user data
                          ` protected ` , ` public_metrics ` , objects.
                          ` url ` , ` username ` ,             
                          ` verified ` , ` withheld ` )        
  ----------------------- ------------------------------------ ------------------------------------------------------------------
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
|                       |                       | large integers.       |
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
|                       |                       | Tweet.                |
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
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` tweet.f             |
|                       |                       | ields=edit_controls ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
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
| ` note_tweet `        | string                | Information about     |
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
|                       |                       | value be ` null `     |
|                       |                       | unless the user       |
|                       |                       | explicitly shared     |
|                       |                       | their precise         |
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
|                       |                       | Organization          |
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
|                       |                       | Tweet.                |
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
|                       |                       | private metric, and   |
|                       |                       | requires the use of   |
|                       |                       | OAuth 2.0 User        |
|                       |                       | Context               |
|                       |                       | authentication.       |
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
|                       |                       | viewed. This is a     |
|                       |                       | private metric, and   |
|                       |                       | requires the use of   |
|                       |                       | OAuth 2.0 User        |
|                       |                       | Context               |
|                       |                       | authentication.       |
+-----------------------+-----------------------+-----------------------+
| ` non_public_metr     | integer               | Number of times a     |
| ics.url_link_clicks ` |                       | user clicks on a URL  |
|                       |                       | link or URL preview   |
|                       |                       | card in a Tweet. This |
|                       |                       | is a private metric,  |
|                       |                       | and requires the use  |
|                       |                       | of OAuth 2.0 User     |
|                       |                       | Context               |
|                       |                       | authentication.       |
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
|                       |                       | authentication.       |
+-----------------------+-----------------------+-----------------------+
| ` organic_metrics `   | object                | Organic engagement    |
|                       |                       | metrics for the Tweet |
|                       |                       | at the time of the    |
|                       |                       | request. Requires     |
|                       |                       | user context          |
|                       |                       | authentication.       |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` tweet.fie           |
|                       |                       | lds=organic_metrics ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` organic_metri       | integer               | Number of times the   |
| cs.impression_count ` |                       | Tweet has been viewed |
|                       |                       | organically. This is  |
|                       |                       | a private metric, and |
|                       |                       | requires the use of   |
|                       |                       | OAuth 2.0 User        |
|                       |                       | Context               |
|                       |                       | authentication.       |
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
|                       |                       | authentication.       |
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
|                       |                       | authentication.       |
+-----------------------+-----------------------+-----------------------+
| ` organic_me          | integer               | Number of times the   |
| trics.retweet_count ` |                       | Tweet has been        |
|                       |                       | Retweeted             |
|                       |                       | organically.          |
+-----------------------+-----------------------+-----------------------+
| ` organic_            | integer               | Number of replies the |
| metrics.reply_count ` |                       | Tweet has received    |
|                       |                       | organically.          |
+-----------------------+-----------------------+-----------------------+
| ` organic             | integer               | Number of likes the   |
| _metrics.like_count ` |                       | Tweet has received    |
|                       |                       | organically.          |
+-----------------------+-----------------------+-----------------------+
| ` promoted_metrics `  | object                | Engagement metrics    |
|                       |                       | for the Tweet at the  |
|                       |                       | time of the request   |
|                       |                       | in a promoted         |
|                       |                       | context. Requires     |
|                       |                       | user context          |
|                       |                       | authentication.       |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` tweet.fiel          |
|                       |                       | ds=promoted_metrics ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` promoted_metri      | integer               | Number of times the   |
| cs.impression_count ` |                       | Tweet has been viewed |
|                       |                       | when that Tweet is    |
|                       |                       | being promoted. This  |
|                       |                       | is a private metric,  |
|                       |                       | and requires the use  |
|                       |                       | of OAuth 2.0 User     |
|                       |                       | Context               |
|                       |                       | authentication.       |
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
|                       |                       | authentication.       |
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
|                       |                       | authentication.       |
+-----------------------+-----------------------+-----------------------+
| ` promoted_me         | integer               | Number of times this  |
| trics.retweet_count ` |                       | Tweet has been        |
|                       |                       | Retweeted when that   |
|                       |                       | Tweet is being        |
|                       |                       | promoted.             |
+-----------------------+-----------------------+-----------------------+
| ` promoted_           | integer               | Number of Replies to  |
| metrics.reply_count ` |                       | this Tweet when that  |
|                       |                       | Tweet is being        |
|                       |                       | promoted.             |
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
| ` meta `\             | object                | This object contains  |
| [Default]{.small}     |                       | information about the |
|                       |                       | number of users       |
|                       |                       | returned in the       |
|                       |                       | current request, and  |
|                       |                       | pagination details.   |
+-----------------------+-----------------------+-----------------------+
| `                     | integer               | The number of users   |
|  meta.result_count `\ |                       | returned in this      |
| [Default]{.small}     |                       | request. Note that    |
|                       |                       | this number may be    |
|                       |                       | lower than what was   |
|                       |                       | specified in the      |
|                       |                       | ` max_results ` query |
|                       |                       | parameter.            |
+-----------------------+-----------------------+-----------------------+
| `                     | string                | Pagination token for  |
| meta.previous_token ` |                       | the previous page of  |
|                       |                       | results. This value   |
|                       |                       | is returned when      |
|                       |                       | there are multiple    |
|                       |                       | pages of results, as  |
|                       |                       | the current request   |
|                       |                       | may only return a     |
|                       |                       | subset of results. To |
|                       |                       | go back to the        |
|                       |                       | previous page,        |
|                       |                       | passing the value     |
|                       |                       | from this field in    |
|                       |                       | the                   |
|                       |                       | ` pagination_token `  |
|                       |                       | query parameter. When |
|                       |                       | this field is not     |
|                       |                       | returned in the       |
|                       |                       | response, it means    |
|                       |                       | you are on the first  |
|                       |                       | page of results.      |
+-----------------------+-----------------------+-----------------------+
| ` meta.next_token `   | string                | Pagination token for  |
|                       |                       | the next page of      |
|                       |                       | results. This value   |
|                       |                       | is returned when      |
|                       |                       | there are multiple    |
|                       |                       | pages of results, as  |
|                       |                       | the current request   |
|                       |                       | may only return a     |
|                       |                       | subset of results. To |
|                       |                       | retrieve the full     |
|                       |                       | list, keep passing    |
|                       |                       | the value from this   |
|                       |                       | field in the          |
|                       |                       | ` pagination_token `  |
|                       |                       | query parameter. When |
|                       |                       | this field is not     |
|                       |                       | returned in the       |
|                       |                       | response, it means    |
|                       |                       | you\'ve reached the   |
|                       |                       | last page of results, |
|                       |                       | and that there are no |
|                       |                       | further pages.        |
+-----------------------+-----------------------+-----------------------+
:::
:::
:::
