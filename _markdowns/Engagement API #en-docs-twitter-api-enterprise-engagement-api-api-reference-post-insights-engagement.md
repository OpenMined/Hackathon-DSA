



POST insights/engagement | Docs | Twitter Developer Platform 





































































































POST insights/engagement



post-insights-engagement

POST insights/engagement
========================


Jump to on this pageMethods

Authentication

POST
/insights/engagement/totals

POST
/insights/engagement/28hr

POST
/insights/engagement/historical

Response
Codes

Error
Messages


Methods¶
--------




| Method | Description |
| --- | --- |
| POST
/insights/engagement/totals | Retrieve total impressions and engagements
for a collection of Tweets. |
| POST
/insights/engagement/historical | Retrieve impressions and engagements for a
collection of Tweets for a period up to 4 weeks in duration, back to
September 1, 2014. |
| POST
/insights/engagement/28hr | Retrieve impressions and engagements for a
collection of Tweets for the past 28 hours. |


Authentication
¶
----------------


The Engagement API requires the use of HTTPS and supports the use of
both User Context and Application-Only OAuth. Most requests to the
Engagement API require the use of 3-Legged OAuth (A specific version of
User Context), meaning that you use the consumer key and secret of the
app that has been registered and approved for Engagement API access by
your Twitter account manager, as well as the Tweet owners' access token
and access token secret to call the endpoint. The following requests
require this type of OAuth:


* Any request to /totals to obtain Impressions and Engagements metric
types, which are limited to owned Tweets
* Any request to /28hr
* Any request to /historical


Some requests to the Engagement API can be performed using
Application-Only OAuth, meaning that you just need to provide your
consumer key and secret, or a bearer token. The following request can be
performed with this type of OAuth:


* Any request to /totals to obtain Favorites, Replies, Retweets, or
Video Views metric types, which can be retrieved for any Tweet


For any request, you will need to set up a Twitter app and
corresponding API key using the app management console available at developer.twitter.com.


Please note - You can view and edit your existing Twitter
apps via the Twitter
app dashboard if you are logged into your Twitter account on
developer.twitter.com.


Once you have set up your app, the app ID will need to be approved by
your account representative in order for your app to make requests to
the Engagement API. Access tokens must be used to represent the “current
user”, and requests made on behalf of a separate user must be signed
with a valid token. Ensure that you’re encoding reserved
characters appropriately within URLs and POST bodies before
preparing OAuth signature base strings.


For more information on how to get started with OAuth, please visit
the following links:


* OAuth
Overview
* Using 3
Legged OAuth, also known as User Context
* Using
Application-Only OAuth


POST
/insights/engagement/totals ¶
----------------------------------


The totals endpoint provides the ability to retrieve current total
impressions and engagements for a collection of up to 250 Tweets at a
time.




|  |  |
| --- | --- |
| **Request Method** | HTTP POST |
| **URL** | `https://data-api.twitter.com/insights/engagement/totals` |
| **Content Type** | `application/json` |
| **Compression** | Gzip. To make a request using Gzip
compression, send an Accept-Encoding header in the connection
request.The header should look like the
following:`Accept-Encoding: gzip` |
| **POST Format** | Requests can be sent as a POST request
where the body is a JSON object containing a collection of Tweet IDs and
a desired grouping. The POST is formatted as an array with a
`tweets`, `engagements`, and
`groupings` object. Each request can have a maximum of 250
Tweet IDs.An example POST body looks
like:
```

  {
    "tweet_ids": [
        "Tweet ID 1",
        "Tweet ID 2",
        "Tweet ID 3"
    ],
      "engagement_types": [
        "impressions",
        "engagements",
        "favorites",
        "quote_tweets"
    ],
    "groupings": {
      "grouping name": {
        "group_by": [
          "tweet.id",
          "engagement.type"
        ]
      }
    }
  }

```
 |
