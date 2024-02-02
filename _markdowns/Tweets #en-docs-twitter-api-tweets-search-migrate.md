::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
The v2 Search Tweets endpoint will eventually replace the [standard v1.1
search/tweets](/content/developer-twitter/en/docs/twitter-api/v1/tweets/search/overview/standard)
endpoint and [enterprise Search
API](/en/docs/twitter-api/enterprise/search-api) . If you have code,
apps, or tools that use an older version of a Twitter search endpoint
and are considering migrating to the newer Twitter API v2 endpoints,
then this guide is for you.

This page contains three comparison tables:

-   [Recent search](#recent)
-   [Full-archive search](#full-archive)
-   [Filtering operator comparison](#operators)

### []{#recent} Recent search comparison

The following table compares the various types of recent search
endpoints:\

+-----------------------+-----------------------+-----------------------+
| **Description**       | **Standard v1.1**     | **Twitter API v2**    |
+=======================+=======================+=======================+
| Host domain           | [                     | [                     |
|                       | ht                    | ht                    |
|                       | tps://api.twitter.com | tps://api.twitter.com |
|                       | ]{.code-inline}       | ]{.code-inline}       |
+-----------------------+-----------------------+-----------------------+
| Endpoint path         | [                     | [                     |
|                       | /1                    | /2                    |
|                       | .1/search/tweets.json | /tweets/search/recent |
|                       | ]{.code-inline}       | ]{.code-inline}       |
+-----------------------+-----------------------+-----------------------+
| [Authentication](/en  | OAuth 1.0a User       | OAuth 1.0a User       |
| /docs/authentication) | Context\              | Context               |
|                       | OAuth 2.0 App-Only    |                       |
|                       |                       | OAuth 2.0             |
|                       |                       | Authorization Code    |
|                       |                       | with PKCE             |
|                       |                       |                       |
|                       |                       | OAuth 2.0 App-Only    |
+-----------------------+-----------------------+-----------------------+
| Timestamp format      | YYYYMMDD              | YYYY-MM-DDTHH:mm:ssZ\ |
|                       |                       | [ISO 8601 / RFC       |
|                       |                       | 3339](https:          |
|                       |                       | //tools.ietf.org/html |
|                       |                       | /rfc3339#section-5.6) |
+-----------------------+-----------------------+-----------------------+
| Returns Tweets that   | 7 days                | 7 days                |
| are no older than     |                       |                       |
+-----------------------+-----------------------+-----------------------+
| HTTP methods          | GET                   | GET                   |
| supported             |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Default request rate  | 180 requests per 15   | **Basic:**            |
| limits                | min with OAuth 1.0a   |                       |
|                       | User Context          | 60 requests per 15    |
|                       |                       | min with OAuth        |
|                       | 450 requests per 15   | 2.0 App-Only          |
|                       | min with OAuth        |                       |
|                       | 2.0 App-Only          | 60 requests per 15    |
|                       |                       | min with OAuth 1.0a   |
|                       |                       | User Context          |
|                       |                       |                       |
|                       |                       | 60 requests per 15    |
|                       |                       | min with OAuth 2.0    |
|                       |                       | Authorization Code    |
|                       |                       | with PKCE             |
|                       |                       |                       |
|                       |                       | **Pro:**              |
|                       |                       |                       |
|                       |                       | 450 requests per 15   |
|                       |                       | min with OAuth        |
|                       |                       | 2.0 App-Only          |
|                       |                       |                       |
|                       |                       | 180 requests per 15   |
|                       |                       | min with OAuth 1.0a   |
|                       |                       | User Context          |
|                       |                       |                       |
|                       |                       | 180 requests per 15   |
|                       |                       | min with OAuth 2.0    |
|                       |                       | Authorization Code    |
|                       |                       | with PKCE             |
+-----------------------+-----------------------+-----------------------+
| Offers fully unwound  |                       | ✔                     |
| URLs                  |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Maximum Tweets per    | 100 (15)              | 100 (10)              |
| response (default)    |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Tweet JSON format     | Standard v1.1 format  | [Twitter API v2       |
|                       |                       | for                   |
|                       |                       | mat](/en/docs/twitter |
|                       |                       | -api/data-dictionary) |
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
| Supports selecting    |                       | ✔                     |
| which                 |                       |                       |
| [fields](/en/doc      |                       |                       |
| s/twitter-api/fields) |                       |                       |
| return in the payload |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Supports requesting   |                       | ✔                     |
| and receiving         |                       |                       |
| [anno                 |                       |                       |
| tations](/en/docs/twi |                       |                       |
| tter-api/annotations) |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Supports requesting   |                       | ✔                     |
| specific              |                       |                       |
| [metrics](/en/docs    |                       |                       |
| /twitter-api/metrics) |                       |                       |
| within Tweet object   |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Supports the          |                       | ✔                     |
| [conversation         |                       |                       |
| _id](/en/docs/twitter |                       |                       |
| -api/conversation-id) |                       |                       |
| operator and field    |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Provides Tweet edit   | ✔                     | ✔                     |
| history               |                       |                       |
+-----------------------+-----------------------+-----------------------+
| JSON key name for     | [ statuses            | [ data                |
| Tweet data array      | ]{.code-inline}       | ]{.code-inline}       |
+-----------------------+-----------------------+-----------------------+
| JSON key name for     | [                     | [ meta.next_token     |
| pagination            | search_               | ]{.code-inline}       |
|                       | metadata.next_results |                       |
|                       | ]{.code-inline}       |                       |
+-----------------------+-----------------------+-----------------------+
| Supports navigating   | ✔                     | ✔                     |
| archive by time range |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Time resolution of    | day                   | second                |
| time-based requests   |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Timezone              | UTC                   | UTC                   |
+-----------------------+-----------------------+-----------------------+
| Request parameters    | [ until               | [ start_time          |
| for navigating by     | ]{.code-inline}       | ]{.code-inline}\      |
| time                  |                       | [ end_time            |
|                       |                       | ]{.code-inline}       |
+-----------------------+-----------------------+-----------------------+
| Request parameters    | [ since_id            | [ since_id            |
| for navigating by     | ]{.code-inline}\      | ]{.code-inline}\      |
| Tweet ID              | [ max_id              | [ until_id            |
|                       | ]{.code-inline}       | ]{.code-inline}\      |
+-----------------------+-----------------------+-----------------------+
| Request parameter for | Provides URL-encoded  | [ next_token          |
| pagination            | query                 | ]{.code-inline}       |
+-----------------------+-----------------------+-----------------------+
| Requires the use of   |                       | ✔                     |
| credentials from a    |                       |                       |
| [developer            |                       |                       |
| App](/en/docs/apps)   |                       |                       |
| associated with a     |                       |                       |
| [Projec               |                       |                       |
| t](/en/docs/projects) |                       |                       |
+-----------------------+-----------------------+-----------------------+

### []{#full-archive} Full-archive search comparison

The following table compares the various types of full-archive search
endpoints:\

+-----------------------+-----------------------+-----------------------+
| **Description**       | **Enterprise**        | **Twitter API v2**    |
+=======================+=======================+=======================+
| Host domain           | [                     | [                     |
|                       | https:/               | ht                    |
|                       | /gnip-api.twitter.com | tps://api.twitter.com |
|                       | ]{.code-inline}       | ]{.code-inline}       |
+-----------------------+-----------------------+-----------------------+
| Endpoint path         | [                     | [                     |
|                       | /search               | /2/tweets/search/all  |
|                       | /fullarchive/accounts | ]{.code-inline}       |
|                       | /:account_name/:label |                       |
|                       | ]{.code-inline}       |                       |
+-----------------------+-----------------------+-----------------------+
| [Authentication](/en  | Basic auth            | OAuth 2.0 App-Only    |
| /docs/authentication) |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Timestamp format      | YYYYMMDDHHMM          | YYYY-MM-DDTHH:mm:ssZ\ |
|                       |                       | [ISO 8601 / RFC       |
|                       |                       | 3339](https:          |
|                       |                       | //tools.ietf.org/html |
|                       |                       | /rfc3339#section-5.6) |
+-----------------------+-----------------------+-----------------------+
| Returns Tweets that   | The full archive      | The full archive      |
| are no older than     | since March 2006      | since March 2006      |
+-----------------------+-----------------------+-----------------------+
| HTTP methods          | GET\                  | GET\                  |
| supported             | POST                  |                       |
+-----------------------+-----------------------+-----------------------+
| Default request rate  | The per minute rate   | 300 requests per 15   |
| limits                | limit will vary by    | min with OAuth        |
|                       | partner as specified  | 2.0 App-Only          |
|                       | in your contract.     |                       |
|                       |                       | 1 requests per 1 sec  |
|                       | 20 requests per sec   | with OAuth            |
|                       | with Basic auth       | 2.0 App-Only          |
+-----------------------+-----------------------+-----------------------+
| Offers fully unwound  | ✔                     | ✔                     |
| URLs                  |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Tweets per response   | Maximum: 500\         | Maximum: 500\         |
|                       | Default: 100          | Default: 10           |
+-----------------------+-----------------------+-----------------------+
| Tweet JSON format     | [Native Enriched or   | [Twitter API          |
|                       | Activity              | v2](/en/docs          |
|                       | Str                   | /twitter-api/data-dic |
|                       | eams](/en/docs/twitte | tionary/introduction) |
|                       | r-api/enterprise/data | format (determined by |
|                       | -dictionary/overview) | [ fields              |
|                       | format\               | ]{.code-inline} and [ |
|                       |                       | expansions            |
|                       |                       | ]{.code-inline}       |
|                       |                       | request parameters)   |
+-----------------------+-----------------------+-----------------------+
| Supports selecting    |                       | ✔                     |
| which                 |                       |                       |
| [fields](/en/doc      |                       |                       |
| s/twitter-api/fields) |                       |                       |
| return in the payload |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Supports requesting   |                       | ✔                     |
| and receiving         |                       |                       |
| [anno                 |                       |                       |
| tations](/en/docs/twi |                       |                       |
| tter-api/annotations) |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Supports requesting   |                       | ✔                     |
| specific              |                       |                       |
| [metrics](/en/docs    |                       |                       |
| /twitter-api/metrics) |                       |                       |
| within Tweet object   |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Supports the          |                       | ✔                     |
| [conversation         |                       |                       |
| _id](/en/docs/twitter |                       |                       |
| -api/conversation-id) |                       |                       |
| operator and field    |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Provides Tweet edit   | ✔                     | ✔                     |
| history               |                       |                       |
+-----------------------+-----------------------+-----------------------+
| JSON key name for     | [ results             | [ data                |
| Tweet data array      | ]{.code-inline}       | ]{.code-inline}       |
+-----------------------+-----------------------+-----------------------+
| JSON key name for     | **[ next              | [ meta.next_token     |
| pagination            | ]{.code-inline}**     | ]{.code-inline}       |
+-----------------------+-----------------------+-----------------------+
| Time resolution of    | second                | second                |
| time-based requests   |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Timezone              | UTC                   | UTC                   |
+-----------------------+-----------------------+-----------------------+
| Supports navigating   |                       | ✔                     |
| archive by Tweet ID   |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Request parameters    | [ fromDate            | [ start_time          |
| for navigation by     | ]{.code-inline}\      | ]{.code-inline}\      |
| time                  | [ toDate              | [ end_time            |
|                       | ]{.code-inline}       | ]{.code-inline}       |
+-----------------------+-----------------------+-----------------------+
| Request parameters    |                       | [ since_id            |
| for navigating by     |                       | ]{.code-inline}\      |
| Tweet ID              |                       | [ until_id            |
|                       |                       | ]{.code-inline}\      |
+-----------------------+-----------------------+-----------------------+
| Request parameter for | [ next_token          | [ next_token          |
| pagination            | ]{.code-inline}       | ]{.code-inline}       |
+-----------------------+-----------------------+-----------------------+
| Requires the use of   |                       | ✔                     |
| credentials from a    |                       |                       |
| [developer            |                       |                       |
| App](/en/docs/apps)   |                       |                       |
| associated with a     |                       |                       |
| [Projec               |                       |                       |
| t](/en/docs/projects) |                       |                       |
| that has Academic     |                       |                       |
| Research access       |                       |                       |
+-----------------------+-----------------------+-----------------------+
:::
:::

::: c01-rich-text-editor
<div>

The four different versions (standard, enterprise, and v2) of search
Tweets differ in which operators are available, and also have varying
levels of operator availability within each version, which are explained
below.

Enterprise

-   There are no sub-tiers of enterprise operators\

Twitter API v2

-   **Free:** Available when using any Project
-   **Basic:** Available when using any Project
-   **Pro:** Available when using a Project
-   **Enterprise:** Available when using a Project

You can learn more about each of these sets of operators in their
respective guides:

-   [Enterprise
    operators](/en/docs/twitter-api/enterprise/search-api/guides/operators)
-   [Twitter API v2
    operators](/en/docs/twitter-api/tweets/search/integrate/build-a-query)\

Now that we understand the different operator levels within Twitter API
v2, here is the table that maps out operator availability for search
Tweets (note that if the cell is left blank, the operator is not
available):

  ----------------------------------- --------------------- ----------------- -----------------
  Search operator                     Standard              Enterprise        v2

  keyword                             Available\            Available         Basic & Pro
                                      q:keyword                               

  emoji                               Available\            Available         Basic & Pro
                                      q:😄                                    

  "exact phrase"                      Available             Available         Basic & Pro

  \#                                  Available             Available         Basic & Pro

  \$                                  Available             Available         Pro

  @                                   Available             Available         Basic & Pro

  from:                               Available             Available         Basic & Pro

  to:                                 Available             Available         Basic & Pro

  url:                                Available             Available         Basic & Pro

  retweets_of:                                              Available         Basic & Pro

  context:                                                                    Basic & Pro

  entity:                                                                     Basic & Pro -
                                                                              Only available
                                                                              with recent
                                                                              search

  conversation_id:                                                            Basic

  place:                                                    Available         Pro

  place_country:                                            Available         Pro

  point_radius:                       geocode parameter     Available         Pro

  bounding_box:                                             Available         Pro

  is:retweet                          filter:retweets       Available         Basic & Pro

  is:reply                                                  Available         Basic & Pro

  is:quote                                                  Available         Basic & Pro

  is:verified                                               Available         Basic & Pro

  -is:nullcast                                              Available         Pro

  has:hashtags                                              Available         Basic & Pro

  has:cashtags                                              Available         Pro

  has:links                           filter:links          Available         Basic & Pro

  has:mentions                                              Available         Basic & Pro

  has:media                           filter:media          Available         Basic & Pro

  has:images                          filter:images,        Available         Basic & Pro
                                      filter:twimg                            

  has:videos                          filter:videos\        Available         Basic & Pro
                                      filter:native_video                     

  has:geo                                                   Available         Pro

  lang:                               lang - can be used as Available         Basic & Pro
                                      an operator or a                        
                                      parameter                               

  has:profile_geo                                           Available         

  profile_country                                           Available         

  profile_locality                                          Available         

  profile_region                                            Available         

  proximity                                                 Available         

  :(                                  Available                               

  :)                                  Available                               

  ?                                   Available                               

  filter:periscope                    Available                               

  list:                               Available                               Pro

  filter:replies                      Available                               

  filter:pro_video                    Available                               

  filter:social                       Available                               

  filter:trusted                      Available                               

  filter:follows                      Available                               

  filter:has_engagement               Available                               

  include:antisocial                  Available                               

  include:offensive_user              Available                               

  include:antisocial_offensive_user   Available                               

  include:sensitive_content           Available                               

  source:                             Available                               

  min_replies:                        Available                               

  min_retweets:                       Available                               

  min_faves:                          Available                               

  card_name:                          Available                               

  card_domain:                        Available                               
  ----------------------------------- --------------------- ----------------- -----------------

</div>
:::
:::
