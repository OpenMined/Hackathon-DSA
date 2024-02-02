
























































List · CrowdTangle/API Wiki · GitHub














































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




 







List
====



Jump to bottom



 mattynoce edited this page Sep 27, 2019
 ·
 5 revisions



 



### 






 Pages 15







* Home
* Account
* AccountStatistics
* Errors
* Formats
* Leaderboard
* Links
* List
 


	+ List
	+ Properties
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

















 

### List


A List Object represents a list, saved search or saved post list in a dashboard /lists.


#### Properties




| Property | Type | Descriptions |
| --- | --- | --- |
| title | string | The title of the list as it appears in the dashboard |
| id | int | The unique identifier of the list in the CrowdTangle system. Use this id when querying by the `listIds` parameters. |
| type | enum (SAVED\_SEARCH, SAVED\_POSTS, LIST) | The type of the list corresponding with its function in the dashboard. |





 







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
 














































