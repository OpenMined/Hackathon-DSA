Overview

Overview
--------

[Enterprise](https://developer.twitter.com/en/products/twitter-api/enterprise)

_This is an enterprise API available within our managed access levels only. To use this API, you must first set up an account with our enterprise sales team. [Learn more](https://developer.twitter.com/en/docs/twitter-api/enterprise)_  

The Engagement API provides access to Tweet impression and engagement metrics. While most metrics and endpoints require you to authenticate using [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a), you can access public Favorite, Retweet, Reply, and Video Views metrics using [OAuth 2.0 Bearer Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0) and the /totals endpoint.  

**Note:** You may observe differences between reported data on some of the Twitter web dashboards, and the data reported in the Engagement API. These differences occur because the web dashboards typically only show engagements and/or impressions that occurred within the selected time range. For example, a web dashboard may show engagement on Tweets within the span of a calendar month, while the Engagement API may show engagements that fall beyond the span of that month, but within the time range requested. The Engagement API should be seen as the valid source, in these cases.  
 

### Request endpoints

The Engagement API has three endpoints:

#### Current Totals: [/totals](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/api-reference/post-insights-engagement#Totals)

* Requests return a total metric for impressions and a total metric for engagements for the desired Tweets
* Limited to the following metrics: Impressions, Engagements, Favorites, Replies, Retweets, Quote Tweets, and Video Views
* Supports the ability to retrieve **Impressions** and **Engagements** metrics for Tweets created **within the last 90 days** using OAuth 1.0a User Context
* Supports the ability to retrieve **Favorites, Retweets, Quote Tweets, Replies,** and **Video Views** metrics for **any Tweet** using OAuth 2.0 Bearer token
* The results are based on the current total of impressions and engagements at the time the request is made
* Ideal for powering a dashboard report and for calculating engagement rates across a variety of @handles
* Supports requesting metrics for up to 250 Tweets per request  
     

#### Last 28 hours: [/28hr](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/api-reference/post-insights-engagement#28hr)

* Requests can return a total metric for impressions, a total metric for engagements, and breakdown of individual engagement metrics that have occurred in the last 28 hours
* Data can be grouped by Tweet ID, and in time-series in aggregate, by day, or by hour
* Ideal for tracking the performance of recently created content
* Supports all available metrics
* Supports requesting metrics for up to 25 Tweets per request  
     

#### Historical: [/historical](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/api-reference/post-insights-engagement#Historical)

* Requests can return impressions, engagements, and a breakdown of individual engagement metrics for the most recent one year, based on the engagement time (not the Tweet creation time).
* Requests support a start date and end date parameter, providing flexibility to narrow into a specific time frame up to 4 weeks in duration.
* Tweet engagement data is limited to only 365 days in the past.
* Data can be grouped by Tweet ID, and in time-series in aggregate, by day, or by hour.
* Ideal for evaluating recent performance against a historical benchmark or developing a historical picture of an @handle’s performance.
* Supports all available metrics.
* Supports requesting metrics for up to 25 Tweets per request.  
      
      
    

### Available metrics

The table below describes the types of metrics that can be accessed through the Engagement API.

Please check out our [Interpreting the metrics page](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/guides/interpreting-metrics) to learn more about the below metrics.

| Metric | Endpoint Availability | User Context Required | Description |
| --- | --- | --- | --- |
| impressions | All | Yes | A count of how many times the Tweet has been viewed. This metric is only available for Tweets that have been posted within the past 90 days. |
| engagements | All | Yes | A count of the number of times a user has interacted with the Tweet. This metric is only available for Tweets that have been posted within the past 90 days. |
| favorites | All | Yes - /28hrs & /Historical<br><br>No - /totals | A count of how many times the Tweet has been favorited. |
| retweets | All | Yes - /28hrs & /Historical<br><br>No - /totals | A count of how many times the Tweet has been Retweeted. |
| quote\_tweets | /totals | No - /totals | A count of times a Tweet has been Retweeted with a comment (also known as Quote). |
| replies | All | Yes - /28hrs & /Historical<br><br>No - /totals | A count of how many times the Tweet has been replied to. |
| video\_views | All | Yes - /28hrs & /Historical<br><br>No - /totals | A count of how many times a video in the given Tweet has been 50% visible for at least two seconds.<br><br>Video views are only available for Tweets that are 1800 days old or less. If you try to request video views for any Tweets older than 1800 days, you will receive the following object within your response, along with a separate object that contains any other metrics that you requested:<br><br>"unsupported\_for\_video\_views\_tweet\_ids": \["TWEET\_ID"\]<br><br>**Please note:** You may see a discrepancy between the video views metric displayed in the Twitter owned and operated platforms (mobile app and website) and the number that you receive via the /28hr and /historical endpoints.  <br><br>* The video views displayed in the Twitter user interface and with the /totals endpoint will display the video view aggregated across all Tweets in which the given video has been posted. That means that the metric displayed in the UI includes the combined views from any instance where the video has been Retweeted or reposted in separate Tweets. This metric does not include video views on gifs.<br>* The video views provided by the /28hr and /historical endpoints will just include those views generated by the specific Tweet for which you are pulling metrics. This metric does not include video views on gifs. |
| media\_views | /28hr /historical | Yes | A count of all views (autoplay and click) of your media counted across videos, gifs, and images. |
| media\_engagements<br><br>([formerly Media Clicks](https://developer.twitter.com/en/docs/metrics/get-tweet-engagement/guides/understanding-recent-changes-to-eapi-metrics)) | /28hr /historical | Yes | A count of how many times media such as an image or video in the Tweet has been clicked. |
| url\_clicks | /28hr /historical | Yes | A count of how many times a URL in the Tweet has been clicked. |
| hashtag\_clicks | /28hr /historical | Yes | A count of how many times a hashtag in the Tweet has been clicked. |
| detail\_expands | /28hr /historical | Yes | A count of how many times the Tweet has been clicked to see more details. |
| permalink\_clicks | /28hr /historical | Yes | A count of how many times the permalink to the Tweet (the individual web page dedicated to this Tweet) has been clicked. |
| app\_install\_attempts | /28hr /historical | Yes | A count of how many times an App Install event has occurred from the Tweet |
| app\_opens | /28hr /historical | Yes | A count of how many times an App Open event has occurred from the Tweet. |
| email\_tweet | /28hr /historical | Yes | A count of how many times the Tweet has been shared via email. |
| user\_follows | /28hr /historical | Yes | A count of how many times the User (Tweet author) has been followed from this Tweet. |
| user\_profile\_clicks | /28hr /historical | Yes | A count of how many times the User (Tweet author) has had their profile clicked from this Tweet. |

### Engagement groupings

Groupings enable custom organization of the returned engagement metrics. You can include a maximum of 3 groupings per request. You can choose to group the metrics by one or more of the following values:

_All three endpoints support:_

* tweet.id
* engagement.type  
     

_The `/28hr` and `/historical` can provide time-series metrics, and thus support:_

* engagement.day
* engagement.hour  
      
    

To learn more about grouping, please visit the [Engagement API Grouping](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/guides/grouping-results) page within the Guides section.  
  

Next steps
----------

* Check out our '[Getting started](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/guides/dev-getting-started-engagement-api)' guide for the Engagement API.
* Figure out [which Engagement API endpoint is right for you](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/guides/selecting-engagement-endpoint).
* Learn more about some of the recent changes to the Engagement API [here](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/guides/understanding-recent-changes-to-eapi-metrics).
* Check out our [API references](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/api-reference/post-insights-engagement) to learn more about how to programmatically access Tweet engagement metrics.
* [Key Characteristics](https://developer.twitter.com/en/docs/metrics/get-tweet-engagement/guides/key-characteristics.html) - serves as a one-page developer’s checklist of API features and details.  
      
    
* Explore our sample code:  
    * [Example Ruby client](https://github.com/twitterdev/engagement-api-client-ruby). This example Engagement API Client helps manage the process of generating engagement metadata for large Tweet collections. The client has a helper feature that can surface ['Top Tweets.'](https://github.com/twitterdev/engagement-api-client-ruby#top-tweets) As engagement metrics are retrieved, on a Tweet-by-Tweet basis, this client maintains a list of 'Top Tweets' with the highest levels of engagement. For example, if you are processing 100,000 Tweets, it can compile the top 10 for Retweets or any other available metric. The  repository includes an extensive README, which serves as an additional source of ‘getting started’ material and orientation for how the API works.
    * [Example Python client](https://github.com/twitterdev/Gnip-Insights-Interface). This example illustrates using OAuth with the Requests package. The client also has an aggregating function for the /historical endpoint that combines API results over an arbitrary time period longer than 28 days.

A developer’s ‘getting started’ guide

Developer getting started guide
-------------------------------

### Introduction

The purpose of this documentation is to provide developers an introduction to integrating with the Engagement API. We’ll start off by discussing the ‘whys’ of integrating, then start digging into the technical ‘how’ details.

#### What does the Engagement API provide?

* The Engagement API provides impression and engagement data for any Twitter account’s owned Tweets from the last 90 days, assuming that account has authorized your App to request metrics on their behalf using [3-legged OAuth](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens). This powerful, yet easy-to-implement solution gives immediate access to impressions and deep engagements such as URL clicks, #hashtag clicks, and many more.
* The Engagement API provides total aggregate metrics for favorites, Retweets, Quote Tweets, replies, and video views views for any Tweet. This can be used as a powerful way to get basic engagement data about any Tweet or collection of Tweets.
* The Engagement API delivers new value to social listening, marketing, and publishing platforms by allowing customers to measure ROI on Twitter by effectively measuring the performance of content using 15+ performance metrics.
* The Engagement API is a request/response API that allows app developers to send requests with Tweet IDs, desired metrics, and a time frame, for which the API instantly returns data.  
     

#### Why integrate? Example use-cases

* Understand the total reach of your content to see how many people view it. See how many people view videos, click on links, click on hashtags, or install my apps.
* Generate both total and time-series engagement metrics.
* Understand basic engagement metrics (favorites, Retweets, Quote Tweets, replies) about any public Tweet.
* Use these metrics to determine what types of Tweets work so I can post them more often and get more impressions and more engagements for my content.
* Automate marketing behavior (such as Retweeting content from a different owned account) every time one of my Tweets reaches 100 Likes, or another threshold.
* Benchmark and compare my campaigns against each other as a tool for A/B testing.
* Analyze what type of content resonates for my customer service department to determine how and when to respond.
* Show analytics for content that is published from my platform.  
     

The [Engagement API was launched in 2016](https://blog.twitter.com/official/en_us/a/2016/gnip-s-engagement-api-is-now-generally-available.html) and was the first Twitter API to provide these in-depth engagement metrics at scale. The Engagement API is easy to use and enables customers to automate the process. Here is a case study describing an example integration:

* [Measuring campaign success with the Red Cross](https://blog.twitter.com/developer/en_us/topics/spotlight/2016/measuring-campaign-success-with-the-red-cross.html)[](https://simplymeasured.com/blog/true-twitter-impressions-and-url-clicks-new-from-simply-measured/#sm.0007werel134td8zqf02m2mduumr6)

Now that we’ve explored the ‘whys’ of the Engagement API, let’s start digging into the technical details.  
  

### Integrating the Engagement API

#### Introduction to API

The Engagement API is a simple RESTful API that receives requests encoded in JSON and responds with engagement metrics encoded in JSON. Requests consist three main parts (follow links for more documentation):

* Array of **_Tweet IDs_**.
* Array specifying the [metric types](https://developer.twitter.com/en/docs/metrics/get-tweet-engagement/overview.html#EngagementTypes) of interest. Types include things such as ‘impressions’, ‘retweets’, ‘hashtag\_clicks’, and ‘user\_follows’.
* [Engagement groupings](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/guides/grouping-results), which is a JSON structure indicating how you want the engagement data arranged in the API response.

  
In many situations, the Engagement Types and Groupings will remains relatively constant from request to request, with only the Tweet IDs being updated.

The Engagement API provides [three endpoints](https://developer.twitter.com/en/docs/metrics/get-tweet-engagement/overview.html#RequestEndpoints):

* **Totals** - Provides grand totals of engagements for Tweets. Some metrics are available for all Tweets, while others are only available for the past 90 days.
* **28 hour** - Provides time-series engagement metrics from the last 28 hours.
* **Historical** - Provides time-series engagement metrics for up to four consecutive weeks for Tweets posted since September 1, 2014.

  
The **/totals** endpoint supports requesting metrics for up to **250 Tweets per request**. The **/28hour** and **/historical** endpoints support **25 per request**.

After discussing getting access to the Engagement API, we’ll walk through making an API request, provide an OAuth overview, and provide links to other technical resources.

#### Getting API access

If you are reading this document, you have most likely already obtained access to the Engagement API. If not, please reach out to your Enterprise account manager, or apply for Enterprise access [here](https://developer.twitter.com/content/developer-twitter/en/enterprise-application).

The first step is creating a [Twitter app](https://developer.twitter.com/content/developer-twitter/en/docs/basics/developer-portal/guides/apps) using an approved developer account via the [developer portal](https://developer.twitter.com/content/developer-twitter/en/docs/basics/developer-portal/overview).  Your account manager will need the numeric App ID associated with this application to provide access. If you need to apply for a developer account, you can do so [here](https://developer.twitter.com/content/developer-twitter/en/apply).

#### Making a request

The good news is that making requests to the Engagement API is simple. For our request, we’ll ask it for total Retweets, Quote Tweets, Favorites, and replies, for the following two [@TwitterDev](https://twitter.com/TwitterDev) Tweets:

> 1/ Today we’re sharing our vision for the future of the Twitter API platform![https://t.co/XweGngmxlP](https://t.co/XweGngmxlP)
> 
> — Twitter Dev (@TwitterDev) [April 6, 2017](https://twitter.com/TwitterDev/status/850006245121695744)

> Don’t miss the Tweets about your Tweet.  
>   
> Now on iOS, you can see Retweets with comments all in one place. [pic.twitter.com/oanjZfzC6y](https://t.co/oanjZfzC6y)
> 
> — Twitter (@Twitter) [May 12, 2020](https://twitter.com/Twitter/status/1260294888811347969?ref_src=twsrc%5Etfw)

The first step is constructing the API request in JSON, consisting of these two Tweet IDs placed in an array, an array of engagement types of interest, and a custom-named “groupings” JSON object that indicates how we want the metrics arranged in the response. Here is what our request looks like:  

      `{   "tweet_ids": [     1260294888811347969, 850006245121695744   ],   "engagement_types": [     "retweets", "quote_tweets", "favorites", "replies"   ],   "groupings": {     "engagement-types-by-id": {       "group_by": [         "Tweet.id", "engagement.type"       ]     }   } }`
    

To retrieve these total metrics, we POST this JSON request to the https://data-api.twitter.com/insights/engagement/totals endpoint.

We’ll include the following headers to indicate that our request is encoded in JSON, and that it is Gzipped (request bodies can get big):

* Content-Type: application/json
* Accept-Encoding: gzip  
     

When making requests we authenticate using OAuth, which we’ll discuss more in the next section.

The API returns the following payload:

      `{   "grouping name": {     "1260294888811347969": {       "favorites": "17111",       "quote_tweets": "3254",       "replies": "1828",       "retweets": "5218"     },     "850006245121695744": {       "favorites": "492",       "quote_tweets": "66",       "replies": "42",       "retweets": "324"     }   } }`
    

  
Note that the response has our requested metrics in the structure described by the “groupings” definitions, with metrics listed by Tweet ID first, then by engagement type on the next level.

That was pretty simple. If you are new to authenticating with OAuth, check out the next section.  
  

### Authenticating with OAuth

OAuth is an authentication standard that is very common in the technology industry.  If you are already using OAuth (perhaps with other Twitter APIs) then you are likely using a language-specific OAuth package that abstracts away all the gnarly details. If you are new to OAuth, please visit our [Oauth with the Twitter API](https://developer.twitter.com/en/docs/basics/authentication/overview/oauth.html) page or head directly to the [https://oauth.net](https://oauth.net/) to learn more. Then we recommend that you find an OAuth package for your integration language of choice and start there. With these packages, the path to authenticating typically means configuring your keys and tokens, creating some sort of HTTP object, then making requests with that object.  

For example, in the Ruby world, the following pseudo-code represents a recipe to build an OAuth-enabled app using the Ruby gem ‘oauth’ and making a POST request:  

      `require 'oauth'  #Assemble JSON request (as above). request = make_json_request()   #Build an app consumer object with my app consumer key and secret. consumer = OAuth::Consumer.new(keys['consumer_key'], keys['consumer_secret'], {:site => ‘https://data-api.twitter.com’}) #Build a user token with tokens provided by account providing permission. If making app-only #request (checking Tweets that do not require permission with /totals endpoint), this step can be #skipped.  token = {:oauth_token => keys['access_token'], :oauth_token_secret => keys['access_token_secret']}  #Create oauth-enabled app object.  app = OAuth::AccessToken.from_hash(consumer, token) #Make POST request. result = app.post(“/insights/engagement/totals", request, {"content-type" => "application/json", "Accept-Encoding" => "gzip"})`
    

The Engagement API supports both application-only and user-context authentication. If you are collecting engagement metrics for unowned public Tweets with the /totals endpoint then no user permission is required and you can use application-only authentication. In this case, you’ll use only your app key and secret to authenticate.

OAuth also allows an app to make an API request “on behalf of another user”, using tokens that relate to the user. If you are generating Engagement metrics for owned Tweets, ie Tweets that were published by a user whom you have user tokens for, you will be making requests with a user context, meaning authenticating with both your app keys and user-specific access tokens. These user access tokens are typically supplied with the '[Sign-in with Twitter](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-for-websites/log-in-with-twitter/login-in-with-twitter)' process or acquired directly from the user (please note that you must use [twurl](https://developer.twitter.com/content/developer-twitter/en/docs/tutorials/using-twurl) if you acquire the tokens directly from the user). Once the user provides their tokens, they do not expire and can be used with the Engagement API to make requests on their behalf,  as long as the user doesn't reset their tokens or change their password, in which case they will have to provide you the new tokens.

You can review which metrics require which authentication via [this table](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/overview#EngagementTypes).  
 

Next steps
----------

* Read through the [Engagement API's Overview page](https://developer.twitter.com/en/docs/metrics/get-tweet-engagement/overview) for general information about the product.
* Figure out [which Engagement API endpoint is right for you](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/guides/selecting-engagement-endpoint).  
    
* Learn more about some of the recent changes to the Engagement API [here](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/guides/understanding-recent-changes-to-eapi-metrics).
* Check out our [API references](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/api-reference/post-insights-engagement) to learn more about how to programmatically access Tweet engagement metrics.
* [Key Characteristics](https://developer.twitter.com/en/docs/metrics/get-tweet-engagement/guides/key-characteristics.html) - serves as a one-page developer’s checklist of API features and details.  
      
    
* Explore our sample code:
    * [Example Ruby client](https://github.com/twitterdev/engagement-api-client-ruby). This example Engagement API Client helps manage the process of generating engagement metadata for large Tweet collections. The client has a helper feature that can surface ['Top Tweets.'](https://github.com/twitterdev/engagement-api-client-ruby#top-tweets) As engagement metrics are retrieved, on a Tweet-by-Tweet basis, this client maintains a list of 'Top Tweets' with the highest levels of engagement. For example, if you are processing 100,000 Tweets, it can compile the top 10 for Retweets or any other available metric. Project repository includes an extensive README, which serves as an additional source of ‘getting started’ material and orientation for how the API works.
    * [Example Python client](https://github.com/jeffakolb/Gnip-Insights-Interface). This example illustrating using OAuth with the Requests package. The client also has an aggregating function for the /historical endpoint that combines API results over an arbitrary time period longer than 28 days.

Selecting an Engagement API Endpoint

Selecting an Engagement API Endpoint
------------------------------------

The Engagement API provides three distinct endpoints:

* **[Totals](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/api-reference/post-insights-engagement#Totals)** - provides grand totals of select metrics from owned 'owned' or 'unowned' Tweets. Some metrics are available for all Tweets, while others are only available for Tweets published in the last 90 days. Supports 250 Tweets per request.
* **[28 hour](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/api-reference/post-insights-engagement#28hr)** - provides time-series Engagement metrics for ‘owned’ Tweets from the last 28 hours. Supports 25 Tweets per request.
* **[Historical](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/api-reference/post-insights-engagement#Historical)** \- provides time-series Engagement metrics for up to four consecutive weeks for ‘owned’ Tweets posted since September 1, 2014. Supports 25 Tweets per request.  
     

Each endpoint has its own unique characteristics. Whether you are planning to use all three, or are trying to decide which one best matches your use case, it’s important to understand the differences between them.

Below we introduce some key concepts, further explore the three endpoints, and then present example use cases that map generally to a specific endpoint. Our hope is that this information will help you more efficiently integrate all three, or help you decide which single endpoint best fits your mission.  
 

### Key concepts

There are several key concepts that help illustrate the different features of, and data provided by, the three Engagement API endpoints.  
 

#### Impressions and engagement metrics

Impressions represent the number of times that a given Tweet has been viewed on the Twitter platform in an organic context. Impressions generated from Tweets that are seen in a Promoted or Paid context are not included. Before the Engagement API, Tweet impressions represented only a measure of potential views. It was based on counting followers of the author’s account and those of any account Retweeting the content. It did not take into account the common situation when a given user does not actually see the Tweet.

The impression metrics generated by the Engagement API is an actual measure of the number of times a Tweet has been rendered for display. If a follower of your account misses your Tweet, it does not count as an impression.  

The Engagement API provides metrics on 14 unique engagement [metric types](https://developer.twitter.com/en/docs/metrics/get-tweet-engagement/overview#EngagementTypes), each representing a distinct action a user can take when presented a Tweet. These include Retweeting, Liking, Replying, clicking on entities like #hashtags, links and media, following the author, and viewing the author’s profile. All of these individual actions are rolled up into a single Engagements metric.  
  

#### Owned and unowned Twitter content

The Engagement makes a clear distinction between owned and unowned Tweets. Owned Tweets are Tweets that are posted from your account, or Tweets that you have obtained permission to request Engagement data for. As with other Twitter APIs, you obtain permission by having other Twitter users/accounts share access tokens that enable you to make API requests on their behalf. A common way to obtain these tokens is with the [‘Sign in with Twitter’ process](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-for-websites/log-in-with-twitter/login-in-with-twitter).  

The /totals endpoint provides engagement data for both owned and unowned Tweets. For unowned Tweets, you can request engagement metrics that are publicly available in a Tweet display: Favorite, Retweet, and Reply. For these metrics, what the Engagement API brings to the table is the ability to retrieve these metrics at scale in an automated way. For owned Tweets, the /totals endpoint also provides Impression and (total) Engagement metrics.  

The /28hr and /historical endpoints provide metrics for owned Tweets only, meaning that you have to pass along user context when making the request to these endpoints.  
  

#### Total and time-series engagement Data

The /totals endpoint provides, as its name implies, only grand totals for its engagement types. Its numbers represent the up-to-date totals since the Tweet was posted. If a Tweet was just posted and you repeatedly request its metrics, these totals will commonly change with each request.  

The /28hr and /historical endpoints can provide both grand totals and time-series data. When requesting time-series data, the engagement metrics can be rolled up into daily or hourly data.     

See our documentation on [engagement groupings](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/guides/grouping-results) for how to request time-series data with the /28hr and /historical endpoints.  
  

### Endpoints and example use cases

Given the characteristics and differences discussed above, each individual endpoint generally maps to different types of use cases. To help you decide which endpoint best serves your particular use case, below are some example user statements and the endpoint that best satisfies it.  

#### **/totals**  

* I only need access to some metric types (Impressions, Engagements, Favorites, Retweets, Quote Tweets, Replies, and Video Views).
* I need access to basic engagement data for any Tweet, not just owned Tweets.
* I want to compare performance against a competitor.
* I want to track basic engagement stats for a hashtag or campaign that includes Tweets that I don’t own.
* I don’t need data broken out by day or hour, I just need the current total when I make a request.
* I need a single metric to show in a report or dashboard and don’t want to store any data.
* I want to show data at page load time, and just need to make a request and get a response.
* I need access to get data for hundreds of thousands or millions of Tweets per day.  
     

#### **/28hr**

* I need access to all 17 metric types.
* I want to show data for very recent Tweets posted in last 28 hours.
* I have a job that runs once a day to get data that I care about and only need to get data for the last day.
* I need to have metrics broken out by day or hour.
* I want to show time-series breakouts of activity by hour in a dashboard.
* I need high access for hundreds of thousands to Tweets per day
* I have storage capabilities and can refresh data once per day and keep a running tally.  
     

#### **/historical**

* I need access to all 17 metric types.
* I need to get historical data for Tweets created all the way back to September 2014.
* I want to show detailed historical analysis that compares campaigns.
* I need to have metrics broken out by day or hour.
* I don’t need high access to the Engagement API and only need to get data for a few hundred or thousand Tweets per day.  
      
     

Next steps
----------

* Read through the [Engagement API's Overview page](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/overview) for general information about the product.
* Check out our '[Getting started](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/guides/dev-getting-started-engagement-api)' guide for the Engagement API.
* Learn more about some of the recent changes to the Engagement API [here](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/guides/understanding-recent-changes-to-eapi-metrics).  
    
* Check out our [API references](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/api-reference/post-insights-engagement) to learn more about how to programmatically access Tweet engagement metrics.
* [Key Characteristics](https://developer.twitter.com/en/docs/metrics/get-tweet-engagement/guides/key-characteristics.html) - serves as a one-page developer’s checklist of API features and details.  
      
    
* Explore our sample code:  
    * [Example Ruby client](https://github.com/twitterdev/engagement-api-client-ruby). This example Engagement API Client helps manage the process of generating engagement metadata for large Tweet collections. The client has a helper feature that can surface ['Top Tweets.'](https://github.com/twitterdev/engagement-api-client-ruby#top-tweets) As engagement metrics are retrieved, on a Tweet-by-Tweet basis, this client maintains a list of 'Top Tweets' with the highest levels of engagement. For example, if you are processing 100,000 Tweets, it can compile the top 10 for Retweets or any other available metric. The  repository includes an extensive README, which serves as an additional source of ‘getting started’ material and orientation for how the API works.
    * [Example Python client](https://github.com/twitterdev/Gnip-Insights-Interface). This example illustrates using OAuth with the Requests package. The client also has an aggregating function for the /historical endpoint that combines API results over an arbitrary time period longer than 28 days.

Key characteristics

Engagement API key characteristics
----------------------------------

* **RESTful API** serving JSON data, supporting POST requests with JSON data bodies.
* **Types of Requests:** Client apps may make the following types of requests:
    * **Total engagements** \-- HTTP POST request to /totals endpoint
    * **Last 28-hour engagements** \-- HTTP POST request to /28hr endpoint
    * **Historical engagements** \-- HTTP POST request to /historical endpoint
* **OAuth authentication:**
    * [OAuth 1.0 User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a): All available metrics are available for Tweets that are owned by a user that has authorized your App using [3-legged OAuth](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens). You must use that user's Access Tokens when making your request.[](https://developer.twitter.com/en/docs/authentication/oauth-1-0a)
    * [OAuth 2.0 Bearer Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0): Select metrics (Retweets, Quote Tweets, Replies, Favorites, and Video Views) are available for any public Tweet. 
* **Request metadata and structure**: Request data is a JSON object consisting of a Tweet ID array, an array of engagement types, and an engagement grouping structure.
* **Tweets per request:**
    * /totals endpoint: 250 Tweet IDs
    * /28hr endpoint: 25 Tweet IDs
    * /historical endpoint: 25 Tweet IDs
* **Engagement metrics availability:**
    * **/totals** -- Metric totals since when Tweet was posted. Impressions and Engagements are available for Tweets published in the last 90 days, while Retweets, Quote Tweets, Replies, Favorites, and Video Views are available for all Tweets.
    * **/28hr** -- Last 28 hours from time of request.
    * **/historical** -- Any 28-day period starting September 1, 2014.
* **Metric types**: Each request includes an array of [Metric Types](http://support.gnip.com/apis/engagement_api/overview.html#EngagementTypes). The availability of these depends on the endpoint and, if requesting from the /totals endpoint, on whether Tweets are user-permissioned.
    * /totals endpoint:
        * All Tweets: Favorites, Retweets, Quote Tweets, Replies, and Video Views
        * Requires OAuth 1.0a User Context: Impressions, Engagements, Favorites, Replies, and Retweets
    * /28hr and /historical endpoints (Requires OAuth 1.0a User Context with Tweet owner's Access Token): Impressions, Engagements, Favorites, Replies, Retweets, URL Clicks, Hashtag Clicks, Detail Click, Permalink Clicks, Media Clicks, App Install Attempts, App Opens, Tweet Emails, Video Views, and Media Views
* **Engagement groupings:** Each request includes an array of [Engagement Groupings](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/guides/grouping-results). With these groupings you can customize how the returned metrics are organized. Up to three groupings can be included with each request. Metrics can be organized by the following values:
    * All endpoints: Tweet ID, Engagement Type
    * /28hr and /historical endpoints: These endpoints provide time-series if these additional groupings are specified: Engagement Day, Engagement Hour
* **Integration Expectations:** Your team will be responsible for the following.
    * Creating and maintaining a client app that can send HTTP requests to the Engagement API that returns engagement metrics for Tweet ID included in request.
* **Limitations**
* Video views are only available for Tweets that are 1800 days old or less.

Authenticating with the Engagement API

**Please note**: 

Twitter needs to enable access to the Engagement API for your developer App before you can start using the API. To this end, make sure to share the App ID that you intend to use for authentication purposes with your account manager or technical support team.

There are two authentication methods available with the Engagement API: [OAuth 1.0a](https://developer.twitter.com/en/docs/tutorials/authenticating-with-twitter-api-for-enterprise/authentication-method-overview#oauth1.0a) and [OAuth 2.0 Bearer Token](https://developer.twitter.com/en/docs/tutorials/authenticating-with-twitter-api-for-enterprise/authentication-method-overview#oauth2.0). 

**OAuth 2.0 Bearer Token** (also referred to as “application-only”) allows you to access publicly available engagement metrics. This authentication method can be used to get total counts for Favorites (aka Likes), Retweets, Quote Tweets, Replies, and video views for any publicly available Tweets when making requests to the [/totals endpoint](https://developer.twitter.com/en/docs/twitter-api/enterprise/engagement-api/api-reference/post-insights-engagement#Totals). 

**OAuth 1.0a** (also referred to as “user context”) allows you to make requests on behalf of a user and access private engagement metrics that belong to the user in question. 

This authentication method is required for:

* All requests sent to the [/28hr endpoint](https://developer.twitter.com/en/docs/twitter-api/enterprise/engagement-api/api-reference/post-insights-engagement#api-28hr) and [/historical endpoint](https://developer.twitter.com/en/docs/twitter-api/enterprise/engagement-api/api-reference/post-insights-engagement#Historical)
* Accessing any of the following private metrics: Impressions, Engagements, Media Views, Media Engagements, URL Clicks, Hashtag Clicks, Detail Expands, Permalink Clicks, App Install Attempts, App Opens, Email Tweet, User Follows, and User Profile Clicks

When sending a request with OAuth 1.0a, you need to include the Access Tokens (Access Token and Secret) of the user who owns the Tweet or protected resource of interest. If you do not provide the correct user Access Tokens when requesting protected user data, the Engagement API will return a `403 Forbidden` error.

The Engagement API will not allow you to fetch engagement data for [protected Tweets](https://help.twitter.com/en/safety-and-security/public-and-protected-tweets), even if you are authenticating on behalf of the user who owns these Tweets. Attempting to do so will return a `400 Bad Request` error, with the message `"Tweet ID(s) are unavailable"`.

If you are sending a request on behalf of your own Twitter account (in other words, the account that owns the developer App), you can generate the required Access Tokens directly from within the [developer portal](https://developer.twitter.com/en/portal/projects-and-apps), under the “Keys and tokens” tab for the developer App.

If you are making a request on behalf of any other user, you will need to use the 3-legged OAuth flow to obtain the required Access Tokens. The following documentation contains more information on how to do this: [OAuth 1.0a: how to obtain a user’s access tokens](https://developer.twitter.com/en/docs/tutorials/authenticating-with-twitter-api-for-enterprise/oauth1-0a-and-user-access-tokens).

For additional examples, including how to authenticate using OAuth 1.0a, check out [TwitterDev’s sample Python code for the Engagement API](https://github.com/twitterdev/enterprise-scripts-python/tree/master/Engagement-API).

Understanding recent changes to Engagement API metrics

Recent changes to the Engagement API
------------------------------------

The Engagement API delivers invaluable impression and engagement metrics that enable you to monitor the performance of your activity on Twitter. In our continual effort to enable marketing decisions based on our data, we are excited to share recent changes to the Engagement API that provide greater consistency with metrics across all of Twitter.  

We recently deployed changes to modernize the Engagement API to use the same metrics aggregation methodology in use by the Twitter analytics dashboard (analytics.twitter.com). We took a thoughtful approach to try and minimize breaking API changes when rolling out these new metrics and deployed the first set of changes on October 9, 2017. These changes improve consistency from all of the places you or your customers might monitor your performance on Twitter. Please see the detailed outline of the changes below:

|     |     |
| --- | --- |
| **Metric** | **Change** |
| engagements | We’ve updated the metrics that roll into overall engagements to match consistency with the Tweet analytics dashboard. Engagements measures “times people interacted with this Tweet”.<br><br>For Tweets that include media like a video or a GIF, the engagements metric will no longer include media views. Media views can now be accessed in a new metric, _media\_views_. |
| media\_clicks\* | This metric has been replaced by a new metric called “_media\_engagements_”. |
| video\_views | As of July 6th, 2018, this metric is now available for 'unowned' Tweets via the [/totals](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/api-reference/post-insights-engagement#Totals) endpoint. This means that you can access the video views for **all** Tweets by using app-only authentication. <br><br>You can only request video views that are younger than 1800 days old. If you try to request video views for a Tweet older than 1800 days, you will receive the following:<br><br>"unsupported\_for\_video\_views\_tweet\_ids": \["TWEET\_ID"\]<br><br>**Please note** that it will differ from media\_views in that video\_views relies on the MRC standard of 50% of the video in view for at least two seconds.  <br><br>**Also,** note that you may see a discrepancy between the video views metric displayed in the Twitter owned and operated platforms (mobile app and website) and the number that you receive via the /28hr and /historical endpoints.<br><br>* The video views displayed in the Twitter user interface and that delivers using the /totals endpoint will display the video view aggregated across all Tweets in which the given video has been posted. That means that the metric displayed in the UI includes the combined views from any instance where the video has been Retweeted or reposted in separate Tweets.<br>* The video views provided by the /28hr and /historical endpoints will just include those views generated by the specific Tweet for which you are pulling metrics. |
| media\_views | This includes all views (autoplay and click) of your media counted across videos, vines, gifs, and images.<br><br>**Please note** that Tweets with images do not show a media\_views metric in the analytics dashboard but will be returned in the Engagement API. |
| media\_engagements\* | This includes the number of clicks on your media across videos, vines, gifs, and images. This metric is replacing _media\_clicks_. |
| quote\_tweets | As of July 7th, 2020, this metric is now available for 'unowned' Tweets via the /totals endpoint. This means that you can access the Quote Tweet count for all Tweets by using app-only authentication. |

Next steps
----------

* Read through the [Engagement API's Overview page](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/overview) for general information about the product.
* Check out our '[Getting started](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/guides/dev-getting-started-engagement-api)' guide for the Engagement API.
* Check out our [API references](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/api-reference/post-insights-engagement) to learn more about how to programmatically access Tweet engagement metrics.  
    
* [Key Characteristics](https://developer.twitter.com/en/docs/metrics/get-tweet-engagement/guides/key-characteristics.html) - serves as a one-page developer’s checklist of API features and details.  
      
    
* Explore our sample code:  
    * [Example Ruby client](https://github.com/twitterdev/engagement-api-client-ruby). This example Engagement API Client helps manage the process of generating engagement metadata for large Tweet collections. The client has a helper feature that can surface ['Top Tweets.'](https://github.com/twitterdev/engagement-api-client-ruby#top-tweets) As engagement metrics are retrieved, on a Tweet-by-Tweet basis, this client maintains a list of 'Top Tweets' with the highest levels of engagement. For example, if you are processing 100,000 Tweets, it can compile the top 10 for Retweets or any other available metric. The  repository includes an extensive README, which serves as an additional source of ‘getting started’ material and orientation for how the API works.
    * [Example Python client](https://github.com/twitterdev/Gnip-Insights-Interface). This example illustrates using OAuth with the Requests package. The client also has an aggregating function for the /historical endpoint that combines API results over an arbitrary time period longer than 28 days.

Interpreting the metrics

Interpreting the metrics
------------------------

**Note:** You may observe differences between reported data on some of the Twitter web dashboards, and the data reported in the Engagement API. These differences occur because the web dashboards typically only show engagements and/or impressions that occurred within the selected time range. For example, a web dashboard may show engagement on Tweets within the span of a calendar month, while the Engagement API may show engagements that fall beyond the span of that month, but within the time range requested. The Engagement API should be seen as the valid source, in these cases.  
 

### Impressions and engagement data

The Engagement API delivers **organic** impressions and engagement data.

Impressions represent the number of times that a given Tweet has been viewed on the Twitter platform in an organic context. Impressions generated from Tweets that are seen in a Promoted or Paid context are **not** included.

Engagements represent the number of times that a given Tweet was engaged upon by a viewer in both an **organic** and **promoted** context. Engagements include, but are not limited to, Retweets, Favorites, Replies, URL Clicks, Hashtag Clicks, Mention Clicks, and Media Views. For the full list of included engagement actions, please see the Engagement Data section. 

In order to calculate a baseline engagement rate, please use the total number of engagements divided by the total number of impressions for a given Tweet for the time period you are analyzing.  

Impression and engagement data can only be retrieved for Tweets from owned @handles, or @handles that have authorized your application to view details about their Tweets.  Internally, the Engagement API will track the number of unique @handles that have been requested against the contracted @handle limit.  It's recommended to also track the @handle request usage on the client side throughout the month.    
  

### Video metrics

There are a couple of different metrics that represent impressions of media within Twitter. The first of which is our video views metric, which relies on the MRC standard of 50% of the video in view for at least two seconds. The second is Media Views, that includes all views (autoplay and click) of your media counted across videos, vines, gifs, and images.

The video views metric is available for owned Tweets via the /28hour and /historical endpoints, as well as for all unowned Tweets via the /totals endpoint. 

While the video views metric within the Twitter user interface is using the same MRC standard, please note that you may see a discrepancy between the video views metric displayed in the Twitter owned and operated platforms (mobile app and website) and the number that you receive via the different Engagement API endpoints.

* The video views provided by the /totals endpoint and the Twitter user interface will display the video view aggregated across all Tweets in which the given video has been posted. That means that the metric delivered via /totals and displayed in the Twitter UI includes the combined views from any instance where the video has been Retweeted or reposted in separate Tweets.
* The video views provided by the /28hour and /historical Engagement API endpoints will just include those views generated by the specific Tweet for which you are pulling metrics.   
     

Please note that we do not deliver video views for Tweets that are older than 1800 days. Instead, we deliver an object that lists the Tweets that are older than 1800 days. You will still receive all other metrics for your requested Tweets in a separate object. Here is an example response:

      `{   "unsupported_for_video_views_tweet_ids": [     "479311209565413376",     "477139122520219648"   ],   "grouping name": {     "479311209565413376": {       "favorites": "69",       "impressions": "1692",       "retweets": "142",       "video_views": "0"     },     "477139122520219648": {       "favorites": "10",       "impressions": "1023",       "retweets": "6",       "video_views": "0"     },     "1397568983931392004": {       "favorites": "268",       "impressions": "26803",       "retweets": "56",       "video_views": "17902"     }   } }`
    

The Media Views metric is only available for owned Tweets with the /28hour and /historical endpoints.  

Next steps
----------

* Read through the [Engagement API's Overview page](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/overview) for general information about the product.
* Check out our '[Getting started](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/guides/dev-getting-started-engagement-api)' guide for the Engagement API.
* Learn more about some of the recent changes to the Engagement API [here](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/guides/understanding-recent-changes-to-eapi-metrics).  
    
* Check out our [API references](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/api-reference/post-insights-engagement) to learn more about how to programmatically access Tweet engagement metrics.
* [Key Characteristics](https://developer.twitter.com/en/docs/metrics/get-tweet-engagement/guides/key-characteristics.html) - serves as a one-page developer’s checklist of API features and details.  
      
    
* Explore our sample code:  
    * [Example Ruby client](https://github.com/twitterdev/engagement-api-client-ruby). This example Engagement API Client helps manage the process of generating engagement metadata for large Tweet collections. The client has a helper feature that can surface ['Top Tweets.'](https://github.com/twitterdev/engagement-api-client-ruby#top-tweets) As engagement metrics are retrieved, on a Tweet-by-Tweet basis, this client maintains a list of 'Top Tweets' with the highest levels of engagement. For example, if you are processing 100,000 Tweets, it can compile the top 10 for Retweets or any other available metric. The  repository includes an extensive README, which serves as an additional source of ‘getting started’ material and orientation for how the API works.
    * [Example Python client](https://github.com/twitterdev/Gnip-Insights-Interface). This example illustrates using OAuth with the Requests package. The client also has an aggregating function for the /historical endpoint that combines API results over an arbitrary time period longer than 28 days.

Grouping Results

Engagement API groupings
------------------------

Groupings enable custom organization of the returned engagement metrics. You can include a maximum of 3 groupings per request. You can choose to group the metrics by one or more of the following values:

_All three endpoints support:_

* tweet.id
* engagement.type  
     

_The `/28hr` and `/historical` can provide time-series metrics, and thus support:_

* engagement.day
* engagement.hour  
      
    

Groupings are honored serially, so that you can change the desired result format by changing the order of your `group_by` values. Groupings that contain four `group_by` values will only be supported in one of the following two formats:  
 

    "group_by": [
        "tweet.id",
        "engagement.type",
        "engagement.day",
        "engagement.hour"
      ]

  
OR

    "group_by": [
        "engagement.type",
        "tweet.id",
        "engagement.day",
        "engagement.hour"
    ]

  
For example, if you want to generate grand totals of metric types, include the following “groupings” specification as part of your request (and see the [API Reference](https://developer.twitter.com/en/docs/metrics/get-tweet-engagement/api-reference/post-insights-engagement.html) page for more information on assembling requests):  
 

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

  
With this grouping, the Engagement API’s JSON response will include a root-level `"Grand Totals"` attribute which contains grand totals by metrics type:  
 

    {
      "Grand Totals": {
        "favorites": "12",
        "replies": "2",
        "retweets": "2"
      }
    }

  
To generate a 4-hour time-series of metrics for a single Tweet grouped by Tweet IDs, the following Grouping specification would be part of the request:  
 

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

  
With this grouping, the Engagement API’s JSON response will include a root-level `"Tweets_MetricType_TimeSeries"` attribute which contains the metrics broken down by Tweet ID, then metric type, and the corresponding hourly time-series:  
 

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

Next steps
----------

* Check out our '[Getting started](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/guides/dev-getting-started-engagement-api)' guide for the Engagement API.
* Figure out [which Engagement API endpoint is right for you](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/guides/selecting-engagement-endpoint).
* Learn more about some of the recent changes to the Engagement API [here](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/guides/understanding-recent-changes-to-eapi-metrics).
* Check out our [API references](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/api-reference/post-insights-engagement) to learn more about how to programatically access Tweet engagement metrics.  
      
    
* Explore our sample code:  
    * [Example Ruby client](https://github.com/twitterdev/engagement-api-client-ruby). This example Engagement API Client helps manage the process of generating engagement metadata for large Tweet collections. The client has a helper feature that can surface ['Top Tweets.'](https://github.com/twitterdev/engagement-api-client-ruby#top-tweets) As engagement metrics are retrieved, on a Tweet-by-Tweet basis, this client maintains a list of 'Top Tweets' with the highest levels of engagement. For example, if you are processing 100,000 Tweets, it can compile the top 10 for Retweets or any other available metric. The  repository includes an extensive README, which serves as an additional source of ‘getting started’ material and orientation for how the API works.
    * [Example Python client](https://github.com/twitterdev/Gnip-Insights-Interface). This example illustrates using OAuth with the Requests package. The client also has an aggregating function for the /historical endpoint that combines API results over an arbitrary time period longer than 28 days.

FAQ

Frequently asked questions
--------------------------

Enterprise

### Engagement API

**How can I access the Engagement API?**

Access to the Engagement API is provisioned through an enterprise subscription.  Please fill out [this form](https://developer.twitter.com/content/developer-twitter/en/enterprise-application) to get in touch with our sales team.  
 

**How is my usage tracked by '@handle'?**

If your contract includes a limit for the number of unique handles that can be used with Engagement API.  The internal Twitter system will keep track of the number of Authenticated users owning Tweets that are queried with the Engagement API.  Customers should also keep track of this unique number on the client side.  Currently, there is no usage API or UI to check the @handle usage for the Engagement API.  The system will not block overages if there are more @handles requested than what is contracted.  At the end of the billing month, the number of unique @handles queried is compared to the contracted amount and an overage will be charged in accordance with the contract terms.

**Can I check my @handle usage for Engagement API?**

Currently, there is no usage API or UI to check the @handle usage for the Engagement API.  The system will not block overages if there are more @handles requested than what is contracted.  At the end of the billing month, the number of unique @handles queried is compared to the contracted amount and an overage will be charged in accordance with the contract terms.

**The `engagements` metadata field returned in the payload is not equal to the sum of all the various engagement metric totals. Why is this the case?**

This is to be expected. The `engagements` metadata field may not always correlate with the sum of all individual engagement metrics returned by the API. This is because the `engagements` metadata field may include additional engagements that do not have specific metrics broken out in the payload. Said another way, adding all of the various engagement metric totals together may not equal the value you are seeing in the `engagements` metric field that is returned to you in the payload.

You can think of the `engagements` metadata field as any click or interaction made on the Tweet.  
 

**The `url_clicks` field in the payload response is returning a number, when in fact the Tweet does not have a URL. How is this possible?**

This may be because a Tweet that contains something like a hashtag (that creates a link to another page) will count as a URL click if it is clicked on by a user.  
 

**Why can I not receive engagement data for a specific Tweet?**

There are various reasons why you might not be able to retrieve engagement data for a specific Tweet, including:

* The Tweet ID or IDs you have requested are not available based on the authentication token you are using to retrieve data on behalf of a third party.
* The Tweet ID or IDs you have requested specific to the /totals endpoint are not 90 days or newer and are thus not available for returning the impressions or engagement metrics.
* The Tweet ID or IDs you have requested are no longer available, usually indicating that they have been deleted or are no longer publicly available for another reason.

Please review the different [error messages](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/api-reference/post-insights-engagement#ErrorMessages) that you will likely receive in any of the above cases.  
 

**How can I handle rate limiting with the Engagement API?**

You can use the `x-per-minute-limit` and `x-per-minute-remaining` information returned by the response header when you make a request to the Engagement API to monitor your consumption.  
  
`x-per-minute-limit` tells you what your allowance is and `x-per-minute-remaining` tells you how many calls you have left.  

###   
Error troubleshooting guide

**I am having problems authenticating**

Please make sure to review our [guidelines on authenticating](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/api-reference/post-insights-engagement#Authentication) with the Engagement API.  
 

**I have passed the correct consumer key and secret, as well as access token and access token secret, but the following error is being returned. What can I do?**

    [
        Your account could not be authenticated. Reason: Unknown Authorization Type;
    ]

  
Make sure not to use any access tokens or secrets when you try and authenticate with the /totals endpoint. This is because if you do include these tokens, and are attempting to pull content from a Tweet not associated with these tokens, you will likely receive an error such as:

    [
        Forbidden to access tweets: 1054424731825229824;
    ]

###   
  
Still can't find what you're looking for?

**I have a question that hasn't yet been answered**

Please reach out to technical support and we will respond to you promptly.

POST insights/engagement

post-insights-engagement

POST insights/engagement
========================

Jump to on this page

[Methods](#Methods)

[Authentication](#Authentication)

[POST /insights/engagement/totals](#Totals)

[POST /insights/engagement/28hr](#api-28hr)

[POST /insights/engagement/historical](#Historical)

[Response Codes](#ResponseCodes)

[Error Messages](#ErrorMessages)

Methods [¶](#methods- "Permalink to this headline")
---------------------------------------------------

| Method | Description |
| --- | --- |
| [POST /insights/engagement/totals](#Totals) | Retrieve total impressions and engagements for a collection of Tweets. |
| [POST /insights/engagement/historical](#Historical) | Retrieve impressions and engagements for a collection of Tweets for a period up to 4 weeks in duration, back to September 1, 2014. |
| [POST /insights/engagement/28hr](#api-28hr) | Retrieve impressions and engagements for a collection of Tweets for the past 28 hours. |

Authentication  [¶](#authentication- "Permalink to this headline")
------------------------------------------------------------------

The Engagement API requires the use of HTTPS and supports the use of both User Context and Application-Only OAuth. Most requests to the Engagement API require the use of 3-Legged OAuth (A specific version of User Context), meaning that you use the consumer key and secret of the app that has been registered and approved for Engagement API access by your Twitter account manager, as well as the Tweet owners' access token and access token secret to call the endpoint. The following requests require this type of OAuth:

* Any request to /totals to obtain Impressions and Engagements metric types, which are limited to owned Tweets
* Any request to /28hr
* Any request to /historical

Some requests to the Engagement API can be performed using Application-Only OAuth, meaning that you just need to provide your consumer key and secret, or a bearer token. The following request can be performed with this type of OAuth:

* Any request to /totals to obtain Favorites, Replies, Retweets, or Video Views metric types, which can be retrieved for any Tweet

For any request, you will need to set up a Twitter app and corresponding API key using the app management console available at [developer.twitter.com](https://developer.twitter.com/en/docs/basics/developer-portal/guides/apps).

Please note - You can view and edit your existing [Twitter apps](https://developer.twitter.com/en/docs/basics/developer-portal/guides/apps) via the [Twitter app dashboard](https://developer.twitter.com/en/apps) if you are logged into your Twitter account on developer.twitter.com.

Once you have set up your app, the app ID will need to be approved by your account representative in order for your app to make requests to the Engagement API. Access tokens must be used to represent the “current user”, and requests made on behalf of a separate user must be signed with a valid token. Ensure that you’re [encoding reserved characters](https://tools.ietf.org/html/rfc3986) appropriately within URLs and POST bodies before preparing OAuth signature base strings.

For more information on how to get started with OAuth, please visit the following links:

* [OAuth Overview](https://developer.twitter.com/en/docs/basics/authentication/overview/oauth.html)
* [Using 3 Legged OAuth, also known as User Context](https://developer.twitter.com/en/docs/basics/authentication/overview/3-legged-oauth)
* [Using Application-Only OAuth](https://developer.twitter.com/en/docs/basics/authentication/overview/application-only)

POST /insights/engagement/totals  [¶](#post-insights-engagement-totals- "Permalink to this headline")
-----------------------------------------------------------------------------------------------------

The totals endpoint provides the ability to retrieve current total impressions and engagements for a collection of up to 250 Tweets at a time.

|     |     |
| --- | --- |
| **Request Method** | HTTP POST |
| **URL** | `https://data-api.twitter.com/insights/engagement/totals` |
| **Content Type** | `application/json` |
| **Compression** | Gzip. To make a request using Gzip compression, send an Accept-Encoding header in the connection request.  <br>The header should look like the following:  <br>  <br>`Accept-Encoding: gzip` |
| **POST Format** | Requests can be sent as a POST request where the body is a JSON object containing a collection of Tweet IDs and a desired grouping. The POST is formatted as an array with a `tweets`, `engagements`, and `groupings` object. Each request can have a maximum of 250 Tweet IDs.  <br>  <br>An example POST body looks like:  <br>  <br><br>  {<br>    "tweet\_ids": \[<br>        "Tweet ID 1",<br>        "Tweet ID 2",<br>        "Tweet ID 3"<br>    \],<br>      "engagement\_types": \[<br>        "impressions",<br>        "engagements",<br>        "favorites",<br>        "quote\_tweets"<br>    \],<br>    "groupings": {<br>      "grouping name": {<br>        "group\_by": \[<br>          "tweet.id",<br>          "engagement.type"<br>        \]<br>      }<br>    }<br>  } |
| **Tweet IDs** | An array that includes the Tweet IDs for the Tweets to be queried for engagement data. Please note that you are only able to request data for Tweets that were created by the authenticating @handle. Up to 250 Tweets may be included per request, and Tweet IDs must be represented as strings. |
| **Engagement Types** | An array that includes the types of engagement metrics to be queried. The Totals endpoint supports only the following engagement types: `impressions`, `engagements`, `favorites`, `retweets`, `quote_tweets`, `replies`, `video_views`.  <br>The `/totals` endpoint supports the ability to retrieve `impressions` and `engagements` for Tweets created within the last 90 days, and `favorites`, `retweets`, `quote_tweets`, `replies`, and `video_views` for any Tweet. |
| **Groupings** | Results from the Engagement API can be returned in different groups to best fit your needs. You can include a maximum of 3 groupings per request.  <br>  <br>For each grouping, you may define a custom grouping name to make it easier to refer to this grouping type in your application.  <br>  <br>Once you have defined a grouping name, you can choose to group `tweet.id` and/or `engagement.type`.  <br>  <br>Groupings are honored serially, so that you can change the desired result format by changing the order of your group\_by values. An example grouping that will show metrics separated by Tweet ID and metric type looks like:  <br>  <br><br>  "groupings": {<br>      "my grouping name": {<br>        "group\_by": \[<br>          "tweet.id",<br>          "engagement.type"<br>        \]<br>      }<br>    } |
| **POST Size Limit** | Requests can be made for a maximum of 250 Tweet IDs at a time. |
| **Response Format** | JSON. The header of your request should specify JSON format for the response. |
| **Rate Limit** | You will be rate limited by minute, as specified in your contract according to your level of access. |
| **Example Request (public metrics)** | curl --request POST <br>  --url https://data-api.twitter.com/insights/engagement/totals <br>  --header 'accept-encoding: gzip' <br>  --header 'authorization: Bearer ' <br>  --header 'content-type: application/json' <br>  --data '{<br>                "tweet\_ids": \[<br>                    "1070059276213702656","1021817816134156288","1067094924124872705"<br>                \],<br>                "engagement\_types": \[<br>                    "favorites","retweets","replies","quote\_tweets","video\_views"<br>                \],<br>                "groupings": {<br>                    "perTweetMetricsUnowned": {<br>                        "group\_by": \[<br>                            "tweet.id",<br>                            "engagement.type"<br>                        \]<br>                    }<br>                }<br>            } <br>  --verbose <br>  --compressed |
| **Example Request** | curl --request POST <br>  --url https://data-api.twitter.com/insights/engagement/totals <br>  --header 'accept-encoding: gzip' <br>  --header 'authorization: OAuth oauth\_consumer\_key="consumer-key-for-app",oauth\_nonce="generated-nonce",oauth\_signature="generated-signature",oauth\_signature\_method="HMAC-SHA1", oauth\_timestamp="generated-timestamp",oauth\_token="access-token-for-authed-user", oauth\_version="1.0"' <br>  --header 'content-type: application/json' <br>  --data '{<br>                "tweet\_ids": \[<br>                    "1060976163948904448","1045709644067471360"<br>                \],<br>                "engagement\_types": \[<br>                    "favorites","replies","retweets","video\_views","impressions","engagements"<br>                \],<br>                "groupings": {<br>                    "perTweetMetricsOwned": {<br>                        "group\_by": \[<br>                            "tweet.id",<br>                            "engagement.type"<br>                        \]<br>                    }<br>                }<br>            }' <br>  --verbose <br>  --compressed |
| **Example Response (public metrics)** | {<br>  "perTweetMetricsUnowned": {<br>    "1021817816134156288": {<br>      "favorites": "530",<br>      "quote\_tweets": "79",<br>      "replies": "147",<br>      "retweets": "323",<br>      "video\_views": "0"<br>    },<br>    "1067094924124872705": {<br>      "favorites": "1360",<br>      "quote\_tweets": "29",<br>      "replies": "56",<br>      "retweets": "178",<br>      "video\_views": "5754512"<br>    },<br>    "1070059276213702656": {<br>      "favorites": "69",<br>      "quote\_tweets": "5",<br>      "replies": "7",<br>      "retweets": "26",<br>      "video\_views": "0"<br>    }<br>  }<br>} |
| **Example Response** | {<br>  "perTweetMetricsOwned": {<br>    "1045709644067471360": {<br>      "engagements": "2",<br>      "favorites": "0",<br>      "impressions": "47",<br>      "replies": "0",<br>      "retweets": "8",<br>      "quote\_tweets": "5",<br>      "video\_views": "0"<br>    },<br>    "1060976163948904448": {<br>      "engagements": "4",<br>      "favorites": "0",<br>      "impressions": "148",<br>      "replies": "1",<br>      "retweets": "9",<br>      "quote\_tweets": "2",<br>      "video\_views": "0"<br>    }<br>  }<br>} |
| **Unavailable Tweet IDs** | For queries that include Tweet IDs that have been made unavailable (e.g., have been deleted), appropriate data will be returned for all available Tweet IDs, and unavailable Tweet IDs will be referenced in an array called `unavailable_tweet_ids`. For example:  <br><br>  {<br>    "start": "2015-11-17T22:00:00Z",<br>    "end": "2015-11-19T02:00:00Z",<br>    "unavailable\_tweet\_ids": \[<br>        "323456789"<br>    \],<br>    "group1": {<br>     "423456789": {<br>      "favorites": "67",<br>      "replies": "8",<br>      "retweets": "26",<br>      "quote\_tweets": "2"<br>     }<br>    }<br>  } |

POST /insights/engagement/28hr [¶](#post-insights-engagement-28hr- "Permalink to this headline")
------------------------------------------------------------------------------------------------

The 28 hour endpoint provides the ability to retrieve impressions and engagements for a collection of up to 25 Tweets for the past 28 hours. The 28 hour endpoint also provides the ability to request metrics for all supported individual metrics. For the full list of supported metrics see [Metric Availability](https://developer.twitter.com/en/docs/metrics/get-tweet-engagement/overview.html#EngagementTypes).

|     |     |
| --- | --- |
| **Request Method** | HTTP POST |
| **URL** | `https://data-api.twitter.com/insights/engagement/28hr` |
| **Content Type** | `application/json` |
| **Compression** | Gzip. To make a request using Gzip compression, send an Accept-Encoding header in the connection request.  <br>The header should look like the following:  <br>  <br>`Accept-Encoding: gzip` |
| **POST Format** | Requests can be sent as a POST request where the body is a JSON object containing a collection of Tweet IDs and a desired grouping. The POST is formatted as an array with a `tweets`, `engagements`, and `groupings` object. Each request can have a maximum of 25 Tweet IDs.  <br>  <br>An example POST body looks like:  <br>  <br><br>  {<br>    "tweet\_ids": \[<br>       "Tweet ID 1",<br>       "Tweet ID 2",<br>       "Tweet ID 3"<br>    \],<br>      "engagement\_types": \[<br>        "impressions",<br>        "engagements",<br>        "url\_clicks",<br>        "detail\_expands"<br>    \],<br>    "groupings": {<br>      "grouping name": {<br>        "group\_by": \[<br>          "tweet.id",<br>          "engagement.type",<br>          "engagement.hour"<br>        \]<br>      }<br>    }<br>  } |
| **Tweet IDs** | An array that includes the Tweet IDs for the Tweets to be queried for engagement data. Please note that you are only able to requests data for Tweets that were created by the authenticating @handle. The 28 hour endpoint supports up to a maximum of 25 Tweets per request, and Tweet IDs must be represented as strings. |
| **Engagement Types** | An array the types of engagement metrics to be queried.  <br>  <br>For the 28 hour endpoint, `impressions`, `engagements`, and all individual engagement types are supported metrics. For the full list of supported engagement metrics see [Engagement Data](https://developer.twitter.com/en/docs/metrics/get-tweet-engagement/overview.html#AvailableData). |
| **Groupings** | Results from the Engagement API can be returned in different groups to best fit your needs. You can include a maximum of 3 groupings per request.  <br>  <br>For each grouping, you may define a custom grouping name to make it easier to refer to this grouping type in your application. Once you have defined a grouping name, you can choose to group by one or more of the following values:  <br>`tweet.id`  <br>`engagement.type`  <br>`engagement.day`  <br>`engagement.hour`  <br>Groupings are honored serially, so that you can change the desired result format by changing the order of your group\_by values. An example grouping that will show metrics separated by Tweet ID, metric type, and looks like:<br><br>  "groupings": {<br>    "my grouping name": {<br>      "group\_by": \[<br>        "tweet.id",<br>        "engagement.type",<br>        "engagement.day"<br>      \]<br>    }<br>  }<br><br>  <br>Groupings that have 4 `group_by` items are only valid if they use one of the following two orders. Requests that have 4 `group_by` items in a single grouping that are not one of the following will return an error. Additionally, only one grouping with 4 `group_by` items will be allowed per request.  <br><br>"group\_by": \[<br>    "tweet.id",<br>    "engagement.type",<br>    "engagement.day",<br>    "engagement.hour"<br>  \]<br><br>"group\_by": \[<br>    "engagement.type",<br>    "tweet.id",<br>    "engagement.day",<br>    "engagement.hour"<br>  \] |
| **POST Size Limit** | Requests can be made for a maximum of 25 Tweet IDs at a time. |
| **Response Format** | JSON. The header of your request should specify JSON format for the response. |
| **Rate Limit** | You will be rate limited by minute, as specified in your contract according to your level of access. |
| **Example Request** | curl -X POST "https://data-api.twitter.com/insights/engagement/28hr" <br>  -H 'Accept-Encoding: gzip' <br>  -H 'Authorization OAuth oauth\_consumer\_key="consumer-key-for-app",oauth\_nonce="generated-nonce",oauth\_signature="generated-signature",oauth\_signature\_method="HMAC-SHA1", oauth\_timestamp="generated-timestamp",oauth\_token="access-token-for-authed-user", oauth\_version="1.0"' <br>  -d '{<br>    "tweet\_ids": \[<br>       "123456789"<br>    \],<br>      "engagement\_types": \[<br>        "impressions",<br>        "engagements"<br>    \],<br>    "groupings": {<br>      "hourly-time-series": {<br>        "group\_by": \[<br>          "tweet.id",<br>          "engagement.type",<br>          "engagement.day",<br>          "engagement.hour"<br>        \]<br>      }<br>    }<br>  }' |
| **Example Response** | {<br>    "start": "2015-09-14T17:00:00Z",<br>    "end": "2015-09-15T22:00:00Z",<br>    "hourly-time-series": {<br>      "123456789": {<br>        "impressions": {<br>          "2015-09-14": {<br>            "17": "551",<br>            "18": "412",<br>            "19": "371",<br>            "20": "280",<br>            "21": "100",<br>            "22": "19",<br>            "23": "6"<br>          },<br>          "2015-09-15": {<br>            "00": "5",<br>            "01": "2",<br>            "02": "7",<br>            "03": "3",<br>            "04": "1",<br>            "05": "0",<br>            "06": "0",<br>            "07": "0",<br>            "08": "0",<br>            "09": "0",<br>            "10": "0",<br>            "11": "0",<br>            "12": "0",<br>            "13": "0",<br>            "14": "0",<br>            "15": "0",<br>            "16": "0",<br>            "17": "0",<br>            "18": "0",<br>            "19": "0",<br>            "20": "0",<br>            "21": "0"<br>          }<br>        },<br>        "engagements": {<br>          "2015-09-14": {<br>            "17": "0",<br>            "18": "0",<br>            "19": "0",<br>            "20": "0",<br>            "21": "0",<br>            "22": "0",<br>            "23": "0"<br>          },<br>          "2015-09-15": {<br>            "00": "0",<br>            "01": "0",<br>            "02": "0",<br>            "03": "0",<br>            "04": "0",<br>            "05": "0",<br>            "06": "0",<br>            "07": "0",<br>            "08": "0",<br>            "09": "0",<br>            "10": "0",<br>            "11": "0",<br>            "12": "0",<br>            "13": "0",<br>            "14": "0",<br>            "15": "0",<br>            "16": "0",<br>            "17": "0",<br>            "18": "0",<br>            "19": "0",<br>            "20": "0",<br>            "21": "0"<br>          }<br>        }<br>      }<br>    }<br>  } |
| **Unavailable Tweet IDs** | For queries that include Tweet IDs that have been made unavailable (e.g., have been deleted), appropriate data will be returned for all available Tweet IDs, and unavailable Tweet IDs will be referenced in an array called `unavailable_tweet_ids`. For example:  <br><br>  {<br>    "start": "2015-11-17T22:00:00Z",<br>    "end": "2015-11-19T02:00:00Z",<br>    "unavailable\_tweet\_ids": \[<br>        "323456789"<br>    \],<br>    "group1": {<br>     "423456789": {<br>      "favorites": "67",<br>      "replies": "8",<br>      "retweets": 26<br>     }<br>    }<br>  } |

POST /insights/engagement/historical [¶](#post-insights-engagement-historical- "Permalink to this headline")
------------------------------------------------------------------------------------------------------------

The historical endpoint provides the ability to retrieve impressions and engagements for a collection of up to 25 Tweets for any period up to 4 weeks in duration. Currently, data older than September 1, 2014 cannot be requested from the API. The historical endpoint also provides the ability to request metrics for all supported individual metrics. For the full list of supported metrics see [Metric Availability](https://developer.twitter.com/en/docs/metrics/get-tweet-engagement/overview.html#EngagementTypes).

|     |     |
| --- | --- |
| **Request Method** | HTTP POST |
| **URL** | `https://data-api.twitter.com/insights/engagement/historical` |
| **Content Type** | `application/json` |
| **Compression** | Gzip. To make a request using Gzip compression, send an Accept-Encoding header in the connection request.  <br>The header should look like the following:  <br>  <br>`Accept-Encoding: gzip` |
| **POST Format** | Requests can be sent as a POST request where the body is a JSON object containing a collection of Tweet IDs and a desired grouping. The POST is formatted as an array with a `tweets`, `engagements`, and `groupings` object. Each request can have a maximum of 25 Tweet IDs. Each request can be specified with a custom Start and End date up to four weeks in duration.  <br>  <br><br>  {<br>    "tweet\_ids": \[<br>       "Tweet ID 1",<br>       "Tweet ID 2",<br>       "Tweet ID 3"<br>    \],<br>      "engagement\_types": \[<br>        "impressions",<br>        "engagements",<br>        "url\_clicks",<br>        "detail\_expands"<br>    \],<br>    "groupings": {<br>      "grouping name": {<br>        "group\_by": \[<br>          "tweet.id",<br>          "engagement.type",<br>          "engagement.hour"<br>        \]<br>      }<br>    }<br>  } |
| **Start and End Date** | A custom start and end date can be specified with the `start` and `end` values as part of the request. You must specify a start and end date that are not longer than 4 weeks in duration. The oldest possible start date at this time is September 1, 2014. End dates in the future are not supported. If no Start and End date are supplied, the API will default to the immediately previous 4 weeks.  <br>  <br>The lowest granularity that data can be returned from the Engagement API is by hour. For any requests made with Start or End values that do not fall directly on an hourly boundary, requests will default to the nearest inclusive hour. For instance, a request with "start":"2015-07-01T12:24:00Z" and "end":"2015-07-10T08:37:00Z" will default to "start":"2015-07-01T12:00:00Z","end":"2015-07-10T09:00:00Z". |
| **Tweet IDs** | An array that includes the Tweet IDs for the Tweets to be queried for engagement data. Please note that you are only able to requests data for Tweets that were created by the authenticating @handle. The 4 week historical endpoint supports up to a maximum of 25 Tweets per request, and Tweet IDs must be represented as strings. |
| **Engagement Types** | n array that includes the types of engagement metrics to be queried.  <br>  <br>For the 4 week historical endpoint, `impressions`, `engagements`, and all individual engagement types are supported metrics. For the full list of supported engagement metrics see [Engagement Data](https://developer.twitter.com/en/docs/metrics/get-tweet-engagement/overview.html#AvailableData).  <br>  <br>\*\*Note:\*\*Currently there are three metrics that will display as zero for queries made before September 15, 2015: `favorites`, `replies`, and `retweets`. |
| **Groupings** | Results from the Engagement API can be returned in different groups to best fit your needs. You can include a maximum of 3 groupings per request.  <br>  <br>For each grouping, you may define a custom grouping name to make it easier to refer to this grouping type in your application. Once you have defined a grouping name, you can choose to group by one or more of the following values:  <br>`tweet.id`  <br>`engagement.type`  <br>`engagement.day`  <br>`engagement.hour`  <br>Groupings are honored serially, so that you can change the desired result format by changing the order of your group\_by values. An example grouping that will show metrics separated by Tweet ID, metric type, and looks like:<br><br>  "groupings": {<br>    "my grouping name": {<br>      "group\_by": \[<br>        "tweet.id",<br>        "engagement.type",<br>        "engagement.day"<br>      \]<br>    }<br>  }<br><br>  <br>Groupings that have 4 `group_by` items are only valid if they use one of the following two orders. Requests that have 4 `group_by` items in a single grouping that are not one of the following will return an error. Additionally, only one grouping with 4 `group_by` items will be allowed per request.  <br><br>"group\_by": \[<br>    "tweet.id",<br>    "engagement.type",<br>    "engagement.day",<br>    "engagement.hour"<br>  \]<br><br>"group\_by": \[<br>    "engagement.type",<br>    "tweet.id",<br>    "engagement.day",<br>    "engagement.hour"<br>  \] |
| **POST Size Limit** | Requests can be made for a maximum of 25 Tweet IDs at a time. |
| **Response Format** | JSON. The header of your request should specify JSON format for the response. |
| **Rate Limit** | You will be rate limited by minute, as specified in your contract according to your level of access. |
| **Example Request** | curl -XPOST "https://data-api.twitter.com/insights/engagement/historical" <br>  -H 'Accept-Encoding: gzip' <br>  -H 'Authorization OAuth oauth\_consumer\_key="consumer-key-for-app",oauth\_nonce="generated-nonce",oauth\_signature="generated-signature",oauth\_signature\_method="HMAC-SHA1", oauth\_timestamp="generated-timestamp",oauth\_token="access-token-for-authed-user", oauth\_version="1.0"' <br>  -d '{<br>    "start": "2015-08-01",<br>    "end": "2015-08-15",<br>    "tweet\_ids": \[<br>       "123456789",<br>       "223456789",<br>       "323456789"<br>    \],<br>      "engagement\_types": \[<br>        "impressions",<br>        "engagements",<br>        "url\_clicks",<br>        "detail\_expands"<br>    \],<br>    "groupings": {<br>      "types-by-tweet-id": {<br>        "group\_by": \[<br>          "tweet.id",<br>          "engagement.type"<br>        \]<br>      }<br>    }<br>  }' |
| **Example Response** | {<br>    "start": "2015-08-01T00:00:00Z",<br>    "end": "2015-08-15T00:00:00Z",<br>    "types-by-tweet-id": {<br>      "123456789": {<br>        "impressions": "0",<br>        "engagements": "0",<br>        "url\_clicks": "0",<br>        "detail\_expands": "0"<br>      },<br>      "223456789": {<br>        "impressions": "788",<br>        "engagements": "134",<br>        "url\_clicks": "30",<br>        "detail\_expands": "1323"<br>      },<br>      "323456789": {<br>        "impressions": "4",<br>        "engagements": "0",<br>        "url\_clicks": "2",<br>        "detail\_expands": "0"<br>      }<br>    }<br>  } |
| **Unavailable Tweet IDs** | For queries that include Tweet IDs that have been made unavailable (e.g., have been deleted), appropriate data will be returned for all available Tweet IDs, and unavailable Tweet IDs will be referenced in an array called `unavailable_tweet_ids`. For example:<br><br>{<br>    "start": "2015-11-17T22:00:00Z",<br>    "end": "2015-11-19T02:27:50Z",<br>    "unavailable\_tweet\_ids": \[<br>        "323456789"<br>    \],<br>    "group1": {<br>     "423456789": {<br>      "favorites": "67",<br>      "replies": "8",<br>      "retweets": 26<br>     }<br>    }<br>  } |

Response Codes [¶](#response-codes- "Permalink to this headline")
-----------------------------------------------------------------

| Status | Text | Description |
| --- | --- | --- |
| 200 | OK  | The request was successful. |
| 400 | Bad Request | Generally, this response occurs due to the presence of invalid JSON in the request, or where the request failed to send any JSON payload. |
| 401 | Unauthorized | HTTP authentication failed due to invalid credentials. Check your OAuth keys and tokens. |
| 404 | Not Found | The resource was not found at the URL to which the request was sent, likely because an incorrect URL was used. |
| 429 | Too Many Requests | Your app has exceeded the limit on API requests. |
| 500 | Internal Server Error | There was an error on Gnip's side. Retry your request using an exponential backoff pattern. |
| 502 | Proxy Error | There was an error on Gnip's side. Retry your request using an exponential backoff pattern. |
| 503 | Service Unavailable | There was an error on Gnip's side. Retry your request using an exponential backoff pattern. |

  

Error Messages [¶](#error-messages- "Permalink to this headline")
-----------------------------------------------------------------

In various scenarios, the Engagement API will occur situation-specific error messages that your application should be equipped to deal with. The table below includes common examples of these error messages and how you should interpret them. Please note that in many cases the Engagement API will return partial results for available data with specific error messages as part of a 200 OK response with more information.

| Error Message | Description |
| --- | --- |
| `"errors":["Your account could not be authenticated. Reason: Access token not found"]` | An error in the authentication component of the request. The “Reason” should provide information that is helpful to troubleshoot the error. In cases where you are not able to resolve, please send the full error, including the “Reason”, to our support team. |
| `"errors":["1 Tweet ID(s) are unavailable"],"unavailable_tweet_ids": ["TWEET_IDS"]` | The Tweet ID or IDs you have requested are no longer available, usually indicating that they have been deleted or are no longer publicly available for another reason. |
| `"errors":["Impressions & engagements for tweets older than 90 days (*TIME_PERIOD*) are not supported"],"unsupported_for_impressions_engagements_tweet_ids":[*TWEET_IDS*]` | The Tweet ID or IDs you have requested specific to the /totals endpoint are not 90 days or newer and are thus not available for returning the impressions or engagements metrics. |
| `"errors":["Forbidden to access tweets: *TWEET_IDS*"]` | The Tweet ID or IDs you have requested are not available based on the authentication token you are using to retrieve data on behalf of a third party. |