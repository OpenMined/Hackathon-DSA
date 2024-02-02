



Introduction | Docs | Twitter Developer Platform 





































































































Introduction



Introduction
------------


### Quote Tweets lookup


The Quote Tweets lookup endpoint gives the Quote Tweets for a given Tweet ID.  This allows developers that build apps and clients to get the Quote Tweets for a Tweet quickly and efficiently. It also makes it easy for researchers to study the full conversation around a Tweet including all its Quote Tweets.


Here is a Quote Tweet for a Tweet from @TwitterAPI:



> Today, OAuth 2.0 and new fine-grained permission scopes are available to all developers for Twitter API v2 endpoints. https://t.co/rNxC0GQDoP
> 
> 
> — Twitter API (@TwitterAPI) December 14, 2021


The Quote Tweets lookup endpoint is a REST endpoint that takes a single path parameter to indicate the desired Tweet (by Tweet ID). 


Tweets are delivered in reverse-chronological order, starting with the most recent. Results are paginated up to 100 Tweets per page (10 Tweets by default). Pagination tokens are provided for paging through large sets of Tweets.


The Quote Tweets endpoint supports fields and expansions parameters, and returns the new JSON data format.


This endpoint will always return the most recent edit, along with the edit history. Any Tweet collected after its 30-minute edit window will represent its final version and will include an array of IDs for all Tweets in its edit history. For Tweets with no edit history, this array will hold a single ID.


To successfully make a request to this endpoint, you will need to authorize your request with the OAuth 1.0a User Context, OAuth 2.0 Authorization Code with PKCE, or OAuth 2.0 App-Only authentication methods. You must use OAuth 1.0a User Context or OAuth 2.0 Authorization Code with PKCE when requesting non public metrics, promoted metrics or a protected user's timeline.


 











**Account setup**


To access these endpoints, you will need:


* An approved developer account.
* To authenticate using the keys and tokens from a developer App that is located within a Project.


Learn more about getting access to the Twitter API v2 endpoints in our getting started guide.












Quick start


Jump to example requests


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















