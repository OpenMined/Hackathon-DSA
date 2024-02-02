



GET statuses/user\_timeline | Docs | Twitter Developer Platform 





































































































GET statuses/user\_timeline



get-statuses-user\_timeline

GET statuses/user\_timeline
===========================




**Important notice:** On June 19, 2019, we began
enforcing a limit of 100,000 requests per day to the
/statuses/user\_timeline endpoint, in addition to existing user-level and
app-level rate limits. This limit is applied on a per-application basis,
meaning that a single developer app can make up to 100,000 calls during
any single 24-hour period.


Returns a collection of the most recent Tweets
posted by the user
indicated by the `screen_name` or `user_id`
parameters.


User timelines belonging to protected users may only be requested
when the authenticated user either "owns" the timeline or is an approved
follower of the owner.


The timeline returned is the equivalent of the one seen as a user's
profile on Twitter.


This method can only return up to 3,200 of a user's most recent
Tweets. Native retweets of other statuses by the user is included in
this total, regardless of whether `include_rts` is set to
`false` when requesting this resource.


See Working
with Timelines for instructions on traversing timelines.


See Embedded Timelines, Embedded Tweets, and GET statuses/oembed for
tools to render Tweets according to Display
Requirements.


Resource URL¶
-------------


`https://api.twitter.com/1.1/statuses/user_timeline.json`


Resource Information¶
---------------------




|  |  |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 900 |
| Requests / 15-min window (app auth) | 1500 |
| Requests / 24-hour window | 100,000 |
| Supports Edit Tweets feature? | Yes |


*Note:* the 24-hour request limit is based on a rolling clock,
beginning at the time of the first request and monitored for the next 24
hours.


Parameters¶
-----------




|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| user\_id | optional | The ID of the user for whom to return results. |  | *12345* |
| screen\_name | optional | The screen name of the user for whom to return results. |  | *noradio* |
| since\_id | optional | Returns results with an ID greater than (that is, more recent than)
the specified ID. There are limits to the number of Tweets that can be
accessed through the API. If the limit of Tweets has occured since the
since\_id, the since\_id will be forced to the oldest ID available. |  | *12345* |
| count | optional | Specifies the number of Tweets to try and retrieve, up to a maximum
of 200 per distinct request. The value of *count* is best thought
of as a limit to the number of Tweets to return because suspended or
deleted content is removed after the count has been applied. We include
retweets in the count, even if *include\_rts* is not supplied. It
is recommended you always send *include\_rts=1* when using this
API method. |  |  |
| max\_id | optional | Returns results with an ID less than (that is, older than) or equal
to the specified ID. |  | *54321* |
| trim\_user | optional | When set to either *true* , *t* or *1* , each
Tweet returned in a timeline will include a user object including only
the status authors numerical ID. Omit this parameter to receive the
complete user object. |  | *true* |
| exclude\_replies | optional | This parameter will prevent replies from appearing in the returned
timeline. Using *exclude\_replies* with the *count*
parameter will mean you will receive up-to count tweets — this is
because the *count* parameter retrieves that many Tweets before
filtering out retweets and replies. |  | *true* |
| include\_rts | optional | When set to *false* , the timeline will strip any native
retweets (though they will still count toward both the maximal length of
the timeline and the slice selected by the count parameter). Note: If
you're using the trim\_user parameter in conjunction with include\_rts,
the retweets will still contain a full user object. |  | *false* |
| include\_ext\_edit\_control | optional | Must be set to true in order to return edited Tweet metadata as
part of the Tweet object.
`include_ext_edit_control=true` Note that historical
Tweets may not contain edited Tweet metadata.To learn more about
how edited Tweets are supported, see the Edit
Tweets fundamentals page. |  | *true* |


Example Request¶
----------------


`GET https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=twitterapi&count=2`


Example Response¶
-----------------