| **Tweet IDs** | An array that includes the Tweet IDs for
the Tweets to be queried for engagement data. Please note that you are
only able to request data for Tweets that were created by the
authenticating @handle. Up to 250 Tweets may be included per request,
and Tweet IDs must be represented as strings. |
| **Engagement Types** | An array that includes the types of
engagement metrics to be queried. The Totals endpoint supports only the
following engagement types: `impressions`,
`engagements`, `favorites`, `retweets`,
`quote_tweets`, `replies`,
`video_views`.The `/totals` endpoint supports
the ability to retrieve `impressions` and
`engagements` for Tweets created within the last 90 days, and
`favorites`, `retweets`,
`quote_tweets`, `replies`, and
`video_views` for any Tweet. |
| **Groupings** | Results from the Engagement API can be
returned in different groups to best fit your needs. You can include a
maximum of 3 groupings per request.For each grouping, you may
define a custom grouping name to make it easier to refer to this
grouping type in your application.Once you have defined a
grouping name, you can choose to group `tweet.id` and/or
`engagement.type`.Groupings are honored serially,
so that you can change the desired result format by changing the order
of your group\_by values. An example grouping that will show metrics
separated by Tweet ID and metric type looks
like:
```

  "groupings": {
      "my grouping name": {
        "group_by": [
          "tweet.id",
          "engagement.type"
        ]
      }
    }

```
 |
| **POST Size Limit** | Requests can be made for a maximum of 250
Tweet IDs at a time. |
| **Response Format** | JSON. The header of your request should
specify JSON format for the response. |
| **Rate Limit** | You will be rate limited by minute, as
specified in your contract according to your level of access. |
| **Example Request (public
metrics)** | 
```

curl --request POST 
  --url https://data-api.twitter.com/insights/engagement/totals 
  --header 'accept-encoding: gzip' 
  --header 'authorization: Bearer ' 
  --header 'content-type: application/json' 
  --data '{
                "tweet_ids": [
                    "1070059276213702656","1021817816134156288","1067094924124872705"
                ],
                "engagement_types": [
                    "favorites","retweets","replies","quote_tweets","video_views"
                ],
                "groupings": {
                    "perTweetMetricsUnowned": {
                        "group_by": [
                            "tweet.id",
                            "engagement.type"
                        ]
                    }
                }
            } 
  --verbose 
  --compressed

```
 |
| **Example Request** | 
```

curl --request POST 
  --url https://data-api.twitter.com/insights/engagement/totals 
  --header 'accept-encoding: gzip' 
  --header 'authorization: OAuth oauth_consumer_key="consumer-key-for-app",oauth_nonce="generated-nonce",oauth_signature="generated-signature",oauth_signature_method="HMAC-SHA1", oauth_timestamp="generated-timestamp",oauth_token="access-token-for-authed-user", oauth_version="1.0"' 
  --header 'content-type: application/json' 
  --data '{
                "tweet_ids": [
                    "1060976163948904448","1045709644067471360"
                ],
                "engagement_types": [
                    "favorites","replies","retweets","video_views","impressions","engagements"
                ],
                "groupings": {
                    "perTweetMetricsOwned": {
                        "group_by": [
                            "tweet.id",
                            "engagement.type"
                        ]
                    }
                }
            }' 
  --verbose 
  --compressed

```
 |
| **Example Response (public
metrics)** | 
```

{
  "perTweetMetricsUnowned": {
    "1021817816134156288": {
      "favorites": "530",
      "quote_tweets": "79",
      "replies": "147",
      "retweets": "323",
      "video_views": "0"
    },
    "1067094924124872705": {
      "favorites": "1360",
      "quote_tweets": "29",
      "replies": "56",
      "retweets": "178",
      "video_views": "5754512"
    },
    "1070059276213702656": {
      "favorites": "69",
      "quote_tweets": "5",
      "replies": "7",
      "retweets": "26",
      "video_views": "0"
    }
  }
}

```
 |
| **Example Response** | 
```

{
  "perTweetMetricsOwned": {
    "1045709644067471360": {
      "engagements": "2",
      "favorites": "0",
      "impressions": "47",
      "replies": "0",
      "retweets": "8",
      "quote_tweets": "5",
      "video_views": "0"
    },
    "1060976163948904448": {
      "engagements": "4",
      "favorites": "0",
      "impressions": "148",
      "replies": "1",
      "retweets": "9",
      "quote_tweets": "2",
      "video_views": "0"
    }
  }
}

```
 |
