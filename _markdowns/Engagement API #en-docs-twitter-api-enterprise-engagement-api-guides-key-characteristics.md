



Key characteristics | Docs | Twitter Developer Platform 





































































































Key characteristics



Engagement API key characteristics
----------------------------------


* **RESTful API** serving JSON data, supporting POST requests with JSON data bodies.
* **Types of Requests:** Client apps may make the following types of requests:
	+ **Total engagements** -- HTTP POST request to /totals endpoint
	+ **Last 28-hour engagements** -- HTTP POST request to /28hr endpoint
	+ **Historical engagements** -- HTTP POST request to /historical endpoint
* **OAuth authentication:**
	+ OAuth 1.0 User Context: All available metrics are available for Tweets that are owned by a user that has authorized your App using 3-legged OAuth. You must use that user's Access Tokens when making your request.
	+ OAuth 2.0 Bearer Token: Select metrics (Retweets, Quote Tweets, Replies, Favorites, and Video Views) are available for any public Tweet.
* **Request metadata and structure**: Request data is a JSON object consisting of a Tweet ID array, an array of engagement types, and an engagement grouping structure.
* **Tweets per request:**
	+ /totals endpoint: 250 Tweet IDs
	+ /28hr endpoint: 25 Tweet IDs
	+ /historical endpoint: 25 Tweet IDs
* **Engagement metrics availability:**
	+ **/totals** -- Metric totals since when Tweet was posted. Impressions and Engagements are available for Tweets published in the last 90 days, while Retweets, Quote Tweets, Replies, Favorites, and Video Views are available for all Tweets.
	+ **/28hr** -- Last 28 hours from time of request.
	+ **/historical** -- Any 28-day period starting September 1, 2014.
* **Metric types**: Each request includes an array of Metric Types. The availability of these depends on the endpoint and, if requesting from the /totals endpoint, on whether Tweets are user-permissioned.
	+ /totals endpoint:
		- All Tweets: Favorites, Retweets, Quote Tweets, Replies, and Video Views
		- Requires OAuth 1.0a User Context: Impressions, Engagements, Favorites, Replies, and Retweets
	+ /28hr and /historical endpoints (Requires OAuth 1.0a User Context with Tweet owner's Access Token): Impressions, Engagements, Favorites, Replies, Retweets, URL Clicks, Hashtag Clicks, Detail Click, Permalink Clicks, Media Clicks, App Install Attempts, App Opens, Tweet Emails, Video Views, and Media Views
* **Engagement groupings:** Each request includes an array of Engagement Groupings. With these groupings you can customize how the returned metrics are organized. Up to three groupings can be included with each request. Metrics can be organized by the following values:
	+ All endpoints: Tweet ID, Engagement Type
	+ /28hr and /historical endpoints: These endpoints provide time-series if these additional groupings are specified: Engagement Day, Engagement Hour
* **Integration Expectations:** Your team will be responsible for the following.
	+ Creating and maintaining a client app that can send HTTP requests to the Engagement API that returns engagement metrics for Tweet ID included in request.
* **Limitations**
* Video views are only available for Tweets that are 1800 days old or less.



















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















