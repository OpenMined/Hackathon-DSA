



Account Activity replay API | Docs | Twitter Developer Platform 





































































































Account Activity replay API



Account Activity Replay API
---------------------------


Enterprise


The Account Activity Replay API is a data recovery tool that allows you to retrieve events from as far back as five days. It should be utilized to recover data in scenarios where your webhook server misses events, -- whether due to disconnections lasting longer than the retry window, or for those disaster recovery scenarios where you need a few days to restore your system back to normal.


The Account Activity Replay API was developed for any scenario where you fail to ingest activities for a period of time. It delivers activities to the same webhook used for the original real-time delivery of activities. This product is a recovery tool and not a backfill tool, which means events will only be replayed if a previous delivery of them was attempted. The Account Activity Replay API cannot deliver events for a time period prior to a subscription’s creation time.


### Using Account Activity Replay API


If your account is configured with Replay functionality, you can make requests in a similar manner as requests to the Account Activity API. It is important to note that your request must specify a webhook id parameter to indicate which webhook’s activities you would like to replay. In other words, a Replay request asks Account Activity Replay API to retrieve events from a start date and time to an end date and time based on the webhook id and application id.


Please note that UTC time is expected. These activities are delivered through the registered webhook associated with the id at a rate of up to 2,500 events per second. Also keep in mind that only one Replay job per webhook may be running at a time, although all subscriptions that were active during the date/time specified on that webhook will be replayed.


Events are delivered beginning with the first (oldest) minute of the specified time period, continuing chronologically (as best as possible) until the final minute is delivered. At that point, Replay will deliver a job completion event to the webhook. Because we work chronologically in delivering activities, if there are little or no matching results near the start time, there will likely be a period of time before the first results are delivered.


### Limitations


Replay is intended as a tool for easily recovering activities as far back as five days ago, but it will not deliver events prior to a subscription’s creation time. For example, if three days ago, you added a new subscription and ran a Replay job with a window for five days prior to today, you would only receive data for the three days that this new subscription was active.


### Data availability and types


Activities from the Account Activity Replay API are available five days from the initiation of the request, with new data becoming available roughly 10 minutes after a given activity is created. You will be able to make requests specifying a timeframe within this five day window using the from\_date and to\_date parameters within the request. Events that were originally delivered prior to having access to Replay cannot be replayed. For example, if your account was enabled for access to the Account Activity Replay API on June 1, 2019 at 3:30PM UTC, you would not be able to use Replay to retrieve any events prior to that date and time.


Continue to the Account Activity Replay API reference



















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















