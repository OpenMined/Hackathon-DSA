
POST users/report\_spam | Docs | Twitter Developer Platform 

POST users/report\_spam

post-users-report\_spam
POST users/report\_spam
=======================

Report the specified user as a spam account to Twitter. Additionally,
optionally performs the equivalent of POST
blocks / create on behalf of the authenticated user.

Resource URL¶
-------------

`https://api.twitter.com/1.1/users/report_spam.json`

Resource Information¶
---------------------

|  |  |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

Parameters¶
-----------

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| screen\_name | optional | The screen\_name of the user to report as a spammer. Helpful for
disambiguating when a valid screen name is also a user ID. |  | *noradio* |
| user\_id | optional | The ID of the user to report as a spammer. Helpful for
disambiguating when a valid user ID is also a valid screen name. |  | *12345* |
| perform\_block | optional | Whether the account should be blocked by the authenticated user, as
well as being reported for spam. | true | *false* |

Example Request¶
----------------

`POST https://api.twitter.com/1.1/users/report_spam.json?screen_name=themattharris&perform_block=false`

Example Response¶
-----------------

```
{
  "name": "Matt Harris",
  "profile_sidebar_border_color": "C0DEED",
  "profile_sidebar_fill_color": "DDEEF6",
  "profile_background_tile": false,
  "profile_image_url": "http://a0.twimg.com/profile_images/554181350/matt_normal.jpg",
  "created_at": "Sat Feb 17 20:49:54 +0000 2007",
  "location": "SFO/LHR/YVR/JAX/IAD",
  "is_translator": false,
  "follow_request_sent": false,
  "id_str": "777925",
  "profile_link_color": "0084B4",
  "entities": {
    "url": {
      "urls": [
        {
          "expanded_url": null,
          "url": "http://www.themattharris.com",
          "indices": [
            0,
            28
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
  "default_profile": true,
  "contributors_enabled": true,
  "url": "http://www.themattharris.com",
  "favourites_count": 213,
  "utc_offset": -28800,
  "id": 777925,
  "profile_image_url_https": "https://si0.twimg.com/profile_images/554181350/matt_normal.jpg",
  "profile_use_background_image": true,
  "listed_count": 303,
  "profile_text_color": "333333",
  "protected": false,
  "lang": "en",
  "followers_count": 7984,
  "time_zone": "Pacific Time (US & Canada)",
  "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme1/bg.png",
  "verified": false,
  "profile_background_color": "C0DEED",
  "notifications": false,
  "description": "Part of @twitter's Platform Services. Married to @cindyli. Kryptonite hurts me.",
  "geo_enabled": true,
  "statuses_count": 4492,
  "default_profile_image": false,
  "status": {
    "coordinates": null,
    "favorited": false,
    "created_at": "Tue Aug 28 00:11:59 +0000 2012",
    "truncated": false,
    "id_str": "240240276298420224",
    "entities": {
      "urls": [
        {
          "expanded_url": "https://twitter.com/rsarver/status/240224006807117828",
          "url": "https://t.co/DdTXEtcd",
          "indices": [
            71,
            92
          ],
          "display_url": "twitter.com/rsarver/status…"
        },
        {
          "expanded_url": "https://twitter.com/rsarver/status/240223841786404864",
          "url": "https://t.co/Pq8Sj0sl",
          "indices": [
            97,
            118
          ],
          "display_url": "twitter.com/rsarver/status…"
        }
      ],
      "hashtags": [
      ],
      "user_mentions": [
        {
          "name": "Heilemann",
          "id_str": "11656",
          "id": 11656,
          "indices": [
            1,
            11
          ],
          "screen_name": "Heilemann"
        },
        {
          "name": "Luke Dorny",
          "id_str": "12587",
          "id": 12587,
          "indices": [
            13,
            24
          ],
          "screen_name": "luxuryluke"
        },
        {
          "name": "Ryan Sarver",
          "id_str": "795649",
          "id": 795649,
          "indices": [
            27,
            35
          ],
          "screen_name": "rsarver"
        },
        {
          "name": "Jeremy Keith",
          "id_str": "11250",
          "id": 11250,
          "indices": [
            61,
            69
          ],
          "screen_name": "adactio"
        }
      ]
    },
    "in_reply_to_user_id_str": "11656",
    "text": ".@Heilemann, @luxuryluke - @rsarver has been clarifying with @adactio: https://t.co/DdTXEtcd and https://t.co/Pq8Sj0sl",
    "contributors": null,
    "retweet_count": 0,
    "id": 240240276298420224,
    "in_reply_to_status_id_str": "240226590703898624",
    "geo": null,
    "retweeted": false,
    "in_reply_to_user_id": 11656,
    "possibly_sensitive": false,
    "place": null,
    "possibly_sensitive_editable": true,
    "source": "Twitter for  iPhone",
    "in_reply_to_screen_name": "Heilemann",
    "in_reply_to_status_id": 240226590703898624
  },
  "friends_count": 430,
  "profile_background_image_url": "http://a0.twimg.com/images/themes/theme1/bg.png",
  "show_all_inline_media": false,
  "screen_name": "themattharris",
  "following": true
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