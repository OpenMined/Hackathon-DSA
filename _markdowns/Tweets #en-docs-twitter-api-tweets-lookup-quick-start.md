



Tweets lookup quick start guide | Docs | Twitter Developer Platform 





































































































Quick start



Getting started with the Tweets lookup endpoints
------------------------------------------------


This quick start guide will help you make your first request to the Tweets lookup endpoints with a set of specified fields using Postman.


If you would like to see sample code in different languages, please visit our Twitter API v2 sample code GitHub repository. 











### Prerequisites


To complete this guide, you will need to have a set of keys and tokens to authenticate your request. You can generate these keys and tokens by following these steps:


* Sign up for a developer account and receive approval.
* Create a Project and an associated developer App in the developer portal.
* Navigate to your App's “Keys and tokens” page to generate the required credentials. Make sure to save all credentials in a secure location.









### 


### Steps to build a GET /tweets request


#### Step one: Start with a tool or library


There are several different tools, code examples, and libraries that you can use to make a request to this endpoint, but we are going to use the Postman tool here to simplify the process.


To load Twitter API v2 Postman collection into your environment, please click on the following button:





Add Twitter API v2 to Postman



  

Once you have the Twitter API v2 collection loaded in Postman, navigate to the "Tweet Lookup > Multiple Tweets" request.  

 


#### Step two: Authenticate your request


To properly make a request to the Twitter API, you need to verify that you have permission. To do this with this endpoint, you must authenticate your request with either OAuth 2.0 App-Only, OAuth 2.0 Authorization Code with PKCE, or OAuth 1.0a User Context authentication methods.


For simplicity's sake, we are going to utilize OAuth 2.0 App-Only with this request, but if you'd like to request private metrics or Tweets, you will need to use one of the other authentication methods. 


To utilize OAuth 2.0 App-Only, you must add your keys and tokens (and specifically theApp Access Token, also known as the App-only Bearer Token) to Postman by selecting the environment named “Twitter API v2” (in the top-right corner of Postman), and adding your keys and tokens to the "initial value" and "current value" fields (by clicking the eye icon next to the environment dropdown).


If you've done this correctly, these variables will automatically be pulled into the request's authorization tab.  

 




#### Step three: Identify and specify which Tweets you would like to retrieve


You must specify a Tweet or a set of Tweets that you would like to receive within the request. You can find the Tweet ID by navigating to twitter.com and clicking on a Tweet and then looking in the URL. For example, the following URL's Tweet ID is `1228393702244134912`.


`https://twitter.com/TwitterDev/status/1228393702244134912`


In Postman, navigate to the "Params" tab and enter this ID, or a string of Tweet IDs separated by a comma, into the "Value" column of the `ids` parameter.




|  |  |
| --- | --- |
| **Key** | **Value** |
| `ids` | `1228393702244134912,``1227640996038684673,``1199786642791452673` |


 


#### Step four: Identify and specify which fields you would like to retrieve


If you click the "Send" button after step three, you will receive the default Tweet object fields in your response: id, text, and edit\_history\_tweet\_ids. 


 


If you would like to receive additional fields beyond id , text, and edit\_history\_tweet\_ids, you will have to specify those fields in your request with the field and/or expansion parameters.


For this exercise, we will request a three additional different sets of fields from different objects:


1. The additional tweet.created\_at field in the primary user objects.
2. The associated authors’ user object’s default fields for the returned Tweets: id, name, and username
3. The additional  user.created\_at field in the associated user objects.


In Postman, navigate to the "Params" tab and add the following key:value pair to the "Query Params" table:  






|  |  |  |
| --- | --- | --- |
| **Key** | **Value** | **Returned fields** |
| `tweet.fields` | `created_at` | `tweets.created_at` |
| `expansions` | `author_id` | `includes.users.id`, `includes.users.name`, `includes.users.username` |
| `user.fields` | `created_at` | `includes.users.created_at` |


You should now see the following URL next to the "Send" button:












```

      https://api.twitter.com/2/tweets?ids=1228393702244134912,1227640996038684673,1199786642791452673&tweet.fields=created_at&expansions=author_id&user.fields=created_at
    
```





Code copied to clipboard








#### 
Step five: Make your request and review your response


Once you have everything set up, hit the "Send" button and you will receive the following response:












```

      {
  "data": [
    {
      "author_id": "2244994945",
      "created_at": "2020-02-14T19:00:55.000Z",
      "id": "1228393702244134912",
      "edit_history_tweet_ids": ["1228393702244134912"],
      "text": "What did the developer write in their Valentine’s card?\n  \nwhile(true) {\n    I = Love(You);  \n}"
    },
    {
      "author_id": "2244994945",
      "created_at": "2020-02-12T17:09:56.000Z",
      "id": "1227640996038684673",
      "edit_history_tweet_ids": ["1227640996038684673"],
      "text": "Doctors: Googling stuff online does not make you a doctor\n\nDevelopers: https://t.co/mrju5ypPkb"
    },
    {
      "author_id": "2244994945",
      "created_at": "2019-11-27T20:26:41.000Z",
      "id": "1199786642791452673",
      "edit_history_tweet_ids": ["1199786642791452673"],
      "text": "C#"
    }
  ],
  "includes": {
    "users": [
      {
        "created_at": "2013-12-14T04:35:55.000Z",
        "id": "2244994945",
        "name": "Twitter Dev",
        "username": "TwitterDev"
      }
    ]
  }
}

    
```










Next steps
----------






Customize your request using the API Reference


Learn how to measure Tweet performance


Get support


Check out some sample code for these endpoints



















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















