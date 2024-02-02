
Post · CrowdTangle/API Wiki · GitHub

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

Post
====

Jump to bottom

 nshiffman edited this page Dec 15, 2020
 ·
 63 revisions

### Post

A post object represents a single post from any of the supported platforms (e.g., Facebook, Instagram). All posts also contain an account object. Below are the properties of a post. See examples in /posts.

#### Properties

| Property | Type | Description |
| --- | --- | --- |
| account | Account | See account. |
| brandedContentSponsor | Account | See account. This field is only present for Facebook Page posts where there is a sponsoring Page. |
| caption | text | The caption to a photo, if available. |
| date | date ("yyyy‑mm‑dd hh:mm:ss") | The date and time the post was published. Time zone is UTC. |
| description | text | Further details, if available. Associated with links or images across different platforms. |
| expandedLinks | map of text | A map where the keys are the original links that came in the post (which are often shortened), and the values are the expanded links. |
| id | string ("account.id|postExternalId") | The unique identifier of the post in the CrowdTangle system. This ID is specific to CrowdTangle, not the platform from which the post originated. |
| imageText | string | The text, if it exists, within an image. |
| legacyid | int | The legacy version of the unique identifier of the post in the CrowdTangle system. This ID is specific to CrowdTangle, not the platform from which the post originated. |
| link | string | An external URL that the post links to, if available. (Facebook only) |
| media | array of media | An array of available media for the post. |
| message | text | The user-submitted text on a post. |
| platform | enum (facebook, instagram, reddit) | The platform on which the post was posted. E.g., Facebook, Instagram, etc. |
| platformId | string | The platform's ID for the post. |
| postUrl | string | The URL to access the post on its platform. |
| score | double | The score of a post as measured by the request. E.g. it will represent the overperforming score if the request `sortBy` specifies `overperforming`, the interaction rate if the request specifies `interaction_rate`, etc. |
| statistics | Statistics | Performance metrics associated with the post. |
| subscriberCount | int | The number of subscriber the account had *when the post was published*. This is in contrast to the subscriberCount found on the account, which represents the current number of subscribers an account has. |
| type | enum (album, igtv, link, live\_video, live\_video\_complete, live\_video\_scheduled, native\_video, photo, status, video, vine, youtube) | The type of the post. |
| updated | date ("yyyy‑mm‑dd hh:mm:ss") | The date and time the post was most recently updated in CrowdTangle, which is most often via getting new scores from the platform. Time zone is UTC. |
| videoLengthMS | int | The length of the video in milliseconds. |
| liveVideoStatus | string ("live", "completed", "upcoming") | The status of the live video. |

### 
Statistics

Two sets of metrics for a post: `actual` and `expected`. `actual` represents the actual metrics of the post, e.g., likeCount or commentCount. `expected` represents what that post's metrics were expected to be given that post's properties, as calculated by CrowdTangle. These metrics differ by `platform`. For instance, Facebook will include, "likeCount," "commentCount," and "shareCount" while Instagram includes "favoriteCount" and "commentCount." The full list is below.

#### Properties

| Property | Type | Description |
| --- | --- | --- |
| actual | Map<String, Long> | A set of key-value pairs representing the actual metrics of the post. |
| expected | Map<String, Long> | A set of key-values pairs representing the metrics CrowdTangle expected a post like this to accrue. |

##### Possible Metrics

| Property | platforms |
| --- | --- |
| angryCount | Facebook |
| commentCount | Facebook, Instagram, Reddit |
| favoriteCount | Instagram |
| hahaCount | Facebook |
| likeCount | Facebook |
| loveCount | Facebook |
| sadCount | Facebook |
| shareCount | Facebook |
| upCount | Reddit |
| wowCount | Facebook |
| thankfulCount\* | Facebook |
| careCount | Facebook |

\*The purple flower "Thankful" reaction was a temporary reaction available in 2016 and 2017. (See more HERE). This metric surfaces thankfulCount for legacy posts that accrued Thankful reactions prior to the reaction's removal from Facebook.

### 
Media

The media object represents a piece of media (e.g., video, photo) for a post. It contains the type, source and any additional metadata.

#### Properties

| Property | Type | Description |
| --- | --- | --- |
| full | string | The source of the full-sized version of the media. |
| height | int | The height of the media. |
| type | enum (photo or video) | The type of the media. |
| url | string | The source of the media. |
| width | int | The width of the media. |

### 

Toggle tagle of contents
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

	+ Post
	+ Properties
	+ Statistics
	+ Properties
	+ Possible Metrics
	+ Media
	+ Properties
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