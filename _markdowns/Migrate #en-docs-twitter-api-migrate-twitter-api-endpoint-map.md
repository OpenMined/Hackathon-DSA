



Twitter API endpoint map | Docs | Twitter Developer Platform 





































































































Twitter API endpoint map



X API endpoint map
------------------


The following table maps the X API v2 endpoints to the corresponding standard v1.1, and enterprise endpoints. To learn more about each of these versions and tiers, please visit our X API getting started guide.


You'll notice that we still have several items marked as **[Coming Soon]**. If you notice anything within this table that is marked as **[Replacement Under Consideration]** or **[No Replacement Planned]**, and you would like to see us release a v2 version of that endpoint, please let us know via our community forum or your enterprise account manager. 








|  | Standard v1.1 | Enterprise | X API v2 |
| --- | --- | --- | --- |
| **Tweets** | GET statuses/show
GET statuses/lookup |  | Tweets lookup |
| POST statuses/update
POST statuses/destroy/:id |  | Manage Tweets |
| GET statuses/user\_timeline
GET statuses/mentions\_timeline
GET statuses/home\_timeline |  | Timelines
- User Tweet timeline
- User mention timeline
- Reverse chronological home timeline |
| GET search/tweets (7 days) | Search API
- 30 day
- Full-archive | Search Tweets
- Recent search
- 30 day [No Replacement Planned]
- Full-archive search |
|  | Search API
- 30 day
- Full-archive | Tweet counts
- Recent Tweet counts
- 30 day [No Replacement Planned]
- Full-archive Tweet counts |
| GET statuses/filter | PowerTrack API | Filtered stream
- Connect to stream
- Add/delete rules
- Retrieve rules |
| GET statuses/sample (1%) | Decahose API
Firehose API | Volume stream
- 1% sampled stream
- 10% decahose stream 
- 100% firehose stream |
| GET statuses/retweeters/:ids
GET statuses/retweets/:id |  | Retweets lookup |
|  |  | Quote Tweets lookup |
| POST statuses/retweet/:id
POST statuses/unretweet/:id |  | Manage Retweets
- Retweet a Tweet
- Undo a Retweet |
| GET favorites/list |  | Likes lookup
- Tweets liked by a user
- Users who have liked a Tweet [NEW to v2] |
| POST favorites/create
POST favorites/destroy |  | Manage Likes
- Like a Tweet
- Unlike a Tweet |
|  |  | Hide replies [NEW to v2] |
| GET statuses/oembed |  | [No Replacement Planned] |
| GET statuses/retweets\_of\_me |  | [No Replacement Planned] |
| **Users** | GET users/show
GET users/lookup |  | Users lookup |
| GET users/search |  | Get user/search |
| GET followers/ids
GET followers/list
GET friends/ids
GET friends/list |  | Follows lookup |
| GET friendships/incoming
GET friendships/lookup
GET friendships/no\_retweets/ids
GET friendships/outgoing
GET friendships/show |  | [Coming Q1-2024]:
friendships/lookup/
friendships/show/ |
| GET friendships/create
GET friendships/destroy |  | Manage follows
- Follow a user
- Unfollow a user |
| POST friendships/update |  | [No Replacement Planned] |
| GET blocks/ids
GET blocks/list |  | Blocks lookup |
| POST blocks/create
POST blocks/destroy |  | Manage blocks
- Block a user
- Unblock a user |
| GET mutes/users/ids
GET mutes/users/list |  | Mutes lookup |
| POST mutes/users/create
POST mutes/users/destroy |  | Manage mutes
- Mute a user
- Unmute a user |
| GET account/settings
GET account/verify\_credentials
GET users/profile\_banner
POST account/settings
POST account/update\_profile
POST account/update\_profile\_banner
POST account/remove\_profile\_banner
POST account/update\_profile\_image |  | [No Replacement Planned] |
| GET saved\_searches/show/:id
GET saved\_searches/list
POST saved\_searches/create
POST saved\_searches/destroy/:id |  | [No Replacement Planned] |
| POST users/report\_spam |  | [No Replacement Planned] |
|  | Account Activity API | [Migrating to Developer Portal Q1/Q2] |
| **Spaces** |  |  | Spaces lookup [NEW to v2] |
|  |  | Spaces search [NEW to v2] |
|  |  | Spaces reminders lookup [COMING SOON]
[NEW to v2] |
|  |  | Manage Spaces reminders [COMING SOON]
[NEW to v2] |
|  |  | Ticketed user lookup
[NEW to v2] |
|  |  | Tweets shared in a Space lookup [NEW to v2] |
| **Direct Messages** |  |  | Direct Messages lookup
Manage Direct Messages |
| **Lists** | GET lists/show |  | Lists lookup |
| POST lists/create
POST lists/destroy
POST lists/update |  | Manage Lists |
| GET lists/statuses |  | Lists Tweets lookup |
| GET lists/members
GET lists/memberships
POST lists/members/create
POST lists/members/destroy |  | List members |
| GET lists/subscribers
GET lists/subscriptions
GET lists/lists
POST lists/subscribers/create
POST lists/subscribers/destroy |  | Lists follows |
| GET lists/ownerships |  | Owned Lists lookup |
|  |  | Pinned Lists [NEW to v2] |
| GET lists/members/show
GET lists/subscribers/show |  | [No Replacement Planned] |
| POST lists/members/create\_all
POST lists/members/destroy\_all |  | [No Replacement Planned] |
| **Media** |  |  | [Coming Q1/Q2 2024] |
| **Trends** |  |  | Trends v2 |
| **Geo** |  |  | [No Replacement Planned] |
| **Collections** | GET collections/entries
GET collections/list
GET collections/show
POST collections/create
POST collections/destroy
POST collections/entries/add
POST collections/entries/curate
POST collections/entries/move
POST collections/entries/remove
POST collections/update |  | [No Replacement Planned] |
| **Metrics** |  | Engagement API
- /totals
- /28hr
- /historical | /totals - data is built into v2 responses
/28hr - [Replacement under consideration]
/historical - [Replacement under consideration] |
| **Compliance** |  |  | Batch compliance
[NEW to v2] |
|  | Compliance firehose | Compliance streams |
| **Utilities** |  | Usage API | Usage API |
| GET application/rate\_limit\_status |  | [No Replacement Planned] |
| GET help/languages |  | [No Replacement Planned] |
| **Authentication** |  |  | [No Changes Planned] |



















Developer policy and terms


Follow @XDevelopers


Subscribe to developer news












#### 
 X platform


* X.com
* Status
* Accessibility
* Embed a post
* Privacy Center
* Transparency Center
* Download the X app




#### 
 X Corp.


* About the company
* Company news
* Brand toolkit
* Jobs and internships
* Investors




#### 
 Help


* Help Center
* Using X
* X for creators
* Ads Help Center
* Managing your account
* Email Preference Center
* Rules and policies
* Contact us




#### 
 Developer resources


* Developer home
* Documentation
* Forums
* Communities
* Developer blog
* Engineering blog
* Developer terms




#### 
 Business resources


* Advertise
* X for business
* Resources and guides
* X for marketers
* Marketing insights
* Brand inspiration
* X Ads Academy









 © 2024 X Corp.
 


Cookies


Privacy


Terms and conditions






















**Did someone say … cookies?**  
  


 X and its partners use cookies to provide you with a better, safer and
 faster service and to support our business. Some cookies are necessary to use
 our services, improve our services, and make sure they work properly.
 Show more about your choices.


 




* Accept all cookies
* Refuse non-essential cookies















