
Options Quick Reply | Docs | Twitter Developer Platform 

Options Quick Reply

options
Options Quick Reply
===================

List of up to 20 predefined options presented for a user to choose
from. For use with POST
direct\_messages/events/new (message\_create).

Quick Reply Object¶
-------------------

|  |  |
| --- | --- |
| **quick\_reply.type** (required) | Must be set to `options` |
| **quick\_reply.option** (required) | An array of `options` objects. |

Option Object¶
--------------

|  |  |
| --- | --- |
| **label** (required) | The text label displayed on the button face. Label text is returned
as the user's message response. String, max length of 36 characters
including spaces. Values with URLs are not allowed and will return an
error. |
| **description** (optional) | Optional description text displayed under label text. All options
must have this property defined if property is present in any option.
Text is auto-wrapped and will display on a max of two lines and supports
`n` for controlling line breaks. Description text is not
include in the user's message response. String, max length of 72
characters including spaces. |
| **metadata** (optional) | Metadata that will be sent back in the webhook request. String, max
length of 1,000 characters including spaces. |

Example Request¶
----------------

Although not required, if one option defines the
`description`, then all `options` must contain the
`description`.

```
{
  "event": {
    "type": "message_create",
    "message_create": {
      "target": {
        "recipient_id": "844385345234"
      },
      "message_data": {
        "text": "What's your favorite type of bird?",
        "quick_reply": {
          "type": "options",
          "options": [
            {
              "label": "Red Bird",
              "description": "A description about the red bird.",
              "metadata": "external_id_1"
            },
            {
              "label": "Blue Bird",
              "description": "A description about the blue bird.",
              "metadata": "external_id_2"
            },
            {
              "label": "Black Bird",
              "description": "A description about the black bird.",
              "metadata": "external_id_3"
            },
            {
              "label": "White Bird",
              "description": "A description about the white bird.",
              "metadata": "external_id_4"
            }
          ]
        }
      }
    }
  }
}
```
Example User Response¶
----------------------

The `type` and `metadata` will be present in
the `quick_reply_response` object. The `label` for
the chosen option is sent as the message `text`.

```
{
  "event": {
    "type": "message_create",
    "id": "1234858592",
    "created_timestamp": "1392078023603",
    "message_create": {
      "target": {
        "recipient_id": "1234858592"
      },
      "sender_id": "3805104374",
      "message_data": {
        "text": "Blue Bird",
        "entities": {
          "hashtags": [],
          "symbols": [],
          "urls": [],
          "user_mentions": []
        },
        "quick_reply_response": {
          "type": "options",
          "metadata": "external_id_2"
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