| **Unavailable Tweet
IDs** | For queries that include Tweet IDs that
have been made unavailable (e.g., have been deleted), appropriate data
will be returned for all available Tweet IDs, and unavailable Tweet IDs
will be referenced in an array called
`unavailable_tweet_ids`. For
example:
```

  {
    "start": "2015-11-17T22:00:00Z",
    "end": "2015-11-19T02:00:00Z",
    "unavailable_tweet_ids": [
        "323456789"
    ],
    "group1": {
     "423456789": {
      "favorites": "67",
      "replies": "8",
      "retweets": "26",
      "quote_tweets": "2"
     }
    }
  }

```
 |


POST
/insights/engagement/28hr¶
-------------------------------


The 28 hour endpoint provides the ability to retrieve impressions and
engagements for a collection of up to 25 Tweets for the past 28 hours.
The 28 hour endpoint also provides the ability to request metrics for
all supported individual metrics. For the full list of supported metrics
see Metric
Availability.




|  |  |
| --- | --- |
| **Request Method** | HTTP POST |
| **URL** | `https://data-api.twitter.com/insights/engagement/28hr` |
| **Content Type** | `application/json` |
| **Compression** | Gzip. To make a request using Gzip
compression, send an Accept-Encoding header in the connection
request.The header should look like the
following:`Accept-Encoding: gzip` |
| **POST Format** | Requests can be sent as a POST request
where the body is a JSON object containing a collection of Tweet IDs and
a desired grouping. The POST is formatted as an array with a
`tweets`, `engagements`, and
`groupings` object. Each request can have a maximum of 25
Tweet IDs.An example POST body looks
like:
```

  {
    "tweet_ids": [
       "Tweet ID 1",
       "Tweet ID 2",
       "Tweet ID 3"
    ],
      "engagement_types": [
        "impressions",
        "engagements",
        "url_clicks",
        "detail_expands"
    ],
    "groupings": {
      "grouping name": {
        "group_by": [
          "tweet.id",
          "engagement.type",
          "engagement.hour"
        ]
      }
    }
  }

```
 |
| **Tweet IDs** | An array that includes the Tweet IDs for
the Tweets to be queried for engagement data. Please note that you are
only able to requests data for Tweets that were created by the
authenticating @handle. The 28 hour endpoint supports up to a maximum of
25 Tweets per request, and Tweet IDs must be represented as
strings. |
| **Engagement Types** | An array the types of engagement metrics
to be queried.For the 28 hour endpoint,
`impressions`, `engagements`, and all individual
engagement types are supported metrics. For the full list of supported
engagement metrics see Engagement
Data. |
| **Groupings** | Results from the Engagement API can be
returned in different groups to best fit your needs. You can include a
maximum of 3 groupings per request.For each grouping, you may
define a custom grouping name to make it easier to refer to this
grouping type in your application. Once you have defined a grouping
name, you can choose to group by one or more of the following
values:`tweet.id``engagement.type``engagement.day``engagement.hour`Groupings
are honored serially, so that you can change the desired result format
by changing the order of your group\_by values. An example grouping that
will show metrics separated by Tweet ID, metric type, and looks
like:
```

  "groupings": {
    "my grouping name": {
      "group_by": [
        "tweet.id",
        "engagement.type",
        "engagement.day"
      ]
    }
  }

```
Groupings
that have 4 `group_by` items are only valid if they use one
of the following two orders. Requests that have 4 `group_by`
items in a single grouping that are not one of the following will return
an error. Additionally, only one grouping with 4 `group_by`
items will be allowed per
request.
```

"group_by": [
    "tweet.id",
    "engagement.type",
    "engagement.day",
    "engagement.hour"
  ]

"group_by": [
    "engagement.type",
    "tweet.id",
    "engagement.day",
    "engagement.hour"
  ]

```
 |
