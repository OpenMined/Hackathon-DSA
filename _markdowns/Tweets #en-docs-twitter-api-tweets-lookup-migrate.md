



Tweet lookup version comparison | Docs | Twitter Developer Platform 





































































































Migrate



Comparing Twitter API’s Tweets lookup endpoints
-----------------------------------------------


The v2 Tweets lookup endpoints will replace the standard v1.1 GET statuses/lookup and GET statuses/show endpoints, as well as the Labs Tweet lookup endpoints. If you have code, apps, or tools that use one of these versions of the Tweet lookup endpoint, and are considering migrating to the newer Twitter API v2 endpoint, then this set of guides is for you. 


The following tables compare the various types of Tweets lookup endpoints:  

 




|  |  |  |
| --- | --- | --- |
| **Description** | **Standard v1.1** | **Twitter API v2** |
| HTTP methods supported | `GET` | `GET` |
| Host domain | `https://api.twitter.com` | `https://api.twitter.com` |
| Endpoint path | `/1.1/statuses/show.json` `/1.1/statuses/lookup.json` | `/2/tweets` |
| Authentication | OAuth 1.0a User Context | OAuth 1.0a User Context
OAuth 2.0 App-Only
OAuth 2.0 Authorization Code with PKCE |
| Tweet JSON format | Standard v1.1 format | Twitter API v2 format (determined by fields and expansions request parameters, not backward-compatible with v1.1 formats)
To learn more about how to migrate from the Standard v1.1 format to the Twitter API v2 format, please visit our data formats migration guide. |
| Supports selecting which fields return in the payload |  | ✔ |
| Supports the annotations fields |  | ✔ |
| Supports requesting new metrics fields |  | ✔ |
| Supports the conversation\_id field |  | ✔ |
| Provides Tweet edit history | ✔ | ✔ |
| Requires the use of credentials from a developer App associated with a Project |  | ✔ |










Other migration resources
-------------------------






Tweet lookup: Standard v1.1 to Twitter API v2


Twitter API migration hub


Sample code



















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















