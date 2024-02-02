



Hide replies quick start guide | Docs | Twitter Developer Platform 





































































































Quick start



Getting started with the hide replies endpoint
----------------------------------------------


This quick start guide will help you make your first request to the hide replies endpoint using Postman.


If you would like to see some code snippets in different languages, please visit the hide replies API Reference page. 











### Prerequisites


To complete this guide, you will need to have a set of keys and tokens to authenticate your request. You can generate these keys and tokens by following these steps:


* Sign up for a developer account and receive approval.
* Create a Project and an associated developer App in the developer portal.
* Navigate to your App's “Keys and tokens” page to generate the required credentials. Make sure to save all credentials in a secure location.










### Steps to build a PUT /tweets/:id/hidden request


#### Step one: Start with a tool or library


There are several different tools, code examples, and libraries that you can use to make a request to this endpoint, but we are going to use the Postman tool here to simplify the process.


To load Twitter API v2 Postman collection into your environment, please click on the following button:





Add Twitter API v2 to Postman



Once you have the Twitter API v2 collection loaded in Postman, navigate to the hide replies endpoint.
-----------------------------------------------------------------------------------------------------


#### 
Step two: Authenticate your request


To properly make a request to the Twitter API, you need to verify that you have permission. To do so with this endpoint, you must authenticate your request using either OAuth 1.0a User Context or OAuth 2.0 Authorization Code with PKCE.


In this example, we are going to use OAuth 1.0a User Context.


You must add your keys and tokens – specifically your API Key, API Secret Key, OAuth 1.0a user Access Token, and OAuth 1.0a user Access Token Secret – to Postman. You can do this by selecting the environment named “Twitter API v2” in the top-right corner of Postman and adding your keys and tokens to the "initial value" and "current value" fields (by clicking the eye icon next to the environment dropdown).


These variables will automatically be pulled into the request's authorization tab if you've done this correctly.  

 


#### Step three: Find a Tweet ID to hide


The hide replies endpoint can hide or unhide replies on behalf of an authorized user. Because we are using the Access Tokens related to your user profile in this example, you will be able to hide replies from users who participate in a conversation started by you. Similarly, if you were using Access Tokens that belong to another user that authorized your app, you would be able to moderate replies to any conversations started by that account.


Ask a friend to reply to a Tweet (let them know you're testing hide replies) or reply to any of your Tweets from a test account. Click on that reply, then copy the numeric part of its URL. That will be the Tweet ID we will hide.


In this case, we will be looking at the following Tweet, which has the ID `1232720193182412800`:


`https://twitter.com/TwitterDev/status/1232720193182412800`


#### 
Step four: Hide the Tweet


In Postman, open the Hide replies folder and select Hide a reply. In the Params tab, paste the Tweet ID next to the id field (you won't need to replace :id in the URL). Click "Send" and you will see a successful response.












```

      {"hidden":true}
    
```





Code copied to clipboard








#### 


#### Step five: Unhide the Tweet


Hidden Tweets are moved to a separate tab in the Twitter app. To unhide a tweet in Postman, open the Hide replies folder and select Unhide a reply. In the Params tab, paste the same Tweet ID used in the previous step next into the id field. Click "Send" and you will see a successful response.












```

      {"hidden":false}
    
```





Code copied to clipboard








  

The hidden field represents the hidden status of the Tweet. A hidden status of true means the Tweet is hidden. Similarly, false means the Tweet is not hidden.










Next steps
----------






Learn how to manage replies in realtime


Learn how to manage replies by topic


Customize your request using the API Reference


Reach out to the community for help



















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















