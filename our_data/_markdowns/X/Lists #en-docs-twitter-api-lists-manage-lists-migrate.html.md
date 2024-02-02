
Migrate | Docs | Twitter Developer Platform 

Migrate

Comparing Twitter API’s Lists endpoints
---------------------------------------

The v2 manage Lists endpoints will eventually replace POST lists/create, POST lists/destroy, and POST lists/update. If you have code, apps, or tools that use an older version of these endpoints and are considering migrating to the newer Twitter API v2, then this guide is for you. 

The following tables compare the standard v1.1 and Twitter API v2 List endpoints:  

**Create a List**

| Description | Standard v1.1 | Twitter API v2 |
| --- | --- | --- |
| HTTP methods supported | POST | POST |
| Host domain | https://api.twitter.com | https://api.twitter.com |
| Endpoint path | /1.1/lists/create.json | /2/lists |
| Authentication | OAuth 1.0a User Context | OAuth 1.0a User Context |
| Default request rate limits | None | 300 requests per 15 min (per user) |

**Delete a List**

| Description | Standard v1.1 | Twitter API v2 |
| --- | --- | --- |
| HTTP methods supported | POST | DELETE |
| Host domain | https://api.twitter.com | https://api.twitter.com |
| Endpoint path | /1.1/lists/destroy.json | /2/lists/:id |
| Authentication | OAuth 1.0a User Context | OAuth 1.0a User Context |
| Default request rate limits | None | 300 requests per 15 min (per user) |

**Update a List**

| Description | Standard v1.1 | Twitter API v2 |
| --- | --- | --- |
| HTTP methods supported | POST | PUT |
| Host domain | https://api.twitter.com | https://api.twitter.com |
| Endpoint path | /1.1/lists/update.json | /2/lists/:id |
| Authentication | OAuth 1.0a User Context | OAuth 1.0a User Context |
| Default request rate limits | None | 300 requests per 15 min (per user) |

### 

To access the Twitter API v2 endpoints, you must sign up for a developer account. When authenticating, you must use keys and tokens from a developer App that is located within a Project. 

Learn more about getting access to the Twitter API v2 endpoints in our getting started page.

Quick start

Sample code

Run in Postman

Supporting resources
--------------------

Learn how to use Postman to make requests

Troubleshoot an error

Visit the API reference page for this endpoint

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