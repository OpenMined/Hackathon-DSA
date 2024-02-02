



Filtered stream version comparison | Docs | Twitter Developer Platform 





































































































Migrate



Comparing Twitter API’s filtered stream endpoints
-------------------------------------------------


The v2 filtered stream endpoints group is replacing the standard v1.1 statuses/filter and PowerTrack API. If you have code, apps, or tools that use an older version of the filtered stream endpoint, and are considering migrating to the newer Twitter API v2 endpoint, then this comparison can help you get started. 


See our more in depth migration guides for:


Migrating from Standard v1.1 compared to Twitter API v2


Migrating from PowerTrack API migration to Twitter API v2


 


The following table compares the filtered streaming endpoints Twitter offers:  

 




| **Description** | **Standard v1.1** | **PowerTrack API** | **Twitter API v2** |
| Access | Twitter App | Requires an enterprise contract and account | Requires a developer account (sign up), and Twitter App within a Project |
| Host domain | ******https://stream.twitter.com****** | ******https://gnip-stream.twitter.com****** | ******https://api.twitter.com****** |
| Endpoint path | ******1.1/statuses/filter.json****** | ******/stream/powertrack/accounts/{gnip\_account\_name}/publishers/twitter/{stream\_label}.json******
******/rules/powertrack/accounts/{gnip\_account\_name}/publishers/twitter/{stream\_label}.json******
******/rules/powertrack/accounts/{gnip\_account\_name}/publishers/twitter/{stream\_label}/validation.json****** | ******/2/tweets/search/stream******
******/2/tweets/search/stream/rules****** |
| Authentication | OAuth 1.0a User Context | HTTP Basic Authentication | OAuth 2.0 App-Only |
| HTTP methods supported | POST | GET
POST | GET
POST |
| Required parameters | Rule defined on connection as parameter, at least one of:* ******follow******
* ******track******
* ******locations******
 | No required parameters for streaming connection, optional backfill parameter.
Rules managed separately | No required parameters for streaming connection, optional parameters to define response format and add backfill recovery feature for Academic Research access.
Rules managed separately |
| Delivery type | Streaming | Streaming
REST (for rules management) | Streaming
REST (for rules management) |
| Default request rate limits | 5 connection attempts per 5 min | 60 requests per min aggregated for both POST and GET requests
/rules:  60 requests per minute, aggregated across all requests to /rules endpoint for the specific stream’s API (POST and GET). | Depends on the endpoint and the access level.
GET /2/tweets/search/stream:
Pro - 50 requests per 15-minutes per App
GET /2/tweets/search/stream/rules:
Pro - 450 requests per 15-minutes per App
---
POST /2/tweets/search/stream/rules:
Pro - 100 requests per 15 minutes per App

  |
| Maximum allowed connections | 2 concurrent per authorized user | Supports multiple/redundant connections, determined by contract | Pro access: 
 1 |
| Recovery and redundancy features | None | Backfill, redundant connections, and the Replay API |  |
| Tweet caps | Limited to 1% of firehose | Determined by contract | There is a monthly, Project-level Tweet cap applied to all Tweets received from this endpoint:
Basic:
10,000 Tweets
Pro:
1 million Tweets |
| Keep-alive signal/heartbeats | blank lines (\r\n or similar) at least every 20 seconds | blank lines (\r\n or similar) every 10 seconds | blank lines (\r\n or similar) at least every 20 seconds |
| Latency | 10 seconds | 2 seconds
At least 10 seconds for URL unwinding enrichment | 10 seconds |
| Maximum allowed rules | 1 rule (within the endpoint connection request) | Determined by contract up to 250,000 | Pro access:
1000 rules |
| Rule filter limitations | One query per connection, up to either:
- 400 track keywords
- 5000 follow user IDs
- 25 location boxes | Up to 2,048 characters per rule | Pro Access: 
1,024 characters per rule
  |
| Tweet JSON format | Standard v1.1 format | Native Enriched or Activity Streams (selected within the console) | Twitter API v2 format (determined by ******fields****** and ******expansions****** request parameters, not backward-compatible with v1.1 formats)
To learn more about how to migrate from the Standard v1.1 format to the Twitter API v2 format, please visit our data formats migration guide. We will be releasing additional data format migration guides for Native Enriched and Activity Streams soon. |
| Provides Tweet edit history and metadata | ✔ | ✔ | ✔ |
| Unique Features | Filtering done via query parameters on connection request
No configuration UI | Filtering done via rules created through an independent endpoint
Enrichment features available in contract
Configuration on console.gnip.com UI | Filtering done via rules created through an independent endpoint
Metrics and URL enrichment features included
Object fields and  expansions specified with request parameters
Tweet Annotations
Conversation ID operator and field
Configuration through developer portal |










Other migration resources
-------------------------






Standard v1.1 migration to Twitter API v2


PowerTrack API migration to Twitter API v2


Twitter API migration hub


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















