



Managing webhooks and subscriptions | Docs | Twitter Developer Platform 





































































































Managing webhooks and subscriptions



Managing webhooks and subscriptions
-----------------------------------


### Creating & changing webhooks


In order to change webhook URLs, you must delete your existing webhook and then create a new one. Note that when you do this, you will be required to re-add user subscriptions to the new webhook.


#### Webhook configuration management endpoints:




|  |  |
| --- | --- |
| **Method** | Enterprise |
| Registers a webhook URL / Generates a webhook\_id | POST webhooks |
| Returns all webhook URLs and their statuses | GET webhooks |
| Delete app’s current webhook configuration | DELETE webhooks/:webhook\_id              |
| Manually trigger a CRC request | PUT webhooks/:webhook\_id |


 


#### Why can’t I just update the webhook URL?


Why are webhook configurations immutable? Twitter takes security very seriously. If your webhook URL is changed, there is a possibility that your application consumer key and consumer secret have been compromised. By requiring you to create a new webhook configuration, you are also required to re-subscribe to your user’s events. This requires the use of access tokens that a malicious party is less likely to possess. As a result, the likelihood that another party will receive your user’s private information is reduced.  

 


### Adding & removing User subscriptions


Support for thousands of subscriptions is available with the enterprise tier. If you already have an account manager, please reach out to them with questions.  To apply for access to the enterprise APIs, click here.   




#### Subscription management endpoints




|  |  |
| --- | --- |
| Method | Enterprise |
| Add new user subscription | POST webhooks/:webhook\_id/subscriptions/all |
| Retrieve a user subscription | GET webhooks/:webhook\_id/subscriptions/all |
| Returns a list of all active subscriptions | GET webhooks/:webhook\_id/subscriptions/all/list |
| Deactivates a user subscription using application only OAuth | DELETE webhooks/:webhook\_id/subscriptions/:user\_id/all.json |


### 


### Next steps


* Learn more about these topics:
	+ Securing your webhook.
	+ Authenticating users.
	+ Webhook event retries.
	+ Webhook JSON payload examples.
* See Account Activity API references.
* See example code:
	+ Premium Account Activity API dashboard, a node web app that displays webhook events.
	+ The SnowBot chatbot, a Ruby web app built with the Account Activity and Direct Message APIs. This code base includes a script to help set up Account Activity API webhooks.


#### 



















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















