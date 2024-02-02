
























































Search · CrowdTangle/API Wiki · GitHub














































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




 







Search
======



Jump to bottom



 nshiffman edited this page Jun 29, 2021
 ·
 62 revisions



 



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
 


	+ GET /posts/search
	+ Endpoint
	+ Calculating the number of responses
	+ Parameters
	+ Response
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

















 

GET /posts/search
-----------------


*Note: Access to the Search is restricted to a limited set customers and usage requires prior approval by CrowdTangle. Apply here to activate Search.*


Retrieve a set of posts for the given parameters and search terms. This endpoint, unlike the main `/posts` endpoint, searches the entire, cross-platform CrowdTangle system of posts. It can be limited by lists and accounts, but by default will search beyond the dashboard the token is associated with.


**If you submit a query with a blank searchTerm (i.e., searchTerm=" "), the result set will be limited to the Dashboard associated with the supplied API token. System-wide blank searches are not supported by default. Please reach out to support@crowdtangle.com for more information.**


#### Endpoint


`GET https://api.crowdtangle.com/posts/search`


#### Calculating the number of responses


To calculate the number of responses you'll get for each query, request activation of the hitCount setting here. Once it's activated, make the query with your full date ranges and `count = 0`. This will return the total number of matches for the search within your date range as a hitCount property.


#### Parameters


Note: **Please use startDate!** Our system works much more quickly (and with much less strain) when it only has to search a subset of dates for your data. If you're looking only for posts in 2019, put in a startDate of 2019-01-01 and our system will know it can ignore years' worth of data. If the event you're interested in happened yesterday, put that in and it will return very quickly! We're not making startDate mandatory, but please strongly consider using it!




