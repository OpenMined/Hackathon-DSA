



Filtered stream - Recovery and redundancy features | Docs | Twitter Developer Platform 





































































































Recovery and redundancy features








Note:These recovery and redundancy features are only available to those that have Enterprise access.









Introduction
------------


When consuming realtime data, maximizing your connection time and receiving all matched data is a fundamental goal. This means that it is important to take advantage of redundant connections, automatically detect disconnections, to reconnect quickly, and to have a plan for recovering lost data.


In this integration guide, we will discuss different recovery and redundancy features: redundant connections, backfill, and recovery.  

 


### Redundant connections


A redundant connection simply allows you to establish more than one simultaneous connections to the filtered stream. This provides redundancy by allowing you to connect to the same stream with two separate consumers, receiving the same data through both connections. Thus, your app has a hot failover for various situations such as if one stream is disconnected or if your application's primary server fails.


Filtered stream currently only allows Projects with Enterprise access to connect to up to two redundant connections. To use a redundant stream, simply connect to the same URL used for your primary connection. The data for your stream will be sent through both connections.


### Recovering missed data after a disconnection: Backfill


After you've detected a disconnection, your system should be smart enough to reconnect to the stream. If possible, your system should take note of how long the disconnection lasted so that you can use the proper recovery feature to backfill the data. 


If you are using a Project with Enterprise access and identified that the disconnection lasted five minutes or less, you can use the backfill parameter, backfill\_minutes. If you pass this parameter with your GET /tweets/search/stream request, you will receive the Tweets that match your rules within the past one to five minutes. We generally deliver these older Tweets first before any newly matched Tweets, and also do not deduplicate Tweets. This means that if you were disconnected for 90 seconds, but request two minutes worth of backfill data, you will receive 30 seconds worth of duplicate Tweets, which your system should be tolerant of. Here is an example of what a request might look like with the backfill parameter:












```

      curl 'https://api.twitter.com/2/tweets/search/stream?backfill_minutes=5' -H "Authorization: Bearer $ACCESS_TOKEN"
    
```





Code copied to clipboard








  

If you don't have Enterprise access, or identified that the disconnection time lasted for longer than five minutes, you can utilize the recent search endpoint or the recovery feature to request missed data. However, note that the search Tweets endpoints do not include the sample:, bio:, bio\_name:, or bio\_location: operators, and has certain differences in matching behavior when using accents and diacritics with the keyword and #hashtag operators. These differences could mean that you don't fully recover all Tweets that might have been received via the filtered stream endpoints. 


 






### Recovering missed data after a disconnection: Recovery


If you are using a Project with Enterprise access, you can use the Recovery feature to recover missed data within the last 24 hours if you are unable to reconnect with the 5 minute backfill window.


The streaming recovery feature allows you to have an extended backfill window of 24 hours. Recovery enables you to 'replay' the time period of missed data. A recovery stream is started when you make a connection request using 'start\_time' and 'end\_time' request parameters. Once connected, Recovery will re-stream the time period indicated, then disconnect.  


You will be able to make 2 concurrent requests to recovery at the same time, i.e. “two recovery jobs”. Recovery works technically in the same way as backfill, except a start and end time is defined. A recovery period is for a single time range.


 




|  |  |  |
| --- | --- | --- |
| **Name** | **Type** | **Description** |
| start\_time | date (ISO 8601) | YYYY-MM-DDTHH:mm:ssZ (ISO 8601/RFC 3339).
Date in UTC signifying the start time to recover from. |
| end\_time | date (ISO 8601) | YYYY-MM-DDTHH:mm:ssZ (ISO 8601/RFC 3339).
Date in UTC signifying the end time to recover to. |


  

Example request URL: https://api.twitter.com/2/tweets/search/stream?start\_time=2022-07-12T15:10:00Z&end\_time=2022-07-12T15:20:00Z  




 



















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















