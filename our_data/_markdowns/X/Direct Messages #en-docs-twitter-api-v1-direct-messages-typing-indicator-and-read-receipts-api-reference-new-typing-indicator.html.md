
POST
direct\_messages/indicate\_typing | Docs | Twitter Developer Platform 

POST
direct\_messages/indicate\_typing

new-typing-indicator
POST
direct\_messages/indicate\_typing
======================================

Displays a visual typing indicator in the recipient’s Direct Message
conversation view with the sender. Each request triggers a typing
indicator animation with a duration of ~3 seconds.

Usage¶
------

A rudimentary approach would be to invoke an API request on every
keypress or input event, however the application may quickly hit rate
limits. A more sophisticated approach is to capture input events, but
limit API requests to a specified interval based on the behavior of your
users and the rate limit specified below.

Resource URL¶
-------------

`https://api.twitter.com/1.1/direct_messages/indicate_typing.json`

Resource Information¶
---------------------

|  |  |
| --- | --- |
| Response formats | JSON |
| Content-Type | application/json |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 1000 / 15 minutes |

Parameters¶
-----------

|  |  |
| --- | --- |
| **recipient\_id** (required) | The user ID of the user to receive the typing indicator. |

Example request using Twurl¶
----------------------------

```
twurl -X POST /1.1/direct_messages/indicate_typing.json -d "recipient_id=3805104374"
```
HTTP Response Codes¶
--------------------

Response contains no body.

| Code | Message |
| --- | --- |
| 204 | Typing indicator successfully sent. |
| 400 | Missing or invalid parameter(s) included in request. |

Webhook Event¶
--------------

**Coming Soon:** If using the Account
Activity API, the following JSON payload will be sent to your
webhook for all subscribed users.

```
{
  "direct_message_indicate_typing_events": [
    {
      "created_timestamp":"1288834974657",
      "sender_id":"2244994945",
      "target":{
        "recipient_id":"3805104374"
      }
    }
  ],
  "users": {
    // hydrated user objects
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