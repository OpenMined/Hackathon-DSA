
Mutes lookup: Standard v1.1 compared to Twitter API v2 | Docs | Twitter Developer Platform 

Mutes lookup: Standard v1.1 compared to Twitter API v2

Mutes lookup: Standard v1.1 compared to Twitter API v2
------------------------------------------------------

If you have been working with the standard v1.1 GET mutes/users/ids and GET mutes/users/list endpoints, the goal of this guide is to help you understand the similarities and differences between the standard v1.1 and Twitter API v2 mutes lookup endpoints.

* **Similarities**
	+ Authentication
* **Differences**
	+ Endpoint URLs
	+ Users per request limits
	+ App and Project requirements
	+ Response data formats
	+ Request parameters

### Similarities

#### **Authentication**

Both the standard v1.1 and Twitter API v2 mutes lookup endpoints use OAuth 1.0a User Context. Therefore, if you were previously using one of the standard v1.1 mutes lookup endpoints, you can continue using the same authentication method if you migrate to the Twitter API v2 version. 

### Differences

#### Endpoint URLs

* Standard v1.1 endpoints:
	+ GET https://api.twitter.com/1.1/mutes/users/ids.json  
	(list of user IDs who the specified user muted)
	+ GET https://api.twitter.com/1.1/mutes/users/lists.json  
	(list of users who are muted by the specified user)
* Twitter API v2 endpoint:
	+ GET https://api.twitter.com/2/users/:id/muting  
	(list of users who are muted by the specified user ID)

#### Users per request limits

The standard v1.1 endpoints allow you to return up to 5000 users per request. The new v2 endpoints allow you to return up to 1000 users per request. To return a full 1000 users, you will need to pass max\_results=1000 as a query parameter; you can then pass the next\_token returned in the response payload to the pagination\_token query parameter in your next request.  

#### App and Project requirements

The Twitter API v2 endpoints require that you use credentials from a developer App that is associated with a Project when authenticating your requests. All Twitter API v1.1 endpoints can use credentials from standalone Apps or Apps associated with a project.  

#### Response data format

One of the biggest differences between standard v1.1 and Twitter API v2 endpoint versions is how you select which fields return in your payload.

For the standard endpoints, you receive many of the response fields by default and then have the option to use parameters to identify which fields or sets of fields should return in the payload.

The Twitter API v2 version only delivers the user id, name, and username fields by default. To request any additional fields or objects, you will need to use the fields and expansions parameters. Any user fields that you request from this endpoint will return in the primary user object. Any expanded Tweet object and fields will return an includes object within your response. You can then match any expanded objects back to the user object by matching the IDs located in both the user and the expanded Tweet object. 

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

The following standard v1.1 request parameters have equivalents in Twitter API v2:

| **Standard** | **Twitter API v2** |
| --- | --- |
| stringify\_ids | No equivalent |
| cursor | pagination\_token |
| skip\_status | No equivalent |

There are also a set of standard v1.1 Mutes lookup request parameters **not** supported in Twitter API v2:

| Standard | Comment |
| --- | --- |
| include\_entities | This parameter is used to remove the entities node from the Tweet payload. It has been replaced with additive fields and expansions functionality. |

Next steps
----------

Review the mutes lookup API references

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