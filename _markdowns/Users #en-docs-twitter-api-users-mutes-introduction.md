::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Muting an account allows you to remove an account\'s Tweets from your
timeline without unfollowing or blocking that account. Muted accounts
will not know that you\'ve muted them and you can unmute them at any
time. With manage mutes endpoints, developers can create safer
experiences for people on Twitter. One example of how to build with
manage mutes is an application that allows you to mute accounts that
might Tweet about specific topics for a specified length of time. With
the mutes lookup endpoint, you can see who you or an authenticated user
has muted. This can be useful to determine how you interact with the
muted accounts.

Since you are making requests for private information with mute lookup,
and on behalf of a user with manage mutes, you must authenticate these
endpoints with either [OAuth 1.0a User
Context](/en/docs/authentication/oauth-1-0a) or [OAuth 2.0 Authorization
Code with PKCE](/en/docs/authentication/oauth-2-0/authorization-code) ,
and use the user Access Tokens associated with a user that has
authorized your App, which can be generated using the [3-legged OAuth
flow](/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens)
(OAuth 1.0a) or the [Authorization Code with PKCE grant
flow](/en/docs/authentication/oauth-2-0/user-access-token) (OAuth 2.0).

### Mutes lookup

The mutes lookup endpoint allows you to see which accounts the
authenticated user has muted. This endpoint has a rate limit of 15
requests per 15 minutes per user.

### Manage mutes

The manage mute endpoints enable you to mute or unmute a specified
account on behalf of an authenticated user. For these endpoints, there
are two methods available: POST and DELETE. The POST method allows you
to mute an account, and the DELETE method allows you to unmute an
account. There is a user rate limit of 50 requests per 15 minutes for
both the POST and DELETE endpoints.

**Please note:** If a user mutes from [Twitter](https://twitter.com/) ,
there is a limit of 200 requests per 15 minutes.
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
