



User Streams and Site Streams migration guide | Docs | Twitter Developer Platform 





































































































User Streams and Site Streams migration guide



 
Migration Guide: Moving from User Streams/Site Streams to Account Activity API
------------------------------------------------------------------------------


**As of August 23rd, 2018, we retired both Site Streams and User Streams. Please make sure to migrate over to the Account Activity API.**


**Please review this announcement to learn more.**



This guide is designed to help you migrate from legacy User Streams and Site Streams APIs to their replacement, the Account Activity API. Below you will find a summary of the changes, new features list, as well as key differences and considerations to help with the transition. For guidance in migrating from basic DM endpoints, please refer to the Direct Message migration guide.  




### Summary of changes


The Account Activity API will deliver you events for authenticated and subscribed accounts via webhooks as opposed to a streaming connection like with User Streams and Site Streams.


#### Deprecated APIs


GET user  

  

GET site  (including control streams: GET site/c/:stream\_id,  GET site/c/:stream\_id/info.json,  GET site/c/:stream\_id/friends/ids.json,  POST site/c/:stream\_id/add\_user.json,  POST /site/c/:stream\_id/remove\_user.json)


#### Replacement APIs


Enterprise Account Activity API - All Activities


Premium Account Activity API - All Activities


### Differences & migration considerations


**API format:** The new Account Activity API operates differently than User Streams and Site Streams. You will need to alter your web app to receive data with webhooks. You can find more information on webhooks here.


**Data Available:** Another key difference you will notice is in regards to the data being delivered. Twitter will no longer send events from people that you follow on Twitter (aka your home timeline). This was an intentional change and is not something we plan to alter going forward.


**Reliability:** Unlike streaming, webhooks enable confirmation of delivery and options to retry POSTed activities that do not make it to the webhook URL.  This gives more assurance that the app is receiving all applicable activities, even if there are brief disconnections or periods of downtime.  

  




### New features


The Account Activity API offers many new features, most notably that data is now delivered via webhooks as opposed to streaming. Webhooks offer many benefits compared to streaming, but the most prominent are speed and reliability. The API will send you data in the form of JSON events as they become available and you will no longer need to maintain an active connection or poll the endpoint. This limits the need for redundancy features and increases efficiency overall. More information on webhooks can be found in the technical documentation.  

  




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


The Twitter app currently used for User Streams or Site Streams will be listed for the owning user within the developer portal. This Twitter app can also be used for Account Activity API to retain authorized users for that application.  A new app can also be created, and users can be re-authorized for this new app if desired.  If you are creating a new app on behalf of a business, it is recommended that you create the app with a corporate Twitter @handle account.


* Enable “Read, Write and Access direct messages” on the permissions tab of your Twitter app page.   

\*Note that changing these settings is not retroactive, any authorized users will keep the authorization settings from the time at which they were authorized. If a user has not already given you read, write and direct message access, you will need to have that user re-authorize your application.
* If you are unfamiliar with Twitter Sign-in and how user contexts work with the Twitter API review Obtaining Access Tokens.
* Generate access tokens for the Twitter app owner at the bottom of the “Keys and Tokens” tab. On this same tab take note of your Consumer Key, Consumer Secret, Access Token and Access Token Secret. You will need these to use the API.
* Generate a bearer token using your Consumer Key and Consumer Secret for application-only API methods.


 


**Step 3: Setup & Configure Your Webhooks**


* Create a web app with an endpoint to use as your webhook to receive events (e.g. https://your\_domain.com/webhook/twitter or https://webhooks.your\_domain.com).
* Use your Consumer Key, Consumer Secret, Access Token and Access Token Secret when creating your webhook, Note that your endpoint must return a JSON response with a response\_token that is a base64 encoded HMAC SHA-256 hash created from the crc\_token and your app Consumer Secret.
* Review Securing Webhooks documentation taking special note of the Challenge Response Check (CRC) requirements.
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
* Set up your new Account Activity API subscriptions using the request:  *POST account\_activity/all/:env\_name/subscriptions*
* Confirm your Account Activity API subscriptions using the request:  *GET account\_activity/all/:env\_name/subscriptions/list*


Converting to the Account Activity API from Site Streams: (using control streams):


* Generate a list of your current subscriptions on Site Streams using the request:  *GET /1.1/site/c/:stream\_id/info.json*
* Set up your new Account Activity API subscriptions using the request:  *POST account\_activity/all/:env\_name/subscriptions*
* Confirm your Account Activity API subscriptions using the request:  *GET account\_activity/all/:env\_name/subscriptions/list*


Registering a Webhook and Creating Subscriptions (not migrating from Site Streams or User Streams)


* Register your webhook URL with your app using POST webhooks and receive a webhook\_id.
* Use the returned webhook\_id to add user subscriptions with POST webhooks/:webhook\_id/subscriptions/all.


 


### The Account Activity dashboard (sample Account Activity API application)


We've created a sample app to make testing the Account Activity API a little quicker:   


* Download the Account Activity Dashboard sample application here (it uses Node.js)
* Follow the instructions on the README to install and launch the app
* Once the application has been launched, you can use the UI to easily set up your webhook and create a new subscription


 


### Available Activities




| Message Type | Details |
| --- | --- |
| tweet\_create\_events | Tweet status payload when any of the following actions are taken by or to the subscription user: Tweets, Retweets, Replies, @mentions, QuoteTweets |
| favorite\_events | Favorite (like) event status with the user and target. |
| follow\_events | Follow event with the user and target. |
| block\_events | Block event with the user and target. |
| mute\_events | Mute event with the user and target. |
| direct\_message\_events | Direct message status with the user and target. |
| direct\_message\_indicate\_typing\_events | Direct message typing event with the user and target. |
| direct\_message\_mark\_read\_events | Direct message read event with the user and target. |


 


### Deprecated streaming message types




|  |  |
| --- | --- |
| Blank lines | Blank lines will no longer be delivered in the Account Activity API as they were used as keep-alive messages in User Streams and Site Streams. |
| Limit notices | Limit notices will no longer be sent to a given webhook.  Instead, users can call the API to get current usage of available handles. This will be included in the developer portal at some time in the future. |
| Disconnect messages | Disconnect notices will no longer be necessary as webhooks do not rely on an active connection. |
| Stall warnings | Stall warnings will no longer be necessary as webhooks do not rely on an active connection being able to handle large numbers of incoming messages. |
| Friends list | Friends lists will no longer be sent proactively. There will now be a REST endpoint to get this information. |


 


### Deprecated event types




|  |  |  |  |  |
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
| User updates their protected status | user\_update | Current user | Current user | Null
 |




















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















