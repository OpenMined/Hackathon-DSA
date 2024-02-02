
Retweets comparison guide | Docs | Twitter Developer Platform 

Migrate

Comparing Twitter API’s Retweets endpoints
------------------------------------------

Retweets lookup  

The v2 Retweets lookup endpoint will replace the standard v1.1 GET statuses/retweets/:id and v1.1 GET statuses/retweets/:ids endpoints.

The following tables compare the standard v1.1 and Twitter API v2 Retweets endpoints:

| Description | Standard v1.1 | Twitter API v2 |
| --- | --- | --- |
| HTTP methods supported | GET | GET |
| Host domain | https://api.twitter.com | https://api.twitter.com |
| Endpoint path | /1.1/retweeters/id.json
`/1.1/retweets/ids.json` | /2/users/:id/retweeted\_by |
| Authentication | OAuth 1.0a User Context | OAuth 2.0 Bearer Token
OAuth 1.0a User Context |
| Default request rate limits | 75 requests per 15 min | 75 requests per 15 min (per App)
75 requests per 15 min (per user) |
| Data format | Standard v1.1 format | Twitter API v2 format (determined by fields and expansions request parameters, not backward-compatible with v1.1 formats)
To learn more about how to migrate from the Standard v1.1 format to the Twitter API v2 format, please visit our data formats migration guide. |
| Requires the use of credentials from a developer App that is associated with a Project |  | ✔️ |

### 

### Manage Retweets

The following tables compare the standard v1.1 and Twitter API v2 undo Retweet endpoint:

**Retweet a Tweet**

| Description | Standard v1.1 | Twitter API v2 |
| --- | --- | --- |
| HTTP methods supported | POST | POST |
| Host domain | https://api.twitter.com | https://api.twitter.com |
| Endpoint path | /1.1/statuses/retweet/:id.json | /2/users/:id/retweets |
| Authentication | OAuth 1.0a User Context | OAuth 1.0a User Context |
| Default request rate limits | None
300 requests per 3-hour window (per user, per app). This is shared with the POST Tweet endpoint | 50 requests per 15 min (per user)
300 requests per 3-hour window (per user, per app). This is shared with the POST Tweet endpoint for manage Tweets.
  |
| Requires the use of credentials from a developer App that is associated with a Project |  | ✔️ |

#### 
Undo a Retweet

The following tables compare the standard v1.1 and Twitter API v2 undo Retweet endpoint:

| Description | Standard v1.1 | Twitter API v2 |
| --- | --- | --- |
| HTTP methods supported | POST | DELETE |
| Host domain | https://api.twitter.com | https://api.twitter.com |
| Endpoint path | /1.1/statuses/unretweet/:id.json | /2/users/:id/retweets/:source\_tweet\_id |
| Authentication | OAuth 1.0a User Context | OAuth 1.0a User Context |
| Default request rate limits | None | 50 requests per 15 min (per user) |
| Requires the use of credentials from a developer App that is associated with a Project |  | ✔️ |

Other migration resources
-------------------------

Retweets lookup: Standard v1.1 to Twitter API v2

Manage Retweets: Standard v1.1 to Twitter API v2

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