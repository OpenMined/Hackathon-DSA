
How to build a standard query | Docs | Twitter Developer Platform 

How to build a standard query

**Please note:**  

We launched a new version of the standard Search Tweets endpoint as part of Twitter API v2: Early Access. If you are currently using any of these endpoints, you can use our migration materials to start working with the newer endpoint.

To see all of Twitter's search endpoint offerings, please visit our search overview.

How to build a query
--------------------

Standard

The best way to build a query and test if it’s valid and will return matched Tweets is to first try it at twitter.com/search. As you get a satisfactory result set, the URL loaded in the browser will contain the proper query syntax that can be reused in the API endpoint. Here’s an example:

1. We want to search for Tweets referencing @twitterapi account. First, we run the search on twitter.com/search
2. Check and copy the URL loaded. In this case, we got: https://twitter.com/search?q=%40twitterapi
3. Replace https://twitter.com/search with https://api.twitter.com/1.1/search/tweets.json and you will get: https://api.twitter.com/1.1/search/tweets.json?q=%40twitterapi
4. Run a Twurl command to execute the search.

Please note that the API requires that the request is authenticated (check Authentication & Authorization documentation for more details on this). Also note that the search results at twitter.com may return historical results, while the Search API usually only serves Tweets from the past week.

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