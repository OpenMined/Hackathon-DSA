::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Using blocks lookup, you can see who you or an authenticated user has
blocked. This can be useful for determining how you can interact with a
given account.

### Blocks lookup

The blocks lookup GET endpoint allows you to see which accounts you've
blocked on behalf of an authorized user. This endpoint has a rate limit
of 15 requests per 15 minutes per user.

Since you are making requests for private information with blocks
lookup, and on behalf of a user with manage blocks, you must
authenticate these endpoints with either [OAuth 1.0a User
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
