
Grouping Results | Docs | Twitter Developer Platform 

Grouping Results

Engagement API groupings
------------------------

Groupings enable custom organization of the returned engagement metrics. You can include a maximum of 3 groupings per request. You can choose to group the metrics by one or more of the following values:

*All three endpoints support:*

* tweet.id
* engagement.type

*The `/28hr` and `/historical` can provide time-series metrics, and thus support:*

* engagement.day
* engagement.hour

Groupings are honored serially, so that you can change the desired result format by changing the order of your `group_by` values. Groupings that contain four `group_by` values will only be supported in one of the following two formats:  

```
"group_by": [
    "tweet.id",
    "engagement.type",
    "engagement.day",
    "engagement.hour"
  ]
```

OR

```
"group_by": [
    "engagement.type",
    "tweet.id",
    "engagement.day",
    "engagement.hour"
]
```

For example, if you want to generate grand totals of metric types, include the following “groupings” specification as part of your request (and see the API Reference page for more information on assembling requests):  

```
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
```

With this grouping, the Engagement API’s JSON response will include a root-level `"Grand Totals"` attribute which contains grand totals by metrics type:  

```
{
  "Grand Totals": {
    "favorites": "12",
    "replies": "2",
    "retweets": "2"
  }
}
```

To generate a 4-hour time-series of metrics for a single Tweet grouped by Tweet IDs, the following Grouping specification would be part of the request:  

```
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
```

With this grouping, the Engagement API’s JSON response will include a root-level `"Tweets_MetricType_TimeSeries"` attribute which contains the metrics broken down by Tweet ID, then metric type, and the corresponding hourly time-series:  

```
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
```

Next steps
----------

* Check out our 'Getting started' guide for the Engagement API.
* Figure out which Engagement API endpoint is right for you.
* Learn more about some of the recent changes to the Engagement API here.
* Check out our API references to learn more about how to programatically access Tweet engagement metrics.
* Explore our sample code:  
	+ Example Ruby client. This example Engagement API Client helps manage the process of generating engagement metadata for large Tweet collections. The client has a helper feature that can surface 'Top Tweets.' As engagement metrics are retrieved, on a Tweet-by-Tweet basis, this client maintains a list of 'Top Tweets' with the highest levels of engagement. For example, if you are processing 100,000 Tweets, it can compile the top 10 for Retweets or any other available metric. The  repository includes an extensive README, which serves as an additional source of ‘getting started’ material and orientation for how the API works.
	+ Example Python client. This example illustrates using OAuth with the Requests package. The client also has an aggregating function for the /historical endpoint that combines API results over an arbitrary time period longer than 28 days.

Developer policy and terms

Follow @XDevelopers

Subscribe to developer news

#### 
 X platform

* X.com
* Status
* Accessibility
* Embed a post
* Privacy Center
* Transparency Center
* Download the X app

#### 
 X Corp.

* About the company
* Company news
* Brand toolkit
* Jobs and internships
* Investors

#### 
 Help

* Help Center
* Using X
* X for creators
* Ads Help Center
* Managing your account
* Email Preference Center
* Rules and policies
* Contact us

#### 
 Developer resources

* Developer home
* Documentation
* Forums
* Communities
* Developer blog
* Engineering blog
* Developer terms

#### 
 Business resources

* Advertise
* X for business
* Resources and guides
* X for marketers
* Marketing insights
* Brand inspiration
* X Ads Academy

 © 2024 X Corp.

Cookies

Privacy

Terms and conditions

**Did someone say … cookies?**  

 X and its partners use cookies to provide you with a better, safer and
 faster service and to support our business. Some cookies are necessary to use
 our services, improve our services, and make sure they work properly.
 Show more about your choices.

* Accept all cookies
* Refuse non-essential cookies