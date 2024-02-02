::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Direct Messages enable private conversations on Twitter. Direct Messages
are one of the most popular features of Twitter, with a wide variety of
use cases. These use cases range from group chats among friends, to
powering customer support for brands around the world. New v2 versions
of Direct Messages endpoints will be introduced in stages, and this
first stage includes fundamental endpoints for creating Direct Messages
and listing Direct Message conversation events. For the first time, the
Twitter API v2 supports *group* conversations.

This initial release of Manage Direct Messages includes three POST
methods for creating Direct Messages:

-   **POST /2/dm_conversations/with/:participant_id/messages** - Creates
    a one-to-one Direct Message. This method either creates a new 1-1
    conversation or retrieves the current conversation and adds the
    Direct Message to it. The [ :participant_id ]{.code-inline} path
    parameter is the User ID of the account receiving the message.
-   **POST /2/dm_conversations** - Creates a new group conversation and
    adds a Direct Message to it. These requests require a list of
    conversation participants. Note that you can create multiple
    conversations with the same participant list. These requests will
    always return a new conversation ID.
-   **POST /2/dm_conversations/:dm_conversation_id/messages** - Creates
    a Direct Message and adds it to an existing conversation. The [
    :dm_conversation_id ]{.code-inline} path parameter is the ID of the
    conversation that the message will be added to.

Note that Direct Message event IDs are common across the v1.1 and v2 (as
well as the Twitter App), so the v1.1 methods to hide/delete Direct
Messages can be used along with this new v2 endpoint. Also note that the
Enterprise and Premium Account Activity APIs support v2 one-to-one
messages, but do not yet support group conversations. \

There is a user rate limit of 200 requests per 15 minutes for the POST
method. There is also a rate limit of 1000 requests per 24 hours per
user. Additionally, there is a rate limit of 15000 requests per 24
hours. Note that these rate limits are shared across these POST
endpoints.

Since you are making requests on behalf of a user with the manage Tweets
endpoints, you must authenticate with either [OAuth 1.0a User
Context](https://developer-staging.twitter.com/en/docs/authentication/oauth-1-0a)
or [OAuth 2.0 Authorization Code with
PKCE](/en/docs/authentication/oauth-2-0/authorization-code) , and use a
user Access Tokens associated with a user that has authorized your App.
To generate this user Access Token with OAuth 1.0a, you can use the
[3-legged OAuth flow](/en/docs/authentication/oauth-2-0/bearer-tokens) .
To generate a user Access Token with OAuth 2.0, you can use the
[Authorization Code with PKCE grant
flow](/en/docs/authentication/oauth-2-0/user-access-token) . \
:::
:::

::: dtc09-callout-text
::: dtc09-callout-text
:::
:::

::: ct01-columns
:::
:::
:::
:::
:::
:::
:::
