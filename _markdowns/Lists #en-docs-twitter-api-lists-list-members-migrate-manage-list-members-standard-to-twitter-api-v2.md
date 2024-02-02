



Manage List members: Standard v1.1 compared to Twitter API v2 | Docs | Twitter Developer Platform 





































































































Manage List members: Standard v1.1 compared to Twitter API v2



Manage List members: Standard v1.1 compared to Twitter API v2
-------------------------------------------------------------


If you have been working with the standard v1.1 POST lists/members/create and POST lists/members/destroy endpoints, the goal of this guide is to help you understand the similarities and differences between the standard v1.1 and Twitter API v2 manage List members endpoints.


* **Similarities**
	+ Authentication
* **Differences**
	+ Endpoint URLs
	+ App and Project requirements
	+ HTTP methods
	+ Rate limits
	+ Request parameters


 


### Similarities


#### **Authentication**


Both endpoint versions support OAuth 1.0a User Context. Therefore, if you were previously using one of the standard v1.1 manage List member endpoints, you can continue using the same authentication method if you migrate to the Twitter API v2 version.


 


### Differences


#### Endpoint URLs


* Standard v1.1 endpoints:
	+ POST https://api.twitter.com/1.1/lists/members/create.json  
	
	(Adds a member to a specified List)
	+ POST https://api.twitter.com/1.1/lists/members/destroy.json  
	
	(Removes a member from a specified List)
* Twitter API v2 endpoint:
	+ POST https://api.twitter.com/2/lists/:id/members  
	
	(Adds a member to a specified List)
	+ DELETE https://api.twitter.com/2/lists/:id/members/:user\_id  
	
	(Removes a member from a specified List)


#### 


#### Rate limits




| **Standard v1.1** | **Twitter API v2** |
| --- | --- |
| /1.1/lists/members/create.json
none | /2/lists/:id/members
300 requests per 15-minute window with OAuth 1.0a User Context
300 requests per 15-minute window with OAuth 2.0 Authorization Code with PKCE |
| /1.1/lists/members/destroy.json
none | /2/lists/:id/members/:user\_id
300 requests per 15-minute window with OAuth 1.0a User Context
300 requests per 15-minute window with OAuth 2.0 Authorization Code with PKCE |


#### App and Project requirements


The Twitter API v2 endpoints require that you use credentials from a developer App that is associated with a Project when authenticating your requests. All Twitter API v1.1 endpoints can use credentials from standalone Apps or Apps related to a project.


#### 


#### Request parameters


The following standard v1.1 request parameters have equivalents in Twitter API v2:


 




| **Standard v1.1** | **Twitter API v2** |
| --- | --- |
| list\_id | id |
| slug | No equivalent |
| screen\_name | No equivalent |
| owner\_screen\_name | No equivalent |
| owner\_id | No equivalent |










Next steps
----------






Review the List members API references



















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















