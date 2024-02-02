
What's new with Twitter API v2 | Docs | Twitter Developer Platform 

What's new

What is the X API v2?
---------------------

The X API v2 is now the primary X API, and is where product investment and innovation are focused. We’ve partnered with developers to build the next generation of the X API to better serve our diverse community of developers. Based on developer feedback, we’ve re-built the API to better serve a broader collection of needs, introduced new features and endpoints, and improved upon the developer experience.  

The X API v2 is now the primary X API, and is where product investment and innovation are focused. Over the past few years, we partnered with developers and re-built the API to better serve a broader collection of needs, introduce new features and endpoints, and improve upon the developer experience. We are committed to continuing to build an open developer platform, and are excited to see what you build with the X API v2.

Why migrate?
------------

The X API v2 is built with a modern and more sustainable foundation and includes both improved replacement endpoints for the standard v1.1, and enterprise products, but also net-new functionality. We strongly encourage customers of legacy APIs (v1.1, and enterprise) to begin to migrate to v2 as we do intend to deprecate them eventually. Use the X API to listen to and analyze the public conversation, engage with people on X, and innovate.  

In this section, we will discuss the endpoints and functionality.

### 

### V2 endpoints

You can see a full list of v2 endpoints and their pre-v2 equivalent via the following guide:

X API Endpoint Map

While most of the endpoints in X API v2 are replacements, we have introduced several new endpoints. Here are several examples of new endpoints that we’ve released to v2:

* Spaces endpoints to help people get more out of X Spaces, and to allow developers to help shape the future of audio conversations.
* Hide replies, which allows you to build tools that help limit the impact of abusive, distracting, or misleading replies at scale – a crucial piece to improving the health of the public conversation on X, and ensuring brands and people feel comfortable starting conversations.
* New Lists endpoints that allow you to pin and unpin Lists, or look up someone’s pinned Lists
* New batch compliance endpoints that allow you to ensure your stored user and Tweet data is in compliance.

New functionality
-----------------

X API v2 also includes new features that will help you find more value with the X API. A lot of what is new has been driven by your feedback, and includes certain features that were reserved for enterprise customers previously. 

Some of the improvements to the API include:

* A consistent design across endpoints
* The ability specify which fields and objects return in the response payload
* New and more detailed data objects
* Receive and filter data with new contextual information powered by Tweet annotations
* Access to new metrics
* Easily identify and filter for conversations that belong to a reply thread
* Advanced functionality and increased access to data for academic researchers
* Recovery and redundancy functionality for streaming endpoints
* Easily return counts of Tweets that match a query
* Support for Edit Tweets
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
| **Tweet** | The Tweet object has a long list of root-level fields, such as id, text, and created\_at. Tweet objects are also the parent object to several child objects including user, media, poll, and place. |
| **User** | The user object contains X user account metadata describing the referenced user. |
| **Spaces** | The Space object consists of fields such as state, host\_id, is\_ticketed, and even lang. |
| **Lists** | The List object contains basic information about the requested list including description, member\_count, and owner\_id. |
| **Media** | If a Tweet contains media (such as images), then the media object can be requested using the media.fields parameter and includes fields such as the media\_key, type, url, preview\_image\_url, and more.  |
| **Poll** | A poll included in a Tweet is not a primary object on any endpoint, but can be found and expanded in the Tweet object. |
| **Place** | The place object consists of fields such as place\_id, geo object, country\_code, and more. This information can be used to identify Tweets and study Tweets by location. |

### 

### Flexibility to choose which objects and fields you receive

When making a request to a GET endpoint, you will receive the primary data object that relates to that endpoint, which will include a set of default fields. For example, the Tweet object delivers the id and text fields as its default. 

If you would like to retrieve additional fields with your request, you will have to use the fields and expansions parameters. The expansions parameter enables you to retrieve related data objects such as a user's pinned Tweet or a media object, while the field operators enable you to request specific fields within returned objects beyond the defaults. 

Here is a full list of expansions that you can request with the different X API v2 endpoints:  

|  |  |
| --- | --- |
| **Object / Resource** | **Available expansions** |
| **Tweets** | author\_id
 edit\_history\_tweet\_ids 
entities.mentions.username
in\_reply\_to\_user\_id
referenced\_tweets.id
referenced\_tweets.id.author\_id
attachments.poll\_ids
attachments.media\_keys
geo.place\_id |
| **Users** | pinned\_tweet\_id |
| **Spaces** | invited\_user\_ids
speaker\_ids
creator\_id
host\_ids
topic\_ids |

Learn more about how to use fields and expansions, and check out our full list of data objects and fields in the X API v2 data dictionary.  

### 

### New metrics available within Tweets, users, Spaces, and media objects

More metrics are now accessible within Tweet, user, Spaces, Lists, and media objects. These metrics are both public and private, and some metrics can be broken down into an organic or promoted context for Tweet ads. 

Learn more about the available metrics.  

