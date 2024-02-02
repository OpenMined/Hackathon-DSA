



GET custom\_profiles/:id | Docs | Twitter Developer Platform 





































































































GET custom\_profiles/:id



get-profile

GET custom\_profiles/:id
========================


Returns a custom profile that was created with POST
custom\_profiles/new.json.


Resource URL¶
-------------


`https://api.twitter.com/1.1/custom_profiles/:id.json`


Resource Information¶
---------------------




|  |  |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 24 hour window (user auth) | Yes (180 / 15 min) |


Parameters¶
-----------




|  |  |
| --- | --- |
| **id** (required) | The string ID of the custom profile that should be returned.
Provided in resource URL. |


Example request using Twurl¶
----------------------------



```
twurl -X GET /1.1/custom_profiles/100001
```

Example Response¶
-----------------



```
{
  "custom_profile": {
    "id": "100001",
    "created_timestamp": "1479767168196",
    "name": "Jon C, Partner Engineer",
    "avatar": {
        "media": {
           "url": "https://pbs.twimg.com/media/Cr7HZpvVYAAYZIX.jpg"
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















