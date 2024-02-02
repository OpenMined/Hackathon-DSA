
Tweets Usage introduction | Docs | Twitter Developer Platform 

Introduction

Introduction
------------

The Usage API in the Twitter API v2 allows developers to programmatically retrieve their project usage. Using thie endpoint, developers can keep a track and monitor of the number of Tweets they have pulled for a given billing cycle.

Developers can use the GET endpoint to get the daily project usage for upto the last 90 days. The usage can also be aggregated per client app connected to your peoject.

There is a app rate limit of 50 requests per 15 minutes for this GET endpoint.

### Getting started

To use this endpoint, you need a bearer token from the developer portal. Once you have the bearer token,  you can call the usage API as shown below:

```
      curl 'https://api.twitter.com/2/usage/tweets' --header 'Authorization: Bearer XXXXX'
```

Code copied to clipboard

If the request is successful, you should see the JSON response as shown below:

```
      {
    "data": {
        "cap_reset_day": 10,
        "project_cap": "5000000000",
        "project_id": "1369785403853424",
        "project_usage": "43435"
    }
}
```

Code copied to clipboard

**Account setup**

To access these endpoints, you will need:

* An approved developer account.
* To authenticate using the keys and tokens from a developer App that is located within a Project.

Learn more about getting access to the Twitter API v2 endpoints in our getting started guide.

Sample code

Run in Postman

Supporting resources
--------------------

Learn how to use Postman

Troubleshoot an error

API Reference

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