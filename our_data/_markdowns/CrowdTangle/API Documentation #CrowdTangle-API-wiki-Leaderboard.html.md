
Leaderboard · CrowdTangle/API Wiki · GitHub

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

Leaderboard
===========

Jump to bottom

 nobengma edited this page Nov 17, 2020
 ·
 30 revisions

GET /leaderboard
----------------

Retrieves leaderboard data for a certain list or set of accounts.

#### Endpoint

`GET https://api.crowdtangle.com/leaderboard`

#### Parameters

| Parameter | Default | Options | Description |
| --- | --- | --- | --- |
| accountIds | - | - | A list of CrowdTangle accountIds to retrieve leaderboard data for. These should be provided comma-separated. This and listId are mutually exclusive; if both are sent, accountIds will be preferred. |
| count | `50` | `1-100` | The number of AccountStatistics to return. |
| endDate | now | - | The endDate of the leaderboard range. Time zone is UTC. Format is “yyyy-mm-ddThh:mm:ss” or “yyyy-mm-dd” (defaults to time 00:00:00). |
| listId | 0 (i.e. the entire dashboard) | - | The list of the leaderboard to retrieve. This and accountIds are mutually exclusive; if both are sent, accountIds will be preferred. |
| offset | `0` | `> 0` | The number of rows to offset (generally used for pagination). Pagination links will also be provided in the response. |
| orderBy | `desc` | `asc` or `desc` | the order of the sort. |
| sortBy | `total_interactions` | `total_interactions`, `interaction_rate` | The method by which the accountStatistics are sorted. |
| startDate | One day earlier than `endDate` | - | The startDate of the leaderboard rage. Time zone is UTC. Format is “yyyy-mm-ddThh:mm:ss” or “yyyy-mm-dd” (defaults to time 00:00:00). This must be before endDate. |

#### Response

The Response contains both a status code and a result. The status will always be 200 if there is no error. The result contains an array of accountStatistics objects and a pagination object with URLs for both the next and previous pages, if they exist. Below is an example response.

