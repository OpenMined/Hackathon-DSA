
Overview | Docs | Twitter Developer Platform 

Overview

**Please note:**

We've recently released the following endpoints within the Twitter API v2.

| v1.1 endpoints | Corresponding v2 endpoints |  |
| --- | --- | --- |
| GET statuses/lookup 
GET statuses/show/:id | Tweet lookup | Migration guide |
| POST statuses/update
POST statuses/destroy/:id | Manage Tweets | Migration guide |
| GET favorites/list
POST favorites/create 
POST favorites/destroy | Likes | Migration guide |
| GET statuses/retweets/:id 
GET statuses/retweeters/:ids
POST statuses/retweet/:id 
POST statuses/unretweet/:id | Retweets | Migration guide |

Please use the migration guides to see what has changed between the standard v1.1 and v2 versions.

**Important note:**

This endpoint has been updated to include Tweet edit metadata. Learn more about these metadata on the "Edit Tweets" fundamentals page. 

Overview
--------

The following API endpoints can be used to programmatically create, retrieve and delete Tweets, Retweets and Likes:

|  |  |  |
| --- | --- | --- |
| **Tweets** | **Retweets** | **Likes (formerly favorites)** |
| * POST statuses/update
* POST statuses/destroy/:id
* GET statuses/show/:id
* GET statuses/oembed
* GET statuses/lookup
 | * POST statuses/retweet/:id
* POST statuses/unretweet/:id
* GET statuses/retweets/:id
* GET statuses/retweets\_of\_me
* GET statuses/retweeters/ids
 | * POST favorites/create/:id
* POST favorites/destroy/:id
* GET favorites/list
 |

For more details, please see the individual endpoint information within the API reference section.  

### Terminology

**Tweet/Status** - when a status message is shared on Twitter. Also see Introduction to Tweet JSON

**Retweet** - when a Tweet is re-shared by another specific user. Also see Introduction to Tweet JSON  

**Like** - when a Tweet recieves a 'heart' from a specific user, formerly known as favo(u)rite or 'star'  

### Rate limits

As part of our effort to reduce the distribution of spam through our APIs, we enforce App-level rate limit on some of our POST endpoints:

* There is a 300 requests per three hours shared App-level rate limit for the POST statuses/update (post a Tweet) and POST statuses/retweet/:id (post a Retweet) endpoints. This means that you can only post either 300 Tweets or Retweets across all of the authorized users of your developer App during a three hour time period.
* There is a 1,000 requests per 24 hours App-level rate limit for the POST favorites/create/:id endpoint. This means that you can only like 1,000 Tweets across all of the authorized users of your developer App during a 24 hour time period.

Please note that you must also consider the user-level rate limits for these endpoints, as they limit the number of posted Tweets or liked Tweets a specific authorized user can make over a given time period. 

You can review each endpoints' rate limits via their API reference page.

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