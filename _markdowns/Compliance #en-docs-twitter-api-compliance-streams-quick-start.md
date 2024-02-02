::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
This quick start guide will help you make your first request to the
compliance stream endpoints using a cURL request. cURL is a command line
tool which allows you to make requests with minimal configuration.

If you would like to see sample code in different programming languages,
please visit our [Twitter API v2 sample code GitHub
repository](https://github.com/twitterdev/Twitter-API-v2-sample-code) .
\
:::
:::

::: dtc09-callout-text
::: dtc09-callout-text
::: dtc09__item
::: dtc09__text
::: c01-rich-text-editor
::: is-table-default
The compliance streams is available with Enterprise access.

To complete this guide, you will need to have a set of [keys and
tokens](/en/docs/authentication) to authenticate your request. You can
generate these keys and tokens by following these steps:

-   [Sign up for a developer account](/en/apply-for-access) and receive
    approval.
-   Create a [Project](/en/docs/projects) and an associated [developer
    App](/en/docs/apps) in the developer portal.
-   Navigate to your App\'s "Keys and tokens" page to generate the
    required credentials. Make sure to save all credentials in a secure
    location.
:::
:::
:::
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
In this quick start, we are going to use a simple cURL request to
connect to a single partition of the Tweet compliance stream. There are
4 partitions in all, so 4 connections must be maintained to receive all
events. The Tweet compliance stream endpoint is a very simple one. All
you will have to do is replace or add a couple of elements of the below
request and submit it to your command line tool.
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 curl -X GET "https://api.twitter.com/2/tweets/compliance/stream?partition=1" \ 
-H "Authorization: Bearer $APP_ACCESS_TOKEN"

    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
To connect to the User compliance stream, update the request URL to
 \"https://api.twitter.com/2/users/compliance/stream?partition=1\"

#### Step two: Authenticate your request

Since the compliance stream endpoints require [OAuth 2.0
App-Only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only)
authentication, you will need to replace \$APP_ACCESS_TOKEN with the App
Access Token that you generated in the prerequisites.

#### Step three: Make your request and review your response

Once you have everything set up, you can submit your request to Twitter
using the cURL command-line tool. If done successfully, you will receive
a live stream of Tweet compliance events with payloads similar to the
following:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button .t05__pre--wrap-text}
 {"data":{"delete":{"tweet":{"id":"1543734217692828673","author_id":"906948460078698496"},"event_at":"2022-07-08T17:54:25.052Z"}}}
{"data":{"delete":{"tweet":{"id":"1518339433317514240","author_id":"906948460078698496"},"event_at":"2022-07-08T17:54:25.098Z"}}}
{"data":{"delete":{"tweet":{"id":"1543019691868381185","author_id":"906948460078698496"},"event_at":"2022-07-08T17:54:25.156Z"}}}
{"data":{"delete":{"tweet":{"id":"1545202024509778944","author_id":"906948460078698496"},"event_at":"2022-07-08T17:54:25.090Z"}}}

    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
If you would like to close your connection, you can press Control-C in
your command line tool on either Mac or Windows systems to break the
connection, or you can also close the window.

Your code can parse each JSON line to locate the Tweet (or User ID if
using the User compliance stream) and delete the Tweets (or Users) with
those IDs from your dataset to stay in compliance.
:::
:::
:::
