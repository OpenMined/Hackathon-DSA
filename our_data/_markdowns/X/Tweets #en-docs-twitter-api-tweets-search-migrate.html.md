
Search Tweets version comparison | Docs | Twitter Developer Platform 

Migrate

Comparing Twitter API’s Search Tweets endpoints
-----------------------------------------------

The v2 Search Tweets endpoint will eventually replace the standard v1.1 search/tweets endpoint and enterprise Search API. If you have code, apps, or tools that use an older version of a Twitter search endpoint and are considering migrating to the newer Twitter API v2 endpoints, then this guide is for you. 

This page contains three comparison tables:

* Recent search
* Full-archive search
* Filtering operator comparison

### Recent search comparison

The following table compares the various types of recent search endpoints:  

| **Description** | **Standard v1.1** | **Twitter API v2** |
| Host domain | https://api.twitter.com | https://api.twitter.com |
| Endpoint path | /1.1/search/tweets.json | /2/tweets/search/recent |
| Authentication | OAuth 1.0a User Context
OAuth 2.0 App-Only | OAuth 1.0a User Context
OAuth 2.0 Authorization Code with PKCE
OAuth 2.0 App-Only |
| Timestamp format | YYYYMMDD | YYYY-MM-DDTHH:mm:ssZ
ISO 8601 / RFC 3339 |
| Returns Tweets that are no older than | 7 days | 7 days |
| HTTP methods supported | GET | GET |
| Default request rate limits | 180 requests per 15 min with OAuth 1.0a User Context
450 requests per 15 min with OAuth 2.0 App-Only | **Basic:**
60 requests per 15 min with OAuth 2.0 App-Only
60 requests per 15 min with OAuth 1.0a User Context
60 requests per 15 min with OAuth 2.0 Authorization Code with PKCE
**Pro:**
450 requests per 15 min with OAuth 2.0 App-Only
180 requests per 15 min with OAuth 1.0a User Context
180 requests per 15 min with OAuth 2.0 Authorization Code with PKCE |
| Offers fully unwound URLs |  | ✔ |
| Maximum Tweets per response (default) | 100 (15) | 100 (10) |
| Tweet JSON format | Standard v1.1 format | Twitter API v2 format (determined by fields and expansions request parameters, not backward-compatible with v1.1 formats)
To learn more about how to migrate from the Standard v1.1 format to the Twitter API v2 format, please visit our data formats migration guide. |
| Supports selecting which fields return in the payload |  | ✔ |
| Supports requesting and receiving annotations |  | ✔ |
| Supports requesting specific metrics within Tweet object |  | ✔ |
| Supports the conversation\_id operator and field |  | ✔ |
| Provides Tweet edit history | ✔ | ✔ |
| JSON key name for Tweet data array | statuses | data |
| JSON key name for pagination | search\_metadata.next\_results | meta.next\_token |
| Supports navigating archive by time range | ✔ | ✔ |
| Time resolution of time-based requests | day | second |
| Timezone | UTC | UTC |
| Request parameters for navigating by time | until | start\_time
end\_time |
| Request parameters for navigating by Tweet ID | since\_id 
max\_id | since\_id 
until\_id |
| Request parameter for pagination | Provides URL-encoded query | next\_token |
| Requires the use of credentials from a developer App associated with a Project |  | ✔ |

### Full-archive search comparison

The following table compares the various types of full-archive search endpoints:  

| **Description** | **Enterprise** | **Twitter API v2** |
| Host domain | https://gnip-api.twitter.com | https://api.twitter.com |
| Endpoint path | /search/fullarchive/accounts/:account\_name/:label | /2/tweets/search/all |
| Authentication | Basic auth | OAuth 2.0 App-Only |
| Timestamp format | YYYYMMDDHHMM | YYYY-MM-DDTHH:mm:ssZ
ISO 8601 / RFC 3339 |
| Returns Tweets that are no older than | The full archive since March 2006 | The full archive since March 2006 |
| HTTP methods supported | GET
POST | GET |
| Default request rate limits | The per minute rate limit will vary by partner as specified in your contract. 
20 requests per sec with Basic auth | 300 requests per 15 min with OAuth 2.0 App-Only
1 requests per 1 sec with OAuth 2.0 App-Only |
| Offers fully unwound URLs | ✔ | ✔ |
| Tweets per response | Maximum: 500
Default: 100 | Maximum: 500
Default: 10 |
| Tweet JSON format | Native Enriched or Activity Streams format | Twitter API v2 format (determined by fields and expansions request parameters) |
| Supports selecting which fields return in the payload |  | ✔ |
| Supports requesting and receiving annotations |  | ✔ |
| Supports requesting specific metrics within Tweet object |  | ✔ |
| Supports the conversation\_id operator and field |  | ✔ |
| Provides Tweet edit history | ✔ | ✔ |
| JSON key name for Tweet data array | results | data |
| JSON key name for pagination | **next** | meta.next\_token |
| Time resolution of time-based requests | second | second |
| Timezone | UTC | UTC |
| Supports navigating archive by Tweet ID |  | ✔ |
| Request parameters for navigation by time | fromDate
toDate | start\_time
end\_time |
| Request parameters for navigating by Tweet ID |  | since\_id 
until\_id |
| Request parameter for pagination | next\_token | next\_token |
| Requires the use of credentials from a developer App associated with a Project that has Academic Research access |  | ✔ |

