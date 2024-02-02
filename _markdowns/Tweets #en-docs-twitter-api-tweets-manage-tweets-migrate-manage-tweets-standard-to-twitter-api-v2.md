



Manage Tweets: Standard v1.1 compared to Twitter API v2 | Docs | Twitter Developer Platform 





































































































Manage Tweets standard to Twitter API v2



Standard v1.1 compared to Twitter API v2
----------------------------------------


If you have been working with the standard v1.1 POST statuses/update and POST statuses/destroy/:idendpoints, the goal of this guide is to help you understand the similarities and differences between the standard and Twitter API v2 manage Tweets endpoints.  




* **Similarities**
	+ Authentiation
* **Differences**
	+ Endpoint URLs
	+ App and Project requirements
	+ Request parameters


 


### Similarities


#### **Authentication**


Both the standard v1.1 and Twitter API v2 manage Tweets (POST statuses/update and POST statuses/destroy/:id) endpoints use OAuth 1.0a User Context. Therefore, if you were previously using one of the standard v1.1 endpoints, you can continue using the same authentication method if you migrate to the Twitter API v2 version. 


 


### Differences


#### Endpoint URLs


* Standard v1.1 endpoints:
	+ https://api.twitter.com/1.1/statuses/update.json  
	
	(Creates a Tweet)
	+ `https://api.twitter.com/1.1/statuses/destroy/:id.json`  
	
	(Deletes a Tweet)
* Twitter API v2 endpoint:
	+ https://api.twitter.com/2/tweets  
	
	(Creates a Tweet)
	+ https://api.twitter.com/2/tweets/:id  
	
	(Deletes a specified Tweet)


 


#### App and Project requirements


The Twitter API v2 endpoints require that you use credentials from a developer App that is associated with a Project when authenticating your requests. All Twitter API v1.1 endpoints can use credentials from standalone Apps or Apps associated with a project.




 


#### Request parameters


The following standard v1.1 request parameters accepted two request query parameters (user\_id or screen\_name). The Twitter API v2 only accepts the numerical Tweet ID for the DELETE endpoint, and it must be passed as part of the endpoint path.


For the POST endpoint, additional parameters will need to be passed in via the JSON body of the request. You can learn more about what parameters are available in the API reference guide.










Next steps
----------






API reference



















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















