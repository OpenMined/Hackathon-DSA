
Mutes introduction | Docs | Twitter Developer Platform 

Introduction

Introduction
------------

Muting an account allows you to remove an account's Tweets from your timeline without unfollowing or blocking that account. Muted accounts will not know that you've muted them and you can unmute them at any time. With manage mutes endpoints, developers can create safer experiences for people on Twitter. One example of how to build with manage mutes is an application that allows you to mute accounts that might Tweet about specific topics for a specified length of time. With the mutes lookup endpoint, you can see who you or an authenticated user has muted. This can be useful to determine how you interact with the muted accounts. 

Since you are making requests for private information with mute lookup, and on behalf of a user with manage mutes, you must authenticate these endpoints with either OAuth 1.0a User Context or OAuth 2.0 Authorization Code with PKCE, and use the user Access Tokens associated with a user that has authorized your App, which can be generated using the 3-legged OAuth flow (OAuth 1.0a) or the Authorization Code with PKCE grant flow (OAuth 2.0).

### Mutes lookup

The mutes lookup endpoint allows you to see which accounts the authenticated user has muted. This endpoint has a rate limit of 15 requests per 15 minutes per user.

### Manage mutes

The manage mute endpoints enable you to mute or unmute a specified account on behalf of an authenticated user. For these endpoints, there are two methods available: POST and DELETE. The POST method allows you to mute an account, and the DELETE method allows you to unmute an account. There is a user rate limit of 50 requests per 15 minutes for both the POST and DELETE endpoints.

**Please note:**If a user mutes from Twitter, there is a limit of 200 requests per 15 minutes.

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