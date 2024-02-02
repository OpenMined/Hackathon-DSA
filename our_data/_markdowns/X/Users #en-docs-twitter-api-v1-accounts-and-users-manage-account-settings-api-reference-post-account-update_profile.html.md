
POST account/update\_profile | Docs | Twitter Developer Platform 

POST account/update\_profile

post-account-update\_profile
POST account/update\_profile
============================

Sets some values that users are able to set under the "Account" tab
of their settings page. Only the parameters specified will be
updated.

Resource URL¶
-------------

`https://api.twitter.com/1.1/account/update_profile.json`

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
| name | optional | Full name associated with the profile. |  | *Marcel Molina* |
| url | optional | URL associated with the profile. Will be prepended with
`http://` if not present. |  | `http://project.ioni.st` |
| location | optional | The city or country describing where the user of the account is
located. The contents are not normalized or geocoded in any way. |  | *San Francisco CA* |
| description | optional | A description of the user owning the account. |  | *Flipped my wig at age 22 and it never grew back. Also: I work at
Twitter.* |
| include\_entities | optional | The *entities* node will not be included when set to
*false* . |  | *false* |
| skip\_status | optional | When set to either *true* , *t* or *1* statuses
will not be included in the returned user object. |  |  |

Example Request¶
----------------

`POST https://api.twitter.com/1.1/account/update_profile.json?name=Sean%20Cook&description=Keep%20calm%20and%20rock%20on.`

Example Response¶
-----------------

```
{
    "contributors_enabled": false,
    "created_at": "Thu Aug 23 19:45:07 +0000 2012",
    "default_profile": false,
    "default_profile_image": false,
    "description": "Keep calm and rock on.",
    "favourites_count": 0,
    "follow_request_sent": false,
    "followers_count": 0,
    "following": false,
    "friends_count": 10,
    "geo_enabled": true,
    "id": 776627022,
    "id_str": "776627022",
    "is_translator": false,
    "lang": "en",
    "listed_count": 0,
    "location": "San Francisco, CA",
    "name": "Sean Cook",
    "notifications": false,
    "profile_background_color": "9AE4E8",
    "profile_background_image_url": "http://a0.twimg.com/images/themes/theme16/bg.gif",
    "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme16/bg.gif",
    "profile_background_tile": false,
    "profile_image_url": "http://a0.twimg.com/profile_images/2550256790/hv5rtkvistn50nvcuydl_normal.jpeg",
    "profile_image_url_https": "https://si0.twimg.com/profile_images/2550256790/hv5rtkvistn50nvcuydl_normal.jpeg",
    "profile_sidebar_border_color": "BDDCAD",
    "profile_sidebar_fill_color": "DDFFCC",
    "profile_text_color": "333333",
    "profile_use_background_image": true,
    "protected": false,
    "screen_name": "s0c1alm3dia",
    "show_all_inline_media": false,
    "statuses_count": 0,
    "time_zone": "Pacific Time (US & Canada)",
    "url": "http://cnn.com",
    "utc_offset": -28800,
    "verified": false
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