| **POST Size Limit** | Requests can be made for a maximum of 25
Tweet IDs at a time. |
| **Response Format** | JSON. The header of your request should
specify JSON format for the response. |
| **Rate Limit** | You will be rate limited by minute, as
specified in your contract according to your level of access. |
| **Example Request** | 
```

curl -X POST "https://data-api.twitter.com/insights/engagement/28hr" 
  -H 'Accept-Encoding: gzip' 
  -H 'Authorization OAuth oauth_consumer_key="consumer-key-for-app",oauth_nonce="generated-nonce",oauth_signature="generated-signature",oauth_signature_method="HMAC-SHA1", oauth_timestamp="generated-timestamp",oauth_token="access-token-for-authed-user", oauth_version="1.0"' 
  -d '{
    "tweet_ids": [
       "123456789"
    ],
      "engagement_types": [
        "impressions",
        "engagements"
    ],
    "groupings": {
      "hourly-time-series": {
        "group_by": [
          "tweet.id",
          "engagement.type",
          "engagement.day",
          "engagement.hour"
        ]
      }
    }
  }'

```
 |
| **Example Response** | 
```
  
  {
    "start": "2015-09-14T17:00:00Z",
    "end": "2015-09-15T22:00:00Z",
    "hourly-time-series": {
      "123456789": {
        "impressions": {
          "2015-09-14": {
            "17": "551",
            "18": "412",
            "19": "371",
            "20": "280",
            "21": "100",
            "22": "19",
            "23": "6"
          },
          "2015-09-15": {
            "00": "5",
            "01": "2",
            "02": "7",
            "03": "3",
            "04": "1",
            "05": "0",
            "06": "0",
            "07": "0",
            "08": "0",
            "09": "0",
            "10": "0",
            "11": "0",
            "12": "0",
            "13": "0",
            "14": "0",
            "15": "0",
            "16": "0",
            "17": "0",
            "18": "0",
            "19": "0",
            "20": "0",
            "21": "0"
          }
        },
        "engagements": {
          "2015-09-14": {
            "17": "0",
            "18": "0",
            "19": "0",
            "20": "0",
            "21": "0",
            "22": "0",
            "23": "0"
          },
          "2015-09-15": {
            "00": "0",
            "01": "0",
            "02": "0",
            "03": "0",
            "04": "0",
            "05": "0",
            "06": "0",
            "07": "0",
            "08": "0",
            "09": "0",
            "10": "0",
            "11": "0",
            "12": "0",
            "13": "0",
            "14": "0",
            "15": "0",
            "16": "0",
            "17": "0",
            "18": "0",
            "19": "0",
            "20": "0",
            "21": "0"
          }
        }
      }
    }
  }

```
 |
| **Unavailable Tweet
IDs** | For queries that include Tweet IDs that
have been made unavailable (e.g., have been deleted), appropriate data
will be returned for all available Tweet IDs, and unavailable Tweet IDs
will be referenced in an array called
`unavailable_tweet_ids`. For
example:
```

  {
    "start": "2015-11-17T22:00:00Z",
    "end": "2015-11-19T02:00:00Z",
    "unavailable_tweet_ids": [
        "323456789"
    ],
    "group1": {
     "423456789": {
      "favorites": "67",
      "replies": "8",
      "retweets": 26
     }
    }
  }

```
 |


POST
/insights/engagement/historical¶
-------------------------------------


The historical endpoint provides the ability to retrieve impressions
and engagements for a collection of up to 25 Tweets for any period up to
4 weeks in duration. Currently, data older than September 1, 2014 cannot
be requested from the API. The historical endpoint also provides the
ability to request metrics for all supported individual metrics. For the
full list of supported metrics see Metric
Availability.




