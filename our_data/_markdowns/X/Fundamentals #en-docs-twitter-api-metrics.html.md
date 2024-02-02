
Metrics | Docs | Twitter Developer Platform 

Metrics

Overview
--------

The metrics field allows developers to access public and private engagement metrics for Tweet and media objects. Public metrics are accessible by anyone with a developer account while private metrics are accessible from owned/authorized accounts (definition below). By metrics, we mean the total count of impressions, Retweets, Quote Tweets, likes, replies, video views, video view quartiles, URL and profile link clicks for each Tweet specified in the request. There is also the option to view a breakdown of metrics earned in an organic or promoted context, if the Tweet was promoted as an Ad.

Public metrics can be requested with App only Token authentication. Non-public metrics can be requested for owned/authorized Tweets only. This means developers are required to authenticate using OAuth 2.0 or OAuth 1.0a user context authorization.

**Non-public, organic, and promoted metrics are only available for Tweets that have been created within the last 30 days.** 

### Terminology

* **Authorized account**: Twitter account that has authorized your Twitter developer app by granting it access to that account (any app permission level will permit access to Tweet metrics). This can be achieved using the Authorization Code Flow with PKCE or 3-legged OAuth process.
* **Owned account**: Twitter account linked to your Twitter developer app.
* **Public metrics**: Metrics’ totals that are available for anyone to access on Twitter, such as number of likes and number of Retweets.
* **Non-public metrics**: Metrics’ totals that are not available for anyone to view on Twitter, such as number of impressions and video view quartiles. Requires OAuth 2.0 or OAuth 1.0a user context authentication.
* **Organic metrics**: Grouping of public and non-public metrics attributed to an organic context (posted and viewed in a regular manner). Requires OAuth 2.0 or OAuth 1.0a user context authentication.
* **Promoted metrics**: Grouping of public and non-public metrics attributed to a promoted context (posted or viewed as part of an Ads campaign). Requires OAuth 2.0 or OAuth 1.0a user context authentication and that the Tweet was promoted in an Ad. Promoted metrics are not included in these counts when a Twitter user is using their own Ads account to promote another Twitter user's Tweets. Promoted metrics are included in these counts when:
	+ a Twitter user promotes their own Tweets
	+ in an Ads account for a specific handle, the admin for that account may add another Twitter user as an account user so this second account user can promote Tweets for the handle

Available Metrics
-----------------

|  |  |  |
| --- | --- | --- |
| **Metric** | **API Representations** | **Description** |
| Impressions | `data.non_public_metrics.impression_count
 data.organic_metrics.impression_count
 data.promoted_metrics.impression_count` | A count of how many times the Tweet has been viewed (not unique by user). A view is counted if any part of the Tweet is visible on the screen.
This is a private, or non-public, metric and always requires OAuth 1.0a User Context authentication.
Using the `non_public_metrics` field, this returns the total count of impressions from both organic and paid contexts.
Using the `organic_metrics` field, this returns the count of impressions from organic contexts.
Using the `promoted_metrics` field, this returns the count of impressions from promoted contexts. |
| Retweets | `data.public_metrics.retweet_count
 data.organic_metrics.retweet_count
 data.promoted_metrics.retweet_count` | A count of how many times the Tweet has been Retweeted. Please note: This does not include Quote Tweets (“Retweets with comment”). To get the "Retweets and comments" total as displayed on the Twitter clients, simply add `retweet_count` and `quote_count`.
Using the `public_metrics` field, this will return the total count of Retweets from both organic and paid contexts, in order to maintain consistency with the counts shown publicly on Twitter.
Using the `organic_metrics` field, this returns the total count of Retweets from organic contexts.
Using the `promoted_metrics` field, this returns the total count of Retweets from paid contexts. |
| Quote Tweets | `data.public_metrics.quote_count` | A count of how many times the Tweet has been Retweeted with a new comment (message). Please note: This does not include Retweets. To get the “Retweets and comments” total as displayed on the Twitter clients, simply add `retweet_count` and `quote_count`.
This will return the total count of Quote Tweets. There are no Quote Tweets from a paid context so all Quote Tweets are organic. |
| Likes | `data.public_metrics.like_count
 data.organic_metrics.like_count
 data.promoted_metrics.like_count` | A count of how many times the Tweet has been liked.
