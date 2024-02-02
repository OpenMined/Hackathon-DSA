
GET friendships/show | Docs | Twitter Developer Platform 

GET friendships/show

get-friendships-show
GET friendships/show
====================

Returns detailed information about the relationship between two
arbitrary users.

Resource URL¶
-------------

`https://api.twitter.com/1.1/friendships/show.json`

Resource Information¶
---------------------

|  |  |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 180 |
| Requests / 15-min window (app auth) | 15 |

Parameters¶
-----------

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| source\_id | optional | The user\_id of the subject user. |  | *783214* |
| source\_screen\_name | optional | The screen\_name of the subject user. |  | *Twitter* |
| target\_id | optional | The user\_id of the target user. |  | *2244994945* |
| target\_screen\_name | optional | The screen\_name of the target user. |  | *TwitterDev* |

Example Request¶
----------------

`GET https://api.twitter.com/1.1/friendships/show.json?source_screen_name=twitterdev&target_screen_name=twitter`

Example Response¶
-----------------

```
{
  "relationship": {
    "source": {
      "id": 783214,
      "id_str": "783214",
      "screen_name": "Twitter",
      "following": true,
      "followed_by": true,
      "live_following": false,
      "following_received": null,
      "following_requested": null,
      "notifications_enabled": null,
      "can_dm": true,
      "blocking": null,
      "blocked_by": null,
      "muting": null,
      "want_retweets": null,
      "all_replies": null,
      "marked_spam": null
    },
    "target": {
      "id": 2244994945,
      "id_str": "2244994945",
      "screen_name": "TwitterDev",
      "following": true,
      "followed_by": true,
      "following_received": null,
      "following_requested": null
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