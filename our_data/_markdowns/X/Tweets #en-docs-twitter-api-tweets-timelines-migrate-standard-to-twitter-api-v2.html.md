
Timelines standard v1.1 to v2 migration guide | Docs | Twitter Developer Platform 

Standard v1.1 migration to Twitter API v2

Standard v1.1 timelines to Twitter API v2 timelines
---------------------------------------------------

If you have been working with the v1.1 timelines endpoints (statuses/user\_timeline and statuses/mentions\_timeline), the goal of this guide is to help you understand the similarities and differences between the standard and Twitter API v2 timelines endpoints so that you can migrate your current integration to the new version.

* **Similarities:**
	+ Authentication:
		- OAuth 1.0a User Context (reverse chronological home timeline, user Tweet timeline and user mentions timeline)
		- OAuth 2.0 App-Only (user Tweet timeline)
	+ Historical Access limit: User timeline (user Tweet timeline) provides access to most recent 3200 Tweets; mentions timeline (user mention timeline) provides access to most recent 800 mentions.
	+ Support for Tweet edit history and metadata
	+ Rate limits (user Tweet timeline)
	+ Refresh polling: Ability to retrieve new results since the since\_id
	+ Traversing timelines by Tweet IDs
	+ Results specifications:
		- Results order: Results returned in reverse chronological order
		- Ability to exclude replies (user Tweet timeline only)
		- Ability to exclude Retweets (user Tweet timeline only)
* **Differences**
	+ New Authentication capability:
		- OAuth 2.0 App-Only (user mention timeline)
		- OAuth 2.0 Authorization Code Flow with PKCE (reverse chronological home timeline, user Tweet timeline and user mentions timeline)
	+ Access requirements: Twitter API v2 App and Project requirements
	+ Rate limits (user mention timeline and reverse chronological home timeline)
	+ Different Request limit & Volume limit
	+ Additional pagination method
		- Different max\_results (count) per response
	+ Response data format
	+ Request parameters  
		- Customized data format based on request parameters, including v2 fields and expansions
		- Additional available data: metrics, Tweet annotations, polls

### Similarities

#### Authentication

The v1.1 statuses/user\_timeline and the Twitter API v2 user Tweet timeline endpoint support both OAuth 1.0a User Context and OAuth 2.0 App-Only. Therefore, you can continue using the same authentication method and authorization tokens if you migrate to the Twitter API v2 version.   

#### Historical Access

The v1.1 statuses/user\_timeline and the Twitter API v2 user Tweet timeline endpoint both will return the most recent 3200 Tweets, including Retweets

The v1.1 statuses/mentions\_timeline and the Twitter API v2 user mention timeline endpoint can return the most recent 800 Tweets.  

**Support for Tweet edit history and metadata**  

Both versions provide metadata that describes any edit history. Check out the filtered stream API References and the Edit Tweets fundamentals page for more details. 

#### Rate Limits

|  |  |
| --- | --- |
| **Standard v1.1** | **Twitter API v2** |
| user\_timeline:900 requests per 15 min with OAuth 1.0a User Context
1500 requests per 15 min with OAuth 2.0 App-Only | User Tweets timeline:900 requests per 15-minute window with OAuth 1.0a User Context
1500 requests per 15-minute window with OAuth 2.0 App-Only |

#### Refresh polling using since\_id

Both versions allow polling for recent results using the since\_id.  

#### Traversing timelines by Tweet IDs

Both endpoints have the capability to traverse through timelines using Tweet ID 'timestamps' based on the way Twitter IDs are constructed.  The functionality is generally  the same except for the following:

|  |  |
| --- | --- |
| **Standard timelines v1.1** | **timelines v2** |
| since\_id (exclusive)
max\_id (inclusive) | since\_id (exclusive)
until\_id (also exclusive, vs max\_id which was inclusive) |

#### Response filtering parameters

|  |  |
| --- | --- |
| **Standard timelines v1.1** | **timelines v2** |
| Response filtering parameters:* include\_rts
* exclude\_replies
  | Response filtering parameters:* exclude=retweets,replies
 |
| Example 
https://api.twitter.com/1.1/statuses/user\_timeline.json?user\_id=2244994945&include\_rts=0&&exclude\_replies=1 | Example:
https://api.twitter.com/2/users/2244994945/tweets?max\_results=100&exclude=retweets,replies |
| Notes:
For user\_timeline:* Using include\_rts=0 does not change the possible historical Tweet limit of the most recent 3200
 | Notes:
For user Tweets timeline:* Using exclude=retweets does not change the possible historical Tweet limit of the most recent  3200
* Using exclude=replies reduces the possible historical Tweet limit to the most recent 800 replies
 |

### Differences

#### **Authentication**

#### The v1.1 statuses/mentions\_timeline endpoint only supports  OAuth 1.0a User Context.  The Twitter API v2 user mention timeline endpoint supports both OAuth 1.0a User Context, OAuth 2.0 App-Only, and OAuth 2.0 Authorization Code with PKCE

If you would like to take advantage of the ability to access private or promoted metrics using the Twitter API v2 user Tweet timeline endpoint, you will need to use OAuth 1.0a User Context or OAuth 2.0 Authorization Code with PKCE, and pass the user access tokens related to the user who posted the Tweet for which you would like to access metrics.  

#### Endpoint URLs

Note that the Twitter API v2 timelines endpoints require a path parameter of :id for the user ID.

* Standard v1.1 endpoints:
	+ https://api.twitter.com/1.1/statuses/home\_timeline
	+ https://api.twitter.com/1.1/statuses/user\_timeline
	+ https://api.twitter.com/1.1/statuses/mention\_timeline
