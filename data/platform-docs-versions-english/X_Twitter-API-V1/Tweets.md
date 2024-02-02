Overview

Overview
--------

Standard

The Twitter's standard search API (search/tweets) allows simple queries against the indices of recent or popular Tweets and behaves similarly to, but not exactly like the [Search UI](https://twitter.com/search-advanced) feature available in Twitter mobile or web clients. The Twitter Search API searches against a sampling of recent Tweets published in the past 7 days.

**Auth:** Twitter Oauth 1.0, app-only or app-user  

**Query abilities:** Limited operators for past ~7 days, recreating the search functionality in the Twitter UI.  See [How to build a standard query here](https://developer.twitter.com/en/docs/tweets/rules-and-filtering/guides/build-standard-queries).

Before digging in, it’s important to know that the standard search API is focused on relevance _and not completeness_. This means that some Tweets and users may be missing from search results. If you want to match for completeness you should consider the [premium](https://developer.twitter.com/content/developer-twitter/en/docs/tweets/search/api-reference/get-search-tweets) or [enterprise](https://developer.twitter.com/content/developer-twitter/en/docs/tweets/search/api-reference/premium-search) search APIs.  

A detailed reference on the standard search API endpoint can be found [HERE](https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets).

How to build a standard query

**Please note:**  

We launched a [new version of the standard Search Tweets endpoint](https://developer.twitter.com/en/docs/twitter-api/tweets/search/introduction) as part of [Twitter API v2: Early Access](https://developer.twitter.com/en/docs/twitter-api/early-access). If you are currently using any of these endpoints, you can use our [migration materials](https://developer.twitter.com/en/docs/twitter-api/tweets/search/migrate/standard-to-twitter-api-v2) to start working with the newer endpoint.

To see all of Twitter's search endpoint offerings, please visit our [search overview](https://developer.twitter.com/en/docs/twitter-api/search-overview).

How to build a query
--------------------

Standard

The best way to build a query and test if it’s valid and will return matched Tweets is to first try it at [twitter.com/search](https://twitter.com/search). As you get a satisfactory result set, the URL loaded in the browser will contain the proper query syntax that can be reused in the API endpoint. Here’s an example:

1. We want to search for Tweets referencing @twitterapi account. First, we run the search on [twitter.com/search](https://twitter.com/search)
2. Check and copy the URL loaded. In this case, we got: [https://twitter.com/search?q=%40twitterapi](https://twitter.com/search?q=%40twitterapi)
3. Replace https://twitter.com/search with https://api.twitter.com/1.1/search/tweets.json and you will get: https://api.twitter.com/1.1/search/tweets.json?q=%40twitterapi
4. Run a Twurl command to execute the search.

Please note that the API requires that the request is authenticated (check [Authentication & Authorization](https://developer.twitter.com/en/docs/basics/authentication/overview/authentication-and-authorization.html) documentation for more details on this). Also note that the search results at twitter.com may return historical results, while the Search API usually only serves Tweets from the past week.

Using standard search

**Please note:**  

We launched a [new version of the standard Search Tweets endpoint](https://developer.twitter.com/en/docs/twitter-api/tweets/search/introduction) as part of [Twitter API v2: Early Access](https://developer.twitter.com/en/docs/twitter-api/early-access). If you are currently using any of these endpoints, you can use our [migration materials](https://developer.twitter.com/en/docs/twitter-api/tweets/search/migrate/standard-to-twitter-api-v2) to start working with the newer endpoint.

To see all of Twitter's search endpoint offerings, please visit our [search overview](https://developer.twitter.com/en/docs/twitter-api/search-overview).

Integrating with standard search
--------------------------------

Standard

One way to start testing searches for Tweets, is to first use the twitter.com/search UI, and build a query there.  There is not complete parity or completeness between the web interface and the standard search API, but this can help to get started.

Using the operators below and the search/tweets API, you can iterate on the result by adding more specificity, or negations to get the desired results.  As you get a satisfactory result set, the URL loaded in the browser will contain the proper query syntax that can be reused in the API endpoint. 

Here’s an example:  

* We want to search for Tweets referencing _TwitterDev_, the word _new_ and the word _premium_. First, we run the search on twitter.com/search: https://twitter.com/search?q=twitterdev%20new%20premium
* Replace “https://twitter.com/search” with “https://api.twitter.com/1.1/search/tweets.json” and you will get: https://api.twitter.com/1.1/search/tweets.json?q=twitterdev%20new%20premium
* Execute this URL to do the search in the API.  

Here's an example twurl command: `twurl /1.1/search/tweets.json?q=twitterdev%20new%20premium`

And the result:

{
	"statuses": \[{
				"created\_at": "Thu Feb 01 16:40:07 +0000 2018",
				"id": 959104084845453312,
				"id\_str": "959104084845453312",
				"text": "RT @TwitterAPI: New year, new access for our developer community! \\ud83c\\udf89\\n\\nToday, we\\u2019re launching our premium Search Tweets: Full-archive endpoin\\u2026",
				"truncated": false,
				"entities": {
					"hashtags": \[\],
					"symbols": \[\],
					"user\_mentions": \[{
						"screen\_name": "TwitterAPI",
						"name": "Twitter API",
						"id": 6253282,
						"id\_str": "6253282",
						"indices": \[3, 14\]
					}\],
					"urls": \[\]
				},
				"metadata": {
					"iso\_language\_code": "en",
					"result\_type": "recent"
				},
				"source": "\\u003ca href=\\"http:\\/\\/twitter.com\\" rel=\\"nofollow\\"\\u003eTwitter Web Client\\u003c\\/a\\u003e",
				"in\_reply\_to\_status\_id": null,
				"in\_reply\_to\_status\_id\_str": null,
				"in\_reply\_to\_user\_id": null,
				"in\_reply\_to\_user\_id\_str": null,
				"in\_reply\_to\_screen\_name": null,
				"user": {
					"id": 2244994945,
					"id\_str": "2244994945",
					"name": "Twitter Dev",
					"screen\_name": "TwitterDev",
					"location": "Internet",
					"description": "Your official source for Twitter Platform news, updates & events. Need technical help? Visit https:\\/\\/t.co\\/mGHnxZU8c1 \\u2328\\ufe0f #TapIntoTwitter",
					"url": "https:\\/\\/t.co\\/FGl7VOULyL",
					"entities": {
						"u.......

### Important Practices

* Ensure all parameters are properly URL encoded.
* Limit your searches to 10 keywords and operators.
* Queries can be limited due to complexity. If this happens, the Search API will respond with the error: {"error":"Sorry, your query is too complex. Please reduce complexity and try again."}.
* The Search API is not a complete index of all Tweets, but instead an index of recent Tweets. The index includes between 6-9 days of Tweets.

**Example searches:**

When you are following an event that’s currently happening, you would be interested in search for recent Tweets using the event hashtag  

You want recent Tweets that contain the hashtag #superbowl

Your search URL is: https://api.twitter.com/1.1/search/tweets.json?q=%23superbowl&result\_type=recent

`twurl /1.1/search/tweets.json?q=%23superbowl&result_type=recent`  

When you want to know what Tweets are coming from a specific location, with a specific language:

You want: all recent Tweets in Portuguese, near Maracanã soccer stadium in Rio de Janeiro

Your search URL is: https://api.twitter.com/1.1/search/tweets.json?q=geocode=-22.912214,-43.230182,1km&lang=pt&result\_type=recent

`twurl /1.1/search/tweets.json?q=geocode=-22.912214,-43.230182,1km&lang=pt&result_type=recent`  

When you want the most popular tweets of a specific user using a hashtag:

You want: popular Tweets from @Cmdr\_Hadfield mentioning the hashtag #nasa

Your search URL is: https://api.twitter.com/1.1/search/tweets.json?q=from%3ACmdr\_Hadfield%20%23nasa&result\_type=popular

`twurl /1.1/search/tweets.json?q=from%3ACmdr_Hadfield%20%23nasa&result_type=popular`  

**Standard search operators**  

The query can have operators that modify its behavior.  Below are examples that illustrate the available operators in standard search:

| Operator | Finds Tweets... |
| --- | --- |
| watching now | containing both “watching” and “now”. This is the default operator. |
| “happy hour” | containing the exact phrase “happy hour”. |
| love OR hate | containing either “love” or “hate” (or both). |
| beer -root | containing “beer” but not “root”. |
| #haiku | containing the hashtag “haiku”. |
| from:interior | sent from Twitter account “interior”. |
| list:NASA/astronauts-in-space-now | sent from a Twitter account in the NASA list astronauts-in-space-now |
| to:NASA | a Tweet authored in reply to Twitter account “NASA”. |
| @NASA | mentioning Twitter account “NASA”. |
| politics filter:safe | containing “politics” with Tweets marked as potentially sensitive removed. |
| puppy filter:media | containing “puppy” and an image or video. |
| puppy -filter:retweets | containing “puppy”, filtering out retweets |
| puppy filter:native\_video | containing “puppy” and an uploaded video, Amplify video, Periscope, or Vine. |
| puppy filter:periscope | containing “puppy” and a Periscope video URL. |
| puppy filter:vine | containing “puppy” and a Vine. |
| puppy filter:images | containing “puppy” and links identified as photos, including third parties such as Instagram. |
| puppy filter:twimg | containing “puppy” and a pic.twitter.com link representing one or more photos. |
| hilarious filter:links | containing “hilarious” and linking to URL. |
| puppy url:amazon | containing “puppy” and a URL with the word “amazon” anywhere within it. |
| superhero since:2015-12-21 | containing “superhero” and sent since date “2015-12-21” (year-month-day). |
| puppy until:2015-12-21 | containing “puppy” and sent before the date “2015-12-21”. |
| movie -scary :) | containing “movie”, but not “scary”, and with a positive attitude. |
| flight :( | containing “flight” and with a negative attitude. |
| traffic ? | containing “traffic” and asking a question. |

Please, make sure to [URL encode](http://en.wikipedia.org/wiki/URL_encoding) these queries before making the request. There are several online tools to help you to do that, or you can search at twitter.com/search and copy the encoded URL from the browser’s address bar. The table below shows some example mappings from search queries to URL encoded queries:

| Search query | URL encoded query |
| --- | --- |
| #haiku #poetry | %23haiku+%23poetry |
| “happy hour” :) | %22happy%20hour%22%20%3A%29 |

Note that the space character can be represented by “%20” or “+” sign.  
 

Additional parameters
---------------------

There is a set of additional parameters that allows a better control of the search results. The [standard search API reference](https://developer.twitter.com/content/developer-twitter/en/docs/tweets/search/api-reference/get-search-tweets) documentation has detailed information about the usage of the parameters, this section will only give a brief description of their capabilities:

* **Result Type**: just like twitter.com/search results, the result\_type parameter selects whether the result set will be represented by recent or popular Tweets, or even a mix of both.
* **Geolocalization**: the search operator “near” isn’t available in the API, but there is a more precise way to restrict your query by a given location using the geocode parameter specified with the template “latitude,longitude,radius”, for example, “37.781157,-122.398720,1mi”. When conducting geo searches, the search API will first attempt to find Tweets which have lat/long within the queried geocode, and in case of not having success, it will attempt to find Tweets created by users whose profile location can be reverse geocoded into a lat/long within the queried geocode, meaning that is possible to receive Tweets which do not include lat/long information.
* **Language**: the lang parameter restricts Tweets to the given language.
* **Iterating in a result set**: parameters such count, until, since\_id, max\_id control iteration through search results, since it could be a large set of Tweets. The [Working with Timelines](https://developer.twitter.com/en/docs/tweets/timelines/guides/working-with-timelines.html) documentation is a rich and illustrative tutorial to learn how to use these parameters to achieve the best efficiency and reliability when processing result sets.

Standard search API

get-search-tweets

Standard search API
===================

Returns a collection of relevant [Tweets](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object) matching a specified query.

Please note that Twitter's search service and, by extension, the Search API is not meant to be an exhaustive source of Tweets. Not all Tweets will be indexed or made available via the search interface.

To learn how to use [Twitter Search](https://twitter.com/search) effectively, please see the [Standard search operators](https://developer.twitter.com/en/docs/tweets/search/guides/standard-operators) page for a list of available filter operators. Also, see the [Working with Timelines](https://developer.twitter.com/en/docs/tweets/timelines/guides/working-with-timelines) page to learn best practices for navigating results by `since_id` and `max_id`.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/search/tweets.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 180 |
| Requests / 15-min window (app auth) | 450 |
| Supports Edit Tweets feature? | Yes |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

| Name | Required | Description | Default Value | Example |
| --- | --- | --- | --- | --- |
| q   | required | A UTF-8, URL-encoded search query of 500 characters maximum, including operators. Queries may additionally be limited by complexity. |     | `@noradio` |
| include\_ext\_edit\_control | optional | Must be set to true in order to return edited Tweet metadata as part of the Tweet object.<br><br>`include_ext_edit_control=true`<br><br>Note that historical Tweets may not contain edited Tweet metadata.<br><br>To learn more about how edited Tweets are supported, see the [Edit Tweets fundamentals](https://developer.twitter.com/en/docs/twitter-api/v1/edit-tweets) page. |     | `true` |
| geocode | optional | Returns tweets by users located within a given radius of the given latitude/longitude. The location is preferentially taking from the Geotagging API, but will fall back to their Twitter profile. The parameter value is specified by " `latitude,longitude,radius` ", where radius units must be specified as either " `mi` " (miles) or " `km` " (kilometers). Note that you cannot use the near operator via the API to geocode arbitrary locations; however you can use this `geocode` parameter to search near geocodes directly. A maximum of 1,000 distinct "sub-regions" will be considered when using the radius modifier. |     | `37.781157 -122.398720 1mi` |
| lang | optional | Restricts tweets to the given language, given by an [ISO 639-1](http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) code. Language detection is best-effort. |     | `eu` |
| locale | optional | Specify the language of the query you are sending (only `ja` is currently effective). This is intended for language-specific consumers and the default should work in the majority of cases. |     | `ja` |
| result\_type | optional | Optional. Specifies what type of search results you would prefer to receive. The current default is "mixed." Valid values include:<br><br>\* `mixed` : Include both popular and real time results in the response.<br><br>\* `recent` : return only the most recent results in the response<br><br>\* `popular` : return only the most popular results in the response. |     | `mixed` `recent` `popular` |
| count | optional | The number of tweets to return per page, up to a maximum of 100. Defaults to 15. This was formerly the "rpp" parameter in the old Search API. |     | `100` |
| until | optional | Returns tweets created before the given date. Date should be formatted as YYYY-MM-DD. Keep in mind that the search index has a 7-day limit. In other words, no tweets will be found for a date older than one week. |     | `2015-07-19` |
| since\_id | optional | Returns results with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets which can be accessed through the API. If the limit of Tweets has occured since the since\_id, the since\_id will be forced to the oldest ID available. |     | `12345` |
| max\_id | optional | Returns results with an ID less than (that is, older than) or equal to the specified ID. |     | `54321` |
| include\_entities | optional | The `entities` node will not be included when set to `false`. |     | `false` |

Example Requests[¶](#example-requests "Permalink to this headline")
-------------------------------------------------------------------

    $ curl --request GET 
     --url 'https://api.twitter.com/1.1/search/tweets.json?q=nasa&result_type=popular' 
     --header 'authorization: OAuth oauth_consumer_key="consumer-key-for-app", 
     oauth_nonce="generated-nonce", oauth_signature="generated-signature", 
     oauth_signature_method="HMAC-SHA1", oauth_timestamp="generated-timestamp", 
     oauth_token="access-token-for-authed-user", oauth_version="1.0"'

    $ twurl /1.1/search/tweets.json?q=nasa&result_type=popular

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
        "statuses": [
            {
                "created_at": "Sun Feb 25 18:11:01 +0000 2018",
                "id": 967824267948773377,
                "id_str": "967824267948773377",
                "text": "From pilot to astronaut, Robert H. Lawrence was the first African-American to be selected as an astronaut by any na… https://t.co/FjPEWnh804",
                "truncated": true,
                "entities": {
                    "hashtags": [],
                    "symbols": [],
                    "user_mentions": [],
                    "urls": [
                        {
                            "url": "https://t.co/FjPEWnh804",
                            "expanded_url": "https://twitter.com/i/web/status/967824267948773377",
                            "display_url": "twitter.com/i/web/status/9…",
                            "indices": [
                                117,
                                140
                            ]
                        }
                    ]
                },
                "metadata": {
                    "result_type": "popular",
                    "iso_language_code": "en"
                },
                "source": "<a href='"https://www.sprinklr.com"' rel='"nofollow"'>Sprinklr</a>",
                "in_reply_to_status_id": null,
                "in_reply_to_status_id_str": null,
                "in_reply_to_user_id": null,
                "in_reply_to_user_id_str": null,
                "in_reply_to_screen_name": null,
                "user": {
                    "id": 11348282,
                    "id_str": "11348282",
                    "name": "NASA",
                    "screen_name": "NASA",
                    "location": "",
                    "description": "Explore the universe and discover our home planet with @NASA. We usually post in EST (UTC-5)",
                    "url": "https://t.co/TcEE6NS8nD",
                    "entities": {
                        "url": {
                            "urls": [
                                {
                                    "url": "https://t.co/TcEE6NS8nD",
                                    "expanded_url": "http://www.nasa.gov",
                                    "display_url": "nasa.gov",
                                    "indices": [
                                        0,
                                        23
                                    ]
                                }
                            ]
                        },
                        "description": {
                            "urls": []
                        }
                    },
                    "protected": false,
                    "followers_count": 28605561,
                    "friends_count": 270,
                    "listed_count": 90405,
                    "created_at": "Wed Dec 19 20:20:32 +0000 2007",
                    "favourites_count": 2960,
                    "utc_offset": -18000,
                    "time_zone": "Eastern Time (US & Canada)",
                    "geo_enabled": false,
                    "verified": true,
                    "statuses_count": 50713,
                    "lang": "en",
                    "contributors_enabled": false,
                    "is_translator": false,
                    "is_translation_enabled": false,
                    "profile_background_color": "000000",
                    "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/590922434682880000/3byPYvqe.jpg",
                    "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/590922434682880000/3byPYvqe.jpg",
                    "profile_background_tile": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/188302352/nasalogo_twitter_normal.jpg",
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/188302352/nasalogo_twitter_normal.jpg",
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/11348282/1518798395",
                    "profile_link_color": "205BA7",
                    "profile_sidebar_border_color": "000000",
                    "profile_sidebar_fill_color": "F3F2F2",
                    "profile_text_color": "000000",
                    "profile_use_background_image": true,
                    "has_extended_profile": true,
                    "default_profile": false,
                    "default_profile_image": false,
                    "following": null,
                    "follow_request_sent": null,
                    "notifications": null,
                    "translator_type": "regular"
                },
                "geo": null,
                "coordinates": null,
                "place": null,
                "contributors": null,
                "is_quote_status": false,
                "retweet_count": 988,
                "favorite_count": 3875,
                "favorited": false,
                "retweeted": false,
                "possibly_sensitive": false,
                "lang": "en"
            },
            {
                "created_at": "Sun Feb 25 19:31:07 +0000 2018",
                "id": 967844427480911872,
                "id_str": "967844427480911872",
                "text": "A magnetic power struggle of galactic proportions - new research highlights the role of the Sun's magnetic landscap… https://t.co/29dZgga54m",
                "truncated": true,
                "entities": {
                    "hashtags": [],
                    "symbols": [],
                    "user_mentions": [],
                    "urls": [
                        {
                            "url": "https://t.co/29dZgga54m",
                            "expanded_url": "https://twitter.com/i/web/status/967844427480911872",
                            "display_url": "twitter.com/i/web/status/9…",
                            "indices": [
                                117,
                                140
                            ]
                        }
                    ]
                },
                "metadata": {
                    "result_type": "popular",
                    "iso_language_code": "en"
                },
                "source": "<a href='"https://www.sprinklr.com"' rel='"nofollow"'>Sprinklr</a>",
                "in_reply_to_status_id": null,
                "in_reply_to_status_id_str": null,
                "in_reply_to_user_id": null,
                "in_reply_to_user_id_str": null,
                "in_reply_to_screen_name": null,
                "user": {
                    "id": 11348282,
                    "id_str": "11348282",
                    "name": "NASA",
                    "screen_name": "NASA",
                    "location": "",
                    "description": "Explore the universe and discover our home planet with @NASA. We usually post in EST (UTC-5)",
                    "url": "https://t.co/TcEE6NS8nD",
                    "entities": {
                        "url": {
                            "urls": [
                                {
                                    "url": "https://t.co/TcEE6NS8nD",
                                    "expanded_url": "http://www.nasa.gov",
                                    "display_url": "nasa.gov",
                                    "indices": [
                                        0,
                                        23
                                    ]
                                }
                            ]
                        },
                        "description": {
                            "urls": []
                        }
                    },
                    "protected": false,
                    "followers_count": 28605561,
                    "friends_count": 270,
                    "listed_count": 90405,
                    "created_at": "Wed Dec 19 20:20:32 +0000 2007",
                    "favourites_count": 2960,
                    "utc_offset": -18000,
                    "time_zone": "Eastern Time (US & Canada)",
                    "geo_enabled": false,
                    "verified": true,
                    "statuses_count": 50713,
                    "lang": "en",
                    "contributors_enabled": false,
                    "is_translator": false,
                    "is_translation_enabled": false,
                    "profile_background_color": "000000",
                    "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/590922434682880000/3byPYvqe.jpg",
                    "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/590922434682880000/3byPYvqe.jpg",
                    "profile_background_tile": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/188302352/nasalogo_twitter_normal.jpg",
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/188302352/nasalogo_twitter_normal.jpg",
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/11348282/1518798395",
                    "profile_link_color": "205BA7",
                    "profile_sidebar_border_color": "000000",
                    "profile_sidebar_fill_color": "F3F2F2",
                    "profile_text_color": "000000",
                    "profile_use_background_image": true,
                    "has_extended_profile": true,
                    "default_profile": false,
                    "default_profile_image": false,
                    "following": null,
                    "follow_request_sent": null,
                    "notifications": null,
                    "translator_type": "regular"
                },
                "geo": null,
                "coordinates": null,
                "place": null,
                "contributors": null,
                "is_quote_status": false,
                "retweet_count": 2654,
                "favorite_count": 7962,
                "favorited": false,
                "retweeted": false,
                "possibly_sensitive": false,
                "lang": "en"
            },
            {
                "created_at": "Mon Feb 26 19:21:43 +0000 2018",
                "id": 968204446625869827,
                "id_str": "968204446625869827",
                "text": "Someone's got to be first. In space, the first explorers beyond Mars were Pioneers 10 and 11, twin robots who chart… https://t.co/SUX30Y45mr",
                "truncated": true,
                "entities": {
                    "hashtags": [],
                    "symbols": [],
                    "user_mentions": [],
                    "urls": [
                        {
                            "url": "https://t.co/SUX30Y45mr",
                            "expanded_url": "https://twitter.com/i/web/status/968204446625869827",
                            "display_url": "twitter.com/i/web/status/9…",
                            "indices": [
                                117,
                                140
                            ]
                        }
                    ]
                },
                "metadata": {
                    "result_type": "popular",
                    "iso_language_code": "en"
                },
                "source": "<a href='"https://www.sprinklr.com"' rel='"nofollow"'>Sprinklr</a>",
                "in_reply_to_status_id": null,
                "in_reply_to_status_id_str": null,
                "in_reply_to_user_id": null,
                "in_reply_to_user_id_str": null,
                "in_reply_to_screen_name": null,
                "user": {
                    "id": 11348282,
                    "id_str": "11348282",
                    "name": "NASA",
                    "screen_name": "NASA",
                    "location": "",
                    "description": "Explore the universe and discover our home planet with @NASA. We usually post in EST (UTC-5)",
                    "url": "https://t.co/TcEE6NS8nD",
                    "entities": {
                        "url": {
                            "urls": [
                                {
                                    "url": "https://t.co/TcEE6NS8nD",
                                    "expanded_url": "http://www.nasa.gov",
                                    "display_url": "nasa.gov",
                                    "indices": [
                                        0,
                                        23
                                    ]
                                }
                            ]
                        },
                        "description": {
                            "urls": []
                        }
                    },
                    "protected": false,
                    "followers_count": 28605561,
                    "friends_count": 270,
                    "listed_count": 90405,
                    "created_at": "Wed Dec 19 20:20:32 +0000 2007",
                    "favourites_count": 2960,
                    "utc_offset": -18000,
                    "time_zone": "Eastern Time (US & Canada)",
                    "geo_enabled": false,
                    "verified": true,
                    "statuses_count": 50713,
                    "lang": "en",
                    "contributors_enabled": false,
                    "is_translator": false,
                    "is_translation_enabled": false,
                    "profile_background_color": "000000",
                    "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/590922434682880000/3byPYvqe.jpg",
                    "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/590922434682880000/3byPYvqe.jpg",
                    "profile_background_tile": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/188302352/nasalogo_twitter_normal.jpg",
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/188302352/nasalogo_twitter_normal.jpg",
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/11348282/1518798395",
                    "profile_link_color": "205BA7",
                    "profile_sidebar_border_color": "000000",
                    "profile_sidebar_fill_color": "F3F2F2",
                    "profile_text_color": "000000",
                    "profile_use_background_image": true,
                    "has_extended_profile": true,
                    "default_profile": false,
                    "default_profile_image": false,
                    "following": null,
                    "follow_request_sent": null,
                    "notifications": null,
                    "translator_type": "regular"
                },
                "geo": null,
                "coordinates": null,
                "place": null,
                "contributors": null,
                "is_quote_status": false,
                "retweet_count": 729,
                "favorite_count": 2777,
                "favorited": false,
                "retweeted": false,
                "possibly_sensitive": false,
                "lang": "en"
            },
            {
                "created_at": "Mon Feb 26 06:42:50 +0000 2018",
                "id": 968013469743288321,
                "id_str": "968013469743288321",
                "text": "宇宙ステーションでも、日本と9時間の時差で月曜日が始まりました。n今週は6人から3人にクルーのサイズダウンがありますが、しっかりと任されているタスクをこなしたいと思います。nn写真は、NASAの実験施設「ディスティニー」のグローブ… https://t.co/2CYoPV6Aqx",
                "truncated": true,
                "entities": {
                    "hashtags": [],
                    "symbols": [],
                    "user_mentions": [],
                    "urls": [
                        {
                            "url": "https://t.co/2CYoPV6Aqx",
                            "expanded_url": "https://twitter.com/i/web/status/968013469743288321",
                            "display_url": "twitter.com/i/web/status/9…",
                            "indices": [
                                117,
                                140
                            ]
                        }
                    ]
                },
                "metadata": {
                    "result_type": "popular",
                    "iso_language_code": "ja"
                },
                "source": "<a href='"http://twitter.com"' rel='"nofollow"'>Twitter Web Client</a>",
                "in_reply_to_status_id": null,
                "in_reply_to_status_id_str": null,
                "in_reply_to_user_id": null,
                "in_reply_to_user_id_str": null,
                "in_reply_to_screen_name": null,
                "user": {
                    "id": 842625693733203968,
                    "id_str": "842625693733203968",
                    "name": "金井 宣茂",
                    "screen_name": "Astro_Kanai",
                    "location": "",
                    "description": "宇宙飛行士。2017年12月19日から国際宇宙ステーションに長期滞在中。 応援いただいているフォロワーのみなさまと一緒に、宇宙滞在を楽しみたいと思います！",
                    "url": "https://t.co/rWU6cxY9iL",
                    "entities": {
                        "url": {
                            "urls": [
                                {
                                    "url": "https://t.co/rWU6cxY9iL",
                                    "expanded_url": "https://ameblo.jp/astro-kanai/",
                                    "display_url": "ameblo.jp/astro-kanai/",
                                    "indices": [
                                        0,
                                        23
                                    ]
                                }
                            ]
                        },
                        "description": {
                            "urls": []
                        }
                    },
                    "protected": false,
                    "followers_count": 51512,
                    "friends_count": 59,
                    "listed_count": 655,
                    "created_at": "Fri Mar 17 06:36:35 +0000 2017",
                    "favourites_count": 7075,
                    "utc_offset": 32400,
                    "time_zone": "Tokyo",
                    "geo_enabled": false,
                    "verified": true,
                    "statuses_count": 1035,
                    "lang": "ja",
                    "contributors_enabled": false,
                    "is_translator": false,
                    "is_translation_enabled": false,
                    "profile_background_color": "000000",
                    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                    "profile_background_tile": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/879071738625232901/u0nlrr4Y_normal.jpg",
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/879071738625232901/u0nlrr4Y_normal.jpg",
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/842625693733203968/1492509582",
                    "profile_link_color": "E81C4F",
                    "profile_sidebar_border_color": "000000",
                    "profile_sidebar_fill_color": "000000",
                    "profile_text_color": "000000",
                    "profile_use_background_image": false,
                    "has_extended_profile": true,
                    "default_profile": false,
                    "default_profile_image": false,
                    "following": null,
                    "follow_request_sent": null,
                    "notifications": null,
                    "translator_type": "none"
                },
                "geo": null,
                "coordinates": null,
                "place": null,
                "contributors": null,
                "is_quote_status": false,
                "retweet_count": 226,
                "favorite_count": 1356,
                "favorited": false,
                "retweeted": false,
                "possibly_sensitive": false,
                "lang": "ja"
            },
            {
                "created_at": "Mon Feb 26 01:07:05 +0000 2018",
                "id": 967928974960545793,
                "id_str": "967928974960545793",
                "text": "Congratulations to #Olympics athletes who won gold! Neutron stars like the one at the heart of the Crab Nebula may… https://t.co/vz4SnPupe2",
                "truncated": true,
                "entities": {
                    "hashtags": [
                        {
                            "text": "Olympics",
                            "indices": [
                                19,
                                28
                            ]
                        }
                    ],
                    "symbols": [],
                    "user_mentions": [],
                    "urls": [
                        {
                            "url": "https://t.co/vz4SnPupe2",
                            "expanded_url": "https://twitter.com/i/web/status/967928974960545793",
                            "display_url": "twitter.com/i/web/status/9…",
                            "indices": [
                                116,
                                139
                            ]
                        }
                    ]
                },
                "metadata": {
                    "result_type": "popular",
                    "iso_language_code": "en"
                },
                "source": "<a href='"https://studio.twitter.com"' rel='"nofollow"'>Media Studio</a>",
                "in_reply_to_status_id": null,
                "in_reply_to_status_id_str": null,
                "in_reply_to_user_id": null,
                "in_reply_to_user_id_str": null,
                "in_reply_to_screen_name": null,
                "user": {
                    "id": 19802879,
                    "id_str": "19802879",
                    "name": "NASA JPL",
                    "screen_name": "NASAJPL",
                    "location": "Pasadena, Calif.",
                    "description": "NASA Jet Propulsion Laboratory manages many of NASA's robotic missions exploring Earth, the solar system and our universe. Tweets from JPL's News Office.",
                    "url": "http://t.co/gcM9d1YLUB",
                    "entities": {
                        "url": {
                            "urls": [
                                {
                                    "url": "http://t.co/gcM9d1YLUB",
                                    "expanded_url": "http://www.jpl.nasa.gov",
                                    "display_url": "jpl.nasa.gov",
                                    "indices": [
                                        0,
                                        22
                                    ]
                                }
                            ]
                        },
                        "description": {
                            "urls": []
                        }
                    },
                    "protected": false,
                    "followers_count": 2566921,
                    "friends_count": 379,
                    "listed_count": 15065,
                    "created_at": "Sat Jan 31 03:19:43 +0000 2009",
                    "favourites_count": 1281,
                    "utc_offset": -32400,
                    "time_zone": "Alaska",
                    "geo_enabled": false,
                    "verified": true,
                    "statuses_count": 6328,
                    "lang": "en",
                    "contributors_enabled": false,
                    "is_translator": false,
                    "is_translation_enabled": false,
                    "profile_background_color": "0B090B",
                    "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/8479565/twitter_jpl_bkg.009.jpg",
                    "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/8479565/twitter_jpl_bkg.009.jpg",
                    "profile_background_tile": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/2305452633/lg0hov3l8g4msxbdwv48_normal.jpeg",
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/2305452633/lg0hov3l8g4msxbdwv48_normal.jpeg",
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/19802879/1398298134",
                    "profile_link_color": "0D1787",
                    "profile_sidebar_border_color": "100F0E",
                    "profile_sidebar_fill_color": "74A6CD",
                    "profile_text_color": "0C0C0D",
                    "profile_use_background_image": true,
                    "has_extended_profile": false,
                    "default_profile": false,
                    "default_profile_image": false,
                    "following": null,
                    "follow_request_sent": null,
                    "notifications": null,
                    "translator_type": "none"
                },
                "geo": null,
                "coordinates": null,
                "place": null,
                "contributors": null,
                "is_quote_status": false,
                "retweet_count": 325,
                "favorite_count": 1280,
                "favorited": false,
                "retweeted": false,
                "possibly_sensitive": false,
                "lang": "en"
            }
        ],
        "search_metadata": {
            "completed_in": 0.057,
            "max_id": 0,
            "max_id_str": "0",
            "next_results": "?max_id=967574182522482687&q=nasa&include_entities=1&result_type=popular",
            "query": "nasa",
            "count": 3,
            "since_id": 0,
            "since_id_str": "0"
        }
    }

Please note that "count" was previously "results\_per\_page".

Overview

**Please note:**

We've recently released the following endpoints within the [Twitter API v2](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api).

| v1.1 endpoints | Corresponding v2 endpoints |     |
| --- | --- | --- |
| [GET statuses/lookup](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-statuses-lookup)   <br>[GET statuses/show/:id](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-statuses-show-id) | [Tweet lookup](https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/introduction) | [Migration guide](https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/migrate) |
| [POST statuses/update](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-update)  <br>[POST statuses/destroy/:id](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-destroy-id) | [Manage Tweets](https://developer.twitter.com/en/docs/twitter-api/tweets/manage-tweets/introduction) | [Migration guide](https://developer.twitter.com/en/docs/twitter-api/tweets/manage-tweets/migrate) |
| [GET favorites/list](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-favorites-list)  <br>[POST favorites/create](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-favorites-create)   <br>[POST favorites/destroy](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-favorites-destroy) | [Likes](https://developer.twitter.com/en/docs/twitter-api/tweets/likes/introduction) | [Migration guide](https://developer.twitter.com/en/docs/twitter-api/tweets/likes/migrate) |
| [GET statuses/retweets/:id](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-statuses-retweets-id)   <br>[GET statuses/retweeters/:ids](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-statuses-retweeters-ids)  <br>[POST statuses/retweet/:id](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-retweet-id)   <br>[POST statuses/unretweet/:id](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-unretweet-id) | [Retweets](https://developer.twitter.com/en/docs/twitter-api/tweets/retweets/introduction) | [Migration guide](https://developer.twitter.com/en/docs/twitter-api/tweets/retweets/migrate) |

Please use the migration guides to see what has changed between the standard v1.1 and v2 versions.

**Important note:**

This endpoint has been updated to include Tweet edit metadata. Learn more about these metadata on the ["Edit Tweets" fundamentals page](https://developer.twitter.com/en/docs/twitter-api/v1/edit-tweets). 

Overview
--------

The following API endpoints can be used to programmatically create, retrieve and delete Tweets, Retweets and Likes:

|     |     |     |
| --- | --- | --- |
| **Tweets** | **Retweets** | **Likes (formerly favorites)** |
| * POST statuses/update<br>* POST statuses/destroy/:id<br>* GET statuses/show/:id<br>* GET statuses/oembed<br>* GET statuses/lookup | * POST statuses/retweet/:id<br>* POST statuses/unretweet/:id<br>* GET statuses/retweets/:id<br>* GET statuses/retweets\_of\_me<br>* GET statuses/retweeters/ids | * POST favorites/create/:id<br>* POST favorites/destroy/:id<br>* GET favorites/list |

For more details, please see the individual endpoint information within the [API reference](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference) section.  
  

### Terminology

**Tweet/Status** - when a status message is shared on Twitter. Also see [Introduction to Tweet JSON](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/intro-to-tweet-json.html)

**Retweet** - when a Tweet is re-shared by another specific user. Also see [Introduction to Tweet JSON](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/intro-to-tweet-json.html)  

**Like** - when a Tweet recieves a 'heart' from a specific user, formerly known as favo(u)rite or 'star'  
  

### Rate limits

As part of our effort to reduce the distribution of spam through our APIs, we enforce App-level rate limit on some of our POST endpoints:

* There is a 300 requests per three hours shared App-level rate limit for the POST statuses/update (post a Tweet) and POST statuses/retweet/:id (post a Retweet) endpoints. This means that you can only post either 300 Tweets or Retweets across all of the authorized users of your developer App during a three hour time period. 
* There is a 1,000 requests per 24 hours App-level rate limit for the POST favorites/create/:id endpoint. This means that you can only like 1,000 Tweets across all of the authorized users of your developer App during a 24 hour time period. 

Please note that you must also consider the user-level rate limits for these endpoints, as they limit the number of posted Tweets or liked Tweets a specific authorized user can make over a given time period. 

You can review each endpoints' rate limits via their [API reference page](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference).

Tweet availability

**Tweets, Retweets, Quote Tweets**: A Twitter user can delete a status at any point in time. Deleted statuses cannot be reversed and are permanently deleted.  When the original Tweet is deleted, all Retweets are also deleted. When the original quoted Tweet is deleted, the Quote Tweet remains.

**Protected accounts**: A Twitter user can protect or unprotect their account at any time. Protected accounts require manual user approval of every person who is allowed to view their account's Tweets. For more information, see [About Public and Protected Tweets](https://help.twitter.com/en/safety-and-security/public-and-protected-tweets).

**Nullcasted Tweets**: A type of Tweet that is created through the Ads API Platform or at ads.twitter.com. Nullcasted Tweets do not appear in the public timeline and are not served to followers, but they do come through the firehose when they are created. In the case of a nullcasted Tweet, the below object will be seen in your enriched native payload. If a Tweet payload includes this object, it was created on the ads platform; however, not all promoted Tweets include this metadata.

      `"scopes": {   "followers": false }`

Post Tweet geo guide

#### **Geo-Tagging**

* Tweets can be created with geo data using the POST statuses/update method.
* Any geo-tagging parameters in an API statuses/update will be ignored if geo\_enabled for the user is false (this is the default setting for all users, unless the user has enabled geolocation in their settings).
* The number of digits after the decimal separator passed to lat (up to 8) is tracked so that when the lat is returned in a status object it will have the same number of digits after the decimal separator.
* Use a decimal point as the separator (and not a decimal comma) for the latitude and the longitude - usage of a decimal comma will cause the geo-tagged portion of the status update to be dropped.

#### **Geo Point**  

* For JSON, the response mostly uses conventions described in [GeoJSON](http://geojson.org/). However, the geo object coordinates that Twitter renders are **reversed** from the GeoJSON specification. GeoJSON specifies a longitude then a latitude, whereas Twitter represents it as a latitude then a longitude: "geo": { "type":"Point", "coordinates":\[37.78217, -122.40062\] }
* The coordinates object is replacing the geo object (no deprecation date has been set for the geo object yet) – the difference is that the coordinates object, in JSON, is now rendered correctly in GeoJSON.

#### **Place ID**

* If a place\_id is passed into the status update, then that place will be attached to the status. If no place\_id was explicitly provided, but latitude and longitude are, the API attempts to implicitly provide a place by calling [geo/reverse\_geocode](https://developer.twitter.com/en/docs/geo/places-near-location/api-reference/get-geo-reverse_geocode.html).

#### **Geo compliance**

* Users have the ability to remove all geotags from all their Tweets en masse via the user settings page. Currently there is no API method to remove geotags from individual Tweets.
* The scrub\_geo compliance object will be sent through the Compliance Firehose for the specific User's Tweets.

POST statuses/update

post-statuses-update

POST statuses/update
====================

Updates the authenticating user's current status, also known as Tweeting.

For each update attempt, the update text is compared with the authenticating user's recent Tweets. Any attempt that would result in duplication will be blocked, resulting in a 403 error. A user cannot submit the same status twice in a row.

While not rate limited by the API, a user is limited in the number of Tweets they can create at a time. If the number of updates posted by the user reaches the current allowed limit this method will return an HTTP 403 error.

**About Geo**

* Any geo-tagging parameters in the update will be ignored if `geo_enabled` for the user is false (this is the default setting for all users, unless the user has enabled geolocation in their settings)
* The number of digits after the decimal separator passed to `lat` (up to 8) is tracked so that when the `lat` is returned in a status object it will have the same number of digits after the decimal separator.
* Use a decimal point as the separator (and not a decimal comma) for the latitude and the longitude - usage of a decimal comma will cause the geo-tagged portion of the status update to be dropped.
* For JSON, the response mostly uses conventions described in [GeoJSON](http://geojson.org/). However, the `geo` object coordinates that Twitter renders are **reversed** from the GeoJSON specification. GeoJSON specifies a longitude then a latitude, whereas Twitter represents it as a latitude then a longitude: `"geo": { "type":"Point", "coordinates":[37.78217, -122.40062] }`
* The `coordinates` object is replacing the `geo` object (no deprecation date has been set for the `geo` object yet) -- the difference is that the coordinates object, in JSON, is now rendered correctly in GeoJSON.
* If a `place_id` is passed into the status update, then that place will be attached to the status. If no `place_id` was explicitly provided, but `latitude` and `longitude` are, the API attempts to implicitly provide a place by calling [geo/reverse\_geocode](https://developer.twitter.com/en/docs/geo/places-near-location/api-reference/get-geo-reverse_geocode).
* Users have the ability to remove all geotags from all their Tweets en masse via the user settings page. Currently there is no method to remove geotags from individual Tweets.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/statuses/update.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 3-hour window | 300\* per user; 300\* per app |

_Please note_ - The 300 per 3 hours is a combined limit with the [POST statuses/retweet/:id](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-statuses-retweet-id) endpoint. You can only post 300 Tweets or Retweets during a 3 hour period.

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

| Name | Required | Description | Default Value | Example |
| --- | --- | --- | --- | --- |
| status | required | The text of the status update. URL encode as necessary. [t.co link wrapping](https://developer.twitter.com/en/docs/basics/tco) will affect character counts. |     |     |
| in\_reply\_to\_status\_id | optional | The ID of an existing status that the update is in reply to. **Note:** This parameter will be ignored unless the author of the Tweet this parameter references is mentioned within the status text. Therefore, you must include `@username` , where `username` is the author of the referenced Tweet, within the update. |     |     |
| auto\_populate\_reply\_metadata | optional | If set to `true` and used with `in_reply_to_status_id`, leading `@mentions` will be looked up from the original Tweet, and added to the new Tweet from there. This wil append `@mentions` into the metadata of an extended Tweet as a reply chain grows, until the limit on `@mentions` is reached. In cases where the original Tweet has been deleted, the reply will fail. | > `false` | > `true` |
| exclude\_reply\_user\_ids | optional | When used with `auto_populate_reply_metadata`, a comma-separated list of user ids which will be removed from the server-generated `@mentions` prefix on an extended Tweet. Note that the leading `@mention` cannot be removed as it would break the `in-reply-to-status-id` semantics. Attempting to remove it will be silently ignored. |     | > `786491,54931584` |
| attachment\_url | optional | In order for a URL to not be counted in the status body of an extended Tweet, provide a URL as a Tweet attachment. This URL must be a Tweet permalink, or Direct Message deep link. Arbitrary, non-Twitter URLs must remain in the status text. URLs passed to the `attachment_url` parameter not matching either a Tweet permalink or Direct Message deep link will fail at Tweet creation and cause an exception. |     | > `https://twitter.com/andypiper/status/903615884664725505` |
| media\_ids | optional | A comma-delimited list of `media_ids` to associate with the Tweet. You may include up to 4 photos or 1 animated GIF or 1 video in a Tweet. See [Uploading Media](https://developer.twitter.com/en/docs/media/upload-media/overview) for further details on uploading media. |     | `471592142565957632` |
| possibly\_sensitive | optional | If you upload Tweet media that might be considered sensitive content such as nudity, or medical procedures, you must set this value to `true`. If this parameter is included in your request, it will override the user’s preferences. Including any value other than `true`, `1`, or `t` will be interpreted as `false`. See [Media setting and best practices](https://support.twitter.com/articles/20169200) for more context. | > If left unspecified, the value applied to the newly created Tweet is derived from the user's preferences. | `true` |
| lat | optional | The latitude of the location this Tweet refers to. This parameter will be ignored unless it is inside the range -90.0 to +90.0 (North is positive) inclusive. It will also be ignored if there is no corresponding `long` parameter. |     | `37.7821120598956` |
| long | optional | The longitude of the location this Tweet refers to. The valid ranges for longitude are -180.0 to +180.0 (East is positive) inclusive. This parameter will be ignored if outside that range, if it is not a number, if `geo_enabled` is turned off, or if there no corresponding `lat` parameter. |     | `-122.400612831116` |
| place\_id | optional | A [place](https://developer.twitter.com/en/docs/geo/place-information/overview) in the world. |     | `df51dec6f4ee2b2c` |
| display\_coordinates | optional | Whether or not to put a pin on the exact coordinates a Tweet has been sent from. |     | `true` |
| trim\_user | optional | When set to either `true` , `t` or `1` , the response will include a user object including only the author's ID. Omit this parameter to receive the complete user object. | > `false` | `true` |
| card\_uri | optional | Associate an ads card with the Tweet using the `card_uri` value from any ads card response. |     | `card://853503245793641682` |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

To obtain the generated oauth\_nonce, oauth\_token, and oauth\_signature you can use a REST tool such as Insomnia or Postman.

    curl -XPOST 
      --url 'https://api.twitter.com/1.1/statuses/update.json?status=hello' 
      --header 'authorization: OAuth
      oauth_consumer_key="oauth_customer_key",
      oauth_nonce="generated_oauth_nonce",
      oauth_signature="generated_oauth_signature",
      oauth_signature_method="HMAC-SHA1",
      oauth_timestamp="generated_timestamp",
      oauth_token="oauth_token",
      oauth_version="1.0"'

You many want to change the status from 'hello' to something different.

You can use also use any other OAuth helper library you'd like such as twurl.

    $ twurl -d 'status=Test tweet using the POST statuses/update endpoint' /1.1/statuses/update.json

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

After you post successfully you should get back something that looks like this:

    {
      "created_at": "Wed Oct 10 20:19:24 +0000 2018",
      "id": 1050118621198921700,
      "id_str": "1050118621198921728",
      "text": "To make room for more expression, we will now count all emojis as equal—including those with gender‍‍‍ ‍‍and skin t… https://t.co/MkGjXf9aXm",
      "source": "<a href="http://twitter.com" rel="nofollow">Twitter Web Client</a>",
      "truncated": true,
      "in_reply_to_status_id": null,
      "in_reply_to_status_id_str": null,
      "in_reply_to_user_id": null,
      "in_reply_to_user_id_str": null,
      "in_reply_to_screen_name": null,
      "user": {
        "id": 6253282,
        "id_str": "6253282",
        "name": "Twitter API",
        "screen_name": "TwitterAPI",
        "location": "San Francisco, CA",
        "url": "https://developer.twitter.com",
        "description": "The Real Twitter API. Tweets about API changes, service issues and our Developer Platform. Don't get an answer? It's on my website.",
        "translator_type": "null",
        "derived": {
          "locations": [
            {
              "country": "United States",
              "country_code": "US",
              "locality": "San Francisco",
              "region": "California",
              "sub_region": "San Francisco County",
              "full_name": "San Francisco, California, United States",
              "geo": {
                "coordinates": [
                  -122.41942,
                  37.77493
                ],
                "type": "point"
              }
            }
          ]
        },
        "protected": false,
        "verified": true,
        "followers_count": 6172196,
        "friends_count": 12,
        "listed_count": 13003,
        "favourites_count": 31,
        "statuses_count": 3650,
        "created_at": "Wed May 23 06:01:13 +0000 2007",
        "utc_offset": null,
        "time_zone": null,
        "geo_enabled": false,
        "lang": "en",
        "contributors_enabled": false,
        "is_translator": null,
        "profile_background_color": "null",
        "profile_background_image_url": "null",
        "profile_background_image_url_https": "null",
        "profile_background_tile": null,
        "profile_link_color": "null",
        "profile_sidebar_border_color": "null",
        "profile_sidebar_fill_color": "null",
        "profile_text_color": "null",
        "profile_use_background_image": null,
        "profile_image_url": "null",
        "profile_image_url_https": "https://pbs.twimg.com/profile_images/942858479592554497/BbazLO9L_normal.jpg",
        "profile_banner_url": "https://pbs.twimg.com/profile_banners/6253282/1497491515",
        "default_profile": false,
        "default_profile_image": false,
        "following": null,
        "follow_request_sent": null,
        "notifications": null
      },
      "geo": null,
      "coordinates": null,
      "place": null,
      "contributors": null,
      "is_quote_status": false,
      "extended_tweet": {
        "full_text": "To make room for more expression, we will now count all emojis as equal—including those with gender‍‍‍ ‍‍and skin tone modifiers 👍🏻👍🏽👍🏿. This is now reflected in Twitter-Text, our Open Source library. nnUsing Twitter-Text? See the forum post for detail: https://t.co/Nx1XZmRCXA",
        "display_text_range": [
          0,
          277
        ],
        "entities": {
          "hashtags": [],
          "urls": [
            {
              "url": "https://t.co/Nx1XZmRCXA",
              "expanded_url": "https://twittercommunity.com/t/new-update-to-the-twitter-text-library-emoji-character-count/114607",
              "display_url": "twittercommunity.com/t/new-update-t…",
              "unwound": {
                "url": "https://twittercommunity.com/t/new-update-to-the-twitter-text-library-emoji-character-count/114607",
                "status": 200,
                "title": "New update to the Twitter-Text library: Emoji character count",
                "description": "Over the years, we have made several updates to the way that people can communicate on Twitter. One of the more notable changes made last year was to increase the number of characters per Tweet from 140 to 280 characters. Today, we continue to expand people’s ability to express themselves by announcing a change to the way that we count emojis. Due to the differences in the way written text and emojis are encoded, many emojis (including emojis where you can apply gender and skin tone) have count..."
              },
              "indices": [
                254,
                277
              ]
            }
          ],
          "user_mentions": [],
          "symbols": []
        }
      },
      "quote_count": 0,
      "reply_count": 0,
      "retweet_count": 0,
      "favorite_count": 0,
      "entities": {
        "hashtags": [],
        "urls": [
          {
            "url": "https://t.co/MkGjXf9aXm",
            "expanded_url": "https://twitter.com/i/web/status/1050118621198921728",
            "display_url": "twitter.com/i/web/status/1…",
            "indices": [
              117,
              140
            ]
          }
        ],
        "user_mentions": [],
        "symbols": []
      },
      "favorited": false,
      "retweeted": false,
      "possibly_sensitive": false,
      "filter_level": "low",
      "lang": "en"
    }

POST statuses/destroy/:id

post-statuses-destroy-id

POST statuses/destroy/:id
=========================

Destroys the status specified by the required ID parameter. The authenticating user must be the author of the specified status. Returns the destroyed status if successful.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/statuses/destroy/:id.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| id  | required | The numerical ID of the desired status. |     | _123_ |
| trim\_user | optional | When set to either _true_ , _t_ or _1_ , each tweet returned in a timeline will include a user object including only the status authors numerical ID. Omit this parameter to receive the complete user object. |     | _true_ |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`POST https://api.twitter.com/1.1/statuses/destroy/240854986559455234.json`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
      "coordinates": null,
      "favorited": false,
      "created_at": "Wed Aug 29 16:54:38 +0000 2012",
      "truncated": false,
      "id_str": "240854986559455234",
      "entities": {
        "urls": [
          {
            "expanded_url": "http://venturebeat.com/2012/08/29/vimeo-dropbox/#.UD5JLsYptSs.twitter",
            "url": "http://t.co/7UlkvZzM",
            "indices": [
              69,
              89
            ],
            "display_url": "venturebeat.com/2012/08/29/vim…"
          }
        ],
        "hashtags": [
    
        ],
        "user_mentions": [
    
        ]
      },
      "in_reply_to_user_id_str": null,
      "text": ""Vimeo integrates with Dropbox for easier video uploads and shares": http://t.co/7UlkvZzM",
      "contributors": null,
      "retweet_count": 1,
      "id": 240854986559455234,
      "in_reply_to_status_id_str": null,
      "geo": null,
      "retweeted": false,
      "in_reply_to_user_id": null,
      "possibly_sensitive": false,
      "place": null,
      "user": {
        "name": "Jason Costa",
        "profile_sidebar_border_color": "86A4A6",
        "profile_sidebar_fill_color": "A0C5C7",
        "profile_background_tile": false,
        "profile_image_url": "http://a0.twimg.com/profile_images/1751674923/new_york_beard_normal.jpg",
        "created_at": "Wed May 28 00:20:15 +0000 2008",
        "location": "",
        "is_translator": true,
        "follow_request_sent": false,
        "id_str": "14927800",
        "profile_link_color": "FF3300",
        "entities": {
          "url": {
            "urls": [
              {
                "expanded_url": "http://www.jason-costa.blogspot.com/",
                "url": "http://t.co/YCA3ZKY",
                "indices": [
                  0,
                  19
                ],
                "display_url": "jason-costa.blogspot.com"
              }
            ]
          },
          "description": {
            "urls": [
    
            ]
          }
        },
        "default_profile": false,
        "contributors_enabled": false,
        "url": "http://t.co/YCA3ZKY",
        "favourites_count": 883,
        "utc_offset": -28800,
        "id": 14927800,
        "profile_image_url_https": "https://si0.twimg.com/profile_images/1751674923/new_york_beard_normal.jpg",
        "profile_use_background_image": true,
        "listed_count": 150,
        "profile_text_color": "333333",
        "protected": false,
        "lang": "en",
        "followers_count": 8760,
        "time_zone": "Pacific Time (US & Canada)",
        "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme6/bg.gif",
        "verified": false,
        "profile_background_color": "709397",
        "notifications": false,
        "description": "Platform at Twitter",
        "geo_enabled": true,
        "statuses_count": 5531,
        "default_profile_image": false,
        "friends_count": 166,
        "profile_background_image_url": "http://a0.twimg.com/images/themes/theme6/bg.gif",
        "show_all_inline_media": true,
        "screen_name": "jasoncosta",
        "following": false
      },
      "possibly_sensitive_editable": true,
      "source": "Tweet Button",
      "in_reply_to_screen_name": null,
      "in_reply_to_status_id": null
    }

GET statuses/show/:id

get-statuses-show-id

GET statuses/show/:id
=====================

Returns a single [Tweet](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object), specified by the id parameter. The Tweet's author will also be embedded within the Tweet.

See [GET statuses / lookup](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/get-statuses-lookup) for getting Tweets in bulk (up to 100 per call). See also [Embedded Timelines](https://developer.twitter.com/web/embedded-timelines), [Embedded Tweets](https://developer.twitter.com/web/embedded-tweets), and [GET statuses/oembed](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/get-statuses-oembed) for tools to render Tweets according to [Display Requirements](https://about.twitter.com/company/display-requirements).

**About Geo**

If there is no geotag for a status, then there will be an empty `<geo></geo>` or `"geo" : {}`. This can only be populated if the user has used the Geotagging API to send a statuses/update.

The JSON response mostly uses conventions laid out in GeoJSON. The coordinates that Twitter renders are _reversed_ from the GeoJSON specification (GeoJSON specifies a longitude then a latitude, whereas Twitter represents it as a latitude then a longitude), eg: `"geo": { "type":"Point", "coordinates":[37.78029, -122.39697] }`

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/statuses/show.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 900 |
| Requests / 15-min window (app auth) | 900 |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| id  | required | The numerical ID of the desired Tweet. |     | _123_ |
| trim\_user | optional | When set to either _true_ , _t_ or _1_ , each Tweet returned in a timeline will include a user object including only the status authors numerical ID. Omit this parameter to receive the complete user object. |     | _true_ |
| include\_my\_retweet | optional | When set to either _true_ , _t_ or _1_ , any Tweets returned that have been retweeted by the authenticating user will include an additional _current\_user\_retweet_ node, containing the ID of the source status for the retweet. |     | _true_ |
| include\_entities | optional | The _entities_ node will not be included when set to _false_. |     | _false_ |
| include\_ext\_alt\_text | optional | If alt text has been added to any attached media entities, this parameter will return an _ext\_alt\_text_ value in the top-level key for the media entity. If no value has been set, this will be returned as `null` |     | _true_ |
| include\_card\_uri | optional | When set to either _true_ , _t_ or _1_ , the retrieved Tweet will include a _card\_uri_ attribute when there is an ads card attached to the Tweet and when that card was attached using the _card\_uri_ value. |     | _true_ |
| include\_ext\_edit\_control | optional | Must be set to true in order to return edited Tweet metadata as part of the Tweet object.<br><br>`include_ext_edit_control=true`<br><br>Note that historical Tweets may not contain edited Tweet metadata. |     | _true_ |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`GET https://api.twitter.com/1.1/statuses/show.json?id=210462857140252672`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
      "created_at": "Wed Oct 10 20:19:24 +0000 2018",
      "id": 1050118621198921728,
      "id_str": "1050118621198921728",
      "text": "To make room for more expression, we will now count all emojis as equal—including those with gender‍‍‍ and skin t… https://t.co/MkGjXf9aXm",
      "truncated": true,
      "entities": {
        "hashtags": [],
        "symbols": [],
        "user_mentions": [],
        "urls": [
          {
            "url": "https://t.co/MkGjXf9aXm",
            "expanded_url": "https://twitter.com/i/web/status/1050118621198921728",
            "display_url": "twitter.com/i/web/status/1…",
            "indices": [
              117,
              140
            ]
          }
        ]
      },
      "source": "<a href="http://twitter.com" rel="nofollow">Twitter Web Client</a>",
      "in_reply_to_status_id": null,
      "in_reply_to_status_id_str": null,
      "in_reply_to_user_id": null,
      "in_reply_to_user_id_str": null,
      "in_reply_to_screen_name": null,
      "user": {
        "id": 6253282,
        "id_str": "6253282",
        "name": "Twitter API",
        "screen_name": "TwitterAPI",
        "location": "San Francisco, CA",
        "description": "The Real Twitter API. Tweets about API changes, service issues and our Developer Platform. Don't get an answer? It's on my website.",
        "url": "https://t.co/8IkCzCDr19",
        "entities": {
          "url": {
            "urls": [
              {
                "url": "https://t.co/8IkCzCDr19",
                "expanded_url": "https://developer.twitter.com",
                "display_url": "developer.twitter.com",
                "indices": [
                  0,
                  23
                ]
              }
            ]
          },
          "description": {
            "urls": []
          }
        },
        "protected": false,
        "followers_count": 6128663,
        "friends_count": 12,
        "listed_count": 12900,
        "created_at": "Wed May 23 06:01:13 +0000 2007",
        "favourites_count": 32,
        "utc_offset": null,
        "time_zone": null,
        "geo_enabled": null,
        "verified": true,
        "statuses_count": 3659,
        "lang": "null",
        "contributors_enabled": null,
        "is_translator": null,
        "is_translation_enabled": null,
        "profile_background_color": "null",
        "profile_background_image_url": "null",
        "profile_background_image_url_https": "null",
        "profile_background_tile": nulll,
        "profile_image_url": "null",
        "profile_image_url_https": "https://pbs.twimg.com/profile_images/942858479592554497/BbazLO9L_normal.jpg",
        "profile_banner_url": "https://pbs.twimg.com/profile_banners/6253282/1497491515",
        "profile_link_color": "null",
        "profile_sidebar_border_color": "null",
        "profile_sidebar_fill_color": "null",
        "profile_text_color": "null",
        "profile_use_background_image": null,
        "has_extended_profile": null,
        "default_profile": false,
        "default_profile_image": false,
        "following": nul,
        "follow_request_sent": null,
        "notifications": null,
        "translator_type": "null"
      },
      "geo": null,
      "coordinates": null,
      "place": null,
      "contributors": null,
      "is_quote_status": false,
      "retweet_count": 161,
      "favorite_count": 296,
      "favorited": false,
      "retweeted": false,
      "possibly_sensitive": false,
      "possibly_sensitive_appealable": false,
      "lang": "en"
    }

This request could also be obtained with: `GET https://api.twitter.com/1.1/statuses/show/210462857140252672.json`

GET statuses/oembed

get-statuses-oembed

GET statuses/oembed
===================

Returns a single Tweet, specified by either a Tweet web URL or the Tweet ID, in an [oEmbed](http://oembed.com/)\-compatible format. The returned HTML snippet will be automatically recognized as an [Embedded Tweet](https://developer.twitter.com/web/embedded-tweets) when [Twitter's widget JavaScript is included on the page](https://developer.twitter.com/web/javascript/loading).

The oEmbed endpoint allows customization of the final appearance of an Embedded Tweet by setting the corresponding properties in HTML markup to be interpreted by Twitter's JavaScript bundled with the HTML response by default. The format of the returned markup may change over time as Twitter adds new features or adjusts its Tweet representation.

The Tweet fallback markup is meant to be cached on your servers for up to the suggested cache lifetime specified in the `cache_age`.

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| **Resource URL** | `https://publish.twitter.com/oembed` |
| **Response formats** | JSON |
| **Requires authentication?** | No  |
| **Rate limited?** | No  |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

| Name | Default | Description |
| --- | --- | --- |
| `url`required  <br>String |     | The URL of the Tweet to be embedded |
| `maxwidth`  <br>Int `[220..550]` | `325` | The maximum width of a rendered Tweet in whole pixels. A supplied value under or over the allowed range will be returned as the minimum or maximum supported width respectively; the reset width value will be reflected in the returned `width` property. Note that Twitter does not support the oEmbed `maxheight` parameter. Tweets are fundamentally text, and are therefore of unpredictable height that cannot be scaled like an image or video. Relatedly, the oEmbed response will not provide a value for `height`. Implementations that need consistent heights for Tweets should refer to the `hide_thread` and `hide_media` parameters below. |
| `hide_media`  <br>Boolean, String or Int | `false` | When set to `true`, `"t"`, or `1` links in a Tweet are not expanded to photo, video, or link previews. |
| `hide_thread`  <br>Boolean, String or Int | `false` | When set to `true`, `"t"`, or `1` a collapsed version of the previous Tweet in a conversation thread will not be displayed when the requested Tweet is in reply to another Tweet. |
| `omit_script`  <br>Boolean, String or Int | `false` | When set to `true`, `"t"`, or `1` the `<script>` responsible for loading `widgets.js` will not be returned. Your webpages should include their own reference to `widgets.js` for use across all Twitter widgets including [Embedded Tweets](https://developer.twitter.com/web/embedded-tweets). |
| `align`  <br>Enum `{left,right,center,none}` | `none` | Specifies whether the embedded Tweet should be floated left, right, or center in the page relative to the parent element. |
| `related`  <br>String |     | A comma-separated list of Twitter usernames related to your content. This value will be forwarded to [Tweet action intents](https://developer.twitter.com/web/intents) if a viewer chooses to reply, like, or retweet the embedded Tweet. |
| `lang`  <br>Enum([Language](https://developer.twitter.com/en/docs/twitter-for-websites/twitter-for-websites-supported-languages/overview)) | `en` | Request returned HTML and a rendered Tweet in the specified [Twitter language supported by embedded Tweets](https://developer.twitter.com/web/overview/languages). |
| `theme`  <br>Enum `{light, dark}` | `light` | When set to `dark`, the Tweet is displayed with light text over a dark background. |
| `link_color`  <br>String |     | Adjust the color of Tweet text links with a [hexadecimal color value](https://en.wikipedia.org/wiki/Web_colors#Hex_triplet). |
| `widget_type`  <br>Enum `{video}` |     | Set to `video` to return a Twitter Video embed for the given Tweet. |
| `dnt`  <br>Boolean | `false` | When set to `true`, the Tweet and its embedded page on your site are not used for purposes that include [personalized suggestions](https://support.twitter.com/articles/20169421) and [personalized ads](https://support.twitter.com/articles/20170405). |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

    curl 'https://publish.twitter.com/oembed?url=https%3A%2F%2Ftwitter.com%2FInterior%2Fstatus%2F507185938620219395'

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
      "url": "https://twitter.com/Interior/status/507185938620219395",
      "author_name": "US Dept of Interior",
      "author_url": "https://twitter.com/Interior",
      "html": "<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Happy 50th anniversary to the Wilderness Act! Here&#39;s a great wilderness photo from <a href="https://twitter.com/YosemiteNPS">@YosemiteNPS</a>. <a href="https://twitter.com/hashtag/Wilderness50?src=hash">#Wilderness50</a> <a href="http://t.co/HMhbyTg18X">pic.twitter.com/HMhbyTg18X</a></p>&mdash; US Dept of Interior (@Interior) <a href="https://twitter.com/Interior/status/507185938620219395">September 3, 2014</a></blockquote>n<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>",
      "width": 550,
      "height": null,
      "type": "rich",
      "cache_age": "3153600000",
      "provider_name": "Twitter",
      "provider_url": "https://twitter.com",
      "version": "1.0"
    }

GET statuses/lookup

get-statuses-lookup

GET statuses/lookup
===================

Returns fully-hydrated [Tweet objects](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object) for up to 100 Tweets per request, as specified by comma-separated values passed to the `id` parameter.

This method is especially useful to get the details (hydrate) a collection of Tweet IDs.

[GET statuses / show / :id](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/get-statuses-show-id) is used to retrieve a single Tweet object.

There are a few things to note when using this method.

* You must be following a protected user to be able to see their most recent Tweets. If you don't follow a protected user their status will be removed.
* The order of Tweet IDs may not match the order of Tweets in the returned array.
* If a requested Tweet is unknown or deleted, then that Tweet will not be returned in the results list, unless the `map` parameter is set to `true`, in which case it will be returned with a value of `null`.
* If none of your lookup criteria matches valid Tweet IDs an empty array will be returned for `map=false`.
* You are strongly encouraged to use a POST for larger requests.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/statuses/lookup.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 900 |
| Requests / 15-min window (app auth) | 300 |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| id  | required | A comma separated list of Tweet IDs, up to 100 are allowed in a single request. |     | _20_ _1050118621198921728_ |
| include\_entities | optional | The _entities_ node that may appear within embedded statuses will not be included when set to _false_. |     | _false_ |
| trim\_user | optional | When set to either _true_ , _t_ or _1_ , each Tweet returned in a timeline will include a user object including only the status authors numerical ID. Omit this parameter to receive the complete user object. |     | _true_ |
| map | optional | When using the _map_ parameter, Tweets that do not exist or cannot be viewed by the current user will still have their key represented but with an explicitly _null_ value paired with it |     | _true_ |
| include\_ext\_alt\_text | optional | If alt text has been added to any attached media entities, this parameter will return an _ext\_alt\_text_ value in the top-level key for the media entity. If no value has been set, this will be returned as `null` |     | _true_ |
| include\_card\_uri | optional | When set to either _true_ , _t_ or _1_ , each Tweet returned will include a _card\_uri_ attribute when there is an ads card attached to the Tweet and when that card was attached using the _card\_uri_ value. |     | _true_ |
| include\_ext\_edit\_control | optional | Must be set to true in order to return edited Tweet metadata as part of the Tweet object.<br><br>`include_ext_edit_control=true`<br><br>Note that historical Tweets may not contain edited Tweet metadata. |     | _true_ |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`GET https://api.twitter.com/1.1/statuses/lookup.json?id=20,1050118621198921728`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    [
      {
        "created_at": "Tue Mar 21 20:50:14 +0000 2006",
        "id": 20,
        "id_str": "20",
        "text": "just setting up my twttr",
        "truncated": false,
        "entities": {
          "hashtags": [],
          "symbols": [],
          "user_mentions": [],
          "urls": []
        },
        "source": "<a href="http://twitter.com" rel="nofollow">Twitter Web Client</a>",
        "in_reply_to_status_id": null,
        "in_reply_to_status_id_str": null,
        "in_reply_to_user_id": null,
        "in_reply_to_user_id_str": null,
        "in_reply_to_screen_name": null,
        "user": {
          "id": 12,
          "id_str": "12",
          "name": "jack",
          "screen_name": "jack",
          "location": "",
          "description": "",
          "url": null,
          "entities": {
            "description": {
              "urls": []
            }
          },
          "protected": false,
          "followers_count": 4183755,
          "friends_count": 3894,
          "listed_count": 28137,
          "created_at": "Tue Mar 21 20:50:14 +0000 2006",
          "favourites_count": 23361,
          "utc_offset": null,
          "time_zone": null,
          "geo_enabled": null,
          "verified": true,
          "statuses_count": 25783,
          "lang": "null",
          "contributors_enabled": null,
          "is_translator": null,
          "is_translation_enabled": null,
          "profile_background_color": "null",
          "profile_background_image_url": "null",
          "profile_background_image_url_https": "null",
          "profile_background_tile": null,
          "profile_image_url": "null",
          "profile_image_url_https": "https://pbs.twimg.com/profile_images/1115644092329758721/AFjOr-K8_normal.jpg",
          "profile_banner_url": "null",
          "profile_link_color": "null",
          "profile_sidebar_border_color": "null",
          "profile_sidebar_fill_color": "null",
          "profile_text_color": "null",
          "profile_use_background_image": null,
          "has_extended_profile": null,
          "default_profile": false,
          "default_profile_image": false,
          "following": null,
          "follow_request_sent": null,
          "notifications": null,
          "translator_type": "null"
        },
        "geo": null,
        "coordinates": null,
        "place": null,
        "contributors": null,
        "is_quote_status": false,
        "retweet_count": 111160,
        "favorite_count": 98090,
        "favorited": false,
        "retweeted": false,
        "lang": "en"
      },
    {
      "created_at": "Wed Oct 10 20:19:24 +0000 2018",
      "id": 1050118621198921728,
      "id_str": "1050118621198921728",
      "text": "To make room for more expression, we will now count all emojis as equal—including those with gender‍‍‍ and skin t… https://t.co/MkGjXf9aXm",
      "truncated": true,
      "entities": {
        "hashtags": [],
        "symbols": [],
        "user_mentions": [],
        "urls": [
          {
            "url": "https://t.co/MkGjXf9aXm",
            "expanded_url": "https://twitter.com/i/web/status/1050118621198921728",
            "display_url": "twitter.com/i/web/status/1…",
            "indices": [
              117,
              140
            ]
          }
        ]
      },
      "source": "<a href="http://twitter.com" rel="nofollow">Twitter Web Client</a>",
      "in_reply_to_status_id": null,
      "in_reply_to_status_id_str": null,
      "in_reply_to_user_id": null,
      "in_reply_to_user_id_str": null,
      "in_reply_to_screen_name": null,
      "user": {
        "id": 6253282,
        "id_str": "6253282",
        "name": "Twitter API",
        "screen_name": "TwitterAPI",
        "location": "San Francisco, CA",
        "description": "The Real Twitter API. Tweets about API changes, service issues and our Developer Platform. Don't get an answer? It's on my website.",
        "url": "https://t.co/8IkCzCDr19",
        "entities": {
          "url": {
            "urls": [
              {
                "url": "https://t.co/8IkCzCDr19",
                "expanded_url": "https://developer.twitter.com",
                "display_url": "developer.twitter.com",
                "indices": [
                  0,
                  23
                ]
              }
            ]
          },
          "description": {
            "urls": []
          }
        },
        "protected": false,
        "followers_count": 6128663,
        "friends_count": 12,
        "listed_count": 12900,
        "created_at": "Wed May 23 06:01:13 +0000 2007",
        "favourites_count": 32,
        "utc_offset": null,
        "time_zone": null,
        "geo_enabled": null,
        "verified": true,
        "statuses_count": 3659,
        "lang": "null",
        "contributors_enabled": null,
        "is_translator": null,
        "is_translation_enabled": null,
        "profile_background_color": "null",
        "profile_background_image_url": "null",
        "profile_background_image_url_https": "null",
        "profile_background_tile": nulll,
        "profile_image_url": "null",
        "profile_image_url_https": "https://pbs.twimg.com/profile_images/942858479592554497/BbazLO9L_normal.jpg",
        "profile_banner_url": "https://pbs.twimg.com/profile_banners/6253282/1497491515",
        "profile_link_color": "null",
        "profile_sidebar_border_color": "null",
        "profile_sidebar_fill_color": "null",
        "profile_text_color": "null",
        "profile_use_background_image": null,
        "has_extended_profile": null,
        "default_profile": false,
        "default_profile_image": false,
        "following": nul,
        "follow_request_sent": null,
        "notifications": null,
        "translator_type": "null"
      },
      "geo": null,
      "coordinates": null,
      "place": null,
      "contributors": null,
      "is_quote_status": false,
      "retweet_count": 161,
      "favorite_count": 296,
      "favorited": false,
      "retweeted": false,
      "possibly_sensitive": false,
      "possibly_sensitive_appealable": false,
      "lang": "en"
    }
      ]

POST statuses/retweet/:id

post-statuses-retweet-id

POST statuses/retweet/:id
=========================

Retweets a tweet. Returns the original Tweet with Retweet details embedded.

_Usage Notes_:

* This method is subject to update limits. A HTTP 403 will be returned if this limit as been hit.
* Twitter will ignore attempts to perform duplicate retweets.
* The retweet\_count will be current as of when the payload is generated and may not reflect the exact count. It is intended as an approximation.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/statuses/retweet/:id.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 3-hour window | 300\* per user; 300\* per app |

_Please note_ - The 300 per 3 hours is a combined limit with the [POST statuses/update](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-statuses-update) endpoint. You can only post 300 Tweets or Retweets during a 3 hour period.

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| id  | required | The numerical ID of the desired status. |     | _123_ |
| trim\_user | optional | When set to either _true_ , _t_ or _1_ , each tweet returned in a timeline will include a user object including only the status authors numerical ID. Omit this parameter to receive the complete user object. |     | _true_ |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

    $ curl --request POST 
    --url 'https://api.twitter.com/1.1/statuses/retweet/TWEET_ID.json' 
    --header 'authorization: OAuth oauth_consumer_key="YOUR_CONSUMER_KEY", oauth_nonce="AUTO_GENERATED_NONCE", oauth_signature="AUTO_GENERATED_SIGNATURE", oauth_signature_method="HMAC-SHA1", oauth_timestamp="AUTO_GENERATED_TIMESTAMP", oauth_token="USERS_ACCESS_TOKEN", oauth_version="1.0"' 
    --header 'content-type: application/json'

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {retweet-status-object,
    "user": {retweeting-user-object},
    "retweeted_status": {retweeted-status-object,
      "user": {retweeted-user-object}
    }
    }

POST statuses/unretweet/:id

post-statuses-unretweet-id

POST statuses/unretweet/:id
===========================

Untweets a retweeted status. Returns the original Tweet with Retweet details embedded.

**Usage Notes**:

* This method is subject to update limits. A HTTP 429 will be returned if this limit has been hit.
* The untweeted retweet status ID must be authored by the user backing the authentication token.
* An application must have write privileges to POST. A HTTP 401 will be returned for read-only applications.
* When passing a source status ID instead of the retweet status ID a HTTP 200 response will be returned with the same Tweet object but no action.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/statuses/unretweet/:id.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| id  | required | The numerical ID of the desired status. |     | _123_ |
| trim\_user | optional | When set to either _true_ , _t_ or _1_ , each Tweet returned in a timeline will include a user object including only the status authors numerical ID. Omit this parameter to receive the complete user object. |     | _true_ |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`POST https://api.twitter.com/1.1/statuses/unretweet/1050118621198921728.json`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
      "created_at": "Wed Oct 10 20:19:24 +0000 2018",
      "id": 1050118621198921728,
      "id_str": "1050118621198921728",
      "text": "To make room for more expression, we will now count all emojis as equal—including those with gender‍‍‍ and skin t… https://t.co/MkGjXf9aXm",
      "truncated": true,
      "entities": {
        "hashtags": [],
        "symbols": [],
        "user_mentions": [],
        "urls": [
          {
            "url": "https://t.co/MkGjXf9aXm",
            "expanded_url": "https://twitter.com/i/web/status/1050118621198921728",
            "display_url": "twitter.com/i/web/status/1…",
            "indices": [
              117,
              140
            ]
          }
        ]
      },
      "source": "<a href="http://twitter.com" rel="nofollow">Twitter Web Client</a>",
      "in_reply_to_status_id": null,
      "in_reply_to_status_id_str": null,
      "in_reply_to_user_id": null,
      "in_reply_to_user_id_str": null,
      "in_reply_to_screen_name": null,
      "user": {
        "id": 6253282,
        "id_str": "6253282",
        "name": "Twitter API",
        "screen_name": "TwitterAPI",
        "location": "San Francisco, CA",
        "description": "The Real Twitter API. Tweets about API changes, service issues and our Developer Platform. Don't get an answer? It's on my website.",
        "url": "https://t.co/8IkCzCDr19",
        "entities": {
          "url": {
            "urls": [
              {
                "url": "https://t.co/8IkCzCDr19",
                "expanded_url": "https://developer.twitter.com",
                "display_url": "developer.twitter.com",
                "indices": [
                  0,
                  23
                ]
              }
            ]
          },
          "description": {
            "urls": []
          }
        },
        "protected": false,
        "followers_count": 6128663,
        "friends_count": 12,
        "listed_count": 12900,
        "created_at": "Wed May 23 06:01:13 +0000 2007",
        "favourites_count": 32,
        "utc_offset": null,
        "time_zone": null,
        "geo_enabled": null,
        "verified": true,
        "statuses_count": 3659,
        "lang": "null",
        "contributors_enabled": null,
        "is_translator": null,
        "is_translation_enabled": null,
        "profile_background_color": "null",
        "profile_background_image_url": "null",
        "profile_background_image_url_https": "null",
        "profile_background_tile": nulll,
        "profile_image_url": "null",
        "profile_image_url_https": "https://pbs.twimg.com/profile_images/942858479592554497/BbazLO9L_normal.jpg",
        "profile_banner_url": "https://pbs.twimg.com/profile_banners/6253282/1497491515",
        "profile_link_color": "null",
        "profile_sidebar_border_color": "null",
        "profile_sidebar_fill_color": "null",
        "profile_text_color": "null",
        "profile_use_background_image": null,
        "has_extended_profile": null,
        "default_profile": false,
        "default_profile_image": false,
        "following": nul,
        "follow_request_sent": null,
        "notifications": null,
        "translator_type": "null"
      },
      "geo": null,
      "coordinates": null,
      "place": null,
      "contributors": null,
      "is_quote_status": false,
      "retweet_count": 161,
      "favorite_count": 296,
      "favorited": false,
      "retweeted": false,
      "possibly_sensitive": false,
      "possibly_sensitive_appealable": false,
      "lang": "en"
    }

GET statuses/retweets/:id

get-statuses-retweets-id

GET statuses/retweets/:id
=========================

Returns a collection of the 100 most recent retweets of the Tweet specified by the `id` parameter.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/statuses/retweets/:id.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 75  |
| Requests / 15-min window (app auth) | 300 |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| id  | required | The numerical ID of the desired status. |     | _123_ |
| count | optional | Specifies the number of records to retrieve. Must be less than or equal to 100. |     | _5_ |
| trim\_user | optional | When set to either _true_ , _t_ or _1_ , each tweet returned in a timeline will include a user object including only the status authors numerical ID. Omit this parameter to receive the complete user object. |     | _true_ |
| include\_ext\_edit\_control | optional | Must be set to true in order to return edited Tweet metadata as part of the Tweet object.<br><br>`include_ext_edit_control=true`<br><br>Note that historical Tweets may not contain edited Tweet metadata. |     | _true_ |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`GET https://api.twitter.com/1.1/statuses/retweets/1128692733353218048.json`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    [
      {
        "created_at": "Wed May 15 16:04:52 +0000 2019",
        "id": 1128692733353218048,
        "id_str": "1128692733353218048",
        "text": "RT @jack: just setting up my twttr",
        "truncated": false,
        "entities": {
          "hashtags": [],
          "symbols": [],
          "user_mentions": [
            {
              "screen_name": "jack",
              "name": "jack",
              "id": 12,
              "id_str": "12",
              "indices": [
                3,
                8
              ]
            }
          ],
          "urls": []
        },
        "source": "<a href="https://mobile.twitter.com" rel="nofollow">Twitter Web App</a>",
        "in_reply_to_status_id": null,
        "in_reply_to_status_id_str": null,
        "in_reply_to_user_id": null,
        "in_reply_to_user_id_str": null,
        "in_reply_to_screen_name": null,
        "user": {
          "id": 6253282,
          "id_str": "6253282",
          "name": "Twitter API",
          "screen_name": "TwitterAPI",
          "location": "San Francisco, CA",
          "description": "The Real Twitter API. Tweets about API changes, service issues and our Developer Platform. Don't get an answer? It's on my website.",
          "url": "https://t.co/8IkCzCDr19",
          "entities": {
            "url": {
              "urls": [
                {
                  "url": "https://t.co/8IkCzCDr19",
                  "expanded_url": "https://developer.twitter.com",
                  "display_url": "developer.twitter.com",
                  "indices": [
                    0,
                    23
                  ]
                }
              ]
            },
            "description": {
              "urls": []
            }
          },
          "protected": false,
          "followers_count": 6128663,
          "friends_count": 12,
          "listed_count": 12900,
          "created_at": "Wed May 23 06:01:13 +0000 2007",
          "favourites_count": 32,
          "utc_offset": null,
          "time_zone": null,
          "geo_enabled": null,
          "verified": true,
          "statuses_count": 3659,
          "lang": "null",
          "contributors_enabled": null,
          "is_translator": null,
          "is_translation_enabled": null,
          "profile_background_color": "null",
          "profile_background_image_url": "null",
          "profile_background_image_url_https": "null",
          "profile_background_tile": nulll,
          "profile_image_url": "null",
          "profile_image_url_https": "https://pbs.twimg.com/profile_images/942858479592554497/BbazLO9L_normal.jpg",
          "profile_banner_url": "https://pbs.twimg.com/profile_banners/6253282/1497491515",
          "profile_link_color": "null",
          "profile_sidebar_border_color": "null",
          "profile_sidebar_fill_color": "null",
          "profile_text_color": "null",
          "profile_use_background_image": null,
          "has_extended_profile": null,
          "default_profile": false,
          "default_profile_image": false,
          "following": null,
          "follow_request_sent": null,
          "notifications": null,
          "translator_type": "null"
        },
        "geo": null,
        "coordinates": null,
        "place": null,
        "contributors": null,
        "is_quote_status": false,
        "retweet_count": 161,
        "favorite_count": 296,
        "favorited": false,
        "retweeted": false,
        "possibly_sensitive": false,
        "possibly_sensitive_appealable": false,
        "lang": "en"
      }
    ]

GET statuses/retweets\_of\_me

get-statuses-retweets\_of\_me

GET statuses/retweets\_of\_me
=============================

Returns the most recent Tweets authored by the authenticating user that have been retweeted by others. This timeline is a subset of the user's [GET statuses / user\_timeline](https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline).

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/statuses/retweets_of_me.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 75  |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| count | optional | Specifies the number of records to retrieve. Must be less than or equal to 100. If omitted, 20 will be assumed. |     | _5_ |
| since\_id | optional | Returns results with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets which can be accessed through the API. If the limit of Tweets has occured since the since\_id, the since\_id will be forced to the oldest ID available. |     | _12345_ |
| max\_id | optional | Returns results with an ID less than (that is, older than) or equal to the specified ID. |     | _54321_ |
| trim\_user | optional | When set to either _true_ , _t_ or _1_ , each tweet returned in a timeline will include a user object including only the status authors numerical ID. Omit this parameter to receive the complete user object. |     | _true_ |
| include\_entities | optional | The tweet _entities_ node will not be included when set to _false_ . |     | _false_ |
| include\_user\_entities | optional | The user _entities_ node will not be included when set to _false_ . |     | _false_ |
| include\_ext\_edit\_control | optional | Must be set to true in order to return edited Tweet metadata as part of the Tweet object.<br><br>`include_ext_edit_control=true`<br><br>Note that historical Tweets may not contain edited Tweet metadata. |     | _true_ |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`GET https://api.twitter.com/1.1/statuses/retweets_of_me.json?count=50&since_id=259320959964680190&max_id=259320959964680500`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    [
      {
        "created_at": "Thu Nov 29 17:13:16 +0000 2018",
        "id": 1068191175616720896,
        "id_str": "1068191175616720896",
        "text": "@TwitterDev is the source of Twitter Developer news",
        "truncated": false,
        "entities": {
          "hashtags": [],
          "symbols": [],
          "user_mentions": [
            {
              "screen_name": "twitterdev",
              "name": "twitterdev",
              "id": 2244994945,
              "id_str": "2244994945",
              "indices": [
                0,
                10
              ]
            }
          ],
          "urls": []
        },
      "source": "<a href="http://twitter.com" rel="nofollow">Twitter Web Client</a>",
        "in_reply_to_status_id": null,
        "in_reply_to_status_id_str": null,
        "in_reply_to_user_id": 2244994945,
        "in_reply_to_user_id_str": "2244994945",
        "in_reply_to_screen_name": "twitterdev",
        "user": {
          "id": 10183220897015316771,
          "id_str": "10183220897015316771",
          "name": "test account",
          "screen_name": "testuser",
          "location": "USA",
          "description": "",
          "url": null,
          "entities": {
            "description": {
              "urls": []
            }
          },
          "protected": false,
          "followers_count": 3,
          "friends_count": 11,
          "listed_count": 0,
          "created_at": "Sun May 15 02:31:20 +0000 2019",
          "favourites_count": 33,
          "utc_offset": null,
          "time_zone": null,
          "geo_enabled": null,
          "verified": false,
          "statuses_count": 164,
          "lang": "null",
          "contributors_enabled": null,
          "is_translator": null,
          "is_translation_enabled": null,
          "profile_background_color": "null",
          "profile_background_image_url": null,
          "profile_background_image_url_https": null,
          "profile_background_tile": null,
          "profile_image_url": "null",
          "profile_image_url_https": "https://pbs.twimg.com/profile_images/1099410185435734016/G0hE-4u9_normal.jpg",
          "profile_banner_url": "https://pbs.twimg.com/profile_banners/1018322089701531651/1539492123",
          "profile_link_color": "null",
          "profile_sidebar_border_color": "null",
          "profile_sidebar_fill_color": "null",
          "profile_text_color": "null",
          "profile_use_background_image": null,
          "has_extended_profile": null,
          "default_profile": true,
          "default_profile_image": false,
          "following": null,
          "follow_request_sent": null,
          "notifications": null,
          "translator_type": "null"
        },
        "geo": null,
        "coordinates": null,
        "place": null,
        "contributors": null,
        "is_quote_status": false,
        "retweet_count": 1,
        "favorite_count": 1,
        "favorited": true,
        "retweeted": true,
        "lang": "en"
      }
    ]

GET statuses/retweeters/ids

get-statuses-retweeters-ids

GET statuses/retweeters/ids
===========================

Returns a collection of up to 100 user IDs belonging to users who have retweeted the Tweet specified by the `id` parameter.

This method offers similar data to [GET statuses / retweets / :id](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/get-statuses-retweets-id).

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/statuses/retweeters/ids.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 75  |
| Requests / 15-min window (app auth) | 300 |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

| Name | Required | Description | Default Value | Example |
| --- | --- | --- | --- | --- |
| id  | required | The numerical ID of the desired status. |     | `327473909412814850` |
| count | optional | Specifies the number of records to retrieve. Must be less than or equal to 100. |     | `5` |
| cursor | semi-optional | Causes the list of IDs to be broken into pages of no more than 100 IDs at a time. The number of IDs returned is not guaranteed to be 100 as suspended users are filtered out after connections are queried. If no cursor is provided, a value of `-1` will be assumed, which is the first "page."<br><br>The response from the API will include a `previous_cursor` and `next_cursor` to allow paging back and forth. See [our cursor docs](https://developer.twitter.com/en/docs/basics/cursoring) for more information.<br><br>While this method supports the cursor parameter, the entire result set can be returned in a single cursored collection. Using the `count` parameter with this method will not provide segmented cursors for use with this parameter. |     | `12893764510938` |
| stringify\_ids | optional | Many programming environments will not consume Tweet ids due to their size. Provide this option to have ids returned as strings instead. |     | `true` |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`GET https://api.twitter.com/1.1/statuses/retweeters/ids.json?id=327473909412814850&count=100&stringify_ids=true`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    { "previous_cursor": 0, "ids": [ "1382021622", "931150754", "1364953914", "92313481",
      "1398853771", "268642828", "1393765387", "417614795", "1401282895", "1319566290",
     "1398546265", "1332481988", "295679474", "967380524", "1278983791", "711759314",
     "1396957736", "1400099804", "1400006540", "307434897", "531100534", "553765661",
     "1398911250", "342624342", "629452817", "117815404", "137706363", "200935461",
     "387409391", "1361168810", "1368343309", "613471026", "439924515", "36049728",
     "1274405064", "1389815384", "1392424261", "577940232", "876175585", "510085789",
     "410346647", "1393727204", "1394189851", "1387201657", "1393950540", "900169760",
     "69572684", "517788963", "386168676", "1378242152", "18442587", "848640758",
     "1366022899", "25457359", "257764557", "795253765", "1170975386", "1229598968",
     "204528531", "954414061", "533154335", "580732530", "350798999", "427506664",
     "527674954", "1389957769", "496054455", "1338136910", "1390051482", "1252565820",
     "815941296", "1357349460", "1214535374", "1192879201", "1353712213", "229798008",
     "1382909124", "1026779562", "917199121", "1388715336", "1388417048", "106315621",
     "109159559", "523186040", "1256627971", "1137979866", "424946721", "1387875991" ],
     "previous_cursor_str": "0", "next_cursor": 0, "next_cursor_str": "0" }

POST favorites/create

post-favorites-create

POST favorites/create
=====================

Note: favorites are now known as _likes_.

Favorites (_likes_) the Tweet specified in the ID parameter as the authenticating user. Returns the favorite Tweet when successful.

The process invoked by this method is asynchronous. The immediately returned Tweet object may not indicate the resultant favorited status of the Tweet. A 200 OK response from this method will indicate whether the intended action was successful or not.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/favorites/create.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 24-hour window | 1000 per user; 1000 per app |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| id  | required | The numerical ID of the Tweet to like. |     | _123_ |
| include\_entities | optional | The _entities_ node will be omitted when set to _false_ . |     | _false_ |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

    curl --request POST 
    --url 'https://api.twitter.com/1.1/favorites/create.json?id=TWEET_ID_TO_FAVORITE' 
    --header 'authorization: OAuth oauth_consumer_key="YOUR_CONSUMER_KEY", oauth_nonce="AUTO_GENERATED_NONCE", oauth_signature="AUTO_GENERATED_SIGNATURE", oauth_signature_method="HMAC-SHA1", oauth_timestamp="AUTO_GENERATED_TIMESTAMP", oauth_token="USERS_ACCESS_TOKEN", oauth_version="1.0"' 
    --header 'content-type: application/json'

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {tweet-object,
    "user": {user-object}
    }

POST favorites/destroy

post-favorites-destroy

POST favorites/destroy
======================

Note: favorites are now known as _likes_.

Unfavorites (_un-likes_) the Tweet specified in the ID parameter as the authenticating user. Returns the un-liked Tweet when successful.

The process invoked by this method is asynchronous. The immediately returned Tweet object may not indicate the resultant favorited status of the Tweet. A 200 OK response from this method will indicate whether the intended action was successful or not.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/favorites/destroy.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| id  | required | The numerical ID of the Tweet to un-like |     | _123_ |
| include\_entities | optional | The _entities_ node will be omitted when set to _false_ . |     | _false_ |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`POST https://api.twitter.com/1.1/favorites/destroy.json?id=1050118621198921728`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
      "created_at": "Wed Oct 10 20:19:24 +0000 2018",
      "id": 1050118621198921728,
      "id_str": "1050118621198921728",
      "text": "To make room for more expression, we will now count all emojis as equal—including those with gender‍‍‍ and skin t… https://t.co/MkGjXf9aXm",
      "truncated": true,
      "entities": {
        "hashtags": [],
        "symbols": [],
        "user_mentions": [],
        "urls": [
          {
            "url": "https://t.co/MkGjXf9aXm",
            "expanded_url": "https://twitter.com/i/web/status/1050118621198921728",
            "display_url": "twitter.com/i/web/status/1…",
            "indices": [
              117,
              140
            ]
          }
        ]
      },
      "source": "<a href="http://twitter.com" rel="nofollow">Twitter Web Client</a>",
      "in_reply_to_status_id": null,
      "in_reply_to_status_id_str": null,
      "in_reply_to_user_id": null,
      "in_reply_to_user_id_str": null,
      "in_reply_to_screen_name": null,
      "user": {
        "id": 6253282,
        "id_str": "6253282",
        "name": "Twitter API",
        "screen_name": "TwitterAPI",
        "location": "San Francisco, CA",
        "description": "The Real Twitter API. Tweets about API changes, service issues and our Developer Platform. Don't get an answer? It's on my website.",
        "url": "https://t.co/8IkCzCDr19",
        "entities": {
          "url": {
            "urls": [
              {
                "url": "https://t.co/8IkCzCDr19",
                "expanded_url": "https://developer.twitter.com",
                "display_url": "developer.twitter.com",
                "indices": [
                  0,
                  23
                ]
              }
            ]
          },
          "description": {
            "urls": []
          }
        },
        "protected": false,
        "followers_count": 6128663,
        "friends_count": 12,
        "listed_count": 12900,
        "created_at": "Wed May 23 06:01:13 +0000 2007",
        "favourites_count": 32,
        "utc_offset": null,
        "time_zone": null,
        "geo_enabled": null,
        "verified": true,
        "statuses_count": 3659,
        "lang": "null",
        "contributors_enabled": null,
        "is_translator": null,
        "is_translation_enabled": null,
        "profile_background_color": "null",
        "profile_background_image_url": "null",
        "profile_background_image_url_https": "null",
        "profile_background_tile": nulll,
        "profile_image_url": "null",
        "profile_image_url_https": "https://pbs.twimg.com/profile_images/942858479592554497/BbazLO9L_normal.jpg",
        "profile_banner_url": "https://pbs.twimg.com/profile_banners/6253282/1497491515",
        "profile_link_color": "null",
        "profile_sidebar_border_color": "null",
        "profile_sidebar_fill_color": "null",
        "profile_text_color": "null",
        "profile_use_background_image": null,
        "has_extended_profile": null,
        "default_profile": false,
        "default_profile_image": false,
        "following": nul,
        "follow_request_sent": null,
        "notifications": null,
        "translator_type": "null"
      },
      "geo": null,
      "coordinates": null,
      "place": null,
      "contributors": null,
      "is_quote_status": false,
      "retweet_count": 161,
      "favorite_count": 296,
      "favorited": false,
      "retweeted": false,
      "possibly_sensitive": false,
      "possibly_sensitive_appealable": false,
      "lang": "en"
    }

GET favorites/list

get-favorites-list

GET favorites/list
==================

Note: favorites are now known as _likes_.

Returns the 20 most recent Tweets liked by the authenticating or specified user.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/favorites/list.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 75  |
| Requests / 15-min window (app auth) | 75  |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| user\_id | optional | The ID of the user for whom to return results. |     | _12345_ |
| screen\_name | optional | The screen name of the user for whom to return results. |     | _twitterdev_ |
| count | optional | Specifies the number of records to retrieve. Must be less than or equal to 200; defaults to 20. The value of count is best thought of as a limit to the number of Tweets to return because suspended or deleted content is removed after the count has been applied. |     | _5_ |
| since\_id | optional | Returns results with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets which can be accessed through the API. If the limit of Tweets has occured since the since\_id, the since\_id will be forced to the oldest ID available. |     | _12345_ |
| max\_id | optional | Returns results with an ID less than (that is, older than) or equal to the specified ID. |     | _54321_ |
| include\_entities | optional | The _entities_ node will be omitted when set to _false_ . |     | _false_ |
| include\_ext\_edit\_control | optional | Must be set to true in order to return edited Tweet metadata as part of the Tweet object.<br><br>`include_ext_edit_control=true`<br><br>Note that historical Tweets may not contain edited Tweet metadata. |     | _true_ |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`GET https://api.twitter.com/1.1/favorites/list.json?count=200&screen_name=twitterdev`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    [
      {
        "created_at": "Tue May 14 17:58:31 +0000 2019",
        "id": 1128358947772145672,
        "id_str": "1128358947772145672",
        "text": "Through the Twitter Developer Labs program, we'll soon preview new versions of GET /tweets and GET /users, followed… https://t.co/9i4c5bUUCu",
        "truncated": true,
        "entities": {
          "hashtags": [],
          "symbols": [],
          "user_mentions": [],
          "urls": [
            {
              "url": "https://t.co/9i4c5bUUCu",
              "expanded_url": "https://twitter.com/i/web/status/1128358947772145672",
              "display_url": "twitter.com/i/web/status/1…",
              "indices": [
                117,
                140
              ]
            }
          ]
        },
        "source": "<a href="http://twitter.com" rel="nofollow">Twitter Web Client</a>",
        "in_reply_to_status_id": null,
        "in_reply_to_status_id_str": null,
        "in_reply_to_user_id": null,
        "in_reply_to_user_id_str": null,
        "in_reply_to_screen_name": null,
        "user": {
          "id": 6253282,
          "id_str": "6253282",
          "name": "Twitter API",
          "screen_name": "TwitterAPI",
          "location": "San Francisco, CA",
          "description": "The Real Twitter API. Tweets about API changes, service issues and our Developer Platform. Don't get an answer? It's on my website.",
          "url": "https://t.co/8IkCzCDr19",
          "entities": {
            "url": {
              "urls": [
                {
                  "url": "https://t.co/8IkCzCDr19",
                  "expanded_url": "https://developer.twitter.com",
                  "display_url": "developer.twitter.com",
                  "indices": [
                    0,
                    23
                  ]
                }
              ]
            },
            "description": {
              "urls": []
            }
          },
          "protected": false,
          "followers_count": 6125649,
          "friends_count": 12,
          "listed_count": 12902,
          "created_at": "Wed May 23 06:01:13 +0000 2007",
          "favourites_count": 31,
          "utc_offset": null,
          "time_zone": null,
          "geo_enabled": null,
          "verified": true,
          "statuses_count": 3664,
          "lang": null,
          "contributors_enabled": null,
          "is_translator": null,
          "is_translation_enabled": null,
          "profile_background_color": "null",
          "profile_background_image_url": "null",
          "profile_background_image_url_https": "null",
          "profile_background_tile": null,
          "profile_image_url": "null",
          "profile_image_url_https": "https://pbs.twimg.com/profile_images/942858479592554497/BbazLO9L_normal.jpg",
          "profile_banner_url": "null",
          "profile_link_color": "null",
          "profile_sidebar_border_color": "null",
          "profile_sidebar_fill_color": "null",
          "profile_text_color": "null",
          "profile_use_background_image": null,
          "has_extended_profile": null,
          "default_profile": false,
          "default_profile_image": false,
          "following": null,
          "follow_request_sent": null,
          "notifications": null,
          "translator_type": "null"
        },
        "geo": null,
        "coordinates": null,
        "place": null,
        "contributors": null,
        "is_quote_status": true,
        "quoted_status_id": 1128357926823976960,
        "quoted_status_id_str": "1128357926823976960",
        "quoted_status": {
          "created_at": "Tue May 14 17:54:28 +0000 2019",
          "id": 1128357926823976960,
          "id_str": "1128357926823976960",
          "text": "📣We’re launching Twitter Developer Labs in the coming weeks so we can build the future of our API together with tho… https://t.co/OVUiDiZqep",
          "truncated": true,
          "entities": {
            "hashtags": [],
            "symbols": [],
            "user_mentions": [],
            "urls": [
              {
                "url": "https://t.co/OVUiDiZqep",
                "expanded_url": "https://twitter.com/i/web/status/1128357926823976960",
                "display_url": "twitter.com/i/web/status/1…",
                "indices": [
                  117,
                  140
                ]
              }
            ]
          },
          "source": "<a href="https://mobile.twitter.com" rel="nofollow">Twitter Web App</a>",
          "in_reply_to_status_id": null,
          "in_reply_to_status_id_str": null,
          "in_reply_to_user_id": null,
          "in_reply_to_user_id_str": null,
          "in_reply_to_screen_name": null,
          "user": {
            "id": 2244994945,
            "id_str": "2244994945",
            "name": "Twitter Dev",
            "screen_name": "TwitterDev",
            "location": "Internet",
            "description": "Your official source for Twitter Platform news, updates & events. Need technical help? Visit https://t.co/mGHnxZU8c1 ⌨️ #TapIntoTwitter",
            "url": "https://t.co/FGl7VOULyL",
            "entities": {
              "url": {
                "urls": [
                  {
                    "url": "https://t.co/FGl7VOULyL",
                    "expanded_url": "https://developer.twitter.com/",
                    "display_url": "developer.twitter.com",
                    "indices": [
                      0,
                      23
                    ]
                  }
                ]
              },
              "description": {
                "urls": [
                  {
                    "url": "https://t.co/mGHnxZU8c1",
                    "expanded_url": "https://twittercommunity.com/",
                    "display_url": "twittercommunity.com",
                    "indices": [
                      93,
                      116
                    ]
                  }
                ]
              }
            },
            "protected": false,
            "followers_count": 502258,
            "friends_count": 1475,
            "listed_count": 1519,
            "created_at": "Sat Dec 14 04:35:55 +0000 2013",
            "favourites_count": 2205,
            "utc_offset": null,
            "time_zone": null,
            "geo_enabled": null,
            "verified": true,
            "statuses_count": 3664,
            "lang": null,
            "contributors_enabled": null,
            "is_translator": null,
            "is_translation_enabled": null,
            "profile_background_color": "null",
            "profile_background_image_url": "null",
            "profile_background_image_url_https": "null",
            "profile_background_tile": null,
            "profile_image_url": "null",
            "profile_image_url_https": "https://pbs.twimg.com/profile_images/942858479592554497/BbazLO9L_normal.jpg",
            "profile_banner_url": "https://pbs.twimg.com/profile_banners/6253282/1497491515",
            "profile_link_color": "null",
            "profile_sidebar_border_color": "null",
            "profile_sidebar_fill_color": "null",
            "profile_text_color": "null",
            "profile_use_background_image": null,
            "has_extended_profile": null,
            "default_profile": false,
            "default_profile_image": false,
            "following": null,
            "follow_request_sent": null,
            "notifications": null,
            "translator_type": "null"
            },
          "geo": null,
          "coordinates": null,
          "place": null,
          "contributors": null,
          "is_quote_status": false,
          "retweet_count": 169,
          "favorite_count": 350,
          "favorited": false,
          "retweeted": false,
          "possibly_sensitive": false,
          "lang": "en"
        },
        "retweet_count": 35,
        "favorite_count": 74,
        "favorited": false,
        "retweeted": false,
        "possibly_sensitive": false,
        "lang": "en"
      }
    ]

POST statuses/update\_with\_media (deprecated)

post-statuses-update\_with\_media

POST statuses/update\_with\_media (deprecated)
==============================================

**This endpoint has been DEPRECATED should no longer be used. This endpoint does not support multiple images, animated GIFs, or video.** Replacement method: follow the [Uploading media guide](https://developer.twitter.com/en/docs/media/upload-media/overview) to upload one or more media entities, and then use [POST statuses/update](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-statuses-update) to attach them to a Tweet.

Updates the authenticated user's current status and attaches media for upload. This creates a Tweet with a (single) picture attached.

Unlike [POST statuses/update](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-statuses-update), this method expects raw multipart data. The POST request's `content-type` should be set to `multipart/form-data` with the `media[]` parameter.

The Tweet text will be rewritten to include the media URL(s), which will reduce the number of characters allowed in the Tweet text. If the URL(s) cannot be appended without text truncation, the Tweet will be rejected and this method will return an HTTP 403 error.

Users are limited to a specific daily media upload limit. Requests to this endpoint will return the following headers with information regarding the user's current media upload limits:

* `x-mediaratelimit-limit` - Indicates the total pieces of media the current user may upload before the time indicated in `x-mediaratelimit-reset`.
* `x-mediaratelimit-remaining` - The remaining pieces of media the current user may upload before the time indicated in `x-mediaratelimit-reset`.
* `x-mediaratelimit-reset` - A UTC-based timestamp (in seconds) indicating when `x-mediaratelimit-remaining` will reset to the value in `x-mediaratelimit-limit` and the user can resume uploading media.

If the user is over the daily media limit, this method will return an HTTP 403 error. In addition to media upload limits, the user is also limited in the number of statuses they can publish daily. If the user tries to exceed the number of updates allowed, this method will also return an HTTP 403 error, similar to [POST statuses/update](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-statuses-update).

There is a 30 second timeout for this endpoint, so network latency may prevent media being posted successfully.

OAuth is handled differently for POST messages. See [Uploading Media](https://developer.twitter.com/en/docs/media/upload-media/overview) for more details on this.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/statuses/update_with_media.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

| Name | Required | Description | Default Value | Example |
| --- | --- | --- | --- | --- |
| status | required | The text of your status update. URL encode as necessary. [t.co link wrapping](https://developer.twitter.com/en/docs/basics/tco) may affect character counts if the post contains URLs. You must additionally account for the `characters_reserved_per_media` per uploaded media, additionally accounting for space characters in between finalized URLs. **Note** : Request the `GET help / configuration &lt;/en/docs/developer-utilities/configuration/api-reference/get-help-c current` characters\_reserved\_per\_media`and`max\_media\_per\_upload\` values. |     | onfiguration>\`\_\_ endpoint to get the |
| media\[\] | required | Up to `max_media_per_upload` files may be specified in the request, each named `media[]` . Supported image formats are PNG, JPG and GIF, including animated GIFs of up to 3MB . This data must be either the raw image bytes or encoded as base64. **Note** : Request the `GET help / configuration &lt;/en/docs/developer-utilities/configuration/api-reference/get-help-c current` max\_media\_per\_upload`and`photo\_size\_limit\` values. | onfiguration>\`\_\_ endpoint to get the |     |
| possibly\_sensitive | optional | Set to `true` for content which may not be suitable for every audience. |     |     |
| in\_reply\_to\_status\_id | optional | The ID of an existing status that the update is in reply to. **Note** : This parameter will be ignored unless the author of the Tweet this parameter references is mentioned within the status text. Therefore, you must include `@username` , where `username` is the author of the referenced Tweet, within the update. |     |     |
| lat | optional | The latitude of the location this Tweet refers to. This parameter will be ignored unless it is inside the range -90.0 to +90.0 (North is positive) inclusive. It will also be ignored if there isn't a corresponding `long` parameter. |     | `37.7821120598956` |
| long | optional | The longitude of the location this Tweet refers to. The valid ranges for longitude is -180.0 to +180.0 (East is positive) inclusive. This parameter will be ignored if outside that range, not a number, `geo_enabled` is turned off, or if there not a corresponding `lat` parameter. |     | `-122.400612831116` |
| place\_id | optional | A place in the world identified by a Twitter place ID. Place IDs can be retrieved from geo/reverse\_geocode. |     | `df51dec6f4ee2b2c` |
| display\_coordinates | optional | Whether or not to put a pin on the exact coordinates a Tweet has been sent from. |     | `true` |
| enable\_dmcommands | optional | When set to `true`, enables shortcode commands for sending Direct Messages as part of the status text to send a Direct Message to a user. When set to `false`, it turns off this behavior and includes any leading characters in the status text. | > `true` | `true` |
| fail\_dmcommands | optional | When set to `true`, causes any status text that starts with shortcode commands to return an API error. When set to `false`, allows shortcode commands to be sent in the status text and acted on by the API. | > `false` | `false` |

### Example Request[¶](#example-request "Permalink to this headline")

**Note:** The example request here demonstrates the multipart request format.

POST /1.1/statuses/update\_with\_media.json HTTP/1.1
Host: api.twitter.com
User-Agent: Go http package
Content-Length: 15532
Authorization: OAuth oauth\_consumer\_key="...", oauth\_nonce="...", oauth\_signature="...", oauth\_signature\_method="HMAC-SHA1", oauth\_timestamp="1347058301", oauth\_token="...", oauth\_version="1.0"
Content-Type: multipart/form-data;boundary=cce6735153bf14e47e999e68bb183e70a1fa7fc89722fc1efdf03a917340
Accept-Encoding: gzip

--cce6735153bf14e47e999e68bb183e70a1fa7fc89722fc1efdf03a917340
Content-Disposition: form-data; name="status" Hello 2012-09-07 15:51:41.375247 -0700 PDT!
--cce6735153bf14e47e999e68bb183e70a1fa7fc89722fc1efdf03a917340

Content-Type: application/octet-stream
Content-Disposition: form-data; name="media\[\]"; filename="media.png" ...
--cce6735153bf14e47e999e68bb183e70a1fa7fc89722fc1efdf03a917340-- 

{
  "contributors": null,
  "coordinates": null,
  "created\_at": "Fri Sep 07 22:46:18 +0000 2012",
  "entities": {
    "hashtags": \[\],
    "media": \[
      {
        "display\_url": "pic.twitter.com/lX5LVZO",
        "expanded\_url": "https://twitter.com/fakekurrik/status/244204973972410368/photo/1",
        "id": 244204973989187584,
        "id\_str": "244204973989187584",
        "indices": \[
          44,
          63
        \],
        "media\_url": "http://pbs.twimg.com/media/A2OXIUcCUAAXj9k.png",
        "media\_url\_https": "https://pbs.twimg.com/media/A2OXIUcCUAAXj9k.png",
        "sizes": {
          "large": {
            "h": 175,
            "resize": "fit",
            "w": 333
          },
          "medium": {
            "h": 175,
            "resize": "fit",
            "w": 333
          },
          "small": {
            "h": 175,
            "resize": "fit",
            "w": 333
          },
          "thumb": {
            "h": 150,
            "resize": "crop",
            "w": 150
          }
        },
        "type": "photo",
        "url": "http://t.co/lX5LVZO"
      }
    \],
    "urls": \[\],
    "user\_mentions": \[\]
  },
  "favorited": false,
  "geo": null,
  "id": 244204973972410368,
  "id\_str": "244204973972410368",
  "in\_reply\_to\_screen\_name": null,
  "in\_reply\_to\_status\_id": null,
  "in\_reply\_to\_status\_id\_str": null,
  "in\_reply\_to\_user\_id": null,
  "in\_reply\_to\_user\_id\_str": null,
  "place": null,
  "possibly\_sensitive": false,
  "retweet\_count": 0,
  "retweeted": false,
  "source": "Fakekurrik's Test Application",
  "text": "Hello 2012-09-07 15:48:27.889593 -0700 PDT! http://t.co/lX5LVZO",
  "truncated": false,
  "user": {
    "contributors\_enabled": false,
    "created\_at": "Fri Sep 09 16:13:20 +0000 2011",
    "default\_profile": false,
    "default\_profile\_image": false,
    "description": "I am just a testing account, following me probably won't gain you very much",
    "entities": {
      "description": {
        "urls": \[\]
      },
      "url": {
        "urls": \[
          {
            "display\_url": null,
            "expanded\_url": null,
            "indices": \[
              0,
              24
            \],
            "url": "http://blog.roomanna.com"
          }
        \]
      }
    },
    "favourites\_count": 1,
    "follow\_request\_sent": false,
    "followers\_count": 2,
    "following": false,
    "friends\_count": 5,
    "geo\_enabled": true,
    "id": 370773112,
    "id\_str": "370773112",
    "is\_translator": false,
    "lang": "en",
    "listed\_count": 0,
    "location": "Trapped in factory",
    "name": "fakekurrik",
    "notifications": false,
    "profile\_background\_color": "C0DEED",
    "profile\_background\_image\_url": "http://a0.twimg.com/profile\_background\_images/616512781/iarz5lvj7lg7zpg3zv8j.jpeg",
    "profile\_background\_image\_url\_https": "https://si0.twimg.com/profile\_background\_images/616512781/iarz5lvj7lg7zpg3zv8j.jpeg",
    "profile\_background\_tile": true,
    "profile\_image\_url": "http://a0.twimg.com/profile\_images/2440719659/x47xdzkguqxr1w1gg5un\_normal.png",
    "profile\_image\_url\_https": "https://si0.twimg.com/profile\_images/2440719659/x47xdzkguqxr1w1gg5un\_normal.png",
    "profile\_link\_color": "0084B4",
    "profile\_sidebar\_border\_color": "C0DEED",
    "profile\_sidebar\_fill\_color": "FFFFFF",
    "profile\_text\_color": "333333",
    "profile\_use\_background\_image": true,
    "protected": true,
    "screen\_name": "fakekurrik",
    "show\_all\_inline\_media": false,
    "statuses\_count": 546,
    "time\_zone": "Pacific Time (US & Canada)",
    "url": "http://blog.roomanna.com",
    "utc\_offset": -28800,
    "verified": false
  }
}

Overview

**Please note:**  

We've recently released the following endpoints within the [Twitter API v2](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api). 

|     |     |     |
| --- | --- | --- |
| **v1.1 endpoints** | **Corresponding v2 endpoints** |     |
| [GET statuses/user\_timeline](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/api-reference/get-statuses-user_timeline.html) | [User Tweet timeline](https://developer.twitter.com/en/docs/twitter-api/tweets/timelines/introduction) | [Migration guide](https://developer.twitter.com/en/docs/twitter-api/tweets/timelines/migrate) |
| [GET statuses/user\_mentions](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/api-reference/get-statuses-mentions_timeline.html) | [User mention timeline](https://developer.twitter.com/en/docs/twitter-api/tweets/timelines/introduction) | [Migration guide](https://developer.twitter.com/en/docs/twitter-api/tweets/timelines/migrate) |

Please use the migration guides to see what has changed between the standard v1.1 and v2 versions.

**Important note:**  

This endpoint has been updated to include Tweet edit metadata. Learn more about these metadata on the ["Edit Tweets" fundamentals page](https://developer.twitter.com/en/docs/twitter-api/v1/edit-tweets). 

Overview
--------

**Important notice:**  On **June 19, 2019**, we began limiting total GET requests to the v1.1 /statuses/mentions\_timeline and /statuses/user\_timeline endpoints to 100,000 requests per day. This is a total request limit (per endpoint) applied across both user-auth and app-auth requests. This means that in a 24-hour period, a single app can make up to 100,000 requests to /statuses/mentions\_timeline and/or 100,000 requests to /statuses/user\_timeline (with either app or user auth) before hitting this new app-level rate limit. The existing default user-auth and app-auth rate limits remain the same.

A timeline is simply a list, or an aggregated stream of Tweets.  The Twitter API has several endpoints that return a timeline of Tweet data - see the table below for more details:  

| API endpoint | Description |
| --- | --- |
| [GET statuses / home\_timeline](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/api-reference/get-statuses-home_timeline) | Returns a collection of the most recent Tweets posted by the authenticating user and the users they follow. |
| [GET statuses / user\_timeline](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/api-reference/get-statuses-user_timeline) | Returns a collection of the most recent Tweets posted by the indicated by the screen\_name or user\_id parameters. |
| [GET statuses/mentions\_timeline](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/api-reference/get-statuses-mentions_timeline) | Returns the 20 most recent mentions (Tweets containing a users’s @handle) for the authenticating user. |

Working with timelines

**Please note:**  

We launched a [new version of the standard v1.1 statuses/user\_timeline and statuses/mentions\_timeline endpoints](https://developer.twitter.com/en/docs/twitter-api/tweets/timelines/introduction) as part of [Twitter API v2: Early Access](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/early-access). If you are currently using either of these endpoints, you can use our [migration materials](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/tweets/timelines/migrate/standard-to-twitter-api-v2) to start working with the newer endpoint.

Working with timelines  

-------------------------

The Twitter API has several methods, such as [GET statuses / user\_timeline](https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline.html) and [GET statuses / home\_timeline](https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-home_timeline.html), which return a timeline of Tweet data. Such timelines can grow very large, so there are limits to how much of a timeline a client application may fetch in a single request. Applications must therefore iterate through timeline results in order to build a more complete list.

Because of Twitter’s realtime nature and the volume of data which is constantly being added to timelines, standard paging approaches are not always effective. The goal of this page is to demonstrate the issues Twitter developers may face when paging through result sets and to give best practices for processing a timeline.

### The problem with “pages”

In an ideal world, paging would be very easy to implement. Consider the case where a timeline has 10 reverse-chronologically sorted Tweets. An application might attempt to read the entire timeline in two requests by setting a page size of 5 elements and requesting the first page, then the second page. 

The problem with this method is that Twitter timelines are constantly having new Tweets added to their front. Consider the previous example. If two new Tweets are added to the timeline between the first and second calls, the second fetch retrieves two Tweets which were returned in the previous call.

In fact, if 5 or more Tweets were added between calls, subsequent calls would eventually retrieve all the Tweets returned from the first request - making an entire API request completely redundant.

### The max\_id parameter

The solution to the issue described above is to use a technique for working with streams of data called cursoring. Instead of reading a timeline relative to the top of the list (which changes frequently), an application should read the timeline relative to the IDs of Tweets it has already processed. This is achieved through the use of the max\_id request parameter.

To use max\_id correctly, an application’s first request to a timeline endpoint should only specify a count. When processing this and subsequent responses, keep track of the lowest ID received. This ID should be passed as the value of the max\_id parameter for the next request, which will only return Tweets with IDs lower than or equal to the value of the max\_id parameter. Note that since the max\_id parameter is inclusive, the Tweet with the matching ID will actually be returned again.

### Optimizing max\_id for environments with 64-bit integers

While one redundant Tweet is not inefficient, it is still possible to optimize max\_id requests to address this problem if your platform is capable of working with 64-bit integers. **Environments where a Tweet ID cannot be represented as an integer with 64 bits of precision (such as JavaScript) should skip this step.** Subtract 1 from the lowest Tweet ID returned from the previous request and use this for the value of max\_id. It does not matter if this adjusted max\_id is a valid Tweet ID, or if it corresponds with a Tweet posted by a different user - the value is just used to decide which Tweets to filter. When adjusted in this manner, it is possible to page through a timeline without receiving redundant Tweets.

### Using since\_id for the greatest efficiency

Applications which process a timeline, wait some quantity of time, and then need to process new Tweets which have been added since the last time the timeline was processed can make one more optimization using the since\_id parameter.

Consider the previous example where Tweets 1 through 10 were processed. Now imagine that Tweets 11 through 18 were added to the timeline since the processing in the previous example began. An inefficient approach to process the new Tweets would be to iterate from the start of the list until Tweet 10 appeared. This causes two Tweets which have already been processed to be returned again.

This problem is avoided by setting the since\_id parameter to the greatest ID of all the Tweets your application has already processed. Unlike max\_id the since\_id parameter is not inclusive, so it is not necessary to adjust the ID in any way. As shown in the following image, Twitter will only return Tweets with IDs higher than the value passed for since\_id.

Applications which use both the max\_id and since\_id parameters correctly minimize the amount of redundant data they fetch and process, while retaining the ability to iterate over the entire available contents of a timeline.

FAQ

**Please note:**  

We launched a [new version of the standard v1.1 statuses/user\_timeline and statuses/mentions\_timeline endpoints](https://developer.twitter.com/en/docs/twitter-api/tweets/timelines/introduction) as part of [Twitter API v2: Early Access](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/early-access). If you are currently using either of these endpoints, you can use our [migration materials](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/tweets/timelines/migrate/standard-to-twitter-api-v2) to start working with the newer endpoint.

Frequently Asked Questions
--------------------------

This FAQ addresses questions about the new request limit (100,000 / 24-hours) enforced on the /statuses/mentions\_timeline and /statuses/user\_timeline endpoints.

**Why are you making this change?**

As noted in [the blog post](https://blog.twitter.com/developer/en_us/topics/tools/2019/previewing-changes-to-the-user-and-mentions-timeline-api-endpoints.html), we’re making these changes so we can appropriately review how developers are using these endpoints, and so that access to our APIs is fair and consistent for developers who have built solutions to serve other businesses. Adjusting these rate limits also contributes to our goal of helping people feel safe and protecting their privacy while maintaining open access to our developer platform.

**What API endpoints are impacted by the announcement?**

We are announcing that we are limiting access to two of the most commonly used Twitter standard API endpoints – [statuses/user\_timeline and statuses/mentions\_timeline.](https://developer.twitter.com/content/developer-twitter/en/docs/tweets/timelines/overview) This change will ensure that we appropriately review how existing apps are using these endpoints, while also making sure that all companies using our APIs to build products for business purposes are doing so fairly and consistently.

**What are the new rate limits?**

On June 19, 2019, we will begin limiting access to the /statuses/mentions\_timeline and /statuses/user\_timeline endpoints to 100,000 requests per day as a default. This is a total request limit that applies across both user-auth and app-auth requests. These limits will be on a per-application and per-endpoint basis, meaning that a single developer app can make up to 100,000 calls to each of the two endpoints during any single 24-hour period. The existing default user-auth and app-auth rate limits will not change.

**Are we changing the existing user-auth and app-auth rate limits?**

No, existing default user-auth and app-auth rate limits are not currently changing. To be clear, as of June 19, rate limits for statuses/mentions\_timeline and statuses/user\_timeline will be as follows:

* **/statuses/mentions\_timeline:**
    * 75 requests/15-min window (user-auth)
    * 100,000 requests/24-hour window (application level)
* **/statuses/user\_timeline:**
    * 900 requests/15-min window (user-auth)
    * 1500 requests/15-min window (app-auth)
    * 100,000 requests/24-hour window (application level)

**Is the 24-hour period based on clock time (e.g., 0:00 UTC) or a rolling clock?**

The 24-hour period is based on a rolling clock, beginning at the time of the first request and monitored for the next 24 hours.

**How do I determine if I am impacted by this change?**

We have proactively contacted developers who will be impacted via their registered developer email addresses. If you did not receive an email, you’ll need to check if your Twitter developer app is making more than 100,000 requests to either /statuses/mentions\_timeline or /statuses/user\_timeline endpoints in a 24-hour period. Please see question 8 (option 2) below for details on what to do if you believe your app will be impacted.

**How do I check whether I am hitting the endpoint(s) near the request limit?**

We do not have an endpoint that provides this information, so you will have to review your logs to track your usage. If you would like to check your usage from the current rate limit window, you can use the [application/rate\_limit\_status](https://developer.twitter.com/content/developer-twitter/en/docs/developer-utilities/rate-limit-status/api-reference/get-application-rate_limit_status) endpoint.

**What can I do if I am impacted by this change?**

Please review the two options outlined below and proceed with the one that best describes your application:

**I. My application serves other businesses:**

1. Please complete the enterprise API application via [this form](https://developer.twitter.com/content/developer-twitter/en/enterprise-application) with detailed information about your application that makes use of these endpoints.
2. A Twitter representative will be in touch to discuss available options for continued access. Part of this process will include a review of your application, your use case, and a consultation of the best API solutions available to serve your needs.

**II. My application does not serve other businesses:**

1. Make sure that you are logged into your Twitter Developer account.
2. Follow [this link](https://help.twitter.com/forms/platform) to the API Policy Support Page, where you might see the option: "I would like to apply for elevated user & mentions timeline limits."
    * _Important note:_ If you do not see this option, please double check the Twitter account you're currently logged in with. If you still do not see this option, your application does not qualify for a review at this time because your usage is well below impacted thresholds. Rest assured, if you start making requests at a volume near the rate limit, the proper form option will become available. Based on this, we request that you don’t post to the forums if you don’t see this option unless you actually hit the rate limit.
3. Complete the form with as much detail as you can about your current use of one (or both) of the mentions and user timeline endpoints. Our team may need to reach out for further clarification if your submission is incomplete or unclear, which may delay a decision about your application. Please provide as much detail as possible.
4. We will review your submission and notify you of our decision when our review is complete.

**Will developers ever be required to migrate off of the user and mentions timeline endpoints?**

We are taking a phased approach at changes to our platform, so that we can collect feedback from developers and minimize impact. We want to make sure we understand how and why developers are using them to help inform any changes we might make in the future.

**If an app makes a request to mentions or user timeline and it fails (e.g., 401 Unauthorized), will it count against the 100,000 limit?**

No. If the request fails, then it will not count against the 100,000 limit.

**How will the API behave if my app exceeds the 100,000 request limit in a 24-hour period?**

The API will return a 429 error response if your app exceeds the 100,000 request limit in a 24-hour period:

HTTP/1.1 429 Too Many Requests

{"errors":\[{"message":"Rate limit exceeded","code":88}\]}

The 429 error response will continue to be returned until the current 24-hour period ends.

GET statuses/home\_timeline

get-statuses-home\_timeline

GET statuses/home\_timeline
===========================

Returns a collection of the most recent [Tweets](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object) and Retweets posted by the authenticating user and the users they follow. The home timeline is central to how most users interact with the Twitter service.

Up to 800 Tweets are obtainable on the home timeline. It is more volatile for users that follow many users or follow users who Tweet frequently.

See [Working with Timelines](https://developer.twitter.com/en/docs/tweets/timelines/guides/working-with-timelines) for instructions on traversing timelines efficiently.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/statuses/home_timeline.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 15  |
| Supports Edit Tweets feature? | Yes |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| count | optional | Specifies the number of records to retrieve. Must be less than or equal to 200. Defaults to 20. The value of count is best thought of as a limit to the number of tweets to return because suspended or deleted content is removed after the count has been applied. |     | _5_ |
| since\_id | optional | Returns results with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets which can be accessed through the API. If the limit of Tweets has occured since the since\_id, the since\_id will be forced to the oldest ID available. |     | _12345_ |
| max\_id | optional | Returns results with an ID less than (that is, older than) or equal to the specified ID. |     | _54321_ |
| trim\_user | optional | When set to either _true_ , _t_ or _1_ , each Tweet returned in a timeline will include a user object including only the status authors numerical ID. Omit this parameter to receive the complete user object. |     | _true_ |
| exclude\_replies | optional | This parameter will prevent replies from appearing in the returned timeline. Using _exclude\_replies_ with the _count_ parameter will mean you will receive up-to count Tweets — this is because the _count_ parameter retrieves that many Tweets before filtering out retweets and replies. |     | _true_ |
| include\_entities | optional | The _entities_ node will not be included when set to _false_. |     | _false_ |
| include\_ext\_edit\_control | optional | Must be set to true in order to return edited Tweet metadata as part of the Tweet object.<br><br>`include_ext_edit_control=true`<br><br>Note that historical Tweets may not contain edited Tweet metadata.<br><br>To learn more about how edited Tweets are supported, see the [Edit Tweets fundamentals](https://developer.twitter.com/en/docs/twitter-api/v1/edit-tweets) page. |     | _true_ |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`GET https://api.twitter.com/1.1/statuses/home_timeline.json`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
      "created_at": "Wed Oct 10 20:19:24 +0000 2018",
      "id": 1050118621198921728,
      "id_str": "1050118621198921728",
      "text": "To make room for more expression, we will now count all emojis as equal—including those with gender‍‍‍ and skin t… https://t.co/MkGjXf9aXm",
      "truncated": true,
      "entities": {
        "hashtags": [],
        "symbols": [],
        "user_mentions": [],
        "urls": [
          {
            "url": "https://t.co/MkGjXf9aXm",
            "expanded_url": "https://twitter.com/i/web/status/1050118621198921728",
            "display_url": "twitter.com/i/web/status/1…",
            "indices": [
              117,
              140
            ]
          }
        ]
      },
      "source": "<a href="http://twitter.com" rel="nofollow">Twitter Web Client</a>",
      "in_reply_to_status_id": null,
      "in_reply_to_status_id_str": null,
      "in_reply_to_user_id": null,
      "in_reply_to_user_id_str": null,
      "in_reply_to_screen_name": null,
      "user": {
        "id": 6253282,
        "id_str": "6253282",
        "name": "Twitter API",
        "screen_name": "TwitterAPI",
        "location": "San Francisco, CA",
        "description": "The Real Twitter API. Tweets about API changes, service issues and our Developer Platform. Don't get an answer? It's on my website.",
        "url": "https://t.co/8IkCzCDr19",
        "entities": {
          "url": {
            "urls": [
              {
                "url": "https://t.co/8IkCzCDr19",
                "expanded_url": "https://developer.twitter.com",
                "display_url": "developer.twitter.com",
                "indices": [
                  0,
                  23
                ]
              }
            ]
          },
          "description": {
            "urls": []
          }
        },
        "protected": false,
        "followers_count": 6128663,
        "friends_count": 12,
        "listed_count": 12900,
        "created_at": "Wed May 23 06:01:13 +0000 2007",
        "favourites_count": 32,
        "utc_offset": null,
        "time_zone": null,
        "geo_enabled": null,
        "verified": true,
        "statuses_count": 3659,
        "lang": "null",
        "contributors_enabled": null,
        "is_translator": null,
        "is_translation_enabled": null,
        "profile_background_color": "null",
        "profile_background_image_url": "null",
        "profile_background_image_url_https": "null",
        "profile_background_tile": nulll,
        "profile_image_url": "null",
        "profile_image_url_https": "https://pbs.twimg.com/profile_images/942858479592554497/BbazLO9L_normal.jpg",
        "profile_banner_url": "https://pbs.twimg.com/profile_banners/6253282/1497491515",
        "profile_link_color": "null",
        "profile_sidebar_border_color": "null",
        "profile_sidebar_fill_color": "null",
        "profile_text_color": "null",
        "profile_use_background_image": null,
        "has_extended_profile": null,
        "default_profile": false,
        "default_profile_image": false,
        "following": nul,
        "follow_request_sent": null,
        "notifications": null,
        "translator_type": "null"
      },
      "geo": null,
      "coordinates": null,
      "place": null,
      "contributors": null,
      "is_quote_status": false,
      "retweet_count": 161,
      "favorite_count": 296,
      "favorited": false,
      "retweeted": false,
      "possibly_sensitive": false,
      "possibly_sensitive_appealable": false,
      "lang": "en"
    }

GET statuses/mentions\_timeline

get-statuses-mentions\_timeline

GET statuses/mentions\_timeline
===============================

**Important notice:** On June 19, 2019, we began enforcing a limit of 100,000 requests per day to the /statuses/mentions\_timeline endpoint. This is in addition to existing user-level rate limits (75 requests / 15-minutes). This limit is enforced on a per-application basis, meaning that a single developer app can make up to 100,000 calls during any single 24-hour period.

Returns the 20 most recent mentions (Tweets containing a users's @screen\_name) for the authenticating user.

The timeline returned is the equivalent of the one seen when you view [your mentions](http://twitter.com/mentions) on twitter.com.

This method can only return up to 800 tweets.

See [Working with Timelines](https://developer.twitter.com/en/docs/tweets/timelines/guides/working-with-timelines) for instructions on traversing timelines.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/statuses/mentions_timeline.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 75  |
| Requests / 24-hour window | 100,000 |
| Supports Edit Tweets feature? | Yes |

_Note:_ the 24-hour request limit is based on a rolling clock, beginning at the time of the first request and monitored for the next 24 hours.

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| count | optional | Specifies the number of Tweets to try and retrieve, up to a maximum of 200. The value of _count_ is best thought of as a limit to the number of tweets to return because suspended or deleted content is removed after the count has been applied. We include retweets in the count, even if _include\_rts_ is not supplied. It is recommended you always send _include\_rts=1_ when using this API method. |     |     |
| since\_id | optional | Returns results with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets which can be accessed through the API. If the limit of Tweets has occured since the since\_id, the since\_id will be forced to the oldest ID available. |     | _12345_ |
| max\_id | optional | Returns results with an ID less than (that is, older than) or equal to the specified ID. |     | _54321_ |
| trim\_user | optional | When set to either _true_ , _t_ or _1_ , each tweet returned in a timeline will include a user object including only the status authors numerical ID. Omit this parameter to receive the complete user object. |     | _true_ |
| include\_entities | optional | The _entities_ node will not be included when set to _false_. |     | _false_ |
| include\_ext\_edit\_control | optional | Must be set to true in order to return edited Tweet metadata as part of the Tweet object.<br><br>`include_ext_edit_control=true`<br><br>Note that historical Tweets may not contain edited Tweet metadata.<br><br>To learn more about how edited Tweets are supported, see the [Edit Tweets fundamentals](https://developer.twitter.com/en/docs/twitter-api/v1/edit-tweets) page. |     | _true_ |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`GET https://api.twitter.com/1.1/statuses/mentions_timeline.json?count=2&since_id=14927799`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    [
      {
        "coordinates": null,
        "favorited": false,
        "truncated": false,
        "created_at": "Mon Sep 03 13:24:14 +0000 2012",
        "id_str": "242613977966850048",
        "entities": {
          "urls": [
    
          ],
          "hashtags": [
    
          ],
          "user_mentions": [
            {
              "name": "Jason Costa",
              "id_str": "14927800",
              "id": 14927800,
              "indices": [
                0,
                11
              ],
              "screen_name": "jasoncosta"
            },
            {
              "name": "Matt Harris",
              "id_str": "777925",
              "id": 777925,
              "indices": [
                12,
                26
              ],
              "screen_name": "themattharris"
            },
            {
              "name": "ThinkWall",
              "id_str": "117426578",
              "id": 117426578,
              "indices": [
                109,
                119
              ],
              "screen_name": "thinkwall"
            }
          ]
        },
        "in_reply_to_user_id_str": "14927800",
        "contributors": null,
        "text": "@jasoncosta @themattharris Hey! Going to be in Frisco in October. Was hoping to have a meeting to talk about @thinkwall if you're around?",
        "retweet_count": 0,
        "in_reply_to_status_id_str": null,
        "id": 242613977966850048,
        "geo": null,
        "retweeted": false,
        "in_reply_to_user_id": 14927800,
        "place": null,
        "user": {
          "profile_sidebar_fill_color": "EEEEEE",
          "profile_sidebar_border_color": "000000",
          "profile_background_tile": false,
          "name": "Andrew Spode Miller",
          "profile_image_url": "http://a0.twimg.com/profile_images/1227466231/spode-balloon-medium_normal.jpg",
          "created_at": "Mon Sep 22 13:12:01 +0000 2008",
          "location": "London via Gravesend",
          "follow_request_sent": false,
          "profile_link_color": "F31B52",
          "is_translator": false,
          "id_str": "16402947",
          "entities": {
            "url": {
              "urls": [
                {
                  "expanded_url": null,
                  "url": "http://www.linkedin.com/in/spode",
                  "indices": [
                    0,
                    32
                  ]
                }
              ]
            },
            "description": {
              "urls": [
    
              ]
            }
          },
          "default_profile": false,
          "contributors_enabled": false,
          "favourites_count": 16,
          "url": "http://www.linkedin.com/in/spode",
          "profile_image_url_https": "https://si0.twimg.com/profile_images/1227466231/spode-balloon-medium_normal.jpg",
          "utc_offset": 0,
          "id": 16402947,
          "profile_use_background_image": false,
          "listed_count": 129,
          "profile_text_color": "262626",
          "lang": "en",
          "followers_count": 2013,
          "protected": false,
          "notifications": null,
          "profile_background_image_url_https": "https://si0.twimg.com/profile_background_images/16420220/twitter-background-final.png",
          "profile_background_color": "FFFFFF",
          "verified": false,
          "geo_enabled": true,
          "time_zone": "London",
          "description": "Co-Founder/Dev (PHP/jQuery) @justFDI. Run @thinkbikes and @thinkwall for events. Ex tech journo, helps run @uktjpr. Passion for Linux and customises everything.",
          "default_profile_image": false,
          "profile_background_image_url": "http://a0.twimg.com/profile_background_images/16420220/twitter-background-final.png",
          "statuses_count": 11550,
          "friends_count": 770,
          "following": null,
          "show_all_inline_media": true,
          "screen_name": "spode"
        },
        "in_reply_to_screen_name": "jasoncosta",
        "source": "JournoTwit",
        "in_reply_to_status_id": null
      },
      {
        "coordinates": {
          "coordinates": [
            121.0132101,
            14.5191613
          ],
          "type": "Point"
        },
        "favorited": false,
        "truncated": false,
        "created_at": "Mon Sep 03 08:08:02 +0000 2012",
        "id_str": "242534402280783873",
        "entities": {
          "urls": [
    
          ],
          "hashtags": [
            {
              "text": "twitter",
              "indices": [
                49,
                57
              ]
            }
          ],
          "user_mentions": [
            {
              "name": "Jason Costa",
              "id_str": "14927800",
              "id": 14927800,
              "indices": [
                14,
                25
              ],
              "screen_name": "jasoncosta"
            }
          ]
        },
        "in_reply_to_user_id_str": null,
        "contributors": null,
        "text": "Got the shirt @jasoncosta thanks man! Loving the #twitter bird on the shirt :-)",
        "retweet_count": 0,
        "in_reply_to_status_id_str": null,
        "id": 242534402280783873,
        "geo": {
          "coordinates": [
            14.5191613,
            121.0132101
          ],
          "type": "Point"
        },
        "retweeted": false,
        "in_reply_to_user_id": null,
        "place": null,
        "user": {
          "profile_sidebar_fill_color": "EFEFEF",
          "profile_sidebar_border_color": "EEEEEE",
          "profile_background_tile": true,
          "name": "Mikey",
          "profile_image_url": "http://a0.twimg.com/profile_images/1305509670/chatMikeTwitter_normal.png",
          "created_at": "Fri Jun 20 15:57:08 +0000 2008",
          "location": "Singapore",
          "follow_request_sent": false,
          "profile_link_color": "009999",
          "is_translator": false,
          "id_str": "15181205",
          "entities": {
            "url": {
              "urls": [
                {
                  "expanded_url": null,
                  "url": "http://about.me/michaelangelo",
                  "indices": [
                    0,
                    29
                  ]
                }
              ]
            },
            "description": {
              "urls": [
    
              ]
            }
          },
          "default_profile": false,
          "contributors_enabled": false,
          "favourites_count": 11,
          "url": "http://about.me/michaelangelo",
          "profile_image_url_https": "https://si0.twimg.com/profile_images/1305509670/chatMikeTwitter_normal.png",
          "utc_offset": 28800,
          "id": 15181205,
          "profile_use_background_image": true,
          "listed_count": 61,
          "profile_text_color": "333333",
          "lang": "en",
          "followers_count": 577,
          "protected": false,
          "notifications": null,
          "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme14/bg.gif",
          "profile_background_color": "131516",
          "verified": false,
          "geo_enabled": true,
          "time_zone": "Hong Kong",
          "description": "Android Applications Developer,  Studying Martial Arts, Plays MTG, Food and movie junkie",
          "default_profile_image": false,
          "profile_background_image_url": "http://a0.twimg.com/images/themes/theme14/bg.gif",
          "statuses_count": 11327,
          "friends_count": 138,
          "following": null,
          "show_all_inline_media": true,
          "screen_name": "mikedroid"
        },
        "in_reply_to_screen_name": null,
        "source": "Twitter for Android",
        "in_reply_to_status_id": null
      }
    ]

GET statuses/user\_timeline

get-statuses-user\_timeline

GET statuses/user\_timeline
===========================

**Important notice:** On June 19, 2019, we began enforcing a limit of 100,000 requests per day to the /statuses/user\_timeline endpoint, in addition to existing user-level and app-level rate limits. This limit is applied on a per-application basis, meaning that a single developer app can make up to 100,000 calls during any single 24-hour period.

Returns a collection of the most recent [Tweets](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object) posted by the [user](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object) indicated by the `screen_name` or `user_id` parameters.

User timelines belonging to protected users may only be requested when the authenticated user either "owns" the timeline or is an approved follower of the owner.

The timeline returned is the equivalent of the one seen as a user's profile on Twitter.

This method can only return up to 3,200 of a user's most recent Tweets. Native retweets of other statuses by the user is included in this total, regardless of whether `include_rts` is set to `false` when requesting this resource.

See [Working with Timelines](https://developer.twitter.com/en/docs/tweets/timelines/guides/working-with-timelines) for instructions on traversing timelines.

See [Embedded Timelines](https://developer.twitter.com/web/embedded-timelines), [Embedded Tweets](https://developer.twitter.com/web/embedded-tweets), and [GET statuses/oembed](https://developer.twitter.com/rest/reference/get/statuses/oembed) for tools to render Tweets according to [Display Requirements](https://about.twitter.com/company/display-requirements).

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/statuses/user_timeline.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 900 |
| Requests / 15-min window (app auth) | 1500 |
| Requests / 24-hour window | 100,000 |
| Supports Edit Tweets feature? | Yes |

_Note:_ the 24-hour request limit is based on a rolling clock, beginning at the time of the first request and monitored for the next 24 hours.

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| user\_id | optional | The ID of the user for whom to return results. |     | _12345_ |
| screen\_name | optional | The screen name of the user for whom to return results. |     | _noradio_ |
| since\_id | optional | Returns results with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets that can be accessed through the API. If the limit of Tweets has occured since the since\_id, the since\_id will be forced to the oldest ID available. |     | _12345_ |
| count | optional | Specifies the number of Tweets to try and retrieve, up to a maximum of 200 per distinct request. The value of _count_ is best thought of as a limit to the number of Tweets to return because suspended or deleted content is removed after the count has been applied. We include retweets in the count, even if _include\_rts_ is not supplied. It is recommended you always send _include\_rts=1_ when using this API method. |     |     |
| max\_id | optional | Returns results with an ID less than (that is, older than) or equal to the specified ID. |     | _54321_ |
| trim\_user | optional | When set to either _true_ , _t_ or _1_ , each Tweet returned in a timeline will include a user object including only the status authors numerical ID. Omit this parameter to receive the complete user object. |     | _true_ |
| exclude\_replies | optional | This parameter will prevent replies from appearing in the returned timeline. Using _exclude\_replies_ with the _count_ parameter will mean you will receive up-to count tweets — this is because the _count_ parameter retrieves that many Tweets before filtering out retweets and replies. |     | _true_ |
| include\_rts | optional | When set to _false_ , the timeline will strip any native retweets (though they will still count toward both the maximal length of the timeline and the slice selected by the count parameter). Note: If you're using the trim\_user parameter in conjunction with include\_rts, the retweets will still contain a full user object. |     | _false_ |
| include\_ext\_edit\_control | optional | Must be set to true in order to return edited Tweet metadata as part of the Tweet object.<br><br>`include_ext_edit_control=true`<br><br>Note that historical Tweets may not contain edited Tweet metadata.<br><br>To learn more about how edited Tweets are supported, see the [Edit Tweets fundamentals](https://developer.twitter.com/en/docs/twitter-api/v1/edit-tweets) page. |     | _true_ |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`GET https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=twitterapi&count=2`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    [
      {
        "created_at": "Thu Apr 06 15:28:43 +0000 2017",
        "id": 850007368138018817,
        "id_str": "850007368138018817",
        "text": "RT @TwitterDev: 1/ Today we’re sharing our vision for the future of the Twitter API platform!nhttps://t.co/XweGngmxlP",
        "truncated": false,
        "entities": {
          "hashtags": [],
          "symbols": [],
          "user_mentions": [
            {
              "screen_name": "TwitterDev",
              "name": "TwitterDev",
              "id": 2244994945,
              "id_str": "2244994945",
              "indices": [
                3,
                14
              ]
            }
          ],
          "urls": [
            {
              "url": "https://t.co/XweGngmxlP",
              "expanded_url": "https://cards.twitter.com/cards/18ce53wgo4h/3xo1c",
              "display_url": "cards.twitter.com/cards/18ce53wg…",
              "indices": [
                94,
                117
              ]
            }
          ]
        },
        "source": "<a href="http://twitter.com" rel="nofollow">Twitter Web Client</a>",
        "in_reply_to_status_id": null,
        "in_reply_to_status_id_str": null,
        "in_reply_to_user_id": null,
        "in_reply_to_user_id_str": null,
        "in_reply_to_screen_name": null,
        "user": {
          "id": 6253282,
          "id_str": "6253282",
          "name": "Twitter API",
          "screen_name": "twitterapi",
          "location": "San Francisco, CA",
          "description": "The Real Twitter API. I tweet about API changes, service issues and happily answer questions about Twitter and our API. Don't get an answer? It's on my website.",
          "url": "http://t.co/78pYTvWfJd",
          "entities": {
            "url": {
              "urls": [
                {
                  "url": "http://t.co/78pYTvWfJd",
                  "expanded_url": "https://dev.twitter.com",
                  "display_url": "dev.twitter.com",
                  "indices": [
                    0,
                    22
                  ]
                }
              ]
            },
            "description": {
              "urls": []
            }
          },
          "protected": false,
          "followers_count": 6172353,
          "friends_count": 46,
          "listed_count": 13091,
          "created_at": "Wed May 23 06:01:13 +0000 2007",
          "favourites_count": 26,
          "utc_offset": -25200,
          "time_zone": "Pacific Time (US & Canada)",
          "geo_enabled": true,
          "verified": true,
          "statuses_count": 3583,
          "lang": "en",
          "contributors_enabled": false,
          "is_translator": false,
          "is_translation_enabled": false,
          "profile_background_color": "C0DEED",
          "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/656927849/miyt9dpjz77sc0w3d4vj.png",
          "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/656927849/miyt9dpjz77sc0w3d4vj.png",
          "profile_background_tile": true,
          "profile_image_url": "http://pbs.twimg.com/profile_images/2284174872/7df3h38zabcvjylnyfe3_normal.png",
          "profile_image_url_https": "https://pbs.twimg.com/profile_images/2284174872/7df3h38zabcvjylnyfe3_normal.png",
          "profile_banner_url": "https://pbs.twimg.com/profile_banners/6253282/1431474710",
          "profile_link_color": "0084B4",
          "profile_sidebar_border_color": "C0DEED",
          "profile_sidebar_fill_color": "DDEEF6",
          "profile_text_color": "333333",
          "profile_use_background_image": true,
          "has_extended_profile": false,
          "default_profile": false,
          "default_profile_image": false,
          "following": true,
          "follow_request_sent": false,
          "notifications": false,
          "translator_type": "regular"
        },
        "geo": null,
        "coordinates": null,
        "place": null,
        "contributors": null,
        "retweeted_status": {
          "created_at": "Thu Apr 06 15:24:15 +0000 2017",
          "id": 850006245121695744,
          "id_str": "850006245121695744",
          "text": "1/ Today we’re sharing our vision for the future of the Twitter API platform!nhttps://t.co/XweGngmxlP",
          "truncated": false,
          "entities": {
            "hashtags": [],
            "symbols": [],
            "user_mentions": [],
            "urls": [
              {
                "url": "https://t.co/XweGngmxlP",
                "expanded_url": "https://cards.twitter.com/cards/18ce53wgo4h/3xo1c",
                "display_url": "cards.twitter.com/cards/18ce53wg…",
                "indices": [
                  78,
                  101
                ]
              }
            ]
          },
          "source": "<a href="http://twitter.com" rel="nofollow">Twitter Web Client</a>",
          "in_reply_to_status_id": null,
          "in_reply_to_status_id_str": null,
          "in_reply_to_user_id": null,
          "in_reply_to_user_id_str": null,
          "in_reply_to_screen_name": null,
          "user": {
            "id": 2244994945,
            "id_str": "2244994945",
            "name": "TwitterDev",
            "screen_name": "TwitterDev",
            "location": "Internet",
            "description": "Your official source for Twitter Platform news, updates & events. Need technical help? Visit https://t.co/mGHnxZCxkt ⌨️  #TapIntoTwitter",
            "url": "https://t.co/66w26cua1O",
            "entities": {
              "url": {
                "urls": [
                  {
                    "url": "https://t.co/66w26cua1O",
                    "expanded_url": "https://dev.twitter.com/",
                    "display_url": "dev.twitter.com",
                    "indices": [
                      0,
                      23
                    ]
                  }
                ]
              },
              "description": {
                "urls": [
                  {
                    "url": "https://t.co/mGHnxZCxkt",
                    "expanded_url": "https://twittercommunity.com/",
                    "display_url": "twittercommunity.com",
                    "indices": [
                      93,
                      116
                    ]
                  }
                ]
              }
            },
            "protected": false,
            "followers_count": 465425,
            "friends_count": 1523,
            "listed_count": 1168,
            "created_at": "Sat Dec 14 04:35:55 +0000 2013",
            "favourites_count": 2098,
            "utc_offset": -25200,
            "time_zone": "Pacific Time (US & Canada)",
            "geo_enabled": true,
            "verified": true,
            "statuses_count": 3031,
            "lang": "en",
            "contributors_enabled": false,
            "is_translator": false,
            "is_translation_enabled": false,
            "profile_background_color": "FFFFFF",
            "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
            "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
            "profile_background_tile": false,
            "profile_image_url": "http://pbs.twimg.com/profile_images/530814764687949824/npQQVkq8_normal.png",
            "profile_image_url_https": "https://pbs.twimg.com/profile_images/530814764687949824/npQQVkq8_normal.png",
            "profile_banner_url": "https://pbs.twimg.com/profile_banners/2244994945/1396995246",
            "profile_link_color": "0084B4",
            "profile_sidebar_border_color": "FFFFFF",
            "profile_sidebar_fill_color": "DDEEF6",
            "profile_text_color": "333333",
            "profile_use_background_image": false,
            "has_extended_profile": false,
            "default_profile": false,
            "default_profile_image": false,
            "following": true,
            "follow_request_sent": false,
            "notifications": false,
            "translator_type": "regular"
          },
          "geo": null,
          "coordinates": null,
          "place": null,
          "contributors": null,
          "is_quote_status": false,
          "retweet_count": 284,
          "favorite_count": 399,
          "favorited": false,
          "retweeted": false,
          "possibly_sensitive": false,
          "lang": "en"
        },
        "is_quote_status": false,
        "retweet_count": 284,
        "favorite_count": 0,
        "favorited": false,
        "retweeted": false,
        "possibly_sensitive": false,
        "lang": "en"
      },
      {
        "created_at": "Mon Apr 03 16:09:50 +0000 2017",
        "id": 848930551989915648,
        "id_str": "848930551989915648",
        "text": "RT @TwitterMktg: Starting today, businesses can request and share locations when engaging with people in Direct Messages. https://t.co/rpYn…",
        "truncated": false,
        "entities": {
          "hashtags": [],
          "symbols": [],
          "user_mentions": [
            {
              "screen_name": "TwitterMktg",
              "name": "Twitter Marketing",
              "id": 357750891,
              "id_str": "357750891",
              "indices": [
                3,
                15
              ]
            }
          ],
          "urls": []
        },
        "source": "<a href="http://twitter.com" rel="nofollow">Twitter Web Client</a>",
        "in_reply_to_status_id": null,
        "in_reply_to_status_id_str": null,
        "in_reply_to_user_id": null,
        "in_reply_to_user_id_str": null,
        "in_reply_to_screen_name": null,
        "user": {
          "id": 6253282,
          "id_str": "6253282",
          "name": "Twitter API",
          "screen_name": "twitterapi",
          "location": "San Francisco, CA",
          "description": "The Real Twitter API. I tweet about API changes, service issues and happily answer questions about Twitter and our API. Don't get an answer? It's on my website.",
          "url": "http://t.co/78pYTvWfJd",
          "entities": {
            "url": {
              "urls": [
                {
                  "url": "http://t.co/78pYTvWfJd",
                  "expanded_url": "https://dev.twitter.com",
                  "display_url": "dev.twitter.com",
                  "indices": [
                    0,
                    22
                  ]
                }
              ]
            },
            "description": {
              "urls": []
            }
          },
          "protected": false,
          "followers_count": 6172353,
          "friends_count": 46,
          "listed_count": 13091,
          "created_at": "Wed May 23 06:01:13 +0000 2007",
          "favourites_count": 26,
          "utc_offset": -25200,
          "time_zone": "Pacific Time (US & Canada)",
          "geo_enabled": true,
          "verified": true,
          "statuses_count": 3583,
          "lang": "en",
          "contributors_enabled": false,
          "is_translator": false,
          "is_translation_enabled": false,
          "profile_background_color": "C0DEED",
          "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/656927849/miyt9dpjz77sc0w3d4vj.png",
          "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/656927849/miyt9dpjz77sc0w3d4vj.png",
          "profile_background_tile": true,
          "profile_image_url": "http://pbs.twimg.com/profile_images/2284174872/7df3h38zabcvjylnyfe3_normal.png",
          "profile_image_url_https": "https://pbs.twimg.com/profile_images/2284174872/7df3h38zabcvjylnyfe3_normal.png",
          "profile_banner_url": "https://pbs.twimg.com/profile_banners/6253282/1431474710",
          "profile_link_color": "0084B4",
          "profile_sidebar_border_color": "C0DEED",
          "profile_sidebar_fill_color": "DDEEF6",
          "profile_text_color": "333333",
          "profile_use_background_image": true,
          "has_extended_profile": false,
          "default_profile": false,
          "default_profile_image": false,
          "following": true,
          "follow_request_sent": false,
          "notifications": false,
          "translator_type": "regular"
        },
        "geo": null,
        "coordinates": null,
        "place": null,
        "contributors": null,
        "retweeted_status": {
          "created_at": "Mon Apr 03 16:05:05 +0000 2017",
          "id": 848929357519241216,
          "id_str": "848929357519241216",
          "text": "Starting today, businesses can request and share locations when engaging with people in Direct Messages. https://t.co/rpYndqWfQw",
          "truncated": false,
          "entities": {
            "hashtags": [],
            "symbols": [],
            "user_mentions": [],
            "urls": [
              {
                "url": "https://t.co/rpYndqWfQw",
                "expanded_url": "https://cards.twitter.com/cards/5wzucr/3x700",
                "display_url": "cards.twitter.com/cards/5wzucr/3…",
                "indices": [
                  105,
                  128
                ]
              }
            ]
          },
          "source": "<a href="https://ads.twitter.com" rel="nofollow">Twitter Ads</a>",
          "in_reply_to_status_id": null,
          "in_reply_to_status_id_str": null,
          "in_reply_to_user_id": null,
          "in_reply_to_user_id_str": null,
          "in_reply_to_screen_name": null,
          "user": {
            "id": 357750891,
            "id_str": "357750891",
            "name": "Twitter Marketing",
            "screen_name": "TwitterMktg",
            "location": "Twitter HQ ",
            "description": "Twitter’s place for marketers, agencies, and creative thinkers ⭐ Bringing you insights, news, updates, and inspiration. Visit @TwitterAdsHelp for Ads support.",
            "url": "https://t.co/Tfo4moo92y",
            "entities": {
              "url": {
                "urls": [
                  {
                    "url": "https://t.co/Tfo4moo92y",
                    "expanded_url": "https://marketing.twitter.com",
                    "display_url": "marketing.twitter.com",
                    "indices": [
                      0,
                      23
                    ]
                  }
                ]
              },
              "description": {
                "urls": []
              }
            },
            "protected": false,
            "followers_count": 924546,
            "friends_count": 661,
            "listed_count": 3893,
            "created_at": "Thu Aug 18 21:08:15 +0000 2011",
            "favourites_count": 1934,
            "utc_offset": -25200,
            "time_zone": "Pacific Time (US & Canada)",
            "geo_enabled": true,
            "verified": true,
            "statuses_count": 6329,
            "lang": "en",
            "contributors_enabled": false,
            "is_translator": false,
            "is_translation_enabled": false,
            "profile_background_color": "C0DEED",
            "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/662767273/jvmxdpdrplhxcw8yvkv2.png",
            "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/662767273/jvmxdpdrplhxcw8yvkv2.png",
            "profile_background_tile": true,
            "profile_image_url": "http://pbs.twimg.com/profile_images/800953549697888256/UlXXL5h5_normal.jpg",
            "profile_image_url_https": "https://pbs.twimg.com/profile_images/800953549697888256/UlXXL5h5_normal.jpg",
            "profile_banner_url": "https://pbs.twimg.com/profile_banners/357750891/1487188210",
            "profile_link_color": "19CF86",
            "profile_sidebar_border_color": "FFFFFF",
            "profile_sidebar_fill_color": "DDEEF6",
            "profile_text_color": "333333",
            "profile_use_background_image": true,
            "has_extended_profile": false,
            "default_profile": false,
            "default_profile_image": false,
            "following": false,
            "follow_request_sent": false,
            "notifications": false,
            "translator_type": "none"
          },
          "geo": null,
          "coordinates": null,
          "place": null,
          "contributors": null,
          "is_quote_status": false,
          "retweet_count": 111,
          "favorite_count": 162,
          "favorited": false,
          "retweeted": false,
          "possibly_sensitive": false,
          "lang": "en"
        },
        "is_quote_status": false,
        "retweet_count": 111,
        "favorite_count": 0,
        "favorited": false,
        "retweeted": false,
        "lang": "en"
      }
    ]

Overview

**Please note:**  

We recently released [filtered stream](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream), a set of [Twitter API v2](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api) endpoints that has similar functionality to this one. The new version is now ready for production and serves adequate access for the majority of developers on our platform.

This endpoint is now deprecated and has NOT been updated to include Tweet edit metadata. Learn more about these metadata on the ["Edit Tweets" fundamentals page](https://developer.twitter.com/en/docs/twitter-api/v1/edit-tweets).   

We have deprecated the delivery of compliance messages through this endpoint. Apps created after April 29, 2022 cannot access this endpoint. This endpoint will stop delivering compliance messages beginning October 31, 2022. [Learn more about this change](https://twittercommunity.com/t/deprecation-announcement-removing-compliance-messages-from-statuses-filter-and-retiring-statuses-sample-from-the-twitter-api-v1-1/170500) and see our [migration resources](https://developer.twitter.com/en/docs/twitter-api/tweets/volume-streams/migrate).

Developers in need of higher levels of access can explore our [enterprise PowerTrack API](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/overview). You can see an overview of our filtered stream offerings on our [filtered stream overview](https://developer.twitter.com/en/docs/twitter-api/filtered-stream-overview) page, and see what's new with v2 by visiting the [migration guide](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/migrate).  

Overview
--------

Standard

Returns public statuses that match one or more filter predicates. Multiple parameters may be specified which allows most clients to use a single connection to the Streaming API. Both GET and POST requests are supported, but GET requests with too many parameters may cause the request to be rejected for excessive URL length. Use a POST request to avoid long URLs.

The track, follow, and locations fields should be considered to be combined with an OR operator. track=foo&follow=1234 returns Tweets matching “foo” OR created by user 1234.

The default access level allows up to 400 track keywords, 5,000 follow userids and 25 0.1-360 degree location boxes. If you need more access to the Streaming API, please use the enterprise streaming API, [PowerTrack](https://developer.twitter.com/en/docs/tweets/filter-realtime/overview/powertrack-api).  
 

Streaming message types
-----------------------

### Standard 'Track' stream messages

In addition to [standard Tweet payloads](https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/tweet.html), the following kinds of messages may be delivered on a stream. Note that this list may not be comprehensive—additional objects may be introduced into streams in the future. Ensure that your parser is tolerant of unexpected message formats.

When parsing Tweets, keep in mind that Retweets are streamed as a status with another status nested inside it. If you are matching Tweet fields using regular expressions, it is possible that you will match fields in the nested Tweet instead of the wrapper. As a rule of thumb it is better to use a JSON parser to extract information from message payloads.

#### Maintenance Messages

#### Blank lines

On slow streams, some messages may be blank lines (\\r\\n or similar) which serve as “keep-alive” signals to prevent clients and other network infrastructure from assuming the stream has stalled and closing the connection.

#### Limit notices (limit)

These messages indicate that a filtered stream has matched more Tweets than its current rate limit allows to be delivered. Limit notices contain a total count of the number of undelivered Tweets since the connection was opened, making them useful for tracking counts of track terms, for example. Note that the counts do not specify which filter predicates undelivered messages matched.

{  
"limit":{  
"track":1234  
}  
}

#### Disconnect messages (disconnect)

Streams may be shut down for a variety of reasons. The streaming API will attempt to deliver a message indicating why a stream was closed. Note that if the disconnect was due to network issues or a client reading too slowly, it is possible that this message will not be received.

{  
"disconnect":{  
"code": 4,  
"stream\_name":"",  
"reason":""  
}  
}

The following table lists possible status codes and their meanings. Additional codes may be used without warning.

| Code | Name | Description |
| --- | --- | --- |
| 1   | Shutdown | The feed was shutdown (possibly a machine restart) |
| 2   | Duplicate stream | The same endpoint was connected too many times. |
| 4   | Stall | The client was reading too slowly and was disconnected by the server. |
| 5   | Normal | The client appeared to have initiated a disconnect. |
| 7   | Admin logout | The same credentials were used to connect a new stream and the oldest was disconnected. |
| 9   | Max message limit | The stream connected with a negative count parameter and was disconnected after all backfill was delivered. |
| 10  | Stream exception | An internal issue disconnected the stream. |
| 11  | Broker stall | An internal issue disconnected the stream. |
| 12  | Shed load | The host the stream was connected to became overloaded and streams were disconnected to balance load. Reconnect as usual. |

#### Stall warnings (warning)

When connected to a stream using the stall\_warnings parameter, you may receive status notices indicating the current health of the connection. See the [stall\_warnings](https://developer.twitter.com/en/docs/tweets/rules-and-filtering/overview/basic-operators.html) documentation for more information.

{  
"warning":{  
"code":"FALLING\_BEHIND",  
"message":"Your connection is falling behind and messages are being queued for delivery to you. Your queue is now over 60% full. You will be disconnected when the queue is full.",  
"percent\_full": 60  
}  
}

### Compliance Messages

#### Status deletion notices (delete)

These messages indicate that a given Tweet has been deleted. Client code must honor these messages by clearing the referenced Tweet from memory and any storage or archive, even in the rare case where a deletion message arrives earlier in the stream that the Tweet it references.

{  
"delete":{  
"status":{  
"id":1234,  
"id\_str":"1234",  
"user\_id":3,  
"user\_id\_str":"3"  
}  
}  
}

#### Location deletion notices (scrub\_geo)

These messages indicate that geolocated data must be stripped from a range of Tweets. Clients must honor these messages by deleting geocoded data from Tweets which fall before the given status ID and belong to the specified user. These messages may also arrive before a Tweet which falls into the specified range, although this is rare.

{  
"scrub\_geo":{  
"user\_id":14090452,  
"user\_id\_str":"14090452",  
"up\_to\_status\_id":23260136625,  
"up\_to\_status\_id\_str":"23260136625"  
}  
}

#### Withheld content notices (status\_withheld, user\_withheld)

These messages indicate that either the indicated Tweet or indicated user has had their content withheld.

#### status\_withheld[¶](https://aem-author-staging.twitter.biz/editor.html/content/developer-twitter/en_US/docs/imported/developer-twitter-com/streaming/overview/messages-types.html#status-withheld "Permalink to this headline")

These events contain an id field indicating the status ID, a user\_id indicating the user, and a collection of withheld\_in\_countries uppercase two-letter country codes. This example illustrates a hypothetical Tweet that has been withheld in Germany and Argentina.

{  
"status\_withheld":{  
"id":1234567890,  
"user\_id":123456,  
"withheld\_in\_countries":\["DE", "AR"\]  
}  
}

#### user\_withheld[¶](https://aem-author-staging.twitter.biz/editor.html/content/developer-twitter/en_US/docs/imported/developer-twitter-com/streaming/overview/messages-types.html#user-withheld "Permalink to this headline")

These events contain an id field indicating the user ID and a collection of withheld\_in\_countries uppercase two-letter country codes. This example illustrates a hypothetical user who has been withheld in Germany and Argentina.

{  
"user\_withheld":{  
"id":123456,  
"withheld\_in\_countries":\["DE","AR"\]  
}  
}

#### User update

Everytime a user updates their profile we broadcast a user\_update event to indicate that an update has been made to the user profile. The source and target objects are identical in content.

{  
"created\_at": "Tue Aug 06 02:23:21 +0000 2013",  
"source": {  
...  
},  
"target": {  
...  
},  
"event": "user\_update"  
}

Streaming message types

**Please note:**  

We launched a [new version of the POST statuses/filter endpoint](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/introduction) as part of [Twitter API v2: Early Access](https://developer.twitter.com/en/docs/twitter-api/early-access). If you are currently using this endpoint, you can use our [migration materials](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/migrate/standard-to-twitter-api-v2) to start working with the newer version.

To see all of Twitter's filtered stream endpoint offerings, please visit our [overview](https://developer.twitter.com/en/docs/twitter-api/filtered-stream-overview).

Streaming message types
=======================

Standard

Standard stream messages
------------------------

In addition to [standard Tweet payloads](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object.html), the following kinds of messages may be delivered on a stream. Note that this list may not be comprehensive—additional objects may be introduced into streams. Ensure that your parser is tolerant of unexpected message formats.

When parsing Tweets, keep in mind that Retweets are streamed as a status with another status nested inside it. If you are matching Tweet fields using regular expressions, it is possible that you will match fields in the nested Tweet instead of the wrapper. As a rule of thumb it is better to use a JSON parser to extract information from message payloads.

### Maintenance Messages

### Blank lines

On slow streams, some messages may be blank lines (\\r\\n or similar) which serve as “keep-alive” signals to prevent clients and other network infrastructure from assuming the stream has stalled and closing the connection.

### Limit notices (limit)

These messages indicate that a filtered stream has matched more Tweets than its current rate limit allows to be delivered. Limit notices contain a total count of the number of undelivered Tweets since the connection was opened, making them useful for tracking counts of track terms, for example. Note that the counts do not specify which filter predicates undelivered messages matched.

{  
"limit":{  
"track":1234  
}  
}

### Disconnect messages (disconnect)

Streams may be shut down for a variety of reasons. The streaming API will attempt to deliver a message indicating why a stream was closed. Note that if the disconnect was due to network issues or a client reading too slowly, it is possible that this message will not be received.

{  
"disconnect":{  
"code": 4,  
"stream\_name":"",  
"reason":""  
}  
}

The following table lists possible status codes and their meanings. Additional codes may be used without warning.

| Code | Name | Description |
| --- | --- | --- |
| 1   | Shutdown | The feed was shutdown (possibly a machine restart) |
| 2   | Duplicate stream | The same endpoint was connected too many times. |
| 4   | Stall | The client was reading too slowly and was disconnected by the server. |
| 5   | Normal | The client appeared to have initiated a disconnect. |
| 7   | Admin logout | The same credentials were used to connect a new stream and the oldest was disconnected. |
| 9   | Max message limit | The stream connected with a negative count parameter and was disconnected after all backfill was delivered. |
| 10  | Stream exception | An internal issue disconnected the stream. |
| 11  | Broker stall | An internal issue disconnected the stream. |
| 12  | Shed load | The host the stream was connected to became overloaded and streams were disconnected to balance load. Reconnect as usual. |

###   
Stall warnings (warning)

When connected to a stream using the stall\_warnings parameter, you may receive status notices indicating the current health of the connection. See the [stall\_warnings](https://developer.twitter.com/en/docs/tweets/rules-and-filtering/overview/basic-operators.html) documentation for more information.

{  
"warning":{  
"code":"FALLING\_BEHIND",  
"message":"Your connection is falling behind and messages are being queued for delivery to you. Your queue is now over 60% full. You will be disconnected when the queue is full.",  
"percent\_full": 60  
}  
}

### Compliance Messages

### Status deletion notices (delete)

These messages indicate that a given Tweet has been deleted. Client code _**must honor these messages**_ by clearing the referenced Tweet from memory and any storage or archive, even in the rare case where a deletion message arrives earlier in the stream than the Tweet it references.

{  
"delete":{  
"status":{  
"id":1234,  
"id\_str":"1234",  
"user\_id":3,  
"user\_id\_str":"3"  
}  
}  
}

### Location deletion notices (scrub\_geo)

These messages indicate that geolocated data must be stripped from a range of Tweets. Clients _**must honor these messages**_ by deleting geocoded data from Tweets which fall before the given status ID and belong to the specified user. These messages may also arrive before a Tweet which falls into the specified range, although this is rare.

{  
"scrub\_geo":{  
"user\_id":14090452,  
"user\_id\_str":"14090452",  
"up\_to\_status\_id":23260136625,  
"up\_to\_status\_id\_str":"23260136625"  
}  
}

### Withheld content notices (status\_withheld, user\_withheld)[](https://aem-author-staging.twitter.biz/editor.html/content/developer-twitter/en_US/docs/imported/developer-twitter-com/streaming/overview/messages-types.html#withheld-content-notices-status-withheld-user-withheld "Permalink to this headline")

These messages indicate that either the indicated Tweet or indicated user has had their content withheld.

#### status\_withheld[](https://aem-author-staging.twitter.biz/editor.html/content/developer-twitter/en_US/docs/imported/developer-twitter-com/streaming/overview/messages-types.html#status-withheld "Permalink to this headline")

These events contain an id field indicating the status ID, a user\_id indicating the user, and a collection of withheld\_in\_countries uppercase two-letter country codes. This example illustrates a hypothetical Tweet that has been withheld in Germany and Argentina.

{  
"status\_withheld":{  
"id":1234567890,  
"user\_id":123456,  
"withheld\_in\_countries":\["DE", "AR"\]  
}  
}

#### user\_withheld[](https://aem-author-staging.twitter.biz/editor.html/content/developer-twitter/en_US/docs/imported/developer-twitter-com/streaming/overview/messages-types.html#user-withheld "Permalink to this headline")

These events contain an id field indicating the user ID and a collection of withheld\_in\_countries uppercase two-letter country codes. This example illustrates a hypothetical user who has been withheld in Germany and Argentina.

{  
"user\_withheld":{  
"id":123456,  
"withheld\_in\_countries":\["DE","AR"\]  
}  
}

Connecting to a streaming endpoint

**Please note:**  

We launched a [new version of the POST statuses/filter endpoint](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/introduction) as part of [Twitter API v2: Early Access](https://developer.twitter.com/en/docs/twitter-api/early-access). If you are currently using this endpoint, you can use our [migration materials](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/migrate/standard-to-twitter-api-v2) to start working with the newer version.

To see all of Twitter's filtered stream endpoint offerings, please visit our [overview](https://developer.twitter.com/en/docs/twitter-api/filtered-stream-overview).

Connecting to a streaming endpoint
==================================

Standard

Establishing a connection to the streaming APIs means making a very long lived HTTP request, and parsing the response incrementally. Conceptually, you can think of it as downloading an infinitely long file over HTTP.

Authentication
--------------

The following authentication methods are supported by the Streaming APIs:

|     |     |     |
| --- | --- | --- |
| Auth Type | Supported APIs | Description |
| [OAuth](https://developer.twitter.com/en/docs/basics/authentication/overview/oauth.html) | * Track API Stream | Requests must be authorized [according to the OAuth specification](https://dev.twitter.com/oauth/overview/authorizing-requests) . |
| [Basic auth](https://developer.twitter.com/en/docs/basics/authentication/overview/basic-auth.html) | * PowerTrack API<br>* Decahose stream | Requests must use of HTTP Basic Authentication, constructed from a valid email address and password combination. |

Connecting
----------

To connect to the Streaming API, form a HTTP request and consume the resulting stream for as long as is practical. Our servers will hold the connection open indefinitely, barring server-side error, excessive client-side lag, network hiccups, routine server maintenance or duplicate logins.

The method to form an HTTP request and parse the response will be different for every language or framework, so consult the documentation for the HTTP library you are using.

Some HTTP client libraries only return the response body after the connection has been closed by the server. These clients will not work for accessing the Streaming API. You must use an HTTP client that will return response data incrementally. Most robust HTTP client libraries will provide this functionality. The [Apache HttpClient](http://hc.apache.org/httpcomponents-client-ga/) will handle this use case, for example.

Disconnections
--------------

Twitter will close a streaming connection for the following reasons:

* A client establishes too many connections with the same credentials. When this occurs, the oldest connection will be terminated. This means you have to be careful not to run two reconnecting clients in parallel with the same credentials, or else they will take turns disconnecting each other.
* A client stops reading data suddenly. If the rate of Tweets being read off of the stream drops suddenly, the connection will be closed.
* A client reads data too slowly. Every streaming connection is backed by a queue of messages to be sent to the client. If this queue grows too large over time, the connection will be closed.
* A streaming server is restarted. This is usually related to a code deploy and is not very frequent.
* Twitter’s network configuration changes. These events are rare, and would represent load balancer restarts or network reconfigurations, for example.

Stalls
------

Set a timer, either a 90 second TCP level socket timeout, or a 90 second application level timer on the receipt of new data. If 90 seconds pass with no data received, including newlines, disconnect and reconnect immediately according to the backoff strategies in the next section. The Streaming API will send a keep-alive newline every 30 seconds to prevent your application from timing out the connection. You should wait at least 3 cycles to prevent spurious reconnects in the event of network congestion, local CPU starvation, local GC pauses, etc.

Reconnecting
------------

Once an **established** connection drops, attempt to reconnect immediately. If the reconnect fails, slow down your reconnect attempts according to the type of error experienced:

* Back off linearly for **TCP/IP level network errors**. These problems are generally temporary and tend to clear quickly. Increase the delay in reconnects by 250ms each attempt, up to 16 seconds.
* Back off exponentially for **HTTP errors** for which reconnecting would be appropriate. Start with a 5 second wait, doubling each attempt, up to 320 seconds.
* Back off exponentially for **HTTP 420 errors**. Start with a 1 minute wait and double each attempt. Note that every HTTP 420 received increases the time you must wait until rate limiting will no longer will be in effect for your account.

Connection churn
----------------

Repeatedly opening and closing a connection (churn) wastes server resources. Keep your connections as stable and long-lived as possible.

Avoid mobile (cellular network) connections from mobile devices. WiFi is generally OK.

Delay opening a streaming connection in cases where the user may quit the application quickly.

If your client works in an environment where the connection quality changes over time, attempt to detect flaky connections. When detected, fall back to REST polling until the connection quality improves.

Rate limiting
-------------

Clients which do not implement backoff and attempt to reconnect as often as possible will have their connections rate limited for a small number of minutes. Rate limited clients will receive HTTP 420 responses for all connection requests.

Clients which break a connection and then reconnect frequently (to change query parameters, for example) run the risk of being rate limited.

Twitter does not make public the number of connection attempts which will cause a rate limiting to occur, but there is some tolerance for testing and development. A few dozen connection attempts from time to time will not trigger a limit. However, it is essential to stop further connection attempts for a few minutes if a HTTP 420 response is received. If your client is rate limited frequently, it is possible that your IP will be blocked from accessing Twitter for an indeterminate period of time.

Best practices
--------------

### Test backoff strategies

A good way to test a backoff implementation is to use invalid authorization credentials and examine the reconnect attempts. A good implementation will not get any 420 responses.

### Issue alerts for multiple reconnects

If a client reaches its upper threshold of its time between reconnects, it should send you notifications so you can triage the issues affecting your connection.

### Handle DNS changes

Test that your client process honors the DNS Time To live (TTL). Some stacks will cache a resolved address for the duration of the process and will not pick up DNS changes within the proscribed TTL. Such aggressive caching will lead to service disruptions on your client as Twitter shifts load between IP addresses.

### User Agent

Ensure your user-agent HTTP header includes the client’s version. This will be critical in diagnosing issues on Twitter’s end. If your environment precludes setting the user-agent field, then set an x-user-agent header.

HTTP Error Codes
----------------

Most error codes are returned with a string with additional details. For all codes greater than 200, clients should wait before attempting another connection. See the Connecting section, above.

|     |     |     |
| --- | --- | --- |
| Status | Text | Description |
| **200** | **Success** | Self evident. |
| **401** | **Unauthorized** | HTTP authentication failed due to either:<br><br>* Invalid basic auth credentials, or an invalid OAuth request.<br>* Out-of-sync timestamp in your OAuth request (the response body will indicate this).<br>* Too many incorrect passwords entered or other login rate limiting. |
| **403** | **Forbidden** | The connecting account is not permitted to access this endpoint. |
| **404** | **Unknown** | There is nothing at this URL, which means the resource does not exist. |
| **406** | **Not Acceptable** | At least one request parameter is invalid. For example, the filter endpoint returns this status if:<br><br>* The track keyword is too long or too short.<br>* An invalid bounding box is specified.<br>* Neither the track nor follow parameter are specified.<br>* The follow user ID is not valid. |
| **413** | **Too Long** | A parameter list is too long. For example, the filter endpoint returns this status if:<br><br>* More track values are sent than the user is allowed to use.<br>* More bounding boxes are sent than the user is allowed to use.<br>* More follow user IDs are sent than the user is allowed to follow. |
| **416** | **Range Unacceptable** | For example, an endpoint returns this status if:<br><br>* A count parameter is specified but the user does not have access to use the count parameter.<br>* A count parameter is specified which is outside of the maximum/minimum allowable values. |
| **420** | **Rate Limited** | The client has connected too frequently. For example, an endpoint returns this status if:<br><br>* A client makes too many login attempts in a short period of time.<br>* Too many copies of an application attempt to authenticate with the same credentials. |
| **503** | **Service Unavailable** | A streaming server is temporarily overloaded. Attempt to make another connection, keeping in mind the connection attempt rate limiting and possible DNS caching in your client. |

Standard stream parameters

**Please note:**  

We launched a [new version of the POST statuses/filter endpoint](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/introduction) as part of [Twitter API v2: Early Access](https://developer.twitter.com/en/docs/twitter-api/early-access). If you are currently using this endpoint, you can use our [migration materials](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/migrate/standard-to-twitter-api-v2) to start working with the newer version.

To see all of Twitter's filtered stream endpoint offerings, please visit our [overview](https://developer.twitter.com/en/docs/twitter-api/filtered-stream-overview).

Standard streaming API request parameters
-----------------------------------------

Standard

1. delimited
2. stall\_warnings
3. filter\_level
4. language
5. follow
6. track
7. locations
8. count
9. with (deprecated)
10. replies (deprecated)
11. stringify\_friend\_id (deprecated)

Use the following request parameters to define what data is returned by the Streaming API endpoints:

### delimited

This parameter may be used on all streaming endpoints, unless explicitly noted.

Setting this to the string length indicates that statuses should be delimited in the stream, so that clients know how many bytes to read before the end of the status message. Statuses are represented by a length, in bytes, a newline, and the status text that is exactly length bytes. Note that “keep-alive” newlines may be inserted before each length.

As an example, consider this response to a request to https://stream.twitter.com/1.1/statuses/filter.json?delimited=length&track=twitterapi:

The 1953 indicates how many bytes to read off of the stream to get the rest of the Tweet (including rn). The next length delimiter will occur exactly after 1953 bytes.

### stall\_warnings

This parameter may be used on all streaming endpoints, unless explicitly noted.

Setting this parameter to the string true will cause periodic messages to be delivered if the client is in danger of being disconnected. These messages are only sent when the client is falling behind, and will occur at a maximum rate of about once every 5 minutes. This parameter is most appropriate for clients with high-bandwidth connections.

Such warning messages will look like:

    {
      "warning":{
        "code":"FALLING_BEHIND",
        "message":"Your connection is falling behind and messages are being queued for delivery to you. Your queue is now over 60% full. You will be disconnected when the queue is full.",
        "percent_full": 60
      }
    }

### filter\_level

This parameter may be used on all streaming endpoints, unless explicitly noted.

Setting this parameter to one of none, low, or medium will set the minimum value of the filter\_level Tweet attribute required to be included in the stream. The default value is none, which includes all available Tweets.

When displaying a stream of Tweets to end users (dashboards or live feeds at a presentation or conference, for example) it is suggested that you set this value to medium.

### language

This parameter may be used on all streaming endpoints, unless explicitly noted.

Setting this parameter to a comma-separated list of [BCP 47](http://tools.ietf.org/html/bcp47) language identifiers corresponding to any of the languages listed on Twitter’s [advanced search](https://twitter.com/search-advanced) page will only return Tweets that have been detected as being written in the specified languages. For example, connecting with language=en will only stream Tweets detected to be in the English language.

### follow

A comma-separated list of user IDs, indicating the users whose Tweets should be delivered on the stream. Following protected users is not supported. For each user specified, the stream will contain:

* Tweets created by the user.
* Tweets which are retweeted by the user.
* Replies to any Tweet created by the user.
* Retweets of any Tweet created by the user.
* Manual replies, created without pressing a reply button (e.g. “@twitterapi I agree”).

The stream will not contain:

* Tweets mentioning the user (e.g. “Hello @twitterapi!”).
* Manual Retweets created without pressing a Retweet button (e.g. “RT @twitterapi The API is great”).
* Tweets by protected users.

### track

A comma-separated list of phrases which will be used to determine what Tweets will be delivered on the stream. A phrase may be one or more terms separated by spaces, and a phrase will match if all of the terms in the phrase are present in the Tweet, regardless of order and ignoring case. By this model, you can think of commas as logical ORs, while spaces are equivalent to logical ANDs (e.g. ‘the twitter’ is the AND twitter, and ‘the,twitter’ is the OR twitter).

The text of the Tweet and some entity fields are considered for matches. Specifically, the text attribute of the Tweet, expanded\_url and display\_url for links and media, text for hashtags, and screen\_name for user mentions are checked for matches.

Each phrase must be between 1 and 60 bytes, inclusive.

Exact matching of phrases (equivalent to quoted phrases in most search engines) is not supported.

Punctuation and special characters will be considered part of the term they are adjacent to. In this sense, “hello.” is a different track term than “hello”. However, matches will ignore punctuation present in the Tweet. So “hello” will match both “hello world” and “my brother says hello.” Note that punctuation is not considered to be part of a #hashtag or @mention, so a track term containing punctuation will not match either #hashtags or @mentions.

UTF-8 characters will match exactly, even in cases where an “equivalent” ASCII character exists. For example, “touché” will not match a Tweet containing “touche”.

Non-space separated languages, such as CJK are currently unsupported.

URLs are considered words for the purposes of matches which means that the entire domain and path must be included in the track query for a Tweet containing an URL to match. Note that display\_url does not contain a protocol, so this is not required to perform a match.

Twitter currently canonicalizes the domain “www.example.com” to “example.com” before the match is performed, so omit the “www” from URL track terms.

Finally, to address a common use case where you may want to track all mentions of a particular domain name (i.e., regardless of subdomain or path), you should use “example com” as the track parameter for “example.com” (notice the lack of period between “example” and “com” in the track parameter). This will be over-inclusive, so make sure to do additional pattern-matching in your code. See the table below for more examples related to this issue.

Track examples:

|     |     |     |
| --- | --- | --- |
| Parameter value | Will match... | Will not match... |
| Twitter | TWITTERtwitter “Twitter” twitter. #twitter @twitter [http://twitter.com](http://twitter.com/) | TwitterTracker#newtwitter |
| Twitter’s | I like Twitter’s new design | Someday I’d like to visit @Twitter’s office |
| twitter api,twitter streaming | The Twitter API is awesomeThe twitter streaming service is fast Twitter has a streaming API | I’m new to Twitter |
| example.com | Someday I will visit example.com | There is no example.com/foobarbaz |
| example.com/foobarbaz | example.com/foobarbazwww.example.com/foobarbaz | example.com |
| www.example.com/foobarbaz |     | www.example.com/foobarbaz |
| example com | example.comwww.example.com foo.example.com foo.example.com/bar I hope my startup isn’t merely another example of a dot com boom! |     |

### locations

A comma-separated list of longitude,latitude pairs specifying a set of bounding boxes to filter Tweets by. Only geolocated Tweets falling within the requested bounding boxes will be included—unlike the Search API, the user’s location field is not used to filter Tweets.

Each bounding box should be specified as a pair of longitude and latitude pairs, with the southwest corner of the bounding box coming first. For example:

|     |     |
| --- | --- |
| Parameter value | Tracks Tweets from... |
| \-122.75,36.8,-121.75,37.8 | San Francisco |
| \-74,40,-73,41 | New York City |
| \-122.75,36.8,-121.75,37.8,-74,40,-73,41 | San FranciscoOR New York City |

Bounding boxes do not act as filters for other filter parameters. For example track=twitter&locations=-122.75,36.8,-121.75,37.8 would match any Tweets containing the term Twitter (even non-geo Tweets) OR coming from the San Francisco area.

The streaming API uses the following heuristic to determine whether a given Tweet falls within a bounding box:

* If the coordinates field is populated, the values there will be tested against the bounding box. Note that this field uses geoJSON order (longitude, latitude).
* If coordinates is empty but place is populated, the region defined in place is checked for intersection against the locations bounding box. Any overlap will match.
* If none of the rules listed above match, the Tweet does not match the location query. Note that the geo field is deprecated, and ignored by the streaming API.

If you would like to exclude place matches or only include places which fall completely within the bounding box, your code will have to perform an additional filtering step after reading the filtered stream.

Note that native Retweets are not matched by this parameter. While the original Tweet may have a location, the Retweet will not.

### count

This parameter requires elevated access to use.

When reconnecting to a streaming endpoint, elevated access clients may include the count parameter to attempt to backfill missed messages which occurred during the disconnect period. The supplied value may be an integer from 1 to 150000 or from -1 to -150000. If a positive number is specified, the stream will transition to live values once the backfill has been delivered to the client. If a negative number is specified, the stream will disconnect once the backfill has been delivered to the client, which may be useful for debugging.

Note that use of this parameter should be carefully considered, as high values increase the chance of a subsequent disconnect. To demonstrate this, consider the case where a client connects without backfill. Upon establishing a connection, Twitter will allocate a fixed-size queue, and begin adding messages to be streamed to the client. If the client reads too slowly, the queue will fill up. Once full, Twitter will disconnect the client:

When a client connects with backfill, that number of messages are immediately added to the queue. The client must read messages faster than the current rate of Tweets being added to the queue, as the available buffer before a disconnect occurs can be much smaller than when connecting without backfill.

### with (deprecated)

Available on User Streams and Site Streams (deprecated)

The with parameter controls the types of messages delivered to User and Site Streams clients.

* The default for Site Streams is with=user, which only streams messages from the user associated with the stream.
* The default for User Streams is with=followings which adds messages from accounts the user follows, equivalent to the user’s home timeline.

Despite the difference in defaults, Site and User each accept both user and followings parameter values.

### replies (deprecated)

Available on User Streams and Site Streams (deprectated)  

By default @replies are only sent if the current user follows both the sender and receiver of the reply. For example, consider the case where Alice follows Bob, but Alice doesn’t follow Carol. By default, if Bob @replies Carol, Alice does not see the Tweet. This mimics twitter.com and api.twitter.com behavior. To have such Tweets returned in a streaming connection, specify replies=all when connecting.

### stringify\_friend\_ids (deprecated)

Available on  User Streams and Site Streams (deprecated)  

By default, user and site streams send the [Friends List](https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-friends-list.html) preamble as an array of integers (equivalent to stringify\_friend\_ids=false). However, as the number of Twitter users grows, user ids are quickly approaching the 32-bit integer threshold, which when passed, will require your code to handle 64-bit integers. Some languages or libraries (including JSON decoders) expect that integers provided in JSON are 32-bit and will therefore have erroneous and potentially unpredictable behavior. If natively interpreting integers as 64-bit poses a challenge for you, we offer the stringify\_friend\_ids=true parameter to have the friends list preamble be an array of strings (instead of integers). If you use this parameter, note that it will suppress the friends array and return the friends\_str array in its place. See the [Friends List](https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-friends-list.html) message type entry for an example payload.

POST statuses/filter

post-statuses-filter

POST statuses/filter
====================

Returns public Tweets that match one or more filter predicates. Multiple parameters may be specified which allows most clients to use a single connection to the Streaming API. Both GET and POST requests are supported, but GET requests with too many parameters may cause the request to be rejected for excessive URL length. Use a POST request to avoid long URLs.

The track, follow, and locations fields should be considered to be combined with an OR operator. `track=foo&follow=1234` returns Tweets matching "foo" OR created by user 1234.

The default access level allows up to 400 track keywords, 5,000 follow userids and 25 0.1-360 degree location boxes. If you need access to more rules and filtering tools, please apply for [enterprise access](https://developer.twitter.com/en/enterprise).

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://stream.twitter.com/1.1/statuses/filter.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Supports Edit Tweets feature? | No  |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |
| --- | --- | --- |
| Name | Required | Description |
| follow | optional | A comma separated list of user IDs, indicating the users to return statuses for in the stream. See [follow](https://developer.twitter.com/en/docs/tweets/filter-realtime/guides/basic-stream-parameters) for more information. |
| track | optional | Keywords to track. Phrases of keywords are specified by a comma-separated list. See [track](https://developer.twitter.com/en/docs/tweets/filter-realtime/guides/basic-stream-parameters) for more information. |
| locations | optional | Specifies a set of bounding boxes to track. See [locations](https://developer.twitter.com/en/docs/tweets/filter-realtime/guides/basic-stream-parameters) for more information. |
| delimited | optional | Specifies whether messages should be length-delimited. See [delimited](https://developer.twitter.com/en/docs/tweets/filter-realtime/guides/basic-stream-parameters) for more information. |
| stall\_warnings | optional | Specifies whether stall warnings should be delivered. See [stall\_warnings](https://developer.twitter.com/en/docs/tweets/filter-realtime/guides/basic-stream-parameters) for more information. |
| include\_ext\_edit\_control | optional | Must be set to true in order to return edited Tweet metadata as part of the Tweet object. |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`GET https://stream.twitter.com/1.1/statuses/filter.json?track=twitter`

Overview

Collections
-----------

A collection is an editable group of Tweets hand-selected by a Twitter user or programmatically managed via collection APIs. Each collection is public and has its own page on twitter.com, making it easy to share and embed in your website and apps.  
 

### Create and edit a collection using TweetDeck

[TweetDeck](https://tweetdeck.twitter.com/) supports adding Tweets to a collection by simply dragging a Tweet into a collection column.

  

### View a collection on Twitter.com

Each collection has a public URL on Twitter.com. Share a collection with others by including it in a Tweet, email, or other share method.

Example: [https://twitter.com/NYTNow/timelines/576828964162965504](https://twitter.com/NYTNow/timelines/576828964162965504)  
 

### Embed a collection in your website or app

[Embed a collection on your website](https://dev.twitter.com/web/embedded-timelines/collection) using an HTML markup snippet generated by [publish.twitter.com](https://publish.twitter.com/).

[National Park Tweets - Curated tweets by TwitterDev](https://twitter.com/TwitterDev/timelines/539487832448843776)

About collections

### About Collections

Collections are a type of timeline that can be controlled and hand-curated, or programmed using an API.

As a unit, collections operate under the following rules:

* Collections are created by users.
* Each collection has a name and description.
* The collection creator can add any public Tweet to the collection.
* When new Tweets are added, they appear at the top of the collection.
* Collections are public, have their own URL on twitter.com, and are viewable by all.

By design, collections do not implement specific rules or logic for sourcing or adding Tweets, leaving that strategy entirely up to you. For example if you want a collection that sources Tweets from multiple lists + a search + your own secret sauce, you can build that easily using the API.

Differences with other methods
------------------------------

Those familiar with Twitter’s family of REST APIs may notice some differences in object structure compared to typical APIs.

Pay close attention to the differences in how collections are presented — often they will be decomposed, efficient objects with information about users, Tweets, and timelines grouped, simplified, and stripped of unnecessary repetition.

[Navigating collections](https://dev.twitter.com/rest/reference/get/collections/entries) also differs from the other APIs in that the collection is not strictly creation-time oriented. Navigating by since\_id and last\_id has been replaced with a position-based pagination system that should still be familiar.

See [Response structures](https://dev.twitter.com/rest/collections/responses) for a deeper overview of these differences.

Authenticating Requests
-----------------------

It is important to note that the Twitter API is strict about character encoding in OAuth 1.0a and HTTP. Reserved characters in query strings and application/x-www-form-urlencoded POST bodies must first be encoded according to RFC 3986.

OAuth 1.0a handles requests of other content-types slightly differently. A POST body that is not application/x-www-form-urlencoded is not considered as part of the parameters that will be encoded in the OAuth signature base string. Instead your signature base string will contain only any parameters contained on the query string and the oauth\_\* parameters that are typically part of the OAuth signature generation process. [POST collections / entries / curate](https://dev.twitter.com/rest/reference/get/collections/entries/curate) uses application/json POST bodies.

Working with the Collections API
--------------------------------

Use these methods to browse Collections, whether by ID, those owned by a specific user, or those containing a specific Tweet.

* [GET collections / list](https://dev.twitter.com/rest/reference/get/collections/list)
* [GET collections / show](https://dev.twitter.com/rest/reference/get/collections/show)

These methods allow you to create, modify, or delete a collection on behalf of the currently authenticated user.

* [POST collections / create](https://dev.twitter.com/rest/reference/post/collections/create)
* [POST collections / destroy](https://dev.twitter.com/rest/reference/post/collections/destroy)
* [POST collections / update](https://dev.twitter.com/rest/reference/post/collections/update)

To curate a collection, add or remove Tweets with these methods:

* [GET collections / entries](https://dev.twitter.com/rest/reference/get/collections/entries)
* [POST collections / entries / add](https://dev.twitter.com/rest/reference/post/collections/entries/add)
* [POST collections / entries / remove](https://dev.twitter.com/rest/reference/post/collections/entries/remove)
* [POST collections / entries / move](https://dev.twitter.com/rest/reference/post/collections/entries/move)
* [POST collections / entries / curate](https://dev.twitter.com/rest/reference/post/collections/entries/curate)

Collections on Twitter.com
--------------------------

Once created, Collections are available to view on twitter.com through a web and mobile-friendly permalink. Collections are meant to be shared with the world! Feel free to Tweet these permalink URLs to share your collection with followers.

Each Collections permalink is indicated in the custom\_timeline\_url field found in Collection timeline object responses.

Embedded Collections on the Web
-------------------------------

Collections are meant to be shared with the world, on and off Twitter. To that end, [embedded timelines](https://dev.twitter.com/web/embedded-timelines) have been expanded to support [embedded collections](https://dev.twitter.com/web/embedded-timelines/collection). Use the [widget configurator](https://twitter.com/settings/widgets/new/custom) to prepare your collections for syndication and receive the simple HTML & JavaScript embed code for your site.

[National Park Tweets](https://twitter.com/TwitterDev/timelines/539487832448843776)

Accounts with protected Tweets and Collections
----------------------------------------------

Some accounts on Twitter have enabled [a setting that “protects” the Tweets they create](https://support.twitter.com/articles/14016) for an approved audience of followers. Users with protected accounts can still use Collections, but with the following caveats:

* Protected accounts can create Collections but the Collections they create will be public.
* Public users can switch to a protected state, but their Collections will remain public.
* Any user can retrieve/discover Collections belonging to any other user, regardless of the Collection owner’s protected account status.
* Tweets created by users with protected accounts cannot be included in Collections.

Response structures

Response Structures
===================

The Collections API responds with data structures that often depart from the objects you traditionally encounter in the Twitter API.

In the Collections API, all identifiers (IDs, cursors, collection positions) are presented as strings. These strings are safe to consume and utilize in all programming languages, including those that do not support 64-bit integers.

While representations of [Tweets](https://dev.twitter.com/overview/api/tweets) and [Users](https://dev.twitter.com/overview/api/users) generally match other Twitter API representations, watch for minor differences in the object structure, especially around data related to counts.

While the API typically returns objects-embedded-within-objects (such as the author of a Tweet being embedded within the Tweet itself), these API methods provide decomposed responses where each object type is grouped together and each object is represented only once. Instead of containing associated child objects, the objects contain simple ID references to the association.

Here are some of the response structures you will encounter in the Collections API.

Object collections
------------------

API methods that return multiple objects of the same type are segmented such that one component of the response contains the objects and any associated objects while another component simply lists references to those same objects and contextual information (such as cursors) needed to navigate the boundaries of the collection in subsequent requests.

You will see responses like this in [GET collections / list](https://dev.twitter.com/rest/reference/get/collections/list).

### Structure

* response (object)
    * results (array of objects)
        * each object typically contains one key/value pair housing an object’s ID
    * cursors (object)
        * next\_cursor (string)
        * previous\_cursor (string)
* objects (object)
    * users (object, ID as key)
    * tweets (object, ID as key)
    * timelines (object, ID as key)

Single objects
--------------

Even methods that return a single “primary object” respond with a decomposed structure, similar to a collection.

Methods that can return only one core object:

You will see responses like this in: [GET collections / show](https://dev.twitter.com/rest/reference/get/collections/show)

### Structure

response (object)

* a key/value pair indicating the object’s type and identifier (e.g. "timeline\_id":"custom-393773270547177472")

objects (object)

* users (object, ID as key)
* tweets (object, ID as key)
* timelines (object, ID as key)

GET collections/entries

get-collections-entries

GET collections/entries
=======================

Retrieve the identified Collection, presented as a list of the Tweets curated within.

The response structure of this method differs significantly from timelines you may be used to working with elsewhere in the Twitter API.

To navigate a Collection, use the position object of a response, which includes attributes for `max_position`, `min_position`, and `was_truncated`. `was_truncated` indicates whether additional Tweets exist in the collection outside of the range of the current request. To retrieve Tweets further back in time, use the value of `min_position` found in the current response as the `max_position` parameter in the next call to this endpoint.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/collections/entries.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 1000 |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| id  | required | The identifier of the Collection for which to return results. |     | _custom-539487832448843776_ |
| count | optional | Specifies the _maximum_ number of results to include in the response. Specify a count between 1 and 200. A _next\_cursor_ value will be provided in the response if additional results are available. |     | _100_ |
| max\_position | optional | Returns results with a position value less than or equal to the specified position. |     | _54321_ |
| min\_position | optional | Returns results with a position greater than the specified position. |     | _12345_ |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`GET https://api.twitter.com/1.1/collections/entries.json?id=custom-539487832448843776`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
      "objects": {
        "timelines": {
          "custom-539487832448843776": {
            "collection_type": "user",
            "collection_url": "https://twitter.com/TwitterDev/timelines/539487832448843776",
            "description": "A collection of Tweets about National Parks in the United States.",
            "name": "National Park Tweets",
            "timeline_order": "curation_reverse_chron",
            "url": "",
            "user_id": "2244994945",
            "visibility": "public"
          }
        },
        "tweets": {
          "504032379045179393": {
            "contributors": null,
            "coordinates": null,
            "created_at": "Mon Aug 25 22:27:38 +0000 2014",
            "entities": {
              "hashtags": [],
              "media": [
                {
                  "display_url": "pic.twitter.com/HtdvV0bPEu",
                  "expanded_url": "http://twitter.com/Interior/status/504032379045179393/photo/1",
                  "id": 504032378411446273,
                  "id_str": "504032378411446273",
                  "indices": [
                    99,
                    121
                  ],
                  "media_url": "http://pbs.twimg.com/media/Bv6uxxaCcAEjWHD.jpg",
                  "media_url_https": "https://pbs.twimg.com/media/Bv6uxxaCcAEjWHD.jpg",
                  "sizes": {
                    "large": {
                      "h": 695,
                      "resize": "fit",
                      "w": 1024
                    },
                    "medium": {
                      "h": 407,
                      "resize": "fit",
                      "w": 600
                    },
                    "small": {
                      "h": 230,
                      "resize": "fit",
                      "w": 340
                    },
                    "thumb": {
                      "h": 150,
                      "resize": "crop",
                      "w": 150
                    }
                  },
                  "type": "photo",
                  "url": "http://t.co/HtdvV0bPEu"
                }
              ],
              "symbols": [],
              "urls": [],
              "user_mentions": [
                {
                  "id": 66453289,
                  "id_str": "66453289",
                  "indices": [
                    47,
                    60
                  ],
                  "name": "Lake Clark NP&P",
                  "screen_name": "LakeClarkNPS"
                }
              ]
            },
            "extended_entities": {
              "media": [
                {
                  "display_url": "pic.twitter.com/HtdvV0bPEu",
                  "expanded_url": "http://twitter.com/Interior/status/504032379045179393/photo/1",
                  "id": 504032378411446273,
                  "id_str": "504032378411446273",
                  "indices": [
                    99,
                    121
                  ],
                  "media_url": "http://pbs.twimg.com/media/Bv6uxxaCcAEjWHD.jpg",
                  "media_url_https": "https://pbs.twimg.com/media/Bv6uxxaCcAEjWHD.jpg",
                  "sizes": {
                    "large": {
                      "h": 695,
                      "resize": "fit",
                      "w": 1024
                    },
                    "medium": {
                      "h": 407,
                      "resize": "fit",
                      "w": 600
                    },
                    "small": {
                      "h": 230,
                      "resize": "fit",
                      "w": 340
                    },
                    "thumb": {
                      "h": 150,
                      "resize": "crop",
                      "w": 150
                    }
                  },
                  "type": "photo",
                  "url": "http://t.co/HtdvV0bPEu"
                }
              ]
            },
            "favorite_count": 639,
            "favorited": false,
            "geo": null,
            "id": 504032379045179393,
            "id_str": "504032379045179393",
            "in_reply_to_screen_name": null,
            "in_reply_to_status_id": null,
            "in_reply_to_status_id_str": null,
            "in_reply_to_user_id": null,
            "in_reply_to_user_id_str": null,
            "is_quote_status": false,
            "lang": "en",
            "place": null,
            "possibly_sensitive": false,
            "retweet_count": 606,
            "retweeted": false,
            "source": "Twitter for iPhone",
            "text": "How about a grizzly bear waving for the camera @LakeClarkNPS to end the day? Photo: Kevin Dietrich http://t.co/HtdvV0bPEu",
            "truncated": false,
            "user": {
              "id": 76348185,
              "id_str": "76348185"
            }
          }
      },
      "response": {
        "position": {
          "max_position": "371578415352947200",
          "min_position": "371578380871797248",
          "was_truncated": false
        },
        "timeline": [
          {
            "feature_context": "HBgGY3VzdG9tFoCAktzo1NL8DgAA",
            "tweet": {
              "id": "504032379045179393",
              "sort_index": "371578415352947200"
            }
          },
          {
            "feature_context": "HBgGY3VzdG9tFoCAktzo1NL8DgAA",
            "tweet": {
              "id": "532654992071852032",
              "sort_index": "371578393139797760"
            }
          },
          {
            "feature_context": "HBgGY3VzdG9tFoCAktzo1NL8DgAA",
            "tweet": {
              "id": "524573263163572224",
              "sort_index": "371578380871797248"
            }
          }
        ],
        "timeline_id": "custom-539487832448843776"
      }
    }

GET collections/list

get-collections-list

GET collections/list
====================

Find Collections created by a specific user or containing a specific curated Tweet.

Results are organized in a cursored collection.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/collections/list.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 1000 |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| user\_id | required | The ID of the user for whom to return results. |     | _20_ |
| screen\_name | required | The screen name of the user for whom to return results. |     | _twitterdev_ |
| tweet\_id | optional | The identifier of the Tweet for which to return results. |     | _514533751213551616_ |
| count | optional | Specifies the _maximum_ number of results to include in the response. Specify a count between 1 and 200. A _next\_cursor_ value will be provided in the response if additional results are available. |     | _100_ |
| cursor | optional | A string identifying the segment of the current result set to retrieve. Values for this parameter are yielded in the _cursors_ node attached to response objects. Usage of the _count_ parameter affects cursoring. |     | _BXb2synCEAE_ |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`GET https://api.twitter.com/1.1/collections/list.json?screen_name=twittermusic&count=1`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
      "objects": {
        "users": {
          "373471064": {
            "id": 373471064,
            "id_str": "373471064",
            "name": "Twitter Music",
            "screen_name": "TwitterMusic",
            "location": "Twitter HQ",
            "description": "Music related Tweets from around the world.",
            "url": "http://t.co/7eUtBKV1bf",
            "entities": {
              "url": {
                "urls": [{
                  "url": "http://t.co/7eUtBKV1bf",
                  "expanded_url": "http://music.twitter.com",
                  "display_url": "music.twitter.com",
                  "indices": [0, 22]
                }]
              },
              "description": {
                "urls": []
              }
            },
            "protected": false,
            "followers_count": 7914124,
            "friends_count": 276,
            "listed_count": 9443,
            "created_at": "Wed Sep 14 16:50:47 +0000 2011",
            "favourites_count": 958,
            "utc_offset": -36000,
            "time_zone": "Hawaii",
            "geo_enabled": true,
            "verified": true,
            "statuses_count": 8416,
            "lang": "en",
            "contributors_enabled": false,
            "is_translator": false,
            "is_translation_enabled": false,
            "profile_background_color": "131516",
            "profile_background_image_url": "http://abs.twimg.com/images/themes/theme14/bg.gif",
            "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme14/bg.gif",
            "profile_background_tile": true,
            "profile_image_url": "http://pbs.twimg.com/profile_images/378800000449287089/70dea90873e8a0f92fd582b4d04cfd4b_normal.png",
            "profile_image_url_https": "https://pbs.twimg.com/profile_images/378800000449287089/70dea90873e8a0f92fd582b4d04cfd4b_normal.png",
            "profile_banner_url": "https://pbs.twimg.com/profile_banners/373471064/1433882163",
            "profile_link_color": "009999",
            "profile_sidebar_border_color": "000000",
            "profile_sidebar_fill_color": "EFEFEF",
            "profile_text_color": "333333",
            "profile_use_background_image": true,
            "default_profile": false,
            "default_profile_image": false,
            "following": false,
            "follow_request_sent": false,
            "notifications": false
          }
        },
        "timelines": {
          "custom-588824628950269952": {
            "name": "Josh Groban Tour",
            "user_id": "373471064",
            "collection_url": "https://twitter.com/TwitterMusic/timelines/588824628950269952",
            "description": "Josh announces his tour by replying to fans in different cities",
            "url": "",
            "visibility": "public",
            "timeline_order": "curation_reverse_chron",
            "collection_type": "user"
          }
        }
      },
      "response": {
        "results": [{
          "timeline_id": "custom-588824628950269952"
        }],
        "cursors": {
          "next_cursor": "B9XAeo1CcAA"
        }
      }
    }

GET collections/show

get-collections-show

GET collections/show
====================

Retrieve information associated with a specific Collection.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/collections/show.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 1000 |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| id  | required | The identifier of the Collection for which to return results. |     | _custom-388061495298244609_ |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`GET https://api.twitter.com/1.1/collections/show.json?id=custom-393773266801659904`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
      "objects": {
        "users": {
          "373471064": {
            "id": 373471064,
            "id_str": "373471064",
            "name": "Twitter Music",
            "screen_name": "TwitterMusic",
            "location": "Twitter HQ",
            "description": "Music related Tweets from around the world.",
            "url": "http://t.co/7eUtBKV1bf",
            "entities": {
              "url": {
                "urls": [{
                  "url": "http://t.co/7eUtBKV1bf",
                  "expanded_url": "http://music.twitter.com",
                  "display_url": "music.twitter.com",
                  "indices": [0, 22]
                }]
              },
              "description": {
                "urls": []
              }
            },
            "protected": false,
            "followers_count": 7914295,
            "friends_count": 276,
            "listed_count": 9444,
            "created_at": "Wed Sep 14 16:50:47 +0000 2011",
            "favourites_count": 958,
            "utc_offset": -36000,
            "time_zone": "Hawaii",
            "geo_enabled": true,
            "verified": true,
            "statuses_count": 8416,
            "lang": "en",
            "contributors_enabled": false,
            "is_translator": false,
            "is_translation_enabled": false,
            "profile_background_color": "131516",
            "profile_background_image_url": "http://abs.twimg.com/images/themes/theme14/bg.gif",
            "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme14/bg.gif",
            "profile_background_tile": true,
            "profile_image_url": "http://pbs.twimg.com/profile_images/378800000449287089/70dea90873e8a0f92fd582b4d04cfd4b_normal.png",
            "profile_image_url_https": "https://pbs.twimg.com/profile_images/378800000449287089/70dea90873e8a0f92fd582b4d04cfd4b_normal.png",
            "profile_banner_url": "https://pbs.twimg.com/profile_banners/373471064/1433882163",
            "profile_link_color": "009999",
            "profile_sidebar_border_color": "000000",
            "profile_sidebar_fill_color": "EFEFEF",
            "profile_text_color": "333333",
            "profile_use_background_image": true,
            "default_profile": false,
            "default_profile_image": false,
            "following": false,
            "follow_request_sent": false,
            "notifications": false
          }
        },
        "timelines": {
          "custom-588824628950269952": {
            "name": "Josh Groban Tour",
            "user_id": "373471064",
            "collection_url": "https://twitter.com/TwitterMusic/timelines/588824628950269952",
            "description": "Josh announces his tour by replying to fans in different cities",
            "url": "",
            "visibility": "public",
            "timeline_order": "curation_reverse_chron",
            "collection_type": "user"
          }
        }
      },
      "response": {
        "timeline_id": "custom-588824628950269952"
      }
    }

POST collections/create

post-collections-create

POST collections/create
=======================

Create a Collection owned by the currently authenticated user.

The API endpoint may refuse to complete the request if the authenticated user has exceeded the total number of allowed collections for their account.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/collections/create.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| name | required | The title of the collection being created, in 25 characters or less. |     | _Sweet%20Tweets_ |
| description | optional | A brief description of this collection in 160 characters or fewer. |     | _My%20favorite%20tweets%20ever_ |
| url | optional | A fully-qualified URL to associate with this collection. |     | `https%3A%2F%2Fexample.com%2F` |
| timeline\_order | optional | Order Tweets chronologically or in the order they are added to a Collection. _curation\_reverse\_chron_ - order added (default) _tweet\_chron_ - oldest first _tweet\_reverse\_chron_ - most recent first |     | _tweet\_reverse\_chron_ |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`POST https://api.twitter.com/1.1/collections/create.json?name=Tweets%20to%20reply%20to`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
      "response": {
        "timeline_id": "custom-390882285743898624"
      },
      "objects": {
        "users": {
          "119476949": {
            "profile_sidebar_fill_color": "DDEEF6",
            "profile_sidebar_border_color": "C0DEED",
            "profile_background_tile": true,
            "name": "OAuth Dancer",
            "profile_image_url": "http://a0.twimg.com/profile_images/730275945/oauth-dancer_normal.jpg",
            "created_at": "Wed Mar 03 19:37:35 +0000 2010",
            "location": "San Francisco, CA",
            "follow_request_sent": null,
            "profile_link_color": "0084B4",
            "is_translator": false,
            "id_str": "119476949",
            "default_profile": false,
            "contributors_enabled": false,
            "favourites_count": 0,
            "url": "http://bit.ly/oauth-dancer",
            "profile_image_url_https": "https://si0.twimg.com/profile_images/730275945/oauth-dancer_normal.jpg",
            "utc_offset": null,
            "id": 119476949,
            "profile_use_background_image": true,
            "listed_count": 0,
            "profile_text_color": "333333",
            "lang": "en",
            "followers_count": 0,
            "protected": false,
            "notifications": null,
            "profile_background_image_url_https": "https://si0.twimg.com/profile_background_images/80151733/oauth-dance.png",
            "profile_background_color": "C0DEED",
            "verified": false,
            "geo_enabled": true,
            "time_zone": null,
            "description": "",
            "default_profile_image": false,
            "profile_background_image_url": "http://a0.twimg.com/profile_background_images/80151733/oauth-dance.png",
            "statuses_count": 0,
            "friends_count": 0,
            "following": null,
            "screen_name": "oauth_dancer",
            "counts": {
              "lists": {
                "owned": null,
                "subscribed": null
              },
              "saved_searches": 0
            }
          }
        },
        "timelines": {
          "custom-390882285743898624": {
            "name": "Tweets to reply to",
            "user_id": "119476949"
          }
        }
      }
    }

POST collections/destroy

post-collections-destroy

POST collections/destroy
========================

Permanently delete a Collection owned by the currently authenticated user.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/collections/destroy.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| id  | required | The identifier of the Collection to destroy. |     | _custom-388061495298244609_ |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`POST https://api.twitter.com/1.1/collections/destroy.json?id=custom-390882285743898624`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
      "destroyed": true
    }

POST collections/entries/add

post-collections-entries-add

POST collections/entries/add
============================

Add a specified Tweet to a Collection.

A collection will store up to a few thousand Tweets. Adding a Tweet to a collection beyond its allowed capacity will remove the oldest Tweet in the collection based on the time it was added to the collection.

Use [POST collections / entries / curate](https://developer.twitter.com/en/docs/tweets/curate-a-collection/api-reference/post-collections-entries-curate) to add Tweets to a Collection in bulk.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/collections/entries/add.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| id  | required | The identifier of the Collection receiving the Tweet. |     | _custom-388061495298244609_ |
| tweet\_id | required | The identifier of the Tweet to add to the Collection. |     | _390839888012382208_ |
| relative\_to | optional | The identifier of the Tweet used for relative positioning in a _curation\_reverse\_chron_ ordered collection. |     | _614929127313965056_ |
| above | optional | Set to _false_ to insert the specified _tweet\_id_ below the _relative\_to_ Tweet in the collection. Default: _true_ |     | _false_ |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`POST https://api.twitter.com/1.1/collections/entries/add.json?tweet_id=390890231215292416&id=custom-388061495298244609`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

Success:[¶](#success- "Permalink to this headline")
---------------------------------------------------

    {
      "objects": {},
      "response": {
        "errors": []
      }
    }

Failure:[¶](#failure- "Permalink to this headline")
---------------------------------------------------

    {
      "objects": {},
      "response": {
        "errors": [
          {
            "change": {
              "op": "add",
              "tweet_id": "390890231215292416"
            },
            "reason": "duplicate"
          }
        ]
      }
    }

POST collections/entries/curate

post-collections-entries-curate

POST collections/entries/curate
===============================

Curate a Collection by adding or removing Tweets in bulk. Updates must be limited to 100 cumulative additions or removals per request.

Use [POST collections / entries / add](https://developer.twitter.com/en/docs/tweets/curate-a-collection/api-reference/post-collections-entries-add) and [POST collections / entries / remove](https://developer.twitter.com/en/docs/tweets/curate-a-collection/api-reference/post-collections-entries-remove) to add or remove a single Tweet.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/collections/entries/curate.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`POST https://api.twitter.com/1.1/collections/entries/curate.json`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    POST /1.1/collections/entries/curate.json
    Content-Type: application/json
    Content-Length: 226

    {"id":"custom-388061495298244609","changes":[{"op":"add","tweet_id":"390897780949925889"},{"op":"add","tweet_id":"390853164611555329"},{"op":"add","tweet_id":"390892747810295808"},{"op":"add","tweet_id":"390898463090561024"}]} 

Success:[¶](#success- "Permalink to this headline")
---------------------------------------------------

    {"objects":{},"response":{"errors":[]}}

Failure:[¶](#failure- "Permalink to this headline")
---------------------------------------------------

    {"objects":{},"response":{"errors":[{"reason":"duplicate","change":{"op":"add","tweet_id":"390897780949925889"}},{"reason":"duplicate","change":{"op":"add","tweet_id":"390853164611555329"}},{"reason":"duplicate","change":{"op":"add","tweet_id":"390892747810295808"}},{"reason":"duplicate","change":{"op":"add","tweet_id":"390898463090561024"}}]}}

POST collections/entries/move

post-collections-entries-move

POST collections/entries/move
=============================

Move a specified Tweet to a new position in a `curation_reverse_chron` ordered collection.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/collections/entries/move.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| id  | required | The identifier of the Collection receiving the Tweet. |     | _custom-388061495298244609_ |
| tweet\_id | required | The identifier of the Tweet to add to the Collection. |     | _390839888012382208_ |
| relative\_to | required | The identifier of the Tweet used for relative positioning. |     | _614929127313965056_ |
| above | optional | Set to _false_ to insert the specified _tweet\_id_ below the _relative\_to_ Tweet in the collection. Default: _true_ |     | _false_ |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`POST https://api.twitter.com/1.1/collections/entries/move.json?id=custom-388061495298244609&tweet_id=390839888012382208&relative_to=614929127313965056`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

Success:[¶](#success- "Permalink to this headline")
---------------------------------------------------

    {
      "objects": {},
      "response": {
        "errors": []
      }
    }

Failure:[¶](#failure- "Permalink to this headline")
---------------------------------------------------

    {
      "objects": {},
      "response": {
        "errors": [
          {
            "change": {
              "op": "move",
              "tweet_id": "610990849493762050"
            },
            "reason": "not_found"
          }
        ]
      }
    }

POST collections/entries/remove

post-collections-entries-remove

POST collections/entries/remove
===============================

Remove the specified Tweet from a Collection.

Use [POST collections / entries / curate](https://developer.twitter.com/en/docs/tweets/curate-a-collection/api-reference/post-collections-entries-curate) to remove Tweets from a Collection in bulk.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/collections/entries/remove.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| id  | required | The identifier of the target Collection. |     | _custom-388061495298244609_ |
| tweet\_id | required | The identifier of the Tweet to remove. |     | _390839888012382208_ |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`POST https://api.twitter.com/1.1/collections/entries/remove.json?id=custom-388061495298244609&tweet_id=390890231215292416`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

Success:

    {
      "response": {
        "errors": [
    
        ]
      },
      "objects": {
      }
    }

Failure:

    {
      "response": {
        "errors": [
          {
            "change": {
              "tweet_id": "390890231215292416",
              "op": "remove"
            },
            "reason": "not_found"
          }
        ]
      },
      "objects": {
      }
    }

POST collections/update

post-collections-update

POST collections/update
=======================

Update information concerning a Collection owned by the currently authenticated user.

Partial updates are not currently supported: please provide `name`, `description`, and `url` whenever using this method. Omitted `description` or `url` parameters will be treated as if an empty string was passed, overwriting any previously stored value for the Collection.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/collections/update.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| id  | required | The identifier of the Collection to modify. |     | _custom-388061495298244609_ |
| name | optional | The title of the Collection being created, in 25 characters or fewer. |     | _Sweet%20Tweets_ |
| description | optional | A brief description of this Collection in 160 characters or fewer. |     | _My%20favorite%20tweets%20ever_ |
| url | optional | A fully-qualified URL to associate with this Collection. |     | `https%3A%2F%2Fexample.com%2F` |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`POST https://api.twitter.com/1.1/collections/update.json?name=Subtweets&id=custom-390882285743898624`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
      "response": {
        "timeline_id": "custom-390882285743898624"
      },
      "objects": {
        "users": {
          "119476949": {
            "profile_sidebar_fill_color": "DDEEF6",
            "profile_sidebar_border_color": "C0DEED",
            "profile_background_tile": true,
            "name": "OAuth Dancer",
            "profile_image_url": "http://a0.twimg.com/profile_images/730275945/oauth-dancer_normal.jpg",
            "created_at": "Wed Mar 03 19:37:35 +0000 2010",
            "location": "San Francisco, CA",
            "follow_request_sent": null,
            "profile_link_color": "0084B4",
            "is_translator": false,
            "id_str": "119476949",
            "default_profile": false,
            "contributors_enabled": false,
            "favourites_count": 0,
            "url": "http://bit.ly/oauth-dancer",
            "profile_image_url_https": "https://si0.twimg.com/profile_images/730275945/oauth-dancer_normal.jpg",
            "utc_offset": null,
            "id": 119476949,
            "profile_use_background_image": true,
            "listed_count": 0,
            "profile_text_color": "333333",
            "lang": "en",
            "followers_count": 0,
            "protected": false,
            "notifications": null,
            "profile_background_image_url_https": "https://si0.twimg.com/profile_background_images/80151733/oauth-dance.png",
            "profile_background_color": "C0DEED",
            "verified": false,
            "geo_enabled": true,
            "time_zone": null,
            "description": "",
            "default_profile_image": false,
            "profile_background_image_url": "http://a0.twimg.com/profile_background_images/80151733/oauth-dance.png",
            "statuses_count": 0,
            "friends_count": 0,
            "following": null,
            "screen_name": "oauth_dancer",
            "counts": {
              "lists": {
                "owned": null,
                "subscribed": null
              },
              "saved_searches": 0
            }
          }
        },
        "timelines": {
          "custom-390882285743898624": {
            "name": "Subtweets",
            "user_id": "119476949"
          }
        }
      }
    }