Using the `public_metrics` field, this will return the total count of likes from both organic and paid contexts, in order to maintain consistency with the counts shown publicly on Twitter.
Using the `organic_metrics` field, this returns the total count of Retweets from organic contexts.
Using the `promoted_metrics` field, this returns the total count of Retweets from paid contexts. |
| Replies | `data.public_metrics.reply_count
 data.organic_metrics.reply_count
 data.promoted_metrics.reply_count` | A count of how many times the Tweet has been replied to.
Using the `public_metrics` field, this will return the total count of replies from both organic and paid contexts, in order to maintain consistency with the counts shown publicly on Twitter.
Using the `organic_metrics` field, this returns the total count of replies from organic contexts.
Using the `promoted_metrics` field, this returns the total count of replies from paid contexts. |
| URL Link Clicks | `data.non_public_metrics.url_link_clicks
 data.organic_metrics.url_link_clicks
 data.promoted_metrics.url_link_clicks` | A count of the number of times a user clicks on a URL link or URL preview card in a Tweet.
This is a private, or non-public, metric and always requires OAuth 1.0a User Context authentication.
Using the `non_public_metrics` field, this returns the total count of URL link clicks from both organic and paid contexts.
Using the `organic_metrics` field, this returns the count of URL link clicks from organic contexts.
Using the `promoted_metrics` field, this returns the count of URL link clicks from paid contexts. |
| User Profile Clicks | `data.non_public_metrics.user_profile_clicks
 data.organic_metrics.user_profile_clicks
 data.promoted_metrics.user_profile_clicks` | A count of the number of times a user clicks the following portions of a Tweet: display name, user name, profile picture.
This is a private, or non-public, metric and always requires OAuth 1.0a User Context authentication.
Using the `non_public_metrics` field, this returns the total count of user profile clicks from both organic and paid contexts.
Using the `organic_metrics` field, this returns the count of user profile clicks from organic contexts.
Using the `promoted_metrics` field, this returns the count of user profile clicks from paid contexts. |
| Video views | `includes.media.public_metrics.view_count
 includes.media.organic_metrics.view_count
 includes.media.promoted_metrics.view_count` | A count of how many times the video included in the Tweet has been viewed.
This is the number of video views aggregated across all Tweets in which the given video has been posted. That means that the metric includes the combined views from any instance where the video has been Retweeted or reposted in separate Tweets.
Use expansion for media objects, `expansions=attachment.media_keys`.
Using the `public_metrics` field, this returns the total count of video views from both organic and paid contexts, in order to maintain consistency with the counts shown publicly on Twitter.
Using the `organic_metrics` field, this returns the total count of video views from organic contexts.
Using the `promoted_metrics` field, this returns the total count of video views from paid contexts. |
| Video view quartiles | `includes.media.non_public_metrics.playback_0_count
 includes.media.non_public_metrics.playback_25_count
 includes.media.non_public_metrics.playback_50_count
 includes.media.non_public_metrics.playback_75_count
 includes.media.non_public_metrics.playback_100_count`
`includes.media.organic_metrics.playback_0_count
 includes.media.organic_metrics.playback_25_count
 includes.media.organic_metrics.playback_50_count
 includes.media.organic_metrics.playback_75_count
 includes.media.organic_metrics.playback_100_count`
`includes.media.promoted_metrics.playback_0_count
 includes.media.promoted_metrics.playback_25_count
 includes.media.promoted_metrics.playback_50_count
 includes.media.promoted_metrics.playback_75_count
 includes.media.promoted_metrics.playback_100_count` | The number of users who played through to each quartile in a video. This reflects the number of quartile views across all Tweets in which the given video has been posted.
