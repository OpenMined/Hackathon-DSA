



GET
direct\_messages/events/show | Docs | Twitter Developer Platform 





































































































GET
direct\_messages/events/show



get-event

GET
direct\_messages/events/show
================================




Returns a single Direct Message event by the given id.


Resource URL¶
-------------


`https://api.twitter.com/1.1/direct_messages/events/show.json`


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




|  |  |
| --- | --- |
| **id** (required) | The id of the Direct Message event that should be returned. |


Example request using Twurl¶
----------------------------



```
twurl -X GET /1.1/direct_messages/events/show.json?id=110
```

Example Response¶
-----------------



```
{
  "event": 
    "id": "110", 
    "created_timestamp": "5300",
    "type": "message_create",
    "message_create": {
      ...
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















