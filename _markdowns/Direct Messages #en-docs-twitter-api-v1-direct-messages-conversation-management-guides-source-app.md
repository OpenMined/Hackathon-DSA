



source\_app | Docs | Twitter Developer Platform 





































































































source\_app



source\_app
===========


Some Twitter accounts may make use of more than one application to send Direct Messages — such as when a human social care app is used alongside a separate bot app to manage the same account. In these cases, it can be helpful for developers to know which app was used to send a given message.


The new source\_app object will return this information for all DMs sent by an account. This object is included in the JSON payload for webhooks and REST endpoints. It is relevant on the read path only — Twitter automatically adds this information based on the app authentication used to post a DM. This value will not be returned in the response for POST events/new.json.


**Note:** This same pattern exists with Tweets with the source property, however the JSON structure is different. Please also note that this object will not be included for DMs received by an authenticating user and is only included for DMs sent by the authenticating user.


source\_app object
------------------




|  |  |
| --- | --- |
| id | The ID of the Twitter app used by the authenticating user to send the DM. |
| name | The name of the Twitter app used by the authenticating user to send the DM. |
| url | The URL of the Twitter app used by the authenticating user to send the DM. |


Example for GET direct\_messages/events/list
--------------------------------------------












```

      {
  "event": {
    "type": "message_create",
    "id": "854103000570187779",
    "created_timestamp": "1492468998459",
    "message_create": {
      "target": {
        "recipient_id": "3340250004"
      },
      "sender_id": "51378538",
      "source_app_id": "268278",
      "message_data": {
        "text": "Hello",
        "entities": {
          "hashtags": [],
          "symbols": [],
          "user_mentions": [],
          "urls": []
        }
      }
    }
  }
  "apps": {
    "268278": {
      "id": "268278",
      "name": "Twitter Web Client",
      "url": "http://twitter.com"
    }
  }
}
    
```






Example for GET direct\_messages/events/show
--------------------------------------------












```

      {
  "events": [
    {
      "type": "message_create",
      "id": "854103000570187779",
      "created_timestamp": "1492468998459",
      "message_create": {
        "target": {
          "recipient_id": "3340250004"
        },
        "sender_id": "51378538",
        "source_app_id": "268278",
        "message_data": {
          "text": "Hello",
          "entities": {
            "hashtags": [],
            "symbols": [],
            "user_mentions": [],
            "urls": []
          }
        }
      }
    },
    {
      "type": "message_create",
      "id": "867807494898188291",
      "created_timestamp": "1495736404524",
      "message_create": {
        "target": {
          "recipient_id": "3340250004"
        },
        "sender_id": "51378538",
        "source_app_id": "9206597",
        "message_data": {
          "text": "World",
          "entities": {
            "hashtags": [],
            "symbols": [],
            "user_mentions": [],
            "urls": []
          }
        }
      }
    },
  ],
  "apps": {
    "9206597": {
      "id": "9206597",
      "name": "BeeToSeaBiz TestApp Awesome",
      "url": "https://twitter.com/beetoseabiz"
    },
    "268278": {
      "id": "268278",
      "name": "Twitter Web Client",
      "url": "http://twitter.com"
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