This is a private, or non-public, metric and always requires OAuth 1.0a User Context authentication.
Use expansion for media objects, `expansions=attachment.media_keys`.
Using the `non_public_metrics` field, this returns the total count of video view quartiles from both organic and paid contexts.
Using the `organic_metrics` field, this returns the total count of video view quartiles from organic contexts.
Using the `promoted_metrics` field, this returns the total count of video view quartiles from paid contexts. |

Requesting metrics
------------------

### Public metrics

In the following request, we are requesting public metrics on the Tweet and on the attached video with the following fields and expansion. Be sure to replace `$BEARER_TOKEN` with your own generated bearer token.

* tweet.fields=public\_metrics
* expansions=attachments.media\_keys&media.fields=public\_metrics

#### Sample Request

```
      curl 'https://api.twitter.com/2/tweets?ids=1204084171334832128&tweet.fields=public_metrics&expansions=attachments.media_keys&media.fields=public_metrics' --header 'Authorization: Bearer $BEARER_TOKEN'
```

Code copied to clipboard

**Sample Response**

```
      {
    "data": [
        {
            "id": "1204084171334832128",
            "text": "Tired of reading? We’ve got you covered. Learn about the capabilities of the Account Activity API in this video walkthrough with @tonyv00 from our DevRel team. 🍿 ⬇️ https://t.co/LdHy4aLu0i",
            "public_metrics": {
                "retweet_count": 9,
                "reply_count": 2,
                "like_count": 49,
                "quote_count": 1
            },
            "attachments": {
                "media_keys": [
                    "13_1204080851740315648"
                ]
            }
        }
    ],
    "includes": {
        "media": [
            {
                "media_key": "13_1204080851740315648",
                "public_metrics": {
                    "view_count": 1808
                },
                "type": "video"
            }
        ]
    }
}
```

### 

### Private metrics (non-public, organic metrics)

In the following request, we are requesting non-public metrics with more details or organic metrics, meaning which of these metrics were generated in an organic context, on the Tweet and attached video with the following fields and expansion. Since these fields are private (not available to view on Twitter.com),Requires OAuth 2.0 or OAuth 1.0a user context authentication. is required for the request. Check out our guide that explains how to generate the OAuth 1.0a signature sampled below.

* `tweet.fields=non_public_metrics,organic_metrics`
* `expansions=attachments.media_keys&media.fields=non_public_metrics,organic_metrics`

**Sample Request**

```
      curl 'https://api.twitter.com/2/tweets/1204084171334832128?tweet.fields=non_public_metrics,organic_metrics&media.fields=non_public_metrics,organic_metrics&expansions=attachments.media_keys'
--header 'authorization: OAuth oauth_consumer_key="CONSUMER_API_KEY", oauth_nonce="OAUTH_NONCE", oauth_signature="OAUTH_SIGNATURE", oauth_signature_method="HMAC-SHA1", oauth_timestamp="OAUTH_TIMESTAMP", oauth_token="ACCESS_TOKEN", oauth_version="1.0"'
```

Code copied to clipboard

**Sample Response**

```
      {
  "data": {
    "attachments": {
      "media_keys": [
        "13_1204080851740315648"
      ]
    },
    "id": "1263145271946551300",
    "non_public_metrics": {
      "impression_count": 956,
      "url_link_clicks": 9,
       "user_profile_clicks": 34
    },
    "organic_metrics": {
      "impression_count": 956,
      "like_count": 49,
      "reply_count": 2,
      "retweet_count": 9,
      "url_link_clicks": 9,
       "user_profile_clicks": 34
    },
    "text": "test"
  },
  "includes": {
    "media": [
      {
        "media_key": "13_1204080851740315648",
        "non_public_metrics": {
          "playback_0_count": 0,
          "playback_100_count": 1,
          "playback_25_count": 2,
          "playback_50_count": 1,
          "playback_75_count": 1
        },
        "organic_metrics": {
          "playback_0_count": 0,
          "playback_100_count": 1,
          "playback_25_count": 2,
          "playback_50_count": 1,
          "playback_75_count": 1,
          "view_count": 1
        },
        "type": "video"
      }
    ]
  }
}
```

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