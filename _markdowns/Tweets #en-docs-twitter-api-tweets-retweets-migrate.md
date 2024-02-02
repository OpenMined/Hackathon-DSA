::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
[]{#manage} Retweets lookup \

The v2 Retweets lookup endpoint will replace the standard [v1.1 GET
statuses/retweets/:id](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-statuses-retweets-id)
and [v1.1 GET
statuses/retweets/:ids](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-statuses-retweeters-ids)
endpoints.

The following tables compare the standard v1.1 and Twitter API v2
Retweets endpoints:

+-----------------------+-----------------------+-----------------------+
| Description           | Standard v1.1         | Twitter API v2        |
+=======================+=======================+=======================+
| HTTP methods          | [ GET ]{.code-inline} | [ GET ]{.code-inline} |
| supported             |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Host domain           | [                     | [                     |
|                       | ht                    | ht                    |
|                       | tps://api.twitter.com | tps://api.twitter.com |
|                       | ]{.code-inline}       | ]{.code-inline}       |
+-----------------------+-----------------------+-----------------------+
| Endpoint path         | [                     | [                     |
|                       | /1                    | /2/u                  |
|                       | .1/retweeters/id.json | sers/:id/retweeted_by |
|                       | ]{.code-inline}       | ]{.code-inline}       |
|                       |                       |                       |
|                       | ` /1.                 |                       |
|                       | 1/retweets/ids.json ` |                       |
+-----------------------+-----------------------+-----------------------+
| [Aut                  | OAuth 1.0a User       | OAuth 2.0 Bearer      |
| hentication](/content | Context               | Token                 |
| /developer-twitter/en |                       |                       |
| /docs/authentication) |                       | OAuth 1.0a User       |
|                       |                       | Context               |
+-----------------------+-----------------------+-----------------------+
| Default request [rate | 75 requests per 15    | 75 requests per 15    |
| limits](/cont         | min                   | min (per App)         |
| ent/developer-twitter |                       |                       |
| /en/docs/rate-limits) |                       | 75 requests per 15    |
|                       |                       | min (per user)        |
+-----------------------+-----------------------+-----------------------+
| Data format           | Standard v1.1 format  | [Twitter API v2       |
|                       |                       | format](              |
|                       |                       | /content/developer-tw |
|                       |                       | itter/en/docs/twitter |
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
| Requires the use of   |                       | ✔️                    |
| credentials from a    |                       |                       |
| [developer            |                       |                       |
| App](/en/docs/apps)   |                       |                       |
| that is associated    |                       |                       |
| with a                |                       |                       |
| [Projec               |                       |                       |
| t](/en/docs/projects) |                       |                       |
+-----------------------+-----------------------+-----------------------+

###  

### []{#manage} Manage Retweets 

The following tables compare the standard v1.1 and Twitter API v2 undo
Retweet endpoint:

**Retweet a Tweet**

+-----------------------+-----------------------+-----------------------+
| Description           | Standard v1.1         | Twitter API v2        |
+=======================+=======================+=======================+
| HTTP methods          | [ POST                | [ POST                |
| supported             | ]{.code-inline}       | ]{.code-inline}       |
+-----------------------+-----------------------+-----------------------+
| Host domain           | [                     | [                     |
|                       | ht                    | ht                    |
|                       | tps://api.twitter.com | tps://api.twitter.com |
|                       | ]{.code-inline}       | ]{.code-inline}       |
+-----------------------+-----------------------+-----------------------+
| Endpoint path         | [                     | [                     |
|                       | /1.1/stat             | /2/users/:id/retweets |
|                       | uses/retweet/:id.json | ]{.code-inline}       |
|                       | ]{.code-inline}       |                       |
+-----------------------+-----------------------+-----------------------+
| [Aut                  | OAuth 1.0a User       | OAuth 1.0a User       |
| hentication](/content | Context               | Context               |
| /developer-twitter/en |                       |                       |
| /docs/authentication) |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Default request [rate | None                  | 50 requests per 15    |
| limits](/cont         |                       | min (per user)        |
| ent/developer-twitter | 300 requests per      |                       |
| /en/docs/rate-limits) | 3-hour window (per    | 300 requests per      |
|                       | user, per app). This  | 3-hour window (per    |
|                       | is shared with the    | user, per app). This  |
|                       | POST Tweet endpoint   | is shared with the    |
|                       |                       | POST Tweet endpoint   |
|                       |                       | for manage Tweets.    |
+-----------------------+-----------------------+-----------------------+
| Requires the use of   |                       | ✔️                    |
| credentials from a    |                       |                       |
| [developer            |                       |                       |
| App](/en/docs/apps)   |                       |                       |
| that is associated    |                       |                       |
| with a                |                       |                       |
| [Projec               |                       |                       |
| t](/en/docs/projects) |                       |                       |
+-----------------------+-----------------------+-----------------------+

####  Undo a Retweet

The following tables compare the standard v1.1 and Twitter API v2 undo
Retweet endpoint:

  -------------------------------------------------------------------------------------------------------------------------------------------------
  Description                                                           Standard v1.1                      Twitter API v2
  --------------------------------------------------------------------- ---------------------------------- ----------------------------------------
  HTTP methods supported                                                [ POST ]{.code-inline}             [ DELETE ]{.code-inline}

  Host domain                                                           [ https://api.twitter.com          [ https://api.twitter.com
                                                                        ]{.code-inline}                    ]{.code-inline}

  Endpoint path                                                         [ /1.1/statuses/unretweet/:id.json [ /2/users/:id/retweets/:source_tweet_id
                                                                        ]{.code-inline}                    ]{.code-inline}

  [Authentication](/content/developer-twitter/en/docs/authentication)   OAuth 1.0a User Context            OAuth 1.0a User Context

  Default request [rate                                                 None\                              50 requests per 15 min (per user)
  limits](/content/developer-twitter/en/docs/rate-limits)                                                  

  Requires the use of credentials from a [developer App](/en/docs/apps)                                    ✔️
  that is associated with a [Project](/en/docs/projects)                                                   
  -------------------------------------------------------------------------------------------------------------------------------------------------
:::
:::
:::
:::
:::
:::
:::
:::
