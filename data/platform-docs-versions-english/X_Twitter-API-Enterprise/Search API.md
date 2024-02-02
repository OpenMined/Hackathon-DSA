Overview

**Please note:**

We have released a new version of [search Tweets](https://developer.twitter.com/en/docs/twitter-api/tweets/search) and [Tweet counts](https://developer.twitter.com/en/docs/twitter-api/tweets/counts) in [Twitter API v2](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api). While we have not announced a deprecation timeline for this API yet, we do encourage you to start to experiment and [review what's new](https://developer.twitter.com/en/docs/twitter-api/migrate) with Twitter API v2. 

These endpoints have been updated to include Tweet edit metadata. Learn more about these metadata on the ["Edit Tweets" fundamentals page](https://developer.twitter.com/en/docs/twitter-api/enterprise/edit-tweets). 

Overview
--------

Enterprise

_The enterprise APIs are available within our managed access levels only. To use these APIs, you must first set up an account with our enterprise sales team. To learn more see [HERE](https://developer.twitter.com/content/developer-twitter/en/enterprise)._  

_You can view all of the Twitter API search Tweet offerings [HERE](https://developer.twitter.com/en/docs/twitter-api/search-overview)._

There are two enterprise search APIs:  

1. 30-Day Search API provides data from the previous 30 days.
2. Full-Archive Search API provides complete and instant access to the full corpus of Twitter data dating all the way back to the first Tweet in March 2006.

These RESTful APIs supports a single query of up to 2,048 characters per request. Queries are written with the PowerTrack rule syntax - see [Rules and filtering](https://developer.twitter.com/en/docs/twitter-api/enterprise/rules-and-filtering/building-a-rule) for more details. Users can specify any time period, to the granularity of a minute. However, responses will be limited to the lesser of your specified maxResults OR 31 days and include a next token to paginate for the next set of results. If time parameters are not specified, the API will return matching data from the 30 most recent days.

The enterprise search APIs provide low-latency, full-fidelity, query-based access to the Tweet archive with minute granularity. Tweet data is served in reverse chronological order, starting with the most recent Tweet that matches your query. Tweets are available from the search API approximately 30 seconds after being published.

These search endpoints provide edited Tweet metadata. All objects for Tweets created since September 29, 2022, include Tweet edit metadata, even if the Tweet was never edited. Each time a Tweet is edited, a new Tweet ID is created. A Tweet's edit history is documented by an array of Tweet IDs, starting with the original ID.

These endpoints will always return the most recent edit, along with any edit history. Any Tweet collected after its 30-minute edit window will represent its final version. To learn more about Edit Tweet metadata, check out the [Edit Tweets fundamentals](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/edit-tweets) page.

Requests include a maxResults parameter that specifies the maximum number of Tweets to return per API response. If more Tweets are associated with the query than this maximum amount of results per response, a next token is included in the response. These next tokens are used in subsequent requests to page through the entire set of Tweets associated with the query.

These enterprise search APIs provide a _counts_ endpoint that enables users to request the data volume associated with their query. 

### Request types

The enterprise search APIs support two types of requests:  

#### Search requests (data)

Search requests to the enterprise search APIs allow you to retrieve up to 500 results per response for a given timeframe, with the ability to paginate for additional data. Using the maxResults parameter, you can specify smaller page sizes for display use cases (allowing your user to request more results as needed) or larger page sizes (up to 500) for larger data pulls. The data is delivered in reverse chronological order and compliant at the time of delivery.

#### Counts requests (Tweet count)

Counts requests provide the ability to retrieve historical activity counts, which reflect the number of activities that occurred which match a given query during the requested timeframe. The response will essentially provide you with a histogram of counts, bucketed by day, hour, or minute (the default bucket is _hour_). It's important to note that counts results do not always reflect compliance events (e.g., Tweets deletes) that happen well after (7+ days) a Tweet is published; therefore, it is expected that the counts metric may not always match that of a data request for the same query.  

**Billing note:** each request – _including pagination requests_ – made against the data and counts endpoints are counted as a billed request. Therefore, if there are multiple pages of results for a single query, paging through the X pages of results would equate to X requests for billing.

### Available operators

Enterprise search APIs support rules with up to 2,048 characters. The enterprise search APIs support the operators listed below. For detailed descriptions see [HERE](https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/guides/search-api/enterprise-operators). 

|     |     |     |     |
| --- | --- | --- | --- |
| **Matching on Tweet contents:** | **Matching on accounts of interest:** | **Tweet attributes:** | **Geospatial operators:** |
| * keyword<br>* “quoted phrase”<br>* “keyword1 keyword2”~N<br>* #<br>* @<br>* $<br>* url:<br>* lang: | * from:<br>* to:<br>* retweets\_of: | * is:retweet  <br>    <br>* has:mentions<br>* has:hashtags<br>* has:media<br>* has:videos<br>* has:images<br>* has:links<br>* has:symbols<br>* is:verified  <br>    <br>* \-is:nullcast (negation only operator) | * bounding\_box:\[west\_long south\_lat east\_long north\_lat\]<br>* point\_radius:\[lon lat radius\]<br>* has:geo<br>* place:<br>* place\_country:<br>* has:profile\_geo<br>* profile\_country:<br>* profile\_region:<br>* profile\_locality: |

  
Notes: Do not embed/nest operators ("#cats") will resolve to cats with the search APIs.   The ‘lang:’ operator and all ‘is:’ and ‘has:’ operators cannot be used as standalone operators and must be combined with another clause (e.g. @twitterdev has:links).    

Search APIs use a limited set of operators due to tokenization/matching functionality. enterprise real-time and batched historical APIs provide additional operators. See [HERE](https://developer.twitter.com/en/docs/twitter-api/enterprise/rules-and-filtering/operators-by-product) for more details.  

For more details, please see the [Getting started with operators](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/rules-and-filtering/building-a-rule) guide.

### Data availability / important date

When using the Full-Archive search API, keep in mind that the Twitter platform has continued to evolve since 2006. As new features were added, the underlying JSON objects have had new metadata added to it. For that reason it is important to understand when Tweet attributes were added that search operators match on. Below are some of the more fundamental 'born on' dates of important groups of metadata. To learn more about when Tweet attributes were first introduced, see [this guide](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/search-api/guides/changelog).  

* First Tweet: 3/21/2006
* First Native Retweets: 11/6/2009
* First Geo-tagged Tweets: 11/19/2009
* URLs first indexed for filtering: 8/27/2011
* Enhanced URL expansion metadata (website titles and descriptions): 12/1/2014
* Profile Geo enrichment metadata and filtering: 2/17/2015

### Data Updates and Mutability

With the enterprise search APIs, some of the data within a Tweet is mutable, i.e. can be updated or changed after initial archival.

This mutable data falls into two categories:

* User object metadata:
    * User’s @handle (numeric ID does not ever change)
    * Bio description
    * Counts: statuses, followers, friends, favorites, lists
    * Profile location
    * Other details such as time zone and language
* Tweet statistics - i.e. anything that can be changed on the platform by user actions (examples below):
    * Favorites count
    * Retweet count

In most of these cases, the search APIs will return data as it exists on the platform at _query-time_, rather than Tweet generation time. However, in the case of queries using select operators (e.g. from, to, @, is:verified), this may not be the case. Data is updated in our index on a regular basis, with an increased frequency for most recent timeframes. As a result, in some cases, the data returned may not exactly match the current data as displayed on Twitter.com, but matches data at the time it was last indexed.

Note, this issue of inconsistency only applies to queries where the operator applies to mutable data. One example is filtering for usernames, and the best workaround would be to use user numeric IDs rather than @handles for these queries.

### Single vs. Multi-threaded Requests

Each customer has a defined rate limit for their search endpoint. The default per-minute rate limit for Full-Archive search is 120 requests per minute, for an average of 2 queries per second (QPS). This average QPS means that, in theory, 2 requests can be made of the API every second. Given the pagination feature of the product, if a one-year query has one million Tweets associated with it, spread evenly over the year, over 2,000 requests would be required (assuming a ‘maxResults’ of 500) to receive all the data. Assuming it takes two seconds per response, that is 4,000 seconds (or just over an hour) to pull all of that data serially/sequentially through a single thread (1 request per second using the prior response’s “next” token). Not bad!

Now consider the situation where twelve parallel threads are used to receive data. Assuming an even distribution of the one million Tweets over the one-year period, you could split the requests into twelve parallel threads (multi-threaded) and utilize more of the per-second rate limit for the single “job”. In other words, you could run one thread per-month you are interested in and by doing so, data could be retrieved 12x as fast (or ~6 minutes).

This multi-threaded example applies equally well to the counts endpoint. For example, if you wanted to receive Tweet counts for a two-year period, you could make a single-threaded request and page back through the counts 31 days at a time. Assuming it takes 2 seconds per response, it would take approximately 48 seconds to make the 24 API requests and retrieve the entire set of counts. However, you also have the option to make multiple one-month requests at a time. When making 12 requests per second, the entire set of counts could be retrieved in approximately 2 seconds.

### Retry Logic

If you experience a 503 error with the enterprise search APIs, it is likely a transient error and can be resolved by re-trying the request a short time later.

If the request fails 4 times in a row, and you have waited at least 10 minutes between failures, use the following steps to troubleshoot:

* Retry the request after reducing the amount of time it covers. Repeat this down to a 6-hour time window if unsuccessful.
* If you are ORing a large number of terms together, split them into separate rules and retry each individually.
* If you are using a large number of exclusions in your rule, reduce the number of negated terms in the rule and retry.

### Next steps

* [Continue to the enterprise search API reference](https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/api-reference/enterprise-search)
* [Learn more about search operators](https://developer.twitter.com/en/docs/twitter-api/enterprise/guides/enterprise-operators)  
    
* [See simple scripts in several languages to help get started](https://github.com/gnip/support/blob/master/Search%20API/readme.md)
* [See an example Python client library](https://github.com/twitterdev/search-tweets-python)
* [See an example Ruby client library](https://github.com/twitterdev/search-tweets-ruby)

Enterprise Search Tweets: 30-Day API

Getting started with enterprise Search Tweets: 30-Day API
---------------------------------------------------------

**⏱ 10 min read**

The enterprise Search Tweets: 30-Day API provides you with Tweets posted within the last 30 days. Tweets are matched and sent back to you based on the query you specify in your request. A query is a rule in which you define what the Tweet you get back should contain. In this tutorial, we will search for Tweets originating from the Twitter account @TwitterDev in English.

The Tweets you get back in your payload can be in a data format, which provides you with the full Tweet payload, or it can be in a counts format which gives you numerical count data of matched Tweets. We will be using cURL to make requests to the data and counts endpoints.

You will need the following:

* [An enterprise account](https://developer.twitter.com/en/enterprise)
* Your username, password, and account name
* Label associated with your search endpoint, as displayed at console.gnip.com

### Accessing the data endpoint

  
The data endpoint will provide us with the full Tweet payload of matched Tweets. We will use the `from:` and `lang:` operators to find Tweets originating from @TwitterDev in English. _For more operators [click here](https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/guides/enterprise-operators)._

* [cURL](#tab1)
* [cURL example](#tab2)
* [](#tab4)

cURL

cURL example

_cURL is a command-line tool for getting or sending files using the URL syntax._

Copy the following cURL request into your command line after making changes to the following:

* **Username** `<USERNAME>` e.g. `email@domain.com`  
    
* **Account name** `<ACCOUNT-NAME>` e.g. `john-doe`  
    
* **Label** `<LABEL>` e.g. `prod`  
    
* **fromDate and toDate** e.g. `"fromDate":"201811010000", "toDate":"201811122359"`

_After sending your request, you will be prompted for your password._

      `curl -X POST -u<USERNAME> "https://gnip-api.twitter.com/search/30day/accounts/<ACCOUNT-NAME>/<LABEL>.json" -d '{"query":"from:TwitterDev lang:en","maxResults":"500","fromDate":"<yyyymmddhhmm>","toDate":"<yyyymmddhhmm>"}'`
    

_This is an example cURL request. If you try to run this it will not work._ 

      `curl -X POST -uemail@domain.com "https://gnip-api.twitter.com/search/30day/accounts/john-doe/prod.json" -d '{"query":"from:TwitterDev lang:en","maxResults":"500","fromDate":"201811100000","toDate":"201812012359"}'`
    

#### Data endpoint response payload

The payload you get back from your API request will appear in JSON format, as shown below.

      `{ 	"results": [ 		{ 			"created_at": "Fri Nov 02 17:18:31 +0000 2018", 			"id": 1058408022936977409, 			"id_str": "1058408022936977409", 			"text": "RT @harmophone: \"The innovative crowdsourcing that the Tagboard, Twitter and TEGNA collaboration enables is surfacing locally relevant conv…", 			"source": "<a href=\"http:\/\/twitter.com\" rel=\"nofollow\">Twitter Web Client<\/a>", 			"truncated": false, 			"in_reply_to_status_id": null, 			"in_reply_to_status_id_str": null, 			"in_reply_to_user_id": null, 			"in_reply_to_user_id_str": null, 			"in_reply_to_screen_name": null, 			"user": { 				"id": 2244994945, 				"id_str": "2244994945", 				"name": "Twitter Dev", 				"screen_name": "TwitterDev", 				"location": "Internet", 				"url": "https:\/\/developer.twitter.com\/", 				"description": "Your official source for Twitter Platform news, updates & events. Need technical help? Visit https:\/\/twittercommunity.com\/ ⌨️ #TapIntoTwitter", 				"translator_type": "null", 				"protected": false, 				"verified": true, 				"followers_count": 503828, 				"friends_count": 1477, 				"listed_count": 1437, 				"favourites_count": 2199, 				"statuses_count": 3380, 				"created_at": "Sat Dec 14 04:35:55 +0000 2013", 				"utc_offset": null, 				"time_zone": null, 				"geo_enabled": true, 				"lang": "en", 				"contributors_enabled": false, 				"is_translator": false, 				"profile_background_color": "null", 				"profile_background_image_url": "null", 				"profile_background_image_url_https": "null", 				"profile_background_tile": null, 				"profile_link_color": "null", 				"profile_sidebar_border_color": "null", 				"profile_sidebar_fill_color": "null", 				"profile_text_color": "null", 				"profile_use_background_image": null, 				"profile_image_url": "null", 				"profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/880136122604507136\/xHrnqf1T_normal.jpg", 				"profile_banner_url": "https:\/\/pbs.twimg.com\/profile_banners\/2244994945\/1498675817", 				"default_profile": false, 				"default_profile_image": false, 				"following": null, 				"follow_request_sent": null, 				"notifications": null 			}, 			"geo": null, 			"coordinates": null, 			"place": null, 			"contributors": null, 			"retweeted_status": { 				"created_at": "Tue Oct 30 21:30:25 +0000 2018", 				"id": 1057384253116289025, 				"id_str": "1057384253116289025", 				"text": "\"The innovative crowdsourcing that the Tagboard, Twitter and TEGNA collaboration enables is surfacing locally relev… https:\/\/t.co\/w46U5TRTzQ", 				"source": "<a href=\"http:\/\/twitter.com\" rel=\"nofollow\">Twitter Web Client<\/a>", 				"truncated": true, 				"in_reply_to_status_id": null, 				"in_reply_to_status_id_str": null, 				"in_reply_to_user_id": null, 				"in_reply_to_user_id_str": null, 				"in_reply_to_screen_name": null, 				"user": { 					"id": 175187944, 					"id_str": "175187944", 					"name": "Tyler Singletary", 					"screen_name": "harmophone", 					"location": "San Francisco, CA", 					"url": "http:\/\/medium.com\/@harmophone", 					"description": "SVP Product at @Tagboard. Did some Data, biz, and product @Klout & for @LithiumTech; @BBI board member; @Insightpool advisor. World's worst whiteboarder.", 					"translator_type": "null", 					"protected": false, 					"verified": false, 					"followers_count": 1982, 					"friends_count": 1877, 					"listed_count": 245, 					"favourites_count": 23743, 					"statuses_count": 12708, 					"created_at": "Thu Aug 05 22:59:29 +0000 2010", 					"utc_offset": null, 					"time_zone": null, 					"geo_enabled": false, 					"lang": "en", 					"contributors_enabled": false, 					"is_translator": false, 					"profile_background_color": "null", 					"profile_background_image_url": "null", 					"profile_background_image_url_https": "null", 					"profile_background_tile": null, 					"profile_link_color": "null", 					"profile_sidebar_border_color": "null", 					"profile_sidebar_fill_color": "null", 					"profile_text_color": "null", 					"profile_use_background_image": null, 					"profile_image_url": "null", 					"profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/719985428632240128\/WYFHcK-m_normal.jpg", 					"profile_banner_url": "https:\/\/pbs.twimg.com\/profile_banners\/175187944\/1398653841", 					"default_profile": false, 					"default_profile_image": false, 					"following": null, 					"follow_request_sent": null, 					"notifications": null 				}, 				"geo": null, 				"coordinates": null, 				"place": null, 				"contributors": null, 				"is_quote_status": false, 				"extended_tweet": { 					"full_text": "\"The innovative crowdsourcing that the Tagboard, Twitter and TEGNA collaboration enables is surfacing locally relevant conversations in real-time and enabling voters to ask questions during debates,”  -- @adamostrow, @TEGNA\nLearn More: https:\/\/t.co\/ivAFtanfje", 					"display_text_range": [ 						0, 						259 					], 					"entities": { 						"hashtags": [], 						"urls": [ 							{ 								"url": "https:\/\/t.co\/ivAFtanfje", 								"expanded_url": "https:\/\/blog.tagboard.com\/twitter-and-tagboard-collaborate-to-bring-best-election-content-to-news-outlets-with-tagboard-e85fc864bcf4", 								"display_url": "blog.tagboard.com\/twitter-and-ta…", 								"unwound": { 									"url": "https:\/\/blog.tagboard.com\/twitter-and-tagboard-collaborate-to-bring-best-election-content-to-news-outlets-with-tagboard-e85fc864bcf4", 									"status": 200, 									"title": "Twitter and Tagboard Collaborate to Bring Best Election Content to News Outlets With Tagboard…", 									"description": "By Tyler Singletary, Head of Product, Tagboard" 								}, 								"indices": [ 									236, 									259 								] 							} 						], 						"user_mentions": [ 							{ 								"screen_name": "adamostrow", 								"name": "Adam Ostrow", 								"id": 5695942, 								"id_str": "5695942", 								"indices": [ 									204, 									215 								] 							}, 							{ 								"screen_name": "TEGNA", 								"name": "TEGNA", 								"id": 34123003, 								"id_str": "34123003", 								"indices": [ 									217, 									223 								] 							} 						], 						"symbols": [] 					} 				}, 				"quote_count": 0, 				"reply_count": 1, 				"retweet_count": 6, 				"favorite_count": 19, 				"entities": { 					"hashtags": [], 					"urls": [ 						{ 							"url": "https:\/\/t.co\/w46U5TRTzQ", 							"expanded_url": "https:\/\/twitter.com\/i\/web\/status\/1057384253116289025", 							"display_url": "twitter.com\/i\/web\/status\/1…", 							"indices": [ 								117, 								140 							] 						} 					], 					"user_mentions": [], 					"symbols": [] 				}, 				"favorited": false, 				"retweeted": false, 				"possibly_sensitive": false, 				"filter_level": "low", 				"lang": "en" 			}, 			"is_quote_status": false, 			"quote_count": 0, 			"reply_count": 0, 			"retweet_count": 0, 			"favorite_count": 0, 			"entities": { 				"hashtags": [], 				"urls": [], 				"user_mentions": [ 					{ 						"screen_name": "harmophone", 						"name": "Tyler Singletary", 						"id": 175187944, 						"id_str": "175187944", 						"indices": [ 							3, 							14 						] 					} 				], 				"symbols": [] 			}, 			"favorited": false, 			"retweeted": false, 			"filter_level": "low", 			"lang": "en", 			"matching_rules": [ 				{ 					"tag": null 				} 			] 		} 	], 	"requestParameters": { 		"maxResults": 100, 		"fromDate": "201811010000", 		"toDate": "201811060000" 	} }`
    

### Accessing the counts endpoint

With the counts endpoint, we’ll retrieve the number of Tweets originating from the @TwitterDev account in English grouped by `day`.

* [cURL](#tab1)
* [cURL example](#tab2)
* [](#tab4)

cURL

cURL example

_cURL is a command-line tool for getting or sending files using the URL syntax._

Copy the following cURL request into your command line after making changes to the following:

* **Username** `<USERNAME>` e.g. `email@domain.com`  
    
* **Account name** `<ACCOUNT-NAME>` e.g. `john-doe`  
    
* **Label** `<LABEL>` e.g. `prod`  
    
* **fromDate and toDate** e.g. `"fromDate":"201811010000", "toDate":"201811122359"`

_After sending your request, you will be prompted for your password._

      `curl -X POST -u<USERNAME> "https://gnip-api.twitter.com/search/30day/accounts/<ACCOUNT-NAME>/<LABEL>/counts.json" -d '{"query":"from:TwitterDev lang:en","fromDate":"<yyyymmddhhmm>","toDate":"<yyyymmddhhmm>","bucket":"day"}'`
    

_This is an example cURL request. If you try to run this it will not work._ 

      `curl -X POST -uemail@domain.com "https://gnip-api.twitter.com/search/30day/accounts/john-doe/prod/counts.json" -d '{"query":"from:TwitterDev lang:en","fromDate":"201811100000","toDate":"201812012359","bucket":"day"}'`
    

#### Counts endpoint response payload

The payload you get back from your API request will appear in JSON format, as shown below.

      `{ 	"results": [ 		{ 			"timePeriod": "201811010000", 			"count": 0 		}, 		{ 			"timePeriod": "201811020000", 			"count": 1 		}, 		{ 			"timePeriod": "201811030000", 			"count": 0 		}, 		{ 			"timePeriod": "201811040000", 			"count": 0 		}, 		{ 			"timePeriod": "201811050000", 			"count": 0 		} 	], 	"totalCount": 1, 	"requestParameters": { 		"bucket": "day", 		"fromDate": "201811010000", 		"toDate": "201811060000" 	} }`
    

Great job! Now you've successfully accessed the enterprise Search Tweets: 30-Day API.  

### Referenced articles

* [Introduction to Tweet objects](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/data-dictionary/overview)
* [Premium search operators](https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/guides/enterprise-operators)
* [Tweet objects and payloads](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects) 

Next Steps
----------

* [Discover more about the counts endpoint](https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/api-reference/enterprise-search)  
    
* [Join the conversation on Twitter community forums](https://twittercommunity.com/)

Enterprise Search Tweets: Full-Archive API

Getting started with enterprise Search Tweets: Full-Archive API
---------------------------------------------------------------

**⏱ 10 min read**

The enterprise Search Tweets: Full-Archive API provides you with Tweets since the first one posted in 2006. Tweets are matched and sent back to you based on the query you specify in your request. A query is a rule in which you define what the Tweet you get back should contain. In this tutorial, we will search for Tweets originating from the Twitter account @TwitterDev in English.

The Tweets you get back in your payload can be in a data format, which provides you with the full Tweet payload, or it can be in a counts format which gives you numerical count data of matched Tweets. We will be using cURL to make requests to the data and counts endpoints.

You will need the following:

* [An enterprise account](https://developer.twitter.com/en/enterprise)
* Your username, password, and account name
* Label associated with your search endpoint, as displayed at console.gnip.com

### Accessing the data endpoint

  
The data endpoint will provide us with the full Tweet payload of matched Tweets. We will use the `from:` and `lang:` operators to find Tweets originating from @TwitterDev in English. _For more operators [click here](https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/guides/enterprise-operators)._

* [cURL](#tab1)
* [cURL example](#tab2)
* [](#tab4)

cURL

cURL example

_cURL is a command-line tool for getting or sending files using the URL syntax._

Copy the following cURL request into your command line after making changes to the following:

* **Username** `<USERNAME>` e.g. `email@domain.com`  
    
* **Account name** `<ACCOUNT-NAME>` e.g. `john-doe`  
    
* **Label** `<LABEL>` e.g. `prod`  
    
* **fromDate and toDate** e.g. `"fromDate":"201802010000", "toDate":"201802282359"`

_After sending your request, you will be prompted for your password._

      `curl -X POST -u<USERNAME> "https://gnip-api.twitter.com/search/fullarchive/accounts/<ACCOUNT-NAME>/<LABEL>.json" -d '{"query":"from:TwitterDev lang:en","maxResults":"500","fromDate":"<yyyymmddhhmm>","toDate":"<yyyymmddhhmm>"}'`
    

_This is an example cURL request. If you try to run this it will not work._ 

      `curl -X POST -uemail@domain.com "https://gnip-api.twitter.com/search/fullarchive/accounts/john-doe/prod.json" -d '{"query":"from:TwitterDev lang:en","maxResults":"500","fromDate":"201802010000","toDate":"201802282359"}'`
    

#### Data endpoint response payload

The payload you get back from your API request will appear in JSON format, as shown below.

      `{ 	"results": [ 		{ 			"created_at": "Fri Nov 02 17:18:31 +0000 2018", 			"id": 1058408022936977409, 			"id_str": "1058408022936977409", 			"text": "RT @harmophone: \"The innovative crowdsourcing that the Tagboard, Twitter and TEGNA collaboration enables is surfacing locally relevant conv…", 			"source": "<a href=\"http:\/\/twitter.com\" rel=\"nofollow\">Twitter Web Client<\/a>", 			"truncated": false, 			"in_reply_to_status_id": null, 			"in_reply_to_status_id_str": null, 			"in_reply_to_user_id": null, 			"in_reply_to_user_id_str": null, 			"in_reply_to_screen_name": null, 			"user": { 				"id": 2244994945, 				"id_str": "2244994945", 				"name": "Twitter Dev", 				"screen_name": "TwitterDev", 				"location": "Internet", 				"url": "https:\/\/developer.twitter.com\/", 				"description": "Your official source for Twitter Platform news, updates & events. Need technical help? Visit https:\/\/twittercommunity.com\/ ⌨️ #TapIntoTwitter", 				"translator_type": "null", 				"protected": false, 				"verified": true, 				"followers_count": 503828, 				"friends_count": 1477, 				"listed_count": 1437, 				"favourites_count": 2199, 				"statuses_count": 3380, 				"created_at": "Sat Dec 14 04:35:55 +0000 2013", 				"utc_offset": null, 				"time_zone": null, 				"geo_enabled": true, 				"lang": "en", 				"contributors_enabled": false, 				"is_translator": false, 				"profile_background_color": "null", 				"profile_background_image_url": "null", 				"profile_background_image_url_https": "null", 				"profile_background_tile": null, 				"profile_link_color": "null", 				"profile_sidebar_border_color": "null", 				"profile_sidebar_fill_color": "null", 				"profile_text_color": "null", 				"profile_use_background_image": null, 				"profile_image_url": "null", 				"profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/880136122604507136\/xHrnqf1T_normal.jpg", 				"profile_banner_url": "https:\/\/pbs.twimg.com\/profile_banners\/2244994945\/1498675817", 				"default_profile": false, 				"default_profile_image": false, 				"following": null, 				"follow_request_sent": null, 				"notifications": null 			}, 			"geo": null, 			"coordinates": null, 			"place": null, 			"contributors": null, 			"retweeted_status": { 				"created_at": "Tue Oct 30 21:30:25 +0000 2018", 				"id": 1057384253116289025, 				"id_str": "1057384253116289025", 				"text": "\"The innovative crowdsourcing that the Tagboard, Twitter and TEGNA collaboration enables is surfacing locally relev… https:\/\/t.co\/w46U5TRTzQ", 				"source": "<a href=\"http:\/\/twitter.com\" rel=\"nofollow\">Twitter Web Client<\/a>", 				"truncated": true, 				"in_reply_to_status_id": null, 				"in_reply_to_status_id_str": null, 				"in_reply_to_user_id": null, 				"in_reply_to_user_id_str": null, 				"in_reply_to_screen_name": null, 				"user": { 					"id": 175187944, 					"id_str": "175187944", 					"name": "Tyler Singletary", 					"screen_name": "harmophone", 					"location": "San Francisco, CA", 					"url": "http:\/\/medium.com\/@harmophone", 					"description": "SVP Product at @Tagboard. Did some Data, biz, and product @Klout & for @LithiumTech; @BBI board member; @Insightpool advisor. World's worst whiteboarder.", 					"translator_type": "null", 					"protected": false, 					"verified": false, 					"followers_count": 1982, 					"friends_count": 1877, 					"listed_count": 245, 					"favourites_count": 23743, 					"statuses_count": 12708, 					"created_at": "Thu Aug 05 22:59:29 +0000 2010", 					"utc_offset": null, 					"time_zone": null, 					"geo_enabled": false, 					"lang": "en", 					"contributors_enabled": false, 					"is_translator": false, 					"profile_background_color": "null", 					"profile_background_image_url": "null", 					"profile_background_image_url_https": "null", 					"profile_background_tile": null, 					"profile_link_color": "null", 					"profile_sidebar_border_color": "null", 					"profile_sidebar_fill_color": "null", 					"profile_text_color": "null", 					"profile_use_background_image": null, 					"profile_image_url": "null", 					"profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/719985428632240128\/WYFHcK-m_normal.jpg", 					"profile_banner_url": "https:\/\/pbs.twimg.com\/profile_banners\/175187944\/1398653841", 					"default_profile": false, 					"default_profile_image": false, 					"following": null, 					"follow_request_sent": null, 					"notifications": null 				}, 				"geo": null, 				"coordinates": null, 				"place": null, 				"contributors": null, 				"is_quote_status": false, 				"extended_tweet": { 					"full_text": "\"The innovative crowdsourcing that the Tagboard, Twitter and TEGNA collaboration enables is surfacing locally relevant conversations in real-time and enabling voters to ask questions during debates,”  -- @adamostrow, @TEGNA\nLearn More: https:\/\/t.co\/ivAFtanfje", 					"display_text_range": [ 						0, 						259 					], 					"entities": { 						"hashtags": [], 						"urls": [ 							{ 								"url": "https:\/\/t.co\/ivAFtanfje", 								"expanded_url": "https:\/\/blog.tagboard.com\/twitter-and-tagboard-collaborate-to-bring-best-election-content-to-news-outlets-with-tagboard-e85fc864bcf4", 								"display_url": "blog.tagboard.com\/twitter-and-ta…", 								"unwound": { 									"url": "https:\/\/blog.tagboard.com\/twitter-and-tagboard-collaborate-to-bring-best-election-content-to-news-outlets-with-tagboard-e85fc864bcf4", 									"status": 200, 									"title": "Twitter and Tagboard Collaborate to Bring Best Election Content to News Outlets With Tagboard…", 									"description": "By Tyler Singletary, Head of Product, Tagboard" 								}, 								"indices": [ 									236, 									259 								] 							} 						], 						"user_mentions": [ 							{ 								"screen_name": "adamostrow", 								"name": "Adam Ostrow", 								"id": 5695942, 								"id_str": "5695942", 								"indices": [ 									204, 									215 								] 							}, 							{ 								"screen_name": "TEGNA", 								"name": "TEGNA", 								"id": 34123003, 								"id_str": "34123003", 								"indices": [ 									217, 									223 								] 							} 						], 						"symbols": [] 					} 				}, 				"quote_count": 0, 				"reply_count": 1, 				"retweet_count": 6, 				"favorite_count": 19, 				"entities": { 					"hashtags": [], 					"urls": [ 						{ 							"url": "https:\/\/t.co\/w46U5TRTzQ", 							"expanded_url": "https:\/\/twitter.com\/i\/web\/status\/1057384253116289025", 							"display_url": "twitter.com\/i\/web\/status\/1…", 							"indices": [ 								117, 								140 							] 						} 					], 					"user_mentions": [], 					"symbols": [] 				}, 				"favorited": false, 				"retweeted": false, 				"possibly_sensitive": false, 				"filter_level": "low", 				"lang": "en" 			}, 			"is_quote_status": false, 			"quote_count": 0, 			"reply_count": 0, 			"retweet_count": 0, 			"favorite_count": 0, 			"entities": { 				"hashtags": [], 				"urls": [], 				"user_mentions": [ 					{ 						"screen_name": "harmophone", 						"name": "Tyler Singletary", 						"id": 175187944, 						"id_str": "175187944", 						"indices": [ 							3, 							14 						] 					} 				], 				"symbols": [] 			}, 			"favorited": false, 			"retweeted": false, 			"filter_level": "low", 			"lang": "en", 			"matching_rules": [ 				{ 					"tag": null 				} 			] 		} 	], 	"requestParameters": { 		"maxResults": 100, 		"fromDate": "201811010000", 		"toDate": "201811060000" 	} }`
    

### Accessing the counts endpoint

With the counts endpoint, we’ll retrieve the number of Tweets originating from the @TwitterDev account in English grouped by `day`.

* [cURL](#tab1)
* [cURL example](#tab2)
* [](#tab4)

cURL

cURL example

_cURL is a command-line tool for getting or sending files using the URL syntax._

Copy the following cURL request into your command line after making changes to the following:

* **Username** `<USERNAME>` e.g. `email@domain.com`  
    
* **Account name** `<ACCOUNT-NAME>` e.g. `john-doe`  
    
* **Label** `<LABEL>` e.g. `prod`  
    
* **fromDate and toDate** e.g. `"fromDate":"201802010000", "toDate":"201802282359"`

_After sending your request, you will be prompted for your password._

      `curl -X POST -u<USERNAME> "https://gnip-api.twitter.com/search/fullarchive/accounts/<ACCOUNT-NAME>/<LABEL>/counts.json" -d '{"query":"from:TwitterDev lang:en","fromDate":"<yyyymmddhhmm>","toDate":"<yyyymmddhhmm>","bucket":"day"}'`
    

_This is an example cURL request. If you try to run this it will not work._ 

      `curl -X POST -uemail@domain.com "https://gnip-api.twitter.com/search/fullarchive/accounts/john-doe/prod/counts.json" -d '{"query":"from:TwitterDev lang:en","fromDate":"201802010000","toDate":"201802282359","bucket":"day"}'`
    

#### Counts endpoint response payload

The payload you get back from your API request will appear in JSON format, as shown below.

      `{ 	"results": [ 		{ 			"timePeriod": "201811010000", 			"count": 0 		}, 		{ 			"timePeriod": "201811020000", 			"count": 1 		}, 		{ 			"timePeriod": "201811030000", 			"count": 0 		}, 		{ 			"timePeriod": "201811040000", 			"count": 0 		}, 		{ 			"timePeriod": "201811050000", 			"count": 0 		} 	], 	"totalCount": 1, 	"requestParameters": { 		"bucket": "day", 		"fromDate": "201811010000", 		"toDate": "201811060000" 	} }`
    

  
Great job! Now you've successfully accessed the enterprise Search Tweets: Full-Archive API.  
 

### Referenced articles

* [Introduction to Tweet objects](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/overview)
* [Premium search operators](https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/guides/premium-operators)
* [Tweet objects and payloads](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects) 

  
Next Steps
-------------

* [Discover more about the counts endpoint](https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/api-reference/enterprise-search#CountsEndpoint)  
    
* [Join the conversation on Twitter community forums](https://twittercommunity.com/)

Building search queries

Premium and enterprise operators  

===================================

Below is a list of all operators supported in Twitter's premium and enterprise search APIs:

* Enterprise 30-day search API
* Enterprise Full-archive search API

For a side-by-side comparison of available operators by product see [HERE](https://developer.twitter.com/en/docs/twitter-api/enterprise/rules-and-filtering/operators-by-product).  
  

 OperatorDescriptionkeyword  

Matches a tokenized keyword within the body or urls of a Tweet. This is a tokenized match, meaning that your keyword string will be matched against the tokenized text of the Tweet body – tokenization is based on punctuation, symbol, and separator Unicode basic plane characters. For example, a Tweet with the text “I like coca-cola” would be split into the following tokens: I, like, coca, cola. These tokens would then be compared to the keyword string used in your rule. To match strings containing punctuation (for example, coca-cola), symbol, or separator characters, you must use a quoted exact match as described below.

**Note:** With the Search API, accented and special characters are normalized to standard latin characters, which can change meanings in foreign languages or return unexpected results:

For example, "músic" will match “music” and vice versa.   
For example, common phrases like "Feliz Año Nuevo!" in Spanish, would be indexed as "Feliz Ano Nuevo", which changes the meaning of the phrase.

**Note:** This operator will match on both URLs and unwound URLs within a Tweet.

emoji  
Matches an emoji within the body of a Tweet. Emojis are a tokenized match, meaning that your emoji will be matched against the tokenized text of the Tweet body – tokenization is based on punctuation, symbol/emoji, and separator Unicode basic plane characters. For example, a Tweet with the text “I like 🍕” would be split into the following tokens: I, like, 🍕. These tokens would then be compared to the emoji used in your rule. Note that if an emoji has a variant, you must use “quotations” to add to a rule.  
"exact phrase match"  

Matches the tokenized and ordered phrase within the body or urls of a Tweet. This is a tokenized match, meaning that your keyword string will be matched against the tokenized text of the Tweet body – tokenization is based on punctuation, symbol, and separator Unicode basic plane characters.  

**Note:** Punctuation is not tokenized and is instead treated as whitespace.   
For example, quoted “#hashtag” will match “hashtag” but not #hashtag (use the hashtag # operator without quotes to match on actual hashtags.   
For example, quoted “$cashtag” will match “cashtag” but not $cashtag (use the cashtag $ operator without quotes to match on actual cashtags.   
For example, "Love Snow" will match "#love #snow"  
For example, "#Love #Snow" will match "love snow"

**Note:** This operator will match on both URLs and unwound URLs within a Tweet.

"keyword1 keyword2"~N  

Commonly referred to as a proximity operator, this matches a Tweet where the keywords are no more than N tokens from each other.

If the keywords are in the opposite order, they can not be more than N-2 tokens from each other. Can have any number of keywords in quotes. N cannot be greater than 6.

Note that this operator is only available in the enterprise search APIs.  

from:  

Matches any Tweet from a specific user.

The value must be the user’s Twitter numeric Account ID or username (excluding the @ character). See [HERE](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/users/lookup) or [HERE](http://gettwitterid.com/) for methods for looking up numeric Twitter Account IDs.

to:  

Matches any Tweet that is in reply to a particular user.

The value must be the user’s numeric Account ID or username (excluding the @ character). See [HERE](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/users/lookup) for methods for looking up numeric Twitter Account IDs.

url:  
Performs a tokenized (keyword/phrase) match on the expanded URLs of a tweet (similar to url\_contains). Tokens and phrases containing punctuation or special characters should be double-quoted. For example, url:"/developer". While generally not recommended, if you want to match on a specific protocol, enclose in double-quotes: url:"https://developer.twitter.com".  
  
**Note:** When using PowerTrack or Historical PowerTrack, this operator will match on URLs contained within the original Tweet of a Quote Tweet. For example, if your rule includes url:"developer.twitter.com", and a Tweet contains that URL, any Quote Tweets of that Tweet will be included in the results. This is not the case when using the Search API. #  

Matches any Tweet with the given hashtag.

This operator performs an exact match, NOT a tokenized match, meaning the rule “2016” will match posts with the exact hashtag “2016”, but not those with the hashtag “2016election”

Note: that the hashtag operator relies on Twitter’s entity extraction to match hashtags, rather than extracting the hashtag from the body itself. See [HERE](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/entities#hashtags) for more information on Twitter Entities JSON attributes.

@  

Matches any Tweet that mentions the given username.

The to: operator returns a subset match of the @mention operator.

$

Matches any Tweet that contains the specified ‘cashtag’ (where the leading character of the token is the ‘$’ character).

Note that the cashtag operator relies on Twitter’s ‘symbols’ entity extraction to match cashtags, rather than trying to extract the cashtag from the body itself. See [HERE](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/entities#symbols) for more information on Twitter Entities JSON attributes.

Note that this operator is only available in the enterprise search APIs.

retweets\_of:  

_Available alias_: retweets\_of\_user:

Matches tweets that are retweets of a specified user. Accepts both usernames and numeric Twitter Account IDs (NOT tweet status IDs).  
See [HERE](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/users/lookup) for methods for looking up numeric Twitter Account IDs.  

lang:  

Matches Tweets that have been classified by Twitter as being of a particular language (if, and only if, the tweet has been classified). It is important to note that each Tweet is currently only classified as being of one language, so AND’ing together multiple languages will yield no results.

**Note:** if no language classification can be made the provided result is ‘und’ (for undefined).

The list below represents the current supported languages and their corresponding BCP 47 language indentifier:

|     |     |     |     |
| --- | --- | --- | --- |
| Amharic: am | German: de | Malayalam: ml | Slovak: sk |
| Arabic: ar | Greek: el | Maldivian: dv | Slovenian: sl |
| Armenian: hy | Gujarati: gu | Marathi: mr | Sorani Kurdish: ckb |
| Basque: eu | Haitian Creole: ht | Nepali: ne | Spanish: es |
| Bengali: bn | Hebrew: iw | Norwegian: no | Swedish: sv |
| Bosnian: bs | Hindi: hi | Oriya: or | Tagalog: tl |
| Bulgarian: bg | Latinized Hindi: hi-Latn | Panjabi: pa | Tamil: ta |
| Burmese: my | Hungarian: hu | Pashto: ps | Telugu: te |
| Croatian: hr | Icelandic: is | Persian: fa | Thai: th |
| Catalan: ca | Indonesian: in | Polish: pl | Tibetan: bo |
| Czech: cs | Italian: it | Portuguese: pt | Traditional Chinese: zh-TW |
| Danish: da | Japanese: ja | Romanian: ro | Turkish: tr |
| Dutch: nl | Kannada: kn | Russian: ru | Ukrainian: uk |
| English: en | Khmer: km | Serbian: sr | Urdu: ur |
| Estonian: et | Korean: ko | Simplified Chinese: zh-CN | Uyghur: ug |
| Finnish: fi | Lao: lo | Sindhi: sd | Vietnamese: vi |
| French: fr | Latvian: lv | Sinhala: si | Welsh: cy |
| Georgian: ka | Lithuanian: lt |     |

place:  

Matches Tweets tagged with the specified location _or_ Twitter place ID (see examples). Multi-word place names (“New York City”, “Palo Alto”) should be enclosed in quotes.

**Note:** See the [GET geo/search](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/v1/geo/place-information/overview) public API endpoint for how to obtain Twitter place IDs.

**Note:** This operator will not match on Retweets, since Retweet's places are attached to the original Tweet. It will also not match on places attached to the original Tweet of a Quote Tweet.

place\_country:  

Matches Tweets where the country code associated with a tagged [place](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/v1/geo/place-information/overview) matches the given ISO alpha-2 character code.

Valid ISO codes can be found here: [http://en.wikipedia.org/wiki/ISO\_3166-1\_alpha-2](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

**Note:** This operator will not match on Retweets, since Retweet's places are attached to the original Tweet. It will also not match on places attached to the original Tweet of a Quote Tweet.

point\_radius:\[lon lat radius\]  

Matches against the Exact Location (x,y) of the Tweet when present, and in Twitter, against a “Place” geo polygon, where the Place is fully contained within the defined region.

* Units of radius supported are miles (mi) and kilometers (km).
* Radius must be less than 25mi.
* Longitude is in the range of ±180
* Latitude is in the range of ±90
* All coordinates are in decimal degrees.
* Rule arguments are contained with brackets, space delimited.

**Note:** This operator will not match on Retweets, since Retweet's places are attached to the original Tweet. It will also not match on places attached to the original Tweet of a Quote Tweet.

bounding\_box:\[west\_long south\_lat east\_long north\_lat\]  

_Available alias_: geo\_bounding\_box:

Matches against the Exact Location (long, lat) of the Tweet when present, and in Twitter, against a “Place” geo polygon, where the Place is fully contained within the defined region.

* west\_long south\_lat represent the southwest corner of the bounding box where west-long is the longitude of that point, and south\_lat is the latitude.
* east\_long and north\_lat represent the northeast corner of the bounding box, where east\_long is the longitude of that point, and north\_lat is the latitude.
* Width and height of the bounding box must be less than 25mi
* Longitude is in the range of ±180
* Latitude is in the range of ±90
* All coordinates are in decimal degrees.
* Rule arguments are contained with brackets, space delimited.

**Note:** This operator will not match on Retweets, since Retweet's places are attached to the original Tweet. It will also not match on places attached to the original Tweet of a Quote Tweet.

profile\_country:  

Exact match on the “countryCode” field from the “address” object in the Profile Geo enrichment.

Uses a normalized set of two-letter country codes, based on ISO-3166-1-alpha-2 specification. This operator is provided in lieu of an operator for “country” field from the “address” object to be concise.

profile\_region:  

Matches on the “region” field from the “address” object in the Profile Geo enrichment.

This is an exact full string match. It is not necessary to escape characters with a backslash. For example, if matching something with a slash, use “one/two”, not “one\\/two”. Use double quotes to match substrings that contain whitespace or punctuation.

profile\_locality:  

Matches on the “locality” field from the “address” object in the Profile Geo enrichment.

This is an exact full string match. It is not necessary to escape characters with a backslash. For example, if matching something with a slash, use “one/two”, not “one\\/two”. Use double quotes to match substrings that contain whitespace or punctuation.

**NOTE:** All is: and has: operators cannot be used as standalone operators when using the Search API, and must be combined with another clause.

For example, @TwitterDev has:links

|     |     |
| --- | --- |
| has:geo | Matches Tweets that have Tweet-specific geo location data provided from Twitter. This can be either “geo” lat-long coordinate, or a “location” in the form of a Twitter [“Place”](https://dev.twitter.com/overview/api/places), with corresponding display name, geo polygon, and other fields.<br><br>  <br><br>**Note:** When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. |
| has:profile\_geo | _Available alias_: has:derived\_user\_geo<br><br>Matches Tweets that have any [Profile Geo](http://support.gnip.com/enrichments/profile_geo.html) metadata, regardless of the actual value.  <br>  <br><br>**Note:** When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. |
| has:links | This operators matches Tweets which contain links in the message body.  <br>  <br><br>**Note:** When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. |
| is:retweet | Deliver only explicit retweets that match a rule. Can also be negated to exclude retweets that match a rule from delivery and only original content is delivered.<br><br>This operator looks only for true Retweets, which use Twitter’s retweet functionality. Quoted Tweets and Modified Tweets which do not use Twitter’s retweet functionality will not be matched by this operator.<br><br>  <br><br>**Note:** When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. |
| is:reply | An operator to filter Tweets based on whether they are or are not replies to Tweets. Deliver only explicit replies that match a rule. Can also be negated to exclude replies that match a rule from delivery.<br><br>Note that this operator is available for paid premium and enterprise search and is not available in Sandbox dev environments.<br><br>  <br><br>**Note:** When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. |
| is:quote | Delivers only Quote Tweets, or Tweets that reference another Tweet, as identified by the "is\_quote\_status":true in Tweet payloads. Can also be negated to exclude Quote Tweets.  <br><br>**Note:** When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. |
| is:verified | Deliver only Tweets where the author is “verified” by Twitter. Can also be negated to exclude Tweets where the author is verified.  <br>  <br><br>**Note:** When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. |
| has:mentions | Matches Tweets that mention another Twitter user.  <br>  <br><br>**Note:** When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. |
| has:hashtags | Matches Tweets that contain a hashtag.  <br>  <br><br>**Note:** When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. |
| has:media | _Available alias_: has:media\_link<br><br>Matches Tweets that contain a media url classified by Twitter. For example, pic.twitter.com.  <br>  <br><br>**Note:** When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. |
| has:images | Matches Tweets that contain a media url classified by Twitter. For example, pic.twitter.com.  <br>  <br><br>**Note:** When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. |
| has:videos | _Available alias_: has:video\_link<br><br>Matches Tweets that contain native Twitter videos, uploaded directly to Twitter. This will not match on videos created with Vine, Periscope, or Tweets with links to other video hosting sites.  <br>  <br><br>**Note:** When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. |
| has:symbols | Matches Tweets that contain a cashtag symbol (with a leading ‘$’ character. For example, $tag).  Note that this operator is only available in the enterprise search APIs.  <br>  <br><br>**Note:** When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. |

Full-archive search - Metadata and filtering timeline

Full-Archive Search metadata timeline
-------------------------------------

That article discusses how the historical changes of the full-archive roadmap affects creating the filters needed to find your historical signal of interest. This article and a complementary [article about Historical PowerTrack](https://developer.twitter.com/en/docs/twitter-api/enterprise/historical-powertrack-api/guides/hpt-timeline), will serve as a ‘compare and contrast’ discussion of the two Twitter historical products.  

### Product overview

The enterprise-tier Full-archive Search was launched in August 2015, and the premium-tier version was launched in February 2018. These search products enable customers to immediately access any publicly available Tweet. With Full-archive Search you submit a single query and receive a response in classic RESTful fashion. Full-archive Search implements (up to) 500-Tweets-per-response pagination, and supports up to a 60-requests-per-minute (rpm) rate-limit for premium, 120 rpm for enterprise. Given these details, Full-archive Search can be used to rapidly retrieve Tweets, and at large scale using concurrent requests.

Unlike Historical PowerTrack, whose archive is based on a set of Tweet flat-files on disk, the Full-archive Search Tweet archive is much like an on-line database. As with all databases, it supports making queries on its contents. It also makes use of an _index_ to enable high-performance data retrieval. With Full-archive search endpoints, the querying language is made up of PowerTrack Operators, and these Operators each correspond to a Tweet JSON attribute that is indexed.

Also, like Historical PowerTrack, there are Tweet attributes that are current to the time a query is made. For example, if you are using Search API to access a Tweet posted in 2010 today, the user's profile description, account 'home' location, display name, and Tweet metrics for Favorites and Retweet counts will be updated to today’s values and not what they were in 2010. 

### Metadata timelines

Below is a timeline of when Full-archive search endpoint Operators begin matching. In some cases Operator matching began well _after_ a ‘communication convention’ became commonplace on Twitter. For example, @Replies emerged as a user convention in 2006, but did not become a _first-class object_ or _event_ with ‘supporting’ JSON until early 2007. Accordingly, matching on @Replies in 2006 requires an examination of the Tweet body, rather than relying on the `to:` and `in_reply_to_status_id:` PowerTrack Operators.

The details provided here were generated using Full-Archive Search (a product of hundreds of searches). This timeline is not 100% complete or precise. If you identify another filtering/metadata “born on date” fundamental to your use-case, please let us know.

Note that the underlying Search index is subject to being rebuilt. Accordingly, these timeline details are subject to change.

#### 2006

* March 26 - `lang:`. An example of Tweet metadata being backfilled while generating the Search index.
* July 13 - `has:mentions` begins matching.
* October 6 - `has:symbols`. $cashtags (or symbols) for discussing stock symbols does not become common until early 2009. Until then most usages were probably slang (e.g., $slang).
* October 26 - `has:links` begins matching.
* November 23 - `has:hashtags` begins matching.

#### 2007

* January 30 - First first-class @reply (in\_reply\_to\_user\_id), `reply_to_status_id:` begins matching.
* August 23 - Hashtags emerge as a common convention for organizing topics and conversations. First real use a week later.

#### 2009

* May 15 - `is:retweet`. Note that this Operator starts matching with the ‘beta’ release of official Retweets and its “Via @’ pattern. During this beta period, the Tweet verb is ‘post’ and the original Tweet is not included in the payload.
* August 13 - Final version of official Retweets is released with “RT @” pattern, a verb set to ‘share’, and the ‘retweet\_status’ attribute containing the original Tweet (thus approximately doubling the JSON payload size).

#### 2010

* March 6 - `has:geo`, `bounding_box:` and `point_radius:` geo Operators begin matching.
* August 28 - `has:videos` (Until February 2015, this Operator matches on Tweets with links to select video hosting sites such as youtube.com, vimeo.com, and vivo.com).

#### 2011

* July 20 - `has:media` and `has:images` begin matching. Native photos officially announced August 9, 2010.

#### 2014

* December 3 - (Approximately) _Some_ [Enhanced URL metadata](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/enrichments/overview/expanded-and-enhanced-urls) with HTML title and description begins in payloads. Enhanced metadata more fully emerged in May 2016.

#### 2015

* February 10 - `has:videos` matches on ‘native’ Twitter videos.
* February 17 - `has:profile_geo`, `profile_country:`, `profile_region:`, `profile_locality:` [Profile Geo](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/enrichments/overview/profile-geo) Operators begin matching.
* February 17 - `place_country:` and `place:` Tweet geo Operators begin matching.

#### 2016

* May 1 - [Enhanced URL metadata](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/enrichments/overview/expanded-and-enhanced-urls) more fully available, and was officially announced as part of the [Gnip 2.0 launch in August 2016](https://blog.twitter.com/2016/gnip-2-is-here). No associated Operators for these metadata with Search APIs.

#### 2017

* February 22 - Poll metadata become available in enriched native format. No associated Operators for these metadata.

#### 2022

* September 27 - All Tweet objects created since this date have Edited Tweet metadata available. All Enterprise endpoints that provide Tweet objects were updated to provide this metadata starting on this date. The edit metadata provided includes edit\_history and edit\_controls objects. These metadata will not be returned for Tweets that were created before September 27, 2022. Currently, there are no Enterprise Operators available that match these metadata.  To learn more about Edit Tweet metadata, check out the [Edit Tweets fundamentals](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/edit-tweets) page.

#### 2022

* September 29 - All Tweet objects created since this date have Edited Tweet metadata available. All Enterprise endpoints that provide Tweet objects were updated to provide this metadata starting on this date. The edit metadata provided includes edit\_history and edit\_controls objects. These metadata will not be returned for Tweets that were created before September 27, 2022. Currently, there are no Enterprise Operators available matching these metadata.  To learn more about Edit Tweet metadata, check out the [Edit Tweets fundamentals](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/edit-tweets) page.

### Filtering tips

Given all the above timeline information, it is clear that there are a lot of details to consider when writing Search APIs filters. There are two key things to consider:

* Some metadata have ‘born-on’ dates so filters can result in _false negatives_. Such searches include Operators reliant on metadata that did not exist for all of part of the search period. For example, if you are searching for Tweets with the `has:images` Operator, you will not have any matches for periods before July 2011. That is because that Operator matches on _native_ photos (attached to a Tweet using the Twitter user-interface). For a more complete data set of photo-sharing Tweets, filters for before July 2011 would need to contain rule clauses that match on common URLs for photo hosting.
* Some metadata has been backfilled with metadata from a time _after_ the Tweet was posted.

There are several attribute types that are commonly focused on when creating PowerTrack queries:

* Twitter Profiles
* Original or shared Tweets
* Tweet language classification
* Geo-referencing Tweets
* Shared links media

Some of these have product-specific behavior while others have identical behavior. See below for more details.

#### Twitter Profiles

The Search APIs serves historical Tweets with the user profile data set as it is at the _time of retrieval_. If you request a Tweet from 2014, the user’s profile metadata will reflect how it exists at query-time.

#### Original Tweets and Retweets

The PowerTrack `_is:retweet_` Operator enables users to either include or exclude Retweets. Users of this Operator need to have two strategies for Retweet matching (or not matching) for data before August 2009. Before August 2009, the Tweet message itself needs to be checked, using exact phrase matching, for matches on the “@RT ” pattern (Actually, if you are filtering on Retweets from between May-August 2009, the “Via @” pattern should be included). For periods after August 2009, the _is:retweet_ Operator is available.

#### Tweet language classifications

For filtering on a Tweet’s language classification, Twitter’s historical products are quite different. When the Search archive was built, all Tweets were backfilled with the Twitter language classification. Therefore the lang: Operator is available for the entire Tweet archive.

#### Geo-referencing Tweets

There are three primary ways to geo-reference Tweets:

* **Geographical references in Tweet message.** Matching on geographic references in the Tweet message, while often the most challenging method since it depends on local knowledge, is an option for the entire Tweet archive. [Here](https://twitter.com/biz/statuses/28311) is an example geo-referenced match from 2006 for the San Francisco area based on a ‘golden gate’ filter.
    
* **Tweets geo-tagged by the user.** With the search APIs the ability to start matching on Tweets with some Geo Operators started in March 2010, and with others in February 2015:
    
    * March 6, 2010: `has:geo`, `bounding_box:` and `point_radius:`
    * February 17, 2015: `place_country:` and `place:`
* **Account profile ‘home’ location set by the user.** Profile Geo Operators are available in both Historical PowerTrack and the Search APIs. With the Search APIs, these Profile Geo metadata is available starting in February 2015. For Tweets posted before Profile Geo metadata became available, the `bio_location:` Operator is available which can be used to match on non-normalized user input.
    

#### Shared links and media

In March 2012, the expanded URL enrichment was introduced. Before this time, the Tweet payloads included only the URL as provided by the user. So, if the user included a shortened URL it can be challenging to match on (expanded) URLs of interest. With the Search APIs, these metadata are available starting in March 2012.

In July 2016, the enhanced URL enrichment was introduced. This enhanced version provides a web site’s HTML title and description in the Tweet payload, along with Operators for matching on those. These metadata begin emerging in December 2014.

In September 2016 Twitter introduced ‘native attachments’ where a trailing shared link is not counted against the 140 Tweet character limit. Both URL enrichments still apply to these shared links.

Here are when related Search Operators begin matching:

* 2006 October 26 - `has:links`
* 2011 July 20 - `has:images` and `has:media`
* 2011 August - `url:` with the [Expanded URLs enrichment](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/enrichments/overview/expanded-and-enhanced-urls) As early as September 2006 `(url:"spotify.com" OR url:gnip OR url:microsoft OR url:google OR url:youtube)` matches http://twitter.com/Adam/statuses/16602, even though there is no urls\[\] metadata in twitter\_entities and gnip objects. “youtube.com” is an example of message content that, without any urls\[\] metadata, matches url:youtube.
* 2015 February 10 - `has:videos` for native videos. Between 2010/08/28 and 2015/02/10, this Operator matches on Tweets with links to select video hosting sites such as youtube.com, vimeo.com, and vivo.com.
* 2016 May 1 - `url_title:` and `url_description:`, based on the [Enhanced URLs enrichment](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/enrichments/overview/expanded-and-enhanced-urls), generally available. First Enhanced URL metadata began appearing in December 2014.

### Next steps

* [Learn more about the Full-Archive Search API](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/search-api/overview)
* [Learn more about Historical PowerTrack and its metadata and filtering timeline](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/historical-powertrack-api/guides/hpt-timeline)
* [Choosing between Historical PowerTrack and Full-Archive Search APIs](https://developer.twitter.com/content/developer-twitter/en/docs/tutorials/choosing-historical-api)

FAQ

Frequently asked questions
--------------------------

### General Search Tweet API questions

**The number of Tweets I receive with the data endpoint doesn't match the number of Tweets identified by the counts endpoint. Why is this the case?**

There is a known difference between results provided by the counts endpoint and the data endpoint. You may see a discrepancy in your results because the counts endpoint is pre-compliance (meaning that it does not account for things like deleted Tweets, scrub geo, etc.) whereas the data endpoint is compliant at the time of delivery and accounts for all compliance events. For further reference, please go to [this document](https://developer.twitter.com/content/developer-twitter/en/docs/tweets/search/api-reference/premium-search#CountsEndpoint) on our support site.

**  
I didn't receive a Tweet that should match my query. Why?**

There are a few different reasons why this might have happened, including

1. the Tweet you expected to see is from a protected account
2. because the data endpoint accounts for all compliance events (meaning that deleted Tweets, scrubbed geos, etc. will not be included in the response).

**  
My query matched a Tweet but includes a keyword that I negated. Why is this happening?**

This is likely due to a wrong usage of our premium rules & filtering. Please review our documentation [here](https://developer.twitter.com/en/docs/tweets/rules-and-filtering/guides/using-premium-operators) and ensure you understand the restrictions around building rules.

**  
Are there any libraries that I can use to get started using the Search Tweet APIs?**

Yes, there are, including:

* [Tweepy](http://www.tweepy.org/) - good for using the standard search/tweets product (Python)
* [Twitter API](https://github.com/geduldig/TwitterAPI) - good for using both the standard and premium Search Tweet APIs (Python)
* [Search Tweets Python](https://github.com/twitterdev/search-tweets-python) and [Search Tweets Ruby](https://github.com/twitterdev/search-tweets-ruby) - two good tools that can be used for both premium and enterprise (and v2!) Search Tweet APIs

All of the libraries that we directly support can be found on our TwitterDev GitHub page: [https://github.com/twitterdev](https://github.com/twitterdev).

There are [other third-party libraries](https://developer.twitter.com/en/docs/developer-utilities/twitter-libraries) that may also be helpful; however, please note that some of these may not work with our premium and enterprise products. 

**  
Will I ever receive less volume of Tweets than the value I set as the `maxResults` in my request to the data endpoint?**

Yes. Our data endpoint paginates at either the specified `maxResults` or after 30 days.

For example, if you have 800 Tweets in a given 30 day period, you will have to make two requests to pull the complete results; because the maximum number of Tweets that can be returned per request is 500 (`maxResults`). And if you just have 400 Tweets in month one, and then 100 Tweets in month two, you will also have to use two requests to pull the full results; because pagination takes place after a period of 30 days even if the first request returns less than the specified `maxResults` Tweets.

**  
In what order are the matching Tweets returned?**

Tweets are returned in reverse chronological order. For example, the first page of results will show the most recent Tweets that match the query, pagination will continue until the results posted dates get to the `fromDate` initially requested.

**How do Edit Tweets impact my usage and billing?** 

Only the original Tweet will count for billing purposes. Any subsequent edits will be ignored and not contribute to your overall activity count. 

Enterprise

**I'm interested in learning more about the pricing of the enterprise Search Tweet API and in applying for this offering. How can I do this?**

Our enterprise solutions are customized with predictable pricing to meet the needs of your business. Please apply [here](https://developer.twitter.com/content/developer-twitter/en/enterprise-application) for more information.

**  
How do I build a rule set that matches my use case?**

* Please refer to our enterprise Search Tweet APIs documentation [here](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/search-api/api-reference/enterprise-search)
* Useful information on rules and filering can be found [here](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/rules-and-filtering/guides/using-enterprise-operators)
* Useful information for using the data endpoint can be found [here](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/search-api/api-reference/enterprise-search#DataEndpoint)
* Useful information for using the counts endpoint can be found [here](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/search-api/api-reference/enterprise-search#CountsEndpoint)
* A list of available operators can be found [here](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/search-api/overview#AvailableOperators)

**  
I have exceeded my request caps/limits for the month, but I need to access more data - what can I do?**

Please get in touch with your Account Manager at Twitter who will be able to help you with this.

### Error troubleshooting guide

**Code 404 - Not Found**

1. Please ensure you are using the right parameters for each endpoint (e.g. the `buckets`field can only be used with the counts endpoint, not the data endpoint)
2. Please double check the `:product` `:account_name` and `:label` fields are correct. You can find your `:label` field in the GNIP Console (enterprise customers only).

l

Enterprise search APIs

enterprise-search

Enterprise search APIs
======================

Jump to on this page

[Introduction](#Introduction)

[Methods](#Methods)

[Authentication](#Authentication)

[Request/response behavior](#RequestResponseBehavior)

[Pagination](#Pagination)

[Data endpoint](#DataEndpoint)

[Data request parameters](#DataParameters)

[Example data requests and responses](#DataRequestExamples)

[Counts endpoint](#CountsEndpoint)

[Counts request parameters](#CountsParameters)

[Example counts requests and responses](#CountsRequestExamples)

[HTTP response codes](#HTTPCodes)

Introduction [¶](#introduction- "Permalink to this headline")
-------------------------------------------------------------

There are two enterprise search APIs:

* 30-Day Search API - provides Tweets posted with the last 30 days.
* Full-Archive Search API - provides Tweets from as early as 2006, starting with the first Tweet posted in March 2006.

These search APIs share a common design and the documentation below applies to both. Note that for Tweets created starting September 29, 2022, Tweet objects will include Tweet edit metadata that describes its edit history. See the ["Edit Tweets"](https://developer.twitter.com/en/docs/twitter-api/enterprise/edit-tweets) fundamentals page for more details.

Below you will find important details needed when integrating with the enterprise search APIs:

* Methods for requesting Tweet data and counts
* Authentication
* Pagination
* API request parameters and example requests
* API response JSON payloads and example responses
* HTTP response codes

The enterprise APIs provide low-latency, full-fidelity, query-based access to the Tweet archive. The only difference in the two APIs is the time frame you can search, either the previous 30 days or from as early as 2006. Time frames can be specified with minute granularity. Tweet data is served in reverse chronological order, starting with the most recent Tweet that matches your query. Tweets are available from the search API approximately 30 seconds after being published.

Methods [¶](#methods- "Permalink to this headline")
---------------------------------------------------

The base URI for enterprise search is `https://gnip-api.twitter.com/search/`.

| Method | Description |
| --- | --- |
| [POST /search/:product/accounts/:account\_name/:label](#SearchRequests) | Retrieve Tweets from the past 30 days that match the specified PowerTrack rule. |
| [POST /search/:product/accounts/:account\_name/:label/counts](#CountRequests) | Retrieve the number of Tweets from the past 30 days that match the specified PowerTrack rule. |

Where:

* `:product` indicates the search endpoint you are making requests to, either `30day` or `fullarchive`.
* `:account_name` is the (case-sensitive) name associated with your account, as displayed at console.gnip.com
* `:label` is the (case-sensitive) label associated with your search endpoint, as displayed at console.gnip.com

For example, if the TwitterDev account has the 30-Day search product with a label of 'prod' (short for production), the search endpoints would be:

* Data endpoint: [https://gnip-api.twitter.com/search/30day/accounts/TwitterDev/prod.json](https://gnip-api.twitter.com/search/30day/accounts/TwitterDev/prod.json)
* Counts endpoint: [https://gnip-api.twitter.com/search/30day/accounts/TwitterDev/prod/counts.json](https://gnip-api.twitter.com/search/30day/accounts/TwitterDev/prod/counts.json)

Your complete enterprise search API endpoint is displayed at [https://console.gnip.com](https://console.gnip.com/).

Below there are several example requests using a simple HTTP utility called curl. These examples use URLs with `:product`, `:account_name`, and `:label`. To use these examples, be sure to update the URLs with your details.

Authentication [¶](#authentication- "Permalink to this headline")
-----------------------------------------------------------------

All requests to the enterprise search APIs must use HTTP _Basic Authentication_, constructed from a valid email address and password combination used to log into your account at [https://console.gnip.com](https://console.gnip.com/). Credentials must be passed as the _Authorization_ header for each request.

Request/response behavior [¶](#request-response-behavior- "Permalink to this headline")
---------------------------------------------------------------------------------------

Using the `fromDate` and `toDate` parameters, you can request any time period that the API supports. The 30-Day search API provides Tweets from the most recent 31 days (even though referred to as the '30-Day' API, it makes 31 days available to enable users to make complete-month requests). The Full-Archive search API provides Tweets back to the very first tweet (March 21, 2006). However, a single response will be limited to the lesser of your specified 'maxResults' or 31 days. If matching data or your time range exceeds your specified maxResults or 31 days, you will receive a 'next' token which you should use to paginate through the remainder of your specified time range.

For example, say you are using Full-Archive search and want all Tweets matching your query from January 1, 2017 to June 30, 2017. You will specify that full six-month time period in your request using the `fromDate` and `toDate` parameters. The search API will respond with the first 'page' of Tweets, with the number of Tweets matching your `maxResults` parameter (which defaults to 100). Assuming there are more Tweets (and there most likely will be more), the API will also provide a 'next' token that enables you to make a request for the next 'page' of data. This process is repeated until the API does not return a 'next' token. See the next section for more details.

Pagination [¶](#pagination- "Permalink to this headline")
---------------------------------------------------------

When making both data and count requests it is likely that there is more data than can be returned in a single response. When that is the case the response will include a ‘next’ token. The ‘next’ token is provided as a root-level JSON attribute. Whenever a ‘next’ token is provided, there is additional data to retrieve so you will need to keep making API requests.

**Note:** The ‘next’ token behavior differs slightly for data and counts requests, and both are described below with example responses provided in the API Reference section.

### Data pagination[¶](#data-pagination "Permalink to this headline")

Requests for data will likely generate more data than can be returned in a single response. Each data request includes a parameter that sets the maximum number of Tweets to return per request. This `maxResults` parameter defaults to 100 and can be set to a range of 10-500. If your query matches more Tweets than the 'maxResults' parameter used in the request, the response will include a 'next' token (as a root-level JSON attribute). This 'next' token is used in the subsequent request to retrieve the next portion of the matching Tweets for that query (i.e. the next 'page”). Next tokens will continue to be provided until you have reached the last 'page' of results for that query when no 'next' token is provided.

To request the next 'page' of data, you must make the exact same query as the original, including `query`, `toDate`, and `fromDate` parameters, if used, and also include a 'next' request parameter set to the value from the previous response. This can be utilized with either a GET or POST request. However, the 'next' parameter must be URL encoded in the case of a GET request.

You can continue to pass in the 'next' element from your previous query until you have received all Tweets from the time period covered by your query. When you receive a response that does not include a 'next' element, it means that you have reached the last page and no additional data is available for the specified query and time range.

### Counts pagination[¶](#counts-pagination "Permalink to this headline")

The 'counts' endpoint provides Tweet volumes associated with a query on either a daily, hourly, or per-minute basis. The 'counts' API endpoint will return a timestamped array of counts for a maximum of a 31-day payload of counts. If you request more than 31 days of counts you will be provided a 'next' token. As with the data 'next' tokens, you must make the exact same query as the original and also include a 'next' request parameter set to the value from the previous response.

Beyond requesting more than 31 days of counts, there is another scenario when a 'next' token is provided. For higher volume queries, there is the potential that the generation of counts will take long enough to trigger a response timeout. When this occurs you will receive less than 31 days of counts but will be provided a 'next' token in order to continue making requests for the entire payload of counts. **_Important:_** Timeouts will only issue full "buckets" - so 2.5 days would result in 2 full day "buckets".

### Additional notes[¶](#additional-notes "Permalink to this headline")

* When using a fromDate or toDate in a search request, you will only get results from within your time range. When you reach the last group of results within your time range, you will not receive a 'next' token.
* The 'next' element can be used with any maxResults value between 10-500 (with a default value of 100). The maxResults determines how many Tweets are returned in each response, but does not prevent you from eventually getting all results.
* The 'next' element does not expire. Multiple requests using the same 'next' query will receive the same results, regardless of when the request is made.
* When paging through results using the 'next' parameter, you may encounter duplicates at the edges of the query. Your application should be tolerant of these.

Data endpoint  [¶](#data-endpoint- "Permalink to this headline")
----------------------------------------------------------------

### POST /search/:product/:label[¶](#post-search-product-label "Permalink to this headline")

#### Endpoint pattern:

This endpoint returns data for the specified query and time period. If a time period is not specified the time parameters will default to the last 30 days. Note: This functionality can also be accomplished using a GET request, instead of a POST, by encoding the parameters described below into the URL.

### Data request parameters [¶](#data-request-parameters- "Permalink to this headline")

| Parameters | Description | Required | Sample Value |
| --- | --- | --- | --- |
| query | The equivalent of one PowerTrack rule, with up to 2,048 characters (and no limits on the number of positive and negative clauses).  <br>  <br>This parameter should include ALL portions of the PowerTrack rule, including all operators, and portions of the rule should not be separated into other parameters of the query.  <br>  <br>**Note:** Not all PowerTrack operators are supported. Supported Operators are listed [HERE](https://developer.twitter.com/en/docs/tweets/search/overview/enterprise#AvailableOperators). | Yes | (snow OR cold OR blizzard) weather |
| tag | Tags can be used to segregate rules and their matching data into different logical groups. If a rule tag is provided the rule tag is included in the 'matching\_rules' attribute.  <br>  <br>It is recommended to assign rule-specific UUIDs to rule tags and maintain desired mappings on the client side. | No  | 8HYG54ZGTU |
| fromDate | The oldest UTC timestamp (back to 3/21/2006 with Full-Archive search) from which the Tweets will be provided. Timestamp is in minute granularity and is inclusive (i.e. 12:00 includes the 00 minute).  <br>  <br>_Specified:_ Using only the fromDate with no toDate parameter will deliver results for the query going back in time from now( ) until the fromDate.  <br>  <br>_Not Specified:_ If a fromDate is not specified, the API will deliver all of the results for 30 days prior to now( ) or the toDate (if specified).  <br>  <br>If neither the fromDate or toDate parameter is used, the API will deliver all results for the most recent 30 days, starting at the time of the request, going backwards. | No  | 201207220000 |
| toDate | The latest, most recent UTC timestamp to which the Tweets will be provided. Timestamp is in minute granularity and is not inclusive (i.e. 11:59 does not include the 59th minute of the hour).  <br>  <br>_Specified:_ Using only the toDate with no fromDate parameter will deliver the most recent 30 days of data prior to the toDate.  <br>  <br>_Not Specified:_ If a toDate is not specified, the API will deliver all of the results from now( ) for the query going back in time to the fromDate.  <br>  <br>If neither the fromDate or toDate parameter is used, the API will deliver all results for the entire 30-day index, starting at the time of the request, going backwards. | No  | 201208220000 |
| maxResults | The maximum number of search results to be returned by a request. A number between 10 and the system limit (currently 500). By default, a request response will return 100 results. | No  | 500 |
| next | This parameter is used to get the next 'page' of results as described [HERE](#Pagination). The value used with the parameter is pulled directly from the response provided by the API, and should not be modified. | No  | NTcxODIyMDMyODMwMjU1MTA0 |

  

#### Additional details 

|     |     |
| --- | --- |
| **Available Timeframe** | 30-Day: last 31 days  <br>Full-Archive: March 21, 2006 - Present |
| **Query Format** | The equivalent of one PowerTrack rule, with up to 2,048 characters (and no limits on the number of positive and negative clauses).  <br>  <br>**Note:** Not all PowerTrack operators are supported. Refer to [Available operators](https://developer.twitter.com/en/docs/tweets/search/overview/enterprise#AvailableOperators) for a list of supported operators. |
| **Rate Limit** | Partners will be rate limited at both minute and second granularity. The per minute rate limit will vary by partner as specified in your contract. However, these per-minute rate limits are not intended to be used in a single burst. Regardless of your per minute rate limit, all partners will be limited to a maximum of 20 requests per second, aggregated across all requests for data and/or counts. |
| **Compliance** | All data delivered via the Full-Archive Search API is compliant at the time of delivery. |
| **Realtime Availability** | Data is available in the index within 30 seconds of generation on the Twitter Platform |

### Example data requests and responses [¶](#example-data-requests-and-responses- "Permalink to this headline")

#### Example POST request

* Request parameters in a POST request are sent via a JSON-formatted body, as shown below.
* All portions of the PowerTrack rule being queried for (e.g. keywords, other operators like bounding\_box:) should be placed in the 'query' parameter.
* Do not split portions of the rule out as separate parameters in the query URL.

Here is an example POST (using cURL) command for making an initial data request:

    curl -X POST -u<username> "https://gnip-api.twitter.com/search/:product/accounts/:account_name/:label.json" -d '{"query":"from:twitterDev","maxResults":500,"fromDate":"yyyymmddhhmm","toDate":"yyyymmddhhmm"}'

If the API data response includes a 'next' token, below is a subsequent request that consists of the original request, with the 'next' parameter set to the provided token:

    curl -X POST -u<username> "https://gnip-api.twitter.com/search/:product/accounts/:account_name/:label.json" -d '{"query":"from:twitterDev","maxResults":500,"fromDate":"yyyymmddhhmm","toDate":"yyyymmddhhmm",
    "next":"NTcxODIyMDMyODMwMjU1MTA0"}'

#### Example GET request 

* Request parameters in a GET request are encoded into the URL, using standard URL encoding.
* All portions of the PowerTrack rule being queried for (e.g. keywords, other operators like bounding\_box:) should be placed in the 'query' parameter.
* Do not split portions of the rule out as separate parameters in the query URL.

Here is an example GET (using cURL) command for making an initial data request:

    curl -u<username> "http://gnip-api.twitter.com/search/:product/accounts/:account_name/:label.json?query=from%3Atwitterdev&maxResults=500&fromDate=yyyymmddhhmm&toDate=yyyymmddhhmm"

#### Example data responses 

Note that for Tweets created starting September 29, 2022, Tweet objects will include Tweet edit metadata that describes its edit history. See the ["Edit Tweets"](https://developer.twitter.com/en/docs/twitter-api/enterprise/edit-tweets) fundamentals page for more details.

Below is an example response to a data query. This example assumes that there were more than ‘maxResults’ Tweets available so a 'next' token is provided for subsequent requests. If 'maxResults' or fewer Tweets are associated with your query, no 'next' token would be included in the response.  
The value of the 'next' element will change with each query and should be treated as an opaque string. The 'next' element will look like the following in the response body:  

    {
        "results":
          [
               {--Tweet 1--},
               {--Tweet 2--},
               ...
               {--Tweet 500--}
          ],
        "next":"NTcxODIyMDMyODMwMjU1MTA0",  
        "requestParameters":
          {
            "maxResults":500,
            "fromDate":"201101010000",
            "toDate":"201201010000"
          }
     }

The response to a subsequent request might look like the following (note the new Tweets and different 'next' value):  

    {
          "results":
          [
               {--Tweet 501--},
               {--Tweet 502--},
               ...
               {--Tweet 1000--}
          ],
          "next":"R2hCDbpBFR6eLXGwiRF1cQ",
          "requestParameters":
          {
            "maxResults":500,
            "fromDate":"201101010000",
            "toDate":"201201010000"
          }
     }

You can continue to pass in the 'next' element from your previous query until you have received all Tweets from the time period covered by your query. When you receive a response that does not include a 'next' element, it means that you have reached the last page and no additional data is available in your time range.

* * *

Counts endpoint  [¶](#counts-endpoint- "Permalink to this headline")
--------------------------------------------------------------------

### /search/:stream/counts[¶](#-search-stream-counts "Permalink to this headline")

#### Endpoint pattern:

`/search/fullarchive/accounts/:account_name/:label/counts.json`

This endpoint returns counts (data volumes) data for the specified query. If a time period is not specified the time parameters will default to the last 30 days. Data volumes are returned as a timestamped array on either daily, hourly (default), or by the minute.

**Note:** This functionality can also be accomplished using a GET request, instead of a POST, by encoding the parameters described below into the URL.

### Counts request parameters [¶](#counts-request-parameters- "Permalink to this headline")

| Parameters | Description | Required | Sample Value |
| --- | --- | --- | --- |
| query | The equivalent of one PowerTrack rule, with up to 2,048 characters (and no limits on the number of positive and negative clauses).  <br>  <br>This parameter should include ALL portions of the PowerTrack rule, including all operators, and portions of the rule should not be separated into other parameters of the query.  <br>  <br>**Note:** Not all PowerTrack operators are supported. Refer to [Available operators](https://developer.twitter.com/en/docs/tweets/search/overview/enterprise#AvailableOperators) for a list of supported operators. | Yes | (snow OR cold OR blizzard) weather |
| fromDate | The oldest UTC timestamp (back to 3/21/2006) from which the Tweets will be provided. Timestamp is in minute granularity and is inclusive (i.e. 12:00 includes the 00 minute).  <br>  <br>_Specified:_ Using only the fromDate with no toDate parameter, the API will deliver counts (data volumes) data for the query going back in time from now until the fromDate. If the fromDate is older than 31 days from now( ), you will receive a next token to page through your request.  <br>  <br>_Not Specified:_ If a fromDate is not specified, the API will deliver counts (data volumes) for 30 days prior to now( ) or the toDate (if specified).  <br>  <br>If neither the fromDate or toDate parameter is used, the API will deliver counts (data volumes) for the most recent 30 days, starting at the time of the request, going backwards. | No  | 201207220000 |
| toDate | The latest, most recent UTC timestamp to which the Tweets will be provided. Timestamp is in minute granularity and is not inclusive (i.e. 11:59 does not include the 59th minute of the hour).  <br>  <br>_Specified:_ Using only the toDate with no fromDate parameter will deliver the most recent counts (data volumes) for 30 days prior to the toDate.  <br>  <br>_Not Specified:_ If a toDate is not specified, the API will deliver counts (data volumes) for the query going back in time to the fromDate. If the fromDate is more than 31 days from now( ), you will receive a next token to page through your request.  <br>  <br>If neither the fromDate or toDate parameter is used, the API will deliver counts (data volumes) for the most recent 30 days, starting at the time of the request, going backwards. | No  | 201208220000 |
| bucket | The unit of time for which count data will be provided. Count data can be returned for every day, hour or minute in the requested timeframe. By default, hourly counts will be provided. Options: 'day', 'hour', 'minute' | No  | minute |
| next | This parameter is used to get the next 'page' of results as described [HERE](#Pagination). The value used with the parameter is pulled directly from the response provided by the API, and should not be modified. | No  | NTcxODIyMDMyODMwMjU1MTA0 |

#### Additional details

|     |     |
| --- | --- |
| **Available Timeframe** | 30-Day: last 31 days  <br>Full-Archive: March 21, 2006 - Present |
| **Query Format** | The equivalent of one PowerTrack rule, with up to 2,048 characters.  <br>  <br>**Note:** Not all PowerTrack operators are supported. Refer to [Available operators](https://developer.twitter.com/en/docs/tweets/search/overview/enterprise#AvailableOperators) for a list of supported operators. |
| **Rate Limit** | Partners will be rate limited at both minute and second granularity. The per minute rate limit will vary by partner as specified in your contract. However, these per-minute rate limits are not intended to be used in a single burst. Regardless of your per minute rate limit, all partners will be limited to a maximum of 20 requests per second, aggregated across all requests for data and/or counts. |
| **Count Precision** | The counts delivered through this endpoint reflect the number of Tweets that occurred and do not reflect any later compliance events (deletions, scrub geos). Some Tweets counted may not be available via data endpoint due to user compliance actions. |

### Example counts requests and responses [¶](#example-counts-requests-and-responses- "Permalink to this headline")

#### Example POST request

* Request parameters in a POST request are sent via a JSON-formatted body, as shown below.
* All portions of the PowerTrack rule being queried for (e.g. keywords, other operators like bounding\_box:) should be placed in the 'query' parameter.
* Do not split portions of the rule out as separate parameters in the query URL.

Here is an example POST (using cURL) command for making an initial counts request:

    curl -X POST -u<username> "https://gnip-api.twitter.com/search/:product/accounts/:account_name/:label/counts.json" -d '{"query":"TwitterDev","fromDate":"yyyymmddhhmm","toDate":"yyyymmddhhmm","bucket":"day"}'

If the API counts response includes a 'next' token, below is a subsequent request that consists of the original request, with the 'next' parameter set to the provided token:

    curl -X POST -u<username> "https://gnip-api.twitter.com/search/:product/accounts/:account_name/:label/counts.json" -d '{"query":"TwitterDev","fromDate":"yyyymmddhhmm","toDate":"yyyymmddhhmm","bucket":"day",
    "next":"YUcxO87yMDMyODMwMjU1MTA0"}'

#### Example GET request

* Request parameters in a GET request are encoded into the URL, using standard URL encoding
* All portions of the PowerTrack rule being queried for (e.g. keywords, other operators like bounding\_box:) should be placed in the 'query' parameter
* Do not split portions of the rule out as separate parameters in the query URL

Here is an example GET (using cURL) command for making an initial counts request:

    curl -u<username> "http://gnip-api.twitter.com/search/fullarchive/accounts/:account_name/:label/counts.json?query=TwitterDev&bucket=day&fromDate=yyyymmddhhmm&toDate=yyyymmddhhmm"

#### Example counts responses

Below is an example response to a counts (data volume) query. This example response includes a 'next' token, meaning the counts request was for more than 31 days, or that the submitted query had a large enough volume associated with it to trigger a partial response.

The value of the 'next' element will change with each query and should be treated as an opaque string. The 'next' element will look like the following in the response body:

    {
      "results": [
        { "timePeriod": "201101010000", "count": 32 },
        { "timePeriod": "201101020000", "count": 45 },
        { "timePeriod": "201101030000", "count": 57 },
        { "timePeriod": "201101040000", "count": 123 },
        { "timePeriod": "201101050000", "count": 134 },
        { "timePeriod": "201101060000", "count": 120 },
        { "timePeriod": "201101070000", "count": 43 },
        { "timePeriod": "201101080000", "count": 65 },
        { "timePeriod": "201101090000", "count": 85 },
        { "timePeriod": "201101100000", "count": 32 },
        { "timePeriod": "201101110000", "count": 23 },
        { "timePeriod": "201101120000", "count": 85 },
        { "timePeriod": "201101130000", "count": 32 },
        { "timePeriod": "201101140000", "count": 95 },
        { "timePeriod": "201101150000", "count": 109 },
        { "timePeriod": "201101160000", "count": 34 },
        { "timePeriod": "201101170000", "count": 74 },
        { "timePeriod": "201101180000", "count": 24 },
        { "timePeriod": "201101190000", "count": 90 },
        { "timePeriod": "201101200000", "count": 85 },
        { "timePeriod": "201101210000", "count": 93 },
        { "timePeriod": "201101220000", "count": 48 },
        { "timePeriod": "201101230000", "count": 37 },
        { "timePeriod": "201101240000", "count": 54 },
        { "timePeriod": "201101250000", "count": 52 },
        { "timePeriod": "201101260000", "count": 84 },
        { "timePeriod": "201101270000", "count": 120 },
        { "timePeriod": "201101280000", "count": 34 },
        { "timePeriod": "201101290000", "count": 83 },
        { "timePeriod": "201101300000", "count": 23 },
        { "timePeriod": "201101310000", "count": 12 }
       ],
      "totalCount":2027,
      "next":"NTcxODIyMDMyODMwMjU1MTA0",
      "requestParameters":
        {
          "bucket":"day",
          "fromDate":"201101010000",
          "toDate":"201201010000"
        }
    }

The response to a subsequent request might look like the following (note the new counts timeline and different 'next' value):

    {
      "results": [
        { "timePeriod": "201102010000", "count": 45 },
        { "timePeriod": "201102020000", "count": 76 },
         ....
        { "timePeriod": "201103030000", "count": 13 }
     ],
     "totalCount":3288,
     "next":"WE79fnakFanyMDMyODMwMjU1MTA0",
     "requestParameters":
        {
          "bucket":"day",
          "fromDate":"201101010000",
          "toDate":"201201010000"
        }
    }
    

You can continue to pass in the 'next' element from your previous query until you have received all counts from the query time period. When you receive a response that does not include a 'next' element, it means that you have reached the last page and no additional counts are available in your time range.

HTTP response codes [¶](#http-response-codes- "Permalink to this headline")
---------------------------------------------------------------------------

| Status | Text | Description |
| --- | --- | --- |
| 200 | OK  | The request was successful. The JSON response will be similar to the following: |
| 400 | Bad Request | Generally, this response occurs due to the presence of invalid JSON in the request, or where the request failed to send any JSON payload. |
| 401 | Unauthorized | HTTP authentication failed due to invalid credentials. Log in to console.gnip.com with your credentials to ensure you are using them correctly with your request. |
| 404 | Not Found | The resource was not found at the URL to which the request was sent, likely because an incorrect URL was used. |
| 422 | Unprocessable Entity | This is returned due to invalid parameters in the query -- e.g. invalid PowerTrack rules. |
| 429 | Unknown Code | Your app has exceeded the limit on connection requests. The corresponding JSON message will look similar to the following: |
| 500 | Internal Server Error | There was an error on the server side. Retry your request using an exponential backoff pattern. |
| 502 | Proxy Error | There was an error on server side. Retry your request using an exponential backoff pattern. |
| 503 | Service Unavailable | There was an error on server side. Retry your request using an exponential backoff pattern. |