* Twitter API v2 endpoint:
	+ https://api.twitter.com/2/users/:id/timelines/reverse\_chronological
	+ https://api.twitter.com/2/users/:id/tweets
	+ https://api.twitter.com/2/users/:id/mentions

#### 
App and Project requirements

The Twitter API v2 endpoints require that you use credentials from a developer App that is associated to a Project when authenticating your requests. All Twitter API v1.1 endpoints can use credentials from standalone Apps or Apps associated with a project.   

#### Rate Limits

|  |  |
| --- | --- |
| **mentions\_timeline:**
75 requests per 15 min with OAuth 1.0a User Context
 | **user mention timeline:**
180 requests per 15-minute window with OAuth 1.0a User Context
450 requests per 15-minute window with OAuth 2.0 Bearer Token |
| **home\_timelime:**
15 requests per 15 minutes
Up to 800 Tweets are obtainable on the home timeline | **reverse chronological home timeline:**
180 requests per 15 minutes
You can return every Tweet created on a timeline over the last 7 days as well as the most recent 800 regardless of creation date. |

#### Request limits

|  |  |
| --- | --- |
| **Standard timelines v1.1** | **timelines v2** |
| Daily request limit* 100,000 request cap within a 24 hour period.
 | No daily request limits, only limited by consumption volume. |

#### Consumption volume limits

|  |  |
| --- | --- |
| **Standard timelines v1.1** | **timelines v2** |
| Consumption limited only by request limits* 100,000 request cap within a 24 hour period.
 | Consumption limited by only Project-level monthly Tweet cap (across multiple v2 endpoints) based on access level.* 500,000 Tweets per month with Essential access.
* 2 million Tweets per month with Elevated access
* 10 million Tweets per month with Academic Research access
Reverse chronological home timeline is not subject to the monthly Tweet cap. |

#### Request parameters

|  |  |
| --- | --- |
| **Standard timelines v1.1** | **timelines v2** |
| Required: user\_id or screen\_name | Required: The specific user ID is specified in the path parameter |
| Optional:
count - sets the maximum results returned per request
exclude\_replies - removes replies from the results
Include\_rts - when set to 0 removes retweets from the results
trim\_user - removes rehydrated user objects from the results
tweet\_mode - sets the data format returned for the results, set to extended for Tweets longer than 140
since\_id - sets the earliest Tweet ID in result (exclusive)
max\_id - sets the latest Tweet ID in result (inclusive) | Optional:
max\_results - sets the maximum results returned per request
exclude=retweets,replies - removes Retweets or replies from the results
tweet.fields - sets the Tweet object fields to return
user.fields - sets the User object fields to return
place.fields - sets the place object fields to return
media.fields - sets the media object fields to return
poll.fields - sets the poll object fields to return
expansions - sets the expanded fields and data to return
start\_time - sets the earliest created\_at time for the results
end\_time - sets the latest created\_at time for the results
since\_id - sets the earliest Tweet ID for the  results (exclusive)
until\_id - sets the latest Tweet ID in result (exclusive) |

**Response data format**

|  |  |
| --- | --- |
| **Standard search v1.1** | **Search Tweets v2** |
| 
```
  [
    {tweet object},
    {tweet object}
  ]
```
 | 
```
{
  "data": [{id,text},{id,text}],
  "meta": {
    "oldest_id": "1337085692623646724",
    "newest_id": "1334183616172019713",
    "previous_token": "77qpymm88g5h9vqkluldpw91lr0qzfz1sqydh841iz48k",
    "result_count": 10,
    "next_token": "7140dibdnow9c7btw3w29gqolns6a1ipl3kzeae41vsxk"
  }
}
```
 |

#### Twitter API v2 JSON format

Twitter API v2 is introducing new JSON designs for the objects returned by the APIs, including Tweet and user objects. You can learn more about the Twitter API v2 format, how to use fields and expansions by visiting our guide, and by reading through our broader data dictionary

* At the JSON root level, the standard endpoints return Tweet objects in a statuses array, while Twitter API v2 returns a data array.
* Instead of referring to Retweeted and Quoted "statuses", Twitter API v2 JSON refers to Retweeted and Quoted Tweets. Many legacy and deprecated fields, such as contributors and user.translator\_type are being removed.
* Instead of using both favorites (in Tweet object) and favorites (in user object), Twitter API v2 uses the term like.
* Twitter is adopting the convention that JSON values with no value (for example, null) are not written to the payload. Tweet and user attributes are only included if they have a non-null value.

One of the biggest differences between standard v1.1 and Twitter API v2 endpoint versions is how you select which fields return in your payload. For the standard endpoints, there are several parameters that you could use to identify which fields or sets of fields would return in the payload, while the Twitter API v2 version simplifies these different parameters into fields and expansions. 

* fields: Twitter API v2 endpoints enable you to select which fields are provided in your payload. For example, Tweet, user, Media, Place, and Poll objects all have a list of fields that can be returned (or not).
* expansions: Used to expand the complementary objects referenced in Tweet JSON payloads. For example, all Retweets and Replies reference other Tweets. By setting expansions=referenced\_tweets.id, these other Tweet objects are expanded according to the tweet.fields setting.  Other objects such as users, polls, and media can be expanded.

* conversation\_id
* Two new annotations fields, including context and entities
* Several new metrics fields

We have put together a data format migration guide which can help you map standard v1.1 fields to the newer v2 fields. This guide will also provide you the specific expansion and field parameter that you will need to pass with your v2 request to return specific fields.   

Next steps
----------

Check out our quick start guide for Twitter API v2 Tweet lookup

Review the API references for v2 Tweet lookup

Check out our sample code for the timelines endpoints

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