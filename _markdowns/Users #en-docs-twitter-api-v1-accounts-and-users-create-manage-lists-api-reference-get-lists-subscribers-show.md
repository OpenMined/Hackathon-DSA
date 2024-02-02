



GET lists/subscribers/show | Docs | Twitter Developer Platform 





































































































GET lists/subscribers/show



get-lists-subscribers-show

GET lists/subscribers/show
==========================




Check if the specified user is a subscriber of the specified list.
Returns the user if they are a subscriber.


Resource URL¶
-------------


`https://api.twitter.com/1.1/lists/subscribers/show.json`


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
| owner\_screen\_name | optional | The screen name of the user who owns the list being requested by a
*slug*. |  |  |
| owner\_id | optional | The user ID of the user who owns the list being requested by a
*slug*. |  |  |
| list\_id | required | The numerical *id* of the list. |  |  |
| slug | required | You can identify a list by its slug instead of its numerical id. If
you decide to do so, note that you'll also have to specify the list
owner using the *owner\_id* or *owner\_screen\_name*
parameters. |  |  |
| user\_id | required | The ID of the user for whom to return results. Helpful for
disambiguating when a valid user ID is also a valid screen name. |  |  |
| screen\_name | required | The screen name of the user for whom to return results. Helpful for
disambiguating when a valid screen name is also a user ID. |  |  |
| include\_entities | optional | When set to either *true*, *t* or *1*, each
Tweet will include a node called "entities". This node offers a variety
of metadata about the tweet in a discreet structure, including:
user\_mentions, urls, and hashtags. While entities are opt-in on
timelines at present, they will be made a default component of output in
the future. See Tweet Entities for
more details. |  |  |
| skip\_status | optional | When set to either *true* , *t* or *1* statuses
will not be included in the returned user objects. |  |  |


Example Request¶
----------------


`GET https://api.twitter.com/1.1/lists/subscribers/show.json?slug=team&owner_screen_name=twitter&screen_name=episod`


Example Response¶
-----------------



```
{
  "id": "819797",
  "id_str": "819797",
  "is_translator": false,
  "default_profile": false,
  "entities": {
    "url": {
      "urls": [
        {
          "url": "http://t.co/Lxw7upbN",
          "indices": [
            0,
            20
          ],
          "display_url": "rebelmouse.com/episod/",
          "expanded_url": "http://www.rebelmouse.com/episod/"
        }
      ]
    },
    "description": {
      "urls": []
    }
  },
  "show_all_inline_media": true,
  "profile_use_background_image": true,
  "profile_text_color": "D20909",
  "utc_offset": -28800,
  "listed_count": 341,
  "name": "Taylor Singletary",
  "notifications": false,
  "profile_sidebar_border_color": "000000",
  "geo_enabled": true,
  "follow_request_sent": false,
  "url": "http://t.co/Lxw7upbN",
  "lang": "en",
  "profile_image_url_https": "https://si0.twimg.com/profile_images/2574556418/dk93ji5e3w4rwscaabt3_normal.png",
  "created_at": "Wed Mar 07 22:23:19 +0000 2007",
  "protected": false,
  "followers_count": 7180,
  "profile_background_image_url_https": "https://si0.twimg.com/profile_background_images/643655842/hzfv12wini4q60zzrthg.png",
  "screen_name": "episod",
  "profile_background_tile": true,
  "friends_count": 5452,
  "profile_sidebar_fill_color": "FBFBFB",
  "description": "Reality Technician, Twitter API team, synthesizer enthusiast; a most excellent adventure in timelines. Missive commander.",
  "time_zone": "Pacific Time (US & Canada)",
  "default_profile_image": false,
  "location": "San Francisco, CA",
  "profile_image_url": "http://a0.twimg.com/profile_images/2574556418/dk93ji5e3w4rwscaabt3_normal.png",
  "profile_banner_url": "https://si0.twimg.com/profile_banners/819797/1346803502",
  "favourites_count": 16076,
  "following": true,
  "profile_background_color": "000000",
  "verified": false,
  "statuses_count": 18132,
  "status": {
    "entities": {
      "urls": [
        {
          "url": "http://t.co/4mdAn0tF",
          "indices": [
            16,
            36
          ],
          "display_url": "youtube.com/watch?v=pPkNtg…",
          "expanded_url": "http://www.youtube.com/watch?v=pPkNtg3Fvwk&feature=youtube_gdata_player"
        }
      ],
      "hashtags": [],
      "user_mentions": []
    },
    "geo": null,
    "place": null,
    "in_reply_to_screen_name": null,
    "in_reply_to_user_id": null,
    "retweeted": false,
    "in_reply_to_status_id": null,
    "created_at": "Wed Sep 05 15:57:09 +0000 2012",
    "possibly_sensitive": false,
    "in_reply_to_status_id_str": null,
    "contributors": null,
    "favorited": false,
    "source": "YouTube on iOS",
    "in_reply_to_user_id_str": null,
    "retweet_count": 0,
    "id": "< Unable to parse in Javascript >",
    "id_str": "243377236902821888",
    "coordinates": null,
    "truncated": false,
    "text": "Current status  http://t.co/4mdAn0tF"
  },
  "contributors_enabled": false,
  "profile_background_image_url": "http://a0.twimg.com/profile_background_images/643655842/hzfv12wini4q60zzrthg.png",
  "profile_link_color": "C71818"
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















