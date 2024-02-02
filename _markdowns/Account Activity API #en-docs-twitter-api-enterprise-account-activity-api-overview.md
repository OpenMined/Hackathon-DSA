



Account Activity API | Twitter API | Docs | Twitter Developer Platform 





































































































Overview








This endpoint has been updated to include Tweet edit metadata. Learn more about these metadata on the "Edit Tweets" fundamentals page. 


 


This endpoint is often used with the Direct Messages endpoints. We have launched new v2 Direct Messages endpoints. Note that the Enterprise and Premium Account Activity APIs support v2 one-to-one messages, but do not yet support group conversations.     











Overview
--------


Enterprise


The Account Activity API provides you the ability to subscribe to realtime activities related to a user account via webhooks. This means that you can receive realtime Tweets, Direct Messages, and other account events from one or more of your owned or subscribed accounts through a single connection.


You will receive all related activities below for each user subscription on your webhook registration:




| Activity types |
| --- |
| * Tweets (by user)
* Tweet deletes (by user)
* @mentions (of user)
* Replies (to or from user)
* Retweets (by user or of user)
* Quote Tweets (by user or of user)
* Retweets of Quoted Tweets (by user or of user)
* Likes (by user or of user)
* Follows (by user or of user)
* Unfollows (by user)
 | * Blocks (by user)
* Unblocks (by user)
* Mutes (by user)
* Unmutes (by user)
* Direct Messages sent (by user)
* Direct Messages received (by user)
* Typing indicators (to user)
* Read receipts (to user)
* Subscription revokes (by user)
 |


**Please note** - We do not deliver home timeline data via the Account Activity API. Please use the GET statuses/home\_timeline to pull this data.  

 


#### Video Series


Check out our four-part video series on the Account Activity API to get up to speed!







> Today we announced the Account Activity API is generally available as a premium and enterprise API. 🔔 pic.twitter.com/xnlF9kPevi
> 
> — Twitter Dev (@TwitterDev) May 16, 2018






 


### Feature summary




| Tier | Pricing | Number of unique subscriptions | Number of webhooks | Reliability and Activity Recovery |
| --- | --- | --- | --- | --- |
| Enterprise | Contact sales | Up to 500+ | 3+ | Retries and Replay |


 






Next steps
----------


* Apply for access and get started with webhooks.
* Check out our API references to find the right endpoint for the job.
* Follow this step-by-step tutorial on how to get started with the Account Activity API.
* Follow this step-by-step tutorial on how to build a customer engagement application on Twitter.
* Have questions? Running into errors?
	+ Read our Frequently asked questions or Error Troubleshooting guide.
* Explore our sample code:  

	+ Enterprise Account Activity API dashboard, a node web app that displays webhook events using the enterprise tier of the Account Activity API and includes Replay functionality.
	+ The SnowBot chatbot, a Ruby web app built on the enterprise Account Activity and Direct Message APIs.



















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















