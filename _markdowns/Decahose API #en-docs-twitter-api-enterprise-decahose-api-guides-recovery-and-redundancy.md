



Recovery and redundancy | Docs | Twitter Developer Platform 





































































































Recovery and redundancy



Introduction
------------


With streaming high volumes of realtime Tweets comes a set of best practices that promote both data reliability and data full-fidelity. When consuming realtime data, maximizing your connection time is a fundamental goal. When disconnects occur, it is important to automatically detect that and reconnect. After reconnecting it’s important to assess if there are any periods to backfill data for. The component that manages these details and consumes realtime Tweets is only one part of a system with network, datastore, server, and storage concerns. Given the complexity of these systems, another best practice is to have different streaming environments, with at least separate streams for development/testing and production.


Decahose comes with a set of features that help with these efforts.


1. To support multiple environments, we can deploy Additional Streams for your account. These streams are independent of each other and have a different stream\_label  to help differentiate them.
2. To help support maintaining a connection, each Decahose stream supports Redundant Connections. The most common architecture is for a stream to have two connections, and on the client-side there are two independent consumers –ideally on different networks. With this design, there can be redundancy across the client-side networks, servers, and datastore pathways. Note that a full-copy of the data is served on each connection and the client-side must be tolerant of and manage duplicate data.
3. A '**heartbeat**' will be provided every 10 seconds; however, with the Decahose stream, the volume of data is high enough that even a small duration (e.g., a few seconds) of no Tweets can indicate a connection issue. Therfore, both a 'data silence' and lack of a heartbeat can be used to detect a disconnect.


Since disconnects will happen, the Decahose stream has a dedicated Recovery and a Backfill feature to help recover data that was missed due to disconnections and other operational issues.


Additional Streams
------------------


Having additional Decahose streams is another way to help build reliability into your solution. Any additional streams are completely independent, having their unique endpoint. Each stream is assigned its own stream\_label, and this label, along with your account name, are part of that stream’s URL. See the example below:


https://gnip-stream.twitter.com/stream/sample10/accounts/:account\_name/publishers/twitter/:stream\_label.json


The most common convention is to have a realtime stream dedicated for you production system, and an additional stream available for development and testing. Having a test/development stream enables Decahose customers to have a stream to test client consumer updates. While any (unique) label can be assigned to a stream, one convention is to use ‘prod’ for production stream, and ‘dev’ or ‘sandbox’ for an additional development stream.


The number of streams, and their unique labels, is configurable by your account representative.


Redundant Connections
---------------------


A redundant connection simply allows you to establish more than one simultaneous connection to the data stream. This provides redundancy by allowing you to connect to the same stream with two separate consumers, receiving the same data through both connections. Thus, your app has a hot failover for various situations, e.g. where one stream is disconnected or where your app’s primary server fails.


The number of connections allowed for any given stream is configurable by your account representative. To use a redundant stream, simply connect to the same URL used for your primary connection. The data for your stream will be sent through both connections, with both stream connections represented on the stream dashboard.


Note that for billing purposes, we deduplicate the activity counts you receive through multiple connections such that you are only billed for each unique activity once. Given the Decahose has two partitions, here's an example of how the connection count works below:


Connect to decahose partition=1  

Connect to decahose partition=1  

Connect to decahose partition=2


The above situation yields a total of three connections – two connections to partition=1 and one connection to partition=2. Normally, you would want the same number of connections to each partition, so this example highlights a situation where the redundant connection to partition=2 has dropped and you want to further invstigate.


Recovery
--------


#### Overview


Recovery is a data recovery tool (not to be used for primary data collection) that provides streaming access to a rolling 5-day window of recent Twitter historical data. It should be utilized to recover data in scenarios where your consuming application misses data in the realtime stream, whether due to disconnecting for a short period, or for any other scenario where you fail to ingest realtime data for a period of time.


#### Using Recovery


With the Recovery stream, your app can make requests to it that operate in the same manner as requests to the realtime streams. However, your app must specify parameters in the URL that indicate the time window you are requesting. In other words, a Recovery request asks the API for "Tweets from time A to time B." These Tweets are then delivered through your streaming connection in a manner that mimics the realtime stream, but at a slightly slower-than-realtime rate. See below for example:


  

"https://stream-data-api.twitter.com/stream/powertrack/accounts/someAccountName/publishers/twitter/powertrack.json?startTime=2023-07-05T17:09:12.070Z"


