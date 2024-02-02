
Search Tweets standard v1.1 to v2 migration guide | Docs | Twitter Developer Platform 

Standard v1.1 compared to Twitter API v2

Standard v1.1 compared to Twitter API v2
----------------------------------------

If you have been working with the v1.1 search/tweets, the goal of this guide is to help you understand the similarities and differences between the standard and Twitter API v2 search Tweets endpoint.

* **Similarities**
	+ OAuth 1.0a User Context and OAuth 2.0 App-Only
	+ Support for Tweet edit history and metadata.
* **Differences**
	+ Endpoint URLs
	+ App and Project requirements
	+ Response data format
	+ Request parameters
	+ New query operators
	+ AND / OR operator precedence

### Similarities

#### OAuth 1.0a User Context and OAuth 2.0 App-Only authentication

The v1.1 search/tweets and the Twitter API v2 recent search endpoint support both OAuth 1.0a User Context and OAuth 2.0 App-Only. 

Therefore, if you were previously using the standard v1.1 search endpoint you can continue using the same authentication method if you migrate to the Twitter API v2 version. 

Depending on your authentication library/package of choice, App-Only authentication is probably the easiest way to get started and can be set with a simple request header. To learn how to generate an App Access Token see this OAuth 2.0 App-Only guide. 

If you would like to take advantage of the ability to pull private or advertising metrics with the Twitter API v2 endpoint, you will need to use OAuth 1.0a User Context, and pass the user access tokens related to the user who posted the Tweet for which you would like to pull metrics. 

**Support for Tweet edit history and metadata**

Both versions provide metadata that describes any edit history. Check out the search API References and the Tweet edits fundamentals page for more details. 

### Differences

#### Endpoint URLs

* Standard v1.1 endpoints:
	+ https://api.twitter.com/1.1/search/tweets
* Twitter API v2 endpoint:
	+ https://api.twitter.com/2/tweets/search/recent

#### App and Project requirements

The Twitter API v2 endpoints require that you use credentials from a developer App that is associated to a Project when authenticating your requests. All Twitter API v1.1 endpoints can use credentials from standalone Apps or Apps associated with a Project.   

#### Response data format

One of the biggest differences between standard v1.1 and Twitter API v2 endpoint versions is how you select which fields return in your payload.

For the standard endpoints, you receive many of the response fields by default, and then have the option to use parameters to identify which fields or sets of fields should return in the payload.

The Twitter API v2 version only delivers the Tweet id and text fields by default. To request any additional fields or objects, you will need to use the fields and expansions parameters. Any Tweet fields that you request from these endpoints will return in the primary Tweet object. Any expanded user, media, poll, or place objects and fields will return in an includes object within your response. You can then match any expanded objects back to the Tweet object by matching the IDs located in both the Tweet and the expanded object. 

We encourage you to read more about these new parameters in their respective guides, or by reading our guide on how to use fields and expansions. 

We have also put together a data format migration guide which can help you map standard v1.1 fields to the newer v2 fields. This guide will also provide you the specific expansion and field parameter that you will need to pass with your v2 request to return specific fields.   

In addition to the changes in how you request certain fields, Twitter API v2 is also introducing new JSON designs for the objects returned by the APIs, including Tweet and user objects.

* At the JSON root level, the standard endpoints return Tweet objects in a statuses array, while Twitter API v2 returns a data array.
* Instead of referring to Retweeted and Quoted "statuses", Twitter API v2 JSON refers to Retweeted and Quoted Tweets. Many legacy and deprecated fields, such as contributors and user.translator\_type are being removed.
* Instead of using both favorites (in Tweet object) and favourites (in user object), Twitter API v2 uses the term like.
* Twitter is adopting the convention that JSON values with no value (for example, null) are not written to the payload. Tweet and user attributes are only included if they have non-null values.

We also introduced a new set of fields to the Tweet object including the following:

* A conversation\_id field
* Two new annotations fields, including context and entities
* Several new metrics fields
* A new reply\_setting field, which shows you who can reply to a given Tweet

#### Request parameters

The following standard v1.1 request parameters have equivalents in Twitter API v2:

| Standard search v1.1 | Search Tweets v2 |
| --- | --- |
| q | query |
|  | start\_time (YYYY-MM-DDTHH:mm:ssZ) |
| until (YYYY-MM-DD) | end\_time (YYYY-MM-DDTHH:mm:ssZ) |
| since\_id | since\_id |
| max\_id | until\_id |
| count | max\_results |
| Response provides search\_metadata.next\_results | next\_token |

There are also a set of standard search Tweets request parameters **not** supported in Twitter API v2:  

