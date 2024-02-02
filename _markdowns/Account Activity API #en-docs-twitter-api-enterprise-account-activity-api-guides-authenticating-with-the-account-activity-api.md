



Authenticating with the Account Activity API | Docs | Twitter Developer Platform 





































































































Authenticating with the Account Activity API








**Please note**: 


Twitter needs to enable access to the Account Activity API for your developer App before you can start using the API. To this end, make sure to share the App ID that you intend to use for authentication purposes with your account manager or technical support team.









The Account Activity API consists of a set of endpoints that allow you to create and manage user subscriptions to receive real-time account activities for all of your subscribed accounts through a single connection. 


There are two authentication methods available with the Account Activity API (OAuth 1.0a and OAuth 2.0 Bearer Token). The authentication method that you should use will depend on which endpoint you are using.






 




|  |  |  |  |
| --- | --- | --- | --- |
| **Description** | **Endpoint** | OAuth 1.0a
(user context) | OAuth 2.0 Bearer Token (application-only) |
| Register a new webhook URL for the given application context | POST account\_activity/webhooks | ✓ |  |
| Return all URLs and their statuses for the given application | GET account\_activity/webhooks |  | ✓ |
| Trigger a challenge response check (CRC) for a given webhook's URL | PUT account\_activity/webhooks/:webhook\_id | ✓ |  |
| Subscribe the application to a user’s account events | POST account\_activity/webhooks/:webhook\_id/subscriptions/all | ✓ \* |  |
| Return a count of currently active subscriptions | GET account\_activity/subscriptions/count |  | ✓ |
| Check if a webhook configuration is subscribed to a user’s events | GET account\_activity/webhooks/:webhook\_id/subscriptions/all | ✓ \* |  |
| Return a list of currently active subscriptions | GET account\_activity/webhooks/:webhook\_id/subscriptions/all/list |  | ✓ |
| Delete a webhook | DELETE account\_activity/webhooks/:webhook\_id | ✓ |  |
| [DEPRECATED] Deactivate a subscription for the provided user context and application | DELETE account\_activity/webhooks/:webhook\_id/subscriptions/all | ✓ \* |  |
| Deactivate a subscription using application-only OAuth | DELETE /account\_activity/webhooks/:webhook\_id/subscriptions/:user\_id/all.json |  | ✓ |
| Redelivers activities to a webhook | POST /1.1/account\_activity/replay/webhooks/:webhook\_id/subscriptions/all.json |  | ✓ |


\**Authentication requires the access tokens of the subscribing user.*






 


For those endpoints that require OAuth 1.0a user context authentication, you will need to provide the following credentials to authenticate the request: 


* Consumer Keys (API Key and Secret)
* Access Tokens (Access Token and Secret)


 


In the case of the following three endpoints, you perform write actions within the context of your application (no Twitter users are involved). Therefore, the Access Tokens you need to provide are the ones belonging to your developer App. These can be generated directly from within the developer portal, under the “Keys and tokens” tab for your App.  


* POST account\_activity/webhooks: Register a new webhook URL for the given application context
* PUT account\_activity/webhooks/:webhook\_id: Trigger a challenge response check (CRC) for a given webhook's URL
* DELETE account\_activity/webhooks/:webhook\_id: Delete a webhook


 


On the other hand, in the case of the following three endpoints, you are making a request that allows your application to access protected data on behalf of a Twitter user (for example, Direct Messages). You must therefore provide the Access Tokens that belong to the subscribing user in question. The required Access tokens can be obtained using the 3-legged OAuth flow (see OAuth 1.0a: how to obtain a user’s Access Tokens). These endpoints have been marked with an asterisk in the above table (\*).


* POST account\_activity/webhooks/:webhook\_id/subscriptions/all: Subscribe the application to a user’s account events
* GET account\_activity/webhooks/:webhook\_id/subscriptions/all: Check if a webhook configuration is subscribed to a user’s events
* DELETE account\_activity/webhooks/:webhook\_id/subscriptions/all: Deactivate a subscription for the provided user context and application [DEPRECATED]











**Please note**: 


Make sure that your developer App is enabled for "Read, Write, and Direct Messages." You can change this setting in the Projects & Apps section of your developer account, under “App permissions” for the selected developer App. You will need to regenerate your App credentials after changing the permissions settings.









A list of all endpoints available with the Account Activity API, including associated description and example cURL requests with authentication implementation examples, can be found inthe API reference documentation.


For additional information, check out TwitterDev’s sample web app and helper scripts to get started with the Enterprise Account Activity API.


 






### Next steps


* See our Managing your webhooks and adding subscriptions for more information on adding Account Activity subscrptions.
* Learn more about these topics:
	+ Securing your webhook.
	+ Webhook JSON payload examples.
* See Account Activity API references.
* Learn more about Twitter authentication.
* See example code:
	+ The SnowBot chatbot, a Ruby web app built with the Account Activity and Direct Message APIs.



















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















