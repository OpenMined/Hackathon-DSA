



GET lists/subscriptions | Docs | Twitter Developer Platform 





































































































GET lists/subscriptions



get-lists-subscriptions

GET lists/subscriptions
=======================




Obtain a collection of the lists the specified user is subscribed to,
20 lists per page by default. Does not include the user's own lists.


Resource URL¶
-------------


`https://api.twitter.com/1.1/lists/subscriptions.json`


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
disambiguating when a valid user ID is also a valid screen name. |  |  |
| screen\_name | optional | The screen name of the user for whom to return results. Helpful for
disambiguating when a valid screen name is also a user ID. |  |  |
| count | optional | The amount of results to return per page. Defaults to 20. No more
than 1000 results will ever be returned in a single page. |  |  |
| cursor | optional | Breaks the results into pages. Provide a value of *-1* to
begin paging. Provide values as returned in the response body's
*next\_cursor* and *previous\_cursor* attributes to page
back and forth in the list. It is recommended to always use cursors when
the method supports them. See Cursoring for more
information. |  |  |


Example Request¶
----------------


`GET https://api.twitter.com/1.1/lists/subscriptions.json?cursor=-1&screen_name=episod&count=5`


Example Response¶
-----------------



```
{
  "previous_cursor": 0,
  "lists": [
    {
      "slug": "team",
      "name": "team",
      "uri": "/TwitterEng/team",
      "created_at": "Mon Oct 03 02:48:07 +0000 2011",
      "subscriber_count": 131,
      "id_str": "55932616",
      "member_count": 324,
      "mode": "public",
      "id": 55932616,
      "full_name": "@TwitterEng/team",
      "description": "",
      "user": {
        "profile_sidebar_border_color": "C6E2EE",
        "profile_sidebar_fill_color": "DAECF4",
        "profile_background_tile": false,
        "expanded_url": null,
        "name": "Twitter Engineering",
        "location": "San Francisco, CA",
        "created_at": "Sat Jun 16 00:14:36 +0000 2007",
        "profile_image_url": "http://a2.twimg.com/profile_images/1262149685/twitter_newbird_boxed_blueonwhite_normal.png",
        "is_translator": false,
        "profile_link_color": "1F98C7",
        "follow_request_sent": null,
        "id_str": "6844292",
        "entities": {
          "urls": [

          ],
          "hashtags": [

          ],
          "user_mentions": [

          ]
        },
        "url": "http://engineering.twitter.com",
        "default_profile": false,
        "favourites_count": 0,
        "contributors_enabled": true,
        "id": 6844292,
        "utc_offset": -14400,
        "profile_image_url_https": "https://si0.twimg.com/profile_images/1262149685/twitter_newbird_boxed_blueonwhite_normal.png",
        "profile_use_background_image": true,
        "listed_count": 1493,
        "profile_text_color": "663B12",
        "lang": "en",
        "followers_count": 132674,
        "protected": false,
        "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme2/bg.gif",
        "verified": true,
        "geo_enabled": true,
        "notifications": null,
        "time_zone": "Atlantic Time (Canada)",
        "description": "The official account for Twitter Engineering.",
        "profile_background_color": "C6E2EE",
        "profile_background_image_url": "http://a1.twimg.com/images/themes/theme2/bg.gif",
        "default_profile_image": false,
        "statuses_count": 61,
        "friends_count": 0,
        "display_url": null,
        "screen_name": "TwitterEng",
        "following": null,
        "show_all_inline_media": true
      },
      "following": false
    },
    {
      "slug": "the-brain-trust",
      "name": "The Brain Trust",
      "uri": "/LTRK140/the-brain-trust",
      "created_at": "Sun Mar 06 20:01:50 +0000 2011",
      "subscriber_count": 24,
      "id_str": "37396827",
      "member_count": 148,
      "mode": "public",
      "id": 37396827,
      "full_name": "@LTRK140/the-brain-trust",
      "description": "Twitter Artists, Ascii, Unicode Art.",
      "user": {
        "profile_sidebar_border_color": "080000",
        "profile_sidebar_fill_color": "",
        "profile_background_tile": true,
        "name": "﹅█▄▀█▀ █▀▐━▀▄ ▌◢▌██﹅",
        "location": "Toronto",
        "created_at": "Fri Jun 04 16:48:39 +0000 2010",
        "profile_image_url": "http://a1.twimg.com/profile_images/1315622089/Cool_Daddy_normal.png",
        "is_translator": false,
        "profile_link_color": "080000",
        "follow_request_sent": false,
        "id_str": "151938348",
        "url": "http://twitter.com/KREWZO",
        "favourites_count": 10,
        "contributors_enabled": false,
        "default_profile": false,
        "id": 151938348,
        "utc_offset": -28800,
        "profile_image_url_https": "https://si0.twimg.com/profile_images/1315622089/Cool_Daddy_normal.png",
        "profile_use_background_image": true,
        "listed_count": 131,
        "profile_text_color": "000000",
        "lang": "en",
        "followers_count": 838,
        "protected": false,
        "profile_background_image_url_https": "https://si0.twimg.com/profile_background_images/285103295/ltrk140.JPG",
        "verified": false,
        "geo_enabled": true,
        "notifications": false,
        "time_zone": "Pacific Time (US & Canada)",
        "description": "▓⁄─⁄⁄﹅█▄▀█▀ █▀▐━▀▄ ▌◢▌██﹅⁄─⁄⁄▓  rn  •140•ASCII•UNICODE•ART• BY OZ MELO   •  I LIVE & WORK IN #YYZ.     ★★ MOST TWEETS ARE BEST VIEWED AS A STATUS PAGE ★★   █♥█",
        "profile_background_color": "030003",
        "profile_background_image_url": "http://a1.twimg.com/profile_background_images/285103295/ltrk140.JPG",
        "default_profile_image": false,
        "statuses_count": 1006,
        "friends_count": 139,
        "screen_name": "LTRK140",
        "following": false,
        "show_all_inline_media": true
      },
      "following": false
    },
    {
      "slug": "twoutside-lands",
      "name": "Twoutside Lands",
      "uri": "/dannyhertz/twoutside-lands",
      "created_at": "Fri Aug 12 07:21:25 +0000 2011",
      "subscriber_count": 12,
      "id_str": "52270561",
      "member_count": 25,
      "mode": "public",
      "id": 52270561,
      "full_name": "@dannyhertz/twoutside-lands",
      "description": "Tweeps @ Outside Lands 2011",
      "user": {
        "profile_sidebar_border_color": "4685e3",
        "profile_sidebar_fill_color": "c7dced",
        "profile_background_tile": false,
        "expanded_url": "http://www.dannyhertz.com",
        "name": "Danny Hertz",
        "location": "San Francisco",
        "created_at": "Sat Nov 15 02:26:09 +0000 2008",
        "profile_image_url": "http://a0.twimg.com/profile_images/1546221308/6153868543_d7ab87737a_b_normal.jpeg",
        "is_translator": true,
        "profile_link_color": "005082",
        "follow_request_sent": false,
        "id_str": "17400516",
        "entities": {
          "urls": [

          ],
          "hashtags": [

          ],
          "user_mentions": [

          ]
        },
        "url": "http://t.co/90RtgWI",
        "favourites_count": 243,
        "contributors_enabled": false,
        "default_profile": false,
        "id": 17400516,
        "utc_offset": -28800,
        "profile_image_url_https": "https://si0.twimg.com/profile_images/1546221308/6153868543_d7ab87737a_b_normal.jpeg",
        "profile_use_background_image": true,
        "listed_count": 52,
        "profile_text_color": "000000",
        "lang": "en",
        "followers_count": 2684,
        "protected": false,
        "profile_background_image_url_https": "https://si0.twimg.com/profile_background_images/331345358/pamperedpuppy20091103.jpeg",
        "verified": false,
        "geo_enabled": true,
        "notifications": false,
        "time_zone": "Pacific Time (US & Canada)",
        "description": "Software Engineer on the User Services team at Twitter and lead singer for the rock band Journey.",
        "profile_background_color": "ffffff",
        "profile_background_image_url": "http://a0.twimg.com/profile_background_images/331345358/pamperedpuppy20091103.jpeg",
        "default_profile_image": false,
        "statuses_count": 2318,
        "friends_count": 261,
        "display_url": "dannyhertz.com",
        "screen_name": "dannyhertz",
        "following": false,
        "show_all_inline_media": true
      },
      "following": false
    },
    {
      "slug": "july-6-curators",
      "name": "July 6 curators",
      "uri": "/townhall/july-6-curators",
      "created_at": "Mon Jul 04 20:37:28 +0000 2011",
      "subscriber_count": 58,
      "id_str": "49286494",
      "member_count": 8,
      "mode": "public",
      "id": 49286494,
      "full_name": "@townhall/july-6-curators",
      "description": "Curators helping for the Town Hall at the White House on July 6th at 2pm ET",
      "user": {
        "profile_sidebar_border_color": "C0DEED",
        "profile_sidebar_fill_color": "DDEEF6",
        "profile_background_tile": true,
        "name": "Town Hall",
        "location": "",
        "created_at": "Tue May 31 01:50:52 +0000 2011",
        "profile_image_url": "http://a2.twimg.com/profile_images/1419432899/avatar_normal.png",
        "is_translator": false,
        "profile_link_color": "0084B4",
        "follow_request_sent": null,
        "id_str": "308230587",
        "url": "http://askobama.twitter.com",
        "default_profile": false,
        "favourites_count": 0,
        "contributors_enabled": true,
        "id": 308230587,
        "utc_offset": -28800,
        "profile_image_url_https": "https://si0.twimg.com/profile_images/1419432899/avatar_normal.png",
        "profile_use_background_image": true,
        "listed_count": 517,
        "profile_text_color": "333333",
        "lang": "en",
        "followers_count": 24456,
        "protected": false,
        "profile_background_image_url_https": "https://si0.twimg.com/profile_background_images/280500767/bg.jpg",
        "verified": true,
        "geo_enabled": false,
        "notifications": null,
        "time_zone": "Pacific Time (US & Canada)",
        "description": "Official account for Twitter hosted town halls. Our first on July 6th, 2PM ET. ",
        "profile_background_color": "C0DEED",
        "profile_background_image_url": "http://a0.twimg.com/profile_background_images/280500767/bg.jpg",
        "default_profile_image": false,
        "statuses_count": 100,
        "friends_count": 2,
        "screen_name": "townhall",
        "following": null,
        "show_all_inline_media": true
      },
      "following": false
    },
    {
      "slug": "streaming-music-industry",
      "name": "Streaming Music Industry ",
      "uri": "/meetmarshall/streaming-music-industry",
      "created_at": "Thu Mar 31 04:04:10 +0000 2011",
      "subscriber_count": 193,
      "id_str": "41857276",
      "member_count": 1,
      "mode": "public",
      "id": 41857276,
      "full_name": "@meetmarshall/streaming-music-industry",
      "description": "A custom list created by adding, subtracting or filtering existing lists (made using @formulists)",
      "user": {
        "profile_sidebar_border_color": "C0DEED",
        "profile_sidebar_fill_color": "DDEEF6",
        "profile_background_tile": false,
        "name": "Marshall Kirkpatrick",
        "location": "",
        "created_at": "Mon Mar 28 20:18:47 +0000 2011",
        "profile_image_url": "http://a3.twimg.com/sticky/default_profile_images/default_profile_0_normal.png",
        "is_translator": false,
        "profile_link_color": "0084B4",
        "follow_request_sent": false,
        "id_str": "273602749",
        "url": "http://twitter.com/marshallk",
        "default_profile": true,
        "favourites_count": 0,
        "contributors_enabled": false,
        "id": 273602749,
        "utc_offset": -28800,
        "profile_image_url_https": "https://si0.twimg.com/sticky/default_profile_images/default_profile_0_normal.png",
        "profile_use_background_image": true,
        "listed_count": 3,
        "profile_text_color": "333333",
        "lang": "en",
        "followers_count": 29,
        "protected": false,
        "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme1/bg.png",
        "verified": false,
        "geo_enabled": false,
        "notifications": false,
        "time_zone": "Pacific Time (US & Canada)",
        "description": "I just came for the lists.",
        "profile_background_color": "C0DEED",
        "profile_background_image_url": "http://a0.twimg.com/images/themes/theme1/bg.png",
        "default_profile_image": true,
        "statuses_count": 3,
        "friends_count": 146,
        "screen_name": "meetmarshall",
        "following": false,
        "show_all_inline_media": false
      },
      "following": false
    }
  ],
  "previous_cursor_str": "0",
  "next_cursor": 1364811190668631091,
  "next_cursor_str": "1364811190668631091"
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















