
Attaching location | Docs | Twitter Developer Platform 

Attaching location

Attaching location
==================

Locations can be attached to Direct Messages created with POST direct\_messages/events/new. The location is defined as an attachement object with longitue and latitude coordinates or a Twitter place.  

Example message with shared coordinate attachment
-------------------------------------------------

```
      {
  "event": {
    "type": "message_create",
    "message_create": {
      "target": {
        "recipient_id": "844385345234"
      },
      "message_data": {
        "text": "Here's my location",
        "attachment": {
          "type": "location",
          "location": {
            "type": "shared_coordinate",
            "shared_coordinate": {
              "coordinates": {
                "type": "Point",
                "coordinates": [-122.443893, 37.771718]
              }
            }
          }
        }
      }
    }
  }
}
```

Example message with shared place attachment
--------------------------------------------

```
      {
  "event": {
    "type": "message_create",
      "message_create": {
        "target": {
          "recipient_id": "844385345234"
        },
        "message_data": {
          "text": "Here's my location",
          "attachment": {
            "type": "location",
            "location": {
              "type": "shared_place",
              "shared_place": {
                "place": {
                  "id": "123456"
                }
              }
            }
          }
        }
      }
    }
  }
}
```

**Note:** Not all place IDs are discoverable with GET geo/search. To retrieve all available details for a place ID you may also use GET geo/id/:place\_id.

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