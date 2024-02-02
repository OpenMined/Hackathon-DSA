
























































Links · CrowdTangle/API Wiki · GitHub














































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




 







Links
=====



Jump to bottom



 nshiffman edited this page Mar 31, 2021
 ·
 43 revisions



 



### 






 Pages 15







* Home
* Account
* AccountStatistics
* Errors
* Formats
* Leaderboard
* Links
 


	+ GET /links
	+ Endpoint
	+ Parameters
	+ Response
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

















 

GET /links
----------


Retrieve a set of posts matching a certain link. This will return up to 1000 posts. This endpoint only pulls data from CrowdTangle. To access interaction metrics across the entirety of Facebook, use this Graph API endpoint.


#### Endpoint


`GET https://api.crowdtangle.com/links`


#### Parameters


Note: **Please use startDate!** Our system works much more quickly (and with much less strain) when it only has to search a subset of dates for your data. If you're looking only for posts in 2019, put in a startDate of 2019-01-01 and our system will know it can ignore years' worth of data. If the URL you're interested in was published yesterday, put that in and it will return very quickly! We're not making startDate mandatory, but please strongly consider using it!




| Parameter | Default | Options | Description |
| --- | --- | --- | --- |
| count | 100 | 1 - 1000 | The number of posts to return. |
| endDate | now | - | The latest date at which a post could be posted. Time zone is UTC. Format is “yyyy-mm-ddThh:mm:ss” or “yyyy-mm-dd”. |
| includeHistory | `null` (does not include) | `true` | Includes timestep data for growth of each post returned. Note that we will not have time-series data for posts that were created after the account was added to CrowdTangle. |
| link | `null` | - | The link to query by. Required. |
| includeSummary | `false` | `true`, `false` | Adds a "summary" section with AccountStatistics for each platform that has posted this link. It will look beyond the count requested to summarize across the time searched. Requires a value for startDate. |
| offset | 0 | >= 0 | The number of posts to offset (generally used for pagination). Pagination links will also be provided in the response. |
| platforms | `null` (i.e., all platforms) | `facebook`, `instagram`, `reddit` (reddit is not currently available for the ACADEMICS vertical) | The platforms from which to retrieve links. This value can be comma-separated. |
| searchField | `null` (i.e., does not support query strings) | `Include_query_strings` | Allows you to search URLs containing query strings. |
| startDate | 0000-00-00 | - | The earliest date at which a post could be posted. Time zone is UTC. Format is “yyyy-mm-ddThh:mm:ss” or “yyyy-mm-dd” (defaults to time 00:00:00). |
| sortBy | `date` | `subscriber_count`, `total_interactions` | The method by which to order posts (defaults to the most recent). If `subscriber_count`, a startDate is required. |


#### Response


This returns the same response as /posts. There is no option for pagination on a links request.





 







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
 














































