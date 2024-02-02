
Likes introduction | Docs | Twitter Developer Platform 

Introduction

Introduction
------------

Liking Tweets is one of the core features people use to engage in the public conversation on  Twitter. With endpoints in our Likes lookup endpoint group, you can see a list of accounts that have liked a given Tweet, or which Tweets a given account has liked. You could use these endpoints to understand what kind of content a specified account or group of accounts likes. 

### Likes lookup

With endpoints in the Likes lookup group, you can retrieve a list of accounts that have liked a Tweet, or a list of Tweets that an account has liked. These endpoints include:

* Tweets liked by a user - GET /2/users/:id/liked\_tweets
* Users who have liked a Tweet - GET /2/tweets/:id/liking\_users

You can authenticate these endpoints with either OAuth 1.0a User Context or OAuth 2.0 Bearer Token. For the liked Tweets endpoints, pagination tokens will be provided for paging through large sets of results.

The liking users endpoint limits you to a total of 100 liking accounts per tweet for all time.  Additionally, the liked Tweets endpoint is also subject to the monthly Tweet cap applied at the Project level.  

### Manage Likes

The manage Likes endpoints enable you to like or unlike a specified Tweet on behalf of an authenticated account. For this endpoint group, there are two methods available POST and DELETE. The POST method allows you to like a Tweet, and the DELETE method will enable you to unlike a Tweet.

Since you are making requests on behalf of a user, you must authenticate these endpoints with OAuth 1.0a User Context and use the Access Tokens associated with the user, which can be generated using the3-legged OAuth flow. You can like a Tweet from your account or an account of an authenticated user. With both endpoints, there is a user rate limit of 50 requests per 15 minutes per endpoint.   

To access these endpoint, you must have an approved developer account. When authenticating, you must use keys and tokens from a developer App that is located within a Project. 

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