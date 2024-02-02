::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
The v2 mutes lookup endpoint will replace the standard [v1.1 GET
mutes/users/ids](/content/developer-twitter/en/docs/twitter-api/v1/accounts-and-users/mute-block-report-users/api-reference/get-mutes-users-ids)
and [GET
mutes/users/list](/content/developer-twitter/en/docs/twitter-api/v1/accounts-and-users/mute-block-report-users/api-reference/get-mutes-users-list)
endpoints.

The following tables compare the standard v1.1 and Twitter API v2 mute
endpoints:\

+-----------------------+-----------------------+-----------------------+
| Description           | Standard v1.1         | Twitter API v2        |
+=======================+=======================+=======================+
| HTTP methods          | ******[ GET           | ******[ GET           |
| supported             | ]{.code-inline}****** | ]{.code-inline}****** |
+-----------------------+-----------------------+-----------------------+
| Host domain           | ******[               | ******[               |
|                       | ht                    | ht                    |
|                       | tps://api.twitter.com | tps://api.twitter.com |
|                       | ]{.code-inline}****** | ]{.code-inline}****** |
+-----------------------+-----------------------+-----------------------+
| Endpoint path         | ******[               | ******[               |
|                       | /1.1                  | /2/users/:id/muting   |
|                       | /mutes/users/ids.json | ]{.code-inline}****** |
|                       | ]{.code-inline}****** |                       |
|                       |                       |                       |
|                       | [                     |                       |
|                       | /1.1/                 |                       |
|                       | mutes/users/list.json |                       |
|                       | ]{.code-inline}       |                       |
+-----------------------+-----------------------+-----------------------+
| [Aut                  | OAuth 1.0a User       | OAuth 1.0a User       |
| hentication](/content | Context               | Context               |
| /developer-twitter/en |                       |                       |
| /docs/authentication) |                       | OAuth 2.0             |
|                       |                       | Authorization Code    |
|                       |                       | with PKCE             |
+-----------------------+-----------------------+-----------------------+
| Default request [rate | 15 requests per 15    | 15 requests per 15    |
| limits](/cont         | min (per user)        | min (per user)        |
| ent/developer-twitter |                       |                       |
| /en/docs/rate-limits) |                       |                       |
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
| Requires use of       |                       | ✔️                    |
| credentials from a    |                       |                       |
| [developer            |                       |                       |
| App](/en/docs/apps)   |                       |                       |
| that is associated    |                       |                       |
| with a                |                       |                       |
| [Projec               |                       |                       |
| t](/en/docs/projects) |                       |                       |
+-----------------------+-----------------------+-----------------------+

### []{#manage} Manage mutes

The v2 manage mutes endpoints will replace the standard v1.1 [POST
mutes/users/create](/en/docs/twitter-api/v1/accounts-and-users/mute-block-report-users/api-reference/post-mutes-users-create)
and [POST
mutes/users/destroy](/en/docs/twitter-api/v1/accounts-and-users/mute-block-report-users/api-reference/post-mutes-users-destroy)
endpoints.

The following tables compare the standard v1.1 and Twitter API v2 mute
endpoints:

#### Mute a user

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
| Endpoint path         | [                     | [ /2/users/:id/muting |
|                       | /1.1/mu               | ]{.code-inline}       |
|                       | tes/users/create.json |                       |
|                       | ]{.code-inline}       |                       |
+-----------------------+-----------------------+-----------------------+
| [Aut                  | OAuth 1.0a User       | OAuth 1.0a User       |
| hentication](/content | Context               | Context               |
| /developer-twitter/en |                       |                       |
| /docs/authentication) |                       | OAuth 2.0             |
|                       |                       | Authorization Code    |
|                       |                       | with PKCE             |
+-----------------------+-----------------------+-----------------------+
| Default request [rate | 50 requests per 15    | 50 requests per 15    |
| limits](/cont         | min                   | min                   |
| ent/developer-twitter |                       |                       |
| /en/docs/rate-limits) |                       |                       |
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

#### Unmute a user

The following tables compare the standard v1.1 and Twitter API v2 unmute
endpoints:

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
|                       | /1.1/mut              | /2/us                 |
|                       | es/users/destroy.json | ers/:source_user_id/m |
|                       | ]{.code-inline}       | uting/:target_user_id |
|                       |                       | ]{.code-inline}       |
+-----------------------+-----------------------+-----------------------+
| [Aut                  | OAuth 1.0a User       | OAuth 1.0a User       |
| hentication](/content | Context               | Context               |
| /developer-twitter/en |                       |                       |
| /docs/authentication) |                       | OAuth 2.0             |
|                       |                       | Authorization Code    |
|                       |                       | with PKCE             |
+-----------------------+-----------------------+-----------------------+
| Default request [rate | 50 requests per 15    | 50 requests per 15    |
| limits](/cont         | min                   | min\                  |
| ent/developer-twitter |                       |                       |
| /en/docs/rate-limits) |                       |                       |
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
