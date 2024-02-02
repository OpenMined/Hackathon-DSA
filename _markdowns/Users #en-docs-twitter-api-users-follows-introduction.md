::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Following users is one of the most foundational actions on Twitter.

We offer two sets of endpoint groups to help you lookup, create, and
delete follow relationships: follows lookup and manage follows.\

### Follows lookup

The follows lookup endpoints enable you to explore and analyze
relationships between users, which is sometimes called network analysis.
Specifically, there are two REST endpoints that return [user
objects](/en/docs/twitter-api/data-dictionary/object-model/user)
representing who a specified user is following, or who is following a
specified user.

You can authenticate this endpoint with either [OAuth 1.0a User
Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a)
, [App
only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only)
, or [OAuth 2.0 Authorization Code with
PKCE](/en/docs/authentication/oauth-2-0/authorization-code) . You can
request up to 1,000 users per request, and pagination tokens will be
provided for paging through large sets of results.\

### Manage follows

The manage follows endpoints enable you to follow or unfollow users.

Since you are making requests on behalf of a user, you must authenticate
these endpoints with either [OAuth 1.0a User
Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a)
or [OAuth 2.0 Authorization Code with
PKCE](/en/docs/authentication/oauth-2-0/authorization-code) , and
utilize the user Access Tokens associated with the user you are making
the request on behalf of. You can generate this user Access Token using
the [3-legged OAuth
flow](/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens)
(OAuth 1.0a) or using the [Authorization Code with PKCE grant
flow](/en/docs/authentication/oauth-2-0/user-access-token) (OAuth 2.0).

You are limited to 400 follow actions per day on behalf of each
authenticated user, and will be limited to 1,000 actions per day per App
across all of your authenticated users. For example, if you have five
authenticated users, you can follow 400 users per day (per user limit)
with two of those users for a total of 800 actions, and will have to
split the remaining 200 actions (per app) amongst the remaining three
users. This limit does not apply to the unfollow endpoint, which has a
separate limit of 500 actions per day (per app).
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
