
POST statuses/destroy/:id | Docs | Twitter Developer Platform 

POST statuses/destroy/:id

post-statuses-destroy-id
POST statuses/destroy/:id
=========================

Destroys the status specified by the required ID parameter. The
authenticating user must be the author of the specified status. Returns
the destroyed status if successful.

Resource URL¶
-------------

`https://api.twitter.com/1.1/statuses/destroy/:id.json`

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
| id | required | The numerical ID of the desired status. |  | *123* |
| trim\_user | optional | When set to either *true* , *t* or *1* , each
tweet returned in a timeline will include a user object including only
the status authors numerical ID. Omit this parameter to receive the
complete user object. |  | *true* |

Example Request¶
----------------

`POST https://api.twitter.com/1.1/statuses/destroy/240854986559455234.json`

Example Response¶
-----------------

```
{
  "coordinates": null,
  "favorited": false,
  "created_at": "Wed Aug 29 16:54:38 +0000 2012",
  "truncated": false,
  "id_str": "240854986559455234",
  "entities": {
    "urls": [
      {
        "expanded_url": "http://venturebeat.com/2012/08/29/vimeo-dropbox/#.UD5JLsYptSs.twitter",
        "url": "http://t.co/7UlkvZzM",
        "indices": [
          69,
          89
        ],
        "display_url": "venturebeat.com/2012/08/29/vim…"
      }
    ],
    "hashtags": [
    ],
    "user_mentions": [
    ]
  },
  "in_reply_to_user_id_str": null,
  "text": ""Vimeo integrates with Dropbox for easier video uploads and shares": http://t.co/7UlkvZzM",
  "contributors": null,
  "retweet_count": 1,
  "id": 240854986559455234,
  "in_reply_to_status_id_str": null,
  "geo": null,
  "retweeted": false,
  "in_reply_to_user_id": null,
  "possibly_sensitive": false,
  "place": null,
  "user": {
    "name": "Jason Costa",
    "profile_sidebar_border_color": "86A4A6",
    "profile_sidebar_fill_color": "A0C5C7",
    "profile_background_tile": false,
    "profile_image_url": "http://a0.twimg.com/profile_images/1751674923/new_york_beard_normal.jpg",
    "created_at": "Wed May 28 00:20:15 +0000 2008",
    "location": "",
    "is_translator": true,
    "follow_request_sent": false,
    "id_str": "14927800",
    "profile_link_color": "FF3300",
    "entities": {
      "url": {
        "urls": [
          {
            "expanded_url": "http://www.jason-costa.blogspot.com/",
            "url": "http://t.co/YCA3ZKY",
            "indices": [
              0,
              19
            ],
            "display_url": "jason-costa.blogspot.com"
          }
        ]
      },
      "description": {
        "urls": [
        ]
      }
    },
    "default_profile": false,
    "contributors_enabled": false,
    "url": "http://t.co/YCA3ZKY",
    "favourites_count": 883,
    "utc_offset": -28800,
    "id": 14927800,
    "profile_image_url_https": "https://si0.twimg.com/profile_images/1751674923/new_york_beard_normal.jpg",
    "profile_use_background_image": true,
    "listed_count": 150,
    "profile_text_color": "333333",
    "protected": false,
    "lang": "en",
    "followers_count": 8760,
    "time_zone": "Pacific Time (US & Canada)",
    "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme6/bg.gif",
    "verified": false,
    "profile_background_color": "709397",
    "notifications": false,
    "description": "Platform at Twitter",
    "geo_enabled": true,
    "statuses_count": 5531,
    "default_profile_image": false,
    "friends_count": 166,
    "profile_background_image_url": "http://a0.twimg.com/images/themes/theme6/bg.gif",
    "show_all_inline_media": true,
    "screen_name": "jasoncosta",
    "following": false
  },
  "possibly_sensitive_editable": true,
  "source": "Tweet Button",
  "in_reply_to_screen_name": null,
  "in_reply_to_status_id": null
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