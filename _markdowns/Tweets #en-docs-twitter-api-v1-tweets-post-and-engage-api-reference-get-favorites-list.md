



GET favorites/list | Docs | Twitter Developer Platform 





































































































GET favorites/list



get-favorites-list

GET favorites/list
==================




Note: favorites are now known as *likes*.


Returns the 20 most recent Tweets liked by the authenticating or
specified user.


Resource URL¶
-------------


`https://api.twitter.com/1.1/favorites/list.json`


Resource Information¶
---------------------




|  |  |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 75 |
| Requests / 15-min window (app auth) | 75 |


Parameters¶
-----------




|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| user\_id | optional | The ID of the user for whom to return results. |  | *12345* |
| screen\_name | optional | The screen name of the user for whom to return results. |  | *twitterdev* |
| count | optional | Specifies the number of records to retrieve. Must be less than or
equal to 200; defaults to 20. The value of count is best thought of as a
limit to the number of Tweets to return because suspended or deleted
content is removed after the count has been applied. |  | *5* |
| since\_id | optional | Returns results with an ID greater than (that is, more recent than)
the specified ID. There are limits to the number of Tweets which can be
accessed through the API. If the limit of Tweets has occured since the
since\_id, the since\_id will be forced to the oldest ID available. |  | *12345* |
| max\_id | optional | Returns results with an ID less than (that is, older than) or equal
to the specified ID. |  | *54321* |
| include\_entities | optional | The *entities* node will be omitted when set to
*false* . |  | *false* |
| include\_ext\_edit\_control | optional | Must be set to true in order to return edited Tweet metadata as
part of the Tweet object.
`include_ext_edit_control=true` Note that historical
Tweets may not contain edited Tweet metadata. |  | *true* |


Example Request¶
----------------


`GET https://api.twitter.com/1.1/favorites/list.json?count=200&screen_name=twitterdev`


Example Response¶
-----------------



