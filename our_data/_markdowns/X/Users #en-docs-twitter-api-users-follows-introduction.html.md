
Follows introduction | Docs | Twitter Developer Platform 

Introduction

Introduction
------------

Following users is one of the most foundational actions on Twitter. 

We offer two sets of endpoint groups to help you lookup, create, and delete follow relationships: follows lookup and manage follows.  

### Follows lookup

The follows lookup endpoints enable you to explore and analyze relationships between users, which is sometimes called network analysis. Specifically, there are two REST endpoints that return user objects representing who a specified user is following, or who is following a specified user.

You can authenticate this endpoint with either OAuth 1.0a User Context, App only, or OAuth 2.0 Authorization Code with PKCE. You can request up to 1,000 users per request, and pagination tokens will be provided for paging through large sets of results.  

### Manage follows

The manage follows endpoints enable you to follow or unfollow users.

Since you are making requests on behalf of a user, you must authenticate these endpoints with either OAuth 1.0a User Context or OAuth 2.0 Authorization Code with PKCE, and utilize the user Access Tokens associated with the user you are making the request on behalf of. You can generate this user Access Token using the 3-legged OAuth flow (OAuth 1.0a) or using the Authorization Code with PKCE grant flow (OAuth 2.0).

You are limited to 400 follow actions per day on behalf of each authenticated user, and will be limited to 1,000 actions per day per App across all of your authenticated users. For example, if you have five authenticated users, you can follow 400 users per day (per user limit) with two of those users for a total of 800 actions, and will have to split the remaining 200 actions (per app) amongst the remaining three users. This limit does not apply to the unfollow endpoint, which has a separate limit of 500 actions per day (per app).

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