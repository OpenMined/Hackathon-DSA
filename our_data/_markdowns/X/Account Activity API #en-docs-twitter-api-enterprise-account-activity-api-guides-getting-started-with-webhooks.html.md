
Getting started with webhooks | Docs | Twitter Developer Platform 

Getting started with webhooks

**Enterprise**

Getting started with webhooks
-----------------------------

The Account Activity API is a webhook-based API that sends account events to a web app you develop, deploy and host. 

There are several 'plumbing' details that need attention before you can start receiving webhook events in your event consumer application. As described below, you will need to create a Twitter app, obtain Account Activity API access, and develop a web app that consumes webhook events. 

### 1. Create a Twitter app.

* Create a Twitter app with an approved developer account from the developer portal. If you are creating the app on behalf of your company, it is recommended you create the app with a corporate Twitter account. To apply for a developer account, click here.
* Enable “Read, Write and Access direct messages” on the permissions tab of your app page.
* On the "Keys and Access Tokens" tab, take note of your app's Consumer Key (API Key) and Consumer Token (API Secret).
* On the same tab, generate your app's Access Token and Access Token Secret. You will need these Access Tokens to register your webhook URL, which is where Twitter will send account events.
* If you are unfamiliar with Twitter Sign-in and how user contexts work with the Twitter API review Obtaining Access Tokens. As you add accounts for which to receive events, you will subscribe them using that account's access tokens.
* Take note of your app's numeric ID, as seen in the "Apps" page of the developer portal. When you apply for Account Activity API access, you'll need this app ID.

### 2. Get Account Activity API access

After creating a Twitter app, the next step is applying for Account Activity API access. 

Those needing enterprise level access to more than 250 account subscriptions and 3+ webhooks will need to submit an application at the following link. If you can satisfy your use case with less access than this, you may want to check out Account Activity API premium. 

Apply for Enterprise access

### 3. Develop webhook consumer app

Once you have received Account Activity API access, you need to develop, deploy and host a web app that will receive Twitter webhook events. 

* Create a web app with a URL to use as your webhook to receive events. This is the endpoint deployed on your server to listen for incoming Twitter webhook events.
	+ The URI *path* is completely up to you. This example would be valid: https://mydomain.com*/service/listen*
	+ If you are listening for webhooks from a variety of sources, a common pattern is: https://mydomain.com/webhook/twitter
	+ Note that the specified URL can not include a port specification (https://mydomain.com:5000/NoWorkie).
* As described in our Securing Webhooks guide, a first step is writing code that receives a Twitter Challenge Response Check (CRC) GET request and responds with a properly formatted JSON response.
* Register your webhook URL. You will make a POST request to a /webhooks.json?url= endpoint. When you make this request Twitter will issue a CRC request to your web app. When a webhook is successfully registered, the response will include a webhook id. This webhook id is needed later when making some requests to the Account Activity API.
* Twitter will send account webhook events to the URL you registered. Make sure your web app supports POST requests for incoming events. These events will be encoded in JSON. See HERE for example webhook JSON payloads.
* Once your web app is ready, the next step is adding accounts to receive activities for. When adding (or deleting) accounts you will make POST requests referencing the account id. See our guide on adding subscriptions for more information.

### 4. Validate setup

* To validate your app and webhook are configured correctly, favorite a Tweet posted by one of the Twitter accounts your app is subscribed to. You should receive a `favorite_events` via a POST request to your webhook URL for each Favorite your subscribers receive.
* Note that it may take up to 10 seconds for events to start being delivered after a subscription has been added.

Important Notes
---------------

* When registering your webhook URL, your web app must authenticate with its consumer token and secret *and the app owner's user access token and secret*.
* All incoming Direct Messages will be delivered via webhooks. All Direct Messages sent via POST direct\_messages/events/new (message\_create) will also be delivered via webhooks. This is so your web app can be aware of Direct Messages sent via a different client.
* Note that every webhook event includes a for\_user\_id user ID that indicates which subscription the event was delivered for.
* If you have two users using your web app for Direct Messages in the same conversation, your webhook will receive two duplicate events (one for each user). Your web app should account for this.
* If you have more than one web app sharing the same webhook URL and the same user mapped to each app, the same event will be sent to your webhook multiple times (once per web app).
* In some cases, your webhook may receive duplicate events. Your webhook app should be tolerant of this and dedupe by event ID.
* Do not expect Quick Reply response to directly follow a request. A user has the ability to ignore a Quick Reply request and may respond via traditional Direct Message. The user may also provide a Quick Reply response to a request they have not replied to earlier in the message thread.

Next steps
----------

* Once you've registered your webhook URL, the next step is to Secure your webhook.
* Learn more about the following topics:   
	+ Managing your webhooks and adding subscriptions.
	+ Authenticating users.
	+ Webhook event retries.
	+ Webhook JSON payload examples.
* Have questions? Running into errors?
	+ Read our Frequently asked questions or Error Troubleshooting guide.
* See example code:
	+ Enterprise Account Activity API dashboard, a node web app that displays webhook events using the enterprise tier of the Account Activity API and includes Replay functionality.
	+ The SnowBot chatbot, a Ruby web app built on the Account Activity and Direct Message APIs. This code base includes a script to help set up Account Activity API webhooks.

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