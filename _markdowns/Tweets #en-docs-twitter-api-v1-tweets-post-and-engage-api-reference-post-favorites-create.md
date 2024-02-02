



POST favorites/create | Docs | Twitter Developer Platform 





































































































POST favorites/create



post-favorites-create

POST favorites/create
=====================




Note: favorites are now known as *likes*.


Favorites (*likes*) the Tweet specified in the ID parameter as
the authenticating user. Returns the favorite Tweet when successful.


The process invoked by this method is asynchronous. The immediately
returned Tweet object may not indicate the resultant favorited status of
the Tweet. A 200 OK response from this method will indicate whether the
intended action was successful or not.


Resource URL¶
-------------


`https://api.twitter.com/1.1/favorites/create.json`


Resource Information¶
---------------------




|  |  |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 24-hour window | 1000 per user; 1000 per app |


Parameters¶
-----------




|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| id | required | The numerical ID of the Tweet to like. |  | *123* |
| include\_entities | optional | The *entities* node will be omitted when set to
*false* . |  | *false* |


Example Request¶
----------------



```
curl --request POST 
--url 'https://api.twitter.com/1.1/favorites/create.json?id=TWEET_ID_TO_FAVORITE' 
--header 'authorization: OAuth oauth_consumer_key="YOUR_CONSUMER_KEY", oauth_nonce="AUTO_GENERATED_NONCE", oauth_signature="AUTO_GENERATED_SIGNATURE", oauth_signature_method="HMAC-SHA1", oauth_timestamp="AUTO_GENERATED_TIMESTAMP", oauth_token="USERS_ACCESS_TOKEN", oauth_version="1.0"' 
--header 'content-type: application/json'
```

Example Response¶
-----------------



```
{tweet-object,
"user": {user-object}
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















