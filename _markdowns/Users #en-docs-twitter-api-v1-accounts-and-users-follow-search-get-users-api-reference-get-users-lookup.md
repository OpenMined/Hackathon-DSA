



GET users/lookup | Docs | Twitter Developer Platform 





































































































GET users/lookup



get-users-lookup

GET users/lookup
================




Returns fully-hydrated user
objects for up to 100 users per request, as specified by
comma-separated values passed to the `user_id` and/or
`screen_name` parameters.


This method is especially useful when used in conjunction with
collections of user IDs returned from GET
friends / ids and GET
followers / ids.


GET
users / show is used to retrieve a single user object.


There are a few things to note when using this method.


* You must be following a protected user to be able to see their most
recent status update. If you don't follow a protected user their status
will be removed.
* The order of user IDs or screen names may not match the order of
users in the returned array.
* If a requested user is unknown, suspended, or deleted, then that
user will not be returned in the results list.
* If none of your lookup criteria can be satisfied by returning a user
object, a HTTP 404 will be thrown.
* You are strongly encouraged to use a POST for larger requests.


Resource URL¶
-------------


`https://api.twitter.com/1.1/users/lookup.json`


Resource Information¶
---------------------




|  |  |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 900 |
| Requests / 15-min window (app auth) | 300 |


Parameters¶
-----------




|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| screen\_name | optional | A comma separated list of screen names, up to 100 are allowed in a
single request. You are strongly encouraged to use a POST for larger (up
to 100 screen names) requests. |  | *twitterapi twitter* |
| user\_id | optional | A comma separated list of user IDs, up to 100 are allowed in a
single request. You are strongly encouraged to use a POST for larger
requests. |  | *783214 6253282* |
| include\_entities | optional | The *entities* node that may appear within embedded statuses
will not be included when set to *false*. |  | *false* |
| tweet\_mode | optional | Valid request values are compat and extended, which give
compatibility mode and extended mode, respectively for Tweets that
contain over 140 characters |  | *false* |


Example Requests¶
-----------------



```
$ curl --request GET 
  --url 'https://api.twitter.com/1.1/users/lookup.json?user_id=783214,6253282' 
  --header 'authorization: OAuth oauth_consumer_key="consumer-key-for-app", 
  oauth_nonce="generated-nonce", oauth_signature="generated-signature", 
  oauth_signature_method="HMAC-SHA1", oauth_timestamp="generated-timestamp", 
  oauth_version="1.0"'
```


```
$ twurl /1.1/users/lookup.json?user_id=783214,6253282,2244994945
```

Example Response¶
-----------------



```
[
  {
    {user-object},
    {user-object},
    {user-object}
  }
]
```

For more detail, see the user-object
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















