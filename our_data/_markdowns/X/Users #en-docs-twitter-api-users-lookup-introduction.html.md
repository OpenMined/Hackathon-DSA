
User lookup introduction | Docs | Twitter Developer Platform 

Introduction

Introduction
------------

The RESTful endpoint uses the GET method to return information about a user or group of users, specified by a user ID or a username. The response includes one or many user objects, which deliver fields such as the Follower count, location, pinned Tweet ID, and profile bio. Responses can also optionally include expansions to return the full Tweet object for a user’s pinned Tweet, including the Tweet text, author, and other Tweet fields. 

You can authenticate your request to all users lookup endpoints other than the authenticated user lookup with OAuth 1.0a User Context, App only, or OAuth 2.0 Authorization code with PKCE. However, if you would like to access private metrics or data from private users, you will need to utilize OAuth 1.0a User Context or OAuth 2.0 Authorization Code with PKCE, and pass the authenticated users' Access Token with your request.    

This endpoint is commonly used to receive up-to-date details on a user, to verify that a user exists, or to update your stored details following a compliance event.

### 

### Authenticated user lookup

If authenticating on behalf of other users, it is critical to be able to see who you can make a request on behalf of.

This endpoint requires you to use OAuth 1.0a User Context or OAuth 2.0 Authorization Code with PKCE. It returns information about the authorized user, meaning the user that is associated with the user Access Tokens that you pass with the request.

You can access this endpoint via the GET method. There is a user rate limit of 75 requests per 15 minutes for this endpoint.

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

Relevant tutorials
------------------

Getting started with R and v2 of the Twitter API

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