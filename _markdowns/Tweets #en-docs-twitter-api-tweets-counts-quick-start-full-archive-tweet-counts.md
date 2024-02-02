



Full-archive Tweet counts quick start | Docs | Twitter Developer Platform 





































































































Full-archive Tweet counts quick start



Getting started with the full-archive Tweet counts     endpoint
---------------------------------------------------------------


This quick start guide will help you make your first request to the full-archive Tweet counts endpoint using Postman, a graphical tool that alows you to make HTTP requests.


If you would like to see sample code in different programming languages, please visit our Twitter API v2 sample code GitHub repository.   













### Prerequisites


The full-archive Tweet counts endpoint is currently only available to those that have Pro or Enterprise access. In order to use this endpoint, you must apply for Pro or Enterprise access. 


In addition to being approved for access, you will need to have a set of keys and tokens to authenticate your request. You can generate these keys and tokens by following these steps:


* Navigate to your Project with Enterprise access in the developer portal and make sure you have an associated developer App within that Project.
* Navigate to your App's “Keys and tokens” page to generate the required credentials. Make sure to save all credentials in a secure location.














 


### Steps to build a full-archive Tweet counts request


#### Step one: Start with a tool or library


There are several different tools, code examples, and libraries that you can use to make a request to this endpoint, but we are going to use the Postman tool here to simplify the process.


To load Twitter API v2 Postman collection into your environment, please click on the following button:





Add Twitter API v2 to Postman



  

Once you have the Twitter API v2 collection loaded in Postman, navigate to the Tweet counts > Full-archive Tweet counts request.


#### Step two: Authenticate your request


To properly make a request to the Twitter API, you need to verify that you have permission. To do so with this endpoint, you must authenticate your request with the OAuth 2.0 App-Only authentication methods.


You must add your keys and tokens, specifically theApp Access Token (also known as the App-only Bearer Token) to Postman. You can do this by selecting the environment named “Twitter API v2” in the top-right corner of Postman and adding your keys and tokens to the "initial value" and "current value" fields (by clicking the eye icon next to the environment dropdown).


This variable will automatically be pulled into the request's authorization tab if you've done this correctly.  

 


#### Step three: Create a query


Each full-archive Tweet counts request requires a single query. For this example, we are going to use a query that matches on Tweets posted by the @XDevelopers account. For this query we use the from operator and set it to XDevelopers (case insensitive):


`from:XDevelopers`


In Postman, navigate to the "Params" tab and enter this ID, or a string of Tweet IDs separated by a comma, into the "Value" column of the `ids` parameter.  

 




| Key | Value | Description |
| --- | --- | --- |
| `query` | `from:XDevelopers` | Query to submit to the full-archive Tweet counts endpoint |


  

Step four (optional): Specify the granularity and time period  




If you click the ‘Send’ button after step three, you will get the default full-archive Tweet counts: by hour for the last 30 days. If you want to get full-archive Tweet counts by day, you will have to add the granularity parameter with a value of day. If you want Tweet counts for more than 30 days ago, you will have to specify the start\_time and end\_time parameters with the desired values. 


In Postman, navigate to the "Params" tab and add the following key:value pair to the "Query Params" table:




|  |  |  |
| --- | --- | --- |
| **Key** | **Value** | **Description** |
| granularity | day | The granularity for the Tweet counts results. Possible values are day, hour or minute |
| start\_time | 2021-05-01T00:00:00Z | The oldest UTC timestamp from which the Tweets will be provided |
| end\_time | 2021-06-01T00:00:00Z | The oldest UTC timestamp from which the Tweets will be provided. |


  

You should now see the following URL next to the "Send" button:  














```

      https://api.twitter.com/2/tweets/counts/all?query=from%3AXDevelopers&start_time=2021-05-01T00:00:00Z&end_time=2021-06-01T00:00:00Z&granularity=day
    
```





Code copied to clipboard








#### 
Step five: Make your request and review your response


Once you have everything set up, hit the "Send" button and you will receive a response similar to the following:












