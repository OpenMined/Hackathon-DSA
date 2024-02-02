
Timelines introduction | Docs | Twitter Developer Platform 

Introduction

Introduction
------------

The Twitter API v2 has three timelines endpoints - reverse chronological home timeline, user Tweet timeline, and user mention timeline. See below for more details.

These three timelines endpoints support edited Tweets. These endpoints will always return the most recent edit, along with the edit history. Any Tweet collected after its 30-minute edit window will represent its final version. Edit metadata includes an array of IDs for all Tweets in its history. For Tweets with no edit history, this array will hold a single ID. For Tweets that have been edited, this array contains multiple IDs, arranged in ascending order reflecting the order of edits, with the most recent version in the last position of the array. To learn more about how Tweet edits work, see the Edit Tweets fundamentals page.   

### Reverse chronological home timeline

This endpoint enables you to retrieve the most recent Tweets, Retweets, and replies posted by the authenticated user and the accounts they follow. 

Since you are making requests on behalf of a user, you must authenticate these endpoints using an OAuth 2.0 Authorization Code Flow with PKCE or OAuth 1.0a User Context. This endpoint has a per-user rate limit of 180 requests per 15-minute window. This endpoint can return every Tweet created on a timeline over the last 7 days as well as the most recent 800 regardless of creation date.

### User Tweet timeline

The user Tweet timeline endpoint provides access to Tweets published by a specific Twitter account.  Retrieving a user's Tweets allows you to build experiences such as showcasing a timeline in a user interface, analyzing a user's Tweets to better understand their content, or creating engagement workflows with their Tweets programmatically. This endpoint gives you access to a single Twitter account's most recent Tweets, Retweets, replies, and Quote Tweets, similar to what may be seen on a user's profile timeline.

Here is a user timeline for @XDevelopers:

Tweets by XDevelopers

The user Tweet timeline endpoint is a REST endpoint that receives a single path parameter to indicate the desired user (by user ID). The endpoint can return the 3,200 most recent Tweets, Retweets, replies, and Quote Tweets posted by the user.

Tweets are delivered in reverse-chronological order, starting with the most recent. Results are paginated up to 100 Tweets per page. Pagination tokens are provided for paging through large sets of Tweets. The Tweet IDs of the newest and the oldest Tweets included in the given page are also provided as metadata, which can also be used for polling timelines for recent Tweets. The user Tweet timeline also supports the ability to specify start\_time and end\_time parameters to receive Tweets that were created within a certain window of time. 

The user Tweet timeline endpoint supports fields and expansions parameters, and returns the new JSON data format.

To successfully make a request to this endpoint, you will need to authorize your request with the OAuth 1.0a User Context, OAuth 2.0 Authorization Code with PKCE, or OAuth 2.0 App-Only authentication methods. You must use OAuth 1.0a User Context or OAuth 2.0 Authorization Code with PKCE when requesting nonpublic metrics, promoted metrics or a protected user's timeline. 

The user Tweet timeline endpoint is designed to support two common usage patterns: 

* "Get a user’s historical Tweets": Requests made to user Tweet timeline in order to receive Tweets authored by the user of interest in chronological order over a specific recent timeframe. The timeframe can be set using the start\_time and end\_time and paginating through the full results.  In some cases, a user’s entire history of Tweets can be retrieved if the user has only authored up to 3,200 Tweets in their account. Tweets included will depend on the public availability and the authentication that is used for the requests.
* "Polling for new Tweets": Requests made to user Tweet timeline on a continual basis, to retrieve new Tweets authored by a specific user. The last Tweet ID received can be set as a parameter for any new requests since the last Tweet.

### User mention timeline

The user mention timeline endpoint allows you to request Tweets mentioning a specific Twitter user, for example, if a Twitter account mentioned @TwitterDev within a Tweet. This will also include replies to Tweets by the user requested. Retrieving a user's mentions allows you to build experiences such as quickly discovering who is replying to a users' Tweets, mentioning or to create engagement workflows with their Tweets programmatically. The endpoint allows you to request to a single user's most recent mentions and replies, similar to what may be seen in a user's notifications for mentions on Twitter.

The user mention timeline is a REST endpoint that receives a single path parameter to indicate the desired user (by user ID). The endpoint can return the 800 most recent mentions for that user.

Tweets are delivered in reverse-chronological order, starting with the most recent. Results are paginated in up to 100 Tweets per page. Pagination tokens are provided for paging through large sets of Tweets. The Tweet IDs of the newest and the oldest Tweets included in the given page are also provided as metadata, which can also be used for polling timelines for recent Tweets, or for navigating through the timeline similar to the v1.1 mentions\_timeline endpoint. The endpoint also supports the ability to specify start\_time and end\_time parameters to receive Tweets that were created within a certain window of time. 

To successfully make a request to this endpoint, you will need to authorize your request with the OAuth 1.0a User Context, OAuth 2.0 Authorization Code with PKCE, or OAuth 2.0 App-Only authentication methods. You must use OAuth 1.0a User Context or OAuth 2.0 Authorization Code with PKCE when requesting non public metrics, promoted metrics or a protected user's timeline. 

The user mention timeline endpoint supports fields and expansions parameters, and returns the new JSON data format.

**Account setup**

To access these endpoints, you will need:

* An approved developer account.
* To authenticate using the keys and tokens from a developer App that is located within a Project.

Learn more about getting access to the Twitter API v2 endpoints in our getting started guide.

Quick start

Jump to example requests

Run in Postman

Try with API Explorer

Supporting resources
--------------------

Learn how to use Postman to make requests

Troubleshoot an error

Visit the API reference page for this endpoint

Tutorials
---------

Measure Tweet performance

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