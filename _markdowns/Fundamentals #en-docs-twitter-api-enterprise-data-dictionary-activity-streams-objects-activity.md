::: main-content__wrapper
::: dtc09-callout-text
::: dtc09-callout-text
:::
:::

::: dtc09-callout-text
::: dtc09-callout-text
::: dtc09__item
::: dtc09__text
::: c01-rich-text-editor
::: is-table-default
Please note: It is highly recommended to use the [Enriched
Native](/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/tweet.html)
format for enterprise data APIs.

-   The Enriched Native format includes all new metadata since 2017,
    such as [poll
    metadata](/en/docs/twitter-api/enterprise/enrichments/overview/poll-metadata.html)
    , and additional metrics such as reply_count and quote_count.

-   Activity Streams format has not been updated with new metadata or
    enrichments since the [character
    update](https://blog.twitter.com/official/en_us/topics/product/2017/Giving-you-more-characters-to-express-yourself.html)
    in 2017.
:::
:::
:::
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
Activity Streams is an object schema translation of Twitter\'s [original
data
format](https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/overview/intro-to-tweet-json)
created by Gnip to \'normalize the format\' of Tweet data and other
social media data using the third party [Activity Base Schema described
here](https://activitystrea.ms/head/activity-schema.html) .  Tweets are
normalized into the activity streams schema, including: note, person,
place and service object types as nested objects.  Tweets can have other
nested Tweet activity obejcts for Retweets, or others including [
twitter_quoted_status ]{.code-inline} , [ long_object ]{.code-inline} .

The base level object type \"activity\" is similar to the [Tweet base
level
object](/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/tweet.html)
of the native enriched format.  Example payloads in activity streams
format can be found
[here](/en/docs/twitter-api/enterprise/data-dictionary/activity-streams-objects/example-payloads.html)
.

### []{#activity-data-dictionary} Data Dictionary

Below you will find the data dictionary for these 'root-level'
\"activity\" attributes, as well as links to child object data
dictionaries.

