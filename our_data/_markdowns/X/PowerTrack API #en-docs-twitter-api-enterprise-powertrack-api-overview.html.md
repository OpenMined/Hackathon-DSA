
PowerTrack API | Twitter API | Docs | Twitter Developer Platform 

Overview

This endpoint has been updated to include Tweet edit metadata. Learn more about these metadata on the "Edit Tweets" fundamentals page. 

Overview
========

Enterprise

*This is an enterprise API available within our managed access levels only. To use this API, you must first set up an account with our enterprise sales team. Learn more*  

*You can view all of the Twitter API filtered stream offerings HERE.*

The PowerTrack API provides customers with the ability to filter the full Twitter firehose, and only receive the data that they or their customers are interested in. This is accomplished by applying the PowerTrack filtering language - see Rules and filtering - to match Tweets based on a wide variety of attributes, including user attributes, geo-location, language, and many others. Using PowerTrack rules to filter Tweet ensures that customers receive all of the data, and *only* the data they need for your app.  

### Core components

The PowerTrack API consists of two endpoints:

#### Rules endpoint

A separate endpoint managed independently by your application, the rules endpoint supports GET, POST, POST \_method=delete and rule validation methods with basic authentication for managing your ruleset. It can support thousands of rules that allow you to filter the realtime stream of data for the topics and conversations that you care about. The rules endpoint can be accessed, managed, and will persist regardless of your connection status to the stream - you can also update (add/remove) rules while connected to the stream and the changes will take effect almost immediately.

#### Stream endpoint

Connecting to the streaming endpoint consists of a simple GET request using basic authentication. Once a connection is established, data is delivered in JSON format (see sample payload below) through a persistent HTTP Streaming connection. You will only receive data matching your rules while connected to the stream.

#### Rule tags

A single PowerTrack stream can support thousands of rules, so being able to discern which rule(s) matched a given Tweet becomes important. This is easily solved by using rule tags. Upon rule creation, you can assign a tag value which will be returned in the matching\_rules object (see here) of the response payload.

Rule tags can represent an end customer use case, a topic or conversation, or another helpful identifier that you can use to route incoming Tweets accordingly.

If, in addition to realtime data, your product also requires instant access to recent data, we recommend using our Search API.  

### Available operators

The PowerTrack API currently supports the following operators:  

* keyword
* emoji
* "exact phrase match"
* "keyword1 keyword2"~N
* contains:
* from:
* to:
* url:
* url\_title:
* url\_description:
* url\_contains:
* has:links
* sample:
* #
* point\_radius:[lon lat radius]
* bounding\_box:[west\_long south\_lat east\_long north\_lat]
* @
* $
* bio:
* bio\_name:
* retweets\_of:
* lang:
* bio\_location:
* statuses\_count:
* followers\_count:
* friends\_count:
* listed\_count:
* is:verified
* source:
* place:
* place\_country:
* has:geo
* has:mentions
* has:hashtags
* has:images
* has:videos
* has:media
* has:symbols
* is:retweet
* is:reply
* is:quote
* retweets\_of\_status\_id:
* in\_reply\_to\_status\_id:
* has:profile\_geo
* profile\_point\_radius:[long lat radius]
* profile\_bounding\_box:[west\_long south\_lat east\_long north\_lat]
* profile\_country:
* profile\_region:
* profile\_locality:
* profile\_subregion:

For more details, please see the Getting started with enterprise rules guide.  

### Sample payload

Below is a sample payload from the PowerTrack API in Native Enriched format:

