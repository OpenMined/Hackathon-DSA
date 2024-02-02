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
use cases. These use cases range from group chats among friends to
powering customer support for brands around the world. New v2 versions
of Direct Messages endpoints will be introduced in stages, and this
first stage includes fundamental endpoints for creating Direct Messages
and listing Direct Message conversation events. For the first time, the
Twitter API v2 supports *group* conversations.

This initial release of Direct Messages lookup includes three GET
methods:

-   **GET /2/dm_conversations/with/:participant_id/dm_events** -
    Retrieves Direct Message events associated with a one-to-one
    conversation. The [ :participant_id ]{.code-inline} path parameter
    is the User ID of the account having the conversation with the
    authenticated user making this request.
-    **GET /2/dm_conversations/:dm_conversation_id/dm_events** -
    Retrieves Direct Message events associated with a specific
    conversation ID, as indicated by the [ :dm_conversation_id
    ]{.code-inline} path parameter.
-    **GET /2/dm_events** - Retrieves Direct Message events associated
    with a user, including both one-to-one and group conversations.
    Events from up to 30 days ago are available.

Note that Direct Message event IDs are common across the v1.1 and v2 (as
well as the Twitter App), so the v1.1 method to list a single event can
be used along with these new v2 endpoints. Also note that the Enterprise
and Premium Account Activity APIs support v2 one-to-one messages, but do
not yet support group conversations.

With this release, three event types are supported, and these endpoints
support query parameters to filter on them:

-   **MessageCreate** - A message has been created.
-   **ParticipantsJoin** - A new participant has joined a conversation.
-   **ParticipantsLeave** - A participant has left a conversation.

There is a user rate limit of 300 requests per 15 minutes for the GET
methods. This rate limit is shared across these GET endpoints.

Since you are making requests on behalf of a user with Direct Message v2
endpoints, you must authenticate with either [OAuth 1.0a User
Context](https://developer-staging.twitter.com/en/docs/authentication/oauth-1-0a)
or [OAuth 2.0 Authorization Code with
PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code)
, using Access Tokens associated with users that have authorized your
Twitter App. To generate these Access Tokens with OAuth 1.0a, you can
use the [3-legged OAuth
flow](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens)
. To generate user Access Tokens with OAuth 2.0, you can use the
[Authorization Code with PKCE grant
flow](https://developer.twitter.com/en/docs/authentication/oauth-2-0/user-access-token)
.
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