```
//Call: https://api.crowdtangle.com/leaderboard?token=TOKEN&count=2&listId=73928&orderBy=desc
{
    "status": 200,
    "result": {
        "accountStatistics": [
            {
                "account": {
                    "id": 19951,
                    "name": "ABS-CBN News",
                    "handle": "abscbnNEWS",
                    "profileImage": "https://scontent-sea1-1.xx.fbcdn.net/v/t1.0-1/p200x200/96088298_10158305548140168_1839350273139539968_n.jpg?_nc_cat=1&ccb=2&_nc_sid=dbb9e7&_nc_ohc=QSY0Yoco5BQAX9fb5os&_nc_ht=scontent-sea1-1.xx&tp=6&oh=8040b4f43cf3be6c5bef5d7749e853e6&oe=5FC002EA",
                    "subscriberCount": 18899596,
                    "url": "https://www.facebook.com/27254475167",
                    "platform": "Facebook",
                    "platformId": "27254475167",
                    "accountType": "facebook_page",
                    "pageAdminTopCountry": "PH",
                    "verified": true
                },
                "summary": {
                    "loveCount": 288478,
                    "threePlusMinuteVideoCount": 14,
                    "totalInteractionCount": 1307675,
                    "wowCount": 63029,
                    "thankfulCount": 0,
                    "interactionRate": 0.025624886373232528,
                    "likeCount": 527989,
                    "hahaCount": 49635,
                    "commentCount": 112467,
                    "shareCount": 152661,
                    "careCount": 9825,
                    "sadCount": 97952,
                    "angryCount": 5639,
                    "totalVideoTimeMS": 5169184,
                    "postCount": 270
                },
                "breakdown": {
                    "native_video": {
                        "loveCount": 741,
                        "threePlusMinuteVideoCount": 2,
                        "totalInteractionCount": 8371,
                        "wowCount": 76,
                        "thankfulCount": 0,
                        "interactionRate": 0.0040265410964340186,
                        "likeCount": 4818,
                        "hahaCount": 558,
                        "commentCount": 475,
                        "shareCount": 966,
                        "careCount": 45,
                        "sadCount": 671,
                        "angryCount": 21,
                        "totalVideoTimeMS": 1162942,
                        "postCount": 11
                    },
                    "owned_video": {
                        "loveCount": 1300,
                        "threePlusMinuteVideoCount": 14,
                        "totalInteractionCount": 25366,
                        "wowCount": 204,
                        "thankfulCount": 0,
                        "interactionRate": 0.004063578925179141,
                        "likeCount": 12782,
                        "hahaCount": 1155,
                        "commentCount": 2081,
                        "shareCount": 4139,
                        "careCount": 116,
                        "sadCount": 3339,
                        "angryCount": 250,
                        "totalVideoTimeMS": 5169184,
                        "postCount": 33
                    },
                    "crosspost": {
                        "loveCount": 559,
                        "threePlusMinuteVideoCount": 12,
                        "totalInteractionCount": 16995,
                        "wowCount": 128,
                        "thankfulCount": 0,
                        "interactionRate": 0.004084743398747783,
                        "likeCount": 7964,
                        "hahaCount": 597,
                        "commentCount": 1606,
                        "shareCount": 3173,
                        "careCount": 71,
                        "sadCount": 2668,
                        "angryCount": 229,
                        "totalVideoTimeMS": 4006242,
                        "postCount": 22
                    },
                    "link": {
                        "loveCount": 27310,
                        "totalInteractionCount": 209492,
                        "wowCount": 7222,
                        "thankfulCount": 0,
                        "interactionRate": 0.006121823979729514,
                        "likeCount": 74381,
                        "hahaCount": 14693,
                        "commentCount": 26168,
                        "shareCount": 24451,
                        "careCount": 1011,
                        "sadCount": 31894,
                        "angryCount": 2362,
                        "postCount": 181
                    },
                    "photo": {
                        "loveCount": 259868,
                        "totalInteractionCount": 1072817,
                        "wowCount": 55603,
                        "thankfulCount": 0,
                        "interactionRate": 0.10136195503861564,
                        "likeCount": 440826,
                        "hahaCount": 33787,
                        "commentCount": 84218,
                        "shareCount": 124071,
                        "careCount": 8698,
                        "sadCount": 62719,
                        "angryCount": 3027,
                        "postCount": 56
                    }
                },
                "subscriberData": {
                    "initialCount": 18899596,
                    "finalCount": 18899596
                }
            },
            {
                "account": {
                    "id": 19950,
                    "name": "GMA News",
                    "handle": "gmanews",
                    "profileImage": "https://scontent-sea1-1.xx.fbcdn.net/v/t1.0-1/p200x200/18485481_10155134880371977_7256210016168898917_n.png?_nc_cat=1&ccb=2&_nc_sid=dbb9e7&_nc_ohc=fgpfHmrieOcAX-GcFmS&_nc_ht=scontent-sea1-1.xx&oh=ff167f2eb43efb84e6f1c9751674abee&oe=5FC0FE2E",
                    "subscriberCount": 15333315,
                    "url": "https://www.facebook.com/116724526976",
                    "platform": "Facebook",
                    "platformId": "116724526976",
                    "accountType": "facebook_page",
                    "pageAdminTopCountry": "PH",
                    "verified": true
                },
                "summary": {
                    "loveCount": 210622,
                    "threePlusMinuteVideoCount": 38,
                    "totalInteractionCount": 1195694,
                    "wowCount": 42123,
                    "thankfulCount": 0,
                    "interactionRate": 0.038034828085120535,
                    "likeCount": 534466,
                    "hahaCount": 38910,
                    "commentCount": 130039,
                    "shareCount": 133426,
                    "careCount": 8274,
                    "sadCount": 80358,
                    "angryCount": 17476,
                    "totalVideoTimeMS": 26721066,
                    "postCount": 205
                },
                "breakdown": {
                    "native_video": {
                        "loveCount": 810,
                        "threePlusMinuteVideoCount": 3,
                        "totalInteractionCount": 11762,
                        "wowCount": 536,
                        "thankfulCount": 0,
                        "interactionRate": 0.004506527127369392,
                        "likeCount": 5445,
                        "hahaCount": 287,
                        "commentCount": 2523,
                        "shareCount": 1152,
                        "careCount": 47,
                        "sadCount": 481,
                        "angryCount": 481,
                        "totalVideoTimeMS": 731320,
                        "postCount": 17
                    },
                    "owned_video": {
                        "loveCount": 5886,
                        "threePlusMinuteVideoCount": 25,
                        "totalInteractionCount": 96042,
                        "wowCount": 2400,
                        "thankfulCount": 0,
                        "interactionRate": 0.012782623979224323,
                        "likeCount": 38531,
                        "hahaCount": 8676,
                        "commentCount": 11158,
                        "shareCount": 14581,
                        "careCount": 410,
                        "sadCount": 9807,
                        "angryCount": 4593,
                        "totalVideoTimeMS": 9241758,
                        "postCount": 49
                    },
                    "crosspost": {
                        "loveCount": 5076,
                        "threePlusMinuteVideoCount": 22,
                        "totalInteractionCount": 84280,
                        "wowCount": 1864,
                        "thankfulCount": 0,
                        "interactionRate": 0.017171759661886554,
                        "likeCount": 33086,
                        "hahaCount": 8389,
                        "commentCount": 8635,
                        "shareCount": 13429,
                        "careCount": 363,
                        "sadCount": 9326,
                        "angryCount": 4112,
                        "totalVideoTimeMS": 8510438,
                        "postCount": 32
                    },
                    "link": {
                        "loveCount": 14972,
                        "totalInteractionCount": 239004,
                        "wowCount": 6058,
                        "thankfulCount": 0,
                        "interactionRate": 0.016063062684096685,
                        "likeCount": 93803,
                        "hahaCount": 9546,
                        "commentCount": 37201,
                        "shareCount": 32432,
                        "careCount": 1286,
                        "sadCount": 34411,
                        "angryCount": 9295,
                        "postCount": 97
                    },
                    "photo": {
                        "loveCount": 189496,
                        "totalInteractionCount": 855693,
                        "wowCount": 33541,
                        "thankfulCount": 0,
                        "interactionRate": 0.12682841251223234,
                        "likeCount": 399963,
                        "hahaCount": 20550,
                        "commentCount": 80677,
                        "shareCount": 85517,
                        "careCount": 6536,
                        "sadCount": 35843,
                        "angryCount": 3570,
                        "postCount": 44
                    },
                    "share": {
                        "loveCount": 268,
                        "threePlusMinuteVideoCount": 13,
                        "totalInteractionCount": 4940,
                        "wowCount": 124,
                        "thankfulCount": 0,
                        "interactionRate": 0.0022956549187178373,
                        "likeCount": 2157,
                        "hahaCount": 138,
                        "commentCount": 1000,
                        "shareCount": 896,
                        "careCount": 42,
                        "sadCount": 297,
                        "angryCount": 18,
                        "totalVideoTimeMS": 17479308,
                        "postCount": 14
                    },
                    "status": {
                        "loveCount": 0,
                        "totalInteractionCount": 15,
                        "wowCount": 0,
                        "thankfulCount": 0,
                        "interactionRate": 9.782620392263512E-5,
                        "likeCount": 12,
                        "hahaCount": 0,
                        "commentCount": 3,
                        "shareCount": 0,
                        "careCount": 0,
                        "sadCount": 0,
                        "angryCount": 0,
                        "postCount": 1
                    }
                },
                "subscriberData": {
                    "initialCount": 15333315,
                    "finalCount": 15333315
                }
            }
        ],
        "pagination": {
            "nextPage": "https://api.crowdtangle.com/leaderboard?token=TOKEN&orderBy=desc&sortBy=total_interactions&count=2&listId=73928&offset=2"
        }
    }
}
```
Important Notes:

* subscriberData: Counts may not be available for selected date ranges based on when we started tracking an account within CrowdTangle. If initialCount or finalCount is 0, we likely were not tracking the account at that time. This can be confirmed by referencing the notes section which could look like this: "No subscriberCount available for beginning of time range." If the note section is present at all, any calculations made with subscriberCount data will need to take into account potentially missing data.

### 

Toggle tagle of contents
Pages 15

* Home
* Account
* AccountStatistics
* Errors
* Formats
* Leaderboard

	+ GET /leaderboard
	+ Endpoint
	+ Parameters
	+ Response
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