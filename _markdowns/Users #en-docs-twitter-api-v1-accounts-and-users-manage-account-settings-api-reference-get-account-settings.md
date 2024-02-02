



GET account/settings | Docs | Twitter Developer Platform 





































































































GET account/settings



get-account-settings

GET account/settings
====================




Returns settings (including current trend, geo and sleep time
information) for the authenticating user.


Resource URL¶
-------------


`https://api.twitter.com/1.1/account/settings.json`


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


None


Example Request¶
----------------


`GET https://api.twitter.com/1.1/account/settings.json`


Example Response¶
-----------------



```
{
    "always_use_https": true,
    "discoverable_by_email": true,
    "geo_enabled": true,
    "language": "en",
    "protected": false,
    "screen_name": "theSeanCook",
    "show_all_inline_media": false,
    "sleep_time": {
        "enabled": false,
        "end_time": null,
        "start_time": null
    },
    "time_zone": {
        "name": "Pacific Time (US & Canada)",
        "tzinfo_name": "America/Los_Angeles",
        "utc_offset": -28800
    },
    "trend_location": [
        {
            "country": "United States",
            "countryCode": "US",
            "name": "Atlanta",
            "parentid": 23424977,
            "placeType": {
                "code": 7,
                "name": "Town"
            },
            "url": "http://where.yahooapis.com/v1/place/2357024",
            "woeid": 2357024
        }
    ],
    "use_cookie_personalization": true,
    "allow_contributor_request": "all"
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















