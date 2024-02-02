



Recovery and redundancy features | Docs | Twitter Developer Platform 





































































































Recovery and redundancy features



Introduction
------------


With streaming high volumes of realtime Tweets comes a set of best practices that promote both data reliability and data full-fidelity. When consuming realtime data, maximizing your connection time is a fundamental goal. When disconnects occur, it is important to automatically detect that and reconnect. After reconnecting it’s important to assess if there are any periods to backfill data for. The component that manages these details and consumes realtime Tweets is only one part of a system with network, datastore, server, and storage concerns. Given the complexity of these systems, another best practice is to have different streaming environments, with at least separate streams for development/testing and production.


PowerTrack comes with a set of features that help with these efforts.


To support multiple environments, we can deploy Additional Streams for your account. These streams are completely independent of each other, having unique URLs and separate rule sets.


To help support maintaining a connection, each realtime PowerTrack stream supports Redundant Connections. The most common architecture is for a stream to have two connections, and on the client-side there are two independent consumers, ideally on different networks. With this design, there can be redundancy across the client-side networks, servers, and datastore pathways. Note that a full-copy of the data is served on each connection (since there is a single ‘source’ server and no partitioning with filtered streams) and the client-side must be tolerant of and manage these duplicate data.


For detecting disconnects, each stream has a ‘heartbeat’ signal that can used to detect when a stream has timed-out. These 10-second heartbeats provide connection confirmation even when there are time periods with no Tweets matching your rules and being delivered on your stream. For most Twitter stream consumers, the data volumes are high enough that even a smaller duration of no Tweets is a sign of a connection issue. So both a ‘data silence’ and lack of a heartbeat can be used to detect a disconnect.


Since disconnects will happen, PowerTrack has a dedicated Recovery and a PowerTrack Backfill feature to help recover data that was missed due to disconnections and other operational issues. To learn more about disconnects see our support article HERE.  

 


Additional streams
------------------


Having additional PowerTrack streams is another way to help build reliability into your solution. So much so that it is considered a best practice. Any additional streams are completely independent, having their unique endpoint and independent rule set. Each stream is assigned its own ‘label’, and this label, along with your account name, are part of that stream’s URL.


https://gnip-stream.twitter.com/stream/powertrack/accounts/{ACCOUNT\_NAME}/publishers/twitter/{STREAM\_LABEL}.json  




The most common convention is to have a realtime stream dedicated for your production system, and an additional stream available for development and testing. Having a test/development stream enables PowerTrack customers to have a stream to test client consumer updates. While any (unique) label can be assigned to a stream, one convention is to use ‘prod’ for production stream, and ‘dev’ or ‘sandbox’ for an additional development stream.


The number of streams, and their unique labels, is configurable by your account representative.  

 


Redundant connections
---------------------


A redundant connection simply allows you to establish more than 1 simultaneous connections to the data stream. This provides redundancy by allowing you to connect to the same stream with two separate consumers, receiving the same data through both connections. Thus, your app has a hot failover for various situations, e.g. where one stream is disconnected or where your app’s primary server fails.


The number of connections allowed for any given stream is configurable by your account representative. To use a redundant stream, simply connect to the same URL used for your primary connection. The data for your stream will be sent through both connections, with both stream connections represented on the stream dashboard.


Note that for billing purposes, we deduplicate the activity counts you receive through multiple connections such that you are only billed for each unique activity once.  

 


Recovery
--------


#### Overview


Recovery is a data tool that provides streaming access to a rolling window of recent Twitter historical data. It should be utilized to recover data in scenarios where your consuming application misses data in the real time stream, whether due to disconnecting for a short period, or for any other scenario where you fail to ingest realtime data for a period of time.


There are different varieties of Recovery streams, corresponding to different types of realtime streams that they complement. PowerTrack Recovery streams are provided to allow customers using realtime PowerTrack to recover data they miss, using the same rules as they use in realtime.


#### Using Recovery


With the Recovery stream, your app can make requests to it that operate in the same manner as requests to existing realtime streams. However, your app must specify parameters in the URL that indicate the time window you are requesting. In other words, a Recovery request asks for “Posts from time A to time B.” These Posts are then delivered through your streaming connection in a manner that mimics the realtime stream.


Posts are delivered beginning with the first minute of the specified time period, continuing until the final minute is delivered. At that point, a “Recovery Request Completed” message is sent through the connection, and the connection is then closed by Gnip. If your request begins at a time of day where little or no matching results occurred, there will likely be some period of time before the first results are delivered – data will be delivered when Recovery encounters matches in the portion of the archive being processed at that time. When no results are available to deliver, the stream will continue sending carriage-return “heartbeats” through the connection to prevent you from timing out.


Recovery is intended as a tool for easily recovering data missed due to short disconnects, not for very long time periods like entire days. If the need to recover data for long periods arises, we recommend breaking longer requests into shorter time windows (e.g. two hours) to reduce the possibility of being disconnected mid-request due to internet volatility or other reasons, and to provide more visibility into the progress of long requests.


#### Data availability


You can use the Recovery feature to recover missed data within the last 24 hours if you are unable to reconnect with the 5 minute backfill window.


The streaming recovery feature allows you to have an extended backfill window of 24 hours. Recovery enables you to ‘recover’ the time period of missed data. A recovery stream is started when you make a connection request using 'startTime' and 'endTime' request parameters. Once connected, Recovery will re-stream the time period indicated, then disconnect.  


You will be able to make 2 concurrent requests to recovery at the same time, i.e. “two recovery jobs”. Recovery works technically in the same way as backfill, except a start and end time is defined. A recovery period is for a single time range.




| Name | Type | Description |
| --- | --- | --- |
| startTime | date (ISO 8601) | YYYY-MM-DDTHH:mm:ssZ (ISO 8601/RFC 3339).
Date in UTC signifying the start time to recover from. |
| endTime | date (ISO 8601) | YYYY-MM-DDTHH:mm:ssZ (ISO 8601/RFC 3339).
Date in UTC signifying the end time to recover to.
  |



Backfill
--------


The Backfill feature is used to request up to 5 minutes of stream data that is missed after a disconnect, and is available on PowerTrack and Volume streams as an *optional* feature.


To request backfill, you need to add a ‘backfillMinutes=number’ parameter to your connection request, where ‘number’ is the number of minutes (1-5, whole numbers only) to backfill when the connection is made. For example, if you disconnect for 90 seconds, you should add ‘backfillMinutes=2’ to your connection request. Since this request will provide backfill for 2 minutes, including for the 30-second period before you disconnected, your *consumer app must be tolerant of duplicate data*.


An example PowerTrack connection request URL, requesting a 5 minute backfill, looks like:


https://gnip-stream.twitter.com/stream/powertrack/accounts/{ACCOUNT\_NAME}/publishers/twitter/{STREAM\_LABEL}.json?backfillMinutes=5


**NOTES:**


* You do have the option to always use ‘backfillMinutes=5’ when you connect, then handling any duplicate data that is provided.
* If you are disconnected for more than five minutes, you can recover data using the Recovery.


Recovering from disconnect
--------------------------


Restarting and recovering from a disconnect involves several steps:


* Determining length of disconnect time period.
	+ 5 minutes or less?
		- If you have Backfill enabled for stream, prepare connection request with appropriate ‘backfillMinutes’ parameter.
	+ More than 5 minutes?
		- Make a connection request using 'startTime' and 'endTime' request parameters in order to start a recovery stream. The streaming recovery feature allows you to have an extended backfill window of 24 hours. Recovery enables you to 'replay' the time period of missed data.
* Request a new connection.



















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















