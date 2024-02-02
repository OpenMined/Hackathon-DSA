::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Returns a variety of information about a single user specified by the
requested ID.

### Endpoint URL

` https://api.twitter.com/2/users/:id `

  ----------------------- ----------------------- -----------------------
  Name                    Type                    Description

  ` id `\                 string                  The ID of the user to
  [Required]{.small}                              lookup.
  ----------------------- ----------------------- -----------------------

  ----------------------- -------------------------- ------------------------------------------------------------------
  Name                    Type                       Description

  ` expansions `\         enum ( ` pinned_tweet_id ` [Expansions](/en/docs/twitter-api/expansions) enable you to
  [Optional]{.small}      )                          request additional data objects that relate to the originally
                                                     returned users. The ID that represents the expanded data object
                                                     will be included directly in the user data object, but the
                                                     expanded object metadata will be returned within the ` includes `
                                                     response object, and will also include the ID so that you can
                                                     match this data object to the original Tweet object. At this time,
                                                     the only expansion available to endpoints that primarily return
                                                     user objects is ` expansions=pinned_tweet_id ` . You will find the
                                                     expanded Tweet data object living in the ` includes ` response
                                                     object.

  ` tweet.fields `\       enum ( ` attachments ` ,   This [fields](/en/docs/twitter-api/fields) parameter enables you
  [Optional]{.small}      ` author_id ` ,            to select which specific [Tweet
                          ` context_annotations ` ,  fields](/en/docs/twitter-api/data-dictionary/object-model/tweet)
                          ` conversation_id ` ,      will deliver in each returned pinned Tweet. Specify the desired
                          ` created_at ` ,           fields in a comma-separated list without spaces between commas and
                          ` edit_controls ` ,        fields. The Tweet fields will only return if the user has a pinned
                          ` entities ` , ` geo ` ,   Tweet and if you\'ve also included the
                          ` id ` ,                   ` expansions=pinned_tweet_id ` query parameter in your request.
                          ` in_reply_to_user_id ` ,  While the referenced Tweet ID will be located in the original
                          ` lang ` ,                 Tweet object, you will find this ID and all additional Tweet
                          ` non_public_metrics ` ,   fields in the ` includes ` data object.
                          ` public_metrics ` ,       
                          ` organic_metrics ` ,      
                          ` promoted_metrics ` ,     
                          ` possibly_sensitive ` ,   
                          ` referenced_tweets ` ,    
                          ` reply_settings ` ,       
                          ` source ` , ` text ` ,    
                          ` withheld ` )             

  ` user.fields `\        enum ( ` created_at ` ,    This [fields](/en/docs/twitter-api/fields) parameter enables you
  [Optional]{.small}      ` description ` ,          to select which specific [user
                          ` entities ` , ` id ` ,    fields](/en/docs/twitter-api/data-dictionary/object-model/user)
                          ` location ` ,             will deliver with each returned users objects. Specify the desired
                          ` most_recent_tweet_id ` , fields in a comma-separated list without spaces between commas and
                          ` name ` ,                 fields. These specified user fields will display directly in the
                          ` pinned_tweet_id ` ,      user data objects.
                          ` profile_image_url ` ,    
                          ` protected ` ,            
                          ` public_metrics ` ,       
                          ` url ` , ` username ` ,   
                          ` verified ` ,             
                          ` verified_type ` ,        
                          ` withheld ` )             
  ----------------------- -------------------------- ------------------------------------------------------------------
:::
:::

