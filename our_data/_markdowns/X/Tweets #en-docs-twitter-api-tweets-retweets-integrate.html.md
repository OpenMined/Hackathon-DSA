
Retweets integration guide | Docs | Twitter Developer Platform 

Integrate

Integration guide
-----------------

This page contains information on several tools and key concepts that you should be aware of as you integrate the Retweet endpoints into your system. We’ve broken the page into a couple of different sections:

* Helpful tools
* Key Concepts
* Authentication
* Developer portal, Projects, and Apps
* Rate limits
* Fields and expansions

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

All Twitter API v2 endpoints require for you to authenticate your requests with a set of credentials, also known as keys and tokens.

You can use either OAuth 1.0a User Context or OAuth 2.0 Bearer Token to authenticate your requests to the Retweets lookup endpoint. 

The manage Retweets endpoints require the use of OAuth 1.0a User Context, which means that you must use a set of API keys and user access tokens to make a successful request. The access tokens must be associated with the user that you are making the request on behalf of. If you would like to generate a set of access tokens for another user, they must authorize or authenticate your App using the 3-legged OAuth flow.

Please note that OAuth 1.0a can be tricky to use. If you are not familiar with this authentication method, we recommend that you use a library to properly authenticate your requests.

**Please note**

If you are requesting the following fields, OAuth 1.0a User Context is required: 

* tweet.fields.non\_public\_metrics
* tweet.fields.promoted\_metrics
* tweet.fields.organic\_metrics
* media.fields.non\_public\_metrics
* media.fields.promoted\_metrics
* media.fields.organic\_metrics

#### 

#### Developer portal, Projects, and developer Apps

To retrieve a set of authentication credentials that will work with the Twitter API v2 endpoints, you must sign up for a developer account, set up a Project within that account, and created a developer App within that Project. You can then find your keys and tokens within your developer App.   

#### Rate limits

Every day, many thousands of developers make requests to the Twitter API. To help manage the sheer volume of these requests, rate limits are placed on each endpoint that limits the number of requests that you can make on behalf of your app or on behalf of an authenticated user.

The manage Retweets endpoints are limited to 50 requests per 15 min (per user). Additionally, for the POST endpoint, you are limited to 300 requests per 3-hour window (per user, per app). 

With the Retweets lookup endpoint, you are limited to 75 requests per 15-min window. 

#### Fields and expansions

The Twitter API v2 allows users to select exactly which data they want to return from the API using a set of tools called fields and expansions. The expansion parameter allows you to expand objects referenced in the payload. For example, this endpoint allows you to pull the following expansions:

* attachments.poll\_ids
* attachments.media\_keys
* author\_id, entities.mentions.username
* geo.place\_id
* in\_reply\_to\_user\_id,
* referenced\_tweets.id,
* referenced\_tweets.id.author\_id

The fields parameter allows you to select exactly which fields within the different data objects you would like to receive. These endpoints delivers Tweet objects primarily. By default, the Tweet object returns the id and text fields. To receive additional fields such as tweet.created\_at or tweet.entities, you will have to specifically request those using a fields parameter. Some important fields that you may want to consider using in your integration are our poll data, metrics, Tweet annotations, and conversation ID fields.

We’ve added a guide on how to use fields and expansions together to our Twitter API v2 data dictionary.

#### Pagination

This endpoint utilizes pagination so that responses are returned quickly. In cases where there are more results than what can be sent in a single response (up to 100 users) you will need to paginate. Use the `max_results` parameter to identify how many results will return per page, and the `pagination_token` parameter to return the next page of results. You can learn more by reviewing our pagination guide.

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