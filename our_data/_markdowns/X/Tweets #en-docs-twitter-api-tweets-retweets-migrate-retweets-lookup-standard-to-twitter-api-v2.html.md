
Retweets lookup: Standard v1.1 compared to Twitter API v2 | Docs | Twitter Developer Platform 

Retweets lookup: Standard v1.1 compared to Twitter API v2

Retweets lookup: Standard v1.1 compared to Twitter API v2
---------------------------------------------------------

If you have been working with the standard v1.1 v1.1 GET statuses/retweets/:id, v1.1 GET statuses/retweets/:ids, the goal of this guide is to help you understand the similarities and differences between the standard v1.1 and Twitter API v2 Retweets lookup endpoints.

* **Similarities**
	+ Authentiation
	+ Users per request limits
* **Differences**
	+ Endpoint URLs
	+ Request limitations
	+ App and Project requirements
	+ Response data format
	+ Request parameters

### Similarities

#### **Authentication**

Both the standard v1.1 and Twitter API v2 Retweets lookup endpoints (v1.1 GET statuses/retweets/:id and v1.1 GET statuses/retweeters/:ids) use OAuth 1.0a User Context or OAuth 2.0 Bearer Token.

**Users per request limits**

For both v1.1 and v2 GET endpoints the max number of users that will be returned by the Retweets lookup endpoint is 100 users per page. For the v2 Retweets lookup endpoint, you can use pagination tokens to page through large results. 

### Differences

#### Endpoint URLs

* Standard v1.1 endpoints:
	+ https://api.twitter.com/1.1/statuses/retweets/:id.json  
	(Returns a collection of the 100 most recent Retweets of the Tweet specified by the `id` parameter)
	+ `https://api.twitter.com/1.1/statuses/retweeters/ids.json`  
	(Returns a collection of up to 100 user IDs belonging to users who have Retweeted the Tweet specified by the `id` parameter)
* Twitter API v2 endpoint:
	+ https://api.twitter.com/2/tweets/:id/retweeted\_by  
	(Returns a list of accounts who have Retweeted a given Tweet)

#### App and Project requirements

The Twitter API v2 endpoints require that you use credentials from a developer App that is associated with a Project when authenticating your requests. All Twitter API v1.1 endpoints can use credentials from standalone Apps or Apps associated with a project.  

#### Response data format

One of the biggest differences between standard v1.1 and Twitter API v2 endpoint versions is how you select which fields return in your payload.

For the standard endpoints, you receive many of the response fields by default, and then have the option to use parameters to identify which fields or sets of fields should return in the payload.

The Twitter API v2 version only delivers the user id , name, and username fields by default. To request any additional fields or objects, you wil need to use the fields and expansions parameters. Any user fields that you request from this endpoint will return in the primary user object. Any expanded Tweet object and fields will return in an includes object within your response. You can then match any expanded objects back to the user object by matching the IDs located in both the user and the expanded Tweet object. 

We encourage you to read more about these new parameters in their respective guides, or by reading our guide on how to use fields and expansions. 

We have also put together a data format migration guide which can help you map standard v1.1 fields to the newer v2 fields. This guide will also provide you the specific expansion and field parameter that you will need to pass with your v2 request to return specific fields.   

In addition to the changes in how you request certain fields, Twitter API v2 is also introducing new JSON designs for the objects returned by the APIs, including Tweet and user objects.

* At the JSON root level, the standard endpoints return Tweet objects in a statuses array, while Twitter API v2 returns a data array.
* Instead of referring to Retweeted and Quoted "statuses", Twitter API v2 JSON refers to Retweeted and Quoted Tweets. Many legacy and deprecated fields, such as contributors and user.translator\_type are being removed.
* Instead of using both favorites (in Tweet object) and favourites (in user object), Twitter API v2 uses the term like.
* Twitter is adopting the convention that JSON values with no value (for example, null) are not written to the payload. Tweet and user attributes are only included if they have a non-null values.

We also introduced a new set of fields to the Tweet object including the following:

* A conversation\_id field
* Two new annotations fields, including context and entities
* Several new metrics fields
* A new reply\_setting field, which shows you who can reply to a given Tweet

#### Request parameters

The following standard v1.1 request parameters accepted two request query parameters (user\_id or screen\_name). The Twitter API v2 only accepts the numerical user ID, and it must be passed as part of the endpoint path.

Next steps
----------

Review the Retweets lookup API references

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