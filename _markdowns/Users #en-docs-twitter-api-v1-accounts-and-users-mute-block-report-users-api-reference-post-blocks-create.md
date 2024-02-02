



POST blocks/create | Docs | Twitter Developer Platform 





































































































POST blocks/create



post-blocks-create

POST blocks/create
==================




Blocks the specified user from following the authenticating user. In
addition the blocked user will not show in the authenticating users
mentions or timeline (unless retweeted by another user). If a follow or
friend relationship exists it is destroyed.


The URL pattern
`/version/block/create/:screen_name_or_user_id.format` is
still accepted but not recommended. As a sequence of numbers is a valid
screen name we recommend using the `screen_name` or
`user_id` parameter instead.


Resource URL¶
-------------


`https://api.twitter.com/1.1/blocks/create.json`


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
| screen\_name | optional | The screen name of the potentially blocked user. Helpful for
disambiguating when a valid screen name is also a user ID. |  | *noradio* |
| user\_id | optional | The ID of the potentially blocked user. Helpful for disambiguating
when a valid user ID is also a valid screen name. |  | *12345* |
| include\_entities | optional | The *entities* node will not be included when set to
*false* . |  | *false* |
| skip\_status | optional | When set to either *true* , *t* or *1* statuses
will not be included in the returned user objects. |  | *true* |


Example Request¶
----------------


`POST https://api.twitter.com/1.1/blocks/create.json?screen_name=theSeanCook&skip_status=1`


Example Response¶
-----------------



```
{
    "contributors_enabled": true, 
    "created_at": "Sat May 09 17:58:22 +0000 2009", 
    "default_profile": false, 
    "default_profile_image": false, 
    "description": "I taught your phone that thing you like.  The Mobile Partner Engineer @Twitter. ", 
    "entities": {
        "description": {
            "urls": []
        }
    }, 
    "favourites_count": 586, 
    "follow_request_sent": false, 
    "followers_count": 10622, 
    "following": false, 
    "friends_count": 1181, 
    "geo_enabled": true, 
    "id": 38895958, 
    "id_str": "38895958", 
    "is_translator": false, 
    "lang": "en", 
    "listed_count": 190, 
    "location": "San Francisco", 
    "name": "Sean Cook", 
    "notifications": false, 
    "profile_background_color": "1A1B1F", 
    "profile_background_image_url": "http://a0.twimg.com/profile_background_images/495742332/purty_wood.png", 
    "profile_background_image_url_https": "https://si0.twimg.com/profile_background_images/495742332/purty_wood.png", 
    "profile_background_tile": true, 
    "profile_image_url": "http://a0.twimg.com/profile_images/1751506047/dead_sexy_normal.JPG", 
    "profile_image_url_https": "https://si0.twimg.com/profile_images/1751506047/dead_sexy_normal.JPG", 
    "profile_link_color": "2FC2EF", 
    "profile_sidebar_border_color": "181A1E", 
    "profile_sidebar_fill_color": "252429", 
    "profile_text_color": "666666", 
    "profile_use_background_image": true, 
    "protected": false, 
    "screen_name": "theSeanCook", 
    "show_all_inline_media": true, 
    "statuses_count": 2609, 
    "time_zone": "Pacific Time (US & Canada)", 
    "url": null, 
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















