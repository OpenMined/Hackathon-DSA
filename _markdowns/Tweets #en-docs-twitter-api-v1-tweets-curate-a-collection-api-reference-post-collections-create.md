



POST collections/create | Docs | Twitter Developer Platform 





































































































POST collections/create



post-collections-create

POST collections/create
=======================




Create a Collection owned by the currently authenticated user.


The API endpoint may refuse to complete the request if the
authenticated user has exceeded the total number of allowed collections
for their account.


Resource URL¶
-------------


`https://api.twitter.com/1.1/collections/create.json`


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
| name | required | The title of the collection being created, in 25 characters or
less. |  | *Sweet%20Tweets* |
| description | optional | A brief description of this collection in 160 characters or
fewer. |  | *My%20favorite%20tweets%20ever* |
| url | optional | A fully-qualified URL to associate with this collection. |  | `https%3A%2F%2Fexample.com%2F` |
| timeline\_order | optional | Order Tweets chronologically or in the order they are added to a
Collection. *curation\_reverse\_chron* - order added (default)
*tweet\_chron* - oldest first *tweet\_reverse\_chron* - most
recent first |  | *tweet\_reverse\_chron* |


Example Request¶
----------------


`POST https://api.twitter.com/1.1/collections/create.json?name=Tweets%20to%20reply%20to`


Example Response¶
-----------------



```
{
  "response": {
    "timeline_id": "custom-390882285743898624"
  },
  "objects": {
    "users": {
      "119476949": {
        "profile_sidebar_fill_color": "DDEEF6",
        "profile_sidebar_border_color": "C0DEED",
        "profile_background_tile": true,
        "name": "OAuth Dancer",
        "profile_image_url": "http://a0.twimg.com/profile_images/730275945/oauth-dancer_normal.jpg",
        "created_at": "Wed Mar 03 19:37:35 +0000 2010",
        "location": "San Francisco, CA",
        "follow_request_sent": null,
        "profile_link_color": "0084B4",
        "is_translator": false,
        "id_str": "119476949",
        "default_profile": false,
        "contributors_enabled": false,
        "favourites_count": 0,
        "url": "http://bit.ly/oauth-dancer",
        "profile_image_url_https": "https://si0.twimg.com/profile_images/730275945/oauth-dancer_normal.jpg",
        "utc_offset": null,
        "id": 119476949,
        "profile_use_background_image": true,
        "listed_count": 0,
        "profile_text_color": "333333",
        "lang": "en",
        "followers_count": 0,
        "protected": false,
        "notifications": null,
        "profile_background_image_url_https": "https://si0.twimg.com/profile_background_images/80151733/oauth-dance.png",
        "profile_background_color": "C0DEED",
        "verified": false,
        "geo_enabled": true,
        "time_zone": null,
        "description": "",
        "default_profile_image": false,
        "profile_background_image_url": "http://a0.twimg.com/profile_background_images/80151733/oauth-dance.png",
        "statuses_count": 0,
        "friends_count": 0,
        "following": null,
        "screen_name": "oauth_dancer",
        "counts": {
          "lists": {
            "owned": null,
            "subscribed": null
          },
          "saved_searches": 0
        }
      }
    },
    "timelines": {
      "custom-390882285743898624": {
        "name": "Tweets to reply to",
        "user_id": "119476949"
      }
    }
  }
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