| **Standard v1.1 parameter** | **Details** |
| geocode | Search Tweets at the Basic Access level does not support geo operators.  |
| locale | With standard search, this was used to specify the language of the query but never fully implemented.  |
| lang | Search Tweets endpoints provide a lang query operator for matching on languages of interest.  |
| include\_entities | Tweet entities are always included. |
| result\_type | Search Tweets endpoints deliver all matching Tweets, regardless of engagement level.  |
| extended | Twitter API v2 is built from the ground up to support Tweets with up to 280 characters. With v2, there is no concept of 'extended' Tweets.  |

Here is an example request that shows the difference between a Standard request and a Search Tweets request:

|  |  |
| --- | --- |
| **Standard v1.1** | **Twitter API v2** |
| https://api.twitter.com/1.1/search/tweets.json?q=snow&count=50 | https://api.twitter.com/2/tweets/search/recent?query=snow&max\_results=50 |

These requests will both return the 50 most recent Tweets that contain the keyword snow. The v2 request will return the default id and text fields of the matching Tweets. Here is an example of specifying additional Tweet and user fields to include in the JSON payload:

|  |
| --- |
| **Twitter API v2** |
| https://api.twitter.com/2/tweets/search/recent?query=snow&max\_results=50&tweet.fields=id,created\_at,author\_id,text,source,entities,attachments&user.fields=id,name,username,description |

#### **New query operators**

Search Tweets introduces new operators in support of two new Twitter API v2 features: 

* **Conversation IDs** - As conversations unfold on Twitter, a conservation ID will be available to mark Tweets that are part of the conversation. All Tweets in the conversation will have their conversation\_id set to the Tweet ID that started it.
	+ `conversation_id:`
* **Twitter Annotations** provide contextual information about Tweets, and include entity and context annotations. Entities are comprised of people, places, products and organizations. Contexts are domains, or topics, that surfaced entities are a part of. For example, people mentioned in a Tweet may have a context that indicates whether they are an athlete, actor, or politician.
	+ context: matches on Tweets that have been annotated with a context of interest.
	+ entity: matches on Tweets that have been annotated with an entity of interest.

#### AND / OR operator precedence

The basic building block for building search queries is the use of OR and AND logical groupings. The standard search API applies ORs before ANDs, while Search Tweets endpoints (as well as the premium and enterprise versions) applies ANDs before ORs. This difference is critical when translating queries between the two. 

For example, with standard search, if you wanted to match Tweets with the keyword ‘storm’ that mention the word ‘colorado’ or the #COwx hashtag, you could do that with the following search query:

storm #COwx OR colorado

With the Search Tweets operator precedence, ANDs are applied before ORs. So the above query is equivalent to: 

(storm #COwx) OR colorado

However, the above rule would match on any Tweets that mentions ‘Colorado’, regardless if the Tweet mentions ‘storm’ or the #COwx hashtag. In addition it would also  match Tweets that mentioned both the keyword ‘storm’ and the #COwx hashtag. 

To make the query behave as originally intended, the OR clauses need to be grouped together. The translation of the original standard query to Search Tweets would be:  

storm (#COwx OR colorado)

These two rules have very different matching behavior. For the month of October 2019, the original rule matches over 1,175,000 Tweets while the correctly translated rule matches around 5,600 Tweets. Be sure to mind your ANDs and ORs, and use parentheses where needed.   

### cURL requests

#### The following section displays cURL requests for the standard v1.1 endpoint and its equivalent endpoint in v2.

The requests are made using OAuth 2.0 App-Only. In order to run the following cURL requests, you will need to replace ACCESS\_TOKEN in the authorization header with your app access token. For v2 endpoints, your app access token must belong to a developer App within a Project. 

The response payload returned by the v1.1 endpoint will be different from the response payload returned by the v2 endpoint. With v2, the response will include the default fields, as well as any other fields requested with the fields and expansions parameters. You can use these parameters to request a different set of fields to be returned.  

**Standard v1.1 GET search/tweets and v2 GET tweets/search/recent endpoints**

```
      curl --request GET \
  --url 'https://api.twitter.com/1.1/search/tweets.json?q=from%3ATwitterDev%20-is%3Aretweet&count=100' \
  --header 'Authorization: Bearer $ACCESS_TOKEN'
```

Code copied to clipboard

```
      curl --request GET \
  --url 'https://api.twitter.com/2/tweets/search/recent?query=from%3ATwitterDev%20-is%3Aretweet&tweet.fields=created_at%2Cconversation_id%2Centities&max_results=100' \
  --header 'Authorization: Bearer $ACCESS_TOKEN'
```

Code copied to clipboard

Next steps
----------

Check out our quick start guide for Twitter API v2 recent search

Review the API reference for recent search

Check out some sample code for these endpoints

Step-by-step guide to making your first request to recent search

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