```

      {
   "data": [
       {
           "end": "2021-05-02T00:00:00.000Z",
           "start": "2021-05-01T00:00:00.000Z",
           "tweet_count": 0
       },
       {
           "end": "2021-05-03T00:00:00.000Z",
           "start": "2021-05-02T00:00:00.000Z",
           "tweet_count": 0
       },
       {
           "end": "2021-05-04T00:00:00.000Z",
           "start": "2021-05-03T00:00:00.000Z",
           "tweet_count": 0
       },
       {
           "end": "2021-05-05T00:00:00.000Z",
           "start": "2021-05-04T00:00:00.000Z",
           "tweet_count": 0
       },
       {
           "end": "2021-05-06T00:00:00.000Z",
           "start": "2021-05-05T00:00:00.000Z",
           "tweet_count": 0
       },
       {
           "end": "2021-05-07T00:00:00.000Z",
           "start": "2021-05-06T00:00:00.000Z",
           "tweet_count": 0
       },
       {
           "end": "2021-05-08T00:00:00.000Z",
           "start": "2021-05-07T00:00:00.000Z",
           "tweet_count": 0
       },
       {
           "end": "2021-05-09T00:00:00.000Z",
           "start": "2021-05-08T00:00:00.000Z",
           "tweet_count": 0
       },
       {
           "end": "2021-05-10T00:00:00.000Z",
           "start": "2021-05-09T00:00:00.000Z",
           "tweet_count": 0
       },
       {
           "end": "2021-05-11T00:00:00.000Z",
           "start": "2021-05-10T00:00:00.000Z",
           "tweet_count": 0
       },
       {
           "end": "2021-05-12T00:00:00.000Z",
           "start": "2021-05-11T00:00:00.000Z",
           "tweet_count": 0
       },
       {
           "end": "2021-05-13T00:00:00.000Z",
           "start": "2021-05-12T00:00:00.000Z",
           "tweet_count": 6
       },
       {
           "end": "2021-05-14T00:00:00.000Z",
           "start": "2021-05-13T00:00:00.000Z",
           "tweet_count": 1
       },
       {
           "end": "2021-05-15T00:00:00.000Z",
           "start": "2021-05-14T00:00:00.000Z",
           "tweet_count": 0
       },
       {
           "end": "2021-05-16T00:00:00.000Z",
           "start": "2021-05-15T00:00:00.000Z",
           "tweet_count": 0
       },
       {
           "end": "2021-05-17T00:00:00.000Z",
           "start": "2021-05-16T00:00:00.000Z",
           "tweet_count": 0
       },
       {
           "end": "2021-05-18T00:00:00.000Z",
           "start": "2021-05-17T00:00:00.000Z",
           "tweet_count": 0
       },
       {
           "end": "2021-05-19T00:00:00.000Z",
           "start": "2021-05-18T00:00:00.000Z",
           "tweet_count": 1
       },
       {
           "end": "2021-05-20T00:00:00.000Z",
           "start": "2021-05-19T00:00:00.000Z",
           "tweet_count": 0
       },
       {
           "end": "2021-05-21T00:00:00.000Z",
           "start": "2021-05-20T00:00:00.000Z",
           "tweet_count": 8
       },
       {
           "end": "2021-05-22T00:00:00.000Z",
           "start": "2021-05-21T00:00:00.000Z",
           "tweet_count": 1
       },
       {
           "end": "2021-05-23T00:00:00.000Z",
           "start": "2021-05-22T00:00:00.000Z",
           "tweet_count": 0
       },
       {
           "end": "2021-05-24T00:00:00.000Z",
           "start": "2021-05-23T00:00:00.000Z",
           "tweet_count": 0
       },
       {
           "end": "2021-05-25T00:00:00.000Z",
           "start": "2021-05-24T00:00:00.000Z",
           "tweet_count": 0
       },
       {
           "end": "2021-05-26T00:00:00.000Z",
           "start": "2021-05-25T00:00:00.000Z",
           "tweet_count": 1
       },
       {
           "end": "2021-05-27T00:00:00.000Z",
           "start": "2021-05-26T00:00:00.000Z",
           "tweet_count": 1
       },
       {
           "end": "2021-05-28T00:00:00.000Z",
           "start": "2021-05-27T00:00:00.000Z",
           "tweet_count": 1
       },
       {
           "end": "2021-05-29T00:00:00.000Z",
           "start": "2021-05-28T00:00:00.000Z",
           "tweet_count": 2
       },
       {
           "end": "2021-05-30T00:00:00.000Z",
           "start": "2021-05-29T00:00:00.000Z",
           "tweet_count": 0
       },
       {
           "end": "2021-05-31T00:00:00.000Z",
           "start": "2021-05-30T00:00:00.000Z",
           "tweet_count": 0
       },
       {
           "end": "2021-06-01T00:00:00.000Z",
           "start": "2021-05-31T00:00:00.000Z",
           "tweet_count": 0
       }
   ],
   "meta": {
       "total_tweet_count": 22
   }
}
    
```






#### 
Step six: Paginate through your results


If the ‘meta’ object in your response also contains next\_token, you can pass its value to the next\_token query parameter.




| Key | Value | Description |
| --- | --- | --- |
| next\_token | You will add the next\_token that you pull from your previous request's meta object and add it here. | If your latest request does not deliver the remainder of the results, you will receive a next\_token in the meta object. You will pull the value of that field and add it as the value of the next\_token parameter in your next request, holding all other request parameters constant. 
 |


Once you have the right value for next\_token set, hit the "Send" button and you will receive the next page of results.
















Next steps
----------






Customize your request using the API Reference


See a full list of query operators


Use sample code for these endpoints





























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















