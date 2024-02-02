
Manage Retweets: Standard v1.1 compared to Twitter API v2 | Docs | Twitter Developer Platform 

Manage Retweets: Standard v1.1 compared to Twitter API v2

Manage Retweets: Standard v1.1 compared to Twitter API v2
---------------------------------------------------------

If you have been working with the standard v1.1 POST statuses/retweet/:id, and POST statuses/unretweet/:id  endpoints, the goal of this guide is to help you understand the similarities and differences between the standard and Twitter API v2 Retweets endpoints.

* **Similarities**
	+ Authentication
* **Differences**
	+ Endpoint URLs and HTTP methods
	+ Request limitations
	+ App and Project requirements
	+ Request parameters

### Similarities

#### Authentication

Both the standard v1.1 and Twitter API v2 manage Retweets (POST statuses/retweet/:id, and POST statuses/unretweet/:id) endpoints use OAuth 1.0a User Context. Therefore, if you were previously using one of the standard v1.1 Retweets lookup endpoints, you can continue using the same authentication method if you migrate to the Twitter API v2 version. 

### Differences

#### Endpoint URLs and HTTP methods

* Standard v1.1 endpoints:
	+ https://api.twitter.com/1.1/statuses/retweet/:id.json  
	(Retweets a tweet. Returns the original Tweet with Retweet details embedded)
	+ https://api.twitter.com/1.1/statuses/unretweet/:id.json  
	(Undo a Retweet. Returns the original Tweet with Retweet details embedded)
* Twitter API v2 endpoint:
	+ https://api.twitter.com/2/tweets/:id/retweets  
	(Retweets a given Tweet)
	+ https://api.twitter.com/2/users/:id/retweets/:source\_tweet\_id  
	(Undo a Retweet of a given Tweet)

#### App and Project requirements

The Twitter API v2 endpoints require that you use credentials from a developer App that is associated to a Project when authenticating your requests. All Twitter API v1.1 endpoints can use credentials from standalone Apps or Apps associated with a Project.  

#### Request parameters

The following standard v1.1 request parameters accepted two request query parameters (user\_id or screen\_name). The Twitter API v2 only accepts the numerical user ID, and it must be passed as part of the endpoint path.

| Standard v1.1 | Twitter API v2 |
| --- | --- |
| **id** | **id** |
| **includes\_entities** | No equivalent |

Please note that the Standard v1.1 parameters are passed as query parameters, whereas the Twitter API v2 parameters are passed as body parameters for the POST endpoint or path parameters for the DELETE endpoint.

Also, an id of the user Retweeting a Tweet is not required when using the standard v1.1 endpoints since the Access Tokens passed with OAuth 1.0a User Context infer which user is initiating the Retweet/undoing a Retweet. 

Next steps
----------

Check out our quick start guide for Twitter API v2 manage Retweets

Review the API reference for the v2 Retweet endpoints

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