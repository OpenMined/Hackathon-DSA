
Manage Likes: Standard v1.1 compared to Twitter API v2 | Docs | Twitter Developer Platform 

Manage Likes: Standard v1.1 compared to Twitter API v2

Manage Likes: Standard v1.1 compared to Twitter API v2
------------------------------------------------------

If you have been working with the standard v1.1 POST favorites/create and POST favorites/destroy endpoints, the goal of this guide is to help you understand the similarities and differences between the standard v1.1 and Twitter API v2 manage Likes endpoints.

* **Similarities**
	+ OAuth 1.0a User Context
* **Differences**
	+ Endpoint URLs and HTTP methods
	+ Request limitations
	+ App and Project requirements
	+ Request parameters

### Similarities

#### OAuth 1.0a User Context authentication method

Both the endpoint versions support OAuth 1.0a User Context. Therefore, if you were previously using one of the standard v1.1 manage favorites endpoints, you can continue using the same authentication method if you migrate to the Twitter API v2 version.

### Differences

#### Endpoint URLs and HTTP methods

* Standard v1.1 endpoints:
	+ POST https://api.twitter.com/1.1/favorites/create.json  
	(like a Tweet)
	+ POST https://api.twitter.com/1.1/favorites/destroy.json  
	(unlike a Tweet)
* Twitter API v2 endpoint:
	+ POST https://api.twitter.com/2/tweets/:id/likes  
	(like a Tweet)
	+ DELETE https://api.twitter.com/2/tweets/:id/likes/:tweet\_id  
	(unlike a Tweet)

**Request limitations**

The v2 liked Tweets endpoint allows you to request 5 to 100 Tweets per request. You can use pagination tokens and multiple requests to get all of a user’s liked Tweets. The v1.1 GET favorites/list endpoint also allows you to pull all liked  Tweets, but you can pull from 20 to 200 Tweets per request.  

For the v2 liking users endpoint, you are limited to 100 liking users per Tweet.

#### App and Project requirements

The Twitter API v2 endpoints require that you use credentials from a developer App that is associated to a Project when authenticating your requests. All Twitter API v1.1 endpoints can use credentials from standalone Apps or Apps associated with a Project.  

#### Request parameters

The following standard v1.1 request parameters have equivalents in Twitter API v2:

| Standard v1.1 | Twitter API v2 |
| --- | --- |
| id | id |
| includes\_entities | No equivalent |

Please note that the Standard v1.1 parameters are passed as query parameters, whereas the Twitter API v2 parameters are passed as body parameters for the POST endpoint or path parameters for the DELETE endpoint.

Also, an id of the user liking a Tweet is not required when using the standard v1.1 endpoints since the Access Tokens passed with OAuth 1.0a User Context infer which user is initiating the like/unlike. 

Next steps
----------

Check out our quick start guide for Twitter API v2 manage Likes

Review the API reference for the v2 Likes endpoints

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