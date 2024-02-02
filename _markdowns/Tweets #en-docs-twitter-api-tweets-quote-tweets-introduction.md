::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
The Quote Tweets lookup endpoint gives the Quote Tweets for a given
Tweet ID.  This allows developers that build apps and clients to get the
Quote Tweets for a Tweet quickly and efficiently. It also makes it easy
for researchers to study the full conversation around a Tweet including
all its Quote Tweets.

Here is a Quote Tweet for a Tweet from \@TwitterAPI:

> Today, OAuth 2.0 and new fine-grained permission scopes are available
> to all developers for Twitter API v2 endpoints.
> <https://t.co/rNxC0GQDoP>
>
> --- Twitter API (@TwitterAPI) [December 14,
> 2021](https://twitter.com/TwitterAPI/status/1470836235413295107?ref_src=twsrc%5Etfw)

The Quote Tweets lookup endpoint is a REST endpoint that takes a single
path parameter to indicate the desired Tweet (by Tweet ID).

Tweets are delivered in reverse-chronological order, starting with the
most recent. Results are
[paginated](https://developer.twitter.com/en/docs/twitter-api/pagination.html)
up to 100 Tweets per page (10 Tweets by default). Pagination tokens are
provided for paging through large sets of Tweets.

The Quote Tweets endpoint supports
[fields](https://developer.twitter.com/en/docs/twitter-api/fields) and
[expansions](https://developer.twitter.com/en/docs/twitter-api/expansions)
parameters, and returns the [new JSON data
format](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/introduction)
.

This endpoint will always return the most recent edit, along with the
edit history. Any Tweet collected after its 30-minute edit window will
represent its final version and will include an array of IDs for all
Tweets in its edit history. For Tweets with no edit history, this array
will hold a single ID.

To successfully make a request to this endpoint, you will need to
authorize your request with the [OAuth 1.0a User
Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a)
, [OAuth 2.0 Authorization Code with
PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code)
, or [OAuth 2.0
App-Only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only)
authentication methods. You must use OAuth 1.0a User Context or OAuth
2.0 Authorization Code with PKCE when requesting non public metrics,
promoted metrics or a protected user\'s timeline.
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
