::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
The Engagement API delivers invaluable impression and engagement metrics
that enable you to monitor the performance of your activity on Twitter.
In our continual effort to enable marketing decisions based on our data,
we are excited to share recent changes to the Engagement API that
provide greater consistency with metrics across all of Twitter.

We recently deployed changes to modernize the Engagement API to use the
same metrics aggregation methodology in use by the Twitter analytics
dashboard (analytics.twitter.com). We took a thoughtful approach to try
and minimize breaking API changes when rolling out these new metrics and
deployed the first set of changes on October 9, 2017. These changes
improve consistency from all of the places you or your customers might
monitor your performance on Twitter. Please see the detailed outline of
the changes below:

+-----------------------------------+-----------------------------------+
| **Metric**                        | **Change**                        |
+-----------------------------------+-----------------------------------+
| engagements                       | We've updated the metrics that    |
|                                   | roll into overall engagements to  |
|                                   | match consistency with the Tweet  |
|                                   | analytics dashboard. Engagements  |
|                                   | measures "times people interacted |
|                                   | with this Tweet".                 |
|                                   |                                   |
|                                   | For Tweets that include media     |
|                                   | like a video or a GIF, the        |
|                                   | engagements metric will no longer |
|                                   | include media views. Media views  |
|                                   | can now be accessed in a new      |
|                                   | metric, *media_views* .           |
+-----------------------------------+-----------------------------------+
| media_clicks\*                    | This metric has been replaced by  |
|                                   | a new metric called "             |
|                                   | *media_engagements* ".            |
+-----------------------------------+-----------------------------------+
| video_views                       | As of July 6th, 2018, this metric |
|                                   | is now available for \'unowned\'  |
|                                   | Tweets via the                    |
|                                   | [/totals](/content/de             |
|                                   | veloper-twitter/en/docs/metrics/g |
|                                   | et-tweet-engagement/api-reference |
|                                   | /post-insights-engagement#Totals) |
|                                   | endpoint. This means that you can |
|                                   | access the video views for        |
|                                   | **all** Tweets by using app-only  |
|                                   | authentication.                   |
|                                   |                                   |
|                                   | You can only request video views  |
|                                   | that are younger than 1800 days   |
|                                   | old. If you try to request video  |
|                                   | views for a Tweet older than 1800 |
|                                   | days, you will receive the        |
|                                   | following:                        |
|                                   |                                   |
|                                   | [                                 |
|                                   | \"unsuppo                         |
|                                   | rted_for_video_views_tweet_ids\": |
|                                   | \[\"TWEET_ID\"\] ]{.code-inline}  |
|                                   |                                   |
|                                   | **Please note** that it will      |
|                                   | differ from media_views in that   |
|                                   | video_views relies on the MRC     |
|                                   | standard of 50% of the video in   |
|                                   | view for at least two seconds. \  |
|                                   |                                   |
|                                   | **Also,** note that you may see a |
|                                   | discrepancy between the video     |
|                                   | views metric displayed in the     |
|                                   | Twitter owned and operated        |
|                                   | platforms (mobile app and         |
|                                   | website) and the number that you  |
|                                   | receive via the /28hr and         |
|                                   | /historical endpoints.            |
|                                   |                                   |
|                                   | -   The video views displayed in  |
|                                   |     the Twitter user interface    |
|                                   |     and that delivers using the   |
|                                   |     /totals endpoint will display |
|                                   |     the video view aggregated     |
|                                   |     across all Tweets in which    |
|                                   |     the given video has been      |
|                                   |     posted. That means that the   |
|                                   |     metric displayed in the UI    |
|                                   |     includes the combined views   |
|                                   |     from any instance where the   |
|                                   |     video has been Retweeted or   |
|                                   |     reposted in separate Tweets.  |
|                                   | -   The video views provided by   |
|                                   |     the /28hr and /historical     |
|                                   |     endpoints will just include   |
|                                   |     those views generated by the  |
|                                   |     specific Tweet for which you  |
|                                   |     are pulling metrics.          |
+-----------------------------------+-----------------------------------+
| media_views                       | This includes all views (autoplay |
|                                   | and click) of your media counted  |
|                                   | across videos, vines, gifs, and   |
|                                   | images.                           |
|                                   |                                   |
|                                   | **Please note** that Tweets with  |
|                                   | images do not show a media_views  |
|                                   | metric in the analytics dashboard |
|                                   | but will be returned in the       |
|                                   | Engagement API.                   |
+-----------------------------------+-----------------------------------+
| media_engagements\*               | This includes the number of       |
|                                   | clicks on your media across       |
|                                   | videos, vines, gifs, and images.  |
|                                   | This metric is replacing          |
|                                   | *media_clicks* .                  |
+-----------------------------------+-----------------------------------+
| quote_tweets                      | As of July 7th, 2020, this metric |
|                                   | is now available for \'unowned\'  |
|                                   | Tweets via the /totals endpoint.  |
|                                   | This means that you can access    |
|                                   | the Quote Tweet count for all     |
|                                   | Tweets by using app-only          |
|                                   | authentication.                   |
+-----------------------------------+-----------------------------------+

## 

## Next steps

-   Read through the [Engagement API\'s Overview
    page](/content/developer-twitter/en/docs/metrics/get-tweet-engagement/overview)
    for general information about the product.
-   Check out our \' [Getting
    started](/content/developer-twitter/en/docs/metrics/get-tweet-engagement/guides/dev-getting-started-engagement-api)
    \' guide for the Engagement API.
-   Check out our [API
    references](/content/developer-twitter/en/docs/metrics/get-tweet-engagement/api-reference/post-insights-engagement)
    to learn more about how to programmatically access Tweet engagement
    metrics.\
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
        longer than 28 days.
:::
:::
:::
:::
:::
:::
:::
:::
