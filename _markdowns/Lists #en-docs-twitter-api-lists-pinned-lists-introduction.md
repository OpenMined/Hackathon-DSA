::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Pinning lists allows Twitter users to more easily access lists that
they\'ve either subscribed to or created themselves.

Since you are making requests on behalf of a user with the these
endpoints, you must authenticate them with either [OAuth 1.0a User
Context](/en/docs/authentication/oauth-1-0a) or [OAuth 2.0 Authorization
Code with PKCE](/en/docs/authentication/oauth-2-0/authorization-code) ,
and use the user Access Tokens associated with a user that has
authorized your App, which can be generated using the [3-legged OAuth
flow](/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens)
(OAuth 1.0a) or the [Authorization Code with PKCE grant
flow](/en/docs/authentication/oauth-2-0/user-access-token) (OAuth 2.0).
\

### Pinned List lookup

Pinned List lookup has one available endpoint that allows you to
retrieve an authenticated user\'s pinned Lists. There is a rate limit of
15 requests per 15 minutes for this endpoint.\

### Manage pinned Lists

The manage pinned List endpoints allow you to pin and unpin a List on
behalf of an authenticated user. For these endpoints, there are two
methods available: POST and DELETE. The POST method allows you to pin a
List, and the DELETE method allows you to unpin a List. There is a user
rate limit of 50 requests per 15 minutes for both endpoints.
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