```
[
  {
    "created_at": "Tue May 14 17:58:31 +0000 2019",
    "id": 1128358947772145672,
    "id_str": "1128358947772145672",
    "text": "Through the Twitter Developer Labs program, we'll soon preview new versions of GET /tweets and GET /users, followed… https://t.co/9i4c5bUUCu",
    "truncated": true,
    "entities": {
      "hashtags": [],
      "symbols": [],
      "user_mentions": [],
      "urls": [
        {
          "url": "https://t.co/9i4c5bUUCu",
          "expanded_url": "https://twitter.com/i/web/status/1128358947772145672",
          "display_url": "twitter.com/i/web/status/1…",
          "indices": [
            117,
            140
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
      "screen_name": "TwitterAPI",
      "location": "San Francisco, CA",
      "description": "The Real Twitter API. Tweets about API changes, service issues and our Developer Platform. Don't get an answer? It's on my website.",
      "url": "https://t.co/8IkCzCDr19",
      "entities": {
        "url": {
          "urls": [
            {
              "url": "https://t.co/8IkCzCDr19",
              "expanded_url": "https://developer.twitter.com",
              "display_url": "developer.twitter.com",
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
      "followers_count": 6125649,
      "friends_count": 12,
      "listed_count": 12902,
      "created_at": "Wed May 23 06:01:13 +0000 2007",
      "favourites_count": 31,
      "utc_offset": null,
      "time_zone": null,
      "geo_enabled": null,
      "verified": true,
      "statuses_count": 3664,
      "lang": null,
      "contributors_enabled": null,
      "is_translator": null,
      "is_translation_enabled": null,
      "profile_background_color": "null",
      "profile_background_image_url": "null",
      "profile_background_image_url_https": "null",
      "profile_background_tile": null,
      "profile_image_url": "null",
      "profile_image_url_https": "https://pbs.twimg.com/profile_images/942858479592554497/BbazLO9L_normal.jpg",
      "profile_banner_url": "null",
      "profile_link_color": "null",
      "profile_sidebar_border_color": "null",
      "profile_sidebar_fill_color": "null",
      "profile_text_color": "null",
      "profile_use_background_image": null,
      "has_extended_profile": null,
      "default_profile": false,
      "default_profile_image": false,
      "following": null,
      "follow_request_sent": null,
      "notifications": null,
      "translator_type": "null"
    },
    "geo": null,
    "coordinates": null,
    "place": null,
    "contributors": null,
    "is_quote_status": true,
    "quoted_status_id": 1128357926823976960,
    "quoted_status_id_str": "1128357926823976960",
    "quoted_status": {
      "created_at": "Tue May 14 17:54:28 +0000 2019",
      "id": 1128357926823976960,
      "id_str": "1128357926823976960",
      "text": "📣We’re launching Twitter Developer Labs in the coming weeks so we can build the future of our API together with tho… https://t.co/OVUiDiZqep",
      "truncated": true,
      "entities": {
        "hashtags": [],
        "symbols": [],
        "user_mentions": [],
        "urls": [
          {
            "url": "https://t.co/OVUiDiZqep",
            "expanded_url": "https://twitter.com/i/web/status/1128357926823976960",
            "display_url": "twitter.com/i/web/status/1…",
            "indices": [
              117,
              140
            ]
          }
        ]
      },
      "source": "<a href="https://mobile.twitter.com" rel="nofollow">Twitter Web App</a>",
      "in_reply_to_status_id": null,
      "in_reply_to_status_id_str": null,
      "in_reply_to_user_id": null,
      "in_reply_to_user_id_str": null,
      "in_reply_to_screen_name": null,
      "user": {
        "id": 2244994945,
        "id_str": "2244994945",
        "name": "Twitter Dev",
        "screen_name": "TwitterDev",
        "location": "Internet",
        "description": "Your official source for Twitter Platform news, updates & events. Need technical help? Visit https://t.co/mGHnxZU8c1 ⌨️ #TapIntoTwitter",
        "url": "https://t.co/FGl7VOULyL",
        "entities": {
          "url": {
            "urls": [
              {
                "url": "https://t.co/FGl7VOULyL",
                "expanded_url": "https://developer.twitter.com/",
                "display_url": "developer.twitter.com",
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
                "url": "https://t.co/mGHnxZU8c1",
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
        "followers_count": 502258,
        "friends_count": 1475,
        "listed_count": 1519,
        "created_at": "Sat Dec 14 04:35:55 +0000 2013",
        "favourites_count": 2205,
        "utc_offset": null,
        "time_zone": null,
        "geo_enabled": null,
        "verified": true,
        "statuses_count": 3664,
        "lang": null,
        "contributors_enabled": null,
        "is_translator": null,
        "is_translation_enabled": null,
        "profile_background_color": "null",
        "profile_background_image_url": "null",
        "profile_background_image_url_https": "null",
        "profile_background_tile": null,
        "profile_image_url": "null",
        "profile_image_url_https": "https://pbs.twimg.com/profile_images/942858479592554497/BbazLO9L_normal.jpg",
        "profile_banner_url": "https://pbs.twimg.com/profile_banners/6253282/1497491515",
        "profile_link_color": "null",
        "profile_sidebar_border_color": "null",
        "profile_sidebar_fill_color": "null",
        "profile_text_color": "null",
        "profile_use_background_image": null,
        "has_extended_profile": null,
        "default_profile": false,
        "default_profile_image": false,
        "following": null,
        "follow_request_sent": null,
        "notifications": null,
        "translator_type": "null"
        },
      "geo": null,
      "coordinates": null,
      "place": null,
      "contributors": null,
      "is_quote_status": false,
      "retweet_count": 169,
      "favorite_count": 350,
      "favorited": false,
      "retweeted": false,
      "possibly_sensitive": false,
      "lang": "en"
    },
    "retweet_count": 35,
    "favorite_count": 74,
    "favorited": false,
    "retweeted": false,
    "possibly_sensitive": false,
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















