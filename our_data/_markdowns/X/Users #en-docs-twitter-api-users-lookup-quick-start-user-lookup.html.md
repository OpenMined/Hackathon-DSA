
User lookup quick start guide | Docs | Twitter Developer Platform 

User lookup

Getting started with the users lookup endpoints
-----------------------------------------------

This quick start guide will help you make your first request to the users lookup endpoints with a set of specified fields using Postman.

If you would like to see sample code in different languages, please visit our Twitter API v2 sample code GitHub repository. 

### Prerequisites

To complete this guide, you will need to have a set of keys and tokens to authenticate your request. You can generate these keys and tokens by following these steps:

* Sign up for a developer account and receive approval.
* Create a Project and an associated developer App in the developer portal.
* Navigate to your App's “Keys and tokens” page to generate the required credentials. Make sure to save all credentials in a secure location.

### Steps to build a users lookup request

#### Step one: Start with a tool or library

There are several different tools, code examples, and libraries that you can use to make a request to this endpoint, but we are going to use the Postman tool here to simplify the process.

To load the Twitter API v2 Postman collection into your environment, please click on the following button:

Add Twitter API v2 to Postman

Once you have the Twitter API v2 collection loaded in Postman, navigate to the GET /users/by endpoint.  

#### Step two: Authenticate your request

To properly make a request to the Twitter API, you need to verify that you have permission. To do so, this endpoint requires you to authenticate your request with either App only, OAuth 2.0 Authorization Code with PKCE, or OAuth 1.0a User Context authentication methods.

For simplicity's sake, we will utilize App only with this request, but you will need to use one of the other authentication methods if you'd like to request private metrics or users. 

To utilize App only, you must add your keys and tokens, specifically theApp Access Token (also known as the App only Bearer Token) to Postman. You can do this by selecting the environment named “Twitter API v2” in the top-right corner of Postman and adding your keys and tokens to the "initial value" and "current value" fields (by clicking the eye icon next to the environment dropdown).

These variables will automatically be pulled into the request's authorization tab if you've done this correctly.  

#### Step three: Identify and specify which user(s) you would like to retrieve

You must specify a user or a set of users that you would like to receive within the request. Depending on which user endpoint you use, you can pass either a user ID or a username. In this situation, we are going to use the GET /users/by endpoint which allows you to pass multiple usernames in a single request (rather than the single-ID, multi-ID, and single-username endpoints) and pass a set of usernames using the usernames query parameter.

Usernames are simply the account handle that you can find within an account's profile URL. For example, the following account’s username is twitterdev.

`https://twitter.com/TwitterDev`

In Postman, navigate to the "Params" tab and enter this username, or a string of usernames separated by a comma, into the "Value" column of the username parameter, making sure to not include any spaces between usernames and commas. 

|  |  |
| --- | --- |
| **Key** | **Value** |
| `username` | twitterdev,twitterapi,adsapi |

#### Step four: Identify and specify which fields you would like to retrieve

If you click the "Send" button after step three, you will receive the default user object fields in your response: id, name, and username.

If you would like to receive additional fields beyond id, name, and username, you will have to specify those fields in your request with the field and/or expansion parameters.

For this exercise, we will request a three additional sets of fields from different objects:

1. The additional user.created\_at field in the primary user objects.
2. The associated pinned Tweets’ object’s default fields for the returned users: id and text.
3. The additional  tweet.created\_at field in the associated Tweet objects.

In Postman, navigate to the "Params" tab and add the following key:value pair to the "Query Params" table:

|  |  |  |
| --- | --- | --- |
| **Key** | **Value** | **Returned fields** |
| `user.fields` | `created_at` | `user.created_at` |
| `expansions` | `author_id` | tweet.id, tweet.text |
| `tweet.fields` | `created_at` | `includes.users.created_at` |

You should now see the following URL next to the "Send" button:

```
      https://api.twitter.com/2/users/by?usernames=twitterdev,twitterapi,adsapi&user.fields=created_at&expansions=pinned_tweet_id&tweet.fields=author_id,created_at
```

Code copied to clipboard

#### 
Step five: Make your request and review your response

Once you have everything set up, hit the "Send" button and you will receive the following response:

```
      {
  "data": [
    {
      "created_at": "2013-12-14T04:35:55.000Z",
      "id": "2244994945",
      "name": "Twitter Dev",
      "pinned_tweet_id": "1255542774432063488",
      "username": "TwitterDev"
    },
    {
      "created_at": "2007-05-23T06:01:13.000Z",
      "id": "6253282",
      "name": "Twitter API",
      "username": "TwitterAPI"
    },
    {
      "created_at": "2013-02-27T20:01:12.000Z",
      "id": "1225933934",
      "name": "Twitter Ads API",
      "username": "AdsAPI"
    }
  ],
  "includes": {
    "tweets": [
      {
        "author_id": "2244994945",
        "created_at": "2020-04-29T17:01:38.000Z",
        "id": "1255542774432063488",
        "text": "During these unprecedented times, what’s happening on Twitter can help the world better understand &amp; respond to the pandemic. \n\nWe're launching a free COVID-19 stream endpoint so qualified devs &amp; researchers can study the public conversation in real-time. https://t.co/BPqMcQzhId"
      }
    ]
  }
}

```

Next steps
----------

Customize your request using the API Reference

Reach out to the community for help

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