| Parameter | Default | Options | Description |
| --- | --- | --- | --- |
| accounts | `null` (any account in the List or Dashboard) | a string corresponding to account handles (ie iamcardib) or platform IDs (ie 1436859892) | The account handles or platform ids to search. These can be separated by commas to include multiple accounts. |
| accountTypes | `null` (all) | `facebook_page`, `facebook_group`, `facebook_profile` | Limits search to a specific Facebook account type. You can use more than one type. Requires "platforms=facebook" to be set also. If "platforms=facebook" is not set, all post types including IG and Reddit will be returned. Only applies to Facebook. |
| and | `null` | - | Post search is split into OR, AND and NOT chunks. This is the AND section. Each is a phrase match, meaning that `searchTerm` is "CrowdTangle, API" and `and` is "so fast, great documentation," it will search for (("CrowdTangle" AND "so fast" AND "great documentation") OR ("API" AND "so fast" AND "great documentation")). |
| brandedContent | `no_filter` e.g. all | `as_publisher`, `as_marketer`, `exclude`, `no_filter` | Limits to or excludes posts that have been marked as Branded Content, either as Publisher or Marketer. |
| count | `10` | `1-100` | The number of posts to return. |
| endDate | now | - | The latest date at which a post could be posted. Time zone is UTC. Format is “yyyy-mm-ddThh:mm:ss” or “yyyy-mm-dd” (defaults to time 00:00:00). |
| excludePageCategories | `null` | - | Exclude one or multiple Page Categories from search results, e.g. ARTIST, TV\_NETWORK, MEDIA\_NEWS\_COMPANY. View the full list of page categories here. |
| includeHistory | `null` (does not include) | `true` | Includes timestep data for growth of each post returned. Note that we will not have time-series data for posts that were created after the account was added to CrowdTangle. |
| inAccountIds | null | - | A comma-separated list of the IDs of accounts to search within. |
| includeSummary | false | true, false | Adds a "summary" section with total interaction statistics for each platform that matches your search. It will look beyond the count requested to summarize across the time searched. When includeSummary is specified, either startDate or timeframe is required. |
| inListIds | null | - | A comma-separated list of the IDs of lists to search within. |
| language | null (all languages) | 2-character Locale code | Exceptions: Some languages require more than two characters: Chinese (Simplified) is zh-CN and Chinese (Traditional) is zh-TW. |
| minInteractions | `0` | `> 0` | If set, will exclude posts with total interactions below this threshold. |
| minSubscriberCount | `0` | `> 0` | The minimum number of subscribers an account must have to be included in the search results. |
| not | `null` | - | A corollary to `and`, `not` will exclude all posts matching this word/phrase. |
| notInAccountIds | null | - | A comma-separated list of the IDs of accounts to exclude. This behaves the same as notInListIds, except with specific accounts. |
| notInListIds | null | - | A comma-separated list of the the IDs of lists to exclude from results. For instance, if don't want to see news outlet mentions of your search term, 'Lebron James,' you could exclude your sports publishers list. |
| notInTitle | `null` | - | Exclude all posts whose *account* title matches this term. E.g. search for "CrowdTangle" but ignore any accounts that include the word "CrowdTangle" to see what other accounts are posting. |
| offset | `0` | `> 0` | The number of posts to offset (generally used for pagination). Pagination links will also be provided in the response. |
| pageAdminTopCountry | `null` | 2-character country code | Limits to posts for which the account has the pageAdminTopCountry matching the parameter setting. |
| pageCategories | `null` | - | Include one or multiple Page Categories in search results, e.g. ARTIST, TV\_NETWORK, MEDIA\_NEWS\_COMPANY. View the full list of page categories here. |
| platforms | `null` (i.e., all platforms) | `facebook`, `instagram`, `reddit` (reddit is not currently available for the ACADEMICS vertical) | The platforms from which to retrieve posts. This value can be comma-separated. |
| searchField | `text_fields_and_image_text` | text\_fields\_and\_image\_text, include\_query\_strings , text\_fields\_only , account\_name\_only, image\_text\_only  | This allows you to search image text, URLs with query strings, and account names, in addition to text fields only or both text fields and image text. |
| searchTerm | `null` | Any string | Note: Use the API request form to request activation of Boolean search for this parameter. By default, post search is split into OR, AND and NOT chunks. This is the OR section. Each is a phrase match, meaning that "CrowdTangle API, organized so cleanly" will search for "CrowdTangle API" or "organized so cleanly." If you want to find those phrases together, put one in here and put one in the AND section. This parameter does not support wildcard or partial-term searches, and is not case-sensitive. If you submit a query with a blank searchTerm (i.e., searchTerm=" "), the result set will be limited to the Dashboard associated with the supplied API token. System-wide blank searches are not supported by default. Please reach out to support@crowdtangle.com for more information. |
| sortBy | `overperforming` | `date`, `interaction_rate`, `overperforming`, `total_interactions`, `underperforming` | The method by which to filter and order posts. |
| startDate | `null` | - | The earliest date at which a post could be posted. Time zone is UTC. Format is “yyyy-mm-ddThh:mm:ss” or “yyyy-mm-dd” (defaults to time 00:00:00). This must be before endDate. Timeframe and startDate are mutually exclusive; if both are passed, startDate will be preferred. |
| timeframe | `6 HOUR` | Any valid SQL interval (No, we don't pass it through to our database. Don't be silly) | The interval of time to consider from the endDate. Timeframe and startDate are mutually exclusive; if both are passed, startDate will be preferred. |
| types | `null` (all) | `album`, `igtv`, `link`, `live_video`, `live_video_complete`, `live_video_scheduled`, `native_video`, `photo`, `status`, `video`, `youtube` | The types of post to include. These can be separated by commas to include multiple types. If you want all live videos (whether currently or formerly live), be sure to include both live\_video and live\_video\_complete. |
| verified | `no_filter` (all) | `only`, `exclude`, `no_filter` | Limits to posts where the account has the verified setting matching the input. This is in addition to the current verifiedOnly parameter. If both are included, Verified will supersede verifiedOnly. |
| verifiedOnly | `false` | - | Limit results to verified accounts only. Note, this only applies to platforms that supply information about verified accounts. |


#### Response


The Response contains both a status code and a result. The status will always be 200 if there is no error. The result contains an array of post objects and a pagination object with URLs for both the next and previous page, if they exist. Below is an example response.



