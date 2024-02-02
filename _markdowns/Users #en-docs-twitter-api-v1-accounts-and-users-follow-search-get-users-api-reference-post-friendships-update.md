



POST friendships/update | Docs | Twitter Developer Platform 





































































































POST friendships/update



post-friendships-update

POST friendships/update
=======================




Turn on/off Retweets and device notifications from the specified
user.


Resource URL¶
-------------


`https://api.twitter.com/1.1/friendships/update.json`


Resource Information¶
---------------------




|  |  |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |


Parameters¶
-----------




|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| screen\_name | optional | The screen name of the user being followed. |  | *twitterdev* |
| user\_id | optional | The ID of the user being followed. |  | *2244994945* |
| device | optional | Turn on/off device notifications from the target user. |  | *true* |
| retweets | optional | Turn on/off Retweets from the target user. |  | *false* |


Example Request¶
----------------


`twurl -X POST /1.1/friendships/update.json?user_id=2244994945`


Example Response¶
-----------------



```
{
  "relationship": {
    "source": {
      "id": 63046977,
      "id_str": "63046977",
      "screen_name": "happycamper",
      "following": true,
      "followed_by": false,
      "live_following": false,
      "following_received": null,
      "following_requested": false,
      "notifications_enabled": false,
      "can_dm": false,
      "blocking": false,
      "blocked_by": false,
      "muting": false,
      "want_retweets": true,
      "all_replies": false,
      "marked_spam": false
    },
    "target": {
      "id": 2244994945,
      "id_str": "2244994945",
      "screen_name": "TwitterDev",
      "following": false,
      "followed_by": true,
      "following_received": false,
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















