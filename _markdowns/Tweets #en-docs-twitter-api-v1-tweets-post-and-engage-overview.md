::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
The following API endpoints can be used to programmatically create,
retrieve and delete Tweets, Retweets and Likes:

+-----------------------+-----------------------+-----------------------+
| **Tweets**            | **Retweets**          | **Likes (formerly     |
|                       |                       | favorites)**          |
+-----------------------+-----------------------+-----------------------+
| -   POST              | -   POST              | -   POST              |
|     statuses/update   |                       |                       |
| -   POST              |  statuses/retweet/:id |  favorites/create/:id |
|                       | -   POST              | -   POST              |
|  statuses/destroy/:id |     s                 |                       |
| -   GET               | tatuses/unretweet/:id | favorites/destroy/:id |
|     statuses/show/:id | -   GET               | -   GET               |
| -   GET               |                       |     favorites/list    |
|     statuses/oembed   | statuses/retweets/:id |                       |
| -   GET               | -   GET               |                       |
|     statuses/lookup   |     st                |                       |
|                       | atuses/retweets_of_me |                       |
|                       | -   GET               |                       |
|                       |     st                |                       |
|                       | atuses/retweeters/ids |                       |
+-----------------------+-----------------------+-----------------------+

For more details, please see the individual endpoint information within
the [API reference](/en/docs/tweets/post-and-engage/api-reference)
section.

### Terminology

**Tweet/Status** - when a status message is shared on Twitter. Also see
[Introduction to Tweet
JSON](/en/docs/tweets/data-dictionary/overview/intro-to-tweet-json.html)

**Retweet** - when a Tweet is re-shared by another specific user. Also
see [Introduction to Tweet
JSON](/en/docs/tweets/data-dictionary/overview/intro-to-tweet-json.html)\

**Like** - when a Tweet recieves a \'heart\' from a specific user,
formerly known as favo(u)rite or \'star\'

### Rate limits

As part of our effort to reduce the distribution of spam through our
APIs, we enforce App-level rate limit on some of our POST endpoints:

-   There is a 300 requests per three hours shared App-level rate limit
    for the POST statuses/update (post a Tweet) and POST
    statuses/retweet/:id (post a Retweet) endpoints. This means that you
    can only post either 300 Tweets or Retweets across all of the
    authorized users of your developer App during a three hour time
    period.
-   There is a 1,000 requests per 24 hours App-level rate limit for the
    POST favorites/create/:id endpoint. This means that you can only
    like 1,000 Tweets across all of the authorized users of your
    developer App during a 24 hour time period.

Please note that you must also consider the user-level rate limits for
these endpoints, as they limit the number of posted Tweets or liked
Tweets a specific authorized user can make over a given time period.

You can review each endpoints\' rate limits via their [API reference
page](/en/docs/tweets/post-and-engage/api-reference) .
:::
:::
:::
:::
:::
:::
:::
:::
