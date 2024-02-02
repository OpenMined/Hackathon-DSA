



POST account/settings | Docs | Twitter Developer Platform 





































































































POST account/settings



post-account-settings

POST account/settings
=====================




Updates the authenticating user's settings.


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


Parameters¶
-----------




|  |  |  |  |
| --- | --- | --- | --- |
| Name | Required | Description | Example |
| sleep\_time\_enabled | optional | When set to *true* , *t* or *1* , will enable
sleep time for the user. Sleep time is the time when push or SMS
notifications should not be sent to the user. | *true* |
| start\_sleep\_time | optional | The hour that sleep time should begin if it is enabled. The value
for this parameter should be provided in ISO 8601 format (i.e.
00-23). The time is considered to be in the same timezone as the user's
*time\_zone* setting. | *13* |
| end\_sleep\_time | optional | The hour that sleep time should end if it is enabled. The value for
this parameter should be provided in ISO 8601 format (i.e.
00-23). The time is considered to be in the same timezone as the user's
*time\_zone* setting. | *13* |
| time\_zone | optional | The timezone dates and times should be displayed in for the user.
The timezone must be one of the Rails
TimeZone names. | *Europe/Copenhagen* *Pacific/Tongatapu* |
| trend\_location\_woeid | optional | The Yahoo! Where On Earth ID to use as the user's default trend
location. Global information is available by using 1 as the WOEID. The
WOEID must be one of the locations returned by GET
trends/available . | *1* |
| lang | optional | The language which Twitter should render in for this user. The
language must be specified by the appropriate two letter ISO 639-1
representation. Currently supported languages are provided by this
endpoint . | *it* *en* *es* |


Example Request¶
----------------


`POST https://api.twitter.com/1.1/account/settings.json?lang=en`


Example Response¶
-----------------



```
{
  "sleep_time": {
    "end_time": null,
    "enabled": false,
    "start_time": null
  },
  "use_cookie_personalization": true,
  "trend_location": [
    {
      "name": "San Francisco",
      "placeType": {
        "name": "Town",
        "code": 7
      },
      "woeid": 2487956,
      "country": "United States",
      "url": "http://where.yahooapis.com/v1/place/2487956",
      "countryCode": "US",
      "parentid": 23424977
    }
  ],
  "language": "en",
  "discoverable_by_email": true,
  "always_use_https": true,
  "protected": false,
  "geo_enabled": true,
  "show_all_inline_media": false,
  "screen_name": "oauth_dancer"
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















