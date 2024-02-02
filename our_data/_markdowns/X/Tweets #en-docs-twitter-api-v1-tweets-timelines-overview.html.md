
Overview | Docs | Twitter Developer Platform 

Overview

**Please note:**  

We've recently released the following endpoints within the Twitter API v2. 

|  |  |  |
| --- | --- | --- |
| **v1.1 endpoints** | **Corresponding v2 endpoints** |  |
| GET statuses/user\_timeline | User Tweet timeline | Migration guide |
| GET statuses/user\_mentions | User mention timeline | Migration guide |

Please use the migration guides to see what has changed between the standard v1.1 and v2 versions.

**Important note:**  

This endpoint has been updated to include Tweet edit metadata. Learn more about these metadata on the "Edit Tweets" fundamentals page. 

Overview
--------

**Important notice:** On **June 19, 2019**, we began limiting total GET requests to the v1.1 /statuses/mentions\_timeline and /statuses/user\_timeline endpoints to 100,000 requests per day. This is a total request limit (per endpoint) applied across both user-auth and app-auth requests. This means that in a 24-hour period, a single app can make up to 100,000 requests to /statuses/mentions\_timeline and/or 100,000 requests to /statuses/user\_timeline (with either app or user auth) before hitting this new app-level rate limit. The existing default user-auth and app-auth rate limits remain the same.

A timeline is simply a list, or an aggregated stream of Tweets.  The Twitter API has several endpoints that return a timeline of Tweet data - see the table below for more details:  

| API endpoint | Description |
| --- | --- |
| GET statuses / home\_timeline
 | Returns a collection of the most recent Tweets posted by the authenticating user and the users they follow. |
| GET statuses / user\_timeline | Returns a collection of the most recent Tweets posted by the indicated by the screen\_name or user\_id parameters. |
| GET statuses/mentions\_timeline | Returns the 20 most recent mentions (Tweets containing a users’s @handle) for the authenticating user. |

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