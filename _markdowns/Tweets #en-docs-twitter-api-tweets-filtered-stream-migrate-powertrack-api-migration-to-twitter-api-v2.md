



Filtered stream - PowerTrack API to Twitter API v2 migration guide | Docs | Twitter Developer Platform 





































































































PowerTrack API migration to Twitter API v2



PowerTrack API migration to Twitter API v2 filtered stream
----------------------------------------------------------


Use this migration guide to understand the similarities and differences between PowerTrack API and Twitter API v2 filtered stream, and to help migrate a current PowerTrack API integration to v2 filtered stream.


* **Similarities**
	+ Streaming delivery method
	+ Integration process
	+ Persistent stream connection with separate rules management endpoints
	+ Rule syntax
	+ Rule operators (with exceptions)
	+ Rule matching logic
	+ Support for Tweet edit history and metadata
* **Differences**
	+ Rule length
	+ Rule volume
	+ Endpoint URLs
	+ App and Project requirement for access
	+ Authentication method
	+ Request parameters
	+ Usage tracking
	+ Multiple streams, redundant conections, backfill and Replay recovery
	+ Request parameters and response format
	+ Response JSON data structure


### 


### Similarities


#### Streaming delivery method


Both PowerTrack and Twitter API v2 filtered stream use streaming data delivery, which require the client to establish an open connection to an endpoint and keeping a very long lived HTTP request, and parsing the response incrementally from the server in real time.  Both PowerTrack and Twitter API v2 filtered stream filter publicly available Tweets matching rules that exist on the stream in real time, and use keep-alive signals as new line characters (\r\n) to signal the connection is still active. Both PowerTrack and Twitter API v2 filtered stream endpoint connections deliver data in real time and should be read by the connecting client quickly.  


 


#### Integration process


Integrating with filtered stream is similar to integrating with PowerTrack, using the general process below:


1. Establish a streaming connection.
2. Asynchronously send separate requests to add and delete rules from the stream.
3. Reconnect to the stream automatically when connection is disconnected.


 


#### Persistent stream connection with separate rules management endpoints


Similar to the PowerTrack API and Rules API, the new Twitter API v2 filtered stream endpoints allows you to apply multiple rules to a single stream and add and remove rules to your stream while maintaining the stream connection.




|  |  |  |
| --- | --- | --- |
| **Feature** | **PowerTrack API** | **Twitter API v2 filtered stream** |
| **Connection endpoint** | GET /stream | GET /2/tweets/search/stream |
| **Add rules** | POST /rules | POST /2/tweets/search/stream/rules |
| **Get rules** | GET /rules | GET /2/tweets/search/stream/rules |
| **Delete rules** | POST /rules\_method=delete | POST /2/tweets/search/stream/rules |


#### 


#### Rule syntax, operators, and matching rules logic


The Twitter API v2 filtered stream uses a subset of the same rule operators currently used for PowerTrack rules. These operators are used to create boolean based rule syntax used for filtering desired matching Tweets from the live stream.  Both PowerTrack and filtered stream use the same rule syntax for building rules and matching logic is the same. While the majority of the operators are available for both PowerTrack and filter stream, there are a few notable differences and net new operators listed below.  For more details and example uses for each operator see current PowerTrack operators and current Twitter API v2 filtered stream operators. 


Please note that many operators (noted as 'advanced operators') are reserved for those users who have been approved for Academic Research access or Enterprise access.


Operators available with both PowerTrack and Twitter API v2 Filter stream:




| **Standalone operators** | **Conjunction required operators (must be used with at least one standalone operator within a rule)** |
| keyword (example: coffee )
emoji (example: 🐶 or \uD83D\uDC36 )
"exact phrase match" (example: "happy birthday" )
from:
to:
@
retweets\_of:
#
url: | has:links
lang:
has:mentions
has:media
has:images
has:videos
is:retweet
is:quote
is:verified
has:hashtags
has:geo
sample:
-is:nullcast |


 




|  |
| --- |
| **Net new operators available with Twitter API v2 filtered stream** |
| conversation\_id: - matches on Tweets that exist in any reply threads from the specified Tweet conversation root.Net new operators available with Twitter API v2 filtered stream:
context: - matches on Tweets that have been annotated with a context of interest. 
entity: - matches on Tweets that have been annotated with an entity of interest. |




