



DELETE
direct\_messages/events/destroy | Docs | Twitter Developer Platform 





































































































DELETE
direct\_messages/events/destroy



delete-message-event

DELETE
direct\_messages/events/destroy
======================================




Deletes the direct message specified in the required ID parameter.
The authenticating user must be the recipient of the specified direct
message. Direct Messages are only removed from the interface of the user
context provided. Other members of the conversation can still access the
Direct Messages. A successful delete will return a 204 http response
code with no body content.


**Important**: This method requires an access token with
RWD (read, write & direct message) permissions.


Resource URL¶
-------------


`https://api.twitter.com/1.1/direct_messages/events/destroy.json`


Resource Information¶
---------------------




|  |  |
| --- | --- |
| Response formats | 204 - No Content |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |


Parameters¶
-----------




|  |  |
| --- | --- |
| **id** (required) | The id of the Direct Message event that should be deleted. |


Example request using Twurl¶
----------------------------



```
twurl -X DELETE "/1.1/direct_messages/events/destroy.json?id=938178981337088004"
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















