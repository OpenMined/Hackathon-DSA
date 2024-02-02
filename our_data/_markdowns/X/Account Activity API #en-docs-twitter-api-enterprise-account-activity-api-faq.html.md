
FAQ | Docs | Twitter Developer Platform 

FAQ

Frequently Asked Questions
--------------------------

### General

**What are the advantages of using the Account Activity API?**  

The Account Activity API uses webhooks, meaning that unlike for the streaming APIs we don't require you to have an open connection for us to send you information. Webhooks are also different from Rest APIs because you don't have to pull us hundreds of times every 15 minutes to get the data you care about. This increases the efficiency between a user and your app, as it delivers data when it happens.

The Account Activity API has a number of benefits:

1. **Speed**: we deliver data at the speed of Twitter.
2. **Simplicity**: we deliver all of an account's events, through one single webhook connection. The activities delivered in the API include Tweets, @mentions, replies, Retweets, Quote Tweets, Retweets of Quote Tweets, favorites, Direct Messages sent, Direct Messages received, follows, blocks, mutes.
3. **Scale**: you receive all of the activities for an account that you manage without being restricted by any rate limits of event caps.

The Account Activity API is available as a premium sandbox, premium paid, and enterprise offering, so you can scale as you require more accounts for liability features or additional functionality.

To get started, visit the playbook or download sample code snippets from GitHub.  

**How do I identify which product tier is best for me?**

Please read through our Account Activity API Overview page to learn more about the differences between the Premium options and the Enterprise option.   

**What is the difference between a Premium environment and an Enterprise webhook?**

There is no difference. Each Premium environment will have its own webhook\_id.  

**I need a development, staging and production environment for Account Activity API, is this possible?**

Yes! With the paid tiers of Account Activity API (Paid Premium and Enterprise), it's possible to register multiple webhook URLs and manage subscriptions separately for each through the API methods. Additionally, multiple client apps may be added to an allowlist to maintain authorization for your current authorized users.  

**Do you have any step-by-step guides on how to get set up with the Account Activity API?**

As a matter of fact, we do!

* If you are just getting started, we recommend that you visit our Getting started with webhooks guide
* Follow along with our Twitter Dev supported scripts:
	+ Account Activity API dashboard, a node web app that displays webhook events.
	+ The SnowBot chatbot, a Ruby web app built on the Account Activity and Direct Message APIs. This code base includes a script to help set up Account Activity API webhooks.

**Is there a way to recover data if our system goes down for a period of time?**

With the paid tiers of Account Activity API (Paid Premium and Enterprise), our system will retry to send the activities to you several times over a four hour period. If your system does not respond within that four hour period, then the activity will be lost and you will have to use other REST endpoints to recover data within 7 days.

We suggest that you use your different webhooks, or environments, as a redundancy tool like the Account Activity Replay API to ensure that you don't miss any activities if one of your systems goes down.  

**What authentication do I have to use with the Account Activity API?**

The authorization methods required for Account Activity API is described per method in the API reference pages. If you are just starting out with Twitter authentication, we recommend that you read through this section.  

**What is a challenge-response check (CRC)?**

The Account Activity API challenge response check is a security feature put in place to ensure that the Account Activity API’s activities are being sent to the proper developer. It also can be used by developers to ensure that the data that they are receiving is coming from Twitter. Twitter will automatically send a CRC to your webhook URL once every 24 hours, starting the last time the webhook URL was validated. Your system must respond with a valid response within 3 seconds to remain validated. 

Please visit our page Securing webhooks for more details.  

**Is there anything that would immediately invalidate my webhook URL?**

If one of the following occurs, we will immediately mark your webhook as invalid:

* The server responds to a CRC with an incorrect token. In this case, our system will not retry to send you the activity.
* The webhook URL has an incorrect certificate configured. In this case, our system will not retry to send you the activity.
* Your server returning a non-2XX, non-4XXX, non-5XXX response code.
* You specify the use of gzip without actually sending it.
* You do not specify the use of gzip, but actually send it in the response.

**Will I get duplicate activities if subscribed to users that are interacting with each other?**

Yes.  If your web app has active subscriptions for User A and User B, and User A mentions User B in a Tweet, there will be two POST activities sent to the registered webhook.  Each activity will have an indicator of "for\_user\_id" to show which subscription the activity belongs to.  

**When I make a subscription to my webhook, can I replace the `/all/` portion of the following endpoint with other account activity data objects to limit the activities the API delivers?**`POST https://api.twitter.com/1.1/account_activity/all/:env_name/subscriptions.json`

No, this is not possible. As it currently stands, we only have the `/all/` product available.  

**Is there any way of using the Account Activity API without requesting Direct Messages permissions from users?**

At this point, Direct Messages permissions are required because there is no way to 'filter out' the Direct Messages activities for this API.   

**Is there a free version of the Account Activity API?**

Yes, we offer the sandbox version as a free tier. Our sandbox option is limited to a single webhook with a limit of a maximum of 15 subscriptions. You can read more about the sandbox option in our documentation.   

**Is it possible to use the Account Activity API to get Retweets of Tweets that mention subscribed users?**

Unfortunately, this is not part of the activities delivered with this API. For this, we suggest using the Streaming API instead.   

**What are the possible activity types that are represented by a tweet\_create\_event?**

