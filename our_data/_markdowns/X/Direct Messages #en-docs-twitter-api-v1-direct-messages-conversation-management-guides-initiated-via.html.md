
initiated\_via | Docs | Twitter Developer Platform 

initiated\_via

When users communicate with businesses through Direct Messages, they may be guided by Welcome Messages or led to a private conversation via a Direct Message deeplink. In these cases, it can be important for developers to know if another object preceded the DM in conversation. For example, Initiated Via helps a customer service agent see the full conversation history or enable a bot developer to perform A/B testing of different welcome messages.

The initiated\_via object in the Direct Message event object indicates the ID of the Twitter entity that directly preceded the DM in the sender’s context. Currently tweet\_id and welcome\_message\_id may be included. The initiated\_via object is only present if a Twitter entity directly preceded the DM.

initiated\_via object
---------------------

|  |  |
| --- | --- |
| initiated\_via.tweet\_id | The ID of the Tweet with Direct Message Prompt the event was initiated from if one was used. |
| initiated\_via.welcome\_message\_id | The ID of the Welcome Message immediately preceding the event if one was used. |

**Note:** Direct Messages are never referenced as an entity type under the “initiated\_via” object. Developers should continue to rely on IDs for ordering Direct Message events.

Example Direct Message Event
----------------------------

The following Direct Message event was preceded by a Direct Message prompt from a Tweet or a Welcome Message was presented to the user.  

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