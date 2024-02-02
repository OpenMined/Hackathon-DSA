
Errors · CrowdTangle/API Wiki · GitHub

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

Errors
======

Jump to bottom

 mattynoce edited this page Feb 12, 2016
 ·
 4 revisions

### Errors

Every error returned by the CrowdTangle API will assume a standard format. The API will additionally return a proper http status as well. If a `200` is returned, there was no error.

#### Error Response

| Property | Type | Description |
| --- | --- | --- |
| code | int | The CrowdTangle error code, if available. |
| message | string | A human-readable message describing the error. Always returned. |
| status | int | The HTTP status code, if available. |
| url | string | A URL for more information, if available. |

For example:

```
{
  "status": 401,
  "code": 30,
  "message": "Please supply an API token"
}
```
#### 
CrowdTangle Error Codes

| Code | Description |
| --- | --- |
| 20 | Unknown Parameter |
| 21 | Illegal Parameter Value |
| 22 | Missing Parameter |
| 30 | Missing Token |
| 31 | Invalid Token |
| 40 | Does Not Exist |
| 41 | Not Allowed |

### 

Toggle tagle of contents
Pages 15

* Home
* Account
* AccountStatistics
* Errors

	+ Errors
	+ Error Response
	+ CrowdTangle Error Codes
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

Footer
------

 © 2024 GitHub, Inc.

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