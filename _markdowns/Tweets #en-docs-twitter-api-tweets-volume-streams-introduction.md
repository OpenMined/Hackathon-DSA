::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Volume streams consist of two streaming endpoints that deliver a random
sample of publicly available Tweets in real-time. They are available to
Enterprise levels of access only.

-    1% sampled stream.
-   10% sampled stream. Commonly referred to as the \"Decahose.\"

These are referred to as \"volume streams\" because they both deliver
large volumes of data. Even the 1% stream can emit many dozens of Tweets
every second. With these streams, you can identify and track trends,
monitor general sentiment, monitor global events, and much more. \

These streaming endpoints deliver [Tweet
objects](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet)
through a persistent HTTP GET connection and use [OAuth 2.0
App-Only](https://developer.twitter.com/en/docs/authentication/oauth-2-0)
authentication. With Essential access, you can have one connection at a
time. With all levels of access, connection requests can be made up to
50 times per 15-minute window.

These volume stream endpoints support edited Tweets. These endpoints
will deliver edited Tweets, along with its edit history, including an
array of Tweet IDs. For Tweets with no edit history, this array will
hold a single ID. For Tweets that have been edited, this array contains
multiple IDs, arranged in ascending order reflecting the order of edits,
with the most recent version in the last position of the array. To learn
more about how Tweet edits work, see the [Tweet edits
fundamentals](/en/docs/twitter-api/tweet-edits) page.

*To use these APIs, you must first set up an account with our enterprise
sales team.*

### 
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
