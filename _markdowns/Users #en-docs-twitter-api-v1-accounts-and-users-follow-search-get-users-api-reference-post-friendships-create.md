



POST friendships/create | Docs | Twitter Developer Platform 





































































































POST friendships/create



post-friendships-create

POST friendships/create
=======================




Allows the authenticating user to follow (*friend*) the user
specified in the ID parameter.


Returns the followed user when successful. Returns a string
describing the failure condition when unsuccessful. If the user is
already friends with the user a HTTP 403 may be returned, though for
performance reasons this method may also return a HTTP 200 OK message
even if the follow relationship already exists.


Actions taken in this method are asynchronous. Changes will be
eventually consistent.


Resource URL¶
-------------


`https://api.twitter.com/1.1/friendships/create.json`


Resource Information¶
---------------------




|  |  |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 24-hour window | 400 per user; 1000 per app |


Parameters¶
-----------




|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| screen\_name | optional | The screen name of the user to follow. |  | *twitterdev* |
| user\_id | optional | The ID of the user to follow. |  | *2244994945* |
| follow | optional | Enable notifications for the target user. |  | *true* |


Example Request¶
----------------



```
curl --request POST 
--url 'https://api.twitter.com/1.1/friendships/create.json?user_id=2244994945&follow=true' 
--header 'authorization: OAuth oauth_consumer_key="YOUR_CONSUMER_KEY", oauth_nonce="AUTO_GENERATED_NONCE", oauth_signature="AUTO_GENERATED_SIGNATURE", oauth_signature_method="HMAC-SHA1", oauth_timestamp="AUTO_GENERATED_TIMESTAMP", oauth_token="USERS_ACCESS_TOKEN", oauth_version="1.0"' 
--header 'content-type: application/json'
```

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















