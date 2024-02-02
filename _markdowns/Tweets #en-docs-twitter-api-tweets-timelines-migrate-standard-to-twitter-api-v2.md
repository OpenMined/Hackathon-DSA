<div>

If you have been working with the v1.1 timelines endpoints
(statuses/user_timeline and statuses/mentions_timeline), the goal of
this guide is to help you understand the similarities and differences
between the standard and Twitter API v2 timelines endpoints so that you
can migrate your current integration to the new version.

-   **Similarities:**
    -   Authentication:
        -   OAuth 1.0a User Context (reverse chronological home
            timeline, user Tweet timeline and user mentions timeline)
        -   OAuth 2.0 App-Only (user Tweet timeline)
    -   Historical Access limit: User timeline (user Tweet timeline)
        provides access to most recent 3200 Tweets; mentions timeline
        (user mention timeline) provides access to most recent 800
        mentions.
    -   Support for Tweet edit history and metadata
    -   Rate limits (user Tweet timeline)
    -   Refresh polling: Ability to retrieve new results since the [
        since_id ]{.code-inline}
    -   Traversing timelines by Tweet IDs
    -   Results specifications:
        -   Results order: Results returned in reverse chronological
            order
        -   Ability to exclude replies (user Tweet timeline only)
        -   Ability to exclude Retweets (user Tweet timeline only)
-   **Differences**
    -   New Authentication capability:
        -   OAuth 2.0 App-Only (user mention timeline)
        -   OAuth 2.0 Authorization Code Flow with PKCE (reverse
            chronological home timeline, user Tweet timeline and user
            mentions timeline)
    -   Access requirements: Twitter API v2 App and Project requirements
    -   Rate limits (user mention timeline and reverse chronological
        home timeline)
    -   Different Request limit & Volume limit
    -   Additional pagination method
        -   Different [ max_results ]{.code-inline} ( [ count
            ]{.code-inline} ) per response
    -   Response data format
    -    Request parameters \
        -   Customized data format based on request parameters,
            including v2 fields and expansions
        -   Additional available data: metrics, Tweet annotations, polls

### Similarities

#### Authentication

