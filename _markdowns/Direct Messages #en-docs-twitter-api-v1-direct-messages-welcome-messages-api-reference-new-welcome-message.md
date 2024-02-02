



POST
direct\_messages/welcome\_messages/new | Docs | Twitter Developer Platform 





































































































POST
direct\_messages/welcome\_messages/new



new-welcome-message

POST
direct\_messages/welcome\_messages/new
===========================================




Creates a new Welcome Message that will be stored and sent in the
future from the authenticating user in defined circumstances. Returns
the message template if successful. Supports publishing with the same
elements as Direct Messages (e.g. Quick Replies, media attachments).


Requires a JSON POST body and `Content-Type` header to be
set to `application/json`. Setting
`Content-Length` may also be required if it is not
automatically.


See the Welcome
Messages overview to learn how to work with Welcome Messages.


Resource URL¶
-------------


`https://api.twitter.com/1.1/direct_messages/welcome_messages/new.json`


Resource Information¶
---------------------




|  |  |
| --- | --- |
| Response formats | JSON |
| Content-Type | application/json |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |


Welcome Message Object¶
-----------------------




|  |  |
| --- | --- |
| **message\_data** (required) | The `Message Data Object` defining the content of the
message template. See POST
direct\_messages/events/new (message\_create) for Message Data object
details. |
| **name** (optional) | A human readable name for the Welcome Message. This is not displayed
to the user. Max length of 100 alpha numeric characters including
hyphens, underscores, spaces, hashes and at signs. |



> 
> **Note**
> 
> 
> See Attaching
> Media to Direct Messages for details on including an image, GIF or
> video in Direct Messages.
> 
> 
> 


Example Request¶
----------------



```
{
  "welcome_message" : {
    "name": "simple_welcome-message 01",
    "message_data": {
      "text": "Welcome!",
      "attachment": {
        "type": "media",
        "media": {
          "id": "48909183894931"
        }
      }
    }
  }
}
```

### Example request using Twurl¶



```
twurl -A 'Content-type: application/json' /1.1/direct_messages/welcome_messages/new.json -d '{"name": "simple_welcome-message 01", "welcome_message": {"message_data": {"text": "Welcome!", "attachment": {"type": "media", "media": {"id": "48909183894931"}}}}}'
```

Example Response¶
-----------------



```
{
  "welcome_message" : {
    "id": "844385345234",
    "created_timestamp": "1470182274821",
    "message_data": {
      "text": "Welcome!",
      "attachment": {
        "type": "media",
        "media": {
          ...
        }
      }
    }
  }
  "name": "simple_welcome-message 01"
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















