



Integrate | Docs | Twitter Developer Platform 





































































































Integrate



Integration guide
-----------------


This page contains information on several tools and critical concepts that you should know as you integrate the List members endpoints into your system. We’ve broken the page into a couple of different sections:


* Helpful tools
* Key Concepts
* Authentication
* Developer portal, Projects, and Apps
* Rate limits
* Fields and expansions
* Pagination


 


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


All Twitter API v2 endpoints require you to authenticate your requests with a set of credentials, also known as keys and tokens. You can use either OAuth 1.0a User Context, OAuth 2.0 Authorization Code with PKCE, or App only to authenticate your requests for the Lists **lookup** endpoints. However, you must authenticate with OAuth 1.0a User Context or OAuth 2.0 for the **manage** Lists endpoints. 


OAuth 1.0a User Context, which means that you must use a set of API Keys and user Access Tokens to make a successful request. The access tokens must be associated with the user that you are making the request on behalf of. If you would like to generate a set of Access Tokens for another user, they must authorize your App using the 3-legged OAuth flow.


Please note that OAuth 1.0a can be difficult to use. If you are not familiar with this authentication method, we recommend that you use a library, use a tool like Postman, or use either OAuth 2.0 or App only to authenticate your requests.


OAuth 2.0 Authorization Code with PKCE allows for greater control over an application’s scope, and authorization flows across multiple devices. OAuth 2.0 allows you to pick specific fine-grained scopes which give you specific permissions on behalf of a user. 


To enable OAuth 2.0 in your App, you must enable it in your’s App’s authentication settings found in the App settings section of the developer portal.


App only just requires that you pass an App only Access Token with your request. You can either generate an App only Access Token directly within a developer App, or generate one using the POST oauth2/token endpoint.


App only just requires that you pass an App only Access Token with your request. You can either generate an App only Access Token directly within a developer App, or generate one using the POST oauth2/token endpoint.






#### Developer portal, Projects, and developer Apps


To retrieve a set of authentication credentials that will work with the Twitter API v2 endpoints, you must sign up for a developer account, set up a Project within that account, and created a developer App within that Project. You can then find your keys and tokens within your developer App.  

 


#### Rate limits


Every day, many thousands of developers make requests to the Twitter API. To help manage the sheer volume of these requests, rate limits are placed on each endpoint that limits the number of requests you can make on behalf of your app or on behalf of an authenticated user. 


Lookup (GET) endpoints are rate limited at both the App-level and the user-level; while manage (POST/DELETE) endpoints are limited at the user-level. The app rate limit means that you, the developer, can only make a certain number of requests to this endpoint over a given period of time from any given App (assumed by using either the API Key and API Secret Key, or the App only Access Token). The user rate limit means that the authenticated user that you are making the request on behalf of can only perform a List lookup a certain number of times across any developer App.


The chart below shows the rate limits for each endpoint.




|  |  |  |
| --- | --- | --- |
| **Endpoint** | **HTTP method** | **Rate limit** |
| /2/lists/:id/members | GET | 900 requests per 15 minutes |
| /2/users/:id/list\_memberships | GET | 75 requests per 15 minutes |
| /2/lists/:id/members | POST | 300 requests per 15 minutes |
| /2/lists/:id/members/:user\_id | DELETE | 300 requests per 15 minutes |


 


#### Fields and expansions


The Twitter API v2 GET endpoint allows users to select exactly which data they want to return from the API using a set of tools called `fields` and `expansions`. The `expansions` parameter allows you to expand objects referenced in the payload. For example, looking up List members allows you to pull the following expansions:


* `pinned\_tweet\_id`


 


The `fields` parameter allows you to select exactly which fields within the different data objects you would like to receive. List members lookup delivers user objects primarily. By default, the user object returns id, name, and username fields. To receive additional fields such as `user.created\_at` or `user.description`, you will have to specifically request those using a user.fields parameter. 


We’ve added a guide on using fields and expansions together to our Twitter API v2 data dictionary.


 


 The chart below shows the field and expansions available for each lookup endpoint:




|  |  |  |
| --- | --- | --- |
| **Endpoint** | **Fields** | **Expansions** |
| /2/lists/:id/members |  `user.fields`
`tweet.fields` |  `pinned\_tweet\_id` |
| /2/users/:id/list\_memberships | list.fields
user.fields | owner\_id |


 


#### Pagination


Looking up membership/members can return a lot of data. To ensure we are returning consistent, high-performing results at any given time, we use pagination. Pagination is a feature in Twitter API v2 endpoints that return more results than can be returned in a single response. When that happens, the data is returned in a series of 'pages'. Learn more about how to paginate through results.


 










Next steps
----------






Visit the API reference page for these endpoint



















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















