::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: bl19-no-edit-wrap
::: {.c15-column-container .js-column-container}
::: {.container--mini .container--mobile}
::: {.column .column-6}
::: c01-rich-text-editor
<div>

[[ Enterprise ]{.subscription-tag
.subscription-tag--enterprise}](/en/products/twitter-api/enterprise)

*This is an enterprise API available within our managed access levels
only. To use this API, you must first set up an account with our
enterprise sales team. [[ Learn more
]{.with-caret}](/en/docs/twitter-api/enterprise)*\

The Engagement API provides access to Tweet impression and engagement
metrics. While most metrics and endpoints require you to authenticate
using [OAuth 1.0a User Context](/en/docs/authentication/oauth-1-0a) ,
you can access public Favorite, Retweet, Reply, and Video Views metrics
using [OAuth 2.0 Bearer Token](/en/docs/authentication/oauth-2-0) and
the /totals endpoint.

**Note:** You may observe differences between reported data on some of
the Twitter web dashboards, and the data reported in the Engagement API.
These differences occur because the web dashboards typically only show
engagements and/or impressions that occurred within the selected time
range. For example, a web dashboard may show engagement on Tweets within
the span of a calendar month, while the Engagement API may show
engagements that fall beyond the span of that month, but within the time
range requested. The Engagement API should be seen as the valid source,
in these cases.\

### []{#RequestEndpoints} Request endpoints []{.tall}

The Engagement API has three endpoints:

#### Current Totals: [/totals](/content/developer-twitter/en/docs/metrics/get-tweet-engagement/api-reference/post-insights-engagement#Totals)

-   Requests return a total metric for impressions and a total metric
    for engagements for the desired Tweets
-   Limited to the following metrics: Impressions, Engagements,
    Favorites, Replies, Retweets, Quote Tweets, and Video Views
-   Supports the ability to retrieve **Impressions** and **Engagements**
    metrics for Tweets created **within the last 90 days** using OAuth
    1.0a User Context
-   Supports the ability to retrieve **Favorites, Retweets, Quote
    Tweets, Replies,** and **Video Views** metrics for **any Tweet**
    using OAuth 2.0 Bearer token
-   The results are based on the current total of impressions and
    engagements at the time the request is made
-   Ideal for powering a dashboard report and for calculating engagement
    rates across a variety of \@handles
-   Supports requesting metrics for up to 250 Tweets per request\

#### Last 28 hours: [/28hr](/content/developer-twitter/en/docs/metrics/get-tweet-engagement/api-reference/post-insights-engagement#28hr)

-   Requests can return a total metric for impressions, a total metric
    for engagements, and breakdown of individual engagement metrics that
    have occurred in the last 28 hours
-   Data can be grouped by Tweet ID, and in time-series in aggregate, by
    day, or by hour
-   Ideal for tracking the performance of recently created content
-   Supports all available metrics
-   Supports requesting metrics for up to 25 Tweets per request\

#### Historical: [/historical](/content/developer-twitter/en/docs/metrics/get-tweet-engagement/api-reference/post-insights-engagement#Historical)

-   Requests can return impressions, engagements, and a breakdown of
    individual engagement metrics for the most recent one year, based on
    the engagement time (not the Tweet creation time).
-   Requests support a start date and end date parameter, providing
    flexibility to narrow into a specific time frame up to 4 weeks in
    duration.
-   Tweet engagement data is limited to only 365 days in the past.
-   Data can be grouped by Tweet ID, and in time-series in aggregate, by
    day, or by hour.
-   Ideal for evaluating recent performance against a historical
    benchmark or developing a historical picture of an \@handle's
    performance.
-   Supports all available metrics.
-   Supports requesting metrics for up to 25 Tweets per request.

### []{#EngagementTypes} Available metrics

The table below describes the types of metrics that can be accessed
through the Engagement API.

Please check out our [Interpreting the metrics
page](/content/developer-twitter/en/docs/metrics/get-tweet-engagement/guides/interpreting-metrics)
to learn more about the below metrics.

