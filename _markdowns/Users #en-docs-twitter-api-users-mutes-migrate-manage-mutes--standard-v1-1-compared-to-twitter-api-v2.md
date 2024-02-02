::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
If you have been working with the standard v1.1 [POST
mutes/users/create](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/mute-block-report-users/api-reference/post-mutes-users-create)
and [POST
mutes/users/destroy](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/mute-block-report-users/api-reference/post-mutes-users-destroy)
endpoints, the goal of this guide is to help you understand the
similarities and differences between the standard v1.1 and Twitter API
v2 manage mutes endpoints.

-   **Similarities**
-   **Differences**
    -   Endpoint URLs
    -   App and Project requirements
    -   HTTP methods
    -   Request parameters\

### Similarities

#### OAuth 1.0a User Context authentication method

Both the endpoint versions support [OAuth 1.0a User
Context](https://developer.twitter.com/content/developer-twitter/en/docs/authentication/oauth-1-0a)
. Therefore, if you were previously using one of the standard v1.1
manage mutes endpoints, you can continue using the same authentication
method if you migrate to the Twitter API v2 version.

### Differences

#### Endpoint URLs

-   Standard v1.1 endpoints:
    -   [ POST https://api.twitter.com/1.1/mutes/users/create.json\
        ]{.code-inline} (mute a user)
    -   [ POST https://api.twitter.com/1.1/mutes/users/destroy.json\
        ]{.code-inline} (unmute a user)
-   Twitter API v2 endpoint:
    -   [ POST https://api.twitter.com/2/users/:id/muting\
        ]{.code-inline} (mute a user)
    -   [ DELETE
        https://api.twitter.com/2/users/:source_user_id/muting/:target_user_id\
        ]{.code-inline} (unmute a user)

#### App and Project requirements

The Twitter API v2 endpoints require that you use credentials from a
[developer App](https://developer.twitter.com/en/docs/apps) that is
associated with a
[Project](https://developer.twitter.com/en/docs/projects) when
authenticating your requests. All Twitter API v1.1 endpoints can use
credentials from standalone Apps or Apps associated with a project.

#### Request parameters

The following standard v1.1 request parameters have equivalents in
Twitter API v2:

  Standard v1.1                   Twitter API v2
  ------------------------------- ----------------------------------
  [ user_id ]{.code-inline}       [ target_user_id ]{.code-inline}
  [ screen_name ]{.code-inline}   No equivalent

Please note that the Standard v1.1 parameters are passed as query
parameters, whereas the Twitter API v2 parameters are passed as body
parameters (for the POST endpoint) or path parameters (for the DELETE
endpoint).

Also, an [ id ]{.code-inline} of the user muting a target user is not
required when using the standard v1.1 endpoints since the access tokens
passed with [OAuth 1.0a User
Context](/en/docs/authentication/oauth-1-0a) inferred which user was
initiating the mute/unmute.
:::
:::
:::
:::
:::
:::
:::
:::
