
Timelines version comparison | Docs | Twitter Developer Platform 

Migrate

Comparing Twitter API's timelines endpoints
-------------------------------------------

The v2 reverse chronological timeline, user Tweets timeline, and user mention timeline endpoints replace the v1.1 statuses/home\_timeine, v1.1 statuses/user\_timeline, and v1.1 statuses/mentions\_timeline endpoints respectively. If you have code, apps, or tools that use an older version of this endpoint and are considering migrating to the newer Twitter API v2 endpoint, then this guide is for you.  For a more in-depth migration guide see Standard v1.1 migration to Twitter API v2.

This page contains three comparison tables:

* Reverse chronological home timeline
* User Tweet timeline
* User mention timeline

### Reverse chronological home timeline

The following tables compare the standard v1.1 and Twitter API v2 home timeline endpoints:

|  |  |  |
| --- | --- | --- |
| **Description** | **Standard v1.1** | **Twitter API v2** |
| Documentation | API Reference | API Reference |
| HTTP methods supported | `GET` | `GET` |
| Host domain | `https://api.twitter.com` | `https://api.twitter.com` |
| Endpoint paths | `/1.1/statuses/home_timeline.json` | `/2/users/:id/timelines/reverse_chronological` |
| Required parameters | `user_id` or `screen_name` | User ID set as path parameter :id |
| Authentication | OAuth 1.0a User Context
  | OAuth 1.0a User Context
OAuth 2.0 Authorization Code Flow with PKCE |
| Request rate limits/Volume limits | 15 requests per 15-minute with OAuth 1.0a User Context
Request cap: 100,000 within a 24 hour period. | 180 requests per 15-minute window 
Tweet cap:
500,000 when using Essential access
2 million when using Elevated access
10 million when using Academic Research access |
| Default Tweets per response | 15 | 100 |
| Maximum Tweets per response | 800 | This endpoint returns every Tweet created on a timeline over the last 7 days as well as the most recent 800 regardless of creation date. |
| Provides Tweet edit history | ✔ | ✔ |
| Historical Tweets available | The most recent 800 Tweets, including Retweets | The most recent 3,200 Tweets, including Retweets |
| Timeline navigation options | since\_id (exclusive) used for update polling
`max_id` (inclusive) | `start_time`
end\_time
`since_id`(exclusive) used for update polling 
`until_id` (exclusive)  |
| Optional parameters for results refinement | `count`
`exclude_replies`
`include_rts`
`trim_user`
`tweet_mode`
`since_id`
`max_id` | `max_results`
`exclude`(retweets,replies)
`tweet.fields`
`user.fields`
`place.fields`
`media.fields`
`poll.fields`
`expansions`
`start_time`
`end_time`
`since_id`
`until_id` |
| Supports requesting and receiving annotations | N/A | If annotations are included in tweet.fields, results will be annotated with inferred annotation data based on the Tweet text, such as 'Music Genre' and 'Folk Music' or 'Musician' and 'Dolly Parton' |
| Supports requesting and receiving specific Tweet metrics | N/A | If annotations are included in `tweet.fields`, results will be annotated with public\_metrics per Tweet including `retweet_count`, `reply_count`, `quote_count` and `like_count`, `non_public_metrics` , including `impression_count`, `user_profile_clicks`, `url_link_clicks`.
Additional media metrics such as view\_count and video playback metrics.
Additional organic\_metrics and promoted\_metrics available with User Context for promoted Tweets. |
| Supports requesting and receiving conversation\_id | N/A | Returns a conversation\_id field where the value represents the first published Tweet in a reply thread to help you track conversations.  |
| Tweet JSON format | Standard v1.1 data format | Twitter API v2 format (determined by fields and expansions request parameters, not backward-compatible with v1.1 formats)
To learn more about how to migrate from the Standard v1.1 format to the Twitter API v2 format, please visit our data formats migration guide. |
| Results order | Reverse chronological | Reverse chronological |
| Results pagination | N/A must use navigation by Tweet ID | Results can be reviewed moving forward or backward using a pagination\_token |
| Requires the use of credentials from a developer App associated with a Project |   | ✔ |

### User Tweet timeline

The following tables compare the standard v1.1 and Twitter API v2 user Tweet timeline endpoints:

|  |  |  |
| --- | --- | --- |
| **Description** | **Standard v1.1** | **Twitter API v2** |
| Documentation | API Reference | API Reference |
| HTTP methods supported | GET | GET |
| Host domain | https://api.twitter.com | https://api.twitter.com |
| Endpoint paths | /1.1/statuses/user\_timeline.json
 | /2/users/:id/tweets |
| Required parameters | user\_id or screen\_name | User ID set as path parameter :id |
| Authentication | OAuth 1.0a User Context
OAuth 2.0 App-Only
 | OAuth 1.0a User Context
OAuth 2.0 App-Only
OAuth 2.0 Authorization Code with PKCE |
| Request rate limits/Volume limits | 900 requests per 15 min with OAuth 1.0a User Context
1500 requests per 15 min with OAuth 2.0 App-Only
Request cap: 100,000 within a 24 hour period. | 900 requests per 15-minute window with OAuth 1.0a User Context
1500 requests per 15-minute window with OAuth 2.0 App-Only
Tweet cap:
500,000 when using Essential access
 2 million when using Elevated access
 10 million when using Academic Research access |
