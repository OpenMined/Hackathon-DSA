
Trends introduction | Docs | Twitter Developer Platform 

Introduction

Introduction
------------

The Trends lookup endpoint allow developers to get the Trends for a location, specified using the where-on-earth id (WOEID).

**Note**: WOEID is a legacy identifier created by Yahoo and has been deprecated. X API uses the numeric value to identify town and country trend locations. Reference our legacy blog post, or archived data

The `tweet_count` for the last 24 hours is also returned for many trends if this is available.

This endpoint supports app-auth authentication and has a rate limit of 75 requests per 15-minute window.

### Getting started

To use this endpoint, you need a bearer token from the developer portal. Once you have the bearer token,  you can call the usage API as shown below:

```
      curl 'https://api.twitter.com/2/trends/by/woeid/26062' --header 'Authorization: Bearer XXXXX' 
```

Code copied to clipboard

If the request is successful, you should see the JSON response as shown below:

```
      {
    "data": [
        {
            "trend_name": "Europe",
            "tweet_count": 232408
        },
        {
            "trend_name": "Isak",
            "tweet_count": 2956
        },
        {
            "trend_name": "RNLI",
            "tweet_count": 2484
        },
        {
            "trend_name": "Toon",
            "tweet_count": 11447
        },
        {
            "trend_name": "St James",
            "tweet_count": 5565
        },
        {
            "trend_name": "Manning",
            "tweet_count": 10077
        },
        {
            "trend_name": "Copenhagen",
            "tweet_count": 35272
        },
        {
            "trend_name": "Coventry",
            "tweet_count": 3662
    ]
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