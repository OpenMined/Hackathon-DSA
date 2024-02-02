



List members introduction | Docs | Twitter Developer Platform 





































































































Introduction






Introduction
------------


### List members lookup


Members lookup group has two available endpoints. You are able to retrieve details on members of a specified List and see which Lists a user is a member of. These endpoints can be used to enable people to curate and organize new Lists based on the membership information.


There is a rate limit of 900 requests per 15 minutes when looking up member details and a limit of 75 requests per 15 minutes when looking up user memberships.


You can use OAuth 1.0a User Context, App only, or OAuth 2.0 Authorization Code with PKCE to authenticate your requests to this endpoint.   

 


### Manage List members


The manage List members endpoints allow you to add and remove members to a List on behalf of an authenticated user. For these endpoints, there are two methods available: POST and DELETE. The POST method allows you to add a member to a List, and the DELETE method allows you to remove a member from a List. There is a user rate limit of 300 requests per 15 minutes for both endpoints.


Note that Lists cannot have more than 5,000 members.


Since you are making requests on behalf of a user with the these endpoints, you must authenticate them with either OAuth 1.0a User Context or OAuth 2.0 Authorization Code with PKCE, and use the user Access Tokens associated with a user that has authorized your App, which can be generated using the 3-legged OAuth flow (OAuth 1.0a) or the Authorization Code with PKCE grant flow (OAuth 2.0).











**Account setup**


To access these endpoints, you will need:


* An approved developer account.
* To authenticate using the keys and tokens from a developer App that is located within a Project.


Learn more about getting access to the Twitter API v2 endpoints in our getting started guide.












Quick start


Sample code


Run in Postman


Try with API Explorer

















Supporting resources
--------------------






Learn how to use Postman to make requests


Troubleshoot an error


Visit the API reference page for this endpoint

























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















