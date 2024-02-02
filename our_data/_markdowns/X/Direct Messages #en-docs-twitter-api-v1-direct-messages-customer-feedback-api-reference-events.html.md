
GET feedback/events.json | Docs | Twitter Developer Platform 

GET feedback/events.json

events
GET feedback/events.json
========================

Returns Feedback creation and response events that occur in a
specified time period. Please note that the max to\_time is 24 hours
prior to the current time.

Resource Information¶
---------------------

|  |  |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15 min window (user auth) | 1,000 |

Parameters¶
-----------

|  |  |
| --- | --- |
| **from\_time** (required) | Required on the 1st page. Epoch timestamp in milliseconds.
Example: 1451936737470The range is inclusive. |
| **to\_time** (required) | Required on the 1st page. Epoch timestamp in milliseconds.
Example: 1451936737470The range is inclusive. The max to\_time is
24 hours before current time. Requests for more recent data via this
endpoint will receive an error. |
| **count** (required) | Max number of results returned. Default and max is 100. |
| **cursor** (optiona) | For paging through results. Required for paging through
result sets greater than 1
page.An empty value
indicates you have reached the end of the result set. |

Response Values¶
----------------

|  |  |
| --- | --- |
| **events** | An array of events. |
| **event\_type** | Possible values: feedback.created, feedback.updated |
| **next\_cursor** | Values are unique to a given from\_time/to\_time range. |

Example Result¶
---------------

```
{
  "events":[
    {
      "event_type": "feedback.updated",
      "created_at": "SatDec1517:58:22+00002015",
      "feedback": {
        "created_at": "SatDec1517:58:20+00002015",
        "updated_at": "SatDec1517:59:22+00002015",
        "id": "123456789",
        ...
      }
    },
    {
      "event_type": "feedback.created",
      "created_at": "SatDec1517:59:22+00002015",
      "feedback":{
        "created_at": "SatDec1517:59:22+00002015",
        "updated_at": "SatDec1517:59:22+00002015",
        "id": "123456799",
        ...
      }
    }
  ],
  "next_cursor": "10011"
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