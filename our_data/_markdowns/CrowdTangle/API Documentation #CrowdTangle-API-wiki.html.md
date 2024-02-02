
Home · CrowdTangle/API Wiki · GitHub

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

Home
====

Jump to bottom

 nshiffman edited this page Dec 15, 2020
 ·
 28 revisions

### Getting Started

Welcome to the CrowdTangle API! You can use the CrowdTangle API to access posts, the leaderboard and the link-checker. Please contact your CrowdTangle representative for access. If you have access to the API, you can locate your API token via your dashboard under Settings > API Access.

#### Authentication

The CrowdTangle API expects the API token to be included either as a custom header with the name `x-api-token` or as a `token` query parameter.

```
// as a custom header
curl "https://api.crowdtangle.com/posts"
  -H "x-api-token: your-api-token"
// as a query parameter 
curl "https://api.crowdtangle.com/posts?token=your-api-token"
```
#### Making a Request

All requests to the CrowdTangle API are made via GET to `https://api.crowdtangle.com/`. You must use https. Please visit the API Cheat Sheet to understand how pagination works with our API.

Below are the available endpoints:

##### GET /posts

##### GET /post

##### GET /posts/search

##### GET /leaderboard

##### GET /links

##### GET /lists

##### Postman Template

Postman is a free API management software. Click here to download a JSON file that you can import into Postman (unzip the file to access), and get a template for each endpoint. Please note that all parameters may not be present in the template; please view the Github API documentation to explore all parameter options.

Happy coding!

### 

Toggle tagle of contents
Pages 15

* Home

	+ Getting Started
	+ Authentication
	+ Making a Request
	+ GET /posts
	+ GET /post
	+ GET /posts/search
	+ GET /leaderboard
	+ GET /links
	+ GET /lists
	+ Postman Template
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