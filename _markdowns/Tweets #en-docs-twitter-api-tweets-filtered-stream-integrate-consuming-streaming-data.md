



Filtered stream - Consuming streaming data | Docs | Twitter Developer Platform 





































































































Consuming streaming data



Building a client to consume streaming data
-------------------------------------------


When using a streaming endpoint, there are some general best practices to consider in order to optimize usage.    

 


#### Client design


When building a solution with the filter stream endpoint, you will need a client that can do the following:


1. Establish an HTTPS streaming connection to the filter stream endpoint.
2. Asynchronously send POST requests to the filter stream rules endpoint to add and delete rules from the stream.
3. Handle low data volumes – Maintain the streaming connection, detecting Tweet objects and keep-alive signals
4. Handle high data volumes – de-couple stream ingestion from additional processing using asynchronous processes, and ensure client side buffers are flushed regularly.
5. Manage volume consumption tracking on the client side.
6. Detect stream disconnections, evaluate and reconnect to the stream automatically.


#### Connecting to a streaming endpoint


Establishing a connection to Twitter API v2 streaming endpoints means making a very long lived HTTP request, and parsing the response incrementally. Conceptually, you can think of it as downloading an infinitely long file over HTTP.  Once a connection has been established, the Twitter server will deliver Tweet events through the connection as long as the connection is open.  

 


#### Consuming data in real time


Note that the individual fields of JSON objects are not ordered, and not all fields will be present in all circumstances. Similarly, separate activities are not delivered in sorted order, and duplicate messages may be encountered. Keep in mind that over time, new message types may be added and sent through the stream.


Thus, your client must tolerate:


* Fields appearing in any order
* Unexpected or missing fields
* Non-sorted Tweets
* Duplicate messages
* New arbitrary message types coming down the stream at any time


In addition to relevant Tweet data and requested field parameters, the following kinds of messages may be delivered on a stream connection. Note that this list may not be comprehensive—additional objects may be introduced into streams. Ensure that your parser is tolerant of unexpected message formats.  

 


#### Buffering


The streaming endpoints will send data to you as quickly as it becomes available, which can result in high volumes in many cases. If the Twitter server cannot write new data to the stream right away (for example if your client is not reading fast enough, see handling disconnections for more), it will buffer the content on its end to allow your client to catch up. However, when this buffer is full, a forced disconnect will be initiated to drop the connection, and the buffered Tweets will be dropped and not resent. See below for more details.


One way to identify times where your app is falling behind is to compare the timestamp of the Tweets being received with the current time, and track this over time.


Although stream backups cannot ever be completely eliminated due to potential latency and hiccups over the public internet, they can be largely eliminated through proper configuration of your app. To minimize the occurrence of backups:


* Ensure that your client is reading the stream fast enough. Typically you should not do any real processing work as you read the stream. Read the stream and hand the activity to another thread/process/data store to do your processing asynchronously.
* Ensure that your data center has inbound bandwidth sufficient to accomodate large sustained data volumes as well as significantly larger spikes (e.g. 5-10x normal volume). For filtered stream, the volume and corresponding bandwidth required on your end are wholly dependent on what Tweets your rules are matching.


#### Usage tracking and rule management


As developers expectations around what “normal” data volume should be for their streams, we do not have a general recommendation for a specific percentage decrease/increase or period of time. 


Consider monitoring your stream data volumes for unexpected deviations. A data volume decrease may be symptomatic of a different issue than a stream disconnection. In such a situation, a stream would still be receiving the keep-alive signal and probably some new activity data. However, a significantly decreased number of Tweets should lead you to investigate whether there is anything causing the decrease in inbound data volume to your application or network, check the status page for any related notices.


To create such monitoring, you could track the number of new Tweets you expect to see in a set amount of time. If a stream’s data volume falls far enough below the specified threshold, and does not recover within a set period of time, then alerts and notifications should be initiated. You may also want to monitor for a large increase in data volume, particularly if you are in the process of modifying rules in a filtered stream, or if an event occurs that produces a spike in Tweet activity.


It's important to note that Tweets delivered through filtered stream do count towards the total monthly Tweet volume, and you should track and adjust consumption in order to optimize.  If volume is high, consider adding a sample: operator to each of your rules to reduce from 100% matching to sample:50 or sample:25 when necessary.


Additionally, we encourage you to implement measures within your app that will alert your team if the volume passes a pre-set threshold, and to possibly introduce other measures such as automated deletion of rules that are bringing in too much data, or disconnecting from the stream completely in extreme circumstances.  

 


#### Responding to system messages


Keep-alive signals  

At least every 20 seconds, the stream will send a keep-alive signal, or heartbeat in the form of an \r\n carriage return through the open connection to prevent your client from timing out. Your client application should be tolerant of the \r\n characters in the stream.


If your client properly implements a read timeout on your HTTP library, your app will be able to rely on the HTTP protocol and your HTTP library to throw an event if no data is read within this period, and you will not need to explicitly monitor for the \r\n character.


This event will typically be an exception being thrown or some other event depending on the HTTP library used. It is highly recommended to wrap your HTTP methods with error/event handlers to detect these timeouts. On timeout, your application should attempt to reconnect.


Error messages  

The v2 streaming endpoints may also deliver in stream error messages. Provided below is the basic format of these messages, along with some examples. Please note that the messages delivered could change, with new message being introduced. Client applications need to be tolerant of changing system message payloads.


Note that error messages will link to the documentation describing how to solve the problem.


Message format:












```

      {
	"errors": [{
		"title": "operational-disconnect",
		"disconnect_type": "UpstreamOperationalDisconnect",
		"detail": "This stream has been disconnected upstream for operational reasons.",
		"type": "https://api.twitter.com/2/problems/operational-disconnect"
	}]
}
    
```





Code copied to clipboard








  

Note that error messages indicating a force disconnect for a full buffer may never get to your client, if the backup which caused the force disconnect prevents it from getting through. Accordingly, your app should not depend on these messages to initiate a reconnect.  





















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















