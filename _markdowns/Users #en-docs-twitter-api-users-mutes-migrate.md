



Mutes version comparison | Docs | Twitter Developer Platform 





































































































Migrate



Comparing Twitter API’s mutes endpoints
---------------------------------------


### Mutes lookup


The v2 mutes lookup endpoint will replace the standard v1.1 GET mutes/users/ids and GET mutes/users/list endpoints.


The following tables compare the standard v1.1 and Twitter API v2 mute endpoints:  

 




| Description | Standard v1.1 | Twitter API v2 |
| --- | --- | --- |
| HTTP methods supported | ******GET****** | ******GET****** |
| Host domain | ******https://api.twitter.com****** | ******https://api.twitter.com****** |
| Endpoint path | ******/1.1/mutes/users/ids.json******
/1.1/mutes/users/list.json | ******/2/users/:id/muting****** |
| Authentication | OAuth 1.0a User Context | OAuth 1.0a User Context
OAuth 2.0 Authorization Code with PKCE |
| Default request rate limits | 15 requests per 15 min (per user) | 15 requests per 15 min (per user) |
| Data formats | Standard v1.1 format | Twitter API v2 format (determined by fields and expansions request parameters, not backward-compatible with v1.1 formats)
To learn more about how to migrate from the Standard v1.1 format to the Twitter API v2 format, please visit our data formats migration guide. |
| Requires use of credentials from a developer App that is associated with a Project |  | ✔️ |


 


### Manage mutes


The v2 manage mutes endpoints will replace the standard v1.1 POST mutes/users/create and POST mutes/users/destroy endpoints.


The following tables compare the standard v1.1 and Twitter API v2 mute endpoints:


#### Mute a user




| Description | Standard v1.1 | Twitter API v2 |
| --- | --- | --- |
| HTTP methods supported | POST | POST |
| Host domain | https://api.twitter.com | https://api.twitter.com |
| Endpoint path | /1.1/mutes/users/create.json | /2/users/:id/muting |
| Authentication | OAuth 1.0a User Context | OAuth 1.0a User Context
OAuth 2.0 Authorization Code with PKCE |
| Default request rate limits | 50 requests per 15 min | 50 requests per 15 min |
| Requires use of credentials from a developer App that is associated with a Project |  | ✔️ |


 


#### Unmute a user


The following tables compare the standard v1.1 and Twitter API v2 unmute endpoints:




| Description | Standard v1.1 | Twitter API v2 |
| --- | --- | --- |
| HTTP methods supported | POST | DELETE |
| Host domain | https://api.twitter.com | https://api.twitter.com |
| Endpoint path | /1.1/mutes/users/destroy.json | /2/users/:source\_user\_id/muting/:target\_user\_id |
| Authentication | OAuth 1.0a User Context | OAuth 1.0a User Context
OAuth 2.0 Authorization Code with PKCE |
| Default request rate limits | 50 requests per 15 min | 50 requests per 15 min |
| Requires use of credentials from a developer App that is associated with a Project |  | ✔️ |










Other migration resources
-------------------------






Manage mutes: Standard v1.1 to Twitter API v2


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















