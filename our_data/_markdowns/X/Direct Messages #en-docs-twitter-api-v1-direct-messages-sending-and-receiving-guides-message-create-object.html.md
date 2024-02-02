
Message Create Object | Docs | Twitter Developer Platform 

Message Create Object

Message Create Object
=====================

Direct Message Event objects are returned by GET direct\_messages/events/list, GET direct\_messages/events/show and can be consumed in real-time using the Account Activity API. Direct Messages have the type of message\_create.

```
      {
  "type": "message_create",
  "id": "1234858592",
  "created_timestamp": "1392078023603",
  "initiated_via": {
    "tweet_id": "123456",
    "welcome_message_id": "456789"
  },
  "message_create": {
    "target": {
      "recipient_id": "1234858592"
    },
    "sender_id": "3805104374",
    "source_app_id": "268278",
    "message_data": {
      "text": "Blue Bird",
      "entities": {
        "hashtags": [],
        "symbols": [],
        "urls": [],
        "user_mentions": [],
      },
      "quick_reply_response": {
        "type": "options",
        "metadata": "external_id_2"
      },
      "attachment": {
        "type": "media",
        "media": {
         ...
        }
      }
    }
  }
}
```

Top level event object
----------------------

|  |  |
| --- | --- |
| Property | Description |
| type | The type of event. For Direct Messages type will be message\_create. |
| id | The ID of the direct message event. |
| created\_timestamp | Epoch timestamp of when the Direct Message event was created. |
| initiated\_via.tweet\_id | The ID of the Tweet with Direct Message Prompt the conversation was initiated from if one was used. |
| initiated\_via.welcome\_message\_id | The ID of the Welcome Message immediatley preceding the conversation if one was used. |

message\_create object
----------------------

|  |  |
| --- | --- |
| message\_create.target.recipient\_id | The ID of the user receiving the message. |
| message\_create.sender\_id | The ID of the user sending the message. |
| message\_create.source\_app\_id | The ID of the application used to create the event. App details are available in the apps object in JSON payloads containing message\_create events. |
| message\_create.message\_data | A message\_data object. |

message\_data object
--------------------

|  |  |
| --- | --- |
| message\_data.text | The Direct Message text. |
| message\_data.entities | A Twitter entities object. |
| message\_data.quick\_reply\_response | A Quick Reply response object. |
| message\_data.attachment | An attachment object (media) |

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