A tweet\_create\_event payload will be sent:

If the subscription user does any of the following actions:

* Creates a Tweet
* Retweets
* Replies to a Tweet

If another user:

* @mentions\* the subscription user
* Quotes a Tweet created by the subscription user

\*Note: The Account Activity API only delivers events when the subscription user would receive a notification from Twitter and could see the event publicly.  This means, If the mentioned account (@userA) follows the protected account (@userB) then UserA will get a notification UserB mentioned them. If UserA is not following UserB (and approved by UserB) UserA will not get a notification, and therefore a tweet\_create\_event would not be sent via AAA if @userA had a subscription.

**If a blocked user mentions my subscribed user, how can I identify this?**

You will see a boolean field `user\_has\_blocked` on the top level of the json response, set to either “true” or “false". This field will only be exposed on Tweet mentions. 

Enterprise

**How can I add my app to an allowlist or check if my app is already on the allowlist?**

To manage the Twitter apps that you have added to an allowlist for access via the Enterprise APIs, please reach out to your account manager with your app ID. You can find your app ID by navigating to the "Apps" page in the developer portal.  

**If I have access to three webhooks, can I use three webhooks for each of the apps that I have registered for enterprise use?**

The webhook limit is set on the account level, not the app level. If you have access to three webhooks and two apps registered for enterprise use, you can use two webhooks on one app and the third on the other app, but not three on each app.   

**Can I specify which types of events will be redelivered using the Account Activity Replay API?**

The types of events to replay cannot be specified. All events delivered during the date and time window specified will be replayed.   

**Will there be any retries if my application fails to ingest an Account Activity Replay API event?**

No, there will not be any retries. If an application fails to ingest an event sent by the Account Activity Replay API, another Replay job can be submitted for the same time period to attempt redelivery of any missed Replay events.   

**What should I do when I receive a partial success completion event?**

We suggest making note of the timestamps for the events that were received and requesting another Replay job for the events that were missed.   

**How many Account Activity Replay API jobs can I have running at a time?**

Only one Account Activity Replay API job per webhook may be running at a time.   

**How can I differentiate Account Activity Replay API events from real-time production events as they are delivered to my webhook?**

Since the Account Activity Replay API will always deliver events from the past, events can be differentiated from real-time production events based on the event’s timestamp.   

**How soon can I start using the Account Activity Replay API to redeliver an activity my application dropped or missed?**

An activity becomes available for redelivery about 10 minutes after it was created. 

### Error troubleshooting guide

#### Code 32

This error generally means that something is either malformed in the request, headers, authorization, or url that you are specifying. This is not an Account Activity API error, it’s an authorization error and Twitter isn’t getting the proper Oauth setup or url.

* **Enterprise** - Make sure the consumer keys and access tokens you are using belong to a Twitter app that has been registered for use of Enterprise products. If you don't have your consumer keys and access tokens, or need to add your Twitter app to the allowlist, please reach out to your account manager.
* If authenticating with user context, make sure you have properly authorized your request with the proper `oauth nonce`, `oauth_signature`, and `oauth_timestamp`.
* Make sure that your access tokens have the proper permission level.
	+ When on the 'Keys and tokens' tab in the app dashboard, please make sure that your access tokens have the 'Read, write, and direct messages' permission level.
	+ If the tokens' permission level is set to anything less than this, please navigate to the 'Permissions' tab, adjust the access permission to 'Read, write, and direct messages', then regenerate your access tokens and secret from the 'Keys and tokens' tab.

* Make sure that your URL is formed properly.
	+ Please keep in mind that `:env_name` is case sensitive.

#### Code 200 - Forbidden

* **Premium** - Make sure that you have an approved developer account before you try to make a request to the API. You also must use the proper :env\_name in the request, which you can setup on the dev environments page.
* **Enterprise** - Make sure that your account manager has set you up with access to the Account Activity API.
* Make sure you have set up your URI properly. This error can trigger if you have entered the incorrect URI in your request.

#### Code 214 - Webhook URL does not meet the requirements.

* Please make sure that you are using https.
* Your webhook URL could be malformed.
* Learn more about how to set up your webhook URL under the Develop webhook consumer app section on Getting started with webhooks page.

#### Code 214 - High latency on CRC GET request. Your webhook should respond in less than 3 seconds.

* This means that your server is slow. Make sure that you are responding to the CRC within 3 seconds.

#### Code 214 - Non-200 response code during CRC GET request (i.e. 404, 500, etc).

* Your server is down. Make sure that your server is running properly.

#### Code 214 - Too many resources already created.

* **Enterprise** - You have already used all of your webhooks. Use the GET webhooks endpoint with each of your registered apps to identify where your webhooks are distributed.

#### Code 261 - Application cannot perform write actions.

* The app that you are using with the API does not have the proper permission level set for its access token and access token secret. Please navigate to the 'Keys and tokens' tab on the Twitter apps dashboard and check the permission levels assigned to your access token and access token secret. If it is set to anything other than 'Read, write and Direct Messages,' then you are going to have to adjust the settings under the 'Permission' tab and regenerate your access token and access token secret to apply the new settings.
* Alternatively, you are trying to register a webhook using app-only authentication, which is not supported. Please authenticate with user context instead as noted in the API reference sections for registering a webhook for Enterprise Account Activity API.

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