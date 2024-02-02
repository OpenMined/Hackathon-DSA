



GET lists/subscribers | Docs | Twitter Developer Platform 





































































































GET lists/subscribers



get-lists-subscribers

GET lists/subscribers
=====================



subscribers/\*



Returns the subscribers of the specified list. Private list
subscribers will only be shown if the authenticated user owns the
specified list.


Resource URL¶
-------------


`https://api.twitter.com/1.1/lists/subscribers.json`


Resource Information¶
---------------------




|  |  |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 180 |
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
| owner\_screen\_name | optional | The screen name of the user who owns the list being requested by a
*slug* . |  |  |
| owner\_id | optional | The user ID of the user who owns the list being requested by a
*slug* . |  |  |
| count | optional | Specifies the number of results to return per page (see
*cursor* below). The default is 20, with a maximum of 5,000. |  |  |
| cursor | optional | Breaks the results into pages. A single page contains 20 lists.
Provide a value of *-1* to begin paging. Provide values as
returned in the response body's *next\_cursor* and
*previous\_cursor* attributes to page back and forth in the list.
See Using cursors to navigate
collections for more information. |  |  |
| include\_entities | optional | When set to either *true* , *t* or *1* , each
tweet will include a node called "entities". This node offers a variety
of metadata about the tweet in a discreet structure, including:
user\_mentions, urls, and hashtags. While entities are opt-in on
timelines at present, they will be made a default component of output in
the future. See Tweet Entities for
more details. |  |  |
| skip\_status | optional | When set to either *true* , *t* or *1* statuses
will not be included in the returned user objects. |  |  |


Example Request¶
----------------


`GET https://api.twitter.com/1.1/lists/subscribers.json?include_entities=true&cursor=-1&skip_status=true&slug=team&owner_screen_name=twitter`


Example Response¶
-----------------



```
{
  "previous_cursor": 0,
  "previous_cursor_str": "0",
  "next_cursor": 1357643166637635702,
  "users": [
    {
      "profile_background_tile": false,
      "profile_sidebar_fill_color": "DDEEF6",
      "name": "Almissen665",
      "profile_sidebar_border_color": "C0DEED",
      "location": null,
      "profile_image_url": "http://a0.twimg.com/sticky/default_profile_images/default_profile_1_normal.png",
      "created_at": "Mon Jun 27 09:17:15 +0000 2011",
      "follow_request_sent": false,
      "is_translator": false,
      "profile_link_color": "0084B4",
      "id_str": "324841714",
      "url": null,
      "default_profile": true,
      "contributors_enabled": false,
      "favourites_count": 0,
      "id": 324841714,
      "utc_offset": null,
      "profile_image_url_https": "https://si0.twimg.com/sticky/default_profile_images/default_profile_1_normal.png",
      "profile_use_background_image": true,
      "listed_count": 0,
      "lang": "en",
      "profile_text_color": "333333",
      "followers_count": 6,
      "protected": false,
      "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme1/bg.png",
      "notifications": false,
      "geo_enabled": false,
      "description": null,
      "profile_background_color": "C0DEED",
      "time_zone": null,
      "verified": false,
      "statuses_count": 1,
      "friends_count": 27,
      "profile_background_image_url": "http://a0.twimg.com/images/themes/theme1/bg.png",
      "default_profile_image": true,
      "screen_name": "bonasser789",
      "following": false,
      "show_all_inline_media": false
    },
    {
      "profile_sidebar_fill_color": "E6F6F9",
      "profile_sidebar_border_color": "DBE9ED",
      "name": "GR Syber-Space",
      "profile_background_tile": true,
      "location": "Grand Rapids, MI",
      "profile_image_url": "http://a2.twimg.com/profile_images/1322547748/images__97__normal.jpg",
      "created_at": "Thu Sep 30 23:05:38 +0000 2010",
      "profile_link_color": "CC3366",
      "id_str": "197218370",
      "follow_request_sent": false,
      "is_translator": false,
      "url": "http://www.wix.com/castlesportsgr/myj",
      "default_profile": false,
      "favourites_count": 2,
      "contributors_enabled": false,
      "id": 197218370,
      "utc_offset": -18000,
      "profile_image_url_https": "https://si0.twimg.com/profile_images/1322547748/images__97__normal.jpg",
      "profile_use_background_image": true,
      "listed_count": 268,
      "lang": "en",
      "profile_text_color": "333333",
      "followers_count": 2628,
      "protected": true,
      "notifications": false,
      "geo_enabled": true,
      "profile_background_color": "DBE9ED",
      "description": "Welcome to Teen Gossip 411. Celebrity Gossip, Teens fashion trends for the summer 2011, Hollywood Gossip, Hotest music, Teen Websites, and more.",
      "time_zone": "Quito",
      "verified": false,
      "profile_background_image_url_https": "https://si0.twimg.com/profile_background_images/237705957/images__97_.jpg",
      "default_profile_image": false,
      "friends_count": 2846,
      "profile_background_image_url": "http://a2.twimg.com/profile_background_images/237705957/images__97_.jpg",
      "statuses_count": 7463,
      "show_all_inline_media": true,
      "screen_name": "GRSYBERSPACE",
      "following": false
    }
  ],
  "next_cursor_str": "1357643166637635702"
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















