



Tweet counts introduction | Docs | Twitter Developer Platform 





































































































Introduction






Introduction
------------


The v2 Tweet counts endpoints allow developers to understand and retrieve the volume of data for a given query.  This can be beneficial for a number of reasons, including:


* Understand the Tweet volume for a keyword to build visualizations, such as trendlines.
* Understanding the time period in which an event or conversation occurred, to ensure your query captures the relevant data
* Understanding how many Tweets a search query will return, in order to refine your query, before using the recent search or full-archive search endpoints.  

**Please note:** The counts will not always match the result that will be returned from search endpoints because the search endpoints go through additional compliance that the counts endpoints do not go through
* Understanding the size of the conversation around a topic, without actually having to pull the raw data, and put Tweets against your monthly Tweet cap.


 


When developing a query, you will be limited to a certain query length and to specific operators based on your access level. 


* If you are using a Project with Essential or Elevated access, you can use the core operators to develop your query, and can use queries up to 512 characters in length.
* If you are using a Project with Academic Research access, you can use all available operators, and use queries up to 1024 characters in length.
* If you are using a Project with Enterprise access, you can use all available operators, and use queries up to 4096 characters in length.


You can also specify the granularity (which can be day, hour, or minute) as well as the time period for which you need the Tweet counts (using the start\_time and end\_time parameters). The default time granularity that this endpoint uses is hour, which means if you do not specify the granularity parameter, the endpoint will give you the Tweet counts per hour, for the last 7 days.  













**Account setup**


To access these endpoints, you will need:


* An approved developer account.
* To authenticate using the keys and tokens from a developer App that is located within a Project.


Learn more about getting access to the Twitter API v2 endpoints in our getting started guide.









 


### Recent Tweet counts


The recent Tweet counts endpoint allows you to programmatically retrieve the numerical count of Tweets for a query, over the last seven days. This endpoint is available via to anyone using keys and tokens that are associated with an App within a Project and uses OAuth 2.0 App-Only for authentication.


 


### Full-archive Tweet counts


Academic Research or Enterprise access only


The full-archive Tweet counts endpoint allows you to programmatically retrieve the numerical count of Tweets for a query, from the entire archive of public Tweets. Currently, this endpoint is only available to those that have been approved for Academic Research or Enterprise access and use the OAuth 2.0 App-Only for authentication.


One example: You could use the full-archive Tweet counts endpoint to see the number of Tweets for the hashtag #SOSHurricaneHarvey per day between August and September 2017.


**Please note:** The counts endpoint paginates at 31 days per response. For example, setting a day granularity, will return the count of results per day for 31 days per page.  Setting an hour granularity, will return the count of results per hour for 744 (31 days x 24 hours) hours per page.  If you do not specify the granularity and time period, this endpoint will give you Tweet counts for a query per hour, for the last 30 days.


 









Quick start


Sample code


Search Tweets Python client


Run in Postman


Try with API Explorer

















Supporting resources
--------------------






Learn how to use Postman to make requests


Troubleshoot an error


Visit the API reference page










Tutorials
---------






Getting started with converting JSON objects to CSV


Learning path: How to build powerful queries

























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















