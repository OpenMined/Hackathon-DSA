



POST saved\_searches/create | Docs | Twitter Developer Platform 





































































































POST saved\_searches/create



post-saved\_searches-create

POST saved\_searches/create
===========================




Create a new saved search for the authenticated user. A user may only
have 25 saved searches.


Resource URL¶
-------------


`https://api.twitter.com/1.1/saved_searches/create.json`


Resource Information¶
---------------------




|  |  |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |


Parameters¶
-----------




|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| query | required | The query of the search the user would like to save. |  |  |


Example Request¶
----------------


`POST https://api.twitter.com/1.1/saved_searches/create.json?query=sandwiches`


Example Response¶
-----------------



```
{
  "created_at": "Fri Aug 24 22:08:58 +0000 2012", 
  "id": 158598597, 
  "id_str": "158598597", 
  "name": "sandwiches", 
  "position": null, 
  "query": "sandwiches"
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















