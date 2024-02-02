::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
<div>

The v2 Tweets lookup endpoints will replace the standard v1.1 [GET
statuses/lookup](/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-statuses-lookup)
and [GET
statuses/show](/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-statuses-show-id)
endpoints, as well as the Labs [Tweet
lookup](/en/docs/labs/tweets-and-users) endpoints. If you have code,
apps, or tools that use one of these versions of the Tweet lookup
endpoint, and are considering migrating to the newer Twitter API v2
endpoint, then this set of guides is for you.

The following tables compare the various types of Tweets lookup
endpoints:\

+-----------------------+-----------------------+-----------------------+
| **Description**       | **Standard v1.1**     | **Twitter API v2**    |
+-----------------------+-----------------------+-----------------------+
| HTTP methods          | ` GET `               | ` GET `               |
| supported             |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Host domain           | ` http                | ` http                |
|                       | s://api.twitter.com ` | s://api.twitter.com ` |
+-----------------------+-----------------------+-----------------------+
| Endpoint path         | ` /1.1                | ` /2/tweets `         |
|                       | /statuses/show.json ` |                       |
|                       | ` /1.1/s              |                       |
|                       | tatuses/lookup.json ` |                       |
+-----------------------+-----------------------+-----------------------+
| [Authentication](/en  | OAuth 1.0a User       | OAuth 1.0a User       |
| /docs/authentication) | Context               | Context               |
|                       |                       |                       |
|                       |                       | OAuth 2.0 App-Only    |
|                       |                       |                       |
|                       |                       | OAuth 2.0             |
|                       |                       | Authorization Code    |
|                       |                       | with PKCE             |
+-----------------------+-----------------------+-----------------------+
| Tweet [JSON           | Standard v1.1 format  | [Twitter API v2       |
| format](/en/docs      |                       | format](              |
| /twitter-api/data-dic |                       | /content/developer-tw |
| tionary/introduction) |                       | itter/en/docs/twitter |
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
| Supports the          |                       | ✔                     |
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
| Provides Tweet edit   | ✔                     | ✔                     |
| history               |                       |                       |
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
