



Filtered stream introduction | Docs | Twitter Developer Platform 






































































































Introduction



Introduction
------------


The filtered stream endpoint group enables developers to filter the real-time stream of public Tweets. This endpoint group’s functionality includes multiple endpoints that enable you to create and manage rules, and apply those rules to filter a stream of real-time Tweets that will return matching public Tweets. This endpoint group allows users to listen for specific topics and events in real-time, monitor the conversation around competitions, understand how trends develop in real-time, and much more.


Developers can use the REST rules endpoint to add and remove rules to a persistent stream connection without needing to disconnect. These rules can be created with operators that match on Tweet attributes such as message keywords, hashtags, and URLs. Operators and rule clauses can be combined with boolean logic and parentheses to help refine the filter’s matching behavior. 


Once you've added a set of rules, you can establish a streaming connection which will start to deliver Tweet objects in JSON format through a persistent HTTP Streaming connection. You will only receive content matching your rules while connected to the stream.


The filtered search endpoint supports edited Tweets. This endpoint will deliver edited Tweets that match one or more of your filters, along with its edit history, including an array of Tweet IDs. For Tweets with no edit history, this array will hold a single ID. For Tweets that have been edited, this array contains multiple IDs, arranged in ascending order reflecting the order of edits, with the most recent version in the last position of the array. To learn more about how Tweet edits work, see the Tweet edits fundamentals page. 


Certain aspects of the filtered stream endpoint are limited by access level:


**Pro access**


* 1000 rules per stream
* 100 requests per 15 minutes when using the POST /2/tweets/search/stream/rules endpoint to add rules
* Can use all operators when building your rule
* Can build rules up to 1024 characters in length


**Enterprise access**


* 2500+ rules per stream
* 450 requests per 15 minutes when using the POST /2/tweets/search/stream/rules endpoint to add rules
* Tweets/second delivery cap is set at access level for connections
* Can use all operators when building your rule
* Can build rules up to 2048 characters in length
* Can use the recovery and redundancy features to maximize up-time and recover lost data in case of an outage


 


The returned Tweets from filtered stream count towards the monthly Tweet cap.











**Account setup**


To access these endpoints, you will need:


* An approved developer account.
* To authenticate using the keys and tokens from a developer App that is located within a Project.


Learn more about getting access to the Twitter API v2 endpoints in our getting started guide.












Quick start


Sample code


Run in Postman


Try with API Explorer


Build a dashboard to find insights from Twitter data

















Supporting resources
--------------------






Learn how to use Postman to make requests


Troubleshoot an error


Visit the API reference page for this endpoint










Tutorials
---------






Stream Tweets in real-time


Build a trends dashboard with Twitter API Toolkit


Listen for important events


Building an app to stream Tweets in real-time

























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















