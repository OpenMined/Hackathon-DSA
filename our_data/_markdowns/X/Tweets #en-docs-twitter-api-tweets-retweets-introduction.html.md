
Retweets | Twitter API | Docs | Twitter Developer Platform 

Introduction

Introduction
------------

Retweeting is one of the core features people use to engage in the public conversation on Twitter. With the Retweets lookup endpoints, you can see a list of accounts that Retweeted a given Tweet. In addition, the new manage Retweets endpoints allow you to Retweet a Tweet or undo a Retweet.

**Account setup**

To access these endpoints, you will need:

* An approved developer account.
* To authenticate using the keys and tokens from a developer App that is located within a Project.

Learn more about getting access to the Twitter API v2 endpoints in our getting started guide.

### 

### Retweets lookup

With the Retweets lookup endpoint, you can retrieve a list of accounts that have Retweeted a Tweet. For this endpoint, pagination tokens will be provided for paging through large sets of results in batches of up to 100 users. 

You can authenticate these endpoints with either OAuth 1.0a User Context, OAuth 2.0 App-Only, or OAuth 2.0 Authorization Code with PKCE. 

### Manage Retweets

The manage Retweets endpoints enable you to Retweet or undo a Retweet of a specified Tweet on behalf of an authenticated account. For this endpoint group, there are two methods available POST and DELETE. The POST method allows you to Retweet a Tweet, and the DELETE method will enable you to undo a Retweet of a given Tweet.

Since you are making requests on behalf of a user, you must authenticate these endpoints with either OAuth 1.0a User Context or OAuth 2.0 Authorization Code with PKCE, and utilize the user Access Tokens associated with the user you are making the request on behalf of. You can generate this user Access Token using the 3-legged OAuth flow (OAuth 1.0a) or using the Authorization Code with PKCE grant flow (OAuth 2.0). You can Retweet a Tweet from your account or an account of an authenticated user. With both endpoints, there is a user rate limit of 50 requests per 15 minutes per endpoint.

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