|  |  |
| --- | --- |
| **Request Method** | HTTP POST |
| **URL** | `https://data-api.twitter.com/insights/engagement/historical` |
| **Content Type** | `application/json` |
| **Compression** | Gzip. To make a request using Gzip
compression, send an Accept-Encoding header in the connection
request.The header should look like the
following:`Accept-Encoding: gzip` |
| **POST Format** | Requests can be sent as a POST request
where the body is a JSON object containing a collection of Tweet IDs and
a desired grouping. The POST is formatted as an array with a
`tweets`, `engagements`, and
`groupings` object. Each request can have a maximum of 25
Tweet IDs. Each request can be specified with a custom Start and End
date up to four weeks in
duration.
```

  {
    "tweet_ids": [
       "Tweet ID 1",
       "Tweet ID 2",
       "Tweet ID 3"
    ],
      "engagement_types": [
        "impressions",
        "engagements",
        "url_clicks",
        "detail_expands"
    ],
    "groupings": {
      "grouping name": {
        "group_by": [
          "tweet.id",
          "engagement.type",
          "engagement.hour"
        ]
      }
    }
  }

```
 |
| **Start and End Date** | A custom start and end date can be
specified with the `start` and `end` values as
part of the request. You must specify a start and end date that are not
longer than 4 weeks in duration. The oldest possible start date at this
time is September 1, 2014. End dates in the future are not supported. If
no Start and End date are supplied, the API will default to the
immediately previous 4 weeks.The lowest granularity that data
can be returned from the Engagement API is by hour. For any requests
made with Start or End values that do not fall directly on an hourly
boundary, requests will default to the nearest inclusive hour. For
instance, a request with "start":"2015-07-01T12:24:00Z" and
"end":"2015-07-10T08:37:00Z" will default to
"start":"2015-07-01T12:00:00Z","end":"2015-07-10T09:00:00Z". |
| **Tweet IDs** | An array that includes the Tweet IDs for
the Tweets to be queried for engagement data. Please note that you are
only able to requests data for Tweets that were created by the
authenticating @handle. The 4 week historical endpoint supports up to a
maximum of 25 Tweets per request, and Tweet IDs must be represented as
strings. |
| **Engagement Types** | n array that includes the types of
engagement metrics to be queried.For the 4 week historical
endpoint, `impressions`, `engagements`, and all
individual engagement types are supported metrics. For the full list of
supported engagement metrics see Engagement
Data.\*\*Note:\*\*Currently there are three metrics that will
display as zero for queries made before September 15, 2015:
`favorites`, `replies`, and
`retweets`. |
| **Groupings** | Results from the Engagement API can be
returned in different groups to best fit your needs. You can include a
maximum of 3 groupings per request.For each grouping, you may
define a custom grouping name to make it easier to refer to this
grouping type in your application. Once you have defined a grouping
name, you can choose to group by one or more of the following
values:`tweet.id``engagement.type``engagement.day``engagement.hour`Groupings
are honored serially, so that you can change the desired result format
by changing the order of your group\_by values. An example grouping that
will show metrics separated by Tweet ID, metric type, and looks
like:
```

  "groupings": {
    "my grouping name": {
      "group_by": [
        "tweet.id",
        "engagement.type",
        "engagement.day"
      ]
    }
  }

```
Groupings
that have 4 `group_by` items are only valid if they use one
of the following two orders. Requests that have 4 `group_by`
items in a single grouping that are not one of the following will return
an error. Additionally, only one grouping with 4 `group_by`
items will be allowed per
request.
```

"group_by": [
    "tweet.id",
    "engagement.type",
    "engagement.day",
    "engagement.hour"
  ]

"group_by": [
    "engagement.type",
    "tweet.id",
    "engagement.day",
    "engagement.hour"
  ]

```
 |
| **POST Size Limit** | Requests can be made for a maximum of 25
Tweet IDs at a time. |
| **Response Format** | JSON. The header of your request should
specify JSON format for the response. |
| **Rate Limit** | You will be rate limited by minute, as
specified in your contract according to your level of access. |
| **Example Request** | 
```

curl -XPOST "https://data-api.twitter.com/insights/engagement/historical" 
  -H 'Accept-Encoding: gzip' 
  -H 'Authorization OAuth oauth_consumer_key="consumer-key-for-app",oauth_nonce="generated-nonce",oauth_signature="generated-signature",oauth_signature_method="HMAC-SHA1", oauth_timestamp="generated-timestamp",oauth_token="access-token-for-authed-user", oauth_version="1.0"' 
  -d '{
    "start": "2015-08-01",
    "end": "2015-08-15",
    "tweet_ids": [
       "123456789",
       "223456789",
       "323456789"
    ],
      "engagement_types": [
        "impressions",
        "engagements",
        "url_clicks",
        "detail_expands"
    ],
    "groupings": {
      "types-by-tweet-id": {
        "group_by": [
          "tweet.id",
          "engagement.type"
        ]
      }
    }
  }'

```
 |