```
      {
  "created_at": "Wed Oct 10 20:19:24 +0000 2018",
  "id": 1050118621198921700,
  "id_str": "1050118621198921728",
  "text": "To make room for more expression, we will now count all emojis as equal—including those with gender‍‍‍ ‍‍and skin t… https://t.co/MkGjXf9aXm",
  "source": "<a href=\"http://twitter.com\" rel=\"nofollow\">Twitter Web Client</a>",
  "truncated": true,
  "in_reply_to_status_id": null,
  "in_reply_to_status_id_str": null,
  "in_reply_to_user_id": null,
  "in_reply_to_user_id_str": null,
  "in_reply_to_screen_name": null,
  "user": {
    "id": 6253282,
    "id_str": "6253282",
    "name": "Twitter API",
    "screen_name": "TwitterAPI",
    "location": "San Francisco, CA",
    "url": "https://developer.twitter.com",
    "description": "The Real Twitter API. Tweets about API changes, service issues and our Developer Platform. Don't get an answer? It's on my website.",
    "translator_type": "null",
    "derived": {
      "locations": [
        {
          "country": "United States",
          "country_code": "US",
          "locality": "San Francisco",
          "region": "California",
          "sub_region": "San Francisco County",
          "full_name": "San Francisco, California, United States",
          "geo": {
            "coordinates": [
              -122.41942,
              37.77493
            ],
            "type": "point"
          }
        }
      ]
    },
    "protected": false,
    "verified": true,
    "followers_count": 6172196,
    "friends_count": 12,
    "listed_count": 13003,
    "favourites_count": 31,
    "statuses_count": 3650,
    "created_at": "Wed May 23 06:01:13 +0000 2007",
    "utc_offset": null,
    "time_zone": null,
    "geo_enabled": false,
    "lang": "en",
    "contributors_enabled": false,
    "is_translator": null,
    "profile_background_color": "null",
    "profile_background_image_url": "null",
    "profile_background_image_url_https": "null",
    "profile_background_tile": null,
    "profile_link_color": "null",
    "profile_sidebar_border_color": "null",
    "profile_sidebar_fill_color": "null",
    "profile_text_color": "null",
    "profile_use_background_image": null,
    "profile_image_url": "null",
    "profile_image_url_https": "https://pbs.twimg.com/profile_images/942858479592554497/BbazLO9L_normal.jpg",
    "profile_banner_url": "https://pbs.twimg.com/profile_banners/6253282/1497491515",
    "default_profile": false,
    "default_profile_image": false,
    "following": null,
    "follow_request_sent": null,
    "notifications": null
  },
  "geo": null,
  "coordinates": null,
  "place": null,
  "contributors": null,
  "is_quote_status": false,
  "extended_tweet": {
    "full_text": "To make room for more expression, we will now count all emojis as equal—including those with gender‍‍‍ ‍‍and skin tone modifiers 👍🏻👍🏽👍🏿. This is now reflected in Twitter-Text, our Open Source library. \n\nUsing Twitter-Text? See the forum post for detail: https://t.co/Nx1XZmRCXA",
    "display_text_range": [
      0,
      277
    ],
    "entities": {
      "hashtags": [],
      "urls": [
        {
          "url": "https://t.co/Nx1XZmRCXA",
          "expanded_url": "https://twittercommunity.com/t/new-update-to-the-twitter-text-library-emoji-character-count/114607",
          "display_url": "twittercommunity.com/t/new-update-t…",
          "unwound": {
            "url": "https://twittercommunity.com/t/new-update-to-the-twitter-text-library-emoji-character-count/114607",
            "status": 200,
            "title": "New update to the Twitter-Text library: Emoji character count",
            "description": "Over the years, we have made several updates to the way that people can communicate on Twitter. One of the more notable changes made last year was to increase the number of characters per Tweet from 140 to 280 characters. Today, we continue to expand people’s ability to express themselves by announcing a change to the way that we count emojis. Due to the differences in the way written text and emojis are encoded, many emojis (including emojis where you can apply gender and skin tone) have count..."
          },
          "indices": [
            254,
            277
          ]
        }
      ],
      "user_mentions": [],
      "symbols": []
    }
  },
  "quote_count": 0,
  "reply_count": 0,
  "retweet_count": 0,
  "favorite_count": 0,
  "entities": {
    "hashtags": [],
    "urls": [
      {
        "url": "https://t.co/MkGjXf9aXm",
        "expanded_url": "https://twitter.com/i/web/status/1050118621198921728",
        "display_url": "twitter.com/i/web/status/1…",
        "indices": [
          117,
          140
        ]
      }
    ],
    "user_mentions": [],
    "symbols": []
  },
  "favorited": false,
  "retweeted": false,
  "possibly_sensitive": false,
  "filter_level": "low",
  "lang": "en",
  "timestamp_ms": "1539202764211",
  "matching_rules": [
    {
      "tag": null,
      "id": 1128017341835464700,
      "id_str": "1128017341835464704"
    }
  ]
}
}
```

Next steps
-----------

Continue to the realtime PowerTrack API reference

See code examples: 

* See simple scripts in several languages to help get started
* Build a trends dashboard with Twitter API Toolkit for Google Cloud
* See an example Java client libraries: Hosebird Client adapted for enterprise streams, Gnip4J
* See an example Python client library

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