| Default Tweets per response | 15 | 10 |
| Maximum Tweets per response | 200 | 100 |
| Historical Tweets available | The most recent 3,200 Tweets, including Retweets | The most recent 3,200 Tweets, including Retweets |
| Timeline navigation options | since\_id (exclusive) used for update polling
max\_id (inclusive) | start\_time
end\_time
since\_id (exclusive) used for update polling 
until\_id (exclusive)  |
| Optional parameters for results refinement | count
 exclude\_replies
 include\_rts
 trim\_user
 tweet\_mode
 since\_id
 max\_id | max\_results
exclude(retweets,replies)
tweet.fields
 user.fields
 place.fields
 media.fields
 poll.fields
 expansions
 start\_time
 end\_time
 since\_id
 until\_id |
| Supports requesting and receiving annotations | N/A | Returns Tweet results with inferred annotation data based on the Tweet text, such as 'Music Genre' and 'Folk Music' or 'Musician' and 'Dolly Parton' |
| Supports requesting and receiving specific Tweet metrics | N/A | Returns Tweet results with available public\_metrics per Tweet including retweet\_count, reply\_count, quote\_count and like\_count.
Available with OAuth1.0a User Context:
Additional non\_public\_metrics , including impression\_count, user\_profile\_clicks, url\_link\_clicks.
Additional media metrics such as view\_count and video playback metrics.
Additional organic\_metrics and promoted\_metrics available with OAuth 1.0a User Context for promoted Tweets. |
| Supports requesting and receiving conversation\_id | N/A | Returns a conversation\_id field where the value represents the first published Tweet in a reply thread to help you track conversations.  |
| Tweet JSON format | Standard v1.1 data format | Twitter API v2 format (determined by fields and expansions request parameters, not backward-compatible with v1.1 formats)
To learn more about how to migrate from the Standard v1.1 format to the Twitter API v2 format, please visit our data formats migration guide. |
| Results order | Reverse chronological | Reverse chronological |
| Results pagination | N/A must use navigation by Tweet ID | Results can be reviewed moving forward or backward using a pagination\_token |
| Requires the use of credentials from a developer App associated with a Project |  | ✔ |
| Provides Tweet edit history | ✔ | ✔ |

### User mention timeline

The following tables compare the standard v1.1 and Twitter API v2 user mention timeline endpoints

|  |  |  |
| --- | --- | --- |
| **Description** | **Standard v1.1** | **Twitter API v2** |
| Documentation | API Reference | API Reference |
| HTTP methods supported | GET | GET |
| Host domain | https://api.twitter.com | https://api.twitter.com |
| Endpoint paths | /1.1/statuses/mentions\_timeline.json | /2/users/:id/mentions |
| Required parameters | no required parameters | User ID set as path parameter :id |
| Authentication | OAuth 1.0a User Context | OAuth 1.0a User Context
OAuth 2.0 App-Only
OAuth 2.0 Authorization Code with PKCE |
| Default request rate limits | 75 requests per 15 min with OAuth 1.0a User Context
100,000 request cap within a 24 hour period. | 180 requests per 15-minute window with OAuth 1.0a User Context
450 requests per 15-minute window with OAuth 2.0 App-Only
Tweet cap:
500,000 when using Essential access
2 million when using Elevated access
 10 million when using Academic Research access |
| Default Tweets per response | 15 | 10 |
| Maximum Tweets per response | 200 | 100 |
| Historical Tweets available | The most recent 800 Tweets | The most recent 800 Tweets |
| Timeline navigation options | since\_id (exclusive) used for update polling
max\_id (inclusive) | start\_time
end\_time
since\_id (exclusive) used for update polling
until\_id (exclusive) |
| Optional parameters for results refinement | count
 trim\_user
 include\_entities
 tweet\_mode
 since\_id
 max\_id | max\_results
 tweet.fields
 user.fields
 place.fields
 media.fields
 poll.fields
 expansions
 start\_time
 end\_time
 since\_id
 until\_id |
| Supports requesting and receiving annotations | N/A | Returns Tweet results with inferred anotation data based on the Tweet text, such as 'Music Genre' and 'Folk Music' or 'Musician' and 'Dolly Parton' |
| Supports requesting and receiving specific Tweet metrics | N/A | Returns Tweet results with available public\_metrics per Tweet including retweet\_count, reply\_count, quote\_count and like\_count.
Available with OAuth 1.0a User Context:
Additional non\_public\_metrics , including impression\_count, user\_profile\_clicks, url\_link\_clicks. 
Additional media metrics such as view\_count and video playback metrics.
Additional organic\_metrics and promoted\_metrics available with OAuth 1.0a User Context for promoted Tweets |
| Supports requesting and receiving conversation\_id | N/A | Returns a conversation\_id field where the value represents the first published Tweet in a reply thread to help you track conversations.  |
| Tweet JSON format | Standard v1.1 data format | Twitter API v2 format (determined by fields and expansions request parameters, not backward-compatible with v1.1 formats)
To learn more about how to migrate from the Standard v1.1 format to the Twitter API v2 format, please visit our data formats migration guide. |
| Results order | Reverse chronological | Reverse chronological |
| Request parameters for pagination | N/A must use navigation by Tweet ID | Results can be reviewed moving forward or backward using pagination\_token |
| Requires the use of credentials from a developer App associated with a Project |  | ✔ |
| Provides Tweet edit history | ✔ | ✔ |

Other migration resources
-------------------------

Tweet lookup: Standard v1.1 to Twitter API v2

Twitter API migration hub

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