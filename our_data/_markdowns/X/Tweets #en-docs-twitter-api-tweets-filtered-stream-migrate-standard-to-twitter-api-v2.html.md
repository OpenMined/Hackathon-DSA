
Filtered stream - Standard v1.1 to Twitter API v2 migration guide | Docs | Twitter Developer Platform 

Standard v1.1 compared to Twitter API v2

Standard v1.1 compared to Twitter API v2
----------------------------------------

If you have been working with the v1.1 statuses/filter endpoint, this guide can help you understand the similarities and differences between the standard and Twitter API v2 filtered stream endpoints.

* **Similarities**
	+ Request parameters and operators
	+ Support for Tweet edit history and metadata
* **Differences**
	+ Endpoint URLs
	+ App and Project requirement
	+ Authentication method
	+ Rule volume and persistent stream
	+ Response data format
	+ Request parameters
	+ Availability of recovery and redundancy features
	+ Query operators

### Similarities

#### Request parameters and operators

The standard v1.1 statuses/filter endpoint features a few parameters that can be passed along with the request to filter the stream. With v2 filtered stream, you instead use a set of operators that can be connected together using boolean logic to filter for desired Tweets. The available operators include some that are direct replacements for the existing standard v1.1 parameters. 

The following standard v1.1 request parameters have equivalent operators in Twitter API v2:  

| **Standard** | **Twitter API v2** |
| follow - A comma-separated list of user IDs, indicating the users whose Tweets should be delivered on the stream. | Many operators that can help you find Tweets related to specific users:* @
* from:
* to:
* etc.
 |
| track - A comma-separated list of phrases which will be used to determine what Tweets will be delivered on the stream. | Many operators that can help you find Tweets related to specific keywords:* keyword
* "exact phrase match"
* #
* etc.
 |

**Support for Tweet edit history and metadata**  

Both versions provide metadata that describes any edit history. Check out the filtered stream API References and the Tweet edits fundamentals page for more details. 

### Differences

#### Endpoint URLs

* Standard v1.1 endpoints:
	+ https://stream.twitter.com/1.1/statuses/filter.json
* Twitter API v2 endpoint:
	+ https://api.twitter.com/2/tweets/search/stream
	+ https://api.twitter.com/2/tweets/search/stream/rule

#### App and Project requirements

The Twitter API v2 endpoints require that you use credentials from a developer App that is associated to a Project when authenticating your requests. All Twitter API v1.1 endpoints can use credentials from standalone Apps or Apps associated with a Project.

#### Authentication method

The standard endpoint supports OAuth 1.0a User Context, whereas the Twitter API v2 filtered stream endpoints supports OAuth 2.0 App-Only (also referred to as Application-only authentication). To make requests to the Twitter API v2 version you must use a App Access Token to authenticate your requests.

If you no longer have the App Access Token that was presented to you when you created your Project and app in the developer portal, you can generate a new one by navigating to your app's “Keys and tokens” page on the developer portal. If you’d like to generate an App Access Token programmatically, see this OAuth 2.0 App-Only guide. 

#### Rule volume and persistent stream

The standard v1.1 endpoint supports a single rule to filter the streaming connection. To change the rule, you have to disconnect the stream and submit a new request with the revised filtering rules submitted as parameters. 

The Twitter API v2 filtered stream endpoint allows you to apply multiple rules to a single stream and add and remove rules to your stream while maintaining the stream connection. 

#### Response data format

One of the biggest differences between standard v1.1 and Twitter API v2 endpoint versions is how you select which fields return in your payload.

For the standard endpoints, you receive many of the response fields by default, and then have the option to use parameters to identify which fields or sets of fields should return in the payload.

The Twitter API v2 version only delivers the Tweet id and text fields by default. To request any additional fields or objects, you wil need to use the fields and expansions parameters. Any Tweet fields that you request from these endpoints will return in the primary Tweet object. Any expanded user, media, poll, or place objects and fields will return in an includes object within your response. You can then match any expanded objects back to the Tweet object by matching the IDs located in both the Tweet and the expanded object. 

We encourage you to read more about these new parameters in their respective guides, or by reading our guide on how to use fields and expansions. 

We have also put together a data format migration guide which can help you map standard v1.1 fields to the newer v2 fields. This guide will also provide you the specific expansion and field parameter that you will need to pass with your v2 request to return specific fields.   

In addition to the changes in how you request certain fields, Twitter API v2 is also introducing new JSON designs for the objects returned by the APIs, including Tweet and user objects.

* At the JSON root level, the standard endpoints return Tweet objects in a statuses array, while Twitter API v2 returns a data array.
* Instead of referring to Retweeted and Quoted "statuses", Twitter API v2 JSON refers to Retweeted and Quoted Tweets. Many legacy and deprecated fields, such as contributors and user.translator\_type are being removed.
* Instead of using both favorites (in Tweet object) and favourites (in user object), Twitter API v2 uses the term like.
* Twitter is adopting the convention that JSON values with no value (for example, null) are not written to the payload. Tweet and user attributes are only included if they have a non-null values.

We also introduced a new set of fields to the Tweet object including the following:

* A conversation\_id field
* Two new annotations fields, including context and entities
* Several new metrics fields
* A new reply\_setting field, which shows you who can reply to a given Tweet

#### Request parameters

There are also a set of standard filtered stream request parameters **not** supported in Twitter API v2:  

| Standard v1.1 parameter | Details |
| --- | --- |
| locations - A comma-separated list of longitude,latitude pairs specifying a set of bounding boxes to filter Tweets by. | We have not released location-based operators for Twitter API v2 yet.  |
| Delimited | With the v1.1 endpoint, setting this to the string length indicates that statuses should be delimited in the stream, so that clients know how many bytes to read before the end of the status message.
This functionality is not available with Twitter API v2. |
| Stall\_warnings | With the v1.1 endpoint, setting this parameter to true will cause periodic messages to be delivered if the client is in danger of being disconnected. 
With Twitter API v2, stall warnings are sent by default with the new line sent every so often. |

#### 
Availability of recovery and redundancy features

The Twitter API v2 version of filtered stream introduces recovery and redundancy features that can help you maximize streaming up-time as well as recover any Tweets that might have been missed due to a disconnection that lasted five minutes or less.

Redundant connections allows you to connect to a given stream up to two times, which can help ensure that you maintain a connection to the stream at all times, even if one of your connections fails. 

The backfill\_minutes parameter can be used to recover up to five minutes of missed data. 

Both of these features are only available via Academic Research access. You can learn more about this functionality via our recovery and redundancy features integration guide. 

#### New query operators

Twitter API v2 introduces new operators in support of two new features: 

* **Conversation IDs** - As conversations unfold on Twitter, a conservation ID will be available to mark Tweets that are part of the conversation. All Tweets in the conversation will have their conversation\_id set to the Tweet ID that started it.
	+ conversation\_id:
* **Twitter Annotations** provide contextual information about Tweets, and include entity and context annotations. Entities are comprised of people, places, products and organizations. Contexts are domains, or topics, that surfaced entities are a part of. For example, people mentioned in a Tweet may have a context that indicates whether they are an athlete, actor, or politician.
	+ context: - matches on Tweets that have been annotated with a context of interest.
	+ entity: - matches on Tweets that have been annotated with an entity of interest.

Next steps
----------

Check out our quick start guide for Twitter API v2 filtered stream

Review the API reference for filtered stream

Check out some sample code for these endpoints

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