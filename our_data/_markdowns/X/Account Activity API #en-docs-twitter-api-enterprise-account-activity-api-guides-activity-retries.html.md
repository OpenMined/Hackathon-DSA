
Activity retries | Docs | Twitter Developer Platform 

Activity retries

Retries
-------

Enterprise

One of the benefits of the enterprise tier of the Account Activity API is a retry mechanism for webhook events. If a 'success' 200 HTTP response code is not received, the Twitter server will initiate a retry mechanism, resending the webhook event up to three times over a five-minute period. This webhook event retry service helps provide reliability and event recovery when network problems occur and during client-side service interruptions and deploys.  

### What are retries?

The Account Activity API provides a retry feature when the client's web app does not return a 'success' 200 response for an account activity webhook event. When the client-side does not confirm the successful receipt of an event, Twitter assumes the event was not received. If a non-200 response is received, a response isn't received within three seconds, or we don't receive a response at all, we retry the request and leave that open for three seconds. This means that you have roughly five seconds over two attempts to respond to receive the activity that we are trying to send to your webhook URL. In the event that your server doesn't response or returns a transient error, we will retry for five minutes. There will be a total of three retry attempts to confirm validation. This allows redundancy and insurance that you receive all webhook events. Note that subscriptions with retries will get retried events for any/all activities for all subscribed users on their webhook.

If you do not confirm validation within these eight attempts, the activity will no longer be available via the Account Activity API.   

### Retry timeline

The Account Activity API will retry up to three times over a five-minute period until a 200 response is received.  Refer to the table below for more details. After around five minutes, the activity cannot be resent through the Account Activity API. You will need to use other Twitter endpoints to collect missed data. For example, the search APIs can be used to retrieve relevant Tweets, Retweets, Quote Tweets, Mentions, and Replies. Missed Direct Messages can be retrieved with this endpoint.

#### Retries timeline

|  |
| --- |
| Activity created, POST to the webhook URL from Account Activity API and times out in three seconds.  |
| Wait three seconds after previous timeout finishes, then POST to the webhook URL from Account Activity API and times out in three seconds. |
| Wait 27 seconds after previous timeout finishes, then POST to the webhook URL from Account Activity API and times out in three seconds. |
| Wait 242 seconds after previous timeout finishes, then POST to the webhook URL from Account Activity API and times out in three seconds |
| The Account Activity API will stop attempting to POST after this. Client must use other Twitter endpoints to recover data. |

Next steps
----------

* Learn more about:
	+ Securing your webhook.
	+ Managing your webhooks and adding subscriptions.
	+ Authenticating users.
	+ Webhook JSON payload examples.
* See Account Activity API references.
* See example code:
	+ The SnowBot chatbot, a Ruby web app built with the Account Activity and Direct Message APIs.

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