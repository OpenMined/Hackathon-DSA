
Migrate | Docs | Twitter Developer Platform 

Migrate

Comparing Twitter API’s List members endpoints
----------------------------------------------

The v2 List members endpoint group will replace the standard v1.1 GET lists/members, GET lists/memberships, POST lists/members/create and POST lists/members/destroy endpoints. If you have code, apps, or tools that use one of these versions of the List member endpoints, and are considering migrating to the newer Twitter API v2 endpoint, then this set of guides is for you. 

### List members lookup

The v2 List members lookup endpoints will replace the standard  GET lists/members, GET lists/memberships, endpoints.

The following tables compare the standard v1.1 and Twitter API v2 List endpoints:

**List member Lookup**

|  |  |  |
| --- | --- | --- |
| Description | Standard v1.1 | Twitter API v2 |
| HTTP methods supported | `GET` | `GET` |
| Host domain | `https://api.twitter.com` | `https://api.twitter.com` |
| Endpoint path | `/1.1/lists/members.json` | `/2/lists/:id/members` |
| Authentication | OAuth 1.0a User Context
App only | OAuth 1.0a User Context
OAuth 2.0 Authorization Code with PKCE
App only |
| Default request rate limits | 900 requests per 15 min with OAuth 1.0a
75 requests per 15min with App only | 900 requests per 15 min with OAuth 1.0a
900 requests per 15 min with OAuth 2.0
900 requests per 15 min with App only |

**List membership lookup**

|  |  |  |
| --- | --- | --- |
| Description | Standard v1.1 | Twitter API v2 |
| HTTP methods supported | `GET` | `GET` |
| Host domain | `https://api.twitter.com` | `https://api.twitter.com` |
| Endpoint path | `/1.1/lists/memberships.json` | `/2/users/:id/list_memberships` |
| Authentication | OAuth 1.0a User Context
App only | OAuth 1.0a User Context
OAuth 2.0 Authorization Code with PKCE
App only |
| Default request rate limits | 75 requests per 15 min with OAuth 1.0a
75 requests per 15min with App only | 75 requests per 15 min with OAuth 1.0a
75 requests per 15 min with OAuth 2.0
75 requests per 15min with App only |

### 

### Manage List members

The v2 manage List members endpoints will replace the standard POST lists/members/create, POST lists/members/destroy endpoints.

The following tables compare the standard v1.1 and Twitter API v2 List endpoints:

**Add member**

| Description | Standard v1.1 | Twitter API v2 |
| --- | --- | --- |
| HTTP methods supported | POST | POST |
| Host domain | https://api.twitter.com | https://api.twitter.com |
| Endpoint path | /1.1/lists/members/create.json | /2/lists/:id/members |
| Authentication | OAuth 1.0a User Context | OAuth 1.0a User Context
OAuth 2.0 Authorization Code with PKCE |
| Default request rate limits | None | 300 requests per 15 min (per user) |

**Remove member**

| Description | Standard v1.1 | Twitter API v2 |
| --- | --- | --- |
| HTTP methods supported | POST | DELETE |
| Host domain | https://api.twitter.com | https://api.twitter.com |
| Endpoint path | /1.1/lists/members/destroy.json | /2/lists/:id/:user\_id |
| Authentication | OAuth 1.0a User Context | OAuth 1.0a User Context
OAuth 2.0 Authorization Code with PKCE |
| Default request rate limits | None | 300 requests per 15 min (per user) |

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