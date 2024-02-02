
Manage Tweets introduction | Docs | Twitter Developer Platform 

Introduction

Introduction
------------

Creating and deleting Tweets using the Twitter API is essential for engaging with the public conversation. The new manage Tweets endpoints allow you to do just that and much more. 

We have two available methods for manage Tweets, POST and DELETE. The POST method lets you post polls, quote Tweets, Tweet with reply settings, Tweet with geo, Tweet with media and tag users, and Tweet to Super Followers, in addition to other features. Likewise, the DELETE method allows you to delete a specific Tweet. For the POST method, you can pass in the parameters you are looking for to enable you to further customize your request.

The 'delete Tweet' method has been updated to support edited Tweets. When any Tweet in a chain of Tweet edits is deleted, all Tweets in that edit chain are also deleted. To learn more about Edit Tweet metadata, check out the Edit Tweets fundamentals page.

There is a user rate limit of 200 requests per 15 minutes for the POST method. The DELETE method has a rate limit of 50 requests per 15 minutes. Additionally, there is a limit of 300 requests per 3 hours, including Tweets created with either manage Tweets or manage Retweets. 

Since you are making requests on behalf of a user with the manage Tweets endpoints, you must authenticate with either OAuth 1.0a User Context or OAuth 2.0 Authorization Code with PKCE, and use a user Access Tokens associated with a user that has authorized your App. To generate this user Access Token with OAuth 1.0a, you can use the 3-legged OAuth flow. To generate a user Access Token with OAuth 2.0, you can use the Authorization Code with PKCE grant flow.

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

Learn how to use Postman

Troubleshoot an error

API Reference

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