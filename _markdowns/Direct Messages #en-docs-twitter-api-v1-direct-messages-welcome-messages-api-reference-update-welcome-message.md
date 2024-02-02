



PUT
direct\_messages/welcome\_messages/update | Docs | Twitter Developer Platform 





































































































PUT
direct\_messages/welcome\_messages/update



update-welcome-message

PUT
direct\_messages/welcome\_messages/update
=============================================




Updates a Welcome Message by the given ID. Updates to the
`welcome_message` object are atomic. For example, if the
Welcome Message currently has `quick_reply` defined and you
only provde `text`, the `quick_reply` object will
be removed from the Welcome Message.


Resource URL¶
-------------


`https://api.twitter.com/1.1/direct_messages/welcome_messages/update.json`


Resource Information¶
---------------------




|  |  |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |


Parameters¶
-----------




|  |  |
| --- | --- |
| **id** (required) | The id of the Welcome Message that should be updated. |


Example request using Twurl¶
----------------------------



```
twurl -A 'Content-type: application/json' -X PUT '/1.1/direct_messages/welcome_messages/update.json?id=4893198399134' -d ‘
{
  "message_data":{
    "text": "Welcome!"
  }
}
```

Example Response¶
-----------------



```
{
  "name": "Generic Welcome 01"
  "welcome_message": {
    "id": "4893198399134",
    "created_timestamp": "154903045",
    "message_data": {
      "text": "Welcome!"
    }
  },
  "apps": {
    "8829219": {
      "id": "8829219",
      "name": "Furni",
      "url": "https://developer.twitter.com"
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















