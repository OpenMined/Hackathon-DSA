::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
The purpose of this documentation is to provide developers an
introduction to integrating with the Engagement API. We'll start off by
discussing the 'whys' of integrating, then start digging into the
technical 'how' details.

#### What does the Engagement API provide?

-   The Engagement API provides impression and engagement data for any
    Twitter account's owned Tweets from the last 90 days, assuming that
    account has authorized your App to request metrics on their behalf
    using [3-legged
    OAuth](/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens)
    . This powerful, yet easy-to-implement solution gives immediate
    access to impressions and deep engagements such as URL clicks,
    #hashtag clicks, and many more.
-   The Engagement API provides total aggregate metrics for favorites,
    Retweets, Quote Tweets, replies, and video views views for any
    Tweet. This can be used as a powerful way to get basic engagement
    data about any Tweet or collection of Tweets.
-   The Engagement API delivers new value to social listening,
    marketing, and publishing platforms by allowing customers to measure
    ROI on Twitter by effectively measuring the performance of content
    using 15+ performance metrics.
-   The Engagement API is a request/response API that allows app
    developers to send requests with Tweet IDs, desired metrics, and a
    time frame, for which the API instantly returns data.\

#### Why integrate? Example use-cases

-   Understand the total reach of your content to see how many people
    view it. See how many people view videos, click on links, click on
    hashtags, or install my apps.
-   Generate both total and time-series engagement metrics.
-   Understand basic engagement metrics (favorites, Retweets, Quote
    Tweets, replies) about any public Tweet.
-   Use these metrics to determine what types of Tweets work so I can
    post them more often and get more impressions and more engagements
    for my content.
-   Automate marketing behavior (such as Retweeting content from a
    different owned account) every time one of my Tweets reaches 100
    Likes, or another threshold.
-   Benchmark and compare my campaigns against each other as a tool for
    A/B testing.
-   Analyze what type of content resonates for my customer service
    department to determine how and when to respond.
-   Show analytics for content that is published from my platform.\

