
Managing Enterprise Account Activity API | Docs | Twitter Developer Platform 

Managing Enterprise Account Activity API

Manage webhooks and subscribed users
------------------------------------

**⏱ 10 min read**

The enterprise Account Activity API provides you webhook-based JSON messages any time there are events associated with Twitter accounts subscribed to your service. Twitter delivers those activities to your registered webhook. In the following steps, you will learn how to manage webhooks and subscribed users.

You will learn how to register, view, and remove, both webhooks and subscribed users. We'll be using simple cURL commands to make requests to the various API endpoints. cURL is a command-line tool for getting or sending requests using the URL syntax.

You will need:

* A registered Twitter app - *register here*
* A bearer token - *learn more*
* A webhook that passes a Challenge-Response Check (CRC) - *learn more*
* An enterprise account - *apply here*

*Before you get started, we recommend you check out our Github repo here that provides a sample web app and helper scripts to get started with Twitter's Account Activity API*

### Managing a webhook:

Using a webhook provides you the ability to subscribe to realtime activities related to a user account through a single connection. 

* Adding a webhook
* Viewing a webhook
* Removing a webhook
* 

 Adding a webhook

 Viewing a webhook

 Removing a webhook

Let’s begin with registering a new webhook URL for the given application context.

The URL will be validated via a CRC request before saving. Once you've registered a webhook, make sure to document the webhook ID as you will need it later on.

Copy the following cURL request into your command line after making changes to the following:

* **URL** `<URL>` e.g. `https://yourdomain.com/webhooks/twitter/`
* **Consumer key** `<CONSUMER_KEY>` e.g. `xvz1evFS4wEEPTGEFPHBog`
* **Access token** `<ACCESS_TOKEN>` e.g.  `370773112-GmHxMAgYyLbNEtIKZeRNFsMKPR9EyMZeS9weJAEb`

```
      curl --request POST --url 'https://api.twitter.com/1.1/account_activity/webhooks.json?url=<URL>' --header 'authorization: OAuth oauth_consumer_key="<CONSUMER_KEY>", oauth_nonce="GENERATED", oauth_signature="GENERATED", oauth_signature_method="HMAC-SHA1", oauth_timestamp="GENERATED", oauth_token="<ACCESS_TOKEN>", oauth_version="1.0"'
```

Code copied to clipboard

We will run the following command to returns all registered webhook URLs and their statuses for the given application.

Copy the following cURL request into your command line after making changes to the following:

* **Bearer token** `<BEARER_TOKEN>` e.g. `AAAAAAAAAAAA0%2EUifi76ZC9Ub0wn...`

```
      curl --request GET --url https://api.twitter.com/1.1/account_activity/webhooks.json --header 'authorization: Bearer <BEARER_TOKEN>'
```

Code copied to clipboard

To remove a webhook from the provided application's configuration, copy the following cURL request into your command line after making changes to the following:

* **Webhook ID** `<:WEBHOOK_ID>` e.g. `1234567890`
* **Consumer key** `<CONSUMER_KEY>` e.g. `xvz1evFS4wEEPTGEFPHBog`
* **Access token** `<ACCESS_TOKEN>` e.g.  `370773112-GmHxMAgYyLbNEtIKZeRNFsMKPR9EyMZeS9weJAEb`

```
      curl --request DELETE --url https://api.twitter.com/1.1/account_activity/webhooks/<:WEBHOOK_ID>.json --header 'authorization: OAuth oauth_consumer_key="<CONSUMER_KEY>", oauth_nonce="GENERATED", oauth_signature="GENERATED", oauth_signature_method="HMAC-SHA1", oauth_timestamp="GENERATED", oauth_token="<ACCESS_TOKEN>", oauth_version="1.0"'
```

Code copied to clipboard

### Managing subscribed users:

Once you've registered a Webhook, you can add a subscribed user to the Account Activity API to begin receiving their account activities.

* Adding a subscription
* Viewing subscriptions
* Removing a subscription
* 

 Adding a subscription

 Viewing subscriptions

 Removing a subscription

We'll begin with subscribing a user so you recieve all event types.

Copy the following cURL request into your command line after making changes to the following:

* **Webhook ID** `<:WEBHOOK_ID>` e.g. `1234567890`
* **Consumer key name** `<CONSUMER_KEY>` e.g. `xvz1evFS4wEEPTGEFPHBog`
* **Subscribing user's access token** `<SUBSCRIBING_USER'S_ACCESS_TOKEN>` e.g. `370773112-GmHxMAgYyLbNEtIKZeRNFsMKPR9EyMZeS9weJAEb`

```
      curl --request POST --url https://api.twitter.com/1.1/account_activity/webhooks/<:WEBHOOK_ID>/subscriptions/all.json --header 'authorization: OAuth oauth_consumer_key="<CONSUMER_KEY>", oauth_nonce="GENERATED", oauth_signature="GENERATED", oauth_signature_method="HMAC-SHA1", oauth_timestamp="GENERATED", oauth_token="<SUBSCRIBING_USER'S_ACCESS_TOKEN>", oauth_version="1.0"'
```

Code copied to clipboard

To view a list of all activity type subscriptions for a specified webhook, copy the following cURL request into your command line after making changes to the following:

* **Webhook ID** `<:WEBHOOK_ID>` e.g. `1234567890`
* **Bearer token** `<BEARER_TOKEN>` e.g. `AAAAAAAAAAAA0%2EUifi76ZC9Ub0wn...`

```
      curl --request GET --url https://api.twitter.com/1.1/account_activity/webhooks/<:WEBHOOK_ID>/subscriptions/all/list.json --header 'authorization: Bearer <BEARER_TOKEN>'
```

Code copied to clipboard

After deactivation, all events for the requesting user will no longer be sent to the webhook URL.  

To deactivate a subscription from the provided user context and application, copy the following cURL request into your command line after making changes to the following:

* **Webhook ID** `<:WEBHOOK_ID>` e.g. `1234567890`
* **Consumer key** `<CONSUMER_KEY>` e.g. `xvz1evFS4wEEPTGEFPHBog`
* **Subscribing user's access token** `<SUBSCRIBING_USER'S_ACCESS_TOKEN>` e.g. `370773112-GmHxMAgYyLbNEtIKZeRNFsMKPR9EyMZeS9weJAEb`

```
      curl --request DELETE --url https://api.twitter.com/1.1/account_activity/webhooks/:WEBHOOK_ID/subscriptions/all.json --header 'authorization: OAuth oauth_consumer_key="CONSUMER_KEY", oauth_nonce="GENERATED", oauth_signature="GENERATED", oauth_signature_method="HMAC-SHA1", oauth_timestamp="GENERATED", oauth_token="SUBSCRIBED_USER'S_ACCESS_TOKEN", oauth_version="1.0"'
```

Code copied to clipboard

Great job! You should now able to manage your webhooks and subscribed users.

### Referenced articles

* Overview of Challenge-Response Check (CRC)
* Account Activity Data Types
* Managing Webhooks and Subscriptions

Next Steps
----------

* Discover more about the Account Activity API
* Join the conversation on Twitter community forums
* Explore our sample code:  
	+ Enterprise Account Activity API dashboard, a node web app that displays webhook events using the enterprise tier of the Account Activity API and includes Replay functionality.

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