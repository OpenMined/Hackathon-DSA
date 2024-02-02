



Manage Direct Messages quick start | Docs | Twitter Developer Platform 





































































































Quick start



Getting started with the manage Direct Message endpoints
--------------------------------------------------------


This quick start guide will help you make your first request to the Direct Message endpoints using Postman, a tool for managing and making HTTP requests. To learn more about our Postman collections, please visit our Using Postman guide,


Please visit our Twitter API v2 sample code GitHub repository if you want to review Python-based examples. In addition, the official Twitter Developer Platform software development kits (SDKs) will be updated to support these Direct Message endpoints.  











### Prerequisites


To complete this guide, you will need to have a set of keys and tokens to authenticate your request. You can generate these keys and tokens by following these steps:


* Sign up for a developer account and receive approval.
* Create a Project and an associated developer App in the developer portal.
* Navigate to your App's “Keys and tokens” page to generate the required credentials. Make sure to save all credentials in a secure location.









### 


### Steps to building manage Direct Message requests


In this example, in one request, we'll create a new group conversation and add our first message to it. We'll then add a second message to the created conversation.


#### Step one: Start with a tool or library


To begin working with the manage Direct Message endpoints, we are going to use the Postman tool to simplify the process. A TwitterDev-authored collection of example Twitter API v2 requests will be used to explore six endpoints used to create new Direct Messages and to list Direct Message conversation events. 


While most of the collection is pre-filled, there are a few details that you'll need to provide that are based on the Twitter App created to host these API requests. First, let's get the collection loaded/updated.


To load the Twitter API v2 Postman collection into your environment, please click on the following button:





Add Twitter API v2 to Postman



Once you have the Twitter API v2 collection loaded in Postman, navigate to the “Manage Direct Messages” folder. This folder's Authorization tab has been pre-filled where possible, and you can update a few settings to share your Twitter App's authentication details. This folder also contains three endpoints for creating new Direct Messages. Note that there is also a "Direct Message lookup" folder with three available endpoints for retrieving Direct Message conversation events, including sending and receiving messages, and when conversation participants join and leave.. 


Since creating group conversations is an exciting new feature of the Twitter API v2, this example will focus on that. We will be working with the "New group DM and conversation" example. We will use this request to create a Direct Message group conversation.


The next step is to authenticate with the endpoint.


**Step two: Authenticate your request**  




To properly make a request to the Twitter API, you need to verify that you have permission to do so. To make a successful request to this endpoint, we will be using OAuth 2.0 Authorization Code Flow with PKCE. You can generate an access token within Postman. 


With Postman you can set the authentication method at the folder level or at the request level. Here we will be configuring the authentication details at the folder level.


Navigate to the "Manage Direct Messages" folder, select the "Authorization" tab and confirm that the Type to set to “OAuth 2.0,” and "Add auth data to" is set to "Request Headers." In the "Current Token" section, make sure the "header Prefix" is set to Bearer.  


To configure and generate a new token:


1. Create a Token Name, such as "Manage DMs."
2. Confirm that **Grant Type** is set to Authorization Code (with PKCE).
3. Set your **Callback URL**. You will want to update your Callback URL to exactly match the Callback URL associated with your application in the v2 Dev Portal. With the Twitter App used with this example, the Callback URL is set to - *https://www.example.com*.(Note that since this must match exactly, *https://example.com* would not work.)
4. Confirm that **Auth URL** is set to https://twitter.com/i/oauth2/authorize.
5. Confirm that **Access Token URL** is set to https://api.twitter.com/2/oauth2/token.**Client ID** - Copy and paste OAuth 2.0 client ID from the Developer Portal  

**Client Secret** - You will need this only if you are using an App type that is a confidential client. If so, copy and paste the OAuth 2.0 Client Secret from the Developer Portal.
6. Confirm that **Scope** is set to dm.read, dm.write, tweet.read, and users.read.
7. Confirm that **State** is set to “state.”
8. Confirm that **Client Authentication** is set to Send as Basic Auth header.
9. Click where it says **Get New Access Token**, click "Authorize app" as part of the "Sign-in with Twitter" process.
10. Click the "Proceed" button and then the "Use Token" to generate a token.
11. Click on the "Save" button to save these configuration details.


You may get a message that you are not logged into Twitter. If you get this error, you will need to log in to the Twitter account you are trying to post on behalf of inside of Postman.


Now that these OAuth 2.0 details have been set at the folder level, navigate to each of the examples and their "Authorization" tab and confirm that they have their Type set to "Inherit auth from parent." 


Note that this token will expire soon, and you'll need to regenerate it by clicking on the "Get New Access Token" button. Clicking that will trigger the "Sign-in with Twitter" process and generate a fresh token to make requests with.


#### Step three: Specify the Direct Message conversation participants and message contents


Navigate to the “Body” tab and make updates to the example JSON object. Set the participant\_ids attribute to the accounts you want to send the Direct Message to.












```

      {
   "message": {"text": "Hello to just you two, this is a new group conversation."},
   "participant_ids": ["944480690","906948460078698496"],
   "conversation_type": "Group"       
}

    
```






#### Step four: Make your request and review the response


Once you have everything set up, hit the "Send" button, and you will receive a similar response to the example response below. A reminder that if your token has expired since you created it above, you can return to the folder's Authorization tab and click on the "Get New Access Token" to create a fresh token.












```

      {
   "data": {
       "dm_conversation_id": "1582103724607971328",
       "dm_event_id": "1582103724607971332"
   }
}

    
```






If the returned response "data" object contains a dm\_conversation\_id and an dm\_event\_id, you have successfully created a new Direct Message conversation. To start looking up events associated with this conversation, head over to the Direct Message lookup Quick start guide.


#### Step five: Add another message to that group conversation


Now select the "Add DM to conversation" example, and select the "Params" tab. Under "Path Variables" , update the dm\_conversation\_id to the ID of the conversation you created above.




|  |  |
| --- | --- |
| **Key** | **Value** |
| dm\_conversation\_id | 1582103724607971328 |


Using this conversation ID, the request path will resolve to: https://api.twitter.com/2/dm\_conversations/1582103724607971328/messages


Also, update the "Body" tab with request JSON containing the message text you want to send: 












```

      {
   "text": "Adding a new message to our group conversation..."
}

    
```






Once you have everything set up, hit the "Send" button, and you will receive a similar response to the following example response:












```

      {
   "data": {
       "dm_conversation_id": "1582103724607971328",
       "dm_event_id": "1582106224379559940"
   }
}
    
```










Next steps
----------






API Reference


Get support


Sample code



















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















