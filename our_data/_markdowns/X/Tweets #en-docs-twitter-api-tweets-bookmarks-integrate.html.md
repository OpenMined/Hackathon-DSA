
Bookmarks integration guide | Docs | Twitter Developer Platform 

Integrate

Integration guide
-----------------

This page contains information on several tools and critical concepts that you should know as you integrate the manage Bookmarks endpoints into your system. We’ve broken the page into a couple of different sections:

* Helpful tools
* Key Concepts
	+ Authentication
	+ Developer portal, Projects, and Apps
	+ Rate limits

### Helpful tools

Before we dive into some key concepts that will help you integrate this endpoint, we recommend that you become familiar with:

#### Postman

Postman is a great tool that you can use to test out an endpoint. Each Postman request includes every path and body parameter to help you quickly understand what is available to you. To learn more about our Postman collections, please visit our "Using Postman" page. 

#### Code samples

Are you interested in getting set up with this endpoint with some code in your preferred coding language? We’ve got a handful of different code samples available that you can use as a starting point on our Github page.

#### Third-party libraries

Take advantage of one of our communities’ third-party libraries to help you get started. You can find a library that works with the v2 endpoints by looking for the proper version tag.

### Key concepts

#### Authentication

All Twitter API v2 endpoints require you to authenticate your requests with a set of credentials, also known as keys and tokens. 

These specific endpoints require the use of OAuth 2.0 Authorization Code Flow with PKCE, which means that you must use a set of keys and user Access Tokens to make a successful request. The Access Tokens must be associated with the user that you are requesting on behalf of. If you want to generate a set of Access Tokens for another user, they must authorize or authenticate your App using an Authorize URL.

Please note that OAuth 2.0 can be tricky to use. If you are not familiar with this authentication method, we recommend using a library or a tool like Postman to properly authenticate your requests.

#### Developer portal, Projects, and developer Apps

To retrieve a set of authentication credentials that will work with the Twitter API v2 endpoints, you must have a developer account, set up a Project within that account, and created a developer App within that Project. You can then find your keys and tokens within your developer App. 

#### Rate limits

Every day, many thousands of developers make requests to the Twitter API. To help manage the sheer volume of these requests, rate limits are placed on each endpoint that limits the number of requests that you can make on behalf of your app or on behalf of an authenticated user. 

These endpoints are rate limited at the user level, meaning that the authenticated user that you are making the request on behalf of can only call the endpoint a certain number of times across any developer App. There is a user rate limit of 180 requests per 15 min window for the GET method. With the GET method of the Bookmarks lookup endpoint you will get back 800 of your most recent Bookmarked Tweets. Additionally, there is a user rate limit of 50 requests per 15 minutes for the POST and DELETE methods. 

Next steps
------------

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