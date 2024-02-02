
Pinned Lists introduction | Docs | Twitter Developer Platform 

Introduction

Introduction
------------

Pinning lists allows Twitter users to more easily access lists that they've either subscribed to or created themselves.

Since you are making requests on behalf of a user with the these endpoints, you must authenticate them with either OAuth 1.0a User Context or OAuth 2.0 Authorization Code with PKCE, and use the user Access Tokens associated with a user that has authorized your App, which can be generated using the 3-legged OAuth flow (OAuth 1.0a) or the Authorization Code with PKCE grant flow (OAuth 2.0).  

### Pinned List lookup

Pinned List lookup has one available endpoint that allows you to retrieve an authenticated user's pinned Lists. There is a rate limit of 15 requests per 15 minutes for this endpoint.  

### Manage pinned Lists

The manage pinned List endpoints allow you to pin and unpin a List on behalf of an authenticated user. For these endpoints, there are two methods available: POST and DELETE. The POST method allows you to pin a List, and the DELETE method allows you to unpin a List. There is a user rate limit of 50 requests per 15 minutes for both endpoints.

**Account setup**

To access these endpoints, you will need:

* An approved developer account.
* To authenticate using the keys and tokens from a developer App that is located within a Project.

Learn more about getting access to the Twitter API v2 endpoints in our getting started guide.

Quick start

Sample code

Run in Postman

Try with API Explorer

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