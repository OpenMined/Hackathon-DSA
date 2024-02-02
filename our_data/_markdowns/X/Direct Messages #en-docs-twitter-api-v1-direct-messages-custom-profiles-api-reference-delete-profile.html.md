
DELETE
custom\_profiles/destroy.json | Docs | Twitter Developer Platform 

DELETE
custom\_profiles/destroy.json

delete-profile
DELETE
custom\_profiles/destroy.json
====================================

Deletes a custom profile that was created with POST
custom\_profiles/new.json.

Resource URL¶
-------------

`https://api.twitter.com/1.1/custom_profiles/destroy.json`

Resource information¶
---------------------

|  |  |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 24 hour window (user auth) | Yes (1000 / 1 day) |

Parameters¶
-----------

|  |  |
| --- | --- |
| **id** (required) | The string ID of the custom profile to destroy. |

Example request using Twurl¶
----------------------------

```
twurl -X DELETE /1.1/custom_profiles/destroy.json?id=100001
```
Example Response¶
-----------------

Calling this multiple times on a valid id will return a 204 response
code.

```
HTTP 204 with empty body
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