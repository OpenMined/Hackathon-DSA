Introduction

Introduction
------------

The RESTful endpoint uses the GET method to return information about a user or group of users, specified by a user ID or a username. The response includes one or many [user objects](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user), which deliver fields such as the Follower count, location, pinned Tweet ID, and profile bio. Responses can also optionally include expansions to return the full Tweet object for a user’s pinned Tweet, including the Tweet text, author, and other Tweet fields. 

You can authenticate your request to all users lookup endpoints other than the authenticated user lookup with [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a), [App only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only), or [OAuth 2.0 Authorization code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code). However, if you would like to access private metrics or data from private users, you will need to utilize OAuth 1.0a User Context or OAuth 2.0 Authorization Code with PKCE, and pass the authenticated users' Access Token with your request.    

This endpoint is commonly used to receive up-to-date details on a user, to verify that a user exists, or to update your stored details following a compliance event.

### Authenticated user lookup

If authenticating on behalf of other users, it is critical to be able to see who you can make a request on behalf of.

This endpoint requires you to use [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) or [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code). It returns information about the authorized user, meaning the user that is associated with the user Access Tokens that you pass with the request.

You can access this endpoint via the GET method. There is a user rate limit of 75 requests per 15 minutes for this endpoint.

**Account setup**

To access these endpoints, you will need:

