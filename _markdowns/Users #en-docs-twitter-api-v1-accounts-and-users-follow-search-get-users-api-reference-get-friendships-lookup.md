



GET friendships/lookup | Docs | Twitter Developer Platform 





































































































GET friendships/lookup



get-friendships-lookup

GET friendships/lookup
======================




Returns the relationships of the authenticating user to the
comma-separated list of up to 100 screen\_names or user\_ids provided.
Values for `connections` can be: `following`,
`following_requested`, `followed_by`,
`none`, `blocking`, `muting`.


Resource URL¶
-------------


`https://api.twitter.com/1.1/friendships/lookup.json`


Resource Information¶
---------------------




|  |  |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 15 |


Parameters¶
-----------




|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| screen\_name | optional | A comma separated list of screen names, up to 100 are allowed in a
single request. |  | *twitterapi twitter* |
| user\_id | optional | A comma separated list of user IDs, up to 100 are allowed in a
single request. |  | *783214 6253282* |


Example Requests¶
-----------------



```
$ curl --request GET 
  --url 'https://api.twitter.com/1.1/friendships/lookup.json?screen_name=andypiper%2Cbinary_aaron%2Ctwitterdev%2Chappycamper%2Charris_0ff' 
  --header 'authorization: OAuth oauth_consumer_key="consumer-key-for-app", 
  oauth_nonce="generated-nonce", oauth_signature="generated-signature", 
  oauth_signature_method="HMAC-SHA1", oauth_timestamp="generated-timestamp", 
  oauth_token="access-token-for-authed-user", oauth_version="1.0"'
```


```
$ twurl /1.1/friendships/lookup.json?screen_name=andypiper,binary_aaron,twitterdev,happycamper,harris_0ff
```

Example Response¶
-----------------



```
[
  {
    "name": "andy piper (pipes)",
    "screen_name": "andypiper",
    "id": 786491,
    "id_str": "786491",
    "connections": [
      "following"
    ]
  },
  {
    "name": "λ🥑. 🍞",
    "screen_name": "binary_aaron",
    "id": 165837734,
    "id_str": "165837734",
    "connections": [
      "following",
      "followed_by"
    ]
  },
  {
    "name": "Twitter Dev",
    "screen_name": "TwitterDev",
    "id": 2244994945,
    "id_str": "2244994945",
    "connections": [
      "following"
    ]
  },
  {
    "name": "Emily Sheehan 🏕",
    "screen_name": "happycamper",
    "id": 63046977,
    "id_str": "63046977",
    "connections": [
      "none"
    ]
  },
  {
    "name": "Harrison Test",
    "screen_name": "Harris_0ff",
    "id": 4337869213,
    "id_str": "4337869213",
    "connections": [
      "following",
      "following_requested",
      "followed_by"
    ]
  }
]
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















