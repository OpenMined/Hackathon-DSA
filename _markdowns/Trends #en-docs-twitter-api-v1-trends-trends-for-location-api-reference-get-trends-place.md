



GET trends/place | Docs | Twitter Developer Platform 





































































































GET trends/place



get-trends-place

GET trends/place
================




Returns the top 50 trending topics for a specific `id`, if
trending information is available for it.


Note: The `id` parameter for this endpoint is the "where
on earth identifier" or WOEID, which is a legacy identifier created by
Yahoo and has been deprecated. Twitter API v1.1 still uses the numeric
value to identify town and country trend locations. Reference our legacy
blog
post, or archived
data


Example WOEID locations include: Worldwide: 1 UK: 23424975 Brazil:
23424768 Germany: 23424829 Mexico: 23424900 Canada: 23424775 United
States: 23424977 New York: 2459115


To identify other ids, please use the GET
trends/available endpoint.


The response is an array of `trend` objects that encode
the name of the trending topic, the query parameter that can be used to
search for the topic on Twitter
Search, and the Twitter Search URL.


The most up to date info available is returned on request. The
`created_at` field will show when the oldest trend started
trending. The `as_of` field contains the timestamp when the
list of trends was created.


The `tweet_volume` for the last 24 hours is also returned
for many trends if this is available.


Resource URL¶
-------------


`https://api.twitter.com/1.1/trends/place.json`


Resource Information¶
---------------------




|  |  |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 75 |
| Requests / 15-min window (app auth) | 75 |


Parameters¶
-----------




|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| id | required | The numeric value that represents the location from where to return
trending information for from. Formerly linked to the Yahoo! Where On
Earth ID Global information is available by using *1* as the
*WOEID* . |  | *1* |
| exclude | optional | Setting this equal to *hashtags* will remove all hashtags
from the trends list. |  |  |


Example Request¶
----------------


`GET https://api.twitter.com/1.1/trends/place.json?id=1`


Example Response¶
-----------------



```
[
  {
    "trends": [
      {
        "name": "#GiftAGamer",
        "url": "http://twitter.com/search?q=%23GiftAGamer",
        "promoted_content": null,
        "query": "%23GiftAGamer",
        "tweet_volume": null
      },
      {
        "name": "#AskCuppyAnything",
        "url": "http://twitter.com/search?q=%23AskCuppyAnything",
        "promoted_content": null,
        "query": "%23AskCuppyAnything",
        "tweet_volume": 14504
      },
      {
        "name": "#givethanks",
        "url": "http://twitter.com/search?q=%23givethanks",
        "promoted_content": null,
        "query": "%23givethanks",
        "tweet_volume": null
      },
      {
        "name": "Carrefour",
        "url": "http://twitter.com/search?q=Carrefour",
        "promoted_content": null,
        "query": "Carrefour",
        "tweet_volume": 438616
      },
      {
        "name": "#StreamLifeGoesOn",
        "url": "http://twitter.com/search?q=%23StreamLifeGoesOn",
        "promoted_content": null,
        "query": "%23StreamLifeGoesOn",
        "tweet_volume": 179026
      },
      {
        "name": "STREAM BE PARTY",
        "url": "http://twitter.com/search?q=%22STREAM+BE+PARTY%22",
        "promoted_content": null,
        "query": "%22STREAM+BE+PARTY%22",
        "tweet_volume": 71404
      },
      {
        "name": "#TransDayOfRemembrance",
        "url": "http://twitter.com/search?q=%23TransDayOfRemembrance",
        "promoted_content": null,
        "query": "%23TransDayOfRemembrance",
        "tweet_volume": 45852
      },
      {
        "name": "Mourão",
        "url": "http://twitter.com/search?q=Mour%C3%A3o",
        "promoted_content": null,
        "query": "Mour%C3%A3o",
        "tweet_volume": 12614
      },
      {
        "name": "Taysom Hill",
        "url": "http://twitter.com/search?q=%22Taysom+Hill%22",
        "promoted_content": null,
        "query": "%22Taysom+Hill%22",
        "tweet_volume": 20311
      },
      {
        "name": "Geraldo",
        "url": "http://twitter.com/search?q=Geraldo",
        "promoted_content": null,
        "query": "Geraldo",
        "tweet_volume": 30166
      }
    ],
    "as_of": "2020-11-20T19:37:52Z",
    "created_at": "2020-11-19T14:15:43Z",
    "locations": [
      {
        "name": "Worldwide",
        "woeid": 1
      }
    ]
  }
]
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















