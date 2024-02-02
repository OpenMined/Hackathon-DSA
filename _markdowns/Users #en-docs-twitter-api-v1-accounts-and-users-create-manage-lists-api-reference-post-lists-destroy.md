



POST lists/destroy | Docs | Twitter Developer Platform 





































































































POST lists/destroy



post-lists-destroy

POST lists/destroy
==================




Deletes the specified list. The authenticated user must own the list
to be able to destroy it.


Resource URL¶
-------------


`https://api.twitter.com/1.1/lists/destroy.json`


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


`POST https://api.twitter.com/1.1/lists/destroy.json?owner_screen_name=kurrik&slug=goonies`


Example Response¶
-----------------



```
{
   "created_at":"Fri Nov 04 21:22:36 +0000 2011",
   "slug":"goonies",
   "name":"Goonies",
   "full_name":"@kurrik/goonies",
   "description":"For life",
   "mode":"public",
   "following":false,
   "user":{
      "geo_enabled":true,
      "profile_background_image_url_https":"https://si0.twimg.com/profile_background_images/342542280/background7.png",
      "profile_background_color":"8fc1ff",
      "protected":false,
      "default_profile":false,
      "listed_count":127,
      "profile_background_tile":true,
      "created_at":"Thu Jul 19 15:58:07 +0000 2007",
      "friends_count":291,
      "name":"Arne Roomann-Kurrik",
      "profile_sidebar_fill_color":"c7e0ff",
      "notifications":false,
      "utc_offset":-28800,
      "profile_image_url_https":"https://si0.twimg.com/profile_images/24229162/arne001_normal.jpg",
      "description":"Developer Advocate at Twitter, practitioner of dark sandwich arts. ",
      "display_url":"roomanna.com",
      "following":false,
      "verified":false,
      "favourites_count":190,
      "profile_sidebar_border_color":"6baeff",
      "followers_count":1705,
      "profile_image_url":"http://a2.twimg.com/profile_images/24229162/arne001_normal.jpg",
      "default_profile_image":false,
      "contributors_enabled":false,
      "deactivated_bit":false,
      "statuses_count":1935,
      "profile_use_background_image":true,
      "location":"Scan Francesco",
      "id_str":"7588892",
      "show_all_inline_media":false,
      "profile_text_color":"000000",
      "screen_name":"kurrik",
      "follow_request_sent":false,
      "profile_background_image_url":"http://a2.twimg.com/profile_background_images/342542280/background7.png",
      "url":"http://t.co/SSiVavc4",
      "expanded_url":"http://roomanna.com",
      "is_translator":false,
      "time_zone":"Pacific Time (US & Canada)",
      "profile_link_color":"0084B4",
      "id":7588892,
      "entities":{
         "urls":[

         ],
         "user_mentions":[

         ],
         "hashtags":[

         ]
      },
      "suspended":false,
      "lang":"en"
   },
   "member_count":0,
   "id_str":"58300198",
   "subscriber_count":0,
   "id":58300198,
   "uri":"/kurrik/goonies"
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















