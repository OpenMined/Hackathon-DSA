



Manage mutes: Standard v1.1 compared to Twitter API v2 | Docs | Twitter Developer Platform 





































































































Manage mutes: Standard v1.1 compared to Twitter API v2



Manage mutes: Standard v1.1 compared to Twitter API v2
------------------------------------------------------


If you have been working with the standard v1.1 POST mutes/users/create and POST mutes/users/destroy endpoints, the goal of this guide is to help you understand the similarities and differences between the standard v1.1 and Twitter API v2 manage mutes endpoints.


* **Similarities**
	+ OAuth 1.0a User Context
* **Differences**
	+ Endpoint URLs
	+ App and Project requirements
	+ HTTP methods
	+ Request parameters


### Similarities


#### OAuth 1.0a User Context authentication method


Both the endpoint versions support OAuth 1.0a User Context. Therefore, if you were previously using one of the standard v1.1 manage mutes endpoints, you can continue using the same authentication method if you migrate to the Twitter API v2 version.


 


### Differences


#### Endpoint URLs


* Standard v1.1 endpoints:
	+ POST https://api.twitter.com/1.1/mutes/users/create.json  
	
	(mute a user)
	+ POST https://api.twitter.com/1.1/mutes/users/destroy.json  
	
	(unmute a user)
* Twitter API v2 endpoint:
	+ POST https://api.twitter.com/2/users/:id/muting  
	
	(mute a user)
	+ DELETE https://api.twitter.com/2/users/:source\_user\_id/muting/:target\_user\_id  
	
	(unmute a user)


 


#### App and Project requirements


The Twitter API v2 endpoints require that you use credentials from a developer App that is associated with a Project when authenticating your requests. All Twitter API v1.1 endpoints can use credentials from standalone Apps or Apps associated with a project.  

  




#### Request parameters


The following standard v1.1 request parameters have equivalents in Twitter API v2:




| Standard v1.1 | Twitter API v2 |
| --- | --- |
| user\_id | target\_user\_id |
| screen\_name | No equivalent |


Please note that the Standard v1.1 parameters are passed as query parameters, whereas the Twitter API v2 parameters are passed as body parameters (for the POST endpoint) or path parameters (for the DELETE endpoint).


Also, an id of the user muting a target user is not required when using the standard v1.1 endpoints since the access tokens passed with OAuth 1.0a User Context inferred which user was initiating the mute/unmute. 


 






Next steps
----------






Review the manage mutes API references



















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















