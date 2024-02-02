



Manage Direct Messages introduction | Docs | Twitter Developer Platform 





































































































Introduction






Introduction
------------


Direct Messages enable private conversations on Twitter. Direct Messages are one of the most popular features of Twitter, with a wide variety of use cases. These use cases range from group chats among friends, to powering customer support for brands around the world. New v2 versions of Direct Messages endpoints will be introduced in stages, and this first stage includes fundamental endpoints for creating Direct Messages and listing Direct Message conversation events. For the first time, the Twitter API v2 supports *group* conversations.


This initial release of Manage Direct Messages includes three POST methods for creating Direct Messages:


* **POST /2/dm\_conversations/with/:participant\_id/messages** - Creates a one-to-one Direct Message. This method either creates a new 1-1 conversation or retrieves the current conversation and adds the Direct Message to it. The :participant\_idpath parameter is the User ID of the account receiving the message.
* **POST /2/dm\_conversations** - Creates a new group conversation and adds a Direct Message to it. These requests require a list of conversation participants. Note that you can create multiple conversations with the same participant list. These requests will always return a new conversation ID.
* **POST /2/dm\_conversations/:dm\_conversation\_id/messages** - Creates a Direct Message and adds it to an existing conversation. The :dm\_conversation\_id path parameter is the ID of the conversation that the message will be added to.


 


Note that Direct Message event IDs are common across the v1.1 and v2 (as well as the Twitter App), so the v1.1 methods to hide/delete Direct Messages can be used along with this new v2 endpoint. Also note that the Enterprise and Premium Account Activity APIs support v2 one-to-one messages, but do not yet support group conversations.     




There is a user rate limit of 200 requests per 15 minutes for the POST method. There is also a rate limit of 1000 requests per 24 hours per user. Additionally, there is a rate limit of 15000 requests per 24 hours. Note that these rate limits are shared across these POST endpoints.


Since you are making requests on behalf of a user with the manage Tweets endpoints, you must authenticate with either OAuth 1.0a User Context or OAuth 2.0 Authorization Code with PKCE, and use a user Access Tokens associated with a user that has authorized your App. To generate this user Access Token with OAuth 1.0a, you can use the 3-legged OAuth flow. To generate a user Access Token with OAuth 2.0, you can use the Authorization Code with PKCE grant flow.  













**Account setup**


To access these endpoints, you will need:


* An approved developer account.
* To authenticate using the keys and tokens from a developer App that is located within a Project.


Learn more about getting access to the Twitter API v2 endpoints in our getting started guide.












Quick start


Sample code


Run in Postman


Try with API Explorer

















Supporting resources
--------------------






Learn how to use Postman


Troubleshoot an error


API Reference





























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















