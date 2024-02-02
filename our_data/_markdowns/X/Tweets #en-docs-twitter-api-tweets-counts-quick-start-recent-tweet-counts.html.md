
Recent Tweet counts quick start | Docs | Twitter Developer Platform 

Recent Tweet counts quick start

Getting started with the recent Tweet counts endpoint
-----------------------------------------------------

This quick start guide will help you make your first request to the recent Tweet counts endpoint using Postman, a graphical tool that allows you to send HTTP requests.

If you would like to see sample code in different programming languages, please visit our Twitter API v2 sample code GitHub repository. 

### Prerequisites

To complete this guide, you will need to have a set of keys and tokens to authenticate your request. You can generate these keys and tokens by following these steps:

* Sign up for a developer account and receive approval.
* Create a Project and an associated developer App in the developer portal.
* Navigate to your App's “Keys and tokens” page to generate the required credentials. Make sure to save all credentials in a secure location.

### Steps to build a recent Tweet counts request

#### Step one: Start with a tool or library

There are several different tools, code examples, and libraries that you can use to make a request to this endpoint, but we are going to use the Postman tool here to simplify the process.

To load Twitter API v2 Postman collection into your environment, please click on the following button:

Add Twitter API v2 to Postman

Once you have the Twitter API v2 collection loaded in Postman, navigate to the Tweet counts > Recent Tweet counts request.

#### 
Step two: Authenticate your request

To properly make a request to the Twitter API, you need to verify that you have permission. To do so with this endpoint, you must authenticate your request with the OAuth 2.0 App-Only authentication methods.

You must add your keys and tokens, specifically theApp Access Token (also known as the App-only Bearer Token) to Postman. You can do this by selecting the environment named “Twitter API v2” in the top-right corner of Postman and adding your keys and tokens to the "initial value" and "current value" fields (by clicking the eye icon next to the environment dropdown).

This variable will automatically be pulled into the request's authorization tab if you've done this correctly.  

#### Step three: Create a query

Each recent Tweet counts request requires a singlequery. For this example, we are going to use a query that matches on Tweets posted by the @XDevelopers account. For this query we use the from: operator and set it to XDevelopers (case insensitive):

`from:XDevelopers`

In Postman, navigate to the "Params" tab and enter this ID, or a string of Tweet IDs separated by a comma, into the "Value" column of the `ids` parameter.

|  |  |  |
| --- | --- | --- |
| **Key** | **Value** | **Description** |
| `query` | from:XDevelopers | Query to submit to the recent Tweet counts endpoint |

#### Step four (optional): Specify the granularity of the request

If you click the ‘Send’ button after step three, you will get the default recent Tweet counts: by hour for the last seven days. If you want to get recent Tweet counts by day, you will have to add the granularity parameter with a value of day.

In Postman, navigate to the "Params" tab and day into the "Value" column of the granularity parameter.

|  |  |  |
| --- | --- | --- |
| **Key** | **Value** | **Description** |
| granularity | day | The granularity for the Tweet counts results. Possible values are day, hour or minute |

You should now see the following URL next to the "Send" button:  

```
      https://api.twitter.com/2/tweets/counts/recent?query=from%3AXDevelopers&granularity=day
```

Code copied to clipboard

#### 
Step five: Make your request and review your response

Once you have everything set up, hit the "Send" button and you will receive the following response:

```
      {
   "data": [
       {
           "end": "2021-06-16T00:00:00.000Z",
           "start": "2021-06-15T00:00:00.000Z",
           "tweet_count": 0
       },
       {
           "end": "2021-06-17T00:00:00.000Z",
           "start": "2021-06-16T00:00:00.000Z",
           "tweet_count": 1
       },
       {
           "end": "2021-06-18T00:00:00.000Z",
           "start": "2021-06-17T00:00:00.000Z",
           "tweet_count": 2
       },
       {
           "end": "2021-06-19T00:00:00.000Z",
           "start": "2021-06-18T00:00:00.000Z",
           "tweet_count": 0
       },
       {
           "end": "2021-06-20T00:00:00.000Z",
           "start": "2021-06-19T00:00:00.000Z",
           "tweet_count": 0
       },
       {
           "end": "2021-06-21T00:00:00.000Z",
           "start": "2021-06-20T00:00:00.000Z",
           "tweet_count": 0
       },
       {
           "end": "2021-06-22T00:00:00.000Z",
           "start": "2021-06-21T00:00:00.000Z",
           "tweet_count": 1
       },
       {
           "end": "2021-06-23T00:00:00.000Z",
           "start": "2021-06-22T00:00:00.000Z",
           "tweet_count": 2
       }
   ],
   "meta": {
       "total_tweet_count": 6
   }
}
```

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