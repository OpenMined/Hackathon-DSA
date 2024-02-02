



Send a Direct Message
with custom profile | Docs | Twitter Developer Platform 





































































































Send a Direct Message
with custom profile



attach-profile

Send a Direct Message
with custom profile
=========================================


To attach a custom profile to a Direct Message add a
`event.custom_profile_id` parameter to the POST
direct\_messages/events/new.json request.


*Note:* See full
documentation for all properties. Custom profiles can also be used
with welcome
messages.


Parameters¶
-----------




|  |  |
| --- | --- |
| **event.custom\_profile\_id** | The string ID of the custom profile to attach to the Direct
Message. |


Example Request¶
----------------



```
{
  "event": {
    "type": "message_create",
    "message_create": {
      "target": {
        "recipient_id": "844385345234"
      },
      "message_data": {
        "text": "Hi, my name is Jon. How can I help?",
      },
      "custom_profile_id": "100001"
    }
  }
}
```

### Example request using Twurl¶



```
twurl -A 'Content-type: application/json' -X POST /1.1/direct_messages/events/new.json -d ' { "event": { "type": "message_create", "message_create": { "target": { "recipient_id": "844385345234" }, "message_data": { "text": "Hi, my name is Jon. How can I help?", }, "custom_profile_id": "100001" } } }'
```

Example Response¶
-----------------



```
{
  "event": {
    "type": "message_create",
    "message_create": {
      "target": {
        "recipient_id": "844385345234"
      },
      "sender_id": "1241124",
      "message_data": {
        "text": "Hi, my name is Jon. How can I help?",
      },
      "custom_profile_id":  "100001"
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















