::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
The v2 List members endpoint group will replace the standard v1.1 [GET
lists/members](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-members)
, [GET
lists/memberships](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-memberships)
, [POST
lists/members/create](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-members-create)
and [POST
lists/members/destroy](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-members-destroy)
endpoints. If you have code, apps, or tools that use one of these
versions of the List member endpoints, and are considering migrating to
the newer Twitter API v2 endpoint, then this set of guides is for you.

### List members lookup

The v2 List members lookup endpoints will replace the standard [GET
lists/members](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-members)
, [GET
lists/memberships](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-memberships)
, endpoints.

The following tables compare the standard v1.1 and Twitter API v2 List
endpoints:

**List member Lookup**

+-----------------------+-----------------------+-----------------------+
| Description           | Standard v1.1         | Twitter API v2        |
+-----------------------+-----------------------+-----------------------+
| HTTP methods          | ` GET `               | ` GET `               |
| supported             |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Host domain           | ` http                | ` http                |
|                       | s://api.twitter.com ` | s://api.twitter.com ` |
+-----------------------+-----------------------+-----------------------+
| Endpoint path         | ` /1.1                | ` /                   |
|                       | /lists/members.json ` | 2/lists/:id/members ` |
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
| ent/developer-twitter | 75 requests per 15min | 900 requests per 15   |
| /en/docs/rate-limits) | with App only         | min with OAuth 2.0    |
|                       |                       |                       |
|                       |                       | 900 requests per 15   |
|                       |                       | min with App only     |
+-----------------------+-----------------------+-----------------------+

**List membership lookup**

+-----------------------+-----------------------+-----------------------+
| Description           | Standard v1.1         | Twitter API v2        |
+-----------------------+-----------------------+-----------------------+
| HTTP methods          | ` GET `               | ` GET `               |
| supported             |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Host domain           | ` http                | ` http                |
|                       | s://api.twitter.com ` | s://api.twitter.com ` |
+-----------------------+-----------------------+-----------------------+
| Endpoint path         | ` /1.1/lis            | ` /2/users/:          |
|                       | ts/memberships.json ` | id/list_memberships ` |
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
| Default request [rate | 75 requests per 15    | 75 requests per 15    |
| limits](https://devel | min with OAuth 1.0a   | min with OAuth 1.0a   |
| oper.twitter.com/cont |                       |                       |
| ent/developer-twitter | 75 requests per 15min | 75 requests per 15    |
| /en/docs/rate-limits) | with App only         | min with OAuth 2.0    |
|                       |                       |                       |
|                       |                       | 75 requests per 15min |
|                       |                       | with App only         |
+-----------------------+-----------------------+-----------------------+

### 

### Manage List members

The v2 manage List members endpoints will replace the standard [POST
lists/members/create](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-members-create)
, [POST
lists/members/destroy](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-members-destroy)
endpoints.

The following tables compare the standard v1.1 and Twitter API v2 List
endpoints:

**Add member**

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
|                       | /1.1/list             | /2/lists/:id/members  |
|                       | s/members/create.json | ]{.code-inline}       |
|                       | ]{.code-inline}       |                       |
+-----------------------+-----------------------+-----------------------+
| [Aut                  | OAuth 1.0a User       | OAuth 1.0a User       |
| hentication](/content | Context               | Context               |
| /developer-twitter/en |                       |                       |
| /docs/authentication) |                       | OAuth 2.0             |
|                       |                       | Authorization Code    |
|                       |                       | with PKCE             |
+-----------------------+-----------------------+-----------------------+
| Default request [rate | None                  | 300 requests per 15   |
| limits](/cont         |                       | min (per user)        |
| ent/developer-twitter |                       |                       |
| /en/docs/rate-limits) |                       |                       |
+-----------------------+-----------------------+-----------------------+

**Remove member**

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
|                       | /1.1/lists            | /2/lists/:id/:user_id |
|                       | /members/destroy.json | ]{.code-inline}       |
|                       | ]{.code-inline}       |                       |
+-----------------------+-----------------------+-----------------------+
| [Aut                  | OAuth 1.0a User       | OAuth 1.0a User       |
| hentication](/content | Context               | Context               |
| /developer-twitter/en |                       |                       |
| /docs/authentication) |                       | OAuth 2.0             |
|                       |                       | Authorization Code    |
|                       |                       | with PKCE             |
+-----------------------+-----------------------+-----------------------+
| Default request [rate | None                  | 300 requests per 15   |
| limits](/cont         |                       | min (per user)        |
| ent/developer-twitter |                       |                       |
| /en/docs/rate-limits) |                       |                       |
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