+-----------------------+-----------------------+-----------------------+
| Attribute             | Type                  | Description           |
+-----------------------+-----------------------+-----------------------+
| id                    | string                | A unique IRI for the  |
|                       |                       | tweet. In more        |
|                       |                       | detail, \"tag\" is    |
|                       |                       | the scheme,           |
|                       |                       | \                     |
|                       |                       | "search.twitter.com\" |
|                       |                       | represents the domain |
|                       |                       | for the scheme, and   |
|                       |                       | 2005 is when the      |
|                       |                       | scheme was derived.   |
|                       |                       | When storing Tweets,  |
|                       |                       | this should be used   |
|                       |                       | as the unique         |
|                       |                       | identifier or primary |
|                       |                       | key.                  |
|                       |                       |                       |
|                       |                       | \"id\":               |
|                       |                       | \"tag:sea             |
|                       |                       | rch.twitter.com,2005: |
|                       |                       | 1050118621198921728\" |
+-----------------------+-----------------------+-----------------------+
| objectType            | string                | Type of object,       |
|                       |                       | always set to         |
|                       |                       | \"activity\"\         |
|                       |                       | \"objectType\":       |
|                       |                       | \"activity\"          |
+-----------------------+-----------------------+-----------------------+
| object                | object                | An object             |
|                       |                       | representing tweet    |
|                       |                       | being posted or       |
|                       |                       | shared. For Retweets, |
|                       |                       | this will contain an  |
|                       |                       | entire \"activity\",  |
|                       |                       | with the pertinent    |
|                       |                       | fields described in   |
|                       |                       | this schema. For      |
|                       |                       | Original Tweets, this |
|                       |                       | will contain a        |
|                       |                       | \"note\" object, with |
|                       |                       | the fields described  |
|                       |                       | here. \"object\":     |
|                       |                       | \"object\": {         |
|                       |                       | \"objectType\":       |
|                       |                       | \"note\", \"id\":     |
|                       |                       | \"object:sear         |
|                       |                       | ch.twitter.com,2005:1 |
|                       |                       | 050118621198921728\", |
|                       |                       | \"summary\": \"To     |
|                       |                       | make room for more    |
|                       |                       | expression, we will   |
|                       |                       | now count all emojis  |
|                       |                       | as equal---including  |
|                       |                       | those with gender‍‍‍ ‍‍and |
|                       |                       | skin t...             |
|                       |                       | https                 |
|                       |                       | ://t.co/MkGjXf9aXm\", |
|                       |                       | \"link\":             |
|                       |                       | \"http://twitter.com/ |
|                       |                       | TwitterAPI/statuses/1 |
|                       |                       | 050118621198921728\", |
|                       |                       | \"postedTime\":       |
|                       |                       | \"2018-               |
|                       |                       | 10-10T20:19:24.000Z\" |
|                       |                       |                       |
|                       |                       | }                     |
+-----------------------+-----------------------+-----------------------+
| long_object           | object                | An object             |
|                       |                       | representing the full |
|                       |                       | text body if the      |
|                       |                       | Tweet text extends    |
|                       |                       | beyond 140            |
|                       |                       | characters.           |
|                       |                       | \"long_object\": {    |
|                       |                       | \"body\": \"To make   |
|                       |                       | room for more         |
|                       |                       | expression, we will   |
|                       |                       | now count all emojis  |
|                       |                       | as equal---including  |
|                       |                       | those with gender‍‍‍ ‍‍and |
|                       |                       | skin tone modifiers   |
|                       |                       | 👍🏻👍🏽👍🏿. This is now   |
|                       |                       | reflected in          |
|                       |                       | Twitter-Text, our     |
|                       |                       | Open Source library.  |
|                       |                       | \\n\\nUsing           |
|                       |                       | Twitter-Text? See the |
|                       |                       | forum post for        |
|                       |                       | detail:               |
|                       |                       | https                 |
|                       |                       | ://t.co/Nx1XZmRCXA\", |
|                       |                       | \"                    |
|                       |                       | display_text_range\": |
|                       |                       | \[ 0, 277 \],         |
|                       |                       | \"twitter_entities\": |
|                       |                       | { \"hashtags\": \[\], |
|                       |                       | \"urls\": \[ {        |
|                       |                       | \"url\":              |
|                       |                       | \"https               |
|                       |                       | ://t.co/Nx1XZmRCXA\", |
|                       |                       | \"expanded_url\":     |
|                       |                       | \"https://twitterco   |
|                       |                       | mmunity.com/t/new-upd |
|                       |                       | ate-to-the-twitter-te |
|                       |                       | xt-library-emoji-char |
|                       |                       | acter-count/114607\", |
|                       |                       | \"display_url\":      |
|                       |                       | \                     |
|                       |                       | "twittercommunity.com |
|                       |                       | /t/new-update-t...\", |
|                       |                       | \"indices\": \[ 254,  |
|                       |                       | 277 \] } \],          |
|                       |                       | \"user_mentions\":    |
|                       |                       | \[\], \"symbols\":    |
|                       |                       | \[\] }                |
|                       |                       |                       |
|                       |                       | }                     |
+-----------------------+-----------------------+-----------------------+
| display_text_range    | array                 | if the Tweet text     |
|                       |                       | extends beyond 140    |
|                       |                       | characters.           |
|                       |                       | \"                    |
|                       |                       | display_text_range\": |
|                       |                       | \[ 0, 142             |
|                       |                       |                       |
|                       |                       | \]                    |
+-----------------------+-----------------------+-----------------------+
| verb                  | string                | [The type of action   |
|                       |                       | being taken by the    |
|                       |                       | user. Tweets,         |
|                       |                       | \"post\" Retweets,    |
|                       |                       | \"share\" Deleted     |
|                       |                       | Tweets,               |
|                       |                       | \"del                 |
|                       |                       | ete\"](http://activit |
|                       |                       | ystrea.ms/head/activi |
|                       |                       | ty-schema.html#verbs) |
|                       |                       |                       |
|                       |                       | The verb is the       |
|                       |                       | proper way to         |
|                       |                       | distinguish between a |
|                       |                       | Tweet and a true      |
|                       |                       | Retweet. However,     |
|                       |                       | this only applies to  |
|                       |                       | true retweets, and    |
|                       |                       | not modified or       |
|                       |                       | quoted Tweets, which  |
|                       |                       | don\'t use Twitter\'s |
|                       |                       | Retweet               |
|                       |                       | functionality. For a  |
|                       |                       | description of AS     |
|                       |                       | verbs                 |
|                       |                       |                       |
|                       |                       | [click                |
|                       |                       | here](http://activit  |
|                       |                       | ystrea.ms/head/activi |
|                       |                       | ty-schema.html#verbs) |
|                       |                       | . For Deletes, note   |
|                       |                       | that only a limited   |
|                       |                       | number of fields will |
|                       |                       | be included, as shown |
|                       |                       | in the sample payload |
|                       |                       | below.                |
|                       |                       |                       |
|                       |                       | \"verb\": \"post\"    |
+-----------------------+-----------------------+-----------------------+
| postedTime            | date (ISO 8601)       | The time the action   |
|                       |                       | occurred, e.g. the    |
|                       |                       | time the Tweet was    |
|                       |                       | posted.               |
|                       |                       |                       |
|                       |                       | \"postedTime\":       |
|                       |                       | \"2018-               |
|                       |                       | 10-10T20:19:24.000Z\" |
+-----------------------+-----------------------+-----------------------+
| generator             | object                | An object             |
|                       |                       | representing the      |
|                       |                       | utility used to post  |
|                       |                       | the Tweet. This will  |
|                       |                       | contain the name      |
|                       |                       | (\"displayName\") and |
|                       |                       | a link (\"link\") for |
|                       |                       | the source            |
|                       |                       | application           |
|                       |                       | generating the Tweet. |
|                       |                       | \"generator\": {      |
|                       |                       | \"displayName\":      |
|                       |                       | \"Twitter Web         |
|                       |                       | Client\", \"link\":   |
|                       |                       | \                     |
|                       |                       | "http://twitter.com\" |
|                       |                       |                       |
|                       |                       | }                     |
+-----------------------+-----------------------+-----------------------+
| provider              | object                | A JSON object         |
|                       |                       | representing the      |
|                       |                       | provider of the       |
|                       |                       | activity. This will   |
|                       |                       | contain an objectType |
|                       |                       | (\"service\"), the    |
|                       |                       | name of the provider  |
|                       |                       | (\"displayName\"),    |
|                       |                       | and a link to the     |
|                       |                       | provider\'s website   |
|                       |                       | (\"link\").           |
|                       |                       | \"provider\": {       |
|                       |                       | \"objectType\":       |
|                       |                       | \"service\",          |
|                       |                       | \"displayName\":      |
|                       |                       | \"Twitter\",          |
|                       |                       | \"link\":             |
|                       |                       | \"htt                 |
|                       |                       | p://www.twitter.com\" |
|                       |                       |                       |
|                       |                       | }                     |
+-----------------------+-----------------------+-----------------------+
| link                  | string                | A Permalink for the   |
|                       |                       | tweet.\               |
|                       |                       | \"link\":             |
|                       |                       | \"http://twitter.com  |
|                       |                       | /TwitterAPI/statuses/ |
|                       |                       | 1050118621198921728\" |
+-----------------------+-----------------------+-----------------------+
| body                  | string                | The tweet text. In    |
|                       |                       | Retweets, note that   |
|                       |                       | Twitter modifies the  |
|                       |                       | value of the body at  |
|                       |                       | the root level by     |
|                       |                       | adding \"RT           |
|                       |                       | \@username\" at the   |
|                       |                       | beginning, and by     |
|                       |                       | truncating the        |
|                       |                       | original text and     |
|                       |                       | adding an ellipsis at |
|                       |                       | the end. Thus, for    |
|                       |                       | Retweets, your app    |
|                       |                       | should look at the    |
|                       |                       | object.body to ensure |
|                       |                       | that it is extracting |
|                       |                       | the non-modified text |
|                       |                       | of the original Tweet |
|                       |                       | (being retweeted).    |
|                       |                       |                       |
|                       |                       | \"body\": \"With      |
|                       |                       | Cardiff, Crystal      |
|                       |                       | Palace, and Hull City |
|                       |                       | joining the EPL from  |
|                       |                       | the Championship it   |
|                       |                       | will be a great       |
|                       |                       | relegation battle at  |
|                       |                       | the end.\"            |
+-----------------------+-----------------------+-----------------------+
| display_text_range    | array                 | Describes the range   |
|                       |                       | of characters within  |
|                       |                       | the body text that    |
|                       |                       | indicates the         |
|                       |                       | displayed Tweet.      |
|                       |                       | Tweets with leading   |
|                       |                       | \@mentions will start |
|                       |                       | at more than 0 and    |
|                       |                       | Tweets with attached  |
|                       |                       | media or that extened |
|                       |                       | beyond 140 characters |
|                       |                       | will indicate the     |
|                       |                       | display_text_range in |
|                       |                       | the long_object.      |
|                       |                       | \"                    |
|                       |                       | display_text_range\": |
|                       |                       | \[ 14, 42 \] or       |
|                       |                       | \"long_object\": {    |
|                       |                       | \"                    |
|                       |                       | display_text_range\": |
|                       |                       | \[ 0, 277             |
|                       |                       |                       |
|                       |                       | \]\...                |
+-----------------------+-----------------------+-----------------------+
| actor                 | object                | [An object            |
|                       |                       | representing the      |
|                       |                       | twitter user who      |
|                       |                       | tweeted. The Actor    |
|                       |                       | Object refers to a    |
|                       |                       | Twitter User, and     |
|                       |                       | contains all metadata |
|                       |                       | relevant to that      |
|                       |                       | user.\                |
|                       |                       | See](ht               |
|                       |                       | tps://aem.twitter.biz |
|                       |                       | /en/docs/twitter-api/ |
|                       |                       | enterprise/data-dicti |
|                       |                       | onary/activity-stream |
|                       |                       | s-objects/actor.html) |
|                       |                       | [actor object         |
|                       |                       | details](ht           |
|                       |                       | tps://aem.twitter.biz |
|                       |                       | /en/docs/twitter-api/ |
|                       |                       | enterprise/data-dicti |
|                       |                       | onary/activity-stream |
|                       |                       | s-objects/actor.html) |
+-----------------------+-----------------------+-----------------------+
| inReplyTo             | object                | A JSON object         |
|                       |                       | referring to the      |
|                       |                       | Tweet being replied   |
|                       |                       | to, if applicable.    |
|                       |                       | Contains a link to    |
|                       |                       | the Tweet.            |
|                       |                       | \"inReplyTo\": {      |
|                       |                       | \"link\":             |
|                       |                       | \                     |
|                       |                       | "http:\\/\\/twitter.c |
|                       |                       | om\\/GOP\\/statuses\\ |
|                       |                       | /349573991561838593\" |
|                       |                       |                       |
|                       |                       | }                     |
+-----------------------+-----------------------+-----------------------+
| location              | object                | [A JSON object        |
|                       |                       | representing the      |
|                       |                       | Twitter \"Place\"     |
|                       |                       | where the tweet was   |
|                       |                       | created. This is an   |
|                       |                       | object passed through |
|                       |                       | from the Twitter      |
|                       |                       | platform.](https      |
|                       |                       | ://aem.twitter.biz/en |
|                       |                       | /docs/twitter-api/ent |
|                       |                       | erprise/data-dictiona |
|                       |                       | ry/activity-streams-o |
|                       |                       | bjects/location.html) |
|                       |                       |                       |
|                       |                       | See                   |
|                       |                       |                       |
|                       |                       | [location             |
|                       |                       | object](https         |
|                       |                       | ://aem.twitter.biz/en |
|                       |                       | /docs/twitter-api/ent |
|                       |                       | erprise/data-dictiona |
|                       |                       | ry/activity-streams-o |
|                       |                       | bjects/location.html) |
+-----------------------+-----------------------+-----------------------+
| twitter_entities      | object                | The entities object   |
|                       |                       | from Twitter\'s data  |
|                       |                       | format which contains |
|                       |                       | lists of urls,        |
|                       |                       | mentions and          |
|                       |                       | hashtags. Please      |
|                       |                       | reference the Twitter |
|                       |                       | documentation on      |
|                       |                       | Entities here Note    |
|                       |                       | that in Retweets,     |
|                       |                       | Twitter may truncate  |
|                       |                       | the values of         |
|                       |                       | entities that it      |
|                       |                       | extracts at the root  |
|                       |                       | level. So, for        |
|                       |                       | Retweets, your app    |
|                       |                       | should look at        |
|                       |                       | ob                    |
|                       |                       | ject.twitter_entities |
|                       |                       | to ensure that you    |
|                       |                       | are using             |
|                       |                       | non-truncated values. |
|                       |                       |                       |
|                       |                       | See twitter_entities  |
|                       |                       | object details        |
+-----------------------+-----------------------+-----------------------+
| twit                  | object                | An object from        |
| ter_extended_entities |                       | Twitter\'s native     |
|                       |                       | data format           |
|                       |                       | containing \"media\". |
|                       |                       | This will be present  |
|                       |                       | for any Tweet where   |
|                       |                       | the twitter_entities  |
|                       |                       | object has data       |
|                       |                       | present in the        |
|                       |                       | \"media\" field, and  |
|                       |                       | will include multiple |
|                       |                       | photos where present  |
|                       |                       | in the post. Note     |
|                       |                       | that this is the      |
|                       |                       | correct location to   |
|                       |                       | retrieve media        |
|                       |                       | information for       |
|                       |                       | multi-photo posts.    |
|                       |                       | Multiple photos are   |
|                       |                       | represented by        |
|                       |                       | comma-separated JSON  |
|                       |                       | objects within the    |
|                       |                       | \"media\" array.      |
|                       |                       |                       |
|                       |                       | See                   |
|                       |                       | [twit                 |
|                       |                       | ter_extended_entities |
|                       |                       | object                |
|                       |                       | details](h            |
|                       |                       | ttps://aem.twitter.bi |
|                       |                       | z/en/docs/twitter-api |
|                       |                       | /enterprise/data-dict |
|                       |                       | ionary/activity-strea |
|                       |                       | ms-objects/twitter-ex |
|                       |                       | tended-entities.html) |
+-----------------------+-----------------------+-----------------------+
| gnip                  | object                | An object added to    |
|                       |                       | the activity payload  |
|                       |                       | to indicate the       |
|                       |                       | matching rules, and   |
|                       |                       | added enriched data   |
|                       |                       | based on enrichments  |
|                       |                       | active on the stream  |
|                       |                       | or product.           |
|                       |                       |                       |
|                       |                       | See [gnip object      |
|                       |                       | details](h            |
|                       |                       | ttps://aem.twitter.bi |
|                       |                       | z/en/docs/twitter-api |
|                       |                       | /enterprise/data-dict |
|                       |                       | ionary/activity-strea |
|                       |                       | ms-objects/gnip.html) |
+-----------------------+-----------------------+-----------------------+
| edit_history          | Object                | Unique identifiers    |
|                       |                       | indicating all        |
|                       |                       | versions of a Tweet.  |
|                       |                       | For Tweets with no    |
|                       |                       | edits, there will be  |
|                       |                       | one ID. For Tweets    |
|                       |                       | with an edit history, |
|                       |                       | there will be         |
|                       |                       | multiple IDs,         |
|                       |                       | arranged in ascending |
|                       |                       | order reflecting the  |
|                       |                       | order of edits, with  |
|                       |                       | the most recent       |
|                       |                       | version in the last   |
|                       |                       | position of the       |
|                       |                       | array.                |
|                       |                       |                       |
|                       |                       | The Tweet IDs can be  |
|                       |                       | used to hydrate and   |
|                       |                       | view previous         |
|                       |                       | versions of a Tweet.  |
|                       |                       |                       |
|                       |                       | Example:              |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     edit_history": {  |
|                       |                       |         "initial_tw   |
|                       |                       | eet_id": "1283764123" |
|                       |                       |         "edi          |
|                       |                       | t_tweet_ids": ["12837 |
|                       |                       | 64123", "1394263866"] |
|                       |                       |       }               |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| edit_controls         | Object                | When present,         |
|                       |                       | indicates how long a  |
|                       |                       | Tweet is still        |
|                       |                       | editable for and the  |
|                       |                       | number of remaining   |
|                       |                       | edits. Tweets are     |
|                       |                       | only editable for the |
|                       |                       | first 30 minutes      |
|                       |                       | after creation and    |
|                       |                       | can be edited up to   |
|                       |                       | five times.           |
|                       |                       |                       |
|                       |                       | The Tweet IDs can be  |
|                       |                       | used to hydrate and   |
|                       |                       | view previous         |
|                       |                       | versions of a Tweet.  |
|                       |                       |                       |
|                       |                       | Example:              |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |                       |
|                       |                       |  "edit_controls": {   |
|                       |                       |          "ed          |
|                       |                       | itable_until_ms": 123 |
|                       |                       |          "e           |
|                       |                       | dits_remaining": 3    |
|                       |                       |       }               |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| editable              | Boolean               | When present,         |
|                       |                       | indicates if a Tweet  |
|                       |                       | was eligible for edit |
|                       |                       | when published. This  |
|                       |                       | field is not dynamic  |
|                       |                       | and won\'t toggle     |
|                       |                       | from True to False    |
|                       |                       | when a Tweet reaches  |
|                       |                       | its editable time     |
|                       |                       | limit, or maximum     |
|                       |                       | number of edits. The  |
|                       |                       | following Tweet       |
|                       |                       | features will cause   |
|                       |                       | this field to be      |
|                       |                       | false:                |
|                       |                       |                       |
|                       |                       | -   Tweets is         |
|                       |                       |     promoted          |
|                       |                       | -   Tweet has a poll  |
|                       |                       | -   Tweet is a        |
|                       |                       |     non-self-thread   |
|                       |                       |     reply             |
|                       |                       | -   Tweet is a        |
|                       |                       |     retweet (note     |
|                       |                       |     that Quote Tweets |
|                       |                       |     are eligible for  |
|                       |                       |     edit)             |
|                       |                       | -   Tweet is nullcast |
|                       |                       | -   Community Tweet   |
|                       |                       | -   Superfollow Tweet |
|                       |                       | -   Collaborative     |
|                       |                       |     Tweet             |
+-----------------------+-----------------------+-----------------------+

###  Additional Tweet attributes

+-----------------------+-----------------------+-----------------------+
| Attribute             | Type                  | Description           |
+-----------------------+-----------------------+-----------------------+
| twitter_lang          | string                |                       |
+-----------------------+-----------------------+-----------------------+
| favoritesCount        | int                   | *Nullable.* Indicates |
|                       |                       | approximately how     |
|                       |                       | many times this Tweet |
|                       |                       | has been liked by     |
|                       |                       | Twitter users.        |
|                       |                       |                       |
|                       |                       | [                     |
|                       |                       | \                     |
|                       |                       | "favoritesCount\":298 |
|                       |                       | ]{.code-inline}       |
+-----------------------+-----------------------+-----------------------+
| \                     | int                   | Number of times this  |
| retweetCount          |                       | Tweet has been        |
|                       |                       | retweeted. Example:   |
|                       |                       |                       |
|                       |                       | [                     |
|                       |                       | \"retweetCount\":153  |
|                       |                       | ]{.code-inline}       |
+-----------------------+-----------------------+-----------------------+

### Deprecated Attributes

+----------------------+----------------------+----------------------+
| Field                | Type                 | Description          |
+----------------------+----------------------+----------------------+
| geo                  | object               | Point location where |
|                      |                      | the Tweet was        |
|                      |                      | created.             |
+----------------------+----------------------+----------------------+
| twitter_filter_level | string               | Deprecated field     |
|                      |                      | left in for non      |
|                      |                      | breaking change      |
+----------------------+----------------------+----------------------+

### 

### 
:::
:::

::: c01-rich-text-editor
::: is-table-default
In several cases, a Tweet object will included other nested Tweets.  If
you are working with nested objects, then that JSON payload will contain
multiple objects, and each Tweet object may contain its own objects. The
root-level object will contain information on the type of action taken,
i.e. whether it is a Retweet or a Quote Tweet, and may also contain an
object that describes the \'original\' Tweet being shared. Extended
Tweets will include a nested extended object that extends beyond 140
characters, which was used to prevent breaking changes when the update
was made in 2017. Each nested object dictionary is described below.
:::
:::

::: c01-rich-text-editor
::: is-table-default
#### []{#retweet} Retweets

Activity streams format of Retweets includes a nested object with the
type \"activity\" and the verb \"note\" to represent the original Tweet
being Retweeted.
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {
    "id": "tag:search.twitter.com,2005:222222222222",
    "objectType": "activity",
    "verb": "share",
    "body": "RT @TheOriginalTweeter: Coffee and art ☕️",
    "actor": {
        "displayName": "TheRetweeter"
    },
    "object": {
        "id": "tag:search.twitter.com,2005:11111111111",
        "objectType": "activity",
        "verb": "post",
        "body": "Coffee and art ☕️",
        "actor": {
            "displayName": "TheOriginalTweeter"
        },
        "object": {
            "objectType": "note",
            "id": "object:search.twitter.com,2005:11111111111",
            "summary": "Coffee and art ☕️",
            "link": "http://twitter.com/originaltweeter/statuses/11111111111",
            "postedTime": "2020-12-04T11:00:01.000Z"
        },
        "twitter_entities": {},
        "twitter_extended_entities": {}
    },
    "twitter_entities": {},
    "twitter_extended_entities": {},
    "gnip": {}
}
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
#### []{#twitter-quoted-status} Twitter quoted status

Activity streams format embeded quote Tweets
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {
    "id": "tag:search.twitter.com,2005:222222222222",
    "objectType": "activity",
    "verb": "post",
    "body": "Quoting a Tweet: https://t.co/mxiFJ59FlB",
    "actor": {
        "displayName": "TheQuoter2"
    },
    "object": {
        "objectType": "note",
        "id": "object:search.twitter.com,2005:111111111",
        "summary": "https://t.co/mxiFJ59FlB"
    },
    "twitter_entities": {},
    "twitter_extended_entities": {},
    "gnip": {},
    "twitter_quoted_status": {
        "id": "tag:search.twitter.com,2005:111111111",
        "objectType": "activity",
        "verb": "post",
        "body": "console.log('Happy birthday, JavaScript!');",
        "actor": {
            "displayName": "TheOriginalTweeter"
        },
        "object": {
            "objectType": "note",
            "id": "object:search.twitter.com,2005:111111111"
        },
        "twitter_entities": {}
    }
}
    
```
:::
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
     {
        "id": "tag:search.twitter.com,2005:1293612267087384577",
        "objectType": "activity",
        "verb": "share",
        "postedTime": "2020-08-12T18:16:13.000Z",
        "generator": {},
        "provider": {},
        "link": "http://twitter.com/TwitterDev/statuses/1293612267087384577",
        "body": "RT @compston: So excited to make this first set of endpoints available - many more to come before we're done. The @TwitterDev #DevRel team…",
        "actor": {},
        "object": {},
        "favoritesCount": 0,
        "twitter_entities": {},
        "twitter_lang": "en",
        "retweetCount": 13,
        "gnip": {},
        "twitter_filter_level": "low",
        "twitter_quoted_status": {}
    }
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
### []{#long-object} Long object

Activity streams format of the extended_tweet
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {
  "id": "tag:search.twitter.com,2005:1050118621198921728",
  "objectType": "activity",
  "verb": "post",
  "postedTime": "2018-10-10T20:19:24.000Z",
  "generator": {
    "displayName": "Twitter Web Client",
    "link": "http://twitter.com"
  },
  "provider": {
    "objectType": "service",
    "displayName": "Twitter",
    "link": "http://www.twitter.com"
  },
  "link": "http://twitter.com/TwitterAPI/statuses/1050118621198921728",
  "body": "To make room for more expression, we will now count all emojis as equal—including those with gender‍‍‍ ‍‍and skin t… https://t.co/MkGjXf9aXm",
  "long_object": {
    "body": "To make room for more expression, we will now count all emojis as equal—including those with gender‍‍‍ ‍‍and skin tone modifiers 👍🏻👍🏽👍🏿. This is now reflected in Twitter-Text, our Open Source library. \n\nUsing Twitter-Text? See the forum post for detail: https://t.co/Nx1XZmRCXA",
    "display_text_range": [
      0,
      277
    ],
    "twitter_entities": {see twitter_entities object},
  "actor": {see actor object},
  "object": {
    "objectType": "note",
    "id": "object:search.twitter.com,2005:1050118621198921728",
    "summary": "To make room for more expression, we will now count all emojis as equal—including those with gender‍‍‍ ‍‍and skin t… https://t.co/MkGjXf9aXm",
    "link": "http://twitter.com/TwitterAPI/statuses/1050118621198921728",
    "postedTime": "2018-10-10T20:19:24.000Z"
  },
  "favoritesCount": 298,
  "twitter_entities": {see twitter_entities object},
  "twitter_lang": "en",
  "retweetCount": 153,
  "gnip": {see gnip object},
  "twitter_filter_level": "low"
}
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
Explore the other nested objects of this format:

-   Review actor object
-   Review location object
-   Review twitter_entities object
-   See migration guide from Activity Streams to Twitter API v2 format
:::
:::
:::