|  |
| --- |
| **Operators currently only available on PowerTrack API** |
| url\_title:
url\_description:
followers\_count:
statuses\_count:
friends\_count:
listed\_count:
"proximity match"~3
contains:
has:symbols
url\_contains:
in\_reply\_to\_status\_id:
retweets\_of\_status\_id:
source:
bio:
bio\_name:
bio\_location:
place:
place\_country:
point\_radius:
bounding\_box:
is:reply
 
(Available without conjunction)
has:links
lang:
has:mentions
has:media
has:images
has:videos
is:retweet
is:quote
is:verified
is:reply
has:hashtags
has:geo
sample: |


**Support for Tweet edit history and metadata**  




Both versions provide metadata that describes any edit history. Check out the filtered stream API References and the Edit Tweets fundamentals page for more details. 


 


### Differences


#### Rule length


Rule length is measured the same way (by character count) for both PowerTrack and filtered stream rules, however the maximum length for PowerTrack rules is 2048 characters and the maximum rule length for rules on Twitter API v2 filtered stream varies by access level. 


Essential and Elevated access - 512 characters  

Academic Research access - 1024 characters  

 Enterprise access - 2048 characters   




#### Rule volume


The PowerTrack maximum rule volume per stream is defined within the enterprise account contract.  Twitter API v2 filtered stream rule volume varies by access level.


Essential access - 5 rules  

Elevated access - 25 rules  

Academic research access - 1000 rules  

Enterprise access - 2500+ rules  

 


#### Endpoint URLs


* PowerTrack endpoints:
	+ https://gnip-stream.twitter.com/stream/powertrack/accounts/{account\_name}/publishers/twitter/{stream\_label}.json
	+ https://gnip-api.twitter.com/rules/powertrack/accounts/{account\_name}/publishers/twitter/{stream\_label}.json
	+ https://gnip-api.twitter.com/rules/powertrack/accounts/{account\_name}/publishers/twitter/{stream\_label}/validation.json
* Twitter API v2 endpoint:
	+ https://api.twitter.com/2/tweets/search/stream
	+ https://api.twitter.com/2/tweets/search/stream/rule


#### 
App and Project requirements for v2 access


PowerTrack access is granted through a contracted annual subscription for data, and set up through console.gnip.com by your account manager at Twitter.  PowerTrack does not require a Twitter developer App to access.  In order to use the Twitter API v2 filter stream, you must have signed up for a Twitter developer account, and a Twitter developer App associated with a Project. The developer App and Project setup for Twitter API v2 access is all done through the developer portal.  


 


#### Authentication method


The PowerTrack API endpoints use Basic Authentication set up in console.gnip.com. The Twitter API v2 filtered stream endpoints require a Twitter developer App and an OAuth 2.0 App Access Token (also referred to as Application-only or Bearer Authentication). To make requests to the Twitter API v2 version you must use your specific developer App's Access Token to authenticate your requests.


In the process of setting up your developer account, developer App and Project, an App Access Token is created and shared within the dev portal user interface, however, you can generate a new one by navigating to your app's “Keys and tokens” page on the developer portal. If you’d like to generate/destroy the App Access Tokens programmatically, see this OAuth 2.0 App-Only guide.


 


#### Usage tracking


PowerTrack usage can be retrieved programatically using the Usage API, or can be seen in console.gnip.com on the usage tab.  Tweet consumption across all PowerTrack streams is deduplicated each day and volume consumption is defined within the enterprise contract. 


Twitter API v2 filtered stream usage can be tracked within the developer portal at the Project level.  Tweet consumption is set at the Project level and is shared across several different Twitter API v2 endpoints, including filtered stream, recent search, user Tweet timeline and user mention timeline.  Currently with Basic Access, the monthly Tweet consumption limit is 500,000 Tweets per month total, and Tweets are not deduplicated across products or time.


#### 


#### Multiple streams, redundant conections, backfill and Replay API for recovery


There are several recovery and redunancy features available via PowerTrack, some of which are not yet available for Twitter API v2 filtered stream.  For PowerTrack, all recovery and redundancy features are configured within the enterprise contract. PowerTrack API currently has the flexibility to offer multiple PowerTrack streams (commonly "dev" and "production") with unique rulesets.  Currently, the Twitter API v2 filtered stream is only available with a single stream.


