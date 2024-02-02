



POST lists/subscribers/create | Docs | Twitter Developer Platform 





































































































POST lists/subscribers/create



post-lists-subscribers-create

POST lists/subscribers/create
=============================




Subscribes the authenticated user to the specified list.


Resource URL¶
-------------


`https://api.twitter.com/1.1/lists/subscribers/create.json`


Resource Information¶
---------------------




|  |  |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |


Parameters¶
-----------




|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| owner\_screen\_name | optional | The screen name of the user who owns the list being requested by a
*slug* . |  |  |
| owner\_id | optional | The user ID of the user who owns the list being requested by a
*slug* . |  |  |
| list\_id | required | The numerical *id* of the list. |  |  |
| slug | required | You can identify a list by its slug instead of its numerical id. If
you decide to do so, note that you'll also have to specify the list
owner using the *owner\_id* or *owner\_screen\_name*
parameters. |  |  |


Example Request¶
----------------


`POST https://api.twitter.com/1.1/lists/subscribers/create.json?slug=team&owner_screen_name=twitter`


Example Response¶
-----------------



```
{
   "created_at":"Wed Sep 23 01:18:01 +0000 2009",
   "slug":"team",
   "name":"Team",
   "full_name":"@twitter/team",
   "description":"",
   "mode":"public",
   "following":false,
   "user":{
      "geo_enabled":true,
      "profile_background_color":"ACDED6",
      "protected":false,
      "profile_background_tile":false,
      "created_at":"Tue Feb 20 14:35:54 +0000 2007",
      "profile_image_url_https":"https://si0.twimg.com/profile_images/1124040897/at-twitter_normal.png",
      "name":"Twitter",
      "favourites_count":16,
      "profile_sidebar_fill_color":"F6F6F6",
      "default_profile_image":false,
      "notifications":false,
      "utc_offset":-28800,
      "description":"Always wondering what's happening. ",
      "display_url":null,
      "deactivated_bit":false,
      "statuses_count":1218,
      "following":false,
      "verified":true,
      "profile_sidebar_border_color":"EEEEEE",
      "followers_count":6619949,
      "profile_image_url":"http://a0.twimg.com/profile_images/1124040897/at-twitter_normal.png",
      "contributors_enabled":true,
      "follow_request_sent":false,
      "profile_use_background_image":true,
      "location":"San Francisco, CA",
      "id_str":"783214",
      "is_translator":false,
      "show_all_inline_media":true,
      "profile_text_color":"333333",
      "screen_name":"twitter",
      "profile_background_image_url":"http://a1.twimg.com/images/themes/theme18/bg.gif",
      "url":"http://blog.twitter.com/",
      "expanded_url":null,
      "default_profile":false,
      "profile_background_image_url_https":"https://si0.twimg.com/images/themes/theme18/bg.gif",
      "time_zone":"Pacific Time (US & Canada)",
      "profile_link_color":"038543",
      "id":783214,
      "entities":{
         "urls":[

         ],
         "user_mentions":[

         ],
         "hashtags":[

         ]
      },
      "suspended":false,
      "listed_count":66018,
      "lang":"en",
      "friends_count":695
   },
   "member_count":643,
   "id_str":"574",
   "subscriber_count":76779,
   "id":574,
   "uri":"/twitter/team"
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