* An approved [developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info).
* To authenticate using the keys and tokens from a [developer App](https://developer.twitter.com/en/docs/apps) that is located within a [Project](https://developer.twitter.com/en/docs/projects). 

Learn more about getting access to the Twitter API v2 endpoints in our [getting started guide](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api).

[Quick start](https://developer.twitter.com/en/docs/twitter-api/users/lookup/quick-start)

[Sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code)

[Run in Postman](https://t.co/twitter-api-postman)

[Try with API Explorer](https://developer.twitter.com/apitools/api?endpoint=/2/users&method=get)

Supporting resources
--------------------

[Learn how to use Postman to make requests](https://developer.twitter.com/en/docs/tutorials/postman-getting-started "Learn how to use Postman to make requests")

[Troubleshoot an error](https://developer.twitter.com/en/support/twitter-api "Troubleshoot an error")

[Visit the API reference page for this endpoint](https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference "Visit the API reference page for this endpoint")

Relevant tutorials
------------------

[Getting started with R and v2 of the Twitter API](https://developer.twitter.com/en/docs/tutorials/getting-started-with-r-and-v2-of-the-twitter-api "Getting started with R and v2 of the Twitter API")

User lookup

Getting started with the users lookup endpoints
-----------------------------------------------

This quick start guide will help you make your first request to the users lookup endpoints with a set of specified fields using [Postman](https://developer.twitter.com/en/docs/tools-and-libraries/using-postman).

If you would like to see sample code in different languages, please visit our [Twitter API v2 sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code) GitHub repository. 

### Prerequisites

To complete this guide, you will need to have a set of [keys and tokens](https://developer.twitter.com/en/docs/authentication) to authenticate your request. You can generate these keys and tokens by following these steps:

* [Sign up for a developer account](https://developer.twitter.com/en/apply-for-access) and receive approval.
* Create a [Project](https://developer.twitter.com/en/docs/projects) and an associated [developer App](https://developer.twitter.com/en/docs/apps) in the developer portal.
* Navigate to your App's “Keys and tokens” page to generate the required credentials. Make sure to save all credentials in a secure location.

### Steps to build a users lookup request

#### Step one: Start with a tool or library

There are several different tools, code examples, and libraries that you can use to make a request to this endpoint, but we are going to use the Postman tool here to simplify the process.

To load the Twitter API v2 Postman collection into your environment, please click on the following button:

[Add Twitter API v2 to Postman](https://t.co/twitter-api-postman)

Once you have the Twitter API v2 collection loaded in Postman, navigate to the GET /users/by endpoint.  
 

#### Step two: Authenticate your request

To properly make a request to the Twitter API, you need to verify that you have permission. To do so, this endpoint requires you to authenticate your request with either [App only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only), [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code), or [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) authentication methods.

For simplicity's sake, we will utilize App only with this request, but you will need to use one of the other authentication methods if you'd like to request private [metrics](https://developer.twitter.com/en/docs/twitter-api/metrics) or users. 

To utilize App only, you must add your keys and tokens, specifically the [App Access Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens) (also known as the App only Bearer Token) to Postman. You can do this by selecting the environment named “Twitter API v2” in the top-right corner of Postman and adding your keys and tokens to the "initial value" and "current value" fields (by clicking the eye icon next to the environment dropdown).

These variables will automatically be pulled into the request's authorization tab if you've done this correctly.  
 

#### Step three: Identify and specify which user(s) you would like to retrieve

You must specify a user or a set of users that you would like to receive within the request. Depending on which user endpoint you use, you can pass either a user ID or a username. In this situation, we are going to use the [GET /users/by endpoint](https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users-by) which allows you to pass multiple usernames in a single request (rather than the [single-ID](https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users-id), [multi-ID](https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users), and [single-username](https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users-by-username-username) endpoints) and pass a set of usernames using the usernames query parameter.

Usernames are simply the account handle that you can find within an account's profile URL. For example, the following account’s username is twitterdev.

`https://twitter.com/TwitterDev`

In Postman, navigate to the "Params" tab and enter this username, or a string of usernames separated by a comma, into the "Value" column of the username parameter, making sure to not include any spaces between usernames and commas. 

|     |     |
| --- | --- |
| **Key** | **Value** |
| `username` | twitterdev,twitterapi,adsapi |

#### Step four: Identify and specify which fields you would like to retrieve

If you click the "Send" button after step three, you will receive the default [user object](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) fields in your response: id, name, and username.

If you would like to receive additional fields beyond id, name, and username, you will have to specify those fields in your request with the [field](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/data-dictionary/introduction/fields) and/or [expansion](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/introduction/expansions) parameters.

For this exercise, we will request a three additional sets of fields from different objects:

1. The additional user.created\_at field in the primary user objects.
2. The associated pinned Tweets’ object’s default fields for the returned users: id and text.
3. The additional  tweet.created\_at field in the associated Tweet objects.  
     

In Postman, navigate to the "Params" tab and add the following key:value pair to the "Query Params" table:

|     |     |     |
| --- | --- | --- |
| **Key** | **Value** | **Returned fields** |
| `user.fields` | `created_at` | `user.created_at` |
| `expansions` | `author_id` | tweet.id, tweet.text |
| `tweet.fields` | `created_at` | `includes.users.created_at` |

You should now see the following URL next to the "Send" button:

      `https://api.twitter.com/2/users/by?usernames=twitterdev,twitterapi,adsapi&user.fields=created_at&expansions=pinned_tweet_id&tweet.fields=author_id,created_at`
    

####   
Step five: Make your request and review your response

Once you have everything set up, hit the "Send" button and you will receive the following response:

      `{   "data": [     {       "created_at": "2013-12-14T04:35:55.000Z",       "id": "2244994945",       "name": "Twitter Dev",       "pinned_tweet_id": "1255542774432063488",       "username": "TwitterDev"     },     {       "created_at": "2007-05-23T06:01:13.000Z",       "id": "6253282",       "name": "Twitter API",       "username": "TwitterAPI"     },     {       "created_at": "2013-02-27T20:01:12.000Z",       "id": "1225933934",       "name": "Twitter Ads API",       "username": "AdsAPI"     }   ],   "includes": {     "tweets": [       {         "author_id": "2244994945",         "created_at": "2020-04-29T17:01:38.000Z",         "id": "1255542774432063488",         "text": "During these unprecedented times, what’s happening on Twitter can help the world better understand &amp; respond to the pandemic. \n\nWe're launching a free COVID-19 stream endpoint so qualified devs &amp; researchers can study the public conversation in real-time. https://t.co/BPqMcQzhId"       }     ]   } }`
    

Next steps
----------

[Customize your request using the API Reference](https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference "Customize your request using the API Reference")

[Reach out to the community for help](https://twittercommunity.com/ "Reach out to the community for help")

[Check out some sample code for these endpoints](https://github.com/twitterdev/Twitter-API-v2-sample-code "Check out some sample code for these endpoints")

Authenticated user lookup

Getting started with the Authenticated User Lookup endpoint
-----------------------------------------------------------

This quick start guide will help you make your first request to the authenticated user lookup endpoint using Postman.

Please visit our [Twitter API v2 sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code) GitHub repository if you want to see sample code in different languages.

### Prerequisites

To complete this guide, you will need to have a set of [keys and tokens](https://developer.twitter.com/en/docs/authentication) to authenticate your request. You can generate these keys and tokens by following these steps:

* [Sign up for a developer account](https://developer.twitter.com/en/apply-for-access) and receive approval.
* Create a [Project](https://developer.twitter.com/en/docs/projects) and an associated [developer App](https://developer.twitter.com/en/docs/apps) in the developer portal.
* Navigate to your App's “Keys and tokens” page to generate the required credentials. Make sure to save all credentials in a secure location.

### Steps to build an authenticated user lookup request

#### Step one: Start with a tool or library

There are several different tools, code examples, and libraries that you can use to make a request to this endpoint, but we will use the Postman tool here to simplify the process.

To load the Twitter API v2 Postman collection into your environment, please click on the following button:

[Add Twitter API v2 to Postman](https://t.co/twitter-api-postman)

Once you have the Twitter API v2 collection loaded in Postman, navigate to the “Authenticated User Lookup” folder, and select “Lookup an Authenticated User”.

#### Step two: Authenticate your request

To properly make a request to the Twitter API, you need to verify that you have permission. To do so with this endpoint, you must authenticate your request using either [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) or [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code).

In this example, we are going to use OAuth 1.0a User Context.

You must add your keys and tokens – specifically your API Key, API Secret Key, OAuth 1.0a user Access Token, and OAuth 1.0a user Access Token Secret – to Postman. You can do this by selecting the environment named “Twitter API v2” in the top-right corner of Postman and adding your keys and tokens to the "initial value" and "current value" fields (by clicking the eye icon next to the environment dropdown).

These variables will automatically be pulled into the request's authorization tab if you've done this correctly.  
 

Step three: Determine which user fields you want to retrieve  

If you click the "Send" button after step three, you will receive the default [user object](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) fields in your response: id, name, and username.

If you would like to receive additional fields beyond id, name, and username, you will have to specify those fields in your request with the [field](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/data-dictionary/introduction/fields) and/or [expansion](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/introduction/expansions) parameters.

For this exercise, we will request three additional sets of fields from different objects:

1. The additional user.created\_at field in the primary user objects.
    
2. The associated pinned Tweets’ object’s default fields for the returned users: id and text.
    
3. The additional tweet.created\_at field in the associated Tweet objects.  
    

In Postman, navigate to the "Params" tab and add the following key:value pair to the "Query Params" table:

|     |     |     |
| --- | --- | --- |
| **Key** | **Value** | **Returned fields** |
| user.fields | created\_at | user.created\_at |
| expansions | pinned\_tweet\_id | includes.tweets.id,  <br>includes.tweets.text |
| tweet.fields | created\_at, author\_id | includes.tweets.created\_at, includes\_tweets.author\_id |

You should now see a similar URL next to the “Send” button:

      `https://api.twitter.com/2/users/me?user.fields=created_at&expansions=pinned_tweet_id&tweet.fields=author_id,created_at`
    

Next steps
----------

[Customize your request using the API Reference](https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference "Customize your request using the API Reference")

[Reach out to the community for help](https://twittercommunity.com/ "Reach out to the community for help")

Integrate

Integration guide
-----------------

This page contains information on several tools and key concepts that you should be aware of as you integrate the users lookup endpoints into your system. We’ve broken the page into a couple of different sections:

* [Helpful tools](#helpful)
* Key Concepts
* [Authentication](#authentication)
* [Developer portal, Projects, and Apps](#portal)
* [Rate limits](#limits)
* [Fields and expansions](#fields)
* [Edge cases](#edge)

### Helpful tools

Before we dive into some key concepts that will help you integrate this endpoint, we recommend that you become familiar with:

#### Postman

Postman is a great tool that you can use to test out an endpoint. Each Postman request includes every path and body parameter to help you quickly understand what is available to you. To learn more about our Postman collections, please visit our ["Using Postman"](https://developer.twitter.com/en/docs/tools-and-libraries/using-postman) page. 

#### Code samples

Interested in getting set up with this endpoint with some code in your preferred coding language? We’ve got a handful of different code samples available that you can use as a starting point on our [Github page](https://github.com/twitterdev/Twitter-API-v2-sample-code).

#### Third-party libraries

Take advantage of one of our communities’ [third-party libraries](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries) to help you get started. You can find a library that works with the v2 endpoints by looking for the proper version tag.

### Key concepts

#### Authentication

All Twitter API v2 endpoints require requests to be [authenticated](https://developer-staging.twitter.com/en/docs/authentication) with a set of credentials, also known as keys and tokens. You can use either OAuth 1.0a User Context, App only, or OAuth 2.0 Authorization Code with PKCE to authenticate requests to these endpoints. 

[OAuth 1.0a User Context](https://developer-staging.twitter.com/en/docs/authentication/oauth-1-0a) requires you to utilize your API Keys, user Access Tokens, and a handful of other parameters to [create an authorization header](https://developer-staging.twitter.com/en/docs/authentication/oauth-1-0a/authorizing-a-request), which you will then pass with your request. The Access Tokens must be associated with the user that you are making the request on behalf of. If you would like to generate a set of Access Tokens for another user, they must authorize your App using the [3-legged OAuth flow](https://developer-staging.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens). 

Please note that OAuth 1.0a can be difficult to use. If you are not familiar with this authentication method, we recommend that you use a [library](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries), use a tool like Postman, or use OAuth 2.0 to authenticate your requests. If you would like to request a Tweet or private metrics from these endpoints, you will need to use a either OAuth 1.0a User Context or OAuth 2.0 Authorization Code with PKCE, which will ensure that you have the proper permissions from the user that owns that content.  
 

[App only](https://developer-staging.twitter.com/en/docs/authentication/oauth-2-0) just requires that you pass an [App only Access Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens) with your request. You can either generate an App only Access Token from directly within a developer App, or generate one using the [POST oauth2/token](https://developer-staging.twitter.com/en/docs/authentication/api-reference/token) endpoint.

[OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code) allows for greater control over an application’s scope, and authorization flows across multiple devices. OAuth 2.0 allows you to pick specific fine-grained scopes which give you specific permissions on behalf of a user. 

To enable OAuth 2.0 in your App, you must enable it in your’s App’s authentication settings found in the App settings section of the developer portal.

**Please note**

If you are requesting the following fields, OAuth 1.0a User Context or OAuth 2.0 Authorization Code is required: 

* tweet.fields.non\_public\_metrics
* tweet.fields.promoted\_metrics
* tweet.fields.organic\_metrics

#### Developer portal, Projects, and developer Apps

To retrieve a set of authentication credentials that will work with the Twitter API v2 endpoints, you must [sign up for a developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info), set up a [Project](https://developer.twitter.com/en/docs/projects) within that account, and created a [developer App](https://developer.twitter.com/en/docs/apps) within that Project. You can then find your keys and tokens within your developer App.   
 

#### Rate limits

Every day, many thousands of developers make requests to the Twitter API. To help manage the sheer volume of these requests, [rate limits](https://developer.twitter.com/en/docs/twitter-api/rate-limits) are placed on each endpoint that limits the number of requests that you can make on behalf of your app or on behalf of an authenticated user. 

The user lookup endpoints are rate limited at both the app-level and the user-level. However, the authenticated user lookup endpoint is rate limited at the user-level

The app-level rate limit means that you, the developer, can only make a certain number of requests to this endpoint over a given period of time from any given App (assumed by the keys and tokens that you are using. The user-level rate limit means that the authenticated user that you are making the request on behalf of can only perform a certain number of times across any developer App.  

The chart below shows the rate limits for each endpoint.

|     |     |     |
| --- | --- | --- |
| **Endpoint** | **HTTP method** | **Rate limit / Level** |
| /2/users | GET | 900 requests per 15 minutes / App and User |
| /2/users/:id | GET | 900 requests per 15 minutes / App and User |
| /2/users/by | GET | 900 requests per 15 minutes / App and User |
| /2/users/by/username/:username | GET | 900 requests per 15 minutes / App and User |
| /2/users/me | GET | 75 requests per 15 minutes / User |

#### Fields and expansions

The Twitter API v2 allows users to select exactly which data they want to return from the API using a set of tools called fields and expansions. The expansion parameter allows you to expand objects referenced in the payload. For example, this endpoint allows you to use the pinned\_tweet\_id expansion.

The fields parameter allows you to select exactly which [fields](https://developer.twitter.com/en/docs/twitter-api/fields) within the different data objects you would like to receive. These endpoints delivers user objects primarily. By default, the user object returns the id, name, and username fields. To receive additional fields such as user.created\_at or user.location, you will have to specifically request those using a fields parameter. Some important fields that you may want to consider using in your integration are our Tweet poll data, metrics, annotations, and conversation ID fields.

We’ve added a guide on how to [use fields and expansions](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/using-fields-and-expansions) in our [Twitter API v2 data dictionary](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/introduction).  
  

#### Edge cases

* Tweet text is truncated for Retweets. The short term workaround is to expand the referenced Tweet and retrieve the full text from the expansion. This is a bug that we will fix in the future.

Next steps
----------

[Visit the API reference page for this endpoint](https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference "Visit the API reference page for this endpoint")

Migrate

Comparing Twitter API’s users lookup endpoints
----------------------------------------------

The v2 user lookup endpoints will replace the standard v1.1 [GET users/lookup](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-users-lookup.html) and [GET users/show](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-users-show.html) endpoints. If you have code, apps, or tools that use one of these versions of the user lookup endpoints, and are considering migrating to the newer Twitter API v2 endpoint, then this set of guides is for you.   
 

The following tables compare the various types of users lookup endpoints:  
 

|     |     |     |
| --- | --- | --- |
| **Description** | **Standard v1.1** | **Twitter API v2** |
| HTTP methods supported | `GET` | `GET` |
| Host domain | `https://api.twitter.com` | `https://api.twitter.com` |
| Endpoint path | `/1.1/users/show.json` `/1.1/users/lookup.json` | `/2/users`<br><br>`/2/users/:id`<br><br>`/2/users/by`<br><br>`/2/users/by/:username` |
| [Authentication](https://developer.twitter.com/en/docs/authentication) | OAuth 1.0a User Context | OAuth 1.0a User Context<br><br>App only<br><br>OAuth 2.0 Authorization Code with PKCE |
| Default request [rate limits](https://developer.twitter.com/en/docs/rate-limits) | 900 requests per 15 min (per user)<br><br>/show - 900 requests per 15 min (per app)  <br>/lookup - 300 requests per 15 min (per app) | 900 requests per 15 min (per user)<br><br>300 requests per 15 min (per app) |
| Maximum Users per response | /show -  1<br><br>/lookup - 100 | 100 |
| JSON response object format | Standard v1.1 format | [Twitter API v2 format](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/data-dictionary) (determined by fields and expansions request parameters, not backward-compatible with v1.1 formats)<br><br>To learn more about how to migrate from the Standard v1.1 format to the Twitter API v2 format, please visit our [data formats migration guide](https://developer.twitter.com/en/docs/twitter-api/migrate/data-formats). |
| Supports selecting which [fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary) return in the payload |     | ✔   |
| Supports the [annotations](https://developer.twitter.com/en/docs/twitter-api/annotations) fields (on pinned Tweet) |     | ✔   |
| Supports requesting new [metrics](https://developer.twitter.com/en/docs/twitter-api/metrics) fields (on pinned Tweet) |     | ✔   |
| Supports the [conversation\_id](https://developer.twitter.com/en/docs/twitter-api/conversation-id) field (on pinned Tweet) |     | ✔   |
| Requires the use of credentials from a [developer App](https://developer.twitter.com/en/docs/apps) associated with a [project](https://developer.twitter.com/en/docs/projects) |     | ✔   |

Other migration resources
-------------------------

[User lookup: Standard v1.1 to Twitter API v2](https://developer.twitter.com/en/docs/twitter-api/users/lookup/migrate/standard-to-twitter-api-v2 "User lookup: Standard v1.1 to Twitter API v2")

[Twitter API migration hub](https://developer.twitter.com/en/docs/twitter-api/migrate "Twitter API migration hub")

[Check out some sample code for these endpoints](https://github.com/twitterdev/Twitter-API-v2-sample-code "Check out some sample code for these endpoints")

Standard v1.1 compared to Twitter API v2

Standard v1.1 compared to Twitter API v2
----------------------------------------

If you have been working with the standard v1.1 GET users/show and GET users/lookup, the goal of this guide is to help you understand the similarities and differences between the standard and Twitter API v2 users lookup endpoints.

* **Similarities**
    * OAuth 1.0a User Context
    * Users per request limits
* **Differences**
    * Endpoint URLs
    * App and Project requirements
    * Response data format
    * Request parameters

### Similarities

#### OAuth 1.0a User Context authentication method

The standard endpoint supports [OAuth 1.0a User Context](https://developer.twitter.com/content/developer-twitter/en/docs/authentication/oauth-1-0a), while the new Twitter API v2 users lookup endpoints supports both OAuth 1.0a User Context and [OAuth 2.0 Bearer Token](https://developer.twitter.com/content/developer-twitter/en/docs/authentication/oauth-2-0). Therefore, if you were previously using one of the standard v1.1 users lookup endpoints, you can continue using the same authentication method if you migrate to the Twitter API v2 version. 

Depending on your authentication library/package of choice, Bearer Token authentication is probably the easiest way to get started and can be set with a simple request header. To learn how to generate a Bearer Token, see [this OAuth 2.0 Bearer Token guide](https://developer.twitter.com/content/developer-twitter/en/docs/basics/authentication/overview/application-only). 

#### Users per request limits

The standard v1.1 GET users/lookup endpoint allows you to specify 100 users per request. This also goes for the GET /users and GET /users/by endpoints. To specify a full 100 users, you will need to pass the ids (GET /users) parameter or the username (GET /users/by) parameter as a query parameter, and include the list of user IDs/usernames in a comma-separated list.   
 

### Differences

#### Endpoint URLs

* Standard v1.1 endpoints:
    * https://api.twitter.com/1.1/users/show (single-ID or username lookup)
    * https://api.twitter.com/1.1/users/lookup (multi-ID or username lookup)
* Twitter API v2 endpoint:
    * https://api.twitter.com/2/users (multi-ID lookup)
    * https://api.twitter.com/2/users/:id (single-ID lookup)
    * https://api.twitter.com/2/users/by (multi-username lookup)
    * https://api.twitter.com/2/users/by/username/:username (single-username lookup)

#### App and Project requirements

The Twitter API v2 endpoints require that you use credentials from a [developer App](https://aem-staging.twitter.biz/content/developer-twitter/en/docs/apps.html) that is associated to a [Project](https://aem-staging.twitter.biz/content/developer-twitter/en/docs/projects.html) when authenticating your requests. All Twitter API v1.1 endpoints can use credentials from standalone Apps or Apps associated with a project.   
  

#### Response data format

One of the biggest differences between standard v1.1 and Twitter API v2 endpoint versions is how you select which fields return in your payload.

For the standard endpoints, you receive many of the response fields by default, and then have the option to use parameters to identify which fields or sets of fields should return in the payload.

The Twitter API v2 version only delivers the user id , name, and username fields by default. To request any additional fields or objects, you wil need to use the [fields](https://developer.twitter.com/en/docs/twitter-api/fields/content/developer-twitter/en/docs/twitter-api/fields) and [expansions](https://developer.twitter.com/en/docs/twitter-api/fields/content/developer-twitter/en/docs/twitter-api/expansions) parameters. Any user fields that you request from this endpoint will return in the primary user object. Any expanded Tweet object and fields will return in an includes object within your response. You can then match any expanded objects back to the user object by matching the IDs located in both the user and the expanded Tweet object. 

We encourage you to read more about these new parameters in their respective guides, or by reading our guide on [how to use fields and expansions](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/using-fields-and-expansions). 

We have also put together a [data format migration guide](https://developer.twitter.com/en/docs/twitter-api/migrate/data-formats/standard-v1-1-to-v2) which can help you map standard v1.1 fields to the newer v2 fields. This guide will also provide you the specific expansion and field parameter that you will need to pass with your v2 request to return specific fields.   
 

In addition to the changes in how you request certain fields, Twitter API v2 is also introducing new JSON designs for the objects returned by the APIs, including [Tweet](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) and [user](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) objects.

* At the JSON root level, the standard endpoints return Tweet objects in a statuses array, while Twitter API v2 returns a data array. 
* Instead of referring to Retweeted and Quoted "statuses", Twitter API v2 JSON refers to Retweeted and Quoted Tweets. Many legacy and deprecated fields, such as contributors and user.translator\_type are being removed. 
* Instead of using both favorites (in Tweet object) and favourites (in user object), Twitter API v2 uses the term like. 
* Twitter is adopting the convention that JSON values with no value (for example, null) are not written to the payload. Tweet and user attributes are only included if they have a non-null values.   
     

We also introduced a new set of fields to the [Tweet object](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) including the following:

* A [conversation\_id](https://developer.twitter.com/en/docs/twitter-api/conversation-id) field
* Two new [annotations](https://developer.twitter.com/en/docs/twitter-api/annotations) fields, including context and entities
* Several new [metrics](https://developer.twitter.com/en/docs/twitter-api/metrics) fields 
* A new reply\_setting field, which shows you who can reply to a given Tweet

#### Request parameters

The following standard v1.1 request parameters have equivalents in Twitter API v2:

|     |     |
| --- | --- |
| **Standard** | **Twitter API v2** |
| user\_id | ids |
| screen\_name | username |

There are also a set of standard users lookup request parameters **not** supported in Twitter API v2:  

| Standard | Comment |
| --- | --- |
| include\_entities | This parameter is used to remove the entities node from the Tweet payload.  It has been replaced with the additive fields and expansions functionality. |

Next steps
----------

[Check out our quick start guide for Twitter API v2 users lookup](https://developer.twitter.com/en/docs/twitter-api/users/lookup/quick-start "Check out our quick start guide for Twitter API v2 users lookup")

[Review the API reference for users lookup](https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference "Review the API reference for users lookup")

[Check out some sample code for these endpoints](https://github.com/twitterdev/Twitter-API-v2-sample-code "Check out some sample code for these endpoints")

API reference

API reference index
-------------------

For the complete API reference, select an endpoint from the list:

|     |     |
| --- | --- |
| **Retrieve multiple users with IDs** | `[GET /2/users](https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users)` |
| **Retrieve a single user with an ID** | `[GET /2/users/:id](https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users-id)` |
| **Retrieve multiple users with usernames  <br>** | `[GET /2/users/by](https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users-by)` |
| **Retrieve a single user with a usernames** | `[GET /2/users/by/username/:username](https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users-by-username-username)` |
| **Returns the information about an authorized user** | `[GET /2/users/me](https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users-me)` |

GET /2/users/:id

GET /2/users/:id
================

Returns a variety of information about a single user specified by the requested ID.

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Try a live request ❯](https://oauth-playground.glitch.me/?id=findUserById&params=%28%27query%21%28%29%7Ebody%21%28%29%7Epath%21%28%21*%7E**id%21%272244994945%27%29%01*_) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Fusers%2F%7Bid%7D&method=get) 

### Endpoint URL

`https://api.twitter.com/2/users/:id`  
  

### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code "This method allows an authorized app to act on behalf of the user, as the user. It is typically used to access or post public information for a specific user, and it us useful when your app needs to be aware of the relationship between a user and what this endpoint returns. Click to learn how to authenticate with OAuth 2.0 Authorization Code with PKCE.")<br><br>[OAuth 2.0 App-only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only "Use this method to obtain information in the context of an unauthenticated public user. This method is for developers that just need read-only access to public information. Click to learn how to obtain an OAuth 2.0 App Access Token.")<br><br>[OAuth 1.0a](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) is also available for this endpoint. |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | App rate limit (Application-only): 300 requests per 15-minute window shared among all users of your app<br><br>User rate limit (User context): 900 requests per 15-minute window per each authenticated user |

### OAuth 2.0 scopes required by this endpoint

|     |
| --- |
| `tweet.read`<br><br>`users.read` |
| [Learn more about OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/twitter-api/oauth2) |

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Required | string | The ID of the user to lookup. |

  
  

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| `expansions`  <br> Optional | enum (`pinned_tweet_id`) | [Expansions](https://developer.twitter.com/en/docs/twitter-api/expansions) enable you to request additional data objects that relate to the originally returned users. The ID that represents the expanded data object will be included directly in the user data object, but the expanded object metadata will be returned within the `includes` response object, and will also include the ID so that you can match this data object to the original Tweet object. At this time, the only expansion available to endpoints that primarily return user objects is `expansions=pinned_tweet_id`. You will find the expanded Tweet data object living in the `includes` response object. |
| `tweet.fields`  <br> Optional | enum (`attachments`, `author_id`, `context_annotations`, `conversation_id`, `created_at`, `edit_controls`, `entities`, `geo`, `id`, `in_reply_to_user_id`, `lang`, `non_public_metrics`, `public_metrics`, `organic_metrics`, `promoted_metrics`, `possibly_sensitive`, `referenced_tweets`, `reply_settings`, `source`, `text`, `withheld`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [Tweet fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) will deliver in each returned pinned Tweet. Specify the desired fields in a comma-separated list without spaces between commas and fields. The Tweet fields will only return if the user has a pinned Tweet and if you've also included the `expansions=pinned_tweet_id` query parameter in your request. While the referenced Tweet ID will be located in the original Tweet object, you will find this ID and all additional Tweet fields in the `includes` data object. |
| `user.fields`  <br> Optional | enum (`created_at`, `description`, `entities`, `id`, `location`, `most_recent_tweet_id`, `name`, `pinned_tweet_id`, `profile_image_url`, `protected`, `public_metrics`, `url`, `username`, `verified`, `verified_type`, `withheld`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [user fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) will deliver with each returned users objects. Specify the desired fields in a comma-separated list without spaces between commas and fields. These specified user fields will display directly in the user data objects. |

  
  

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript (Default fields)](#tab0)
* [TypeScript (Optional fields)](#tab1)
* [Java (Default fields)](#tab2)
* [Java (Optional fields)](#tab3)

TypeScript (Default fields)

TypeScript (Optional fields)

Java (Default fields)

Java (Optional fields)

      `(async () => {   try {     const getUserById = await twitterClient.users.findUserById(       //The User ID       2244994945     );     console.dir(getUserById, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `(async () => {   try {     const getUserById = await twitterClient.users.findUserById(       //The User ID       2244994945,       {         //A comma separated list of User fields to display         "user.fields": ["created_at"],          //A comma separated list of Tweet fields to display.         "tweet.fields": ["created_at"],          //A comma separated list of fields to expand         expansions: ["pinned_tweet_id"],       }     );     console.dir(getUserById, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  // String | Required. A User ID. String id = "2244994945";  try {     SingleUserLookupResponse result = apiInstance.users().findUserById(id, null, null, null);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling UsersApi#findUserById");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

      `// Set the params values  // String | Required. A User ID. String id = "2244994945";  // Set<String> | A comma separated list of fields to expand. Set<String> expansions = new HashSet<>(Arrays.asList("pinned_tweet_id"));  // Set<String> | A comma separated list of Tweet fields to display. Set<String> tweetFields = new HashSet<>(Arrays.asList("created_at"));  // Set<String> | A comma separated list of User fields to display. Set<String> userFields = new HashSet<>(Arrays.asList("created_at"));  try {     SingleUserLookupResponse result = apiInstance.users().findUserById(id, expansions, tweetFields, userFields);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling UsersApi#findUserById");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

### Example responses

* [Default fields](#tab0)
* [Optional fields](#tab1)

Default fields

Optional fields

      `{   "data": {     "id": "2244994945",     "name": "Twitter Dev",     "username": "TwitterDev"   } }`
    

      `{   "data": {     "username": "TwitterDev",     "created_at": "2013-12-14T04:35:55.000Z",     "pinned_tweet_id": "1255542774432063488",     "id": "2244994945",     "name": "Twitter Dev"   },   "includes": {     "tweets": [       {         "text": "During these unprecedented times, what’s happening on Twitter can help the world better understand &amp; respond to the pandemic. nnWe're launching a free COVID-19 stream endpoint so qualified devs &amp; researchers can study the public conversation in real-time. https://t.co/BPqMcQzhId",         "created_at": "2020-04-29T17:01:38.000Z",         "id": "1255542774432063488"       }     ]   } }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Default | string | Unique identifier of this user. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. |
| `name`  <br> Default | string | The friendly name of this user, as shown on their profile. |
| `username`  <br> Default | string | The Twitter handle (screen name) of this user. |
| `created_at` | date (ISO 8601) | Creation time of this account.  <br>  <br>To return this field, add `user.fields=created_at` in the request's query parameter. |
| `most_recent_tweet_id` | string | The ID of the User's most recent Tweet  <br>  <br>To return this field, add `user.fields=most_recent_tweet_id` in the request's query parameter. |
| `protected` | boolean | Indicates if this user has chosen to protect their Tweets (in other words, if this user's Tweets are private).  <br>  <br>To return this field, add `user.fields=protected` in the request's query parameter. |
| `withheld` | object | Contains withholding details for [withheld content](https://help.twitter.com/en/rules-and-policies/tweet-withheld-by-country).  <br>  <br>To return this field, add `user.fields=withheld` in the request's query parameter. |
| `withheld.country_codes` | array | Provides a list of countries where this user is not available.  <br>  <br>To return this field, add `user.fields=withheld.country_codes` in the request's query parameter. |
| `withheld.scope` | enum (`tweet`, `user`) | Indicates whether the content being withheld is a Tweet or a user (this API will return `user`).  <br>  <br>To return this field, add `user.fields=withheld.scope` in the request's query parameter. |
| `location` | string | The location specified in the user's profile, if the user provided one. As this is a freeform value, it may not indicate a valid location, but it may be fuzzily evaluated when performing searches with location queries.  <br>  <br>To return this field, add `user.fields=location` in the request's query parameter. |
| `url` | string | The URL specified in the user's profile, if present.  <br>  <br>To return this field, add `user.fields=url` in the request's query parameter. |
| `description` | string | The text of this user's profile description (also known as bio), if the user provided one.  <br>  <br>To return this field, add `user.fields=description` in the request's query parameter. |
| `verified` | boolean | Indicate if this user is a verified Twitter user.  <br>  <br>To return this field, add `user.fields=verified` in the request's query parameter. |
| `verified_type` | enum (`blue`, `business`, `government`, `none`) | Indicates the type of verification for the Twitter account.  <br>  <br>To return this field, add `user.fields=verified_type` in the request's query parameter. |
| `entities` | object | This object and its children fields contain details about text that has a special meaning in the user's description.  <br>  <br>To return this field, add `user.fields=entities` in the request's query parameter. |
| `entities.url` | array | Contains details about the user's profile website. |
| `entities.url.urls` | array | Contains details about the user's profile website. |
| `entities.url.urls.start` | integer | The start position (zero-based) of the recognized user's profile website. All start indices are inclusive. |
| `entities.url.urls.end` | integer | The end position (zero-based) of the recognized user's profile website. This end index is exclusive. |
| `entities.url.urls.url` | string | The URL in the format entered by the user. |
| `entities.url.urls.expanded_url` | string | The fully resolved URL. |
| `entities.url.urls.display_url` | string | The URL as displayed in the user's profile. |
| `entities.description` | array | Contains details about URLs, Hashtags, Cashtags, or mentions located within a user's description. |
| `entities.description.urls` | array | Contains details about any URLs included in the user's description. |
| `entities.description.urls.start` | integer | The start position (zero-based) of the recognized URL in the user's description. All start indices are inclusive. |
| `entities.description.urls.end` | integer | The end position (zero-based) of the recognized URL in the user's description. This end index is exclusive. |
| `entities.description.urls.url` | string | The URL in the format entered by the user. |
| `entities.description.urls.expanded_url` | string | The fully resolved URL. |
| `entities.description.urls.display_url` | string | The URL as displayed in the user's description. |
| `entities.description.hashtags` | array | Contains details about text recognized as a Hashtag. |
| `entities.description.hashtags.start` | integer | The start position (zero-based) of the recognized Hashtag within the Tweet. All start indices are inclusive. |
| `entities.description.hashtags.end` | integer | The end position (zero-based) of the recognized Hashtag within the Tweet. This end index is exclusive. |
| `entities.description.hashtags.hashtag` | string | The text of the Hashtag. |
| `entities.description.mentions` | array | Contains details about text recognized as a user mention. |
| `entities.description.mentions.start` | integer | The start position (zero-based) of the recognized user mention within the Tweet. All start indices are inclusive. |
| `entities.description.mentions.end` | integer | The end position (zero-based) of the recognized user mention within the Tweet. This end index is exclusive. |
| `entities.description.mentions.username` | string | The part of text recognized as a user mention. |
| `entities.description.cashtags` | array | Contains details about text recognized as a Cashtag. |
| `entities.description.cashtags.start` | integer | The start position (zero-based) of the recognized Cashtag within the Tweet. All start indices are inclusive. |
| `entities.description.cashtags.end` | integer | The end position (zero-based) of the recognized Cashtag within the Tweet. This end index is exclusive. |
| `entities.description.cashtags.cashtag` | string | The text of the Cashtag. |
| `profile_image_url` | string | The URL to the profile image for this user, as shown on the user's profile. |
| `public_metrics` | object | Contains details about activity for this user. |
| `public_metrics.followers_count` | integer | Number of users who follow this user. |
| `public_metrics.following_count` | integer | Number of users this user is following. |
| `public_metrics.tweet_count` | integer | Number of Tweets (including Retweets) posted by this user. |
| `public_metrics.listed_count` | integer | Number of lists that include this user. |
| `pinned_tweet_id` | string | Unique identifier of this user's pinned Tweet.  <br>  <br>You can obtain the expanded object in `includes.tweets` by adding `expansions=pinned_tweet_id` in the request's query parameter. |
| `includes.tweets` | array | When including the `expansions=pinned_tweet_id` parameter, this includes the pinned Tweets attached to the returned users' profiles in the form of [Tweet objects](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) with their default fields and any additional fields requested using the `tweet.fields` parameter, assuming there is a referenced Tweet present in the returned Tweet(s). |
| `errors` | object | Contains details about errors that affected any of the requested users. See [Status codes and error messages](https://developer.twitter.com/en/support/twitter-api/error-troubleshooting) for more details. |

GET /2/users

GET /2/users
============

Returns a variety of information about one or more users specified by the requested IDs.

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Try a live request ❯](https://oauth-playground.glitch.me/?id=findUsersById&params=%28%27query%21%28%27*%7Ebody%21%28%29%7Epath%21%28%29%7E**ids%21%272244994945%2C6253282%27%29%01*_) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Fusers&method=get) 

### Endpoint URL

`https://api.twitter.com/2/users`  
  

### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 2.0 App-only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only "Use this method to obtain information in the context of an unauthenticated public user. This method is for developers that just need read-only access to public information. Click to learn how to obtain an OAuth 2.0 App Access Token.")<br><br>[OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code "This method allows an authorized app to act on behalf of the user, as the user. It is typically used to access or post public information for a specific user, and it us useful when your app needs to be aware of the relationship between a user and what this endpoint returns. Click to learn how to authenticate with OAuth 2.0 Authorization Code with PKCE.")<br><br>[OAuth 1.0a](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) is also available for this endpoint. |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | App rate limit (Application-only): 300 requests per 15-minute window shared among all users of your app<br><br>User rate limit (User context): 900 requests per 15-minute window per each authenticated user |

### OAuth 2.0 scopes required by this endpoint

|     |
| --- |
| `tweet.read`<br><br>`users.read` |
| [Learn more about OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/twitter-api/oauth2) |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| `ids`  <br> Required | string | A comma separated list of user IDs. Up to 100 are allowed in a single request. Make sure to not include a space between commas and fields. |
| `expansions`  <br> Optional | enum (`pinned_tweet_id`) | [Expansions](https://developer.twitter.com/en/docs/twitter-api/expansions) enable you to request additional data objects that relate to the originally returned users. The ID that represents the expanded data object will be included directly in the user data object, but the expanded object metadata will be returned within the `includes` response object, and will also include the ID so that you can match this data object to the original Tweet object. At this time, the only expansion available to endpoints that primarily return user objects is `expansions=pinned_tweet_id`. You will find the expanded Tweet data object living in the `includes` response object. |
| `tweet.fields`  <br> Optional | enum (`attachments`, `author_id`, `context_annotations`, `conversation_id`, `created_at`, `edit_controls`, `entities`, `geo`, `id`, `in_reply_to_user_id`, `lang`, `non_public_metrics`, `public_metrics`, `organic_metrics`, `promoted_metrics`, `possibly_sensitive`, `referenced_tweets`, `reply_settings`, `source`, `text`, `withheld`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [Tweet fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) will deliver in each returned pinned Tweet. Specify the desired fields in a comma-separated list without spaces between commas and fields. The Tweet fields will only return if the user has a pinned Tweet and if you've also included the `expansions=pinned_tweet_id` query parameter in your request. While the referenced Tweet ID will be located in the original Tweet object, you will find this ID and all additional Tweet fields in the `includes` data object. |
| `user.fields`  <br> Optional | enum (`created_at`, `description`, `entities`, `id`, `location`, `most_recent_tweet_id`, `name`, `pinned_tweet_id`, `profile_image_url`, `protected`, `public_metrics`, `url`, `username`, `verified`, `verified_type`, `withheld`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [user fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) will deliver with each returned users objects. Specify the desired fields in a comma-separated list without spaces between commas and fields. These specified user fields will display directly in the user data objects. |

  
  

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript (Default fields)](#tab0)
* [TypeScript (Optional fields)](#tab1)
* [Java (Default fields)](#tab2)
* [Java (Optional fields)](#tab3)

TypeScript (Default fields)

TypeScript (Optional fields)

Java (Default fields)

Java (Optional fields)

      `(async () => {   try {     const userIdsLookup = await twitterClient.users.findUsersById({       //A list of User IDs, comma-separated. You can specify up to 100 IDs.       ids: ["2244994945", "6253282"]     });     console.dir(userIdsLookup, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `(async () => {   try {     const userIdsLookup = await twitterClient.users.findUsersById({       //A list of User IDs, comma-separated. You can specify up to 100 IDs.       ids: ["2244994945", "6253282"],        //A comma separated list of User fields to display       "user.fields": ["created_at"],        //A comma separated list of Tweet fields to display.       "tweet.fields": ["created_at"],        //A comma separated list of fields to expand       expansions: ["pinned_tweet_id"],     });     console.dir(userIdsLookup, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  // List<String> | Required. A list of User IDs, comma-separated. You can specify up to 100 IDs. List<String> ids = Arrays.asList("2244994945", "6253282");  try {     MultiUserLookupResponse result = apiInstance.users().findUsersById(ids, null, null, null);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling UsersApi#findUsersById");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

      `// Set the params values  // List<String> | Required. A list of User IDs, comma-separated. You can specify up to 100 IDs. List<String> ids = Arrays.asList("2244994945", "6253282");  // Set<String> | A comma separated list of fields to expand. Set<String> expansions = new HashSet<>(Arrays.asList("pinned_tweet_id"));  // Set<String> | A comma separated list of Tweet fields to display. Set<String> tweetFields = new HashSet<>(Arrays.asList("created_at"));  // Set<String> | A comma separated list of User fields to display. Set<String> userFields = new HashSet<>(Arrays.asList("created_at"));  try {     MultiUserLookupResponse result = apiInstance.users().findUsersById(ids, expansions, tweetFields, userFields);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling UsersApi#findUsersById");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

### Example responses

* [Default fields](#tab0)
* [Optional fields](#tab1)

Default fields

Optional fields

      `{   "data": [     {       "id": "2244994945",       "username": "TwitterDev",       "name": "Twitter Dev"     },     {       "id": "783214",       "username": "Twitter",       "name": "Twitter"     }   ] }`
    

      `{   "data": [     {       "created_at": "2013-12-14T04:35:55.000Z",       "username": "TwitterDev",       "pinned_tweet_id": "1255542774432063488",       "id": "2244994945",       "name": "Twitter Dev"     },     {       "created_at": "2007-02-20T14:35:54.000Z",       "username": "Twitter",       "pinned_tweet_id": "1274087687469715457",       "id": "783214",       "name": "Twitter"     }   ],   "includes": {     "tweets": [       {         "created_at": "2020-04-29T17:01:38.000Z",         "text": "During these unprecedented times, what’s happening on Twitter can help the world better understand &amp; respond to the pandemic. nnWe're launching a free COVID-19 stream endpoint so qualified devs &amp; researchers can study the public conversation in real-time. https://t.co/BPqMcQzhId",         "id": "1255542774432063488"       },       {         "created_at": "2020-06-19T21:12:30.000Z",         "text": "📍 Minneapolisn🗣️ @FredTJoseph https://t.co/lNTOkyguG1",         "id": "1274087687469715457"       }     ]   } }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Default | string | Unique identifier of this user. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. |
| `name`  <br> Default | string | The friendly name of this user, as shown on their profile. |
| `username`  <br> Default | string | The Twitter handle (screen name) of this user. |
| `created_at` | date (ISO 8601) | Creation time of this account.  <br>  <br>To return this field, add `user.fields=created_at` in the request's query parameter. |
| `most_recent_tweet_id` | string | The ID of the User's most recent Tweet  <br>  <br>To return this field, add `user.fields=most_recent_tweet_id` in the request's query parameter. |
| `protected` | boolean | Indicates if this user has chosen to protect their Tweets (in other words, if this user's Tweets are private).  <br>  <br>To return this field, add `user.fields=protected` in the request's query parameter. |
| `withheld` | object | Contains withholding details for [withheld content](https://help.twitter.com/en/rules-and-policies/tweet-withheld-by-country).  <br>  <br>To return this field, add `user.fields=withheld` in the request's query parameter. |
| `withheld.country_codes` | array | Provides a list of countries where this user is not available.  <br>  <br>To return this field, add `user.fields=withheld.country_codes` in the request's query parameter. |
| `withheld.scope` | enum (`tweet`, `user`) | Indicates whether the content being withheld is a Tweet or a user (this API will return `user`).  <br>  <br>To return this field, add `user.fields=withheld.scope` in the request's query parameter. |
| `location` | string | The location specified in the user's profile, if the user provided one. As this is a freeform value, it may not indicate a valid location, but it may be fuzzily evaluated when performing searches with location queries.  <br>  <br>To return this field, add `user.fields=location` in the request's query parameter. |
| `url` | string | The URL specified in the user's profile, if present.  <br>  <br>To return this field, add `user.fields=url` in the request's query parameter. |
| `description` | string | The text of this user's profile description (also known as bio), if the user provided one.  <br>  <br>To return this field, add `user.fields=description` in the request's query parameter. |
| `verified` | boolean | Indicate if this user is a verified Twitter user.  <br>  <br>To return this field, add `user.fields=verified` in the request's query parameter. |
| `verified_type` | enum (`blue`, `business`, `government`, `none`) | Indicates the type of verification for the Twitter account.  <br>  <br>To return this field, add `user.fields=verified_type` in the request's query parameter. |
| `entities` | object | This object and its children fields contain details about text that has a special meaning in the user's description.  <br>  <br>To return this field, add `user.fields=entities` in the request's query parameter. |
| `entities.url` | array | Contains details about the user's profile website. |
| `entities.url.urls` | array | Contains details about the user's profile website. |
| `entities.url.urls.start` | integer | The start position (zero-based) of the recognized user's profile website. All start indices are inclusive. |
| `entities.url.urls.end` | integer | The end position (zero-based) of the recognized user's profile website. This end index is exclusive. |
| `entities.url.urls.url` | string | The URL in the format entered by the user. |
| `entities.url.urls.expanded_url` | string | The fully resolved URL. |
| `entities.url.urls.display_url` | string | The URL as displayed in the user's profile. |
| `entities.description` | array | Contains details about URLs, Hashtags, Cashtags, or mentions located within a user's description. |
| `entities.description.urls` | array | Contains details about any URLs included in the user's description. |
| `entities.description.urls.start` | integer | The start position (zero-based) of the recognized URL in the user's description. All start indices are inclusive. |
| `entities.description.urls.end` | integer | The end position (zero-based) of the recognized URL in the user's description. This end index is exclusive. |
| `entities.description.urls.url` | string | The URL in the format entered by the user. |
| `entities.description.urls.expanded_url` | string | The fully resolved URL. |
| `entities.description.urls.display_url` | string | The URL as displayed in the user's description. |
| `entities.description.hashtags` | array | Contains details about text recognized as a Hashtag. |
| `entities.description.hashtags.start` | integer | The start position (zero-based) of the recognized Hashtag within the Tweet. All start indices are inclusive. |
| `entities.description.hashtags.end` | integer | The end position (zero-based) of the recognized Hashtag within the Tweet. This end index is exclusive. |
| `entities.description.hashtags.hashtag` | string | The text of the Hashtag. |
| `entities.description.mentions` | array | Contains details about text recognized as a user mention. |
| `entities.description.mentions.start` | integer | The start position (zero-based) of the recognized user mention within the Tweet. All start indices are inclusive. |
| `entities.description.mentions.end` | integer | The end position (zero-based) of the recognized user mention within the Tweet. This end index is exclusive. |
| `entities.description.mentions.username` | string | The part of text recognized as a user mention. |
| `entities.description.cashtags` | array | Contains details about text recognized as a Cashtag. |
| `entities.description.cashtags.start` | integer | The start position (zero-based) of the recognized Cashtag within the Tweet. All start indices are inclusive. |
| `entities.description.cashtags.end` | integer | The end position (zero-based) of the recognized Cashtag within the Tweet. This end index is exclusive. |
| `entities.description.cashtags.cashtag` | string | The text of the Cashtag. |
| `profile_image_url` | string | The URL to the profile image for this user, as shown on the user's profile. |
| `public_metrics` | object | Contains details about activity for this user. |
| `public_metrics.followers_count` | integer | Number of users who follow this user. |
| `public_metrics.following_count` | integer | Number of users this user is following. |
| `public_metrics.tweet_count` | integer | Number of Tweets (including Retweets) posted by this user. |
| `public_metrics.listed_count` | integer | Number of lists that include this user. |
| `pinned_tweet_id` | string | Unique identifier of this user's pinned Tweet.  <br>  <br>You can obtain the expanded object in `includes.tweets` by adding `expansions=pinned_tweet_id` in the request's query parameter. |
| `includes.tweets` | array | When including the `expansions=pinned_tweet_id` parameter, this includes the pinned Tweets attached to the returned users' profiles in the form of [Tweet objects](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) with their default fields and any additional fields requested using the `tweet.fields` parameter, assuming there is a referenced Tweet present in the returned Tweet(s). |
| `errors` | object | Contains details about errors that affected any of the requested users. See [Status codes and error messages](https://developer.twitter.com/en/support/twitter-api/error-troubleshooting) for more details. |

GET /2/users/by/username/:username

GET /2/users/by/username/:username
==================================

Returns a variety of information about one or more users specified by their usernames.

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Try a live request ❯](https://oauth-playground.glitch.me/?id=findUserByUsername&params=%28%27query%21%28%29%7Ebody%21%27%27%7Epath%21%28%27*%7E**username%21%27TwitterDev%27%29%01*_) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Fusers%2Fby%2Fusername%2F%7Busername%7D&method=get) 

### Endpoint URL

`https://api.twitter.com/2/users/by/username/:username`  
  

### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 2.0 App-only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only "Use this method to obtain information in the context of an unauthenticated public user. This method is for developers that just need read-only access to public information. Click to learn how to obtain an OAuth 2.0 App Access Token.")<br><br>[OAuth 1.0a](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) is also available for this endpoint.<br><br>[OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code "This method allows an authorized app to act on behalf of the user, as the user. It is typically used to access or post public information for a specific user, and it us useful when your app needs to be aware of the relationship between a user and what this endpoint returns. Click to learn how to authenticate with OAuth 2.0 Authorization Code with PKCE.") |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | App rate limit (Application-only): 300 requests per 15-minute window shared among all users of your app<br><br>User rate limit (User context): 900 requests per 15-minute window per each authenticated user |

### OAuth 2.0 scopes required by this endpoint

|     |
| --- |
| `tweet.read`<br><br>`users.read` |
| [Learn more about OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/twitter-api/oauth2) |

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `username`  <br> Required | string | The Twitter username (handle) of the user. |

  
  

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| `expansions`  <br> Optional | enum (`pinned_tweet_id`) | [Expansions](https://developer.twitter.com/en/docs/twitter-api/expansions) enable you to request additional data objects that relate to the originally returned users. The ID that represents the expanded data object will be included directly in the user data object, but the expanded object metadata will be returned within the `includes` response object, and will also include the ID so that you can match this data object to the original Tweet object. At this time, the only expansion available to endpoints that primarily return user objects is `expansions=pinned_tweet_id`. You will find the expanded Tweet data object living in the `includes` response object. |
| `tweet.fields`  <br> Optional | enum (`attachments`, `author_id`, `context_annotations`, `conversation_id`, `created_at`, `edit_controls`, `entities`, `geo`, `id`, `in_reply_to_user_id`, `lang`, `non_public_metrics`, `public_metrics`, `organic_metrics`, `promoted_metrics`, `possibly_sensitive`, `referenced_tweets`, `reply_settings`, `source`, `text`, `withheld`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [Tweet fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) will deliver in each returned pinned Tweet. Specify the desired fields in a comma-separated list without spaces between commas and fields. The Tweet fields will only return if the user has a pinned Tweet and if you've also included the `expansions=pinned_tweet_id` query parameter in your request. While the referenced Tweet ID will be located in the original Tweet object, you will find this ID and all additional Tweet fields in the `includes` data object. |
| `user.fields`  <br> Optional | enum (`created_at`, `description`, `entities`, `id`, `location`, `most_recent_tweet_id`, `name`, `pinned_tweet_id`, `profile_image_url`, `protected`, `public_metrics`, `url`, `username`, `verified`, `verified_type`, `withheld`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [user fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) will deliver with each returned users objects. Specify the desired fields in a comma-separated list without spaces between commas and fields. These specified user fields will display directly in the user data objects. |

  
  

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript (Default fields)](#tab0)
* [TypeScript (Optional fields)](#tab1)
* [Java (Default fields)](#tab2)
* [Java (Optional fields)](#tab3)

TypeScript (Default fields)

TypeScript (Optional fields)

Java (Default fields)

Java (Optional fields)

      `(async () => {   try {     const usernameLookup = await twitterClient.users.findUserByUsername(       //The Twitter username (handle) of the user.       "TwitterDev"     );     console.dir(usernameLookup, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `(async () => {   try {     const usernameLookup = await twitterClient.users.findUserByUsername(       //The Twitter username (handle) of the user.       "TwitterDev"       {         //A comma separated list of User fields to display         "user.fields": ["created_at"],                  //A comma separated list of Tweet fields to display.         "tweet.fields": ["created_at"],                  //A comma separated list of fields to expand         expansions: ["pinned_tweet_id"]       }     );     console.dir(usernameLookup, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  // String | Required. A username. String username = "TwitterDev";  try {     SingleUserLookupResponse result = apiInstance.users().findUserByUsername(username, null, null, null);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling UsersApi#findUserByUsername");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

      `// Set the params values  // String | Required. A username. String username = "TwitterDev";  // Set<String> | A comma separated list of fields to expand. Set<String> expansions = new HashSet<>(Arrays.asList("pinned_tweet_id"));  // Set<String> | A comma separated list of Tweet fields to display. Set<String> tweetFields = new HashSet<>(Arrays.asList("created_at"));  // Set<String> | A comma separated list of User fields to display. Set<String> userFields = new HashSet<>(Arrays.asList("created_at"));  try {     SingleUserLookupResponse result = apiInstance.users().findUserByUsername(username, expansions, tweetFields, userFields);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling UsersApi#findUserByUsername");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

### Example responses

* [Default fields](#tab0)
* [Optional fields](#tab1)

Default fields

Optional fields

      `{   "data": {     "id": "2244994945",     "name": "Twitter Dev",     "username": "TwitterDev"   } }`
    

      `{   "data": {     "username": "TwitterDev",     "created_at": "2013-12-14T04:35:55.000Z",     "pinned_tweet_id": "1255542774432063488",     "id": "2244994945",     "name": "Twitter Dev"   },   "includes": {     "tweets": [       {         "text": "During these unprecedented times, what’s happening on Twitter can help the world better understand &amp; respond to the pandemic. nnWe're launching a free COVID-19 stream endpoint so qualified devs &amp; researchers can study the public conversation in real-time. https://t.co/BPqMcQzhId",         "created_at": "2020-04-29T17:01:38.000Z",         "id": "1255542774432063488"       }     ]   } }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Default | string | Unique identifier of this user. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. |
| `name`  <br> Default | string | The friendly name of this user, as shown on their profile. |
| `username`  <br> Default | string | The Twitter handle (screen name) of this user. |
| `created_at` | date (ISO 8601) | Creation time of this account.  <br>  <br>To return this field, add `user.fields=created_at` in the request's query parameter. |
| `most_recent_tweet_id` | string | The ID of the User's most recent Tweet  <br>  <br>To return this field, add `user.fields=most_recent_tweet_id` in the request's query parameter. |
| `protected` | boolean | Indicates if this user has chosen to protect their Tweets (in other words, if this user's Tweets are private).  <br>  <br>To return this field, add `user.fields=protected` in the request's query parameter. |
| `withheld` | object | Contains withholding details for [withheld content](https://help.twitter.com/en/rules-and-policies/tweet-withheld-by-country).  <br>  <br>To return this field, add `user.fields=withheld` in the request's query parameter. |
| `withheld.country_codes` | array | Provides a list of countries where this user is not available.  <br>  <br>To return this field, add `user.fields=withheld.country_codes` in the request's query parameter. |
| `withheld.scope` | enum (`tweet`, `user`) | Indicates whether the content being withheld is a Tweet or a user (this API will return `user`).  <br>  <br>To return this field, add `user.fields=withheld.scope` in the request's query parameter. |
| `location` | string | The location specified in the user's profile, if the user provided one. As this is a freeform value, it may not indicate a valid location, but it may be fuzzily evaluated when performing searches with location queries.  <br>  <br>To return this field, add `user.fields=location` in the request's query parameter. |
| `url` | string | The URL specified in the user's profile, if present.  <br>  <br>To return this field, add `user.fields=url` in the request's query parameter. |
| `description` | string | The text of this user's profile description (also known as bio), if the user provided one.  <br>  <br>To return this field, add `user.fields=description` in the request's query parameter. |
| `verified` | boolean | Indicate if this user is a verified Twitter user.  <br>  <br>To return this field, add `user.fields=verified` in the request's query parameter. |
| `verified_type` | enum (`blue`, `business`, `government`, `none`) | Indicates the type of verification for the Twitter account.  <br>  <br>To return this field, add `user.fields=verified_type` in the request's query parameter. |
| `entities` | object | This object and its children fields contain details about text that has a special meaning in the user's description.  <br>  <br>To return this field, add `user.fields=entities` in the request's query parameter. |
| `entities.url` | array | Contains details about the user's profile website. |
| `entities.url.urls` | array | Contains details about the user's profile website. |
| `entities.url.urls.start` | integer | The start position (zero-based) of the recognized user's profile website. All start indices are inclusive. |
| `entities.url.urls.end` | integer | The end position (zero-based) of the recognized user's profile website. This end index is exclusive. |
| `entities.url.urls.url` | string | The URL in the format entered by the user. |
| `entities.url.urls.expanded_url` | string | The fully resolved URL. |
| `entities.url.urls.display_url` | string | The URL as displayed in the user's profile. |
| `entities.description` | array | Contains details about URLs, Hashtags, Cashtags, or mentions located within a user's description. |
| `entities.description.urls` | array | Contains details about any URLs included in the user's description. |
| `entities.description.urls.start` | integer | The start position (zero-based) of the recognized URL in the user's description. All start indices are inclusive. |
| `entities.description.urls.end` | integer | The end position (zero-based) of the recognized URL in the user's description. This end index is exclusive. |
| `entities.description.urls.url` | string | The URL in the format entered by the user. |
| `entities.description.urls.expanded_url` | string | The fully resolved URL. |
| `entities.description.urls.display_url` | string | The URL as displayed in the user's description. |
| `entities.description.hashtags` | array | Contains details about text recognized as a Hashtag. |
| `entities.description.hashtags.start` | integer | The start position (zero-based) of the recognized Hashtag within the Tweet. All start indices are inclusive. |
| `entities.description.hashtags.end` | integer | The end position (zero-based) of the recognized Hashtag within the Tweet. This end index is exclusive. |
| `entities.description.hashtags.hashtag` | string | The text of the Hashtag. |
| `entities.description.mentions` | array | Contains details about text recognized as a user mention. |
| `entities.description.mentions.start` | integer | The start position (zero-based) of the recognized user mention within the Tweet. All start indices are inclusive. |
| `entities.description.mentions.end` | integer | The end position (zero-based) of the recognized user mention within the Tweet. This end index is exclusive. |
| `entities.description.mentions.username` | string | The part of text recognized as a user mention. |
| `entities.description.cashtags` | array | Contains details about text recognized as a Cashtag. |
| `entities.description.cashtags.start` | integer | The start position (zero-based) of the recognized Cashtag within the Tweet. All start indices are inclusive. |
| `entities.description.cashtags.end` | integer | The end position (zero-based) of the recognized Cashtag within the Tweet. This end index is exclusive. |
| `entities.description.cashtags.cashtag` | string | The text of the Cashtag. |
| `profile_image_url` | string | The URL to the profile image for this user, as shown on the user's profile. |
| `public_metrics` | object | Contains details about activity for this user. |
| `public_metrics.followers_count` | integer | Number of users who follow this user. |
| `public_metrics.following_count` | integer | Number of users this user is following. |
| `public_metrics.tweet_count` | integer | Number of Tweets (including Retweets) posted by this user. |
| `public_metrics.listed_count` | integer | Number of lists that include this user. |
| `pinned_tweet_id` | string | Unique identifier of this user's pinned Tweet.  <br>  <br>You can obtain the expanded object in `includes.tweets` by adding `expansions=pinned_tweet_id` in the request's query parameter. |
| `includes.tweets` | array | When including the `expansions=pinned_tweet_id` parameter, this includes the pinned Tweets attached to the returned users' profiles in the form of [Tweet objects](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) with their default fields and any additional fields requested using the `tweet.fields` parameter, assuming there is a referenced Tweet present in the returned Tweet(s). |
| `errors` | object | Contains details about errors that affected any of the requested users. See [Status codes and error messages](https://developer.twitter.com/en/support/twitter-api/error-troubleshooting) for more details. |

GET /2/users/by

GET /2/users/by
===============

Returns a variety of information about one or more users specified by their usernames.

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Try a live request ❯](https://oauth-playground.glitch.me/?id=findUsersByUsername&params=%28%27query%21%28%27*%7Ebody%21%28%29%7Epath%21%28%29%7E**usernames%21%27-Dev%2C-%27%29-Twitter%01-*_) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Fusers%2Fby&method=get) 

### Endpoint URL

`https://api.twitter.com/2/users/by`  
  

### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 1.0a](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) is also available for this endpoint.<br><br>[OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code "This method allows an authorized app to act on behalf of the user, as the user. It is typically used to access or post public information for a specific user, and it us useful when your app needs to be aware of the relationship between a user and what this endpoint returns. Click to learn how to authenticate with OAuth 2.0 Authorization Code with PKCE.")<br><br>[OAuth 2.0 App-only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only "Use this method to obtain information in the context of an unauthenticated public user. This method is for developers that just need read-only access to public information. Click to learn how to obtain an OAuth 2.0 App Access Token.") |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | App rate limit (Application-only): 300 requests per 15-minute window shared among all users of your app<br><br>User rate limit (User context): 900 requests per 15-minute window per each authenticated user |

### OAuth 2.0 scopes required by this endpoint

|     |
| --- |
| `tweet.read`<br><br>`users.read` |
| [Learn more about OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/twitter-api/oauth2) |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| `usernames`  <br> Required | string | A comma separated list of Twitter usernames (handles). Up to 100 are allowed in a single request. Make sure to not include a space between commas and fields. |
| `expansions`  <br> Optional | enum (`pinned_tweet_id`) | [Expansions](https://developer.twitter.com/en/docs/twitter-api/expansions) enable you to request additional data objects that relate to the originally returned users. The ID that represents the expanded data object will be included directly in the user data object, but the expanded object metadata will be returned within the `includes` response object, and will also include the ID so that you can match this data object to the original Tweet object. At this time, the only expansion available to endpoints that primarily return user objects is `expansions=pinned_tweet_id`. You will find the expanded Tweet data object living in the `includes` response object. |
| `tweet.fields`  <br> Optional | enum (`attachments`, `author_id`, `context_annotations`, `conversation_id`, `created_at`, `edit_controls`, `entities`, `geo`, `id`, `in_reply_to_user_id`, `lang`, `non_public_metrics`, `public_metrics`, `organic_metrics`, `promoted_metrics`, `possibly_sensitive`, `referenced_tweets`, `reply_settings`, `source`, `text`, `withheld`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [Tweet fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) will deliver in each returned pinned Tweet. Specify the desired fields in a comma-separated list without spaces between commas and fields. The Tweet fields will only return if the user has a pinned Tweet and if you've also included the `expansions=pinned_tweet_id` query parameter in your request. While the referenced Tweet ID will be located in the original Tweet object, you will find this ID and all additional Tweet fields in the `includes` data object. |
| `user.fields`  <br> Optional | enum (`created_at`, `description`, `entities`, `id`, `location`, `most_recent_tweet_id`, `name`, `pinned_tweet_id`, `profile_image_url`, `protected`, `public_metrics`, `url`, `username`, `verified`, `verified_type`, `withheld`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [user fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) will deliver with each returned users objects. Specify the desired fields in a comma-separated list without spaces between commas and fields. These specified user fields will display directly in the user data objects. |

  
  

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript (Default fields)](#tab0)
* [TypeScript (Optional fields)](#tab1)
* [Java (Default fields)](#tab2)
* [Java (Optional fields)](#tab3)

TypeScript (Default fields)

TypeScript (Optional fields)

Java (Default fields)

Java (Optional fields)

      `(async () => {   try {     const usernamesLookup = await twitterClient.users.findUsersByUsername({       //A list of usernames, comma-separated. You can specify up to 100 usernames.       usernames: ["TwitterDev", "Twitter"]     });     console.dir(usernamesLookup, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `(async () => {   try {     const usernamesLookup = await twitterClient.users.findUsersByUsername({       //A list of usernames, comma-separated. You can specify up to 100 usernames.       usernames: ["TwitterDev", "Twitter"],        //A comma separated list of User fields to display       "user.fields": ["created_at"],        //A comma separated list of Tweet fields to display.       "tweet.fields": ["created_at"],        //A comma separated list of fields to expand       expansions: ["pinned_tweet_id"],     });     console.dir(usernamesLookup, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  // List<String> | Required . A list of usernames, comma-separated. You can specify up to 100 usernames. List<String> usernames = Arrays.asList("TwitterDev", "Twitter");  try {     MultiUserLookupResponse result = apiInstance.users().findUsersByUsername(usernames, null, null, null);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling UsersApi#findUsersByUsername");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

      `// Set the params values  // List<String> | Required . A list of usernames, comma-separated. You can specify up to 100 usernames. List<String> usernames = Arrays.asList("TwitterDev", "Twitter");  // Set<String> | A comma separated list of fields to expand. Set<String> expansions = new HashSet<>(Arrays.asList("pinned_tweet_id"));  // Set<String> | A comma separated list of Tweet fields to display. Set<String> tweetFields = new HashSet<>(Arrays.asList("created_at"));  // Set<String> | A comma separated list of User fields to display. Set<String> userFields = new HashSet<>(Arrays.asList("created_at"));  try {     MultiUserLookupResponse result = apiInstance.users().findUsersByUsername(usernames, expansions, tweetFields, userFields);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling UsersApi#findUsersByUsername");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

### Example responses

* [Default fields](#tab0)
* [Optional fields](#tab1)

Default fields

Optional fields

      `{   "data": [     {       "id": "2244994945",       "username": "TwitterDev",       "name": "Twitter Dev"     },     {       "id": "783214",       "username": "Twitter",       "name": "Twitter"     }   ] }`
    

      `{   "data": [     {       "created_at": "2013-12-14T04:35:55.000Z",       "username": "TwitterDev",       "pinned_tweet_id": "1255542774432063488",       "id": "2244994945",       "name": "Twitter Dev"     },     {       "created_at": "2007-02-20T14:35:54.000Z",       "username": "Twitter",       "pinned_tweet_id": "1274087687469715457",       "id": "783214",       "name": "Twitter"     }   ],   "includes": {     "tweets": [       {         "created_at": "2020-04-29T17:01:38.000Z",         "text": "During these unprecedented times, what’s happening on Twitter can help the world better understand &amp; respond to the pandemic. nnWe're launching a free COVID-19 stream endpoint so qualified devs &amp; researchers can study the public conversation in real-time. https://t.co/BPqMcQzhId",         "id": "1255542774432063488"       },       {         "created_at": "2020-06-19T21:12:30.000Z",         "text": "📍 Minneapolisn🗣️ @FredTJoseph https://t.co/lNTOkyguG1",         "id": "1274087687469715457"       }     ]   } }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Default | string | Unique identifier of this user. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. |
| `name`  <br> Default | string | The friendly name of this user, as shown on their profile. |
| `username`  <br> Default | string | The Twitter handle (screen name) of this user. |
| `created_at` | date (ISO 8601) | Creation time of this account.  <br>  <br>To return this field, add `user.fields=created_at` in the request's query parameter. |
| `most_recent_tweet_id` | string | The ID of the User's most recent Tweet  <br>  <br>To return this field, add `user.fields=most_recent_tweet_id` in the request's query parameter. |
| `protected` | boolean | Indicates if this user has chosen to protect their Tweets (in other words, if this user's Tweets are private).  <br>  <br>To return this field, add `user.fields=protected` in the request's query parameter. |
| `withheld` | object | Contains withholding details for [withheld content](https://help.twitter.com/en/rules-and-policies/tweet-withheld-by-country).  <br>  <br>To return this field, add `user.fields=withheld` in the request's query parameter. |
| `withheld.country_codes` | array | Provides a list of countries where this user is not available.  <br>  <br>To return this field, add `user.fields=withheld.country_codes` in the request's query parameter. |
| `withheld.scope` | enum (`tweet`, `user`) | Indicates whether the content being withheld is a Tweet or a user (this API will return `user`).  <br>  <br>To return this field, add `user.fields=withheld.scope` in the request's query parameter. |
| `location` | string | The location specified in the user's profile, if the user provided one. As this is a freeform value, it may not indicate a valid location, but it may be fuzzily evaluated when performing searches with location queries.  <br>  <br>To return this field, add `user.fields=location` in the request's query parameter. |
| `url` | string | The URL specified in the user's profile, if present.  <br>  <br>To return this field, add `user.fields=url` in the request's query parameter. |
| `description` | string | The text of this user's profile description (also known as bio), if the user provided one.  <br>  <br>To return this field, add `user.fields=description` in the request's query parameter. |
| `verified` | boolean | Indicate if this user is a verified Twitter user.  <br>  <br>To return this field, add `user.fields=verified` in the request's query parameter. |
| `verified_type` | enum (`blue`, `business`, `government`, `none`) | Indicates the type of verification for the Twitter account.  <br>  <br>To return this field, add `user.fields=verified_type` in the request's query parameter. |
| `entities` | object | This object and its children fields contain details about text that has a special meaning in the user's description.  <br>  <br>To return this field, add `user.fields=entities` in the request's query parameter. |
| `entities.url` | array | Contains details about the user's profile website. |
| `entities.url.urls` | array | Contains details about the user's profile website. |
| `entities.url.urls.start` | integer | The start position (zero-based) of the recognized user's profile website. All start indices are inclusive. |
| `entities.url.urls.end` | integer | The end position (zero-based) of the recognized user's profile website. This end index is exclusive. |
| `entities.url.urls.url` | string | The URL in the format entered by the user. |
| `entities.url.urls.expanded_url` | string | The fully resolved URL. |
| `entities.url.urls.display_url` | string | The URL as displayed in the user's profile. |
| `entities.description` | array | Contains details about URLs, Hashtags, Cashtags, or mentions located within a user's description. |
| `entities.description.urls` | array | Contains details about any URLs included in the user's description. |
| `entities.description.urls.start` | integer | The start position (zero-based) of the recognized URL in the user's description. All start indices are inclusive. |
| `entities.description.urls.end` | integer | The end position (zero-based) of the recognized URL in the user's description. This end index is exclusive. |
| `entities.description.urls.url` | string | The URL in the format entered by the user. |
| `entities.description.urls.expanded_url` | string | The fully resolved URL. |
| `entities.description.urls.display_url` | string | The URL as displayed in the user's description. |
| `entities.description.hashtags` | array | Contains details about text recognized as a Hashtag. |
| `entities.description.hashtags.start` | integer | The start position (zero-based) of the recognized Hashtag within the Tweet. All start indices are inclusive. |
| `entities.description.hashtags.end` | integer | The end position (zero-based) of the recognized Hashtag within the Tweet. This end index is exclusive. |
| `entities.description.hashtags.hashtag` | string | The text of the Hashtag. |
| `entities.description.mentions` | array | Contains details about text recognized as a user mention. |
| `entities.description.mentions.start` | integer | The start position (zero-based) of the recognized user mention within the Tweet. All start indices are inclusive. |
| `entities.description.mentions.end` | integer | The end position (zero-based) of the recognized user mention within the Tweet. This end index is exclusive. |
| `entities.description.mentions.username` | string | The part of text recognized as a user mention. |
| `entities.description.cashtags` | array | Contains details about text recognized as a Cashtag. |
| `entities.description.cashtags.start` | integer | The start position (zero-based) of the recognized Cashtag within the Tweet. All start indices are inclusive. |
| `entities.description.cashtags.end` | integer | The end position (zero-based) of the recognized Cashtag within the Tweet. This end index is exclusive. |
| `entities.description.cashtags.cashtag` | string | The text of the Cashtag. |
| `profile_image_url` | string | The URL to the profile image for this user, as shown on the user's profile. |
| `public_metrics` | object | Contains details about activity for this user. |
| `public_metrics.followers_count` | integer | Number of users who follow this user. |
| `public_metrics.following_count` | integer | Number of users this user is following. |
| `public_metrics.tweet_count` | integer | Number of Tweets (including Retweets) posted by this user. |
| `public_metrics.listed_count` | integer | Number of lists that include this user. |
| `pinned_tweet_id` | string | Unique identifier of this user's pinned Tweet.  <br>  <br>You can obtain the expanded object in `includes.tweets` by adding `expansions=pinned_tweet_id` in the request's query parameter. |
| `includes.tweets` | array | When including the `expansions=pinned_tweet_id` parameter, this includes the pinned Tweets attached to the returned users' profiles in the form of [Tweet objects](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) with their default fields and any additional fields requested using the `tweet.fields` parameter, assuming there is a referenced Tweet present in the returned Tweet(s). |
| `errors` | object | Contains details about errors that affected any of the requested users. See [Status codes and error messages](https://developer.twitter.com/en/support/twitter-api/error-troubleshooting) for more details. |

GET /2/users/me

GET /2/users/me
===============

Returns information about an authorized user.

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Try a live request ❯](https://oauth-playground.glitch.me/?id=findMyUser&params=%28%27query%21%28%29%7Ebody%21%27%27%7Epath%21%28%29%29_) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Fusers%2Fme&method=get) 

### Endpoint URL

`https://api.twitter.com/2/users/me`  
  

### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code "This method allows an authorized app to act on behalf of the user, as the user. It is typically used to access or post public information for a specific user, and it us useful when your app needs to be aware of the relationship between a user and what this endpoint returns. Click to learn how to authenticate with OAuth 2.0 Authorization Code with PKCE.")<br><br>[OAuth 1.0a](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) is also available for this endpoint. |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | User rate limit (User context): 75 requests per 15-minute window per each authenticated user |

### OAuth 2.0 scopes required by this endpoint

|     |
| --- |
| `tweet.read`<br><br>`users.read` |
| [Learn more about OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/twitter-api/oauth2) |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| `expansions`  <br> Optional | enum (`pinned_tweet_id`) | [Expansions](https://developer.twitter.com/en/docs/twitter-api/expansions) enable you to request additional data objects that relate to the originally returned users. The ID that represents the expanded data object will be included directly in the user data object, but the expanded object metadata will be returned within the `includes` response object, and will also include the ID so that you can match this data object to the original Tweet object. At this time, the only expansion available to endpoints that primarily return user objects is `expansions=pinned_tweet_id`. You will find the expanded Tweet data object living in the `includes` response object. |
| `tweet.fields`  <br> Optional | enum (`attachments`, `author_id`, `context_annotations`, `conversation_id`, `created_at`, `edit_controls`, `entities`, `geo`, `id`, `in_reply_to_user_id`, `lang`, `non_public_metrics`, `public_metrics`, `organic_metrics`, `promoted_metrics`, `possibly_sensitive`, `referenced_tweets`, `reply_settings`, `source`, `text`, `withheld`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [Tweet fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) will deliver in each returned pinned Tweet. Specify the desired fields in a comma-separated list without spaces between commas and fields. The Tweet fields will only return if the user has a pinned Tweet and if you've also included the `expansions=pinned_tweet_id` query parameter in your request. While the referenced Tweet ID will be located in the original Tweet object, you will find this ID and all additional Tweet fields in the `includes` data object. |
| `user.fields`  <br> Optional | enum (`created_at`, `description`, `entities`, `id`, `location`, `most_recent_tweet_id`, `name`, `pinned_tweet_id`, `profile_image_url`, `protected`, `public_metrics`, `url`, `username`, `verified`, `verified_type`, `withheld`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [user fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) will deliver with each returned users objects. Specify the desired fields in a comma-separated list without spaces between commas and fields. These specified user fields will display directly in the user data objects. |

  
  

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript (Default fields)](#tab0)
* [TypeScript (Optional fields)](#tab1)
* [Java (Default fields)](#tab2)
* [Java (Optional fields)](#tab3)

TypeScript (Default fields)

TypeScript (Optional fields)

Java (Default fields)

Java (Optional fields)

      `(async () => {   try {     const getCurrentUser = await twitterClient.users.findMyUser();     console.dir(getCurrentUser, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `(async () => {   try {     const getCurrentUser = await twitterClient.users.findMyUser({       //A comma separated list of User fields to display       "user.fields": ["created_at"],        //A comma separated list of Tweet fields to display.       "tweet.fields": ["created_at"],        //A comma separated list of fields to expand       expansions: ["pinned_tweet_id"],     });     console.dir(getCurrentUser, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `try {     SingleUserLookupResponse result = apiInstance.users().findMyUser(null, null, null);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling UsersApi#findMyUser");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

      `// Set the params values  // Set<String> | A comma separated list of fields to expand. Set<String> expansions = new HashSet<>(Arrays.asList("pinned_tweet_id"));  // Set<String> | A comma separated list of Tweet fields to display. Set<String> tweetFields = new HashSet<>(Arrays.asList("created_at"));  // Set<String> | A comma separated list of User fields to display. Set<String> userFields = new HashSet<>(Arrays.asList("created_at"));  try {     SingleUserLookupResponse result = apiInstance.users().findMyUser(expansions, tweetFields, userFields);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling UsersApi#findMyUser");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

### Example responses

* [Default fields](#tab0)
* [Optional fields](#tab1)

Default fields

Optional fields

      `{   "data": {     "id": "2244994945",     "name": "TwitterDev",     "username": "Twitter Dev"   } }`
    

      `{   "data": {     "created_at": "2013-12-14T04:35:55.000Z",     "username": "TwitterDev",     "pinned_tweet_id": "1255542774432063488",     "id": "2244994945",     "name": "Twitter Dev"   } }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Default | string | Unique identifier of this user. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. |
| `name`  <br> Default | string | The friendly name of this user, as shown on their profile. |
| `username`  <br> Default | string | The Twitter handle (screen name) of this user. |
| `created_at` | date (ISO 8601) | Creation time of this account.  <br>  <br>To return this field, add `user.fields=created_at` in the request's query parameter. |
| `most_recent_tweet_id` | string | The ID of the User's most recent Tweet  <br>  <br>To return this field, add `user.fields=most_recent_tweet_id` in the request's query parameter. |
| `protected` | boolean | Indicates if this user has chosen to protect their Tweets (in other words, if this user's Tweets are private).  <br>  <br>To return this field, add `user.fields=protected` in the request's query parameter. |
| `withheld` | object | Contains withholding details for [withheld content](https://help.twitter.com/en/rules-and-policies/tweet-withheld-by-country).  <br>  <br>To return this field, add `user.fields=withheld` in the request's query parameter. |
| `withheld.country_codes` | array | Provides a list of countries where this user is not available.  <br>  <br>To return this field, add `user.fields=withheld.country_codes` in the request's query parameter. |
| `withheld.scope` | enum (`tweet`, `user`) | Indicates whether the content being withheld is a Tweet or a user (this API will return `user`).  <br>  <br>To return this field, add `user.fields=withheld.scope` in the request's query parameter. |
| `location` | string | The location specified in the user's profile, if the user provided one. As this is a freeform value, it may not indicate a valid location, but it may be fuzzily evaluated when performing searches with location queries.  <br>  <br>To return this field, add `user.fields=location` in the request's query parameter. |
| `url` | string | The URL specified in the user's profile, if present.  <br>  <br>To return this field, add `user.fields=url` in the request's query parameter. |
| `description` | string | The text of this user's profile description (also known as bio), if the user provided one.  <br>  <br>To return this field, add `user.fields=description` in the request's query parameter. |
| `verified` | boolean | Indicate if this user is a verified Twitter user.  <br>  <br>To return this field, add `user.fields=verified` in the request's query parameter. |
| `verified_type` | enum (`blue`, `business`, `government`, `none`) | Indicates the type of verification for the Twitter account.  <br>  <br>To return this field, add `user.fields=verified_type` in the request's query parameter. |
| `entities` | object | This object and its children fields contain details about text that has a special meaning in the user's description.  <br>  <br>To return this field, add `user.fields=entities` in the request's query parameter. |
| `entities.url` | array | Contains details about the user's profile website. |
| `entities.url.urls` | array | Contains details about the user's profile website. |
| `entities.url.urls.start` | integer | The start position (zero-based) of the recognized user's profile website. All start indices are inclusive. |
| `entities.url.urls.end` | integer | The end position (zero-based) of the recognized user's profile website. This end index is exclusive. |
| `entities.url.urls.url` | string | The URL in the format entered by the user. |
| `entities.url.urls.expanded_url` | string | The fully resolved URL. |
| `entities.url.urls.display_url` | string | The URL as displayed in the user's profile. |
| `entities.description` | array | Contains details about URLs, Hashtags, Cashtags, or mentions located within a user's description. |
| `entities.description.urls` | array | Contains details about any URLs included in the user's description. |
| `entities.description.urls.start` | integer | The start position (zero-based) of the recognized URL in the user's description. All start indices are inclusive. |
| `entities.description.urls.end` | integer | The end position (zero-based) of the recognized URL in the user's description. This end index is exclusive. |
| `entities.description.urls.url` | string | The URL in the format entered by the user. |
| `entities.description.urls.expanded_url` | string | The fully resolved URL. |
| `entities.description.urls.display_url` | string | The URL as displayed in the user's description. |
| `entities.description.hashtags` | array | Contains details about text recognized as a Hashtag. |
| `entities.description.hashtags.start` | integer | The start position (zero-based) of the recognized Hashtag within the Tweet. All start indices are inclusive. |
| `entities.description.hashtags.end` | integer | The end position (zero-based) of the recognized Hashtag within the Tweet. This end index is exclusive. |
| `entities.description.hashtags.hashtag` | string | The text of the Hashtag. |
| `entities.description.mentions` | array | Contains details about text recognized as a user mention. |
| `entities.description.mentions.start` | integer | The start position (zero-based) of the recognized user mention within the Tweet. All start indices are inclusive. |
| `entities.description.mentions.end` | integer | The end position (zero-based) of the recognized user mention within the Tweet. This end index is exclusive. |
| `entities.description.mentions.username` | string | The part of text recognized as a user mention. |
| `entities.description.cashtags` | array | Contains details about text recognized as a Cashtag. |
| `entities.description.cashtags.start` | integer | The start position (zero-based) of the recognized Cashtag within the Tweet. All start indices are inclusive. |
| `entities.description.cashtags.end` | integer | The end position (zero-based) of the recognized Cashtag within the Tweet. This end index is exclusive. |
| `entities.description.cashtags.cashtag` | string | The text of the Cashtag. |
| `profile_image_url` | string | The URL to the profile image for this user, as shown on the user's profile. |
| `public_metrics` | object | Contains details about activity for this user. |
| `public_metrics.followers_count` | integer | Number of users who follow this user. |
| `public_metrics.following_count` | integer | Number of users this user is following. |
| `public_metrics.tweet_count` | integer | Number of Tweets (including Retweets) posted by this user. |
| `public_metrics.listed_count` | integer | Number of lists that include this user. |
| `pinned_tweet_id` | string | Unique identifier of this user's pinned Tweet.  <br>  <br>You can obtain the expanded object in `includes.tweets` by adding `expansions=pinned_tweet_id` in the request's query parameter. |
| `includes.tweets` | array | When including the `expansions=pinned_tweet_id` parameter, this includes the pinned Tweets attached to the returned users' profiles in the form of [Tweet objects](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) with their default fields and any additional fields requested using the `tweet.fields` parameter, assuming there is a referenced Tweet present in the returned Tweet(s). |
| `errors` | object | Contains details about errors that affected any of the requested users. See [Status codes and error messages](https://developer.twitter.com/en/support/twitter-api/error-troubleshooting) for more details. |

Introduction

Introduction
------------

Following users is one of the most foundational actions on Twitter. 

We offer two sets of endpoint groups to help you lookup, create, and delete follow relationships: follows lookup and manage follows.  
 

### Follows lookup

The follows lookup endpoints enable you to explore and analyze relationships between users, which is sometimes called network analysis. Specifically, there are two REST endpoints that return [user objects](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) representing who a specified user is following, or who is following a specified user.

You can authenticate this endpoint with either [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a), [App only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only), or [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code). You can request up to 1,000 users per request, and pagination tokens will be provided for paging through large sets of results.  
 

### Manage follows

The manage follows endpoints enable you to follow or unfollow users.

Since you are making requests on behalf of a user, you must authenticate these endpoints with either [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) or [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code), and utilize the user Access Tokens associated with the user you are making the request on behalf of. You can generate this user Access Token using the [3-legged OAuth flow](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens) (OAuth 1.0a) or using the [Authorization Code with PKCE grant flow](https://developer.twitter.com/en/docs/authentication/oauth-2-0/user-access-token) (OAuth 2.0).

You are limited to 400 follow actions per day on behalf of each authenticated user, and will be limited to 1,000 actions per day per App across all of your authenticated users. For example, if you have five authenticated users, you can follow 400 users per day (per user limit) with two of those users for a total of 800 actions, and will have to split the remaining 200 actions (per app) amongst the remaining three users. This limit does not apply to the unfollow endpoint, which has a separate limit of 500 actions per day (per app).

**Account setup**

To access these endpoints, you will need:

* An approved [developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info).
* To authenticate using the keys and tokens from a [developer App](https://developer.twitter.com/en/docs/apps) that is located within a [Project](https://developer.twitter.com/en/docs/projects). 

Learn more about getting access to the Twitter API v2 endpoints in our [getting started guide](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api).

[Quick start](https://developer.twitter.com/en/docs/twitter-api/users/follows/quick-start)

[Sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code)

[Run in Postman](https://t.co/twitter-api-postman)

[Try with API Explorer](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Fusers%2F%7Bid%7D%2Ffollowers&method=get)

Supporting resources
--------------------

[Learn how to use Postman to make requests](https://developer.twitter.com/en/docs/tutorials/postman-getting-started "Learn how to use Postman to make requests")

[Troubleshoot an error](https://developer.twitter.com/en/support/twitter-api "Troubleshoot an error")

[Visit the API reference page for this endpoint](https://developer.twitter.com/en/docs/twitter-api/users/follows/api-reference "Visit the API reference page for this endpoint")

Manage follows quick start

Getting started with the manage follows endpoints
-------------------------------------------------

This quick start guide will help you make your first request to the manage follows endpoints using [Postman](https://developer.twitter.com/en/docs/tutorials/postman-getting-started).

If you would like to see sample code in different languages, please visit our [Twitter API v2 sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code) GitHub repository.   

### Prerequisites

To complete this guide, you will need to have a set of [keys and tokens](https://developer.twitter.com/en/docs/authentication) to authenticate your request. You can generate these keys and tokens by following these steps:

* [Sign up for a developer account](https://developer.twitter.com/en/apply-for-access) and receive approval.
* Create a [Project](https://developer.twitter.com/en/docs/projects) and an associated [developer App](https://developer.twitter.com/en/docs/apps) in the developer portal.
* Navigate to your App's “Keys and tokens” page to generate the required credentials. Make sure to save all credentials in a secure location.

### Steps to build a manage follows request

#### Step one: Start with a tool or library

There are several different tools, code examples, and libraries that you can use to make a request to this endpoint, but we are going to use the Postman tool here to simplify the process.

To load the Twitter API v2 Postman collection into your environment, please click on the following button:

[Add Twitter API v2 to Postman](https://t.co/twitter-api-postman)

Once you have the Twitter API v2 collection loaded in Postman, navigate to the “Follows” folder, and select “Follow a user ID”.  
 

#### Step two: Authenticate your request

To properly make a request to the Twitter API, you need to verify that you have permission. To do so with this endpoint, you must authenticate your request using either [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) or [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code).

In this example, we are going to use OAuth 1.0a User Context.

You must add your keys and tokens – specifically your API Key, API Secret Key, OAuth 1.0a user Access Token, and OAuth 1.0a user Access Token Secret – to Postman. You can do this by selecting the environment named “Twitter API v2” in the top-right corner of Postman and adding your keys and tokens to the "initial value" and "current value" fields (by clicking the eye icon next to the environment dropdown).

These variables will automatically be pulled into the request's authorization tab if you've done this correctly.  
 

#### Step three: Specify who is going to follow whom

Manage follows endpoints take two IDs: one for the source user (the user who wishes to follow or unfollow another user) and the target user (the user that will be followed or unfollowed). The source user’s ID must correspond to the user ID of the authenticating user. In this case, you can specify the ID belonging to your own user. You can find your ID in two ways:

1. Using the [user lookup by username](https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference) endpoint, you can pass a username and receive the id field. 
2. Looking at your Access Token, you will find that the numeric part is your user ID.  
     

The target ID can be any valid user ID. For example the user ID for @TwitterDev is 2244994945.

In Postman, navigate to the "Params" tab, and enter your ID into the "Value" column of the id path variable. Navigate to the “Body” tab and and 2244994945 (the user ID for @TwitterDev) as the value for the target\_user\_id parameter. Making sure to not include any spaces before or after any ID.

|     |     |
| --- | --- |
| **Key** | **Value** |
| `id` | (your user ID) |
| target\_user\_id | 2244994945 |

  
If you click the "Send" button, you will receive a response object containing the status of the relationship:

* If you receive a "following": true, then the id is successfully following the target\_user\_id.
* If you receive a "pending": true, then the target\_user\_id is protected and must accept your follow request.

####   
Step four: Make your request and review your response

Once you have everything set up, hit the "Send" button and you will receive the following response:

      `{     "data": {         "following": true,         "pending_follow": false     } }`
    

Similarly, if you were trying to unfollow a user, you would use the "Unfollow a user ID" request within the same Postman collection. However, both the source\_user\_id and target\_user\_id parameters should be passed as path variables using the unfollow endpoint. 

Next steps
----------

[Customize your request using the API Reference](https://developer.twitter.com/en/docs/twitter-api/users/follows/api-reference "Customize your request using the API Reference")

[Reach out to the community for help](https://twittercommunity.com/ "Reach out to the community for help")

Migrate

Comparing Twitter API’s follows endpoints
-----------------------------------------

### Follows lookup

The v2 follows lookup endpoints will replace the standard v1.1 [followers/ids](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-followers-ids), v1.1 [followers/list](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-followers-list), v1.1 [friends/ids](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-friends-ids), and v1.1 [friends/list](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-friends-list) endpoints.

The following tables compare the various types of follows lookup endpoints:

|     |     |     |
| --- | --- | --- |
| **Description** | **Standard v1.1** | **Twitter API v2** |
| HTTP methods supported | `GET` | `GET` |
| Host domain | `https://api.twitter.com` | `https://api.twitter.com` |
| Endpoint path | /1.1/friends/ids.json<br><br>/1.1/friends/list.json<br><br>/1.1/followers/ids.json<br><br>/1.1/followers/list.json | /2/users/:id/following<br><br>/2/users/:id/followers |
| [Authentication](https://developer.twitter.com/en/docs/authentication) | OAuth 1.0a User Context<br><br>App only | OAuth 1.0a User Context<br><br>OAuth 2.0 Authorization Code with PKCE<br><br>App only |
| Default request [rate limits](https://developer.twitter.com/en/docs/rate-limits) | 15 requests per 15 min (per user)<br><br>15 requests per 15 min (per app) | 15 requests per 15 min (per user)<br><br>15 requests per 15 min (per app) |
| Maximum users per response | GET friends/id & GET followers/id return a maximum of 5000 users IDs per page.<br><br>  <br><br>GET friends/list & GET followers/list return a maximum of 200 user objects per page. | 1000 user objects per page |
| Pagination | Token returns in a next\_cursor field, which can then be passed as the value to the cursor parameter to return the next page of results. | Token returns in a next\_token field, which can then be passed as the value to the token parameter to return the next page of results.<br><br>The v2 payload also delivers a previous\_token field, which can also be passed with the pagination\_token parameter to return the previous page of results. |
| JSON format | Standard v1.1 format | [Twitter API v2 format](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/data-dictionary) (determined by fields and expansions request parameters, not backward-compatible with v1.1 formats)<br><br>To learn more about how to migrate from the Standard v1.1 format to the Twitter API v2 format, please visit our [data formats migration guide](https://developer.twitter.com/en/docs/twitter-api/migrate/data-formats). |
| Supports selecting which [fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary) return in the payload |     | ✔   |
| Supports the Tweet [annotations](https://developer.twitter.com/en/docs/twitter-api/annotations) fields |     | ✔   |
| Supports requesting new [metrics](https://developer.twitter.com/en/docs/twitter-api/metrics) fields |     | ✔   |
| Supports the [conversation\_id](https://developer.twitter.com/en/docs/twitter-api/conversation-id) field |     | ✔   |
| Requires the use of credentials from a [developer App](https://developer.twitter.com/en/docs/apps) associated with a [project](https://developer.twitter.com/en/docs/projects) |     | ✔   |

### Manage follows

The v2 manage follows endpoints will replace the standard v1.1 [POST friendships/create](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/post-friendships-create) and [POST friendships/destroy](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/post-friendships-destroy) endpoints.

The following tables compare the standard v1.1 and Twitter API v2 create follow endpoints:

#### Follow a user

| Description | Standard v1.1 | Twitter API v2 |
| --- | --- | --- |
| HTTP methods supported | POST | POST |
| Host domain | https://api.twitter.com | https://api.twitter.com |
| Endpoint path | /1.1/friendships/create.json | /2/users/:id/following |
| [Authentication](https://developer.twitter.com/content/developer-twitter/en/docs/authentication) | OAuth 1.0a User Context | OAuth 1.0a User Context<br><br>OAuth 2.0 Authorization Code with PKCE |
| Default request [rate limits](https://developer.twitter.com/content/developer-twitter/en/docs/rate-limits) | 50 requests per 15 min | 50 requests per 15 min |
| Maximum daily operations per users | 400 | 400 |
| Maximum daily operations per app | 1000 | 1000 |
| Requires use of credentials from a [developer App](https://developer.twitter.com/en/docs/apps) that is associated with a [Project](https://developer.twitter.com/en/docs/projects) |     | ✔️  |

#### Unfollow a user

The following tables compare the standard v1.1 and Twitter API v2 delete follow endpoints:

| Description | Standard v1.1 | Twitter API v2 |
| --- | --- | --- |
| HTTP methods supported | POST | DELETE |
| Host domain | https://api.twitter.com | https://api.twitter.com |
| Endpoint path | /1.1/friendships/destroy.json | /2/users/:source\_user\_id/following/:target\_user\_id |
| [Authentication](https://developer.twitter.com/content/developer-twitter/en/docs/authentication) | OAuth 1.0a User Context | OAuth 1.0a User Context<br><br>OAuth 2.0 Authorization Code with PKCE |
| Default request [rate limits](https://developer.twitter.com/content/developer-twitter/en/docs/rate-limits) | 15 requests per 15 min (per user) | 50 requests per 15 min (per user) |
| Maximum daily operations per app | None | 500 |
| Requires use of credentials from a [developer App](https://developer.twitter.com/en/docs/apps) that is associated with a [Project](https://developer.twitter.com/en/docs/projects) |     | ✔️  |

Other migration resources
-------------------------

[Follows lookup: Standard v1.1 to Twitter API v2](https://developer.twitter.com/en/docs/twitter-api/users/follows/migrate/follows-lookup-standard-to-twitter-api-v2 "Follows lookup: Standard v1.1 to Twitter API v2")

[Manage follows: Standard v1.1 to Twitter API v2](https://developer.twitter.com/en/docs/twitter-api/users/follows/migrate/manage-follows-standard-to-twitter-api-v2 "Manage follows: Standard v1.1 to Twitter API v2")

[Twitter API migration hub](https://developer.twitter.com/en/docs/twitter-api/migrate "Twitter API migration hub")

Manage follows: Standard v1.1 compared to Twitter API v2

Manage follows: Standard v1.1 compared to Twitter API v2
--------------------------------------------------------

If you have been working with the standard v1.1 [POST friendships/create](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/post-friendships-create) and [POST friendships/destroy](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/post-friendships-destroy) endpoints, the goal of this guide is to help you understand the similarities and differences between the standard and Twitter API v2 manage follows endpoints.

* **Similarities**
    * OAuth 1.0a User Context
* **Differences**
    * Endpoint URLs
    * App and Project requirements
    * HTTP methods
    * Request parameters  
          
         

### Similarities

#### OAuth 1.0a User Context authentication method

Both the endpoint versions support [OAuth 1.0a User Context](https://developer.twitter.com/content/developer-twitter/en/docs/authentication/oauth-1-0a). Therefore, if you were previously using one of the standard v1.1 manage follows endpoints, you can continue using the same authentication method if you migrate to the Twitter API v2 version. 

### Differences

#### Endpoint URLs

* Standard v1.1 endpoints:
    * POST https://api.twitter.com/1.1/friendships/create.json  
        (follow a user)
    * POST https://api.twitter.com/1.1/friendships/destroy.json  
        (unfollow a user)
* Twitter API v2 endpoint:
    * POST https://api.twitter.com/2/users/:id/following  
        (follow a user)
    * DELETE https://api.twitter.com/2/users/:source\_user\_id/following/:target\_user\_id  
        (unfollow a user) 

#### App and Project requirements

The Twitter API v2 endpoints require that you use credentials from a [developer App](https://developer.twitter.com/en/docs/apps) that is associated to a [Project](https://developer.twitter.com/en/docs/projects) when authenticating your requests. All Twitter API v1.1 endpoints can use credentials from standalone Apps or Apps associated with a project.  
  

#### Request parameters

The following standard v1.1 request parameters have equivalents in Twitter API v2:

| Standard v1.1 | Twitter API v2 |
| --- | --- |
| No equivalent | id (POST), source\_user\_id (DELETE) |
| user\_id | target\_user\_id |
| screen\_name | No equivalent |

Please note that the Standard v1.1 parameters are passed as query parameters, whereas the Twitter API v2 parameters are passed as body parameters (for the POST endpoint) or path parameters (for the DELETE endpoint).

Also, the v2 id and source\_user\_id are not required when using the standard v1.1 endpoints since the Access Tokens passed with OAuth 1.0a User Context inferred which user was initiating the follow/unfollow.   
  

Next steps
----------

[Check out our quick start guide for Twitter API v2 manage follows](https://developer.twitter.com/en/docs/twitter-api/users/follows/quick-start/manage-follows "Check out our quick start guide for Twitter API v2 manage follows")

[Review the API reference for the v2 follows endpoints](https://developer.twitter.com/en/docs/twitter-api/users/follows/api-reference "Review the API reference for the v2 follows endpoints")

API reference

API reference index
-------------------

For the complete API reference, select an endpoint from the list:

### Manage follows

|     |     |
| --- | --- |
| **Allows a user ID to follow another user** | `[POST /2/users/:id/following](https://developer.twitter.com/en/docs/twitter-api/users/follows/api-reference/post-users-source_user_id-following)` |
| **Allows a user ID to unfollow another user** | `[DELETE /2/users/:source_user_id/following/:target_user_id](https://developer.twitter.com/en/docs/twitter-api/users/follows/api-reference/delete-users-source_id-following)` |

POST /2/users/:id/following

POST /2/users/:id/following
===========================

Allows a user ID to follow another user.  
  
If the target user does not have public Tweets, this endpoint will send a follow request.  
  
The request succeeds with no action when the authenticated user sends a request to a user they're already following, or if they're sending a follower request to a user that does not have public Tweets.

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Try a live request ❯](https://oauth-playground.glitch.me/?id=usersIdFollow&params=%28%27query%21%28%29%7Ebody%21%28%27target*2244994945%27%29%7Epath%21%28%21source*6253282%27%29%29*_user_id%21%27%01*_) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Fusers%2F%7Bid%7D%2Ffollowing&method=post) 

### Endpoint URL

`https://api.twitter.com/2/users/:id/following`  
  

### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 1.0a](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) is also available for this endpoint.<br><br>[OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code "This method allows an authorized app to act on behalf of the user, as the user. It is typically used to access or post public information for a specific user, and it us useful when your app needs to be aware of the relationship between a user and what this endpoint returns. Click to learn how to authenticate with OAuth 2.0 Authorization Code with PKCE.") |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | User rate limit (User context): 50 requests per 15-minute window per each authenticated user |

### OAuth 2.0 scopes required by this endpoint

|     |
| --- |
| `tweet.read`<br><br>`users.read`<br><br>`follows.write` |
| [Learn more about OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/twitter-api/oauth2) |

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Required | string | The authenticated user ID who you would like to initiate the follow on behalf of. You must pass the [Access Tokens](https://developer.twitter.com/en/docs/authentication/oauth-2-0/user-access-token) that relate to this user when authenticating the request. |

  
  

### JSON body parameters

| Name | Type | Description |
| --- | --- | --- |
| `target_user_id`  <br> Required | string | The user ID of the user that you would like the `id` to follow. |

  
  

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript](#tab0)
* [Java](#tab1)

TypeScript

Java

      `(async () => {   try {     const followUser = await twitterClient.users.usersIdFollow(       //The ID of the user that is requesting to follow the target user       "6253282",       {         //The ID of the user that the source user is requesting to follow         target_user_id: "2244994945",       }     );     console.dir(followUser, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  UsersIdFollowRequest usersIdFollowRequest = new UsersIdFollowRequest();  //The ID of the user that the source user is requesting to follow usersIdFollowRequest.targetUserId("2244994945");  // String | The ID of the user that is requesting to follow the target user String id = "6253282";  try {     UsersFollowingCreateResponse result = apiInstance.users().usersIdFollow(usersIdFollowRequest, id);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling UsersApi#usersIdFollow");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

### Example responses

* [Successful response (public user)](#tab0)
* [Successful response (protected user)](#tab1)

Successful response (public user)

Successful response (protected user)

      `{   "data": {     "following": true,     "pending_follow": false   } }`
    

      `{   "data": {     "following": false,     "pending_follow": true   } }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `following` | boolean | Indicates whether the `id` is following the specified user as a result of this request. This value is `false` if the target user does not have public Tweets, as they will have to approve the follower request. |
| `pending_follow` | boolean | Indicates whether the target user will need to approve the follow request. Note that the authenticated user will follow the target user only when they approve the incoming follower request. |

DELETE /2/users/:source\_user\_id/following/:target\_user\_id

DELETE /2/users/:source\_user\_id/following/:target\_user\_id
=============================================================

Allows a user ID to unfollow another user.  
  
The request succeeds with no action when the authenticated user sends a request to a user they're not following or have already unfollowed.

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Try a live request ❯](https://oauth-playground.glitch.me/?id=usersIdUnfollow&params=%28%27query%21%28%29%7Ebody%21%28%29%7Epath%21%28%21source*6253282%27%2C%21target*2244994945%27%29%29*_user_id%21%27%01*_) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Fusers%2F%7Bsource_user_id%7D%2Ffollowing%2F%7Btarget_user_id%7D&method=delete) 

### Endpoint URL

`https://api.twitter.com/2/users/:source_user_id/following/:target_user_id`  
  

### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code "This method allows an authorized app to act on behalf of the user, as the user. It is typically used to access or post public information for a specific user, and it us useful when your app needs to be aware of the relationship between a user and what this endpoint returns. Click to learn how to authenticate with OAuth 2.0 Authorization Code with PKCE.")<br><br>[OAuth 1.0a](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) is also available for this endpoint. |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | User rate limit (User context): 50 requests per 15-minute window per each authenticated user |

### OAuth 2.0 scopes required by this endpoint

|     |
| --- |
| `tweet.read`<br><br>`users.read`<br><br>`follows.write` |
| [Learn more about OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/twitter-api/oauth2) |

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `source_user_id`  <br> Required | string | The user ID who you would like to initiate the unfollow on behalf of. You must pass the [Access Tokens](https://developer.twitter.com/en/docs/authentication/oauth-2-0/user-access-token) that relate to this user when authenticating the request. |
| `target_user_id`  <br> Required | string | The user ID of the user that you would like the `source_user_id` to unfollow. |

  
  

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript](#tab0)
* [Java](#tab1)

TypeScript

Java

      `(async () => {   try {     const unfollowUser = await twitterClient.users.usersIdUnfollow(       //The ID of the user that is requesting to unfollow the target user       "2244994945",        //The ID of the user that the source user is requesting to unfollow       "6253282"     );     console.dir(unfollowUser, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  // String | The ID of the user that is requesting to unfollow the target user String sourceUserId = "2244994945";  // String | The ID of the user that the source user is requesting to unfollow String targetUserId = "6253282";  try {     UsersFollowingDeleteResponse result = apiInstance.users().usersIdUnfollow(sourceUserId, targetUserId);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling UsersApi#usersIdUnfollow");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

### Example responses

* [Successful response](#tab0)

Successful response

      `{   "data": {     "following": false   } }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `following` | boolean | Indicates whether the source\_user\_id is unfollowing the specified user as a result of this request. This value is `false` for a successful the unfollow request. |

GET /2/users/:id/followers

GET /2/users/:id/followers
==========================

Returns a list of users who are followers of the specified user ID.

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Try a live request ❯](https://oauth-playground.glitch.me/?id=usersIdFollowers&params=%28%27query%21%28%29%7Ebody%21%27%27%7Epath%21%28%27*%7E**id%21%272244994945%27%29%01*_) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Fusers%2F%7Bid%7D%2Ffollowers&method=get) 

### Endpoint URL

`https://api.twitter.com/2/users/:id/followers`  
  

### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code "This method allows an authorized app to act on behalf of the user, as the user. It is typically used to access or post public information for a specific user, and it us useful when your app needs to be aware of the relationship between a user and what this endpoint returns. Click to learn how to authenticate with OAuth 2.0 Authorization Code with PKCE.")<br><br>[OAuth 1.0a](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) is also available for this endpoint.<br><br>[OAuth 2.0 App-only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only "Use this method to obtain information in the context of an unauthenticated public user. This method is for developers that just need read-only access to public information. Click to learn how to obtain an OAuth 2.0 App Access Token.") |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | App rate limit (Application-only): 15 requests per 15-minute window shared among all users of your app<br><br>User rate limit (User context): 15 requests per 15-minute window per each authenticated user |

### OAuth 2.0 scopes required by this endpoint

|     |
| --- |
| `tweet.read`<br><br>`users.read`<br><br>`follows.read` |
| [Learn more about OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/twitter-api/oauth2) |

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Required | string | The user ID whose followers you would like to retrieve. |

  
  

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| `expansions`  <br> Optional | enum (`pinned_tweet_id`) | [Expansions](https://developer.twitter.com/en/docs/twitter-api/expansions) enable you to request additional data objects that relate to the originally returned users. The ID that represents the expanded data object will be included directly in the user data object, but the expanded object metadata will be returned within the `includes` response object, and will also include the ID so that you can match this data object to the original Tweet object. At this time, the only expansion available to endpoints that primarily return user objects is `expansions=pinned_tweet_id`. You will find the expanded Tweet data object living in the `includes` response object. |
| `max_results`  <br> Optional | integer | The maximum number of results to be returned per page. This can be a number between 1 and the 1000. By default, each page will return 100 results. |
| `pagination_token`  <br> Optional | string | Used to request the next page of results if all results weren't returned with the latest request, or to go back to the previous page of results. To return the next page, pass the `next_token` returned in your previous response. To go back one page, pass the `previous_token` returned in your previous response. |
| `tweet.fields`  <br> Optional | enum (`attachments`, `author_id`, `context_annotations`, `conversation_id`, `created_at`, `edit_controls`, `entities`, `geo`, `id`, `in_reply_to_user_id`, `lang`, `non_public_metrics`, `public_metrics`, `organic_metrics`, `promoted_metrics`, `possibly_sensitive`, `referenced_tweets`, `reply_settings`, `source`, `text`, `withheld`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [Tweet fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) will deliver in each returned pinned Tweet. Specify the desired fields in a comma-separated list without spaces between commas and fields. The Tweet fields will only return if the user has a pinned Tweet and if you've also included the `expansions=pinned_tweet_id` query parameter in your request. While the referenced Tweet ID will be located in the original Tweet object, you will find this ID and all additional Tweet fields in the `includes` data object. |
| `user.fields`  <br> Optional | enum (`created_at`, `description`, `entities`, `id`, `location`, `most_recent_tweet_id`, `name`, `pinned_tweet_id`, `profile_image_url`, `protected`, `public_metrics`, `url`, `username`, `verified`, `verified_type`, `withheld`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [user fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) will deliver with each returned users objects. Specify the desired fields in a comma-separated list without spaces between commas and fields. These specified user fields will display directly in the user data objects. |

  
  

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript (Default fields)](#tab0)
* [TypeScript (Optional fields)](#tab1)
* [Java (Default fields)](#tab2)
* [Java (Optional fields)](#tab3)

TypeScript (Default fields)

TypeScript (Optional fields)

Java (Default fields)

Java (Optional fields)

      `(async () => {   try {     const getUsersFollowers = await twitterClient.users.usersIdFollowers(       //The ID of the user for whom to return results       "2244994945"     );     console.dir(getUsersFollowers, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `(async () => {   try {     const getUsersFollowers = await twitterClient.users.usersIdFollowers(       //The ID of the user for whom to return results       "2244994945",       {         //A comma separated list of User fields to display         "user.fields": ["created_at"],                  //A comma separated list of Tweet fields to display.         "tweet.fields": ["created_at"],                  //A comma separated list of fields to expand         expansions: ["pinned_tweet_id"],          //The maximum number of results         max_results: 10,       }     );     console.dir(getUsersFollowers, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  // String | The ID of the user for whom to return results String id = "2244994945";  try {     GenericMultipleUsersLookupResponse result = apiInstance.users().usersIdFollowers(id, null, null, null, null, null);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling UsersApi#usersIdFollowers");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

      `// Set the params values  // String | The ID of the user for whom to return results String id = "2244994945";  // Integer | The maximum number of results to be returned. Integer maxResults = 10;  // Set<String> | A comma separated list of fields to expand. Set<String> expansions = new HashSet<>(Arrays.asList("pinned_tweet_id"));  // Set<String> | A comma separated list of Tweet fields to display. Set<String> tweetFields = new HashSet<>(Arrays.asList("created_at"));   // Set<String> | A comma separated list of User fields to display. Set<String> userFields = new HashSet<>(Arrays.asList("created_at"));  try {     GenericMultipleUsersLookupResponse result = apiInstance.users().usersIdFollowers(id, maxResults, null, userFields, expansions, tweetFields);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling UsersApi#usersIdFollowers");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

### Example responses

* [Default fields](#tab0)
* [Optional fields](#tab1)

Default fields

Optional fields

      `{   "data": [     {       "id": "6253282",       "name": "Twitter API",       "username": "TwitterAPI"     },     {       "id": "2244994945",       "name": "Twitter Dev",       "username": "TwitterDev"     },     {       "id": "783214",       "name": "Twitter",       "username": "Twitter"     },     {       "id": "95731075",       "name": "Twitter Safety",       "username": "TwitterSafety"     },     {       "id": "3260518932",       "name": "Twitter Moments",       "username": "TwitterMoments"     },     {       "id": "373471064",       "name": "Twitter Music",       "username": "TwitterMusic"     },     {       "id": "791978718",       "name": "Twitter Official Partner",       "username": "OfficialPartner"     },     {       "id": "17874544",       "name": "Twitter Support",       "username": "TwitterSupport"     },     {       "id": "234489024",       "name": "Twitter Comms",       "username": "TwitterComms"     },     {       "id": "1526228120",       "name": "Twitter Data",       "username": "TwitterData"     }   ],   "meta": {     "result_count": 10,     "next_token": "DFEDBNRFT3MHCZZZ"   } }`
    

      `{   "data": [     {       "pinned_tweet_id": "1293595870563381249",       "id": "6253282",       "username": "TwitterAPI",       "name": "Twitter API"     },     {       "pinned_tweet_id": "1293593516040269825",       "id": "2244994945",       "username": "TwitterDev",       "name": "Twitter Dev"     },     {       "id": "783214",       "username": "Twitter",       "name": "Twitter"     },     {       "pinned_tweet_id": "1271186240323432452",       "id": "95731075",       "username": "TwitterSafety",       "name": "Twitter Safety"     },     {       "id": "3260518932",       "username": "TwitterMoments",       "name": "Twitter Moments"     },     {       "pinned_tweet_id": "1293216056274759680",       "id": "373471064",       "username": "TwitterMusic",       "name": "Twitter Music"     },     {       "id": "791978718",       "username": "OfficialPartner",       "name": "Twitter Official Partner"     },     {       "pinned_tweet_id": "1289000334497439744",       "id": "17874544",       "username": "TwitterSupport",       "name": "Twitter Support"     },     {       "pinned_tweet_id": "1283543147444711424",       "id": "234489024",       "username": "TwitterComms",       "name": "Twitter Comms"     },     {       "id": "1526228120",       "username": "TwitterData",       "name": "Twitter Data"     }   ],   "includes": {     "tweets": [       {         "context_annotations": [           {             "domain": {               "id": "46",               "name": "Brand Category",               "description": "Categories within Brand Verticals that narrow down the scope of Brands"             },             "entity": {               "id": "781974596752842752",               "name": "Services"             }           },           {             "domain": {               "id": "47",               "name": "Brand",               "description": "Brands and Companies"             },             "entity": {               "id": "10045225402",               "name": "Twitter"             }           },           {             "domain": {               "id": "65",               "name": "Interests and Hobbies Vertical",               "description": "Top level interests and hobbies groupings, like Food or Travel"             },             "entity": {               "id": "848920371311001600",               "name": "Technology",               "description": "Technology and computing"             }           },           {             "domain": {               "id": "66",               "name": "Interests and Hobbies Category",               "description": "A grouping of interests and hobbies entities, like Novelty Food or Destinations"             },             "entity": {               "id": "848921413196984320",               "name": "Computer programming",               "description": "Computer programming"             }           },           {             "domain": {               "id": "47",               "name": "Brand",               "description": "Brands and Companies"             },             "entity": {               "id": "10045225402",               "name": "Twitter"             }           }         ],         "id": "1293595870563381249",         "text": "Twitter API v2: Early Access releasednnToday we announced Early Access to the first endpoints of the new Twitter API!nn#TwitterAPI #EarlyAccess #VersionBump https://t.co/g7v3aeIbtQ"       },       {         "context_annotations": [           {             "domain": {               "id": "46",               "name": "Brand Category",               "description": "Categories within Brand Verticals that narrow down the scope of Brands"             },             "entity": {               "id": "781974596752842752",               "name": "Services"             }           },           {             "domain": {               "id": "47",               "name": "Brand",               "description": "Brands and Companies"             },             "entity": {               "id": "10045225402",               "name": "Twitter"             }           },           {             "domain": {               "id": "65",               "name": "Interests and Hobbies Vertical",               "description": "Top level interests and hobbies groupings, like Food or Travel"             },             "entity": {               "id": "848920371311001600",               "name": "Technology",               "description": "Technology and computing"             }           },           {             "domain": {               "id": "66",               "name": "Interests and Hobbies Category",               "description": "A grouping of interests and hobbies entities, like Novelty Food or Destinations"             },             "entity": {               "id": "848921413196984320",               "name": "Computer programming",               "description": "Computer programming"             }           }         ],         "id": "1293593516040269825",         "text": "It’s finally here! 🥁 Say hello to the new #TwitterAPI.nnWe’re rebuilding the Twitter API v2 from the ground up to better serve our developer community. And today’s launch is only the beginning.nnhttps://t.co/32VrwpGaJw https://t.co/KaFSbjWUA8"       },       {         "id": "1271186240323432452",         "text": "We’re disclosing new state-linked information operations to our public archive — the only one of its kind in the industry. Originating from the People’s Republic of China (PRC), Russia, and Turkey, all associated accounts and content have been removed. https://t.co/obRqr96iYm"       },       {         "id": "1293216056274759680",         "text": "say howdy to your new yeehaw king @orvillepeck—our #ArtistToFollow this month 🤠 https://t.co/3pk9fYcPHb"       },       {         "context_annotations": [           {             "domain": {               "id": "46",               "name": "Brand Category",               "description": "Categories within Brand Verticals that narrow down the scope of Brands"             },             "entity": {               "id": "781974596752842752",               "name": "Services"             }           },           {             "domain": {               "id": "47",               "name": "Brand",               "description": "Brands and Companies"             },             "entity": {               "id": "10045225402",               "name": "Twitter"             }           }         ],         "id": "1289000334497439744",         "text": "We’ve significantly limited access to our internal tools and systems. Until we can safely resume normal operations, our response times to some support needs and reports will be slower. Thank you for your patience as we work through this."       },       {         "context_annotations": [           {             "domain": {               "id": "46",               "name": "Brand Category",               "description": "Categories within Brand Verticals that narrow down the scope of Brands"             },             "entity": {               "id": "781974596752842752",               "name": "Services"             }           },           {             "domain": {               "id": "47",               "name": "Brand",               "description": "Brands and Companies"             },             "entity": {               "id": "10045225402",               "name": "Twitter"             }           }         ],         "id": "1283543147444711424",         "text": "Follow @TwitterSupport for the latest on the security incident ⬇️ https://t.co/7FKKksJqxV"       }     ],     "meta": {       "result_count": 10,       "next_token": "DFEDBNRFT3MHCZZZ"     }   } }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Default | string | Unique identifier of this user. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. |
| `name`  <br> Default | string | The friendly name of this user, as shown on their profile. |
| `username`  <br> Default | string | The Twitter handle (screen name) of this user. |
| `created_at` | date (ISO 8601) | Creation time of this account.  <br>  <br>To return this field, add `user.fields=created_at` in the request's query parameter. |
| `most_recent_tweet_id` | string | The ID of the User's most recent Tweet  <br>  <br>To return this field, add `user.fields=most_recent_tweet_id` in the request's query parameter. |
| `protected` | boolean | Indicates if this user has chosen to protect their Tweets (in other words, if this user's Tweets are private).  <br>  <br>To return this field, add `user.fields=protected` in the request's query parameter. |
| `withheld` | object | Contains withholding details for [withheld content](https://help.twitter.com/en/rules-and-policies/tweet-withheld-by-country).  <br>  <br>To return this field, add `user.fields=withheld` in the request's query parameter. |
| `withheld.country_codes` | array | Provides a list of countries where this user is not available.  <br>  <br>To return this field, add `user.fields=withheld.country_codes` in the request's query parameter. |
| `withheld.scope` | enum (`tweet`, `user`) | Indicates whether the content being withheld is a Tweet or a user (this API will return `user`).  <br>  <br>To return this field, add `user.fields=withheld.scope` in the request's query parameter. |
| `location` | string | The location specified in the user's profile, if the user provided one. As this is a freeform value, it may not indicate a valid location, but it may be fuzzily evaluated when performing searches with location queries.  <br>  <br>To return this field, add `user.fields=location` in the request's query parameter. |
| `url` | string | The URL specified in the user's profile, if present.  <br>  <br>To return this field, add `user.fields=url` in the request's query parameter. |
| `description` | string | The text of this user's profile description (also known as bio), if the user provided one.  <br>  <br>To return this field, add `user.fields=description` in the request's query parameter. |
| `verified` | boolean | Indicate if this user is a verified Twitter user.  <br>  <br>To return this field, add `user.fields=verified` in the request's query parameter. |
| `verified_type` | enum (`blue`, `business`, `government`, `none`) | Indicates the type of verification for the Twitter account.  <br>  <br>To return this field, add `user.fields=verified_type` in the request's query parameter. |
| `entities` | object | This object and its children fields contain details about text that has a special meaning in the user's description.  <br>  <br>To return this field, add `user.fields=entities` in the request's query parameter. |
| `entities.url` | array | Contains details about the user's profile website. |
| `entities.url.urls` | array | Contains details about the user's profile website. |
| `entities.url.urls.start` | integer | The start position (zero-based) of the recognized user's profile website. All start indices are inclusive. |
| `entities.url.urls.end` | integer | The end position (zero-based) of the recognized user's profile website. This end index is exclusive. |
| `entities.url.urls.url` | string | The URL in the format entered by the user. |
| `entities.url.urls.expanded_url` | string | The fully resolved URL. |
| `entities.url.urls.display_url` | string | The URL as displayed in the user's profile. |
| `entities.description` | array | Contains details about URLs, Hashtags, Cashtags, or mentions located within a user's description. |
| `entities.description.urls` | array | Contains details about any URLs included in the user's description. |
| `entities.description.urls.start` | integer | The start position (zero-based) of the recognized URL in the user's description. All start indices are inclusive. |
| `entities.description.urls.end` | integer | The end position (zero-based) of the recognized URL in the user's description. This end index is exclusive. |
| `entities.description.urls.url` | string | The URL in the format entered by the user. |
| `entities.description.urls.expanded_url` | string | The fully resolved URL. |
| `entities.description.urls.display_url` | string | The URL as displayed in the user's description. |
| `entities.description.hashtags` | array | Contains details about text recognized as a Hashtag. |
| `entities.description.hashtags.start` | integer | The start position (zero-based) of the recognized Hashtag within the Tweet. All start indices are inclusive. |
| `entities.description.hashtags.end` | integer | The end position (zero-based) of the recognized Hashtag within the Tweet. This end index is exclusive. |
| `entities.description.hashtags.hashtag` | string | The text of the Hashtag. |
| `entities.description.mentions` | array | Contains details about text recognized as a user mention. |
| `entities.description.mentions.start` | integer | The start position (zero-based) of the recognized user mention within the Tweet. All start indices are inclusive. |
| `entities.description.mentions.end` | integer | The end position (zero-based) of the recognized user mention within the Tweet. This end index is exclusive. |
| `entities.description.mentions.username` | string | The part of text recognized as a user mention. |
| `entities.description.cashtags` | array | Contains details about text recognized as a Cashtag. |
| `entities.description.cashtags.start` | integer | The start position (zero-based) of the recognized Cashtag within the Tweet. All start indices are inclusive. |
| `entities.description.cashtags.end` | integer | The end position (zero-based) of the recognized Cashtag within the Tweet. This end index is exclusive. |
| `entities.description.cashtags.cashtag` | string | The text of the Cashtag. |
| `profile_image_url` | string | The URL to the profile image for this user, as shown on the user's profile. |
| `public_metrics` | object | Contains details about activity for this user. |
| `public_metrics.followers_count` | integer | Number of users who follow this user. |
| `public_metrics.following_count` | integer | Number of users this user is following. |
| `public_metrics.tweet_count` | integer | Number of Tweets (including Retweets) posted by this user. |
| `public_metrics.listed_count` | integer | Number of lists that include this user. |
| `pinned_tweet_id` | string | Unique identifier of this user's pinned Tweet.  <br>  <br>You can obtain the expanded object in `includes.tweets` by adding `expansions=pinned_tweet_id` in the request's query parameter. |
| `includes.tweets` | array | When including the `expansions=pinned_tweet_id` parameter, this includes the pinned Tweets attached to the returned users' profiles in the form of [Tweet objects](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) with their default fields and any additional fields requested using the `tweet.fields` parameter, assuming there is a referenced Tweet present in the returned Tweet(s). |
| `errors` | object | Contains details about errors that affected any of the requested users. See [Status codes and error messages](https://developer.twitter.com/en/support/twitter-api/error-troubleshooting) for more details. |
| `meta`  <br> Default | object | This object contains information about the number of users returned in the current request, and pagination details. |
| `meta.result_count`  <br> Default | integer | The number of users returned in this request. Note that this number may be lower than what was specified in the `max_results` query parameter. |
| `meta.previous_token` | string | Pagination token for the previous page of results. This value is returned when there are multiple pages of results, as the current request may only return a subset of results. To go back to the previous page, passing the value from this field in the `pagination_token` query parameter. When this field is not returned in the response, it means you are on the first page of results. |
| `meta.next_token` | string | Pagination token for the next page of results. This value is returned when there are multiple pages of results, as the current request may only return a subset of results. To retrieve the full list, keep passing the value from this field in the `pagination_token` query parameter. When this field is not returned in the response, it means you've reached the last page of results, and that there are no further pages. |

GET /2/users/:id/following

GET /2/users/:id/following
==========================

Returns a list of users the specified user ID is following.

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Try a live request ❯](https://oauth-playground.glitch.me/?id=usersIdFollowing&params=%28%27query%21%28%29%7Ebody%21%28%29%7Epath%21%28%21id%21%272244994945%27%29%29_) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Fusers%2F%7Bid%7D%2Ffollowing&method=get) 

### Endpoint URL

`https://api.twitter.com/2/users/:id/following`  
  

### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 2.0 App-only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only "Use this method to obtain information in the context of an unauthenticated public user. This method is for developers that just need read-only access to public information. Click to learn how to obtain an OAuth 2.0 App Access Token.")<br><br>[OAuth 1.0a](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) is also available for this endpoint.<br><br>[OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code "This method allows an authorized app to act on behalf of the user, as the user. It is typically used to access or post public information for a specific user, and it us useful when your app needs to be aware of the relationship between a user and what this endpoint returns. Click to learn how to authenticate with OAuth 2.0 Authorization Code with PKCE.") |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | App rate limit (Application-only): 15 requests per 15-minute window shared among all users of your app<br><br>User rate limit (User context): 15 requests per 15-minute window per each authenticated user |

### OAuth 2.0 scopes required by this endpoint

|     |
| --- |
| `tweet.read`<br><br>`users.read`<br><br>`follows.read` |
| [Learn more about OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/twitter-api/oauth2) |

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Required | string | The user ID whose following you would like to retrieve. |

  
  

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| `expansions`  <br> Optional | enum (`pinned_tweet_id`) | [Expansions](https://developer.twitter.com/en/docs/twitter-api/expansions) enable you to request additional data objects that relate to the originally returned users. At this time, the only expansion available to endpoints that primarily return user objects is `expansions=pinned_tweet_id`. You will find the expanded Tweet data object living in the `includes` response object. |
| `max_results`  <br> Optional | integer | The maximum number of results to be returned per page. This can be a number between 1 and the 1000. By default, each page will return 100 results. |
| `pagination_token`  <br> Optional | string | Used to request the next page of results if all results weren't returned with the latest request, or to go back to the previous page of results. To return the next page, pass the `next_token` returned in your previous response. To go back one page, pass the `previous_token` returned in your previous response. |
| `tweet.fields`  <br> Optional | enum (`attachments`, `author_id`, `context_annotations`, `conversation_id`, `created_at`, `edit_controls`, `entities`, `geo`, `id`, `in_reply_to_user_id`, `lang`, `non_public_metrics`, `public_metrics`, `organic_metrics`, `promoted_metrics`, `possibly_sensitive`, `referenced_tweets`, `reply_settings`, `source`, `text`, `withheld`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [Tweet fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) will deliver in each returned pinned Tweet. Specify the desired fields in a comma-separated list without spaces between commas and fields. The Tweet fields will only return if the user has a pinned Tweet and if you've also included the `expansions=pinned_tweet_id` query parameter in your request. While the referenced Tweet ID will be located in the original Tweet object, you will find this ID and all additional Tweet fields in the `includes` data object. |
| `user.fields`  <br> Optional | enum (`created_at`, `description`, `entities`, `id`, `location`, `most_recent_tweet_id`, `name`, `pinned_tweet_id`, `profile_image_url`, `protected`, `public_metrics`, `url`, `username`, `verified`, `verified_type`, `withheld`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [user fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) will deliver with each returned users objects. Specify the desired fields in a comma-separated list without spaces between commas and fields. These specified user fields will display directly in the user data objects. |

  
  

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript (Default fields)](#tab0)
* [TypeScript (Optional fields)](#tab1)
* [Java (Default fields)](#tab2)
* [Java (Optional fields)](#tab3)

TypeScript (Default fields)

TypeScript (Optional fields)

Java (Default fields)

Java (Optional fields)

      `(async () => {   try {     const getUsersFollowing = await twitterClient.users.usersIdFollowing(       //The ID of the user for whom to return results       "2244994945"     );     console.dir(getUsersFollowing, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `(async () => {   try {     const getUsersFollowing = await twitterClient.users.usersIdFollowing(       //The ID of the user for whom to return results       "2244994945",       {         //A comma separated list of User fields to display         "user.fields": ["created_at"],                  //A comma separated list of Tweet fields to display.         "tweet.fields": ["created_at"],                  //A comma separated list of fields to expand         expansions: ["pinned_tweet_id"],          //The maximum number of results         max_results: 10,       }     );     console.dir(getUsersFollowing, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  // String | The ID of the user for whom to return results String id = "2244994945";  try {     UsersFollowingLookupResponse result = apiInstance.users().usersIdFollowing(id, null, null, null, null, null);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling UsersApi#usersIdFollowing");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

      `// Set the params values  // String | The ID of the user for whom to return results String id = "2244994945";  // Integer | The maximum number of results to be returned. Integer maxResults = 10;  // Set<String> | A comma separated list of fields to expand. Set<String> expansions = new HashSet<>(Arrays.asList("pinned_tweet_id"));  // Set<String> | A comma separated list of Tweet fields to display. Set<String> tweetFields = new HashSet<>(Arrays.asList("created_at"));   // Set<String> | A comma separated list of User fields to display. Set<String> userFields = new HashSet<>(Arrays.asList("created_at"));  try {     UsersFollowingLookupResponse result = apiInstance.users().usersIdFollowing(id, maxResults, null, userFields, expansions, tweetFields);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling UsersApi#usersIdFollowing");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

### Example responses

* [Default fields](#tab0)
* [Optional fields](#tab1)

Default fields

Optional fields

      `{   "data": [     {       "id": "6253282",       "name": "Twitter API",       "username": "TwitterAPI"     },     {       "id": "2244994945",       "name": "Twitter Dev",       "username": "TwitterDev"     },     {       "id": "783214",       "name": "Twitter",       "username": "Twitter"     },     {       "id": "95731075",       "name": "Twitter Safety",       "username": "TwitterSafety"     },     {       "id": "3260518932",       "name": "Twitter Moments",       "username": "TwitterMoments"     },     {       "id": "373471064",       "name": "Twitter Music",       "username": "TwitterMusic"     },     {       "id": "791978718",       "name": "Twitter Official Partner",       "username": "OfficialPartner"     },     {       "id": "17874544",       "name": "Twitter Support",       "username": "TwitterSupport"     },     {       "id": "234489024",       "name": "Twitter Comms",       "username": "TwitterComms"     },     {       "id": "1526228120",       "name": "Twitter Data",       "username": "TwitterData"     }   ],   "meta": {     "result_count": 10,     "next_token": "DFEDBNRFT3MHCZZZ"   } }`
    

      `{   "data": [     {       "pinned_tweet_id": "1293595870563381249",       "id": "6253282",       "username": "TwitterAPI",       "name": "Twitter API"     },     {       "pinned_tweet_id": "1293593516040269825",       "id": "2244994945",       "username": "TwitterDev",       "name": "Twitter Dev"     },     {       "id": "783214",       "username": "Twitter",       "name": "Twitter"     },     {       "pinned_tweet_id": "1271186240323432452",       "id": "95731075",       "username": "TwitterSafety",       "name": "Twitter Safety"     },     {       "id": "3260518932",       "username": "TwitterMoments",       "name": "Twitter Moments"     },     {       "pinned_tweet_id": "1293216056274759680",       "id": "373471064",       "username": "TwitterMusic",       "name": "Twitter Music"     },     {       "id": "791978718",       "username": "OfficialPartner",       "name": "Twitter Official Partner"     },     {       "pinned_tweet_id": "1289000334497439744",       "id": "17874544",       "username": "TwitterSupport",       "name": "Twitter Support"     },     {       "pinned_tweet_id": "1283543147444711424",       "id": "234489024",       "username": "TwitterComms",       "name": "Twitter Comms"     },     {       "id": "1526228120",       "username": "TwitterData",       "name": "Twitter Data"     }   ],   "includes": {     "tweets": [       {         "context_annotations": [           {             "domain": {               "id": "46",               "name": "Brand Category",               "description": "Categories within Brand Verticals that narrow down the scope of Brands"             },             "entity": {               "id": "781974596752842752",               "name": "Services"             }           },           {             "domain": {               "id": "47",               "name": "Brand",               "description": "Brands and Companies"             },             "entity": {               "id": "10045225402",               "name": "Twitter"             }           },           {             "domain": {               "id": "65",               "name": "Interests and Hobbies Vertical",               "description": "Top level interests and hobbies groupings, like Food or Travel"             },             "entity": {               "id": "848920371311001600",               "name": "Technology",               "description": "Technology and computing"             }           },           {             "domain": {               "id": "66",               "name": "Interests and Hobbies Category",               "description": "A grouping of interests and hobbies entities, like Novelty Food or Destinations"             },             "entity": {               "id": "848921413196984320",               "name": "Computer programming",               "description": "Computer programming"             }           },           {             "domain": {               "id": "47",               "name": "Brand",               "description": "Brands and Companies"             },             "entity": {               "id": "10045225402",               "name": "Twitter"             }           }         ],         "id": "1293595870563381249",         "text": "Twitter API v2: Early Access releasednnToday we announced Early Access to the first endpoints of the new Twitter API!nn#TwitterAPI #EarlyAccess #VersionBump https://t.co/g7v3aeIbtQ"       },       {         "context_annotations": [           {             "domain": {               "id": "46",               "name": "Brand Category",               "description": "Categories within Brand Verticals that narrow down the scope of Brands"             },             "entity": {               "id": "781974596752842752",               "name": "Services"             }           },           {             "domain": {               "id": "47",               "name": "Brand",               "description": "Brands and Companies"             },             "entity": {               "id": "10045225402",               "name": "Twitter"             }           },           {             "domain": {               "id": "65",               "name": "Interests and Hobbies Vertical",               "description": "Top level interests and hobbies groupings, like Food or Travel"             },             "entity": {               "id": "848920371311001600",               "name": "Technology",               "description": "Technology and computing"             }           },           {             "domain": {               "id": "66",               "name": "Interests and Hobbies Category",               "description": "A grouping of interests and hobbies entities, like Novelty Food or Destinations"             },             "entity": {               "id": "848921413196984320",               "name": "Computer programming",               "description": "Computer programming"             }           }         ],         "id": "1293593516040269825",         "text": "It’s finally here! 🥁 Say hello to the new #TwitterAPI.nnWe’re rebuilding the Twitter API v2 from the ground up to better serve our developer community. And today’s launch is only the beginning.nnhttps://t.co/32VrwpGaJw https://t.co/KaFSbjWUA8"       },       {         "id": "1271186240323432452",         "text": "We’re disclosing new state-linked information operations to our public archive — the only one of its kind in the industry. Originating from the People’s Republic of China (PRC), Russia, and Turkey, all associated accounts and content have been removed. https://t.co/obRqr96iYm"       },       {         "id": "1293216056274759680",         "text": "say howdy to your new yeehaw king @orvillepeck—our #ArtistToFollow this month 🤠 https://t.co/3pk9fYcPHb"       },       {         "context_annotations": [           {             "domain": {               "id": "46",               "name": "Brand Category",               "description": "Categories within Brand Verticals that narrow down the scope of Brands"             },             "entity": {               "id": "781974596752842752",               "name": "Services"             }           },           {             "domain": {               "id": "47",               "name": "Brand",               "description": "Brands and Companies"             },             "entity": {               "id": "10045225402",               "name": "Twitter"             }           }         ],         "id": "1289000334497439744",         "text": "We’ve significantly limited access to our internal tools and systems. Until we can safely resume normal operations, our response times to some support needs and reports will be slower. Thank you for your patience as we work through this."       },       {         "context_annotations": [           {             "domain": {               "id": "46",               "name": "Brand Category",               "description": "Categories within Brand Verticals that narrow down the scope of Brands"             },             "entity": {               "id": "781974596752842752",               "name": "Services"             }           },           {             "domain": {               "id": "47",               "name": "Brand",               "description": "Brands and Companies"             },             "entity": {               "id": "10045225402",               "name": "Twitter"             }           }         ],         "id": "1283543147444711424",         "text": "Follow @TwitterSupport for the latest on the security incident ⬇️ https://t.co/7FKKksJqxV"       }     ],     "meta": {       "result_count": 10,       "next_token": "DFEDBNRFT3MHCZZZ"     }   } }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Default | string | Unique identifier of this user. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. |
| `name`  <br> Default | string | The friendly name of this user, as shown on their profile. |
| `username`  <br> Default | string | The Twitter handle (screen name) of this user. |
| `created_at` | date (ISO 8601) | Creation time of this account.  <br>  <br>To return this field, add `user.fields=created_at` in the request's query parameter. |
| `most_recent_tweet_id` | string | The ID of the User's most recent Tweet  <br>  <br>To return this field, add `user.fields=most_recent_tweet_id` in the request's query parameter. |
| `protected` | boolean | Indicates if this user has chosen to protect their Tweets (in other words, if this user's Tweets are private).  <br>  <br>To return this field, add `user.fields=protected` in the request's query parameter. |
| `withheld` | object | Contains withholding details for [withheld content](https://help.twitter.com/en/rules-and-policies/tweet-withheld-by-country).  <br>  <br>To return this field, add `user.fields=withheld` in the request's query parameter. |
| `withheld.country_codes` | array | Provides a list of countries where this user is not available.  <br>  <br>To return this field, add `user.fields=withheld.country_codes` in the request's query parameter. |
| `withheld.scope` | enum (`tweet`, `user`) | Indicates whether the content being withheld is a Tweet or a user (this API will return `user`).  <br>  <br>To return this field, add `user.fields=withheld.scope` in the request's query parameter. |
| `location` | string | The location specified in the user's profile, if the user provided one. As this is a freeform value, it may not indicate a valid location, but it may be fuzzily evaluated when performing searches with location queries.  <br>  <br>To return this field, add `user.fields=location` in the request's query parameter. |
| `url` | string | The URL specified in the user's profile, if present.  <br>  <br>To return this field, add `user.fields=url` in the request's query parameter. |
| `description` | string | The text of this user's profile description (also known as bio), if the user provided one.  <br>  <br>To return this field, add `user.fields=description` in the request's query parameter. |
| `verified` | boolean | Indicate if this user is a verified Twitter user.  <br>  <br>To return this field, add `user.fields=verified` in the request's query parameter. |
| `verified_type` | enum (`blue`, `business`, `government`, `none`) | Indicates the type of verification for the Twitter account.  <br>  <br>To return this field, add `user.fields=verified_type` in the request's query parameter. |
| `entities` | object | This object and its children fields contain details about text that has a special meaning in the user's description.  <br>  <br>To return this field, add `user.fields=entities` in the request's query parameter. |
| `entities.url` | array | Contains details about the user's profile website. |
| `entities.url.urls` | array | Contains details about the user's profile website. |
| `entities.url.urls.start` | integer | The start position (zero-based) of the recognized user's profile website. All start indices are inclusive. |
| `entities.url.urls.end` | integer | The end position (zero-based) of the recognized user's profile website. This end index is exclusive. |
| `entities.url.urls.url` | string | The URL in the format entered by the user. |
| `entities.url.urls.expanded_url` | string | The fully resolved URL. |
| `entities.url.urls.display_url` | string | The URL as displayed in the user's profile. |
| `entities.description` | array | Contains details about URLs, Hashtags, Cashtags, or mentions located within a user's description. |
| `entities.description.urls` | array | Contains details about any URLs included in the user's description. |
| `entities.description.urls.start` | integer | The start position (zero-based) of the recognized URL in the user's description. All start indices are inclusive. |
| `entities.description.urls.end` | integer | The end position (zero-based) of the recognized URL in the user's description. This end index is exclusive. |
| `entities.description.urls.url` | string | The URL in the format entered by the user. |
| `entities.description.urls.expanded_url` | string | The fully resolved URL. |
| `entities.description.urls.display_url` | string | The URL as displayed in the user's description. |
| `entities.description.hashtags` | array | Contains details about text recognized as a Hashtag. |
| `entities.description.hashtags.start` | integer | The start position (zero-based) of the recognized Hashtag within the Tweet. All start indices are inclusive. |
| `entities.description.hashtags.end` | integer | The end position (zero-based) of the recognized Hashtag within the Tweet. This end index is exclusive. |
| `entities.description.hashtags.hashtag` | string | The text of the Hashtag. |
| `entities.description.mentions` | array | Contains details about text recognized as a user mention. |
| `entities.description.mentions.start` | integer | The start position (zero-based) of the recognized user mention within the Tweet. All start indices are inclusive. |
| `entities.description.mentions.end` | integer | The end position (zero-based) of the recognized user mention within the Tweet. This end index is exclusive. |
| `entities.description.mentions.username` | string | The part of text recognized as a user mention. |
| `entities.description.cashtags` | array | Contains details about text recognized as a Cashtag. |
| `entities.description.cashtags.start` | integer | The start position (zero-based) of the recognized Cashtag within the Tweet. All start indices are inclusive. |
| `entities.description.cashtags.end` | integer | The end position (zero-based) of the recognized Cashtag within the Tweet. This end index is exclusive. |
| `entities.description.cashtags.cashtag` | string | The text of the Cashtag. |
| `profile_image_url` | string | The URL to the profile image for this user, as shown on the user's profile. |
| `public_metrics` | object | Contains details about activity for this user. |
| `public_metrics.followers_count` | integer | Number of users who follow this user. |
| `public_metrics.following_count` | integer | Number of users this user is following. |
| `public_metrics.tweet_count` | integer | Number of Tweets (including Retweets) posted by this user. |
| `public_metrics.listed_count` | integer | Number of lists that include this user. |
| `pinned_tweet_id` | string | Unique identifier of this user's pinned Tweet.  <br>  <br>You can obtain the expanded object in `includes.tweets` by adding `expansions=pinned_tweet_id` in the request's query parameter. |
| `includes.tweets` | array | When including the `expansions=pinned_tweet_id` parameter, this includes the pinned Tweets attached to the returned users' profiles in the form of [Tweet objects](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) with their default fields and any additional fields requested using the `tweet.fields` parameter, assuming there is a referenced Tweet present in the returned Tweet(s). |
| `errors` | object | Contains details about errors that affected any of the requested users. See [Status codes and error messages](https://developer.twitter.com/en/support/twitter-api/error-troubleshooting) for more details. |
| `meta`  <br> Default | object | This object contains information about the number of users returned in the current request, and pagination details. |
| `meta.result_count`  <br> Default | integer | The number of users returned in this request. Note that this number may be lower than what was specified in the `max_results` query parameter. |
| `meta.previous_token` | string | Pagination token for the previous page of results. This value is returned when there are multiple pages of results, as the current request may only return a subset of results. To go back to the previous page, passing the value from this field in the `pagination_token` query parameter. When this field is not returned in the response, it means you are on the first page of results. |
| `meta.next_token` | string | Pagination token for the next page of results. This value is returned when there are multiple pages of results, as the current request may only return a subset of results. To retrieve the full list, keep passing the value from this field in the `pagination_token` query parameter. When this field is not returned in the response, it means you've reached the last page of results, and that there are no further pages. |

Introduction

Introduction
------------

Using blocks lookup, you can see who you or an authenticated user has blocked. This can be useful for determining how you can interact with a given account. 

### Blocks lookup

The blocks lookup GET endpoint allows you to see which accounts you’ve blocked on behalf of an authorized user. This endpoint has a rate limit of 15 requests per 15 minutes per user. 

Since you are making requests for private information with blocks lookup, and on behalf of a user with manage blocks, you must authenticate these endpoints with either [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) or [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code), and use the user Access Tokens associated with a user that has authorized your App, which can be generated using the [3-legged OAuth flow](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens) (OAuth 1.0a) or the [Authorization Code with PKCE grant flow](https://developer.twitter.com/en/docs/authentication/oauth-2-0/user-access-token) (OAuth 2.0).

**Account setup**

To access these endpoints, you will need:

* An approved [developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info).
* To authenticate using the keys and tokens from a [developer App](https://developer.twitter.com/en/docs/apps) that is located within a [Project](https://developer.twitter.com/en/docs/projects). 

Learn more about getting access to the Twitter API v2 endpoints in our [getting started guide](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api).

[Quick start](https://developer.twitter.com/en/docs/twitter-api/users/blocks/quick-start)

[Sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code)

[Run in Postman](https://t.co/twitter-api-postman)

[Try with API Explorer](https://developer.twitter.com/apitools/api?endpoint=/2/users/%7Bid%7D/blocking&method=get)

Supporting resources
--------------------

[Learn how to use Postman to make requests](https://developer.twitter.com/en/docs/tutorials/postman-getting-started "Learn how to use Postman to make requests")

[Troubleshoot an error](https://developer.twitter.com/en/support/twitter-api "Troubleshoot an error")

[Visit the API reference page for this endpoint](https://developer.twitter.com/en/docs/twitter-api/users/blocks/api-reference "Visit the API reference page for this endpoint")

Blocks lookup quick start

Getting started with the blocks lookup endpoint
-----------------------------------------------

This quick start guide will help you make your first request to the blocks lookup endpoint using [Postman](https://developer.twitter.com/en/docs/tools-and-libraries/using-postman).

If you would like to see sample code in different languages, please visit our [Twitter API v2 sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code) GitHub repository.  

### Prerequisites

To complete this guide, you will need to have a set of [keys and tokens](https://developer.twitter.com/en/docs/authentication) to authenticate your request. You can generate these keys and tokens by following these steps:

* [Sign up for a developer account](https://developer.twitter.com/en/apply-for-access) and receive approval.
* Create a [Project](https://developer.twitter.com/en/docs/projects) and an associated [developer App](https://developer.twitter.com/en/docs/apps) in the developer portal.
* Navigate to your App's “Keys and tokens” page to generate the required credentials. Make sure to save all credentials in a secure location.

### Steps to build a blocks lookup request

#### Step one: Start with a tool or library

There are several different tools, code examples, and libraries that you can use to make a request to this endpoint, but we will use the Postman tool here to simplify the process.

To load the Twitter API v2 Postman collection into your environment, please click on the following button:

[Add Twitter API v2 to Postman](https://t.co/twitter-api-postman)

Once you have the Twitter API v2 collection loaded in Postman, navigate to the “Blocks” folder, and select “Blocks Lookup”.  
 

#### Step two: Authenticate your request

To properly make a request to the Twitter API, you need to verify that you have permission. To do so with this endpoint, you must authenticate your request using either [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) or [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code).

In this example, we are going to use OAuth 1.0a User Context.

You must add your keys and tokens – specifically your API Key, API Secret Key, OAuth 1.0a user Access Token, and OAuth 1.0a user Access Token Secret – to Postman. You can do this by selecting the environment named “Twitter API v2” in the top-right corner of Postman and adding your keys and tokens to the "initial value" and "current value" fields (by clicking the eye icon next to the environment dropdown).

These variables will automatically be pulled into the request's authorization tab if you've done this correctly.  
 

#### Step three: Specify a user

With this endpoint, you must specify your user ID or the user ID of an authenticated user to see who you have blocked.

In Postman, navigate to the "Params" tab and enter this username into the "Value" column of the id path variable (at the bottom of the section), making sure to not include any spaces before or after usernames.  
 

|     |     |
| --- | --- |
| **Key** | **Value** |
| `id` | (your user ID) |
| max\_results | 5   |

#### Step four: Identify and specify which fields you would like to retrieve

If you click the "Send" button after step three, you will receive the default [user object](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) fields in your response: id, name, and username.

If you would like to receive additional fields beyond id, name, and username, you will have to specify those fields in your request with the [fields](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/data-dictionary/introduction/fields) and/or [expansions](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/introduction/expansions) parameters.

For this exercise, we will request three additional sets of fields from different objects:

1. The additional user.created\_at field in the primary user objects.
2. The associated pinned Tweets’ object’s default fields for the returned users: id and text.
3. The additional  tweet.created\_at field in the associated Tweet objects.

In Postman, navigate to the "Params" tab and add the following key:value pair to the "Query Params" table:

|     |     |     |
| --- | --- | --- |
| **Key** | **Value** | **Returned fields** |
| user.fields | created\_at | user.created\_at |
| expansions | pinned\_tweet\_id | tweet.id, tweet.text |
| tweet.fields | created\_at | includes.tweets.created\_at |

You should now see a similar URL with your own user ID instead of TwitterDev’s URL next to the "Send" button:

      `https://api.twitter.com/2/users/2244994945/blocking?user.fields=created_at&expansions=pinned_tweet_id&tweet.fields=created_at`
    

#### Step five: Make your request and review your response

Once you have everything set up, hit the "Send" button and you will receive a similar response to the following example response:

      `{   "data": [     {       "created_at": "2008-12-04T18:51:57.000Z",       "id": "17874544",       "username": "TwitterSupport",       "name": "Twitter Support"     },     {       "created_at": "2007-02-20T14:35:54.000Z",       "id": "783214",       "username": "Twitter",       "name": "Twitter"     },     {       "pinned_tweet_id": "1389270063807598594",       "created_at": "2018-11-21T14:24:58.000Z",       "id": "1065249714214457345",       "username": "TwitterSpaces",       "name": "Spaces"     },     {       "pinned_tweet_id": "1293595870563381249",       "created_at": "2007-05-23T06:01:13.000Z",       "id": "6253282",       "username": "TwitterAPI",       "name": "Twitter API"     }   ],   "includes": {     "tweets": [       {         "created_at": "2021-05-03T17:26:09.000Z",         "id": "1389270063807598594",         "text": "now, everyone with 600 or more followers can host a Space.\n\nbased on what we've learned, these accounts are likely to have a good experience hosting because of their existing audience. before bringing the ability to create a Space to everyone, we’re focused on a few things. 🧵"       },       {         "created_at": "2020-08-12T17:11:04.000Z",         "id": "1293595870563381249",         "text": "Twitter API v2: Early Access released\n\nToday we announced Early Access to the first endpoints of the new Twitter API!\n\n#TwitterAPI #EarlyAccess #VersionBump https://t.co/g7v3aeIbtQ"       }     ]   }`
    

####   
Step six: Paginate through your results

You may notice that there is a meta object located at the bottom of the response. If you received a next\_token, this signals that there is another page of results that we can retrieve. To pull the next page of results, you will pull the value of the next\_token field and add it to the request as the value to an additional pagination\_token parameter.  
 

|     |     |
| --- | --- |
| **Key** | **Value** |
| pagination\_token | 1D3PU6DRII9HEZZZ |

If you send the request after adding this additional parameter, the next five results will be delivered with the subsequent payload since we specified max\_results as 5 in step three. You can continue to repeat this process until all results have been returned, but you can also use the max\_results parameter to request up to 1000 users per request, so you don’t have to paginate through results quite as much.

Next steps
----------

[Customize your request using the API Reference](https://developer.twitter.com/en/docs/twitter-api/users/blocks/api-reference "Customize your request using the API Reference")

[Reach out to the community for help](https://twittercommunity.com/ "Reach out to the community for help")

Integrate

Integration guide
-----------------

This page contains information on several tools and key concepts that you should be aware of as you integrate the blocks endpoints into your system. We’ve broken the page into a couple of different sections:

* [Helpful tools](#helpful)
* Key Concepts
* [Authentication](#authentication)
* [Developer portal, Projects, and Apps](#portal)
* [Rate limits](#limits)
* [Fields and expansions](#fields)
* [Pagination](#pagination)

### Helpful tools

Before we dive into some key concepts that will help you integrate this endpoint, we recommend that you become familiar with:

#### Postman

Postman is a great tool that you can use to test out an endpoint. Each Postman request includes every path and body parameter to help you quickly understand what is available to you. To learn more about our Postman collections, please visit our ["Using Postman"](https://developer.twitter.com/en/docs/tools-and-libraries/using-postman) page. 

#### Code samples

Interested in getting set up with this endpoint with some code in your preferred coding language? We’ve got a handful of different code samples available that you can use as a starting point on our [Github page](https://github.com/twitterdev/Twitter-API-v2-sample-code).

#### Third-party libraries

Take advantage of one of our communities’ [third-party libraries](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries) to help you get started. You can find a library that works with the v2 endpoints by looking for the proper version tag.

### Key concepts

#### Authentication

All Twitter API v2 endpoints require you to authenticate your requests with a set of credentials, also known as keys and tokens. You can use either OAuth 1.0a User Context or OAuth 2.0 Authorization Code with PKCE to authenticate your requests to these endpoints. 

[OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) requires you to utilize your API Keys, user Access Tokens, and a handful of other parameters to [create an authorization header](https://developer-staging.twitter.com/en/docs/authentication/oauth-1-0a/authorizing-a-request), which you will then pass with your request. The Access Tokens must be associated with the user that you are making the request on behalf of. If you would like to generate a set of Access Tokens for another user, they must authorize your App using the [3-legged OAuth flow](https://developer-staging.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens). 

Please note that OAuth 1.0a can be difficult to use. If you are not familiar with this authentication method, we recommend that you use a [library](https://developer.twitter.com/content/en/docs/twitter-api/tools-and-libraries), use a tool like Postman, or use OAuth 2.0 to authenticate your requests.

[OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code) allows for greater control over an application’s scope, and authorization flows across multiple devices. OAuth 2.0 allows you to pick specific fine-grained scopes which give you specific permissions on behalf of a user. 

To enable OAuth 2.0 in your App, you must enable it in your’s App’s authentication settings found in the App settings section of the developer portal.

#### Developer portal, Projects, and developer Apps

To retrieve a set of authentication credentials that will work with the Twitter API v2 endpoints, you must [sign up for a developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info), set up a [Project](https://developer.twitter.com/en/docs/projects) within that account, and created a [developer App](https://developer.twitter.com/en/docs/apps) within that Project. You can then find your keys and tokens within your developer App.  
 

#### Rate limits

Every day, many thousands of developers make requests to the Twitter API. To help manage the sheer volume of these requests, [rate limits](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/rate-limits) are placed on each endpoint that limits the number of requests that you can make on behalf of your app or on behalf of an authenticated user. 

These endpoints are rate limited at the user level, meaning that the authenticated user that you are making the request on behalf of can only call the endpoint a certain number of times across any developer App. There is a user rate limit of 50 requests per 15 minutes per endpoint with both POST and DELETE methods. However, with the GET method, the rate limit is only 15 requests per 15 minutes.  
 

#### Fields and expansions

The Twitter API v2 GET endpoints allow users to select exactly which data they want to return from the API using a set of tools called fields and expansions. The expansions parameter allows you to expand objects referenced in the payload. For example, this endpoint allows you to pull the following [expansions](https://developer.twitter.com/en/docs/twitter-api/expansions):

* pinned\_tweet\_id

  
The **fields** parameter allows you to select exactly which [fields](https://developer.twitter.com/en/docs/twitter-api/fields) within the different data objects you would like to receive. These endpoints delivers Tweet objects primarily. By default, the Tweet object returns the **id** and **text** fields. To receive additional fields such as **tweet.created\_at** or **tweet.entities**, you will have to specifically request those using a **fields** parameter. Some important fields that you may want to consider using in your integration are our poll data, metrics, Tweet annotations, and conversation ID fields.

We’ve added a guide on how to [use fields and expansions](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/using-fields-and-expansions) together to our [Twitter API v2 data dictionary](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/introduction).

#### Pagination

Blocks lookup can return a lot of data. To ensure we don’t return to many results at any given time, we use pagination. Learn more about how to [paginate through results.](https://developer.twitter.com/en/docs/twitter-api/users/blocks/content/developer-twitter/en/docs/twitter-api/pagination)

Next steps
----------

[Visit the API reference page for these endpoint](https://developer.twitter.com/en/docs/twitter-api/users/blocks/api-reference "Visit the API reference page for these endpoint")

Migrate

Other migration resources
-------------------------

[Blocks lookup: Standard v1.1 to Twitter API v2](https://developer.twitter.com/en/docs/twitter-api/users/blocks/migrate/blocks-lookup-standard-to-twitter-api-v2 "Blocks lookup: Standard v1.1 to Twitter API v2")

[Twitter API migration hub](https://developer.twitter.com/en/docs/twitter-api/migrate "Twitter API migration hub")

Blocks lookup: Standard v1.1 compared to Twitter API v2

Blocks lookup: Standard v1.1 compared to Twitter API v2
-------------------------------------------------------

If you have been working with the standard v1.1 [GET blocks/ids](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/mute-block-report-users/api-reference/get-blocks-ids) and [GET blocks/list](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/v1/accounts-and-users/mute-block-report-users/api-reference/get-blocks-list) endpoints, the goal of this guide is to help you understand the similarities and differences between the standard v1.1 and Twitter API v2 blocks lookup endpoints.

* **Similarities**
    * Authentication
* **Differences**
    * Endpoint URLs  
        
    * Users per request limits
    * App and Project requirements
    * Response data formats
    * Request parameters

### Similarities

#### **Authentication**

Both the standard v1.1 and Twitter API v2 blocks lookup endpoints use [OAuth 1.0a User Context](https://developer.twitter.com/content/developer-twitter/en/docs/authentication/oauth-1-0a). Therefore, if you were previously using one of the standard v1.1 blocks lookup endpoints, you can continue using the same authentication method if you migrate to the Twitter API v2 version. 

### Differences

#### Endpoint URLs

* Standard v1.1 endpoints:
    * GET https://api.twitter.com/1.1/blocks/ids.json  
        (list of user IDs who are blocked by the specified user)
    * GET https://api.twitter.com/1.1/blocks/lists.json  
        (list of users who are blocked by the specified user)
* Twitter API v2 endpoint:
    * GET https://api.twitter.com/2/users/:id/blocking  
        (list of users who are blocked by the specified user ID)  
         

#### Users per request limits

The standard v1.1 endpoints allow you to return up to 5000 users per request. The new v2 endpoints allow you to return up to 1000 users per request. To return a full 1000 users, you will need to pass max\_results=1000 as a query parameter; you can then pass the next\_token returned in the response payload to the pagination\_token query parameter in your next request.  
 

#### App and Project requirements

The Twitter API v2 endpoints require that you use credentials from a [developer App](https://developer.twitter.com/content/developer-twitter/en/docs/apps) that is associated with a [Project](https://developer.twitter.com/content/developer-twitter/en/docs/projects) when authenticating your requests. All Twitter API v1.1 endpoints can use credentials from standalone Apps or Apps associated with a project.  
  

#### Response data format

One of the biggest differences between standard v1.1 and Twitter API v2 endpoint versions is how you select which fields return in your payload.

For the standard endpoints, you receive many of the response fields by default, and then have the option to use parameters to identify which fields or sets of fields should return in the payload.

The Twitter API v2 version only delivers the user id , name, and username fields by default. To request any additional fields or objects, you wil need to use the [fields](https://developer.twitter.com/en/docs/twitter-api/fields/content/developer-twitter/en/docs/twitter-api/fields) and [expansions](https://developer.twitter.com/en/docs/twitter-api/fields/content/developer-twitter/en/docs/twitter-api/expansions) parameters. Any user fields that you request from this endpoint will return in the primary user object. Any expanded Tweet object and fields will return in an includes object within your response. You can then match any expanded objects back to the user object by matching the IDs located in both the user and the expanded Tweet object. 

We encourage you to read more about these new parameters in their respective guides, or by reading our guide on [how to use fields and expansions](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/using-fields-and-expansions). 

We have also put together a [data format migration guide](https://developer.twitter.com/en/docs/twitter-api/migrate/data-formats/standard-v1-1-to-v2) which can help you map standard v1.1 fields to the newer v2 fields. This guide will also provide you the specific expansion and field parameter that you will need to pass with your v2 request to return specific fields.   
 

In addition to the changes in how you request certain fields, Twitter API v2 is also introducing new JSON designs for the objects returned by the APIs, including [Tweet](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) and [user](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) objects.

* At the JSON root level, the standard endpoints return Tweet objects in a statuses array, while Twitter API v2 returns a data array. 
* Instead of referring to Retweeted and Quoted "statuses", Twitter API v2 JSON refers to Retweeted and Quoted Tweets. Many legacy and deprecated fields, such as contributors and user.translator\_type are being removed. 
* Instead of using both favorites (in Tweet object) and favourites (in user object), Twitter API v2 uses the term like. 
* Twitter is adopting the convention that JSON values with no value (for example, null) are not written to the payload. Tweet and user attributes are only included if they have a non-null values.   
     

We also introduced a new set of fields to the [Tweet object](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) including the following:

* A [conversation\_id](https://developer.twitter.com/en/docs/twitter-api/conversation-id) field
* Two new [annotations](https://developer.twitter.com/en/docs/twitter-api/annotations) fields, including context and entities
* Several new [metrics](https://developer.twitter.com/en/docs/twitter-api/metrics) fields 
* A new reply\_setting field, which shows you who can reply to a given Tweet

#### Request parameters

The following standard v1.1 request parameters accepted two request query parameters (user\_id or screen\_name). The Twitter API v2 only accepts the numerical user ID, and it must be passed as part of the endpoint path.

Next steps
----------

[Review the blocks lookup API references](https://developer.twitter.com/en/docs/twitter-api/users/blocks/api-reference "Review the blocks lookup API references")

API reference

API reference index
-------------------

For the complete API reference, select an endpoint from the list.  
 

### Blocks lookup

|     |     |
| --- | --- |
| **Returns a list of users who are blocked by the specified user ID** | `[GET /2/users/:id/blocking](https://developer.twitter.com/en/docs/twitter-api/users/blocks/api-reference/get-users-blocking)` |

GET /2/users/:id/blocking

GET /2/users/:id/blocking
=========================

Returns a list of users who are blocked by the specified user ID.

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Try a live request ❯](https://oauth-playground.glitch.me/?id=usersIdBlocking&params=%28%27query%21%28%29%7Ebody%21%27%27%7Epath%21%28%29%29_) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Fusers%2F%7Bid%7D%2Fblocking&method=get) 

### Endpoint URL

`https://api.twitter.com/2/users/:id/blocking`  
  

### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 1.0a](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) is also available for this endpoint.<br><br>[OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code "This method allows an authorized app to act on behalf of the user, as the user. It is typically used to access or post public information for a specific user, and it us useful when your app needs to be aware of the relationship between a user and what this endpoint returns. Click to learn how to authenticate with OAuth 2.0 Authorization Code with PKCE.") |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | User rate limit (User context): 15 requests per 15-minute window per each authenticated user |

### OAuth 2.0 scopes required by this endpoint

|     |
| --- |
| `tweet.read`<br><br>`users.read`<br><br>`block.read` |
| [Learn more about OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/twitter-api/oauth2) |

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Required | string | The user ID whose blocked users you would like to retrieve. The user’s ID must correspond to the user ID of the authenticating user, meaning that you must pass the [Access Tokens](https://developer.twitter.com/en/docs/authentication/oauth-2-0/user-access-token) associated with the user ID when authenticating your request. |

  
  

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| `expansions`  <br> Optional | enum (`pinned_tweet_id`) | [Expansions](https://developer.twitter.com/en/docs/twitter-api/expansions) enable you to request additional data objects that relate to the originally returned users. The ID that represents the expanded data object will be included directly in the user data object, but the expanded object metadata will be returned within the `includes` response object, and will also include the ID so that you can match this data object to the original Tweet object. At this time, the only expansion available to endpoints that primarily return user objects is `expansions=pinned_tweet_id`. You will find the expanded Tweet data object living in the `includes` response object. |
| `max_results`  <br> Optional | integer | The maximum number of results to be returned per page. This can be a number between 1 and 1000. By default, each page will return 100 results. |
| `pagination_token`  <br> Optional | string | Used to request the next page of results if all results weren't returned with the latest request, or to go back to the previous page of results. |
| `tweet.fields`  <br> Optional | enum (`attachments`, `author_id`, `context_annotations`, `conversation_id`, `created_at`, `edit_controls`, `entities`, `geo`, `id`, `in_reply_to_user_id`, `lang`, `non_public_metrics`, `public_metrics`, `organic_metrics`, `promoted_metrics`, `possibly_sensitive`, `referenced_tweets`, `reply_settings`, `source`, `text`, `withheld`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [Tweet fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) will deliver in each returned pinned Tweet. Specify the desired fields in a comma-separated list without spaces between commas and fields. The Tweet fields will only return if the user has a pinned Tweet and if you've also included the `expansions=pinned_tweet_id` query parameter in your request. While the referenced Tweet ID will be located in the original Tweet object, you will find this ID and all additional Tweet fields in the `includes` data object. |
| `user.fields`  <br> Optional | enum (`created_at`, `description`, `entities`, `id`, `location`, `most_recent_tweet_id`, `name`, `pinned_tweet_id`, `profile_image_url`, `protected`, `public_metrics`, `url`, `username`, `verified`, `verified_type`, `withheld`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [user fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) will deliver with each returned users objects. Specify the desired fields in a comma-separated list without spaces between commas and fields. These specified user fields will display directly in the user data objects. |

  
  

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript (Default fields)](#tab0)
* [TypeScript (Optional fields)](#tab1)
* [Java (Default fields)](#tab2)
* [Java (Optional fields)](#tab3)

TypeScript (Default fields)

TypeScript (Optional fields)

Java (Default fields)

Java (Optional fields)

      `(async () => {   try {     const getBlockedUsers = await twitterClient.users.usersIdBlocking(       //The ID of the user for whom to return results       "2244994945"     );     console.dir(getBlockedUsers, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `(async () => {   try {     const getBlockedUsers = await twitterClient.users.usersIdBlocking(       //The ID of the user for whom to return results       "2244994945",       {         //A comma separated list of User fields to display         "user.fields": ["created_at"],                  //A comma separated list of Tweet fields to display.         "tweet.fields": ["created_at"],                  //A comma separated list of fields to expand         expansions: ["pinned_tweet_id"],          //The maximum number of results         max_results: 10,       }     );     console.dir(getBlockedUsers, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  // String | The ID of the user for whom to return results String id = "2244994945";   try {     GenericMultipleUsersLookupResponse result = apiInstance.users().usersIdBlocking(id, null, null, null, null, null);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling UsersApi#usersIdBlocking");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

      `// Set the params values  // String | The ID of the user for whom to return results String id = "2244994945";  // Integer | The maximum number of results to be returned. Integer maxResults = 10;  // Set<String> | A comma separated list of fields to expand. Set<String> expansions = new HashSet<>(Arrays.asList("pinned_tweet_id"));  // Set<String> | A comma separated list of Tweet fields to display. Set<String> tweetFields = new HashSet<>(Arrays.asList("created_at"));   // Set<String> | A comma separated list of User fields to display. Set<String> userFields = new HashSet<>(Arrays.asList("created_at"));  try {     GenericMultipleUsersLookupResponse result = apiInstance.users().usersIdBlocking(id, maxResults, null, userFields, expansions, tweetFields);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling UsersApi#usersIdBlocking");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

### Example responses

* [Default fields](#tab0)
* [Optional fields](#tab1)

Default fields

Optional fields

      `{   "data": [     {       "id": "1065249714214457345",       "name": "Spaces",       "username": "TwitterSpaces"     },     {       "id": "783214",       "name": "Twitter",       "username": "Twitter"     },     {       "id": "1526228120",       "name": "Twitter Data",       "username": "TwitterData"     },     {       "id": "2244994945",       "name": "Twitter Dev",       "username": "TwitterDev"     },     {       "id": "6253282",       "name": "Twitter API",       "username": "TwitterAPI"     }   ] }`
    

      `{   "data": [     {       "id": "1065249714214457345",       "created_at": "2018-11-21T14:24:58.000Z",       "name": "Spaces",       "pinned_tweet_id": "1389270063807598594",       "description": "Twitter Spaces is where live audio conversations happen.",       "username": "TwitterSpaces"     },     {       "id": "783214",       "created_at": "2007-02-20T14:35:54.000Z",       "name": "Twitter",       "description": "What's happening?!",       "username": "Twitter"     },     {       "id": "1526228120",       "created_at": "2013-06-17T23:57:45.000Z",       "name": "Twitter Data",       "description": "Data-driven insights about notable moments and conversations from Twitter, Inc., plus tips and tricks to help you get the most out of Twitter data.",       "username": "TwitterData"     },     {       "id": "2244994945",       "created_at": "2013-12-14T04:35:55.000Z",       "name": "Twitter Dev",       "pinned_tweet_id": "1354143047324299264",       "description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",       "username": "TwitterDev"     },     {       "id": "6253282",       "created_at": "2007-05-23T06:01:13.000Z",       "name": "Twitter API",       "pinned_tweet_id": "1293595870563381249",       "description": "Tweets about changes and service issues. Follow @TwitterDev for more.",       "username": "TwitterAPI"     }   ],   "includes": {     "tweets": [       {         "id": "1389270063807598594",         "text": "now, everyone with 600 or more followers can host a Space.nnbased on what we've learned, these accounts are likely to have a good experience hosting because of their existing audience. before bringing the ability to create a Space to everyone, we’re focused on a few things. 🧵"       },       {         "id": "1354143047324299264",         "text": "Academics are one of the biggest groups using the #TwitterAPI to research what’s happening. Their work helps make the world (&amp; Twitter) a better place, and now more than ever, we must enable more of it. nIntroducing 🥁 the Academic Research product track!nhttps://t.co/nOFiGewAV2"       },       {         "id": "1293595870563381249",         "text": "Twitter API v2: Early Access releasednnToday we announced Early Access to the first endpoints of the new Twitter API!nn#TwitterAPI #EarlyAccess #VersionBump https://t.co/g7v3aeIbtQ"       }     ]   } }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Default | string | Unique identifier of this user. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. |
| `name`  <br> Default | string | The friendly name of this user, as shown on their profile. |
| `username`  <br> Default | string | The Twitter handle (screen name) of this user. |
| `created_at` | date (ISO 8601) | Creation time of this account.  <br>  <br>To return this field, add `user.fields=created_at` in the request's query parameter. |
| `most_recent_tweet_id` | string | The ID of the User's most recent Tweet  <br>  <br>To return this field, add `user.fields=most_recent_tweet_id` in the request's query parameter. |
| `protected` | boolean | Indicates if this user has chosen to protect their Tweets (in other words, if this user's Tweets are private).  <br>  <br>To return this field, add `user.fields=protected` in the request's query parameter. |
| `withheld` | object | Contains withholding details for [withheld content](https://help.twitter.com/en/rules-and-policies/tweet-withheld-by-country).  <br>  <br>To return this field, add `user.fields=withheld` in the request's query parameter. |
| `withheld.country_codes` | array | Provides a list of countries where this user is not available.  <br>  <br>To return this field, add `user.fields=withheld.country_codes` in the request's query parameter. |
| `withheld.scope` | enum (`tweet`, `user`) | Indicates whether the content being withheld is a Tweet or a user (this API will return `user`).  <br>  <br>To return this field, add `user.fields=withheld.scope` in the request's query parameter. |
| `location` | string | The location specified in the user's profile, if the user provided one. As this is a freeform value, it may not indicate a valid location, but it may be fuzzily evaluated when performing searches with location queries.  <br>  <br>To return this field, add `user.fields=location` in the request's query parameter. |
| `url` | string | The URL specified in the user's profile, if present.  <br>  <br>To return this field, add `user.fields=url` in the request's query parameter. |
| `description` | string | The text of this user's profile description (also known as bio), if the user provided one.  <br>  <br>To return this field, add `user.fields=description` in the request's query parameter. |
| `verified` | boolean | Indicate if this user is a verified Twitter user.  <br>  <br>To return this field, add `user.fields=verified` in the request's query parameter. |
| `verified_type` | enum (`blue`, `business`, `government`, `none`) | Indicates the type of verification for the Twitter account.  <br>  <br>To return this field, add `user.fields=verified_type` in the request's query parameter. |
| `entities` | object | This object and its children fields contain details about text that has a special meaning in the user's description.  <br>  <br>To return this field, add `user.fields=entities` in the request's query parameter. |
| `entities.url` | array | Contains details about the user's profile website. |
| `entities.url.urls` | array | Contains details about the user's profile website. |
| `entities.url.urls.start` | integer | The start position (zero-based) of the recognized user's profile website. All start indices are inclusive. |
| `entities.url.urls.end` | integer | The end position (zero-based) of the recognized user's profile website. This end index is exclusive. |
| `entities.url.urls.url` | string | The URL in the format entered by the user. |
| `entities.url.urls.expanded_url` | string | The fully resolved URL. |
| `entities.url.urls.display_url` | string | The URL as displayed in the user's profile. |
| `entities.description` | array | Contains details about URLs, Hashtags, Cashtags, or mentions located within a user's description. |
| `entities.description.urls` | array | Contains details about any URLs included in the user's description. |
| `entities.description.urls.start` | integer | The start position (zero-based) of the recognized URL in the user's description. All start indices are inclusive. |
| `entities.description.urls.end` | integer | The end position (zero-based) of the recognized URL in the user's description. This end index is exclusive. |
| `entities.description.urls.url` | string | The URL in the format entered by the user. |
| `entities.description.urls.expanded_url` | string | The fully resolved URL. |
| `entities.description.urls.display_url` | string | The URL as displayed in the user's description. |
| `entities.description.hashtags` | array | Contains details about text recognized as a Hashtag. |
| `entities.description.hashtags.start` | integer | The start position (zero-based) of the recognized Hashtag within the Tweet. All start indices are inclusive. |
| `entities.description.hashtags.end` | integer | The end position (zero-based) of the recognized Hashtag within the Tweet. This end index is exclusive. |
| `entities.description.hashtags.hashtag` | string | The text of the Hashtag. |
| `entities.description.mentions` | array | Contains details about text recognized as a user mention. |
| `entities.description.mentions.start` | integer | The start position (zero-based) of the recognized user mention within the Tweet. All start indices are inclusive. |
| `entities.description.mentions.end` | integer | The end position (zero-based) of the recognized user mention within the Tweet. This end index is exclusive. |
| `entities.description.mentions.username` | string | The part of text recognized as a user mention. |
| `entities.description.cashtags` | array | Contains details about text recognized as a Cashtag. |
| `entities.description.cashtags.start` | integer | The start position (zero-based) of the recognized Cashtag within the Tweet. All start indices are inclusive. |
| `entities.description.cashtags.end` | integer | The end position (zero-based) of the recognized Cashtag within the Tweet. This end index is exclusive. |
| `entities.description.cashtags.cashtag` | string | The text of the Cashtag. |
| `profile_image_url` | string | The URL to the profile image for this user, as shown on the user's profile. |
| `public_metrics` | object | Contains details about activity for this user. |
| `public_metrics.followers_count` | integer | Number of users who follow this user. |
| `public_metrics.following_count` | integer | Number of users this user is following. |
| `public_metrics.tweet_count` | integer | Number of Tweets (including Retweets) posted by this user. |
| `public_metrics.listed_count` | integer | Number of lists that include this user. |
| `pinned_tweet_id` | string | Unique identifier of this user's pinned Tweet.  <br>  <br>You can obtain the expanded object in `includes.tweets` by adding `expansions=pinned_tweet_id` in the request's query parameter. |
| `includes.tweets` | array | When including the `expansions=pinned_tweet_id` parameter, this includes the pinned Tweets attached to the returned users' profiles in the form of [Tweet objects](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) with their default fields and any additional fields requested using the `tweet.fields` parameter, assuming there is a referenced Tweet present in the returned Tweet(s). |
| `errors` | object | Contains details about errors that affected any of the requested users. See [Status codes and error messages](https://developer.twitter.com/en/support/twitter-api/error-troubleshooting) for more details. |
| `meta`  <br> Default | object | This object contains information about the number of users returned in the current request, and pagination details. |
| `meta.result_count`  <br> Default | integer | The number of users returned in this request. Note that this number may be lower than what was specified in the `max_results` query parameter. |
| `meta.previous_token` | string | Pagination token for the previous page of results. This value is returned when there are multiple pages of results, as the current request may only return a subset of results. To go back to the previous page, passing the value from this field in the `pagination_token` query parameter. When this field is not returned in the response, it means you are on the first page of results. |
| `meta.next_token` | string | Pagination token for the next page of results. This value is returned when there are multiple pages of results, as the current request may only return a subset of results. To retrieve the full list, keep passing the value from this field in the `pagination_token` query parameter. When this field is not returned in the response, it means you've reached the last page of results, and that there are no further pages. |

Introduction

Introduction
------------

Muting an account allows you to remove an account's Tweets from your timeline without unfollowing or blocking that account. Muted accounts will not know that you've muted them and you can unmute them at any time. With manage mutes endpoints, developers can create safer experiences for people on Twitter. One example of how to build with manage mutes is an application that allows you to mute accounts that might Tweet about specific topics for a specified length of time. With the mutes lookup endpoint, you can see who you or an authenticated user has muted. This can be useful to determine how you interact with the muted accounts. 

Since you are making requests for private information with mute lookup, and on behalf of a user with manage mutes, you must authenticate these endpoints with either [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) or [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code), and use the user Access Tokens associated with a user that has authorized your App, which can be generated using the [3-legged OAuth flow](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens) (OAuth 1.0a) or the [Authorization Code with PKCE grant flow](https://developer.twitter.com/en/docs/authentication/oauth-2-0/user-access-token) (OAuth 2.0).

### Mutes lookup

The mutes lookup endpoint allows you to see which accounts the authenticated user has muted. This endpoint has a rate limit of 15 requests per 15 minutes per user.

### Manage mutes

The manage mute endpoints enable you to mute or unmute a specified account on behalf of an authenticated user. For these endpoints, there are two methods available: POST and DELETE. The POST method allows you to mute an account, and the DELETE method allows you to unmute an account. There is a user rate limit of 50 requests per 15 minutes for both the POST and DELETE endpoints.

**Please note:** If a user mutes from [Twitter](https://twitter.com/), there is a limit of 200 requests per 15 minutes.

**Account setup**

To access these endpoints, you will need:

* An approved [developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info).
* To authenticate using the keys and tokens from a [developer App](https://developer.twitter.com/en/docs/apps) that is located within a [Project](https://developer.twitter.com/en/docs/projects). 

Learn more about getting access to the Twitter API v2 endpoints in our [getting started guide](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api).

[Quick start](https://developer.twitter.com/en/docs/twitter-api/users/mutes/quick-start)

[Sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code)

[Run in Postman](https://t.co/twitter-api-postman)

[Try with API Explorer](https://developer.twitter.com/apitools/api?endpoint=/2/users/%7Bid%7D/muting&method=get)

Supporting resources
--------------------

[Learn how to use Postman to make requests](https://developer.twitter.com/en/docs/tutorials/postman-getting-started "Learn how to use Postman to make requests")

[Troubleshoot an error](https://developer.twitter.com/en/support/twitter-api "Troubleshoot an error")

[Visit the API reference page for this endpoint](https://developer.twitter.com/en/docs/twitter-api/users/mutes/api-reference "Visit the API reference page for this endpoint")

Mutes lookup quick start

Getting started with the mutes lookup endpoint
----------------------------------------------

This quick start guide will help you make your first request to the mutes lookup endpoint using Postman.

Please visit our [Twitter API v2 sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code) GitHub repository if you want to see sample code in different languages.

### Prerequisites

To complete this guide, you will need to have a set of [keys and tokens](https://developer.twitter.com/en/docs/authentication) to authenticate your request. You can generate these keys and tokens by following these steps:

* [Sign up for a developer account](https://developer.twitter.com/en/apply-for-access) and receive approval.
* Create a [Project](https://developer.twitter.com/en/docs/projects) and an associated [developer App](https://developer.twitter.com/en/docs/apps) in the developer portal.
* Navigate to your App's “Keys and tokens” page to generate the required credentials. Make sure to save all credentials in a secure location.

### Steps to build a mutes lookup request

#### Step one: Start with a tool or library

There are several different tools, code examples, and libraries that you can use to make a request to this endpoint, but we will use the Postman tool here to simplify the process.

To load the Twitter API v2 Postman collection into your environment, please click on the following button:

[Add Twitter API v2 to Postman](https://t.co/twitter-api-postman)

Once you have the Twitter API v2 collection loaded in Postman, navigate to the “Mutes” folder, and select “Mutes lookup”.  
 

#### Step two: Authenticate your request

To properly make a request to the Twitter API, you need to verify that you have permission. To do so with this endpoint, you must authenticate your request using either [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) or [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code).

In this example, we are going to use OAuth 1.0a User Context.

You must add your keys and tokens – specifically your API Key, API Secret Key, OAuth 1.0a user Access Token, and OAuth 1.0a user Access Token Secret – to Postman. You can do this by selecting the environment named “Twitter API v2” in the top-right corner of Postman and adding your keys and tokens to the "initial value" and "current value" fields (by clicking the eye icon next to the environment dropdown).

These variables will automatically be pulled into the request's authorization tab if you've done this correctly.  
 

#### Step three: Specify a user

With this endpoint, you must specify your user ID or the ID of an authenticated user to see who you or the authenticated user has muted.

  
In Postman, navigate to the "Params" tab and enter the authenticated user ID into the "Value" column of the id under “Path Variables” (at the bottom of the section), making sure to not include any spaces before or after ID.

Above the “Path Variables” section, you’ll notice there are optional “Query Params” to add. For this example, we will check the variable max\_results and add a value of 5.

|     |     |     |
| --- | --- | --- |
| **Key** | **Value** | **Parameter Type** |
| `id` | (your user ID) | Path |
| max\_results | 5   | Query |

#### Step four: Identify and specify which fields you would like to retrieve

If you click the "Send" button after step three, you will receive the default [user object](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) fields in your response: id, name, and username.

If you want to receive additional fields beyond id, name, and username, you will have to specify those fields in your request with the [fields](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/data-dictionary/introduction/fields) and/or [expansions](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/introduction/expansions) parameters.

For this exercise, we will request three additional sets of fields from different objects:

1. The additional user.created\_at field in the primary user objects.
2. The associated pinned Tweets’ object’s default fields for the returned users: id and text.
3. The additional  tweet.created\_at field in the associated Tweet objects.

In Postman, navigate to the "Params" tab and add the following key:value pair to the "Query Params" table:

|     |     |     |
| --- | --- | --- |
| **Key** | **Value** | **Returned fields** |
| user.fields | created\_at | user.created\_at |
| expansions | pinned\_tweet\_id | tweet.id, tweet.text |
| tweet.fields | created\_at | includes.tweets.created\_at |

You should now see a similar URL with your own user ID instead of the example ID URL next to the "Send" button:

      `https://api.twitter.com/2/users/1324848235714736129/muting?user.fields=created_at&expansions=pinned_tweet_id&tweet.fields=created_at&max_results=5`
    

#### Step five: Make your request and review your response

Once you have everything set up, hit the "Send" button, and you will receive a similar response to the following example response:

      `{   "data": [     {       "username": "TwitterDev",       "created_at": "2013-12-14T04:35:55.000Z",       "id": "2244994945",       "name": "Twitter Dev",       "pinned_tweet_id": "1430984356139470849"     }   ],   "includes": {     "tweets": [       {         "created_at": "2021-08-26T20:03:51.000Z",         "id": "1430984356139470849",         "text": "Help us build a better Twitter Developer Platform!\n \nTake the annual developer survey &gt;&gt;&gt; https://t.co/9yTbEKlJHH https://t.co/fYIwKPzqua"       }     ]   },   "meta": {     "result_count": 1   } }`
    

####   
Step six: Paginate through your results

You may notice that there is a meta object located at the bottom of the response. If you received a next\_token, this signals that there is another page of results that we can retrieve. To pull the next page of results, you will pull the value of the next\_token field and add it to the request as the value to an additional pagination\_token query parameter.  
 

|     |     |
| --- | --- |
| **Key** | **Value** |
| pagination\_token | 1710819323648428707 |

If you send the request after adding this additional parameter, the next five results will be delivered with the subsequent payload since we specified max\_results as 5 in step three. You can continue to repeat this process until all results have been returned, but you can also use the max\_results parameter to request up to 1000 users per request, so you don’t have to paginate through results quite as much.

Next steps
----------

[Customize your request using the API Reference](https://developer.twitter.com/en/docs/twitter-api/users/mutes/api-reference "Customize your request using the API Reference")

[Reach out to the community for help](https://twittercommunity.com/ "Reach out to the community for help")

Manage mutes quick start

Getting started with the manage mutes endpoints
-----------------------------------------------

This quick start guide will help you make your first request to the manage mutes endpoints using [Postman](https://developer.twitter.com/en/docs/tools-and-libraries/using-postman).

If you would like to see sample code in different languages, please visit our [Twitter API v2 sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code) GitHub repository.

### Prerequisites

To complete this guide, you will need to have a set of [keys and tokens](https://developer.twitter.com/en/docs/authentication) to authenticate your request. You can generate these keys and tokens by following these steps:

* [Sign up for a developer account](https://developer.twitter.com/en/apply-for-access) and receive approval.
* Create a [Project](https://developer.twitter.com/en/docs/projects) and an associated [developer App](https://developer.twitter.com/en/docs/apps) in the developer portal.
* Navigate to your App's “Keys and tokens” page to generate the required credentials. Make sure to save all credentials in a secure location.

### Steps to build a manage mutes request

#### Step one: Start with a tool or library

There are several different tools, code examples, and libraries that you can use to make a request to this endpoint, but we will use the Postman tool here to simplify the process.

To load the Twitter API v2 Postman collection into your environment, please click on the following button:

[Add Twitter API v2 to Postman](https://t.co/twitter-api-postman)

Once you have the Twitter API v2 collection loaded in Postman, navigate to the “Mutes” folder, and select “Mute a user’s ID”.  
 

#### Step two: Authenticate your request

To properly make a request to the Twitter API, you need to verify that you have permission. To do so with this endpoint, you must authenticate your request using either [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) or [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code).

In this example, we are going to use OAuth 1.0a User Context.

You must add your keys and tokens – specifically your API Key, API Secret Key, OAuth 1.0a user Access Token, and OAuth 1.0a user Access Token Secret – to Postman. You can do this by selecting the environment named “Twitter API v2” in the top-right corner of Postman and adding your keys and tokens to the "initial value" and "current value" fields (by clicking the eye icon next to the environment dropdown).

These variables will automatically be pulled into the request's authorization tab if you've done this correctly.  
 

#### Step three: Specify who is going to mute whom

Manage mutes endpoints require two IDs: one for the user (the user who wishes to mute or unmute another user) and the target user (the user that will be muted or unmuted). The user’s ID must correspond to the authenticating user’s ID, meaning that you must pass the Access Tokens associated with the user ID when authenticating your request. In this case, you can specify the ID belonging to your own user. You can find your ID in two ways:

1. Using the [user lookup](https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference) by username endpoint, you can pass a username and receive the id field. 
2. Looking at your Access Token, you will find that the numeric part is your user ID.  
     

The target ID can be any valid user ID. In Postman, navigate to the "Params" tab, and enter your ID into the "Value" column of the `id` path variable. Navigate to the “Body” tab and ID of the user you wish to mute as the value for the target\_user\_id parameter. Be sure not to include any spaces before or after any ID.

|     |     |
| --- | --- |
| **Key** | **Value** |
| `id` | authenticated user ID |
| target\_user\_id | the user ID you wish to mute |

#### Step four: Make your request and review your response

Once you have everything set up, hit the "Send" button, and you will receive a similar response to the following example response:

      `{ "data": { "muting": true } }`
    

If you receive a "muting": true, then the id is successfully muting the target\_user\_id

To unmute the same user you can use the request entitled “Unmute a user ID”, which is also found in the “Mutes” folder of the Twitter API v2 collection loaded in Postman. The source\_user\_id should be your user ID and target\_user\_id should be the user ID to unmute. You will not have to add this as a JSON body so you will want to make sure that you add in the requisite query params for source\_user\_id and target\_user\_id.

On a successful unmute, you will receive a similar response to the following example:

      `{ "data": { "muting": false } }`
    

Next steps
----------

[Customize your request using the API Reference](https://developer.twitter.com/en/docs/twitter-api/users/mutes/api-reference "Customize your request using the API Reference")

[Reach out to the community for help](https://twittercommunity.com/ "Reach out to the community for help")

Integrate

Integration guide
-----------------

This page contains information on several tools and key concepts that you should be aware of as you integrate the mutes endpoints into your system. We’ve broken the page into a couple of different sections:

* [Helpful tools](#helpful)
* Key Concepts
* [Authentication](#authentication)
* [Developer portal, Projects, and Apps](#portal)
* [Rate limits](#limits)
* [Fields and expansions](#fields)
* [Pagination](#pagination)

### Helpful tools

Before we dive into some key concepts that will help you integrate this endpoint, we recommend that you become familiar with:

#### Postman

Postman is a great tool that you can use to test out an endpoint. Each Postman request includes every path and body parameter to help you quickly understand what is available to you. To learn more about our Postman collections, please visit our ["Using Postman"](https://developer.twitter.com/en/docs/tools-and-libraries/using-postman) page. 

#### Code samples

Interested in getting set up with this endpoint with some code in your preferred coding language? We’ve got a handful of different code samples available that you can use as a starting point on our [Github page](https://github.com/twitterdev/Twitter-API-v2-sample-code).

#### Third-party libraries

Take advantage of one of our communities’ [third-party libraries](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries) to help you get started. You can find a library that works with the v2 endpoints by looking for the proper version tag.

### Key concepts

#### Authentication

All Twitter API v2 endpoints require you to authenticate your requests with a set of credentials, also known as keys and tokens. You can use either OAuth 1.0a User Context, or OAuth 2.0 Authorization Code with PKCE to authenticate your requests to these endpoints. 

[OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) requires you to utilize your API Keys, user Access Tokens, and a handful of other parameters to [create an authorization header](https://developer-staging.twitter.com/en/docs/authentication/oauth-1-0a/authorizing-a-request), which you will then pass with your request. The Access Tokens must be associated with the user that you are making the request on behalf of. If you would like to generate a set of Access Tokens for another user, they must authorize your App using the [3-legged OAuth flow](https://developer-staging.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens). 

Please note that OAuth 1.0a can be difficult to use. If you are not familiar with this authentication method, we recommend that you use a [library](https://developer.twitter.com/content/en/docs/twitter-api/tools-and-libraries), use a tool like Postman, or use OAuth 2.0 to authenticate your requests.

[OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code) allows for greater control over an application’s scope, and authorization flows across multiple devices. OAuth 2.0 allows you to pick specific fine-grained scopes which give you specific permissions on behalf of a user. 

To enable OAuth 2.0 in your App, you must enable it in your’s App’s authentication settings found in the App settings section of the developer portal.

#### Developer portal, Projects, and developer Apps

To retrieve a set of authentication credentials that will work with the Twitter API v2 endpoints, you must [sign up for a developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info), set up a [Project](https://developer.twitter.com/en/docs/projects) within that account, and created a [developer App](https://developer.twitter.com/en/docs/apps) within that Project. You can then find your keys and tokens within your developer App.  
 

#### Rate limits

Every day, many thousands of developers make requests to the Twitter API. To help manage the sheer volume of these requests, [rate limits](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/rate-limits) are placed on each endpoint that limits the number of requests you can make on behalf of your app or on behalf of an authenticated user. 

These endpoints are rate limited at the user level, meaning that the authenticated user that you are making the request on behalf of can only call the endpoint a certain number of times across any developer App.

There is a user rate limit of 50 requests per 15 minutes per endpoint with both POST and DELETE methods. However, with the GET method, the rate limit is only 15 requests per 15 minutes.  
 

#### Fields and expansions

The Twitter API v2 GET endpoint allows users to select exactly which data they want to return from the API using a set of tools called fields and expansions. The expansions parameter allows you to expand objects referenced in the payload. For example, this endpoint allows you to pull the following [expansions](https://developer.twitter.com/en/docs/twitter-api/expansions):

* pinned\_tweet\_id

  
The **fields** parameter allows you to select exactly which [fields](https://developer.twitter.com/en/docs/twitter-api/fields) within the different data objects you would like to receive. This endpoint delivers User objects primarily. By default, the User object returns the **id** , **name**  and **username** fields. To receive additional fields such as **user.created\_at** or **user.entities**, you will have to specifically request those using a **fields** parameter. 

We’ve added a guide on using [fields and expansions](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/using-fields-and-expansions) together to our [Twitter API v2 data dictionary](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/introduction).

#### Pagination

Mutes lookup can return a lot of data. To ensure we are returning consistent, high-performing results at any given time, we use pagination. Pagination is a feature in Twitter API v2 endpoints that return more results than can be returned in a single response. When that happens, the data is returned in a series of 'pages'. Learn more about how to [paginate through results.](https://developer.twitter.com/en/docs/twitter-api/users/mutes/content/developer-twitter/en/docs/twitter-api/pagination)

**Please note:** If a user mutes from [Twitter](https://twitter.com/), there is a limit of 200 requests per 15 minutes.

Next steps
----------

[Visit the API reference page for these endpoint](https://developer.twitter.com/en/docs/twitter-api/users/mutes/api-reference "Visit the API reference page for these endpoint")

Migrate

Comparing Twitter API’s mutes endpoints
---------------------------------------

### Mutes lookup

The v2 mutes lookup endpoint will replace the standard [v1.1 GET mutes/users/ids](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/v1/accounts-and-users/mute-block-report-users/api-reference/get-mutes-users-ids) and [GET mutes/users/list](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/v1/accounts-and-users/mute-block-report-users/api-reference/get-mutes-users-list) endpoints.

The following tables compare the standard v1.1 and Twitter API v2 mute endpoints:  
 

| Description | Standard v1.1 | Twitter API v2 |
| --- | --- | --- |
| HTTP methods supported | ******GET****** | ******GET****** |
| Host domain | ******https://api.twitter.com****** | ******https://api.twitter.com****** |
| Endpoint path | ******/1.1/mutes/users/ids.json******<br><br>/1.1/mutes/users/list.json | ******/2/users/:id/muting****** |
| [Authentication](https://developer.twitter.com/content/developer-twitter/en/docs/authentication) | OAuth 1.0a User Context | OAuth 1.0a User Context<br><br>OAuth 2.0 Authorization Code with PKCE |
| Default request [rate limits](https://developer.twitter.com/content/developer-twitter/en/docs/rate-limits) | 15 requests per 15 min (per user) | 15 requests per 15 min (per user) |
| Data formats | Standard v1.1 format | [Twitter API v2 format](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/data-dictionary) (determined by fields and expansions request parameters, not backward-compatible with v1.1 formats)<br><br>To learn more about how to migrate from the Standard v1.1 format to the Twitter API v2 format, please visit our [data formats migration guide](https://developer.twitter.com/en/docs/twitter-api/migrate/data-formats). |
| Requires use of credentials from a [developer App](https://developer.twitter.com/en/docs/apps) that is associated with a [Project](https://developer.twitter.com/en/docs/projects) |     | ✔️  |

### Manage mutes

The v2 manage mutes endpoints will replace the standard v1.1 [POST mutes/users/create](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/mute-block-report-users/api-reference/post-mutes-users-create) and [POST mutes/users/destroy](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/mute-block-report-users/api-reference/post-mutes-users-destroy) endpoints.

The following tables compare the standard v1.1 and Twitter API v2 mute endpoints:

#### Mute a user

| Description | Standard v1.1 | Twitter API v2 |
| --- | --- | --- |
| HTTP methods supported | POST | POST |
| Host domain | https://api.twitter.com | https://api.twitter.com |
| Endpoint path | /1.1/mutes/users/create.json | /2/users/:id/muting |
| [Authentication](https://developer.twitter.com/content/developer-twitter/en/docs/authentication) | OAuth 1.0a User Context | OAuth 1.0a User Context<br><br>OAuth 2.0 Authorization Code with PKCE |
| Default request [rate limits](https://developer.twitter.com/content/developer-twitter/en/docs/rate-limits) | 50 requests per 15 min | 50 requests per 15 min |
| Requires use of credentials from a [developer App](https://developer.twitter.com/en/docs/apps) that is associated with a [Project](https://developer.twitter.com/en/docs/projects) |     | ✔️  |

#### Unmute a user

The following tables compare the standard v1.1 and Twitter API v2 unmute endpoints:

| Description | Standard v1.1 | Twitter API v2 |
| --- | --- | --- |
| HTTP methods supported | POST | DELETE |
| Host domain | https://api.twitter.com | https://api.twitter.com |
| Endpoint path | /1.1/mutes/users/destroy.json | /2/users/:source\_user\_id/muting/:target\_user\_id |
| [Authentication](https://developer.twitter.com/content/developer-twitter/en/docs/authentication) | OAuth 1.0a User Context | OAuth 1.0a User Context<br><br>OAuth 2.0 Authorization Code with PKCE |
| Default request [rate limits](https://developer.twitter.com/content/developer-twitter/en/docs/rate-limits) | 50 requests per 15 min | 50 requests per 15 min |
| Requires use of credentials from a [developer App](https://developer.twitter.com/en/docs/apps) that is associated with a [Project](https://developer.twitter.com/en/docs/projects) |     | ✔️  |

Other migration resources
-------------------------

[Manage mutes: Standard v1.1 to Twitter API v2](https://developer.twitter.com/en/docs/twitter-api/users/mutes/migrate/manage-mutes--standard-v1-1-compared-to-twitter-api-v2 "Manage mutes: Standard v1.1 to Twitter API v2")

[Twitter API migration hub](https://developer.twitter.com/en/docs/twitter-api/migrate "Twitter API migration hub")

Mutes lookup: Standard v1.1 compared to Twitter API v2

Mutes lookup: Standard v1.1 compared to Twitter API v2
------------------------------------------------------

If you have been working with the standard v1.1 [GET mutes/users/ids](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/mute-block-report-users/api-reference/get-mutes-users-ids) and [GET mutes/users/list](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/v1/accounts-and-users/mute-block-report-users/api-reference/get-mutes-users-list) endpoints, the goal of this guide is to help you understand the similarities and differences between the standard v1.1 and Twitter API v2 mutes lookup endpoints.

* **Similarities**
    * Authentication
* **Differences**
    * Endpoint URLs  
        
    * Users per request limits
    * App and Project requirements
    * Response data formats
    * Request parameters

### Similarities

#### **Authentication**

Both the standard v1.1 and Twitter API v2 mutes lookup endpoints use [OAuth 1.0a User Context](https://developer.twitter.com/content/developer-twitter/en/docs/authentication/oauth-1-0a). Therefore, if you were previously using one of the standard v1.1 mutes lookup endpoints, you can continue using the same authentication method if you migrate to the Twitter API v2 version. 

### Differences

#### Endpoint URLs

* Standard v1.1 endpoints:
    * GET https://api.twitter.com/1.1/mutes/users/ids.json  
        (list of user IDs who the specified user muted)
    * GET https://api.twitter.com/1.1/mutes/users/lists.json  
        (list of users who are muted by the specified user)
* Twitter API v2 endpoint:
    * GET https://api.twitter.com/2/users/:id/muting  
        (list of users who are muted by the specified user ID)  
         

#### Users per request limits

The standard v1.1 endpoints allow you to return up to 5000 users per request. The new v2 endpoints allow you to return up to 1000 users per request. To return a full 1000 users, you will need to pass max\_results=1000 as a query parameter; you can then pass the next\_token returned in the response payload to the pagination\_token query parameter in your next request.  
 

#### App and Project requirements

The Twitter API v2 endpoints require that you use credentials from a [developer App](https://developer.twitter.com/content/developer-twitter/en/docs/apps) that is associated with a [Project](https://developer.twitter.com/content/developer-twitter/en/docs/projects) when authenticating your requests. All Twitter API v1.1 endpoints can use credentials from standalone Apps or Apps associated with a project.  
  

#### Response data format

One of the biggest differences between standard v1.1 and Twitter API v2 endpoint versions is how you select which fields return in your payload.

For the standard endpoints, you receive many of the response fields by default and then have the option to use parameters to identify which fields or sets of fields should return in the payload.

The Twitter API v2 version only delivers the user id, name, and username fields by default. To request any additional fields or objects, you will need to use the [fields](https://developer.twitter.com/en/docs/twitter-api/fields/content/developer-twitter/en/docs/twitter-api/fields) and [expansions](https://developer.twitter.com/en/docs/twitter-api/fields/content/developer-twitter/en/docs/twitter-api/expansions) parameters. Any user fields that you request from this endpoint will return in the primary user object. Any expanded Tweet object and fields will return an includes object within your response. You can then match any expanded objects back to the user object by matching the IDs located in both the user and the expanded Tweet object. 

We encourage you to read more about these new parameters in their respective guides, or by reading our guide on [how to use fields and expansions](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/using-fields-and-expansions). 

We have also put together a [data format migration guide](https://developer.twitter.com/en/docs/twitter-api/migrate/data-formats/standard-v1-1-to-v2) which can help you map standard v1.1 fields to the newer v2 fields. This guide will also provide you the specific expansion and field parameter that you will need to pass with your v2 request to return specific fields.   
 

In addition to the changes in how you request certain fields, Twitter API v2 is also introducing new JSON designs for the objects returned by the APIs, including [Tweet](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) and [user](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) objects.

* At the JSON root level, the standard endpoints return Tweet objects in a statuses array, while Twitter API v2 returns a data array. 
* Instead of referring to Retweeted and Quoted "statuses", Twitter API v2 JSON refers to Retweeted and Quoted Tweets. Many legacy and deprecated fields, such as contributors and user.translator\_type are being removed. 
* Instead of using both favorites (in Tweet object) and favourites (in user object), Twitter API v2 uses the term like. 
* Twitter is adopting the convention that JSON values with no value (for example, null) are not written to the payload. Tweet and user attributes are only included if they have a non-null values.   
     

We also introduced a new set of fields to the [Tweet object](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) including the following:

* A [conversation\_id](https://developer.twitter.com/en/docs/twitter-api/conversation-id) field
* Two new [annotations](https://developer.twitter.com/en/docs/twitter-api/annotations) fields, including context and entities
* Several new [metrics](https://developer.twitter.com/en/docs/twitter-api/metrics) fields 
* A new reply\_setting field, which shows you who can reply to a given Tweet

#### Request parameters

The following standard v1.1 request parameters have equivalents in Twitter API v2:

| **Standard** | **Twitter API v2** |
| --- | --- |
| stringify\_ids | No equivalent |
| cursor | pagination\_token |
| skip\_status | No equivalent |

There are also a set of standard v1.1 Mutes lookup request parameters **not** supported in Twitter API v2:

| Standard | Comment |
| --- | --- |
| include\_entities | This parameter is used to remove the entities node from the Tweet payload. It has been replaced with additive fields and expansions functionality. |

Next steps
----------

[Review the mutes lookup API references](https://developer.twitter.com/en/docs/twitter-api/users/mutes/api-reference "Review the mutes lookup API references")

Manage mutes: Standard v1.1 compared to Twitter API v2

Manage mutes: Standard v1.1 compared to Twitter API v2
------------------------------------------------------

If you have been working with the standard v1.1 [POST mutes/users/create](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/mute-block-report-users/api-reference/post-mutes-users-create) and [POST mutes/users/destroy](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/mute-block-report-users/api-reference/post-mutes-users-destroy) endpoints, the goal of this guide is to help you understand the similarities and differences between the standard v1.1 and Twitter API v2 manage mutes endpoints.

* **Similarities**
    * OAuth 1.0a User Context
* **Differences**
    * Endpoint URLs
    * App and Project requirements
    * HTTP methods
    * Request parameters  
         

### Similarities

#### OAuth 1.0a User Context authentication method

Both the endpoint versions support [OAuth 1.0a User Context](https://developer.twitter.com/content/developer-twitter/en/docs/authentication/oauth-1-0a). Therefore, if you were previously using one of the standard v1.1 manage mutes endpoints, you can continue using the same authentication method if you migrate to the Twitter API v2 version.

### Differences

#### Endpoint URLs

* Standard v1.1 endpoints:
    * POST https://api.twitter.com/1.1/mutes/users/create.json  
        (mute a user)
    * POST https://api.twitter.com/1.1/mutes/users/destroy.json  
        (unmute a user)
* Twitter API v2 endpoint:
    * POST https://api.twitter.com/2/users/:id/muting  
        (mute a user)
    * DELETE https://api.twitter.com/2/users/:source\_user\_id/muting/:target\_user\_id  
        (unmute a user) 

#### App and Project requirements

The Twitter API v2 endpoints require that you use credentials from a [developer App](https://developer.twitter.com/en/docs/apps) that is associated with a [Project](https://developer.twitter.com/en/docs/projects) when authenticating your requests. All Twitter API v1.1 endpoints can use credentials from standalone Apps or Apps associated with a project.  
  

#### Request parameters

The following standard v1.1 request parameters have equivalents in Twitter API v2:

| Standard v1.1 | Twitter API v2 |
| --- | --- |
| user\_id | target\_user\_id |
| screen\_name | No equivalent |

Please note that the Standard v1.1 parameters are passed as query parameters, whereas the Twitter API v2 parameters are passed as body parameters (for the POST endpoint) or path parameters (for the DELETE endpoint).

Also, an id of the user muting a target user is not required when using the standard v1.1 endpoints since the access tokens passed with [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) inferred which user was initiating the mute/unmute. 

Next steps
----------

[Review the manage mutes API references](https://developer.twitter.com/en/docs/twitter-api/users/mutes/api-reference "Review the manage mutes API references")

API reference

API reference index
-------------------

For the complete API reference, select an endpoint from the list.  
  

### Mutes lookup  

|     |     |
| --- | --- |
| **Returns a list of users who are muted by the specified user ID** | `[GET /2/users/:id/muting](https://developer.twitter.com/en/docs/twitter-api/users/mutes/api-reference/get-users-muting)` |

### Manage mutes  

|     |     |
| --- | --- |
| **Allows a user ID to mute another user** | `[POST /2/users/:id/muting](https://developer.twitter.com/en/docs/twitter-api/users/mutes/api-reference/post-users-user_id-muting)` |
| **Allows a user ID to unmute another user** | `[DELETE /2/users/:source_user_id/muting/:target_user_id](https://developer.twitter.com/en/docs/twitter-api/users/mutes/api-reference/delete-users-user_id-muting)` |

GET /2/users/:id/muting

GET /2/users/:id/muting
=======================

Returns a list of users who are muted by the specified user ID.

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Try a live request ❯](https://oauth-playground.glitch.me/?id=usersIdMuting&params=%28%27query%21%28%29%7Ebody%21%27%27%7Epath%21%28%29%29_) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Fusers%2F%7Bid%7D%2Fmuting&method=get) 

### Endpoint URL

`https://api.twitter.com/2/users/:id/muting`  
  

### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 1.0a](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) is also available for this endpoint.<br><br>[OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code "This method allows an authorized app to act on behalf of the user, as the user. It is typically used to access or post public information for a specific user, and it us useful when your app needs to be aware of the relationship between a user and what this endpoint returns. Click to learn how to authenticate with OAuth 2.0 Authorization Code with PKCE.") |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | User rate limit (User context): 15 requests per 15-minute window per each authenticated user |

### OAuth 2.0 scopes required by this endpoint

|     |
| --- |
| `tweet.read`<br><br>`users.read`<br><br>`mute.read` |
| [Learn more about OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/twitter-api/oauth2) |

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Required | string | The user ID whose muted users you would like to retrieve. The user’s ID must correspond to the user ID of the authenticating user, meaning that you must pass the [Access Tokens](https://developer.twitter.com/en/docs/authentication/oauth-2-0/user-access-token) associated with the user ID when authenticating your request. |

  
  

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| `expansions`  <br> Optional | enum (`pinned_tweet_id`) | [Expansions](https://developer.twitter.com/en/docs/twitter-api/expansions) enable you to request additional data objects that relate to the originally returned users. The ID that represents the expanded data object will be included directly in the user data object, but the expanded object metadata will be returned within the `includes` response object, and will also include the ID so that you can match this data object to the original Tweet object. At this time, the only expansion available to endpoints that primarily return user objects is `expansions=pinned_tweet_id`. You will find the expanded Tweet data object living in the `includes` response object. |
| `max_results`  <br> Optional | integer | The maximum number of results to be returned per page. This can be a number between 1 and 1000. By default, each page will return 100 results. |
| `pagination_token`  <br> Optional | string | Used to request the next page of results if all results weren't returned with the latest request, or to go back to the previous page of results. |
| `tweet.fields`  <br> Optional | enum (`attachments`, `author_id`, `context_annotations`, `conversation_id`, `created_at`, `edit_controls`, `entities`, `geo`, `id`, `in_reply_to_user_id`, `lang`, `non_public_metrics`, `public_metrics`, `organic_metrics`, `promoted_metrics`, `possibly_sensitive`, `referenced_tweets`, `reply_settings`, `source`, `text`, `withheld`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [Tweet fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) will deliver in each returned pinned Tweet. Specify the desired fields in a comma-separated list without spaces between commas and fields. The Tweet fields will only return if the user has a pinned Tweet and if you've also included the `expansions=pinned_tweet_id` query parameter in your request. While the referenced Tweet ID will be located in the original Tweet object, you will find this ID and all additional Tweet fields in the `includes` data object. |
| `user.fields`  <br> Optional | enum (`created_at`, `description`, `entities`, `id`, `location`, `most_recent_tweet_id`, `name`, `pinned_tweet_id`, `profile_image_url`, `protected`, `public_metrics`, `url`, `username`, `verified`, `verified_type`, `withheld`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [user fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) will deliver with each returned users objects. Specify the desired fields in a comma-separated list without spaces between commas and fields. These specified user fields will display directly in the user data objects. |

  
  

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript (Default fields)](#tab0)
* [TypeScript (Optional fields)](#tab1)
* [Java (Default fields)](#tab2)
* [Java (Optional fields)](#tab3)

TypeScript (Default fields)

TypeScript (Optional fields)

Java (Default fields)

Java (Optional fields)

      `(async () => {   try {     const getMutedUsers = await twitterClient.users.usersIdMuting(       //The ID of the user for whom to return results       "2244994945"     );     console.dir(getMutedUsers, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `(async () => {   try {     const getUsersMuted = await twitterClient.users.usersIdMuting(       //The ID of the user for whom to return results       "2244994945",       {         //A comma separated list of User fields to display         "user.fields": ["created_at"],                  //A comma separated list of Tweet fields to display.         "tweet.fields": ["created_at"],                  //A comma separated list of fields to expand         expansions: ["pinned_tweet_id"],          //The maximum number of results         max_results: 10,       }     );     console.dir(getUsersMuted, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  // String | The ID of the user for whom to return results String id = "2244994945";  try {     GenericMultipleUsersLookupResponse result = apiInstance.users().usersIdMuting(id, null, null, null, null, null);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling UsersApi#usersIdMuting");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

      `// Set the params values  // String | The ID of the user for whom to return results String id = "2244994945";  // Integer | The maximum number of results to be returned. Integer maxResults = 10;  // Set<String> | A comma separated list of fields to expand. Set<String> expansions = new HashSet<>(Arrays.asList("pinned_tweet_id"));  // Set<String> | A comma separated list of Tweet fields to display. Set<String> tweetFields = new HashSet<>(Arrays.asList("created_at"));   // Set<String> | A comma separated list of User fields to display. Set<String> userFields = new HashSet<>(Arrays.asList("created_at"));  try {     GenericMultipleUsersLookupResponse result = apiInstance.users().usersIdMuting(id, maxResults, null, userFields, expansions, tweetFields);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling UsersApi#usersIdMuting");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

### Example responses

* [Default fields](#tab0)
* [Optional fields](#tab1)

Default fields

Optional fields

      `{   "data": [     {       "id": "2244994945",       "name": "Twitter Dev",       "username": "TwitterDev"     }   ],   "meta": {     "result_count": 1   } }`
    

      `{   "data": [     {       "username": "TwitterDev",       "created_at": "2013-12-14T04:35:55.000Z",       "id": "2244994945",       "name": "Twitter Dev",       "pinned_tweet_id": "1430984356139470849"     }   ],   "includes": {     "tweets": [       {         "created_at": "2021-08-26T20:03:51.000Z",         "id": "1430984356139470849",         "text": "Help us build a better Twitter Developer Platform!n nTake the annual developer survey &gt;&gt;&gt; https://t.co/9yTbEKlJHH https://t.co/fYIwKPzqua"       }     ]   },   "meta": {     "result_count": 1   } }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Default | string | Unique identifier of this user. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. |
| `name`  <br> Default | string | The friendly name of this user, as shown on their profile. |
| `username`  <br> Default | string | The Twitter handle (screen name) of this user. |
| `created_at` | date (ISO 8601) | Creation time of this account.  <br>  <br>To return this field, add `user.fields=created_at` in the request's query parameter. |
| `most_recent_tweet_id` | string | The ID of the User's most recent Tweet  <br>  <br>To return this field, add `user.fields=most_recent_tweet_id` in the request's query parameter. |
| `protected` | boolean | Indicates if this user has chosen to protect their Tweets (in other words, if this user's Tweets are private).  <br>  <br>To return this field, add `user.fields=protected` in the request's query parameter. |
| `withheld` | object | Contains withholding details for [withheld content](https://help.twitter.com/en/rules-and-policies/tweet-withheld-by-country).  <br>  <br>To return this field, add `user.fields=withheld` in the request's query parameter. |
| `withheld.country_codes` | array | Provides a list of countries where this user is not available.  <br>  <br>To return this field, add `user.fields=withheld.country_codes` in the request's query parameter. |
| `withheld.scope` | enum (`tweet`, `user`) | Indicates whether the content being withheld is a Tweet or a user (this API will return `user`).  <br>  <br>To return this field, add `user.fields=withheld.scope` in the request's query parameter. |
| `location` | string | The location specified in the user's profile, if the user provided one. As this is a freeform value, it may not indicate a valid location, but it may be fuzzily evaluated when performing searches with location queries.  <br>  <br>To return this field, add `user.fields=location` in the request's query parameter. |
| `url` | string | The URL specified in the user's profile, if present.  <br>  <br>To return this field, add `user.fields=url` in the request's query parameter. |
| `description` | string | The text of this user's profile description (also known as bio), if the user provided one.  <br>  <br>To return this field, add `user.fields=description` in the request's query parameter. |
| `verified` | boolean | Indicate if this user is a verified Twitter user.  <br>  <br>To return this field, add `user.fields=verified` in the request's query parameter. |
| `verified_type` | enum (`blue`, `business`, `government`, `none`) | Indicates the type of verification for the Twitter account.  <br>  <br>To return this field, add `user.fields=verified_type` in the request's query parameter. |
| `entities` | object | This object and its children fields contain details about text that has a special meaning in the user's description.  <br>  <br>To return this field, add `user.fields=entities` in the request's query parameter. |
| `entities.url` | array | Contains details about the user's profile website. |
| `entities.url.urls` | array | Contains details about the user's profile website. |
| `entities.url.urls.start` | integer | The start position (zero-based) of the recognized user's profile website. All start indices are inclusive. |
| `entities.url.urls.end` | integer | The end position (zero-based) of the recognized user's profile website. This end index is exclusive. |
| `entities.url.urls.url` | string | The URL in the format entered by the user. |
| `entities.url.urls.expanded_url` | string | The fully resolved URL. |
| `entities.url.urls.display_url` | string | The URL as displayed in the user's profile. |
| `entities.description` | array | Contains details about URLs, Hashtags, Cashtags, or mentions located within a user's description. |
| `entities.description.urls` | array | Contains details about any URLs included in the user's description. |
| `entities.description.urls.start` | integer | The start position (zero-based) of the recognized URL in the user's description. All start indices are inclusive. |
| `entities.description.urls.end` | integer | The end position (zero-based) of the recognized URL in the user's description. This end index is exclusive. |
| `entities.description.urls.url` | string | The URL in the format entered by the user. |
| `entities.description.urls.expanded_url` | string | The fully resolved URL. |
| `entities.description.urls.display_url` | string | The URL as displayed in the user's description. |
| `entities.description.hashtags` | array | Contains details about text recognized as a Hashtag. |
| `entities.description.hashtags.start` | integer | The start position (zero-based) of the recognized Hashtag within the Tweet. All start indices are inclusive. |
| `entities.description.hashtags.end` | integer | The end position (zero-based) of the recognized Hashtag within the Tweet. This end index is exclusive. |
| `entities.description.hashtags.hashtag` | string | The text of the Hashtag. |
| `entities.description.mentions` | array | Contains details about text recognized as a user mention. |
| `entities.description.mentions.start` | integer | The start position (zero-based) of the recognized user mention within the Tweet. All start indices are inclusive. |
| `entities.description.mentions.end` | integer | The end position (zero-based) of the recognized user mention within the Tweet. This end index is exclusive. |
| `entities.description.mentions.username` | string | The part of text recognized as a user mention. |
| `entities.description.cashtags` | array | Contains details about text recognized as a Cashtag. |
| `entities.description.cashtags.start` | integer | The start position (zero-based) of the recognized Cashtag within the Tweet. All start indices are inclusive. |
| `entities.description.cashtags.end` | integer | The end position (zero-based) of the recognized Cashtag within the Tweet. This end index is exclusive. |
| `entities.description.cashtags.cashtag` | string | The text of the Cashtag. |
| `profile_image_url` | string | The URL to the profile image for this user, as shown on the user's profile. |
| `public_metrics` | object | Contains details about activity for this user. |
| `public_metrics.followers_count` | integer | Number of users who follow this user. |
| `public_metrics.following_count` | integer | Number of users this user is following. |
| `public_metrics.tweet_count` | integer | Number of Tweets (including Retweets) posted by this user. |
| `public_metrics.listed_count` | integer | Number of lists that include this user. |
| `pinned_tweet_id` | string | Unique identifier of this user's pinned Tweet.  <br>  <br>You can obtain the expanded object in `includes.tweets` by adding `expansions=pinned_tweet_id` in the request's query parameter. |
| `includes.tweets` | array | When including the `expansions=pinned_tweet_id` parameter, this includes the pinned Tweets attached to the returned users' profiles in the form of [Tweet objects](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) with their default fields and any additional fields requested using the `tweet.fields` parameter, assuming there is a referenced Tweet present in the returned Tweet(s). |
| `errors` | object | Contains details about errors that affected any of the requested users. See [Status codes and error messages](https://developer.twitter.com/en/support/twitter-api/error-troubleshooting) for more details. |
| `meta`  <br> Default | object | This object contains information about the number of users returned in the current request, and pagination details. |
| `meta.result_count`  <br> Default | integer | The number of users returned in this request. Note that this number may be lower than what was specified in the `max_results` query parameter. |
| `meta.previous_token` | string | Pagination token for the previous page of results. This value is returned when there are multiple pages of results, as the current request may only return a subset of results. To go back to the previous page, passing the value from this field in the `pagination_token` query parameter. When this field is not returned in the response, it means you are on the first page of results. |
| `meta.next_token` | string | Pagination token for the next page of results. This value is returned when there are multiple pages of results, as the current request may only return a subset of results. To retrieve the full list, keep passing the value from this field in the `pagination_token` query parameter. When this field is not returned in the response, it means you've reached the last page of results, and that there are no further pages. |

POST /2/users/:id/muting

POST /2/users/:id/muting
========================

Allows an authenticated user ID to mute the target user.

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Try a live request ❯](https://oauth-playground.glitch.me/?id=usersIdMute&params=%28%27query%21%28%29%7Ebody%21%27%27%7Epath%21%28%29%29_) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Fusers%2F%7Bid%7D%2Fmuting&method=post) 

### Endpoint URL

`https://api.twitter.com/2/users/:id/muting`  
  

### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 1.0a](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) is also available for this endpoint.<br><br>[OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code "This method allows an authorized app to act on behalf of the user, as the user. It is typically used to access or post public information for a specific user, and it us useful when your app needs to be aware of the relationship between a user and what this endpoint returns. Click to learn how to authenticate with OAuth 2.0 Authorization Code with PKCE.") |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | User rate limit (User context): 50 requests per 15-minute window per each authenticated user |

### OAuth 2.0 scopes required by this endpoint

|     |
| --- |
| `tweet.read`<br><br>`users.read`<br><br>`mute.write` |
| [Learn more about OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/twitter-api/oauth2) |

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Required | string | The user ID who you would like to initiate the mute on behalf of. It must match your own user ID or that of an authenticating user, meaning that you must pass the [Access Tokens](https://developer.twitter.com/en/docs/authentication/oauth-2-0/user-access-token) associated with the user ID when authenticating your request. |

  
  

### JSON body parameters

| Name | Type | Description |
| --- | --- | --- |
| `target_user_id`  <br> Required | string | The user ID of the user that you would like the `id` to mute. The body should contain a string of the user ID inside of a JSON object. |

  
  

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript](#tab0)
* [Java](#tab1)

TypeScript

Java

      `(async () => {   try {     const muteUser = await twitterClient.users.usersIdMute(       //The ID of the user that is requesting to mute the target user       "6253282",       {         //The ID of the user that the source user is requesting to mute         target_user_id: "2244994945",       }     );     console.dir(muteUser, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  UsersIdMuteRequest usersIdMuteRequest = new UsersIdMuteRequest();  //The ID of the user that the source user is requesting to mute usersIdMuteRequest.targetUserId("2244994945");  // String | The ID of the user that is requesting to mute the target user String id = "6253282";  try {     UsersMutingMutationResponse result = apiInstance.users().usersIdMute(usersIdMuteRequest, id);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling UsersApi#usersIdMute");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

### Example responses

* [Successful response](#tab0)

Successful response

      `{   "data": {     "muting": true   } }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `muting` | boolean | Indicates whether the user is muting the specified user as a result of this request. |

DELETE /2/users/:source\_user\_id/muting/:target\_user\_id

DELETE /2/users/:source\_user\_id/muting/:target\_user\_id
==========================================================

Allows an authenticated user ID to unmute the target user.  
  
The request succeeds with no action when the user sends a request to a user they're not muting or have already unmuted.

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Try a live request ❯](https://oauth-playground.glitch.me/?id=usersIdUnmute&params=%28%27query%21%28%29%7Ebody%21%27%27%7Epath%21%28%29%29_) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Fusers%2F%7Bsource_user_id%7D%2Fmuting%2F%7Btarget_user_id%7D&method=delete) 

### Endpoint URL

`https://api.twitter.com/2/users/:source_user_id/muting/:target_user_id`  
  

### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code "This method allows an authorized app to act on behalf of the user, as the user. It is typically used to access or post public information for a specific user, and it us useful when your app needs to be aware of the relationship between a user and what this endpoint returns. Click to learn how to authenticate with OAuth 2.0 Authorization Code with PKCE.")<br><br>[OAuth 1.0a](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) is also available for this endpoint. |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | User rate limit (User context): 50 requests per 15-minute window per each authenticated user |

### OAuth 2.0 scopes required by this endpoint

|     |
| --- |
| `tweet.read`<br><br>`users.read`<br><br>`mute.write` |
| [Learn more about OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/twitter-api/oauth2) |

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `source_user_id`  <br> Required | string | The user ID who you would like to initiate an unmute on behalf of. The user’s ID must correspond to the user ID of the authenticating user, meaning that you must pass the [Access Tokens](https://developer.twitter.com/en/docs/authentication/oauth-2-0/user-access-token) associated with the user ID when authenticating your request. |
| `target_user_id`  <br> Required | string | The user ID of the user that you would like the `source_user_id` to unmute. |

  
  

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript](#tab0)
* [Java](#tab1)

TypeScript

Java

      `(async () => {   try {     const unmuteUser = await twitterClient.users.usersIdUnmute(       //The ID of the user that is requesting to unmute the target user       "2244994945",        //The ID of the user that the source user is requesting to unmute       "6253282"     );     console.dir(unmuteUser, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  // String | The ID of the user that is requesting to unmute the target user String sourceUserId = "2244994945";  // String | The ID of the user that the source user is requesting to unmute String targetUserId = "6253282";  try {     UsersMutingMutationResponse result = apiInstance.users().usersIdUnmute(sourceUserId, targetUserId);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling UsersApi#usersIdUnmute");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

### Example responses

* [Successful response](#tab0)

Successful response

      `{   "data": {     "muting": false   } }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `muting` | boolean | Indicates whether the user is muting the specified user as a result of this request. The returned value is `false` for a successful unmute request. |

Introduction

Introduction
------------

Available to developers with Pro access and higher

The Users Search endpoint provides a simple, relevance-based search interface to public user accounts on X. Try querying by topical interest, full name, company name, location, or other criteria.  

This endpoint currently supports [User Auth](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) . By default, you get 100 Users per request and you can specify up to 1000 Users per request. It has a limit of 10,000 requests per 24 hours (in addition to the 300 requests per 15 minutes)

**Account setup**

To access these endpoints, you will need:

* An approved [developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info).
* To authenticate using the keys and tokens from a [developer App](https://developer.twitter.com/en/docs/apps) that is located within a [Project](https://developer.twitter.com/en/docs/projects). 

Learn more about getting access to the Twitter API v2 endpoints in our [getting started guide](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api).

[Quick start](https://developer.twitter.com/en/docs/twitter-api/users/search/quick-start)

[Sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code)

[Run in Postman](https://t.co/twitter-api-postman)

Supporting resources
--------------------

[Learn how to use Postman to make requests](https://developer.twitter.com/en/docs/tutorials/postman-getting-started "Learn how to use Postman to make requests")

[Troubleshoot an error](https://developer.twitter.com/en/support/twitter-api "Troubleshoot an error")

[Visit the API reference page for this endpoint](https://developer.twitter.com/en/docs/twitter-api/users/mutes/api-reference "Visit the API reference page for this endpoint")

API reference

API reference index
-------------------

|     |     |
| --- | --- |
| **Search Users** | `[GET /2/users/search](https://developer.twitter.com/en/docs/twitter-api/users/search/api-reference/get-users-search)` |

GET /2/users/search

GET /2/users/search
===================

The users endpoint returns Users that match a search query. This endpoint has a limit of 10,000 requests per 24 hours (in addition to the 300 requests per 15 minutes.

[Run in Postman ❯](https://t.co/twitter-api-postman) 

### Endpoint URL

`https://api.twitter.com/2/users/search`  
  

### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 2.0 App-only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only "Use this method to obtain information in the context of an unauthenticated public user. This method is for developers that just need read-only access to public information. Click to learn how to obtain an OAuth 2.0 App Access Token.") |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | App rate limit (Application-only): 300 requests per 15-minute window shared among all users of your app |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| `query`  <br> Required | string | One query for matching Tweets. You can learn how to build this query by reading our [build a query guide](https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query).  <br>  <br>If you have Essential or Elevated access, you can use the Basic operators when building your query and can make queries up to 512 characters long. If you have been approved for Academic Research access, you can use all available operators and can make queries up to 1,024 characters long.  <br>  <br>Learn more about our access levels on the about Twitter API page. |
| `expansions`  <br> Optional | enum (`pinned_tweet_id`) | [Expansions](https://developer.twitter.com/en/docs/twitter-api/expansions) enable you to request additional data objects that relate to the originally returned users. The ID that represents the expanded data object will be included directly in the user data object, but the expanded object metadata will be returned within the `includes` response object, and will also include the ID so that you can match this data object to the original Tweet object. At this time, the only expansion available to endpoints that primarily return user objects is `expansions=pinned_tweet_id`. You will find the expanded Tweet data object living in the `includes` response object. |
| `max_results`  <br> Optional | integer | The maximum number of search results to be returned by a request. A number between 1 and 1000. By default, a request response will return 100 results. |
| `next_token`  <br> Optional | string | This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified. |
| `tweet.fields`  <br> Optional | enum (`attachments`, `author_id`, `context_annotations`, `conversation_id`, `created_at`, `edit_controls`, `entities`, `geo`, `id`, `in_reply_to_user_id`, `lang`, `non_public_metrics`, `public_metrics`, `organic_metrics`, `promoted_metrics`, `possibly_sensitive`, `referenced_tweets`, `reply_settings`, `source`, `text`, `withheld`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [Tweet fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) will deliver in each returned pinned Tweet. Specify the desired fields in a comma-separated list without spaces between commas and fields. The Tweet fields will only return if the user has a pinned Tweet and if you've also included the `expansions=pinned_tweet_id` query parameter in your request. While the referenced Tweet ID will be located in the original Tweet object, you will find this ID and all additional Tweet fields in the `includes` data object. |
| `user.fields`  <br> Optional | enum (`created_at`, `description`, `entities`, `id`, `location`, `most_recent_tweet_id`, `name`, `pinned_tweet_id`, `profile_image_url`, `protected`, `public_metrics`, `url`, `username`, `verified`, `verified_type`, `withheld`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [user fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) will deliver with each returned users objects. Specify the desired fields in a comma-separated list without spaces between commas and fields. These specified user fields will display directly in the user data objects. |

### Example responses

* [Default Fields](#tab0)
* [Optional Fields](#tab1)

Default Fields

Optional Fields

      `{   "data": [     {       "id": "2244994945",       "name": "Developers",       "username": "XDevelopers"     },     {       "id": "857699969263964161",       "name": "Suhem Parack",       "username": "suhemparack"     },     {       "id": "2533341854",       "name": "Chris Park",       "username": "chrisparkX"     },     {       "id": "853388192",       "name": "Haim Vaturi",       "username": "haimvat"     },     {       "id": "829457852125306890",       "name": "ROBLOX Devs",       "username": "RBXdevelopers"     },     {       "id": "70915829",       "name": "Twitter Dev Japan",       "username": "TwitterDevJP"     },     {       "id": "1619352801104039936",       "name": "Rains®™☔️🧠 0xdevelopers.eth.eth",       "username": "0xdevelopersTm"     },     {       "id": "708786906058756096",       "name": "Project X Developers",       "username": "ProXDevelopers"     },     {       "id": "1315227013028904960",       "name": "XDevelopersUS",       "username": "XDevelopersUS"     },     {       "id": "3296066705",       "name": "XDevelopers",       "username": "XDevBrasil"     },     {       "id": "1234855897370910720",       "name": "ajX developers",       "username": "ajXdevelopers"     },     {       "id": "1453775246",       "name": "The X Developers",       "username": "TheXDevelopers"     },     {       "id": "1513675812486193158",       "name": "RBLXdevelopers",       "username": "XdevelopersRbl"     },     {       "id": "1375178694520627204",       "name": "XDevelopersUK",       "username": "XDevelopersUK"     },     {       "id": "1363113804842881024",       "name": "xDevelopers",       "username": "xdevelopers_st"     },     {       "id": "2885219741",       "name": "xdevelopers",       "username": "itdenps"     },     {       "id": "1684769811539087362",       "name": "X",       "username": "xdevelopers_es"     },     {       "id": "732232220803485696",       "name": "XDevelopers",       "username": "XDeveloper_"     },     {       "id": "831241935675326464",       "name": "xDevelopers",       "username": "developers_x"     },     {       "id": "1580611661169238016",       "name": "0xspark",       "username": "0xdevelopers"     },     {       "id": "2175184873",       "name": "XeXDevelopers",       "username": "XeXDevelopers"     },     {       "id": "1684141917129539585",       "name": "Izu",       "username": "XDevelopersJP"     },     {       "id": "1521381726",       "name": "SXDevelopers",       "username": "SonyXDevelopers"     }   ],   "meta": {     "next_token": "5qym3iwm0eyn796h9x2mc2ri54ub5te"   } }`
    

      `{   "data": [     {       "location": "127.0.0.1",       "name": "Developers",       "description": "The voice of the X Dev team and your official source for updates, news, and events, related to the X API.",       "username": "XDevelopers",       "id": "2244994945"     },     {       "location": "Seattle, WA",       "name": "Suhem Parack",       "description": "Partner Engineering @XDevelopers",       "username": "suhemparack",       "id": "857699969263964161"     },     {       "location": "New York, NY",       "name": "Chris Park",       "description": "𝕏 | @X @API @XDevelopers",       "username": "chrisparkX",       "id": "2533341854"     },     {       "location": "Islington, London",       "name": "Haim Vaturi",       "description": "@XDevelopers",       "username": "haimvat",       "id": "853388192"     },     {       "location": "Canada",       "name": "ROBLOX Devs",       "description": "Follow this account for a lot of cool ROBLOXdev from all kinds of different ROBLOX developers! Not an official @ROBLOX twitter account",       "username": "RBXdevelopers",       "id": "829457852125306890"     },     {       "location": "東京都港区",       "name": "Twitter Dev Japan",       "description": "This account is no longer active. Follow @XDevelopers for updates.",       "username": "TwitterDevJP",       "id": "70915829"     },     {       "name": "Rains®™☔️🧠 0xdevelopers.eth.eth",       "description": "",       "username": "0xdevelopersTm",       "id": "1619352801104039936"     },     {       "name": "Project X Developers",       "description": "",       "username": "ProXDevelopers",       "id": "708786906058756096"     },     {       "location": "Los Angeles, CA",       "name": "XDevelopersUS",       "description": "",       "username": "XDevelopersUS",       "id": "1315227013028904960"     },     {       "location": "Rio de Janeiro & São Paulo",       "name": "XDevelopers",       "description": "Contato e Suporte Via Telefone (RJ): 21 980534086 e Via Email: contato@XDevelopers.com.br",       "username": "XDevBrasil",       "id": "3296066705"     },     {       "location": "India",       "name": "ajX developers",       "description": "app developernweb designernentrepreneurnmachine learningnAI PIONEERnage just 16",       "username": "ajXdevelopers",       "id": "1234855897370910720"     },     {       "name": "The X Developers",       "description": "",       "username": "TheXDevelopers",       "id": "1453775246"     },     {       "name": "RBLXdevelopers",       "description": "",       "username": "XdevelopersRbl",       "id": "1513675812486193158"     },     {       "location": "London, England",       "name": "XDevelopersUK",       "description": "",       "username": "XDevelopersUK",       "id": "1375178694520627204"     },     {       "name": "xDevelopers",       "description": "",       "username": "xdevelopers_st",       "id": "1363113804842881024"     },     {       "name": "xdevelopers",       "description": "",       "username": "itdenps",       "id": "2885219741"     },     {       "name": "X",       "description": "",       "username": "xdevelopers_es",       "id": "1684769811539087362"     },     {       "name": "XDevelopers",       "description": "",       "username": "XDeveloper_",       "id": "732232220803485696"     },     {       "name": "xDevelopers",       "description": "",       "username": "developers_x",       "id": "831241935675326464"     },     {       "location": "United States",       "name": "0xspark",       "description": "",       "username": "0xdevelopers",       "id": "1580611661169238016"     },     {       "name": "XeXDevelopers",       "description": "",       "username": "XeXDevelopers",       "id": "2175184873"     },     {       "name": "Izu",       "description": "",       "username": "XDevelopersJP",       "id": "1684141917129539585"     },     {       "name": "SXDevelopers",       "description": "",       "username": "SonyXDevelopers",       "id": "1521381726"     }   ],   "meta": {     "next_token": "5qym3iwm0f05lqu1ezcdkohsl2i4lyq"   } }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Default | string | Unique identifier of this user. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. |
| `name`  <br> Default | string | The friendly name of this user, as shown on their profile. |
| `username`  <br> Default | string | The Twitter handle (screen name) of this user. |
| `created_at` | date (ISO 8601) | Creation time of this account.  <br>  <br>To return this field, add `user.fields=created_at` in the request's query parameter. |
| `most_recent_tweet_id` | string | The ID of the User's most recent Tweet  <br>  <br>To return this field, add `user.fields=most_recent_tweet_id` in the request's query parameter. |
| `protected` | boolean | Indicates if this user has chosen to protect their Tweets (in other words, if this user's Tweets are private).  <br>  <br>To return this field, add `user.fields=protected` in the request's query parameter. |
| `withheld` | object | Contains withholding details for [withheld content](https://help.twitter.com/en/rules-and-policies/tweet-withheld-by-country).  <br>  <br>To return this field, add `user.fields=withheld` in the request's query parameter. |
| `withheld.country_codes` | array | Provides a list of countries where this user is not available.  <br>  <br>To return this field, add `user.fields=withheld.country_codes` in the request's query parameter. |
| `withheld.scope` | enum (`tweet`, `user`) | Indicates whether the content being withheld is a Tweet or a user (this API will return `user`).  <br>  <br>To return this field, add `user.fields=withheld.scope` in the request's query parameter. |
| `location` | string | The location specified in the user's profile, if the user provided one. As this is a freeform value, it may not indicate a valid location, but it may be fuzzily evaluated when performing searches with location queries.  <br>  <br>To return this field, add `user.fields=location` in the request's query parameter. |
| `url` | string | The URL specified in the user's profile, if present.  <br>  <br>To return this field, add `user.fields=url` in the request's query parameter. |
| `description` | string | The text of this user's profile description (also known as bio), if the user provided one.  <br>  <br>To return this field, add `user.fields=description` in the request's query parameter. |
| `verified` | boolean | Indicate if this user is a verified Twitter user.  <br>  <br>To return this field, add `user.fields=verified` in the request's query parameter. |
| `verified_type` | enum (`blue`, `business`, `government`, `none`) | Indicates the type of verification for the Twitter account.  <br>  <br>To return this field, add `user.fields=verified_type` in the request's query parameter. |
| `entities` | object | This object and its children fields contain details about text that has a special meaning in the user's description.  <br>  <br>To return this field, add `user.fields=entities` in the request's query parameter. |
| `entities.url` | array | Contains details about the user's profile website. |
| `entities.url.urls` | array | Contains details about the user's profile website. |
| `entities.url.urls.start` | integer | The start position (zero-based) of the recognized user's profile website. All start indices are inclusive. |
| `entities.url.urls.end` | integer | The end position (zero-based) of the recognized user's profile website. This end index is exclusive. |
| `entities.url.urls.url` | string | The URL in the format entered by the user. |
| `entities.url.urls.expanded_url` | string | The fully resolved URL. |
| `entities.url.urls.display_url` | string | The URL as displayed in the user's profile. |
| `entities.description` | array | Contains details about URLs, Hashtags, Cashtags, or mentions located within a user's description. |
| `entities.description.urls` | array | Contains details about any URLs included in the user's description. |
| `entities.description.urls.start` | integer | The start position (zero-based) of the recognized URL in the user's description. All start indices are inclusive. |
| `entities.description.urls.end` | integer | The end position (zero-based) of the recognized URL in the user's description. This end index is exclusive. |
| `entities.description.urls.url` | string | The URL in the format entered by the user. |
| `entities.description.urls.expanded_url` | string | The fully resolved URL. |
| `entities.description.urls.display_url` | string | The URL as displayed in the user's description. |
| `entities.description.hashtags` | array | Contains details about text recognized as a Hashtag. |
| `entities.description.hashtags.start` | integer | The start position (zero-based) of the recognized Hashtag within the Tweet. All start indices are inclusive. |
| `entities.description.hashtags.end` | integer | The end position (zero-based) of the recognized Hashtag within the Tweet. This end index is exclusive. |
| `entities.description.hashtags.hashtag` | string | The text of the Hashtag. |
| `entities.description.mentions` | array | Contains details about text recognized as a user mention. |
| `entities.description.mentions.start` | integer | The start position (zero-based) of the recognized user mention within the Tweet. All start indices are inclusive. |
| `entities.description.mentions.end` | integer | The end position (zero-based) of the recognized user mention within the Tweet. This end index is exclusive. |
| `entities.description.mentions.username` | string | The part of text recognized as a user mention. |
| `entities.description.cashtags` | array | Contains details about text recognized as a Cashtag. |
| `entities.description.cashtags.start` | integer | The start position (zero-based) of the recognized Cashtag within the Tweet. All start indices are inclusive. |
| `entities.description.cashtags.end` | integer | The end position (zero-based) of the recognized Cashtag within the Tweet. This end index is exclusive. |
| `entities.description.cashtags.cashtag` | string | The text of the Cashtag. |
| `profile_image_url` | string | The URL to the profile image for this user, as shown on the user's profile. |
| `public_metrics` | object | Contains details about activity for this user. |
| `public_metrics.followers_count` | integer | Number of users who follow this user. |
| `public_metrics.following_count` | integer | Number of users this user is following. |
| `public_metrics.tweet_count` | integer | Number of Tweets (including Retweets) posted by this user. |
| `public_metrics.listed_count` | integer | Number of lists that include this user. |
| `pinned_tweet_id` | string | Unique identifier of this user's pinned Tweet.  <br>  <br>You can obtain the expanded object in `includes.tweets` by adding `expansions=pinned_tweet_id` in the request's query parameter. |
| `includes.tweets` | array | When including the `expansions=pinned_tweet_id` parameter, this includes the pinned Tweets attached to the returned users' profiles in the form of [Tweet objects](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) with their default fields and any additional fields requested using the `tweet.fields` parameter, assuming there is a referenced Tweet present in the returned Tweet(s). |
| `errors` | object | Contains details about errors that affected any of the requested users. See [Status codes and error messages](https://developer.twitter.com/en/support/twitter-api/error-troubleshooting) for more details. |

Quick start

Getting started with the users search endpoint
----------------------------------------------

This quick start guide will help you make your first request to the users search endpoints using [Postman](https://developer.twitter.com/en/docs/tools-and-libraries/using-postman).

If you would like to see sample code in different languages, please visit our [Twitter API v2 sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code) GitHub repository.   

**Note**: This endpoint is available only to developers with Pro access. Sign up for Pro access [here](https://developer.twitter.com/en/portal/products/pro).

### Prerequisites

For you to be able to complete this guide, you will have need to have a set of [keys and tokens](https://developer.twitter.com/en/docs/authentication), which you can generate by following these steps:

1. [Sign up for a developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info).
2. Create a [Project](https://developer.twitter.com/en/docs/projects) and an associated [developer App](https://developer.twitter.com/en/docs/apps) in the developer portal.  
    
3. Navigate to your app's “Keys and tokens” page, and save your credentials in a secure location.  
    

### Steps to build a users lookup request

#### Step one: Start with a tool or library

There are several different tools, code examples, and libraries that you can use to make a request to this endpoint, but we are going to use the Postman tool here to simplify the process.

To load the Twitter API v2 Postman collection into your environment, please click on the following button:

[Add Twitter API v2 to Postman](https://t.co/twitter-api-postman)

Once you have the Twitter API v2 collection loaded in Postman, navigate to the GET /users/search.  
 

#### Step two: Authenticate your request

To properly make a request to the Twitter API, you need to verify that you have permission to do so. To do this with the GET /users/by endpoint, you must pass your developer App's Bearer Token along with your request.

First, from within the GET /users/by request in Postman, navigate to the “Authentication” tab. In the "Type" dropdown, select "Bearer Token", and then copy and paste your App only Bearer Token from your password manager into the "Token" field.  
 

#### Step three: Identify and specify the query for which you want to get the Users for

You must specify the query for which you want to get the Users for. In this example, we will get Users for the search term xdevelopers

In Postman, navigate to the "Params" tab and enter your query i.e. xdevelopers into the "Value" column of the query parameter

|     |     |
| --- | --- |
| **Key** | **Value** |
| `username` | xdevelopers |

#### Step four: Identify and specify which fields you would like to retrieve

If you click the "Send" button after step three, you will receive the default [user object](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) fields in your response: id, name, and username.

If you would like to receive additional fields beyond id, name, and username, you will have to specify those fields in your request with the [field](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/data-dictionary/introduction/fields) and/or [expansion](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/introduction/expansions) parameters.

For this exercise, we will request a three additional sets of fields from different objects:

1. The additional user.created\_at field in the primary user objects.
2. The associated pinned Tweets’ object’s default fields for the returned users: id and text.
3. The additional  tweet.created\_at field in the associated Tweet objects.  
     

In Postman, navigate to the "Params" tab and add the following key:value pair to the "Query Params" table:

|     |     |     |
| --- | --- | --- |
| **Key** | **Value** | **Returned fields** |
| `user.fields` | `created_at` | `user.created_at` |
| `expansions` | `author_id` | tweet.id, tweet.text |
| `tweet.fields` | `created_at` | `includes.users.created_at` |

You should now see the following URL next to the "Send" button:

      `https://api.twitter.com/2/users/search?query=xdevelopers&user.fields=description,location`
    

####   
Step five: Make your request and review your response

Once you have everything set up, hit the "Send" button and you will receive the following response:

      `{     "data": [         {             "location": "127.0.0.1",             "name": "Developers",             "description": "The voice of the X Dev team and your official source for updates, news, and events, related to the X API.",             "username": "XDevelopers",             "id": "2244994945"         },         {             "location": "Seattle, WA",             "name": "Suhem Parack",             "description": "Partner Engineering @XDevelopers",             "username": "suhemparack",             "id": "857699969263964161"         },         {             "location": "New York, NY",             "name": "Chris Park",             "description": "𝕏 | @X @API @XDevelopers",             "username": "chrisparkX",             "id": "2533341854"         },         {             "location": "Islington, London",             "name": "Haim Vaturi",             "description": "@XDevelopers",             "username": "haimvat",             "id": "853388192"         },         {             "location": "Canada",             "name": "ROBLOX Devs",             "description": "Follow this account for a lot of cool ROBLOXdev from all kinds of different ROBLOX developers! Not an official @ROBLOX twitter account",             "username": "RBXdevelopers",             "id": "829457852125306890"         },         {             "location": "東京都港区",             "name": "Twitter Dev Japan",             "description": "This account is no longer active. Follow @XDevelopers for updates.",             "username": "TwitterDevJP",             "id": "70915829"         },         {             "name": "Rains®™☔️🧠 0xdevelopers.eth.eth",             "description": "",             "username": "0xdevelopersTm",             "id": "1619352801104039936"         },         {             "name": "Project X Developers",             "description": "",             "username": "ProXDevelopers",             "id": "708786906058756096"         },         {             "location": "Los Angeles, CA",             "name": "XDevelopersUS",             "description": "",             "username": "XDevelopersUS",             "id": "1315227013028904960"         },         {             "location": "Rio de Janeiro & São Paulo",             "name": "XDevelopers",             "description": "Contato e Suporte Via Telefone (RJ): 21 980534086 e Via Email: contato@XDevelopers.com.br",             "username": "XDevBrasil",             "id": "3296066705"         }     ],     "meta": {         "next_token": "5qym3iwo3naekslszn59lxy1d9nmc6q"     } }`
    

Next steps
----------

[Customize your request using the API Reference](https://developer.twitter.com/en/docs/twitter-api/compliance/batch-compliance/api-reference "Customize your request using the API Reference")

[Reach out to the community for help](https://twittercommunity.com/ "Reach out to the community for help")