PowerTrack allows you to connect to have multiple connections to a single stream, generally used for redundant connections to different data centers or clients. If you have Academic Research access, you will have access redundant connections, enabling you to make up to two connections to a single stream.


If a PowerTrack stream is disconnected breifly, a reconnection can be made using the backfillMinutes parameter to reduce the chance of data loss within five minutes of the disconection. While we have added this functionality to the Twitter API v2 version, it is currently only available with Academic Research access, and has been renamed to backfill\_minutes.


If a PowerTrack stream is disconnected for longer than a 5 minute period, the separate Replay API can be used to recover data for up to a 2 hour period in the recent 5 day past.  Currently, the Twitter API v2 filtered stream does not have a replay feature.


 


#### Request parameters and response format


One of the biggest differences between PowerTrack API and Twitter API v2 filtered stream is the parameter functionality.


Using the Twitter API v2 filtered stream, there are several parameters used on the connection request to identify which fields or expanded objects to return in the Tweet payload.  This is common for all v2 endpoints. By default, only the Tweet id and text are returned for matching Tweets but additional parameters, fields and expansions described below, can be added in order to recieve more detailed data per matching Tweet. 


fields: Twitter API v2 endpoints enable you to select which fields are provided in your payload. For example, Tweet, User, Media, Place, and Poll objects all have a list of fields that can be returned (or not). 


expansions: Used to expand the complementary objects referenced in Tweet JSON payloads. For example, all Retweets and Replies reference other Tweets. By setting expansions=referenced\_tweets.id, these other Tweet objects are expanded according to the `tweet.fields` setting.  Other objects such as users, polls, and media can be expanded.



https://api.twitter.com/2/tweets/search/stream?tweet.fields=created\_at,public\_metrics,author\_id,entities&expansions=attachments.poll\_ids


You can learn more about how to use fields and expansions by visiting our guide, and by reading through our broader data dictionary.




|  |  |
| --- | --- |
| **Connection to PowerTrack** | **Example request to Twitter API v2 filtered stream** |
| 
```

curl --compressed -v -uexample@customer.com "https://gnip-stream.twitter.com/stream/powertrack/accounts/:account_name/publishers/twitter/:stream_label.json"

```
 | 
```

curl "https://api.twitter.com/2/tweets/search/stream?tweet.fields=attachments,author_id,context_annotations,conversation_id,created_at,entities,geo,id,in_reply_to_user_id,lang,possibly_sensitive,public_metrics,referenced_tweets,reply_settings,source,text,withheld&user.fields=created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,public_metrics,url,username,verified,withheld&expansions=author_id,referenced_tweets.id,referenced_tweets.id.author_id,entities.mentions.username,attachments.poll_ids,attachments.media_keys,in_reply_to_user_id,geo.place_id&place.fields=contained_within,country,country_code,full_name,geo,id,name,place_type&poll.fields=duration_minutes,end_datetime,id,options,voting_status" -H "Authorization: Bearer $ACCESS_TOKEN"

```
 |


The PowerTrack API data format is set within console.gnip.com at the stream settings level, which can be set to either the Twitter native enriched format or Activity streams format. 


PowerTrack API only uses one optional parameter on connection, to reconnect using backfill (backfillMinutes=5). This optional parameter is also available to filtered stream, but is called backfill\_minutes, and is only available via Academic Research access.  

 



```

https://gnip-stream.twitter.com/stream/powertrack/accounts/{account_name}/publishers/twitter/{stream_label}.json?backfillMinutes=5

```

 


#### Response structure and data format


As described above, the request parameters set at the connection request for Twitter API v2 filtered stream determine the response data returned.  There are several different response possibilites using different fields and expansions which can range from the most simple default response with only the Tweet id and text, to an extremely detailed and expanded data payload.


The data format for PowerTrack is set within console.gnip.com at the stream settings level, which can be set to either the Twitter Native Enriched format or Activity Streams format. 


The following table references Tweet response examples in each different format:




|  |  |  |
| --- | --- | --- |
| **Native enriched format** | **Activity streams format** | **Twitter API v2 filtered stream format** |
| Payload examples | Payload examples | Payload examples |


If you would like to know more about how the enterprise data formats map to the Twitter API v2 format, please visit our following guides:


* Native Enriched to Twitter API v2 format migration guide
* Activity Streams to Twitter API v2 format migration guide



















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















