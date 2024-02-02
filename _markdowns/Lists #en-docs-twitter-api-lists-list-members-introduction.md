::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Members lookup group has two available endpoints. You are able to
retrieve details on members of a specified List and see which Lists a
user is a member of. These endpoints can be used to enable people to
curate and organize new Lists based on the membership information.

There is a rate limit of 900 requests per 15 minutes when looking up
member details and a limit of 75 requests per 15 minutes when looking up
user memberships.

You can use [OAuth 1.0a User
Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a)
, [App
only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only)
, or [OAuth 2.0 Authorization Code with
PKCE](/en/docs/authentication/oauth-2-0/authorization-code) to
authenticate your requests to this endpoint.\

### Manage List members

The manage List members endpoints allow you to add and remove members to
a List on behalf of an authenticated user. For these endpoints, there
are two methods available: POST and DELETE. The POST method allows you
to add a member to a List, and the DELETE method allows you to remove a
member from a List. There is a user rate limit of 300 requests per 15
minutes for both endpoints.

Note that Lists cannot have more than 5,000 members.

Since you are making requests on behalf of a user with the these
endpoints, you must authenticate them with either [OAuth 1.0a User
Context](/en/docs/authentication/oauth-1-0a) or [OAuth 2.0 Authorization
Code with PKCE](/en/docs/authentication/oauth-2-0/authorization-code) ,
and use the user Access Tokens associated with a user that has
authorized your App, which can be generated using the [3-legged OAuth
flow](/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens)
(OAuth 1.0a) or the [Authorization Code with PKCE grant
flow](/en/docs/authentication/oauth-2-0/user-access-token) (OAuth 2.0).
:::
:::

::: dtc09-callout-text
::: dtc09-callout-text
:::
:::
:::
:::
:::
:::
:::
:::
