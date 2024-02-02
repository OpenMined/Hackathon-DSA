



GET trends/available | Docs | Twitter Developer Platform 





































































































GET trends/available



get-trends-available

GET trends/available
====================




Returns the locations that Twitter has trending topic information
for.


The response is an array of "locations" that encode the location's
`WOEID` and some other human-readable information such as a
canonical name and country the location belongs in.


Note: This endpoint uses the "where on earth identifier" or WOEID,
which is a legacy identifier created by Yahoo and has been deprecated.
Twitter API v1.1 still uses the numeric value to identify town and
country trend locations. Reference our legacy blog
post for more details. The url returned in the response,
`where.yahooapis.com` is no longer valid.


Resource URL¶
-------------


`https://api.twitter.com/1.1/trends/available.json`


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


None


Example Request¶
----------------


`GET https://api.twitter.com/1.1/trends/available.json`


Example Response¶
-----------------



```
[
  {
    "country": "Sweden",
    "countryCode": "SE",
    "name": "Sweden",
    "parentid": 1,
    "placeType": {
      "code": 12,
      "name": "Country"
    },
    "url": "http://where.yahooapis.com/v1/place/23424954",
    "woeid": 23424954
  },
  {
    "country": "United States",
    "countryCode": "US",
    "name": "New Haven",
    "parentid": 23424977,
    "placeType": {
      "code": 7,
      "name": "Town"
    },
    "url": "http://where.yahooapis.com/v1/place/2458410",
    "woeid": 2458410
  },
  {
    "country": "Japan",
    "countryCode": "JP",
    "name": "Sapporo",
    "parentid": 23424856,
    "placeType": {
      "code": 7,
      "name": "Town"
    },
    "url": "http://where.yahooapis.com/v1/place/1118108",
    "woeid": 1118108
  },
  ...
  {
    "country": "United States",
    "countryCode": "US",
    "name": "Providence",
    "parentid": 23424977,
    "placeType": {
      "code": 7,
      "name": "Town"
    },
    "url": "http://where.yahooapis.com/v1/place/2477058",
    "woeid": 2477058
  },
  {
    "country": "United States",
    "countryCode": "US",
    "name": "Cincinnati",
    "parentid": 23424977,
    "placeType": {
      "code": 7,
      "name": "Town"
    },
    "url": "http://where.yahooapis.com/v1/place/2380358",
    "woeid": 2380358
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















