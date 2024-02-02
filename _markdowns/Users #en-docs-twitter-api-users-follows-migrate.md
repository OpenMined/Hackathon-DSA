



Follows version comparison | Docs | Twitter Developer Platform 





































































































Migrate



Comparing Twitter API’s follows endpoints
-----------------------------------------


### Follows lookup


The v2 follows lookup endpoints will replace the standard v1.1 followers/ids, v1.1 followers/list, v1.1 friends/ids, and v1.1 friends/list endpoints.


The following tables compare the various types of follows lookup endpoints:




|  |  |  |
| --- | --- | --- |
| **Description** | **Standard v1.1** | **Twitter API v2** |
| HTTP methods supported | `GET` | `GET` |
| Host domain | `https://api.twitter.com` | `https://api.twitter.com` |
| Endpoint path | /1.1/friends/ids.json
/1.1/friends/list.json
/1.1/followers/ids.json
/1.1/followers/list.json | /2/users/:id/following
/2/users/:id/followers |
| Authentication | OAuth 1.0a User Context
App only | OAuth 1.0a User Context
OAuth 2.0 Authorization Code with PKCE
App only |
| Default request rate limits | 15 requests per 15 min (per user)
15 requests per 15 min (per app) | 15 requests per 15 min (per user)
15 requests per 15 min (per app) |
| Maximum users per response  | GET friends/id & GET followers/id return a maximum of 5000 users IDs per page.

GET friends/list & GET followers/list return a maximum of 200 user objects per page. | 1000 user objects per page |
| Pagination | Token returns in a next\_cursor field, which can then be passed as the value to the cursor parameter to return the next page of results. | Token returns in a next\_token field, which can then be passed as the value to the token parameter to return the next page of results.
The v2 payload also delivers a previous\_token field, which can also be passed with the pagination\_token parameter to return the previous page of results.

 |
| JSON format | Standard v1.1 format | Twitter API v2 format (determined by fields and expansions request parameters, not backward-compatible with v1.1 formats)
To learn more about how to migrate from the Standard v1.1 format to the Twitter API v2 format, please visit our data formats migration guide. |
| Supports selecting which fields return in the payload |  | ✔ |
| Supports the Tweet annotations fields |  | ✔ |
| Supports requesting new metrics fields |  | ✔ |
| Supports the conversation\_id field |  | ✔ |
| Requires the use of credentials from a developer App associated with a project |  | ✔ |


### 


### Manage follows


The v2 manage follows endpoints will replace the standard v1.1 POST friendships/create and POST friendships/destroy endpoints.


The following tables compare the standard v1.1 and Twitter API v2 create follow endpoints:


#### Follow a user




| Description | Standard v1.1 | Twitter API v2 |
| --- | --- | --- |
| HTTP methods supported | POST | POST |
| Host domain | https://api.twitter.com | https://api.twitter.com |
| Endpoint path | /1.1/friendships/create.json | /2/users/:id/following |
| Authentication | OAuth 1.0a User Context | OAuth 1.0a User Context
OAuth 2.0 Authorization Code with PKCE |
| Default request rate limits | 50 requests per 15 min | 50 requests per 15 min |
| Maximum daily operations per users | 400 | 400 |
| Maximum daily operations per app | 1000 | 1000 |
| Requires use of credentials from a developer App that is associated with a Project |  | ✔️ |


 


#### Unfollow a user


The following tables compare the standard v1.1 and Twitter API v2 delete follow endpoints:




| Description | Standard v1.1 | Twitter API v2 |
| --- | --- | --- |
| HTTP methods supported | POST | DELETE |
| Host domain | https://api.twitter.com | https://api.twitter.com |
| Endpoint path | /1.1/friendships/destroy.json | /2/users/:source\_user\_id/following/:target\_user\_id |
| Authentication | OAuth 1.0a User Context | OAuth 1.0a User Context
OAuth 2.0 Authorization Code with PKCE |
| Default request rate limits | 15 requests per 15 min (per user) | 50 requests per 15 min (per user) |
| Maximum daily operations per app | None | 500 |
| Requires use of credentials from a developer App that is associated with a Project |  | ✔️ |










Other migration resources
-------------------------






Follows lookup: Standard v1.1 to Twitter API v2


Manage follows: Standard v1.1 to Twitter API v2


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















