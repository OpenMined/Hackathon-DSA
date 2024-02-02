
GET lists/members/show | Docs | Twitter Developer Platform 

GET lists/members/show

get-lists-members-show
GET lists/members/show
======================

Check if the specified user is a member of the specified list.

Resource URL¶
-------------

`https://api.twitter.com/1.1/lists/members/show.json`

Resource Information¶
---------------------

|  |  |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 15 |
| Requests / 15-min window (app auth) | 15 |

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
| user\_id | required | The ID of the user for whom to return results. Helpful for
disambiguating when a valid user ID is also a valid screen name. |  |  |
| screen\_name | required | The screen name of the user for whom to return results. Helpful for
disambiguating when a valid screen name is also a user ID. |  |  |
| owner\_screen\_name | optional | The screen name of the user who owns the list being requested by a
*slug*. |  |  |
| owner\_id | optional | The user ID of the user who owns the list being requested by a
*slug*. |  |  |
| include\_entities | optional | When set to either *true*, *t* or *1*, each
tweet will include a node called "entities". This node offers a variety
of metadata about the tweet in a discreet structure, including:
user\_mentions, urls, and hashtags. While entities are opt-in on
timelines at present, they will be made a default component of output in
the future. See Tweet Entities for
more details. |  |  |
| skip\_status | optional | When set to either *true*, *t* or *1* statuses
will not be included in the returned user objects. |  |  |

Example Request¶
----------------

`GET https://api.twitter.com/1.1/lists/members/show.json?slug=team&owner_screen_name=twitter&screen_name=froginthevalley`

Example Response¶
-----------------

```
{
  "id": "657693",
  "id_str": "657693",
  "is_translator": false,
  "default_profile": false,
  "entities": {
    "url": {
      "urls": [
        {
          "url": "http://t.co/jtb0IaGT",
          "indices": [
            0,
            20
          ],
          "display_url": "afroginthevalley.com",
          "expanded_url": "http://afroginthevalley.com/"
        }
      ]
    },
    "description": {
      "urls": []
    }
  },
  "show_all_inline_media": false,
  "profile_use_background_image": false,
  "profile_text_color": "999999",
  "utc_offset": -18000,
  "listed_count": 302,
  "name": "Sylvain Carle",
  "notifications": false,
  "profile_sidebar_border_color": "87CB00",
  "geo_enabled": true,
  "follow_request_sent": false,
  "url": "http://t.co/jtb0IaGT",
  "lang": "en",
  "profile_image_url_https": "https://si0.twimg.com/profile_images/1532782858/sylvaincarle-2011-profile-480_normal.png",
  "created_at": "Thu Jan 18 00:10:45 +0000 2007",
  "protected": false,
  "followers_count": 4281,
  "profile_background_image_url_https": "https://si0.twimg.com/profile_background_images/228591248/bg-14.png",
  "screen_name": "froginthevalley",
  "profile_background_tile": true,
  "friends_count": 2367,
  "profile_sidebar_fill_color": "333333",
  "description": "Developer Advocate at Twitter. Internet, opensource, media & geo/local geek. See also @sylvaincarle for LANG=FR.",
  "time_zone": "Eastern Time (US & Canada)",
  "default_profile_image": false,
  "location": "San Francisco",
  "profile_image_url": "http://a0.twimg.com/profile_images/1532782858/sylvaincarle-2011-profile-480_normal.png",
  "favourites_count": 1790,
  "following": false,
  "profile_background_color": "000000",
  "verified": false,
  "statuses_count": 8191,
  "status": {
    "entities": {
      "urls": [
        {
          "url": "http://t.co/GtBxX0IW",
          "indices": [
            54,
            74
          ],
          "display_url": "example.com",
          "expanded_url": "http://www.example.com"
        },
        {
          "url": "http://t.co/2E5hDjME",
          "indices": [
            94,
            114
          ],
          "display_url": "example.com",
          "expanded_url": "http://example.com"
        }
      ],
      "hashtags": [],
      "user_mentions": [
        {
          "name": "VO5",
          "indices": [
            0,
            6
          ],
          "screen_name": "MyVO5",
          "id": "485879570",
          "id_str": "485879570"
        }
      ]
    },
    "geo": null,
    "place": null,
    "in_reply_to_screen_name": "MyVO5",
    "in_reply_to_user_id": 485879570,
    "retweeted": false,
    "in_reply_to_status_id": 243404113679888400,
    "created_at": "Wed Sep 05 17:45:14 +0000 2012",
    "possibly_sensitive": false,
    "in_reply_to_status_id_str": "243404113679888385",
    "contributors": null,
    "favorited": false,
    "source": "YoruFukurou",
    "in_reply_to_user_id_str": "485879570",
    "retweet_count": 0,
    "id": "< Unable to parse in Javascript >",
    "id_str": "243404435752099841",
    "coordinates": null,
    "truncated": false,
    "text": "@MyVO5 make sure you configure your domain correctly, http://t.co/GtBxX0IW is not the same as http://t.co/2E5hDjME (also, refresh cache)."
  },
  "contributors_enabled": false,
  "profile_background_image_url": "http://a0.twimg.com/profile_background_images/228591248/bg-14.png",
  "profile_link_color": "009DFF"
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