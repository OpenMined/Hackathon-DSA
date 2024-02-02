



Tweet counts version comparison | Docs | Twitter Developer Platform 





































































































Migrate



Comparing Twitter API’s Tweet counts endpoints
----------------------------------------------


The v2 Tweet counts endpoint will eventually replace the enterprise Search API’s counts endpoint. If you have code, apps, or tools that use an older version of a Tweet counts endpoint and are considering migrating to the newer Twitter API v2 endpoints, then this guide is for you.


This page contains two comparison tables:


* Recent Tweet counts
* Full-archive Tweet counts
* Filtering operator comparison


### Recent Tweet counts comparison


The enterprise version of the Tweet counts endpoints allow you to pull counts for either 30 days or from the full-archive. Therefore, the v2 recent Tweet counts endpoint, which looks at a 7 day time period, is not a direct replacement for either of the aforementioned endpoints.


However, to help with comparisons, we will look at how the v2 recent Tweet counts endpoint compares to the enterprise 30-day endpoint.


The following table compares the various types of recent Tweet counts endpoints:




| **Description** | **Enterprise** | **Twitter API v2** |
| Host domain | https://gnip-api.twitter.com | https://api.twitter.com |
| Endpoint path | /search/30day/accounts/:account\_name/:label/counts.json | /2/tweets/counts/recent |
| Authentication | Basic authentication | OAuth 2.0 Bearer Token |
| Timestamp format | YYYYMMDDhhmm | YYYY-MM-DDTHH:mm:ssZ
ISO 8601 / RFC 3339 |
| Returns counts of Tweets that are no older than | 31 days | 7 days |
| HTTP methods supported | GET | GET |
| Default request rate limits | 20 requests per 1 sec, aggregated across search data and counts requests
The per minute rate limit will vary by partner as specified in your contract. | 180 requests per 15 min per user
450 requests per 15 min per App |
| Supports filtering using annotations |  | ✔ |
| Supports filtering using conversation\_id |  | ✔ |
| JSON key name for Tweet data array | results | data |
| Time granularity | Day, hour, or minute | Day, hour, or minute |
| Timezone | UTC | UTC |
| Request parameters for selecting time period | fromDate
toDate | start\_time
end\_time |
| Request parameters for navigating by Tweet ID |  | since\_id
until\_id |
| Requires the use of credentials from a developer App associated with a project |  | ✔ |


### 


Full-archive Tweet counts comparison


The following table compares the various types of full-archive search endpoints:




| Description | Enterprise | Twitter API v2 |
| --- | --- | --- |
| Host domain | https://gnip-api.twitter.com | https://api.twitter.com |
| Endpoint path | /search/fullarchive/accounts/:account\_name/:label/counts | /2/tweets/counts/all |
| Authentication | Basic auth | OAuth 2.0 Bearer Token |
| Timestamp format | YYYYMMDDHHMM | YYYY-MM-DDTHH:mm:ssZ
ISO 8601 / RFC 3339 |
| Returns Tweet counts that are no older than | The full archive since March 2006 | The full archive since March 2006 |
| HTTP methods supported | GET
POST | GET |
| Default request rate limits | The per minute rate limit will vary by partner as specified in your contract.
20 requests per sec | 300 requests per 15 min per App
1 request per 1 sec per App |
| Granularity | Day, hour, minute | Day, hour, minute |
| Supports filtering using annotations |  | ✔ |
| Supports filtering using conversation\_id |  | ✔ |
| JSON key name for Tweet data array | results | data |
| Request parameters for selecting time period | fromDate
toDate | start\_time
end\_time |
| Request parameters for navigating by Tweet ID |  | since\_id
until\_id |
| JSON key name for pagination | next | meta.next\_token |
| Request parameter for pagination | next\_token | next\_token or pagination\_token |
| Timezone | UTC | UTC |
| Requires the use of credentials from a developer App associated with a Project that has Academic Research access |  | ✔ |


### 


Filtering operator comparison


The two different versions (enterprise, and v2) of Tweet counts differ in which operators are available, and also have varying levels of operator availability within each version, which are explained below.


Enterprise


* There are no sub-tiers of enterprise operators. All enterprise operators are available to all enterprise users.


Twitter API v2


* **Core:** These operators are available to any v2 user.
* **Advanced:** These operators are only available to users that have been approved for Academic Research access.


You can learn more about each of these sets of operators in their respective guides:


* Enterprise operators
* Twitter API v2 operators


Now that we understand these different operator levels within Twitter API v2, here is the table that maps out operator availability for Tweet counts (note that if the cell is left blank, the operator is not available):




|  | Enterprise | v2 |
| --- | --- | --- |
| keyword | Available | Core |
| emoji | Available | Core |
| “exact phrase” | Available | Core |
| # | Available | Core |
| $ | Available | Advanced |
| @ | Available | Core |
| from: | Available | Core |
| to: | Available | Core |
| url: | Available | Core |
| retweets\_of: | Available | Core |
| context: |  | Core |
| entity: |  | Core - Only available with recent search |
| conversation\_id: |  | Core |
| place: | Available | Advanced |
| place\_country: | Available | Advanced |
| point\_radius: | Available | Advanced |
| bounding\_box: | Available | Advanced |
| is:retweet | Available | Core |
| is:reply | Available | Core |
| is:quote | Available | Core |
| is:verified | Available | Core |
| -is:nullcast | Available | Advanced |
| has:hashtags | Available | Core |
| has:cashtags | Available | Advanced |
| has:links | Available | Core |
| has:mentions | Available | Core |
| has:media | Available | Core |
| has:images | Available | Core |
| has:videos | Available | Core |
| has:geo | Available | Advanced |
| lang: | Available | Core |
| list: |  | Advanced |
| has:profile\_geo | Available |  |
| profile\_country | Available |  |
| profile\_locality | Available |  |
| profile\_region | Available |  |
| proximity | Available |  |









Other migration resources
-------------------------






Twitter API migration hub


Check out some sample code for these endpoints


Tweet counts: Enterprise to Twitter API v2



















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















