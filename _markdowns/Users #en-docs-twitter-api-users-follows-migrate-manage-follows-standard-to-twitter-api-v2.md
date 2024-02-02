::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
If you have been working with the standard v1.1 [POST
friendships/create](/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/post-friendships-create)
and [POST
friendships/destroy](/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/post-friendships-destroy)
endpoints, the goal of this guide is to help you understand the
similarities and differences between the standard and Twitter API v2
manage follows endpoints.

-   **Similarities**
-   **Differences**
    -   Endpoint URLs
    -   App and Project requirements
    -   HTTP methods
    -   Request parameters

### Similarities

#### OAuth 1.0a User Context authentication method

Both the endpoint versions support [OAuth 1.0a User
Context](/content/developer-twitter/en/docs/authentication/oauth-1-0a) .
Therefore, if you were previously using one of the standard v1.1 manage
follows endpoints, you can continue using the same authentication method
if you migrate to the Twitter API v2 version.

### Differences

#### Endpoint URLs

-   Standard v1.1 endpoints:
    -   [ POST https://api.twitter.com/1.1/friendships/create.json\
        ]{.code-inline} (follow a user)
    -   [ POST https://api.twitter.com/1.1/friendships/destroy.json\
        ]{.code-inline} (unfollow a user)
-   Twitter API v2 endpoint:
    -   [ POST https://api.twitter.com/2/users/:id/following\
        ]{.code-inline} (follow a user)
    -   [ DELETE
        https://api.twitter.com/2/users/:source_user_id/following/:target_user_id\
        ]{.code-inline} (unfollow a user)

#### App and Project requirements

The Twitter API v2 endpoints require that you use credentials from a
[developer App](/en/docs/apps) that is associated to a
[Project](/en/docs/projects) when authenticating your requests. All
Twitter API v1.1 endpoints can use credentials from standalone Apps or
Apps associated with a project.

#### Request parameters

The following standard v1.1 request parameters have equivalents in
Twitter API v2:

  Standard v1.1                   Twitter API v2
  ------------------------------- ------------------------------------------------------------------------
  No equivalent                   [ id ]{.code-inline} (POST), [ source_user_id ]{.code-inline} (DELETE)
  [ user_id ]{.code-inline}       [ target_user_id ]{.code-inline}
  [ screen_name ]{.code-inline}   No equivalent

Please note that the Standard v1.1 parameters are passed as query
parameters, whereas the Twitter API v2 parameters are passed as body
parameters (for the POST endpoint) or path parameters (for the DELETE
endpoint).

Also, the v2 [ id ]{.code-inline} and [ source_user_id ]{.code-inline}
are not required when using the standard v1.1 endpoints since the Access
Tokens passed with OAuth 1.0a User Context inferred which user was
initiating the follow/unfollow.
:::
:::
:::
:::
:::
:::
:::
:::