The [Engagement API was launched in
2016](https://blog.twitter.com/official/en_us/a/2016/gnip-s-engagement-api-is-now-generally-available.html)
and was the first Twitter API to provide these in-depth engagement
metrics at scale. The Engagement API is easy to use and enables
customers to automate the process. Here is a case study describing an
example integration:

-   [Measuring campaign success with the Red
    Cross](https://blog.twitter.com/developer/en_us/topics/spotlight/2016/measuring-campaign-success-with-the-red-cross.html)
    [](https://simplymeasured.com/blog/true-twitter-impressions-and-url-clicks-new-from-simply-measured/#sm.0007werel134td8zqf02m2mduumr6)

Now that we've explored the 'whys' of the Engagement API, let's start
digging into the technical details.

### Integrating the Engagement API

#### Introduction to API

The Engagement API is a simple RESTful API that receives requests
encoded in JSON and responds with engagement metrics encoded in JSON.
Requests consist three main parts (follow links for more documentation):

-   Array of ***Tweet IDs*** .
-   Array specifying the [metric
    types](/en/docs/metrics/get-tweet-engagement/overview.html#EngagementTypes)
    of interest. Types include things such as 'impressions', 'retweets',
    'hashtag_clicks', and 'user_follows'.
-   [Engagement
    groupings](/content/developer-twitter/en/docs/metrics/get-tweet-engagement/guides/grouping-results)
    , which is a JSON structure indicating how you want the engagement
    data arranged in the API response.

\
In many situations, the Engagement Types and Groupings will remains
relatively constant from request to request, with only the Tweet IDs
being updated.

The Engagement API provides [three
endpoints](/en/docs/metrics/get-tweet-engagement/overview.html#RequestEndpoints)
:

-   **Totals** - Provides grand totals of engagements for Tweets. Some
    metrics are available for all Tweets, while others are only
    available for the past 90 days.
-   **28 hour** - Provides time-series engagement metrics from the last
    28 hours.
-   **Historical** - Provides time-series engagement metrics for up to
    four consecutive weeks for Tweets posted since September 1, 2014.

\
The **/totals** endpoint supports requesting metrics for up to **250
Tweets per request** . The **/28hour** and **/historical** endpoints
support **25 per request** .

After discussing getting access to the Engagement API, we'll walk
through making an API request, provide an OAuth overview, and provide
links to other technical resources.

#### Getting API access

If you are reading this document, you have most likely already obtained
access to the Engagement API. If not, please reach out to your
Enterprise account manager, or apply for Enterprise access
[here](/content/developer-twitter/en/enterprise-application) .

The first step is creating a [Twitter
app](/content/developer-twitter/en/docs/basics/developer-portal/guides/apps)
using an approved developer account via the [developer
portal](/content/developer-twitter/en/docs/basics/developer-portal/overview)
.  Your account manager will need the numeric App ID associated with
this application to provide access. If you need to apply for a developer
account, you can do so [here](/content/developer-twitter/en/apply) .

#### Making a request

The good news is that making requests to the Engagement API is simple.
For our request, we'll ask it for total Retweets, Quote Tweets,
Favorites, and replies, for the following two
[\@TwitterDev](https://twitter.com/TwitterDev) Tweets:
:::
:::

::: c01-rich-text-editor
::: is-table-default
The first step is constructing the API request in JSON, consisting of
these two Tweet IDs placed in an array, an array of engagement types of
interest, and a custom-named "groupings" JSON object that indicates how
we want the metrics arranged in the response. Here is what our request
looks like:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {
  "tweet_ids": [
    1260294888811347969, 850006245121695744
  ],
  "engagement_types": [
    "retweets", "quote_tweets", "favorites", "replies"
  ],
  "groupings": {
    "engagement-types-by-id": {
      "group_by": [
        "Tweet.id", "engagement.type"
      ]
    }
  }
}
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
To retrieve these total metrics, we POST this JSON request to the [
https://data-api.twitter.com/insights/engagement/totals ]{.code-inline}
endpoint.

We'll include the following headers to indicate that our request is
encoded in JSON, and that it is Gzipped (request bodies can get big):

-   Content-Type: application/json
-   Accept-Encoding: gzip

When making requests we authenticate using OAuth, which we'll discuss
more in the next section.

The API returns the following payload:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` line-numbers
 {
  "grouping name": {
    "1260294888811347969": {
      "favorites": "17111",
      "quote_tweets": "3254",
      "replies": "1828",
      "retweets": "5218"
    },
    "850006245121695744": {
      "favorites": "492",
      "quote_tweets": "66",
      "replies": "42",
      "retweets": "324"
    }
  }
}
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
\
Note that the response has our requested metrics in the structure
described by the "groupings" definitions, with metrics listed by Tweet
ID first, then by engagement type on the next level.

That was pretty simple. If you are new to authenticating with OAuth,
check out the next section.

### Authenticating with OAuth

OAuth is an authentication standard that is very common in the
technology industry.  If you are already using OAuth (perhaps with other
Twitter APIs) then you are likely using a language-specific OAuth
package that abstracts away all the gnarly details. If you are new to
OAuth, please visit our [Oauth with the Twitter
API](/en/docs/basics/authentication/overview/oauth.html) page or head
directly to the [https://oauth.net](https://oauth.net/) to learn more.
Then we recommend that you find an OAuth package for your integration
language of choice and start there. With these packages, the path to
authenticating typically means configuring your keys and tokens,
creating some sort of HTTP object, then making requests with that
object.\

For example, in the Ruby world, the following pseudo-code represents a
recipe to build an OAuth-enabled app using the Ruby gem 'oauth' and
making a POST request:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: {.t05-inline-code-snippet .t05-inline-code-snippet--full-height}
``` line-numbers
 require 'oauth'

#Assemble JSON request (as above).
request = make_json_request() 

#Build an app consumer object with my app consumer key and secret.
consumer = OAuth::Consumer.new(keys['consumer_key'], keys['consumer_secret'], {:site => ‘https://data-api.twitter.com’})
#Build a user token with tokens provided by account providing permission. If making app-only #request (checking Tweets that do not require permission with /totals endpoint), this step can be #skipped. 
token = {:oauth_token => keys['access_token'], :oauth_token_secret => keys['access_token_secret']}

#Create oauth-enabled app object. 
app = OAuth::AccessToken.from_hash(consumer, token)
#Make POST request.
result = app.post(“/insights/engagement/totals", request, {"content-type" => "application/json", "Accept-Encoding" => "gzip"})

    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
The Engagement API supports both application-only and user-context
authentication. If you are collecting engagement metrics for unowned
public Tweets with the /totals endpoint then no user permission is
required and you can use application-only authentication. In this case,
you'll use only your app key and secret to authenticate.

OAuth also allows an app to make an API request "on behalf of another
user", using tokens that relate to the user. If you are generating
Engagement metrics for owned Tweets, ie Tweets that were published by a
user whom you have user tokens for, you will be making requests with a
user context, meaning authenticating with both your app keys and
user-specific access tokens. These user access tokens are typically
supplied with the \' [Sign-in with
Twitter](/content/developer-twitter/en/docs/twitter-for-websites/log-in-with-twitter/login-in-with-twitter)
\' process or acquired directly from the user (please note that you must
use [twurl](/content/developer-twitter/en/docs/tutorials/using-twurl) if
you acquire the tokens directly from the user). Once the user provides
their tokens, they do not expire and can be used with the Engagement API
to make requests on their behalf,  as long as the user doesn\'t reset
their tokens or change their password, in which case they will have to
provide you the new tokens.

You can review which metrics require which authentication via [this
table](/content/developer-twitter/en/docs/metrics/get-tweet-engagement/overview#EngagementTypes)
.\

## Next steps

-   Read through the [Engagement API\'s Overview
    page](/en/docs/metrics/get-tweet-engagement/overview) for general
    information about the product.
-   Figure out [which Engagement API endpoint is right for
    you](/content/developer-twitter/en/docs/metrics/get-tweet-engagement/guides/selecting-engagement-endpoint)
    .\
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
-   Explore our sample code:
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
        available metric. Project repository includes an extensive
        README, which serves as an additional source of 'getting
        started' material and orientation for how the API works.
    -   [Example Python
        client](https://github.com/jeffakolb/Gnip-Insights-Interface) .
        This example illustrating using OAuth with the Requests package.
        The client also has an aggregating function for the /historical
        endpoint that combines API results over an arbitrary time period
        longer than 28 days.
:::
:::
:::
