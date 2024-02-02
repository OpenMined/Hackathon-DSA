



FAQ | Docs | Twitter Developer Platform 





































































































FAQ



Frequently asked questions
--------------------------


Enterprise


### Realtime PowerTrack API


**I am interested in Twitter data and would like to find out approximate subscription costs.**


Please fill out this form to get in touch with our Sales team.  

 


**What are some of the features provided by realtime PowerTrack?**  




By connecting directly to our data services, you can take advantage of many enterprise-ready features that provide reliable connectivity and full-fidelity data. As an enterprise licensed-access offering, realtime PowerTrack includes tools for dynamic filtering, consistent connection, data recovery and data compliance management. This technology, paired with operational monitoring, guaranteed support and integration services allows businesses to start with a strong foundation to serve their own customers.


These features include:


* Dynamic rule updates while connected to the stream. There is no need to disconnect your stream while you update your stream’s ruleset.
* Support for multiple connections to each stream.
* Ability to automatically recover data that is missed during brief disconnects when you reconnect within 5 minutes with Backfill.
* Availability of Recovery feature to recover missed data within the last 24 hours if you are unable to reconnect with the 5 minute backfill window.
* Availability of additional streams for testing and development.
* Status dashboard to communicate with customers about any operational issues.


**How do I consume streaming data?**


Realtime streams of data are initiated by sending a HTTP GET command to your custom `https://gnip-stream.twitter.com` URL. HTTP streaming connections are requested with HTTP headers that indicate a ‘keep-alive’ connection. More information on realtime streaming is available here.


Given the potential of high volumes of Twitter data delivered in a stream, it is highly recommended that incoming data is processed in an asynchronous fashion. What this means is that your code that ‘hosts’ the client side of the stream simply inserts incoming Tweets into a (FIFO) queue, or similar memory structure, and then you have a separate process/thread that consumes Tweets from that queue and does more of the ‘heavy lifting’ of parsing and preparing the data for storage. With this design, you can implement a process that will bend but not break in case incoming data volumes change dramatically.  

 


**How can multiple customers, projects, and campaigns be managed in a single stream?**


The vast majority of realtime PowerTrack users manage multiple customers, projects, and campaigns within a single realtime stream by using PowerTrack rule ‘tags’. Rule tags have no special meaning, they are simply treated as opaque strings carried along with the rule. They will be included in the “matching rules” metadata in activities returned.


Tags provide an easy way to create logical groupings of PowerTrack rules. For example, you may generate a unique ID for a specific rule as its tag and allow your application to reference that ID within activities it processes to associate a result with specific customers, campaigns, categories, or other related groups.  

 


**How many connections to a given PowerTrack stream can I have at one time?**


PowerTrack streams support multiple connections to a single endpoint. Having multiple connections enables customers to build redundant data consumer clients, ideally on different networks. While PowerTrack streams default to a single connection, many customers prefer to have two connections per PowerTrack stream to ensure continuous delivery. If multiple connections are made to a single endpoint, and/or multiple streams exist with common rules, a given Tweet will be received multiple times. Note that for accounting purposes, the Tweet will be counted once.


Please talk to your Account Manager for more information.  

 


**How 'realtime' are the results? Is there any delay/elaboration time between the publication of a Tweet on Twitter and their release on the PowerTrack stream?**


Tweets that match your ruleset will be delivered to your stream within seconds of being published on the platform. There are variables, such as network connectivity and how your consuming application reads data off the stream; but all things being equal, you should receive Tweets within seconds of them being published.


Please note that the URL enrichment does cause an increased latency, due to the unwinding of each URL in the Tweet. 


Generally speaking, you should expect Volume streams (e.g. Firehose and Decahose) to be faster than PowerTrack, and PowerTrack to be fast than statuses/filter.  

 


**Is it possible to update several rules in one go?**


Yes, you can add or delete several rules with one request.  

  

However, note that the add and delete steps are separate and you will need two requests: one request to add one or several rule(s) and another request to delete one or several rule(s).


The upper limit number of rules that can either be added or be deleted in one go is a JSON body that is 5MB or less in size. Depending on the length of your rule values and tags, the upper number will be in the lower thousands.  

 


**Why isn't my rule appearing on the stream right away?**


Most rule additions take effect almost immediately. However, depending on factors such as network connectivity and rule size/complexity, it may take up to 5 minutes before you start receiving matching Tweets.  

 


**What if some Tweets are missing: I was expecting them to be returned by the stream, but they weren't?**