::: c01-rich-text-editor
::: is-table-default
+-----------------------+-----------------------+-----------------------+
| Name                  | Type                  | Description           |
+-----------------------+-----------------------+-----------------------+
| ` id `\               | string                | Unique identifier of  |
| [Default]{.small}     |                       | this user. This is    |
|                       |                       | returned as a string  |
|                       |                       | in order to avoid     |
|                       |                       | complications with    |
|                       |                       | languages and tools   |
|                       |                       | that cannot handle    |
|                       |                       | large integers.       |
+-----------------------+-----------------------+-----------------------+
| ` name `\             | string                | The friendly name of  |
| [Default]{.small}     |                       | this user, as shown   |
|                       |                       | on their profile.     |
+-----------------------+-----------------------+-----------------------+
| ` username `\         | string                | The Twitter handle    |
| [Default]{.small}     |                       | (screen name) of this |
|                       |                       | user.                 |
+-----------------------+-----------------------+-----------------------+
| ` created_at `        | date (ISO 8601)       | Creation time of this |
|                       |                       | account.              |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` use                 |
|                       |                       | r.fields=created_at ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` m                   | string                | The ID of the User\'s |
| ost_recent_tweet_id ` |                       | most recent Tweet     |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` user.fields=m       |
|                       |                       | ost_recent_tweet_id ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` protected `         | boolean               | Indicates if this     |
|                       |                       | user has chosen to    |
|                       |                       | protect their Tweets  |
|                       |                       | (in other words, if   |
|                       |                       | this user\'s Tweets   |
|                       |                       | are private).         |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` us                  |
|                       |                       | er.fields=protected ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
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
|                       |                       | ` u                   |
|                       |                       | ser.fields=withheld ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` wit                 | array                 | Provides a list of    |
| hheld.country_codes ` |                       | countries where this  |
|                       |                       | user is not           |
|                       |                       | available.            |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` user.fields=wit     |
|                       |                       | hheld.country_codes ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` withheld.scope `    | enum ( ` tweet ` ,    | Indicates whether the |
|                       | ` user ` )            | content being         |
|                       |                       | withheld is a Tweet   |
|                       |                       | or a user (this API   |
|                       |                       | will return ` user `  |
|                       |                       | ).                    |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` user.fi             |
|                       |                       | elds=withheld.scope ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` location `          | string                | The location          |
|                       |                       | specified in the      |
|                       |                       | user\'s profile, if   |
|                       |                       | the user provided     |
|                       |                       | one. As this is a     |
|                       |                       | freeform value, it    |
|                       |                       | may not indicate a    |
|                       |                       | valid location, but   |
|                       |                       | it may be fuzzily     |
|                       |                       | evaluated when        |
|                       |                       | performing searches   |
|                       |                       | with location         |
|                       |                       | queries.              |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` u                   |
|                       |                       | ser.fields=location ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` url `               | string                | The URL specified in  |
|                       |                       | the user\'s profile,  |
|                       |                       | if present.           |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` user.fields=url `   |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` description `       | string                | The text of this      |
|                       |                       | user\'s profile       |
|                       |                       | description (also     |
|                       |                       | known as bio), if the |
|                       |                       | user provided one.    |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` user                |
|                       |                       | .fields=description ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` verified `          | boolean               | Indicate if this user |
|                       |                       | is a verified Twitter |
|                       |                       | user.                 |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` u                   |
|                       |                       | ser.fields=verified ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` verified_type `     | enum ( ` blue ` ,     | Indicates the type of |
|                       | ` business ` ,        | verification for the  |
|                       | ` government ` ,      | Twitter account.      |
|                       | ` none ` )            |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` user.f              |
|                       |                       | ields=verified_type ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` entities `          | object                | This object and its   |
|                       |                       | children fields       |
|                       |                       | contain details about |
|                       |                       | text that has a       |
|                       |                       | special meaning in    |
|                       |                       | the user\'s           |
|                       |                       | description.          |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` u                   |
|                       |                       | ser.fields=entities ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` entities.url `      | array                 | Contains details      |
|                       |                       | about the user\'s     |
|                       |                       | profile website.      |
+-----------------------+-----------------------+-----------------------+
| ` entities.url.urls ` | array                 | Contains details      |
|                       |                       | about the user\'s     |
|                       |                       | profile website.      |
+-----------------------+-----------------------+-----------------------+
| ` enti                | integer               | The start position    |
| ties.url.urls.start ` |                       | (zero-based) of the   |
|                       |                       | recognized user\'s    |
|                       |                       | profile website. All  |
|                       |                       | start indices are     |
|                       |                       | inclusive.            |
+-----------------------+-----------------------+-----------------------+
| ` en                  | integer               | The end position      |
| tities.url.urls.end ` |                       | (zero-based) of the   |
|                       |                       | recognized user\'s    |
|                       |                       | profile website. This |
|                       |                       | end index is          |
|                       |                       | exclusive.            |
+-----------------------+-----------------------+-----------------------+
| ` en                  | string                | The URL in the format |
| tities.url.urls.url ` |                       | entered by the user.  |
+-----------------------+-----------------------+-----------------------+
| ` entities.ur         | string                | The fully resolved    |
| l.urls.expanded_url ` |                       | URL.                  |
+-----------------------+-----------------------+-----------------------+
| ` entities.u          | string                | The URL as displayed  |
| rl.urls.display_url ` |                       | in the user\'s        |
|                       |                       | profile.              |
+-----------------------+-----------------------+-----------------------+
| ` e                   | array                 | Contains details      |
| ntities.description ` |                       | about URLs, Hashtags, |
|                       |                       | Cashtags, or mentions |
|                       |                       | located within a      |
|                       |                       | user\'s description.  |
+-----------------------+-----------------------+-----------------------+
| ` entiti              | array                 | Contains details      |
| es.description.urls ` |                       | about any URLs        |
|                       |                       | included in the       |
|                       |                       | user\'s description.  |
+-----------------------+-----------------------+-----------------------+
| ` entities.des        | integer               | The start position    |
| cription.urls.start ` |                       | (zero-based) of the   |
|                       |                       | recognized URL in the |
|                       |                       | user\'s description.  |
|                       |                       | All start indices are |
|                       |                       | inclusive.            |
+-----------------------+-----------------------+-----------------------+
| ` entities.d          | integer               | The end position      |
| escription.urls.end ` |                       | (zero-based) of the   |
|                       |                       | recognized URL in the |
|                       |                       | user\'s description.  |
|                       |                       | This end index is     |
|                       |                       | exclusive.            |
+-----------------------+-----------------------+-----------------------+
| ` entities.d          | string                | The URL in the format |
| escription.urls.url ` |                       | entered by the user.  |
+-----------------------+-----------------------+-----------------------+
| ` entities.descriptio | string                | The fully resolved    |
| n.urls.expanded_url ` |                       | URL.                  |
+-----------------------+-----------------------+-----------------------+
| ` entities.descripti  | string                | The URL as displayed  |
| on.urls.display_url ` |                       | in the user\'s        |
|                       |                       | description.          |
+-----------------------+-----------------------+-----------------------+
| ` entities.d          | array                 | Contains details      |
| escription.hashtags ` |                       | about text recognized |
|                       |                       | as a Hashtag.         |
+-----------------------+-----------------------+-----------------------+
| ` entities.descrip    | integer               | The start position    |
| tion.hashtags.start ` |                       | (zero-based) of the   |
|                       |                       | recognized Hashtag    |
|                       |                       | within the Tweet. All |
|                       |                       | start indices are     |
|                       |                       | inclusive.            |
+-----------------------+-----------------------+-----------------------+
| ` entities.descr      | integer               | The end position      |
| iption.hashtags.end ` |                       | (zero-based) of the   |
|                       |                       | recognized Hashtag    |
|                       |                       | within the Tweet.     |
|                       |                       | This end index is     |
|                       |                       | exclusive.            |
+-----------------------+-----------------------+-----------------------+
| ` entities.descripti  | string                | The text of the       |
| on.hashtags.hashtag ` |                       | Hashtag.              |
+-----------------------+-----------------------+-----------------------+
| ` entities.d          | array                 | Contains details      |
| escription.mentions ` |                       | about text recognized |
|                       |                       | as a user mention.    |
+-----------------------+-----------------------+-----------------------+
| ` entities.descrip    | integer               | The start position    |
| tion.mentions.start ` |                       | (zero-based) of the   |
|                       |                       | recognized user       |
|                       |                       | mention within the    |
|                       |                       | Tweet. All start      |
|                       |                       | indices are           |
|                       |                       | inclusive.            |
+-----------------------+-----------------------+-----------------------+
| ` entities.descr      | integer               | The end position      |
| iption.mentions.end ` |                       | (zero-based) of the   |
|                       |                       | recognized user       |
|                       |                       | mention within the    |
|                       |                       | Tweet. This end index |
|                       |                       | is exclusive.         |
+-----------------------+-----------------------+-----------------------+
| ` entities.descriptio | string                | The part of text      |
| n.mentions.username ` |                       | recognized as a user  |
|                       |                       | mention.              |
+-----------------------+-----------------------+-----------------------+
| ` entities.d          | array                 | Contains details      |
| escription.cashtags ` |                       | about text recognized |
|                       |                       | as a Cashtag.         |
+-----------------------+-----------------------+-----------------------+
| ` entities.descrip    | integer               | The start position    |
| tion.cashtags.start ` |                       | (zero-based) of the   |
|                       |                       | recognized Cashtag    |
|                       |                       | within the Tweet. All |
|                       |                       | start indices are     |
|                       |                       | inclusive.            |
+-----------------------+-----------------------+-----------------------+
| ` entities.descr      | integer               | The end position      |
| iption.cashtags.end ` |                       | (zero-based) of the   |
|                       |                       | recognized Cashtag    |
|                       |                       | within the Tweet.     |
|                       |                       | This end index is     |
|                       |                       | exclusive.            |
+-----------------------+-----------------------+-----------------------+
| ` entities.descripti  | string                | The text of the       |
| on.cashtags.cashtag ` |                       | Cashtag.              |
+-----------------------+-----------------------+-----------------------+
| ` profile_image_url ` | string                | The URL to the        |
|                       |                       | profile image for     |
|                       |                       | this user, as shown   |
|                       |                       | on the user\'s        |
|                       |                       | profile.              |
+-----------------------+-----------------------+-----------------------+
| ` public_metrics `    | object                | Contains details      |
|                       |                       | about activity for    |
|                       |                       | this user.            |
+-----------------------+-----------------------+-----------------------+
| ` public_metr         | integer               | Number of users who   |
| ics.followers_count ` |                       | follow this user.     |
+-----------------------+-----------------------+-----------------------+
| ` public_metr         | integer               | Number of users this  |
| ics.following_count ` |                       | user is following.    |
+-----------------------+-----------------------+-----------------------+
| ` public_             | integer               | Number of Tweets      |
| metrics.tweet_count ` |                       | (including Retweets)  |
|                       |                       | posted by this user.  |
+-----------------------+-----------------------+-----------------------+
| ` public_m            | integer               | Number of lists that  |
| etrics.listed_count ` |                       | include this user.    |
+-----------------------+-----------------------+-----------------------+
| ` pinned_tweet_id `   | string                | Unique identifier of  |
|                       |                       | this user\'s pinned   |
|                       |                       | Tweet.                |
|                       |                       |                       |
|                       |                       | You can obtain the    |
|                       |                       | expanded object in    |
|                       |                       | ` includes.tweets `   |
|                       |                       | by adding             |
|                       |                       | ` expansi             |
|                       |                       | ons=pinned_tweet_id ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` includes.tweets `   | array                 | When including the    |
|                       |                       | ` expansi             |
|                       |                       | ons=pinned_tweet_id ` |
|                       |                       | parameter, this       |
|                       |                       | includes the pinned   |
|                       |                       | Tweets attached to    |
|                       |                       | the returned users\'  |
|                       |                       | profiles in the form  |
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
| ` errors `            | object                | Contains details      |
|                       |                       | about errors that     |
|                       |                       | affected any of the   |
|                       |                       | requested users. See  |
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
