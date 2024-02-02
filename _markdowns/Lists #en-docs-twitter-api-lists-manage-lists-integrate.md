::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
This page contains information on several tools and critical concepts
that you should know as you integrate the Lists endpoints into your
system. We've broken the page into a couple of different sections:

### []{#helpful} Helpful tools

Before we dive into some key concepts that will help you integrate this
endpoint, we recommend that you become familiar with:

#### Postman

Postman is a great tool that you can use to test out an endpoint. Each
Postman request includes every path and body parameter to help you
quickly understand what is available to you. To learn more about our
Postman collections, please visit our [\"Using
Postman\"](/en/docs/tools-and-libraries/using-postman) page.

#### Code samples

Are you interested in getting set up with this endpoint with some code
in your preferred coding language? We've got a handful of different code
samples available that you can use as a starting point on our [Github
page](https://github.com/twitterdev/Twitter-API-v2-sample-code) .

#### Third-party libraries

Take advantage of one of our communities' [third-party
libraries](/en/docs/twitter-api/tools-and-libraries) to help you get
started. You can find a library that works with the v2 endpoints by
looking for the proper version tag.

### Key concepts

#### []{#authentication} Authentication

All Twitter API v2 endpoints require you to authenticate your requests
with a set of credentials, also known as keys and tokens.

These specific endpoints requires the use of [OAuth 1.0a User
Context](/en/docs/authentication/oauth-1-0a) , which means that you must
use a set of API keys and user Access Tokens to make a successful
request. The Access Tokens must be associated with the user that you are
making the request on behalf of. If you would like to generate a set of
Access Tokens for another user, they must authorize or authenticate your
App using the [3-legged OAuth
flow](/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens) .

Please note that OAuth 1.0a can be tricky to use. If you are not
familiar with this authentication method, we recommend that you use a
[library](/content/developer-twitter/en/docs/twitter-api/tools-and-libraries)
or a tool like Postman to properly authenticate your requests.\
:::
:::

::: c01-rich-text-editor
::: is-table-default
To retrieve a set of authentication credentials that will work with the
Twitter API v2 endpoints, you must [sign up for a developer
account](https://developer.twitter.com/en/portal/petition/essential/basic-info)
, set up a [Project](/en/docs/projects) within that account, and created
a [developer App](/en/docs/apps) within that Project. You can then find
your keys and tokens within your developer App.\

#### []{#limits} Rate limits

Every day, many thousands of developers make requests to the Twitter
API. To help manage the sheer volume of these requests, [rate
limits](/content/developer-twitter/en/docs/twitter-api/rate-limits) are
placed on each endpoint that limits the number of requests that you can
make on behalf of your app or on behalf of an authenticated user.

These endpoints are rate limited at the user level, meaning that the
authenticated user that you are making the request on behalf of can only
call the endpoint a certain number of times across any developer App.

The chart below shows the rate limits for each endpoint.

  -------------------------------- ----------------- -----------------------------
  **Endpoint**                     **HTTP method**   **Rate limit**
  [ /2/lists ]{.code-inline}       POST              300 requests per 15 minutes
  [ /2/lists/:id ]{.code-inline}   DELETE / PUT      300 requests per 15 minutes
  -------------------------------- ----------------- -----------------------------
:::
:::
:::
:::
:::
:::
:::
:::