```
//Call: https://api.crowdtangle.com/posts/search?token=TOKEN&count=2&platforms=instagram&searchTerm=spongebob
{
    "status": 200,
    "result": {
        "posts": [
            {
                "platformId": "2430747914999752704_8048483788",
                "platform": "Instagram",
                "date": "2020-10-29 16:09:13",
                "updated": "2020-10-29 19:16:26",
                "type": "album",
                "description": "your move biden😼 @nelkboys \n-------------------------------------------\nWelcome to @lolkowalski.anal ---------------\nHope you enjoy!\n---------------\nTag a friend to make their day! 🙌🎉\n---------------\nSupport the page for more ❤\n———————\n#memesdaily #memes😂 #memes #dankmemes #dankestmemes #funnymemes #funnyvideos #racooneggs #swaggersouls #kermitmemes #dogmemes #stupidmemes #russianbadger #wholesomememes #viral #robloxmemes #funnyvines #funny #deadmemes #dumbmemes #offensivememes #offensivememes💦👀💯😂😂💎🔥😤💦👌💯😂🙏😂😂💎💎🔥😤💦👀👀 #fortnite #vinesthatkeepmefromendingitall #vinez #fitzmemes #fitz #spongebobmemes #spongebob #memesvirales",
                "postUrl": "https://www.instagram.com/p/CG7wFmcFOgA/",
                "subscriberCount": 16210,
                "score": 5.601123595505618,
                "media": [
                    {
                        "type": "video",
                        "url": "https://video-sea1-1.cdninstagram.com/v/t50.2886-16/122949371_696991084251666_2254624911693548026_n.mp4?_nc_cat=104&vs=17847823484380766_3400261711&_nc_vs=HBksFQAYJEdQc09WQWNTQ3YzaDZIa0NBUHFKUFdOcENVb2Zia1lMQUFBRhUAAsgBABUAGCRHUGhHVkFmU2xBbGlOVVFCQUlveTM4eThEWGxnYmtZTEFBQUYVAgLIAQAoABgAGwGIB3VzZV9vaWwBMRUAABgAFry6zoeHoLQ%2FFQIoAkMzLBdAPTvnbItDlhgSZGFzaF9iYXNlbGluZV8xX3YxEQB17gcA&ccb=2&_nc_sid=59939d&efg=eyJ2ZW5jb2RlX3RhZyI6InZ0c192b2RfdXJsZ2VuLjY0MC5jYXJvdXNlbF9pdGVtIn0%3D&_nc_ohc=FlW2Y_LowDIAX8MoxPb&_nc_ht=video-sea1-1.cdninstagram.com&oh=cf1ea844fb180481304cba578199cdf9&oe=5FC08662&_nc_rid=bfb325b314",
                        "height": 0,
                        "width": 0
                    },
                    {
                        "type": "photo",
                        "url": "https://scontent-sea1-1.cdninstagram.com/v/t51.29350-15/122846131_366536778121839_2835711148568567312_n.jpg?_nc_cat=111&ccb=2&_nc_sid=8ae9d6&_nc_ohc=I9zZKpLDkxcAX8Edz5D&_nc_ht=scontent-sea1-1.cdninstagram.com&oh=ff48970e6c456d6ad5c35da1b0577a04&oe=5FC0359A",
                        "height": 800,
                        "width": 640
                    }
                ],
                "statistics": {
                    "actual": {
                        "favoriteCount": 441,
                        "commentCount": 13
                    },
                    "expected": {
                        "favoriteCount": 215,
                        "commentCount": 4
                    }
                },
                "account": {
                    "id": 12625341,
                    "name": "Kowalski.analysis",
                    "handle": "lolkowalski.anal",
                    "profileImage": "https://scontent-sea1-1.cdninstagram.com/v/t51.2885-15/s150x150/120798515_324484358851454_8006262765166311798_n.jpg?_nc_cat=102&ccb=2&_nc_sid=8ae9d6&_nc_ohc=4NjtWMHg9qYAX8muiwk&_nc_ht=scontent-sea1-1.cdninstagram.com&tp=7&oh=7af14f05c70cec57ae30fbc73aaa0a9c&oe=5FC0C74D",
                    "subscriberCount": 16210,
                    "url": "https://www.instagram.com/lolkowalski.anal/",
                    "platform": "Instagram",
                    "platformId": "8048483788",
                    "verified": false
                },
                "newId": "12625341|2430747914999752704",
                "id": 110177990485
            },
            {
                "platformId": "2430746373845915986_452950430",
                "platform": "Instagram",
                "date": "2020-10-29 16:07:58",
                "updated": "2020-10-29 19:12:35",
                "type": "video",
                "description": "Did you not hear me the first time... 😂\n.\n.\n.\n#meme #memes #spongebob #spongebobmemes #otf #orangetheory #orangetheoryfitness #hellweek #hellweek2020 #flex #arms #armworkout #armsworkout #biceps #triceps #shoulders #muscle #gains #strength #workout #workoutmeme #fitness #fitnessmeme",
                "postUrl": "https://www.instagram.com/p/CG7vvLIJ5lS/",
                "subscriberCount": 33290,
                "score": 3.622107969151671,
                "media": [
                    {
                        "type": "video",
                        "url": "https://video-sea1-1.cdninstagram.com/v/t50.2886-16/122990926_109613797612159_8742625114362453296_n.mp4?_nc_cat=100&vs=17917143178490028_177546623&_nc_vs=HBkcFQAYJEdFNnhWQWQtR25oenNXTUFBRENkXzVrNEMxUjVia1lMQUFBRhUAAsgBACgAGAAbAYgHdXNlX29pbAExFQAAGAAW2Ornkf%2Fi0z8VAigCQzMsF0ARu2RaHKwIGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHXqBwA%3D&ccb=2&_nc_sid=59939d&efg=eyJ2ZW5jb2RlX3RhZyI6InZ0c192b2RfdXJsZ2VuLjcyMC5mZWVkIn0%3D&_nc_ohc=QB2cENLm54UAX9nTcWc&_nc_ht=video-sea1-1.cdninstagram.com&oh=430ff67c681dc2d72eb397c549ed1ae0&oe=5FC030ED&_nc_rid=3aab47924d",
                        "height": 0,
                        "width": 0
                    },
                    {
                        "type": "photo",
                        "url": "https://scontent-sea1-1.cdninstagram.com/v/t51.29350-15/123137960_357996108745190_4752433128898279482_n.jpg?_nc_cat=107&ccb=2&_nc_sid=8ae9d6&_nc_ohc=kRAG7qpfnnYAX_4E_Ut&_nc_ht=scontent-sea1-1.cdninstagram.com&oh=2596387b30cdbe10916d6da4684df14e&oe=5FC21966",
                        "height": 883,
                        "width": 720
                    }
                ],
                "statistics": {
                    "actual": {
                        "favoriteCount": 186,
                        "commentCount": 5,
                    },
                    "expected": {
                        "favoriteCount": 55,
                        "commentCount": 3,
                    }
                },
                "account": {
                    "id": 8953132,
                    "name": "Austin Hendrickson",
                    "handle": "trainingtall",
                    "profileImage": "https://scontent-sea1-1.cdninstagram.com/v/t51.2885-15/s150x150/66480173_498100930731771_674954802056134656_n.jpg?_nc_cat=111&ccb=2&_nc_sid=8ae9d6&_nc_ohc=xYDt_yNs-w0AX-wj5Hm&_nc_ht=scontent-sea1-1.cdninstagram.com&tp=7&oh=4779f2a782dd1850280e01b50748e253&oe=5FC1FE33",
                    "subscriberCount": 33290,
                    "url": "https://www.instagram.com/trainingtall/",
                    "platform": "Instagram",
                    "platformId": "452950430",
                    "verified": false
                },
                "imageText": "Friend: what was your workout today Me: arms Friend: okay but what else Me:... * @trainingtall",
                "newId": "8953132|2430746373845915986",
                "id": 110177735489
            }
        ],
        "pagination": {
            "nextPage": "https://api.crowdtangle.com/posts/search?token=TOKEN&sortBy=overperforming&endDate=2020-10-29T19:30&startDate=2020-10-29T13:30:39&searchTerm=spongebob&platforms=instagram&count=2&offset=2"
        },
        "hitCount": 19
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
 














































