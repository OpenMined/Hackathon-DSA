



Direct Message lookup standard v1.1 to v2 migration guide | Docs | Twitter Developer Platform 





































































































Standard v1.1 compared to Twitter API v2



Comparing v1.1 and v2 Direct Message event lookup endpoints
-----------------------------------------------------------


Both v1.1 and v2 versions of the Direct Messages endpoints provide methods for looking up Direct Message events. This guide is intended to help understand the differences and provide information for migrating to v2. 


A major difference between the two versions is that v1.1 supports only one-to-one conversations, while v2 introduces support for group conversations. One artifact of this is that v1.1 supports only "message created" events, while v2 also supports events associated with participants joining and leaving conversations. In fact, a fundamental v2 update is establishing dm\_conversations as a core API object.     




With v1.1. there are two endpoints for retrieving Direct Messages (again, new messages are the only event type supported with v1.1):  




* GET direct\_messages/events/show - Retrieves a single event by ID.
* GET direct\_messages/events/list - Retrieves up to 30 days of one-to-one Direct Messages sent and received by the authenticated user. Note that this method is not able to retrieve messages from group conversations.


With this v2 release, there are three GET methods for retrieving Direct Message conversation events:   




* **GET /2/dm\_conversations/with/:participant\_id/dm\_events** - Retrieves Direct Message events associated with a one-to-one conversation. The :participant\_id path parameter is the User ID of the account having the conversation with the authenticated user making this request.
* **GET /2/dm\_conversations/:dm\_conversation\_id/dm\_events** - Retrieves Direct Message events associated with a specific conversation ID, as indicated by the :dm\_conversation\_id path parameter. This method supports both one-to-one and group conversations.
* **GET /2/dm\_events** - Retrieves Direct Message events associated with a user, including both one-to-one and group conversations. Events from up to 30 days ago are available.


An important detail is that conversation and event IDs are shared across v1.1 and v2 versions of the Twitter Platform. This means both versions can be used together. For example, the Direct Messages v1.1 endpoints provide methods for returning a single event and for deleting events, methods not yet available with v2. Since IDs are common across v1.1 and v2, you can make v1.1 requests based on IDs provided by v2, or by referencing conversation IDs displayed in conversation URLs on the Twitter application.


The following table compares fundamental aspects of the v1.1 and v2 Direct Message event lookup endpoints. The Twitter API v2 characteristics shared here are common to all of the Direct Message lookup endpoints.








|  |  |  |
| --- | --- | --- |
| **Description** | **Standard v1.1** | **Twitter API v2** |
| Host domain | https://api.twitter.com | https://api.twitter.com |
| Endpoint root path | /1.1/direct\_messages | /2/dm\_conversations
Direct Messages conversations are introduced as a fundamental API object. 

These endpoints retrieve MessageCreate, ParticipantsJoin, and ParticipantLeave events. |
| HTTP methods supported | GET | GET |
| Supports Group Direct Messages |  | ✔ |
| Event types supported | message\_create | MessageCreate, ParticipantsJoin, ParticipantsLeave |
| Authentication | OAuth 1.0a User Context | OAuth 1.0a User Context
OAuth 2 User Context (scopes: dm.read, tweet.read, user.read) |
| Requires the use of credentials from a developer App associated with a Twitter API v2 Project |  | ✔ |
| Default request rate limits\*
\*All requests require user tokens |  | GET requests: 300 requests per 15 mins
Rate limit is applied across all three endpoints |






The following tables compare the v2 GET methods with version v1.1. Note that these v2 offerings expand the available capabilities by supporting group conversations. 


**Get all messages in a specific one-to-one conversation**
----------------------------------------------------------


Path: GET /2/dm\_conversations/with/:participant\_id/dm\_events








|  |  |  |
| --- | --- | --- |
| **Description** | **Standard v1.1** | **Twitter API v2** |
| Endpoint path | GET 
/1.1/direct\_messages/events/list | GET /2/dm\_conversations/with/:participant\_id/dm\_events |
| How much event history is available | 30 days | No limit |
| Default request rate limits | 15 requests per 15 minutes | 300 requests per 15 minutes
Rate limit is applied across all three GET endpoints |






**Get all messages by conversation ID**  




Path: GET /2/dm\_conversations/:dm\_conversation\_id/dm\_events








|  |  |  |
| --- | --- | --- |
| **Description** | **Standard v1.1** | **Twitter API v2** |
| Endpoint path | Not supported. V1.1 can return messages from one-to-one conversations only and there is no support for retrieving events by conversation IDs. | GET /2/dm\_conversations/:dm\_conversation\_id/dm\_events |
| How much event history is available | 30 days | No limit |
| Supports group conversations |  | ✔ |
| Default request rate limits
 | 15 requests per 15 minutes
 | 300 requests per 15 minutes
Rate limit is applied across all three GET endpoints |
|  |  |






**Get all events across an authenticated user's conversations, both one-to-one and group conversations**  




Path: GET /2/dm\_events








|  |  |  |
| --- | --- | --- |
| **Description** | **Standard v1.1** | **Twitter API v2** |
| Endpoint path | GET /1.1/direct\_messages/events/list

V1.1 can return messages from one-to-one conversations only. | GET /2/dm\_events |
| How much event history is available | 30 days | 30 days |
| Supports group conversations |  | ✔ |
| Default request rate limits
 | 15 requests per 15 minutes
 | 300 requests per 15 minutes
Rate limit is applied across all three GET endpoints |
|  |  |










Next steps
----------






Quick start guide


API reference


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















