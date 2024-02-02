



Quick start | Docs | Twitter Developer Platform 





































































































Quick start



Getting started with the Spaces lookup endpoints
------------------------------------------------


This quick start guide will help you make your first request to one of the Spaces lookup endpoints with a set of specified fields using Postman.


If you would like to see sample code in different programming languages, please visit our Twitter API v2 sample code GitHub repository.  













### Prerequisites


To complete this guide, you will need to have a set of keys and tokens to authenticate your request. You can generate these keys and tokens by following these steps:


* Sign up for a developer account and receive approval.
* Create a Project and an associated developer App in the developer portal.
* Navigate to your App's “Keys and tokens” page to generate the required credentials. Make sure to save all credentials in a secure location.









 
### Steps to build a Spaces lookup request


*For this example, we will make a request to the user Spaces lookup by creator ID endpoint, but you can apply the learnings from this quick start to other lookup requests as well.*


**Step one: Start with a tool or library**


There are several different tools, code examples, and libraries that you can use to make a request to this endpoint, but we are going to use the Postman tool here to simplify the process.


To load Twitter API v2 Postman collection into your environment, please click on the following button:


 





Add Twitter API v2 to Postman



Once you have the Twitter API v2 collection loaded in Postman, navigate to the Spaces folder and find the "Lookup Spaces created by one or more users" request.  

 


**Step two: Authenticate your request**


To properly make a request to the Twitter API, you need to verify that you have permission. To do so, this endpoint requires you to authenticate your request with either OAuth 2.0 App-Only or OAuth 2.0 Authorization Code with PKCE authentication methods.


For simplicity's sake, we will utilize OAuth 2.0 App-Only with this request, but you will need to use one of the other authentication methods if you'd like to request private metrics or Spaces from a private user. 


To utilize OAuth 2.0 App-Only, you must add your keys and tokens, specifically the App Access Token (also known as the App-only Bearer Token) to Postman. You can do this by selecting the environment named “Twitter API v2” in the top-right corner of Postman and adding your keys and tokens to the "initial value" and "current value" fields (by clicking the eye icon next to the environment dropdown).


These variables will automatically be pulled into the request's authorization tab if you've done this correctly.  

 


**Step three: Identify and specify which user from which you would like to retrieve Tweets**


You must specify a user you would like to retrieve live or upcoming Spaces for within the request. In this example, we will be passing a single user ID.


User IDs are simply the numerical value that represents an account handle that you can find within an account's profile URL. For example, the following account’s username is TwitterDev.


https://twitter.com/TwitterDev


To convert this username to the user ID, you will have to use the user lookup endpoint with the username and find the numerical user ID in the payload. In the case of @TwitterDev, the user ID is 2244994945.


In Postman, navigate to the "Params" tab and enter this user ID into the "Value" column of the id parameter.




|  |  |
| --- | --- |
| **Key** | **Value** |
| id | 2244994945 |


 


#### Step four: Identify and specify which fields you would like to retrieve


If you click the "Send" button after step three, you will receive an id, which is the only Space object field returned by default in your response.


If you would like to receive additional fields, you will have to specify them in your request with the space.fields or expansions parameters.


For this exercise, we will requested three additional sets of fields from different objects:


* The additional title field in the primary Spaces object.
* The full user object of the specified creator ID
* The additional user.created\_at field in the associated user object.


 



In Postman, navigate to the “Params” tab and add the following key:value pair to the “Query Params” table:


 




|  |  |  |
| --- | --- | --- |
| **Key** | **Value** | **Returned fields** |
| space.fields | title | creator\_id |
| expansions | creator\_id | includes.users.id, includes.users.name, includes.users.username |
| user.fields | created\_at | includes.users.created\_at |


 


You should now see the following URL next to the “Send” button:


https://api.twitter.com/2/spaces/by/creator\_ids?user\_ids=2244994945&space.fields=creator\_id&expansions=creator\_id&user.fields=created\_at


 






 **Step five: Make your request and review your response**


Once you have everything set up, hit the “Send” button and you will receive the following response:












```

      {
   "data": [
    {
        "creator_id": "2244994945",
        "id": "1zqKVXPQhvZJB",
        "title": "Hello world 👋",
        "state": "Running"
   },
   "includes": {
       "users": [
           {
               "created_at": "2013-12-14T04:35:55.000Z",
               "name": "Twitter Dev",
               "id": "2244994945",
               "username": "TwitterDev"
           }
       ]
   }
]
}

    
```





Code copied to clipboard














Next steps
----------






Customize your request using the API Reference





























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















