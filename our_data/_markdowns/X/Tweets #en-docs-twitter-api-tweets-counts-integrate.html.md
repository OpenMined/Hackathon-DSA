
Integrate | Docs | Twitter Developer Platform 

Integrate

How to integrate with the Tweets counts endpoints
-------------------------------------------------

This page contains information on several tools and key concepts that you should be aware of as you integrate the recent or full-archive Tweet counts endpoints into your system. We’ve split the page into the following sections:

* Helpful tools
* Key concepts
	+ Authentication
	+ Developer portal, Projects, and Apps
	+ Rate limits
	+ Building queries
	+ Pagination

### Helpful tools

Before we start to explore some key concepts, we recommend that you use one of the following tools or code samples to start testing the functionality of these endpoints.

#### Code samples

Interested in getting set up with these endpoints with some code in your preferred coding language? We’ve got a handful of different code samples available that you can use as a starting point on our GitHub page, including a Python client.

#### Libraries

Take advantage of one of our many community third-party libraries to help you get started. You can find a library that works with the v2 endpoints by looking for the appropriate version tag.

#### Postman

Postman is a great tool that you can use to test out these endpoints. Each Postman request includes all of the given endpoint’s parameters to help you quickly understand what is available to you. To learn more about our Postman collections, please visit our Using Postman page.  

### Key concepts

#### Authentication

All Twitter API v2 endpoints require requests to be authenticated with a set of credentials, also known as keys and tokens. This specific endpoint requires the use of OAuth 2.0 Bearer Token, which means that you must pass a Bearer Token to make a successful request. You can either generate a Bearer Token from directly within a developer App, or generate one using the POST oauth2/token endpoint.

#### 
Developer portal, Projects, and developer Apps

To work with any Twitter API v2 endpoints, you must have a developer account, set up a Project within that account, and created a developer App within that Project. Your keys and tokens within that developer App will work for the recent Tweet counts endpoints. If you would like to use the full-archive Tweet counts endpoint, or utilize the advanced operators and longer query length, you will need to have been approved for enterprise access.

Please visit our section on enterprise access to learn more.  

#### Rate limits

Every day, many thousands of developers make requests to the Twitter API. To help manage the volume, rate limits are placed on each endpoint that limits the number of requests that every developer can make on behalf of an app or on behalf of an authenticated user.

This endpoint is rate limited at the App-level, meaning that you, the developer, can only make a certain number of requests to this endpoint over a given period of time from any given App (assumed by the credentials that you are using).   

#### Building queries

The central feature of these endpoints is their use of a single query to filter the Tweets into the counts that deliver to you. These queries are made up of operators that match on Tweet and user attributes, such as message keywords, hashtags, and URLs. Operators can be combined into queries with boolean logic and parentheses to help refine the query's matching behavior.

You can use our guide on how to build a query to learn more.

We have also written a more in-depth tutorial on how to build high-quality filters for getting Twitter data.  

#### Pagination

For recent Tweet counts, there is no next\_token returned, which means that regardless of the granularity, you will get  the Tweet volume for the last 7 days in one API call.

For full-archive Tweet counts, you will get data for the last 30 days. For data more than 30 days, you will get a next\_token which you can then use to paginate to get the additional data. 

Next steps
----------

Make your first request to a Tweet counts endpoint

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