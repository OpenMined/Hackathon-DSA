::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
If you have been working with the standard v1.1 [POST
statuses/retweet/:id](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-retweet-id)
, and [POST
statuses/unretweet/:id](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-unretweet-id)
endpoints, the goal of this guide is to help you understand the
similarities and differences between the standard and Twitter API v2
Retweets endpoints.

-   **Similarities**
-   **Differences**
    -   Endpoint URLs and HTTP methods
    -   Request limitations
    -   App and Project requirements
    -   Request parameters

### Similarities

#### Authentication

Both the standard v1.1 and Twitter API v2 manage Retweets ( [POST
statuses/retweet/:id](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-retweet-id)
, and [POST
statuses/unretweet/:id](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-unretweet-id)
) endpoints use [OAuth 1.0a User
Context](https://developer.twitter.com/content/developer-twitter/en/docs/authentication/oauth-1-0a)
. Therefore, if you were previously using one of the standard v1.1
Retweets lookup endpoints, you can continue using the same
authentication method if you migrate to the Twitter API v2 version.

### Differences

#### Endpoint URLs and HTTP methods

-   Standard v1.1 endpoints:
    -   [ https://api.twitter.com/1.1/statuses/retweet/:id.json\
        ]{.code-inline} (Retweets a tweet. Returns the original Tweet
        with Retweet details embedded)
    -   [ https://api.twitter.com/1.1/statuses/unretweet/:id.json\
        ]{.code-inline} (Undo a Retweet. Returns the original Tweet with
        Retweet details embedded)
-   Twitter API v2 endpoint:
    -   [ https://api.twitter.com/2/tweets/:id/retweets\
        ]{.code-inline} (Retweets a given Tweet)
    -   [ https://api.twitter.com/2/users/:id/retweets/:source_tweet_id\
        ]{.code-inline} (Undo a Retweet of a given Tweet)

#### App and Project requirements

The Twitter API v2 endpoints require that you use credentials from a
[developer App](/en/docs/apps) that is associated to a
[Project](/en/docs/projects) when authenticating your requests. All
Twitter API v1.1 endpoints can use credentials from standalone Apps or
Apps associated with a Project.

#### Request parameters

The following standard v1.1 request parameters accepted two request
query parameters (user_id or screen_name). The Twitter API v2 only
accepts the numerical user ID, and it must be passed as part of the
endpoint path.

  Standard v1.1                             Twitter API v2
  ----------------------------------------- --------------------------
  **[ id ]{.code-inline}**                  **[ id ]{.code-inline}**
  **[ includes_entities ]{.code-inline}**   No equivalent

Please note that the Standard v1.1 parameters are passed as query
parameters, whereas the Twitter API v2 parameters are passed as body
parameters for the POST endpoint or path parameters for the DELETE
endpoint.

Also, an [ id ]{.code-inline} of the user Retweeting a Tweet is not
required when using the standard v1.1 endpoints since the [Access
Tokens](/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens)
passed with [OAuth 1.0a User
Context](/en/docs/authentication/oauth-1-0a) infer which user is
initiating the Retweet/undoing a Retweet.
:::
:::
:::
:::
:::
:::
:::
:::
