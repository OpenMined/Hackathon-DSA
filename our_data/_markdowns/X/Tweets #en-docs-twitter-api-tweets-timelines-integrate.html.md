
Timelines integration guide | Docs | Twitter Developer Platform 

Integrate

How to integrate with the Timelines endpoints
---------------------------------------------

This page contains information on several tools and key concepts that you should be aware of as you integrate the timelines endpoints into your system. We’ve split the page into the following sections:

* Helpful tools
* Key Concepts
	+ Authentication
	+ Developer portal, Projects, and Apps
	+ Rate limits
	+ Fields and expansions
	+ Tweet metrics
	+ Pagination
	+ Filtering results
	+ Tweet caps and volume of Tweets returned
	+ Edit Tweets
	+ Edge cases

### Helpful tools

Before we explore some key concepts, we recommend that you use one of the following tools or code samples to start testing the functionality of these endpoints.

#### Code samples

Interested in getting set up with these endpoints with some code in your preferred coding language? We’ve got a handful of different code samples available that you can use as a starting point on our GitHub page.

#### Libraries

Take advantage of one of our many community third-party libraries to help you get started. You can find a library that works with the v2 endpoints by looking for the proper version tag.

#### Postman

Postman is a great tool that you can use to test out these endpoints. Each Postman request includes every path and body parameter to help you quickly understand what is available to you. To learn more about our Postman collections, please visit our Using Postman page.  

### Key concepts

#### Authentication

All Twitter API v2 endpoints require requests to be authenticated with a set of credentials, also known as keys and tokens. You can use either OAuth 1.0a User Context or OAuth 2.0 Authorization Code with PKCE to authenticate requests to these endpoints. You can use OAuth 2.0 App-Only for user Tweets timeline and user mentions timeline.

OAuth 1.0a User Context requires you to utilize your API Keys, user Access Tokens, and a handful of other parameters to create an authorization header, which you will then pass with your request. The Access Tokens must be associated with the user that you are making the request on behalf of. If you would like to generate a set of Access Tokens for another user, they must authorize your App using the 3-legged OAuth flow. 

Please note that OAuth 1.0a can be difficult to use. If you are not familiar with this authentication method, we recommend that you use a library, use a tool like Postman, or use OAuth 2.0 to authenticate your requests. If you would like to request a Tweet or private metrics from these endpoints, you will need to use a either OAuth 1.0a User Context or OAuth 2.0 Authorization Code with PKCE, which will ensure that you have the proper permissions from the user that owns that content.

OAuth 2.0 App-Only just requires that you pass an OAuth 2.0 App Access Token with your request. You can either generate an App Access Token from directly within a developer App, or generate one using the POST oauth2/token endpoint. You can use this for user Tweets timeline or user mention timeline.

OAuth 2.0 Authorization Code with PKCE allows for greater control over an application’s scope, and authorization flows across multiple devices. OAuth 2.0 allows you to pick specific fine-grained scopes which give you specific permissions on behalf of a user. 

To enable OAuth 2.0 in your App, you must enable it in your’s App’s authentication settings found in the App settings section of the developer portal.

**Please note**

If you are requesting the following fields, OAuth 1.0a User Context or OAuth 2.0 Authorization Code is required: 

* `tweet.fields.non_public_metrics`
* `tweet.fields.promoted_metrics`
* `tweet.fields.organic_metrics`
* `media.fields.non_public_metrics`
* `media.fields.promoted_metrics`
* `media.fields.organic_metrics`

#### Developer portal, Projects, and developer Apps

To work with any Twitter API v2 endpoints, you must sign up for a developer account, set up a Project within that account, and created a developer App within that Project. Your keys and tokens within that developer App will work for these timelines endpoints.  

#### Rate limits

Every day, many thousands of developers make requests to the Twitter API. To help manage the volume, rate limits are placed on each endpoint that limits the number of requests that every developer can make on behalf of an app or on behalf of an authenticated user. 

There are different rate limits applied for these endpoints depending on which authentication method is being used. The app-level rate limits apply to an App making requests using OAuth 2.0 App-Only, whereas the user-level rate limit applies to requests being made on behalf of the specific authorizing user using OAuth 1.0a User Context. These two rate limits are based on the frequency of requests within a 15-minute window.  

For example, an app using OAuth 2.0 App-Only auth for both of these timelines endpoints, can make 1500 requests (including pagination requests) to the user Tweet timeline, and 450 requests (including pagination requests) to the user mention timeline within a 15-minute timeframe.  That same app, within the same 15-minute timeframe, with two different authorized users (using OAuth 1.0a User Context) can make 900 requests (including pagination requests) to the user Tweet timeline, and 180 requests (including pagination requests) to the user mention timeline for each authenticated user. 

Reverse chronological home timeline has a per-user rate limit of 180 requests per a 15 min window. With this endpoint you can return every Tweet created on a timeline over the last 7 days as well as the most recent 800 regardless of creation date.

#### Fields and expansions

