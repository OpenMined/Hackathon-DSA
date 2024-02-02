::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
<div>

The v2 reverse chronological timeline, user Tweets timeline, and user
mention timeline endpoints replace the [v1.1
statuses/home_timeine,](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/api-reference/get-statuses-home_timeline)
[v1.1
statuses/user_timeline](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/api-reference/get-statuses-user_timeline.html)
, and [v1.1
statuses/mentions_timeline](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/api-reference/get-statuses-mentions_timeline.html)
endpoints respectively. If you have code, apps, or tools that use an
older version of this endpoint and are considering migrating to the
newer Twitter API v2 endpoint, then this guide is for you.  For a more
in-depth migration guide see [Standard v1.1 migration to Twitter API
v2](https://developer.twitter.com/en/docs/twitter-api/tweets/timelines/migrate/standard-to-twitter-api-v2.html)
.

This page contains three comparison tables:

-    Reverse chronological home timeline
-   User Tweet timeline
-   User mention timeline

### []{#revcron} Reverse chronological home timeline

The following tables compare the standard v1.1 and Twitter API v2 home
timeline endpoints:

+-----------------------+-----------------------+-----------------------+
| **Description**       | **Standard v1.1**     | **Twitter API v2**    |
+-----------------------+-----------------------+-----------------------+
| Documentation         | [API                  | [API                  |
|                       | Reference](https:     | Reference](           |
|                       | //developer.twitter.c | https://developer.twi |
|                       | om/en/docs/twitter-ap | tter.com/en/docs/twit |
|                       | i/v1/tweets/timelines | ter-api/tweets/timeli |
|                       | /api-reference/get-st | nes/api-reference/get |
|                       | atuses-home_timeline) | -users-id-reverse-chr |
|                       |                       | onological.html.html) |
+-----------------------+-----------------------+-----------------------+
| HTTP methods          | ` GET `               | ` GET `               |
| supported             |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Host domain           | ` http                | ` http                |
|                       | s://api.twitter.com ` | s://api.twitter.com ` |
+-----------------------+-----------------------+-----------------------+
| Endpoint paths        | ` /1.1/statuses       | ` /2/u                |
|                       | /home_timeline.json ` | sers/:id/timelines/re |
|                       |                       | verse_chronological ` |
+-----------------------+-----------------------+-----------------------+
| Required parameters   | ` user_id ` or        | User ID set as path   |
|                       | ` screen_name `       | parameter :id         |
+-----------------------+-----------------------+-----------------------+
| Authentication        | OAuth 1.0a User       | OAuth 1.0a User       |
|                       | Context               | Context               |
|                       |                       |                       |
|                       |                       | [OAuth 2.0            |
|                       |                       | Authorization Code    |
|                       |                       | Flow with             |
|                       |                       | PKCE                  |
|                       |                       | ](https://developer.t |
|                       |                       | witter.com/en/docs/au |
|                       |                       | thentication/oauth-2- |
|                       |                       | 0/authorization-code) |
+-----------------------+-----------------------+-----------------------+
| Request rate          | 15 requests per       | 180 requests per      |
| limits/Volume limits  | 15-minute with OAuth  | 15-minute window      |
|                       | 1.0a User Context     |                       |
|                       |                       | [Tweet                |
|                       | Request cap: 100,000  | cap                   |
|                       | within a 24 hour      | ](https://developer.t |
|                       | period.               | witter.com/en/docs/tw |
|                       |                       | itter-api/tweet-caps) |
|                       |                       | :                     |
|                       |                       |                       |
|                       |                       | 500,000 when using    |
|                       |                       | Essential access      |
|                       |                       |                       |
|                       |                       | 2 million when using  |
|                       |                       | Elevated access       |
|                       |                       |                       |
|                       |                       | 10 million when using |
|                       |                       | Academic Research     |
|                       |                       | access                |
+-----------------------+-----------------------+-----------------------+
| Default Tweets per    | 15                    | 100                   |
| response              |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Maximum Tweets per    | 800                   | This endpoint returns |
| response              |                       | every Tweet created   |
|                       |                       | on a timeline over    |
|                       |                       | the last 7 days as    |
|                       |                       | well as the most      |
|                       |                       | recent 800 regardless |
|                       |                       | of creation date.     |
+-----------------------+-----------------------+-----------------------+
| Provides Tweet edit   | ✔                     | ✔                     |
| history               |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Historical Tweets     | The most recent 800   | The most recent 3,200 |
| available             | Tweets, including     | Tweets, including     |
|                       | Retweets              | Retweets              |
+-----------------------+-----------------------+-----------------------+
| Timeline navigation   | since_id (exclusive)  | ` start_time `        |
| options               | used for update       |                       |
|                       | polling               | end_time              |
|                       |                       |                       |
|                       | ` max_id `            | ` since_id `          |
|                       | (inclusive)           | (exclusive) used for  |
|                       |                       | update polling        |
|                       |                       |                       |
|                       |                       | ` until_id `          |
|                       |                       | (exclusive)           |
+-----------------------+-----------------------+-----------------------+
| Optional parameters   | ` count `             | ` max_results `       |
| for results           |                       |                       |
| refinement            | ` exclude_replies `   | ` exclude `           |
|                       |                       | (retweets,replies)    |
|                       | ` include_rts `       |                       |
|                       |                       | ` tweet.fields `      |
|                       | ` trim_user `         |                       |
|                       |                       | ` user.fields `       |
|                       | ` tweet_mode `        |                       |
|                       |                       | ` place.fields `      |
|                       | ` since_id `          |                       |
|                       |                       | ` media.fields `      |
|                       | ` max_id `            |                       |
|                       |                       | ` poll.fields `       |
|                       |                       |                       |
|                       |                       | ` expansions `        |
|                       |                       |                       |
|                       |                       | ` start_time `        |
|                       |                       |                       |
|                       |                       | ` end_time `          |
|                       |                       |                       |
|                       |                       | ` since_id `          |
|                       |                       |                       |
|                       |                       | ` until_id `          |
+-----------------------+-----------------------+-----------------------+
| Supports requesting   | N/A                   | If annotations are    |
| and receiving         |                       | included in           |
| [annotations]         |                       | tweet.fields, results |
| (https://developer.tw |                       | will be annotated     |
| itter.com/en/docs/twi |                       | with inferred         |
| tter-api/annotations) |                       | annotation data based |
|                       |                       | on the Tweet text,    |
|                       |                       | such as \'Music       |
|                       |                       | Genre\' and \'Folk    |
|                       |                       | Music\' or            |
|                       |                       | \'Musician\' and      |
|                       |                       | \'Dolly Parton\'      |
+-----------------------+-----------------------+-----------------------+
| Supports requesting   | N/A                   | If annotations are    |
| and receiving         |                       | included in           |
| specific Tweet        |                       | ` tweet.fields ` ,    |
| [metr                 |                       | results will be       |
| ics](https://develope |                       | annotated with        |
| r.twitter.com/en/docs |                       | public_metrics per    |
| /twitter-api/metrics) |                       | Tweet including       |
|                       |                       | ` retweet_count ` ,   |
|                       |                       | ` reply_count ` ,     |
|                       |                       | ` quote_count ` and   |
|                       |                       | ` like_count ` ,      |
|                       |                       | `                     |
|                       |                       |  non_public_metrics ` |
|                       |                       | , including           |
|                       |                       | ` impression_count `  |
|                       |                       | ,                     |
|                       |                       | `                     |
|                       |                       | user_profile_clicks ` |
|                       |                       | , ` url_link_clicks ` |
|                       |                       | .                     |
|                       |                       |                       |
|                       |                       | Additional media      |
|                       |                       | metrics such as       |
|                       |                       | view_count and video  |
|                       |                       | playback metrics.     |
|                       |                       |                       |
|                       |                       | Additional            |
|                       |                       | organic_metrics and   |
|                       |                       | promoted_metrics      |
|                       |                       | available with User   |
|                       |                       | Context for promoted  |
|                       |                       | Tweets.               |
+-----------------------+-----------------------+-----------------------+
| Supports requesting   | N/A                   | Returns a             |
| and receiving         |                       | conversation_id field |
| [conv                 |                       | where the value       |
| ersation_id](https:// |                       | represents the first  |
| developer.twitter.com |                       | published Tweet in a  |
| /en/docs/twitter-api/ |                       | reply thread to help  |
| conversation-id.html) |                       | you track             |
|                       |                       | conversations.        |
+-----------------------+-----------------------+-----------------------+
| Tweet JSON format     | [Standard v1.1 data   | [Twitter API          |
|                       | format]               | v2](htt               |
|                       | (https://developer.tw | ps://developer.twitte |
|                       | itter.com/en/docs/twi | r.com/en/docs/twitter |
|                       | tter-api/v1/data-dict | -api/data-dictionary) |
|                       | ionary/overview.html) | format (determined by |
|                       |                       | fields and expansions |
|                       |                       | request parameters,   |
|                       |                       | not                   |
|                       |                       | backward-compatible   |
|                       |                       | with v1.1 formats)    |
|                       |                       |                       |
|                       |                       | To learn more about   |
|                       |                       | how to migrate from   |
|                       |                       | the Standard v1.1     |
|                       |                       | format to the Twitter |
|                       |                       | API v2 format, please |
|                       |                       | visit our [data       |
|                       |                       | formats migration     |
|                       |                       | guide](https://       |
|                       |                       | developer.twitter.com |
|                       |                       | /en/docs/twitter-api/ |
|                       |                       | migrate/data-formats) |
|                       |                       | .                     |
+-----------------------+-----------------------+-----------------------+
| Results order         | Reverse chronological | Reverse chronological |
+-----------------------+-----------------------+-----------------------+
| Results pagination    | N/A must use          | Results can be        |
|                       | navigation by Tweet   | reviewed moving       |
|                       | ID                    | forward or backward   |
|                       |                       | using a               |
|                       |                       | pagination_token      |
+-----------------------+-----------------------+-----------------------+
| Requires the use of   |                       | ✔                     |
| credentials from a    |                       |                       |
| [developer            |                       |                       |
| App](h                |                       |                       |
| ttps://developer.twit |                       |                       |
| ter.com/en/docs/apps) |                       |                       |
| associated with a     |                       |                       |
| [Project](https       |                       |                       |
| ://developer.twitter. |                       |                       |
| com/en/docs/projects) |                       |                       |
+-----------------------+-----------------------+-----------------------+

### []{#user-tweet-timeline} User Tweet timeline

The following tables compare the standard v1.1 and Twitter API v2 user
Tweet timeline endpoints:

+-----------------------+-----------------------+-----------------------+
| **Description**       | **Standard v1.1**     | **Twitter API v2**    |
+-----------------------+-----------------------+-----------------------+
| Documentation         | [API                  | [API                  |
|                       | Reference](/en        | Refe                  |
|                       | /docs/twitter-api/v1/ | rence](/en/docs/twitt |
|                       | tweets/timelines/api- | er-api/tweets/timelin |
|                       | reference/get-statuse | es/api-reference/get- |
|                       | s-user_timeline.html) | users-id-tweets.html) |
+-----------------------+-----------------------+-----------------------+
| HTTP methods          | [ GET ]{.code-inline} | [ GET ]{.code-inline} |
| supported             |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Host domain           | [                     | [                     |
|                       | ht                    | ht                    |
|                       | tps://api.twitter.com | tps://api.twitter.com |
|                       | ]{.code-inline}       | ]{.code-inline}       |
+-----------------------+-----------------------+-----------------------+
| Endpoint paths        | [                     | [ /2/users/:id/tweets |
|                       | /1.1/statuse          | ]{.code-inline}\      |
|                       | s/user_timeline.json\ |                       |
|                       | ]{.code-inline}       |                       |
+-----------------------+-----------------------+-----------------------+
| Required parameters   | [ user_id             | User ID set as path   |
|                       | ]{.code-inline} or [  | parameter [ :id       |
|                       | screen_name           | ]{.code-inline}       |
|                       | ]{.code-inline}       |                       |
+-----------------------+-----------------------+-----------------------+
| Authentication        | OAuth 1.0a User       | OAuth 1.0a User       |
|                       | Context               | Context               |
|                       |                       |                       |
|                       | OAuth 2.0 App-Only\   | OAuth 2.0 App-Only    |
|                       |                       |                       |
|                       |                       | OAuth 2.0             |
|                       |                       | Authorization Code    |
|                       |                       | with PKCE             |
+-----------------------+-----------------------+-----------------------+
| Request rate          | 900 requests per 15   | 900 requests per      |
| limits/Volume limits  | min with OAuth 1.0a   | 15-minute window with |
|                       | User Context          | OAuth 1.0a User       |
|                       |                       | Context               |
|                       | 1500 requests per 15  |                       |
|                       | min with OAuth 2.0    | 1500 requests per     |
|                       | App-Only              | 15-minute window with |
|                       |                       | OAuth 2.0 App-Only    |
|                       | Request cap: 100,000  |                       |
|                       | within a 24 hour      | [Tweet                |
|                       | period.               | cap](/en/docs/tw      |
|                       |                       | itter-api/tweet-caps) |
|                       |                       | :\                    |
|                       |                       |                       |
|                       |                       | <div>                 |
|                       |                       |                       |
|                       |                       | 500,000 when using    |
|                       |                       | Essential access 2    |
|                       |                       | million when using    |
|                       |                       | Elevated access       |
|                       |                       |                       |
|                       |                       | 10 million when using |
|                       |                       | Academic Research     |
|                       |                       | access                |
|                       |                       |                       |
|                       |                       | </div>                |
+-----------------------+-----------------------+-----------------------+
| Default Tweets per    | 15                    | 10                    |
| response              |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Maximum Tweets per    | 200                   | 100                   |
| response              |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Historical Tweets     | The most recent 3,200 | The most recent 3,200 |
| available             | Tweets, including     | Tweets, including     |
|                       | Retweets              | Retweets              |
+-----------------------+-----------------------+-----------------------+
| Timeline navigation   | [ since_id            | [ start_time          |
| options               | ]{.code-inline}       | ]{.code-inline}       |
|                       | (exclusive) used for  |                       |
|                       | update polling        | [ end_time            |
|                       |                       | ]{.code-inline}       |
|                       | [ max_id              |                       |
|                       | ]{.code-inline}       | [ since_id            |
|                       | (inclusive)           | ]{.code-inline}       |
|                       |                       | (exclusive) used for  |
|                       |                       | update polling        |
|                       |                       |                       |
|                       |                       | [ until_id            |
|                       |                       | ]{.code-inline}       |
|                       |                       | (exclusive)           |
+-----------------------+-----------------------+-----------------------+
| Optional parameters   | ::: code-inline       | [ max_results         |
| for results           | count exclude_replies | ]{.code-inline}\      |
| refinement            | include_rts trim_user | [ exclude             |
|                       | tweet_mode since_id   | ]{.code-inline}       |
|                       |                       | (retweets,replies)\   |
|                       | max_id                |                       |
|                       | :::                   | ::: code-inline       |
|                       |                       | tweet.fields          |
|                       |                       | user.fields           |
|                       |                       | place.fields          |
|                       |                       | media.fields          |
|                       |                       | poll.fields           |
|                       |                       | expansions start_time |
|                       |                       | end_time since_id     |
|                       |                       |                       |
|                       |                       | until_id              |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| Supports requesting   | N/A                   | Returns Tweet results |
| and receiving         |                       | with inferred         |
| [annotations]         |                       | annotation data based |
| (https://developer.tw |                       | on the Tweet text,    |
| itter.com/en/docs/twi |                       | such as \'Music       |
| tter-api/annotations) |                       | Genre\' and \'Folk    |
|                       |                       | Music\' or            |
|                       |                       | \'Musician\' and      |
|                       |                       | \'Dolly Parton\'      |
+-----------------------+-----------------------+-----------------------+
| Supports requesting   | N/A                   | Returns Tweet results |
| and receiving         |                       | with available [      |
| specific Tweet        |                       | public_metrics        |
| [metr                 |                       | ]{.code-inline} per   |
| ics](https://develope |                       | Tweet including [     |
| r.twitter.com/en/docs |                       | retweet_count         |
| /twitter-api/metrics) |                       | ]{.code-inline} , [   |
|                       |                       | reply_count           |
|                       |                       | ]{.code-inline} , [   |
|                       |                       | quote_count           |
|                       |                       | ]{.code-inline} and [ |
|                       |                       | like_count            |
|                       |                       | ]{.code-inline} .     |
|                       |                       | Available with        |
|                       |                       | OAuth1.0a User        |
|                       |                       | Context:              |
|                       |                       |                       |
|                       |                       | Additional [          |
|                       |                       | non_public_metrics    |
|                       |                       | ]{.code-inline} ,     |
|                       |                       | including [           |
|                       |                       | impression_count      |
|                       |                       | ]{.code-inline} , [   |
|                       |                       | user_profile_clicks   |
|                       |                       | ]{.code-inline} , [   |
|                       |                       | url_link_clicks       |
|                       |                       | ]{.code-inline} .     |
|                       |                       |                       |
|                       |                       | Additional media      |
|                       |                       | metrics such as [     |
|                       |                       | view_count            |
|                       |                       | ]{.code-inline} and   |
|                       |                       | video playback        |
|                       |                       | metrics.              |
|                       |                       |                       |
|                       |                       | Additional [          |
|                       |                       | organic_metrics       |
|                       |                       | ]{.code-inline} and [ |
|                       |                       | promoted_metrics      |
|                       |                       | ]{.code-inline}       |
|                       |                       | available with OAuth  |
|                       |                       | 1.0a User Context for |
|                       |                       | promoted Tweets.      |
+-----------------------+-----------------------+-----------------------+
| Supports requesting   | N/A                   | Returns a [           |
| and receiving         |                       | conversation_id       |
| [conversation_id](    |                       | ]{.code-inline} field |
| /en/docs/twitter-api/ |                       | where the value       |
| conversation-id.html) |                       | represents the first  |
|                       |                       | published Tweet in a  |
|                       |                       | reply thread to help  |
|                       |                       | you track             |
|                       |                       | conversations.        |
+-----------------------+-----------------------+-----------------------+
| Tweet JSON format     | [Standard v1.1 data   | [Twitter API          |
|                       | format](/en/docs/twi  | v2](/en/docs/twitter  |
|                       | tter-api/v1/data-dict | -api/data-dictionary) |
|                       | ionary/overview.html) | format (determined by |
|                       |                       | [ fields              |
|                       |                       | ]{.code-inline} and [ |
|                       |                       | expansions            |
|                       |                       | ]{.code-inline}       |
|                       |                       | request parameters,   |
|                       |                       | not                   |
|                       |                       | backward-compatible   |
|                       |                       | with v1.1 formats)    |
|                       |                       |                       |
|                       |                       | To learn more about   |
|                       |                       | how to migrate from   |
|                       |                       | the Standard v1.1     |
|                       |                       | format to the Twitter |
|                       |                       | API v2 format, please |
|                       |                       | visit our [data       |
|                       |                       | formats migration     |
|                       |                       | guide](               |
|                       |                       | /en/docs/twitter-api/ |
|                       |                       | migrate/data-formats) |
|                       |                       | .                     |
+-----------------------+-----------------------+-----------------------+
| Results order         | Reverse chronological | Reverse chronological |
+-----------------------+-----------------------+-----------------------+
| Results pagination    | N/A must use          | Results can be        |
|                       | navigation by Tweet   | reviewed moving       |
|                       | ID\                   | forward or backward   |
|                       |                       | using a [             |
|                       |                       | pagination_token      |
|                       |                       | ]{.code-inline}\      |
+-----------------------+-----------------------+-----------------------+
| Requires the use of   |                       | ✔                     |
| credentials from a    |                       |                       |
| [developer            |                       |                       |
| App](/en/docs/apps)   |                       |                       |
| associated with a     |                       |                       |
| [Projec               |                       |                       |
| t](/en/docs/projects) |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Provides Tweet edit   | ✔                     | ✔                     |
| history               |                       |                       |
+-----------------------+-----------------------+-----------------------+

