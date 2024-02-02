



GET feedback/show/:id.json | Docs | Twitter Developer Platform 





































































































GET feedback/show/:id.json



show

GET feedback/show/:id.json
==========================


Returns a single Feedback response for the specified ID in the
URL.


Resource Information¶
---------------------




|  |  |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15 min window (user auth) | 180 |


Parameters¶
-----------




|  |  |
| --- | --- |
| **feedback\_id** (required) | Required in path. |


Response Values¶
----------------




|  |  |
| --- | --- |
| **score** | The user provided score response. 1­5 if type is CSAT. 0­10 if type is
NPS. |
| **text** | The user provided text response. |


Example Result¶
---------------



```
{
  "created_at": "SatDec1517:58:20+00002015",
  "updated_at": "SatDec1517:59:22+00002015",
  "id": "123456789"
  "text": "Thankyouforbeingaloyalcustomer!",
  "media_id_str": 12345,
  "response": {
    "score": {
      "created_at": "SatDec1518:59:22+00002015",
      "value": 1
    },
    "text": {
      "created_at": "SatDec1518:59:52+00002015",
      "value": "I<3thisbiz"
    }
  }
}
```



Note



Response object will only be present if data is available.




















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