You can follow the next few steps to understand why some Tweets might not have been delivered:


1. Check your rule and ensure that you are using the correct operators.
2. Were you connected to the stream when the Tweet was created? You can use the 'Connections' tab in the console to check your connection history.
3. Was your rule already in place when the Tweet was created?
4. Note that if the account from which the Tweet was sent was private at the time the Tweet was created, the Tweet won't be returned - even if the account is public at the time of the request.
  


**If I lose the connection to the stream and then connect back, will I lose all Tweets from that duration?**


Yes, if you lose the connection to the stream, you may be missing data for the period of time that you were disconnected from the stream. Whenever a disconnection occurs, your client app must restart the process by establishing a new connection.


Additionally, to ensure that you do not miss any data, you may need to utilize a Redundant Connection, Backfill, or a Replay stream to mitigate or recover data from disconnections from the stream. Please see our answer to the next question for more information.  

 


**What if I get disconnected from the stream? How can I collect any data that was missed while disconnected?**


When streaming data, the goal is to stay connected for as long as possible, recognizing that disconnects will occur. PowerTrack streams provide a 15-second heartbeat (in the form of a new-line character) that enable client applications to detect disconnects. When fresh data and the heartbeat stop arriving, reconnection logic should be triggered. In most software languages this can be easily implemented by setting a data read timeout.


Any time you disconnect from the stream, you are potentially missing data that would have been sent if connected. However, there are multiple ways to mitigate these disconnects and recover data when they occur.


There is a range of tools available for retrieving historical tweets, including:


1. Redundant Streams - With multiple connections, consume the stream from multiple servers to prevent missed data when one is disconnected.
2. Recovery - Recover data within the last 24 hours.
3. Backfill - Reconnect within 5 minutes and start from where you left off.
4. Full Archive Search - Recover data from the entire Twitter archive.


  

Please also refer to our documentation on disconnects.  

 


**How fast is the streaming speed of Recovery?**


Recovery will deliver up to 1000 posts per second. It is intended to deliver the posts for the period of time that a customer is disconnected.


**Do you have any realtime PowerTrack code examples I can use to get started with?**


Yes, we have several realtime code examples available, including:


* Sample Python scripts
* Sample Ruby scripts


Note that these are only available to enterprise customers.


 **How do Edit Tweets impact my usage and billing?**  




Only the original Tweet will count for billing purposes. Any subsequent edits will be ignored and not contribute to your overall activity count. 


 


### 
Error troubleshooting guide


**Code 429 - Rate Limited: Your app has exceeded the limit on requests to add, delete, or list rules for this stream**


You may be receiving the 429 error code because you are adding or deleting rules too quickly. If you are adding or deleting rules individually, this could add up and exceed the rate limit.


A workaround could be to add or delete several rules at one time.


For example, the below sample cURL command shows you how to delete several rules at once:



```

curl -v -X POST -uexample@customer.com "https://gnip-api.twitter.com/rules/powertrack/accounts/:account_name/publishers/twitter/:stream_label.json?_method=delete" -d '{"rule_ids":[734938587381145604,734938587381174273]}"

```

  

You can learn more about adding or deleting rules and the relevant rate limits here.  

 


**Code 400**


A 400 error code normally indicates that the server was unable to process the request sent by the client due to poorly formatted JSON.


There are many reasons why this might be the case and you will need to double check the format of your JSON query.


For example, you may need to escape the quotes around the exact phrase match(es) in your rule (as in the example below):


{"rules":[{"tag":"test1","value":"coffee OR \"I love coffee\""}]}  




 **Frequent Disconnects - I am experiencing frequent disconnections on the stream and one of the following messages is being returned. Why is this happening?**


`This stream has been disconnected because your client was unable to keep up with us.`


`This stream has been disconnected for operational reasons.`


This kind of error occurs when your stream is not keeping up with the speed at which we are delivering data and your app isn't consuming the data from the stream fast enough.


We allow delivery to get behind for a period of time, and we have a temporary staging buffer amount for each stream on our side; but if you don't catch up, we initiate a disconnect to allow you to reconnect at the current point in time. Please note that this may lead to data loss (for data that is within the buffer at the time of the full buffer disconnect).


These can occur around large spikes in data. Generally, we recommend using a buffer process for consuming data quickly that is separate from the processing process.


You can find out more about optimizing your app to prevent disconnects like this in our articles on connection and on consuming streaming data here and here.



















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















