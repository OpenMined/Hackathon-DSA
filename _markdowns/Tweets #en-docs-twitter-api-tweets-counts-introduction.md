::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
The v2 Tweet counts endpoints allow developers to understand and
retrieve the volume of data for a given query.  This can be beneficial
for a number of reasons, including:

-    Understand the Tweet volume for a keyword to build visualizations,
    such as trendlines. \
-   Understanding the time period in which an event or conversation
    occurred, to ensure your query captures the relevant data
-   Understanding how many Tweets a search query will return, in order
    to refine your query, before using the recent search or full-archive
    search endpoints.\
    **Please note:** The counts will not always match the result that
    will be returned from search endpoints because the search endpoints
    go through additional compliance that the counts endpoints do not go
    through
-   Understanding the size of the conversation around a topic, without
    actually having to pull the raw data, and put Tweets against your
    monthly [Tweet cap](/en/docs/twitter-api/tweet-caps) .

When developing a query, you will be limited to a certain query length
and to specific operators based on your [access
level](/en/docs/twitter-api/getting-started/about-twitter-api#v2-access-level)
.

-   If you are using a Project with Essential or Elevated access, you
    can use the core operators to develop your query, and can use
    queries up to 512 characters in length.
-   If you are using a Project with Academic Research access, you can
    use all available operators, and use queries up to 1024 characters
    in length.\
-   If you are using a Project with Enterprise access, you can use all
    available operators, and use queries up to 4096 characters in
    length.

You can also specify the granularity (which can be [ day ]{.code-inline}
, [ hour, ]{.code-inline} or [ minute ]{.code-inline} ) as well as the
time period for which you need the Tweet counts (using the [ start_time
]{.code-inline} and [ end_time ]{.code-inline} parameters). The default
time granularity that this endpoint uses is hour, which means if you do
not specify the granularity parameter, the endpoint will give you the
Tweet counts per hour, for the last 7 days.\
:::
:::

::: dtc09-callout-text
::: dtc09-callout-text
:::
:::

::: c01-rich-text-editor
::: is-table-default
### Recent Tweet counts

The recent Tweet counts endpoint allows you to programmatically retrieve
the numerical count of Tweets for a query, over the last seven days.
This endpoint is available via to anyone using keys and tokens that are
associated with an [App](/en/docs/apps) within a
[Project](/en/docs/projects) and uses [OAuth 2.0
App-Only](https://developer.twitter.com/content/developer-twitter/en/docs/authentication/oauth-2-0)
for authentication.

### Full-archive Tweet counts

[ Academic Research or Enterprise access only ]{.subscription-tag
.subscription-tag--product}

The full-archive Tweet counts endpoint allows you to programmatically
retrieve the numerical count of Tweets for a query, from the entire
archive of public Tweets. Currently, this endpoint is only available to
those that have been approved for [Academic Research or Enterprise
access](/en/docs/twitter-api/getting-started/about-twitter-api#v2-access-level)
and use the [OAuth 2.0
App-Only](https://developer.twitter.com/content/developer-twitter/en/docs/authentication/oauth-2-0)
for authentication.

One example: You could use the full-archive Tweet counts endpoint to see
the number of Tweets for the hashtag #SOSHurricaneHarvey per day between
August and September 2017.

**Please note:** The counts endpoint paginates at 31 days per response.
For example, setting a day [ granularity ]{.code-inline} , will return
the count of results per day for 31 days per page.  Setting an hour [
granularity ]{.code-inline} , will return the count of results per hour
for 744 (31 days x 24 hours) hours per page.  If you do not specify the
[ granularity ]{.code-inline} and time period, this endpoint will give
you Tweet counts for a query per hour, for the last 30 days.
:::
:::
:::
