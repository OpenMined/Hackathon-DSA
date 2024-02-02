::: is-table-default
Groupings enable custom organization of the returned engagement metrics.
You can include a maximum of 3 groupings per request. You can choose to
group the metrics by one or more of the following values:

*All three endpoints support:*

*The ` /28hr ` and ` /historical ` can provide time-series metrics, and
thus support:*

-   engagement.day
-   engagement.hour

Groupings are honored serially, so that you can change the desired
result format by changing the order of your ` group_by ` values.
Groupings that contain four ` group_by ` values will only be supported
in one of the following two formats:\

    "group_by": [
        "tweet.id",
        "engagement.type",
        "engagement.day",
        "engagement.hour"
      ]

\
OR

    "group_by": [
        "engagement.type",
        "tweet.id",
        "engagement.day",
        "engagement.hour"
    ]

\
For example, if you want to generate grand totals of metric types,
include the following "groupings" specification as part of your request
(and see the [API
Reference](/en/docs/metrics/get-tweet-engagement/api-reference/post-insights-engagement.html)
page for more information on assembling requests):\

    {
      "engagement_types": [
        "favorites",
        "replies",
        "retweets"
      ],
      "groupings": {
        "Grand Totals": {
          "group_by": [
            "engagement.type"
          ]
        }
      }
    }

\
With this grouping, the Engagement API's JSON response will include a
root-level ` "Grand Totals" ` attribute which contains grand totals by
metrics type:\

    {
      "Grand Totals": {
        "favorites": "12",
        "replies": "2",
        "retweets": "2"
      }
    }

To generate a 4-hour time-series of metrics for a single Tweet grouped
by Tweet IDs, the following Grouping specification would be part of the
request:

    {
      "start": "2016-02-10T17:00:00Z",
      "end": "2016-02-10T21:00:00Z",
      "tweet_ids": [
        "697506383516729344"
      ],
      "engagement_types": [
        "impressions",
        "engagements"
      ],
      "groupings": {
        "Tweets_MetricType_TimeSeries": {
          "group_by": [
            "tweet.id",
            "engagement.type",
            "engagement.hour"
          ]
        }
      }
    }

\
With this grouping, the Engagement API's JSON response will include a
root-level ` "Tweets_MetricType_TimeSeries" ` attribute which contains
the metrics broken down by Tweet ID, then metric type, and the
corresponding hourly time-series:\

    {
      "Tweets_MetricType_TimeSeries": {
        "697506383516729344": {
          "impressions": {
            "2016-02-10": {
              "17": "551",
              "18": "412",
              "19": "371",
              "20": "280"
            }
          },
          "engagements": {
            "2016-02-10": {
              "17": "8",
              "18": "6",
              "19": "3",
              "20": "0"
            }
          }
        }
      }
    }

## Next steps

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
    to learn more about how to programatically access Tweet engagement
    metrics.
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
