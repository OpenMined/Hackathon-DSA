



POST
direct\_messages/welcome\_messages/rules/new | Docs | Twitter Developer Platform 





































































































POST
direct\_messages/welcome\_messages/rules/new



new-welcome-message-rule

POST
direct\_messages/welcome\_messages/rules/new
=================================================




Creates a new Welcome Message Rule that determines which Welcome
Message will be shown in a given conversation. Returns the created rule
if successful.


Requires a JSON POST body and `Content-Type` header to be
set to `application/json`. Setting
`Content-Length` may also be required if it is not
automatically.


Additional rule configurations are forthcoming. For the initial beta
release, the most recently created Rule will always take precedence, and
the assigned Welcome Message will be displayed in the conversation.


See the Welcome
Messages overview to learn how to work with Welcome Messages.


Resource URL¶
-------------


`https://api.twitter.com/1.1/direct_messages/welcome_messages/rules/new.json`


Resource Information¶
---------------------




|  |  |
| --- | --- |
| Response formats | JSON |
| Content-Type | application/json |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |


Welcome Message Rule Object¶
----------------------------




|  |  |
| --- | --- |
| **welcome\_message\_id** (required) | The ID of the Welcome Message that will be sent when this Rule is
triggered. |


Example Request¶
----------------



```
{
  "welcome_message_rule": {
    "welcome_message_id": "844385345234"
  }
}
```

### Example request using Twurl¶



```
twurl -A 'Content-type: application/json' -X POST /1.1/direct_messages/welcome_messages/rules/new.json -d '{"welcome_message_rule": {"welcome_message_id": "844385345234"}}'
```

Example Response¶
-----------------



```
{
  "welcome_message_rule" : {
    "id": "9910934913490319",
    "created_timestamp": "1470182394258",
    "welcome_message_id": "844385345234"
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















