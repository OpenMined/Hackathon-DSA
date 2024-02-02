Home
====

### [](#getting-started)Getting Started

Welcome to the CrowdTangle API! You can use the CrowdTangle API to access posts, the leaderboard and the link-checker. Please contact your CrowdTangle representative for access. If you have access to the API, you can locate your API token via your dashboard under Settings > API Access.

#### [](#authentication)Authentication

The CrowdTangle API expects the API token to be included either as a custom header with the name `x-api-token` or as a `token` query parameter.

    // as a custom header
    curl "https://api.crowdtangle.com/posts"
      -H "x-api-token: your-api-token"
    
    // as a query parameter 
    curl "https://api.crowdtangle.com/posts?token=your-api-token"
    

#### [](#making-a-request)Making a Request

All requests to the CrowdTangle API are made via GET to `https://api.crowdtangle.com/`. You must use https. Please visit the [API Cheat Sheet](https://help.crowdtangle.com/en/articles/3443476-api-cheat-sheet) to understand how pagination works with our API.

Below are the available endpoints:

##### [](#get-posts)[GET /posts](https://github.com/CrowdTangle/API/wiki/Posts)

##### [](#get-post)[GET /post](https://github.com/CrowdTangle/API/wiki/Posts#get-postid)

##### [](#get-postssearch)[GET /posts/search](https://github.com/CrowdTangle/API/wiki/Search)

##### [](#get-leaderboard)[GET /leaderboard](https://github.com/CrowdTangle/API/wiki/Leaderboard)

##### [](#get-links)[GET /links](https://github.com/CrowdTangle/API/wiki/Links)

##### [](#get-lists)[GET /lists](https://github.com/CrowdTangle/API/wiki/Lists)

##### [](#postman-template)Postman Template

[Postman](https://www.getpostman.com/) is a free API management software. [Click here to download a JSON file that you can import into Postman (unzip the file to access)](https://www.crowdtangle.com/assets/API-Demo.postman_collection.json.zip), and get a template for each endpoint. Please note that all parameters may not be present in the template; please view the Github API documentation to explore all parameter options.

Happy coding!

Posts
=====

[](#get-posts)GET /posts
------------------------

Retrieve a set of posts for the given parameters.

#### [](#endpoint)Endpoint

`GET https://api.crowdtangle.com/posts`

#### [](#parameters)Parameters

| Parameter | Default | Options | Description |
| --- | --- | --- | --- |
| accounts | `null` (any account in the List or Dashboard) | a string corresponding to account handles (ie iamcardib) or platform IDs (ie 1436859892) | The account handles or platform ids to search. These can be separated by commas to include multiple accounts. |
| brandedContent | `no_filter` e.g. all | `as_publisher`, `as_marketer`, `exclude`, `no_filter` | Limits to or excludes posts that have been marked as Branded Content, either as Publisher or Marketer. |
| count | `10` | `1-100` | The number of posts to return. |
| endDate | now | \-  | The latest date at which a post could be posted. Time zone is UTC. Format is “yyyy-mm-ddThh:mm:ss” or “yyyy-mm-dd” (defaults to time 00:00:00). |
| includeHistory | `null` (does not include) | `true` | Includes timestep data for growth of each post returned. Note that we will not have time-series data for posts that were created after the account was added to CrowdTangle. |
| language | `null` (all languages) | [2-character Locale code](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) | Exceptions: Some languages require more than two characters: Chinese (Simplified) is zh-CN and Chinese (Traditional) is zh-TW. |
| listIds | `null` (i.e posts from all Lists, not including saved searches or saved posts lists, in the Dashboard) | \-  | The IDs of lists or saved searches to retrieve. These can be separated by commas to include multiple lists. |
| minInteractions | `0` | `> 0` | If set, will exclude posts with total interactions below this threshold. |
| offset | `0` | `> 0` | The number of posts to offset (generally used for pagination). Pagination links will also be provided in the response. |
| pageAdminTopCountry | `null` | [2-character country code](https://en.m.wikipedia.org/wiki/List_of_ISO_3166_country_codes#Current_ISO_3166_country_codes) | Limits to posts for which the account has the pageAdminTopCountry matching the parameter setting. |
| searchTerm | `null` | Any string | Returns only posts that match this search term. Terms AND automatically. Separate with commas for OR, use quotes for phrases. E.g. CrowdTangle API -> AND. CrowdTangle, API -> OR. "CrowdTangle API" -> AND in that exact order. You can also use traditional Boolean search with this parameter. |
| sortBy | `overperforming` | `date`, `interaction_rate`, `overperforming`, `total_interactions`, `underperforming` | The method by which to filter and order posts. |
| startDate | `null` | \-  | The earliest date at which a post could be posted. Time zone is UTC. Format is “yyyy-mm-ddThh:mm:ss” or “yyyy-mm-dd” (defaults to time 00:00:00). This must be before endDate. Timeframe and startDate are mutually exclusive; if both are passed, startDate will be preferred. |
| timeframe | `6 HOUR` | Any valid SQL interval (No, we don't pass it through to our database. Don't be silly) | The interval of time to consider from the endDate. Timeframe and startDate are mutually exclusive; if both are passed, startDate will be preferred. Depending on the number of posts, longer timeframes may not return within the timeout window. If you get a 504, try shortening your timeframe. |
| types | `null` (all) | `album`, `igtv`, `link`, `live_video`, `live_video_complete`, `live_video_scheduled`, `native_video`, `photo`, `status`, `video`, `vine`, `youtube` | The types of post to include. These can be separated by commas to include multiple types. If you want all live videos (whether currently or formerly live), be sure to include both live\_video and live\_video\_complete. The "video" type does not mean all videos, it refers to videos that aren't native\_video or youtube (e.g. a video on Vimeo). |
| verified | `no_filter` (all) | `only`, `exclude`, `no_filter` | Limits to posts where the account has the verified setting matching the input. |
| weightAngry, weightComment, weightHaha, weightLike, weightLove, weightRepost, weightSad, weightShare, weightUpvote, weightView, weightWow | 0   | 0-10 | How much weight to give to each type of interaction. If you send in no weights, all weights will use the current dashboard defaults. If you send in at least one weight, all other weights will default to 0. Weights are multiplied by interaction counts: e.g. weightsComment at 1 and all others at 0 will find the most commented-on posts. weightLike at 1 and weightShare at 2 will give shares twice the impact as likes when computing scores. |

#### [](#response)Response

The Response contains both a status code and a result. The status will always be 200 if there is no error. The result contains an array of [post objects](https://github.com/CrowdTangle/API/wiki/Post) and a [pagination object](https://github.com/CrowdTangle/API/wiki/Pagination) with URLs for both the next and previous page, if they exist. Below is an example response.

    // Call: https://api.crowdtangle.com/posts?token=TOKEN&listIds=1310154&sortBy=total_interactions&count=2
    {
        "status": 200,
        "result": {
            "posts": [
                {
                    "platformId": "11430503918_10159078346893919",
                    "platform": "Facebook",
                    "date": "2020-10-29 14:56:05",
                    "updated": "2020-10-29 19:03:44",
                    "type": "photo",
                    "message": "Salió el sol 😎 Ánimo mi gente que hoy es JUERNES!!!! 🕺🏻#Perfecta",
                    "expandedLinks": [
                        {
                            "original": "https://www.facebook.com/luisfonsi/photos/a.74490428918/10159078346893919/?type=3",
                            "expanded": "https://www.facebook.com/luisfonsi/photos/a.74490428918/10159078346893919/?type=3"
                        }
                    ],
                    "link": "https://www.facebook.com/luisfonsi/photos/a.74490428918/10159078346893919/?type=3",
                    "postUrl": "https://www.facebook.com/luisfonsi/posts/10159078346893919",
                    "subscriberCount": 13231210,
                    "score": 55081.0,
                    "media": [
                        {
                            "type": "photo",
                            "url": "https://scontent-sea1-1.xx.fbcdn.net/v/t1.0-0/p600x600/123184409_10159078346898919_2930797796463495309_o.jpg?_nc_cat=110&ccb=2&_nc_sid=2d5d41&_nc_ohc=K6a18H3Rdd0AX_6WnSi&_nc_ht=scontent-sea1-1.xx&tp=6&oh=f2f8879521dd107979e73ccad9a40260&oe=5FC0E9D8",
                            "height": 719,
                            "width": 600,
                            "full": "https://scontent-sea1-1.xx.fbcdn.net/v/t1.0-0/p600x600/123184409_10159078346898919_2930797796463495309_o.jpg?_nc_cat=110&ccb=2&_nc_sid=2d5d41&_nc_ohc=K6a18H3Rdd0AX_6WnSi&_nc_ht=scontent-sea1-1.xx&tp=6&oh=f2f8879521dd107979e73ccad9a40260&oe=5FC0E9D8"
                        }
                    ],
                    "statistics": {
                        "actual": {
                            "likeCount": 42617,
                            "shareCount": 303,
                            "commentCount": 1060,
                            "loveCount": 10937,
                            "wowCount": 35,
                            "hahaCount": 123,
                            "sadCount": 4,
                            "angryCount": 2,
                            "thankfulCount": 0,
                            "careCount": 520
                        },
                        "expected": {
                            "likeCount": 10773,
                            "shareCount": 137,
                            "commentCount": 359,
                            "loveCount": 3279,
                            "wowCount": 18,
                            "hahaCount": 16,
                            "sadCount": 2,
                            "angryCount": 2,
                            "thankfulCount": 0,
                            "careCount": 167
                        }
                    },
                    "account": {
                        "id": 11023,
                        "name": "Luis Fonsi",
                        "handle": "luisfonsi",
                        "profileImage": "https://scontent-sea1-1.xx.fbcdn.net/v/t1.0-1/p200x200/44395322_10156942313018919_1108227336190296064_n.jpg?_nc_cat=1&ccb=2&_nc_sid=dbb9e7&_nc_ohc=q9kfC3Ks0HcAX-7VZ53&_nc_ht=scontent-sea1-1.xx&tp=6&oh=1f921982b59ade01b6b5907929b2ee30&oe=5FBFC603",
                        "subscriberCount": 13231210,
                        "url": "https://www.facebook.com/11430503918",
                        "platform": "Facebook",
                        "platformId": "11430503918",
                        "accountType": "facebook_page",
                        "pageAdminTopCountry": "US",
                        "verified": true
                    },
                    "Id": "11023|10159078346893919",
                    "legacyid": 110173423951
                },
                {
                    "platformId": "10162931178_10157582304861179",
                    "platform": "Facebook",
                    "date": "2020-10-29 17:00:00",
                    "updated": "2020-10-29 19:07:42",
                    "type": "photo",
                    "expandedLinks": [
                        {
                            "original": "https://www.facebook.com/tobymac/photos/a.241173571178/10157582303601179/?type=3",
                            "expanded": "https://www.facebook.com/tobymac/photos/a.241173571178/10157582303601179/?type=3"
                        }
                    ],
                    "link": "https://www.facebook.com/tobymac/photos/a.241173571178/10157582303601179/?type=3",
                    "postUrl": "https://www.facebook.com/tobymac/posts/10157582304861179",
                    "subscriberCount": 5043407,
                    "score": 52888.0,
                    "media": [
                        {
                            "type": "photo",
                            "url": "https://scontent-sea1-1.xx.fbcdn.net/v/t1.0-9/p720x720/123164065_10157582303606179_1644220515968605599_o.jpg?_nc_cat=102&ccb=2&_nc_sid=8024bb&_nc_ohc=xzqACcCLEjwAX9l86ZA&_nc_ht=scontent-sea1-1.xx&tp=6&oh=cf86ece71d72344058e2115fdcfb7de2&oe=5FC1563B",
                            "height": 720,
                            "width": 720,
                            "full": "https://scontent-sea1-1.xx.fbcdn.net/v/t1.0-9/p720x720/123164065_10157582303606179_1644220515968605599_o.jpg?_nc_cat=102&ccb=2&_nc_sid=8024bb&_nc_ohc=xzqACcCLEjwAX9l86ZA&_nc_ht=scontent-sea1-1.xx&tp=6&oh=cf86ece71d72344058e2115fdcfb7de2&oe=5FC1563B"
                        }
                    ],
                    "statistics": {
                        "actual": {
                            "likeCount": 22509,
                            "shareCount": 15651,
                            "commentCount": 383,
                            "loveCount": 14248,
                            "wowCount": 58,
                            "hahaCount": 9,
                            "sadCount": 29,
                            "angryCount": 1,
                            "thankfulCount": 0,
                            "careCount": 410
                        },
                        "expected": {
                            "likeCount": 11644,
                            "shareCount": 5123,
                            "commentCount": 280,
                            "loveCount": 5404,
                            "wowCount": 9,
                            "hahaCount": 4,
                            "sadCount": 8,
                            "angryCount": 2,
                            "thankfulCount": 0,
                            "careCount": 190
                        }
                    },
                    "account": {
                        "id": 20656,
                        "name": "TobyMac",
                        "handle": "tobymac",
                        "profileImage": "https://scontent-sea1-1.xx.fbcdn.net/v/t1.0-1/p200x200/96034089_10157131542946179_1640202341955141632_n.jpg?_nc_cat=1&ccb=2&_nc_sid=dbb9e7&_nc_ohc=qy0yJDS2mAQAX_jqKlW&_nc_ht=scontent-sea1-1.xx&tp=6&oh=8b8c02a81a13632fdb4b1340abdba255&oe=5FC170E9",
                        "subscriberCount": 5043407,
                        "url": "https://www.facebook.com/10162931178",
                        "platform": "Facebook",
                        "platformId": "10162931178",
                        "accountType": "facebook_page",
                        "pageAdminTopCountry": "US",
                        "verified": true
                    },
                    "imageText": "2 the trees are about to show us how lovely it is to let things go tOBYMAC #SPEAKLIFE",
                    "Id": "20656|10157582304861179",
                    "legacyid": 110181321374
                }
            ],
            "pagination": {
                "nextPage": "https://api.crowdtangle.com/posts?token=TOKEN&sortBy=total_interactions&endDate=2020-10-29T19:21&startDate=2020-10-29T13:21:06&listIds=1310154&searchField=TEXT_FIELDS_AND_IMAGE_TEXT&count=2&offset=2"
            }
        }
    }
    

[](#get-postid)GET /post/:id
----------------------------

Retrieves a specific post. There are two versions of this endpoint, depending upon what you need. Both return the same data. Please note that you must use a dashboard token that corresponds to the post platform - i.e. an Instagram token for Instagram posts, and a Facebook token for Facebook posts.

Please also note that the ID format for Facebook and Instagram are different. For Instagram, it's `[post_id]_[page_id]`, while for Facebook, it's `[page_id]_[post_id]`. While Page and Post IDs can be found in Facebook post URLs, Instagram does not expose the IDs in its URLs. You can pull the necessary Instagram IDs from our API.

#### [](#endpoint---platform-id)Endpoint - Platform ID

`GET http://api.crowdtangle.com/post/:id`

#### [](#path-variables)Path Variables

| Path Variable | Description |
| --- | --- |
| id  | The ID of the post on its platform which corresponds to the **platformId** property of the Post object. This is provided as a path variable in the URL. For Facebook and Instagram, requires the full \[number\]\_\[number\] ID format. |

#### [](#parameters-1)Parameters

| Parameter | Description |
| --- | --- |
| account | The slug or ID of the posting account on its platform. This is required for Reddit, ignored for Facebook and Instagram (where a post ID contain the account's ID). |
| includeHistory | `null` (does not include) |

#### [](#endpoint---crowdtangle-id)Endpoint - CrowdTangle ID

`GET http://api.crowdtangle.com/ctpost/:id`

#### [](#path-variables-1)Path Variables

| Path Variable | Description |
| --- | --- |
| id  | The CrowdTangle ID of the post which corresponds to the **id** property of the Post object and is represented in the \[number\]\|\[number\] ID format. This is provided as a path variable in the URL. |

#### [](#response-1)Response

The response contains a status code and a result. The result is an array of posts containing a single [post](https://github.com/CrowdTangle/API/wiki/Post).

    // Call: https://api.crowdtangle.com/post/47657117525_10154014482272526?token=TOKEN
    {
        "status": 200,
        "result": {
            "posts": [
                {
                    "platformId": "47657117525_10154014482272526",
                    "platform": "Facebook",
                    "date": "2016-02-12 23:38:14",
                    "updated": "2020-08-23 05:48:22",
                    "type": "live_video_complete",
                    "message": "Draymond at Foot Locker for #NBAAllStarTO with a special shoutout to #DubNation.",
                    "expandedLinks": [
                        {
                            "original": "https://www.facebook.com/warriors/videos/10154014482272526/",
                            "expanded": "https://www.facebook.com/warriors/videos/10154014482272526/"
                        }
                    ],
                    "link": "https://www.facebook.com/warriors/videos/10154014482272526/",
                    "postUrl": "https://www.facebook.com/warriors/posts/10154014482272526",
                    "subscriberCount": 6041837,
                    "score": 4.750579867017164,
                    "media": [
                        {
                            "type": "video",
                            "url": "https://video-sea1-1.xx.fbcdn.net/v/t42.1790-29/12718926_1213464465334694_1083747983_n.mp4?_nc_cat=109&_nc_sid=985c63&efg=eyJybHIiOjQ0MiwicmxhIjoxNDIwLCJ2ZW5jb2RlX3RhZyI6InYyXzQwMF9jcmZfMjdfbWFpbl8zLjBfc2QifQ%3D%3D&_nc_ohc=e7Ygz2qv-24AX-wSWX2&rl=442&vabr=246&_nc_ht=video-sea1-1.xx&oh=889e0d776d92a84bb57099cad3d28d55&oe=5F43C879",
                            "height": 0,
                            "width": 0
                        },
                        {
                            "type": "photo",
                            "url": "https://scontent-sea1-1.xx.fbcdn.net/v/t15.5256-10/12526285_831341603658336_1493677499_n.jpg?_nc_cat=101&_nc_sid=1055be&_nc_ohc=DH0vfblGwtIAX_x8SBs&_nc_ht=scontent-sea1-1.xx&oh=b09d6378fa261fd45345e79c50c254cb&oe=5F696BE1",
                            "height": 400,
                            "width": 400,
                            "full": "https://scontent-sea1-1.xx.fbcdn.net/v/t15.5256-10/12526285_831341603658336_1493677499_n.jpg?_nc_cat=101&_nc_sid=1055be&_nc_ohc=DH0vfblGwtIAX_x8SBs&_nc_ht=scontent-sea1-1.xx&oh=b09d6378fa261fd45345e79c50c254cb&oe=5F696BE1"
                        }
                    ],
                    "statistics": {
                        "actual": {
                            "likeCount": 24235,
                            "shareCount": 753,
                            "commentCount": 5675,
                            "loveCount": 33,
                            "wowCount": 18,
                            "hahaCount": 3,
                            "sadCount": 0,
                            "angryCount": 5,
                            "thankfulCount": 0,
                            "careCount": 0
                        },
                        "expected": {
                            "likeCount": 3927,
                            "shareCount": 279,
                            "commentCount": 1041,
                            "loveCount": 1046,
                            "wowCount": 94,
                            "hahaCount": 45,
                            "sadCount": 14,
                            "angryCount": 19,
                            "thankfulCount": 0,
                            "careCount": 2
                        }
                    },
                    "account": {
                        "id": 19889,
                        "name": "Golden State Warriors",
                        "handle": "warriors",
                        "profileImage": "https://scontent-sea1-1.xx.fbcdn.net/v/t1.0-1/p200x200/74788912_10158146665972526_3545220405897723904_n.jpg?_nc_cat=1&ccb=2&_nc_sid=dbb9e7&_nc_ohc=9snUpG_pdlQAX90IhWM&_nc_ht=scontent-sea1-1.xx&tp=6&oh=f8a3d3b62b507966ecc68de3b557fe84&oe=5FBF1185",
                        "subscriberCount": 11580228,
                        "url": "https://www.facebook.com/47657117525",
                        "platform": "Facebook",
                        "platformId": "47657117525",
                        "accountType": "facebook_page",
                        "pageAdminTopCountry": "US",
                        "verified": true
                    },
                    "videoLengthMS": 307968,
                    "liveVideoStatus": "completed",
                    "Id": "19889|10154014482272526",
                    "legacyid": 1686762829
                }
            ]
        }
    }

Search
======

[](#get-postssearch)GET /posts/search
-------------------------------------

_Note: Access to the Search is restricted to a limited set customers and usage requires prior approval by CrowdTangle. [Apply here to activate Search.](https://www.facebook.com/help/contact/908993259530156)_

Retrieve a set of posts for the given parameters and search terms. This endpoint, unlike the main `/posts` endpoint, searches the entire, cross-platform CrowdTangle system of posts. It can be limited by lists and accounts, but by default will search beyond the dashboard the token is associated with.

**If you submit a query with a blank searchTerm (i.e., searchTerm=" "), the result set will be limited to the Dashboard associated with the supplied API token. System-wide blank searches are not supported by default. Please reach out to [support@crowdtangle.com](mailto:support@crowdtangle.com) for more information.**

#### [](#endpoint)Endpoint

`GET https://api.crowdtangle.com/posts/search`

#### [](#calculating-the-number-of-responses)Calculating the number of responses

To calculate the number of responses you'll get for each query, request activation of the hitCount setting [here](https://www.facebook.com/help/contact/908993259530156). Once it's activated, make the query with your full date ranges and `count = 0`. This will return the total number of matches for the search within your date range as a hitCount property.

#### [](#parameters)Parameters

Note: **Please use startDate!** Our system works much more quickly (and with much less strain) when it only has to search a subset of dates for your data. If you're looking only for posts in 2019, put in a startDate of 2019-01-01 and our system will know it can ignore years' worth of data. If the event you're interested in happened yesterday, put that in and it will return very quickly! We're not making startDate mandatory, but please strongly consider using it!

| Parameter | Default | Options | Description |
| --- | --- | --- | --- |
| accounts | `null` (any account in the List or Dashboard) | a string corresponding to account handles (ie iamcardib) or platform IDs (ie 1436859892) | The account handles or platform ids to search. These can be separated by commas to include multiple accounts. |
| accountTypes | `null` (all) | `facebook_page`, `facebook_group`, `facebook_profile` | Limits search to a specific Facebook account type. You can use more than one type. Requires "platforms=facebook" to be set also. If "platforms=facebook" is not set, all post types including IG and Reddit will be returned. Only applies to Facebook. |
| and | `null` | \-  | Post search is split into OR, AND and NOT chunks. This is the AND section. Each is a phrase match, meaning that `searchTerm` is "CrowdTangle, API" and `and` is "so fast, great documentation," it will search for (("CrowdTangle" AND "so fast" AND "great documentation") OR ("API" AND "so fast" AND "great documentation")). |
| brandedContent | `no_filter` e.g. all | `as_publisher`, `as_marketer`, `exclude`, `no_filter` | Limits to or excludes posts that have been marked as Branded Content, either as Publisher or Marketer. |
| count | `10` | `1-100` | The number of posts to return. |
| endDate | now | \-  | The latest date at which a post could be posted. Time zone is UTC. Format is “yyyy-mm-ddThh:mm:ss” or “yyyy-mm-dd” (defaults to time 00:00:00). |
| excludePageCategories | `null` | \-  | Exclude one or multiple Page Categories from search results, e.g. ARTIST, TV\_NETWORK, MEDIA\_NEWS\_COMPANY. [View the full list of page categories here.](https://www.facebook.com/pages/category/) |
| includeHistory | `null` (does not include) | `true` | Includes timestep data for growth of each post returned. Note that we will not have time-series data for posts that were created after the account was added to CrowdTangle. |
| inAccountIds | null | \-  | A comma-separated list of the IDs of accounts to search within. |
| includeSummary | false | true, false | Adds a "summary" section with total interaction statistics for each platform that matches your search. It will look beyond the count requested to summarize across the time searched. When includeSummary is specified, either startDate or timeframe is required. |
| inListIds | null | \-  | A comma-separated list of the IDs of lists to search within. |
| language | null (all languages) | [2-character Locale code](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) | Exceptions: Some languages require more than two characters: Chinese (Simplified) is zh-CN and Chinese (Traditional) is zh-TW. |
| minInteractions | `0` | `> 0` | If set, will exclude posts with total interactions below this threshold. |
| minSubscriberCount | `0` | `> 0` | The minimum number of subscribers an account must have to be included in the search results. |
| not | `null` | \-  | A corollary to `and`, `not` will exclude all posts matching this word/phrase. |
| notInAccountIds | null | \-  | A comma-separated list of the IDs of accounts to exclude. This behaves the same as notInListIds, except with specific accounts. |
| notInListIds | null | \-  | A comma-separated list of the the IDs of lists to exclude from results. For instance, if don't want to see news outlet mentions of your search term, 'Lebron James,' you could exclude your sports publishers list. |
| notInTitle | `null` | \-  | Exclude all posts whose _account_ title matches this term. E.g. search for "CrowdTangle" but ignore any accounts that include the word "CrowdTangle" to see what other accounts are posting. |
| offset | `0` | `> 0` | The number of posts to offset (generally used for pagination). Pagination links will also be provided in the response. |
| pageAdminTopCountry | `null` | [2-character country code](https://en.m.wikipedia.org/wiki/List_of_ISO_3166_country_codes#Current_ISO_3166_country_codes) | Limits to posts for which the account has the pageAdminTopCountry matching the parameter setting. |
| pageCategories | `null` | \-  | Include one or multiple Page Categories in search results, e.g. ARTIST, TV\_NETWORK, MEDIA\_NEWS\_COMPANY. [View the full list of page categories here.](https://www.facebook.com/pages/category/) |
| platforms | `null` (i.e., all platforms) | `facebook`, `instagram`, `reddit` (reddit is not currently available for the ACADEMICS vertical) | The platforms from which to retrieve posts. This value can be comma-separated. |
| searchField | `text_fields_and_image_text` | text\_fields\_and\_image\_text, include\_query\_strings , text\_fields\_only , account\_name\_only, image\_text\_only | This allows you to search image text, URLs with query strings, and account names, in addition to text fields only or both text fields and image text. |
| searchTerm | `null` | Any string | Note: Use the [API request form](https://www.facebook.com/help/contact/908993259530156) to request activation of Boolean search for this parameter. By default, post search is split into OR, AND and NOT chunks. This is the OR section. Each is a phrase match, meaning that "CrowdTangle API, organized so cleanly" will search for "CrowdTangle API" or "organized so cleanly." If you want to find those phrases together, put one in here and put one in the AND section. This parameter does not support wildcard or partial-term searches, and is not case-sensitive. If you submit a query with a blank searchTerm (i.e., searchTerm=" "), the result set will be limited to the Dashboard associated with the supplied API token. System-wide blank searches are not supported by default. Please reach out to [support@crowdtangle.com](mailto:support@crowdtangle.com) for more information. |
| sortBy | `overperforming` | `date`, `interaction_rate`, `overperforming`, `total_interactions`, `underperforming` | The method by which to filter and order posts. |
| startDate | `null` | \-  | The earliest date at which a post could be posted. Time zone is UTC. Format is “yyyy-mm-ddThh:mm:ss” or “yyyy-mm-dd” (defaults to time 00:00:00). This must be before endDate. Timeframe and startDate are mutually exclusive; if both are passed, startDate will be preferred. |
| timeframe | `6 HOUR` | Any valid SQL interval (No, we don't pass it through to our database. Don't be silly) | The interval of time to consider from the endDate. Timeframe and startDate are mutually exclusive; if both are passed, startDate will be preferred. |
| types | `null` (all) | `album`, `igtv`, `link`, `live_video`, `live_video_complete`, `live_video_scheduled`, `native_video`, `photo`, `status`, `video`, `youtube` | The types of post to include. These can be separated by commas to include multiple types. If you want all live videos (whether currently or formerly live), be sure to include both live\_video and live\_video\_complete. |
| verified | `no_filter` (all) | `only`, `exclude`, `no_filter` | Limits to posts where the account has the verified setting matching the input. This is in addition to the current verifiedOnly parameter. If both are included, Verified will supersede verifiedOnly. |
| verifiedOnly | `false` | \-  | Limit results to verified accounts only. Note, this only applies to platforms that supply information about verified accounts. |

#### [](#response)Response

The Response contains both a status code and a result. The status will always be 200 if there is no error. The result contains an array of [post objects](https://github.com/CrowdTangle/API/wiki/Post) and a [pagination object](https://github.com/CrowdTangle/API/wiki/Pagination) with URLs for both the next and previous page, if they exist. Below is an example response.

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

Leaderboard
===========

[](#get-leaderboard)GET /leaderboard
------------------------------------

Retrieves leaderboard data for a certain list or set of accounts.

#### [](#endpoint)Endpoint

`GET https://api.crowdtangle.com/leaderboard`

#### [](#parameters)Parameters

| Parameter | Default | Options | Description |
| --- | --- | --- | --- |
| accountIds | \-  | \-  | A list of CrowdTangle accountIds to retrieve leaderboard data for. These should be provided comma-separated. This and listId are mutually exclusive; if both are sent, accountIds will be preferred. |
| count | `50` | `1-100` | The number of [AccountStatistics](https://github.com/CrowdTangle/API/wiki/AccountStatistics) to return. |
| endDate | now | \-  | The endDate of the leaderboard range. Time zone is UTC. Format is “yyyy-mm-ddThh:mm:ss” or “yyyy-mm-dd” (defaults to time 00:00:00). |
| listId | 0 (i.e. the entire dashboard) | \-  | The list of the leaderboard to retrieve. This and accountIds are mutually exclusive; if both are sent, accountIds will be preferred. |
| offset | `0` | `> 0` | The number of rows to offset (generally used for pagination). Pagination links will also be provided in the response. |
| orderBy | `desc` | `asc` or `desc` | the order of the sort. |
| sortBy | `total_interactions` | `total_interactions`, `interaction_rate` | The method by which the accountStatistics are sorted. |
| startDate | One day earlier than `endDate` | \-  | The startDate of the leaderboard rage. Time zone is UTC. Format is “yyyy-mm-ddThh:mm:ss” or “yyyy-mm-dd” (defaults to time 00:00:00). This must be before endDate. |

#### [](#response)Response

The Response contains both a status code and a result. The status will always be 200 if there is no error. The result contains an array of [accountStatistics objects](https://github.com/CrowdTangle/API/wiki/AccountStatistics) and a [pagination object](https://github.com/CrowdTangle/API/wiki/Pagination) with URLs for both the next and previous pages, if they exist. Below is an example response.

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
    

Important Notes:

* subscriberData: Counts may not be available for selected date ranges based on when we started tracking an account within CrowdTangle. If initialCount or finalCount is 0, we likely were not tracking the account at that time. This can be confirmed by referencing the notes section which could look like this: "No subscriberCount available for beginning of time range." If the note section is present at all, any calculations made with subscriberCount data will need to take into account potentially missing data.

Links
=====

[](#get-links)GET /links
------------------------

Retrieve a set of posts matching a certain link. This will return up to 1000 posts. This endpoint only pulls data from CrowdTangle. To access interaction metrics across the entirety of Facebook, [use this Graph API endpoint.](https://developers.facebook.com/docs/graph-api/reference/v10.0/url)

#### [](#endpoint)Endpoint

`GET https://api.crowdtangle.com/links`

#### [](#parameters)Parameters

Note: **Please use startDate!** Our system works much more quickly (and with much less strain) when it only has to search a subset of dates for your data. If you're looking only for posts in 2019, put in a startDate of 2019-01-01 and our system will know it can ignore years' worth of data. If the URL you're interested in was published yesterday, put that in and it will return very quickly! We're not making startDate mandatory, but please strongly consider using it!

| Parameter | Default | Options | Description |
| --- | --- | --- | --- |
| count | 100 | 1 - 1000 | The number of posts to return. |
| endDate | now | \-  | The latest date at which a post could be posted. Time zone is UTC. Format is “yyyy-mm-ddThh:mm:ss” or “yyyy-mm-dd”. |
| includeHistory | `null` (does not include) | `true` | Includes timestep data for growth of each post returned. Note that we will not have time-series data for posts that were created after the account was added to CrowdTangle. |
| link | `null` | \-  | The link to query by. Required. |
| includeSummary | `false` | `true`, `false` | Adds a "summary" section with AccountStatistics for each platform that has posted this link. It will look beyond the count requested to summarize across the time searched. Requires a value for startDate. |
| offset | 0   | \>= 0 | The number of posts to offset (generally used for pagination). Pagination links will also be provided in the response. |
| platforms | `null` (i.e., all platforms) | `facebook`, `instagram`, `reddit` (reddit is not currently available for the ACADEMICS vertical) | The platforms from which to retrieve links. This value can be comma-separated. |
| searchField | `null` (i.e., does not support query strings) | `Include_query_strings` | Allows you to search URLs containing query strings. |
| startDate | 0000-00-00 | \-  | The earliest date at which a post could be posted. Time zone is UTC. Format is “yyyy-mm-ddThh:mm:ss” or “yyyy-mm-dd” (defaults to time 00:00:00). |
| sortBy | `date` | `subscriber_count`, `total_interactions` | The method by which to order posts (defaults to the most recent). If `subscriber_count`, a startDate is required. |

#### [](#response)Response

This returns the same response as [/posts](https://github.com/CrowdTangle/API/wiki/Posts). There is no option for pagination on a links request.

Lists
=====

[](#get-lists)GET /lists
------------------------

Retrieve the lists, saved searches and saved post lists of the dashboard associated with the token sent in.

#### [](#endpoint)Endpoint

`GET https://api.crowdtangle.com/lists`

#### [](#parameters)Parameters

This endpoint accepts no parameters other than the token.

#### [](#response)Response

The Response contains both a status code and a result. The status will always be 200 if there is no error. The result contains an array of list objects.

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

List Accounts
=============

[](#get-listslistidaccounts)GET /lists/:listId/accounts
-------------------------------------------------------

Retrieve the accounts for a given list. Accounts may only be retrieved for [lists](https://github.com/CrowdTangle/API/wiki/List) of type `LIST`, as saved searches and saved posts do not have associated accounts.

#### [](#endpoint)Endpoint

`GET https://api.crowdtangle.com/lists/:listId/accounts` (note that :listID is a placeholder for the actual List ID)

#### [](#path-variables)Path Variables

| Path Variable | Options | Description |
| --- | --- | --- |
| :listId | int | The id of the list for which to retrieve accounts. This is provided as a path variable in the URL. |

#### [](#parameters)Parameters

| Parameter | Default | Options | Description |
| --- | --- | --- | --- |
| count | `10` | `1-100` | The number of accounts to return. |
| offset | `0` | `>= 0` | The number of accounts to offset (generally used for pagination). Pagination links will also be provided in the response. |

#### [](#response)Response

The Response contains both a status code and a result. The status will always be 200 if there is no error. The result contains an array of [account](https://github.com/CrowdTangle/API/wiki/Account) objects as well as pagination.

    //Call: https://api.crowdtangle.com/lists/73928/accounts?token=TOKEN
    {
        "status": 200,
        "result": {
            "accounts": [
                {
                    "id": 599177,
                    "name": "102.3 FM",
                    "handle": "102.3oficial",
                    "profileImage": "https://scontent-sea1-1.xx.fbcdn.net/v/t1.0-1/p200x200/80087839_10156959736320756_6094224427388502016_n.png?_nc_cat=104&ccb=2&_nc_sid=dbb9e7&_nc_ohc=EU8CreSOPHEAX9hIp8D&_nc_ht=scontent-sea1-1.xx&oh=7b6950783794fdc724e0f4db6d16376d&oe=5FC188F0",
                    "subscriberCount": 76531,
                    "url": "https://www.facebook.com/219679725755",
                    "platform": "Facebook",
                    "platformId": "219679725755",
                    "accountType": "facebook_page",
                    "pageAdminTopCountry": "BR",
                    "verified": true
                },
                {
                    "id": 350212,
                    "name": "1 NEWS Sport",
                    "handle": "1NEWSSportNZ",
                    "profileImage": "https://scontent-sea1-1.xx.fbcdn.net/v/t1.0-1/p200x200/84670284_2748436965204409_1817888033798619136_o.jpg?_nc_cat=104&ccb=2&_nc_sid=dbb9e7&_nc_ohc=0Qx-7jQ7uQMAX9dFON4&_nc_ht=scontent-sea1-1.xx&tp=6&oh=cc940281a14f4d8b47c64aaf44bc0c6f&oe=5FC24AC1",
                    "subscriberCount": 491559,
                    "url": "https://www.facebook.com/122959744418824",
                    "platform": "Facebook",
                    "platformId": "122959744418824",
                    "accountType": "facebook_page",
                    "pageAdminTopCountry": "NZ",
                    "verified": true
                },
                {
                    "id": 3197681,
                    "name": "92 Rádio",
                    "handle": "92radio",
                    "profileImage": "https://scontent-sea1-1.xx.fbcdn.net/v/t1.0-1/p200x200/99257503_722143998557016_8827713529218859008_n.png?_nc_cat=103&ccb=2&_nc_sid=dbb9e7&_nc_ohc=8r4QxU6sRMcAX_DqkaD&_nc_ht=scontent-sea1-1.xx&oh=d58aff39f73b1f48e9f33354a87078f9&oe=5FC22EC1",
                    "subscriberCount": 371061,
                    "url": "https://www.facebook.com/142034879901267",
                    "platform": "Facebook",
                    "platformId": "142034879901267",
                    "accountType": "facebook_page",
                    "pageAdminTopCountry": "BR",
                    "verified": true
                },
                {
                    "id": 103875,
                    "name": "1 NEWS",
                    "handle": "1NEWSNZ",
                    "profileImage": "https://scontent-sea1-1.xx.fbcdn.net/v/t1.0-1/p200x200/83740946_10156915024251218_5477944535067656192_o.jpg?_nc_cat=1&ccb=2&_nc_sid=dbb9e7&_nc_ohc=C-MytOLfteYAX91gnog&_nc_ht=scontent-sea1-1.xx&tp=6&oh=f2a50999c0973deb3d5e7e6d15b571cc&oe=5FBED15B",
                    "subscriberCount": 860358,
                    "url": "https://www.facebook.com/179995481217",
                    "platform": "Facebook",
                    "platformId": "179995481217",
                    "accountType": "facebook_page",
                    "pageAdminTopCountry": "NZ",
                    "verified": true
                },
                {
                    "id": 890542,
                    "name": "180graus",
                    "handle": "portal180",
                    "profileImage": "https://scontent-sea1-1.xx.fbcdn.net/v/t1.0-1/p200x200/21317492_1550607891667164_6010646426118565060_n.png?_nc_cat=1&ccb=2&_nc_sid=dbb9e7&_nc_ohc=L4KDOPydKawAX8s6P3U&_nc_ht=scontent-sea1-1.xx&oh=54d627c3a9f0f29d47a008422166ecd6&oe=5FC11277",
                    "subscriberCount": 498309,
                    "url": "https://www.facebook.com/133619913365976",
                    "platform": "Facebook",
                    "platformId": "133619913365976",
                    "accountType": "facebook_page",
                    "pageAdminTopCountry": "BR",
                    "verified": false
                },
                {
                    "id": 125506,
                    "name": "3al6ayer على الطاير",
                    "handle": "3al6ayer",
                    "profileImage": "https://scontent-sea1-1.xx.fbcdn.net/v/t1.0-1/p200x200/998336_681411518551934_1908797493_n.jpg?_nc_cat=102&ccb=2&_nc_sid=dbb9e7&_nc_ohc=lvNmqMEq_xIAX_TGB5O&_nc_ht=scontent-sea1-1.xx&tp=6&oh=088d3ca604cc66319bd182957c429d91&oe=5FC1FD04",
                    "subscriberCount": 165400,
                    "url": "https://www.facebook.com/167202989972792",
                    "platform": "Facebook",
                    "platformId": "167202989972792",
                    "accountType": "facebook_page",
                    "pageAdminTopCountry": "SA",
                    "verified": false
                },
                {
                    "id": 73861,
                    "name": "7NEWS Brisbane",
                    "handle": "7NEWSBrisbane",
                    "profileImage": "https://scontent-sea1-1.xx.fbcdn.net/v/t1.0-1/p200x200/110153825_3519595848053242_4551573958521464986_o.jpg?_nc_cat=1&ccb=2&_nc_sid=dbb9e7&_nc_ohc=J4dfl6cHW9gAX_8Rqo4&_nc_ht=scontent-sea1-1.xx&tp=6&oh=d807f3b3de789deb0e5eeb8dea2635ef&oe=5FBF3622",
                    "subscriberCount": 879485,
                    "url": "https://www.facebook.com/130736376939223",
                    "platform": "Facebook",
                    "platformId": "130736376939223",
                    "accountType": "facebook_page",
                    "pageAdminTopCountry": "AU",
                    "verified": true
                },
                {
                    "id": 370544,
                    "name": "20minutos.es",
                    "handle": "20minutos.es",
                    "profileImage": "https://scontent-sea1-1.xx.fbcdn.net/v/t1.0-1/p200x200/101918673_10158805078443028_8487187545371705344_n.jpg?_nc_cat=1&ccb=2&_nc_sid=dbb9e7&_nc_ohc=eAgajQdoI6QAX8tpvjc&_nc_ht=scontent-sea1-1.xx&tp=6&oh=3d97d06c47b5bdc49d32b7639f1ef9bc&oe=5FC0ADE7",
                    "subscriberCount": 1182770,
                    "url": "https://www.facebook.com/38352573027",
                    "platform": "Facebook",
                    "platformId": "38352573027",
                    "accountType": "facebook_page",
                    "pageAdminTopCountry": "ES",
                    "verified": true
                },
                {
                    "id": 126940,
                    "name": "8视界新闻新加坡 8world News",
                    "handle": "8worldnews",
                    "profileImage": "https://scontent-sea1-1.xx.fbcdn.net/v/t1.0-1/p200x200/67619567_2718618618156437_1151093394726977536_o.jpg?_nc_cat=1&ccb=2&_nc_sid=dbb9e7&_nc_ohc=gTsIUOT20AEAX8xZruI&_nc_ht=scontent-sea1-1.xx&tp=6&oh=e1cade89b1c644d32f186b4fd5599c0e&oe=5FBFDD41",
                    "subscriberCount": 541283,
                    "url": "https://www.facebook.com/140711089280549",
                    "platform": "Facebook",
                    "platformId": "140711089280549",
                    "accountType": "facebook_page",
                    "pageAdminTopCountry": "SG",
                    "verified": true
                },
                {
                    "id": 126958,
                    "name": "7NEWS Australia",
                    "handle": "7NewsAustralia",
                    "profileImage": "https://scontent-sea1-1.xx.fbcdn.net/v/t1.0-1/p200x200/112317767_4000945319915631_7312856053571991158_n.jpg?_nc_cat=1&ccb=2&_nc_sid=dbb9e7&_nc_ohc=Rs8hBtmGC2UAX_TBxSR&_nc_ht=scontent-sea1-1.xx&tp=6&oh=9328967efcc8f1d6fac13d5773ba3fb0&oe=5FBFE517",
                    "subscriberCount": 2058247,
                    "url": "https://www.facebook.com/114503341893201",
                    "platform": "Facebook",
                    "platformId": "114503341893201",
                    "accountType": "facebook_page",
                    "pageAdminTopCountry": "AU",
                    "verified": true
                }
            ],
            "pagination": {
                "nextPage": "https://api.crowdtangle.com/lists/:listId/accounts?token=TOKEN"
            }
        }
    }

Account
=======

### [](#account)Account

An Account Object represents a page, account or user on a given platform. See examples in [/posts](https://github.com/CrowdTangle/API/wiki/Posts).

#### [](#properties)Properties

| Property | Type | Descriptions |
| --- | --- | --- |
| accountType | string | For Facebook only. Options are facebook\_page, facebook\_profile, facebook\_group. |
| handle | string | The handle or vanity URL of the account. |
| id  | int | The unique identifier of the account in the CrowdTangle system. This ID is specific to CrowdTangle, not the platform on which the account exists. |
| name | string | The name of the account. |
| pageAdminTopCountry | string | The [ISO country code](https://en.m.wikipedia.org/wiki/List_of_ISO_3166_country_codes#Current_ISO_3166_country_codes) of the the country from where the plurality of page administrators operate. |
| pageCategory | string | The page category as submitted by the page. View all page categories [here](https://www.facebook.com/pages/category/). |
| pageCreatedDate | int | The date on which the page was created. |
| pageDescription | string | The description of the page as documented in Page Transparency information. |
| platform | enum (facebook, instagram, reddit) | The platform on which the account exists. |
| platformId | string | The platform's ID for the account. This is not shown for Facebook public users. |
| profileImage | string | A URL pointing at the profile image. |
| subscriberCount | int | The number of subscribers/likes/followers the account has. By default, the subscriberCount property will show page Followers (as of January 26, 2021). You can select either Page Likes or Followers in your Dashboard settings. [Learn more here.](https://help.crowdtangle.com/en/articles/4797890-faq-measuring-followers) |
| url | string | A link to the account on its platform. |
| verified | boolean | Whether or not the account is verified by the platform, if supported by the platform. If not supported, will return false. |

Post
====

### [](#post)Post

A post object represents a single post from any of the supported platforms (e.g., Facebook, Instagram). All posts also contain an [account object](https://github.com/CrowdTangle/API/wiki/Account). Below are the properties of a post. See examples in [/posts](https://github.com/CrowdTangle/API/wiki/Posts).

#### [](#properties)Properties

| Property | Type | Description |
| --- | --- | --- |
| account | [Account](https://github.com/CrowdTangle/API/wiki/Account) | See [account](https://github.com/CrowdTangle/API/wiki/Account). |
| brandedContentSponsor | [Account](https://github.com/CrowdTangle/API/wiki/Account) | See [account](https://github.com/CrowdTangle/API/wiki/Account). This field is only present for Facebook Page posts where there is a sponsoring Page. |
| caption | text | The caption to a photo, if available. |
| date | date ("yyyy‑mm‑dd hh:mm:ss") | The date and time the post was published. Time zone is UTC. |
| description | text | Further details, if available. Associated with links or images across different platforms. |
| expandedLinks | map of text | A map where the keys are the original links that came in the post (which are often shortened), and the values are the expanded links. |
| id  | string ("account.id\|postExternalId") | The unique identifier of the post in the CrowdTangle system. This ID is specific to CrowdTangle, not the platform from which the post originated. |
| imageText | string | The text, if it exists, within an image. |
| legacyid | int | The legacy version of the unique identifier of the post in the CrowdTangle system. This ID is specific to CrowdTangle, not the platform from which the post originated. |
| link | string | An external URL that the post links to, if available. (Facebook only) |
| media | array of [media](#media) | An array of available media for the post. |
| message | text | The user-submitted text on a post. |
| platform | enum (facebook, instagram, reddit) | The platform on which the post was posted. E.g., Facebook, Instagram, etc. |
| platformId | string | The platform's ID for the post. |
| postUrl | string | The URL to access the post on its platform. |
| score | double | The score of a post as measured by the request. E.g. it will represent the overperforming score if the request `sortBy` specifies `overperforming`, the interaction rate if the request specifies `interaction_rate`, etc. |
| statistics | [Statistics](#statistics) | Performance metrics associated with the post. |
| subscriberCount | int | The number of subscriber the account had _when the post was published_. This is in contrast to the subscriberCount found on the [account](https://github.com/CrowdTangle/API/wiki/Account), which represents the current number of subscribers an account has. |
| type | enum (album, igtv, link, live\_video, live\_video\_complete, live\_video\_scheduled, native\_video, photo, status, video, vine, youtube) | The type of the post. |
| updated | date ("yyyy‑mm‑dd hh:mm:ss") | The date and time the post was most recently updated in CrowdTangle, which is most often via getting new scores from the platform. Time zone is UTC. |
| videoLengthMS | int | The length of the video in milliseconds. |
| liveVideoStatus | string ("live", "completed", "upcoming") | The status of the live video. |

### [](#statistics)Statistics

Two sets of metrics for a post: `actual` and `expected`. `actual` represents the actual metrics of the post, e.g., likeCount or commentCount. `expected` represents what that post's metrics were expected to be given that post's properties, as calculated by CrowdTangle. These metrics differ by `platform`. For instance, Facebook will include, "likeCount," "commentCount," and "shareCount" while Instagram includes "favoriteCount" and "commentCount." The full list is below.

#### [](#properties-1)Properties

| Property | Type | Description |
| --- | --- | --- |
| actual | Map<String, Long> | A set of key-value pairs representing the actual metrics of the post. |
| expected | Map<String, Long> | A set of key-values pairs representing the metrics CrowdTangle expected a post like this to accrue. |

##### [](#possible-metrics)Possible Metrics

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

\*The purple flower "Thankful" reaction was a temporary reaction available in 2016 and 2017. (See more [HERE](https://about.fb.com/news/2017/05/join-facebook-in-celebrating-moms-around-the-world/)). This metric surfaces thankfulCount for legacy posts that accrued Thankful reactions prior to the reaction's removal from Facebook.

### [](#media)Media

The media object represents a piece of media (e.g., video, photo) for a post. It contains the type, source and any additional metadata.

#### [](#properties-2)Properties

| Property | Type | Description |
| --- | --- | --- |
| full | string | The source of the full-sized version of the media. |
| height | int | The height of the media. |
| type | enum (photo or video) | The type of the media. |
| url | string | The source of the media. |
| width | int | The width of the media. |

List
====

### [](#list)List

A List Object represents a list, saved search or saved post list in a dashboard [/lists](https://github.com/CrowdTangle/API/wiki/Lists).

#### [](#properties)Properties

| Property | Type | Descriptions |
| --- | --- | --- |
| title | string | The title of the list as it appears in the dashboard |
| id  | int | The unique identifier of the list in the CrowdTangle system. Use this id when querying by the `listIds` parameters. |
| type | enum (SAVED\_SEARCH, SAVED\_POSTS, LIST) | The type of the list corresponding with its function in the dashboard. |

AccountStatistics
=================

### [](#accountstatistics)AccountStatistics

An AccountStatistics object represents the aggregate statistics of an [account](https://github.com/CrowdTangle/API/wiki/Account) over the specified time. A list of these objects makes up a leaderboard, see examples in [/leaderboard](https://github.com/CrowdTangle/API/wiki/Leaderboard).

#### [](#properties)Properties

| Property | Type | Description |
| --- | --- | --- |
| account | [account](https://github.com/CrowdTangle/API/wiki/Account) | Details about the account not related to statistics. |
| breakdown | Map<String, [StatisticSet](https://github.com/CrowdTangle/API/wiki/AccountStatistics#StatisticSet)\> | A StatisticSet for each type of [post](https://github.com/CrowdTangle/API/wiki/Post) the account posted. E.g. photo, video, etc. |
| subscriberData | [SubscriberData](https://github.com/CrowdTangle/API/wiki/AccountStatistics#SubscriberData) | The subscriberCounts relevant to the date range requested. |
| summary | [StatisticSet](https://github.com/CrowdTangle/API/wiki/AccountStatistics#StatisticSet) | An aggregate StatisticSet of the `breakdown`. |

### [](#statisticset)StatisticSet

Aggregate data for the account in question. Includes basic metrics (likeCount, commentCount, shareCount) as well as some additional metrics. Some of these metrics are platform specific. See [Post/statistics](https://github.com/CrowdTangle/API/wiki/Post#statistics) for the by-platform breakdown.

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

### [](#subscriberdata)SubscriberData

The subscriberData for the given date range.

| Property | Type | Description |
| --- | --- | --- |
| finalCount | int | The number of the subscribers the account had at the end of the date range. |
| initialCount | int | The number of subscribers the account had at the start of the date range. |
| notes | String | Human-readable notes. Counts may not be available for selected date ranges based on when we started tracking an account within CrowdTangle. If initialCount or finalCount is 0, we likely were not tracking the account at that time. This can be confirmed by referencing the notes section which could look like this: "No subscriberCount available for beginning of time range." If the note section is present at all, any calculations made with subscriberCount data will need to take into account potentially missing data. |

Pagination
==========

### [](#pagination)Pagination

An Pagination object offers API endpoints to call for the next or previous pages. The CrowdTangle API simply uses counts and offsets to paginate, so constructing your own pagination URLs is simple as well.

#### [](#properties)Properties

| Property | Type | Descriptions |
| --- | --- | --- |
| nextPage | string | The API URL to call for the next page, if available. |
| previousPage | string | The API URL to call for the previous page, if available. |

Errors
======

### [](#errors)Errors

Every error returned by the CrowdTangle API will assume a standard format. The API will additionally return a proper http status as well. If a `200` is returned, there was no error.

#### [](#error-response)Error Response

| Property | Type | Description |
| --- | --- | --- |
| code | int | The [CrowdTangle error code](https://github.com/CrowdTangle/API/wiki/Errors#errorcodes), if available. |
| message | string | A human-readable message describing the error. Always returned. |
| status | int | The HTTP status code, if available. |
| url | string | A URL for more information, if available. |

For example:

    {
      "status": 401,
      "code": 30,
      "message": "Please supply an API token"
    }
    

#### [](#crowdtangle-error-codes)CrowdTangle Error Codes

| Code | Description |
| --- | --- |
| 20  | Unknown Parameter |
| 21  | Illegal Parameter Value |
| 22  | Missing Parameter |
| 30  | Missing Token |
| 31  | Invalid Token |
| 40  | Does Not Exist |
| 41  | Not Allowed |

Formats
=======

### [](#formats)Formats

The CrowdTangle API supports two formats: xml and json. Requesting the different formats is easy: simply add the extension to the specified endpoint. For example:

`https://api.crowdtangle.com/posts.json //=> json`

`https://api.crowdtangle.com/posts.xml //=> xml`

Terms and Policy
================

By using the CrowdTangle API, you agree to follow the guidelines set forth by the following policy:

[](#things-you-care-about)Things You Care About
-----------------------------------------------

* Tokens
    * To make calls to the API, you must use your own token(s), which you can find in your dashboard(s).
* Rate Limits
    * Rate limits are set at different levels for different calls, starting as low as 2 per minute per token. We also have internal limits for memory/data/CPU usage and will contact users who go over them.
* Visibility
    * Do not connect front-end widgets directly to our API. Have your back end pull from the API and cache it, and make the front end use your cache.

[](#boring-stuff)Boring Stuff
-----------------------------

* Platforms
    * The CrowdTangle API includes data from social media platforms. The platforms' individual policies apply to similar objects from CrowdTangle. For example, relevant data from a Facebook post found through the CrowdTangle API remains bound by the Facebook policies.
* Modification
    * We reserve the right to change this policy at any time without notice or liability to you. Continued use of the API constitutes acceptance of any modifications.
* Termination
    * If you fail to comply with the policy, we have the right to revoke your API access.
    * If you disagree with any parts of the policy, you may terminate this policy by discontinuing use of our API.
* Terms
    * CrowdTangle, Inc ("CrowdTangle", "we", "us", "our").
    * The CrowdTangle publicly available Application Programming Interface as well as the related API Documentation ("API").
    * A person using the API or on behalf of a legal entity with the authority to bind such entity to the policy ("you", "your").
* Responsibility
    * You agree to defend, indemnify and hold harmless CrowdTangle from and against all damages, losses, and expenses of any kind (including reasonable legal fees and costs) related to any claim against us related to your service, actions, content or information.
    * API use remains bound by the terms already agreed to with CrowdTangle, which may be our [general terms](https://www.crowdtangle.com/terms).