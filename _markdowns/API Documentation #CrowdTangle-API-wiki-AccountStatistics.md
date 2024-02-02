
























































AccountStatistics · CrowdTangle/API Wiki · GitHub














































Skip to content



















Toggle navigation





Sign in


 










* Product
 






	+ Actions
	 Automate any workflow
	+ Packages
	 Host and manage packages
	+ Security
	 Find and fix vulnerabilities
	+ Codespaces
	 Instant dev environments
	+ Copilot
	 Write better code with AI
	+ Code review
	 Manage code changes
	+ Issues
	 Plan and track work
	+ Discussions
	 Collaborate outside of code


Explore

	+ All features
	+ Documentation
	+ GitHub Skills
	+ Blog
* Solutions
 





For

	+ Enterprise
	+ Teams
	+ Startups
	+ Education


By Solution

	+ CI/CD & Automation
	+ DevOps
	+ DevSecOps


Resources

	+ Learning Pathways
	+ White papers, Ebooks, Webinars
	+ Customer Stories
	+ Partners
* Open Source
 






	+ GitHub Sponsors
	 Fund open source developers



	+ The ReadME Project
	 GitHub community articles


Repositories

	+ Topics
	+ Trending
	+ Collections
* Pricing












Search or jump to...







Search code, repositories, users, issues, pull requests...
==========================================================



 




 Search
 













Clear
 
















































































 



Search syntax tips 














 Provide feedback
==================











 
We read every piece of feedback, and take your input very seriously.




Include my email address so I can be contacted


  Cancel

 Submit feedback










 Saved searches
================


Use saved searches to filter your results more quickly
------------------------------------------------------











 





Name






Query



 To see all available qualifiers, see our documentation.
 


 





  Cancel

 Create saved search







Sign in

Sign up









You signed in with another tab or window. Reload to refresh your session.
You signed out in another tab or window. Reload to refresh your session.
You switched accounts on another tab or window. Reload to refresh your session.
 


Dismiss alert














{{ message }}

















CrowdTangle 
/
**API**
Public



* Notifications
* Fork
 18
* Star
 126







* Code
* Issues
6
* Pull requests
0
* Actions
* Projects
0
* Wiki
* Security
* Insights


 

 


Additional navigation options


 
* Code
* Issues
* Pull requests
* Actions
* Projects
* Wiki
* Security
* Insights




 







AccountStatistics
=================



Jump to bottom



 nobengma edited this page Nov 17, 2020
 ·
 21 revisions



 



### 






 Pages 15







* Home
* Account
* AccountStatistics
 


	+ AccountStatistics
	+ Properties
	+ StatisticSet
	+ SubscriberData
* Errors
* Formats
* Leaderboard
* Links
* List
* List Accounts
* Lists
* Pagination
* Post
* Posts
* Search
* Terms and Policy








* Getting Started


### Endpoints


* /post/:id
* /posts
* /posts/search
* /leaderboard
* /links
* /lists
* /lists/:listId/accounts


### Objects


* Account
* Post
* List
* AccountStatistics


### Additional Information


* Pagination
* Errors
* Formats
* Policy





##### Clone this wiki locally

















 

### AccountStatistics


An AccountStatistics object represents the aggregate statistics of an account over the specified time. A list of these objects makes up a leaderboard, see examples in /leaderboard.


#### Properties




| Property | Type | Description |
| --- | --- | --- |
| account | account | Details about the account not related to statistics. |
| breakdown | Map<String, StatisticSet> | A StatisticSet for each type of post the account posted. E.g. photo, video, etc. |
| subscriberData | SubscriberData | The subscriberCounts relevant to the date range requested. |
| summary | StatisticSet | An aggregate StatisticSet of the `breakdown`. |


### 
StatisticSet


Aggregate data for the account in question. Includes basic metrics (likeCount, commentCount, shareCount) as well as some additional metrics. Some of these metrics are platform specific. See Post/statistics for the by-platform breakdown.




| Property | Type | Description |
| --- | --- | --- |
| angryCount | int | Total number of angrys. |
| commentCount | int | Total number of comments. |
| favoriteCount | int | Total number of favorites. |
| hahaCount | int | Total number of hahas. |
| interactionRate | double | The interactionRate for the given aggregation. This is provided at a percentage. E.g., An `interactionRate` of 1.324 is 1.32%, not 132%. |
| likeCount | int | Total number of likes for given aggregation. |
| loveCount | int | Total number of loves. |
| postCount | int | Total number of posts posted for the given aggregation. |
| repostCount | int | Total number of reposts. |
| sadCount | int | Total number of sads. |
| shareCount | int | Total number of shares. |
| totalInteractionCount | int | The sum of the individual metric counts. E.g., likeCount + shareCount + commentCount. |
| upCount | int | Total number of upvotes. |
| wowCount | int | Total number of wows. |
| careCount | int | Total number of cares. |
| threePlusMinuteVideoCount | int | The count of the aggregation's videos of length 3 minutes or longer. |
| totalVideoTimeMS | int | Total video time in milliseconds. |


### 
SubscriberData


The subscriberData for the given date range.




| Property | Type | Description |
| --- | --- | --- |
| finalCount | int | The number of the subscribers the account had at the end of the date range. |
| initialCount | int | The number of subscribers the account had at the start of the date range. |
| notes | String | Human-readable notes. Counts may not be available for selected date ranges based on when we started tracking an account within CrowdTangle. If initialCount or finalCount is 0, we likely were not tracking the account at that time. This can be confirmed by referencing the notes section which could look like this: "No subscriberCount available for beginning of time range." If the note section is present at all, any calculations made with subscriberCount data will need to take into account potentially missing data. |





 







Footer
------






 © 2024 GitHub, Inc.
 


### Footer navigation


* Terms
* Privacy
* Security
* Status
* Docs
* Contact
* Manage cookies
* Do not share my personal information















 You can’t perform that action at this time.
 














































