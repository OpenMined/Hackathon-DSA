
GET lists/list | Docs | Twitter Developer Platform 

GET lists/list

get-lists-list
GET lists/list
==============

Returns all lists the authenticating or specified user subscribes to,
including their own. The user is specified using the
`user_id` or `screen_name` parameters. If no user
is given, the authenticating user is used.

A maximum of 100 results will be returned by this call. Subscribed
lists are returned first, followed by owned lists. This means that if a
user subscribes to 90 lists and owns 20 lists, this method returns 90
subscriptions and 10 owned lists. The `reverse` method
returns owned lists first, so with `reverse=true`, 20 owned
lists and 80 subscriptions would be returned. If your goal is to obtain
every list a user owns or subscribes to, use GET lists / ownerships
and/or GET lists /
subscriptions instead.

Resource URL¶
-------------

`https://api.twitter.com/1.1/lists/list.json`

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
| user\_id | optional | The ID of the user for whom to return results. Helpful for
disambiguating when a valid user ID is also a valid screen name.
**Note:** : Specifies the ID of the user to get lists from.
Helpful for disambiguating when a valid user ID is also a valid screen
name. |  | *12345* |
| screen\_name | optional | The screen name of the user for whom to return results. Helpful for
disambiguating when a valid screen name is also a user ID. |  | *noradio* |
| reverse | optional | Set this to *true* if you would like owned lists to be
returned first. See description above for information on how this
parameter works. |  | *true* |

Example Request¶
----------------

`GET https://api.twitter.com/1.1/lists/list.json?screen_name=twitterapi`

Example Response¶
-----------------

```
[
  {
    "slug": "meetup-20100301",
    "name": "meetup-20100301",
    "created_at": "Sat Feb 27 21:39:24 +0000 2010",
    "uri": "/twitterapi/meetup-20100301",
    "subscriber_count": 147,
    "id_str": "8044403",
    "member_count": 116,
    "mode": "public",
    "id": 8044403,
    "full_name": "@twitterapi/meetup-20100301",
    "description": "Guests attending the Twitter meetup on 1 March 2010 at the @twoffice",
    "user": {
      "profile_background_tile": true,
      "profile_sidebar_border_color": "C0DEED",
      "name": "Twitter API",
      "profile_sidebar_fill_color": "DDEEF6",
      "location": "San Francisco, CA",
      "created_at": "Wed May 23 06:01:13 +0000 2007",
      "profile_image_url": "http://a0.twimg.com/profile_images/2284174872/7df3h38zabcvjylnyfe3_normal.png",
      "is_translator": false,
      "id_str": "6253282",
      "profile_link_color": "0084B4",
      "follow_request_sent": false,
      "favourites_count": 25,
      "contributors_enabled": true,
      "url": "",
      "default_profile": false,
      "profile_image_url_https": "https://si0.twimg.com/profile_images/2284174872/7df3h38zabcvjylnyfe3_normal.png",
      "utc_offset": -28800,
      "profile_banner_url": "https://si0.twimg.com/profile_banners/6253282/1347394302",
      "id": 6253282,
      "profile_use_background_image": true,
      "listed_count": 11201,
      "profile_text_color": "333333",
      "protected": false,
      "lang": "en",
      "followers_count": 1444739,
      "description": "The Real Twitter API. I tweet about API changes, service issues and happily answer questions about Twitter and our API. Don't get an answer? It's on my website.",
      "notifications": false,
      "geo_enabled": true,
      "verified": true,
      "time_zone": "Pacific Time (US & Canada)",
      "profile_background_color": "C0DEED",
      "profile_background_image_url_https": "https://si0.twimg.com/profile_background_images/656927849/miyt9dpjz77sc0w3d4vj.png",
      "statuses_count": 3367,
      "friends_count": 33,
      "default_profile_image": false,
      "profile_background_image_url": "http://a0.twimg.com/profile_background_images/656927849/miyt9dpjz77sc0w3d4vj.png",
      "following": true,
      "screen_name": "twitterapi"
    },
    "following": false
  },
  {
    "slug": "team",
    "name": "team",
    "created_at": "Wed Nov 04 01:24:28 +0000 2009",
    "uri": "/twitterapi/team",
    "subscriber_count": 277,
    "id_str": "2031945",
    "member_count": 20,
    "mode": "public",
    "id": 2031945,
    "full_name": "@twitterapi/team",
    "description": "",
    "user": {
      "profile_background_tile": true,
      "profile_sidebar_border_color": "C0DEED",
      "name": "Twitter API",
      "profile_sidebar_fill_color": "DDEEF6",
      "location": "San Francisco, CA",
      "created_at": "Wed May 23 06:01:13 +0000 2007",
      "profile_image_url": "http://a0.twimg.com/profile_images/2284174872/7df3h38zabcvjylnyfe3_normal.png",
      "is_translator": false,
      "id_str": "6253282",
      "profile_link_color": "0084B4",
      "follow_request_sent": false,
      "favourites_count": 25,
      "contributors_enabled": true,
      "url": "",
      "default_profile": false,
      "profile_image_url_https": "https://si0.twimg.com/profile_images/2284174872/7df3h38zabcvjylnyfe3_normal.png",
      "utc_offset": -28800,
      "profile_banner_url": "https://si0.twimg.com/profile_banners/6253282/1347394302",
      "id": 6253282,
      "profile_use_background_image": true,
      "listed_count": 11201,
      "profile_text_color": "333333",
      "protected": false,
      "lang": "en",
      "followers_count": 1444739,
      "description": "The Real Twitter API. I tweet about API changes, service issues and happily answer questions about Twitter and our API. Don't get an answer? It's on my website.",
      "notifications": false,
      "geo_enabled": true,
      "verified": true,
      "time_zone": "Pacific Time (US & Canada)",
      "profile_background_color": "C0DEED",
      "profile_background_image_url_https": "https://si0.twimg.com/profile_background_images/656927849/miyt9dpjz77sc0w3d4vj.png",
      "statuses_count": 3367,
      "friends_count": 33,
      "default_profile_image": false,
      "profile_background_image_url": "http://a0.twimg.com/profile_background_images/656927849/miyt9dpjz77sc0w3d4vj.png",
      "following": true,
      "screen_name": "twitterapi"
    },
    "following": true
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