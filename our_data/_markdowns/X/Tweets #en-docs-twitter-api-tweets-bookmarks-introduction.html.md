
Bookmarks introduction | Docs | Twitter Developer Platform 

Introduction

Introduction
------------

Bookmarks are a core feature of the Twitter app that allows you to “save” Tweets and easily access them later. With these endpoints, you can retrieve, create, delete or build solutions to manage your Bookmarks via the API.  

### Manage Bookmarks

We have two available methods for manage Bookmarks, POST and DELETE. The POST method lets you create Bookmarks. Likewise, the DELETE method allows you to delete a specific Bookmark. 

There is a per-user rate limit of 50 requests per 15 minutes for the POST and DELETE methods.

Since you are making requests on behalf of a user with the manage Bookmarks endpoints, you must authenticate by generating a user Access Token with OAuth 2.0. You can use the Authorization Code with PKCE grant flow to do so. To use this endpoint you must pass in the scopes `tweet.read`, `users.read`, and  `bookmark.write`.

### Bookmarks lookup

The Bookmarks lookup endpoint has one method available, GET. This method allows you to get Bookmarks back from yourself or an authenticated account. Pagination tokens will be provided for paging through large sets of results for this endpoint.

There is a per-user rate limit of 180 requests per 15 min window for the GET method. With this endpoint you will get back 800 of your most recent Bookmarked Tweets.

Since you are making requests on behalf of a user with the lookup Bookmarks endpoints, you must authenticate by generating a user Access Token with OAuth 2.0. You can use the Authorization Code with PKCE grant flow to do so. To use this endpoint you must pass in the scopes `tweet.read`, `users.read`, and `bookmark.read`.

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