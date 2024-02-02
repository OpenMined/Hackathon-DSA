



GET trends/closest | Docs | Twitter Developer Platform 





































































































GET trends/closest



get-trends-closest

GET trends/closest
==================




Returns the locations that Twitter has trending topic information
for, closest to a specified location.


The response is an array of "locations" that encode the location's
`WOEID` and some other human-readable information such as a
canonical name and country the location belongs in.


Note: The "where on earth identifier" or WOEID, is a legacy
identifier created by Yahoo and has been deprecated. Twitter API v1.1
still uses the numeric value to identify town and country trend
locations. Reference our legacy blog
post, or archived
data. The url returned in the response,
`where.yahooapis.com` is no longer valid.


Resource URL¶
-------------


`https://api.twitter.com/1.1/trends/closest.json`


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
| lat | required | If provided with a *long* parameter the available trend
locations will be sorted by distance, nearest to furthest, to the
co-ordinate pair. The valid ranges for longitude is -180.0 to +180.0
(West is negative, East is positive) inclusive. |  | *37.781157* |
| long | required | If provided with a *lat* parameter the available trend
locations will be sorted by distance, nearest to furthest, to the
co-ordinate pair. The valid ranges for longitude is -180.0 to +180.0
(West is negative, East is positive) inclusive. |  | *-122.400612831116* |


Example Request¶
----------------


`GET https://api.twitter.com/1.1/trends/closest.json?lat=37.781157&long=-122.400612831116`


Example Response¶
-----------------



```
[
  {
    "country": "Australia",
    "countryCode": "AU",
    "name": "Australia",
    "parentid": 1,
    "placeType": {
      "code": 12,
      "name": "Country"
    },
    "url": "http://where.yahooapis.com/v1/place/23424748",
    "woeid": 23424748
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















