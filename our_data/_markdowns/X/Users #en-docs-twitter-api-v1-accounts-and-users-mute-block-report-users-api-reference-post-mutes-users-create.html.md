
POST mutes/users/create | Docs | Twitter Developer Platform 

POST mutes/users/create

post-mutes-users-create
POST mutes/users/create
=======================

Mutes the user specified in the ID parameter for the authenticating
user.

Returns the muted user when successful. Returns a string describing
the failure condition when unsuccessful.

Actions taken in this method are asynchronous. Changes will be
eventually consistent.

Resource URL¶
-------------

`https://api.twitter.com/1.1/mutes/users/create.json`

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
| screen\_name | optional | The screen name of the potentially muted user. Helpful for
disambiguating when a valid screen name is also a user ID. |  | *whiteleaf* |
| user\_id | optional | The ID of the potentially muted user. Helpful for disambiguating
when a valid user ID is also a valid screen name. |  | *12345* |

Example Request¶
----------------

`POST https://api.twitter.com/1.1/mutes/users/create.json?screen_name=evilpiper`

Example Response¶
-----------------

```
{
  "id": 54931584,
  "id_str": "54931584",
  "name": "Evil Piper",
  "screen_name": "evilpiper",
  "location": "",
  "description": "mwah-ha-haaaaa",
  "url": null,
  "entities": {
    "description": {
      "urls": [
      ]
    }
  },
  "protected": false,
  "followers_count": 16,
  "friends_count": 10,
  "listed_count": 0,
  "created_at": "Wed Jul 08 15:40:42 +0000 2009",
  "favourites_count": 1,
  "utc_offset": 3600,
  "time_zone": "London",
  "geo_enabled": false,
  "verified": false,
  "statuses_count": 71,
  "lang": "en",
  "status": {
    "created_at": "Tue Apr 15 00:10:23 +0000 2014",
    "id": 455860653731753984,
    "id_str": "455860653731753984",
    "text": "Super cool app to install http://t.co/ZiH6VOqLB3",
    "source": "Twitter for  iPhone",
    "truncated": false,
    "in_reply_to_status_id": null,
    "in_reply_to_status_id_str": null,
    "in_reply_to_user_id": null,
    "in_reply_to_user_id_str": null,
    "in_reply_to_screen_name": null,
    "geo": null,
    "coordinates": null,
    "place": null,
    "contributors": null,
    "retweet_count": 0,
    "favorite_count": 0,
    "entities": {
      "hashtags": [
      ],
      "symbols": [
      ],
      "urls": [
        {
          "url": "http://t.co/ZiH6VOqLB3",
          "expanded_url": "http://cards-demo.cfapps.io/owntracks.html",
          "display_url": "cards-demo.cfapps.io/owntracks.html",
          "indices": [
            26,
            48
          ]
        }
      ],
      "user_mentions": [
      ]
    },
    "favorited": false,
    "retweeted": false,
    "possibly_sensitive": false,
    "lang": "en"
  },
  "contributors_enabled": false,
  "is_translator": false,
  "is_translation_enabled": false,
  "profile_background_color": "1A1B1F",
  "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
  "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
  "profile_background_tile": false,
  "profile_image_url": "http://pbs.twimg.com/profile_images/307611594/evil_normal.png",
  "profile_image_url_https": "https://pbs.twimg.com/profile_images/307611594/evil_normal.png",
  "profile_link_color": "A6001E",
  "profile_sidebar_border_color": "181A1E",
  "profile_sidebar_fill_color": "949399",
  "profile_text_color": "120312",
  "profile_use_background_image": false,
  "default_profile": false,
  "default_profile_image": false,
  "following": true,
  "follow_request_sent": false,
  "notifications": false,
  "muting": true
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