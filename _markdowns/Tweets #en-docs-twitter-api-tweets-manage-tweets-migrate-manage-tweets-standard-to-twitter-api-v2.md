::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
If you have been working with the standard v1.1 [POST
statuses/update](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-update)
and [POST
statuses/destroy/:id](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-destroy-id)
endpoints, the goal of this guide is to help you understand the
similarities and differences between the standard and Twitter API v2
manage Tweets endpoints. \

-   **Similarities**
-   **Differences**
    -    Endpoint URLs
    -    App and Project requirements \
    -    Request parameters \

### Similarities

####   **Authentication**  

Both the standard v1.1 and Twitter API v2 manage Tweets ( [POST
statuses/update](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-update)
and [POST
statuses/destroy/:id](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-destroy-id)
) endpoints use [OAuth 1.0a User
Context](https://developer.twitter.com/content/developer-twitter/en/docs/authentication/oauth-1-0a)
. Therefore, if you were previously using one of the standard v1.1
endpoints, you can continue using the same authentication method if you
migrate to the Twitter API v2 version.

### Differences

#### Endpoint URLs

-   Standard v1.1 endpoints:
    -   [ https://api.twitter.com/1.1/statuses/update.json\
        ]{.code-inline} (Creates a Tweet)
    -   ` https://api.twitter.com/1.1/statuses/destroy/:id.json `\
        (Deletes a Tweet)
-   Twitter API v2 endpoint:
    -   [ https://api.twitter.com/2/tweets\
        ]{.code-inline} (Creates a Tweet)
    -   [ https://api.twitter.com/2/tweets/:id ]{.code-inline}\
        (Deletes a specified Tweet)

#### App and Project requirements

The Twitter API v2 endpoints require that you use credentials from a
[developer App](/content/developer-twitter/en/docs/apps) that is
associated with a [Project](/content/developer-twitter/en/docs/projects)
when authenticating your requests. All Twitter API v1.1 endpoints can
use credentials from standalone Apps or Apps associated with a project.

#### Request parameters

The following standard v1.1 request parameters accepted two request
query parameters ( [ user_id ]{.code-inline} or [ screen_name
]{.code-inline} ). The Twitter API v2 only accepts the numerical Tweet
ID for the DELETE endpoint, and it must be passed as part of the
endpoint path.

For the POST endpoint, additional parameters will need to be passed in
via the JSON body of the request. You can learn more about what
parameters are available in the [API reference
guide](https://developer.twitter.com/en/docs/twitter-api/tweets/manage-tweets/api-reference)
.
:::
:::
:::
:::
:::
:::
:::
:::
