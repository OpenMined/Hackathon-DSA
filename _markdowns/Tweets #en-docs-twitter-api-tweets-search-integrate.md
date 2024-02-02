



Search Tweets integration reference | Docs | Twitter Developer Platform 





































































































Integrate



How to integrate with the Search Tweets endpoints
-------------------------------------------------


This page contains information on several tools and key concepts that you should be aware of as you integrate the recent search or full archive search endpoints into your system. We’ve split the page into the following sections:


* Helpful tools
* Key concepts
	+ Authentication
	+ Developer portal, Projects, and Apps
	+ Rate limits
	+ Fields and expansions
	+ Metrics
	+ Building search queries
	+ Pagination
	+ Tweet caps
	+ Tweet edits


 


### Helpful tools


Before we start to explore some key concepts, we recommend that you use one of the following tools or code samples to start testing the functionality of these endpoints.


#### Code samples


Interested in getting set up with these endpoints with some code in your preferred coding language? We’ve got a handful of different code samples available that you can use as a starting point on our GitHub page, including a Python client and a Ruby client.


#### Libraries


Take advantage of one of our many community third-party libraries to help you get started. You can find a library that works with the v2 endpoints by looking for the appropriate version tag.


#### Postman


Postman is a great tool that you can use to test out these endpoints. Each Postman request includes all of the given endpoint’s parameters to help you quickly understand what is available to you. To learn more about our Postman collections, please visit our Using Postman page.  

 


### Key concepts


#### Authentication


All Twitter API v2 endpoints require you to authenticate your requests with a set of credentials, also known as keys and tokens. You can use either OAuth 1.0a User Context, OAuth 2.0 App-Only, or OAuth 2.0 Authorization Code with PKCE to authenticate your requests to the recent search endpoint. You must use OAuth 2.0 App-Only when using the full archive search endpoint.


OAuth 2.0 App-Only just requires that you pass an OAuth 2.0 App Access Token with your request. You can either generate an App Access Token from directly within a developer App, or generate one using the POST oauth2/token endpoint.


OAuth 1.0a User Context requires you to utilize your API Keys, user Access Tokens, and a handful of other parameters to create an authorization header, which you will then pass with your request. The Access Tokens must be associated with the user that you are making the request on behalf of. If you would like to generate a set of Access Tokens for another user, they must authorize your App using the 3-legged OAuth flow. 


Please note that OAuth 1.0a can be difficult to use. If you are not familiar with this authentication method, we recommend that you use a library, use a tool like Postman, or use OAuth 2.0 to authenticate your requests. If you would like to request a Tweet or private metrics from these endpoints, you will need to use a either OAuth 1.0a User Context or OAuth 2.0 Authorization Code with PKCE, which will ensure that you have the proper permissions from the user that owns that content.


OAuth 2.0 Authorization Code with PKCE allows for greater control over an application’s scope, and authorization flows across multiple devices. OAuth 2.0 allows you to pick specific fine-grained scopes which give you specific permissions on behalf of a user. 


To enable OAuth 2.0 in your App, you must enable it in your’s App’s authentication settings found in the App settings section of the developer portal.











**Please note**


If you are requesting the following fields, OAuth 1.0a User Context or OAuth 2.0 Authorization Code is required: 


* tweet.fields.non\_public\_metrics
* tweet.fields.promoted\_metrics
* tweet.fields.organic\_metrics
* media.fields.non\_public\_metrics
* media.fields.promoted\_metrics
* media.fields.organic\_metrics









#### 
Developer portal, Projects, and developer Apps


To work with any Twitter API v2 endpoints, you must have signed up for a developer account, set up a Project within that account, and created a developer App within that Project. Your keys and tokens within that developer App will work for these search endpoints.


You can use keys and tokens from a Project with any access level to make requests to the recent search endpoint. However, you will need to use Project with the Pro or Enterprise access level to make requests to the full archive search endpoint. If you have Enterprise access, you will have access to additional functionality, including the availability of additional operators and longer query lengths.  

 


#### Rate limits


Every day, many thousands of developers make requests to the Twitter API. To help manage the volume, rate limits are placed on each endpoint that limits the number of requests that every developer can make on behalf of an app or on behalf of an authenticated user.


There are different rate limits applied for these endpoints depending on which authentication method is being used. The app-level rate limits apply to an App making requests using OAuth 2.0 App-Only, whereas the user-level rate limit applies to requests being made on behalf of the specific authorizing user using OAuth 1.0a User Context or OAuth 2.0 Authorization Code with PKCE. These two rate limits are based on the frequency of requests within a 15-minute window.


