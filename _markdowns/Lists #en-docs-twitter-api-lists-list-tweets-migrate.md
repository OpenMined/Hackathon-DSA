::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
The v2 List Tweets lookup endpoint will replace the standard v1.1 [GET
lists/statuses](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-statuses)
. If you have code, apps, or tools that use this version of the
endpoint, and are considering migrating to the newer Twitter API v2
endpoint, then this set of guides is for you.

The following tables compare the standard v1.1 and Twitter API v2 List
endpoints: \

**List Lookup by ID**

+-----------------------+-----------------------+-----------------------+
| Description           | Standard v1.1         | Twitter API v2        |
+-----------------------+-----------------------+-----------------------+
| HTTP methods          | ` GET `               | ` GET `               |
| supported             |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Host domain           | ` http                | ` http                |
|                       | s://api.twitter.com ` | s://api.twitter.com ` |
+-----------------------+-----------------------+-----------------------+
| Endpoint path         | ` /1.1/               | `                     |
|                       | lists/statuses.json ` | /2/lists/:id/tweets ` |
+-----------------------+-----------------------+-----------------------+
| [Authenticat          | OAuth 1.0a User       | OAuth 1.0a User       |
| ion](https://develope | Context               | Context               |
| r.twitter.com/content |                       |                       |
| /developer-twitter/en | App only              | OAuth 2.0             |
| /docs/authentication) |                       | Authorization Code    |
|                       |                       | with PKCE             |
|                       |                       |                       |
|                       |                       | App only              |
+-----------------------+-----------------------+-----------------------+
| Default request [rate | 900 requests per 15   | 900 requests per 15   |
| limits](https://devel | min with OAuth 1.0a   | min with OAuth 1.0a   |
| oper.twitter.com/cont |                       |                       |
| ent/developer-twitter | 900 requests per      | 900 requests per 15   |
| /en/docs/rate-limits) | 15min with App only   | min with OAuth 2.0    |
|                       |                       |                       |
|                       |                       | 900 requests per 15   |
|                       |                       | min with App only     |
+-----------------------+-----------------------+-----------------------+
:::
:::

::: c01-rich-text-editor
:::
:::
:::
:::
:::
:::
:::