### Filtering operator comparison

The four different versions (standard, enterprise, and v2) of search Tweets differ in which operators are available, and also have varying levels of operator availability within each version, which are explained below. 

Enterprise

* There are no sub-tiers of enterprise operators

Twitter API v2

* **Free:**Available when using any Project
* **Basic:** Available when using any Project
* **Pro:** Available when using a Project
* **Enterprise:** Available when using a Project

You can learn more about each of these sets of operators in their respective guides:

* Enterprise operators
* Twitter API v2 operators

Now that we understand the different operator levels within Twitter API v2, here is the table that maps out operator availability for search Tweets (note that if the cell is left blank, the operator is not available):

| Search operator | Standard | Enterprise | v2 |
| --- | --- | --- | --- |
| keyword | Available
q:keyword | Available | Basic & Pro |
| emoji | Available
q:😄 | Available | Basic & Pro |
| “exact phrase” | Available | Available | Basic & Pro |
| # | Available | Available | Basic & Pro |
| $ | Available | Available | Pro |
| @ | Available | Available | Basic & Pro |
| from: | Available | Available | Basic & Pro |
| to: | Available | Available | Basic & Pro |
| url: | Available | Available | Basic & Pro |
| retweets\_of: |  | Available | Basic & Pro |
| context: |  |  | Basic & Pro |
| entity: |  |  | Basic & Pro - Only available with recent search |
| conversation\_id: |  |  | Basic |
| place: |  | Available | Pro |
| place\_country: |  | Available | Pro |
| point\_radius: | geocode parameter | Available | Pro |
| bounding\_box: |  | Available | Pro |
| is:retweet | filter:retweets | Available | Basic & Pro |
| is:reply |  | Available | Basic & Pro |
| is:quote |  | Available | Basic & Pro |
| is:verified |  | Available | Basic & Pro |
| -is:nullcast |  | Available | Pro |
| has:hashtags |  | Available | Basic & Pro |
| has:cashtags |  | Available | Pro |
| has:links | filter:links | Available | Basic & Pro |
| has:mentions |  | Available | Basic & Pro |
| has:media | filter:media | Available | Basic & Pro |
| has:images | filter:images, filter:twimg | Available | Basic & Pro |
| has:videos | filter:videos
filter:native\_video | Available | Basic & Pro |
| has:geo |  | Available | Pro |
| lang: | lang - can be used as an operator or a parameter | Available | Basic & Pro |
| has:profile\_geo |  | Available |  |
| profile\_country |  | Available |  |
| profile\_locality |  | Available |  |
| profile\_region |  | Available |  |
| proximity |  | Available |  |
| :( | Available |  |  |
| :) | Available |  |  |
| ? | Available |  |  |
| filter:periscope | Available |  |  |
| list: | Available |  | Pro |
| filter:replies | Available |  |  |
| filter:pro\_video | Available |  |  |
| filter:social | Available |  |  |
| filter:trusted | Available |  |  |
| filter:follows | Available |  |  |
| filter:has\_engagement | Available |  |  |
| include:antisocial | Available |  |  |
| include:offensive\_user | Available |  |  |
| include:antisocial\_offensive\_user | Available |  |  |
| include:sensitive\_content | Available |  |  |
| source: | Available |  |  |
| min\_replies: | Available |  |  |
| min\_retweets: | Available |  |  |
| min\_faves: | Available |  |  |
| card\_name: | Available |  |  |
| card\_domain: | Available |  |  |

Other migration resources
-------------------------

Twitter API migration hub

Check out some sample code for these endpoints

Search Tweets: Standard v1.1 to Twitter API v2

Search Tweets: Enterprise to Twitter API v2

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