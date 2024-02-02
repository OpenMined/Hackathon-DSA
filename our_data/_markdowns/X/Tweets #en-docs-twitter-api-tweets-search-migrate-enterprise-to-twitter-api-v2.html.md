
Search Tweets enterprise to v2 migration guide | Docs | Twitter Developer Platform 

Enterprise compared to Twitter API v2

Enterprise compared to Twitter API v2
-------------------------------------

**Similarities**

* Pagination
* Timezone
* Support for Tweet edit history and metadata.

**Differences**

* Endpoint URLs
* App and Project requirement
* Available time periods
* Response data format
* HTTP methods
* Request time formats
* Request parameters
* Filtering operators

### Similarities

#### Pagination

While v2 has additional pagination features (new pagination parameters that allow you to navigate using Tweet IDs with `since_id` and `until_id`), both enterprise and v2 allow you to paginate using time (`fromDate` and `toDate` with enterprise, and `start_time` and `end_time` for v2).  

#### Timezone

As noted in the pagination section, you can navigate different pages of data using time for both enterprise and v2. In both cases, you will be using UTC as the timezone when using these parameters.

**Support for Tweet edit history and metadata**

Both versions provide metadata that describes any edit history. Check out the search API References and the Tweet edits fundamentals page for more details. 

### Differences

#### Endpoint URLs

* Enterprise endpoints:
	+ 30 day - `http://gnip-api.twitter.com/search/30day/accounts/:account_name/:label.json`
	+ Full-archive - `http://gnip-api.twitter.com/search/fullarchive/accounts/:account_name/:label.json`
* Twitter API v2 endpoints
	+ Recent (7 day) - `https://api.twitter.com/2/tweets/search/recent`
	+ Full-archive - `https://api.twitter.com/2/tweets/search/all`

#### App and Project requirement

The Twitter API v2 endpoints require that you use credentials from a Project when authenticating your requests. All Twitter API v1.1 endpoints can use credentials from standalone Apps or Apps associated with a Project.  

#### Available time periods

Both the enterprise API and Twitter API v2 offer endpoints that allow you to retrieve filtered Tweet data for the full-archive of Tweets.

However, the Twitter API v2 does not offer a 30 day time period endpoint like the enterprise API does. Instead it offers the aforementioned full-archive, or a 7 day time period, which align with the Native Enriched to v2 and Activity Streams to v2 which can help you map enterprise fields to the newer v2 fields. This guide will also provide you the specific expansion and field parameter that you will need to pass with your v2 request to return specific fields.  

#### Response data format

One of the biggest differences between the enterprise response format and Twitter API v2’s format is how you select which fields return in your payload.  

For the enterprise Search API, you receive many of the response fields by default, and then have the option to use parameters to identify which fields or sets of fields should return in the payload.

The Twitter API v2 version only delivers the Tweet `id` and `text` fields by default. To request any additional fields or objects, you will need to use the fields and expansions parameters. Any Tweet fields that you request from these endpoints will return in the primary Tweet object. Any expanded user, media, poll, or place objects and fields will return in an `includes` object within your response. You can then match any expanded objects back to the Tweet object by matching the IDs located in both the Tweet and the expanded object.

We encourage you to read more about these new parameters in their respective guides, or by reading our guide on how to use fields and expansions.

In addition to the changes in how you request certain fields, Twitter API v2 is also introducing new JSON designs for the objects returned by the APIs, including Tweet and user objects.

* At the JSON root level, the standard endpoints return Tweet objects in a `statuses` array, while Twitter API v2 returns a `data` array.
* Instead of referring to Retweeted and Quoted "statuses", Twitter API v2 JSON refers to Retweeted and Quoted Tweets. Many legacy and deprecated fields, such as `contributors` and `user.translator_type` are being removed.
* Instead of using both `favorites` (in Tweet object) and `favourites` (in user object), Twitter API v2 uses the term like.
* Twitter is adopting the convention that JSON values with no value (for example, `null`) are not written to the payload. Tweet and user attributes are only included if they have non-null values.

We also introduced a new set of fields to the Tweet object including the following:

* A conversation\_id field
* Two new annotations fields, including context and entities
* Several new metrics fields
* A new `reply_setting` field, which shows you who can reply to a given Tweet

And one last note. The premium response includes a `requestParameters` object at the root level, which contains the parameters that you included in your request. The v2 version instead contains a `meta` object that lives at the root level which includes the `newest_id`, `oldest_id`, `result_count`, and `next_token` if there is an additional page of results.  

#### HTTP methods

The enterprise version of the API allows you to pass the request as either a POST HTTP method with a JSON body, or a GET HTTP method with a query string.

V2 only allows you to use the GET HTTP method with a query string.  

#### Request time formats

The enterprise version of this endpoint uses the following date/time format in both the pagination parameters and the `timePeriod` response field: `YYYYMMDDHHmm`

The v2 endpoint uses ISO 8601/RFC 3339 date/time format in both the pagination parameters and the `start` and `end` response fields: `YYYY-MM-DDTHH:mm:ssZ`

#### Request parameters

The following is a table of the request parameters for enterprise and Twitter API v2:

| Enterprise | Search Tweets v2 |
| --- | --- |
| query | query |
| maxResults | max\_results |
| fromDate (YYMMDDHHmm) | start\_time (YYYY-MM-DDTHH:mm:ssZ) |
| toDate (YYMMDDHHmm) | end\_time (YYYY-MM-DDTHH:mm:ssZ) |
|  | since\_id |
|  | until\_id |
| next | next\_token or pagination\_token |

#### Filtering operators

While the operators between enterprise and Twitter API v2 are mostly the same, there are some differences in operator availability and some new operators that were introduced to just the Twitter API v2 version.

To see a full table of the operators that are available for Twitter API v2, enterprise, and even premium and standard, please visit the Search Tweets migration landing page.

Next steps
----------

Check out our quick start guide for Twitter API v2 full-archive search

Review the API reference for full-archive search

Check out some sample code for these endpoints

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