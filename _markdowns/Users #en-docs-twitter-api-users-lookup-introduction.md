::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
The RESTful endpoint uses the GET method to return information about a
user or group of users, specified by a user ID or a username. The
response includes one or many [user
objects](/en/docs/twitter-api/data-dictionary/object-model/user) , which
deliver fields such as the Follower count, location, pinned Tweet ID,
and profile bio. Responses can also optionally include expansions to
return the full Tweet object for a user's pinned Tweet, including the
Tweet text, author, and other Tweet fields.

You can authenticate your request to all users lookup endpoints other
than the authenticated user lookup with [OAuth 1.0a User
Context](/en/docs/authentication/oauth-1-0a) , [App
only](/en/docs/authentication/oauth-2-0/application-only) , or [OAuth
2.0 Authorization code with
PKCE](/en/docs/authentication/oauth-2-0/authorization-code) . However,
if you would like to access private metrics or data from private users,
you will need to utilize OAuth 1.0a User Context or OAuth 2.0
Authorization Code with PKCE, and pass the authenticated users\' Access
Token with your request.

This endpoint is commonly used to receive up-to-date details on a user,
to verify that a user exists, or to update your stored details following
a compliance event.

### 

### Authenticated user lookup

If authenticating on behalf of other users, it is critical to be able to
see who you can make a request on behalf of.

This endpoint requires you to use [OAuth 1.0a User
Context](/en/docs/authentication/oauth-1-0a) or [OAuth 2.0 Authorization
Code with PKCE](/en/docs/authentication/oauth-2-0/authorization-code) .
It returns information about the authorized user, meaning the user that
is associated with the user Access Tokens that you pass with the
request.

You can access this endpoint via the GET method. There is a user rate
limit of 75 requests per 15 minutes for this endpoint.
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
