::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
<div>

The v2 manage Tweets endpoints will replace the standard v1.1 [POST
statuses/update](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-update)
and [POST
statuses/destroy/:id](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-destroy-id)
endpoints. If you have code, apps, or tools that use the v1.1 version of
the manage Tweets endpoints and are considering migrating to the newer
Twitter API v2 endpoint, then this set of guides is for you. \

The following tables compare the standard v1.1 and Twitter API v2 manage
Tweets endpoints:

**Create a Tweet**

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
| Endpoint path         | [                     | [ /2/tweets           |
|                       | /1.1                  | ]{.code-inline}       |
|                       | /statuses/update.json |                       |
|                       | ]{.code-inline}       |                       |
+-----------------------+-----------------------+-----------------------+
| [Aut                  | OAuth 1.0a User       | OAuth 1.0a User       |
| hentication](/content | Context               | Context               |
| /developer-twitter/en |                       |                       |
| /docs/authentication) |                       | OAuth 2.0 User        |
|                       |                       | Context               |
+-----------------------+-----------------------+-----------------------+
| Default request [rate | None                  | 200 requests per 15   |
| limits](/en/docs/twi  |                       | min per user          |
| tter-api/rate-limits) | 300 requests per      |                       |
|                       | 3-hour window per     | 300 requests per      |
|                       | user, per app. Shared | 3-hour window per     |
|                       | with the v1.1 POST    | user, per app. Shared |
|                       | Retweets endpoint.    | with the v2 POST      |
|                       |                       | Retweets endpoint.    |
+-----------------------+-----------------------+-----------------------+
| Requires the use of   |                       | ✔                     |
| credentials from a    |                       |                       |
| [developer            |                       |                       |
| App](/en/docs/apps)   |                       |                       |
| associated with a     |                       |                       |
| [Projec               |                       |                       |
| t](/en/docs/projects) |                       |                       |
+-----------------------+-----------------------+-----------------------+

####  Delete a Tweet

+-----------------------+-----------------------+-----------------------+
| \                     | Standard v1.1         | Twitter API v2        |
| Description           |                       |                       |
+=======================+=======================+=======================+
| HTTP methods          | [ POST                | [ DELETE              |
| supported             | ]{.code-inline}       | ]{.code-inline}       |
+-----------------------+-----------------------+-----------------------+
| Host domain           | [                     | [                     |
|                       | ht                    | ht                    |
|                       | tps://api.twitter.com | tps://api.twitter.com |
|                       | ]{.code-inline}       | ]{.code-inline}       |
+-----------------------+-----------------------+-----------------------+
| Endpoint path         | [                     | [ /2/tweets/:id       |
|                       | /1.1/stat             | ]{.code-inline}       |
|                       | uses/destroy/:id.json |                       |
|                       | ]{.code-inline}       |                       |
+-----------------------+-----------------------+-----------------------+
| [Aut                  | OAuth 1.0a User       | OAuth 1.0a User       |
| hentication](/content | Context               | Context               |
| /developer-twitter/en |                       |                       |
| /docs/authentication) |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Default request [rate | None\                 | 50 requests per 15    |
| limits](/en/docs/twi  |                       | min per user          |
| tter-api/rate-limits) |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Requires the use of   |                       | ✔                     |
| credentials from a    |                       |                       |
| [developer            |                       |                       |
| App](/en/docs/apps)   |                       |                       |
| associated with a     |                       |                       |
| [Projec               |                       |                       |
| t](/en/docs/projects) |                       |                       |
+-----------------------+-----------------------+-----------------------+

</div>
:::
:::
:::
:::
:::
:::
:::