### []{#user-mention-timeline} User mention timeline

The following tables compare the standard v1.1 and Twitter API v2 user
mention timeline endpoints

+-----------------------+-----------------------+-----------------------+
| **Description**       | **Standard v1.1**     | **Twitter API v2**    |
+-----------------------+-----------------------+-----------------------+
| Documentation         | [API                  | [API                  |
|                       | Reference](/en/doc    | Refere                |
|                       | s/twitter-api/v1/twee | nce](/en/docs/twitter |
|                       | ts/timelines/api-refe | -api/tweets/timelines |
|                       | rence/get-statuses-me | /api-reference/get-us |
|                       | ntions_timeline.html) | ers-id-mentions.html) |
+-----------------------+-----------------------+-----------------------+
| HTTP methods          | [ GET ]{.code-inline} | [ GET ]{.code-inline} |
| supported             |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Host domain           | [                     | [                     |
|                       | ht                    | ht                    |
|                       | tps://api.twitter.com | tps://api.twitter.com |
|                       | ]{.code-inline}       | ]{.code-inline}       |
+-----------------------+-----------------------+-----------------------+
| Endpoint paths        | [                     | [                     |
|                       | /1.1/statuses/m       | /2/users/:id/mentions |
|                       | entions_timeline.json | ]{.code-inline}\      |
|                       | ]{.code-inline}       |                       |
+-----------------------+-----------------------+-----------------------+
| Required parameters   | no required           | User ID set as path   |
|                       | parameters            | parameter [ :id       |
|                       |                       | ]{.code-inline}       |
+-----------------------+-----------------------+-----------------------+
| Authentication        | OAuth 1.0a User       | OAuth 1.0a User       |
|                       | Context               | Context               |
|                       |                       |                       |
|                       |                       | OAuth 2.0 App-Only    |
|                       |                       |                       |
|                       |                       | OAuth 2.0             |
|                       |                       | Authorization Code    |
|                       |                       | with PKCE             |
+-----------------------+-----------------------+-----------------------+
| Default request rate  | 75 requests per 15    | 180 requests per      |
| limits                | min with OAuth 1.0a   | 15-minute window with |
|                       | User Context          | OAuth 1.0a User       |
|                       |                       | Context               |
|                       | 100,000 request cap   |                       |
|                       | within a 24 hour      | 450 requests per      |
|                       | period.               | 15-minute window with |
|                       |                       | OAuth 2.0 App-Only    |
|                       |                       |                       |
|                       |                       | [Tweet                |
|                       |                       | cap](/en/docs/tw      |
|                       |                       | itter-api/tweet-caps) |
|                       |                       | :                     |
|                       |                       |                       |
|                       |                       | 500,000 when using    |
|                       |                       | Essential access\     |
|                       |                       | 2 million when using  |
|                       |                       | Elevated access\      |
|                       |                       | 10 million when using |
|                       |                       | Academic Research     |
|                       |                       | access                |
+-----------------------+-----------------------+-----------------------+
| Default Tweets per    | 15                    | 10                    |
| response              |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Maximum Tweets per    | 200                   | 100                   |
| response              |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Historical Tweets     | The most recent 800   | The most recent 800   |
| available             | Tweets                | Tweets                |
+-----------------------+-----------------------+-----------------------+
| Timeline navigation   | [ since_id            | [ start_time          |
| options               | ]{.code-inline}       | ]{.code-inline}       |
|                       | (exclusive) used for  |                       |
|                       | update polling        | [ end_time            |
|                       |                       | ]{.code-inline}       |
|                       | [ max_id              |                       |
|                       | ]{.code-inline}       | [ since_id            |
|                       | (inclusive)           | ]{.code-inline}       |
|                       |                       | (exclusive) used for  |
|                       |                       | update polling        |
|                       |                       |                       |
|                       |                       | [ until_id            |
|                       |                       | ]{.code-inline}       |
|                       |                       | (exclusive)           |
+-----------------------+-----------------------+-----------------------+
| Optional parameters   | ::: code-inline       | ::: code-inline       |
| for results           | count trim_user       | max_results           |
| refinement            | include_entities      | tweet.fields          |
|                       | tweet_mode since_id   | user.fields           |
|                       |                       | place.fields          |
|                       | max_id                | media.fields          |
|                       | :::                   | poll.fields           |
|                       |                       | expansions start_time |
|                       |                       | end_time since_id     |
|                       |                       |                       |
|                       |                       | until_id              |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| Supports requesting   | N/A                   | Returns Tweet results |
| and receiving         |                       | with inferred         |
| [annotations]         |                       | anotation data based  |
| (https://developer.tw |                       | on the Tweet text,    |
| itter.com/en/docs/twi |                       | such as \'Music       |
| tter-api/annotations) |                       | Genre\' and \'Folk    |
|                       |                       | Music\' or            |
|                       |                       | \'Musician\' and      |
|                       |                       | \'Dolly Parton\'      |
+-----------------------+-----------------------+-----------------------+
| Supports requesting   | N/A                   | Returns Tweet results |
| and receiving         |                       | with available [      |
| specific Tweet        |                       | public_metrics        |
| [metr                 |                       | ]{.code-inline} per   |
| ics](https://develope |                       | Tweet including [     |
| r.twitter.com/en/docs |                       | retweet_count         |
| /twitter-api/metrics) |                       | ]{.code-inline} , [ [ |
|                       |                       | reply_count           |
|                       |                       | ]{.code-inline}       |
|                       |                       | ]{.with-caret} , [    |
|                       |                       | quote_count           |
|                       |                       | ]{.code-inline} and [ |
|                       |                       | like_count            |
|                       |                       | ]{.code-inline} .     |
|                       |                       | Available with OAuth  |
|                       |                       | 1.0a User Context:    |
|                       |                       |                       |
|                       |                       | Additional [          |
|                       |                       | non_public_metrics    |
|                       |                       | ]{.code-inline} ,     |
|                       |                       | including [           |
|                       |                       | impression_count      |
|                       |                       | ]{.code-inline} , [   |
|                       |                       | user_profile_clicks   |
|                       |                       | ]{.code-inline} , [   |
|                       |                       | url_link_clicks       |
|                       |                       | ]{.code-inline} .     |
|                       |                       |                       |
|                       |                       | Additional media      |
|                       |                       | metrics such as [     |
|                       |                       | view_count            |
|                       |                       | ]{.code-inline} and   |
|                       |                       | video playback        |
|                       |                       | metrics.              |
|                       |                       |                       |
|                       |                       | Additional [          |
|                       |                       | organic_metrics       |
|                       |                       | ]{.code-inline} and [ |
|                       |                       | promoted_metrics      |
|                       |                       | ]{.code-inline}       |
|                       |                       | available with OAuth  |
|                       |                       | 1.0a User Context for |
|                       |                       | promoted Tweets       |
+-----------------------+-----------------------+-----------------------+
| Supports requesting   | N/A                   | Returns a [           |
| and receiving         |                       | conversation_id       |
| [conversation_id](    |                       | ]{.code-inline} field |
| /en/docs/twitter-api/ |                       | where the value       |
| conversation-id.html) |                       | represents the first  |
|                       |                       | published Tweet in a  |
|                       |                       | reply thread to help  |
|                       |                       | you track             |
|                       |                       | conversations.        |
+-----------------------+-----------------------+-----------------------+
| Tweet JSON format     | [Standard v1.1        | [Twitter API v2       |
|                       | data                  | format](              |
|                       |  format](/en/docs/twi | /content/developer-tw |
|                       | tter-api/v1/data-dict | itter/en/docs/twitter |
|                       | ionary/overview.html) | -api/data-dictionary) |
|                       |                       | (determined by [      |
|                       |                       | fields                |
|                       |                       | ]{.code-inline} and [ |
|                       |                       | expansions            |
|                       |                       | ]{.code-inline}       |
|                       |                       | request parameters,   |
|                       |                       | not                   |
|                       |                       | backward-compatible   |
|                       |                       | with v1.1 formats)    |
|                       |                       |                       |
|                       |                       | To learn more about   |
|                       |                       | how to migrate from   |
|                       |                       | the Standard v1.1     |
|                       |                       | format to the Twitter |
|                       |                       | API v2 format, please |
|                       |                       | visit our [data       |
|                       |                       | formats migration     |
|                       |                       | guide](               |
|                       |                       | /en/docs/twitter-api/ |
|                       |                       | migrate/data-formats) |
|                       |                       | .                     |
+-----------------------+-----------------------+-----------------------+
| Results order         | Reverse chronological | Reverse chronological |
+-----------------------+-----------------------+-----------------------+
| Request parameters    | N/A must use          | Results can be        |
| for pagination        | navigation by Tweet   | reviewed moving       |
|                       | ID\                   | forward or backward   |
|                       |                       | using [               |
|                       |                       | pagination_token      |
|                       |                       | ]{.code-inline}\      |
+-----------------------+-----------------------+-----------------------+
| Requires the use of   |                       | ✔                     |
| credentials from a    |                       |                       |
| [developer            |                       |                       |
| App](/en/docs/apps)   |                       |                       |
| associated with a     |                       |                       |
| [Projec               |                       |                       |
| t](/en/docs/projects) |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Provides Tweet edit   | ✔                     | ✔                     |
| history               |                       |                       |
+-----------------------+-----------------------+-----------------------+

</div>
:::
:::
:::
:::
:::
:::
:::
