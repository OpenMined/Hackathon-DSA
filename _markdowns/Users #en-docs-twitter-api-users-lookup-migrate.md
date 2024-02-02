::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
The v2 user lookup endpoints will replace the standard v1.1 [GET
users/lookup](/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-users-lookup.html)
and [GET
users/show](/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-users-show.html)
endpoints. If you have code, apps, or tools that use one of these
versions of the user lookup endpoints, and are considering migrating to
the newer Twitter API v2 endpoint, then this set of guides is for you.\

The following tables compare the various types of users lookup
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
| Endpoint path         | ` /                   | ` /2/users `          |
|                       | 1.1/users/show.json ` |                       |
|                       | ` /1.                 | ` /2/users/:id `      |
|                       | 1/users/lookup.json ` |                       |
|                       |                       | ` /2/users/by `       |
|                       |                       |                       |
|                       |                       | ` /2                  |
|                       |                       | /users/by/:username ` |
+-----------------------+-----------------------+-----------------------+
| [Authentication](/en  | OAuth 1.0a User       | OAuth 1.0a User       |
| /docs/authentication) | Context               | Context               |
|                       |                       |                       |
|                       |                       | App only              |
|                       |                       |                       |
|                       |                       | OAuth 2.0             |
|                       |                       | Authorization Code    |
|                       |                       | with PKCE             |
+-----------------------+-----------------------+-----------------------+
| Default request [rate | 900 requests per 15   | 900 requests per 15   |
| limits](              | min (per user)        | min (per user)        |
| /en/docs/rate-limits) |                       |                       |
|                       | /show - 900 requests  | 300 requests per 15   |
|                       | per 15 min (per app)\ | min (per app)         |
|                       | /lookup - 300         |                       |
|                       | requests per 15 min   |                       |
|                       | (per app)             |                       |
+-----------------------+-----------------------+-----------------------+
| Maximum Users per     | /show -  1            | 100                   |
| response              |                       |                       |
|                       | /lookup - 100         |                       |
+-----------------------+-----------------------+-----------------------+
| JSON response object  | Standard v1.1 format  | [Twitter API v2       |
| format                |                       | format](              |
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
| Supports the          |                       | ✔                     |
| [anno                 |                       |                       |
| tations](/en/docs/twi |                       |                       |
| tter-api/annotations) |                       |                       |
| fields (on pinned     |                       |                       |
| Tweet)                |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Supports requesting   |                       | ✔                     |
| new                   |                       |                       |
| [metrics](/en/docs    |                       |                       |
| /twitter-api/metrics) |                       |                       |
| fields (on pinned     |                       |                       |
| Tweet)                |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Supports the [        |                       | ✔                     |
| [conversation         |                       |                       |
| _id](/en/docs/twitter |                       |                       |
| -api/conversation-id) |                       |                       |
| ]{.code-inline}       |                       |                       |
| field (on pinned      |                       |                       |
| Tweet)                |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Requires the use of   |                       | ✔                     |
| credentials from a    |                       |                       |
| [developer            |                       |                       |
| App](/en/docs/apps)   |                       |                       |
| associated with a     |                       |                       |
| [projec               |                       |                       |
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
