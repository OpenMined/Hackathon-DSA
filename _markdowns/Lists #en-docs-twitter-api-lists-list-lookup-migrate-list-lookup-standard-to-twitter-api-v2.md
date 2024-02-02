



List lookup: Standard v1.1 compared to Twitter API v2 | Docs | Twitter Developer Platform 





































































































List lookup: Standard v1.1 compared to Twitter API v2



List lookup: Standard v1.1 compared to Twitter API v2
-----------------------------------------------------


If you have been working with the standard v1.1 GET lists/show and  GET lists/ownerships endpoints, the goal of this guide is to help you understand the similarities and differences between the standard v1.1 and Twitter API v2 List lookup endpoints.


* **Similarities**
	+ Authentication methods
	+ Rate limits
* **Differences**
	+ Endpoint URLs
	+ App and Project requirements
	+ Data objects per request limits
	+ Response data formats
	+ Request parameters


 


### Similarities


#### **Authentication**


Both endpoint versions support both OAuth 1.0a User Context and App only. Therefore, if you were previously using one of the standard v1.1 List lookup endpoints, you can continue using the same authentication method if you migrate to the Twitter API v2 version.


 


Depending on your authentication library/package of choice, App only authentication is probably the easiest way to get started and can be set with a simple request header. To learn how to generate an App only Access Token, see this App only guide.


 


**Rate limits**




|  |  |
| --- | --- |
| **Standard v1.1** | **Twitter API v2** |
| /1.1/lists/show.json
75 requests per 15-minute window with OAuth 1.0a User Context
75 requests per 15-minute window with App only | /2/lists/:id
75 requests per 15-minute window with OAuth 1.0a User Context
75 requests per 15-minute window with OAuth 2.0 Authorization Code with PKCE |
| /1.1/lists/ownerships.json
15 requests per 15-minute window with OAuth 1.0a User Context
15 requests per 15-minute window with App only | /2/users/:id/owned\_lists
15 requests per 15-minute window with OAuth 1.0a User Context
15 requests per 15-minute window with OAuth 2.0 Authorization Code with PKCE
15 requests per 15-minute window with App only |


#### 


### Differences


#### Endpoint URLs


* Standard v1.1 endpoints:
	+ GET https://api.twitter.com/1.1/lists/show.json  
	
	(Lookup a specified List)
	+ GET https://api.twitter.com/1.1/lists/ownerships.json  
	
	(Lookup specified user owned Lists)
* Twitter API v2 endpoint:
	+ GET https://api.twitter.com/2/lists/:id  
	
	(Lookup a specified List)
	+ GET https://api.twitter.com/2/users/:id/owned\_lists  
	
	(Lookup specified user owned Lists)


#### 


#### App and Project requirements


The Twitter API v2 endpoints require that you use credentials from a developer App that is associated with a Project when authenticating your requests. All Twitter API v1.1 endpoints can use credentials from standalone Apps or Apps associated with a project.


#### 

Data objects per request limits


The standard v1.1 /lists/ownerships endpoint allows you to return up to 1000 Lists per request. The new v2 endpoints allow you to return up to 100 Lists per request. By default, 100 user objects will be returned, to change the number of results you will need to pass a query parameter max\_results= with a number between 1-100; you can then pass the next\_token returned in the response payload to the pagination\_token query parameter in your next request.


 


**Response data format**


One of the biggest differences between standard v1.1 and Twitter API v2 endpoint versions is how you select which fields return in your payload.


For the standard endpoints, you receive many of the response fields by default and then have the option to use parameters to identify which additional fields or sets of fields should return in the payload.


The Twitter API v2 version only delivers the List id and name fields by default. To request any additional fields or objects, you will need to use the fields and expansions parameters. Any List fields that you request from this endpoint will return in the primary List object. Any expanded Tweet or user object and fields will return an includes object within your response. You can then match any expanded objects back to the List object by matching the IDs located in both the user and the expanded Tweet object. 


Here are examples of possible List fields and expansions:


* created\_at
* follower\_count
* member\_count
* owner\_id
* description
* private


 




|  |  |
| --- | --- |
| **Endpoint** | **Expansion** |
| /2/lists/:id | owner\_id |
| /2/users/:id/owned\_lists | owner\_id |


 


We encourage you to read more about these new parameters in their respective guides, or by reading our guide on how to use fields and expansions. 


We have also put together a data format migration guide that can help you map standard v1.1 fields to the newer v2 fields. This guide will also provide you with the specific expansion and field parameter that you will need to pass with your v2 request to return specific fields. 


 


In addition to the changes in how you request certain fields, Twitter API v2 is also introducing new JSON designs for the objects returned by the APIs, including Tweet and user objects.


* At the JSON root level, the standard endpoints return Tweet objects in a statuses array, while Twitter API v2 returns a data array.
* Instead of referring to Retweeted and Quoted "statuses", Twitter API v2 JSON refers to Retweeted and Quoted Tweets. Many legacy and deprecated fields, such as contributors and user.translator\_type are being removed.
* Instead of using both favorites (in Tweet object) and favourites (in user object), Twitter API v2 uses the term like.
* Twitter is adopting the convention that JSON values with no value (for example, null) are not written to the payload. Tweet and user attributes are only included if they have non-null values.


 


#### Request parameters


The following standard v1.1 request parameters have equivalents in Twitter API v2:


 


**List lookup by ID**




|  |  |
| --- | --- |
| **Standard v1.1** | **Twitter API v2** |
| list\_id | id |
| slug | No equivalent |
| owner\_screen\_name | No equivalent |
| owner\_id
 | Requested with expansions/fields parameter |


 


 


**User owned List lookup**




|  |  |
| --- | --- |
| **Standard v1.1** | **Twitter API v2** |
| user\_id | id |
| screen\_name | No equivalent  |
| count | max\_results |
| cursor | pagination\_token |
|  |  |










Next steps
----------






Review the List lookup API references



















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