| **Example Response** | 
```

  {
    "start": "2015-08-01T00:00:00Z",
    "end": "2015-08-15T00:00:00Z",
    "types-by-tweet-id": {
      "123456789": {
        "impressions": "0",
        "engagements": "0",
        "url_clicks": "0",
        "detail_expands": "0"
      },
      "223456789": {
        "impressions": "788",
        "engagements": "134",
        "url_clicks": "30",
        "detail_expands": "1323"
      },
      "323456789": {
        "impressions": "4",
        "engagements": "0",
        "url_clicks": "2",
        "detail_expands": "0"
      }
    }
  }

```
 |
| **Unavailable Tweet
IDs** | For queries that include Tweet IDs that
have been made unavailable (e.g., have been deleted), appropriate data
will be returned for all available Tweet IDs, and unavailable Tweet IDs
will be referenced in an array called
`unavailable_tweet_ids`. For
example:
```

{
    "start": "2015-11-17T22:00:00Z",
    "end": "2015-11-19T02:27:50Z",
    "unavailable_tweet_ids": [
        "323456789"
    ],
    "group1": {
     "423456789": {
      "favorites": "67",
      "replies": "8",
      "retweets": 26
     }
    }
  }

```
 |


Response
Codes¶
---------------




| Status | Text | Description |
| --- | --- | --- |
| 200 | OK | The request was successful. |
| 400 | Bad Request | Generally, this response occurs due to the
presence of invalid JSON in the request, or where the request failed to
send any JSON payload. |
| 401 | Unauthorized | HTTP authentication failed due to invalid
credentials. Check your OAuth keys and tokens. |
| 404 | Not Found | The resource was not found at the URL to
which the request was sent, likely because an incorrect URL was
used. |
| 429 | Too Many Requests | Your app has exceeded the limit on API
requests. |
| 500 | Internal Server Error | There was an error on Gnip's side. Retry
your request using an exponential backoff pattern. |
| 502 | Proxy Error | There was an error on Gnip's side. Retry
your request using an exponential backoff pattern. |
| 503 | Service Unavailable | There was an error on Gnip's side. Retry
your request using an exponential backoff pattern. |


  

Error
Messages¶
---------------


In various scenarios, the Engagement API will occur
situation-specific error messages that your application should be
equipped to deal with. The table below includes common examples of these
error messages and how you should interpret them. Please note that in
many cases the Engagement API will return partial results for available
data with specific error messages as part of a 200 OK response with more
information.




| Error Message | Description |
| --- | --- |
| `"errors":["Your account could not be authenticated. Reason: Access token not found"]` | An error in the authentication component
of the request. The “Reason” should provide information that is helpful
to troubleshoot the error. In cases where you are not able to resolve,
please send the full error, including the “Reason”, to our support
team. |
| `"errors":["1 Tweet ID(s) are unavailable"],"unavailable_tweet_ids": ["TWEET_IDS"]` | The Tweet ID or IDs you have requested are
no longer available, usually indicating that they have been deleted or
are no longer publicly available for another reason. |
| `"errors":["Impressions & engagements for tweets older than 90 days (*TIME_PERIOD*) are not supported"],"unsupported_for_impressions_engagements_tweet_ids":[*TWEET_IDS*]` | The Tweet ID or IDs you have requested
specific to the /totals endpoint are not 90 days or newer and are thus
not available for returning the impressions or engagements metrics. |
| `"errors":["Forbidden to access tweets: *TWEET_IDS*"]` | The Tweet ID or IDs you have requested are
not available based on the authentication token you are using to
retrieve data on behalf of a third party. |



















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















