



GET friendships/incoming | Docs | Twitter Developer Platform 





































































































GET friendships/incoming



get-friendships-incoming

GET friendships/incoming
========================




Returns a collection of numeric IDs for every user who has a pending
request to follow the authenticating user.


Resource URL¶
-------------


`https://api.twitter.com/1.1/friendships/incoming.json`


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
| cursor | semi-optional | Causes the list of connections to be broken into pages of no more
than 5000 IDs at a time. The number of IDs returned is not guaranteed to
be 5000 as suspended users are filtered out after connections are
queried. If no cursor is provided, a value of `-1` will be
assumed, which is the first "page."The response from the API will
include a `previous_cursor` and `next_cursor` to
allow paging back and forth. |  | `12893764510938` |
| stringify\_ids | optional | Many programming environments will not consume our Tweet ids due to
their size. Provide this option to have ids returned as strings
instead. |  | `true` |


Example Request¶
----------------


`GET https://api.twitter.com/1.1/friendships/incoming.json`


Example Response¶
-----------------



```
{
  "previous_cursor": 0,
  "ids": [6253282],
  "previous_cursor_str": "0",
  "next_cursor": 0,
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















