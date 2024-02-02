
Quick start | Docs | Twitter Developer Platform 

Quick start

Getting started with the manage Tweets endpoints
------------------------------------------------

This quick start guide will help you make your first request to the manage Tweets endpoints using Postman.  

Please visit our Twitter API v2 sample code GitHub repository if you want to see sample code in different languages.

### Prerequisites

To complete this guide, you will need to have a set of keys and tokens to authenticate your request. You can generate these keys and tokens by following these steps:

* Sign up for a developer account and receive approval.
* Create a Project and an associated developer App in the developer portal.
* Navigate to your App's “Keys and tokens” page to generate the required credentials. Make sure to save all credentials in a secure location.

### 

### Steps to building manage Tweets requests

#### Step one: Start with a tool or library

There are several different tools, code examples, and libraries that you can use to make a request to this endpoint, but we are going to use the Postman tool here to simplify the process.

To load Twitter API v2 Postman collection into your environment, please click on the following button:

Add Twitter API v2 to Postman

Once you have the Twitter API v2 collection loaded in Postman, navigate to the “Manage Tweets” folder, and select “Create a Tweet”.  

#### Step two: Authenticate your request

To properly make a request to the Twitter API, you need to verify that you have permission to do so. To do this with the manage Tweets endpoints, you must authenticate your request using either OAuth 1.0a User Context or OAuth 2.0 Authorization Code with PKCE.

In this example, we are going to use OAuth 1.0a User Context.

You must add your keys and tokens (and specifically your API Key, API Secret Key, OAuth 1.0a user Access Token, and OAuth 1.0a user Access Token Secret) to Postman. You can do this by selecting the environment named “Twitter API v2” (in the top-right corner of Postman), and adding your keys and tokens to the "initial value" and "current value" fields (by clicking the eye icon next to the environment dropdown).

If you've done this correctly, these variables will automatically be pulled into the request's authorization tab.

#### Step three: Specify the text of the Tweet

When creating a new Tweet with this endpoint, text or media for the Tweet are the required body parameters.

In Postman, navigate to the “Body” tab and enter the text of the Tweet as the value for the `text` parameter. Additionally, if you wish to add parameters for items such as polls, replying to a Tweet ID, or adding reply settings you can also do so here. You can learn more about what’s available in our API reference guide.  

|  |  |  |
| --- | --- | --- |
| **Key** | **Value** | **Parameter type** |
| `text` | Hello world!  | body |

#### 
Step four: Identify and specify which fields you would like to retrieve

Once you have everything set up, hit the "Send" button, and you will receive a similar response to the following example response:

```
      {
  "data": {
    "id": "1445880548472328192",
    "text": "Hello world!"
  }
}
```

If the returned response object contains an `id` and the `text` of your Tweet, you have successfully created a Tweet.  

#### Step five: Delete your Tweet

To delete a Tweet, select the “Delete a Tweet” request also found in the “Manage Tweets” folder of the Twitter API v2 collection loaded in Postman. This endpoint requires the ID of the Tweet you wish to delete. Then, in the “Params” tab, enter the ID of the Tweet you wish to delete as the value for the `id` column. 

On successful delete request, you will receive a response similar to the following example:

```
      {
   "data": {
       "deleted" : true
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