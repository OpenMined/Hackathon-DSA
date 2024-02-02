



POST
direct\_messages/events/new (message\_create) | Docs | Twitter Developer Platform 





































































































POST
direct\_messages/events/new (message\_create)



new-event

POST
direct\_messages/events/new (message\_create)
==================================================




Publishes a new `message_create` event resulting in a
Direct Message sent to a specified user from the authenticating user.
Returns an event if successful. Supports publishing Direct Messages with
optional Quick Reply and media attachment. Replaces behavior currently
provided by POST
direct\_messages/new.


Requires a JSON POST body and `Content-Type` header to be
set to `application/json`. Setting
`Content-Length` may also be required if it is not
automatically.


Resource URL¶
-------------


`https://api.twitter.com/1.1/direct_messages/events/new.json`


Resource Information¶
---------------------




|  |  |
| --- | --- |
| Response formats | JSON |
| Content-Type | application/json |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 24-hour window | 1000 per user; 15000 per app |


Direct Message Rate Limiting¶
-----------------------------


When a message is received from a user you may send up to 5 messages
in response within a 24 hour window. Each message received resets the 24
hour window and the 5 allotted messages. Sending a 6th message within a
24 hour window or sending a message outside of a 24 hour window will
count towards rate-limiting. This behavior only applies when using the
POST direct\_messages/events/new endpoint.


Event Object¶
-------------




|  |  |
| --- | --- |
| **type** (required) | The type of event you are posting. For Direct Messages, use
`message_create` |
| **message\_create.target.recipient\_id** (required) | The ID of the user who should receive the direct message. |
| **message\_create.message\_data** (required) | The `Message Data Object` defining the content to deliver
to the reciepient. |


Message Data Object¶
--------------------




|  |  |
| --- | --- |
| **text** (required) | The text of your Direct Message. URL encode as necessary. Max length
of 10,000 characters. Max length of 9,990 characters if used as a Welcome
Message. |
| **quick\_reply.type** (optional) | The Quick Reply type to present to the user (example requests
below):* **options** - Array of
`Options` objects (20 max).
 |
| **attachment.type** (optional) | The attachment type. Can be media or location. |
| **attachment.media.id** (optional) | A media id to associate with the message. A Direct Message may only
reference a single media\_id. See Uploading
Media for further details on uploading media. |


**Note**


See Attaching
Media to Direct Messages for details on including an image, GIF or
video in Direct Messages.


### Example request¶



```
curl --request POST 
--url https://api.twitter.com/1.1/direct_messages/events/new.json 
--header 'authorization: OAuth oauth_consumer_key="YOUR_CONSUMER_KEY", oauth_nonce="AUTO_GENERATED_NONCE", oauth_signature="AUTO_GENERATED_SIGNATURE", oauth_signature_method="HMAC-SHA1", oauth_timestamp="AUTO_GENERATED_TIMESTAMP", oauth_token="USERS_ACCESS_TOKEN", oauth_version="1.0"' 
--header 'content-type: application/json' 
--data '{"event": {"type": "message_create", "message_create": {"target": {"recipient_id": "RECIPIENT_USER_ID"}, "message_data": {"text": "Hello World!"}}}}'
```


```
twurl -A 'Content-type: application/json' -X POST /1.1/direct_messages/events/new.json -d '{"event": {"type": "message_create", "message_create": {"target": {"recipient_id": "RECIPIENT_USER_ID"}, "message_data": {"text": "Hello World!"}}}}'
```

Example Response¶
-----------------



```
{
"event": {
  "type": "message_create",
  "message_create": {
    "target": {
      "recipient_id": "RECIPIENT_USER_ID"
    },
    "message_data": {
      "text": "Hello World!",
    }
  }
}
}
```

**Note**


See media/entity
documentation for details on returned media object properties.



















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















