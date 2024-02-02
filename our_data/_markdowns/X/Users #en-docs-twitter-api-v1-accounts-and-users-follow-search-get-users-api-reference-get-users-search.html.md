
GET users/search | Docs | Twitter Developer Platform 

GET users/search

get-users-search
GET users/search
================

Provides a simple, relevance-based search interface to public user
accounts on Twitter. Try querying by topical interest, full name,
company name, location, or other criteria. Exact match searches are not
supported.

Only the first 1,000 matching results are available.

Resource URL¶
-------------

`https://api.twitter.com/1.1/users/search.json`

Resource Information¶
---------------------

|  |  |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 900 |

Parameters¶
-----------

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| q | required | The search query to run against people search. |  | *Twitter%20API* |
| page | optional | Specifies the page of results to retrieve. |  | *3* |
| count | optional | The number of potential user results to retrieve per page. This
value has a maximum of 20. |  | *5* |
| include\_entities | optional | The *entities* node will not be included in embedded Tweet
objects when set to *false* . |  | *false* |

Example Request¶
----------------

```
$ curl --request GET 
  --url 'https://api.twitter.com/1.1/users/search.json?q=soccer' 
  --header 'authorization: OAuth oauth_consumer_key="consumer-key-for-app", 
  oauth_nonce="generated-nonce", oauth_signature="generated-signature", 
  oauth_signature_method="HMAC-SHA1", oauth_timestamp="generated-timestamp", 
  oauth_token="access-token-for-authed-user", oauth_version="1.0"'
```

```
$ twurl /1.1/users/search.json?q=soccer
```
Example Response¶
-----------------

```
[
  {user-object},
  {user-object},
  {user-object},
  {user-object},
  {user-object},
  {user-object}
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