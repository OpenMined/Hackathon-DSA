



Search Tweets introduction | Docs | Twitter Developer Platform 






































































































Introduction






Introduction
------------


Searching for Tweets is an important feature used to surface Twitter conversations about a specific topic or event. While this functionality is present in Twitter, these endpoints provide greater flexibility and power when filtering for and ingesting Tweets so you can find relevant data for your research more easily; build out near-real-time ‘listening’ applications; or generally explore, analyze, and/or act upon Tweets related to a topic of interest. 


We offer two endpoints that allow you to search for Tweets: Recent search and full-archive search. Both of these REST endpoints share a common design and features, including their use of a single search query to filter for Tweets around a specific topic. These search queries are created with a set of operators that match on Tweet and user attributes, such as message keywords, hashtags, and URLs. Operators can be combined into queries with boolean logic and parentheses to help refine the queries matching behavior. 


Both the recent search and the full-archive search endpoints provide edited Tweet metadata. All objects for Tweets created since September 29, 2022, include Tweet edit metadata, even if the Tweet was never edited. Each time a Tweet is edited, a new Tweet ID is created. A Tweet's edit history is documented by an array of Tweet IDs, starting with the original ID.


These endpoints will always return the most recent edit, along with any edit history. Any Tweet collected after its 30-minute edit window will represent its final version. To learn more about Edit Tweet metadata, check out the Edit Tweets fundamentals page.


Once you’ve set up your query and start receiving Tweets, these endpoints support navigating the results both by time and Tweet ID ranges. This is designed to support two common use cases: 


* **Get historical**: Requests are for a period of interest, with no focus on the real-time nature of the data. A single request is made, and all matching data is delivered using pagination as needed. This is the default mode for Search Tweets.
* **Polling** or **listening**: Requests are made in a "any new Tweets since my last request?" mode. Requests are made on a continual basis, and typically there is a use case focused on near real-time 'listening' for Tweets of interest.


Many operators and query limits are exclusive to Enterprise access, meaning that you must use keys and tokens from an App within a Project with Enterprise access to utilize the additional functionality. You can learn more about this in the endpoint sections below.


Both the recent search and the full-archive search endpoints returned Tweets contribute to the monthly Tweet cap.











**Account setup**


To access these endpoints, you will need:


* An approved developer account.
* To authenticate using the keys and tokens from a developer App that is located within a Project.


Learn more about getting access to the Twitter API v2 endpoints in our getting started guide.









### 


### Recent search


The recent search endpoint allows you to programmatically access filtered public Tweets posted over the last week, and is available to all developers who have a developer account and are using keys and tokens from an App within a Project.


You can authenticate your requests with OAuth 1.0a User Context, OAuth 2.0 App-Only, or OAuth 2.0 Authorization Code with PKCE. However, if you would like to receive private metrics, or a breakdown of organic and promoted metrics within your Tweet results, you will have to use OAuth 1.0a User Context or OAuth 2.0 Authorization Code with PKCE, and pass user Access Tokens that are associated with the user that published the given content. 


This endpoint can deliver up to 100 Tweets per request in reverse-chronological order, and pagination tokens are provided for paging through large sets of matching Tweets. 


When using a Project with regular access, you can use the basic set of operators and can make queries up to 512 characters long. When using a Project with Enterprise access, you have access to additional operators. Projects with Enterprise Access can make queries up to 4096 characters long.


Learn more about access levels.  

  




### Full-archive search


The v2 full-archive search endpoint is only available to Projects with Enteprise access. The endpoint allows you to programmatically access public Tweets from the complete archive dating back to the first Tweet in March 2006, based on your search query.


You can authenticate your requests to this endpoint using OAuth 2.0 App-Only, and the App Access Token must come from an App that is within a Project that has Enterprise access. Since you cannot make a request on behalf of other users (OAuth 1.0a User Context or OAuth 2.0 Authorization Code with PKCE) with this endpoint, you will not be able to pull private metrics. 


This endpoint can deliver up to 500 Tweets per request in reverse-chronological order, and pagination tokens are provided for paging through large sets of matching Tweets.


**Note:** If requesting annotations through the tweet.fields parameter, the max\_results parameter is currently limited to a max value of 100. This may change in the future, but please be mindful of this limitation.


Since this endpoint is only available to those that have been approved for Enterprise access, you have access to the full set of search operators and can make queries up to 1024 characters long.


 









Quick start


Sample code


Search Tweets Python client


Search Tweets Ruby client


Run in Postman


Try with API Explorer


Search and Visualize Tweets

















Supporting resources
--------------------






Learn how to use Postman to make requests


Troubleshoot an error


Visit the API reference page










Tutorials
---------






Analyze past conversations


Explore a user's Tweets


Building high-quality filters for getting Twitter data


Step-by-step guide on making a request to recent search


Getting started with converting JSON objects to CSV


A guide to full-archive search, for academic researchers


Process, analyze, and visualize Tweets with Google Cloud

























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















