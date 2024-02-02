
POST custom\_profiles/new.json | Docs | Twitter Developer Platform 

POST custom\_profiles/new.json

new-profile
POST custom\_profiles/new.json
==============================

Creates a new custom profile. The returned ID should be used with
when publishing a new message with POST
direct\_messages/events/new.

Resource URL¶
-------------

`https://api.twitter.com/1.1/custom_profiles/new.json`

Resource Information¶
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
| **name** (required) | The string ID of of the custom profile. 48 characters max
length. |
| **avatar.media.id** (required) | The string ID of the media to associate with the profile. See Uploading Media for
further details on generating a media ID. |

Example Request¶
----------------

```
{
  "custom_profile": {
    "name": "Jon C, Partner Engineer",
    "avatar": {
        "media": {
           "id": "1234"
       }
    }
}
```
### Example request using Twurl¶

```
twurl -A 'Content-type: application/json' /1.1/custom_profiles/new.json -d ' { "custom_profile": { "name": "Jon C, Partner Engineer", "avatar": { "media": { "id": "1234" } } }'
```
Example Response¶
-----------------

```
{
  "custom_profile": {
    "id": "100001",
    "created_timestamp": "1479767168196",
    "name": "Jon C, Partner Engineer",
    "avatar": {
        "media": {
           "url": "https://pbs.twimg.com/media/Cr7HZpvVYAAYZIX.jpg"
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