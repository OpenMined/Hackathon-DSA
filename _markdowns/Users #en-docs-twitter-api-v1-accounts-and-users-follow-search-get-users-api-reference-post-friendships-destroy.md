



POST friendships/destroy | Docs | Twitter Developer Platform 





































































































POST friendships/destroy



post-friendships-destroy

POST friendships/destroy
========================




Allows the authenticating user to unfollow the user specified in the
ID parameter.


Returns the unfollowed user when successful. Returns a string
describing the failure condition when unsuccessful.


Actions taken in this method are asynchronous. Changes will be
eventually consistent.


Resource URL¶
-------------


`https://api.twitter.com/1.1/friendships/destroy.json`


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
| screen\_name | optional | The screen name of the user to unfollow. |  | *twitterdev* |
| user\_id | optional | The ID of the user to unfollow. |  | *2244994945* |


Example Request¶
----------------


`POST https://api.twitter.com/1.1/friendships/destroy.json?user_id=2244994945`


Example Response¶
-----------------



```
{user-object,
  "status": {tweet-object}
}
```

For more detail, see the user-object
definition and the tweet-object
definition.



















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















