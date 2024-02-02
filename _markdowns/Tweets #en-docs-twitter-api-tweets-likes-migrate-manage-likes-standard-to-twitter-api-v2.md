::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
If you have been working with the standard v1.1 [POST
favorites/create](/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-favorites-create)
and [POST
favorites/destroy](/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-favorites-destroy)
endpoints, the goal of this guide is to help you understand the
similarities and differences between the standard v1.1 and Twitter API
v2 manage Likes endpoints.

-   **Similarities**
-   **Differences**
    -   Endpoint URLs and HTTP methods
    -   Request limitations
    -   App and Project requirements
    -   Request parameters

### Similarities

#### OAuth 1.0a User Context authentication method

Both the endpoint versions support [OAuth 1.0a User
Context](/content/developer-twitter/en/docs/authentication/oauth-1-0a) .
Therefore, if you were previously using one of the standard v1.1
manage favorites endpoints, you can continue using the same
authentication method if you migrate to the Twitter API v2 version.

### Differences

#### Endpoint URLs and HTTP methods

-   Standard v1.1 endpoints:
    -   [ POST https://api.twitter.com/1.1/favorites/create.json\
        ]{.code-inline} (like a Tweet)
    -   [ POST https://api.twitter.com/1.1/favorites/destroy.json\
        ]{.code-inline} (unlike a Tweet)
-   Twitter API v2 endpoint:
    -   [ POST https://api.twitter.com/2/tweets/:id/likes\
        ]{.code-inline} (like a Tweet)
    -   [ DELETE https://api.twitter.com/2/tweets/:id/likes/:tweet_id\
        ]{.code-inline} (unlike a Tweet)

**Request limitations**

The v2 liked Tweets endpoint allows you to request 5 to 100 Tweets per
request. You can use pagination tokens and multiple requests to get all
of a user's liked Tweets. The v1.1 GET favorites/list endpoint also
allows you to pull all liked  Tweets, but you can pull from 20 to 200
Tweets per request. \

For the v2 liking users endpoint, you are limited to 100 liking users
per Tweet.

#### App and Project requirements

The Twitter API v2 endpoints require that you use credentials from a
[developer App](/en/docs/apps) that is associated to a
[Project](/en/docs/projects) when authenticating your requests. All
Twitter API v1.1 endpoints can use credentials from standalone Apps or
Apps associated with a Project.

#### Request parameters

The following standard v1.1 request parameters have equivalents in
Twitter API v2:

  Standard v1.1                         Twitter API v2
  ------------------------------------- ----------------------
  [ id ]{.code-inline}                  [ id ]{.code-inline}
  [ includes_entities ]{.code-inline}   No equivalent

Please note that the Standard v1.1 parameters are passed as query
parameters, whereas the Twitter API v2 parameters are passed as body
parameters for the POST endpoint or path parameters for the DELETE
endpoint.

Also, an [ id ]{.code-inline} of the user liking a Tweet is not required
when using the standard v1.1 endpoints since the [Access
Tokens](/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens)
passed with [OAuth 1.0a User
Context](/en/docs/authentication/oauth-1-0a) infer which user is
initiating the like/unlike.
:::
:::
:::
:::
:::
:::
:::
:::
