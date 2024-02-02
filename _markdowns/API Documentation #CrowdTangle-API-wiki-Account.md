
























































Account · CrowdTangle/API Wiki · GitHub














































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




 







Account
=======



Jump to bottom



 Todd Kamin edited this page Jul 30, 2021
 ·
 23 revisions



 



### 






 Pages 15







* Home
* Account
 


	+ Account
	+ Properties
* AccountStatistics
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

















 

### Account


An Account Object represents a page, account or user on a given platform. See examples in /posts.


#### Properties




| Property | Type | Descriptions |
| --- | --- | --- |
| accountType | string | For Facebook only. Options are facebook\_page, facebook\_profile, facebook\_group. |
| handle | string | The handle or vanity URL of the account. |
| id | int | The unique identifier of the account in the CrowdTangle system. This ID is specific to CrowdTangle, not the platform on which the account exists. |
| name | string | The name of the account. |
| pageAdminTopCountry | string | The ISO country code of the the country from where the plurality of page administrators operate. |
| pageCategory | string | The page category as submitted by the page. View all page categories here. |
| pageCreatedDate | int | The date on which the page was created. |
| pageDescription | string | The description of the page as documented in Page Transparency information. |
| platform | enum (facebook, instagram, reddit) | The platform on which the account exists. |
| platformId | string | The platform's ID for the account. This is not shown for Facebook public users. |
| profileImage | string | A URL pointing at the profile image. |
| subscriberCount | int | The number of subscribers/likes/followers the account has. By default, the subscriberCount property will show page Followers (as of January 26, 2021). You can select either Page Likes or Followers in your Dashboard settings. Learn more here. |
| url | string | A link to the account on its platform. |
| verified | boolean | Whether or not the account is verified by the platform, if supported by the platform. If not supported, will return false. |





 







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
 














































