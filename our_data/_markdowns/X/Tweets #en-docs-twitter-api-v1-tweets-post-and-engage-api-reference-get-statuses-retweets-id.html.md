
GET statuses/retweets/:id | Docs | Twitter Developer Platform 

GET statuses/retweets/:id

get-statuses-retweets-id
GET statuses/retweets/:id
=========================

Returns a collection of the 100 most recent retweets of the Tweet
specified by the `id` parameter.

Resource URL¶
-------------

`https://api.twitter.com/1.1/statuses/retweets/:id.json`

Resource Information¶
---------------------

|  |  |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 75 |
| Requests / 15-min window (app auth) | 300 |

Parameters¶
-----------

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| id | required | The numerical ID of the desired status. |  | *123* |
| count | optional | Specifies the number of records to retrieve. Must be less than or
equal to 100. |  | *5* |
| trim\_user | optional | When set to either *true* , *t* or *1* , each
tweet returned in a timeline will include a user object including only
the status authors numerical ID. Omit this parameter to receive the
complete user object. |  | *true* |
| include\_ext\_edit\_control | optional | Must be set to true in order to return edited Tweet metadata as
part of the Tweet object.
`include_ext_edit_control=true` Note that historical
Tweets may not contain edited Tweet metadata. |  | *true* |

Example Request¶
----------------

`GET https://api.twitter.com/1.1/statuses/retweets/1128692733353218048.json`

Example Response¶
-----------------

```
[
  {
    "created_at": "Wed May 15 16:04:52 +0000 2019",
    "id": 1128692733353218048,
    "id_str": "1128692733353218048",
    "text": "RT @jack: just setting up my twttr",
    "truncated": false,
    "entities": {
      "hashtags": [],
      "symbols": [],
      "user_mentions": [
        {
          "screen_name": "jack",
          "name": "jack",
          "id": 12,
          "id_str": "12",
          "indices": [
            3,
            8
          ]
        }
      ],
      "urls": []
    },
    "source": "<a href="https://mobile.twitter.com" rel="nofollow">Twitter Web App</a>",
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
      "followers_count": 6128663,
      "friends_count": 12,
      "listed_count": 12900,
      "created_at": "Wed May 23 06:01:13 +0000 2007",
      "favourites_count": 32,
      "utc_offset": null,
      "time_zone": null,
      "geo_enabled": null,
      "verified": true,
      "statuses_count": 3659,
      "lang": "null",
      "contributors_enabled": null,
      "is_translator": null,
      "is_translation_enabled": null,
      "profile_background_color": "null",
      "profile_background_image_url": "null",
      "profile_background_image_url_https": "null",
      "profile_background_tile": nulll,
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
    "retweet_count": 161,
    "favorite_count": 296,
    "favorited": false,
    "retweeted": false,
    "possibly_sensitive": false,
    "possibly_sensitive_appealable": false,
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