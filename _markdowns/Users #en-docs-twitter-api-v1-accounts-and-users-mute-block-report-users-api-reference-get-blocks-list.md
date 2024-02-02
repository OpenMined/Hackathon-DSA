



GET blocks/list | Docs | Twitter Developer Platform 





































































































GET blocks/list



get-blocks-list

GET blocks/list
===============




Returns a collection of user
objects that the authenticating user is blocking.


**Important** This method is cursored, meaning your app
must make multiple requests in order to receive all blocks correctly.
See Using cursors to navigate
collections for more details on how cursoring works.


Resource URL¶
-------------


`https://api.twitter.com/1.1/blocks/list.json`


Resource Information¶
---------------------




|  |  |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 15 |


Parameters¶
-----------




| Name | Required | Description | Default Value | Example |
| --- | --- | --- | --- | --- |
| include\_entities | optional | The `entities` node will not be included when set to
`false` . |  | `false` |
| skip\_status | optional | When set to either `true` , `t` or
`1` statuses will not be included in the returned user
objects. |  |  |
| cursor | semi-optional | Causes the list of blocked users to be broken into pages of no
more than 5000 IDs at a time. The number of IDs returned is not
guaranteed to be 5000 as suspended users are filtered out after
connections are queried. If no cursor is provided, a value of
`-1` will be assumed, which is the first "page."The
response from the API will include a `previous_cursor` and
`next_cursor` to allow paging back and forth. See Using cursors to navigate
collections for more information. |  | `12893764510938` |


Example Request¶
----------------


`GET https://api.twitter.com/1.1/blocks/list.json?skip_status=true&cursor=-1`


Example Response¶
-----------------



```
{
  "previous_cursor": 0,
  "previous_cursor_str": "0",
  "next_cursor": 0,
  "users": [
    {
      "profile_sidebar_fill_color": "DDEEF6",
      "profile_background_tile": false,
      "profile_sidebar_border_color": "C0DEED",
      "name": "Javier Heady r",
      "created_at": "Thu Mar 01 00:16:47 +0000 2012",
      "profile_image_url": "http://a0.twimg.com/sticky/default_profile_images/default_profile_4_normal.png",
      "location": "",
      "is_translator": false,
      "follow_request_sent": false,
      "profile_link_color": "0084B4",
      "id_str": "509466276",
      "entities": {
        "description": {
          "urls": [

          ]
        }
      },
      "contributors_enabled": false,
      "favourites_count": 0,
      "url": null,
      "default_profile": true,
      "utc_offset": null,
      "profile_image_url_https": "https://si0.twimg.com/sticky/default_profile_images/default_profile_4_normal.png",
      "id": 509466276,
      "listed_count": 0,
      "profile_use_background_image": true,
      "followers_count": 0,
      "protected": false,
      "lang": "en",
      "profile_text_color": "333333",
      "profile_background_color": "C0DEED",
      "notifications": false,
      "verified": false,
      "description": "",
      "geo_enabled": false,
      "time_zone": null,
      "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme1/bg.png",
      "friends_count": 0,
      "default_profile_image": true,
      "statuses_count": 4,
      "profile_background_image_url": "http://a0.twimg.com/images/themes/theme1/bg.png",
      "following": false,
      "screen_name": "javierg3ong"
    }
  ],
  "next_cursor_str": "0"
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