Tweets are delivered beginning with the first (oldest) minute of the specified time period, continuing chronologically until the final minute is delivered. At that point, aRecovery Request Completed message is sent through the connection, and the connection is then closed by the server. If your request begins at a time of day where little or no matching results occurred, there will likely be some period of time before the first results are delivered – data will be delivered when Recovery encounters matches in the portion of the archive being processed at that time. When no results are available to deliver, the stream will continue sending carriage-return, or "heartbeats", through the connection to prevent you from timing out.


Recovery is intended as a tool for easily recovering data missed due to short disconnects, not for very long time periods like an entire day. If the need to recover data for long periods arises, we recommend breaking longer requests into shorter time windows (e.g. two hours) to reduce the possibility of being disconnected mid-request due to internet volatility or other reasons, and to provide more visibility into the progress of long requests.


#### Data Availability


You can use the Recovery feature to recover missed data within the last 24 hours if you are unable to reconnect with the 5 minute backfill window.


The streaming recovery feature allows you to have an extended backfill window of 24 hours. Recovery enables you to ‘recover’ the time period of missed data. A recovery stream is started when you make a connection request using 'start\_time' and 'end\_time' request parameters. Once connected, Recovery will re-stream the time period indicated, then disconnect.  


You will be able to make 2 concurrent requests to recovery at the same time, i.e. “two recovery jobs”. Recovery works technically in the same way as backfill, except a start and end time is defined. A recovery period is for a single time range.


 


Backfill
--------


To request backfill, you need to add a backfillMinutes=N parameter to your connection request, where N is the number of minutes (1-5, whole numbers only) to backfill when the connection is made. For example, if you disconnect for 90 seconds, you should add backfillMinutes=2 to your connection request. Since this request will provide backfill for 2 minutes, including for the 30-second period before you disconnected, your *consumer app must be tolerant of duplicate data*.


An example Decahose connection request URL, requesting a 5 minute backfill to partition 1, looks like:


https://gnip-stream.twitter.com/stream/sample10/accounts/:account\_name/publishers/twitter/:stream\_label.json?partition=1&backfillMinutes=5  




**NOTES:**


* You do have the option to always use ‘backfillMinutes=5’ when you connect, then handling any duplicate data that is provided.
* If you are disconnected for more than five minutes, you can recover data using Recovery.


Recovering from Disconnect
--------------------------


Restarting and recovering from a disconnect involves several steps:


* Determining length of disconnect time period.
	+ 5 minutes or less?
		- If you have Backfill enabled for stream, prepare connection request with appropriate ‘backfillMinutes’ parameter.
	+ More than 5 minutes?
		- If you have a Recovery stream, make a Recovery request for the disconnected time period (ideally with your current realtime rule set, using the Rules API if necessary).
* Request a new connection.


When you experience disconnects or downtime, here are strategies to mitigate and recover in this scenario:


1. **Implement backfill**  

Backfill lets you reconnect from a point prior to disconnecting from a stream connection, and covers disconnects of up to 5 minutes. It is implemented by including a parameter in the connection request.
2. **Consume a redundant stream from another location**  

If the redundant stream can be streamed into the same live environment, deduplicating data, you will eliminate the need for recovery unless BOTH the normal stream and redundant stream experience simultaneous downtime or disconnects. If the redundant stream cannot be streamed live into the production environment, it can be written into a separate “emergency” data store. Then, in the event of disconnects or downtime on the primary stream connection, your system will have data on hand to fill in your primary database for the period of time where data is missing
3. **Implement Recovery**  

Where disconnects or downtime affect both the primary stream and redundant stream, use the Decahose Recovery to recover any data missed. The API provides a rolling window covering 5 days of the archive, and would be best utilized by requesting no more than an hour of that window at a time, and streaming it in. This is done in parallel to the realtime stream. Note that we do not have solutions for recovering Decahose data from beyond the 5 day window provided by Recovery, so it is important for you to utilize a redundant stream to ensure you have a complete copy of data on your side in the case of significant downtime on your side.


When you detect abnormal stored data volumes-   

Potential ways you can detect missing data where no disconnects or downtime occurred…


1. Count inbound Tweets  

Your system should count the raw number of Tweets you receive at the very beginning of your ingestion app, and then provide a way to compare those numbers to the number of Tweets that reaches your final data store. Any differences can be monitored, and alert your team to issues causing data to be dropped after it is received.
2. Analyze for abnormal stored volumes  

You may also want to analyze the volumes of stored data in your final database to look for abnormal drops. This can indicate issues as well, although there will likely be circumstances in which drops in volume are normal (e.g. if the Twitter platform is unavailable and people are not able to create Tweets for some period of time).



















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















