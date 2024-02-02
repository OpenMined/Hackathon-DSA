



Likes version comparison | Docs | Twitter Developer Platform 





































































































Migrate



Comparing Twitter API’s Likes endpoints
---------------------------------------


### Likes lookup


#### Users who have liked a Tweet


The liked users endpoint is new functionality for v2, allowing you to get information about a Tweet’s liking users.




| Description | Twitter API v2 |
| --- | --- |
| HTTP methods supported | GET |
| Host domain | https://api.twitter.com |
| Endpoint path | /2/tweets/:id/liking\_users |
| Authentication | OAuth 2.0 Bearer Token
OAuth 1.0a User Context |
| Default request rate limits | 75 requests per 15 min (per App)
75 requests per 15 min (per user) |
| Requires the use of credentials from a developer App that is associated with a Project | ✔️ |


#### 
Tweets liked by a user


The following tables compare the standard v1.1 GET favorites/list endpoint and the Twitter API v2 liked Tweets endpoints:




| Description | Standard v1.1 | Twitter API v2 |
| --- | --- | --- |
| HTTP methods supported | GET | GET |
| Host domain | https://api.twitter.com | https://api.twitter.com |
| Endpoint path | /1.1/favorites/list.json | /2/users/:id/liked\_tweets |
| Authentication | OAuth 1.0a User Context | OAuth 2.0 Bearer Token
OAuth 1.0a User Context |
| Default request rate limits | 75 requests per 15 min | 75 requests per 15 min (per App)
75 requests per 15 min (per user) |
| Data formats | Standard v1.1 format | Twitter API v2 format (determined by fields and expansions request parameters, not backward-compatible with v1.1 formats)
To learn more about how to migrate from the Standard v1.1 format to the Twitter API v2 format, please visit our data formats migration guide. |
| Requires the use of credentials from a developer App that is associated with a Project |  | ✔️ |


### 


### Manage Likes


The v2 manage Likes endpoints replace the v1.1 POST favorites/create and POST favorites/destroy endpoints.


The following tables compare the standard v1.1 and Twitter API v2 manage Like endpoints:


#### Like a Tweet




| Description | Standard v1.1 | Twitter API v2 |
| --- | --- | --- |
| HTTP methods supported | POST | POST |
| Host domain | https://api.twitter.com | https://api.twitter.com |
| Endpoint path | /1.1/favorites/create.json | /2/users/:id/likes |
| Authentication | OAuth 1.0a User Context | OAuth 1.0a User Context |
| Default request rate limits | 1000 requests per 24 hours (per user)
1000 requests per 24 hours (per App) | 50 requests per 15 min (per user)
1000 successful requests per 24 hours (per user, shared with DELETE) |
| Requires the use of credentials from a developer App that is associated with a Project |  | ✔️ |


 


#### Unlike a Tweet




| Description | Standard v1.1 | Twitter API v2 |
| --- | --- | --- |
| HTTP methods supported | POST | DELETE |
| Host domain | https://api.twitter.com | https://api.twitter.com |
| Endpoint path | /1.1/favorites/destroy.json | /2/users/:id/likes/:tweet\_id |
| Authentication | OAuth 1.0a User Context | OAuth 1.0a User Context |
| Default request rate limits | 1000 requests per 24 hours (per user)
1000 requests per 24 hours (per App) | 50 requests per 15 min (per user)
1000 successful requests per 24 hours (per user, shared with POST) |
| Requires the use of credentials from a developer App that is associated with a Project |  | ✔️ |










Other migration resources
-------------------------






Likes lookup: Standard v1.1 to Twitter API v2


Manage Likes: Standard v1.1 to Twitter API v2


Twitter API migration hub



















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















