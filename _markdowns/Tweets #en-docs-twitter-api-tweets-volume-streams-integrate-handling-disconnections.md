



Sampled stream - Handling disconnections | Docs | Twitter Developer Platform 





































































































Handling disconnections



What is a disconnection?
------------------------


Establishing a connection to the streaming APIs means making a very long lived HTTPS request, and parsing the response incrementally. When connecting to the sampled stream endpoint, you should form a HTTPS request and consume the resulting stream for as long as is practical. Our servers will hold the connection open indefinitely, barring server-side error, excessive client-side lag, network issues, routine server maintenance, or duplicate logins. With connections to streaming endpoints, it is likely, and should be expected, that disconnections will take place and reconnection logic built.  

 


### Why a streaming connection might be disconnected


Your stream can disconnect for a number of reasons. Inspect the error message returned by the stream to understand the reason for the failure. Possible reasons for disconnections are as follows:


* An authentication error (such as a wrong token or a wrong authentication method being used).
* A streaming server is restarted on the Twitter side. This is usually related to a code deploy and should be generally expected and designed around.
* Your client is not keeping up with the volume of Tweets the stream is delivering or is reading data too slowly. Every streaming connection is backed by a queue of messages to be sent to the client. If this queue grows too large over time, the connection will be closed.
* Your account exceeded your daily/monthly quota of Tweets.
* You have too many active redundant connections.
* A client stops reading data suddenly. If the rate of Tweets being read off of the stream drops suddenly, the connection will be closed.
* Possible networking issues between server and client
* A temporary server side issue, scheduled maintenance and updates. (Check the status page)


#### Common disconnection errors include:












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

















```

      
{
	"title": "ConnectionException",
	"detail": "This stream is currently at the maximum allowed connection limit.",
	"connection_issue": "TooManyConnections",
	"type": "https://api.twitter.com/2/problems/streaming-connection"
}
    
```





Code copied to clipboard








 


### Anticipating disconnects and reconnecting


When streaming Tweets, the goal is to stay connected for as long as possible, recognizing that disconnects may occur. The endpoint provides a 20-second keep alive heartbeat (it will look like a new line character). Use this signal to detect if you’re being disconnected.


1. Your code should detect when fresh content and the heartbeat stop arriving.
2. If that happens, your code should trigger a reconnection logic. Some clients and languages allow you to specify a read timeout, which you can set to 20 seconds.
3. Your service should detect these disconnections and reconnect as soon as possible.


The code samples on the API reference page provide an example of this reconnect logic.


Once an established connection drops, attempt to reconnect immediately. If the reconnect fails, slow down your reconnect attempts according to the type of error experienced:


* Back off linearly for TCP/IP level network errors. These problems are generally temporary and tend to clear quickly. Increase the delay in reconnects by 250ms each attempt, up to 16 seconds.
* Back off exponentially for HTTP errors for which reconnecting would be appropriate. Start with a 5 second wait, doubling each attempt, up to 320 seconds.
* Back off exponentially for HTTP 429 errors Rate limit exceeded. Start with a 1 minute wait and double each attempt. Note that every HTTP 429 received increases the time you must wait until rate limiting will no longer be in effect for your account.


### Rate limits and usage


To check connection limits response will return three headers. This is useful to understand how many reconnections attempts are allowed for the streaming endpoint.


* x-rate-limit-limit indicates the number of allotted requests your client is allowed to make during the 15-minute window.
* x-rate-limit-remaining indicates the number of requests made so far in the 15-minute window.
* x-rate-limit-reset is a UNIX timestamp indicating when the 15-minute window will restart, resetting x-rate-limit-remaining to 0.


The sampled stream endpoint does not currently report usage data. To check how many Tweets have been delivered, your code can implement a metering logic, so that consumption can be measured and paused if needed. 


Your code that hosts the client side of the stream simply inserts incoming Tweets into a first in, first out (FIFO) queue, or a similar memory structure; a separate process/thread should consume Tweets from that queue to parse and prepare content for storage. With this design, you can implement a service that can scale efficiently in case incoming Tweet volumes changes dramatically. Conceptually, you can think of it as downloading an infinitely long file over HTTP.


 


### Reconnection best practices


#### Test backoff strategies


A good way to test a backoff implementation is to use invalid authorization credentials and examine the reconnect attempts. A good implementation will not get any 429 responses.


#### Issue alerts for multiple reconnects


If a client reaches its upper threshold of its time between reconnects, it should send you notifications so you can triage the issues affecting your connection.


#### Handle DNS changes


Test that your client process honors the DNS Time To live (TTL). Some stacks will cache a resolved address for the duration of the process and will not pick up DNS changes within the prescribed TTL. Such aggressive caching will lead to service disruptions on your client as Twitter shifts load between IP addresses.


#### User Agent


Ensure your user-agent HTTP header includes the client’s version. This will be critical in diagnosing issues on Twitter’s end. If your environment precludes setting the user-agent field, then set an x-user-agent header.


 



















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















