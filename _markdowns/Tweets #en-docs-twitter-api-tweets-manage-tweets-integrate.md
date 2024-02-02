



Manage Tweets integration guide | Docs | Twitter Developer Platform 





































































































Integrate



Integration guide
-----------------


This page contains information on several tools and key concepts that you should be aware of as you integrate the manag Tweets endpoints into your system. We’ve broken the page into a couple of different sections:


* Helpful tools
* Key Concepts
* Authentication
* Developer portal, Projects, and Apps
* Rate limits
* Source labels
* Profile settings
* Adding media to a Tweet


 


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


All Twitter API v2 endpoints require you to authenticate your requests with a set of credentials, also known as keys and tokens. 


These specific endpoints requires the use of OAuth 1.0a User Context, which means that you must use a set of API keys and user Access Tokens to make a successful request. The Access Tokens must be associated with the user that you are making the request on behalf of. If you would like to generate a set of Access Tokens for another user, they must authorize or authenticate your App using the 3-legged OAuth flow.


Please note that OAuth 1.0a can be difficult to use. If you are not familiar with this authentication method, we recommend that you use a library, use a tool like Postman, or use OAuth 2.0 to authenticate your requests.


OAuth 2.0 Authorization Code with PKCE allows for greater control over an application’s scope, and authorization flows across multiple devices. OAuth 2.0 allows you to pick specific fine-grained scopes which give you specific permissions on behalf of a user. 


To enable OAuth 2.0 in your App, you must enable it in your’s App’s authentication settings found in the App settings section of the developer portal.


 






#### Developer portal, Projects, and developer Apps


To retrieve a set of authentication credentials that will work with the Twitter API v2 endpoints, you must have a developer account, set up a Project within that account, and created a developer App within that Project. You can then find your keys and tokens within your developer App.   

 


#### Rate limits


Every day, many thousands of developers make requests to the Twitter API. To help manage the sheer volume of these requests, rate limits are placed on each endpoint that limits the number of requests that you can make on behalf of your app or on behalf of an authenticated user.   




These endpoints are rate limited at the user level, meaning that the authenticated user that you are making the request on behalf of can only call the endpoint a certain number of times across any developer App. There is a user rate limit of 200 requests per 15 minutes for the POST method. The DELETE method has a rate limit of 50 requests for 15 minutes. Additionally, there is a limit of 300 requests per 3 hours, including Tweets created with either manage Tweets or manage Retweets.  

 


#### Source labels


Your App name and website URL will be shown as the source label within metadata for any Tweets created programmatically by your application. If you change the use case of a Twitter App, be sure to update the use case in these settings in order to ensure you are in compliance with the Developer Terms.  

 


#### Profile settings


You can only add a location to Tweets if you have geo enabled in your profile settings. If you don’t have geo enabled, you can still add a location parameter in your request body, but it won’t get attached to your Tweet. The same is also true for tagging users in images. If the user you’re tagging doesn’t have photo-tagging enabled, their names won’t show up in the list of tagged users even though the Tweet is successfully created.   

 


#### Adding media to a Tweet


#### Currently, isn’t a way to fully upload media using v2 of the Twitter API currently. However, you attach previously uploaded media to a Tweet. You can use media IDs that have been already uploaded using the v1 media endpoint or Twitter Media Studio. These media ids must be your own or that of an authenticated user.










Next steps
----------






API reference



















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