+-----------------+-----------------+-----------------+-----------------+
| Metric          | Endpoint        | User Context    | Description     |
|                 | Availability    | Required        |                 |
+-----------------+-----------------+-----------------+-----------------+
| impressions     | All             | Yes             | A count of how  |
|                 |                 |                 | many times the  |
|                 |                 |                 | Tweet has been  |
|                 |                 |                 | viewed. This    |
|                 |                 |                 | metric is only  |
|                 |                 |                 | available for   |
|                 |                 |                 | Tweets that     |
|                 |                 |                 | have been       |
|                 |                 |                 | posted within   |
|                 |                 |                 | the past 90     |
|                 |                 |                 | days.           |
+-----------------+-----------------+-----------------+-----------------+
| engagements     | All             | Yes             | A count of the  |
|                 |                 |                 | number of times |
|                 |                 |                 | a user has      |
|                 |                 |                 | interacted with |
|                 |                 |                 | the Tweet. This |
|                 |                 |                 | metric is only  |
|                 |                 |                 | available for   |
|                 |                 |                 | Tweets that     |
|                 |                 |                 | have been       |
|                 |                 |                 | posted within   |
|                 |                 |                 | the past 90     |
|                 |                 |                 | days.\          |
+-----------------+-----------------+-----------------+-----------------+
| favorites       | All             | Yes - /28hrs &  | A count of how  |
|                 |                 | /Historical     | many times the  |
|                 |                 |                 | Tweet has been  |
|                 |                 | No - /totals    | favorited.      |
+-----------------+-----------------+-----------------+-----------------+
| retweets        | All             | Yes - /28hrs &  | A count of how  |
|                 |                 | /Historical     | many times the  |
|                 |                 |                 | Tweet has been  |
|                 |                 | No - /totals    | Retweeted.      |
+-----------------+-----------------+-----------------+-----------------+
| quote_tweets    | /totals         | No - /totals \  | A count of      |
|                 |                 |                 | times a Tweet   |
|                 |                 |                 | has been        |
|                 |                 |                 | Retweeted with  |
|                 |                 |                 | a comment (also |
|                 |                 |                 | known as        |
|                 |                 |                 | Quote).         |
+-----------------+-----------------+-----------------+-----------------+
| replies         | All             | Yes - /28hrs &  | A count of how  |
|                 |                 | /Historical     | many times the  |
|                 |                 |                 | Tweet has been  |
|                 |                 | No - /totals    | replied to.     |
+-----------------+-----------------+-----------------+-----------------+
| video_views     | All             | Yes - /28hrs &  | A count of how  |
|                 |                 | /Historical     | many times a    |
|                 |                 |                 | video in the    |
|                 |                 | No - /totals    | given Tweet has |
|                 |                 |                 | been 50%        |
|                 |                 |                 | visible for at  |
|                 |                 |                 | least two       |
|                 |                 |                 | seconds.        |
|                 |                 |                 |                 |
|                 |                 |                 | Video views are |
|                 |                 |                 | only available  |
|                 |                 |                 | for Tweets that |
|                 |                 |                 | are 1800 days   |
|                 |                 |                 | old or less. If |
|                 |                 |                 | you try to      |
|                 |                 |                 | request video   |
|                 |                 |                 | views for any   |
|                 |                 |                 | Tweets older    |
|                 |                 |                 | than 1800 days, |
|                 |                 |                 | you will        |
|                 |                 |                 | receive the     |
|                 |                 |                 | following       |
|                 |                 |                 | object within   |
|                 |                 |                 | your response,  |
|                 |                 |                 | along with a    |
|                 |                 |                 | separate object |
|                 |                 |                 | that contains   |
|                 |                 |                 | any other       |
|                 |                 |                 | metrics that    |
|                 |                 |                 | you requested:  |
|                 |                 |                 |                 |
|                 |                 |                 | [               |
|                 |                 |                 | \"unsupporte    |
|                 |                 |                 | d_for_video_vie |
|                 |                 |                 | ws_tweet_ids\": |
|                 |                 |                 | \               |
|                 |                 |                 | [\"TWEET_ID\"\] |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 |                 |
|                 |                 |                 | **Please        |
|                 |                 |                 | note:** You may |
|                 |                 |                 | see a           |
|                 |                 |                 | discrepancy     |
|                 |                 |                 | between the     |
|                 |                 |                 | video views     |
|                 |                 |                 | metric          |
|                 |                 |                 | displayed in    |
|                 |                 |                 | the Twitter     |
|                 |                 |                 | owned and       |
|                 |                 |                 | operated        |
|                 |                 |                 | platforms       |
|                 |                 |                 | (mobile app and |
|                 |                 |                 | website) and    |
|                 |                 |                 | the number that |
|                 |                 |                 | you receive via |
|                 |                 |                 | the /28hr and   |
|                 |                 |                 | /historical     |
|                 |                 |                 | endpoints. \    |
|                 |                 |                 |                 |
|                 |                 |                 | -   The video   |
|                 |                 |                 |     views       |
|                 |                 |                 |     displayed   |
|                 |                 |                 |     in the      |
|                 |                 |                 |     Twitter     |
|                 |                 |                 |     user        |
|                 |                 |                 |     interface   |
|                 |                 |                 |     and with    |
|                 |                 |                 |     the /totals |
|                 |                 |                 |     endpoint    |
|                 |                 |                 |     will        |
|                 |                 |                 |     display the |
|                 |                 |                 |     video view  |
|                 |                 |                 |     aggregated  |
|                 |                 |                 |     across all  |
|                 |                 |                 |     Tweets in   |
|                 |                 |                 |     which the   |
|                 |                 |                 |     given video |
|                 |                 |                 |     has been    |
|                 |                 |                 |     posted.     |
|                 |                 |                 |     That means  |
|                 |                 |                 |     that the    |
|                 |                 |                 |     metric      |
|                 |                 |                 |     displayed   |
|                 |                 |                 |     in the UI   |
|                 |                 |                 |     includes    |
|                 |                 |                 |     the         |
|                 |                 |                 |     combined    |
|                 |                 |                 |     views from  |
|                 |                 |                 |     any         |
|                 |                 |                 |     instance    |
|                 |                 |                 |     where the   |
|                 |                 |                 |     video has   |
|                 |                 |                 |     been        |
|                 |                 |                 |     Retweeted   |
|                 |                 |                 |     or reposted |
|                 |                 |                 |     in separate |
|                 |                 |                 |     Tweets.     |
|                 |                 |                 |     This metric |
|                 |                 |                 |     does not    |
|                 |                 |                 |     include     |
|                 |                 |                 |     video views |
|                 |                 |                 |     on gifs.    |
|                 |                 |                 | -   The video   |
|                 |                 |                 |     views       |
|                 |                 |                 |     provided by |
|                 |                 |                 |     the /28hr   |
|                 |                 |                 |     and         |
|                 |                 |                 |     /historical |
|                 |                 |                 |     endpoints   |
|                 |                 |                 |     will just   |
|                 |                 |                 |     include     |
|                 |                 |                 |     those views |
|                 |                 |                 |     generated   |
|                 |                 |                 |     by the      |
|                 |                 |                 |     specific    |
|                 |                 |                 |     Tweet for   |
|                 |                 |                 |     which you   |
|                 |                 |                 |     are pulling |
|                 |                 |                 |                 |
|                 |                 |                 |   metrics. This |
|                 |                 |                 |     metric does |
|                 |                 |                 |     not include |
|                 |                 |                 |     video views |
|                 |                 |                 |     on gifs.    |
+-----------------+-----------------+-----------------+-----------------+
| media_views     | /28hr           | Yes\            | A count of all  |
|                 | /historical     |                 | views (autoplay |
|                 |                 |                 | and click) of   |
|                 |                 |                 | your media      |
|                 |                 |                 | counted across  |
|                 |                 |                 | videos, gifs,   |
|                 |                 |                 | and images.\    |
+-----------------+-----------------+-----------------+-----------------+
| me              | /28hr           | Yes\            | A count of how  |
| dia_engagements | /historical     |                 | many times      |
|                 |                 |                 | media such as   |
| ( [formerly     |                 |                 | an image or     |
| Media           |                 |                 | video in the    |
| Clicks](        |                 |                 | Tweet has been  |
| /en/docs/metric |                 |                 | clicked.        |
| s/get-tweet-eng |                 |                 |                 |
| agement/guides/ |                 |                 |                 |
| understanding-r |                 |                 |                 |
| ecent-changes-t |                 |                 |                 |
| o-eapi-metrics) |                 |                 |                 |
| )               |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| url_clicks      | /28hr           | Yes             | A count of how  |
|                 | /historical     |                 | many times a    |
|                 |                 |                 | URL in the      |
|                 |                 |                 | Tweet has been  |
|                 |                 |                 | clicked.        |
+-----------------+-----------------+-----------------+-----------------+
| hashtag_clicks  | /28hr           | Yes\            | A count of how  |
|                 | /historical     |                 | many times a    |
|                 |                 |                 | hashtag in the  |
|                 |                 |                 | Tweet has been  |
|                 |                 |                 | clicked.        |
+-----------------+-----------------+-----------------+-----------------+
| detail_expands  | /28hr           | Yes\            | A count of how  |
|                 | /historical     |                 | many times the  |
|                 |                 |                 | Tweet has been  |
|                 |                 |                 | clicked to see  |
|                 |                 |                 | more details.   |
+-----------------+-----------------+-----------------+-----------------+
| p               | /28hr           | Yes\            | A count of how  |
| ermalink_clicks | /historical     |                 | many times the  |
|                 |                 |                 | permalink to    |
|                 |                 |                 | the Tweet (the  |
|                 |                 |                 | individual web  |
|                 |                 |                 | page dedicated  |
|                 |                 |                 | to this Tweet)  |
|                 |                 |                 | has been        |
|                 |                 |                 | clicked.        |
+-----------------+-----------------+-----------------+-----------------+
| app_i           | /28hr           | Yes\            | A count of how  |
| nstall_attempts | /historical     |                 | many times an   |
|                 |                 |                 | App Install     |
|                 |                 |                 | event has       |
|                 |                 |                 | occurred from   |
|                 |                 |                 | the Tweet       |
+-----------------+-----------------+-----------------+-----------------+
| app_opens       | /28hr           | Yes\            | A count of how  |
|                 | /historical     |                 | many times an   |
|                 |                 |                 | App Open event  |
|                 |                 |                 | has occurred    |
|                 |                 |                 | from the Tweet. |
+-----------------+-----------------+-----------------+-----------------+
| email_tweet     | /28hr           | Yes\            | A count of how  |
|                 | /historical     |                 | many times the  |
|                 |                 |                 | Tweet has been  |
|                 |                 |                 | shared via      |
|                 |                 |                 | email.          |
+-----------------+-----------------+-----------------+-----------------+
| user_follows    | /28hr           | Yes\            | A count of how  |
|                 | /historical     |                 | many times the  |
|                 |                 |                 | User (Tweet     |
|                 |                 |                 | author) has     |
|                 |                 |                 | been followed   |
|                 |                 |                 | from this       |
|                 |                 |                 | Tweet.          |
+-----------------+-----------------+-----------------+-----------------+
| user            | /28hr           | Yes\            | A count of how  |
| _profile_clicks | /historical     |                 | many times the  |
|                 |                 |                 | User (Tweet     |
|                 |                 |                 | author) has had |
|                 |                 |                 | their profile   |
|                 |                 |                 | clicked from    |
|                 |                 |                 | this Tweet.     |
+-----------------+-----------------+-----------------+-----------------+

### []{#EngagementGroupings} Engagement groupings

Groupings enable custom organization of the returned engagement metrics.
You can include a maximum of 3 groupings per request. You can choose to
group the metrics by one or more of the following values:

*All three endpoints support:*

*The ` /28hr ` and ` /historical ` can provide time-series metrics, and
thus support:*

-   engagement.day
-   engagement.hour

To learn more about grouping, please visit the [Engagement API
Grouping](/content/developer-twitter/en/docs/metrics/get-tweet-engagement/guides/grouping-results)
page within the Guides section.

## []{#NextSteps} Next steps

-   Check out our \' [Getting
    started](/content/developer-twitter/en/docs/metrics/get-tweet-engagement/guides/dev-getting-started-engagement-api)
    \' guide for the Engagement API.
-   Figure out [which Engagement API endpoint is right for
    you](/content/developer-twitter/en/docs/metrics/get-tweet-engagement/guides/selecting-engagement-endpoint)
    .
-   Learn more about some of the recent changes to the Engagement API
    [here](/content/developer-twitter/en/docs/metrics/get-tweet-engagement/guides/understanding-recent-changes-to-eapi-metrics)
    .
-   Check out our [API
    references](/content/developer-twitter/en/docs/metrics/get-tweet-engagement/api-reference/post-insights-engagement)
    to learn more about how to programmatically access Tweet engagement
    metrics.
-   [Key
    Characteristics](/en/docs/metrics/get-tweet-engagement/guides/key-characteristics.html) -
    serves as a one-page developer's checklist of API features and
    details.
-   Explore our sample code:\
    -   [Example Ruby
        client](https://github.com/twitterdev/engagement-api-client-ruby)
        . This example Engagement API Client helps manage the process of
        generating engagement metadata for large Tweet collections. The
        client has a helper feature that can surface [\'Top
        Tweets.\'](https://github.com/twitterdev/engagement-api-client-ruby#top-tweets)
        As engagement metrics are retrieved, on a Tweet-by-Tweet basis,
        this client maintains a list of \'Top Tweets\' with the highest
        levels of engagement. For example, if you are processing 100,000
        Tweets, it can compile the top 10 for Retweets or any other
        available metric. The  repository includes an extensive README,
        which serves as an additional source of 'getting started'
        material and orientation for how the API works.
    -   [Example Python
        client](https://github.com/twitterdev/Gnip-Insights-Interface) .
        This example illustrates using OAuth with the Requests package.
        The client also has an aggregating function for the /historical
        endpoint that combines API results over an arbitrary time period
        longer than 28 days.\

</div>
:::
:::
:::
:::
:::
:::
:::
:::
:::
:::
:::
