::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: dtc09-callout-text
::: dtc09-callout-text
::: dtc09__item
::: dtc09__text
::: c01-rich-text-editor
::: is-table-default
**Please note:**

These recovery and redundancy features are only available to those that
have been approved for [Enterprise
Access](https://developer.twitter.com/en/docs/twitter-api/enterprise) .
:::
:::
:::
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
When consuming realtime data, maximizing your connection time and
receiving all matched data is a fundamental goal. This means that it is
important to take advantage of redundant connections, automatically
detect disconnections, to reconnect quickly, and to have a plan for
recovering lost data.

In this integration guide, we will discuss two different recovery and
redundancy features: redundant connections and backfill.\

### Redundant connections

A redundant connection simply allows you to establish more than one
simultaneous connections to sampled stream. This provides redundancy by
allowing you to connect to the same stream with two separate consumers,
receiving the same data through both connections. Thus, your app has a
hot failover for various situations such as if one stream is
disconnected or if your application\'s primary server fails.

Sampled stream currently only allows those with [Enterprise
Access](https://developer.twitter.com/en/docs/twitter-api/enterprise) to
connect to up to two redundant connections. To use a redundant stream,
simply connect to the same URL used for your primary connection. The
data for your stream will be sent through both connections.\

### Recovering missed data after a disconnection: Backfill

After you\'ve detected a disconnection, your system should be smart
enough to reconnect to the stream. If possible, your system should take
note of how long the disconnection lasted so that you can use the proper
recovery feature to backfill the data.

If you are using a Project with Academic Research access and identified
that the disconnection lasted five minutes or less, you can use the
backfill parameter, [ backfill_minutes ]{.code-inline} . If you pass
this parameter with your [GET
/tweets/sample/stream](/en/docs/twitter-api/tweets/sampled-stream/api-reference/get-tweets-sample-stream)
request, you will receive the Tweets that match your rules within the
past one to five minutes. We generally deliver these older Tweets first
before any newer sampled Tweets, and also do not deduplicate Tweets.
This means that if you were disconnected for 90 seconds, but request two
minutes worth of backfill data, you will receive 30 seconds worth of
duplicate Tweets, which your system should be tolerant of. Here is an
example of what a request might look like with the backfill parameter:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 curl 'https://api.twitter.com/2/tweets/sample/stream?backfill_minutes=5' -H "Authorization: Bearer $BEARER_TOKEN"
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
\
If you don\'t have access to the Enterprise access, or identified that
the disconnection time lasted for longer than five minutes, you can try
to utilize the [recent search
endpoint](/en/docs/twitter-api/tweets/search/introduction) to request
missed data. However, note that the search Tweets endpoints do not
include the [ sample: ]{.code-inline} operator, so requesting a random
sample of data is not possible.
:::
:::
:::
:::
:::
:::
:::
:::
