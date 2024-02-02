Introduction

Introduction
------------

This List lookup group has two available endpoints. You are able to retrieve a specified List by ID and get details on user-owned Lists. With the Lists endpoints, you can build solutions that enable people to curate and organize Tweets based on preferences, interests, groups, or topics. 

There is a rate limit of 75 requests per 15 minutes when looking up a specified List by ID and a limit of 15 requests per 15 minutes when looking up user-owned Lists.

You can use [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a), [App only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only), or [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code) to authenticate your requests to these endpoints. 

**Account setup**

To access these endpoints, you will need:

* An approved [developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info).
* To authenticate using the keys and tokens from a [developer App](https://developer.twitter.com/en/docs/apps) that is located within a [Project](https://developer.twitter.com/en/docs/projects). 

Learn more about getting access to the Twitter API v2 endpoints in our [getting started guide](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api).

[Quick start](https://developer.twitter.com/en/docs/twitter-api/lists/manage-lists/quick-start)

[Sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code)

[Run in Postman](https://t.co/twitter-api-postman)

[Try with API Explorer](https://developer.twitter.com/apitools/api?endpoint=/2/lists/%7Bid%7D&method=get)

Supporting resources
--------------------

[Learn how to use Postman to make requests](https://developer.twitter.com/en/docs/tutorials/postman-getting-started "Learn how to use Postman to make requests")

[Troubleshoot an error](https://developer.twitter.com/en/support/twitter-api "Troubleshoot an error")

[Visit the API reference page for this endpoint](https://developer.twitter.com/en/docs/twitter-api/lists/list-lookup/api-reference "Visit the API reference page for this endpoint")

Quick start

Getting started with the List lookup endpoint
---------------------------------------------

This quick start guide will help you make your first request to the List lookup endpoint using Postman.

Please visit our [Twitter API v2 sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code) GitHub repository if you want to see sample code in different languages.

**Note:** For this example, we will make a request to the _List lookup by ID_ endpoint, but you can apply the learnings from this quick start to other lookup requests as well.

### Prerequisites

To complete this guide, you will need to have a set of [keys and tokens](https://developer.twitter.com/en/docs/authentication) to authenticate your request. You can generate these keys and tokens by following these steps:

* [Sign up for a developer account](https://developer.twitter.com/en/apply-for-access) and receive approval.
* Create a [Project](https://developer.twitter.com/en/docs/projects) and an associated [developer App](https://developer.twitter.com/en/docs/apps) in the developer portal.
* Navigate to your App's “Keys and tokens” page to generate the required credentials. Make sure to save all credentials in a secure location.

### Steps to build a List lookup request

#### Step one: Start with a tool or library

There are several different tools, code examples, and libraries that you can use to make a request to this endpoint, but we will use the Postman tool here to simplify the process.

To load the Twitter API v2 Postman collection into your environment, please click on the following button:

[Add Twitter API v2 to Postman](https://t.co/twitter-api-postman)

Once you have the Twitter API v2 collection loaded in Postman, navigate to the “List” folder, select another folder “List lookup”, and then choose "List by ID".  
 

#### Step two: Authenticate your request

To properly make a request to the Twitter API, you need to verify that you have permission. To do this with this endpoint, you must authenticate your request with either [App only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only), [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code), or [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) authentication methods.

For simplicity's sake, we are going to utilize App only with this request, but if you'd like to request private [metrics](https://developer.twitter.com/en/docs/twitter-api/metrics) or Lists, you will need to use one of the other authentication methods. 

To utilize App only, you must add your keys and tokens (specifically the [App only Access Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens)) to Postman by selecting the environment named “Twitter API v2” (in the top-right corner of Postman), and adding your keys and tokens to the "initial value" and "current value" fields (by clicking the eye icon next to the environment dropdown).

If you've done this correctly, these variables will automatically be pulled into the request's authorization tab.  
 

#### Step three: Identify and specify which List you would like to retrieve

You must specify a List that you would like to receive within the request. You can find the List ID by navigating to twitter.com and clicking on a List and then looking in the URL. For example, the following URL's List ID is 84839422.

https://twitter.com/i/lists/84839422

The target ID can be any valid List ID. In Postman, navigate to the "Params" tab, and enter your ID into the "Value" column of the id path variable. Be sure not to include any spaces before or after any ID.

|     |     |
| --- | --- |
| **Key** | **Value** |
| id  | 84839422 (The List ID) |

  
Step four: Identify and specify which fields you would like to retrieve  

If you click the "Send" button after step three, you will receive the default [List object](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/lists) fields in your response: id, name.

If you would like to receive additional fields, you will have to specify those fields in your request with list.fields and/or [expansion](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/introduction/expansions) parameters.

For this exercise, we will request three additional sets of fields from different objects:

* The additional created\_at field in the primary Lists object.
    
* The full [user object](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) using the expansion parameter
    
* The additional user.created\_at field in the associated user object.
    

In Postman, navigate to the "Params" tab and add the following key:value pair to the "Query Params" table:

|     |     |     |
| --- | --- | --- |
| **Key** | **Value** | **Returned fields** |
| list.fields | created\_at | created\_at |
| expansions | owner\_id | includes.users.id,  <br>includes.users.name,  <br>includes.users.username |
| user.fields | created\_at | includes.users.created\_at |

You should now see a similar URL next to the “Send” button:

      `https://api.twitter.com/2/lists/84839422?list.fields=owner_id&expansions=owner_id&user.fields=created_at`
    

Step five: Make your request and review your response  

Once you have everything set up, hit the "Send" button, and you will receive a similar response to the following example response:

      `{   "data": {     "id": "84839422",     "name": "Official Twitter Accounts",     "owner_id": "783214"   },   "includes": {     "users": [       {         "name": "Twitter",         "created_at": "2007-02-20T14:35:54.000Z",         "username": "Twitter",         "id": "783214"       }     ]   } }`
    

Next steps
----------

[Customize your request using the API Reference](https://developer.twitter.com/en/docs/twitter-api/lists/list-lookup/api-reference "Customize your request using the API Reference")

[Reach out to the community for help](https://twittercommunity.com/ "Reach out to the community for help")

Integrate

Integration guide
-----------------

This page contains information on several tools and critical concepts that you should know as you integrate the List lookup endpoints into your system. We’ve broken the page into a couple of different sections:

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

Are you interested in getting set up with this endpoint with some code in your preferred coding language? We’ve got a handful of different code samples available that you can use as a starting point on our [Github page](https://github.com/twitterdev/Twitter-API-v2-sample-code).

#### Third-party libraries

Take advantage of one of our communities’ [third-party libraries](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries) to help you get started. You can find a library that works with the v2 endpoints by looking for the proper version tag.

### Key concepts

#### Authentication

All Twitter API v2 endpoints require you to authenticate your requests with a set of credentials, also known as keys and tokens. You can use either OAuth 1.0a User Context, App only or OAuth 2.0 Authorization Code with PKCE to authenticate your requests to these endpoints. . 

[OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a), which means that you must use a set of API Keys and user Access Tokens to make a successful request. The access tokens must be associated with the user that you are making the request on behalf of. If you would like to generate a set of Access Tokens for another user, they must authorize your App using the [3-legged OAuth flow](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens).

Please note that OAuth 1.0a can be difficult to use. If you are not familiar with this authentication method, we recommend that you use a [library](https://developer.twitter.com/content/en/docs/twitter-api/tools-and-libraries), use a tool like Postman, or use OAuth 2.0 to authenticate your requests.

[OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code) allows for greater control over an application’s scope, and authorization flows across multiple devices. OAuth 2.0 allows you to pick specific fine-grained scopes which give you specific permissions on behalf of a user. 

To enable OAuth 2.0 in your App, you must enable it in your’s App’s authentication settings found in the App settings section of the developer portal.

[App only](https://developer.twitter.com/en/docs/authentication/oauth-2-0) just requires that you pass a [App only Access Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens) with your request. You can either generate an App only token from directly within a developer App, or generate one using the [POST oauth2/token](https://developer.twitter.com/en/docs/authentication/api-reference/token) endpoint.

#### Developer portal, Projects, and developer Apps

To retrieve a set of authentication credentials that will work with the Twitter API v2 endpoints, you must [sign up for a developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info), set up a [Project](https://developer.twitter.com/en/docs/projects) within that account, and created a [developer App](https://developer.twitter.com/en/docs/apps) within that Project. You can then find your keys and tokens within your developer App.  
 

#### Rate limits

Every day, many thousands of developers make requests to the Twitter API. To help manage the sheer volume of these requests, [rate limits](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/rate-limits) are placed on each endpoint that limits the number of requests you can make on behalf of your app or on behalf of an authenticated user. 

These endpoints are rate limited at both the App-level and the user-level. The app rate limit means that you, the developer, can only make a certain number of requests to this endpoint over a given period of time from any given App (assumed by using either the API Key and API Secret Key, or the App only Access Token). The user rate limit means that the authenticated user that you are making the request on behalf of can only perform a List lookup a certain number of times across any developer App.

The chart below shows the rate limits for each endpoint.

|     |     |     |
| --- | --- | --- |
| **Endpoint** | **HTTP method** | **Rate limit** |
| /2/lists/:id | GET | 75 requests per 15 minutes |
| /2/users/:id/owned\_lists | GET | 15 requests per 15 minutes |

Fields and expansions  

The Twitter API v2 GET endpoint allows users to select exactly which data they want to return from the API using a set of tools called `fields` and `expansions`. The `expansions` parameter allows you to expand objects referenced in the payload. For example, looking up a List by ID allows you to pull the following [expansions](https://developer.twitter.com/en/docs/twitter-api/expansions):

* `owner_id`
    

The `fields` parameter allows you to select exactly which [fields](https://developer.twitter.com/en/docs/twitter-api/fields) within the different data objects you would like to receive. These endpoints deliver List objects primarily. By default, the List object returns the `id`, and `name` fields. To receive additional fields such as `list.created_at` or `list.follower_count`, you will have to specifically request those using a list.fields parameter. 

We’ve added a guide on using [fields and expansions](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/using-fields-and-expansions) together to our [Twitter API v2 data dictionary](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/introduction).

 The chart below shows the field and expansions available for this endpoint group:

|     |     |     |
| --- | --- | --- |
| **Endpoint** | **Fields** | **Expansions** |
| /2/lists/:id | `list.fields`<br><br>`user.fields` | `owner_id` |
| /2/users/:id/owned\_lists | list.fields<br><br>user.fields | owner\_id |

#### Pagination

Looking up user owned Lists can return a lot of data. To ensure we are returning consistent, high-performing results at any given time, we use pagination. Pagination is a feature in Twitter API v2 endpoints that return more results than can be returned in a single response. When that happens, the data is returned in a series of 'pages'. Learn more about how to [paginate through results.](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/pagination)

Next steps
----------

[Visit the API reference page for these endpoint](https://developer.twitter.com/en/docs/twitter-api/lists/list-lookup/api-reference "Visit the API reference page for these endpoint")

Migrate

Comparing Twitter API’s List lookup endpoints
---------------------------------------------

The v2 List lookup endpoint group will replace the standard v1.1 [GET lists/show](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-show) and  [GET lists/ownership](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-ownerships) endpoints. If you have code, apps, or tools that use one of these versions of the List lookup endpoints, and are considering migrating to the newer Twitter API v2 endpoint, then this set of guides is for you.

The following tables compare the standard v1.1 and Twitter API v2 List endpoints:

**List Lookup by ID**

|     |     |     |
| --- | --- | --- |
| Description | Standard v1.1 | Twitter API v2 |
| HTTP methods supported | `GET` | `GET` |
| Host domain | `https://api.twitter.com` | `https://api.twitter.com` |
| Endpoint path | `/1.1/lists/show.json` | `/2/lists/:id` |
| [Authentication](https://developer.twitter.com/content/developer-twitter/en/docs/authentication) | OAuth 1.0a User Context<br><br>App only | OAuth 1.0a User Context<br><br>OAuth 2.0 Authorization Code with PKCE<br><br>App only |
| Default request [rate limits](https://developer.twitter.com/content/developer-twitter/en/docs/rate-limits) | 75 requests per 15 min with OAuth 1.0a<br><br>75 requests per 15min with OAuth 2.0<br><br>75 requests per 15 min with App only | 75 requests per 15 min with OAuth 1.0a<br><br>75 requests per 15 min with OAuth 2.0<br><br>75 requests per 15 min with App only |

**User owned List lookup**

|     |     |     |
| --- | --- | --- |
| Description | Standard v1.1 | Twitter API v2 |
| HTTP methods supported | `GET` | `GET` |
| Host domain | `https://api.twitter.com` | `https://api.twitter.com` |
| Endpoint path | `/1.1/lists/ownerships.json` | `/2/users/:id/owned_lists` |
| [Authentication](https://developer.twitter.com/content/developer-twitter/en/docs/authentication) | OAuth 1.0a User Context<br><br>App only | OAuth 1.0a User Context<br><br>OAuth 2.0 Authorization Code with PKCE<br><br>App only |
| Default request [rate limits](https://developer.twitter.com/content/developer-twitter/en/docs/rate-limits) | 15 requests per 15 min with OAuth 1.0a<br><br>15 requests per 15 min with App only | 15 requests per 15 min with OAuth 1.0a<br><br>15 requests per 15min with OAuth 2.0<br><br>15 requests per 15 min with App only |

To access the Twitter API v2 endpoints, you must [sign up for a developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info). When authenticating, you must use keys and tokens from a [developer App](https://developer.twitter.com/en/docs/apps) that is located within a [Project](https://developer.twitter.com/en/docs/projects). 

Learn more about getting access to the Twitter API v2 endpoints in our [getting started](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api) page.

[Quick start](https://developer.twitter.com/en/docs/twitter-api/lists/list-lookup/quick-start)

[Sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code)

[Run in Postman](https://t.co/twitter-api-postman)

Supporting resources
--------------------

[Learn how to use Postman to make requests](https://developer.twitter.com/en/docs/tutorials/postman-getting-started "Learn how to use Postman to make requests")

[Troubleshoot an error](https://developer.twitter.com/en/support/twitter-api "Troubleshoot an error")

[Visit the API reference page for this endpoint](https://developer.twitter.com/en/docs/twitter-api/lists/list-lookup/api-reference "Visit the API reference page for this endpoint")

List lookup: Standard v1.1 compared to Twitter API v2

List lookup: Standard v1.1 compared to Twitter API v2
-----------------------------------------------------

If you have been working with the standard v1.1 [GET lists/show](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-show) and  [GET lists/ownerships](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-ownerships) endpoints, the goal of this guide is to help you understand the similarities and differences between the standard v1.1 and Twitter API v2 List lookup endpoints.

* **Similarities**
    * Authentication methods
    * Rate limits
* **Differences**
    * Endpoint URLs
    * App and Project requirements
    * Data objects per request limits
    * Response data formats
    * Request parameters

### Similarities

#### **Authentication**

Both endpoint versions support both [OAuth 1.0a User Context](https://developer.twitter.com/content/developer-twitter/en/docs/authentication/oauth-1-0a) and [App only](https://developer.twitter.com/content/developer-twitter/en/docs/authentication/oauth-2-0). Therefore, if you were previously using one of the standard v1.1 List lookup endpoints, you can continue using the same authentication method if you migrate to the Twitter API v2 version.

Depending on your authentication library/package of choice, App only authentication is probably the easiest way to get started and can be set with a simple request header. To learn how to generate an App only Access Token, see [this App only guide](https://developer.twitter.com/en/docs/basics/authentication/overview/application-only).

**Rate limits**

|     |     |
| --- | --- |
| **Standard v1.1** | **Twitter API v2** |
| /1.1/lists/show.json<br><br>75 requests per 15-minute window with OAuth 1.0a User Context<br><br>75 requests per 15-minute window with App only | /2/lists/:id<br><br>75 requests per 15-minute window with OAuth 1.0a User Context<br><br>75 requests per 15-minute window with OAuth 2.0 Authorization Code with PKCE |
| /1.1/lists/ownerships.json<br><br>15 requests per 15-minute window with OAuth 1.0a User Context<br><br>15 requests per 15-minute window with App only | /2/users/:id/owned\_lists<br><br>15 requests per 15-minute window with OAuth 1.0a User Context<br><br>15 requests per 15-minute window with OAuth 2.0 Authorization Code with PKCE<br><br>15 requests per 15-minute window with App only |

### Differences

#### Endpoint URLs

* Standard v1.1 endpoints:
    * GET https://api.twitter.com/1.1/lists/show.json  
        (Lookup a specified List)
    * GET https://api.twitter.com/1.1/lists/ownerships.json  
        (Lookup specified user owned Lists)
* Twitter API v2 endpoint:
    * GET https://api.twitter.com/2/lists/:id  
        (Lookup a specified List)  
        
    * GET https://api.twitter.com/2/users/:id/owned\_lists  
        (Lookup specified user owned Lists)

#### App and Project requirements

The Twitter API v2 endpoints require that you use credentials from a [developer App](https://developer.twitter.com/en/docs/apps) that is associated with a [Project](https://developer.twitter.com/en/docs/projects) when authenticating your requests. All Twitter API v1.1 endpoints can use credentials from standalone Apps or Apps associated with a project.

####   
  
Data objects per request limits

The standard v1.1 /lists/ownerships endpoint allows you to return up to 1000 Lists per request. The new v2 endpoints allow you to return up to 100 Lists per request. By default, 100 user objects will be returned, to change the number of results you will need to pass a query parameter max\_results= with a number between 1-100; you can then pass the next\_token returned in the response payload to the pagination\_token query parameter in your next request.

**Response data format**

One of the biggest differences between standard v1.1 and Twitter API v2 endpoint versions is how you select which fields return in your payload.

For the standard endpoints, you receive many of the response fields by default and then have the option to use parameters to identify which additional fields or sets of fields should return in the payload.

The Twitter API v2 version only delivers the List id and name fields by default. To request any additional fields or objects, you will need to use the [fields](https://developer.twitter.com/en/docs/twitter-api/fields/content/developer-twitter/en/docs/twitter-api/fields) and [expansions](https://developer.twitter.com/en/docs/twitter-api/fields/content/developer-twitter/en/docs/twitter-api/expansions) parameters. Any List fields that you request from this endpoint will return in the primary List object. Any expanded Tweet or user object and fields will return an includes object within your response. You can then match any expanded objects back to the List object by matching the IDs located in both the user and the expanded Tweet object. 

Here are examples of possible List fields and expansions:

* created\_at
    
* follower\_count
    
* member\_count
    
* owner\_id
    
* description
    
* private
    

|     |     |
| --- | --- |
| **Endpoint** | **Expansion** |
| /2/lists/:id | owner\_id |
| /2/users/:id/owned\_lists | owner\_id |

We encourage you to read more about these new parameters in their respective guides, or by reading our guide on [how to use fields and expansions](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/using-fields-and-expansions). 

We have also put together a [data format migration guide](https://developer.twitter.com/en/docs/twitter-api/migrate/data-formats/standard-v1-1-to-v2) that can help you map standard v1.1 fields to the newer v2 fields. This guide will also provide you with the specific expansion and field parameter that you will need to pass with your v2 request to return specific fields. 

In addition to the changes in how you request certain fields, Twitter API v2 is also introducing new JSON designs for the objects returned by the APIs, including [Tweet](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) and [user](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) objects.

* At the JSON root level, the standard endpoints return Tweet objects in a statuses array, while Twitter API v2 returns a data array. 
    
* Instead of referring to Retweeted and Quoted "statuses", Twitter API v2 JSON refers to Retweeted and Quoted Tweets. Many legacy and deprecated fields, such as contributors and user.translator\_type are being removed. 
    
* Instead of using both favorites (in Tweet object) and favourites (in user object), Twitter API v2 uses the term like. 
    
* Twitter is adopting the convention that JSON values with no value (for example, null) are not written to the payload. Tweet and user attributes are only included if they have non-null values.  
     
    

#### Request parameters

The following standard v1.1 request parameters have equivalents in Twitter API v2:

**List lookup by ID**

|     |     |
| --- | --- |
| **Standard v1.1** | **Twitter API v2** |
| list\_id | id  |
| slug | No equivalent |
| owner\_screen\_name | No equivalent |
| owner\_id | Requested with expansions/fields parameter |

**User owned List lookup**

|     |     |
| --- | --- |
| **Standard v1.1** | **Twitter API v2** |
| user\_id | id  |
| screen\_name | No equivalent |
| count | max\_results |
| cursor | pagination\_token |
|     |     |

Next steps
----------

[Review the List lookup API references](https://developer.twitter.com/en/docs/twitter-api/lists/list-lookup/api-reference "Review the List lookup API references")

API reference

API reference index
-------------------

For the complete API reference, select an endpoint from the list.  
  

|     |     |
| --- | --- |
| **Lookup a specific list by ID** | `[GET /2/lists/:id](https://developer.twitter.com/en/docs/twitter-api/lists/list-lookup/api-reference/get-lists-id)` |
| **Lookup a user's owned List** | `[GET /2/users/:id/owned_lists](https://developer.twitter.com/en/docs/twitter-api/lists/list-lookup/api-reference/get-users-id-owned_lists)` |

GET /2/lists/:id

GET /2/lists/:id
================

Returns the details of a specified List.

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Try a live request ❯](https://oauth-playground.glitch.me/?id=listIdGet&params=%28%27query%21%28%29%7Ebody%21%27%27%7Epath%21%28%29%29_) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Flists%2F%7Bid%7D&method=get) 

### Endpoint URL

`https://api.twitter.com/2/lists/:id`  
  

### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 2.0 App-only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only "Use this method to obtain information in the context of an unauthenticated public user. This method is for developers that just need read-only access to public information. Click to learn how to obtain an OAuth 2.0 App Access Token.")<br><br>[OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code "This method allows an authorized app to act on behalf of the user, as the user. It is typically used to access or post public information for a specific user, and it us useful when your app needs to be aware of the relationship between a user and what this endpoint returns. Click to learn how to authenticate with OAuth 2.0 Authorization Code with PKCE.")<br><br>[OAuth 1.0a](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) is also available for this endpoint. |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | App rate limit (Application-only): 75 requests per 15-minute window shared among all users of your app<br><br>User rate limit (User context): 75 requests per 15-minute window per each authenticated user |

### OAuth 2.0 scopes required by this endpoint

|     |
| --- |
| `tweet.read`<br><br>`users.read`<br><br>`list.read` |
| [Learn more about OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/twitter-api/oauth2) |

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Required | string | The ID of the List to lookup. |

  
  

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| `expansions`  <br> Optional | enum (`owner_id`) | [Expansions](https://developer.twitter.com/en/docs/twitter-api/expansions) enable you to request additional data objects that relate to the originally returned List. The ID that represents the expanded data object will be included directly in the List data object, but the expanded object metadata will be returned within the `includes` response object, and will also include the ID so that you can match this data object to the original user object. At this time, the only expansion available to endpoints that primarily return List objects is `expansions=owner_id`. You will find the expanded user data object living in the `includes` response object. |
| `list.fields`  <br> Optional | enum (`created_at`, `follower_count`, `member_count`, `private`, `description`, `owner_id`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [List fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/lists) will deliver with each returned List objects. Specify the desired fields in a comma-separated list without spaces between commas and fields. These specified List fields will display directly in the List data objects. |
| `user.fields`  <br> Optional | enum (`created_at`, `description`, `entities`, `id`, `location`, `most_recent_tweet_id`, `name`, `pinned_tweet_id`, `profile_image_url`, `protected`, `public_metrics`, `url`, `username`, `verified`, `withheld`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [user fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) will deliver with the users object. Specify the desired fields in a comma-separated list without spaces between commas and fields. The user fields will only be returned if you have included `expansions=owner_id` query parameter in your request. You will find this ID and all additional user fields in the `included` data object. |

  
  

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript (Default fields)](#tab0)
* [TypeScript (Optional fields)](#tab1)
* [Java (Default fields)](#tab2)
* [Java (Optional fields)](#tab3)

TypeScript (Default fields)

TypeScript (Optional fields)

Java (Default fields)

Java (Optional fields)

      `(async () => {   try {     const getListBtId = await twitterClient.lists.listIdGet(       //The ID of the List to get       84839422     );     console.dir(getListBtId, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `(async () => {   try {     const getListBtId = await twitterClient.lists.listIdGet(       //The ID of the List to get       84839422,       {         //A comma separated list of fields to expand         expansions: ["owner_id"],          //A comma separated list of List fields to display         "list.fields": ["follower_count"],          //A comma separated list of User fields to display         "user.fields": ["username"],       }     );     console.dir(getListBtId, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  // String | The ID of the List to get String id = "84839422";  try {     SingleListLookupResponse result = apiInstance.lists().listIdGet(id, null, null, null);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling ListsApi#listIdGet");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

      `// Set the params values  // String | The ID of the List to get String id = "84839422";  // Set<String> | A comma separated list of List fields to display Set<String> listFields = new HashSet<>(Arrays.asList("follower_count"));  // Set<String> | A comma separated list of fields to expand Set<String> expansions = new HashSet<>(Arrays.asList("owner_id"));  // Set<String> | A comma separated list of User fields to display Set<String> userFields = new HashSet<>(Arrays.asList("username"));  try {     SingleListLookupResponse result = apiInstance.lists().listIdGet(id, listFields, expansions, userFields);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling ListsApi#listIdGet");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

### Example responses

* [Default fields](#tab0)
* [Optional fields](#tab1)

Default fields

Optional fields

      `{   "data": {     "id": "84839422",     "name": "Official Twitter Accounts"   } }`
    

      `{   "data": {     "follower_count": 906,     "id": "84839422",     "name": "Official Twitter Accounts",     "owner_id": "783214"   },   "includes": {     "users": [       {         "id": "783214",         "name": "Twitter",         "username": "Twitter"       }     ]   } }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Default | string | Unique identifier of this List. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. |
| `name`  <br> Default | string | The name of this List. |
| `created_at` | date (ISO 8601) | Creation time of this List.  <br>  <br>To return this field, add `list.fields=created_at` in the request's query parameter. |
| `private` | boolean | Indicates if this List has been set to private. The List (in other words, if this is publicly viewed or not).  <br>  <br>To return this field, add `list.fields=private` in the request's query parameter. |
| `follower_count` | integer | Number of users who follow this List.  <br>  <br>To return this field, add `list.fields=follower_count` in the request's query parameter. |
| `member_count` | integer | Number of users who are a member of this List.  <br>  <br>To return this field, add `list.fields=member_count` in the request's query parameter. |
| `owner_id` | string | Unique identifier of this List's owner. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers.  <br>  <br>To return this field, add `list.fields=owner_id` in the request's query parameter. |
| `description` | string | A brief description of this List, if the owner provided one.  <br>  <br>To return this field, add `list.fields=description` in the request's query parameter. |
| `includes.users` | array | When including the `expansions=owner_id` parameter, this includes the referenced List owner in the form of a [user object](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) with their default fields and any additional fields requested using the `user.fields` parameter. |

GET /2/users/:id/owned\_lists

GET /2/users/:id/owned\_lists
=============================

Returns all Lists owned by the specified user.

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Try a live request ❯](https://oauth-playground.glitch.me/?id=listUserOwnedLists&params=%28%27query%21%28%29%7Ebody%21%27%27%7Epath%21%28%29%29_) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Fusers%2F%7Bid%7D%2Fowned_lists&method=get) 

### Endpoint URL

`https://api.twitter.com/2/users/:id/owned_lists`  
  

### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code "This method allows an authorized app to act on behalf of the user, as the user. It is typically used to access or post public information for a specific user, and it us useful when your app needs to be aware of the relationship between a user and what this endpoint returns. Click to learn how to authenticate with OAuth 2.0 Authorization Code with PKCE.")<br><br>[OAuth 2.0 App-only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only "Use this method to obtain information in the context of an unauthenticated public user. This method is for developers that just need read-only access to public information. Click to learn how to obtain an OAuth 2.0 App Access Token.")<br><br>[OAuth 1.0a](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) is also available for this endpoint. |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | App rate limit (Application-only): 15 requests per 15-minute window shared among all users of your app<br><br>User rate limit (User context): 15 requests per 15-minute window per each authenticated user |

### OAuth 2.0 scopes required by this endpoint

|     |
| --- |
| `tweet.read`<br><br>`users.read`<br><br>`list.read` |
| [Learn more about OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/twitter-api/oauth2) |

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Required | string | The user ID whose owned Lists you would like to retrieve. |

  
  

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| `expansions`  <br> Optional | enum (`owner_id`) | [Expansions](https://developer.twitter.com/en/docs/twitter-api/expansions) enable you to request additional data objects that relate to the originally returned List. The ID that represents the expanded data object will be included directly in the List data object, but the expanded object metadata will be returned within the `includes` response object, and will also include the ID so that you can match this data object to the original user object. At this time, the only expansion available to endpoints that primarily return List objects is `expansions=owner_id`. You will find the expanded user data object living in the `includes` response object. |
| `list.fields`  <br> Optional | enum (`created_at`, `follower_count`, `member_count`, `private`, `description`, `owner_id`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [List fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/lists) will deliver with each returned List objects. Specify the desired fields in a comma-separated list without spaces between commas and fields. These specified List fields will display directly in the List data objects. |
| `max_results`  <br> Optional | integer | The maximum number of results to be returned per page. This can be a number between 1 and 100. By default, each page will return 100 results. |
| `pagination_token`  <br> Optional | string | Used to request the next page of results if all results weren't returned with the latest request, or to go back to the previous page of results. To return the next page, pass the next\_token returned in your previous response. To go back one page, pass the previous\_token returned in your previous response. |
| `user.fields`  <br> Optional | enum (`created_at`, `description`, `entities`, `id`, `location`, `most_recent_tweet_id`, `name`, `pinned_tweet_id`, `profile_image_url`, `protected`, `public_metrics`, `url`, `username`, `verified`, `withheld`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [user fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) will deliver with the users object. Specify the desired fields in a comma-separated list without spaces between commas and fields. The user fields will only be returned if you have included `expansions=owner_id` query parameter in your request. You will find this ID and all additional user fields in the `included` data object. |

  
  

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript (Default fields)](#tab0)
* [TypeScript (Optional fields)](#tab1)
* [Java (Default fields)](#tab2)
* [Java (Optional fields)](#tab3)

TypeScript (Default fields)

TypeScript (Optional fields)

Java (Default fields)

Java (Optional fields)

      `(async () => {   try {     const getListBtId = await twitterClient.lists.listUserOwnedLists(       //The ID of the user for whom to return results       2244994945     );     console.dir(getListBtId, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `(async () => {   try {     const getListBtId = await twitterClient.lists.listUserOwnedLists(       //The ID of the user for whom to return results       2244994945,       {         //A comma separated list of fields to expand         expansions: ["owner_id"],          //A comma separated list of List fields to display         "list.fields": ["follower_count"],          //A comma separated list of User fields to display         "user.fields": ["created_at"],       }     );     console.dir(getListBtId, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  // String | The ID of the user for whom to return results String id = "2244994945";  try {     MultiListResponse result = apiInstance.lists().listUserOwnedLists(id, null, null, null, null, null);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling ListsApi#listUserOwnedLists");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

      `// Set the params values // For full list of params visit - https://github.com/twitterdev/twitter-api-java-sdk/blob/main/docs/ListsApi.md#listUserOwnedLists  // String | The ID of the user for whom to return results String id = "2244994945";  // Set<String> | A comma separated list of List fields to display Set<String> listFields = new HashSet<>(Arrays.asList("follower_count"));  // Set<String> | A comma separated list of fields to expand Set<String> expansions = new HashSet<>(Arrays.asList("owner_id"));  // Set<String> | A comma separated list of User fields to display Set<String> userFields = new HashSet<>(Arrays.asList("created_at"));  try {     MultiListResponse result = apiInstance.lists().listUserOwnedLists(id, null, null, listFields, expansions, userFields);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling ListsApi#listUserOwnedLists");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

### Example responses

* [Default fields](#tab0)
* [Optional fields](#tab1)

Default fields

Optional fields

      `{   "data": [     {       "id": "1451305624956858369",       "name": "Test List"     }   ],   "meta": {     "result_count": 1   } }`
    

      `{   "data": [     {       "follower_count": 0,       "id": "1451305624956858369",       "name": "Test List",       "owner_id": "2244994945"     }   ],   "includes": {     "users": [       {         "username": "TwitterDev",         "id": "2244994945",         "created_at": "2013-12-14T04:35:55.000Z",         "name": "Twitter Dev"       }     ]   },   "meta": {     "result_count": 1   } }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Default | string | Unique identifier of this List. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. |
| `name`  <br> Default | string | The name of this List. |
| `created_at` | date (ISO 8601) | Creation time of this List.  <br>  <br>To return this field, add `list.fields=created_at` in the request's query parameter. |
| `private` | boolean | Indicates if this List has been set to private. The List (in other words, if this is publicly viewed or not).  <br>  <br>To return this field, add `list.fields=private` in the request's query parameter. |
| `follower_count` | integer | Number of users who follow this List.  <br>  <br>To return this field, add `list.fields=follower_count` in the request's query parameter. |
| `member_count` | integer | Number of users who are a member of this List.  <br>  <br>To return this field, add `list.fields=member_count` in the request's query parameter. |
| `owner_id` | string | Unique identifier of this List's owner. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers.  <br>  <br>To return this field, add `list.fields=owner_id` in the request's query parameter. |
| `description` | string | A brief description of this List, if the owner provided one.  <br>  <br>To return this field, add `list.fields=description` in the request's query parameter. |
| `includes.users` | array | When including the `expansions=owner_id` parameter, this includes the referenced List owner in the form of a [user object](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) with their default fields and any additional fields requested using the `user.fields` parameter. |
| `meta`  <br> Default | object | This object contains information about the number of users returned in the current request, and pagination details. |
| `meta.result_count`  <br> Default | integer | The number of users returned in this request. Note that this number may be lower than what was specified in the `max_results` query parameter. |
| `meta.previous_token` | string | Pagination token for the previous page of results. This value is returned when there are multiple pages of results, as the current request may only return a subset of results. To go back to the previous page, passing the value from this field in the `pagination_token` query parameter. When this field is not returned in the response, it means you are on the first page of results. |
| `meta.next_token` | string | Pagination token for the next page of results. This value is returned when there are multiple pages of results, as the current request may only return a subset of results. To retrieve the full list, keep passing the value from this field in the `pagination_token` query parameter. When this field is not returned in the response, it means you've reached the last page of results, and that there are no further pages. |

Introduction

Introduction
------------

[Twitter Lists](https://help.twitter.com/en/using-twitter/twitter-lists) allows users to customize, organize and prioritize the Tweets they see in their timeline. With the Lists endpoints, you can build solutions that enable people to curate and organize Tweets based on preferences, interests, groups, or topics.

Since you are making requests on behalf of a user with the manage List endpoints, you must authenticate these endpoints with either [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) or [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code), and use the user Access Tokens associated with a user that has authorized your App, which can be generated using the [3-legged OAuth flow](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens) (OAuth 1.0a) or the [Authorization Code with PKCE grant flow](https://developer.twitter.com/en/docs/authentication/oauth-2-0/user-access-token) (OAuth 2.0).  
 

### Manage Lists

The manage List endpoints allow you to create, delete, and update Lists on behalf of an authenticated user. For these endpoints, there are three methods available: POST, DELETE and PUT. The POST method allows you to create a List, the DELETE method allows you to delete a List, and the PUT method allows you to update the metadata of a List. There is a user rate limit of 300 requests per 15 minutes for all three endpoints.

Note that you can create up to 1000 Lists per account.

**Account setup**

To access these endpoints, you will need:

* An approved [developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info).
* To authenticate using the keys and tokens from a [developer App](https://developer.twitter.com/en/docs/apps) that is located within a [Project](https://developer.twitter.com/en/docs/projects). 

Learn more about getting access to the Twitter API v2 endpoints in our [getting started guide](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api).

[Quick start](https://developer.twitter.com/en/docs/twitter-api/lists/manage-lists/quick-start)

[Sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code)

[Run in Postman](https://t.co/twitter-api-postman)

[Try with API Explorer](https://developer.twitter.com/apitools/api?endpoint=/2/lists&method=post)

Supporting resources
--------------------

[Learn how to use Postman to make requests](https://developer.twitter.com/en/docs/tutorials/postman-getting-started "Learn how to use Postman to make requests")

[Troubleshoot an error](https://developer.twitter.com/en/support/twitter-api "Troubleshoot an error")

[Visit the API reference page for this endpoint](https://developer.twitter.com/en/docs/twitter-api/lists/manage-lists/api-reference "Visit the API reference page for this endpoint")

Quick start

Getting started with the manage Lists endpoint group
----------------------------------------------------

This quick overview will help you make your first request to the manage List endpoints using [Postman](https://developer.twitter.com/en/docs/tools-and-libraries/using-postman).

If you would like to see sample code in different languages, please visit our [Twitter API v2 sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code) GitHub repository. 

**Note:** For this example, we will make a request to the _Create a List_ endpoint, but you can apply the learnings from this quick start to other manage requests as well.

### Prerequisites

To complete this guide, you will need to have a set of [keys and tokens](https://developer.twitter.com/en/docs/authentication) to authenticate your request. You can generate these keys and tokens by following these steps:

* [Sign up for a developer account](https://developer.twitter.com/en/apply-for-access) and receive approval.
* Create a [Project](https://developer.twitter.com/en/docs/projects) and an associated [developer App](https://developer.twitter.com/en/docs/apps) in the developer portal.
* Navigate to your App's “Keys and tokens” page to generate the required credentials. Make sure to save all credentials in a secure location.

### Steps to build a manage List request

Step one: Start with a tool or library  

-----------------------------------------

There are several different tools, code examples, and libraries that you can use to make a request to this endpoint, but we will use the Postman tool here to simplify the process.

To load the Twitter API v2 Postman collection into your environment, please click on the following button:

[Add Twitter API v2 to Postman](https://t.co/twitter-api-postman)

Once you have the Twitter API v2 collection loaded in Postman, navigate to the “List” folder, select another folder “Manage List”, and then choose "Create a List".

#### Step two: Authenticate your request

To properly make a request to the Twitter API, you need to verify that you have permission to do so. To do this with the manage Tweets endpoints, you must authenticate your request using either [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) or [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code).

In this example, we are going to use OAuth 1.0a User Context.

You must add your keys and tokens (and specifically your API Key, API Secret Key, OAuth 1.0a user Access Token, and OAuth 1.0a user Access Token Secret) to Postman. You can do this by selecting the environment named “Twitter API v2” (in the top-right corner of Postman), and adding your keys and tokens to the "initial value" and "current value" fields (by clicking the eye icon next to the environment dropdown).

If you've done this correctly, these variables will automatically be pulled into the request's authorization tab.  
 

### Step three: Specify the name for the new List  

When creating a new List with this endpoint, a name for the List is a required body parameter. Optionally, you can provide a description and specify whether the List is private.

In Postman, navigate to the “Body” tab and enter the name of the List as the value for the name parameter. Additionally, if you wish to add a description for the List, simply add a new key labeled description in the same fashion as the name, followed by the description of the List as the value. Making a List private will follow the same pattern, but only true or false values are accepted for this parameter. 

|     |     |     |
| --- | --- | --- |
| **Key** | **Value** | **Parameter type** |
| `name` | Name of the list (required) | body |
| description | Description for the list (optional) | body |
| private | true or false (optional) | body |

You should now see a similar URL next to the "Send" button:

      `https://api.twitter.com/2/lists`
    

Step four: Make your request and review your response  

Once you have everything set up, hit the "Send" button, and you will receive a similar response to the following example response:

      `{   "data": {     "id": "1441162269824405510",     "name": "New list created from Postman"   } }`
    

If the returned response object contains an id and the name of your List, you have successfully created the List. 

To delete a List, select the “Delete a List” request also found in the “Lists” folder of the Twitter API v2 collection loaded in Postman. This endpoint requires the ID of the List you wish to delete. In the “Params” tab, enter the ID of the List you wish to delete as the value for the id column. 

On successful delete request, you will receive a response similar to the following example: 

      `{   "data": {     "deleted": true   } }`
    

Next steps
----------

[Customize your request using the API Reference](https://developer.twitter.com/en/docs/twitter-api/lists/manage-lists/api-reference "Customize your request using the API Reference")

[Reach out to the community for help](https://twittercommunity.com/ "Reach out to the community for help")

Integrate

Integration guide
-----------------

This page contains information on several tools and critical concepts that you should know as you integrate the Lists endpoints into your system. We’ve broken the page into a couple of different sections:

* [Helpful tools](#helpful)
* Key Concepts
* [Authentication](#authentication)
* [Developer portal, Projects, and Apps](#portal)
* [Rate limits](#limits)

### Helpful tools

Before we dive into some key concepts that will help you integrate this endpoint, we recommend that you become familiar with:

#### Postman

Postman is a great tool that you can use to test out an endpoint. Each Postman request includes every path and body parameter to help you quickly understand what is available to you. To learn more about our Postman collections, please visit our ["Using Postman"](https://developer.twitter.com/en/docs/tools-and-libraries/using-postman) page. 

#### Code samples

Are you interested in getting set up with this endpoint with some code in your preferred coding language? We’ve got a handful of different code samples available that you can use as a starting point on our [Github page](https://github.com/twitterdev/Twitter-API-v2-sample-code).

#### Third-party libraries

Take advantage of one of our communities’ [third-party libraries](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries) to help you get started. You can find a library that works with the v2 endpoints by looking for the proper version tag.

### Key concepts

#### Authentication

All Twitter API v2 endpoints require you to authenticate your requests with a set of credentials, also known as keys and tokens. 

These specific endpoints requires the use of [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a), which means that you must use a set of API keys and user Access Tokens to make a successful request. The Access Tokens must be associated with the user that you are making the request on behalf of. If you would like to generate a set of Access Tokens for another user, they must authorize or authenticate your App using the [3-legged OAuth flow](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens).

Please note that OAuth 1.0a can be tricky to use. If you are not familiar with this authentication method, we recommend that you use a [library](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/tools-and-libraries) or a tool like Postman to properly authenticate your requests.  
 

#### Developer portal, Projects, and developer Apps

To retrieve a set of authentication credentials that will work with the Twitter API v2 endpoints, you must [sign up for a developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info), set up a [Project](https://developer.twitter.com/en/docs/projects) within that account, and created a [developer App](https://developer.twitter.com/en/docs/apps) within that Project. You can then find your keys and tokens within your developer App.  
 

#### Rate limits

Every day, many thousands of developers make requests to the Twitter API. To help manage the sheer volume of these requests, [rate limits](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/rate-limits) are placed on each endpoint that limits the number of requests that you can make on behalf of your app or on behalf of an authenticated user. 

These endpoints are rate limited at the user level, meaning that the authenticated user that you are making the request on behalf of can only call the endpoint a certain number of times across any developer App. 

The chart below shows the rate limits for each endpoint.

|     |     |     |
| --- | --- | --- |
| **Endpoint** | **HTTP method** | **Rate limit** |
| /2/lists | POST | 300 requests per 15 minutes |
| /2/lists/:id | DELETE / PUT | 300 requests per 15 minutes |

Next steps
----------

[Visit the API reference page for these endpoint](https://developer.twitter.com/en/docs/twitter-api/lists/manage-lists/api-reference "Visit the API reference page for these endpoint")

Migrate

Comparing Twitter API’s Lists endpoints
---------------------------------------

The v2 manage Lists endpoints will eventually replace [POST lists/create](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-create), [POST lists/destroy](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-destroy), and [POST lists/update](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-update). If you have code, apps, or tools that use an older version of these endpoints and are considering migrating to the newer Twitter API v2, then this guide is for you. 

The following tables compare the standard v1.1 and Twitter API v2 List endpoints:  

**Create a List**

| Description | Standard v1.1 | Twitter API v2 |
| --- | --- | --- |
| HTTP methods supported | POST | POST |
| Host domain | https://api.twitter.com | https://api.twitter.com |
| Endpoint path | /1.1/lists/create.json | /2/lists |
| [Authentication](https://developer.twitter.com/content/developer-twitter/en/docs/authentication) | OAuth 1.0a User Context | OAuth 1.0a User Context |
| Default request [rate limits](https://developer.twitter.com/content/developer-twitter/en/docs/rate-limits) | None | 300 requests per 15 min (per user) |

**Delete a List**

| Description | Standard v1.1 | Twitter API v2 |
| --- | --- | --- |
| HTTP methods supported | POST | DELETE |
| Host domain | https://api.twitter.com | https://api.twitter.com |
| Endpoint path | /1.1/lists/destroy.json | /2/lists/:id |
| [Authentication](https://developer.twitter.com/content/developer-twitter/en/docs/authentication) | OAuth 1.0a User Context | OAuth 1.0a User Context |
| Default request [rate limits](https://developer.twitter.com/content/developer-twitter/en/docs/rate-limits) | None | 300 requests per 15 min (per user) |

**Update a List**

| Description | Standard v1.1 | Twitter API v2 |
| --- | --- | --- |
| HTTP methods supported | POST | PUT |
| Host domain | https://api.twitter.com | https://api.twitter.com |
| Endpoint path | /1.1/lists/update.json | /2/lists/:id |
| [Authentication](https://developer.twitter.com/content/developer-twitter/en/docs/authentication) | OAuth 1.0a User Context | OAuth 1.0a User Context |
| Default request [rate limits](https://developer.twitter.com/content/developer-twitter/en/docs/rate-limits) | None | 300 requests per 15 min (per user) |

To access the Twitter API v2 endpoints, you must [sign up for a developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info). When authenticating, you must use keys and tokens from a [developer App](https://developer.twitter.com/en/docs/apps) that is located within a [Project](https://developer.twitter.com/en/docs/projects). 

Learn more about getting access to the Twitter API v2 endpoints in our [getting started](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api) page.

[Quick start](https://developer.twitter.com/en/docs/twitter-api/lists/manage-lists/quick-start)

[Sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code)

[Run in Postman](https://t.co/twitter-api-postman)

Supporting resources
--------------------

[Learn how to use Postman to make requests](https://developer.twitter.com/en/docs/tutorials/postman-getting-started "Learn how to use Postman to make requests")

[Troubleshoot an error](https://developer.twitter.com/en/support/twitter-api "Troubleshoot an error")

[Visit the API reference page for this endpoint](https://developer.twitter.com/en/docs/twitter-api/lists/manage-lists/api-reference "Visit the API reference page for this endpoint")

Manage Lists: Standard v1.1 compared to Twitter API v2

Manage Lists: Standard v1.1 compared to Twitter API v2
------------------------------------------------------

If you have been working with the standard v1.1 [POST lists/create](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-create), [POST lists/destroy](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-destroy), and [POST lists/update](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-update) endpoints, the goal of this guide is to help you understand the similarities and differences between the standard v1.1 and Twitter API v2 manage List endpoints.

* **Similarities**
    * Authentication
* **Differences**
    * Endpoint URLs
    * App and Project requirements
    * HTTP methods
    * Rate limits
    * Request parameters

### Similarities

#### **Authentication**

Both endpoint versions support [OAuth 1.0a User Context](https://developer.twitter.com/content/developer-twitter/en/docs/authentication/oauth-1-0a). Therefore, if you were previously using one of the standard v1.1 manage Lists endpoints, you can continue using the same authentication method if you migrate to the Twitter API v2 version.

### Differences

#### Endpoint URLs

* Standard v1.1 endpoints:
    * POST https://api.twitter.com/1.1/lists/create.json  
        (Creates a List)
    * POST https://api.twitter.com/1.1/lists/destroy.json  
        (Deletes a List)
    * POST https://api.twitter.com/1.1/lists/update.json  
        (Updates a List)
* Twitter API v2 endpoint:
    * POST https://api.twitter.com/2/lists  
        (Creates a List)  
        
    * DELETE https://api.twitter.com/2/lists/:id  
        (Deletes a List)  
        
    * PUT https://api.twitter.com/2/lists/:id  
        (Updates a List)  
          
        

#### Rate limits

| **Standard v1.1** | **Twitter API v2** |
| --- | --- |
| /1.1/lists/create.json<br><br>none | /2/lists<br><br>300 requests per 15-minute window with OAuth 1.0a User Context |
| /1.1/lists/destroy.json<br><br>none | /2/lists/:id<br><br>300 requests per 15-minute window with OAuth 1.0a User Context |
| /1.1/lists/update.json<br><br>none | /2/lists/:id<br><br>300 requests per 15-minute window with OAuth 1.0a User Context |

#### App and Project requirements

The Twitter API v2 endpoints require that you use credentials from a [developer App](https://developer.twitter.com/en/docs/apps) associated with a [Project](https://developer.twitter.com/en/docs/projects) when authenticating your requests. All Twitter API v1.1 endpoints can use credentials from standalone Apps or Apps related to a project.

#### Request parameters

The following standard v1.1 request parameters have equivalents in Twitter API v2:

**Create a List**  

| **Standard** | **Twitter API v2** |
| --- | --- |
| name | name |
| mode | private |
| description | description |

**Delete/Update a List**

| **Standard** | **Twitter API v2** |
| --- | --- |
| owner\_screen\_name | No equivalent |
| owner\_id | No equivalent |
| list\_id | id  |
| slug | No equivalent |

**Please note:** Standard v1.1 parameters are passed as query parameters, whereas the Twitter API v2 parameters are passed as body parameters (for the POST endpoint) or path parameters (for the DELETE and PUT endpoints).

Next steps
----------

[Review the manage Lists API references](https://developer.twitter.com/en/docs/twitter-api/lists/manage-lists/api-reference "Review the manage Lists  API references")

API reference

API reference index
-------------------

For the complete API reference, select an endpoint from the list.  
  

### Manage Lists  

|     |     |
| --- | --- |
| **Creates a new List on behalf of an authenticated user** | `[POST /2/lists](https://developer.twitter.com/en/docs/twitter-api/lists/manage-lists/api-reference/post-lists)` |
| **Deletes a List the authenticated user owns** | `[DELETE /2/lists/:id](https://developer.twitter.com/en/docs/twitter-api/lists/manage-lists/api-reference/delete-lists-id)` |
| **Updates the metadata for a List the authenticated user owns** | `[PUT /2/lists/:id](https://developer.twitter.com/en/docs/twitter-api/lists/manage-lists/api-reference/put-lists-id)` |

POST /2/lists

POST /2/lists
=============

Enables the authenticated user to create a List.

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Try a live request ❯](https://oauth-playground.glitch.me/?id=listIdCreate&params=%28%27query%21%28%29%7Ebody%21%27%27%7Epath%21%28%29%29_) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Flists&method=post) 

### Endpoint URL

`https://api.twitter.com/2/lists`  
  

### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code "This method allows an authorized app to act on behalf of the user, as the user. It is typically used to access or post public information for a specific user, and it us useful when your app needs to be aware of the relationship between a user and what this endpoint returns. Click to learn how to authenticate with OAuth 2.0 Authorization Code with PKCE.")<br><br>[OAuth 1.0a](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) is also available for this endpoint. |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | User rate limit (User context): 300 requests per 15-minute window per each authenticated user |

### OAuth 2.0 scopes required by this endpoint

|     |
| --- |
| `tweet.read`<br><br>`users.read`<br><br>`list.read`<br><br>`list.write` |
| [Learn more about OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/twitter-api/oauth2) |

### JSON body parameters

| Name | Type | Description |
| --- | --- | --- |
| `name`  <br> Required | string | The name of the List you wish to create. |
| `description`  <br> Optional | string | Description of the List. |
| `private`  <br> Optional | boolean | Determine whether the List should be private. |

  
  

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript](#tab0)
* [Java](#tab1)

TypeScript

Java

      `(async () => {   try {     const createList = await twitterClient.lists.listIdCreate({       name: "test v2 create list",       description: "example create",       private: false,     });     console.dir(createList, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  ListCreateRequest listCreateRequest = new ListCreateRequest(); listCreateRequest.name("test v2 create list"); listCreateRequest.description("example create"); listCreateRequest._private(false);  try {     ListCreateResponse result = apiInstance.lists().listIdCreate(listCreateRequest);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling ListsApi#listIdCreate");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

### Example responses

* [Successful response](#tab0)

Successful response

      `{   "data": {     "id": "1441162269824405510",     "name": "test v2 create list"   } }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | number | The id of the newly created List. |
| `name` | string | The name of the newly created List. |

PUT /2/lists/:id

PUT /2/lists/:id
================

Enables the authenticated user to update the meta data of a specified List that they own.

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Try a live request ❯](https://oauth-playground.glitch.me/?id=listIdUpdate&params=%28%27query%21%28%29%7Ebody%21%27%27%7Epath%21%28%29%29_) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Flists%2F%7Bid%7D&method=put) 

### Endpoint URL

`https://api.twitter.com/2/lists/:id`  
  

### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code "This method allows an authorized app to act on behalf of the user, as the user. It is typically used to access or post public information for a specific user, and it us useful when your app needs to be aware of the relationship between a user and what this endpoint returns. Click to learn how to authenticate with OAuth 2.0 Authorization Code with PKCE.")<br><br>[OAuth 1.0a](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) is also available for this endpoint. |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | User rate limit (User context): 300 requests per 15-minute window per each authenticated user |

### OAuth 2.0 scopes required by this endpoint

|     |
| --- |
| `tweet.read`<br><br>`users.read`<br><br>`list.write` |
| [Learn more about OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/twitter-api/oauth2) |

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Required | string | The ID of the List to be updated. |

  
  

### JSON body parameters

| Name | Type | Description |
| --- | --- | --- |
| `description`  <br> Optional | string | Updates the description of the List. |
| `name`  <br> Optional | string | Updates the name of the List. |
| `private`  <br> Optional | boolean | Determines whether the List should be private. |

  
  

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript](#tab0)
* [Java](#tab1)

TypeScript

Java

      `(async () => {   try {     const updateList = await twitterClient.lists.listIdUpdate(       //The ID of the List to modify       1441163524802158595,       {         name: "test v2 create list",         description: "example code",         private: false,       }     );     console.dir(updateList, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  ListUpdateRequest listUpdateRequest = new ListUpdateRequest(); listUpdateRequest.name("test v2 update list"); listUpdateRequest.description("example update"); listUpdateRequest.private(false);  // String | The ID of the List to modify String id = "1441163524802158595";  try {     ListUpdateResponse result = apiInstance.lists().listIdUpdate(listUpdateRequest, id);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling ListsApi#listIdUpdate");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

### Example responses

* [Successful response](#tab0)

Successful response

      `{   "data": {     "updated": true   } }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `updated` | boolean | Indicates whether the List specified in the request has been updated. |

DELETE /2/lists/:id

DELETE /2/lists/:id
===================

Enables the authenticated user to delete a List that they own.

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Try a live request ❯](https://oauth-playground.glitch.me/?id=listIdDelete&params=%28%27query%21%28%29%7Ebody%21%27%27%7Epath%21%28%29%29_) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Flists%2F%7Bid%7D&method=delete) 

### Endpoint URL

`https://api.twitter.com/2/lists/:id`  
  

### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code "This method allows an authorized app to act on behalf of the user, as the user. It is typically used to access or post public information for a specific user, and it us useful when your app needs to be aware of the relationship between a user and what this endpoint returns. Click to learn how to authenticate with OAuth 2.0 Authorization Code with PKCE.")<br><br>[OAuth 1.0a](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) is also available for this endpoint. |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | User rate limit (User context): 300 requests per 15-minute window per each authenticated user |

### OAuth 2.0 scopes required by this endpoint

|     |
| --- |
| `tweet.read`<br><br>`users.read`<br><br>`list.write` |
| [Learn more about OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/twitter-api/oauth2) |

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Required | string | The ID of the List to be deleted. |

  
  

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript](#tab0)
* [Java](#tab1)

TypeScript

Java

      `(async () => {   try {     const deleteList = await twitterClient.lists.listIdDelete(       //The ID of the List to delete       1441162269824405510,     );     console.dir(deleteList, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  //The ID of the List to delete String id = "1441162269824405510";   try {     ListDeleteResponse result = apiInstance.lists().listIdDelete(id);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling ListsApi#listIdDelete");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

### Example responses

* [Successful response](#tab0)

Successful response

      `{   "data": {     "deleted": true   } }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `deleted` | boolean | Indicates whether the List specified in the request has been deleted. |

Introduction

Introduction
------------

List Tweets lookup has one available endpoint to retrieve Tweets from a specified List. With this endpoint, you can build solutions that enable users to customize, organize and prioritize the Tweets they see in their timeline.  

There is a rate limit of 900 requests per 15 minutes for this endpoint and the response will support querying the latest 800 Tweets for a given List.

You can use [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a), [App only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only), or [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code) to authenticate your requests to this endpoint. 

**Account setup**

To access these endpoints, you will need:

* An approved [developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info).
* To authenticate using the keys and tokens from a [developer App](https://developer.twitter.com/en/docs/apps) that is located within a [Project](https://developer.twitter.com/en/docs/projects). 

Learn more about getting access to the Twitter API v2 endpoints in our [getting started guide](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api).

[Quick start](https://developer.twitter.com/en/docs/twitter-api/lists/list-tweets/quick-start)

[Sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code)

[Run in Postman](https://t.co/twitter-api-postman)

[Try with API Explorer](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Flists%2F%7Bid%7D%2Ftweets&method=get)

Supporting resources
--------------------

[Learn how to use Postman to make requests](https://developer.twitter.com/en/docs/tutorials/postman-getting-started "Learn how to use Postman to make requests")

[Troubleshoot an error](https://developer.twitter.com/en/support/twitter-api "Troubleshoot an error")

[Visit the API reference page for this endpoint](https://developer.twitter.com/en/docs/twitter-api/lists/list-tweets/api-reference "Visit the API reference page for this endpoint")

Quick start

Getting started with the List Tweets lookup endpoint
----------------------------------------------------

This quick start guide will help you make your first request to the List Tweets lookup endpoint using Postman.

Please visit our [Twitter API v2 sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code) GitHub repository if you want to see sample code in different languages.

### Prerequisites

To complete this guide, you will need to have a set of [keys and tokens](https://developer.twitter.com/en/docs/authentication) to authenticate your request. You can generate these keys and tokens by following these steps:

* [Sign up for a developer account](https://developer.twitter.com/en/apply-for-access) and receive approval.
* Create a [Project](https://developer.twitter.com/en/docs/projects) and an associated [developer App](https://developer.twitter.com/en/docs/apps) in the developer portal.
* Navigate to your App's “Keys and tokens” page to generate the required credentials. Make sure to save all credentials in a secure location.

### Steps to build a List Tweets lookup request

#### Step one: Start with a tool or library

There are several different tools, code examples, and libraries that you can use to make a request to this endpoint, but we will use the Postman tool here to simplify the process.

To load the Twitter API v2 Postman collection into your environment, please click on the following button:

[Add Twitter API v2 to Postman](https://t.co/twitter-api-postman)

Once you have the Twitter API v2 collection loaded in Postman, navigate to the “List” folder, select another folder “List Tweets”, and then choose "List Tweets lookup".  
 

#### Step two: Authenticate your request

To properly make a request to the Twitter API, you need to verify that you have permission. To do this with this endpoint, you must authenticate your request with either [App only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only), [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code), or [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) authentication methods.

For simplicity's sake, we are going to utilize App only with this request, but if you'd like to request private [metrics](https://developer.twitter.com/en/docs/twitter-api/metrics) or Tweets, you will need to use one of the other authentication methods. 

To utilize App only, you must add your keys and tokens (specifically the [App only Access Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens), also known as the App only Bearer Token) to Postman by selecting the environment named “Twitter API v2” (in the top-right corner of Postman), and adding your keys and tokens to the "initial value" and "current value" fields (by clicking the eye icon next to the environment dropdown).

If you've done this correctly, these variables will automatically be pulled into the request's authorization tab.  
 

Step three: Identify and specify which List you would like to retrieve Tweets from  

You must specify a List that you would like to receive within the request. You can find the List ID by navigating to twitter.com and clicking on a List and then looking in the URL. For example, the following URL's List ID is 84839422.

https://twitter.com/i/lists/84839422

The target ID can be any valid List ID. In Postman, navigate to the "Params" tab, and enter your ID into the "Value" column of the id path variable. Be sure not to include any spaces before or after any ID.

|     |     |
| --- | --- |
| **Key** | **Value** |
| id  | 84839422 (The List ID) |

  
Step four: Identify and specify which fields you would like to retrieve  

If you click the "Send" button after step three, you will receive the default [Tweet object](https://developer-staging.twitter.com/content/developer-twitter/en/docs/twitter-api/object-reference/tweet) fields in your response: idand text.

If you would like to receive additional fields, you will have to specify those fields in your request with tweet.fields and/or [expansion](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/introduction/expansions) parameters.

For this exercise, we will request three additional sets of fields from different objects:

* The additional created\_at field in the primary Lists object.
    
* The full [user object](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) using the expansion parameter
    
* The additional user.created\_at field in the associated user object.
    

In Postman, navigate to the "Params" tab and add the following key:value pair to the "Query Params" table:

|     |     |     |
| --- | --- | --- |
| **Key** | **Value** | **Returned fields** |
| tweet.fields | created\_at | created\_at |
| expansions | author\_id | includes.users.id,  <br>includes.users.name,  <br>includes.users.username |
| user.fields | created\_at | includes.users.created\_at |

You should now see a similar URL next to the “Send” button:

      `https://api.twitter.com/2/lists/84839422/tweets?expansions=author_id&user.fields=created_at&max_results=1`
    

Step five: Make your request and review your response  

Once you have everything set up, hit the "Send" button, and you will receive a similar response to the following example response:

      `{   "data": [     {       "author_id": "4172587277",       "id": "1458172421115101189",       "text": "A Alemanha registrou nesta semana um recorde de novos casos de Covid-19. Segundo o governo e especialistas em Saúde, pessoas não vacinadas são responsáveis pela situação \nhttps://t.co/4POyaPwMLu"     }   ],   "includes": {     "users": [       {         "username": "MomentsBrasil",         "name": "Twitter Moments Brasil",         "created_at": "2015-11-12T16:46:02.000Z",         "id": "4172587277"       }     ]   },   "meta": {     "result_count": 1,     "next_token": "7140dibdnow9c7btw3z2vwioavpvutgzrzm9icis4ndix"   } }`
    

**Please note:** The response of this endpoint will support querying the latest 800 Tweets for a given List

Next steps
----------

[Customize your request using the API Reference](https://developer.twitter.com/en/docs/twitter-api/lists/list-tweets/api-reference "Customize your request using the API Reference")

[Reach out to the community for help](https://twittercommunity.com/ "Reach out to the community for help")

Integrate

Integration guide
-----------------

This page contains information on several tools and critical concepts that you should know as you integrate the List Tweets lookup endpoint into your system. We’ve broken the page into a couple of different sections:

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

Are you interested in getting set up with this endpoint with some code in your preferred coding language? We’ve got a handful of different code samples available that you can use as a starting point on our [Github page](https://github.com/twitterdev/Twitter-API-v2-sample-code).

#### Third-party libraries

Take advantage of one of our communities’ [third-party libraries](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries) to help you get started. You can find a library that works with the v2 endpoints by looking for the proper version tag.

### Key concepts

#### Authentication

All Twitter API v2 endpoints require you to authenticate your requests with a set of credentials, also known as keys and tokens. You can use either OAuth 1.0a User Context, App only, or OAuth 2.0 Authorization Code with PKCE to authenticate your requests to this endpoint. 

[OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a), which means that you must use a set of API Keys and user Access Tokens to make a successful request. The access tokens must be associated with the user that you are making the request on behalf of. If you would like to generate a set of Access Tokens for another user, they must authorize your App using the [3-legged OAuth flow](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens).

Please note that OAuth 1.0a can be difficult to use. If you are not familiar with this authentication method, we recommend that you use a [library](https://developer.twitter.com/content/en/docs/twitter-api/tools-and-libraries), use a tool like Postman, or use either OAuth 2.0 or App only to authenticate your requests.

[OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code) allows for greater control over an application’s scope, and authorization flows across multiple devices. OAuth 2.0 allows you to pick specific fine-grained scopes which give you specific permissions on behalf of a user. 

To enable OAuth 2.0 in your App, you must enable it in your’s App’s authentication settings found in the App settings section of the developer portal.

[App only](https://developer.twitter.com/en/docs/authentication/oauth-2-0) just requires that you pass an [App only Access Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens) with your request. You can either generate an App only Access Token directly within a developer App, or generate one using the [POST oauth2/token](https://developer.twitter.com/en/docs/authentication/api-reference/token) endpoint.

#### Developer portal, Projects, and developer Apps

To retrieve a set of authentication credentials that will work with the Twitter API v2 endpoints, you must [sign up for a developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info), set up a [Project](https://developer.twitter.com/en/docs/projects) within that account, and created a [developer App](https://developer.twitter.com/en/docs/apps) within that Project. You can then find your keys and tokens within your developer App.  
 

#### Rate limits

Every day, many thousands of developers make requests to the Twitter API. To help manage the sheer volume of these requests, [rate limits](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/rate-limits) are placed on each endpoint that limits the number of requests you can make on behalf of your app or on behalf of an authenticated user. 

This endpoint is rate limited at both the App-level and the user-level. The app rate limit means that you, the developer, can only make a certain number of requests to this endpoint over a given period of time from any given App (assumed by using either the API Key and API Secret Key, or the Bearer Token). The user rate limit means that the authenticated user that you are making the request on behalf of can only perform a List Tweet lookup a certain number of times across any developer App.

The chart below shows the rate limits for each endpoint.

|     |     |     |
| --- | --- | --- |
| **Endpoint** | **HTTP method** | **Rate limit** |
| /2/lists/:id/tweets | GET | 900 requests per 15 minutes |

Fields and expansions  

The Twitter API v2 GET endpoint allows users to select exactly which data they want to return from the API using a set of tools called `fields` and `expansions`. The `expansions` parameter allows you to expand objects referenced in the payload. For example, looking up List Tweets allows you to pull the following [expansions](https://developer.twitter.com/en/docs/twitter-api/expansions):

* `author_id`
    

The `fields` parameter allows you to select exactly which [fields](https://developer.twitter.com/en/docs/twitter-api/fields) within the different data objects you would like to receive. This endpoint delivers Tweet objects primarily. By default, the Tweet object returns the `id`, and `text` fields. To receive additional fields such as `tweet.created_at` or `tweet.lang`, you will have to specifically request those using a fields parameter. 

We’ve added a guide on using [fields and expansions](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/using-fields-and-expansions) together to our [Twitter API v2 data dictionary](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/introduction).

 The chart below shows the field and expansions available for the lookup endpoint:

|     |     |     |
| --- | --- | --- |
| **Endpoint** | **Fields** | **Expansions** |
| /2/lists/:id/tweets | `tweet.fields`<br><br>`user.fields` | `author_id` |

Pagination  

Looking up List Tweets can return a lot of data. To ensure we are returning consistent, high-performing results at any given time, we use pagination. Pagination is a feature in Twitter API v2 endpoints that return more results than can be returned in a single response. When that happens, the data is returned in a series of 'pages'. Learn more about how to [paginate through results.](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/pagination)

Next steps
----------

[Visit the API reference page for these endpoint](https://developer.twitter.com/en/docs/twitter-api/lists/list-tweets/api-reference "Visit the API reference page for these endpoint")

Migrate

Comparing Twitter API’s List Tweets lookup endpoints
----------------------------------------------------

The v2 List Tweets lookup endpoint will replace the standard v1.1 [GET lists/statuses](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-statuses). If you have code, apps, or tools that use this version of the endpoint, and are considering migrating to the newer Twitter API v2 endpoint, then this set of guides is for you.

The following tables compare the standard v1.1 and Twitter API v2 List endpoints:  

**List Lookup by ID**

|     |     |     |
| --- | --- | --- |
| Description | Standard v1.1 | Twitter API v2 |
| HTTP methods supported | `GET` | `GET` |
| Host domain | `https://api.twitter.com` | `https://api.twitter.com` |
| Endpoint path | `/1.1/lists/statuses.json` | `/2/lists/:id/tweets` |
| [Authentication](https://developer.twitter.com/content/developer-twitter/en/docs/authentication) | OAuth 1.0a User Context<br><br>App only | OAuth 1.0a User Context<br><br>OAuth 2.0 Authorization Code with PKCE<br><br>App only |
| Default request [rate limits](https://developer.twitter.com/content/developer-twitter/en/docs/rate-limits) | 900 requests per 15 min with OAuth 1.0a<br><br>900 requests per 15min with App only | 900 requests per 15 min with OAuth 1.0a<br><br>900 requests per 15 min with OAuth 2.0<br><br>900 requests per 15 min with App only |

To access the Twitter API v2 endpoints, you must [sign up for a developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info). When authenticating, you must use keys and tokens from a [developer App](https://developer.twitter.com/en/docs/apps) that is located within a [Project](https://developer.twitter.com/en/docs/projects). 

Learn more about getting access to the Twitter API v2 endpoints in our [getting started](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api) page.

[Quick start](https://developer.twitter.com/en/docs/twitter-api/lists/list-tweets/quick-start)

[Sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code)

[Run in Postman](https://t.co/twitter-api-postman)

Supporting resources
--------------------

[Learn how to use Postman to make requests](https://developer.twitter.com/en/docs/tutorials/postman-getting-started "Learn how to use Postman to make requests")

[Troubleshoot an error](https://developer.twitter.com/en/support/twitter-api "Troubleshoot an error")

[Visit the API reference page for this endpoint](https://developer.twitter.com/en/docs/twitter-api/lists/list-tweets/api-reference "Visit the API reference page for this endpoint")

List Tweets lookup: Standard v1.1 compared to Twitter API v2

List Tweets lookup: Standard v1.1 compared to Twitter API v2
------------------------------------------------------------

If you have been working with the standard v1.1 [GET lists/statuses](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-statuses) endpoint, the goal of this guide is to help you understand the similarities and differences between the standard v1.1 and Twitter API v2 endpoints.

* **Similarities**
    * Authentication methods
    * Rate limits
* **Differences**
    * Endpoint URLs
    * App and Project requirements
    * Data objects per request limits
    * Response data formats
    * Request parameters

### Similarities

#### **Authentication**

Both endpoint versions support both [OAuth 1.0a User Context](https://developer.twitter.com/content/developer-twitter/en/docs/authentication/oauth-1-0a) and [App only](https://developer.twitter.com/content/developer-twitter/en/docs/authentication/oauth-2-0). Therefore, if you were previously using one of the standard v1.1 List Tweets lookup endpoints, you can continue using the same authentication method if you migrate to the Twitter API v2 version.

Depending on your authentication library/package of choice, App only authentication is probably the easiest way to get started and can be set with a simple request header. To learn how to generate an App only Access Token, see [this App only guide](https://developer.twitter.com/en/docs/basics/authentication/overview/application-only).

**Rate limits**

|     |     |
| --- | --- |
| **Standard v1.1** | **Twitter API v2** |
| /1.1/lists/statuses.json<br><br>900 requests per 15-minute window with OAuth 1.0a User Context<br><br>900 requests per 15-minute window with App only | /2/lists/:id/tweets<br><br>900 requests per 15-minute window with OAuth 1.0a User Context<br><br>900 requests per 15-minute window with OAuth 2.0 Authorization Code with PKCE<br><br>900 requests per 15-minute window with App only |

### Differences

#### Endpoint URLs

* Standard v1.1 endpoints:
    * GET https://api.twitter.com/1.1/lists/statuses.json  
        (Lookup Tweets from a specified List)
* Twitter API v2 endpoint:
    * GET https://api.twitter.com/2/lists/:id/tweets  
        (Lookup Tweets from a specified List)

#### App and Project requirements

The Twitter API v2 endpoints require that you use credentials from a [developer App](https://developer.twitter.com/en/docs/apps) that is associated with a [Project](https://developer.twitter.com/en/docs/projects) when authenticating your requests. All Twitter API v1.1 endpoints can use credentials from standalone Apps or Apps associated with a project.

####   
  
Data objects per request limits

The standard v1.1 /lists/statuses endpoint allows you to return up to 5000 Tweets per request. The new v2 endpoints allow you to return up to 100 Tweets per request. By default, 100 user objects will be returned, to change the number of results you will need to pass a query parameter max\_results= with a number between 1-100; you can then pass the next\_token returned in the response payload to the pagination\_token query parameter in your next request.

**Response data format**

One of the biggest differences between standard v1.1 and Twitter API v2 endpoint versions is how you select which fields return in your payload.

For the standard endpoints, you receive many of the response fields by default and then have the option to use parameters to identify which additional fields or sets of fields should return in the payload.

The Twitter API v2 version only delivers the Tweet id and text fields by default. To request any additional fields or objects, you will need to use the [fields](https://developer.twitter.com/en/docs/twitter-api/fields/content/developer-twitter/en/docs/twitter-api/fields) and [expansions](https://developer.twitter.com/en/docs/twitter-api/fields/content/developer-twitter/en/docs/twitter-api/expansions) parameters. Any Tweet fields that you request from this endpoint will return in the primary Tweet object. Any expanded object fields will return an includes object within your response. You can then match any expanded objects back to the primary Tweet object by matching the IDs from the primary object and in expanded objects. 

Here are examples of possible Tweet fields and expansions:

* attachments
    
* author\_id
    
* context\_annotations
    
* created\_at
    
* geo
    
* lang
    

|     |     |
| --- | --- |
| **Endpoint** | **Expansion** |
| /2/lists/:id/tweets | author\_id |

We encourage you to read more about these new parameters in their respective guides, or by reading our guide on [how to use fields and expansions](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/using-fields-and-expansions). 

We have also put together a [data format migration guide](https://developer.twitter.com/en/docs/twitter-api/migrate/data-formats/standard-v1-1-to-v2) that can help you map standard v1.1 fields to the newer v2 fields. This guide will also provide you the specific expansion and field parameter that you will need to pass with your v2 request to return specific fields. 

In addition to the changes in how you request certain fields, Twitter API v2 is also introducing new JSON designs for the objects returned by the APIs, including [Tweet](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) and [user](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) objects.

* At the JSON root level, the standard endpoints return Tweet objects in a statuses array, while Twitter API v2 returns a data array. 
    
* Instead of referring to Retweeted and Quoted "statuses", Twitter API v2 JSON refers to Retweeted and Quoted Tweets. Many legacy and deprecated fields, such as contributors and user.translator\_type are being removed. 
    
* Instead of using both favorites (in Tweet object) and favourites (in user object), Twitter API v2 uses the term like. 
    
* Twitter is adopting the convention that JSON values with no value (for example, null) are not written to the payload. Tweet and user attributes are only included if they have non-null values.  
     
    

#### Request parameters

The following standard v1.1 request parameters have equivalents in Twitter API v2:

|     |     |
| --- | --- |
| Standard v1.1 | Twitter API v2 |
| list\_id | id  |
| slug | No equivalent |
| owner\_screen\_name | No equivalent |
| owner\_id | Requested with expansions parameter with value of author\_id |
| since\_id | No equivalent |
| max\_id | No equivalent |
| include\_entities | Requested with tweet.fields parameter with value of entities |
| include\_rts | No equivalent |
| count | max\_results |

Next steps
----------

[Review the List lookup API references](https://developer.twitter.com/en/docs/twitter-api/lists/list-tweets/api-reference "Review the List lookup API references")

API reference

API reference index
-------------------

For the complete API reference, click on the endpoint link below.  
  

|     |     |
| --- | --- |
| **Lookup Tweets from a specified List** | `[GET /2/lists/:id/tweets](https://developer.twitter.com/en/docs/twitter-api/lists/list-tweets/api-reference/get-lists-id-tweets)` |

GET /2/lists/:id/tweets

GET /2/lists/:id/tweets
=======================

Returns a list of Tweets from the specified List.

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Try a live request ❯](https://oauth-playground.glitch.me/?id=listsIdTweets&params=%28%27query%21%28%29%7Ebody%21%27%27%7Epath%21%28%29%29_) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Flists%2F%7Bid%7D%2Ftweets&method=get) 

### Endpoint URL

`https://api.twitter.com/2/lists/:id/tweets`  
  

### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 1.0a](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) is also available for this endpoint.<br><br>[OAuth 2.0 App-only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only "Use this method to obtain information in the context of an unauthenticated public user. This method is for developers that just need read-only access to public information. Click to learn how to obtain an OAuth 2.0 App Access Token.")<br><br>[OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code "This method allows an authorized app to act on behalf of the user, as the user. It is typically used to access or post public information for a specific user, and it us useful when your app needs to be aware of the relationship between a user and what this endpoint returns. Click to learn how to authenticate with OAuth 2.0 Authorization Code with PKCE.") |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | App rate limit (Application-only): 900 requests per 15-minute window shared among all users of your app<br><br>User rate limit (User context): 900 requests per 15-minute window per each authenticated user |

### OAuth 2.0 scopes required by this endpoint

|     |
| --- |
| `tweet.read`<br><br>`users.read`<br><br>`list.read` |
| [Learn more about OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/twitter-api/oauth2) |

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Required | string | The ID of the List whose Tweets you would like to retrieve. |

  
  

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| `expansions`  <br> Optional | enum (`attachments.poll_ids`, `attachments.media_keys`, `author_id`, `edit_history_tweet_ids`, `entities.mentions.username`, `geo.place_id`, `in_reply_to_user_id`, `referenced_tweets.id`, `referenced_tweets.id.author_id`) | [Expansions](https://developer.twitter.com/en/docs/twitter-api/expansions) enable you to request additional data objects that relate to the originally returned users. The ID that represents the expanded data object will be included directly in the user data object, but the expanded object metadata will be returned within the `includes` response object, and will also include the ID so that you can match this data object to the original Tweet object. At this time, the only expansion available to endpoints that primarily return user objects is `expansions=pinned_tweet_id`. You will find the expanded Tweet data object living in the `includes` response object. |
| `max_results`  <br> Optional | integer | The maximum number of results to be returned per page. This can be a number between 1 and 100. By default, each page will return 100 results. |
| `media.fields`  <br> Optional | enum (`duration_ms`, `height`, `media_key`, `preview_image_url`, `type`, `url`, `width`, `public_metrics`, `non_public_metrics`, `organic_metrics`, `promoted_metrics`, `alt_text`, `variants`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [media fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/media) will deliver in each returned Tweet. Specify the desired fields in a comma-separated list without spaces between commas and fields. The Tweet will only return media fields if the Tweet contains media and if you've also included the `expansions=attachments.media_keys` query parameter in your request. While the media ID will be located in the Tweet object, you will find this ID and all additional media fields in the `includes` data object. |
| `pagination_token`  <br> Optional | string | Used to request the next page of results if all results weren't returned with the latest request, or to go back to the previous page of results. To return the next page, pass the next\_token returned in your previous response. To go back one page, pass the previous\_token returned in your previous response. |
| `place.fields`  <br> Optional | enum (`contained_within`, `country`, `country_code`, `full_name`, `geo`, `id`, `name`, `place_type`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [place fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/place) will deliver in each returned Tweet. Specify the desired fields in a comma-separated list without spaces between commas and fields. The Tweet will only return place fields if the Tweet contains a place and if you've also included the `expansions=geo.place_id` query parameter in your request. While the place ID will be located in the Tweet object, you will find this ID and all additional place fields in the `includes` data object. |
| `poll.fields`  <br> Optional | enum (`duration_minutes`, `end_datetime`, `id`, `options`, `voting_status`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [poll fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/poll) will deliver in each returned Tweet. Specify the desired fields in a comma-separated list without spaces between commas and fields. The Tweet will only return poll fields if the Tweet contains a poll and if you've also included the `expansions=attachments.poll_ids` query parameter in your request. While the poll ID will be located in the Tweet object, you will find this ID and all additional poll fields in the `includes` data object. |
| `tweet.fields`  <br> Optional | enum (`attachments`, `author_id`, `context_annotations`, `conversation_id`, `created_at`, `edit_controls`, `entities`, `geo`, `id`, `in_reply_to_user_id`, `lang`, `non_public_metrics`, `public_metrics`, `organic_metrics`, `promoted_metrics`, `possibly_sensitive`, `referenced_tweets`, `reply_settings`, `source`, `text`, `withheld`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [Tweet fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) will deliver in each returned pinned Tweet. Specify the desired fields in a comma-separated list without spaces between commas and fields. The Tweet fields will only return if the user has a pinned Tweet and if you've also included the `expansions=pinned_tweet_id` query parameter in your request. While the referenced Tweet ID will be located in the original Tweet object, you will find this ID and all additional Tweet fields in the `includes` data object. |
| `user.fields`  <br> Optional | enum (`created_at`, `description`, `entities`, `id`, `location`, `most_recent_tweet_id`, `name`, `pinned_tweet_id`, `profile_image_url`, `protected`, `public_metrics`, `url`, `username`, `verified`, `withheld`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [user fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) will deliver with the users object. Specify the desired fields in a comma-separated list without spaces between commas and fields. These specified user fields will display directly in the user data objects. |

  
  

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript (Default fields)](#tab0)
* [TypeScript (Optional fields)](#tab1)
* [Java (Default fields)](#tab2)
* [Java (Optional fields)](#tab3)

TypeScript (Default fields)

TypeScript (Optional fields)

Java (Default fields)

Java (Optional fields)

      `(async () => {   try {     const getListTweets = await twitterClient.tweets.listsIdTweets(       //The ID of the List to list Tweets of       84839422     );     console.dir(getListTweets, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `(async () => {   try {     const getListTweets = await twitterClient.tweets.listsIdTweets(       //The ID of the List to list Tweets of       84839422,       {         //A comma separated list of fields to expand         expansions: ["author_id"],          //A comma separated list of User fields to display         "user.fields": ["verified"],       }     );     console.dir(getListTweets, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  // String | The ID of the List to list Tweets of String id = "84839422";  try {     ListsIdTweetsResponse result = apiInstance.tweets().listsIdTweets(id, null, null, null, null, null, null, null, null);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling TweetsApi#listsIdTweets");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

      `// Set the params values // For full list of params visit - https://github.com/twitterdev/twitter-api-java-sdk/blob/main/docs/TweetsApi.md#listsIdTweets  // String | The ID of the List to list Tweets of String id = "84839422";  // Set<String> | A comma separated list of fields to expand Set<String> expansions = new HashSet<>(Arrays.asList("author_id"));  // Set<String> | A comma separated list of User fields to display Set<String> userFields = new HashSet<>(Arrays.asList("verified"));  try {     ListsIdTweetsResponse result = apiInstance.tweets().listsIdTweets(id, null, null, expansions, null, userFields, null, null, null);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling TweetsApi#listsIdTweets");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

### Example responses

* [Default fields](#tab0)
* [Optional fields](#tab1)

Default fields

Optional fields

      `{   "data": [     {       "id": "1067094924124872705",       "text": "Just getting started with Twitter APIs? Find out what you need in order to build an app. Watch this video! https://t.co/Hg8nkfoizN"     }   ],   "meta": {     "result_count": 1   } }`
    

      `{   "data": {     "author_id": "2244994945",     "created_at": "2018-11-26T16:37:10.000Z",     "text": "Just getting started with Twitter APIs? Find out what you need in order to build an app. Watch this video! https://t.co/Hg8nkfoizN",     "id": "1067094924124872705"   },   "includes": {     "users": [       {         "verified": true,         "username": "TwitterDev",         "id": "2244994945",         "name": "Twitter Dev"       }     ]   },   "meta": {     "result_count": 1   } }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Default | string | Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. |
| `text`  <br> Default | string | The content of the Tweet.  <br>  <br>To return this field, add `tweet.fields=text` in the request's query parameter. |
| `created_at` | date (ISO 8601) | Creation time of the Tweet.  <br>  <br>To return this field, add `tweet.fields=created_at` in the request's query parameter. |
| `author_id` | string | Unique identifier of this user. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers.  <br>  <br>You can obtain the expanded object in `includes.users` by adding `expansions=author_id` in the request's query parameter. |
| `edit_history_tweet_ids`  <br> Default | array | Unique identifiers indicating all versions of an edited Tweet. For Tweets with no edits, there will be one ID. For Tweets with an edit history, there will be multiple IDs, arranged in ascending order reflecting the order of edit, with the most recent version in the last position of the array. |
| `edit_controls` | object | Indicates if a Tweet is eligible for edit, how long it is editable for, and the number of remaining edits.  <br>  <br>The `is_edit_eligible` field indicates if a Tweet was eligible for edit when published. This field is not dynamic and won't toggle from True to False when a Tweet reaches its editable time limit, or maximum number of edits. The following Tweet features will cause this field to be false:<br><br>* Tweet is promoted<br>* Tweet has a poll<br>* Tweet is a non-self-thread reply<br>* Tweet is a Retweet (note that Quote Tweets are eligible for edit)<br>* Tweet is nullcast<br>* Community Tweet<br>* Superfollow Tweet<br>* Collaborative Tweet<br><br>`{     "edit_controls": {      "is_edit_eligible": true,      "editable_until": "2022-08-21 09:35:20.311",      "edits_remaining": 4    }   }   `Editable Tweets can be edited for the first 30 minutes after creation and can be edited up to five times.  <br>  <br>To return this field, add `tweet.fields=edit_controls` in the request's query parameter. |
| `conversation_id` | string | The Tweet ID of the original Tweet of the conversation (which includes direct replies, replies of replies).  <br>  <br>To return this field, add `tweet.fields=conversation_id` in the request's query parameter. |
| `note_tweet` | string | Information about Tweets with more than 280 characters.  <br>  <br>To return this field, add `tweet.fields=note_tweet` in the request's query parameter. |
| `in_reply_to_user_id` | string | If this Tweet is a Reply, indicates the user ID of the parent Tweet's author. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers.  <br>  <br>You can obtain the expanded object in `includes.users` by adding `expansions=in_reply_to_user_id` in the request's query parameter. |
| `referenced_tweets` | array | A list of Tweets this Tweet refers to. For example, if the parent Tweet is a Retweet, a Retweet with comment (also known as Quoted Tweet) or a Reply, it will include the related Tweet referenced to by its parent.  <br>  <br>To return this field, add `tweet.fields=referenced_tweets` in the request's query parameter. |
| `referenced_tweets.type` | enum (`retweeted`, `quoted`, `replied_to`) | Indicates the type of relationship between this Tweet and the Tweet returned in the response: `retweeted` (this Tweet is a Retweet), `quoted` (a Retweet with comment, also known as Quoted Tweet), or `replied_to` (this Tweet is a reply). |
| `referenced_tweets.id` | string | The unique identifier of the referenced Tweet.  <br>  <br>You can obtain the expanded object in `includes.tweets` by adding `expansions=referenced_tweets.id` in the request's query parameter. |
| `attachments` | object | Specifies the type of attachments (if any) present in this Tweet.  <br>  <br>To return this field, add `tweet.fields=attachments` in the request's query parameter. |
| `attachments.media_keys` | array | List of unique identifiers of media attached to this Tweet. These identifiers use the same media key format as those returned by the [Media Library](https://developer.twitter.com/en/docs/ads/creatives/guides/media-library).  <br>  <br>You can obtain the expanded object in `includes.media` by adding `expansions=attachments.media_keys` in the request's query parameter. |
| `attachments.poll_ids` | array | List of unique identifiers of polls present in the Tweets returned. These are returned as a string in order to avoid complications with languages and tools that cannot handle large integers.  <br>  <br>You can obtain the expanded object in `includes.polls` by adding `expansions=attachments.polls_ids` in the request's query parameter. |
| `geo` | object | Contains details about the location tagged by the user in this Tweet, if they specified one.  <br>  <br>To return this field, add `tweet.fields=geo` in the request's query parameter. |
| `geo.coordinates` | object | Contains details about the coordinates of the location tagged by the user in this Tweet, if they specified one.  <br>  <br>To return this field, add `tweet.fields=geo.coordinates` in the request's query parameter. |
| `geo.coordinates.type` | string | Describes the type of coordinate. The only value supported at present is `Point`. |
| `geo.coordinates.coordinates` | array | A pair of decimal values representing the precise location of the user (latitude, longitude). This value be `null` unless the user explicitly shared their precise location. |
| `geo.place_id` | string | The unique identifier of the place, if this is a point of interest tagged in the Tweet.  <br>  <br>You can obtain the expanded object in `includes.places` by adding `expansions=geo.place_id` in the request's query parameter. |
| `context_annotations` | array | Contains context annotations for the Tweet.  <br>  <br>To return this field, add `tweet.fields=context_annotations` in the request's query parameter. |
| `context_annotations.domain` | object | Contains elements which identify detailed information regarding the domain classification based on Tweet text. |
| `context_annotations.domain.id` | string | Contains the numeric value of the domain. |
| `context_annotations.domain.name` | string | Domain name based on the Tweet text. |
| `context_annotations.domain.description` | string | Long form description of domain classification. |
| `context_annotations.entity` | object | Contains elements which identify detailed information regarding the domain classification bases on Tweet text. |
| `context_annotations.entity.id` | string | Unique value which correlates to an explicitly mentioned Person, Place, Product or Organization |
| `context_annotations.entity.name` | string | Name or reference of entity referenced in the Tweet. |
| `context_annotations.entity.description` | string | Additional information regarding referenced entity. |
| `entities` | object | Contains details about text that has a special meaning in a Tweet.  <br>  <br>To return this field, add `tweet.fields=entities` in the request's query parameter. |
| `entities.annotations` | array | Contains details about annotations relative to the text within a Tweet. |
| `entities.annotations.start` | integer | The start position (zero-based) of the text used to annotate the Tweet. All start indices are inclusive. |
| `entities.annotations.end` | integer | The end position (zero based) of the text used to annotate the Tweet. While all other end indices are exclusive, this one is inclusive. |
| `entities.annotations.probability` | number | The confidence score for the annotation as it correlates to the Tweet text. |
| `entities.annotations.type` | string | The description of the type of entity identified when the Tweet text was interpreted. |
| `entities.annotations.normalized_text` | string | The text used to determine the annotation type. |
| `entities.urls` | array | Contains details about text recognized as a URL. |
| `entities.urls.start` | integer | The start position (zero-based) of the recognized URL within the Tweet. All start indices are inclusive. |
| `entities.urls.end` | integer | The end position (zero-based) of the recognized URL within the Tweet. This end index is exclusive. |
| `entities.urls.url` | string | The URL in the format tweeted by the user. |
| `entities.urls.expanded_url` | string | The fully resolved URL. |
| `entities.urls.display_url` | string | The URL as displayed in the Twitter client. |
| `entities.urls.unwound_url` | string | The full destination URL. |
| `entities.hashtags` | array | Contains details about text recognized as a Hashtag. |
| `entities.hashtags.start` | integer | The start position (zero-based) of the recognized Hashtag within the Tweet. All start indices are inclusive. |
| `entities.hashtags.end` | integer | The end position (zero-based) of the recognized Hashtag within the Tweet. |
| `entities.hashtags.tag` | string | The text of the Hashtag. |
| `entities.mentions` | array | Contains details about text recognized as a user mention. |
| `entities.mentions.start` | integer | The start position (zero-based) of the recognized user mention within the Tweet. All start indices are inclusive. |
| `entities.mentions.end` | integer | The end position (zero-based) of the recognized user mention within the Tweet. |
| `entities.mentions.username` | string | The part of text recognized as a user mention.  <br>  <br>You can obtain the expanded object in `includes.users` by adding `expansions=entities.mentions.username` in the request's query parameter. |
| `entities.cashtags` | array | Contains details about text recognized as a Cashtag. |
| `entities.cashtags.start` | integer | The start position (zero-based) of the recognized Cashtag within the Tweet. All start indices are inclusive. |
| `entities.cashtags.end` | integer | The end position (zero-based) of the recognized Cashtag within the Tweet. |
| `entities.cashtags.tag` | string | The text of the Cashtag. |
| `withheld` | object | Contains withholding details for [withheld content](https://help.twitter.com/en/rules-and-policies/tweet-withheld-by-country).  <br>  <br>To return this field, add `tweet.fields=withheld` in the request's query parameter. |
| `withheld.copyright` | boolean | Indicates if the content is being withheld for on the basis of copyright infringement. |
| `withheld.country_codes` | array | Provides a list of countries where this content is not available. |
| `withheld.scope` | enum (`tweet`, `user`) | Indicates whether the content being withheld is a Tweet or a user. |
| `note_tweet` | object | Information for Tweets longer than 280 characters.  <br>  <br>To return this field, add `tweet.fields=note_tweet` in the request's query parameter. |
| `note_tweet.text` | string | The text for Tweets longer than 280 characters. |
| `note_tweet.entities` | object | Contains details about text that has a special meaning in a Tweet. |
| `note_tweet.entities.urls` | array | Contains details about text recognized as a URL. |
| `note_tweet.entities.mentions` | array | Contains details about text recognized as a user mention. |
| `note_tweet.entities.hashtags` | array | Contains details about text recognized as a Hashtag. |
| `note_tweet.entities.cashtags` | array | Contains details about text recognized as a Cashtag. |
| `public_metrics` | object | Engagement metrics for the Tweet at the time of the request.  <br>  <br>To return this field, add `tweet.fields=public_metrics` in the request's query parameter. |
| `public_metrics.retweet_count` | integer | Number of times this Tweet has been Retweeted. |
| `public_metrics.reply_count` | integer | Number of Replies of this Tweet. |
| `public_metrics.like_count` | integer | Number of Likes of this Tweet. |
| `public_metrics.quote_count` | integer | Number of times this Tweet has been Retweeted with a comment (also known as Quote). |
| `public_metrics.impression_count` | integer | Number of times this Tweet has been viewed. |
| `public_metrics.bookmark_count` | integer | Number of times this Tweet has been bookmarked. |
| `non_public_metrics` | object | Non-public engagement metrics for the Tweet at the time of the request. This is a private metric, and requires the use of OAuth 2.0 User Context authentication.  <br>  <br>To return this field, add `tweet.fields=non_public_metrics` in the request's query parameter. |
| `non_public_metrics.impression_count` | integer | Number of times the Tweet has been viewed. This is a private metric, and requires the use of OAuth 2.0 User Context authentication. |
| `non_public_metrics.url_link_clicks` | integer | Number of times a user clicks on a URL link or URL preview card in a Tweet. This is a private metric, and requires the use of OAuth 2.0 User Context authentication. |
| `non_public_metrics.user_profile_clicks` | integer | Number of times a user clicks the following portions of a Tweet - display name, user name, profile picture. This is a private metric, and requires the use of OAuth 2.0 User Context authentication. |
| `organic_metrics` | object | Organic engagement metrics for the Tweet at the time of the request. Requires user context authentication.  <br>  <br>To return this field, add `tweet.fields=organic_metrics` in the request's query parameter. |
| `organic_metrics.impression_count` | integer | Number of times the Tweet has been viewed organically. This is a private metric, and requires the use of OAuth 2.0 User Context authentication. |
| `organic_metrics.url_link_clicks` | integer | Number of times a user clicks on a URL link or URL preview card in a Tweet organically. This is a private metric, and requires the use of OAuth 2.0 User Context authentication. |
| `organic_metrics.user_profile_clicks` | integer | Number of times a user clicks the following portions of a Tweet organically - display name, user name, profile picture. This is a private metric, and requires the use of OAuth 2.0 User Context authentication. |
| `organic_metrics.retweet_count` | integer | Number of times the Tweet has been Retweeted organically. |
| `organic_metrics.reply_count` | integer | Number of replies the Tweet has received organically. |
| `organic_metrics.like_count` | integer | Number of likes the Tweet has received organically. |
| `promoted_metrics` | object | Engagement metrics for the Tweet at the time of the request in a promoted context. Requires user context authentication.  <br>  <br>To return this field, add `tweet.fields=promoted_metrics` in the request's query parameter. |
| `promoted_metrics.impression_count` | integer | Number of times the Tweet has been viewed when that Tweet is being promoted. This is a private metric, and requires the use of OAuth 2.0 User Context authentication. |
| `promoted_metrics.url_link_clicks` | integer | Number of times a user clicks on a URL link or URL preview card in a Tweet when it is being promoted. This is a private metric, and requires the use of OAuth 2.0 User Context authentication. |
| `promoted_metrics.user_profile_clicks` | integer | Number of times a user clicks the following portions of a Tweet when it is being promoted - display name, user name, profile picture. This is a private metric, and requires the use of OAuth 2.0 User Context authentication. |
| `promoted_metrics.retweet_count` | integer | Number of times this Tweet has been Retweeted when that Tweet is being promoted. |
| `promoted_metrics.reply_count` | integer | Number of Replies to this Tweet when that Tweet is being promoted. |
| `promoted_metrics.like_count` | integer | Number of Likes of this Tweet when that Tweet is being promoted. |
| `possibly_sensitive` | boolean | Indicates if this Tweet contains URLs marked as sensitive, for example content suitable for mature audiences.  <br>  <br>To return this field, add `tweet.fields=possibly_sensitive` in the request's query parameter. |
| `lang` | string | Language of the Tweet, if detected by Twitter. Returned as a BCP47 language tag.  <br>  <br>To return this field, add `tweet.fields=lang` in the request's query parameter. |
| `reply_settings` | string | Shows who can reply to this Tweet. Fields returned are `everyone`, `mentionedUsers`, and `following`.  <br>  <br>To return this field, add `tweet.fields=reply_settings` in the request's query parameter. |
| `source` | string | The name of the app the user Tweeted from.  <br>  <br>To return this field, add `tweet.fields=source` in the request's query parameter. |
| `includes` | object | If you include an `[expansion](https://developer.twitter.com/en/docs/twitter-api/expansions)` parameter, the referenced objects will be returned if available. |
| `includes.tweets` | array | When including the `expansions=referenced_tweets.id` parameter, this includes a list of referenced Retweets, Quoted Tweets, or replies in the form of [Tweet objects](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) with their default fields and any additional fields requested using the `tweet.fields` parameter, assuming there is a referenced Tweet present in the returned Tweet(s). |
| `includes.users` | array | When including the `expansions=author_id` parameter, this includes a list of referenced Tweet authors in the form of [user objects](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) with their default fields and any additional fields requested using the `user.fields` parameter. |
| `errors` | object | Contains details about errors that affected any of the requested Tweets. See [Status codes and error messages](https://developer.twitter.com/en/support/twitter-api/error-troubleshooting) for more details. |
| `meta`  <br> Default | object | This object contains information about the number of users returned in the current request, and pagination details. |
| `meta.result_count`  <br> Default | integer | The number of users returned in this request. Note that this number may be lower than what was specified in the `max_results` query parameter. |
| `meta.previous_token` | string | Pagination token for the previous page of results. This value is returned when there are multiple pages of results, as the current request may only return a subset of results. To go back to the previous page, passing the value from this field in the `pagination_token` query parameter. When this field is not returned in the response, it means you are on the first page of results. |
| `meta.next_token` | string | Pagination token for the next page of results. This value is returned when there are multiple pages of results, as the current request may only return a subset of results. To retrieve the full list, keep passing the value from this field in the `pagination_token` query parameter. When this field is not returned in the response, it means you've reached the last page of results, and that there are no further pages. |

Introduction

Introduction
------------

### List members lookup

Members lookup group has two available endpoints. You are able to retrieve details on members of a specified List and see which Lists a user is a member of. These endpoints can be used to enable people to curate and organize new Lists based on the membership information.

There is a rate limit of 900 requests per 15 minutes when looking up member details and a limit of 75 requests per 15 minutes when looking up user memberships.

You can use [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a), [App only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only), or [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code) to authenticate your requests to this endpoint.   
 

### Manage List members

The manage List members endpoints allow you to add and remove members to a List on behalf of an authenticated user. For these endpoints, there are two methods available: POST and DELETE. The POST method allows you to add a member to a List, and the DELETE method allows you to remove a member from a List. There is a user rate limit of 300 requests per 15 minutes for both endpoints.

Note that Lists cannot have more than 5,000 members.

Since you are making requests on behalf of a user with the these endpoints, you must authenticate them with either [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) or [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code), and use the user Access Tokens associated with a user that has authorized your App, which can be generated using the [3-legged OAuth flow](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens) (OAuth 1.0a) or the [Authorization Code with PKCE grant flow](https://developer.twitter.com/en/docs/authentication/oauth-2-0/user-access-token) (OAuth 2.0).

**Account setup**

To access these endpoints, you will need:

* An approved [developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info).
* To authenticate using the keys and tokens from a [developer App](https://developer.twitter.com/en/docs/apps) that is located within a [Project](https://developer.twitter.com/en/docs/projects). 

Learn more about getting access to the Twitter API v2 endpoints in our [getting started guide](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api).

[Quick start](https://developer.twitter.com/en/docs/twitter-api/lists/list-members/quick-start)

[Sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code)

[Run in Postman](https://t.co/twitter-api-postman)

[Try with API Explorer](https://developer.twitter.com/apitools/api?endpoint=/2/lists/%7Bid%7D/members&method=get)

Supporting resources
--------------------

[Learn how to use Postman to make requests](https://developer.twitter.com/en/docs/tutorials/postman-getting-started "Learn how to use Postman to make requests")

[Troubleshoot an error](https://developer.twitter.com/en/support/twitter-api "Troubleshoot an error")

[Visit the API reference page for this endpoint](https://developer.twitter.com/en/docs/twitter-api/lists/list-members/api-reference "Visit the API reference page for this endpoint")

Quick start

Getting started with the List members endpoint group
----------------------------------------------------

This quick overview will help you make your first request to List members endpoints using [Postman](https://developer.twitter.com/en/docs/tools-and-libraries/using-postman).

If you would like to see sample code in different languages, please visit our [Twitter API v2 sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code) GitHub repository. 

### Prerequisites

To complete this guide, you will need to have a set of [keys and tokens](https://developer.twitter.com/en/docs/authentication) to authenticate your request. You can generate these keys and tokens by following these steps:

* [Sign up for a developer account](https://developer.twitter.com/en/apply-for-access) and receive approval.
* Create a [Project](https://developer.twitter.com/en/docs/projects) and an associated [developer App](https://developer.twitter.com/en/docs/apps) in the developer portal.
* Navigate to your App's “Keys and tokens” page to generate the required credentials. Make sure to save all credentials in a secure location.

#### Load the Twitter API v2 Postman Collection

To load the Twitter API v2 Postman collection into your workspace, please click on the following button:

[Add Twitter API v2 to Postman](https://t.co/twitter-api-postman)

  
 

#### Authenticate your request

To make a successful request to **lookup** endpoints, you can use either [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a), [App only](https://developer.twitter.com/en/docs/authentication/oauth-2-0), or [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code). However, with **manage** endpoints, you can only authenticate with OAuth 1.0a User Context or OAuth 2.0 Authorization Code with PKCE.

Regardless, when using Postman, the default authentication keys and tokens will automatically populate in your requests as long as you've set up your environment properly. 

You can do this by selecting the environment named “Twitter API v2” (in the top-right corner of Postman), and adding your keys and tokens to the "initial value" and "current value" fields (by clicking the eye icon next to the environment dropdown). These keys include the following:

* API Key (also known as Consumer Key)
* API Secret Key (also known as Consumer Secret)
* OAuth 1.0a user Access Token
* OAuth 1.0a user Access Token Secret
* App only Access Token
* OAuth 2.0 Client Key (only available if you've set up OAuth 2.0 User Authentication settings in your App's settings)
* OAuth 2.0 Client Secret (only available if you've set up OAuth 2.0 User Authentication settings in your App's settings)

Next steps
----------

Choose any of the following endpoints for a more in-depth guide once, you have completed the prerequisites:

[List members lookup](https://developer.twitter.com/en/docs/twitter-api/lists/list-members/quick-start/list-members-lookup "List members lookup")

[Manage List members](https://developer.twitter.com/en/docs/twitter-api/lists/list-members/quick-start/manage-list-members "Manage List members")

List members lookup

**Please note:** This guide assumes you have completed the prerequisites from the [quick start overview](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/lists/list-members/quick-start).

### Steps to build a List members lookup request

#### Step one: Choose the List endpoint collection from Postman

Once you have the Twitter API v2 collection loaded in Postman, navigate to the “List” folder, select another folder “List members”, and then choose "Members lookup".  
 

#### Step two: Identify and specify which List you would like to retrieve members from

You must specify a List that you would like to receive members from. You can find the List ID by navigating to twitter.com and clicking on a List and then looking in the URL. For example, the following URL's List ID is 84839422.

https://twitter.com/i/lists/84839422

The target ID can be any valid List ID. In Postman, navigate to the "Params" tab, and enter your ID into the "Value" column of the id path variable. Be sure not to include any spaces before or after any ID.

|     |     |
| --- | --- |
| **Key** | **Value** |
| `id` | 84839422 (List ID) |

#### Step three: Identify and specify which fields you would like to retrieve

If you click the "Send" button after step three, you will receive the default [user object](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) fields in your response: id, name, and username.

If you would like to receive additional fields beyond id, name, and username, you will have to specify those fields in your request with the [field](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/data-dictionary/introduction/fields) and/or [expansion](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/introduction/expansions) parameters.

For this exercise, we will request three additional sets of fields from different objects:

* The additional user.created\_at field in the primary user objects.
* The full [Tweet object](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) using the expansion parameter.
* The additional tweet.created\_at field in the associated Tweet objects.

In Postman, navigate to the "Params" tab and add the following key:value pair to the "Query Params" table:

|     |     |     |
| --- | --- | --- |
| **Key** | **Value** | **Returned fields** |
| user.fields | created\_at | `created_at` |
| expansions | pinned\_tweet\_id | `includes.tweets.id,   includes.tweets.text   ` |
| tweet.fields | created\_at | `includes.tweets.created_at` |

You should now see a similar URL next to the “Send” button:

      `https://api.twitter.com/2/lists/84839422/members?user.fields=created_at&expansions=pinned_tweet_id&tweet.fields=created_at`
    

Step four: Make your request and review your response  

Once you have everything set up, hit the "Send" button, and you will receive a similar response to the following example response:

      `{   "data": [     {       "pinned_tweet_id": "1353789891348475905",       "id": "1319036828964454402",       "created_at": "2020-10-21T22:04:47.000Z",       "name": "Birdwatch",       "username": "birdwatch"     },     {       "id": "1244731491088809984",       "created_at": "2020-03-30T21:02:29.000Z",       "name": "Twitter Thailand",       "username": "TwitterThailand"     },     {       "id": "1194267639100723200",       "created_at": "2019-11-12T14:56:22.000Z",       "name": "Twitter Retweets",       "username": "TwitterRetweets"     },     {       "id": "1168976680867762177",       "created_at": "2019-09-03T19:59:02.000Z",       "name": "Twitter Able",       "username": "TwitterAble"     },     {       "pinned_tweet_id": "1451239134798942208",       "id": "1065249714214457345",       "created_at": "2018-11-21T14:24:58.000Z",       "name": "Spaces",       "username": "TwitterSpaces"     },     {       "id": "1049385226424786944",       "created_at": "2018-10-08T19:45:09.000Z",       "name": "Twitter Miami",       "username": "TwitterMiami"     },     {       "pinned_tweet_id": "1438533888498876420",       "id": "1004367799588880384",       "created_at": "2018-06-06T14:21:58.000Z",       "name": "Twitter México",       "username": "TwitterMexico"     },     {       "pinned_tweet_id": "1370178223846297602",       "id": "773578328498372608",       "created_at": "2016-09-07T17:47:00.000Z",       "name": "Twitter Together",       "username": "TwitterTogether"     },     {       "id": "766296039036948480",       "created_at": "2016-08-18T15:29:47.000Z",       "name": "Moments MENA",       "username": "momentsmena"     },     {       "id": "738118487122419712",       "created_at": "2016-06-01T21:22:15.000Z",       "name": "Twitter Asians",       "username": "TwitterAsians"     }   ],   "includes": {     "tweets": [       {         "created_at": "2021-01-25T19:40:36.000Z",         "id": "1353789891348475905",         "text": "Want to help build a new community-driven approach to tackling misleading information? Join us — sign up for Birdwatch! \n\nhttps://t.co/FSsqNznPy1"       },       {         "created_at": "2021-10-21T17:29:07.000Z",         "id": "1451239134798942208",         "text": "the time has arrived -- we’re now rolling out the ability for everyone on iOS and Android to host a Space\n\nif this is your first time hosting, welcome! here’s a refresher on how https://t.co/cLH8z0bocy"       },       {         "created_at": "2021-09-16T16:03:00.000Z",         "id": "1438533888498876420",         "text": "Algunos le dicen amor, pero yo le digo:\n\n‌    ∧＿∧　 \n（｡･ω･｡)つ━☆・*\n⊂     　ノ 　　　・゜+.\n　しーＪ　　　°。+ *´¨)\n　　　　　 　　　☆ RECALENTADO ☆ \n#VivaMéxico"       },       {         "created_at": "2021-03-12T01:01:59.000Z",         "id": "1370178223846297602",         "text": "Still, We Fly\n\n... because no matter how many times 2020 tried to knock us down, we got back up and responded with empathy, agility, innovation, and leadership.\n\nRead more in our 2020 Inclusion &amp; Diversity Annual Report #UntilWeAllBelong"       }     ]   },   "meta": {     "result_count": 10,     "next_token": "5349804505549807616"   } }`
    

Next steps
----------

[Customize your request using the API Reference](https://developer.twitter.com/en/docs/twitter-api/lists/list-members/api-reference "Customize your request using the API Reference")

[Reach out to the community for help](https://twittercommunity.com/ "Reach out to the community for help")

Manage List members

**Please note:** This guide assumes you have completed the prerequisites from the [quick start overview](https://developer.twitter.com/en/docs/twitter-api/lists/list-members/quick-start).

### Steps to build a manage List member request

#### Step one: Choose the List endpoint collection from Postman

Once you have the Twitter API v2 collection loaded in Postman, navigate to the “List” folder, select another folder “List members”, and then choose "Add a member".  
 

#### Step two: Specify the user to add

Manage List member endpoints require two IDs: the ID of the List and the ID of the user to add. You can find the user’s ID using the [users lookup](https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference) and pass a username to receive the id field.

The target ID can be any valid user ID. In Postman, navigate to the "Params" tab, and enter your ID into the "Value" column of the id path variable. Navigate to the “Body” tab and ID of the user you wish to add as the value for the user\_id parameter. Be sure not to include any spaces before or after any ID.

|     |     |     |
| --- | --- | --- |
| **Key** | **Value** | **Parameter type** |
| `id` | The List ID | path |
| user\_id | The target user ID you wish to add as a member | body |

You should now see a similar URL next to the "Send" button:

      `https://api.twitter.com/2/lists/1441162269824405510/members`
    

Step three: Make your request and review your response  

Once you have everything set up, hit the "Send" button, and you will receive a similar response to the following example response:

      `{   "data": {     "is_member": true   } }`
    

If the returned response object contains a true value for the key is\_member, you have successfully added the user as a member of the List. 

To remove a member from a List, select the “Remove a member” request also found in the “Lists” folder of the Twitter API v2 collection loaded in Postman. This endpoint requires the ID of the List and the user ID of the member you wish to remove. In the “Params” tab, enter the ID of the List as the value for the id column and ID of the user to be removed as the value for the  user\_id column. 

On successful delete request, you will receive a response similar to the following example:

      `{   "data": {     "is_member": false   } }`
    

Next steps
----------

[Customize your request using the API Reference](https://developer.twitter.com/en/docs/twitter-api/lists/list-members/api-reference "Customize your request using the API Reference")

[Reach out to the community for help](https://twittercommunity.com/ "Reach out to the community for help")

Integrate

Integration guide
-----------------

This page contains information on several tools and critical concepts that you should know as you integrate the List members endpoints into your system. We’ve broken the page into a couple of different sections:

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

Are you interested in getting set up with this endpoint with some code in your preferred coding language? We’ve got a handful of different code samples available that you can use as a starting point on our [Github page](https://github.com/twitterdev/Twitter-API-v2-sample-code).

#### Third-party libraries

Take advantage of one of our communities’ [third-party libraries](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries) to help you get started. You can find a library that works with the v2 endpoints by looking for the proper version tag.

### Key concepts

#### Authentication

All Twitter API v2 endpoints require you to authenticate your requests with a set of credentials, also known as keys and tokens. You can use either OAuth 1.0a User Context, OAuth 2.0 Authorization Code with PKCE, or App only to authenticate your requests for the Lists **lookup** endpoints. However, you must authenticate with OAuth 1.0a User Context or OAuth 2.0 for the **manage** Lists endpoints. 

[OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a), which means that you must use a set of API Keys and user Access Tokens to make a successful request. The access tokens must be associated with the user that you are making the request on behalf of. If you would like to generate a set of Access Tokens for another user, they must authorize your App using the [3-legged OAuth flow](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens).

Please note that OAuth 1.0a can be difficult to use. If you are not familiar with this authentication method, we recommend that you use a [library](https://developer.twitter.com/content/en/docs/twitter-api/tools-and-libraries), use a tool like Postman, or use either OAuth 2.0 or App only to authenticate your requests.

[OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code) allows for greater control over an application’s scope, and authorization flows across multiple devices. OAuth 2.0 allows you to pick specific fine-grained scopes which give you specific permissions on behalf of a user. 

To enable OAuth 2.0 in your App, you must enable it in your’s App’s authentication settings found in the App settings section of the developer portal.

[App only](https://developer.twitter.com/en/docs/authentication/oauth-2-0) just requires that you pass an [App only Access Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens) with your request. You can either generate an App only Access Token directly within a developer App, or generate one using the [POST oauth2/token](https://developer.twitter.com/en/docs/authentication/api-reference/token) endpoint.

[App only](https://developer.twitter.com/en/docs/authentication/oauth-2-0) just requires that you pass an [App only Access Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens) with your request. You can either generate an App only Access Token directly within a developer App, or generate one using the [POST oauth2/token](https://developer.twitter.com/en/docs/authentication/api-reference/token) endpoint.

#### Developer portal, Projects, and developer Apps

To retrieve a set of authentication credentials that will work with the Twitter API v2 endpoints, you must [sign up for a developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info), set up a [Project](https://developer.twitter.com/en/docs/projects) within that account, and created a [developer App](https://developer.twitter.com/en/docs/apps) within that Project. You can then find your keys and tokens within your developer App.  
 

#### Rate limits

Every day, many thousands of developers make requests to the Twitter API. To help manage the sheer volume of these requests, [rate limits](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/rate-limits) are placed on each endpoint that limits the number of requests you can make on behalf of your app or on behalf of an authenticated user. 

Lookup (GET) endpoints are rate limited at both the App-level and the user-level; while manage (POST/DELETE) endpoints are limited at the user-level. The app rate limit means that you, the developer, can only make a certain number of requests to this endpoint over a given period of time from any given App (assumed by using either the API Key and API Secret Key, or the App only Access Token). The user rate limit means that the authenticated user that you are making the request on behalf of can only perform a List lookup a certain number of times across any developer App.

The chart below shows the rate limits for each endpoint.

|     |     |     |
| --- | --- | --- |
| **Endpoint** | **HTTP method** | **Rate limit** |
| /2/lists/:id/members | GET | 900 requests per 15 minutes |
| /2/users/:id/list\_memberships | GET | 75 requests per 15 minutes |
| /2/lists/:id/members | POST | 300 requests per 15 minutes |
| /2/lists/:id/members/:user\_id | DELETE | 300 requests per 15 minutes |

#### Fields and expansions

The Twitter API v2 GET endpoint allows users to select exactly which data they want to return from the API using a set of tools called `fields` and `expansions`. The `expansions` parameter allows you to expand objects referenced in the payload. For example, looking up List members allows you to pull the following [expansions](https://developer.twitter.com/en/docs/twitter-api/expansions):

* `pinned_tweet_id`
    

The `fields` parameter allows you to select exactly which [fields](https://developer.twitter.com/en/docs/twitter-api/fields) within the different data objects you would like to receive. List members lookup delivers user objects primarily. By default, the user object returns id, name, and username fields. To receive additional fields such as `user.created_at` or `user.description`, you will have to specifically request those using a user.fields parameter. 

We’ve added a guide on using [fields and expansions](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/using-fields-and-expansions) together to our [Twitter API v2 data dictionary](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/introduction).

 The chart below shows the field and expansions available for each lookup endpoint:

|     |     |     |
| --- | --- | --- |
| **Endpoint** | **Fields** | **Expansions** |
| /2/lists/:id/members | `user.fields`<br><br>`tweet.fields` | `pinned_tweet_id` |
| /2/users/:id/list\_memberships | list.fields<br><br>user.fields | owner\_id |

#### Pagination

Looking up membership/members can return a lot of data. To ensure we are returning consistent, high-performing results at any given time, we use pagination. Pagination is a feature in Twitter API v2 endpoints that return more results than can be returned in a single response. When that happens, the data is returned in a series of 'pages'. Learn more about how to [paginate through results.](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/pagination)

Next steps
----------

[Visit the API reference page for these endpoint](https://developer.twitter.com/en/docs/twitter-api/lists/list-members/api-reference "Visit the API reference page for these endpoint")

Migrate

Comparing Twitter API’s List members endpoints
----------------------------------------------

The v2 List members endpoint group will replace the standard v1.1 [GET lists/members](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-members), [GET lists/memberships](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-memberships), [POST lists/members/create](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-members-create) and [POST lists/members/destroy](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-members-destroy) endpoints. If you have code, apps, or tools that use one of these versions of the List member endpoints, and are considering migrating to the newer Twitter API v2 endpoint, then this set of guides is for you. 

### List members lookup

The v2 List members lookup endpoints will replace the standard  [GET lists/members](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-members), [GET lists/memberships](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-memberships), endpoints.

The following tables compare the standard v1.1 and Twitter API v2 List endpoints:

**List member Lookup**

|     |     |     |
| --- | --- | --- |
| Description | Standard v1.1 | Twitter API v2 |
| HTTP methods supported | `GET` | `GET` |
| Host domain | `https://api.twitter.com` | `https://api.twitter.com` |
| Endpoint path | `/1.1/lists/members.json` | `/2/lists/:id/members` |
| [Authentication](https://developer.twitter.com/content/developer-twitter/en/docs/authentication) | OAuth 1.0a User Context<br><br>App only | OAuth 1.0a User Context<br><br>OAuth 2.0 Authorization Code with PKCE<br><br>App only |
| Default request [rate limits](https://developer.twitter.com/content/developer-twitter/en/docs/rate-limits) | 900 requests per 15 min with OAuth 1.0a<br><br>75 requests per 15min with App only | 900 requests per 15 min with OAuth 1.0a<br><br>900 requests per 15 min with OAuth 2.0<br><br>900 requests per 15 min with App only |

**List membership lookup**

|     |     |     |
| --- | --- | --- |
| Description | Standard v1.1 | Twitter API v2 |
| HTTP methods supported | `GET` | `GET` |
| Host domain | `https://api.twitter.com` | `https://api.twitter.com` |
| Endpoint path | `/1.1/lists/memberships.json` | `/2/users/:id/list_memberships` |
| [Authentication](https://developer.twitter.com/content/developer-twitter/en/docs/authentication) | OAuth 1.0a User Context<br><br>App only | OAuth 1.0a User Context<br><br>OAuth 2.0 Authorization Code with PKCE<br><br>App only |
| Default request [rate limits](https://developer.twitter.com/content/developer-twitter/en/docs/rate-limits) | 75 requests per 15 min with OAuth 1.0a<br><br>75 requests per 15min with App only | 75 requests per 15 min with OAuth 1.0a<br><br>75 requests per 15 min with OAuth 2.0<br><br>75 requests per 15min with App only |

### Manage List members

The v2 manage List members endpoints will replace the standard [POST lists/members/create](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-members-create), [POST lists/members/destroy](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-members-destroy) endpoints.

The following tables compare the standard v1.1 and Twitter API v2 List endpoints:

**Add member**

| Description | Standard v1.1 | Twitter API v2 |
| --- | --- | --- |
| HTTP methods supported | POST | POST |
| Host domain | https://api.twitter.com | https://api.twitter.com |
| Endpoint path | /1.1/lists/members/create.json | /2/lists/:id/members |
| [Authentication](https://developer.twitter.com/content/developer-twitter/en/docs/authentication) | OAuth 1.0a User Context | OAuth 1.0a User Context<br><br>OAuth 2.0 Authorization Code with PKCE |
| Default request [rate limits](https://developer.twitter.com/content/developer-twitter/en/docs/rate-limits) | None | 300 requests per 15 min (per user) |

**Remove member**

| Description | Standard v1.1 | Twitter API v2 |
| --- | --- | --- |
| HTTP methods supported | POST | DELETE |
| Host domain | https://api.twitter.com | https://api.twitter.com |
| Endpoint path | /1.1/lists/members/destroy.json | /2/lists/:id/:user\_id |
| [Authentication](https://developer.twitter.com/content/developer-twitter/en/docs/authentication) | OAuth 1.0a User Context | OAuth 1.0a User Context<br><br>OAuth 2.0 Authorization Code with PKCE |
| Default request [rate limits](https://developer.twitter.com/content/developer-twitter/en/docs/rate-limits) | None | 300 requests per 15 min (per user) |

To access the Twitter API v2 endpoints, you must [sign up for a developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info). When authenticating, you must use keys and tokens from a [developer App](https://developer.twitter.com/en/docs/apps) that is located within a [Project](https://developer.twitter.com/en/docs/projects). 

Learn more about getting access to the Twitter API v2 endpoints in our [getting started](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api) page.

[Quick start](https://developer.twitter.com/en/docs/twitter-api/lists/list-members/quick-start)

[Sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code)

[Run in Postman](https://t.co/twitter-api-postman)

Supporting resources
--------------------

[Learn how to use Postman to make requests](https://developer.twitter.com/en/docs/tutorials/postman-getting-started "Learn how to use Postman to make requests")

[Troubleshoot an error](https://developer.twitter.com/en/support/twitter-api "Troubleshoot an error")

[Visit the API reference page for this endpoint](https://developer.twitter.com/en/docs/twitter-api/lists/list-members/api-reference "Visit the API reference page for this endpoint")

List members lookup: Standard v1.1 compared to Twitter API v2

List members lookup: Standard v1.1 compared to Twitter API v2
-------------------------------------------------------------

If you have been working with the standard v1.1 [GET lists/members](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-members) and [GET lists/memberships](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-memberships) endpoints, the goal of this guide is to help you understand the similarities and differences between the standard v1.1 and Twitter API v2 List member endpoints.

* **Similarities**
    * Authentication methods
* **Differences**
    * Endpoint URLs
    * Rate limits
    * App and Project requirements
    * Data objects per request limits
    * Response data formats
    * Request parameters

### Similarities

#### **Authentication**

Both endpoint versions support both [OAuth 1.0a User Context](https://developer.twitter.com/content/developer-twitter/en/docs/authentication/oauth-1-0a) and [App only](https://developer.twitter.com/content/developer-twitter/en/docs/authentication/oauth-2-0). Therefore, if you were previously using one of the standard v1.1 List members endpoints, you can continue using the same authentication method if you migrate to the Twitter API v2 version.

Depending on your authentication library/package of choice, App only authentication is probably the easiest way to get started and can be set with a simple request header. To learn how to generate an App only Access Token, see [this App only guide](https://developer.twitter.com/en/docs/basics/authentication/overview/application-only).

### Differences

#### Endpoint URLs

* Standard v1.1 endpoints:
    * GET https://api.twitter.com/1.1/lists/members.json  
        (Lookup members of a specified List)
    * GET https://api.twitter.com/1.1/lists/memberships.json  
        (Lookup Lists a user is a member of)
* Twitter API v2 endpoint:
    * GET https://api.twitter.com/2/lists/:id/members  
        (Lookup members of a specified List)  
        
    * GET https://api.twitter.com/2/users/:id/list\_memberships  
        (Lookup Lists a user is a member of)

**Rate limits**

|     |     |
| --- | --- |
| **Standard v1.1** | **Twitter API v2** |
| /1.1/lists/members.json<br><br>900 requests per 15-minute window with OAuth 1.0a User Context<br><br>15 requests per 15-minute window with App only | /2/lists/:id/members<br><br>900 requests per 15-minute window with OAuth 1.0a User Context<br><br>900 requests per 15-minute window with OAuth 2.0 Authorization Code with PKCE<br><br>900 requests per 15-minute window with App only |
| /1.1/lists/memberships.json<br><br>15 requests per 15-minute window with OAuth 1.0a User Context<br><br>15 requests per 15-minute window with App only | /2/users/:id/list\_memberships<br><br>15 requests per 15-minute window with OAuth 1.0a User Context<br><br>15 requests per 15-minute window with OAuth 2.0 Authorization Code with PKCE<br><br>15 requests per 15-minute window with App only |

#### App and Project requirements

The Twitter API v2 endpoints require that you use credentials from a [developer App](https://developer.twitter.com/en/docs/apps) that is associated with a [Project](https://developer.twitter.com/en/docs/projects) when authenticating your requests. All Twitter API v1.1 endpoints can use credentials from standalone Apps or Apps associated with a project.

####   
  
Data objects per request limits

The standard v1.1 /1.1/lists/members endpoint allows you to return up to 5000 users per request. The new v2 endpoints allow you to return up to 100 users per request. By default, 100 user objects will be returned, to change the number of results you will need to pass a query parameter max\_results= with a number between 1-100; you can then pass the next\_token returned in the response payload to the pagination\_token query parameter in your next request.

 Additionally, the endpoint /1.1/lists/memberships, allow you to return up to 1000 Lists per request. With the v2 replacement, the endpoint allows up to 100 Lists per request. By default 100 Lists objects are returned, use the query parameters max\_results= and pagination\_token in the same fashion as /1.1/lists/members to change the number of results.

**Response data format**

One of the biggest differences between standard v1.1 and Twitter API v2 endpoint versions is how you select which fields return in your payload.

For the standard endpoints, you receive many of the response fields by default and then have the option to use parameters to identify which additional fields or sets of fields should return in the payload.

The Twitter API v2 version /users/:id/list\_memberships will deliver the List id and name fields by default. To request any additional fields or objects, you will need to use the [fields](https://developer.twitter.com/en/docs/twitter-api/fields/content/developer-twitter/en/docs/twitter-api/fields) and [expansions](https://developer.twitter.com/en/docs/twitter-api/fields/content/developer-twitter/en/docs/twitter-api/expansions) parameters. Any List fields that you request from this endpoint will return in the primary List object. Any expanded object and fields will return an includes object within your response. You can then match any expanded objects back to the primary List object by matching the IDs located in both the primary and the expanded object. 

Here are examples of possible List fields and expansions:

* created\_at
    
* follower\_count
    
* member\_count
    
* owner\_id
    
* description
    
* private
    

|     |     |
| --- | --- |
| **Endpoint** | **Expansion** |
| /2/lists/:id/members | pinned\_tweet\_id |
| /2/users/:id/list\_memberships | owner\_id |

We encourage you to read more about these new parameters in their respective guides, or by reading our guide on [how to use fields and expansions](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/using-fields-and-expansions). 

We have also put together a [data format migration guide](https://developer.twitter.com/en/docs/twitter-api/migrate/data-formats/standard-v1-1-to-v2) that can help you map standard v1.1 fields to the newer v2 fields. This guide will also provide you with the specific expansion and field parameter that you will need to pass with your v2 request to return specific fields. 

In addition to the changes in how you request certain fields, Twitter API v2 is also introducing new JSON designs for the objects returned by the APIs, including [Tweet](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) and [user](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) objects.

* At the JSON root level, the standard endpoints return Tweet objects in a statuses array, while Twitter API v2 returns a data array. 
    
* Instead of referring to Retweeted and Quoted "statuses", Twitter API v2 JSON refers to Retweeted and Quoted Tweets. Many legacy and deprecated fields, such as contributors and user.translator\_type are being removed. 
    
* Instead of using both favorites (in Tweet object) and favourites (in user object), Twitter API v2 uses the term like. 
    
* Twitter is adopting the convention that JSON values with no value (for example, null) are not written to the payload. Tweet and user attributes are only included if they have non-null values.  
      
    

#### Request parameters

The following standard v1.1 request parameters have equivalents in Twitter API v2:

**List members lookup**

|     |     |
| --- | --- |
| **Standard v1.1** | **Twitter API v2** |
| list\_id | id  |
| slug | No equivalent |
| owner\_screen\_name | No equivalent |
| owner\_id | No equivalent |
| count | max\_results |
| cursor | pagination\_token |
| include\_entities | No equivalent |
| skip\_status | No equivalent |

**List membership lookup**

|     |     |
| --- | --- |
| **Standard v1.1** | **Twitter API v2** |
| user\_id | id  |
| screen\_name | No equivalent |
| count | max\_results |
| cursor | pagination\_token |

Next steps
----------

[Review the List members API references](https://developer.twitter.com/en/docs/twitter-api/lists/list-members/api-reference "Review the List members API references")

Manage List members: Standard v1.1 compared to Twitter API v2

Manage List members: Standard v1.1 compared to Twitter API v2
-------------------------------------------------------------

If you have been working with the standard v1.1 [POST lists/members/create](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-members-create) and [POST lists/members/destroy](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-members-destroy) endpoints, the goal of this guide is to help you understand the similarities and differences between the standard v1.1 and Twitter API v2 manage List members endpoints.

* **Similarities**
    * Authentication
* **Differences**
    * Endpoint URLs
    * App and Project requirements
    * HTTP methods
    * Rate limits
    * Request parameters

### Similarities

#### **Authentication**

Both endpoint versions support [OAuth 1.0a User Context](https://developer.twitter.com/content/developer-twitter/en/docs/authentication/oauth-1-0a). Therefore, if you were previously using one of the standard v1.1 manage List member endpoints, you can continue using the same authentication method if you migrate to the Twitter API v2 version.

### Differences

#### Endpoint URLs

* Standard v1.1 endpoints:
    * POST https://api.twitter.com/1.1/lists/members/create.json  
        (Adds a member to a specified List)
    * POST https://api.twitter.com/1.1/lists/members/destroy.json  
        (Removes a member from a specified List)
* Twitter API v2 endpoint:
    * POST https://api.twitter.com/2/lists/:id/members  
        (Adds a member to a specified List)  
        
    * DELETE https://api.twitter.com/2/lists/:id/members/:user\_id  
        (Removes a member from a specified List)

#### Rate limits

| **Standard v1.1** | **Twitter API v2** |
| --- | --- |
| /1.1/lists/members/create.json<br><br>none | /2/lists/:id/members<br><br>300 requests per 15-minute window with OAuth 1.0a User Context<br><br>300 requests per 15-minute window with OAuth 2.0 Authorization Code with PKCE |
| /1.1/lists/members/destroy.json<br><br>none | /2/lists/:id/members/:user\_id<br><br>300 requests per 15-minute window with OAuth 1.0a User Context<br><br>300 requests per 15-minute window with OAuth 2.0 Authorization Code with PKCE |

#### App and Project requirements

The Twitter API v2 endpoints require that you use credentials from a [developer App](https://developer.twitter.com/en/docs/apps) that is associated with a [Project](https://developer.twitter.com/en/docs/projects) when authenticating your requests. All Twitter API v1.1 endpoints can use credentials from standalone Apps or Apps related to a project.

#### Request parameters

The following standard v1.1 request parameters have equivalents in Twitter API v2:

| **Standard v1.1** | **Twitter API v2** |
| --- | --- |
| list\_id | id  |
| slug | No equivalent |
| screen\_name | No equivalent |
| owner\_screen\_name | No equivalent |
| owner\_id | No equivalent |

Next steps
----------

[Review the List members API references](https://developer.twitter.com/en/docs/twitter-api/lists/list-members/api-reference "Review the List members API references")

API reference

API reference index
-------------------

For the complete API reference, select an endpoint from the list.  
  

### List members lookup  

|     |     |
| --- | --- |
| **Returns a list of members from a specified List** | `[GET /2/lists/:id/members](https://developer.twitter.com/en/docs/twitter-api/lists/list-members/api-reference/get-lists-id-members)` |
| **Returns all Lists a specified user is a member of** | `[GET /2/users/:id/list_memberships](https://developer.twitter.com/en/docs/twitter-api/lists/list-members/api-reference/get-users-id-list_memberships)` |

### Manage List members  

|     |     |
| --- | --- |
| **Add a member to a List that the authenticated user owns** | `[POST /2/lists/:id/members](https://developer.twitter.com/en/docs/twitter-api/lists/list-members/api-reference/post-lists-id-members)` |
| **Removes a member from a List the authenticated user owns** | `[DELETE /2/lists/:id/members/:user_id](https://developer.twitter.com/en/docs/twitter-api/lists/list-members/api-reference/delete-lists-id-members-user_id)` |

POST /2/lists/:id/members

POST /2/lists/:id/members
=========================

Enables the authenticated user to add a member to a List they own.

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Try a live request ❯](https://oauth-playground.glitch.me/?id=listAddMember&params=%28%27query%21%28%29%7Ebody%21%27%27%7Epath%21%28%29%29_) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Flists%2F%7Bid%7D%2Fmembers&method=post) 

### Endpoint URL

`https://api.twitter.com/2/lists/:id/members`  
  

### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code "This method allows an authorized app to act on behalf of the user, as the user. It is typically used to access or post public information for a specific user, and it us useful when your app needs to be aware of the relationship between a user and what this endpoint returns. Click to learn how to authenticate with OAuth 2.0 Authorization Code with PKCE.")<br><br>[OAuth 1.0a](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) is also available for this endpoint. |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | User rate limit (User context): 300 requests per 15-minute window per each authenticated user |

### OAuth 2.0 scopes required by this endpoint

|     |
| --- |
| `tweet.read`<br><br>`users.read`<br><br>`list.write` |
| [Learn more about OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/twitter-api/oauth2) |

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Required | string | The ID of the List you are adding a member to. |

  
  

### JSON body parameters

| Name | Type | Description |
| --- | --- | --- |
| `user_id`  <br> Required | string | The ID of the user you wish to add as a member of the List. |

  
  

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript](#tab0)
* [Java](#tab1)

TypeScript

Java

      `(async () => {   try {     const addMember = await twitterClient.lists.listAddMember(       //The ID of the user to be added as a member of the List       2244994945,        //The ID of the List to add a member       1441162269824405510     );     console.dir(addMember, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  // String | The ID of the user to be added as a member of the List String usersId = "2244994945" ListAddMemberRequest listAddMemberRequest = new ListAddMemberRequest(); listAddMemberRequest.userId(usersId);  // String | The ID of the List to add a member String id = "1441162269824405510";  try {     ListMemberResponse result = apiInstance.lists().listAddMember(listAddMemberRequest, id);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling ListsApi#listAddMember");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

### Example responses

* [Successful response](#tab0)

Successful response

      `{   "data": {     "is_member": true   } }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `is_member` | boolean | Indicates whether the member specified in the request has been added to the List. |

DELETE /2/lists/:id/members/:user\_id

DELETE /2/lists/:id/members/:user\_id
=====================================

Enables the authenticated user to remove a member from a List they own.

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Try a live request ❯](https://oauth-playground.glitch.me/?id=listRemoveMember&params=%28%27query%21%28%29%7Ebody%21%27%27%7Epath%21%28%29%29_) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Flists%2F%7Bid%7D%2Fmembers%2F%7Buser_id%7D&method=delete) 

### Endpoint URL

`https://api.twitter.com/2/lists/:id/members/:user_id`  
  

### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 1.0a](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) is also available for this endpoint.<br><br>[OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code "This method allows an authorized app to act on behalf of the user, as the user. It is typically used to access or post public information for a specific user, and it us useful when your app needs to be aware of the relationship between a user and what this endpoint returns. Click to learn how to authenticate with OAuth 2.0 Authorization Code with PKCE.") |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | User rate limit (User context): 300 requests per 15-minute window per each authenticated user |

### OAuth 2.0 scopes required by this endpoint

|     |
| --- |
| `tweet.read`<br><br>`users.read`<br><br>`list.write` |
| [Learn more about OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/twitter-api/oauth2) |

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Required | string | The ID of the List you are removing a member from. |
| `user_id`  <br> Required | string | The ID of the user you wish to remove as a member of the List. |

  
  

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript](#tab0)
* [Java](#tab1)

TypeScript

Java

      `(async () => {   try {     const removeMember = await twitterClient.lists.listRemoveMember(       //The ID of the List to remove a member       1441162269824405510,        //The ID of user that will be removed from the List       2244994945     );     console.dir(removeMember, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  // String |The ID of the List to remove a member String id = "1441162269824405510";   // String | The ID of user that will be removed from the List String userId = "2244994945"; try {     ListMemberResponse result = apiInstance.lists().listRemoveMember(id, userId);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling ListsApi#listRemoveMember");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

### Example responses

* [Successful response](#tab0)

Successful response

      `{   "data": {     "is_member": false   } }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `is_member` | boolean | Indicates whether the member specified in the request has been removed from the List. |

GET /2/users/:id/list\_memberships

GET /2/users/:id/list\_memberships
==================================

Returns all Lists a specified user is a member of.

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Try a live request ❯](https://oauth-playground.glitch.me/?id=getUserListMemberships&params=%28%27query%21%28%29%7Ebody%21%27%27%7Epath%21%28%29%29_) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Fusers%2F%7Bid%7D%2Flist_memberships&method=get) 

### Endpoint URL

`https://api.twitter.com/2/users/:id/list_memberships`  
  

### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 2.0 App-only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only "Use this method to obtain information in the context of an unauthenticated public user. This method is for developers that just need read-only access to public information. Click to learn how to obtain an OAuth 2.0 App Access Token.")<br><br>[OAuth 1.0a](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) is also available for this endpoint.<br><br>[OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code "This method allows an authorized app to act on behalf of the user, as the user. It is typically used to access or post public information for a specific user, and it us useful when your app needs to be aware of the relationship between a user and what this endpoint returns. Click to learn how to authenticate with OAuth 2.0 Authorization Code with PKCE.") |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | User rate limit (User context): 75 requests per 15-minute window per each authenticated user<br><br>App rate limit (Application-only): 75 requests per 15-minute window shared among all users of your app |

### OAuth 2.0 scopes required by this endpoint

|     |
| --- |
| `tweet.read`<br><br>`users.read`<br><br>`list.read` |
| [Learn more about OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/twitter-api/oauth2) |

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Required | string | The user ID whose List memberships you would like to retrieve. |

  
  

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| `expansions`  <br> Optional | enum (`owner_id`) | [Expansions](https://developer.twitter.com/en/docs/twitter-api/expansions) enable you to request additional data objects that relate to the originally returned List. The ID that represents the expanded data object will be included directly in the List data object, but the expanded object metadata will be returned within the `includes` response object, and will also include the ID so that you can match this data object to the original user object. At this time, the only expansion available to endpoints that primarily return List objects is `expansions=owner_id`. You will find the expanded user data object living in the `includes` response object. |
| `list.fields`  <br> Optional | enum (`created_at`, `follower_count`, `member_count`, `private`, `description`, `owner_id`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [List fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/lists) will deliver with each returned List objects. Specify the desired fields in a comma-separated list without spaces between commas and fields. These specified List fields will display directly in the List data objects. |
| `max_results`  <br> Optional | integer | The maximum number of results to be returned per page. This can be a number between 1 and 100. By default, each page will return 100 results. |
| `pagination_token`  <br> Optional | string | Used to request the next page of results if all results weren't returned with the latest request, or to go back to the previous page of results. To return the next page, pass the next\_token returned in your previous response. To go back one page, pass the previous\_token returned in your previous response. |
| `user.fields`  <br> Optional | enum (`created_at`, `description`, `entities`, `id`, `location`, `most_recent_tweet_id`, `name`, `pinned_tweet_id`, `profile_image_url`, `protected`, `public_metrics`, `url`, `username`, `verified`, `withheld`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [user fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) will deliver with the users object. Specify the desired fields in a comma-separated list without spaces between commas and fields. The user fields will only be returned if you have included `expansions=owner_id` query parameter in your request. You will find this ID and all additional user fields in the `included` data object. |

  
  

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript (Default fields)](#tab0)
* [TypeScript (Optional fields)](#tab1)
* [Java (Default fields)](#tab2)
* [Java (Optional fields)](#tab3)

TypeScript (Default fields)

TypeScript (Optional fields)

Java (Default fields)

Java (Optional fields)

      `(async () => {   try {     const getUserMemberships =       await twitterClient.lists.getUserListMemberships(         //The ID of the user for whom to return results         84839422       );     console.dir(getUserMemberships, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `(async () => {   try {     const getUserMemberships =       await twitterClient.lists.getUserListMemberships(         //The ID of the user for whom to return results         84839422,         {           //A comma separated list of fields to expand           expansions: ["owner_id"],            //A comma separated list of List fields to display           "list.fields": ["follower_count"],            //A comma separated list of User fields to display           "user.fields": ["created_at"],         }       );     console.dir(getUserMemberships, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  // String | The ID of the user for whom to return results String id = "84839422";  try {     MultiListResponse result = apiInstance.lists().getUserListMemberships(id, null, null, null, null, null);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling ListsApi#getUserListMemberships");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

      `// Set the params values // For full list of params visit - https://github.com/twitterdev/twitter-api-java-sdk/blob/main/docs/ListsApi.md#getUserListMemberships  // String | The ID of the user for whom to return results String id = "84839422";  // Set<String> | A comma separated list of List fields to display Set<String> listFields = new HashSet<>(Arrays.asList("follower_count"));   // Set<String> | A comma separated list of fields to expand Set<String> expansions = new HashSet<>(Arrays.asList("owner_id"));  // Set<String> | A comma separated list of User fields to display Set<String> userFields = new HashSet<>(Arrays.asList("created_at"));  try {     MultiListResponse result = apiInstance.lists().getUserListMemberships(id, null, null, listFields, expansions, userFields);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling ListsApi#getUserListMemberships");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

### Example responses

* [Default fields](#tab0)
* [Optional fields](#tab1)

Default fields

Optional fields

      `{   "data": [     {       "id": "1451951974291689472",       "name": "Twitter"     },     {       "id": "1451812298184540161",       "name": "Updates"     },     {       "id": "1450519480132509697",       "name": "Twitter"     }   ],   "meta": {     "result_count": 3   } }`
    

      `{   "data": [     {       "follower_count": 5,       "id": "1451951974291689472",       "name": "Twitter",       "owner_id": "1227213680120479745"     }   ],   "includes": {     "users": [       {         "name": "구돆",         "created_at": "2020-02-11T12:52:11.000Z",         "id": "1227213680120479745",         "username": "Follow__Y0U"       }     ]   },   "meta": {     "result_count": 1   } }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Default | string | Unique identifier of this List. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. |
| `name`  <br> Default | string | The name of this List. |
| `created_at` | date (ISO 8601) | Creation time of this List.  <br>  <br>To return this field, add `list.fields=created_at` in the request's query parameter. |
| `private` | boolean | Indicates if this List has been set to private. The List (in other words, if this is publicly viewed or not).  <br>  <br>To return this field, add `list.fields=private` in the request's query parameter. |
| `follower_count` | integer | Number of users who follow this List.  <br>  <br>To return this field, add `list.fields=follower_count` in the request's query parameter. |
| `member_count` | integer | Number of users who are a member of this List.  <br>  <br>To return this field, add `list.fields=member_count` in the request's query parameter. |
| `owner_id` | string | Unique identifier of this List's owner. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers.  <br>  <br>To return this field, add `list.fields=owner_id` in the request's query parameter. |
| `description` | string | A brief description of this List, if the owner provided one.  <br>  <br>To return this field, add `list.fields=description` in the request's query parameter. |
| `includes.users` | array | When including the `expansions=owner_id` parameter, this includes the referenced List owner in the form of a [user object](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) with their default fields and any additional fields requested using the `user.fields` parameter. |
| `meta`  <br> Default | object | This object contains information about the number of users returned in the current request, and pagination details. |
| `meta.result_count`  <br> Default | integer | The number of users returned in this request. Note that this number may be lower than what was specified in the `max_results` query parameter. |
| `meta.previous_token` | string | Pagination token for the previous page of results. This value is returned when there are multiple pages of results, as the current request may only return a subset of results. To go back to the previous page, passing the value from this field in the `pagination_token` query parameter. When this field is not returned in the response, it means you are on the first page of results. |
| `meta.next_token` | string | Pagination token for the next page of results. This value is returned when there are multiple pages of results, as the current request may only return a subset of results. To retrieve the full list, keep passing the value from this field in the `pagination_token` query parameter. When this field is not returned in the response, it means you've reached the last page of results, and that there are no further pages. |

GET /2/lists/:id/members

GET /2/lists/:id/members
========================

Returns a list of users who are members of the specified List.

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Try a live request ❯](https://oauth-playground.glitch.me/?id=listGetMembers&params=%28%27query%21%28%29%7Ebody%21%27%27%7Epath%21%28%29%29_) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Flists%2F%7Bid%7D%2Fmembers&method=get) 

### Endpoint URL

`https://api.twitter.com/2/lists/:id/members`  
  

### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 2.0 App-only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only "Use this method to obtain information in the context of an unauthenticated public user. This method is for developers that just need read-only access to public information. Click to learn how to obtain an OAuth 2.0 App Access Token.")<br><br>[OAuth 1.0a](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) is also available for this endpoint.<br><br>[OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code "This method allows an authorized app to act on behalf of the user, as the user. It is typically used to access or post public information for a specific user, and it us useful when your app needs to be aware of the relationship between a user and what this endpoint returns. Click to learn how to authenticate with OAuth 2.0 Authorization Code with PKCE.") |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | App rate limit (Application-only): 900 requests per 15-minute window shared among all users of your app<br><br>User rate limit (User context): 900 requests per 15-minute window per each authenticated user |

### OAuth 2.0 scopes required by this endpoint

|     |
| --- |
| `tweet.read`<br><br>`users.read`<br><br>`list.read` |
| [Learn more about OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/twitter-api/oauth2) |

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Required | string | The ID of the List whose members you would like to retrieve. |

  
  

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| `expansions`  <br> Optional | enum (`pinned_tweet_id`) | [Expansions](https://developer.twitter.com/en/docs/twitter-api/expansions) enable you to request additional data objects that relate to the originally returned users. The ID that represents the expanded data object will be included directly in the user data object, but the expanded object metadata will be returned within the `includes` response object, and will also include the ID so that you can match this data object to the original Tweet object. At this time, the only expansion available to endpoints that primarily return user objects is `expansions=pinned_tweet_id`. You will find the expanded Tweet data object living in the `includes` response object. |
| `max_results`  <br> Optional | integer | The maximum number of results to be returned per page. This can be a number between 1 and 100. By default, each page will return 100 results. |
| `pagination_token`  <br> Optional | string | Used to request the next page of results if all results weren't returned with the latest request, or to go back to the previous page of results. To return the next page, pass the next\_token returned in your previous response. To go back one page, pass the previous\_token returned in your previous response. |
| `tweet.fields`  <br> Optional | enum (`attachments`, `author_id`, `context_annotations`, `conversation_id`, `created_at`, `edit_controls`, `entities`, `geo`, `id`, `in_reply_to_user_id`, `lang`, `non_public_metrics`, `public_metrics`, `organic_metrics`, `promoted_metrics`, `possibly_sensitive`, `referenced_tweets`, `reply_settings`, `source`, `text`, `withheld`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [Tweet fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) will deliver in each returned pinned Tweet. Specify the desired fields in a comma-separated list without spaces between commas and fields. The Tweet fields will only return if the user has a pinned Tweet and if you've also included the `expansions=pinned_tweet_id` query parameter in your request. While the referenced Tweet ID will be located in the original Tweet object, you will find this ID and all additional Tweet fields in the `includes` data object. |
| `user.fields`  <br> Optional | enum (`created_at`, `description`, `entities`, `id`, `location`, `most_recent_tweet_id`, `name`, `pinned_tweet_id`, `profile_image_url`, `protected`, `public_metrics`, `url`, `username`, `verified`, `withheld`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [user fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) will deliver with the users object. Specify the desired fields in a comma-separated list without spaces between commas and fields. These specified user fields will display directly in the user data objects. |

  
  

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript (Default fields)](#tab0)
* [TypeScript (Optional fields)](#tab1)
* [Java (Default fields)](#tab2)
* [Java (Optional fields)](#tab3)

TypeScript (Default fields)

TypeScript (Optional fields)

Java (Default fields)

Java (Optional fields)

      `(async () => {   try {     const getMembers = await twitterClient.users.listGetMembers(       //The ID of the List for which to return members       84839422     );     console.dir(getMembers, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `(async () => {   try {     const getMembers = await twitterClient.users.listGetMembers(       //The ID of the List for which to return members       84839422,       {         //A comma separated list of fields to expand         expansions: ["pinned_tweet_id"],          //The maximum number of results         max_results: 5,          //A comma separated list of User fields to display         "user.fields": ["username"],       }     );     console.dir(getMembers, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  // String | The ID of the List for which to return members String id = "84839422";  try {     ListLookupMultipleUsersLookupResponse result = apiInstance.users().listGetMembers(id, null, null, null, null, null);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling UsersApi#listGetMembers");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

      `// Set the params values // For full list of params visit - https://github.com/twitterdev/twitter-api-java-sdk/blob/main/docs/UsersApi.md#listGetMembers  // String | The ID of the List for which to return members String id = "84839422";  // Integer | The maximum number of results Integer maxResults = 5;  // Set<String> | A comma separated list of fields to expand Set<String> expansions = new HashSet<>(Arrays.asList("pinned_tweet_id"));  // Set<String> | A comma separated list of User fields to display Set<String> userFields = new HashSet<>(Arrays.asList("username"));  try {     ListLookupMultipleUsersLookupResponse result = apiInstance.users().listGetMembers(id, maxResults, null, expansions, null, userFields);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling UsersApi#listGetMembers");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

### Example responses

* [Default fields](#tab0)
* [Optional fields](#tab1)

Default fields

Optional fields

      `{   "data": [     {       "id": "1319036828964454402",       "name": "Birdwatch",       "username": "birdwatch"     },     {       "id": "1244731491088809984",       "name": "Twitter Thailand",       "username": "TwitterThailand"     },     {       "id": "1194267639100723200",       "name": "Twitter Retweets",       "username": "TwitterRetweets"     },     {       "id": "1168976680867762177",       "name": "Twitter Able",       "username": "TwitterAble"     },     {       "id": "1065249714214457345",       "name": "Spaces",       "username": "TwitterSpaces"     }   ],   "meta": {     "result_count": 5,     "next_token": "5676935732641845249"   } }`
    

      `{   "data": [     {       "name": "Birdwatch",       "id": "1319036828964454402",       "username": "birdwatch",       "pinned_tweet_id": "1353789891348475905"     },     {       "name": "Twitter Thailand",       "id": "1244731491088809984",       "username": "TwitterThailand"     },     {       "name": "Twitter Retweets",       "id": "1194267639100723200",       "username": "TwitterRetweets"     },     {       "name": "Twitter Able",       "id": "1168976680867762177",       "username": "TwitterAble"     },     {       "name": "Spaces",       "id": "1065249714214457345",       "username": "TwitterSpaces",       "pinned_tweet_id": "1451239134798942208"     }   ],   "includes": {     "tweets": [       {         "id": "1353789891348475905",         "text": "Want to help build a new community-driven approach to tackling misleading information? Join us — sign up for Birdwatch! nnhttps://t.co/FSsqNznPy1"       },       {         "id": "1451239134798942208",         "text": "the time has arrived -- we’re now rolling out the ability for everyone on iOS and Android to host a Spacennif this is your first time hosting, welcome! here’s a refresher on how https://t.co/cLH8z0bocy"       }     ]   },   "meta": {     "result_count": 5,     "next_token": "5676935732641845249"   } }`
    

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

Pinning lists allows Twitter users to more easily access lists that they've either subscribed to or created themselves.

Since you are making requests on behalf of a user with the these endpoints, you must authenticate them with either [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) or [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code), and use the user Access Tokens associated with a user that has authorized your App, which can be generated using the [3-legged OAuth flow](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens) (OAuth 1.0a) or the [Authorization Code with PKCE grant flow](https://developer.twitter.com/en/docs/authentication/oauth-2-0/user-access-token) (OAuth 2.0).  

### Pinned List lookup

Pinned List lookup has one available endpoint that allows you to retrieve an authenticated user's pinned Lists. There is a rate limit of 15 requests per 15 minutes for this endpoint.  
 

### Manage pinned Lists

The manage pinned List endpoints allow you to pin and unpin a List on behalf of an authenticated user. For these endpoints, there are two methods available: POST and DELETE. The POST method allows you to pin a List, and the DELETE method allows you to unpin a List. There is a user rate limit of 50 requests per 15 minutes for both endpoints.

**Account setup**

To access these endpoints, you will need:

* An approved [developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info).
* To authenticate using the keys and tokens from a [developer App](https://developer.twitter.com/en/docs/apps) that is located within a [Project](https://developer.twitter.com/en/docs/projects). 

Learn more about getting access to the Twitter API v2 endpoints in our [getting started guide](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api).

[Quick start](https://developer.twitter.com/en/docs/twitter-api/lists/pinned-lists/quick-start)

[Sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code)

[Run in Postman](https://t.co/twitter-api-postman)

[Try with API Explorer](https://developer.twitter.com/apitools/api?endpoint=/2/users/%7Bid%7D/pinned_lists&method=get)

Supporting resources
--------------------

[Learn how to use Postman to make requests](https://developer.twitter.com/en/docs/tutorials/postman-getting-started "Learn how to use Postman to make requests")

[Troubleshoot an error](https://developer.twitter.com/en/support/twitter-api "Troubleshoot an error")

[Visit the API reference page for this endpoint](https://developer.twitter.com/en/docs/twitter-api/lists/pinned-lists/api-reference "Visit the API reference page for this endpoint")

Quick start

Getting started with the pinned List endpoint group
---------------------------------------------------

This quick overview will help you make your first request to the pinned List endpoints using [Postman](https://developer.twitter.com/en/docs/tools-and-libraries/using-postman).

Please visit our [Twitter API v2 sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code) GitHub repository if you want to see sample code in different languages.

### Prerequisites

To complete this guide, you will need to have a set of [keys and tokens](https://developer.twitter.com/en/docs/authentication) to authenticate your request. You can generate these keys and tokens by following these steps:

* [Sign up for a developer account](https://developer.twitter.com/en/apply-for-access) and receive approval.
* Create a [Project](https://developer.twitter.com/en/docs/projects) and an associated [developer App](https://developer.twitter.com/en/docs/apps) in the developer portal.
* Navigate to your App's “Keys and tokens” page to generate the required credentials. Make sure to save all credentials in a secure location.

Load the Twitter API v2 Postman collection  

---------------------------------------------

To load the Twitter API v2 Postman collection into your workspace, please click on the following button:

[Add Twitter API v2 to Postman](https://t.co/twitter-api-postman)

  
 

#### Authenticate your request

To make a successful request to **lookup** endpoints, you can use either [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a), [OAuth 2.0 App-Only](https://developer.twitter.com/en/docs/authentication/oauth-2-0), or [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code). However, with **manage** endpoints, you can only authenticate with OAuth 1.0a User Context or OAuth 2.0 Authorization Code with PKCE.

Regardless, when using Postman, the default authentication keys and tokens will automatically populate in your requests as long as you've set up your environment properly. 

You can do this by selecting the environment named “Twitter API v2” (in the top-right corner of Postman), and adding your keys and tokens to the "initial value" and "current value" fields (by clicking the eye icon next to the environment dropdown). These keys include the following:

* API Key (also known as Consumer Key)
* API Secret Key (also known as Consumer Secret)
* OAuth 1.0a user Access Token
* OAuth 1.0a user Access Token Secret
* OAuth 2.0 App Access Token
* OAuth 2.0 Client Key (only available if you've set up OAuth 2.0 User Authentication settings in your App's settings)
* OAuth 2.0 Client Secret (only available if you've set up OAuth 2.0 User Authentication settings in your App's settings)

Next steps
----------

Choose any of the following endpoints for a more in-depth guide once, you have completed the prerequisites:

[Pinned List lookup](https://developer.twitter.com/en/docs/twitter-api/lists/pinned-lists/quick-start/pinned-list-lookup "Pinned List lookup")

[Manage Pinned Lists](https://developer.twitter.com/en/docs/twitter-api/lists/pinned-lists/quick-start/manage-pinned-lists "Manage Pinned Lists")

Pinned List lookup

**Please note:** This guide assumes you have completed the prerequisites from the [quick start overview](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/lists/pinned-lists/quick-start).

### Steps to build a pinned List lookup request

#### Step one: Choose the List endpoint collection from Postman

Once you have the Twitter API v2 collection loaded in Postman, navigate to the “List” folder, select another folder “Pinned Lists”, and then choose "User's pinned Lists".  
 

#### Step two: Identify and specify the user

In order to retrieve a user’s pinned List, you must specify their user ID within the request. The user ID must correspond to the authenticating user’s ID, meaning that you must pass the Access Tokens associated with the user ID when authenticating your request. In this example, you can specify the ID belonging to your own user. You can find your ID in two ways:

1. Using the [users lookup](https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference) by username endpoint, you can pass a username and receive the id field.
2. Looking at your Access Token, you will find that the numeric part is your user ID.

In Postman, navigate to the "Params" tab and enter this user ID into the "Value" column of the `id` parameter.

|     |     |
| --- | --- |
| **Key** | **Value** |
| `id` | 2244994945 (user ID) |

#### Step three: Identify and specify which fields you would like to retrieve

If you click the "Send" button after step three, you will receive the default [List object](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/lists) fields in your response: `id` and `name`.

If you would like to receive additional fields beyond `id` and `name`, you will have to specify those fields in your request with the [`field`](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/data-dictionary/introduction/fields) and/or [`expansion`](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/introduction/expansions) parameters.

For this exercise, we will request a three additional sets of fields from different objects:

* The additional `follower_count` field in the primary List object.
* The full [user object](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) using the expansion parameter.
* The additional  `tweet.created_at` field in the associated user object.
    

In Postman, navigate to the "Params" tab and add the following key:value pair to the "Query Params" table:

|     |     |     |
| --- | --- | --- |
| Key | Value | Returned fields |
| list.fields | follower\_count | `follower_count` |
| expansions | owner\_id | `includes.users.id,   includes.users.name,   includes.users.username` |
| user.fields | created\_at | `includes.users.created_at` |

You should now see a similar URL next to the “Send” button:

      `https://api.twitter.com/2/users/2244994945/pinned_lists?expansions=owner_id&list.fields=follower_count&user.fields=created_at`
    

Step four: Make your request and review your response  

Once you have everything set up, hit the "Send" button, and you will receive a similar response to the following example response:

      `{   "data": [     {       "follower_count": 0,       "id": "1454155907651158017",       "name": "test list",       "owner_id": "2244994945"     }   ],   "includes": {     "users": [       {         "username": "TwitterDev",         "id": "2244994945",         "created_at": "2013-12-14T04:35:55.000Z",         "name": "Twitter Dev"       }     ]   },   "meta": {     "result_count": 1   } }`
    

Next steps
----------

[Customize your request using the API Reference](https://developer.twitter.com/en/docs/twitter-api/lists/pinned-lists/api-reference "Customize your request using the API Reference")

[Reach out to the community for help](https://twittercommunity.com/ "Reach out to the community for help")

Manage pinned List

**Please note:** This guide assumes you have completed the prerequisites from the [quick start overview](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/lists/pinned-lists/quick-start).

### Steps to build a manage pinned List request

#### Step one: Choose the List endpoint collection from Postman

Once you have the Twitter API v2 collection loaded in Postman, navigate to the “List” folder, select another folder “Pinned Lists”, and then choose "Pin a List".  
 

#### Step two: Specify the List to pin

Manage pinned List endpoints require two IDs: one for the user (the authenticated user to pin a List) and the target List (the List to be pinned). The user’s ID must correspond to the authenticating user’s ID, meaning that you must pass the Access Tokens associated with the user ID when authenticating your request. In this case, you can specify the ID belonging to your user. You can find your ID in two ways:

1. Using the [users lookup](https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference) by username endpoint, you can pass a username and receive the id field.
2. Looking at your Access Token, you will find that the numeric part is your user ID.

The target List ID can be any valid list. In Postman, navigate to the "Params" tab, and enter the user ID into the "Value" column of the id path variable. Navigate to the “Body” tab and ID of the List you wish to pin as the value for the list\_id  parameter. Be sure not to include any spaces before or after any ID.

|     |     |     |
| --- | --- | --- |
| **Key** | **Value** | **Parameter type** |
| `id` | The user ID | path |
| list\_id | The target List ID to be pinned | body |

You should now see a similar URL next to the "Send" button:

      `https://api.twitter.com/2/users/2244994945/pinned_lists`
    

Step three: Make your request and review your response  

Once you have everything set up, hit the "Send" button, and you will receive a similar response to the following example response:

      `{   "data": {     "pinned": true   } }`
    

You have successfully pinned the target List if the returned response object contains a true value for the key pinned. 

To unpin a List, select the Unpin List” request also found in the “Lists” folder of the Twitter API v2 collection loaded in Postman. This endpoint requires the authenticated user ID and the ID of the List to be unpinned. In the “Params” tab, enter the user ID as the value for the id column and ID of the List to be unpinned as the value for the  list\_id column. 

On successful delete request, you will receive a response similar to the following example:

      `{   "data": {     "pinned": false   } }`
    

Next steps
----------

[Customize your request using the API Reference](https://developer.twitter.com/en/docs/twitter-api/lists/pinned-lists/api-reference "Customize your request using the API Reference")

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

All Twitter API v2 endpoints require you to authenticate your requests with a set of credentials, also known as keys and tokens. You can use OAuth 1.0a User Context to authenticate your requests to this endpoint. 

[OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a), which means that you must use a set of API Keys and user Access Tokens to make a successful request. The access tokens must be associated with the user that you are making the request on behalf of. If you would like to generate a set of Access Tokens for another user, they must authorize your App using the [3-legged OAuth flow](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens).

Please note that OAuth 1.0a can be difficult to use. If you are not familiar with this authentication method, we recommend that you use a [library](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries), use a tool like Postman.

#### Developer portal, Projects, and developer Apps

To retrieve a set of authentication credentials that will work with the Twitter API v2 endpoints, you must [sign up for a developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info), set up a [Project](https://developer.twitter.com/en/docs/projects) within that account, and created a [developer App](https://developer.twitter.com/en/docs/apps) within that Project. You can then find your keys and tokens within your developer App.  
 

#### Rate limits

Every day, many thousands of developers make requests to the Twitter API. To help manage the sheer volume of these requests, [rate limits](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/rate-limits) are placed on each endpoint that limits the number of requests you can make on behalf of your app or on behalf of an authenticated user. 

These endpoints are rate limited at the user level, meaning that the authenticated user that you are making the request on behalf of can only call the endpoint a certain number of times across any developer App. 

The chart below shows the rate limits for each endpoint.

|     |     |     |
| --- | --- | --- |
| **Endpoint** | **HTTP method** | **Rate limit** |
| /2/users/:id/pinned\_lists | POST | 50 requests per 15 minutes |
| /2/users/:id/pinned\_lists/:list\_id | DELETE | 50 requests per 15 minutes |
| /2/users/:id/pinned\_lists | GET | 15 requests per 15 minutes |

#### Fields and expansions

The Twitter API v2 GET endpoint allows users to select exactly which data they want to return from the API using a set of tools called `fields` and `expansions`. The `expansions` parameter allows you to expand objects referenced in the payload. For example, looking up pinned Lists allows you to pull the following [expansions](https://developer.twitter.com/en/docs/twitter-api/expansions):

* `owner_id`
    

The `fields` parameter allows you to select exactly which [fields](https://developer.twitter.com/en/docs/twitter-api/fields) within the different data objects you would like to receive. This endpoint delivers user objects primarily. By default, the List object returns the `id`, and `name` fields. To receive additional fields such as `list.created_at` or `list.description`, you will have to specifically request those using a fields parameter. 

We’ve added a guide on using [fields and expansions](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/using-fields-and-expansions) together to our [Twitter API v2 data dictionary](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/introduction).

 The chart below shows the field and expansions available for the lookup endpoint:

|     |     |     |
| --- | --- | --- |
| **Endpoint** | **Fields** | **Expansions** |
| /2/users/:id/pinned\_lists | `list.fields`<br><br>`user.fields` | `owner_id` |

Next steps
----------

[Visit the API reference page for these endpoint](https://developer.twitter.com/en/docs/twitter-api/lists/pinned-lists/api-reference "Visit the API reference page for these endpoint")

API reference

API reference index
-------------------

For the complete API reference, select an endpoint from the list.  
  

### Pinned List lookup  

|     |     |
| --- | --- |
| **Returns the pinned Lists of the authenticated user** | `[GET /2/users/:id/pinned_lists](https://developer.twitter.com/en/docs/twitter-api/lists/pinned-lists/api-reference/get-users-id-pinned_lists)` |

### Manage pinned List  

|     |     |
| --- | --- |
| **Pins a List on behalf of an authenticated user** | `[POST /2/users/:id/pinned_lists](https://developer.twitter.com/en/docs/twitter-api/lists/pinned-lists/api-reference/post-users-id-pinned-lists)` |
| **Unpins a List on behalf of an authenticated user** | `[DELETE /2/users/:id/pinned_lists/:list_id](https://developer.twitter.com/en/docs/twitter-api/lists/pinned-lists/api-reference/delete-users-id-pinned-lists-list_id)` |

POST /2/users/:id/pinned\_lists

POST /2/users/:id/pinned\_lists
===============================

Enables the authenticated user to pin a List.

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Try a live request ❯](https://oauth-playground.glitch.me/?id=listUserPin&params=%28%27query%21%28%29%7Ebody%21%27%27%7Epath%21%28%29%29_) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Fusers%2F%7Bid%7D%2Fpinned_lists&method=post) 

### Endpoint URL

`https://api.twitter.com/2/users/:id/pinned_lists`  
  

### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 1.0a](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) is also available for this endpoint.<br><br>[OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code "This method allows an authorized app to act on behalf of the user, as the user. It is typically used to access or post public information for a specific user, and it us useful when your app needs to be aware of the relationship between a user and what this endpoint returns. Click to learn how to authenticate with OAuth 2.0 Authorization Code with PKCE.") |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | User rate limit (User context): 50 requests per 15-minute window per each authenticated user |

### OAuth 2.0 scopes required by this endpoint

|     |
| --- |
| `tweet.read`<br><br>`users.read`<br><br>`list.write` |
| [Learn more about OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/twitter-api/oauth2) |

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Required | string | The user ID who you are pinning a List on behalf of. It must match your own user ID or that of an authenticating user, meaning that you must pass the [Access Tokens](https://developer.twitter.com/en/docs/authentication/oauth-2-0/user-access-token) associated with the user ID when authenticating your request. |

  
  

### JSON body parameters

| Name | Type | Description |
| --- | --- | --- |
| `list_id`  <br> Required | string | The ID of the List that you would like the user `id` to pin. |

  
  

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript](#tab0)
* [Java](#tab1)

TypeScript

Java

      `(async () => {   try {     const pinList = await twitterClient.lists.listUserPin(       //The ID of the authenticated source user that will pin the List       2244994945,              //The ID of the List to be pinned       1441162269824405510     );     console.dir(pinList, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  // String | The ID of the List to be pinned String listsId = "1441162269824405510"; ListPinRequest listPinRequest = new ListPinRequest(); listPinRequest.listId(listsId);  // String | The ID of the authenticated source user that will pin the List String id = "2244994945";   try {     ListPinnedResponse result = apiInstance.lists().listUserPin(listPinRequest, id);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling ListsApi#listUserPin");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

### Example responses

* [Successful response](#tab0)

Successful response

      `{   "data": {     "pinned": true   } }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `pinned` | boolean | Indicates whether the user pinned the specified List as a result of the request. |

DELETE /2/users/:id/pinned\_lists/:list\_id

DELETE /2/users/:id/pinned\_lists/:list\_id
===========================================

Enables the authenticated user to unpin a List.

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Try a live request ❯](https://oauth-playground.glitch.me/?id=listUserUnpin&params=%28%27query%21%28%29%7Ebody%21%27%27%7Epath%21%28%29%29_) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Fusers%2F%7Bid%7D%2Fpinned_lists%2F%7Blist_id%7D&method=delete) 

### Endpoint URL

`https://api.twitter.com/2/users/:id/pinned_lists/:list_id`  
  

### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 1.0a](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) is also available for this endpoint.<br><br>[OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code "This method allows an authorized app to act on behalf of the user, as the user. It is typically used to access or post public information for a specific user, and it us useful when your app needs to be aware of the relationship between a user and what this endpoint returns. Click to learn how to authenticate with OAuth 2.0 Authorization Code with PKCE.") |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | User rate limit (User context): 50 requests per 15-minute window per each authenticated user |

### OAuth 2.0 scopes required by this endpoint

|     |
| --- |
| `tweet.read`<br><br>`users.read`<br><br>`list.write` |
| [Learn more about OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/twitter-api/oauth2) |

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Required | string | The user ID who you are unpin a List on behalf of. It must match your own user ID or that of an authenticating user, meaning that you must pass the [Access Tokens](https://developer.twitter.com/en/docs/authentication/oauth-2-0/user-access-token) associated with the user ID when authenticating your request. |
| `list_id`  <br> Required | string | The ID of the List that you would like the user `id` to unpin. |

  
  

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript](#tab0)
* [Java](#tab1)

TypeScript

Java

      `(async () => {   try {     const unpinList = await twitterClient.lists.listUserUnpin(       //The ID of the authenticated source user that will remove the pinned List       2244994945,        //The ID of the List to unpin       1441162269824405510     );     console.dir(unpinList, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  // String | The ID of the authenticated source user that will remove the pinned List String id = "2244994945";   // String | The ID of the List to unpin String listId = "1441162269824405510"; try {     ListPinnedResponse result = apiInstance.lists().listUserUnpin(id, listId);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling ListsApi#listUserUnpin");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

### Example responses

* [Successful response](#tab0)

Successful response

      `{   "data": {     "pinned": false   } }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `pinned` | boolean | Indicates whether the user unpinned the specified List as a result of the request. |

GET /2/users/:id/pinned\_lists

GET /2/users/:id/pinned\_lists
==============================

Returns the Lists pinned by a specified user.

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Try a live request ❯](https://oauth-playground.glitch.me/?id=listUserPinnedLists&params=%28%27query%21%28%29%7Ebody%21%27%27%7Epath%21%28%29%29_) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Fusers%2F%7Bid%7D%2Fpinned_lists&method=get) 

### Endpoint URL

`https://api.twitter.com/2/users/:id/pinned_lists`  
  

### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code "This method allows an authorized app to act on behalf of the user, as the user. It is typically used to access or post public information for a specific user, and it us useful when your app needs to be aware of the relationship between a user and what this endpoint returns. Click to learn how to authenticate with OAuth 2.0 Authorization Code with PKCE.")<br><br>[OAuth 1.0a](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) is also available for this endpoint. |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | User rate limit (User context): 15 requests per 15-minute window per each authenticated user |

### OAuth 2.0 scopes required by this endpoint

|     |
| --- |
| `tweet.read`<br><br>`users.read`<br><br>`list.read` |
| [Learn more about OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/twitter-api/oauth2) |

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Required | string | The user ID whose pinned Lists you would like to retrieve. The user’s ID must correspond to the user ID of the authenticating user, meaning that you must pass the [Access Tokens](https://developer.twitter.com/en/docs/authentication/oauth-2-0/user-access-token) associated with the user ID when authenticating your request. |

  
  

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| `expansions`  <br> Optional | enum (`owner_id`) | [Expansions](https://developer.twitter.com/en/docs/twitter-api/expansions) enable you to request additional data objects that relate to the originally returned List. The ID that represents the expanded data object will be included directly in the List data object, but the expanded object metadata will be returned within the `includes` response object, and will also include the ID so that you can match this data object to the original user object. At this time, the only expansion available to endpoints that primarily return List objects is `expansions=owner_id`. You will find the expanded user data object living in the `includes` response object. |
| `list.fields`  <br> Optional | enum (`created_at`, `follower_count`, `member_count`, `private`, `description`, `owner_id`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [List fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/lists) will deliver with each returned List objects. Specify the desired fields in a comma-separated list without spaces between commas and fields. These specified List fields will display directly in the List data objects. |
| `user.fields`  <br> Optional | enum (`created_at`, `description`, `entities`, `id`, `location`, `most_recent_tweet_id`, `name`, `pinned_tweet_id`, `profile_image_url`, `protected`, `public_metrics`, `url`, `username`, `verified`, `withheld`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [user fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) will deliver with the users object. Specify the desired fields in a comma-separated list without spaces between commas and fields. The user fields will only be returned if you have included `expansions=owner_id` query parameter in your request. You will find this ID and all additional user fields in the `included` data object. |

  
  

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript (Default fields)](#tab0)
* [TypeScript (Optional fields)](#tab1)
* [Java (Default fields)](#tab2)
* [Java (Optional fields)](#tab3)

TypeScript (Default fields)

TypeScript (Optional fields)

Java (Default fields)

Java (Optional fields)

      `(async () => {   try {     const getPinnedLists = await twitterClient.lists.listUserPinnedLists(       //The ID of the user for whom to return results       2244994945     );     console.dir(getPinnedLists, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `(async () => {   try {     const getPinnedLists = await twitterClient.lists.listUserPinnedLists(       //The ID of the user for whom to return results       2244994945,       {         //A comma separated list of fields to expand         expansions: ["owner_id"],          //A comma separated list of List fields to display         "list.fields": ["follower_count"],          //A comma separated list of User fields to display         "user.fields": ["created_at"],       }     );     console.dir(getPinnedLists, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  // String | The ID of the user for whom to return results String id = "2244994945";  try {     MultiListNoPaginationResponse result = apiInstance.lists().listUserPinnedLists(id, listFields, expansions, userFields);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling ListsApi#listUserPinnedLists");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

      `// Set the params values  // String | The ID of the user for whom to return results String id = "2244994945";  // Set<String> | A comma separated list of List fields to display Set<String> listFields = new HashSet<>(Arrays.asList("follower_count"));   // Set<String> | A comma separated list of fields to expand Set<String> expansions = new HashSet<>(Arrays.asList("owner_id"));  // Set<String> | A comma separated list of User fields to display Set<String> userFields = new HashSet<>(Arrays.asList("created_at"));  try {     MultiListNoPaginationResponse result = apiInstance.lists().listUserPinnedLists(id, listFields, expansions, userFields);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling ListsApi#listUserPinnedLists");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

### Example responses

* [Default fields](#tab0)
* [Optional fields](#tab1)

Default fields

Optional fields

      `{   "data": [     {       "id": "1451305624956858369",       "name": "Test List"     }   ],   "meta": {     "result_count": 1   } }`
    

      `{   "data": [     {       "follower_count": 0,       "id": "1451305624956858369",       "name": "Test List",       "owner_id": "2244994945"     }   ],   "includes": {     "users": [       {         "username": "TwitterDev",         "id": "2244994945",         "created_at": "2013-12-14T04:35:55.000Z",         "name": "Twitter Dev"       }     ]   },   "meta": {     "result_count": 1   } }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Default | string | Unique identifier of this List. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. |
| `name`  <br> Default | string | The name of this List. |
| `created_at` | date (ISO 8601) | Creation time of this List.  <br>  <br>To return this field, add `list.fields=created_at` in the request's query parameter. |
| `private` | boolean | Indicates if this List has been set to private. The List (in other words, if this is publicly viewed or not).  <br>  <br>To return this field, add `list.fields=private` in the request's query parameter. |
| `follower_count` | integer | Number of users who follow this List.  <br>  <br>To return this field, add `list.fields=follower_count` in the request's query parameter. |
| `member_count` | integer | Number of users who are a member of this List.  <br>  <br>To return this field, add `list.fields=member_count` in the request's query parameter. |
| `owner_id` | string | Unique identifier of this List's owner. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers.  <br>  <br>To return this field, add `list.fields=owner_id` in the request's query parameter. |
| `description` | string | A brief description of this List, if the owner provided one.  <br>  <br>To return this field, add `list.fields=description` in the request's query parameter. |
| `includes.users` | array | When including the `expansions=owner_id` parameter, this includes the referenced List owner in the form of a [user object](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) with their default fields and any additional fields requested using the `user.fields` parameter. |