



Integrate | Docs | Twitter Developer Platform 





































































































Integrate



Integration guide
-----------------


This page contains information on several tools and key concepts that you should be aware of as you integrate the users lookup endpoints into your system. We’ve broken the page into a couple of different sections:


* Helpful tools
* Key Concepts
* Authentication
* Developer portal, Projects, and Apps
* Rate limits
* Fields and expansions
* Edge cases


 


### Helpful tools


Before we dive into some key concepts that will help you integrate this endpoint, we recommend that you become familiar with:


#### Postman


Postman is a great tool that you can use to test out an endpoint. Each Postman request includes every path and body parameter to help you quickly understand what is available to you. To learn more about our Postman collections, please visit our "Using Postman" page. 


#### Code samples


Interested in getting set up with this endpoint with some code in your preferred coding language? We’ve got a handful of different code samples available that you can use as a starting point on our Github page.


#### Third-party libraries


Take advantage of one of our communities’ third-party libraries to help you get started. You can find a library that works with the v2 endpoints by looking for the proper version tag.


 


### Key concepts


#### Authentication


All Twitter API v2 endpoints require requests to be authenticated with a set of credentials, also known as keys and tokens. You can use either OAuth 1.0a User Context, App only, or OAuth 2.0 Authorization Code with PKCE to authenticate requests to these endpoints. 


OAuth 1.0a User Context requires you to utilize your API Keys, user Access Tokens, and a handful of other parameters to create an authorization header, which you will then pass with your request. The Access Tokens must be associated with the user that you are making the request on behalf of. If you would like to generate a set of Access Tokens for another user, they must authorize your App using the 3-legged OAuth flow. 


Please note that OAuth 1.0a can be difficult to use. If you are not familiar with this authentication method, we recommend that you use a library, use a tool like Postman, or use OAuth 2.0 to authenticate your requests. If you would like to request a Tweet or private metrics from these endpoints, you will need to use a either OAuth 1.0a User Context or OAuth 2.0 Authorization Code with PKCE, which will ensure that you have the proper permissions from the user that owns that content.  

 


App only just requires that you pass an App only Access Token with your request. You can either generate an App only Access Token from directly within a developer App, or generate one using the POST oauth2/token endpoint.


OAuth 2.0 Authorization Code with PKCE allows for greater control over an application’s scope, and authorization flows across multiple devices. OAuth 2.0 allows you to pick specific fine-grained scopes which give you specific permissions on behalf of a user. 


To enable OAuth 2.0 in your App, you must enable it in your’s App’s authentication settings found in the App settings section of the developer portal.


 











**Please note**


If you are requesting the following fields, OAuth 1.0a User Context or OAuth 2.0 Authorization Code is required: 


* tweet.fields.non\_public\_metrics
* tweet.fields.promoted\_metrics
* tweet.fields.organic\_metrics









#### Developer portal, Projects, and developer Apps


To retrieve a set of authentication credentials that will work with the Twitter API v2 endpoints, you must sign up for a developer account, set up a Project within that account, and created a developer App within that Project. You can then find your keys and tokens within your developer App.   

 


#### Rate limits


Every day, many thousands of developers make requests to the Twitter API. To help manage the sheer volume of these requests, rate limits are placed on each endpoint that limits the number of requests that you can make on behalf of your app or on behalf of an authenticated user. 


The user lookup endpoints are rate limited at both the app-level and the user-level. However, the authenticated user lookup endpoint is rate limited at the user-level


The app-level rate limit means that you, the developer, can only make a certain number of requests to this endpoint over a given period of time from any given App (assumed by the keys and tokens that you are using. The user-level rate limit means that the authenticated user that you are making the request on behalf of can only perform a certain number of times across any developer App.  




The chart below shows the rate limits for each endpoint.




|  |  |  |
| --- | --- | --- |
| **Endpoint** | **HTTP method** | **Rate limit / Level** |
| /2/users | GET | 900 requests per 15 minutes / App and User |
| /2/users/:id | GET | 900 requests per 15 minutes / App and User |
| /2/users/by | GET | 900 requests per 15 minutes / App and User |
| /2/users/by/username/:username | GET | 900 requests per 15 minutes / App and User |
| /2/users/me | GET | 75 requests per 15 minutes / User |


 


#### Fields and expansions


The Twitter API v2 allows users to select exactly which data they want to return from the API using a set of tools called fields and expansions. The expansion parameter allows you to expand objects referenced in the payload. For example, this endpoint allows you to use the pinned\_tweet\_id expansion.


The fields parameter allows you to select exactly which fields within the different data objects you would like to receive. These endpoints delivers user objects primarily. By default, the user object returns the id, name, and username fields. To receive additional fields such as user.created\_at or user.location, you will have to specifically request those using a fields parameter. Some important fields that you may want to consider using in your integration are our Tweet poll data, metrics, annotations, and conversation ID fields.


We’ve added a guide on how to use fields and expansions in our Twitter API v2 data dictionary.  

  




#### Edge cases


* Tweet text is truncated for Retweets. The short term workaround is to expand the referenced Tweet and retrieve the full text from the expansion. This is a bug that we will fix in the future.


 










Next steps
----------






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















