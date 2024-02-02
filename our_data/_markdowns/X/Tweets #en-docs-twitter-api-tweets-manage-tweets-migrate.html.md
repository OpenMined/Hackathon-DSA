
Manage Tweets | Docs | Twitter Developer Platform 

Migrate

Comparing Twitter API’s manage Tweets endpoints
-----------------------------------------------

The v2 manage Tweets endpoints will replace the standard v1.1 POST statuses/update and POST statuses/destroy/:id endpoints. If you have code, apps, or tools that use the v1.1 version of the manage Tweets endpoints and are considering migrating to the newer Twitter API v2 endpoint, then this set of guides is for you.   

The following tables compare the standard v1.1 and Twitter API v2 manage Tweets endpoints:

**Create a Tweet**

| Description | Standard v1.1 | Twitter API v2 |
| --- | --- | --- |
| HTTP methods supported | POST | POST |
| Host domain | https://api.twitter.com | https://api.twitter.com |
| Endpoint path | /1.1/statuses/update.json | /2/tweets |
| Authentication | OAuth 1.0a User Context | OAuth 1.0a User Context
OAuth 2.0 User Context |
| Default request rate limits | None
300 requests per 3-hour window per user, per app. Shared with the v1.1 POST Retweets endpoint. | 200 requests per 15 min per user
300 requests per 3-hour window per user, per app. Shared with the v2 POST Retweets endpoint. |
| Requires the use of credentials from a developer App associated with a Project |  | ✔ |

#### 
Delete a Tweet

| 
Description | Standard v1.1 | Twitter API v2 |
| --- | --- | --- |
| HTTP methods supported | POST | DELETE |
| Host domain | https://api.twitter.com | https://api.twitter.com |
| Endpoint path | /1.1/statuses/destroy/:id.json
  | /2/tweets/:id |
| Authentication | OAuth 1.0a User Context | OAuth 1.0a User Context |
| Default request rate limits | None | 50 requests per 15 min per user |
| Requires the use of credentials from a developer App associated with a Project |  | ✔ |

Other migration resources
-------------------------

Manage Tweets: Standard v1.1 to Twitter API v2

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