For example, an app using OAuth 2.0 App-Only auth to make requests to the recent search endpoint can make 450 requests (including pagination requests) within a 15-minute timeframe. That same app, within the same 15-minute timeframe and with two different authenticated users (using OAuth 1.0a User Context or OAuth 2.0 Authorization Code with PKCE) can make up to 180 requests (including pagination requests) to the recent search endpoint for each authenticated user.  

 


#### Fields and expansions


The Twitter API v2 allows you to select exactly which data you want returned from the API using fields and expansions. The expansion parameter allows you to expand objects referenced in the payload. For example, this endpoint allows you to request poll, place, media, and other objects using the expansions parameter.


The fields parameters allows you to select exactly which fields within the different data objects you would like to receive. By default, the primary Tweet object returned by these endpoints include the id and text fields (in addition to edit\_history\_tweet\_ids for Tweets created after that feature was launched). To receive additional fields such as author\_id or public\_metrics, you will have to specifically request those using the fields parameters. Some important fields that you may want to consider using in your integration are our poll data, metrics, Tweet annotations, and conversation ID fields.


We’ve added a guide on how to use fields and expansions together to our Twitter API v2 data dictionary.  

 


#### Metrics


The Twitter API v2 endpoints allow you to request metrics directly from the returned objects, assuming you pass the proper fields with your request.


There are some limitations with Tweet metrics that you should be aware of, specifically related to user privacy and the following response fields:


* tweet.fields.non\_public\_metrics
* tweet.fields.promoted\_metrics
* tweet.fields.organic\_metrics
* media.fields.non\_public\_metrics
* media.fields.promoted\_metrics
* media.fields.organic\_metrics


  

The noted fields include private metrics data, meaning you must be authorized by the Tweet’s publisher to retrieve this data on their behalf when using the recent search endpoint, meaning you must use OAuth 1.0a User Context. Since you can only use this authentication method using recent search, you will not be able to retrieve these metrics via the full archive search endpoint.


For example, in order to receive non\_public\_metrics for user ID 1234's Tweets, you will need to include access tokens associated with that user in your request. You can have users authorize your app and receive a set of access tokens associated with them by using the 3-legged OAuth flow.


All non\_public\_metrics, organic\_metrics, and promoted\_metrics are only available for Tweets created in the last 30 days. This means that when you are requesting the noted fields, the results will automatically adjust to only include Tweets from the last 30 days.


If these noted fields are requested, only Tweets that are authored by the authenticated user will be returned, all other Tweets will receive an error message.  

 


#### Building search queries


The central feature of these endpoints is their use of a single search query to filter the Tweets that deliver to you. These queries are made up of operators that match on Tweet and user attributes, such as message keywords, hashtags, and URLs. Operators can be combined into queries with boolean logic and parentheses to help refine the query's matching behavior.


You can use our guide on how to build a query to learn more.


We have also written a more in-depth tutorial on how to build high-quality filters for getting Twitter data.  

 


#### Pagination


These endpoints utilize pagination so that responses are returned quickly. In cases where there are more results than what can be sent in a single response (up to 100 Tweets for recent search and 500 for full-archive search) you will need to paginate. Use the max\_results parameter to identify how many results will return per page, and the pagination\_token parameter to return the next page of results. You can learn more by reviewing our pagination guide.  

 


#### Tweet caps


The Search Tweets endpoints are limited in the number of Tweets that they can return in a given month, regardless of pagination.


Regardless of which search endpoint you use, the Tweets returned will count towards the Project-level Tweet caps. Usage is shown in the developer portal, and the 'month' starts on your subscription renewal day shown on the developer portal dashboard.


 


**Tweet edits**


Tweets that are eligible for edits can be edited up to five times in the 30 minutes after the original Tweet was published. The search endpoints will always provide the latest version of the Tweet. If you only request Tweets that were published 30 or more minutes ago, you will always receive the final version of the Tweet. However, if you have a near-real-time use case, and are querying Tweets published within the last thirty minutes, those Tweets could have been edited after you received them. These Tweets can be rehydrated with search, or the Tweet Lookup endpoint to confirm their final state. To learn more about how Tweet edits work, see the Tweet edits fundamentals page.  










Next steps
----------






Make your first request to a Search Tweets endpoint


See a full list of parameters, fields, and more in our API Reference pages


Get support or troubleshoot an error



















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