|  |  | All Tweets | Ads |
| **Object** | **Available metrics** | **Public metrics** | **Private metrics**
(requires OAuth 1.0a User Context auth) | **Organic metrics** | **Promoted metrics** |
| tweets | retweet\_count | ✔️ |  | ✔️ | ✔️ |
| quote\_count | ✔️ |  |  |  |
| like\_count | ✔️ |  | ✔️ | ✔️ |
| reply\_count | ✔️ |  | ✔️ | ✔️ |
| impression\_count |  | ✔️ | ✔️ | ✔️ |
| url\_profile\_clicks |  | ✔️ | ✔️ | ✔️ |
| url\_link\_clicks |  | ✔️ | ✔️ | ✔️ |
| user | follower\_count | ✔️ |  |  |  |
| following\_count | ✔️ |  |  |  |
| tweet\_count | ✔️ |  |  |  |
| listed\_count | ✔️ |  |  |  |
| media | view\_count |  | ✔️ |  |  |
| playback\_0\_count
playback\_25\_count
playback\_50\_count
playback\_75\_count
playback\_100\_count |  | ✔️ |  |  |
| space | participant\_count | ✔️ |  |  |  |
| subscriber\_count |  | ✔️ |  |  |
| list | follower\_count | ✔️ |  |  |  |
| member\_count | ✔️ |  |  |  |

```
       "public_metrics": {
            "retweet_count": 5239,
            "reply_count": 1844,
            "like_count": 17168,
            "quote_count": 3275
        }

  "non_public_metrics": {
            "impression_count": 956,
            "user_profile_clicks": 34,
            "url_link_clicks": 57
   }

   "organic_metrics": {
            "impression_count": 956,
            "like_count": 1244,
            "reply_count": 300,
            "user_profile_clicks": 150
            "url_link_clicks": 57
        }

   "promoted_metrics": {
            "impression_count": 25086,
            "like_count": 9045,
            "reply_count": 637,
            "user_profile_clicks": 265,
            "url_link_clicks": 48
        }
```

### 
Tweet annotations

Annotations can be used to discover Tweets on topics of interest or to segment Tweets by entity categories. 

Tweets are analyzed and annotated based on the content of the Tweet text by both semantic labeling (context annotations) and internal machine learning algorithms (named entity recognition). These annotations are now available via API in the response payload. We call these new elements “annotations” and they are delivered as two fields, context\_annotations and entity, and can be used to filter search Tweets, Tweet counts, and filtered stream responses.

Learn more about Tweet annotations.

Here is an example of what this would look like in your payload:

```
      "context_annotations": [
      {
        "domain": {
          "id": "45",
          "name": "Brand Vertical",
          "description": "Top level entities that describe a Brands industry"
        }
      },
      {
        "domain": {
          "id": "46",
          "name": "Brand Category",
          "description": "Categories within Brand Verticals that narrow down the scope of Brands"
        },
        "entity": {
          "id": "781974596752842752",
          "name": "Services"
        }
      },
      {
        "domain": {
          "id": "47",
          "name": "Brand",
          "description": "Brands and Companies"
        },
        "entity": {
          "id": "10026364281",
          "name": "Apple"
        }
      },
      {
        "domain": {
          "id": "48",
          "name": "Product",
          "description": "Products created by Brands.  Examples: Ford Explorer, Apple iPhone."
        },
        "entity": {
          "id": "10044903039",
          "name": "Apple - iOS"
        }
      }
    ],
    "created_at": "2020-05-12T19:44:51.000Z",
    "entities": {
      "annotations": [
        {
          "start": 49,
          "end": 51,
          "probability": 0.8997,
          "type": "Product",
          "normalized_text": "iOS"
        }
      ]

```

### Connection Status

X API v2 now includes a feature that allows developers to lookup the relationship (called connection status) between the authenticating user and the user being looked up in the response payload.

This is comparable to GET friendships/show and GET friendships/lookup endpoints in V1.1. 

The sample API Request to get the connection status using the User Lookup Endpoint in the X API v2 is:

```
      https://api.twitter.com/2/users/by/username/XDevelopers?user.fields=connection_status
```

Code copied to clipboard

```
      {
    "data": {
        "username": "XDevelopers",
        "name": "Developers",
        "connection_status": [
            "following"
        ],
        "id": "2244994945"
    }
}
```

Code copied to clipboard

Using the X API v2, a developer can programmatically find out if the authenticating user:

* is being followed by the user being looked up.
* is following the user being looked up.
* has received a follow request from the user being looked up.
* sent a follow request to the user being looked up.
* blocked the user being looked up.
* muted the user being looked up.

### Edit Tweets

The X API v2 endpoints provide edited Tweet metadata. The *Edit Tweet* feature was first introduced for testing among X employees on September 1, 2022. Starting on that date, eligible Tweets are editable for 30 minutes and up to 5 times. Also, all objects for Tweets since September 29, 2022  include Tweet edit metadata, even if the Tweet was never edited. Each time a Tweet is edited, a new Tweet ID is created. A Tweet's edit history can be described by chaining these IDs together, starting with the original ID.  

Using the X API v2, a developer can find out:

* If a Tweet was edit eligible at the time of creation. Some Tweets, such as those with polls or scheduled Tweets, can not be edited.
* Tweets are editable for 30 minutes, and can be edited up to 5 times. For editable Tweets you can see if time for editing remains and how many more edits are possible.
* If you are viewing an edited version of a Tweet (in most cases the API will return the most recent version of a Tweet, unless a specific past version is requested by Tweet ID).
* The entire edit history of the Tweet.
* The engagement attributed to each version of the Tweet.

Learn more about Edit Tweets.

### 
Track threaded conversations

We have introduced a new Tweet field to help you identify which conversation thread that Tweet belongs to. In addition to this, we launched a new filter operator that matches Tweets that share a common conversation ID, and is available for search Tweets, Tweet counts, and filtered stream. 

A conversation ID is the Tweet ID of the Tweet that started the conversation. 

Learn more about conversation tracking.

Ready to migrate?

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