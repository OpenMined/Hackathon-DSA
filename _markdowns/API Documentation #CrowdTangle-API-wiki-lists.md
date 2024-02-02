
























































Lists · CrowdTangle/API Wiki · GitHub














































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




 







Lists
=====



Jump to bottom



 nobengma edited this page Oct 29, 2020
 ·
 9 revisions



 



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

















 

GET /lists
----------


Retrieve the lists, saved searches and saved post lists of the dashboard associated with the token sent in.


#### Endpoint


`GET https://api.crowdtangle.com/lists`


#### Parameters


This endpoint accepts no parameters other than the token.


#### Response


The Response contains both a status code and a result. The status will always be 200 if there is no error. The result contains an array of list objects.



```
//Call: https://api.crowdtangle.com/lists?token=TOKEN
{
    "status": 200,
    "result": {
        "lists": [
            {
                "id": 1172985,
                "title": "Music Media & Artist Pages",
                "type": "LIST"
            },
            {
                "id": 1177583,
                "title": "Television",
                "type": "LIST"
            },
            {
                "id": 1191568,
                "title": "candidato presidencial, presidente, elección",
                "type": "SAVED_SEARCH"
            },
            {
                "id": 1224851,
                "title": "Test",
                "type": "SAVED_POSTS"
            },
            {
                "id": 1391155,
                "title": "Women of the US Senate",
                "type": "LIST"
            },
            {
                "id": 1394602,
                "title": "coronavirus, 2019nCoV, covid19, covid-19, covid",
                "type": "SAVED_SEARCH"
            },
            {
                "id": 1424665,
                "title": "2020 US Election",
                "type": "LIST"
            },
            {
                "id": 1447044,
                "title": "APAC Media",
                "type": "LIST"
            }
            
        ]
    }
}

```




 







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
 














































