::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: dtc09-callout-text
::: dtc09-callout-text
:::
:::

::: c01-rich-text-editor
::: is-table-default
[ Standard ]{.subscription-tag .subscription-tag--standard}

The best way to build a query and test if it's valid and will return
matched Tweets is to first try it at
[twitter.com/search](https://twitter.com/search) . As you get a
satisfactory result set, the URL loaded in the browser will contain the
proper query syntax that can be reused in the API endpoint. Here's an
example:

1.  We want to search for Tweets referencing \@twitterapi account.
    First, we run the search on
    [twitter.com/search](https://twitter.com/search)
2.  Check and copy the URL loaded. In this case, we got:
    <https://twitter.com/search?q=%40twitterapi>
3.  Replace [ https://twitter.com/search ]{.code-inline} with [
    https://api.twitter.com/1.1/search/tweets.json ]{.code-inline} and
    you will get: [
    https://api.twitter.com/1.1/search/tweets.json?q=%40twitterapi
    ]{.code-inline}
4.  Run a Twurl command to execute the search.

Please note that the API requires that the request is authenticated
(check [Authentication &
Authorization](/en/docs/basics/authentication/overview/authentication-and-authorization.html)
documentation for more details on this). Also note that the search
results at twitter.com may return historical results, while the Search
API usually only serves Tweets from the past week.
:::
:::
:::
:::
:::
:::
:::
:::
