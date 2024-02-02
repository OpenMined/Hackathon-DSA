
GET lists/statuses | Docs | Twitter Developer Platform 

GET lists/statuses

get-lists-statuses
GET lists/statuses
==================

Returns a timeline of tweets authored by members of the specified
list. Retweets are included by default. Use the
`include_rts=false` parameter to omit retweets.

Embedded Timelines is a great
way to embed list timelines on your website.

Resource URL¶
-------------

`https://api.twitter.com/1.1/lists/statuses.json`

Resource Information¶
---------------------

|  |  |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 900 |
| Requests / 15-min window (app auth) | 900 |

Parameters¶
-----------

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| list\_id | required | The numerical *id* of the list. |  |  |
| slug | required | You can identify a list by its slug instead of its numerical id. If
you decide to do so, note that you'll also have to specify the list
owner using the *owner\_id* or *owner\_screen\_name*
parameters. |  |  |
| owner\_screen\_name | optional | The screen name of the user who owns the list being requested by a
*slug* . |  |  |
| owner\_id | optional | The user ID of the user who owns the list being requested by a
*slug* . |  |  |
| since\_id | optional | Returns results with an ID greater than (that is, more recent than)
the specified ID. There are limits to the number of Tweets which can be
accessed through the API. If the limit of Tweets has occured since the
since\_id, the since\_id will be forced to the oldest ID available. |  |  |
| max\_id | optional | Returns results with an ID less than (that is, older than) or equal
to the specified ID. |  |  |
| count | optional | Specifies the number of results to retrieve per "page." |  |  |
| include\_entities | optional | Entities are ON by default in API 1.1, each tweet includes a node
called "entities". This node offers a variety of metadata about the
tweet in a discreet structure, including: user\_mentions, urls, and
hashtags. You can omit entities from the result by using
*include\_entities=false* |  |  |
| include\_rts | optional | When set to either *true* , *t* or *1* , the
list timeline will contain native retweets (if they exist) in addition
to the standard stream of tweets. The output format of retweeted tweets
is identical to the representation you see in home\_timeline. |  |  |

Example Request¶
----------------

`GET https://api.twitter.com/1.1/lists/statuses.json?slug=teams&owner_screen_name=MLS&count=1`

Example Response¶
-----------------

```
[
  {
    "coordinates": null,
    "created_at": "Mon Sep 10 14:04:58 +0000 2012",
    "truncated": false,
    "favorited": false,
    "id_str": "245160944223793152",
    "in_reply_to_user_id_str": null,
    "entities": {
      "urls": [
        {
          "expanded_url": "http://bit.ly/MuCCDo",
          "url": "http://t.co/W2tON3OK",
          "indices": [
            41,
            61
          ],
          "display_url": "bit.ly/MuCCDo"
        }
      ],
      "hashtags": [
        {
          "text": "TorontoFC",
          "indices": [
            87,
            97
          ]
        },
        {
          "text": "MLS",
          "indices": [
            98,
            102
          ]
        }
      ],
      "user_mentions": [
        {
          "name": "Team Up Foundation",
          "id_str": "210844741",
          "id": 210844741,
          "indices": [
            76,
            86
          ],
          "screen_name": "TeamUpFdn"
        }
      ]
    },
    "text": "Create your own TFC ESQ by Movado Watch: http://t.co/W2tON3OK in support of @TeamUpFdn #TorontoFC #MLS",
    "contributors": null,
    "id": 245160944223793152,
    "retweet_count": 0,
    "in_reply_to_status_id_str": null,
    "geo": null,
    "retweeted": false,
    "possibly_sensitive": false,
    "in_reply_to_user_id": null,
    "in_reply_to_screen_name": null,
    "source": "TweetDeck",
    "user": {
      "profile_sidebar_fill_color": "EB1D31",
      "profile_background_tile": false,
      "profile_sidebar_border_color": "FFFFFF",
      "name": "Toronto FC",
      "profile_image_url": "http://a0.twimg.com/profile_images/1827235104/TorontoFC1_normal.jpg",
      "created_at": "Fri Sep 11 15:42:26 +0000 2009",
      "location": "Toronto, ON",
      "follow_request_sent": false,
      "is_translator": false,
      "id_str": "73412535",
      "profile_link_color": "000000",
      "entities": {
        "url": {
          "urls": [
            {
              "expanded_url": null,
              "url": "http://www.torontofc.ca",
              "indices": [
                0,
                23
              ],
              "display_url": null
            }
          ]
        },
        "description": {
          "urls": [
          ]
        }
      },
      "favourites_count": 2,
      "url": "http://www.torontofc.ca",
      "default_profile": false,
      "contributors_enabled": false,
      "profile_image_url_https": "https://si0.twimg.com/profile_images/1827235104/TorontoFC1_normal.jpg",
      "utc_offset": -18000,
      "id": 73412535,
      "listed_count": 1078,
      "profile_use_background_image": true,
      "followers_count": 28281,
      "protected": false,
      "profile_text_color": "000000",
      "lang": "en",
      "profile_background_color": "BC1228",
      "verified": true,
      "time_zone": "Eastern Time (US & Canada)",
      "profile_background_image_url_https": "https://si0.twimg.com/profile_background_images/603424485/k9py0fm18qrjr8l22qlp.jpeg",
      "notifications": false,
      "description": "Official Toronto FC Twitter by @AsifinToronto & @JonSinden. Follow us for the latest club news, links, pics & videos. Join us during matches for #TFClive",
      "geo_enabled": false,
      "default_profile_image": false,
      "friends_count": 13947,
      "profile_background_image_url": "http://a0.twimg.com/profile_background_images/603424485/k9py0fm18qrjr8l22qlp.jpeg",
      "statuses_count": 10774,
      "screen_name": "torontofc",
      "following": true,
      "show_all_inline_media": false
    },
    "place": null,
    "in_reply_to_status_id": null
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