```
[
  {
    "created_at": "Thu Apr 06 15:28:43 +0000 2017",
    "id": 850007368138018817,
    "id_str": "850007368138018817",
    "text": "RT @TwitterDev: 1/ Today we’re sharing our vision for the future of the Twitter API platform!nhttps://t.co/XweGngmxlP",
    "truncated": false,
    "entities": {
      "hashtags": [],
      "symbols": [],
      "user_mentions": [
        {
          "screen_name": "TwitterDev",
          "name": "TwitterDev",
          "id": 2244994945,
          "id_str": "2244994945",
          "indices": [
            3,
            14
          ]
        }
      ],
      "urls": [
        {
          "url": "https://t.co/XweGngmxlP",
          "expanded_url": "https://cards.twitter.com/cards/18ce53wgo4h/3xo1c",
          "display_url": "cards.twitter.com/cards/18ce53wg…",
          "indices": [
            94,
            117
          ]
        }
      ]
    },
    "source": "<a href="http://twitter.com" rel="nofollow">Twitter Web Client</a>",
    "in_reply_to_status_id": null,
    "in_reply_to_status_id_str": null,
    "in_reply_to_user_id": null,
    "in_reply_to_user_id_str": null,
    "in_reply_to_screen_name": null,
    "user": {
      "id": 6253282,
      "id_str": "6253282",
      "name": "Twitter API",
      "screen_name": "twitterapi",
      "location": "San Francisco, CA",
      "description": "The Real Twitter API. I tweet about API changes, service issues and happily answer questions about Twitter and our API. Don't get an answer? It's on my website.",
      "url": "http://t.co/78pYTvWfJd",
      "entities": {
        "url": {
          "urls": [
            {
              "url": "http://t.co/78pYTvWfJd",
              "expanded_url": "https://dev.twitter.com",
              "display_url": "dev.twitter.com",
              "indices": [
                0,
                22
              ]
            }
          ]
        },
        "description": {
          "urls": []
        }
      },
      "protected": false,
      "followers_count": 6172353,
      "friends_count": 46,
      "listed_count": 13091,
      "created_at": "Wed May 23 06:01:13 +0000 2007",
      "favourites_count": 26,
      "utc_offset": -25200,
      "time_zone": "Pacific Time (US & Canada)",
      "geo_enabled": true,
      "verified": true,
      "statuses_count": 3583,
      "lang": "en",
      "contributors_enabled": false,
      "is_translator": false,
      "is_translation_enabled": false,
      "profile_background_color": "C0DEED",
      "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/656927849/miyt9dpjz77sc0w3d4vj.png",
      "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/656927849/miyt9dpjz77sc0w3d4vj.png",
      "profile_background_tile": true,
      "profile_image_url": "http://pbs.twimg.com/profile_images/2284174872/7df3h38zabcvjylnyfe3_normal.png",
      "profile_image_url_https": "https://pbs.twimg.com/profile_images/2284174872/7df3h38zabcvjylnyfe3_normal.png",
      "profile_banner_url": "https://pbs.twimg.com/profile_banners/6253282/1431474710",
      "profile_link_color": "0084B4",
      "profile_sidebar_border_color": "C0DEED",
      "profile_sidebar_fill_color": "DDEEF6",
      "profile_text_color": "333333",
      "profile_use_background_image": true,
      "has_extended_profile": false,
      "default_profile": false,
      "default_profile_image": false,
      "following": true,
      "follow_request_sent": false,
      "notifications": false,
      "translator_type": "regular"
    },
    "geo": null,
    "coordinates": null,
    "place": null,
    "contributors": null,
    "retweeted_status": {
      "created_at": "Thu Apr 06 15:24:15 +0000 2017",
      "id": 850006245121695744,
      "id_str": "850006245121695744",
      "text": "1/ Today we’re sharing our vision for the future of the Twitter API platform!nhttps://t.co/XweGngmxlP",
      "truncated": false,
      "entities": {
        "hashtags": [],
        "symbols": [],
        "user_mentions": [],
        "urls": [
          {
            "url": "https://t.co/XweGngmxlP",
            "expanded_url": "https://cards.twitter.com/cards/18ce53wgo4h/3xo1c",
            "display_url": "cards.twitter.com/cards/18ce53wg…",
            "indices": [
              78,
              101
            ]
          }
        ]
      },
      "source": "<a href="http://twitter.com" rel="nofollow">Twitter Web Client</a>",
      "in_reply_to_status_id": null,
      "in_reply_to_status_id_str": null,
      "in_reply_to_user_id": null,
      "in_reply_to_user_id_str": null,
      "in_reply_to_screen_name": null,
      "user": {
        "id": 2244994945,
        "id_str": "2244994945",
        "name": "TwitterDev",
        "screen_name": "TwitterDev",
        "location": "Internet",
        "description": "Your official source for Twitter Platform news, updates & events. Need technical help? Visit https://t.co/mGHnxZCxkt ⌨️  #TapIntoTwitter",
        "url": "https://t.co/66w26cua1O",
        "entities": {
          "url": {
            "urls": [
              {
                "url": "https://t.co/66w26cua1O",
                "expanded_url": "https://dev.twitter.com/",
                "display_url": "dev.twitter.com",
                "indices": [
                  0,
                  23
                ]
              }
            ]
          },
          "description": {
            "urls": [
              {
                "url": "https://t.co/mGHnxZCxkt",
                "expanded_url": "https://twittercommunity.com/",
                "display_url": "twittercommunity.com",
                "indices": [
                  93,
                  116
                ]
              }
            ]
          }
        },
        "protected": false,
        "followers_count": 465425,
        "friends_count": 1523,
        "listed_count": 1168,
        "created_at": "Sat Dec 14 04:35:55 +0000 2013",
        "favourites_count": 2098,
        "utc_offset": -25200,
        "time_zone": "Pacific Time (US & Canada)",
        "geo_enabled": true,
        "verified": true,
        "statuses_count": 3031,
        "lang": "en",
        "contributors_enabled": false,
        "is_translator": false,
        "is_translation_enabled": false,
        "profile_background_color": "FFFFFF",
        "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
        "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
        "profile_background_tile": false,
        "profile_image_url": "http://pbs.twimg.com/profile_images/530814764687949824/npQQVkq8_normal.png",
        "profile_image_url_https": "https://pbs.twimg.com/profile_images/530814764687949824/npQQVkq8_normal.png",
        "profile_banner_url": "https://pbs.twimg.com/profile_banners/2244994945/1396995246",
        "profile_link_color": "0084B4",
        "profile_sidebar_border_color": "FFFFFF",
        "profile_sidebar_fill_color": "DDEEF6",
        "profile_text_color": "333333",
        "profile_use_background_image": false,
        "has_extended_profile": false,
        "default_profile": false,
        "default_profile_image": false,
        "following": true,
        "follow_request_sent": false,
        "notifications": false,
        "translator_type": "regular"
      },
      "geo": null,
      "coordinates": null,
      "place": null,
      "contributors": null,
      "is_quote_status": false,
      "retweet_count": 284,
      "favorite_count": 399,
      "favorited": false,
      "retweeted": false,
      "possibly_sensitive": false,
      "lang": "en"
    },
    "is_quote_status": false,
    "retweet_count": 284,
    "favorite_count": 0,
    "favorited": false,
    "retweeted": false,
    "possibly_sensitive": false,
    "lang": "en"
  },
  {
    "created_at": "Mon Apr 03 16:09:50 +0000 2017",
    "id": 848930551989915648,
    "id_str": "848930551989915648",
    "text": "RT @TwitterMktg: Starting today, businesses can request and share locations when engaging with people in Direct Messages. https://t.co/rpYn…",
    "truncated": false,
    "entities": {
      "hashtags": [],
      "symbols": [],
      "user_mentions": [
        {
          "screen_name": "TwitterMktg",
          "name": "Twitter Marketing",
          "id": 357750891,
          "id_str": "357750891",
          "indices": [
            3,
            15
          ]
        }
      ],
      "urls": []
    },
    "source": "<a href="http://twitter.com" rel="nofollow">Twitter Web Client</a>",
    "in_reply_to_status_id": null,
    "in_reply_to_status_id_str": null,
    "in_reply_to_user_id": null,
    "in_reply_to_user_id_str": null,
    "in_reply_to_screen_name": null,
    "user": {
      "id": 6253282,
      "id_str": "6253282",
      "name": "Twitter API",
      "screen_name": "twitterapi",
      "location": "San Francisco, CA",
      "description": "The Real Twitter API. I tweet about API changes, service issues and happily answer questions about Twitter and our API. Don't get an answer? It's on my website.",
      "url": "http://t.co/78pYTvWfJd",
      "entities": {
        "url": {
          "urls": [
            {
              "url": "http://t.co/78pYTvWfJd",
              "expanded_url": "https://dev.twitter.com",
              "display_url": "dev.twitter.com",
              "indices": [
                0,
                22
              ]
            }
          ]
        },
        "description": {
          "urls": []
        }
      },
      "protected": false,
      "followers_count": 6172353,
      "friends_count": 46,
      "listed_count": 13091,
      "created_at": "Wed May 23 06:01:13 +0000 2007",
      "favourites_count": 26,
      "utc_offset": -25200,
      "time_zone": "Pacific Time (US & Canada)",
      "geo_enabled": true,
      "verified": true,
      "statuses_count": 3583,
      "lang": "en",
      "contributors_enabled": false,
      "is_translator": false,
      "is_translation_enabled": false,
      "profile_background_color": "C0DEED",
      "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/656927849/miyt9dpjz77sc0w3d4vj.png",
      "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/656927849/miyt9dpjz77sc0w3d4vj.png",
      "profile_background_tile": true,
      "profile_image_url": "http://pbs.twimg.com/profile_images/2284174872/7df3h38zabcvjylnyfe3_normal.png",
      "profile_image_url_https": "https://pbs.twimg.com/profile_images/2284174872/7df3h38zabcvjylnyfe3_normal.png",
      "profile_banner_url": "https://pbs.twimg.com/profile_banners/6253282/1431474710",
      "profile_link_color": "0084B4",
      "profile_sidebar_border_color": "C0DEED",
      "profile_sidebar_fill_color": "DDEEF6",
      "profile_text_color": "333333",
      "profile_use_background_image": true,
      "has_extended_profile": false,
      "default_profile": false,
      "default_profile_image": false,
      "following": true,
      "follow_request_sent": false,
      "notifications": false,
      "translator_type": "regular"
    },
    "geo": null,
    "coordinates": null,
    "place": null,
    "contributors": null,
    "retweeted_status": {
      "created_at": "Mon Apr 03 16:05:05 +0000 2017",
      "id": 848929357519241216,
      "id_str": "848929357519241216",
      "text": "Starting today, businesses can request and share locations when engaging with people in Direct Messages. https://t.co/rpYndqWfQw",
      "truncated": false,
      "entities": {
        "hashtags": [],
        "symbols": [],
        "user_mentions": [],
        "urls": [
          {
            "url": "https://t.co/rpYndqWfQw",
            "expanded_url": "https://cards.twitter.com/cards/5wzucr/3x700",
            "display_url": "cards.twitter.com/cards/5wzucr/3…",
            "indices": [
              105,
              128
            ]
          }
        ]
      },
      "source": "<a href="https://ads.twitter.com" rel="nofollow">Twitter Ads</a>",
      "in_reply_to_status_id": null,
      "in_reply_to_status_id_str": null,
      "in_reply_to_user_id": null,
      "in_reply_to_user_id_str": null,
      "in_reply_to_screen_name": null,
      "user": {
        "id": 357750891,
        "id_str": "357750891",
        "name": "Twitter Marketing",
        "screen_name": "TwitterMktg",
        "location": "Twitter HQ ",
        "description": "Twitter’s place for marketers, agencies, and creative thinkers ⭐ Bringing you insights, news, updates, and inspiration. Visit @TwitterAdsHelp for Ads support.",
        "url": "https://t.co/Tfo4moo92y",
        "entities": {
          "url": {
            "urls": [
              {
                "url": "https://t.co/Tfo4moo92y",
                "expanded_url": "https://marketing.twitter.com",
                "display_url": "marketing.twitter.com",
                "indices": [
                  0,
                  23
                ]
              }
            ]
          },
          "description": {
            "urls": []
          }
        },
        "protected": false,
        "followers_count": 924546,
        "friends_count": 661,
        "listed_count": 3893,
        "created_at": "Thu Aug 18 21:08:15 +0000 2011",
        "favourites_count": 1934,
        "utc_offset": -25200,
        "time_zone": "Pacific Time (US & Canada)",
        "geo_enabled": true,
        "verified": true,
        "statuses_count": 6329,
        "lang": "en",
        "contributors_enabled": false,
        "is_translator": false,
        "is_translation_enabled": false,
        "profile_background_color": "C0DEED",
        "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/662767273/jvmxdpdrplhxcw8yvkv2.png",
        "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/662767273/jvmxdpdrplhxcw8yvkv2.png",
        "profile_background_tile": true,
        "profile_image_url": "http://pbs.twimg.com/profile_images/800953549697888256/UlXXL5h5_normal.jpg",
        "profile_image_url_https": "https://pbs.twimg.com/profile_images/800953549697888256/UlXXL5h5_normal.jpg",
        "profile_banner_url": "https://pbs.twimg.com/profile_banners/357750891/1487188210",
        "profile_link_color": "19CF86",
        "profile_sidebar_border_color": "FFFFFF",
        "profile_sidebar_fill_color": "DDEEF6",
        "profile_text_color": "333333",
        "profile_use_background_image": true,
        "has_extended_profile": false,
        "default_profile": false,
        "default_profile_image": false,
        "following": false,
        "follow_request_sent": false,
        "notifications": false,
        "translator_type": "none"
      },
      "geo": null,
      "coordinates": null,
      "place": null,
      "contributors": null,
      "is_quote_status": false,
      "retweet_count": 111,
      "favorite_count": 162,
      "favorited": false,
      "retweeted": false,
      "possibly_sensitive": false,
      "lang": "en"
    },
    "is_quote_status": false,
    "retweet_count": 111,
    "favorite_count": 0,
    "favorited": false,
    "retweeted": false,
    "lang": "en"
  }
]
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















