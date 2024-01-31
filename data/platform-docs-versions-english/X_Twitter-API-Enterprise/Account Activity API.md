Overview

This endpoint has been updated to include Tweet edit metadata. Learn more about these metadata on the ["Edit Tweets" fundamentals page](https://developer.twitter.com/en/docs/twitter-api/enterprise/edit-tweets). 

This endpoint is often used with the Direct Messages endpoints. We have launched new [v2 Direct Messages endpoints](https://developer.twitter.com/en/docs/twitter-api/direct-messages/manage/introduction). Note that the Enterprise and Premium Account Activity APIs support v2 one-to-one messages, but do not yet support group conversations.     

Overview  

-----------

Enterprise

The Account Activity API provides you the ability to subscribe to realtime activities related to a user account via webhooks. This means that you can receive realtime Tweets, Direct Messages, and other account events from one or more of your owned or subscribed accounts through a single connection.

You will receive all related activities below for each user subscription on your webhook registration:

| Activity types |     |
| --- | --- |
| * Tweets (by user)  <br>    <br>* Tweet deletes (by user)<br>* @mentions (of user)<br>* Replies (to or from user)<br>* Retweets (by user or of user)<br>* Quote Tweets (by user or of user)<br>* Retweets of Quoted Tweets (by user or of user)<br>* Likes (by user or of user)<br>* Follows (by user or of user)  <br>    <br>* Unfollows (by user) | * Blocks (by user)<br>* Unblocks (by user)<br>* Mutes (by user)<br>* Unmutes (by user)<br>* Direct Messages sent (by user)<br>* Direct Messages received (by user)<br>* Typing indicators (to user)<br>* Read receipts (to user)<br>* Subscription revokes (by user) |

**Please note** - We do not deliver home timeline data via the Account Activity API. Please use the [GET statuses/home\_timeline](https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-home_timeline) to pull this data.  
 

#### Video Series

Check out our [four-part video series](https://www.youtube.com/watch?v=otPxejFhyy8&index=0&list=PLFKjcMIU2WshGG6Yj940XM7Z6BFs1zfBg) on the Account Activity API to get up to speed!

> Today we announced the Account Activity API is generally available as a premium and enterprise API. 🔔 [pic.twitter.com/xnlF9kPevi](https://t.co/xnlF9kPevi)
> 
> — Twitter Dev (@TwitterDev) [May 16, 2018](https://twitter.com/TwitterDev/status/996790447048613888?ref_src=twsrc%5Etfw)

### Feature summary

| Tier | Pricing | Number of unique subscriptions | Number of webhooks | Reliability and Activity Recovery |
| --- | --- | --- | --- | --- |
| Enterprise | [Contact sales](https://developer.twitter.com/content/developer-twitter/en/enterprise-application) | Up to 500+ | 3+  | [Retries](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/activity-retries) and [Replay](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/activity-replay-api) |

Next steps
----------

* [Apply for access and get started with webhooks.](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/getting-started-with-webhooks)
* Check out our [API references](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/api-reference) to find the right endpoint for the job.
* Follow this step-by-step [tutorial on how to get started with the Account Activity API](https://developer.twitter.com/content/developer-twitter/en/docs/tutorials/getting-started-with-the-account-activity-api).
* Follow this [step-by-step tutorial on how to build a customer engagement application](https://developer.twitter.com/content/developer-twitter/en/docs/tutorials/customer-engagement-application-playbook) on Twitter.  
      
    
* Have questions? Running into errors?
    * Read our [Frequently asked questions](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/faq) or [Error Troubleshooting guide](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/faq#troubleshooting).  
          
        
* Explore our sample code:  
    * [Enterprise Account Activity API dashboard](https://github.com/twitterdev/account-activity-dashboard-enterprise), a node web app that displays webhook events using the enterprise tier of the Account Activity API and includes [Replay](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/activity-replay-api) functionality.
    * The [SnowBot chatbot](https://github.com/twitterdev/SnowBotDev), a Ruby web app built on the enterprise Account Activity and Direct Message APIs.

Managing Enterprise Account Activity API

Manage webhooks and subscribed users
------------------------------------

**⏱ 10 min read**

The enterprise Account Activity API provides you webhook-based JSON messages any time there are events associated with Twitter accounts subscribed to your service. Twitter delivers those activities to your registered webhook. In the following steps, you will learn how to manage webhooks and subscribed users.

You will learn how to register, view, and remove, both webhooks and subscribed users. We'll be using simple cURL commands to make requests to the various API endpoints. cURL is a command-line tool for getting or sending requests using the URL syntax.

You will need:

* A registered Twitter app - _[register here](https://developer.twitter.com/content/developer-twitter/en/apps)_
* A bearer token - _[learn more](https://developer.twitter.com/content/developer-twitter/en/docs/basics/authentication/guides/bearer-tokens)_
* A webhook that passes a Challenge-Response Check (CRC) - _[learn more](https://developer.twitter.com/en/docs/accounts-and-users/subscribe-account-activity/guides/securing-webhooks)_
* An enterprise account - _[apply here](https://developer.twitter.com/en/enterprise)_

_Before you get started, we recommend you check out our [Github repo here](https://github.com/twitterdev/account-activity-dashboard) that provides a sample web app and helper scripts to get started with Twitter's Account Activity API_

### Managing a webhook:

  
Using a webhook provides you the ability to subscribe to realtime activities related to a user account through a single connection. 

* [Adding a webhook](#tab1)
* [Viewing a webhook](#tab2)
* [Removing a webhook](#tab3)
* [](#tab4)

Adding a webhook

Viewing a webhook

Removing a webhook

Let’s begin with registering a new webhook URL for the given application context.

The URL will be validated via a CRC request before saving. Once you've registered a webhook, make sure to document the webhook ID as you will need it later on.

Copy the following cURL request into your command line after making changes to the following:

* **URL** `<URL>` e.g. `https://yourdomain.com/webhooks/twitter/`  
    
* **Consumer key** `<CONSUMER_KEY>` e.g. `xvz1evFS4wEEPTGEFPHBog`  
    
* **Access token** `<ACCESS_TOKEN>` e.g.  `370773112-GmHxMAgYyLbNEtIKZeRNFsMKPR9EyMZeS9weJAEb`

      `curl --request POST --url 'https://api.twitter.com/1.1/account_activity/webhooks.json?url=<URL>' --header 'authorization: OAuth oauth_consumer_key="<CONSUMER_KEY>", oauth_nonce="GENERATED", oauth_signature="GENERATED", oauth_signature_method="HMAC-SHA1", oauth_timestamp="GENERATED", oauth_token="<ACCESS_TOKEN>", oauth_version="1.0"'`
    

We will run the following command to returns all registered webhook URLs and their statuses for the given application.

Copy the following cURL request into your command line after making changes to the following:

* **Bearer token** `<BEARER_TOKEN>` e.g. `AAAAAAAAAAAA0%2EUifi76ZC9Ub0wn...`

      `curl --request GET --url https://api.twitter.com/1.1/account_activity/webhooks.json --header 'authorization: Bearer <BEARER_TOKEN>'`
    

To remove a webhook from the provided application's configuration, copy the following cURL request into your command line after making changes to the following:

* **Webhook ID** `<:WEBHOOK_ID>` e.g. `1234567890`  
    
* **Consumer key** `<CONSUMER_KEY>` e.g. `xvz1evFS4wEEPTGEFPHBog`  
    
* **Access token** `<ACCESS_TOKEN>` e.g.  `370773112-GmHxMAgYyLbNEtIKZeRNFsMKPR9EyMZeS9weJAEb`

      `curl --request DELETE --url https://api.twitter.com/1.1/account_activity/webhooks/<:WEBHOOK_ID>.json --header 'authorization: OAuth oauth_consumer_key="<CONSUMER_KEY>", oauth_nonce="GENERATED", oauth_signature="GENERATED", oauth_signature_method="HMAC-SHA1", oauth_timestamp="GENERATED", oauth_token="<ACCESS_TOKEN>", oauth_version="1.0"'`
    

### Managing subscribed users:

  
Once you've registered a Webhook, you can add a subscribed user to the Account Activity API to begin receiving their account activities.

* [Adding a subscription](#tab1)
* [Viewing subscriptions](#tab2)
* [Removing a subscription](#tab3)
* [](#tab4)

Adding a subscription

Viewing subscriptions

Removing a subscription

We'll begin with subscribing a user so you recieve all event types.

Copy the following cURL request into your command line after making changes to the following:

* **Webhook ID** `<:WEBHOOK_ID>` e.g. `1234567890`  
    
* **Consumer key name** `<CONSUMER_KEY>` e.g. `xvz1evFS4wEEPTGEFPHBog`  
    
* **Subscribing user's access token** `<SUBSCRIBING_USER'S_ACCESS_TOKEN>` e.g. `370773112-GmHxMAgYyLbNEtIKZeRNFsMKPR9EyMZeS9weJAEb`  
    

      `curl --request POST --url https://api.twitter.com/1.1/account_activity/webhooks/<:WEBHOOK_ID>/subscriptions/all.json --header 'authorization: OAuth oauth_consumer_key="<CONSUMER_KEY>", oauth_nonce="GENERATED", oauth_signature="GENERATED", oauth_signature_method="HMAC-SHA1", oauth_timestamp="GENERATED", oauth_token="<SUBSCRIBING_USER'S_ACCESS_TOKEN>", oauth_version="1.0"'`
    

To view a list of all activity type subscriptions for a specified webhook, copy the following cURL request into your command line after making changes to the following:

* **Webhook ID** `<:WEBHOOK_ID>` e.g. `1234567890`  
    
* **Bearer token** `<BEARER_TOKEN>` e.g. `AAAAAAAAAAAA0%2EUifi76ZC9Ub0wn...`  
    

      `curl --request GET --url https://api.twitter.com/1.1/account_activity/webhooks/<:WEBHOOK_ID>/subscriptions/all/list.json --header 'authorization: Bearer <BEARER_TOKEN>'`
    

After deactivation, all events for the requesting user will no longer be sent to the webhook URL.  

To deactivate a subscription from the provided user context and application, copy the following cURL request into your command line after making changes to the following:

* **Webhook ID** `<:WEBHOOK_ID>` e.g. `1234567890`  
    
* **Consumer key** `<CONSUMER_KEY>` e.g. `xvz1evFS4wEEPTGEFPHBog`  
    
* **Subscribing user's access token** `<SUBSCRIBING_USER'S_ACCESS_TOKEN>` e.g. `370773112-GmHxMAgYyLbNEtIKZeRNFsMKPR9EyMZeS9weJAEb`  
    

      `curl --request DELETE --url https://api.twitter.com/1.1/account_activity/webhooks/:WEBHOOK_ID/subscriptions/all.json --header 'authorization: OAuth oauth_consumer_key="CONSUMER_KEY", oauth_nonce="GENERATED", oauth_signature="GENERATED", oauth_signature_method="HMAC-SHA1", oauth_timestamp="GENERATED", oauth_token="SUBSCRIBED_USER'S_ACCESS_TOKEN", oauth_version="1.0"'`
    

Great job! You should now able to manage your webhooks and subscribed users.

### Referenced articles

* [Overview of Challenge-Response Check (CRC)](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/guides/securing-webhooks) 
* [Account Activity Data Types](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/account-activity-data-objects)
* [Managing Webhooks and Subscriptions](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/managing-webhooks-and-subscriptions)

Next Steps
----------

* [Discover more about the Account Activity API](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/overview)
* [Join the conversation on Twitter community forums](https://twittercommunity.com/)
* Explore our sample code:  
    * [Enterprise Account Activity API dashboard](https://github.com/twitterdev/account-activity-dashboard-enterprise), a node web app that displays webhook events using the enterprise tier of the Account Activity API and includes [Replay](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/activity-replay-api) functionality.

A video walkthrough of the Account Activity API

A video walkthrough of the Account Activity API
-----------------------------------------------

In this video walkthrough, you will learn about the capabilities of the premium and enterprise tiers of the Account Activity API.

By the end of this video, you will learn about the following capabilities.

* Registering a webhook
* Adding a user subscription
* Removing a user subscription
* Receiving account activities
* Replay account activities

> Tired of reading? We’ve got you covered. Learn about the capabilities of the Account Activity API in this video walkthrough with [@tonyv00](https://twitter.com/tonyv00?ref_src=twsrc%5Etfw) from our DevRel team. 🍿 ⬇️ [pic.twitter.com/LdHy4aLu0i](https://t.co/LdHy4aLu0i)
> 
> — Twitter Dev (@TwitterDev) [December 9, 2019](https://twitter.com/TwitterDev/status/1204084171334832128?ref_src=twsrc%5Etfw)

Next steps  

-------------

* [Apply for access and get started with webhooks.](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/getting-started-with-webhooks)
* Check out our [API references](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/api-reference) to find the right endpoint for the job.
* Follow this step-by-step [tutorial on how to get started with the Account Activity API](https://developer.twitter.com/content/developer-twitter/en/docs/tutorials/getting-started-with-the-account-activity-api).
* Follow this [step-by-step tutorial on how to build a customer engagement application](https://developer.twitter.com/content/developer-twitter/en/docs/tutorials/customer-engagement-application-playbook) on Twitter.  
      
    
* Have questions? Running into errors?
    * Read our [Frequently asked questions](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/faq) or [Error Troubleshooting guide](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/faq#troubleshooting).  
          
        
* Explore our sample code:  
    * [Enterprise Account Activity API dashboard](https://github.com/twitterdev/account-activity-dashboard-enterprise), a node web app that displays webhook events using the enterprise tier of the Account Activity API and includes [Replay](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/activity-replay-api) functionality.
    * The [SnowBot chatbot](https://github.com/twitterdev/SnowBotDev), a Ruby web app built on the enterprise Account Activity and Direct Message APIs.

Getting started with webhooks

**Enterprise**

Getting started with webhooks
-----------------------------

The Account Activity API is a webhook-based API that sends account events to a web app you develop, deploy and host. 

There are several 'plumbing' details that need attention before you can start receiving webhook events in your event consumer application. As described below, you will need to create a Twitter app, obtain Account Activity API access, and develop a web app that consumes webhook events. 

### 1\. Create a Twitter app.

* Create a [Twitter app](https://developer.twitter.com/content/developer-twitter/en/docs/apps) with an approved developer account from the [developer portal](https://developer.twitter.com/content/developer-twitter/en/docs/developer-portal/overview). If you are creating the app on behalf of your company, it is recommended you create the app with a corporate Twitter account. To apply for a developer account, [click here](https://developer.twitter.com/content/developer-twitter/en/apply).
* Enable “Read, Write and Access direct messages” on the [permissions](https://developer.twitter.com/content/developer-twitter/en/docs/authentication/overview/application-permission-model) tab of your app page.
* On the "Keys and Access Tokens" tab, take note of your app's Consumer Key (API Key) and Consumer Token (API Secret).
* On the same tab, generate your app's [Access Token and Access Token Secret](https://developer.twitter.com/content/developer-twitter/en/docs/authentication/guides/access-tokens). You will need these Access Tokens to register your webhook URL, which is where Twitter will send account events.
* If you are unfamiliar with [Twitter Sign-in](https://developer.twitter.com/content/developer-twitter/en/docs/basics/authentication/overview/sign-in-with-twitter) and how user contexts work with the Twitter API review [Obtaining Access Tokens](https://dev.twitter.com/webhooks/access-tokens). As you add accounts for which to receive events, you will subscribe them using that account's access tokens.
* Take note of your app's numeric ID, as seen in the ["Apps"](https://developer.twitter.com/content/developer-twitter/en/docs/apps) page of the [developer portal](https://developer.twitter.com/content/developer-twitter/en/docs/developer-portal/overview). When you apply for Account Activity API access, you'll need this app ID.  
     

### 2\. Get Account Activity API access

After creating a Twitter app, the next step is applying for Account Activity API access. 

Those needing enterprise level access to more than 250 account subscriptions and 3+ webhooks will need to submit an application at the following link. If you can satisfy your use case with less access than this, you may want to check out [Account Activity API premium](https://developer.twitter.com/en/docs/twitter-api/premium/account-activity-api/overview). 

[Apply for Enterprise access](https://developer.twitter.com/en/enterprise-application.html)

### 3\. Develop webhook consumer app

Once you have received Account Activity API access, you need to develop, deploy and host a web app that will receive Twitter webhook events. 

* Create a web app with a URL to use as your webhook to receive events. This is the endpoint deployed on your server to listen for incoming Twitter webhook events. 
    * The URI _path_ is completely up to you. This example would be valid: https://mydomain.com_/service/listen_  
        
    * If you are listening for webhooks from a variety of sources, a common pattern is: https://mydomain.com/webhook/twitter
    * Note that the specified URL can not include a port specification (https://mydomain.com:5000/NoWorkie).
* As described in our [Securing Webhooks](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/securing-webhooks) guide, a first step is writing code that receives a Twitter Challenge Response Check (CRC) GET request and responds with a properly formatted JSON response. 
* Register your webhook URL. You will make a POST request to a /webhooks.json?url= endpoint. When you make this request Twitter will issue a CRC request to your web app. When a webhook is successfully registered, the response will include a webhook id. This webhook id is needed later when making some requests to the Account Activity API.   
    
* Twitter will send account webhook events to the URL you registered. Make sure your web app supports POST requests for incoming events. These events will be encoded in JSON. See [HERE](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/guides/account-activity-data-objects) for example webhook JSON payloads.
* Once your web app is ready, the next step is adding accounts to receive activities for. When adding (or deleting) accounts you will make POST requests referencing the account id. See our [guide on adding subscriptions](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/guides/managing-webhooks-and-subscriptions) for more information.  
      
    

### 4\. Validate setup

* To validate your app and webhook are configured correctly, favorite a Tweet posted by one of the Twitter accounts your app is subscribed to. You should receive a `favorite_events` via a POST request to your webhook URL for each Favorite your subscribers receive.
* Note that it may take up to 10 seconds for events to start being delivered after a subscription has been added.

Important Notes
---------------

* When registering your webhook URL, your web app must authenticate with its consumer token and secret _and the app owner's user access token and secret_. 
* All incoming Direct Messages will be delivered via webhooks. All Direct Messages sent via [POST direct\_messages/events/new (message\_create)](https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/api-reference/new-event) will also be delivered via webhooks. This is so your web app can be aware of Direct Messages sent via a different client.
* Note that every webhook event includes a for\_user\_id user ID that indicates which subscription the event was delivered for.
* If you have two users using your web app for Direct Messages in the same conversation, your webhook will receive two duplicate events (one for each user). Your web app should account for this.   
    
* If you have more than one web app sharing the same webhook URL and the same user mapped to each app, the same event will be sent to your webhook multiple times (once per web app).
* In some cases, your webhook may receive duplicate events. Your webhook app should be tolerant of this and dedupe by event ID.
* Do not expect Quick Reply response to directly follow a request. A user has the ability to ignore a Quick Reply request and may respond via traditional Direct Message. The user may also provide a Quick Reply response to a request they have not replied to earlier in the message thread.

Next steps
----------

* Once you've registered your webhook URL, the next step is to [Secure your webhook](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/guides/securing-webhooks).
* Learn more about the following topics:   
    * [Managing your webhooks and adding subscriptions](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/guides/managing-webhooks-and-subscriptions).
    * [Authenticating users](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/guides/authenticating-users).
    * [Webhook event retries](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/guides/activity-retries).
    * [Webhook JSON payload examples.](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/guides/account-activity-data-objects)  
* Have questions? Running into errors?
    * Read our [Frequently asked questions](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/faq) or [Error Troubleshooting guide](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/faq#troubleshooting).  
          
        
* See example code:
    * [Enterprise Account Activity API dashboard](https://github.com/twitterdev/account-activity-dashboard-enterprise), a node web app that displays webhook events using the enterprise tier of the Account Activity API and includes [Replay](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/activity-replay-api) functionality.  
        
    * The [SnowBot chatbot](https://github.com/twitterdev/SnowBotDev), a Ruby web app built on the Account Activity and Direct Message APIs. This code base includes a [script](https://github.com/twitterdev/SnowBotDev/wiki/Account-Activity-API-setup-script) to help set up Account Activity API webhooks.

Securing webhooks

Securing webhooks
-----------------

Twitter's webhook-based APIs provide two methods for confirming the security of your webhook server:

1. The challenge-response checks enable Twitter to confirm the ownership of the web app receiving webhook events. 
2. The signature header in each POST request enables you to confirm that Twitter is the source of the incoming webhooks.  
       
    

### Challenge-Response Checks 

In order to verify that you are both the owner of the app and the webhook URL, Twitter will perform a Challenge-Response Check (CRC), which is not to be confused with a cyclic redundancy check. When a CRC is sent, Twitter will make a GET request of your web app with a ;_`crc_token`_ parameter. When that request is received, your web app needs to build an encrypted `response_token` based on the _`crc_token`_ parameter and your app's Consumer Secret (details below). The response\_token must be encoded in JSON (see example below) and returned within three seconds. When successful, a webhook `id` will be returned. 

A CRC will be sent when you register your webhook URL, so implementing your CRC response code is a fundamental first step. Once your webhook is established, Twitter will trigger a CRC roughly every 24 hours from the last time we received a successful response. Your app can also trigger a CRC when needed by making a PUT request with your webhook `id`. Triggering a CRC is useful as you develop your webhook application, after deploying new code and restarting your service. 

The _`crc_token`_ should be expected to change for each incoming CRC request and should be used as the message in the calculation, where your Consumer Secret is the key.

In the event that the response is not posted within 3 seconds or becomes invalid, events will cease to be sent to the registered webhook.

#### The CRC request will occur:  

* When a webhook URL is registered.
* Approximately _hourly_ to validate your webhook URL.
* You can manually trigger a CRC by making a PUT request. As you develop your webhook client, you should plan on manually triggering the CRC as you develop your CRC response.   
     

#### Response requirements:

* A base64 encoded HMAC SHA-256 hash created from the `crc_token` and your app Consumer Secret
* Valid response\_token and JSON format.
* Latency less than 3 seconds.
* 200 HTTP response code.  
     

#### Language-specific HMAC libraries:

* [Java/Scala](https://docs.oracle.com/javase/8/docs/api/index.html?javax/crypto/Mac.html)
* [Ruby](http://ruby-doc.org/stdlib-2.1.0/libdoc/openssl/rdoc/OpenSSL/HMAC.html)
* [Node.js](https://nodejs.org/api/crypto.html#crypto_class_hmac)
* [Python](https://docs.python.org/2/library/hmac.html) 

#### Example response token generation in Python:

The following defines a route in a Python 2.7 Flask webapp that will respond to the challenge response check correctly.

import base64
import hashlib
import hmac
import json


# Defines a route for the GET request
@app.route('/webhooks/twitter', methods=\['GET'\])
def webhook\_challenge():

  # creates HMAC SHA-256 hash from incomming token and your consumer secret
  sha256\_hash\_digest = hmac.new(TWITTER\_CONSUMER\_SECRET, msg=request.args.get('crc\_token'), digestmod=hashlib.sha256).digest()

  # construct response data with base64 encoded hash
  response = {
    'response\_token': 'sha256=' + base64.b64encode(sha256\_hash\_digest)
  }

  # returns properly formatted json response
  return json.dumps(response)

#### Example JSON response:  

With the route defined as above your webapp should return a response similar to below when navigating to https://your-app-domain/webhooks/twitter?crc\_token=foo in your web browser.

{
  "response\_token": "sha256=x0mYd8hz2goCTfcNAaMqENy2BFgJJfJOb4PdvTffpwg="
}

#### Other examples:

* [HERE](https://github.com/twitterdev/account-activity-dashboard/blob/master/helpers/security.js) is an example CRC response method written in Node/JS.
* [HERE](https://github.com/twitterdev/SnowBotDev/blob/master/app/controllers/snow_bot_dev_app.rb) is an example CRC response method written in Ruby (see the _generate\_crc\_response_ and the /GET route that receives CRC events).  
      
    

### Optional signature header validation

When receiving a POST request from Twitter, sending a GET request to create a webhook, or sending a GET request to perform a manual CRC, a hash signature will be passed in the headers as x-twitter-webhooks-signature. This signature can be used to validate the source of the data is Twitter. The POST hash signature starts with sha256= indicating the use of HMAC SHA-256 to encrypt your Twitter App Consumer Secret and payload. The GET hash is calculated from the query parameter string crc\_token=$token&nonce=$nonce. 

**Steps to validate a request**

1. Create a hash using your consumer secret and incoming payload body.
2. Compare created hash with the base64 encoded x-twitter-webhooks-signature value. Use a method like [compare\_digest](https://docs.python.org/2/library/hmac.html) to reduce the vulnerability to timing attacks.  
      
    

### Additional security guidelines

The following are additional security guidelines to consider for your web application. Not having these guidelines implemented will not prevent your webhook from functioning, but are highly reccomended by the Twitter Information Security team. If you are unfamilair with the below recommendations consult with your server administrator.

#### Twitter aggregate network blocks  

For added security you may wish to add the following aggregate network blocks to an allowlist:

* 199.59.148.0/22
* 199.16.156.0/22
* 192.133.77.0/26
* 64.63.15.0/24  
    
* 64.63.31.0/24
* 64.63.47.0/24
* 202.160.128.0/24
* 202.160.129.0/24
* 202.160.130.0/24

#### Recommended server configurations

* "A" rating on [ssllabs.com](http://ssllabs.com/) test
* **Enable TLS 1.2**
* Enable Forward Secrecy
* Turn off SSLv2
* Turn off SSLv3 (because of POODLE)
* Turn off TLS 1.0
* Turn off TLS 1.1
* Turn off TLS Compression
* Turn off Session Tickets unless you rotate session ticket keys.
* Set the “ssl\_prefer\_server\_ciphers” or “SSLHonorCipherOrder” option in the SSL Configuration “on”.
* Ensure the list of ciphers is a modern list such as:  
    `ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:AES128-GCM-SHA256:AES128-SHA256:AES128-SHA:AES256-GCM-SHA384:AES256-SHA256:AES256-SHA:ECDHE-RSA-DES-CBC3-SHA:DES-CBC3-SHA`  
    

### Next steps

* Once you have secured your webhook app, the next step is [adding user subscriptions](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/guides/managing-webhooks-and-subscriptions).
* Learn more about these topics:
    * [Authenticating users](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/guides/authenticating-users).
    * [Webhook event retries](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/guides/activity-retries).
    * [Webhook JSON payload examples.](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/guides/account-activity-data-objects)
* See [Account Activity API references](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference).
* See example code:  
    * The [SnowBot chatbot](https://github.com/twitterdev/SnowBotDev), a Ruby web app built with the Account Activity and Direct Message APIs. This code base includes a [script](https://github.com/twitterdev/SnowBotDev/wiki/Account-Activity-API-setup-script) to help set up Account Activity API webhooks.

Managing webhooks and subscriptions

Managing webhooks and subscriptions
-----------------------------------

### Creating & changing webhooks

In order to change webhook URLs, you must delete your existing webhook and then create a new one. Note that when you do this, you will be required to re-add user subscriptions to the new webhook.

#### Webhook configuration management endpoints:  
  

|     |     |
| --- | --- |
| **Method** | Enterprise |
| Registers a webhook URL / Generates a webhook\_id | [POST webhooks](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#post-account-activity-webhooks) |
| Returns all webhook URLs and their statuses | [GET webhooks](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#get-account-activity-webhooks) |
| Delete app’s current webhook configuration | [DELETE webhooks/:webhook\_id](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#delete-account-activity-webhooks-webhook-id) |
| Manually trigger a CRC request | [PUT webhooks/:webhook\_id](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#put-account-activity-webhooks-webhook-id) |

#### Why can’t I just update the webhook URL?

Why are webhook configurations immutable? Twitter takes security very seriously. If your webhook URL is changed, there is a possibility that your application consumer key and consumer secret have been compromised. By requiring you to create a new webhook configuration, you are also required to re-subscribe to your user’s events. This requires the use of access tokens that a malicious party is less likely to possess. As a result, the likelihood that another party will receive your user’s private information is reduced.  
 

### Adding & removing User subscriptions

Support for thousands of subscriptions is available with the enterprise tier. If you already have an account manager, please reach out to them with questions.  To apply for access to the enterprise APIs, [click here](https://developer.twitter.com/content/developer-twitter/en/enterprise).   

#### Subscription management endpoints  
 

|     |     |
| --- | --- |
| Method | Enterprise |
| Add new user subscription | [POST webhooks/:webhook\_id/subscriptions/all](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#post-account-activity-webhooks-webhook-id-subscriptions-all) |
| Retrieve a user subscription | [GET webhooks/:webhook\_id/subscriptions/all](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#get-account-activity-webhooks-webhook-id-subscriptions-all) |
| Returns a list of all active subscriptions | [GET webhooks/:webhook\_id/subscriptions/all/list](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#get-account-activity-webhooks-webhook-id-subscriptions-all-list) |
| Deactivates a user subscription using application only OAuth | [DELETE webhooks/:webhook\_id/subscriptions/:user\_id/all.json](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#delete-account-activity-webhooks-webhook-id-subscriptions-user-id-all-json) |

### Next steps

* Learn more about these topics:
    * [Securing your webhook](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/guides/securing-webhooks).
    * [Authenticating users](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/guides/authenticating-users).
    * [Webhook event retries](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/guides/activity-retries).
    * [Webhook JSON payload examples.](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/guides/account-activity-data-objects)
* See [Account Activity API references](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference).
* See example code:
    * [Premium Account Activity API dashboard](https://github.com/twitterdev/account-activity-dashboard), a node web app that displays webhook events.
    * The [SnowBot chatbot](https://github.com/twitterdev/SnowBotDev), a Ruby web app built with the Account Activity and Direct Message APIs. This code base includes a [script](https://github.com/twitterdev/SnowBotDev/wiki/Account-Activity-API-setup-script) to help set up Account Activity API webhooks.  
        

####

Authenticating with the Account Activity API

**Please note**: 

Twitter needs to enable access to the Account Activity API for your developer App before you can start using the API. To this end, make sure to share the App ID that you intend to use for authentication purposes with your account manager or technical support team.

The [Account Activity API](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/overview) consists of a set of endpoints that allow you to create and manage user subscriptions to receive real-time account activities for all of your subscribed accounts through a single connection. 

There are two authentication methods available with the Account Activity API ([OAuth 1.0a](https://developer.twitter.com/en/docs/tutorials/authenticating-with-twitter-api-for-enterprise/authentication-method-overview#oauth1.0a) and [OAuth 2.0 Bearer Token](https://developer.twitter.com/en/docs/tutorials/authenticating-with-twitter-api-for-enterprise/authentication-method-overview#oauth2.0)). The authentication method that you should use will depend on which endpoint you are using.

|     |     |     |     |
| --- | --- | --- | --- |
| **Description** | **Endpoint** | OAuth 1.0a  <br>(user context) | OAuth 2.0 Bearer Token (application-only) |
| Register a new webhook URL for the given application context | [POST account\_activity/webhooks](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#post-account-activity-webhooks) | ✓   |     |
| Return all URLs and their statuses for the given application | [GET account\_activity/webhooks](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#get-account-activity-webhooks) |     | ✓   |
| Trigger a challenge response check (CRC) for a given webhook's URL | [PUT account\_activity/webhooks/:webhook\_id](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#put-account-activity-webhooks-webhook-id) | ✓   |     |
| Subscribe the application to a user’s account events | [POST account\_activity/webhooks/:webhook\_id/subscriptions/all](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#post-account-activity-webhooks-webhook-id-subscriptions-all) | ✓ \* |     |
| Return a count of currently active subscriptions | [GET account\_activity/subscriptions/count](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#get-account-activity-subscriptions-count) |     | ✓   |
| Check if a webhook configuration is subscribed to a user’s events | [GET account\_activity/webhooks/:webhook\_id/subscriptions/all](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#get-account-activity-webhooks-webhook-id-subscriptions-all) | ✓ \* |     |
| Return a list of currently active subscriptions | [GET account\_activity/webhooks/:webhook\_id/subscriptions/all/list](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#get-account-activity-webhooks-webhook-id-subscriptions-all-list) |     | ✓   |
| Delete a webhook | [DELETE account\_activity/webhooks/:webhook\_id](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#delete-account-activity-webhooks-webhook-id) | ✓   |     |
| \[DEPRECATED\] Deactivate a subscription for the provided user context and application | [DELETE account\_activity/webhooks/:webhook\_id/subscriptions/all](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#delete-account-activity-webhooks-webhook-id-subscriptions-all-deprecated-) | ✓ \* |     |
| Deactivate a subscription using application-only OAuth | [DELETE /account\_activity/webhooks/:webhook\_id/subscriptions/:user\_id/all.json](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#delete-account-activity-webhooks-webhook-id-subscriptions-user-id-all-json) |     | ✓   |
| Redelivers activities to a webhook | [POST /1.1/account\_activity/replay/webhooks/:webhook\_id/subscriptions/all.json](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/replay-api) |     | ✓   |

\* _Authentication requires the access tokens of the subscribing user._ 

For those endpoints that require OAuth 1.0a user context authentication, you will need to provide the following credentials to authenticate the request: 

* Consumer Keys (API Key and Secret)
* Access Tokens (Access Token and Secret)

In the case of the following three endpoints, you perform write actions within the context of your application (no Twitter users are involved). Therefore, the Access Tokens you need to provide are the ones belonging to your developer App. These can be generated directly from within the [developer portal](https://developer.twitter.com/en/portal/projects-and-apps), under the “Keys and tokens” tab for your App.  

* [POST account\_activity/webhooks](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#post-account-activity-webhooks): Register a new webhook URL for the given application context
* [PUT account\_activity/webhooks/:webhook\_id](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#put-account-activity-webhooks-webhook-id): Trigger a challenge response check (CRC) for a given webhook's URL
* [DELETE account\_activity/webhooks/:webhook\_id](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#delete-account-activity-webhooks-webhook-id): Delete a webhook

On the other hand, in the case of the following three endpoints, you are making a request that allows your application to access protected data on behalf of a Twitter user (for example, Direct Messages). You must therefore provide the Access Tokens that belong to the subscribing user in question. The required Access tokens can be obtained using the 3-legged OAuth flow (see [OAuth 1.0a: how to obtain a user’s Access Tokens](https://developer.twitter.com/en/docs/tutorials/authenticating-with-twitter-api-for-enterprise/oauth1-0a-and-user-access-tokens)). These endpoints have been marked with an asterisk in the above table (\*).

* [POST account\_activity/webhooks/:webhook\_id/subscriptions/all](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#post-account-activity-webhooks-webhook-id-subscriptions-all): Subscribe the application to a user’s account events
* [GET account\_activity/webhooks/:webhook\_id/subscriptions/all](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#get-account-activity-webhooks-webhook-id-subscriptions-all): Check if a webhook configuration is subscribed to a user’s events
* [DELETE account\_activity/webhooks/:webhook\_id/subscriptions/all](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#delete-account-activity-webhooks-webhook-id-subscriptions-all-deprecated-): Deactivate a subscription for the provided user context and application \[DEPRECATED\]

**Please note**: 

Make sure that your developer App is enabled for "Read, Write, and Direct Messages." You can change this setting in the [Projects & Apps section](https://developer.twitter.com/en/portal/projects-and-apps) of your developer account, under “App permissions” for the selected developer App. You will need to regenerate your App credentials after changing the permissions settings.

A list of all endpoints available with the Account Activity API, including associated description and example cURL requests with authentication implementation examples, can be found in [the API reference documentation](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise).

For additional information, check out TwitterDev’s [sample web app and helper scripts](https://github.com/twitterdev/account-activity-dashboard-enterprise) to get started with the Enterprise Account Activity API.

### Next steps

* See our [Managing your webhooks and adding subscriptions](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/guides/managing-webhooks-and-subscriptions) for more information on adding Account Activity subscrptions.
* Learn more about these topics:
    * [Securing your webhook](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/guides/securing-webhooks).
    * [Webhook JSON payload examples.](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/guides/account-activity-data-objects)
* See [Account Activity API references](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference).
* Learn more about [Twitter authentication](https://developer.twitter.com/en/docs/basics/authentication/overview/oauth).
* See example code:
    * The [SnowBot chatbot](https://github.com/twitterdev/SnowBotDev), a Ruby web app built with the Account Activity and Direct Message APIs.

Activity retries

Retries
-------

Enterprise

One of the benefits of the enterprise tier of the Account Activity API is a retry mechanism for webhook events. If a 'success' 200 HTTP response code is not received, the Twitter server will initiate a retry mechanism, resending the webhook event up to three times over a five-minute period. This webhook event retry service helps provide reliability and event recovery when network problems occur and during client-side service interruptions and deploys.  
 

### What are retries?

The Account Activity API provides a retry feature when the client's web app does not return a 'success' 200 response for an account activity webhook event. When the client-side does not confirm the successful receipt of an event, Twitter assumes the event was not received. If a non-200 response is received, a response isn't received within three seconds, or we don't receive a response at all, we retry the request and leave that open for three seconds. This means that you have roughly five seconds over two attempts to respond to receive the activity that we are trying to send to your webhook URL. In the event that your server doesn't response or returns a transient error, we will retry for five minutes. There will be a total of three retry attempts to confirm validation. This allows redundancy and insurance that you receive all webhook events. Note that subscriptions with retries will get retried events for any/all activities for all subscribed users on their webhook.

If you do not confirm validation within these eight attempts, the activity will no longer be available via the Account Activity API.   
  

### Retry timeline

The Account Activity API will retry up to three times over a five-minute period until a 200 response is received.  Refer to the table below for more details. After around five minutes, the activity cannot be resent through the Account Activity API. You will need to use other Twitter endpoints to collect missed data. For example, the [search APIs](https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/overview) can be used to retrieve relevant Tweets, Retweets, Quote Tweets, Mentions, and Replies. Missed Direct Messages can be retrieved with [this endpoint](https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/api-reference/list-events).

#### Retries timeline

|     |
| --- |
| Activity created, POST to the webhook URL from Account Activity API and times out in three seconds. |
| Wait three seconds after previous timeout finishes, then POST to the webhook URL from Account Activity API and times out in three seconds. |
| Wait 27 seconds after previous timeout finishes, then POST to the webhook URL from Account Activity API and times out in three seconds. |
| Wait 242 seconds after previous timeout finishes, then POST to the webhook URL from Account Activity API and times out in three seconds |
| The Account Activity API will stop attempting to POST after this. Client must use other Twitter endpoints to recover data. |

Next steps
----------

* Learn more about:
    * [Securing your webhook](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/guides/securing-webhooks).
    * [Managing your webhooks and adding subscriptions](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/guides/managing-webhooks-and-subscriptions).
    * [Authenticating users](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/guides/authenticating-users).
    * [Webhook JSON payload examples.](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/guides/account-activity-data-objects)
* See [Account Activity API references](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference).
* See example code:
    * The [SnowBot chatbot](https://github.com/twitterdev/SnowBotDev), a Ruby web app built with the Account Activity and Direct Message APIs.

Account Activity data objects

Account Activity data object structure
--------------------------------------

| Object | Details |
| --- | --- |
| for\_user\_id | Identifies the user subscription subscribed that the event is related to. |
| is\_blocked\_by | (conditional) Shown only when another user mentions your subscribed user. Included if true for Tweet mention events only. |
| source | The user that is performing the activity. For example, the user that is following, blocking, or muting is the source user. |
| target | The user that the activity applies to. For example, the user that is being followed, blocked, or muted is the target user. |

  
Available Activities
-----------------------

| Message Type | Details |
| --- | --- |
| [tweet\_create\_events](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/account-activity-data-objects#tweet_create_events) | Tweet status payload when any of the following actions are taken by or to the subscription user: Tweets, Retweets, Replies, @mentions, QuoteTweets, Retweet of Quote Tweets. |
| [favorite\_events](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/account-activity-data-objects#favorite_events) | Favorite (like) event status with the user and target. |
| [follow\_events](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/account-activity-data-objects#follow_events) | Follow event with the user and target. |
| [unfollow\_events](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/account-activity-data-objects#unfollow_events) | Unfollow event with the user and target. |
| [block\_events](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/account-activity-data-objects#block_events) | Block event with the user and target. |
| [unblock\_events](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/account-activity-data-objects#unblock_events) | Unblock event with the user and target. |
| [mute\_events](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/account-activity-data-objects#mute_events) | Mute event with the user and target. |
| [unmute\_events](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/account-activity-data-objects#unmute_events) | Unmute event with the user and target. |
| [user\_event](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/account-activity-data-objects#user_event) | Revoke events sent when a user removes application authorization and subscription is automatically deleted. |
| [direct\_message\_events](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/account-activity-data-objects#direct_message_events) | Direct message status with the user and target when a direct message is sent or received. |
| [direct\_message\_indicate\_typing\_events](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/account-activity-data-objects#direct_message_indicate_typing_events) | Direct message typing event with the user and target. |
| [direct\_message\_mark\_read\_events](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/account-activity-data-objects#direct_message_mark_read_events) | Direct message read event with the user and target. |
| [tweet\_delete\_events](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/account-activity-data-objects#tweet_delete_events) | Notice of deleted Tweets to make it easier to maintain compliance. |

Payload examples
----------------

See the payload examples below for each Account Activity event described in the table above.

#### tweet\_create\_events (Tweets, Retweets, Replies, QuoteTweets) 

      `{ 	"for_user_id": "2244994945", 	"tweet_create_events": [ 	  { 		<Tweet Object> 	  } 	] }`
    

#### tweet\_create\_events (@mentions) 

      `{ 	"for_user_id": "2244994945", 	"user_has_blocked": "false", 	"tweet_create_events": [ 	  { 		<Tweet Object> 	  } 	] }`
    

#### favorite\_events

      `{ 	"for_user_id": "2244994945", 	"favorite_events": [{ 		"id": "a7ba59eab0bfcba386f7acedac279542", 		"created_at": "Mon Mar 26 16:33:26 +0000 2018", 		"timestamp_ms": 1522082006140, 		"favorited_status": { 			<Tweet Object> 		}, 		"user": { 			<User Object> 		} 	}] }`
    

#### follow\_events

      `{ 	"for_user_id": "2244994945", 	"follow_events": [{ 			"type": "follow", 			"created_timestamp": "1517588749178", 			"target": { 				<User Object > 			}, 			"source": { 				< User Object > 			} 		] 	} }`
    

#### unfollow\_events

      `{ 	"for_user_id": "2244994945", 	"follow_events": [{ 			"type": "unfollow", 			"created_timestamp": "1517588749178", 			"target": { 				<User Object > 			}, 			"source": { 				< User Object > 			} 		] 	} }`
    

#### block\_events

      `{ 	"for_user_id": "2244994945", 	"block_events": [{ 		"type": "block", 		"created_timestamp": "1518127020304", 		"source": { 			<User Object> 		}, 		"target": { 			<User Object> 		} 	}] }`
    

#### unblock\_events

      `{ 	"for_user_id": "2244994945", 	"block_events": [{ 		"type": "unblock", 		"created_timestamp": "1518127020304", 		"source": { 			<User Object> 		}, 		"target": { 			<User Object> 		} 	}] }`
    

#### mute\_events

      `{ 	"for_user_id": "2244994945", 	"mute_events": [ 		{ 			"type": "mute", 		  	"created_timestamp": "1518127020304", 			"source": { 				<User Object> 			}, 			"target": { 				<User Object> 			} 		} 	] }`
    

#### unmute\_events

      `{ 	"for_user_id": "2244994945", 	"mute_events": [ 		{ 			"type": "unmute", 		  	"created_timestamp": "1518127020304", 			"source": { 				<User Object> 			}, 			"target": { 				<User Object> 			} 		} 	] }`
    

#### user\_event

      `{ 	"user_event": { 		"revoke": { 			"date_time": "2018-05-24T09:48:12+00:00", 			"target": { 				"app_id": "13090192" 			}, 			"source": { 				"user_id": "63046977" 			} 		} 	} }`
    

#### direct\_message\_events

      `{   	"for_user_id": "4337869213", 	"direct_message_events": [{ 		"type": "message_create", 		"id": "954491830116155396", 		"created_timestamp": "1516403560557", 		"message_create": { 			"target": { 				"recipient_id": "4337869213" 			}, 			"sender_id": "3001969357", 			"source_app_id": "13090192", 			"message_data": { 				"text": "Hello World!", 				"entities": { 					"hashtags": [], 					"symbols": [], 					"user_mentions": [], 					"urls": [] 				} 			} 		} 	}], 	"apps": { 		"13090192": { 			"id": "13090192", 			"name": "FuriousCamperTestApp1", 			"url": "https://twitter.com/furiouscamper" 		}, 		"users": {}, 		"3001969357": { 			"id": "3001969357", 			"created_timestamp": "1422556069340", 			"name": "Jordan Brinks", 			"screen_name": "furiouscamper", 			"location": "Boulder, CO", 			"description": "Alter Ego - Twitter PE opinions-are-my-own", 			"url": "https://t.co/SnxaA15ZuY", 			"protected": false, 			"verified": false, 			"followers_count": 22, 			"friends_count": 45, 			"statuses_count": 494, 			"profile_image_url": "null", 			"profile_image_url_https": "https://pbs.twimg.com/profile_images/851526626785480705/cW4WTi7C_normal.jpg" 		}, 		"4337869213": { 			"id": "4337869213", 			"created_timestamp": "1448312972328", 			"name": "Harrison Test", 			"screen_name": "Harris_0ff", 			"location": "Burlington, MA", 			"protected": false, 			"verified": false, 			"followers_count": 8, 			"friends_count": 8, 			"profile_image_url": "null", 			"statuses_count": 240, 			"profile_image_url_https": "https://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png" 		} 	} }`
    

#### direct\_message\_indicate\_typing\_events

      `{ 	"for_user_id": "4337869213", 	"direct_message_indicate_typing_events": [{ 		"created_timestamp": "1518127183443", 		"sender_id": "3284025577", 		"target": { 			"recipient_id": "3001969357" 		} 	}], 	"users": { 		"3001969357": { 			"id": "3001969357", 			"created_timestamp": "1422556069340", 			"name": "Jordan Brinks", 			"screen_name": "furiouscamper", 			"location": "Boulder, CO", 			"description": "Alter Ego - Twitter PE opinions-are-my-own", 			"url": "https://t.co/SnxaA15ZuY", 			"protected": false, 			"verified": false, 			"followers_count": 23, 			"friends_count": 47, 			"statuses_count": 509, 			"profile_image_url": "null", 			"profile_image_url_https": "https://pbs.twimg.com/profile_images/851526626785480705/cW4WTi7C_normal.jpg" 		}, 		"3284025577": { 			"id": "3284025577", 			"created_timestamp": "1437281176085", 			"name": "Bogus Bogart", 			"screen_name": "bogusbogart", 			"protected": true, 			"verified": false, 			"followers_count": 1, 			"friends_count": 4, 			"statuses_count": 35, 			"profile_image_url": "null", 			"profile_image_url_https": "https://pbs.twimg.com/profile_images/763383202857779200/ndvZ96mE_normal.jpg" 		} 	} }`
    

#### direct\_message\_mark\_read\_events

      `{ 	"for_user_id": "4337869213", 	"direct_message_mark_read_events": [{ 		"created_timestamp": "1518452444662", 		"sender_id": "199566737", 		"target": { 			"recipient_id": "3001969357" 		}, 		"last_read_event_id": "963085315333238788" 	}], 	"users": { 		"199566737": { 			"id": "199566737", 			"created_timestamp": "1286429788000", 			"name": "Le Braat", 			"screen_name": "LeBraat", 			"location": "Denver, CO", 			"description": "data by day @twitter, design by dusk", 			"protected": false, 			"verified": false, 			"followers_count": 299, 			"friends_count": 336, 			"statuses_count": 752, 			"profile_image_url": "null", 			"profile_image_url_https": "https://pbs.twimg.com/profile_images/936652894371119105/YHEozVAg_normal.jpg" 		}, 		"3001969357": { 			"id": "3001969357", 			"created_timestamp": "1422556069340", 			"name": "Jordan Brinks", 			"screen_name": "furiouscamper", 			"location": "Boulder, CO", 			"description": "Alter Ego - Twitter PE opinions-are-my-own", 			"url": "https://t.co/SnxaA15ZuY", 			"protected": false, 			"verified": false, 			"followers_count": 23, 			"friends_count": 48, 			"statuses_count": 510, 			"profile_image_url": "null", 			"profile_image_url_https": "https://pbs.twimg.com/profile_images/851526626785480705/cW4WTi7C_normal.jpg" 		} 	} }`
    

####   
tweet\_delete\_events

      `{     "for_user_id": "930524282358325248",     "tweet_delete_events": [ {         "status": {             "id": "1045405559317569537",             "user_id": "930524282358325248"         },         "timestamp_ms": "1432228155593"     }    ] }`

Account Activity replay API

Account Activity Replay API
---------------------------

Enterprise

The Account Activity Replay API is a data recovery tool that allows you to retrieve events from as far back as five days. It should be utilized to recover data in scenarios where your [webhook](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise) server misses events, -- whether due to disconnections lasting longer than the [retry window](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/activity-retries), or for those disaster recovery scenarios where you need a few days to restore your system back to normal.

The Account Activity Replay API was developed for any scenario where you fail to ingest [activities](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/overview) for a period of time. It delivers activities to the same webhook used for the original real-time delivery of activities. This product is a recovery tool and not a backfill tool, which means events will only be replayed if a previous delivery of them was attempted. The Account Activity Replay API cannot deliver events for a time period prior to a subscription’s creation time.

### Using Account Activity Replay API

If your account is configured with Replay functionality, you can make requests in a similar manner as requests to the Account Activity API. It is important to note that your request must specify a webhook id parameter to indicate which webhook’s activities you would like to replay. In other words, a Replay request asks Account Activity Replay API to retrieve events from a start date and time to an end date and time based on the webhook id and application id.

Please note that UTC time is expected. These activities are delivered through the registered webhook associated with the id at a rate of up to 2,500 events per second. Also keep in mind that only one Replay job per webhook may be running at a time, although all subscriptions that were active during the date/time specified on that webhook will be replayed.

Events are delivered beginning with the first (oldest) minute of the specified time period, continuing chronologically (as best as possible) until the final minute is delivered. At that point, Replay will deliver a [job completion event](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/api-reference/replay-api#job-completed-successfully-message) to the webhook. Because we work chronologically in delivering activities, if there are little or no matching results near the start time, there will likely be a period of time before the first results are delivered.

### Limitations

Replay is intended as a tool for easily recovering activities as far back as five days ago, but it will not deliver events prior to a subscription’s creation time. For example, if three days ago, you added a new subscription and ran a Replay job with a window for five days prior to today, you would only receive data for the three days that this new subscription was active.

### Data availability and types

Activities from the Account Activity Replay API are available five days from the initiation of the request, with new data becoming available roughly 10 minutes after a given activity is created. You will be able to make requests specifying a timeframe within this five day window using the from\_date and to\_date parameters within the request. Events that were originally delivered prior to having access to Replay cannot be replayed. For example, if your account was enabled for access to the Account Activity Replay API on June 1, 2019 at 3:30PM UTC, you would not be able to use Replay to retrieve any events prior to that date and time.

Continue to the [Account Activity Replay API reference](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/api-reference/replay-api)

Migration introduction

Migration introduction
----------------------

**We retired the Site Streams, User Streams, and standard beta version of the Account Activity API - DM Only products in 2018. If you had been using those products, please make sure to migrate over to the premium or enterprise version of the Account Activity API.**

**We have also retired the legacy Direct Message endpoints. If you had been using those endpoints, please make sure to migrate over to either the new DM endpoints, or to the premium or enterprise version of the Account Activity API.** 

**Please review [this announcment](https://twittercommunity.com/t/details-and-what-to-expect-from-the-api-deprecations-this-week-on-august-16-2018/110746) to learn more.**

Here are the endpoints that will be affected by these changes:  

* User Streams
* Site Streams
* GET direct\_messages
* GET direct\_messages/sent
* GET direct\_messages/show
* POST direct\_messages/new
* POST direct\_messages/destroy  
     

We have new endpoints and services available that provide similar access and, for Direct Messages, some additional functionality:

* Account Activity API [enterprise](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise) and [premium](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/premium/account-activity-api/api-reference/aaa-premium)
* [GET direct\_messages/events/list](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/list-events)
* [GET direct\_messages/events/show](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/get-event)
* [POST direct\_messages/events/new](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/new-event)
* [POST direct\_messages/events/destroy](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/delete-message-event) 

To help you make a smooth migration to these new endpoints and services we have two migration guides:

* [Account Activity API migration guide](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/migration/us-ss-migration-guide) for those going from User Streams and Site Streams to our new webhooks based service
* [Direct Message migration guide](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/guides/direct-message-migration) for those migrating between Direct Message REST endpoints  
     

Additionally, we have a [series of videos](https://www.youtube.com/playlist?list=PLFKjcMIU2WshGG6Yj940XM7Z6BFs1zfBg) about the Account Activity API and how to get started.

And, finally, we have code samples to further your understanding and help you get started quickly:

* The [Account Activity Dashboard](https://github.com/twitterdev/Account-Activity-dashboard) is a sample Node.js web app with helper scripts to get started with the Account Activity API.
* [SnowBot](https://github.com/twitterdev/SnowBotDev) is a sample chatbot using the Account Activity API and REST Direct Message endpoints. It’s written in Ruby, uses the Sinatra web app framework, and is deployed on Heroku.  
     

If you are building solutions that ingest data and respond in Direct Messages we also have a [Building a Customer Engagement Application on Twitter playbook](https://developer.twitter.com/en/docs/tutorials/customer-engagement-application-playbook).

Next steps
----------

Review our [User Streams and Site Streams migration guide](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/migration/us-ss-migration-guide)

Review our [Direct Message API migration guide](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/migration/direct-message-migration)

Learn more about the [Account Activity API](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/overview)

User Streams and Site Streams migration guide

Migration Guide: Moving from User Streams/Site Streams to Account Activity API
------------------------------------------------------------------------------

**As of August 23rd, 2018, we retired both Site Streams and User Streams. Please make sure to migrate over to the Account Activity API.**

**Please review [this announcement](https://twittercommunity.com/t/details-and-what-to-expect-from-the-api-deprecations-this-week-on-august-16-2018/110746) to learn more.**

This guide is designed to help you migrate from legacy User Streams and Site Streams APIs to their replacement, the Account Activity API. Below you will find a summary of the changes, new features list, as well as key differences and considerations to help with the transition. For guidance in migrating from basic DM endpoints, please refer to the [Direct Message migration guide](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/guides/direct-message-migration).  

### Summary of changes

The Account Activity API will deliver you events for authenticated and subscribed accounts via webhooks as opposed to a streaming connection like with User Streams and Site Streams.

#### Deprecated APIs

GET user  
  
GET site  (including control streams: GET site/c/:stream\_id,  GET site/c/:stream\_id/info.json,  GET site/c/:stream\_id/friends/ids.json,  POST site/c/:stream\_id/add\_user.json,  POST /site/c/:stream\_id/remove\_user.json)

#### Replacement APIs

[Enterprise Account Activity API - All Activities](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise)

[Premium Account Activity API - All Activities](https://developer.twitter.com/en/docs/twitter-api/premium/account-activity-api/api-reference/aaa-premium)  

### Differences & migration considerations

**API format:** The new Account Activity API operates differently than User Streams and Site Streams. You will need to alter your web app to receive data with webhooks. You can find more information on webhooks [here](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/getting-started-with-webhooks).

**Data Available:** Another key difference you will notice is in regards to the data being delivered. Twitter will no longer send events from people that you follow on Twitter (aka your home timeline). This was an intentional change and is not something we plan to alter going forward.

**Reliability:** Unlike streaming, webhooks enable confirmation of delivery and options to retry POSTed activities that do not make it to the webhook URL.  This gives more assurance that the app is receiving all applicable activities, even if there are brief disconnections or periods of downtime.  
  

### New features

The Account Activity API offers many new features, most notably that data is now delivered via webhooks as opposed to streaming. Webhooks offer many benefits compared to streaming, but the most prominent are speed and reliability. The API will send you data in the form of JSON events as they become available and you will no longer need to maintain an active connection or poll the endpoint. This limits the need for redundancy features and increases efficiency overall. More information on webhooks can be found in the [technical documentation](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/getting-started-with-webhooks).  
  

### Managing user subscriptions

The Account Activity API allows multiple subscriptions for a single registered webhook.  This allows multiple user subscriptions activities to be delivered to the same location, similar to the Site Streams architecture, with webhooks.  This means you can track subscriptions, as they pertain to your subscription limits, independently from the webhook connection.  This also allows scalability from only one or a few subscriptions to thousands of subscriptions for a single webhook.

### **How to Migrate**

### **Follow the steps below to easily migrate from the Site Streams API to the Account Activity API**

**Step 1: Decide on a Package**

Depending on how you are currently operating with User Streams or Site Streams, you should consider moving to either the enterprise or premium version of the Account Activity API.  Consider the number of applications or authorized users you are currently supporting and scale appropriately to the volume and reliability needed.  When deciding on the package that best suits your needs, some things worth considering are:

* Number of webhooks needed
* Current/projected subscriptions/authorized users managed on your application
* Current number of Twitter client applications
* The level of support you'd prefer from Twitter (forum support or managed enterprise level 1:1 support)
* Price of each package

**Step 2:** **Check the Setup of your Twitter app in the developer portal**

The [Twitter app](https://developer.twitter.com/content/developer-twitter/en/docs/basics/developer-portal/guides/apps) currently used for User Streams or Site Streams will be listed for the owning user within the [developer portal](https://developer.twitter.com/content/developer-twitter/en/docs/basics/developer-portal/overview). This Twitter app can also be used for Account Activity API to retain authorized users for that application.  A new app can also be created, and users can be re-authorized for this new app if desired.  If you are creating a new app on behalf of a business, it is recommended that you create the app with a corporate Twitter @handle account.

* Enable “Read, Write and Access direct messages” on the [permissions](https://developer.twitter.com/content/developer-twitter/en/docs/basics/authentication/overview/application-permission-model) tab of your Twitter app page.   
    \*Note that changing these settings is not retroactive, any authorized users will keep the authorization settings from the time at which they were authorized. If a user has not already given you read, write and direct message access, you will need to have that user re-authorize your application.
* If you are unfamiliar with [Twitter Sign-in](https://developer.twitter.com/content/developer-twitter/en/docs/authentication/guides/log-in-with-twitter) and how user contexts work with the Twitter API review [Obtaining Access Tokens](https://dev.twitter.com/webhooks/access-tokens).
* Generate access tokens for the Twitter app owner at the bottom of the “Keys and Tokens” tab. On this same tab take note of your Consumer Key, Consumer Secret, Access Token and Access Token Secret. You will need these to use the API.
* Generate a bearer token using your Consumer Key and Consumer Secret for [application-only](https://developer.twitter.com/content/developer-twitter/en/docs/basics/authentication/overview/application-only) API methods.

**Step 3: Setup & Configure Your Webhooks**

* Create a web app with an endpoint to use as your webhook to receive events (e.g. https://your\_domain.com/webhook/twitter or https://webhooks.your\_domain.com).
* Use your Consumer Key, Consumer Secret, Access Token and Access Token Secret when creating your webhook, Note that your endpoint must return a JSON response with a response\_token that is a base64 encoded HMAC SHA-256 hash created from the crc\_token and your app Consumer Secret.  
    
* Review [Securing Webhooks](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/securing-webhooks) documentation taking special note of the Challenge Response Check (CRC) requirements.
* Make sure your webhook supports POST requests for incoming events and GET requests for the CRC.
* Make sure your webhook has low latency (<3 seconds to respond to POST requests)

**Step 4: Validate Your Webhook Setup**

* Webhook APIs will secure your webhooks in two ways:

               - Require challenge response checks to validate that the webhook owner is the web app owner.

               - A signature header in each POST request for your web app to validate the source.

* In order to verify that you are both the owner of the web app and the webhook URL, Twitter will perform a Challenge Response Check (CRC), which is not to be confused with a cyclic redundancy check.
* A GET request with a parameter named crc\_token will be sent to your webhook URL. Your endpoint must return a JSON response with a response\_token that is a base64 encoded HMAC SHA-256 hash created from the crc\_token and your app Consumer Secret.
* The crc\_token should be expected to change for each incoming CRC request. The crc\_token should be used as the message in the calculation, where your Consumer Secret is the key.
* In the event that the response is invalid, events will cease to be sent to the registered webhook.

**Step 5: Create Subscriptions for Each User Stream or Site Streams Authorized User**

Converting to the Account Activity API from User Streams:

* Generate a list of your current user subscriptions on User Streams
* Set up your new Account Activity API subscriptions using the request:  _POST account\_activity/all/:env\_name/subscriptions_
* Confirm your Account Activity API subscriptions using the request:  _GET account\_activity/all/:env\_name/subscriptions/list_ 

Converting to the Account Activity API from Site Streams: (using control streams):

* Generate a list of your current subscriptions on Site Streams using the request:  _GET /1.1/site/c/:stream\_id/info.json_
* Set up your new Account Activity API subscriptions using the request:  _POST account\_activity/all/:env\_name/subscriptions_
* Confirm your Account Activity API subscriptions using the request:  _GET account\_activity/all/:env\_name/subscriptions/list_ 

Registering a Webhook and Creating Subscriptions (not migrating from Site Streams or User Streams)

* Register your webhook URL with your app using [POST webhooks](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#post-account-activity-webhooks) and receive a webhook\_id.
* Use the returned webhook\_id to add user subscriptions with [POST webhooks/:webhook\_id/subscriptions/all](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#post-account-activity-webhooks-webhook-id-subscriptions-all).

### The Account Activity dashboard (sample Account Activity API application)

We've created a sample app to make testing the Account Activity API a little quicker:   

* Download the Account Activity Dashboard sample application [here](https://github.com/twitterdev/Account-Activity-dashboard) (it uses Node.js)
* Follow the instructions on the README to install and launch the app
* Once the application has been launched, you can use the UI to easily set up your webhook and create a new subscription

### Available Activities

| Message Type | Details |
| --- | --- |
| [tweet\_create\_events](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/account-activity-data-objects#tweet_create_events) | Tweet status payload when any of the following actions are taken by or to the subscription user: Tweets, Retweets, Replies, @mentions, QuoteTweets |
| [favorite\_events](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/account-activity-data-objects#favorite_events) | Favorite (like) event status with the user and target. |
| [follow\_events](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/account-activity-data-objects#follow_events) | Follow event with the user and target. |
| [block\_events](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/account-activity-data-objects#block_events) | Block event with the user and target. |
| [mute\_events](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/account-activity-data-objects#mute_events) | Mute event with the user and target. |
| [direct\_message\_events](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/account-activity-data-objects#direct_message_events) | Direct message status with the user and target. |
| [direct\_message\_indicate\_typing\_events](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/account-activity-data-objects#direct_message_indicate_typing_events) | Direct message typing event with the user and target. |
| [direct\_message\_mark\_read\_events](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/account-activity-data-objects#direct_message_mark_read_events) | Direct message read event with the user and target. |

### Deprecated streaming message types 

|     |     |
| --- | --- |
| Blank lines | Blank lines will no longer be delivered in the Account Activity API as they were used as keep-alive messages in User Streams and Site Streams. |
| Limit notices | Limit notices will no longer be sent to a given webhook.  Instead, users can call the API to get current usage of available handles. This will be included in the developer portal at some time in the future. |
| Disconnect messages | Disconnect notices will no longer be necessary as webhooks do not rely on an active connection. |
| Stall warnings | Stall warnings will no longer be necessary as webhooks do not rely on an active connection being able to handle large numbers of incoming messages. |
| Friends list | Friends lists will no longer be sent proactively. There will now be a REST endpoint to get this information. |

### Deprecated event types

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Description** | **Event Name** | **Source** | **Target** | **Target Object** |
| User deletes a Tweet | delete | Current user | Current User | Tweet |
| Followed user deletes a Tweet | delete | Followed user | Followed user | Tweet |
| User unfavorites a Tweet | unfavorite | Current user | Tweet author | Tweet |
| User’s Tweet is unfavorited | unfavorite | Unfavoriting user | Current user | Tweet |
| User unfollows someone | unfollow | Current user | Followed user | Null |
| User creates a list | list\_created | Current user | Current user | List |
| User deletes a list | list\_destroyed | Current user | Current user | List |
| User edits a list | list\_updated | Current user | Current user | List |
| User adds someone to a list | list\_member\_added | Current user | Added user | List |
| User is added to a list | list\_member\_added | Adding user | Current user | List |
| User removes someone from a list | list\_member\_removed | Current user | Removed user | List |
| User is removed from a list | list\_member\_removed | Removing user | Current user | List |
| User subscribes to a list | list\_user\_subscribed | Current user | List owner | List |
| User’s list is subscribed to | list\_user\_subscribed | Subscribing user | Current user | List |
| User unsubscribes from a list | list\_user\_unsubscribed | Current user | List owner | List |
| User’s list is unsubscribed from | list\_user\_unsubscribed | Unsubscribing user | Current user | List |
| User updates their profile | user\_update | Current user | Current user | Null |
| User updates their protected status | user\_update | Current user | Current user | Null |

Direct Message migration guide

Direct Message migration guide
------------------------------

**On September 17th, 2018 we retired the legacy Direct Message endpoints.  
If you had been using those endpoints, please make sure to migrate over to the new Direct Message endpoints or the Account Activity API.**

**Please review [this announcment](https://twittercommunity.com/t/details-and-what-to-expect-from-the-api-deprecations-this-week-on-august-16-2018/110746) to learn more.**

This guide is designed to help you migrate from legacy Direct Message REST APIs to their enhanced replacements which have graduated from beta. Below you will find a summary of the changes, a new features list, and key differences and considerations to help with the transition. The new Direct Message endpoints are available now to all developers. For guidance in migrating from User Streams or Site Streams, see the [migration guide to Account Activity API](https://developer.twitter.com/content/developer-twitter/en/docs/accounts-and-users/subscribe-account-activity/migration/us-ss-migration-guide).

* [Summary of changes](#summary)
* [New features](#features)
* [Sending Direct Messages](#sending)
* [Receiving Direct Messages](#receiving)
* [Deleting Direct Messages](#deleting) 

### Summary of changes

If you are still using the following DM endpoints, you will have to migrate to the newer endpoints. 

| Deprecated endpoint | New migration alternative |
| --- | --- |
| [POST direct\_messages/new](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/new-message) | [POST direct\_messages/events/new](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/new-event) |
| [GET direct\_messages/show](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/get-message) | [GET direct\_messages/events/show](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/get-event) |
| [GET direct\_messages](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/get-messages) | [GET direct\_messages/events/list](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/list-events) |
| [GET direct\_messages/sent](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/get-sent-message) | [GET direct\_messages/events/list](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/list-events) |
| [POST direct\_messages/destroy](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/delete-message) | [DELETE direct\_messages/events/destroy](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/delete-message-event "GET direct_messages/events/list") |

### New features

The new Direct Message API endpoints support a number of new capabilities and provide improved access to previous Direct Messages. New features include:

* Support for media attachments (image, GIF, and video).
* Ability to prompt users for structured replies with a predefined options list.
* Up to 30 days of access to past Direct Messages.

For a full list of new Direct Message features and additional new API endpoints refer to the [technical documentation](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/overview).  
 

### Differences & migration considerations

The new API endpoints behave very differently from their previous counterparts. Simply updating the endpoint URLs will result in errors in your application. Consider the following when updating your application for the migration.

#### New Direct Message object

The first thing you are likely to notice is the new object structure of Direct Messages. This new Message Create object structure has been introduced to support new capabilities like [Quick Replies](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/quick-replies) and [Attachments](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/message-attachments). The new object also contains a smaller condensed user object. Your application will need to be updated to account for this new object structure when parsing and potentially in data models or storage. For descriptions of each property see the [full documentation on the Message Create Object](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/guides/message-create-object).  

**Example message create object**  

    {
      "type": "message_create",
      "id": "1234858592",
      "created_timestamp": "1392078023603",
      "initiated_via": {
        "tweet_id": "123456",
        "welcome_message_id": "456789"
      },
      "message_create": {
        "target": {
          "recipient_id": "1234858592"
        },
        "sender_id": "3805104374",
        "source_app_id": "268278",
        "message_data": {
          "text": "Blue Bird",
          "entities": {
            "hashtags": [],
            "symbols": [],
            "urls": [],
            "user_mentions": [],
          },
          "quick_reply_response": {
            "type": "options",
            "metadata": "external_id_2"
          },
          "attachment": {
            "type": "media",
            "media": {
             ...
            }
          }
        }
      }

#### Summary

* Entirely new Direct Message object structure.
* Condensed user object.
* New information provided (quick reply responses, attachments, etc).  
      
    

### Sending Direct Messages

[POST direct\_messages/events/new](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/new-event) is a direct replacement for sending Direct Messages. The most significant difference with this endpoint is that all information is now sent as JSON in the POST request body as opposed to individual POST params.

**Example Twurl request**  

twurl -A 'Content-type: application/json' -X POST /1.1/direct\_messages/events/new.json -d '{"event": {"type": "message\_create", "message\_create": {"target": {"recipient\_id": "4534871"}, "message\_data": {"text": "Hello World!"}}}}'

Note in the above request that the content-type is set to application/json as opposed to application/x-www-form-urlencoded. Additionally, if you are constructing the OAuth 1.0a signature, note that the JSON body is not included in the generation of the signature. Most OAuth libraries already account for this. If you are using [twurl](https://github.com/twitter/twurl), ensure you are using at least version 0.9.3.  

#### Summary

* Message is defined in JSON POST body
* Content-type header must be set to application/json
* JSON body is not included in the generation of the OAuth signature.  
     

### Retrieving Direct Messages

Retrieving past Direct Message is now accomplished with a single API endpoint: [GET direct\_messages/events/list](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/list-events). The significant difference with this new endpoint is that it now returns both sent and received messages in reverse chronological order. This may make it easier to rebuild a conversation. However, if you are only looking for sent or received messages you will need to post-process the response by referring to the sender\_id property.

Pagination is now based on a cursor value rather an ID of a Direct Message. A cursor property is returned with each response. [GET direct\_messages/events/list](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/list-events) will return up to 30 days of past messages, regardless of how many messages exist within the past 30 days. When a cursor is not returned, there are no more messages to be returned. The method for accessing individual Direct Messages with [GET direct\_messages/events/show](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/get-event) remains the same, although the Direct Message object returned has a different structure as described previously.

Finally, real-time access to Direct Messages will now be accomplished via webhook with the [Account Activity API](https://developer.twitter.com/content/developer-twitter/en/docs/accounts-and-users/subscribe-account-activity/overview). For guidance in migrating from User Streams or Site Streams, see the migration guide to Account Activity API for more information.

#### Summary

* Sent and Received messages are now returned on the same endpoint.
* Up to 30 days of messages returned.
* Cursor based pagination.
* Real-time access to Direct Message via webhook.  
     

### Deleting Direct Messages

Direct Messages can now be deleted with DELETE direct\_messages/events/destroy. The interface is largely the same requiring the ID of the message to delete. The key differences is the endpoint now requires a DELETE request instead of a POST request.  
  
How deleted Direct Messages are reflected in official Twitter clients remains the same. Direct Messages are only removed from the interface of the user context provided. Other members of the conversation can still access the Direct Message.

#### Summary

* Deleting a Direct Message requires the ID.
* New endpoint requires a DELETE request.
* How deleted Direct Messages are reflected in official Twitter clients remains unchanged.

**Questions about migrating to the new Direct Message endpoints?  
**Post your question to the developer community forum on [twittercommunity.com](https://twittercommunity.com/tags/c/rest-api/rest-api-v1-1/directmessages).

Next Steps
----------

*     Download our Direct Message Migration Guide (below)

Direct Messages[Direct Message - Migration Guide
--------------------------------](https://cdn.cms-twdigitalassets.com/content/dam/developer-twitter/pdfs-and-files/DM%20-%20Migration%20Guide.pdf)

[Download PDF](https://cdn.cms-twdigitalassets.com/content/dam/developer-twitter/pdfs-and-files/DM%20-%20Migration%20Guide.pdf)

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

To get started, visit the [playbook](https://developer.twitter.com/content/developer-twitter/en/docs/tutorials/customer-engagement-application-playbook) or download sample code snippets from [GitHub](https://github.com/twitterdev/account-activity-dashboard).  
 

**How do I identify which product tier is best for me?**

Please read through our [Account Activity API Overview](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/overview) page to learn more about the differences between the Premium options and the Enterprise option.   
 

**What is the difference between a Premium environment and an Enterprise webhook?**

There is no difference. Each Premium environment will have its own webhook\_id.  
 

**I need a development, staging and production environment for Account Activity API, is this possible?**

Yes! With the paid tiers of Account Activity API (Paid Premium and Enterprise), it's possible to register multiple webhook URLs and manage subscriptions separately for each through the API methods. Additionally, multiple client apps may be added to an allowlist to maintain authorization for your current authorized users.  
 

**Do you have any step-by-step guides on how to get set up with the Account Activity API?**

As a matter of fact, we do!

* If you are just getting started, we recommend that you visit our [Getting started with webhooks](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/getting-started-with-webhooks) guide  
    
* Follow along with our Twitter Dev supported scripts: 
    * [Account Activity API dashboard](https://github.com/twitterdev/account-activity-dashboard), a node web app that displays webhook events.
    * The [SnowBot chatbot](https://github.com/twitterdev/SnowBotDev), a Ruby web app built on the Account Activity and Direct Message APIs. This code base includes a [script](https://github.com/twitterdev/SnowBotDev/wiki/Account-Activity-API-setup-script) to help set up Account Activity API webhooks.  
         

**Is there a way to recover data if our system goes down for a period of time?**

With the paid tiers of Account Activity API (Paid Premium and Enterprise), our system will [retry](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/activity-retries) to send the activities to you several times over a four hour period. If your system does not respond within that four hour period, then the activity will be lost and you will have to use other REST endpoints to recover data within 7 days.

We suggest that you use your different webhooks, or environments, as a redundancy tool like the [Account Activity Replay API](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/guides/activity-replay-api) to ensure that you don't miss any activities if one of your systems goes down.  
 

**What authentication do I have to use with the Account Activity API?**

The authorization methods required for Account Activity API is described per method in the [API reference pages](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/api-reference). If you are just starting out with Twitter authentication, we recommend that you read through [this section](https://developer.twitter.com/content/developer-twitter/en/docs/basics/authentication/overview/oauth).  
  

**What is a challenge-response check (CRC)?**

The Account Activity API challenge response check is a security feature put in place to ensure that the Account Activity API’s activities are being sent to the proper developer. It also can be used by developers to ensure that the data that they are receiving is coming from Twitter. Twitter will automatically send a CRC to your webhook URL once every 24 hours, starting the last time the webhook URL was validated. Your system must respond with a valid response within 3 seconds to remain validated. 

Please visit our page [Securing webhooks](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/securing-webhooks) for more details.  
 

**Is there anything that would immediately invalidate my webhook URL?**

If one of the following occurs, we will immediately mark your webhook as invalid:

* The server responds to a CRC with an incorrect token. In this case, our system will not [retry](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/activity-retries) to send you the activity.
* The webhook URL has an incorrect certificate configured. In this case, our system will not [retry](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/activity-retries) to send you the activity.
* Your server returning a non-2XX, non-4XXX, non-5XXX response code.
* You specify the use of gzip without actually sending it.
* You do not specify the use of gzip, but actually send it in the response.  
     

**Will I get duplicate activities if subscribed to users that are interacting with each other?**

Yes.  If your web app has active subscriptions for User A and User B, and User A mentions User B in a Tweet, there will be two POST activities sent to the registered webhook.  Each activity will have an indicator of "for\_user\_id" to show which subscription the activity belongs to.  
 

**When I make a subscription to my webhook, can I replace the `/all/` portion of the following endpoint with other account activity data objects to limit the activities the API delivers?** `POST https://api.twitter.com/1.1/account_activity/all/:env_name/subscriptions.json`

No, this is not possible. As it currently stands, we only have the `/all/` product available.  
 

**Is there any way of using the Account Activity API without requesting Direct Messages permissions from users?** 

At this point, Direct Messages permissions are required because there is no way to 'filter out' the Direct Messages activities for this API.   
 

**Is there a free version of the Account Activity API?**

Yes, we offer the sandbox version as a free tier. Our sandbox option is limited to a single webhook with a limit of a maximum of 15 subscriptions. You can read more about the sandbox option in [our documentation](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/premium/account-activity-api/overview).   
  

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

You will see a boolean field \`user\_has\_blocked\` on the top level of the json response, set to either “true” or “false". This field will only be exposed on Tweet mentions. 

Enterprise

**How can I add my app to an allowlist or check if my app is already on the allowlist?**

To manage the [Twitter apps](https://developer.twitter.com/content/developer-twitter/en/docs/basics/developer-portal/guides/apps) that you have added to an allowlist for access via the Enterprise APIs, please reach out to your account manager with your app ID. You can find your app ID by navigating to the ["Apps"](https://developer.twitter.com/content/developer-twitter/en/docs/basics/developer-portal/guides/apps) page in the [developer portal](https://developer.twitter.com/content/developer-twitter/en/docs/basics/developer-portal/overview).  
 

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

* **Enterprise** - Make sure the consumer keys and access tokens you are using belong to a [Twitter app](https://developer.twitter.com/content/developer-twitter/en/docs/basics/developer-portal/guides/apps) that has been registered for use of Enterprise products. If you don't have your consumer keys and access tokens, or need to add your Twitter app to the allowlist, please reach out to your account manager.   
    
* If authenticating with user context, make sure you have properly [authorized your request](https://developer.twitter.com/content/developer-twitter/en/docs/basics/authentication/guides/authorizing-a-request) with the proper `oauth nonce`, `oauth_signature`, and `oauth_timestamp`.  
    
* Make sure that your access tokens have the proper permission level.
    * When on the 'Keys and tokens' tab in the [app dashboard](https://developer.twitter.com/content/developer-twitter/en/docs/basics/developer-portal/guides/apps), please make sure that your access tokens have the 'Read, write, and direct messages' [permission level](https://developer.twitter.com/content/developer-twitter/en/docs/basics/authentication/overview/application-permission-model). 
    * If the tokens' permission level is set to anything less than this, please navigate to the 'Permissions' tab, adjust the access permission to 'Read, write, and direct messages', then regenerate your access tokens and secret from the 'Keys and tokens' tab.

* Make sure that your URL is formed properly.
    * Please keep in mind that `:env_name` is case sensitive.  
         

#### Code 200 - Forbidden

* **Premium** - Make sure that you have an approved [developer account](https://developer.twitter.com/content/developer-twitter/en/docs/basics/developer-portal/overview) before you try to make a request to the API. You also must use the proper :env\_name in the request, which you can setup on the [dev environments](https://developer.twitter.com/content/developer-twitter/en/docs/basics/developer-portal/guides/dev-environments) page.  
    
* **Enterprise** - Make sure that your account manager has set you up with access to the Account Activity API.
* Make sure you have set up your URI properly. This error can trigger if you have entered the incorrect URI in your request.  
     

#### Code 214 - Webhook URL does not meet the requirements.

* Please make sure that you are using https.
* Your webhook URL could be malformed.
* Learn more about how to set up your webhook URL under the [Develop webhook consumer app](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/getting-started-with-webhooks#webhook-url) section on [Getting started with webhooks](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/getting-started-with-webhooks) page.  
     

#### Code 214 - High latency on CRC GET request. Your webhook should respond in less than 3 seconds.

* This means that your server is slow. Make sure that you are responding to the CRC within 3 seconds.  
     

#### Code 214 - Non-200 response code during CRC GET request (i.e. 404, 500, etc).

* Your server is down. Make sure that your server is running properly.  
     

#### Code 214 - Too many resources already created.

* **Enterprise** - You have already used all of your webhooks. Use the [GET webhooks](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#get-account-activity-webhooks) endpoint with each of your registered apps to identify where your webhooks are distributed.   
      
    

#### Code 261 - Application cannot perform write actions.

* The app that you are using with the API does not have the proper [permission level](https://developer.twitter.com/content/developer-twitter/en/docs/basics/authentication/overview/application-permission-model) set for its access token and access token secret. Please navigate to the 'Keys and tokens' tab on the [Twitter apps](https://developer.twitter.com/content/developer-twitter/en/docs/basics/developer-portal/guides/apps) dashboard and check the permission levels assigned to your access token and access token secret. If it is set to anything other than 'Read, write and Direct Messages,' then you are going to have to adjust the settings under the 'Permission' tab and regenerate your access token and access token secret to apply the new settings.
* Alternatively, you are trying to register a webhook using app-only authentication, which is not supported. Please authenticate with user context instead as noted in the API reference sections for registering a webhook for [Enterprise Account Activity API](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#post-account-activity-webhooks).

Enterprise Account Activity API

aaa-enterprise

Enterprise Account Activity API
===============================

POST account\_activity/webhooks[¶](#post-account-activity-webhooks "Permalink to this headline")
------------------------------------------------------------------------------------------------

Registers a new webhook URL for the given application context. The URL will be validated via CRC request before saving. In case the validation failed, returns comprehensive error message to the requester.

The number of allowed webhooks is determined by billing package.

### Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/account_activity/webhooks.json`

### Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response Format | JSON |
| Requires Authentication | Yes (user context - all consumer and access tokens) |
| Rate Limited | Yes |
| Requests / 15-min window (user auth) | 15  |
| Support for Tweet edits | All Tweet objects will include Tweet edit metadata describing the Tweet's edit history. See the ["Tweet edits" fundamentals](https://developer.twitter.com/en/docs/twitter-api/enterprise/tweet-edits) page for more details. |

### Parameters[¶](#parameters "Permalink to this headline")

|     |     |
| --- | --- |
| url (required) | Encoded URL for the callback endpoint. |

### Example Request[¶](#example-request "Permalink to this headline")

    $ curl --request POST 
       --url 'https://api.twitter.com/1.1/account_activity/webhooks.json?url=https%3A%2F%2Fyour_domain.com%2Fwebhooks%2Ftwitter%2F0' 
       --header 'authorization: OAuth oauth_consumer_key="CONSUMER_KEY", oauth_nonce="GENERATED", oauth_signature="GENERATED", oauth_signature_method="HMAC-SHA1", oauth_timestamp="GENERATED", oauth_token="ACCESS_TOKEN", oauth_version="1.0"'

### HTTP Responses[¶](#http-responses "Permalink to this headline")

| HTTP Code | Message |
| --- | --- |
| 200 | Webhook URL is registered to the provided application |
| 403 | There is an error with your request. See error messages section below. |

### Example Response - Success[¶](#example-response-success "Permalink to this headline")

_HTTP 200_

    {
      "id": "1234567890",
      "url": "https://your_domain.com/webhook/twitter/0",
      "valid": true,
      "created_at": "2016-06-02T23:54:02Z"
    }

### Error Messages[¶](#error-messages "Permalink to this headline")

| Code | Message |
| --- | --- |
| 214 | Webhook URL does not meet the requirements. |
| 214 | Too many resources already created. |
| 214 | Webhook URL does not meet the requirements. Invalid CRC token or json response format. |
| 214 | High latency on CRC GET request. Your webhook should respond in less than 3 seconds. |
| 214 | Non-200 response code during CRC GET request (i.e. 404, 500, etc). |

_HTTP 403_

    {
      "errors": [
        {
          "code": 214,
          "message": "Too many resources already created."
        }
      ]
    }

GET account\_activity/webhooks[¶](#get-account-activity-webhooks "Permalink to this headline")
----------------------------------------------------------------------------------------------

Returns all URLs and their statuses for the given application.

We mark a URL as invalid if it fails the daily validation check. In order to re-enable the URL, call the update endpoint.

### Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/account_activity/webhooks.json`

### Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response Format | JSON |
| Requires Authentication | Yes (application only - bearer token) |
| Rate Limited | Yes |
| Requests / 15-min window (application auth) | 15  |

### Example Request[¶](#example-request "Permalink to this headline")

    $ curl --request GET 
     --url https://api.twitter.com/1.1/account_activity/webhooks.json 
     --header 'authorization: Bearer TOKEN'

### Example Response[¶](#example-response "Permalink to this headline")

_HTTP 200 OK_

    [
      {
        "id": "1234567890",
        "url": "https://your_domain.com/webhook/twitter/0",
        "valid": true,
        "created_at": "2016-06-02T23:54:02Z"
      }
      {
        "id": "2468013579",
        "url": "https://your_domain2.com/webhook/twitter/0",
        "valid": true,
        "created_at": "2016-06-04T22:31:29Z"
      }
    ]

### Error Messages[¶](#error-messages "Permalink to this headline")

| Code | Message |
| --- | --- |
| 99  | You don’t have access to this resource. |

PUT account\_activity/webhooks/:webhook\_id[¶](#put-account-activity-webhooks-webhook-id "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------------

Triggers the challenge response check (CRC) for the given webhook's URL. If the check is successful, returns 204 and reenables the webhook by setting its status to `valid`.

### Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/account_activity/webhooks/:webhook_id.json`

### Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response Format | JSON |
| Requires Authentication | Yes (user context - all consumer and access tokens) |
| Rate Limited | Yes |
| Requests / 15-min window (user auth) | 15  |

### Parameters[¶](#parameters "Permalink to this headline")

|     |     |
| --- | --- |
| webhook\_id (required) | Webhook ID. Defined in resource path. |

### Example Request[¶](#example-request "Permalink to this headline")

    $ curl --request PUT 
     --url https://api.twitter.com/1.1/account_activity/webhooks/:WEBHOOK_ID.json 
     --header 'authorization: OAuth oauth_consumer_key="CONSUMER_KEY", oauth_nonce="GENERATED", oauth_signature="GENERATED", oauth_signature_method="HMAC-SHA1", oauth_timestamp="GENERATED", oauth_token="ACCESS_TOKEN", oauth_version="1.0"'

### Response[¶](#response "Permalink to this headline")

_HTTP 204 OK_

    { }

### Error Messages[¶](#error-messages "Permalink to this headline")

| Code | Message |
| --- | --- |
| 34  | Webhook does not exist or is associated with a different twitter application. |
| 214 | Webhook URL does not meet the requirements. |
| 214 | Webhook URL does not meet the requirements. Invalid CRC token or json response format. |
| 214 | High latency on CRC GET request. Your webhook should respond in less than 3 seconds. |
| 214 | Non-200 response code during CRC GET request (i.e. 404, 500, etc). |

POST account\_activity/webhooks/:webhook\_id/subscriptions/all[¶](#post-account-activity-webhooks-webhook-id-subscriptions-all "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------------------------------------

Subscribes the provided application to all events for the provided user context for all message types. After activation, all events for the requesting user will be sent to the application’s webhook via POST request.

Subscriptions are currently limited based on your account configuration. If you have a need to add more subscriptions, please contact your account manager.

### Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/account_activity/webhooks/:webhook_id/subscriptions/all.json`

### Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response Format | JSON |
| Requires Authentication | Yes (3-legged OAuth - Whitelisted consumer key and subscribing user's access token) |
| Rate Limited | Yes |
| Requests / 15-min window (user auth) | 500 |

### Parameters[¶](#parameters "Permalink to this headline")

|     |     |
| --- | --- |
| webhook\_id (required) | Webhook ID. Defined in resource path. |

### Example Request[¶](#example-request "Permalink to this headline")

    $ curl --request POST 
     --url https://api.twitter.com/1.1/account_activity/webhooks/:WEBHOOK_ID/subscriptions/all.json 
     --header 'authorization: OAuth oauth_consumer_key="WHITELISTED_CONSUMER_KEY", oauth_nonce="GENERATED", oauth_signature="GENERATED", oauth_signature_method="HMAC-SHA1", oauth_timestamp="GENERATED", oauth_token="SUBSCRIBING_USER'S_ACCESS_TOKEN", oauth_version="1.0"'

### Example Response - Success[¶](#example-response-success "Permalink to this headline")

_HTTP 204 NO CONTENT_

    {}

### Error Messages[¶](#error-messages "Permalink to this headline")

| Code | Message |
| --- | --- |
| 34  | Webhook does not exist or is associated with a different twitter application. |
| 348 | Client application is not permitted to access this user's webhook subscriptions. |

GET account\_activity/subscriptions/count[¶](#get-account-activity-subscriptions-count "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------

Returns the count of subscriptions that are currently active on your account. Note that the /count endpoint requires application-only OAuth, so that you should make requests using a bearer token instead of user context.

### Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/account_activity/subscriptions/count.json`

### Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response Format | HTTP response code |
| Requires Authentication | Yes (application only - bearer token) |
| Rate Limited | Yes |
| Requests / 15-min window (application auth) | 15  |

### HTTP Response Codes[¶](#http-response-codes "Permalink to this headline")

|     |     |
| --- | --- |
| Code | Message |
| 200 | Success. A count of subscriptions for the requested webhook will be returned. |
| 401 | Your application does not have permission to view subscriptions for the specified webhook. |

### Example Request[¶](#example-request "Permalink to this headline")

    $ curl --request GET 
     --url https://api.twitter.com/1.1/account_activity/subscriptions/count.json 
     --header 'authorization: Bearer TOKEN'

### Example Response - Success[¶](#example-response-success "Permalink to this headline")

_HTTP 200_

    {
      "account_name":"my-account",
      "subscriptions_count_all":"1",
      "subscriptions_count_direct_messages":"0",
      "provisioned_count":"50"
    }

### Error Messages[¶](#error-messages "Permalink to this headline")

| Code | Message |
| --- | --- |
| 32  | Could not authenticate you. |

_HTTP 401_

    {
      "errors": [
        {
           "code": 32,
          "message": "Could not authenticate you."
        }
      ]
    }

GET account\_activity/webhooks/:webhook\_id/subscriptions/all[¶](#get-account-activity-webhooks-webhook-id-subscriptions-all "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------------------------------------------------

Provides a way to determine if a webhook configuration is subscribed to the provided user’s events. If the provided user context has an active subscription with provided application, returns 204 OK. If the response code is not 204, then the user does not have an active subscription. See HTTP Response code and error messages below for details.

### Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/account_activity/webhooks/:webhook_id/subscriptions/all.json`

### Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response Format | JSON |
| Requires Authentication | Yes (3-legged OAuth - Whitelisted consumer key and subscribing user's access token) |
| Rate Limited | Yes |
| Requests / 15-min window (user auth) | 500 |

### Parameters[¶](#parameters "Permalink to this headline")

|     |     |
| --- | --- |
| webhook\_id (required) | Webhook ID. Defined in resource path. |

### Example Request[¶](#example-request "Permalink to this headline")

    $ curl --request GET 
     --url https://api.twitter.com/1.1/account_activity/webhooks/:WEBHOOK_ID/subscriptions/all.json 
     --header 'authorization: OAuth oauth_consumer_key="WHITELISTED_CONSUMER_KEY", oauth_nonce="GENERATED", oauth_signature="GENERATED", oauth_signature_method="HMAC-SHA1", oauth_timestamp="GENERATED", oauth_token="SUBSCRIBING_USER'S_ACCESS_TOKEN", oauth_version="1.0"'

### Example Response - Success[¶](#example-response-success "Permalink to this headline")

_HTTP 204 NO CONTENT_

    { }

GET account\_activity/webhooks/:webhook\_id/subscriptions/all/list[¶](#get-account-activity-webhooks-webhook-id-subscriptions-all-list "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

Returns a list of the current All Activity type subscriptions for the specified webhook. Note that the /list endpoint requires application-only OAuth, so requests should be made using a bearer token instead of user context.

### Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/account_activity/webhooks/:webhook_id/subscriptions/all/list.json`

### Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response Format | HTTP response code |
| Requires Authentication | Yes (application only - bearer token) |
| Rate Limited | Yes |
| Requests / 15-min window (application auth) | 50  |

### Parameters[¶](#parameters "Permalink to this headline")

|     |     |
| --- | --- |
| webhook\_id (required) | Webhook ID. Defined in resource path. |

### HTTP Response Codes[¶](#http-response-codes "Permalink to this headline")

| Code | Message |
| --- | --- |
| 200 | Success. A list of subscriptions for the requested webhook will be returned. |
| 401 | Your application does not have permission to view subscriptions for the specified webhook. |

### Example Request[¶](#example-request "Permalink to this headline")

    $ curl --request GET 
     --url https://api.twitter.com/1.1/account_activity/webhooks/:WEBHOOK_ID/subscriptions/all/list.json 
     --header 'authorization: Bearer TOKEN'

### Example Response - Success[¶](#example-response-success "Permalink to this headline")

_HTTP 200_

    {
      "webhook_id": "1234567890",
      "webhook_url": "https://your_domain.com/webhook/twitter/0",
      "application_id": "11231812",
      "subscriptions": [{
        "user_id": "20212306"
      }]
    }

### Error Messages[¶](#error-messages "Permalink to this headline")

| Code | Message |
| --- | --- |
| 32  | Could not authenticate you. |

_HTTP 401_

    {
      "errors": [
        {
           "code": 32,
          "message": "Could not authenticate you."
        }
      ]
    }

DELETE account\_activity/webhooks/:webhook\_id[¶](#delete-account-activity-webhooks-webhook-id "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------------------

Removes the webhook from the provided application's configuration. The webhook ID can be accessed by making a call to GET /1.1/account\_activity/webhooks.

### Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/account_activity/webhooks/:webhook_id.json`

### Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response Format | JSON |
| Requires Authentication | Yes (user context - all consumer and access tokens) |
| Rate Limited | Yes |
| Requests / 15-min window (user auth) | 15  |

### Parameters[¶](#parameters "Permalink to this headline")

|     |     |
| --- | --- |
| webhook\_id (required) | Webhook ID. Defined in resource path. |

### Example Request[¶](#example-request "Permalink to this headline")

    $ curl --request DELETE 
     --url https://api.twitter.com/1.1/account_activity/webhooks/:WEBHOOK_ID.json 
     --header 'authorization: OAuth oauth_consumer_key="CONSUMER_KEY", oauth_nonce="GENERATED", oauth_signature="GENERATED", oauth_signature_method="HMAC-SHA1", oauth_timestamp="GENERATED", oauth_token="ACCESS_TOKEN", oauth_version="1.0"'

### Response[¶](#response "Permalink to this headline")

_HTTP 204 OK_

    { }

DELETE account\_activity/webhooks/:webhook\_id/subscriptions/all (DEPRECATED)[¶](#delete-account-activity-webhooks-webhook-id-subscriptions-all-deprecated- "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Deactivates subscription(s) for the provided user context and application. After deactivation, all events for the requesting user will no longer be sent to the webhook URL.

### Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/account_activity/webhooks/:webhook_id/subscriptions/all.json`

### Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response Format | JSON |
| Requires Authentication | Yes (3-legged OAuth - Whitelisted consumer key and subscribed user's access token) |
| Rate Limited | Yes |
| Requests / 15-min window (user auth) | 500 |

### Parameters[¶](#parameters "Permalink to this headline")

|     |     |
| --- | --- |
| webhook\_id (required) | Webhook ID. Defined in resource path. |

### Example Request[¶](#example-request "Permalink to this headline")

    $ curl --request DELETE 
     --url https://api.twitter.com/1.1/account_activity/webhooks/:WEBHOOK_ID/subscriptions/all.json 
     --header 'authorization: OAuth oauth_consumer_key="WHITELISTED_CONSUMER_KEY", oauth_nonce="GENERATED", oauth_signature="GENERATED", oauth_signature_method="HMAC-SHA1", oauth_timestamp="GENERATED", oauth_token="SUBSCRIBED_USER'S_ACCESS_TOKEN", oauth_version="1.0"'
    
    Example Request

* * *

    { }

DELETE /account\_activity/webhooks/:webhook\_id/subscriptions/:user\_id/all.json[¶](#delete-account-activity-webhooks-webhook-id-subscriptions-user-id-all-json "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Deactivates subscription for the specified webhook and user id. After deactivation, all events for the requesting user will no longer be sent to the webhook URL. Note, that this endpoint requires application-only OAuth, so requests should be made using a bearer token instead of user context.

### Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/account_activity/webhooks/:webhook_id/subscriptions/:user_id/all.json`

### Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response Format | JSON |
| Requires Authentication | Yes (application only - bearer token) |
| Rate Limited | Yes |
| Requests / 15-min window | 500 |

### Example Request[¶](#example-request "Permalink to this headline")

    $ curl --request DELETE 
     --url https://api.twitter.com/1.1/account_activity/webhooks/:webhook_id/subscriptions/:user_id/all.json 
     --header 'authorization: Bearer TOKEN'
    

### Response[¶](#response "Permalink to this headline")

_HTTP 204 NO CONTENT_

### Error Messages[¶](#error-messages "Permalink to this headline")

| Code | Message |
| --- | --- |
| 404 | Sorry, that page does not exist. - This often occurs when the specified user id is not actually subscribed. |

Replay API

replay-api

Replay API
==========

POST /1.1/account\_activity/replay/webhooks/:webhook\_id/subscriptions/all.json [¶](#post-1-1-account-activity-replay-webhooks-webhook-id-subscriptions-all-json- "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Submits a request to retrieve activities from up to the past five days from all subscriptions present during the date and time windows specified in the request. If your webhook has active user subscriptions, you will concurrently receive those events as well. Note: We do perform a CRC before delivering replay events.

|     |     |
| --- | --- |
| **Request Method** | HTTP POST |
| **URL** | /1.1/account\_activity/replay/webhooks/:webhook\_id/subscriptions/all.json?from\_date=yyyymmddhhmm&to\_date=yyyymmddhhmm |
| **Response Format** | JSON |
| **Requires Authentication** | Yes (application only - bearer token) |
| **Rate Limit** | 5 requests per 15 minutes. There is currently no maximum on the number of replay jobs that can requested. |
| **from\_date** | The oldest (starting) UTC timestamp from which the events will be provided, must be in 'yyyymmddhhmm' format. Timestamp is in minute granularity and is inclusive (i.e. 12:00 includes the 00 minute). Valid times must be within the last 5 days, UTC time, and no more recent than 31 minutes before the current point in time. It's recommended that the from\_date and to\_date should be within ~2 hours. |
| **to\_date** | The latest (ending) UTC timestamp to which the event will be provided, must be in 'yyyymmddhhmm' format. Timestamp is in minute granularity and is exclusive (i.e. 12:30 does not include the 30th minute of the hour). Valid times must be within the last 5 days, UTC time, and no more recent than 10 minutes before the current point in time. |

  

#### Responses

The following responses may be returned by the API. Most error codes are returned with a string including additional details in the body. For non-200 responses, you should resolve the error and try again.

| Status | Text | Error Code | Description | Message |
| --- | --- | --- | --- | --- |
| 202 | Accepted | N/A | The request was successful and the activities will be sent. | N/A |
| 400 | Bad Request | 214 | Webhook has been marked as invalid. | Webhook is marked invalid and requires a CRC check. |
| 400 | Bad Request | 357 | Query parameter is missing. | : queryParam is required. |
| 400 | Bad Request | 358 | Route or query parameter is malformed. | Unable to parse parameter. |
| 400 | Bad Request | 360 | Route parameter is negative. | webhook\_id: \[\] is not greater than or equal to 0. |
| 400 | Bad Request | 368 | from\_date or to\_date is not in the past. | : \[<field\_value>\] is not in the past. |
| 400 | Bad Request | 356 | from\_date must be before to\_date. | from\_date must be before to\_date. |
| 400 | Bad Request | 356 | from\_date must be within the past 5 days. | from\_date must be within the past 5 days. |
| 401 | Unauthorized | 32  | HTTP authentication failed due to 3-legged auth provided. | Invalid authentication method. Please use application-only authentication. |
| 401 | Unauthorized | 61  | Client is not permitted to request this method. | Client is not permitted to request this method. |
| 403 | Forbidden | 200 | Client does not have an enterprise account with Replay enabled. | Account Activity API enterprise account with replay is required. Please confirm you have an enterprise account and replay is enabled. |
| 404 | Not Found | 34  | Non-existing webhook\_id; webhook\_id-application\_id mismatch. | Webhook does not exist or is associated with a different twitter application. |
| 409 | Conflict | 355 | There is a request in flight and it will need to finish processing before making another. | A replay job is already in progress for this webhook. |
| 429 | Too Many Requests | 88  | Rate limited (hit limit of the number of requests per time period) | Too many requests. Please back off your API request rate. |
| 500 | Internal Server Error | 0   | Internal server error. | Internal server error. |
| 503 | Service Unavailable | 67  | One or more dependent services at Twitter is unavailable. | Twitter server error. Retry using an exponential backoff pattern. |

  

#### "Job completed successfully” message

Once your job successfully completes, Account Activity Replay API will deliver the following job completion event. Once you receive this event, the job has finished running and another can be submitted.

{
  "replay\_job\_status": {
    "webhook\_id": "1234577122340233217",
    "job\_state": "Complete",
    "job\_state\_description": "Job completed successfully"
    "job\_id": "1095098195724558337"
  }
}

#### "Job failed to complete" message

In the event your job does not complete successfully, we will return the following message encouraging you to retry your Replay job. Once you receive this event, the job has finished running and another can be submitted.

{
  "replay\_job\_status": {
    "webhook\_id": "123451374207332352",
    "job\_state": "Incomplete",
    "job\_state\_description": "Job failed to deliver all events, please retry your replay job",
    "job\_id": "1093226942650736640"
  }
}

#### Example curl request

    curl --request POST  --url 'https://api.twitter.com/1.1/account_activity/replay/webhooks/:webhook_id/subscriptions/all.json?from_date=yyyymmddhhmm&to_date=yyyymmddhhmm'
    --header 'authorization: Bearer TOKEN'

#### Example response

HTTP 202

{
  "job\_id": "1234567890",
  "created\_at": "2016-06-02T23:54:02Z"
}