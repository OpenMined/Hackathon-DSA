



Engagement API | Twitter API | Docs | Twitter Developer Platform 





































































































Overview








Overview
--------


Enterprise


*This is an enterprise API available within our managed access levels only. To use this API, you must first set up an account with our enterprise sales team. Learn more*  




The Engagement API provides access to Tweet impression and engagement metrics. While most metrics and endpoints require you to authenticate using OAuth 1.0a User Context, you can access public Favorite, Retweet, Reply, and Video Views metrics using OAuth 2.0 Bearer Token and the /totals endpoint.  


**Note:** You may observe differences between reported data on some of the Twitter web dashboards, and the data reported in the Engagement API. These differences occur because the web dashboards typically only show engagements and/or impressions that occurred within the selected time range. For example, a web dashboard may show engagement on Tweets within the span of a calendar month, while the Engagement API may show engagements that fall beyond the span of that month, but within the time range requested. The Engagement API should be seen as the valid source, in these cases.  

 


### Request endpoints


The Engagement API has three endpoints:


#### Current Totals: /totals


* Requests return a total metric for impressions and a total metric for engagements for the desired Tweets
* Limited to the following metrics: Impressions, Engagements, Favorites, Replies, Retweets, Quote Tweets, and Video Views
* Supports the ability to retrieve **Impressions** and **Engagements** metrics for Tweets created **within the last 90 days** using OAuth 1.0a User Context
* Supports the ability to retrieve **Favorites, Retweets, Quote Tweets, Replies,** and **Video Views** metrics for **any Tweet** using OAuth 2.0 Bearer token
* The results are based on the current total of impressions and engagements at the time the request is made
* Ideal for powering a dashboard report and for calculating engagement rates across a variety of @handles
* Supports requesting metrics for up to 250 Tweets per request


#### Last 28 hours: /28hr


* Requests can return a total metric for impressions, a total metric for engagements, and breakdown of individual engagement metrics that have occurred in the last 28 hours
* Data can be grouped by Tweet ID, and in time-series in aggregate, by day, or by hour
* Ideal for tracking the performance of recently created content
* Supports all available metrics
* Supports requesting metrics for up to 25 Tweets per request


#### Historical: /historical


* Requests can return impressions, engagements, and a breakdown of individual engagement metrics for the most recent one year, based on the engagement time (not the Tweet creation time).
* Requests support a start date and end date parameter, providing flexibility to narrow into a specific time frame up to 4 weeks in duration.
* Tweet engagement data is limited to only 365 days in the past.
* Data can be grouped by Tweet ID, and in time-series in aggregate, by day, or by hour.
* Ideal for evaluating recent performance against a historical benchmark or developing a historical picture of an @handle’s performance.
* Supports all available metrics.
* Supports requesting metrics for up to 25 Tweets per request.


### Available metrics


The table below describes the types of metrics that can be accessed through the Engagement API.


Please check out our Interpreting the metrics page to learn more about the below metrics.


 




| Metric | Endpoint Availability | User Context Required | Description |
| --- | --- | --- | --- |
| impressions | All | Yes | A count of how many times the Tweet has been viewed. This metric is only available for Tweets that have been posted within the past 90 days. |
| engagements | All | Yes | A count of the number of times a user has interacted with the Tweet. This metric is only available for Tweets that have been posted within the past 90 days. |
| favorites | All | Yes - /28hrs & /Historical
No - /totals | A count of how many times the Tweet has been favorited.  |
| retweets | All | Yes - /28hrs & /Historical
No - /totals | A count of how many times the Tweet has been Retweeted. |
| quote\_tweets | /totals | No - /totals | A count of times a Tweet has been Retweeted with a comment (also known as Quote). |
| replies | All | Yes - /28hrs & /Historical
No - /totals | A count of how many times the Tweet has been replied to. |
| video\_views | All | Yes - /28hrs & /Historical
No - /totals | A count of how many times a video in the given Tweet has been 50% visible for at least two seconds.
Video views are only available for Tweets that are 1800 days old or less. If you try to request video views for any Tweets older than 1800 days, you will receive the following object within your response, along with a separate object that contains any other metrics that you requested:
"unsupported\_for\_video\_views\_tweet\_ids": ["TWEET\_ID"]
**Please note:** You may see a discrepancy between the video views metric displayed in the Twitter owned and operated platforms (mobile app and website) and the number that you receive via the /28hr and /historical endpoints.
* The video views displayed in the Twitter user interface and with the /totals endpoint will display the video view aggregated across all Tweets in which the given video has been posted. That means that the metric displayed in the UI includes the combined views from any instance where the video has been Retweeted or reposted in separate Tweets. This metric does not include video views on gifs.
* The video views provided by the /28hr and /historical endpoints will just include those views generated by the specific Tweet for which you are pulling metrics. This metric does not include video views on gifs.
 |
| media\_views | /28hr /historical
 | Yes | A count of all views (autoplay and click) of your media counted across videos, gifs, and images. |
| media\_engagements
(formerly Media Clicks) | /28hr /historical | Yes | A count of how many times media such as an image or video in the Tweet has been clicked. |
| url\_clicks | /28hr /historical | Yes | A count of how many times a URL in the Tweet has been clicked. |
| hashtag\_clicks | /28hr /historical | Yes | A count of how many times a hashtag in the Tweet has been clicked. |
| detail\_expands | /28hr /historical | Yes | A count of how many times the Tweet has been clicked to see more details. |
| permalink\_clicks | /28hr /historical | Yes | A count of how many times the permalink to the Tweet (the individual web page dedicated to this Tweet) has been clicked. |
| app\_install\_attempts | /28hr /historical | Yes | A count of how many times an App Install event has occurred from the Tweet |
| app\_opens | /28hr /historical | Yes | A count of how many times an App Open event has occurred from the Tweet. |
| email\_tweet | /28hr /historical | Yes | A count of how many times the Tweet has been shared via email. |
| user\_follows | /28hr /historical | Yes | A count of how many times the User (Tweet author) has been followed from this Tweet. |
| user\_profile\_clicks | /28hr /historical | Yes | A count of how many times the User (Tweet author) has had their profile clicked from this Tweet. |


 


### Engagement groupings


Groupings enable custom organization of the returned engagement metrics. You can include a maximum of 3 groupings per request. You can choose to group the metrics by one or more of the following values:


*All three endpoints support:*


* tweet.id
* engagement.type


*The `/28hr` and `/historical` can provide time-series metrics, and thus support:*


* engagement.day
* engagement.hour


To learn more about grouping, please visit the Engagement API Grouping page within the Guides section.  

  




Next steps
----------


* Check out our 'Getting started' guide for the Engagement API.
* Figure out which Engagement API endpoint is right for you.
* Learn more about some of the recent changes to the Engagement API here.
* Check out our API references to learn more about how to programmatically access Tweet engagement metrics.
* Key Characteristics - serves as a one-page developer’s checklist of API features and details.
* Explore our sample code:  

	+ Example Ruby client. This example Engagement API Client helps manage the process of generating engagement metadata for large Tweet collections. The client has a helper feature that can surface 'Top Tweets.' As engagement metrics are retrieved, on a Tweet-by-Tweet basis, this client maintains a list of 'Top Tweets' with the highest levels of engagement. For example, if you are processing 100,000 Tweets, it can compile the top 10 for Retweets or any other available metric. The  repository includes an extensive README, which serves as an additional source of ‘getting started’ material and orientation for how the API works.
	+ Example Python client. This example illustrates using OAuth with the Requests package. The client also has an aggregating function for the /historical endpoint that combines API results over an arbitrary time period longer than 28 days.
























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















