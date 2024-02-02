



Retweets lookup quick start guide | Docs | Twitter Developer Platform 





































































































Retweets lookup quick start



Getting started with the Retweets lookup endpoint
-------------------------------------------------


This quick start guide will help you make your first request to the Retweets lookup endpoint using Postman. If you would like to see sample code in different languages, please visit our Twitter API v2 sample code GitHub repository.  













### Prerequisites


To complete this guide, you will need to have a set of keys and tokens to authenticate your request. You can generate these keys and tokens by following these steps:


* Sign up for a developer account and receive approval.
* Create a Project and an associated developer App in the developer portal.
* Navigate to your App's “Keys and tokens” page to generate the required credentials. Make sure to save all credentials in a secure location.









 
### Steps to build a Retweets lookup request


#### Step one: Start with a tool or library


There are several different tools, code examples, and libraries that you can use to make a request to this endpoint, but we will use the Postman tool here to simplify the process.


To load the Twitter API v2 Postman collection into your environment, please click on the following button:





Add Twitter API v2 to Postman






Once you have the Twitter API v2 collection loaded in Postman, navigate to the "Retweets" folder and select "Retweeted by.” 


#### Step two: Authenticate your request


To properly make a request to the Twitter API, you need to verify that you have permission. To do so, this endpoint requires you to authenticate your request with either OAuth 2.0 App-Only, OAuth 2.0 Authorization Code with PKCE, or OAuth 1.0a User Context authentication methods.


For simplicity's sake, we will utilize OAuth 2.0 App-Only with this request, but you will need to use one of the other authentication methods if you'd like to request private metrics or Retweets. 


To utilize OAuth 2.0 App-Only, you must add your keys and tokens, specifically theApp Access Token (also known as the App-only Bearer Token) to Postman. You can do this by selecting the environment named “Twitter API v2” in the top-right corner of Postman and adding your keys and tokens to the "initial value" and "current value" fields (by clicking the eye icon next to the environment dropdown).


These variables will automatically be pulled into the request's authorization tab if you've done this correctly.  

 


#### Step three: Specify a Tweet


With this endpoint, you must specify the Tweet ID that you want to get Retweeting users of.  You can find the ID of a Tweet by navigating to that Tweet on Twitter and pulling the numerical code at the end of the URL. For example, the following URL's Tweet ID is 1354143047324299264.


https://twitter.com/TwitterDev/status/1354143047324299264


In Postman, navigate to the "Params" tab and enter this username into the "Value" column of the id path variable (at the bottom of the section), making sure to not include any spaces before or after usernames. 




|  |  |
| --- | --- |
| **Key** | **Value** |
| `id` | The Tweet ID you want to get the Reweeting users of |


#### 
Step four: Identify and specify which fields you would like to retrieve


If you click the "Send" button after step three, you will receive the default user object fields in your response: id, name, and username.


If you would like to receive additional fields beyond id, name, and username, you will have to specify those fields in your request with the fields and/or expansions parameters.


For this exercise, we will request three additional sets of fields from different objects:


1. The additional user.created\_at field in the primary user objects.
2. The associated pinned Tweets’ object’s default fields for the returned users: id and text.
3. The additional  tweet.created\_at field in the associated Tweet objects.


In Postman, navigate to the "Params" tab and add the following key:value pair to the "Query Params" table:


 




|  |  |  |
| --- | --- | --- |
| **Key** | **Value** | **Returned fields** |
| user.fields | created\_at |  user.created\_at |
| expansions | pinned\_tweet\_id | tweet.id, tweet.text |
| tweet.fields | created\_at | tweet.created\_at |


You should now see the following URL next to the "Send" button:












```

      https://api.twitter.com/2/tweets/1354143047324299264/retweeted_by?user.fields=created_at&expansions=pinned_tweet_id&tweet.fields=created_at
    
```





Code copied to clipboard








 


#### Step five: Make your request and review your response


Once you have everything set up, hit the "Send" button and you will receive a similar response to the following example response:


 












```

      {
  "data": [
    {
      "created_at": "2008-12-04T18:51:57.000Z",
      "id": "17874544",
      "username": "TwitterSupport",
      "name": "Twitter Support"
    },
    {
      "created_at": "2007-02-20T14:35:54.000Z",
      "id": "783214",
      "username": "Twitter",
      "name": "Twitter"
    },
    {
      "pinned_tweet_id": "1389270063807598594",
      "created_at": "2018-11-21T14:24:58.000Z",
      "id": "1065249714214457345",
      "username": "TwitterSpaces",
      "name": "Spaces"
    },
    {
      "pinned_tweet_id": "1293595870563381249",
      "created_at": "2007-05-23T06:01:13.000Z",
      "id": "6253282",
      "username": "TwitterAPI",
      "name": "Twitter API"
    }
  ],
  "includes": {
    "tweets": [
      {
        "created_at": "2021-05-03T17:26:09.000Z",
        "id": "1389270063807598594",
        "text": "now, everyone with 600 or more followers can host a Space.\n\nbased on what we've learned, these accounts are likely to have a good experience hosting because of their existing audience. before bringing the ability to create a Space to everyone, we’re focused on a few things. 🧵"
      },
      {
        "created_at": "2020-08-12T17:11:04.000Z",
        "id": "1293595870563381249",
        "text": "Twitter API v2: Early Access released\n\nToday we announced Early Access to the first endpoints of the new Twitter API!\n\n#TwitterAPI #EarlyAccess #VersionBump https://t.co/g7v3aeIbtQ"
      }
    ]
  }
}
    
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















