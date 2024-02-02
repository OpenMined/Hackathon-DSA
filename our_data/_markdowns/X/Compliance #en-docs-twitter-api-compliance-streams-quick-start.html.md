
Compliance streams quick start guide | Docs | Twitter Developer Platform 

Quick start

Getting started with the compliance stream endpoints
----------------------------------------------------

This quick start guide will help you make your first request to the compliance stream endpoints using a cURL request. cURL is a command line tool which allows you to make requests with minimal configuration.

If you would like to see sample code in different programming languages, please visit our Twitter API v2 sample code GitHub repository.  

### Prerequisites

The compliance streams is available with Enterprise access.

To complete this guide, you will need to have a set of keys and tokens to authenticate your request. You can generate these keys and tokens by following these steps:

* Sign up for a developer account and receive approval.
* Create a Project and an associated developer App in the developer portal.
* Navigate to your App's “Keys and tokens” page to generate the required credentials. Make sure to save all credentials in a secure location.

Steps to build a compliance stream request
------------------------------------------

#### Step one: Start with a cURL command

In this quick start, we are going to use a simple cURL request to connect to a single partition of the Tweet compliance stream. There are 4 partitions in all, so 4 connections must be maintained to receive all events. The Tweet compliance stream endpoint is a very simple one. All you will have to do is replace or add a couple of elements of the below request and submit it to your command line tool.

```
      curl -X GET "https://api.twitter.com/2/tweets/compliance/stream?partition=1" \ 
-H "Authorization: Bearer $APP_ACCESS_TOKEN"

```

Code copied to clipboard

To connect to the User compliance stream, update the request URL to  "https://api.twitter.com/2/users/compliance/stream?partition=1"

#### Step two: Authenticate your request

Since the compliance stream endpoints require OAuth 2.0 App-Only authentication, you will need to replace $APP\_ACCESS\_TOKEN with the App Access Token that you generated in the prerequisites. 

#### Step three: Make your request and review your response

Once you have everything set up, you can submit your request to Twitter using the cURL command-line tool. If done successfully, you will receive a live stream of Tweet compliance events with payloads similar to the following:

```
      {"data":{"delete":{"tweet":{"id":"1543734217692828673","author_id":"906948460078698496"},"event_at":"2022-07-08T17:54:25.052Z"}}}
{"data":{"delete":{"tweet":{"id":"1518339433317514240","author_id":"906948460078698496"},"event_at":"2022-07-08T17:54:25.098Z"}}}
{"data":{"delete":{"tweet":{"id":"1543019691868381185","author_id":"906948460078698496"},"event_at":"2022-07-08T17:54:25.156Z"}}}
{"data":{"delete":{"tweet":{"id":"1545202024509778944","author_id":"906948460078698496"},"event_at":"2022-07-08T17:54:25.090Z"}}}

```

Code copied to clipboard

If you would like to close your connection, you can press Control-C in your command line tool on either Mac or Windows systems to break the connection, or you can also close the window. 

Your code can parse each JSON line to locate the Tweet (or User ID if using the User compliance stream) and delete the Tweets (or Users) with those IDs from your dataset to stay in compliance. 

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