The v1.1 statuses/user_timeline and the Twitter API v2 user Tweet
timeline endpoint support both [OAuth 1.0a User
Context](https://developer-staging.twitter.com/en/docs/authentication/oauth-1-0a)
and [OAuth 2.0
App-Only](https://developer-staging.twitter.com/en/docs/authentication/oauth-2-0)
. Therefore, you can continue using the same authentication method and
authorization tokens if you migrate to the Twitter API v2 version.\

#### Historical Access

The v1.1 statuses/user_timeline and the Twitter API v2 user Tweet
timeline endpoint both will return the most recent 3200 Tweets,
including Retweets

The v1.1 statuses/mentions_timeline and the Twitter API v2 user mention
timeline endpoint can return the most recent 800 Tweets.\

**Support for Tweet edit history and metadata**\

Both versions provide metadata that describes any edit history. Check
out the [filtered stream API
References](/en/docs/twitter-api/tweets/filtered-stream/api-reference)
and the [Edit Tweets fundamentals
page](/en/docs/twitter-api/edit-tweets) for more details.

#### Rate Limits

+-----------------------------------+-----------------------------------+
| **Standard v1.1**                 | **Twitter API v2**                |
+-----------------------------------+-----------------------------------+
| user_timeline:                    | User Tweets timeline:             |
+-----------------------------------+-----------------------------------+

#### Refresh polling using since_id

Both versions allow polling for recent results using the [ since_id
]{.code-inline} .\

#### Traversing timelines by Tweet IDs

Both endpoints have the capability to traverse through timelines using
Tweet ID \'timestamps\' based on the way Twitter IDs are constructed. 
The functionality is generally  the same except for the following:

+-----------------------------------+-----------------------------------+
| **Standard timelines v1.1**       | **timelines v2**                  |
+-----------------------------------+-----------------------------------+
| [ since_id ]{.code-inline}        | [ since_id ]{.code-inline}        |
| (exclusive)                       | (exclusive)                       |
|                                   |                                   |
| [ max_id ]{.code-inline}          | [ until_id ]{.code-inline} (also  |
| (inclusive)                       | exclusive, vs [ max_id            |
|                                   | ]{.code-inline} which was         |
|                                   | inclusive)                        |
+-----------------------------------+-----------------------------------+

#### Response filtering parameters

+-----------------------------------+-----------------------------------+
| **Standard timelines v1.1**       | **timelines v2**                  |
+-----------------------------------+-----------------------------------+
| Response filtering parameters:    | Response filtering parameters:    |
|                                   |                                   |
| -   [ include_rts ]{.code-inline} |                                   |
| -   [ exclude_replies             |                                   |
|     ]{.code-inline}               |                                   |
+-----------------------------------+-----------------------------------+
| Example                           | Example:                          |
|                                   |                                   |
| [                                 | [                                 |
| https://                          | https://api.twitter.com/          |
| api.twitter.com/1.1/statuses/user | 2/users/2244994945/tweets?max_res |
| _timeline.json?user_id=2244994945 | ults=100&exclude=retweets,replies |
| &include_rts=0&&exclude_replies=1 | ]{.code-inline}                   |
| ]{.code-inline}                   |                                   |
+-----------------------------------+-----------------------------------+
| Notes:                            | Notes:                            |
|                                   |                                   |
| For user_timeline:                | For user Tweets timeline:         |
|                                   |                                   |
| -   Using [ include_rts=0         | -   Using [ exclude=retweets      |
|     ]{.code-inline} does not      |     ]{.code-inline} does not      |
|     change the possible           |     change the possible           |
|     historical Tweet limit of the |     historical Tweet limit of the |
|     most recent 3200              |     most recent  3200             |
|                                   | -   Using [ exclude=replies       |
|                                   |     ]{.code-inline} reduces the   |
|                                   |     possible historical Tweet     |
|                                   |     limit to the most recent 800  |
|                                   |     replies                       |
+-----------------------------------+-----------------------------------+

### Differences

####   **Authentication**  

####  The v1.1 statuses/mentions_timeline endpoint only supports  [OAuth 1.0a User Context](https://developer-staging.twitter.com/en/docs/authentication/oauth-1-0a)  .  The Twitter API v2 user mention timeline endpoint supports both  [OAuth 1.0a User Context](https://developer-staging.twitter.com/en/docs/authentication/oauth-1-0a) ,   [OAuth 2.0 App-Only](https://developer-staging.twitter.com/en/docs/authentication/oauth-2-0)  , and [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code)  

If you would like to take advantage of the ability to access private or
promoted metrics using the Twitter API v2 user Tweet timeline endpoint,
you will need to use OAuth 1.0a User Context or OAuth 2.0 Authorization
Code with PKCE, and pass the user access tokens related to the user who
posted the Tweet for which you would like to access metrics.\

#### Endpoint URLs

Note that the Twitter API v2 timelines endpoints require a path
parameter of [ :id ]{.code-inline} for the user ID.

-   Standard v1.1 endpoints:
    -   [ https://api.twitter.com/1.1/statuses/home_timeline
        ]{.code-inline}
    -   [ https://api.twitter.com/1.1/statuses/user_timeline
        ]{.code-inline}
    -   [ https://api.twitter.com/1.1/statuses/mention_timeline
        ]{.code-inline}
-   Twitter API v2 endpoint:
    -   [
        https://api.twitter.com/2/users/:id/timelines/reverse_chronological
        ]{.code-inline}
    -   [ https://api.twitter.com/2/users/:id/tweets ]{.code-inline}
    -   [ https://api.twitter.com/2/users/:id/mentions ]{.code-inline}

####  App and Project requirements

The Twitter API v2 endpoints require that you use credentials from a
[developer App](https://developer-staging.twitter.com/en/docs/apps) that
is associated to a
[Project](https://developer-staging.twitter.com/en/docs/projects) when
authenticating your requests. All Twitter API v1.1 endpoints can use
credentials from standalone Apps or Apps associated with a project.\

#### Rate Limits

+-----------------------------------+-----------------------------------+
| **mentions_timeline:**            | **user mention timeline:**        |
|                                   |                                   |
| 75 requests per 15 min with OAuth | 180 requests per 15-minute window |
| 1.0a User Context \               | with OAuth 1.0a User Context\     |
|                                   | 450 requests per 15-minute window |
|                                   | with OAuth 2.0 Bearer Token       |
+-----------------------------------+-----------------------------------+
| **home_timelime:**                | **reverse chronological home      |
|                                   | timeline:**                       |
| 15 requests per 15 minutes \      |                                   |
|                                   | 180 requests per 15 minutes       |
| Up to 800 Tweets are obtainable   |                                   |
| on the home timeline              | You can return every Tweet        |
|                                   | created on a timeline over the    |
|                                   | last 7 days as well as the most   |
|                                   | recent 800 regardless of creation |
|                                   | date.                             |
+-----------------------------------+-----------------------------------+

#### Request limits

+-----------------------------------+-----------------------------------+
| **Standard timelines v1.1**       | **timelines v2**                  |
+-----------------------------------+-----------------------------------+
| Daily request limit               | No daily request limits, only     |
|                                   | limited by consumption volume.    |
| -   100,000 request cap within a  |                                   |
|     24 hour period.               |                                   |
+-----------------------------------+-----------------------------------+

#### Consumption volume limits

+-----------------------------------+-----------------------------------+
| **Standard timelines v1.1**       | **timelines v2**                  |
+-----------------------------------+-----------------------------------+
| Consumption limited only by       | Consumption limited by only       |
| request limits                    | Project-level monthly [Tweet      |
|                                   | cap]                              |
| -   100,000 request cap within a  | (/en/docs/twitter-api/tweet-caps) |
|     24 hour period.               | (across multiple v2 endpoints)    |
|                                   | based on [access                  |
|                                   | level](/en/d                      |
|                                   | ocs/twitter-api/getting-started/a |
|                                   | bout-twitter-api#v2-access-level) |
|                                   | .                                 |
|                                   |                                   |
|                                   | -   500,000 Tweets per month with |
|                                   |     Essential access.             |
|                                   | -   2 million Tweets per month    |
|                                   |     with Elevated access          |
|                                   | -   10 million Tweets per month   |
|                                   |     with Academic Research access |
|                                   |                                   |
|                                   | Reverse chronological home        |
|                                   | timeline is not subject to the    |
|                                   | monthly Tweet cap.                |
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| **Standard timelines v1.1**       | **timelines v2**                  |
+-----------------------------------+-----------------------------------+
| Required: [ user_id               | Required: The specific user ID is |
| ]{.code-inline} or [ screen_name  | specified in the path parameter \ |
| ]{.code-inline}\                  |                                   |
+-----------------------------------+-----------------------------------+
| Optional:                         | Optional:                         |
|                                   |                                   |
| [ count ]{.code-inline} - sets    | [ max_results ]{.code-inline} -   |
| the maximum results returned per  | sets the maximum results returned |
| request                           | per request                       |
|                                   |                                   |
| [ exclude_replies                 | [ exclude=retweets,replies        |
| ]{.code-inline} - removes replies | ]{.code-inline} - removes         |
| from the results                  | Retweets or replies from the      |
|                                   | results                           |
| [ Include_rts ]{.code-inline} -   |                                   |
| when set to 0 removes retweets    | [ tweet.fields ]{.code-inline} -  |
| from the results                  | sets the Tweet object fields to   |
|                                   | return                            |
| [ trim_user ]{.code-inline} -     |                                   |
| removes rehydrated user objects   | [ user.fields ]{.code-inline} -   |
| from the results                  | sets the User object fields to    |
|                                   | return                            |
| [ tweet_mode ]{.code-inline} -    |                                   |
| sets the data format returned for | [ place.fields ]{.code-inline} -  |
| the results, set to extended for  | sets the place object fields to   |
| Tweets longer than 140            | return                            |
|                                   |                                   |
| [ since_id ]{.code-inline} - sets | [ media.fields ]{.code-inline} -  |
| the earliest Tweet ID in result   | sets the media object fields to   |
| (exclusive)                       | return                            |
|                                   |                                   |
| [ max_id ]{.code-inline} - sets   | [ poll.fields ]{.code-inline} -   |
| the latest Tweet ID in result     | sets the poll object fields to    |
| (inclusive)                       | return                            |
|                                   |                                   |
|                                   | expansions - sets the expanded    |
|                                   | fields and data to return         |
|                                   |                                   |
|                                   | [ start_time ]{.code-inline} -    |
|                                   | sets the earliest created_at time |
|                                   | for the results                   |
|                                   |                                   |
|                                   | [ end_time ]{.code-inline} - sets |
|                                   | the latest created_at time for    |
|                                   | the results                       |
|                                   |                                   |
|                                   | [ since_id ]{.code-inline} - sets |
|                                   | the earliest Tweet ID for the     |
|                                   | results (exclusive)               |
|                                   |                                   |
|                                   | [ until_id ]{.code-inline} - sets |
|                                   | the latest Tweet ID in result     |
|                                   | (exclusive)                       |
+-----------------------------------+-----------------------------------+

**Response data format**

+-----------------------------------+-----------------------------------+
| **Standard search v1.1**          | **Search Tweets v2**              |
+-----------------------------------+-----------------------------------+
|       [                           |     {                             |
|         {tweet object},           |                                   |
|         {tweet object}            |    "data": [{id,text},{id,text}], |
|       ]                           |       "meta": {                   |
|                                   |         "o                        |
|                                   | ldest_id": "1337085692623646724", |
|                                   |         "n                        |
|                                   | ewest_id": "1334183616172019713", |
|                                   |                                   |
|                                   | "previous_token": "77qpymm88g5h9v |
|                                   | qkluldpw91lr0qzfz1sqydh841iz48k", |
|                                   |         "result_count": 10,       |
|                                   |                                   |
|                                   |      "next_token": "7140dibdnow9c |
|                                   | 7btw3w29gqolns6a1ipl3kzeae41vsxk" |
|                                   |       }                           |
|                                   |     }                             |
+-----------------------------------+-----------------------------------+

#### Twitter API v2 JSON format

Twitter API v2 is introducing new JSON designs for the objects returned
by the APIs, including
[Tweet](https://developer-staging.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet)
and
[user](https://developer-staging.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user)
objects. You can learn more about the Twitter API v2 format, how to use
fields and expansions by visiting our
[guide](https://developer-staging.twitter.com/en/docs/twitter-api/data-dictionary/using-fields-and-expansions)
, and by reading through our broader [data
dictionary](https://developer-staging.twitter.com/en/docs/twitter-api/data-dictionary)

-   At the JSON root level, the standard endpoints return Tweet objects
    in a statuses array, while Twitter API v2 returns a data array.
-   Instead of referring to Retweeted and Quoted \"statuses\", Twitter
    API v2 JSON refers to Retweeted and Quoted Tweets. Many legacy and
    deprecated fields, such as contributors and user.translator_type are
    being removed.
-   Instead of using both favorites (in Tweet object) and favorites (in
    user object), Twitter API v2 uses the term like.
-   Twitter is adopting the convention that JSON values with no value
    (for example, null) are not written to the payload. Tweet and user
    attributes are only included if they have a non-null value.\

One of the biggest differences between standard v1.1 and Twitter API v2
endpoint versions is how you select which fields return in your payload.
For the standard endpoints, there are several parameters that you could
use to identify which fields or sets of fields would return in the
payload, while the Twitter API v2 version simplifies these different
parameters into
[fields](https://developer-staging.twitter.com/content/developer-twitter/en/docs/twitter-api/fields)
and
[expansions](https://developer-staging.twitter.com/content/developer-twitter/en/docs/twitter-api/expansions)
.

-   fields: Twitter API v2 endpoints enable you to select which fields
    are provided in your payload. For example, Tweet, user, Media,
    Place, and Poll objects all have a list of fields that can be
    returned (or not).
-   expansions: Used to expand the complementary objects referenced in
    Tweet JSON payloads. For example, all Retweets and Replies reference
    other Tweets. By setting expansions=referenced_tweets.id, these
    other Tweet objects are expanded according to the tweet.fields
    setting.  Other objects such as users, polls, and media can be
    expanded.

```{=html}
<!-- -->
```
-   conversation_id
-   Two new
    [annotations](https://developer-staging.twitter.com/en/docs/twitter-api/annotations)
    fields, including context and entities
-   Several new
    [metrics](https://developer-staging.twitter.com/en/docs/twitter-api/metrics)
    fields\

We have put together a [data format migration
guide](/en/docs/twitter-api/migrate/data-formats/standard-v1-1-to-v2)
which can help you map standard v1.1 fields to the newer v2 fields. This
guide will also provide you the specific expansion and field parameter
that you will need to pass with your v2 request to return specific
fields.\

</div>
