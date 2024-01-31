Overview

Overview
--------

The latest version of the Twitter API v2 is a big deal. As such, we’ve broken this migration section into a few partitions:

|     |     |
| --- | --- |
| **[What’s new with Twitter API v2](https://developer.twitter.com/en/docs/twitter-api/migrate/whats-new)** | Learn about the new endpoints and functionality that we’ve released to Twitter API v2. |
| **[Ready to migrate?](https://developer.twitter.com/en/docs/twitter-api/migrate/ready-to-migrate)** | Get started with your migration with a set of guides and instructions. |
| **[Data format migration guide](https://developer.twitter.com/en/docs/twitter-api/migrate/data-formats)** | Learn how to rework your data parsers that previously worked with the standard v1.1, and enterprise data formats. |
| **[Twitter API endpoint map](https://developer.twitter.com/en/docs/twitter-api/migrate/twitter-api-endpoint-map)** | See how standard v1.1, and enterprise endpoints map to the new Twitter API v2 endpoints. |

What's new

What is the X API v2?  

------------------------

The X API v2 is now the primary X API, and is where product investment and innovation are focused. We’ve partnered with developers to build the next generation of the X API to better serve our diverse community of developers. Based on developer feedback, we’ve re-built the API to better serve a broader collection of needs, introduced new features and endpoints, and improved upon the developer experience.  

The X API v2 is now the primary X API, and is where product investment and innovation are focused. Over the past few years, we partnered with developers and re-built the API to better serve a broader collection of needs, introduce new features and endpoints, and improve upon the developer experience. We are committed to continuing to build an open developer platform, and are excited to see what you build with the X API v2.

Why migrate?
------------

The X API v2 is built with a modern and more sustainable foundation and includes both improved replacement endpoints for the standard v1.1, and enterprise products, but also net-new functionality. We strongly encourage customers of legacy APIs (v1.1, and enterprise) to begin to migrate to v2 as we do intend to deprecate them eventually. Use the X API to listen to and analyze the public conversation, engage with people on X, and innovate.  

In this section, we will discuss the endpoints and functionality.

### V2 endpoints

You can see a full list of v2 endpoints and their pre-v2 equivalent via the following guide:

[X API Endpoint Map](https://developer.twitter.com/en/docs/twitter-api/migrate/twitter-api-endpoint-map)

  
While most of the endpoints in X API v2 are replacements, we have introduced several new endpoints. Here are several examples of new endpoints that we’ve released to v2:

* [Spaces endpoints](https://developer.twitter.com/en/docs/twitter-api/spaces/overview) to help people get more out of X Spaces, and to allow developers to help shape the future of audio conversations.
* [Hide replies](https://developer.twitter.com/en/docs/twitter-api/tweets/hide-replies), which allows you to build tools that help limit the impact of abusive, distracting, or misleading replies at scale – a crucial piece to improving the health of the public conversation on X, and ensuring brands and people feel comfortable starting conversations.
* New Lists endpoints that allow you to [pin and unpin Lists](https://developer.twitter.com/en/docs/twitter-api/lists/pinned-lists/introduction), or look up someone’s pinned Lists
* New [batch compliance endpoints](https://developer.twitter.com/en/docs/twitter-api/compliance/batch-compliance/introduction) that allow you to ensure your stored user and Tweet data is in compliance.

New functionality
-----------------

X API v2 also includes new features that will help you find more value with the X API. A lot of what is new has been driven by your feedback, and includes certain features that were reserved for enterprise customers previously. 

Some of the improvements to the API include:

* [A consistent design across endpoints](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/consistency)
* [The ability specify which fields and objects return in the response payload](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/data-dictionary/using-fields-and-expansions)
* [New and more detailed data objects](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/data-dictionary/introduction)
* [Receive and filter data with new contextual information powered by Tweet annotations](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/annotations/overview)
* [Access to new metrics](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/metrics)
* [Easily identify and filter for conversations that belong to a reply thread](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/conversation-id)
* [Advanced functionality and increased access to data for academic researchers](https://developer.twitter.com/content/developer-twitter/en/products/twitter-api/academic-research)
* [Recovery and redundancy functionality for streaming endpoints](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/tweets/filtered-stream/integrate/recovery-and-redundancy-features)
* [Easily return counts of Tweets that match a query](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/tweets/counts/introduction)
* [Support for Edit Tweets](https://developer.twitter.com/en/docs/twitter-api/edit-tweets)
* High confidence spam filtering
* Shortened URLs are fully unwound for more effective filtering and analysis 
* Simplified JSON response objects by removing deprecated fields and modernizing labels
* Return of 100% of matching public and available Tweets in search queries
* Streaming "rules" so you can make changes without dropping connections
* More expressive query language for search Tweets, Tweet counts, and filtered stream
* OpenAPI spec to build new libraries & more transparently track changes  
      
    

Before you dive in, let’s cover some of the fundamental changes we’ve made to the way you will access and consume data from the endpoints.

### Discover new and updated response objects

The following six data objects are available with the v2 endpoints:

| **Object** | **Description** |
| --- | --- |
| **[Tweet](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet)** | The Tweet object has a long list of root-level fields, such as id, text, and created\_at. Tweet objects are also the parent object to several child objects including user, media, poll, and place. |
| **[User](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user)** | The user object contains X user account metadata describing the referenced user. |
| **[Spaces](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/space)** | The Space object consists of fields such as state, host\_id, is\_ticketed, and even lang. |
| **[Lists](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/space)** | The List object contains basic information about the requested list including description, member\_count, and owner\_id. |
| **[Media](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/media)** | If a Tweet contains media (such as images), then the media object can be requested using the media.fields parameter and includes fields such as the media\_key, type, url, preview\_image\_url, and more. |
| **[Poll](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/poll)** | A poll included in a Tweet is not a primary object on any endpoint, but can be found and expanded in the Tweet object. |
| **[Place](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/place)** | The place object consists of fields such as place\_id, geo object, country\_code, and more. This information can be used to identify Tweets and study Tweets by location. |

### Flexibility to choose which objects and fields you receive  

When making a request to a GET endpoint, you will receive the primary data object that relates to that endpoint, which will include a set of default fields. For example, the Tweet object delivers the id and text fields as its default. 

If you would like to retrieve additional fields with your request, you will have to use the [fields](https://developer.twitter.com/en/docs/twitter-api/fields) and [expansions](https://developer.twitter.com/en/docs/twitter-api/expansions) parameters. The expansions parameter enables you to retrieve related data objects such as a user's pinned Tweet or a media object, while the field operators enable you to request specific fields within returned objects beyond the defaults. 

Here is a full list of expansions that you can request with the different X API v2 endpoints:  
 

|     |     |
| --- | --- |
| **Object / Resource** | **Available expansions** |
| **Tweets** | author\_id  <br>edit\_history\_tweet\_ids  <br>entities.mentions.username  <br>in\_reply\_to\_user\_id  <br>referenced\_tweets.id  <br>referenced\_tweets.id.author\_id  <br>attachments.poll\_ids  <br>attachments.media\_keys  <br>geo.place\_id |
| **Users** | pinned\_tweet\_id |
| **Spaces** | invited\_user\_ids  <br>speaker\_ids  <br>creator\_id  <br>host\_ids  <br>topic\_ids |

  
Learn more about [how to use fields and expansions](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/using-fields-and-expansions), and check out our [full list of data objects and fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary) in the X API v2 data dictionary.  

### New metrics available within Tweets, users, Spaces, and media objects

More metrics are now accessible within Tweet, user, Spaces, Lists, and media objects. These metrics are both public and private, and some metrics can be broken down into an organic or promoted context for Tweet ads. 

Learn more about the available [metrics](https://developer.twitter.com/en/docs/twitter-api/metrics).  
 

|     |     | All Tweets |     | Ads |     |
| --- | --- | --- | --- | --- | --- |
| **Object** | **Available metrics** | **Public metrics** | **Private metrics**  <br>(requires [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) auth) | **Organic metrics** | **Promoted metrics** |
| tweets | retweet\_count | ✔️  |     | ✔️  | ✔️  |
| quote\_count | ✔️  |     |     |     |
| like\_count | ✔️  |     | ✔️  | ✔️  |
| reply\_count | ✔️  |     | ✔️  | ✔️  |
| impression\_count |     | ✔️  | ✔️  | ✔️  |
| url\_profile\_clicks |     | ✔️  | ✔️  | ✔️  |
| url\_link\_clicks |     | ✔️  | ✔️  | ✔️  |
| user | follower\_count | ✔️  |     |     |     |
| following\_count | ✔️  |     |     |     |
| tweet\_count | ✔️  |     |     |     |
| listed\_count | ✔️  |     |     |     |
| media | view\_count |     | ✔️  |     |     |
| playback\_0\_count  <br>playback\_25\_count  <br>playback\_50\_count  <br>playback\_75\_count  <br>playback\_100\_count |     | ✔️  |     |     |
| space | participant\_count | ✔️  |     |     |     |
| subscriber\_count |     | ✔️  |     |     |
| list | follower\_count | ✔️  |     |     |     |
| member\_count | ✔️  |     |     |     |

      ` "public_metrics": {             "retweet_count": 5239,             "reply_count": 1844,             "like_count": 17168,             "quote_count": 3275         }     "non_public_metrics": {             "impression_count": 956,             "user_profile_clicks": 34,             "url_link_clicks": 57    }      "organic_metrics": {             "impression_count": 956,             "like_count": 1244,             "reply_count": 300,             "user_profile_clicks": 150             "url_link_clicks": 57         }      "promoted_metrics": {             "impression_count": 25086,             "like_count": 9045,             "reply_count": 637,             "user_profile_clicks": 265,             "url_link_clicks": 48         }`
    

###   
Tweet annotations

Annotations can be used to discover Tweets on topics of interest or to segment Tweets by entity categories. 

Tweets are analyzed and annotated based on the content of the Tweet text by both semantic labeling (context annotations) and internal machine learning algorithms (named entity recognition). These annotations are now available via API in the response payload. We call these new elements “annotations” and they are delivered as two fields, context\_annotations and entity, and can be used to filter search Tweets, Tweet counts, and filtered stream responses.

Learn more about [Tweet annotations](https://developer.twitter.com/en/docs/twitter-api/annotations).

Here is an example of what this would look like in your payload:

      `"context_annotations": [       {         "domain": {           "id": "45",           "name": "Brand Vertical",           "description": "Top level entities that describe a Brands industry"         }       },       {         "domain": {           "id": "46",           "name": "Brand Category",           "description": "Categories within Brand Verticals that narrow down the scope of Brands"         },         "entity": {           "id": "781974596752842752",           "name": "Services"         }       },       {         "domain": {           "id": "47",           "name": "Brand",           "description": "Brands and Companies"         },         "entity": {           "id": "10026364281",           "name": "Apple"         }       },       {         "domain": {           "id": "48",           "name": "Product",           "description": "Products created by Brands.  Examples: Ford Explorer, Apple iPhone."         },         "entity": {           "id": "10044903039",           "name": "Apple - iOS"         }       }     ],     "created_at": "2020-05-12T19:44:51.000Z",     "entities": {       "annotations": [         {           "start": 49,           "end": 51,           "probability": 0.8997,           "type": "Product",           "normalized_text": "iOS"         }       ]`
    

### Connection Status

X API v2 now includes a feature that allows developers to lookup the relationship (called connection status) between the authenticating user and the user being looked up in the response payload.

This is comparable to [GET friendships/show](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-friendships-show) and [GET friendships/lookup](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-friendships-lookup) endpoints in V1.1. 

The sample API Request to get the connection status using the [User Lookup](https://developer.twitter.com/en/docs/twitter-api/users/lookup/introduction) Endpoint in the X API v2 is:

      `https://api.twitter.com/2/users/by/username/XDevelopers?user.fields=connection_status`
    

      `{     "data": {         "username": "XDevelopers",         "name": "Developers",         "connection_status": [             "following"         ],         "id": "2244994945"     } }`
    

Using the X API v2, a developer can programmatically find out if the authenticating user:

* is being followed by the user being looked up.
* is following the user being looked up.
* has received a follow request from the user being looked up.
* sent a follow request to the user being looked up.
* blocked the user being looked up.
* muted the user being looked up.

### Edit Tweets

The X API v2 endpoints provide edited Tweet metadata. The _Edit Tweet_ feature was first introduced for testing among X employees on September 1, 2022. Starting on that date, eligible Tweets are editable for 30 minutes and up to 5 times. Also, all objects for Tweets since September 29, 2022  include Tweet edit metadata, even if the Tweet was never edited. Each time a Tweet is edited, a new Tweet ID is created. A Tweet's edit history can be described by chaining these IDs together, starting with the original ID.  

Using the X API v2, a developer can find out:

* If a Tweet was edit eligible at the time of creation. Some Tweets, such as those with polls or scheduled Tweets, can not be edited.
* Tweets are editable for 30 minutes, and can be edited up to 5 times. For editable Tweets you can see if time for editing remains and how many more edits are possible.
* If you are viewing an edited version of a Tweet (in most cases the API will return the most recent version of a Tweet, unless a specific past version is requested by Tweet ID).
* The entire edit history of the Tweet.
* The engagement attributed to each version of the Tweet.

Learn more about [Edit Tweets](https://developer.twitter.com/en/docs/twitter-api/edit-tweets).

###   
Track threaded conversations

We have introduced a new Tweet field to help you identify which conversation thread that Tweet belongs to. In addition to this, we launched a new filter operator that matches Tweets that share a common conversation ID, and is available for search Tweets, Tweet counts, and filtered stream. 

A conversation ID is the Tweet ID of the Tweet that started the conversation. 

Learn more about [conversation tracking](https://developer.twitter.com/en/docs/twitter-api/conversation-id).

[Ready to migrate?](https://developer.twitter.com/en/docs/twitter-api/migrate/ready-to-migrate)

Ready to migrate?

Ready to migrate?
-----------------

In order to use v2 endpoints, you will need the following things:

* [A developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info)
* [A developer App](https://developer.twitter.com/en/apps) created within a [Project](https://developer.twitter.com/en/docs/projects)
* [Keys and tokens](https://developer.twitter.com/en/docs/authentication) from that Project’s developer App  
      
    

Please note the importance of using keys and tokens from an App within a Project. If you are using keys and tokens from an App outside of a Project, you will not be able to make a request to v2 endpoints.

Once you have a developer account, you can set up all of the above in the [developer portal](https://developer.twitter.com/en/portal). 

### Authentication

With the new Twitter API, you’ll use two different authentication patterns, [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) and [OAuth 2.0 Bearer Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0), to access different endpoints. Each serves a different purpose when making requests to the endpoints: 

* OAuth 1.0a User Context is required when making a request on behalf of a Twitter user
* OAuth 2.0 Bearer token is required to make requests on behalf of your developer App

### Tools and Code 

To help you get started and familiarize yourself with the new endpoints and capabilities we have a few options to jump start your work:

First, we have a Twitter [Postman collection](https://t.co/twitter-api-postman) that allows you to use the Postman client to make requests of and connect to the individual endpoints. This is a low friction way to test authentication and experiment with the endpoints. It’s important to note the Postman client is best for RESTful endpoints, but you can copy requests to streaming endpoints from the tool and paste them into your command line tool.

If you want to dig deeper, we’ve also provided a list of both Twitter supported and third party libraries in Ruby, Python, Node, Java, and many more. For additional context, take a look at our [tools and libraries page](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries).

### Migrating to updated endpoints

As you start to explore the new Twitter v2 endpoints, we’ve built a series of detailed migration guides to help you compare and contrast each updated endpoints' capabilities compared to older versions:

* Tweets
* [Tweets lookup](https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/migrate)
* [Manage Tweets](https://developer.twitter.com/en/docs/twitter-api/tweets/manage-tweets/migrate)
[](https://developer.twitter.com/en/docs/twitter-api/tweets/manage-tweets/migrate)* [](https://developer.twitter.com/en/docs/twitter-api/tweets/manage-tweets/migrate)[](https://developer.twitter.com/en/docs/twitter-api/tweets/search/migrate)[Timelines](https://developer.twitter.com/en/docs/twitter-api/tweets/timelines/migrate)
* [Search Tweets](https://developer.twitter.com/en/docs/twitter-api/tweets/search/migrate)
* [Tweet counts](https://developer.twitter.com/en/docs/twitter-api/tweets/counts/migrate)
* [Filtered stream](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/migrate)
* [Sampled stream](https://developer.twitter.com/en/docs/twitter-api/tweets/sampled-stream/migrate)
* [Retweets](https://developer.twitter.com/en/docs/twitter-api/tweets/retweets/migrate)
* [Likes](https://developer.twitter.com/en/docs/twitter-api/tweets/likes/migrate)
* [Hide replies](https://developer.twitter.com/en/docs/twitter-api/tweets/hide-replies/migrate)
* Users
* [Users lookup](https://developer.twitter.com/en/docs/twitter-api/users/lookup/migrate)
* [Follows](https://developer.twitter.com/en/docs/twitter-api/users/follows/migrate)
* [Blocks](https://developer.twitter.com/en/docs/twitter-api/users/blocks/migrate)
* [Mutes](https://developer.twitter.com/en/docs/twitter-api/users/mutes/migrate)            
* Lists
* [List lookup](https://developer.twitter.com/en/docs/twitter-api/lists/list-lookup/migrate)
* [Manage Lists](https://developer.twitter.com/en/docs/twitter-api/lists/manage-lists/migrate)
* [List Tweet lookup](https://developer.twitter.com/en/docs/twitter-api/lists/list-tweets/migrate)
* [List members](https://developer.twitter.com/en/docs/twitter-api/lists/list-members/migrate)
* [List follows](https://developer.twitter.com/en/docs/twitter-api/users/follows/migrate)

### Migrating to the new data format

As you move from v1.1 or enterprise to v2, it is important to understand that the format the data are delivered in has changed significantly. We have added new fields, modified the sequence of fields, and in some cases removed elements altogether. 

To learn more about these changes, we are developing a series of guides that will help you map out the pre-v2 data format fields to the newer fields, and describe how to request these new fields. 

You can learn more by visiting our [data formats migration](https://developer.twitter.com/en/docs/twitter-api/migrate/data-formats) section of this migration hub, or by visiting our specific data format guides:  

* [Native format to Twitter API v2 (standard v1.1)](https://developer.twitter.com/en/docs/twitter-api/migrate/data-formats/standard-v1-1-to-v2) 
* [Native Enriched to Twitter API v2 (enterprise)](https://developer.twitter.com/en/docs/twitter-api/migrate/data-formats/native-enriched-to-v2)
* [Activity Streams to Twitter API v2 (enterprise)](https://developer.twitter.com/en/docs/twitter-api/migrate/data-formats/activity-streams-to-v2)  
     

  
What’s next?
---------------

Those of you who have used the platform for some time will notice that many of the new endpoints are aligned with existing [standard v1.1](https://developer.twitter.com/en/docs/twitter-api/v1), and [enterprise](https://developer.twitter.com/en/docs/twitter-api/enterprise) endpoints. Indeed, we intend for these to replace all three versions in the future. 

We’ve put together a table to help you understand how the [Twitter API endpoints map](https://developer.twitter.com/en/docs/twitter-api/migrate/twitter-api-endpoint-map) to previous versions.

If you’d like to see what’s coming next, please visit our [product roadmap](https://trello.com/b/myf7rKwV/twitter-developer-platform-roadmap).

We also have a [changelog](https://developer.twitter.com/en/updates/changelog) that you can check out to understand what we have already released.

### What should we build next?

As we build out additional capabilities of the Twitter API v2 we want to continue to hear from you. We welcome and encourage [feedback](https://twitterdevfeedback.uservoice.com/) from you. 

Take a look at the ideas that have already been submitted, show your support for those that correlate with your needs and provide feedback as well!

Twitter API endpoint map

X API endpoint map
------------------

The following table maps the X API v2 endpoints to the corresponding standard v1.1, and enterprise endpoints. To learn more about each of these versions and tiers, please visit our [X API getting started guide](https://developer.twitter.com/en/docs/twitter-api/migrate/twitter-api-endpoint-map).

You'll notice that we still have several items marked as **\[Coming Soon\]**. If you notice anything within this table that is marked as **\[Replacement Under Consideration\]** or **\[No Replacement Planned\]**, and you would like to see us release a v2 version of that endpoint, please let us know via our [community forum](https://devcommunity.x.com/) or your enterprise account manager. 

|     | Standard v1.1 | Enterprise | X API v2 |
| --- | --- | --- | --- |
| **Tweets** | [GET statuses/show](https://developer.twitter.com/en/products/twitter-api/tweets/post-and-engage/api-reference/get-statuses-show-id)  <br>[GET statuses/lookup](https://developer.twitter.com/en/products/twitter-api/tweets/post-and-engage/api-reference/get-statuses-lookup) |     | [Tweets lookup](https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/introduction) |
| [POST statuses/update](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-update)  <br>[POST statuses/destroy/:id](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-destroy-id) |     | [Manage Tweets](https://developer.twitter.com/en/docs/twitter-api/tweets/manage-tweets/introduction) |
| [GET statuses/user\_timeline](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/api-reference/get-statuses-user_timeline.html)  <br>[GET statuses/mentions\_timeline](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/api-reference/get-statuses-mentions_timeline.html)  <br>[GET statuses/home\_timeline](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/api-reference/get-statuses-user_timeline) |     | [Timelines](https://developer.twitter.com/en/docs/twitter-api/tweets/timelines/introduction)  <br>\- User Tweet timeline  <br>\- User mention timeline  <br>\- Reverse chronological home timeline |
| [GET search/tweets (7 days)](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/search/overview) | [Search API](https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/overview)  <br>\- 30 day  <br>\- Full-archive | [Search Tweets](https://developer.twitter.com/en/docs/twitter-api/tweets/search/introduction)  <br>\- Recent search  <br>\- 30 day \[No Replacement Planned\]  <br>\- Full-archive search |
|     | [Search API](https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/overview)  <br>\- 30 day  <br>\- Full-archive | [Tweet counts](https://developer.twitter.com/en/docs/twitter-api/tweets/counts/introduction)  <br>\- Recent Tweet counts  <br>\- 30 day \[No Replacement Planned\]  <br>\- Full-archive Tweet counts |
| [GET statuses/filter](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/filter-realtime/overview) | [PowerTrack API](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/overview) | [Filtered stream](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/introduction)  <br>\- Connect to stream  <br>\- Add/delete rules  <br>\- Retrieve rules |
| [GET statuses/sample (1%)](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/sample-realtime/overview/get_statuses_sample) | [Decahose API](https://developer.twitter.com/en/docs/twitter-api/enterprise/decahose-api)  <br>Firehose API | [Volume stream](https://developer.twitter.com/en/docs/twitter-api/tweets/sampled-stream/introduction)  <br>\- 1% sampled stream  <br>\- 10% decahose stream   <br>\- 100% firehose stream |
| [GET statuses/retweeters/:ids](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-statuses-retweeters-ids)  <br>[GET statuses/retweets/:id](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-statuses-retweets-id) |     | [Retweets lookup](https://developer.twitter.com/en/docs/twitter-api/tweets/retweets/introduction) |
|     |     | [Quote Tweets lookup](https://developer.twitter.com/en/docs/twitter-api/tweets/quote-tweets/introduction) |
| [POST statuses/retweet/:id](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-retweet-id)  <br>[POST statuses/unretweet/:id](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-unretweet-id) |     | [Manage Retweets](https://developer.twitter.com/en/docs/twitter-api/tweets/retweets/introduction)  <br>\- Retweet a Tweet  <br>\- Undo a Retweet |
| [GET favorites/list](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-favorites-list) |     | [Likes lookup](https://developer.twitter.com/en/docs/twitter-api/tweets/likes/introduction)  <br>\- Tweets liked by a user  <br>\- Users who have liked a Tweet \[NEW to v2\] |
| [POST favorites/create](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-favorites-create)  <br>[POST favorites/destroy](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-favorites-destroy) |     | [Manage Likes](https://developer.twitter.com/en/docs/twitter-api/tweets/likes/introduction)  <br>\- Like a Tweet  <br>\- Unlike a Tweet |
|     |     | [Hide replies](https://developer.twitter.com/en/docs/twitter-api/tweets/hide-replies/introduction) \[NEW to v2\] |
| [GET statuses/oembed](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-statuses-oembed) |     | \[No Replacement Planned\] |
| [GET statuses/retweets\_of\_me](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-statuses-retweets_of_me) |     | \[No Replacement Planned\] |
| **Users** | [GET users/show](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-users-show)  <br>[GET users/lookup](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-users-lookup) |     | [Users lookup](https://developer.twitter.com/en/docs/twitter-api/users/lookup/introduction) |
| [GET users/search](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-users-search) |     | [Get user/search](https://developer.twitter.com/en/docs/twitter-api/users/search/introduction) |
| [GET followers/ids](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-followers-ids)  <br>[GET followers/list](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-followers-list)  <br>[GET friends/ids](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-friends-ids)  <br>[GET friends/list](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-friends-list) |     | [Follows lookup](https://developer.twitter.com/en/docs/twitter-api/users/follows) |
| [GET friendships/incoming](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-friendships-incoming)  <br>[GET friendships/lookup](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-friendships-lookup)  <br>[GET friendships/no\_retweets/ids](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-friendships-no_retweets-ids)  <br>[GET friendships/outgoing](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-friendships-outgoing)  <br>[GET friendships/show](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-friendships-show) |     | \[Coming Q1-2024\]:<br><br>friendships/lookup/<br><br>friendships/show/ |
| [GET friendships/create](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/post-friendships-create)  <br>[GET friendships/destroy](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/post-friendships-destroy) |     | [Manage follows](https://developer.twitter.com/en/docs/twitter-api/users/follows)  <br>\- Follow a user  <br>\- Unfollow a user |
| [POST friendships/update](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/post-friendships-update) |     | \[No Replacement Planned\] |
| [GET blocks/ids](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/mute-block-report-users/api-reference/get-blocks-ids)  <br>[GET blocks/list](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/mute-block-report-users/api-reference/get-blocks-list) |     | [Blocks lookup](https://developer.twitter.com/en/docs/twitter-api/users/blocks) |
| [POST blocks/create](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/mute-block-report-users/api-reference/post-blocks-create)  <br>[POST blocks/destroy](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/mute-block-report-users/api-reference/post-blocks-destroy) |     | [Manage blocks](https://developer.twitter.com/en/docs/twitter-api/users/blocks)  <br>\- Block a user  <br>\- Unblock a user |
| [GET mutes/users/ids](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/mute-block-report-users/api-reference/get-mutes-users-ids)  <br>[GET mutes/users/list](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/mute-block-report-users/api-reference/get-mutes-users-list) |     | [Mutes lookup](https://developer.twitter.com/en/docs/twitter-api/users/mutes) |
| [POST mutes/users/create](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/mute-block-report-users/api-reference/post-mutes-users-create)  <br>[POST mutes/users/destroy](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/mute-block-report-users/api-reference/post-mutes-users-destroy) |     | [Manage mutes](https://developer.twitter.com/en/docs/twitter-api/users/mutes)  <br>\- Mute a user  <br>\- Unmute a user |
| [GET account/settings](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/manage-account-settings/api-reference/get-account-settings)  <br>[GET account/verify\_credentials](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/manage-account-settings/api-reference/get-account-verify_credentials)  <br>[GET users/profile\_banner](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/manage-account-settings/api-reference/get-users-profile_banner)  <br>[POST account/settings](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/manage-account-settings/api-reference/post-account-settings)  <br>[POST account/update\_profile](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/manage-account-settings/api-reference/post-account-update_profile)  <br>[POST account/update\_profile\_banner](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/manage-account-settings/api-reference/post-account-update_profile_banner)  <br>[POST account/remove\_profile\_banner](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/manage-account-settings/api-reference/post-account-remove_profile_banner)  <br>[POST account/update\_profile\_image](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/manage-account-settings/api-reference/post-account-update_profile_image) |     | \[No Replacement Planned\] |
| [GET saved\_searches/show/:id](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/manage-account-settings/api-reference/get-saved_searches-show-id)  <br>[GET saved\_searches/list](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/manage-account-settings/api-reference/get-saved_searches-list)  <br>[POST saved\_searches/create](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/manage-account-settings/api-reference/post-saved_searches-create)  <br>[POST saved\_searches/destroy/:id](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/manage-account-settings/api-reference/post-saved_searches-destroy-id) |     | \[No Replacement Planned\] |
| [POST users/report\_spam](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/mute-block-report-users/api-reference/post-users-report_spam) |     | \[No Replacement Planned\] |
|     | [Account Activity API](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/overview) | \[Migrating to Developer Portal Q1/Q2\] |
| **Spaces** |     |     | [Spaces lookup](https://developer.twitter.com/en/docs/twitter-api/spaces/lookup) \[NEW to v2\] |
|     |     | [Spaces search](https://developer.twitter.com/en/docs/twitter-api/spaces/search) \[NEW to v2\] |
|     |     | Spaces reminders lookup \[[COMING SOON](https://trello.com/c/2D2p9It3/101-additional-spaces-endpoints-functionality)\]  <br>\[NEW to v2\] |
|     |     | Manage Spaces reminders \[[COMING SOON](https://trello.com/c/2D2p9It3/101-additional-spaces-endpoints-functionality)\]  <br>\[NEW to v2\] |
|     |     | [Ticketed user lookup](https://developer.twitter.com/en/docs/twitter-api/spaces/lookup/api-reference/get-spaces-id-buyers)  <br>\[NEW to v2\] |
|     |     | [Tweets shared in a Space lookup](https://developer.twitter.com/en/docs/twitter-api/spaces/lookup/api-reference/get-spaces-id-tweets) \[NEW to v2\] |
| **Direct Messages** |     |     | [Direct Messages lookup](https://developer.twitter.com/en/docs/twitter-api/direct-messages/lookup/introduction)  <br>[Manage Direct Messages](https://developer.twitter.com/en/docs/twitter-api/direct-messages/manage/introduction) |
| **Lists** | [GET lists/show](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-show) |     | [Lists lookup](https://developer.twitter.com/en/docs/twitter-api/lists/list-lookup/introduction) |
| [POST lists/create](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-create)  <br>[POST lists/destroy](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-destroy)  <br>[POST lists/update](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-update) |     | [Manage Lists](https://developer.twitter.com/en/docs/twitter-api/lists/manage-lists/introduction) |
| [GET lists/statuses](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-statuses) |     | [Lists Tweets lookup](https://developer.twitter.com/en/docs/twitter-api/lists/list-tweets/introduction) |
| [GET lists/members](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-members)  <br>[GET lists/memberships](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-memberships)  <br>[POST lists/members/create](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-members-create)  <br>[POST lists/members/destroy](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-members-destroy) |     | [List members](https://developer.twitter.com/en/docs/twitter-api/lists/list-members/introduction) |
| [GET lists/subscribers](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-subscribers)  <br>[GET lists/subscriptions](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-subscriptions)  <br>[GET lists/lists](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-list)  <br>[POST lists/subscribers/create](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-subscribers-create)  <br>[POST lists/subscribers/destroy](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-subscribers-destroy) |     | [Lists follows](https://developer.twitter.com/en/docs/twitter-api/lists/list-follows/introduction) |
| [GET lists/ownerships](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-ownerships) |     | [Owned Lists lookup](https://developer.twitter.com/en/docs/twitter-api/lists/list-lookup/introduction) |
|     |     | [Pinned Lists](https://developer.twitter.com/en/docs/twitter-api/lists/pinned-lists/introduction) \[NEW to v2\] |
| [GET lists/members/show](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-members-show)  <br>[GET lists/subscribers/show](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-subscribers-show) |     | \[No Replacement Planned\] |
| [POST lists/members/create\_all](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-members-create_all)  <br>[POST lists/members/destroy\_all](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-members-destroy_all) |     | \[No Replacement Planned\] |
| **Media** |     |     | \[Coming Q1/Q2 2024\] |
| **Trends** |     |     | [Trends v2](https://developer.twitter.com/en/docs/twitter-api/trends/introduction) |
| **Geo** |     |     | \[No Replacement Planned\] |
| **Collections** | [GET collections/entries](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/curate-a-collection/api-reference/get-collections-entries)  <br>[GET collections/list](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/curate-a-collection/api-reference/get-collections-list)  <br>[GET collections/show](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/curate-a-collection/api-reference/get-collections-show)  <br>[POST collections/create](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/curate-a-collection/api-reference/post-collections-create)  <br>[POST collections/destroy](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/curate-a-collection/api-reference/post-collections-destroy)  <br>[POST collections/entries/add](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/curate-a-collection/api-reference/post-collections-entries-add)  <br>[POST collections/entries/curate](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/curate-a-collection/api-reference/post-collections-entries-curate)  <br>[POST collections/entries/move](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/curate-a-collection/api-reference/post-collections-entries-move)  <br>[POST collections/entries/remove](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/curate-a-collection/api-reference/post-collections-entries-remove)  <br>[POST collections/update](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/curate-a-collection/api-reference/post-collections-update) |     | \[No Replacement Planned\] |
| **Metrics** |     | [Engagement API](https://developer.twitter.com/en/docs/twitter-api/enterprise/engagement-api/overview)  <br>\- /totals  <br>\- /28hr  <br>\- /historical | /totals - [data is built into v2 responses](https://developer.twitter.com/en/docs/twitter-api/metrics)  <br>/28hr - \[Replacement under consideration\]  <br>/historical - \[Replacement under consideration\] |
| **Compliance** |     |     | [Batch compliance](https://developer.twitter.com/en/docs/twitter-api/compliance/batch-compliance/introduction)  <br>\[NEW to v2\] |
|     | [Compliance firehose](https://developer.twitter.com/en/docs/twitter-api/enterprise/compliance-firehose-api/overview) | [Compliance streams](https://developer.twitter.com/en/docs/twitter-api/compliance/streams/introduction) |
| **Utilities** |     | [Usage API](https://developer.twitter.com/en/docs/twitter-api/enterprise/usage-api/overview) | [Usage API](https://developer.twitter.com/en/docs/twitter-api/usage/tweets/introduction) |
| [GET application/rate\_limit\_status](https://developer.twitter.com/en/docs/twitter-api/v1/developer-utilities/rate-limit-status/api-reference/get-application-rate_limit_status) |     | \[No Replacement Planned\] |
| [GET help/languages](https://developer.twitter.com/en/docs/twitter-api/v1/developer-utilities/supported-languages/api-reference/get-help-languages) |     | \[No Replacement Planned\] |
| **Authentication** |     |     | \[No Changes Planned\] |