The Twitter API v2 allows you to select exactly which data you want returned from the API using fields and expansions. The expansion parameter allows you to expand objects referenced in the payload. For example, this endpoint allows you to request poll, place, media, and other objects using the expansions parameter.

The fields parameter allows you to select exactly which fields within the different data objects you would like to receive. By default, the primary Tweet object returned by these endpoints include the id and text fields. To receive additional fields such as author\_id or public\_metrics, you will have to specifically request those using the fields parameters. Some important fields that you may want to consider using in your integration are our poll data, metrics, Tweet annotations, and conversation ID fields.

We’ve added a guide on how to use fields and expansions together to our Twitter API v2 data dictionary.  

#### Tweet metrics

The Twitter API v2 endpoints allow you to request Tweet metrics directly from the returned Tweet object, assuming you pass the proper fields with your request.

There are some limitations with Tweet metrics that you should be aware of, specifically related to user privacy and the following response fields:

* `tweet.fields.non_public_metrics`
* `tweet.fields.promoted_metrics`
* `tweet.fields.organic_metrics`
* `media.fields.non_public_metrics`
* `media.fields.promoted_metrics`
* `media.fields.organic_metrics`

The noted fields include private metrics data, meaning you must be authorized by the Tweet’s publisher to retrieve this data on their behalf when using the user Tweet timeline endpoint, meaning you must use OAuth 1.0a User Context or OAuth 2.0 Authorization Code Flow with PKCE.

For example, in order to receive non\_public\_metrics for user ID 1234's user Tweet timeline you will need to include access tokens associated with that user in your request. You can have users authorize your app and receive a set of access tokens associated with them by using the 3-legged OAuth flow. 

If you are using user mention timeline, the noted fields will not be available unless the mentioning author has authorized your App to access their private metrics data and you are using that user’s access tokens when making the request with OAuth 1.0a User Context.

All non\_public\_metrics, organic\_metrics, and promoted\_metrics are only available for Tweets created in the last 30 days. This means that when you are requesting the noted fields, the results will automatically adjust to only include Tweets from the last 30 days.

If these noted fields are requested, only Tweets that are authored by the authenticated user will be returned, all other Tweets will receive an error message.  

#### Pagination

These endpoints utilize pagination so that responses are returned quickly. In cases where there are more results than what can be sent in a single response (up to 100 Tweets for the timelines endpoints) you will need to paginate. Use the max\_results parameter to identify how many results will return per page, and the pagination\_token parameter return the next page of results. You can learn more by reviewing our pagination guide.  

#### Filtering results

These endpoints include several parameters that you can use to filter results. Using start\_date and end\_date, you can narrow down results to a specific timeframe. If you’d rather use Tweet IDs to select a specific set of Tweets, you can use the since\_id and until\_id. The user Tweets timeline also has an exclude parameter that can remove Retweets and Replies from your results.   

#### Tweet caps and volume of Tweets returned

The user Tweet timeline and user mention timeline endpoints are limited in the number of Tweets that they can return in a given month. The reverse chronological home timeline endpoint is not subject to this limitation.

Regardless of which timelines endpoint you use, the Tweets returned will count towards the Project-level Tweet caps. Usage is shown in the developer portal, and the 'month' starts on your subscription renewal day shown on the developer portal dashboard. 

The user Tweet timeline endpoint will only return the most recent 3200 Tweets posted to a user’s timeline. Setting start\_time and end\_time to a time period that includes Tweets beyond the 3200 most recent, you will receive a successful response, but no Tweets.

It is also important to note that, if you pass the excludes=replies with your user Tweet timeline requests, only the most recent 800 Tweets will be returned.

The user mention timeline endpoint will only return the most recent 800 Tweet mentions.

The reverse chronological home timeline endpoint returns the last 3200 Tweets.  

#### Tweet edits

Tweets that are eligible for edits can be edited up to five times in the 30 minutes after the original Tweet was published. The search endpoints will always provide the latest version of the Tweet. If you only request Tweets that were published 30 or more minutes ago, you will always receive the final version of the Tweet. However, if you have a near-real-time use case, and are querying Tweets published within the last thirty minutes, those Tweets could have been edited after you received them. These Tweets can be rehydrated with search, or the Tweet Lookup endpoint to confirm their final state. To learn more about how Tweet edits work, see the Edit Tweets fundamentals page.    

#### 

#### Edge cases

* When requesting non-public metrics on the User Tweet timeline endpoint for Tweets that are older than 30 days, you may see a next\_token in the response with a result count of 0. To avoid encountering this issue, ensure that the timeframe requested with the non\_public\_metrics parameter is within the most recent 30 days. Additionally, the max\_results minimum value should be 10. These may help to avoid this scenario, but this could still occur.
* Requesting promoted metrics for Tweets that were not promoted returns an empty response, instead of Tweet data. Our team is currently working on fixing this issue.

* For a Retweet that contains Tweet body text greater than 140 characters in length, the text field will be truncated instead of returning the full Tweet text. The short term workaround is to expand the referenced Tweet and retrieve the full text from the expansion. This is a bug that we will fix in the future.

Next steps
----------

Make your first request to a Timelines endpoint

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