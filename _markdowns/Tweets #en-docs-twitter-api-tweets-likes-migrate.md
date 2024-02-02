::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
The liked users endpoint is new functionality for v2, allowing you to
get information about a Tweet's liking users.

+-----------------------------------+-----------------------------------+
| Description                       | Twitter API v2                    |
+===================================+===================================+
| HTTP methods supported            | [ GET ]{.code-inline}             |
+-----------------------------------+-----------------------------------+
| Host domain                       | [ https://api.twitter.com         |
|                                   | ]{.code-inline}                   |
+-----------------------------------+-----------------------------------+
| Endpoint path                     | [ /2/tweets/:id/liking_users      |
|                                   | ]{.code-inline}                   |
+-----------------------------------+-----------------------------------+
| [                                 | OAuth 2.0 Bearer Token            |
| Authentication](/content/develope |                                   |
| r-twitter/en/docs/authentication) | OAuth 1.0a User Context           |
+-----------------------------------+-----------------------------------+
| Default request [rate             | 75 requests per 15 min (per App)  |
| limits](/content/devel            |                                   |
| oper-twitter/en/docs/rate-limits) | 75 requests per 15 min (per user) |
+-----------------------------------+-----------------------------------+
| Requires the use of credentials   | ✔️                                |
| from a [developer                 |                                   |
| App](/en/docs/apps) that is       |                                   |
| associated with a                 |                                   |
| [Project](/en/docs/projects)      |                                   |
+-----------------------------------+-----------------------------------+

####  Tweets liked by a user

The following tables compare the standard v1.1 [GET
favorites/list](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-favorites-list)
endpoint and the Twitter API v2 liked Tweets endpoints:

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
|                       | /1.                   | /2/u                  |
|                       | 1/favorites/list.json | sers/:id/liked_tweets |
|                       | ]{.code-inline}       | ]{.code-inline}       |
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
| Data formats          | Standard v1.1 format  | [Twitter API v2       |
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

### []{#manage} Manage Likes 

The v2 manage Likes endpoints replace the v1.1 [POST
favorites/create](/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-favorites-create)
and [POST
favorites/destroy](/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-favorites-destroy)
endpoints.

The following tables compare the standard v1.1 and Twitter API v2 manage
Like endpoints:

#### Like a Tweet

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
| Endpoint path         | [                     | [ /2/users/:id/likes  |
|                       | /1.1/                 | ]{.code-inline}       |
|                       | favorites/create.json |                       |
|                       | ]{.code-inline}       |                       |
+-----------------------+-----------------------+-----------------------+
| [Aut                  | OAuth 1.0a User       | OAuth 1.0a User       |
| hentication](/content | Context               | Context               |
| /developer-twitter/en |                       |                       |
| /docs/authentication) |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Default request [rate | 1000 requests per 24  | 50 requests per 15    |
| limits](/cont         | hours (per user)      | min (per user)        |
| ent/developer-twitter |                       |                       |
| /en/docs/rate-limits) | 1000 requests per 24  | 1000 successful       |
|                       | hours (per App)       | requests per 24 hours |
|                       |                       | (per user, shared     |
|                       |                       | with DELETE)          |
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

#### Unlike a Tweet

+-----------------------+-----------------------+-----------------------+
| Description           | Standard v1.1         | Twitter API v2        |
+=======================+=======================+=======================+
| HTTP methods          | [ POST                | [ DELETE              |
| supported             | ]{.code-inline}       | ]{.code-inline}       |
+-----------------------+-----------------------+-----------------------+
| Host domain           | [                     | [                     |
|                       | ht                    | ht                    |
|                       | tps://api.twitter.com | tps://api.twitter.com |
|                       | ]{.code-inline}       | ]{.code-inline}       |
+-----------------------+-----------------------+-----------------------+
| Endpoint path         | [                     | [                     |
|                       | /1.1/f                | /2/user               |
|                       | avorites/destroy.json | s/:id/likes/:tweet_id |
|                       | ]{.code-inline}       | ]{.code-inline}       |
+-----------------------+-----------------------+-----------------------+
| [Aut                  | OAuth 1.0a User       | OAuth 1.0a User       |
| hentication](/content | Context               | Context               |
| /developer-twitter/en |                       |                       |
| /docs/authentication) |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Default request [rate | 1000 requests per 24  | 50 requests per 15    |
| limits](/cont         | hours (per user)      | min (per user)        |
| ent/developer-twitter |                       |                       |
| /en/docs/rate-limits) | 1000 requests per 24  | 1000 successful       |
|                       | hours (per App)       | requests per 24 hours |
|                       |                       | (per user, shared     |
|                       |                       | with POST)            |
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
:::
:::
:::
:::
:::
:::
:::
:::
