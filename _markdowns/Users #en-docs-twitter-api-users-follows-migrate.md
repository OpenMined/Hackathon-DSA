::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
The v2 follows lookup endpoints will replace the standard v1.1
[followers/ids](/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-followers-ids)
, v1.1
[followers/list](/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-followers-list)
, v1.1
[friends/ids](/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-friends-ids)
, and v1.1
[friends/list](/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-friends-list)
endpoints.

The following tables compare the various types of follows lookup
endpoints:

+-----------------------+-----------------------+-----------------------+
| **Description**       | **Standard v1.1**     | **Twitter API v2**    |
+-----------------------+-----------------------+-----------------------+
| HTTP methods          | ` GET `               | ` GET `               |
| supported             |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Host domain           | ` http                | ` http                |
|                       | s://api.twitter.com ` | s://api.twitter.com ` |
+-----------------------+-----------------------+-----------------------+
| Endpoint path         | [                     | [                     |
|                       | /1.1/friends/ids.json | /                     |
|                       | ]{.code-inline}       | 2/users/:id/following |
|                       |                       | ]{.code-inline}       |
|                       | [                     |                       |
|                       | /                     | [                     |
|                       | 1.1/friends/list.json | /                     |
|                       | ]{.code-inline}       | 2/users/:id/followers |
|                       |                       | ]{.code-inline}       |
|                       | [                     |                       |
|                       | /1                    |                       |
|                       | .1/followers/ids.json |                       |
|                       | ]{.code-inline}       |                       |
|                       |                       |                       |
|                       | [                     |                       |
|                       | /1.                   |                       |
|                       | 1/followers/list.json |                       |
|                       | ]{.code-inline}       |                       |
+-----------------------+-----------------------+-----------------------+
| [Authentication](/en  | OAuth 1.0a User       | OAuth 1.0a User       |
| /docs/authentication) | Context               | Context               |
|                       |                       |                       |
|                       | App only              | OAuth                 |
|                       |                       | 2.0 Authorization     |
|                       |                       | Code with PKCE        |
|                       |                       |                       |
|                       |                       | App only              |
+-----------------------+-----------------------+-----------------------+
| Default request [rate | 15 requests per 15    | 15 requests per 15    |
| limits](              | min (per user)        | min (per user)        |
| /en/docs/rate-limits) |                       |                       |
|                       | 15 requests per 15    | 15 requests per 15    |
|                       | min (per app)         | min (per app)         |
+-----------------------+-----------------------+-----------------------+
| Maximum users per     | GET friends/id & GET  | 1000 user objects per |
| response              | followers/id return a | page                  |
|                       | maximum of 5000 users |                       |
|                       | IDs per page.         |                       |
|                       |                       |                       |
|                       | \                     |                       |
|                       |                       |                       |
|                       | GET friends/list &    |                       |
|                       | GET followers/list    |                       |
|                       | return a maximum of   |                       |
|                       | 200 user objects per  |                       |
|                       | page.                 |                       |
+-----------------------+-----------------------+-----------------------+
| Pagination            | Token returns in a [  | Token returns in a [  |
|                       | next_cursor           | next_token            |
|                       | ]{.code-inline}       | ]{.code-inline}       |
|                       | field, which can then | field, which can then |
|                       | be passed as the      | be passed as the      |
|                       | value to the [ cursor | value to the token    |
|                       | ]{.code-inline}       | parameter to return   |
|                       | parameter to return   | the next page of      |
|                       | the next page of      | results.              |
|                       | results.              |                       |
|                       |                       | The v2 payload also   |
|                       |                       | delivers a [          |
|                       |                       | previous_token        |
|                       |                       | ]{.code-inline}       |
|                       |                       | field, which can also |
|                       |                       | be passed with the [  |
|                       |                       | pagination_token      |
|                       |                       | ]{.code-inline}       |
|                       |                       | parameter to return   |
|                       |                       | the previous page of  |
|                       |                       | results.              |
+-----------------------+-----------------------+-----------------------+
| JSON format           | Standard v1.1 format  | [Twitter API v2       |
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
| Supports selecting    |                       | ✔                     |
| which                 |                       |                       |
| [fie                  |                       |                       |
| lds](/en/docs/twitter |                       |                       |
| -api/data-dictionary) |                       |                       |
| return in the payload |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Supports the Tweet    |                       | ✔                     |
| [anno                 |                       |                       |
| tations](/en/docs/twi |                       |                       |
| tter-api/annotations) |                       |                       |
| fields                |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Supports requesting   |                       | ✔                     |
| new                   |                       |                       |
| [metrics](/en/docs    |                       |                       |
| /twitter-api/metrics) |                       |                       |
| fields                |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Supports the [        |                       | ✔                     |
| [conversation         |                       |                       |
| _id](/en/docs/twitter |                       |                       |
| -api/conversation-id) |                       |                       |
| ]{.code-inline} field |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Requires the use of   |                       | ✔                     |
| credentials from a    |                       |                       |
| [developer            |                       |                       |
| App](/en/docs/apps)   |                       |                       |
| associated with a     |                       |                       |
| [projec               |                       |                       |
| t](/en/docs/projects) |                       |                       |
+-----------------------+-----------------------+-----------------------+

### 

### []{#manage} Manage follows

The v2 manage follows endpoints will replace the standard v1.1 [POST
friendships/create](/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/post-friendships-create)
and [POST
friendships/destroy](/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/post-friendships-destroy)
endpoints.

The following tables compare the standard v1.1 and Twitter API v2 create
follow endpoints:

#### Follow a user

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
|                       | /1.1/fr               | /                     |
|                       | iendships/create.json | 2/users/:id/following |
|                       | ]{.code-inline}       | ]{.code-inline}       |
+-----------------------+-----------------------+-----------------------+
| [Aut                  | OAuth 1.0a User       | OAuth 1.0a User       |
| hentication](/content | Context               | Context               |
| /developer-twitter/en |                       |                       |
| /docs/authentication) |                       | OAuth                 |
|                       |                       | 2.0 Authorization     |
|                       |                       | Code with PKCE        |
+-----------------------+-----------------------+-----------------------+
| Default request [rate | 50 requests per 15    | 50 requests per 15    |
| limits](/cont         | min                   | min                   |
| ent/developer-twitter |                       |                       |
| /en/docs/rate-limits) |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Maximum daily         | 400                   | 400                   |
| operations per users  |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Maximum daily         | 1000                  | 1000                  |
| operations per app    |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Requires use of       |                       | ✔️                    |
| credentials from a    |                       |                       |
| [developer            |                       |                       |
| App](/en/docs/apps)   |                       |                       |
| that is associated    |                       |                       |
| with a                |                       |                       |
| [Projec               |                       |                       |
| t](/en/docs/projects) |                       |                       |
+-----------------------+-----------------------+-----------------------+

#### Unfollow a user

The following tables compare the standard v1.1 and Twitter API v2 delete
follow endpoints:

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
|                       | /1.1/fri              | /2/users              |
|                       | endships/destroy.json | /:source_user_id/foll |
|                       | ]{.code-inline}       | owing/:target_user_id |
|                       |                       | ]{.code-inline}       |
+-----------------------+-----------------------+-----------------------+
| [Aut                  | OAuth 1.0a User       | OAuth 1.0a User       |
| hentication](/content | Context               | Context               |
| /developer-twitter/en |                       |                       |
| /docs/authentication) |                       | OAuth                 |
|                       |                       | 2.0 Authorization     |
|                       |                       | Code with PKCE        |
+-----------------------+-----------------------+-----------------------+
| Default request [rate | 15 requests per 15    | 50 requests per 15    |
| limits](/cont         | min (per user)        | min (per user)\       |
| ent/developer-twitter |                       |                       |
| /en/docs/rate-limits) |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Maximum daily         | None                  | 500                   |
| operations per app    |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Requires use of       |                       | ✔️                    |
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
