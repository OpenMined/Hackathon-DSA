::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
[Twitter Lists](https://help.twitter.com/en/using-twitter/twitter-lists)
allows users to customize, organize and prioritize the Tweets they see
in their timeline. With the Lists endpoints, you can build solutions
that enable people to curate and organize Tweets based on preferences,
interests, groups, or topics.

Since you are making requests on behalf of a user with the manage List
endpoints, you must authenticate these endpoints with either [OAuth 1.0a
User Context](/en/docs/authentication/oauth-1-0a) or [OAuth 2.0
Authorization Code with
PKCE](/en/docs/authentication/oauth-2-0/authorization-code) , and use
the user Access Tokens associated with a user that has authorized your
App, which can be generated using the [3-legged OAuth
flow](/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens)
(OAuth 1.0a) or the [Authorization Code with PKCE grant
flow](/en/docs/authentication/oauth-2-0/user-access-token) (OAuth 2.0).\

### Manage Lists

The manage List endpoints allow you to create, delete, and update Lists
on behalf of an authenticated user. For these endpoints, there are three
methods available: POST, DELETE and PUT. The POST method allows you to
create a List, the DELETE method allows you to delete a List, and the
PUT method allows you to update the metadata of a List. There is a user
rate limit of 300 requests per 15 minutes for all three endpoints.

Note that you can create up to 1000 Lists per account.
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
