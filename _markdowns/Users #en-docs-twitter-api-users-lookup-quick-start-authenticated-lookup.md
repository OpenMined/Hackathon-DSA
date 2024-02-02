



Authenticated user lookup quick start guide | Docs | Twitter Developer Platform 





































































































Authenticated user lookup



Getting started with the Authenticated User Lookup endpoint
-----------------------------------------------------------


This quick start guide will help you make your first request to the authenticated user lookup endpoint using Postman.


Please visit our Twitter API v2 sample code GitHub repository if you want to see sample code in different languages.











### Prerequisites


To complete this guide, you will need to have a set of keys and tokens to authenticate your request. You can generate these keys and tokens by following these steps:


* Sign up for a developer account and receive approval.
* Create a Project and an associated developer App in the developer portal.
* Navigate to your App's “Keys and tokens” page to generate the required credentials. Make sure to save all credentials in a secure location.










### Steps to build an authenticated user lookup request


#### Step one: Start with a tool or library


There are several different tools, code examples, and libraries that you can use to make a request to this endpoint, but we will use the Postman tool here to simplify the process.


 


To load the Twitter API v2 Postman collection into your environment, please click on the following button:





Add Twitter API v2 to Postman



 


Once you have the Twitter API v2 collection loaded in Postman, navigate to the “Authenticated User Lookup” folder, and select “Lookup an Authenticated User”.


#### 


#### Step two: Authenticate your request


To properly make a request to the Twitter API, you need to verify that you have permission. To do so with this endpoint, you must authenticate your request using either OAuth 1.0a User Context or OAuth 2.0 Authorization Code with PKCE.


In this example, we are going to use OAuth 1.0a User Context.


You must add your keys and tokens – specifically your API Key, API Secret Key, OAuth 1.0a user Access Token, and OAuth 1.0a user Access Token Secret – to Postman. You can do this by selecting the environment named “Twitter API v2” in the top-right corner of Postman and adding your keys and tokens to the "initial value" and "current value" fields (by clicking the eye icon next to the environment dropdown).


These variables will automatically be pulled into the request's authorization tab if you've done this correctly.  

 


Step three: Determine which user fields you want to retrieve  




If you click the "Send" button after step three, you will receive the default user object fields in your response: id, name, and username.


If you would like to receive additional fields beyond id, name, and username, you will have to specify those fields in your request with the field and/or expansion parameters.


For this exercise, we will request three additional sets of fields from different objects:


1. The additional user.created\_at field in the primary user objects.
2. The associated pinned Tweets’ object’s default fields for the returned users: id and text.
3. The additional tweet.created\_at field in the associated Tweet objects.


 


In Postman, navigate to the "Params" tab and add the following key:value pair to the "Query Params" table:




|  |  |  |
| --- | --- | --- |
| **Key** | **Value** | **Returned fields** |
| user.fields | created\_at | user.created\_at |
| expansions | pinned\_tweet\_id | includes.tweets.id,
 includes.tweets.text |
| tweet.fields | created\_at, author\_id | includes.tweets.created\_at, includes\_tweets.author\_id |


You should now see a similar URL next to the “Send” button:












```

      https://api.twitter.com/2/users/me?user.fields=created_at&expansions=pinned_tweet_id&tweet.fields=author_id,created_at
    
```





Code copied to clipboard












Next steps
----------






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















