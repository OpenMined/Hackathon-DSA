Overview

This endpoint has been updated to include Tweet edit metadata. Learn more about these metadata on the ["Edit Tweets" fundamentals page](https://developer.twitter.com/en/docs/twitter-api/enterprise/edit-tweets). 

Overview
========

[Enterprise](https://developer.twitter.com/en/products/twitter-api/enterprise)

_This is an enterprise API available within our managed access levels only. To use this API, you must first set up an account with our enterprise sales team. [Learn more](https://developer.twitter.com/en/products/twitter-api/enterprise)_  

_You can view all of the Twitter API filtered stream offerings [HERE](https://developer.twitter.com/en/docs/twitter-api/filtered-stream-overview)._

The PowerTrack API provides customers with the ability to filter the full Twitter firehose, and only receive the data that they or their customers are interested in. This is accomplished by applying the PowerTrack filtering language - see [Rules and filtering](https://developer.twitter.com/en/docs/twitter-api/enterprise/rules-and-filtering/overview.html) - to match Tweets based on a wide variety of attributes, including user attributes, geo-location, language, and many others. Using PowerTrack rules to filter Tweet ensures that customers receive all of the data, and _only_ the data they need for your app.  
  

### Core components

The PowerTrack API consists of two endpoints:

#### Rules endpoint

A separate endpoint managed independently by your application, the rules endpoint supports GET, POST, POST \_method=delete and rule validation methods with basic authentication for managing your ruleset. It can support thousands of rules that allow you to filter the realtime stream of data for the topics and conversations that you care about. The rules endpoint can be accessed, managed, and will persist regardless of your connection status to the stream - you can also update (add/remove) rules while connected to the stream and the changes will take effect almost immediately.

#### Stream endpoint

Connecting to the streaming endpoint consists of a simple [GET](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/api-reference/powertrack-stream) request using basic authentication. Once a connection is established, data is delivered in JSON format (see sample payload below) through a persistent HTTP Streaming connection. You will only receive data matching your rules while connected to the stream.

#### Rule tags

A single PowerTrack stream can support thousands of rules, so being able to discern which rule(s) matched a given Tweet becomes important. This is easily solved by using rule tags. Upon rule creation, you can assign a tag value which will be returned in the matching\_rules object ([see here](https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/matching-rules.html)) of the response payload.

Rule tags can represent an end customer use case, a topic or conversation, or another helpful identifier that you can use to route incoming Tweets accordingly.

If, in addition to realtime data, your product also requires instant access to recent data, we recommend using our [Search API](https://developer.twitter.com/en/docs/twitter-api/search-overview).  
  

### Available operators

The PowerTrack API currently supports the following operators:  

* keyword
* emoji
* "exact phrase match"
* "keyword1 keyword2"~N
* contains:
* from:
* to:
* url:
* url\_title:
* url\_description:
* url\_contains:
* has:links
* sample:
* #
* point\_radius:\[lon lat radius\]
* bounding\_box:\[west\_long south\_lat east\_long north\_lat\]
* @
* $
* bio:
* bio\_name:
* retweets\_of:
* lang:
* bio\_location:
* statuses\_count:
* followers\_count:
* friends\_count:
* listed\_count:
* is:verified
* source:
* place:
* place\_country:
* has:geo
* has:mentions
* has:hashtags
* has:images
* has:videos
* has:media
* has:symbols
* is:retweet
* is:reply
* is:quote
* retweets\_of\_status\_id:
* in\_reply\_to\_status\_id:
* has:profile\_geo
* profile\_point\_radius:\[long lat radius\]
* profile\_bounding\_box:\[west\_long south\_lat east\_long north\_lat\]
* profile\_country:
* profile\_region:
* profile\_locality:
* profile\_subregion:

For more details, please see the [Getting started with enterprise rules](https://developer.twitter.com/en/docs/twitter-api/enterprise/rules-and-filtering/enterprise-operators) guide.  
  

### Sample payload

Below is a sample payload from the PowerTrack API in Native Enriched format:

      `{   "created_at": "Wed Oct 10 20:19:24 +0000 2018",   "id": 1050118621198921700,   "id_str": "1050118621198921728",   "text": "To make room for more expression, we will now count all emojis as equal—including those with gender‍‍‍ ‍‍and skin t… https://t.co/MkGjXf9aXm",   "source": "<a href=\"http://twitter.com\" rel=\"nofollow\">Twitter Web Client</a>",   "truncated": true,   "in_reply_to_status_id": null,   "in_reply_to_status_id_str": null,   "in_reply_to_user_id": null,   "in_reply_to_user_id_str": null,   "in_reply_to_screen_name": null,   "user": {     "id": 6253282,     "id_str": "6253282",     "name": "Twitter API",     "screen_name": "TwitterAPI",     "location": "San Francisco, CA",     "url": "https://developer.twitter.com",     "description": "The Real Twitter API. Tweets about API changes, service issues and our Developer Platform. Don't get an answer? It's on my website.",     "translator_type": "null",     "derived": {       "locations": [         {           "country": "United States",           "country_code": "US",           "locality": "San Francisco",           "region": "California",           "sub_region": "San Francisco County",           "full_name": "San Francisco, California, United States",           "geo": {             "coordinates": [               -122.41942,               37.77493             ],             "type": "point"           }         }       ]     },     "protected": false,     "verified": true,     "followers_count": 6172196,     "friends_count": 12,     "listed_count": 13003,     "favourites_count": 31,     "statuses_count": 3650,     "created_at": "Wed May 23 06:01:13 +0000 2007",     "utc_offset": null,     "time_zone": null,     "geo_enabled": false,     "lang": "en",     "contributors_enabled": false,     "is_translator": null,     "profile_background_color": "null",     "profile_background_image_url": "null",     "profile_background_image_url_https": "null",     "profile_background_tile": null,     "profile_link_color": "null",     "profile_sidebar_border_color": "null",     "profile_sidebar_fill_color": "null",     "profile_text_color": "null",     "profile_use_background_image": null,     "profile_image_url": "null",     "profile_image_url_https": "https://pbs.twimg.com/profile_images/942858479592554497/BbazLO9L_normal.jpg",     "profile_banner_url": "https://pbs.twimg.com/profile_banners/6253282/1497491515",     "default_profile": false,     "default_profile_image": false,     "following": null,     "follow_request_sent": null,     "notifications": null   },   "geo": null,   "coordinates": null,   "place": null,   "contributors": null,   "is_quote_status": false,   "extended_tweet": {     "full_text": "To make room for more expression, we will now count all emojis as equal—including those with gender‍‍‍ ‍‍and skin tone modifiers 👍🏻👍🏽👍🏿. This is now reflected in Twitter-Text, our Open Source library. \n\nUsing Twitter-Text? See the forum post for detail: https://t.co/Nx1XZmRCXA",     "display_text_range": [       0,       277     ],     "entities": {       "hashtags": [],       "urls": [         {           "url": "https://t.co/Nx1XZmRCXA",           "expanded_url": "https://twittercommunity.com/t/new-update-to-the-twitter-text-library-emoji-character-count/114607",           "display_url": "twittercommunity.com/t/new-update-t…",           "unwound": {             "url": "https://twittercommunity.com/t/new-update-to-the-twitter-text-library-emoji-character-count/114607",             "status": 200,             "title": "New update to the Twitter-Text library: Emoji character count",             "description": "Over the years, we have made several updates to the way that people can communicate on Twitter. One of the more notable changes made last year was to increase the number of characters per Tweet from 140 to 280 characters. Today, we continue to expand people’s ability to express themselves by announcing a change to the way that we count emojis. Due to the differences in the way written text and emojis are encoded, many emojis (including emojis where you can apply gender and skin tone) have count..."           },           "indices": [             254,             277           ]         }       ],       "user_mentions": [],       "symbols": []     }   },   "quote_count": 0,   "reply_count": 0,   "retweet_count": 0,   "favorite_count": 0,   "entities": {     "hashtags": [],     "urls": [       {         "url": "https://t.co/MkGjXf9aXm",         "expanded_url": "https://twitter.com/i/web/status/1050118621198921728",         "display_url": "twitter.com/i/web/status/1…",         "indices": [           117,           140         ]       }     ],     "user_mentions": [],     "symbols": []   },   "favorited": false,   "retweeted": false,   "possibly_sensitive": false,   "filter_level": "low",   "lang": "en",   "timestamp_ms": "1539202764211",   "matching_rules": [     {       "tag": null,       "id": 1128017341835464700,       "id_str": "1128017341835464704"     }   ] } }`
    

  
Next steps
-------------

[Continue to the realtime PowerTrack API reference](https://developer.twitter.com/en/docs/tweets/filter-realtime/api-reference/powertrack-stream)

See code examples: 

* [See simple scripts in several languages to help get started](https://github.com/gnip/support/tree/master/Premium%20Stream%20Connection)
* [Build a trends dashboard with Twitter API Toolkit for Google Cloud](https://developer.twitter.com/en/docs/tutorials/developer-guide--twitter-api-toolkit-for-google-cloud11)
* See an example Java client libraries: [Hosebird Client adapted for enterprise streams](https://github.com/jimmoffitt/hbc), [Gnip4J](https://github.com/zauberlabs/gnip4j)  
    
* [See an example Python client library](https://github.com/tw-ddis/Gnip-Stream-Collector-Metrics)

Integrating with PowerTrack

Integrating with PowerTrack
---------------------------

To integrate PowerTrack into your product, you will need to build an application that can do the following:

1. Establish a streaming connection to the PowerTrack stream API.
2. Asynchronously send POST requests to the PowerTrack rules API to add and delete rules from the stream.
3. Handle low data volumes – Maintain the streaming connection, and ensure buffers are flushed regularly.
4. Handle high data volumes – de-couple stream ingestion from additional processing using asynchronous processes.
5. Reconnect to the stream automatically when disconnected for any reason.

For details on the types of requests needed for tasks 1 and 2, and important considerations in implementing them, see the [API reference](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/api-reference).

For information on consuming a realtime data stream, see [here](https://developer.twitter.com/en/docs/tutorials/consuming-streaming-data.html).

PowerTrack rules & filtering

Rules & Filtering
-----------------

Take a deeper dive into building PowerTrack rules using our [learning path: How to detect signal from noise and build powerful filtering rules](https://developer.twitter.com/en/docs/tutorials/building-powerful-enterprise-filters)

PowerTrack enhances the ability to filter Twitter’s full firehose, and only receive the data that they or their customers are interested in. This is accomplished by applying PowerTrack filtering language to match Tweets based on a wide variety of attributes, including user attributes, geo-location, language, and many others. Using PowerTrack rules to filter a data source ensures that customers receive all of the data, and _only_ the data they need for your app.

As described, customers add filtering rules to the PowerTrack stream to determine which activities will be sent through the connection. The PowerTrack stream can support thousands of these individual rules, and deliver the combined set of matching activities through the single stream connection.

The set of PowerTrack rules used to filter a customer’s stream is highly flexible. If a customer needs to add a new filtering rule to capture a different type of content, or remove an existing rule, their app can send a request to the PowerTrack API to make it happen. When that request is sent, the filtering rules are automatically modified and the changes simply take effect in the data stream with no need to reconnect. This allows customers to provide data for many customers at scale, while supporting distinct filtering requirements for each of those customers.

[See Complete List of Operators »](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/guides/enterprise-operators.html)

#### Data

Data is delivered to the customer’s app through a constant stream as it is created. The realtime stream does not provide recent data – rather, it begins filtering for and delivering results based on the time a filtering rule is added to the stream. If, in addition to realtime data, your product also requires instant access to recent data, we recommend using the [Search API](https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/overview.html).

Data is in Gzip compressed JSON format.

#### Matching Rules

When an activity is delivered through the PowerTrack stream, adds metadata in the [“matching rules”](https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/matching-rules) portion of that activity to indicate which rule or rules caused that specific activity to be delivered. If multiple rules match a single activity, the activity is delivered a single time with each of the matching rules included in this metadata. The matching rules provide an easy way to associate a specific activity with specific rules and customers in your product, even where you have many customers with lots of distinct rules. Since the data is delivered through a single stream in this manner, scaling up as your product gains additional customers is simple.

#### Rule Tags

At the time they are created, each filtering rule may be created with a tag. Rule tags have no special meaning, they are simply treated as opaque strings carried along with the rule. They will be included in the “matching rules” metadata in activities returned. Tags provide an easy way to create logical groupings of PowerTrack rules. For example, you may generate a unique ID for a specific rule as its tag, and allow your app to reference that ID within activities it processes to associate a result with specific customers, campaigns, categories, or other related groups.

Note that tags cannot be updated on an existing rule, but can only be included when a rule is created. In order to “update” a tag, you need to first remove the rule, then add it again with the updated tag. The best solution is to simply use a unique identifier as your tag, which your system can associate with various other data points within your own app, all without having to change anything in the rule set.

PowerTrack operators

PowerTrack operators
====================

Below is a list of all operators supported in Twitter's enterprise real-time and historical PowerTrack APIs.  

 OperatorDescriptionkeyword  
Matches a keyword within the body of a Tweet. This is a tokenized match, meaning that your keyword string will be matched against the tokenized text of the Tweet body – tokenization is based on punctuation, symbol, and separator Unicode basic plane characters. For example, a Tweet with the text “I like coca-cola” would be split into the following tokens: I, like, coca, cola. These tokens would then be compared to the keyword string used in your rule. To match strings containing punctuation (for example, coca-cola), symbol, or separator characters, you must use a quoted exact match as described below.  
  
**Note:** This operator will match on both URLs and unwound URLs within a Tweet.emoji  
Matches an emoji within the body of a Tweet. Emojis are a tokenized match, meaning that your emoji will be matched against the tokenized text of the Tweet body – tokenization is based on punctuation, symbol/emoji, and separator Unicode basic plane characters. For example, a Tweet with the text “I like 🍕” would be split into the following tokens: I, like, 🍕. These tokens would then be compared to the emoji used in your rule. Note that if an emoji has a variant, you must use “quotations” to add to a rule.  
"exact phrase match"  

Matches an exact phrase within the body of a Tweet.

**Note:** In 30 Day Search and Full Archive Search, punctuation is not tokenized and is instead treated as whitespace.   
For example, quoted “#hashtag” will match “hashtag” but not #hashtag (use the hashtag # operator without quotes to match on actual hashtags   
For example, quoted “$cashtag” will match “cashtag” but not $cashtag (use the cashtag $ operator without quotes to match on actual cashtags

**Note:** This operator will match on both URLs and unwound URLs within a Tweet.

#  

Matches any Tweet with the given hashtag.

This operator performs an exact match, NOT a tokenized match, meaning the rule “2016” will match posts with the exact hashtag “2016”, but not those with the hashtag “2016election”

Note: that the hashtag operator relies on Twitter’s entity extraction to match hashtags, rather than extracting the hashtag from the body itself. See [HERE](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/entities) for more information on Twitter Entities JSON attributes.

@  

Matches any Tweet that mentions the given username.

The to: operator returns a subset match of the @mention operator.

"keyword1 keyword2"~N  

Commonly referred to as a proximity operator, this matches a Tweet where the keywords are no more than N tokens from each other.

If the keywords are in the opposite order, they can not be more than N-2 tokens from each other.

Can have any number of keywords in quotes.

N cannot be greater than 6.

**Example:** ********************"snowy mountain resort"~6********************

contains:

Substring match for Tweets that have the given substring in the body, regardless of tokenization. In other words, this does a pure substring match and does not consider word boundaries.

Use double quotes to match substrings that contain whitespace or punctuation.

from:  

Matches any Tweet from a specific user.

The value must be the user’s Twitter numeric Account ID or username (excluding the @ character). See HERE or [HERE](http://gettwitterid.com/) for methods for looking up numeric Twitter Account IDs.  

url:  
Performs a tokenized (keyword/phrase) match on the expanded URLs of a Tweet (similar to url\_contains). Tokens and phrases containing punctuation or special characters should be double-quoted. For example, url:"/developer". While generally not recommended, if you want to match on a specific protocol, enclose in double-quotes: url:"https://developer.twitter.com".  
  
**Note:** When using PowerTrack or Historical PowerTrack, this operator will match on URLs contained within the original Tweet of a Quote Tweet. For example, if your rule includes url:"developer.twitter.com", and a Tweet contains that URL, any Quote Tweets of that Tweet will be included in the results. This is not the case when using the Search API.url\_title:  

_Available alias_: url\_title:

Performs a keyword/phrase match on the (new) expanded URL HTML title metadata. See [HERE](https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/expanded-and-enhanced-urls) for more information on expanded URL enrichment.

url\_description:  

_Available alias_: within\_url\_description:

Performs a keyword/phrase match on the (new) expanded page description metadata. See [HERE](https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/expanded-and-enhanced-urls) for more information on expanded URL enrichment.

url\_contains:  

Matches Tweets with URLs that literally contain the given phrase or keyword. To search for patterns with punctuation in them (i.e. google.com) enclose the search term in quotes.

NOTE: If you’re using the [Expanded URL](https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/expanded-and-enhanced-urls) output format, we will match against the expanded URL as well.

bio:  

_Available alias_: user\_bio:

Matches a keyword or phrase within the user bio of a Tweet. This is a tokenized match within the contents of the 'description' field within the [User object](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/user).

bio\_name:  
Matches a keyword within the user bio name of a Tweet. This is a tokenized match within the contents of a user’s “name” field within the [User object](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/user).  
bio\_location:  

_Available alias_: user\_bio\_location: 

Matches tweets where the User object's location contains the specified keyword or phrase. This operator performs a tokenized match, similar to the normal keyword rules on the message body.

This location is part of the [User object](https://developer.twitter.com/en/docs/tweets/data-dictionary/native-enriched-objects/user), and is the account's 'home' location, is a non-normalized, user-generated, free-form string, and is different from a Tweet's location (when available). 

statuses\_count:  

_Available alias_: tweets\_count:

Matches Tweets when the author has posted a number of statuses that falls within the given range.

If a single number is specified, any number equal to or higher will match.

Additionally, a range can be specified to match any number in the given range  (for example, statuses\_count:1000..10000).

followers\_count:  

Matches Tweets when the author has a followers count within the given range.

If a single number is specified, any number equal to or higher will match.

Additionally, a range can be specified to match any number in the given range (for example, followers\_count:1000..10000).  

friends\_count:  

_Available alias_: following\_count: 

Matches Tweets when the author has a friends count (the number of users they follow) that falls within the given range.

If a single number is specified, any number equal to or higher will match.

Additionally, a range can be specified to match any number in the given range (for example, friends\_count:1000..10000).

listed\_count:  

_Available alias_: user\_in\_lists\_count: 

Matches Tweets when the author has been listed on Twitter a number of times falls within the given range.

If a single number is specified, any number equal to or higher will match.

Additionally, a range can be specified to match any number in the given range (for example, listed\_count:10..100).

$

Matches any Tweet that contains the specified ‘cashtag’ (where the leading character of the token is the ‘$’ character).

Note that the cashtag operator relies on Twitter’s ‘symbols’ entity extraction to match cashtags, rather than trying to extract the cashtag from the body itself. See [HERE](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/entities) for more information on Twitter Entities JSON attributes.  

retweets\_of:  

_Available alias_: retweets\_of\_user:

Matches Tweets that are Retweets of a specified user. Accepts both usernames and numeric Twitter Account IDs (NOT tweet status IDs).  
See [HERE](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/users/lookup) for methods for looking up numeric Twitter Account IDs.  

retweets\_of\_status\_id:  

_Available alias_: retweets\_of\_tweet\_id: 

Deliver only explicit Retweets of the specified Tweet. Note that the status ID used should be the ID of an original Tweet and not a Retweet. 

in\_reply\_to\_status\_id:  

_Available alias_: in\_reply\_to\_tweet\_id:

Deliver only explicit replies to the specified Tweet.

sample:

Returns a random sample of Tweets that match a rule rather than the entire set of Tweets. Sample percent must be represented by an integer value between 1 and 100. This operator applies to the entire rule and requires any “OR’d” terms be grouped.

**Important Note:** The sample operator first reduces the scope of the firehose to X%, then the rule/filter is applied to that sampled subset. If you are using, for example, **sample:10**, each Tweet has a 10% chance of being in the sample. 

Also, the sampling is deterministic, and you will get the same data sample in realtime as you would if you pulled the data historically.

source:Matches any Tweet generated by the given source application. The value must be either the name of the application or the application’s URL. **Cannot be used alone.**  
lang:  

Matches Tweets that have been classified by Twitter as being of a particular language (if, and only if, the tweet has been classified). It is important to note that each Tweet is currently only classified as being of one language, so AND’ing together multiple languages will yield no results.

**Note:** if no language classification can be made the provided result is ‘und’ (for undefined).

The list below represents the currently supported languages and their corresponding BCP 47 language identifier:

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

**Note:** See the [GET geo/search](https://developer.twitter.com/en/docs/geo/places-near-location/api-reference/get-geo-search) public API endpoint for how to obtain Twitter place IDs.

**Note:** This operator will not match on Retweets, since Retweet's places are attached to the original Tweet. It will also not match on places attached to the original Tweet of a Quote Tweet.

place\_country:  

Matches Tweets where the country code associated with a tagged [place/location](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/geo) matches the given ISO alpha-2 character code.

Valid ISO codes can be found here: [http://en.wikipedia.org/wiki/ISO\_3166-1\_alpha-2](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

**Note:** This operator will not match on Retweets, since Retweet's places are attached to the original Tweet. It will also not match on places attached to the original Tweet of a Quote Tweet.

point\_radius:\[lon lat radius\]  

Matches against the Exact Location (x,y) of the Tweet when present, and in Twitter, against a “Place” geo polygon, where the Place is fully contained within the defined region.

* Units of radius supported are miles (mi) and kilometers (km).
* Radius must be less than 25mi.
* Longitude is in the range of ±180
* Latitude is in the range of ±90
* All coordinates are in decimal degrees.
* Rule arguments are contained within brackets, space delimited.

**Note:** This operator will not match on Retweets, since Retweet's places are attached to the original Tweet. It will also not match on places attached to the original Tweet of a Quote Tweet.

**Example:** ********************point\_radius:\[2.355128 48.861118 16km\] OR point\_radius:\[-41.287336 174.761070 20mi\]********************

bounding\_box:\[west\_long south\_lat east\_long north\_lat\]  

_Available alias_: geo\_bounding\_box:

Matches against the Exact Location (long, lat) of the Tweet when present, and in Twitter, against a “Place” geo polygon, where the Place is fully contained within the defined region.

* west\_long south\_lat represent the southwest corner of the bounding box where west-long is the longitude of that point, and south\_lat is the latitude.
* east\_long and north\_lat represent the northeast corner of the bounding box, where east\_long is the longitude of that point, and north\_lat is the latitude.
* Width and height of the bounding box must be less than 25mi
* Longitude is in the range of ±180
* Latitude is in the range of ±90
* All coordinates are in decimal degrees.
* Rule arguments are contained within brackets, space delimited.

**Note:** This operator will not match on Retweets, since Retweet's places are attached to the original Tweet. It will also not match on places attached to the original Tweet of a Quote Tweet.

**Example:** ********************bounding\_box:\[-105.301758 39.964069 -105.178505 40.09455\]********************

profile\_country:  

Exact match on the “countryCode” field from the “address” object in the Profile Geo enrichment.

Uses a normalized set of two-letter country codes, based on ISO-3166-1-alpha-2 specification. This operator is provided in lieu of an operator for “country” field from the “address” object to be concise.

profile\_region:  

Matches on the “region” field from the “address” object in the Profile Geo enrichment.

This is an exact full string match. It is not necessary to escape characters with a backslash. For example, if matching something with a slash, use “one/two”, not “one\\/two”. Use double quotes to match substrings that contain whitespace or punctuation.

profile\_locality:  

Matches on the “locality” field from the “address” object in the Profile Geo enrichment.

This is an exact full string match. It is not necessary to escape characters with a backslash. For example, if matching something with a slash, use “one/two”, not “one\\/two”. Use double quotes to match substrings that contain whitespace or punctuation.

profile\_subregion:  

Matches on the “subRegion” field from the “address” object in the [Profile Geo](https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/profile-geo) enrichment. In addition to targeting specific counties, these operators can be helpful to filter on a metro area without defining filters for every city and town within the region.

This is an exact full string match. It is not necessary to escape characters with a backslash. For example, if matching something with a slash, use “one/two”, not “one\\/two”. Use double quotes to match substrings that contain whitespace or punctuation.

has:geo  

Matches Tweets that have Tweet-specific geolocation data provided from Twitter. This can be either “geo” lat-long coordinate, or a “location” in the form of a Twitter [“Place”](https://dev.twitter.com/overview/api/places), with the corresponding display name, geo polygon, and other fields.

**Note:** Operators matching on place (Tweet geo) will only include matches from original tweets. Retweets do not contain any place data.  

has:profile\_geo  

_Available alias_: has:derived\_user\_geo

Matches Tweets that have any [Profile Geo](https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/profile-geo) metadata, regardless of the actual value.  

has:links

This operator matches Tweets which contain links in the message body.is:retweet  

Deliver only explicit retweets that match a rule. Can also be negated to exclude retweets that match a rule from delivery and only original content is delivered.

This operator looks only for true Retweets, which use Twitter’s Retweet functionality. Quoted Tweets and Modified Tweets which do not use Twitter’s Retweet functionality will not be matched by this operator.

Can also be negated to match only on original Tweets.  

is:quoteDelivers only Quote Tweets, or Tweets that reference another Tweet, as identified by the "is\_quote\_status":true in Tweet payloads. Can also be negated to exclude Quote Tweets.  
is:verified  
Deliver only Tweets where the author is “verified” by Twitter. Can also be negated to exclude Tweets where the author is verified.  
is:replyDeliver only replies that match a rule. It can also be negated to exclude delivery of replies that match the specified rule. This operator matches on replies in original Tweets, as well as replies in quoted Tweets and Retweets. You can use is:reply in conjunction with is:retweet and is:quote to only deliver replies to original Tweets.  
\-is:nullcast

Negation only. Negates Tweets that are nullcasted (for example, contains the ********************"scopes": {"followers": false}"******************** object). For more info on Nullcasted Tweets, [see here](https://developer.twitter.com/en/docs/tweets/post-and-engage/guides/tweet-availability).

Note: Must be used at highest level of rule when used with the Search API.   
Example: (gold AND silver) -is:nullcast

has:mentions  
Matches Tweets that mention another Twitter user.  
has:hashtags  
Matches Tweets that contain a hashtag.  
has:media  

_Available alias_: has:media\_link

Matches Tweets that contain a media URL classified by Twitter. For example, pic.twitter.com.  

has:images  
Matches Tweets that contain a media URL classified by Twitter. For example, pic.twitter.com.  
has:videos  

_Available alias_: has:video\_link

Matches Tweets that contain native Twitter videos, uploaded directly to Twitter. This will not match on videos created with Vine, Periscope, or Tweets with links to other video hosting sites.

has:symbols  
Matches Tweets that contain a cashtag symbol (with a leading ‘$’ character. For example, $tag).

Connecting to a streaming endpoint

Connecting to a streaming endpoint
==================================

Establishing a connection to the streaming APIs means making a very long lived HTTP request, and parsing the response incrementally. Conceptually, you can think of it as downloading an infinitely long file over HTTP.

Authentication
--------------

The following authentication methods are supported by the Streaming APIs:

|     |     |     |
| --- | --- | --- |
| Auth Type | Supported APIs | Description |
| [OAuth](https://developer.twitter.com/en/docs/basics/authentication/overview) | * Track API Stream | Requests must be authorized [according to the OAuth specification](https://developer.twitter.com/content/developer-twitter/en/docs/authentication) . |
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

Rule limits

Rule limits
-----------

Twitter will now begin to enforce long-held contractual limits for the number of rules that a customer is able to add to their stream by enforcing rule limits on PowerTrack. While these limits have always been observed, we are now making it easier for customers to know where their limits stand and how close they are to their cap. Functionality has been added to our console that will allow you to observe your current rule count for each product and stream. This information can be found on the right hand side of a product page just under the activity counter (see below).

  

This can also be found under the rules section of the usage tab (see below).

  

  
What If I Hit My Cap?
------------------------

If you attempt to upload more rules to your stream that you are contractually allowed, you will receive the following message:

_“Request exceeds account’s Rule Limit. Delete rules or contact your account manager to proceed.”_

If you encounter this error message while you have an open connection, your stream will not be disrupted. In order to add more rules once you hit your cap, you will either need to delete rules from your stream or reach out to your account manager to increase your contractual limit.

Recovery and redundancy features

Introduction
------------

With streaming high volumes of realtime Tweets comes a set of best practices that promote both data reliability and data full-fidelity. When consuming realtime data, maximizing your connection time is a fundamental goal. When disconnects occur, it is important to automatically detect that and reconnect. After reconnecting it’s important to assess if there are any periods to backfill data for. The component that manages these details and consumes realtime Tweets is only one part of a system with network, datastore, server, and storage concerns. Given the complexity of these systems, another best practice is to have different streaming environments, with at least separate streams for development/testing and production.

PowerTrack comes with a set of features that help with these efforts.

To support multiple environments, we can deploy [Additional Streams](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/guides/powertrack_recovery_and_redundancy_features#additional_streams) for your account. These streams are completely independent of each other, having unique URLs and separate rule sets.

To help support maintaining a connection, each realtime PowerTrack stream supports [Redundant Connections](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/guides/powertrack_recovery_and_redundancy_features#redundant_connections). The most common architecture is for a stream to have two connections, and on the client-side there are two independent consumers, ideally on different networks. With this design, there can be redundancy across the client-side networks, servers, and datastore pathways. Note that a full-copy of the data is served on each connection (since there is a single ‘source’ server and no partitioning with filtered streams) and the client-side must be tolerant of and manage these duplicate data.

For detecting disconnects, each stream has a ‘heartbeat’ signal that can used to detect when a stream has timed-out. These 10-second heartbeats provide connection confirmation even when there are time periods with no Tweets matching your rules and being delivered on your stream. For most Twitter stream consumers, the data volumes are high enough that even a smaller duration of no Tweets is a sign of a connection issue. So both a ‘data silence’ and lack of a heartbeat can be used to detect a disconnect.

Since disconnects will happen, PowerTrack has a dedicated [Recovery](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/guides/powertrack_recovery_and_redundancy_features#replay) and a PowerTrack [Backfill](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/guides/powertrack_recovery_and_redundancy_features#backfill) feature to help recover data that was missed due to disconnections and other operational issues. To learn more about disconnects see our support article [HERE](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/guides/disconnections-explained).  
 

Additional streams 
-------------------

Having additional PowerTrack streams is another way to help build reliability into your solution. So much so that it is considered a best practice. Any additional streams are completely independent, having their unique endpoint and independent rule set. Each stream is assigned its own ‘label’, and this label, along with your account name, are part of that stream’s URL.

https://gnip-stream.twitter.com/stream/powertrack/accounts/{ACCOUNT\_NAME}/publishers/twitter/{STREAM\_LABEL}.json  

The most common convention is to have a realtime stream dedicated for your production system, and an additional stream available for development and testing. Having a test/development stream enables PowerTrack customers to have a stream to test client consumer updates. While any (unique) label can be assigned to a stream, one convention is to use ‘prod’ for production stream, and ‘dev’ or ‘sandbox’ for an additional development stream.

The number of streams, and their unique labels, is configurable by your account representative.  
 

Redundant connections 
----------------------

A redundant connection simply allows you to establish more than 1 simultaneous connections to the data stream. This provides redundancy by allowing you to connect to the same stream with two separate consumers, receiving the same data through both connections. Thus, your app has a hot failover for various situations, e.g. where one stream is disconnected or where your app’s primary server fails.

The number of connections allowed for any given stream is configurable by your account representative. To use a redundant stream, simply connect to the same URL used for your primary connection. The data for your stream will be sent through both connections, with both stream connections represented on the stream dashboard.

Note that for billing purposes, we deduplicate the activity counts you receive through multiple connections such that you are only billed for each unique activity once.  
 

Recovery 
---------

#### Overview 

Recovery is a data tool that provides streaming access to a rolling window of recent Twitter historical data. It should be utilized to recover data in scenarios where your consuming application misses data in the real time stream, whether due to disconnecting for a short period, or for any other scenario where you fail to ingest realtime data for a period of time.

There are different varieties of Recovery streams, corresponding to different types of realtime streams that they complement. PowerTrack Recovery streams are provided to allow customers using realtime PowerTrack to recover data they miss, using the same rules as they use in realtime.

#### Using Recovery 

With the Recovery stream, your app can make requests to it that operate in the same manner as requests to existing realtime streams. However, your app must specify parameters in the URL that indicate the time window you are requesting. In other words, a Recovery request asks for “Posts from time A to time B.” These Posts are then delivered through your streaming connection in a manner that mimics the realtime stream.

Posts are delivered beginning with the first minute of the specified time period, continuing until the final minute is delivered. At that point, a “Recovery Request Completed” message is sent through the connection, and the connection is then closed by Gnip. If your request begins at a time of day where little or no matching results occurred, there will likely be some period of time before the first results are delivered – data will be delivered when Recovery encounters matches in the portion of the archive being processed at that time. When no results are available to deliver, the stream will continue sending carriage-return “heartbeats” through the connection to prevent you from timing out.

Recovery is intended as a tool for easily recovering data missed due to short disconnects, not for very long time periods like entire days. If the need to recover data for long periods arises, we recommend breaking longer requests into shorter time windows (e.g. two hours) to reduce the possibility of being disconnected mid-request due to internet volatility or other reasons, and to provide more visibility into the progress of long requests.

#### Data availability

You can use the Recovery feature to recover missed data within the last 24 hours if you are unable to reconnect with the 5 minute backfill window.

The streaming recovery feature allows you to have an extended backfill window of 24 hours. Recovery enables you to ‘recover’ the time period of missed data. A recovery stream is started when you make a connection request using 'startTime' and 'endTime' request parameters. Once connected, Recovery will re-stream the time period indicated, then disconnect.  

You will be able to make 2 concurrent requests to recovery at the same time, i.e. “two recovery jobs”. Recovery works technically in the same way as backfill, except a start and end time is defined. A recovery period is for a single time range.

| Name | Type | Description |
| --- | --- | --- |
| startTime | date (ISO 8601) | YYYY-MM-DDTHH:mm:ssZ (ISO 8601/RFC 3339).<br><br>Date in UTC signifying the start time to recover from. |
| endTime | date (ISO 8601) | YYYY-MM-DDTHH:mm:ssZ (ISO 8601/RFC 3339).<br><br>Date in UTC signifying the end time to recover to. |

 [](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/api-reference/replay-stream)

Backfill 
---------

The Backfill feature is used to request up to 5 minutes of stream data that is missed after a disconnect, and is available on PowerTrack and Volume streams as an _optional_ feature.

To request backfill, you need to add a ‘backfillMinutes=number’ parameter to your connection request, where ‘number’ is the number of minutes (1-5, whole numbers only) to backfill when the connection is made. For example, if you disconnect for 90 seconds, you should add ‘backfillMinutes=2’ to your connection request. Since this request will provide backfill for 2 minutes, including for the 30-second period before you disconnected, your _consumer app must be tolerant of duplicate data_.

An example PowerTrack connection request URL, requesting a 5 minute backfill, looks like:

https://gnip-stream.twitter.com/stream/powertrack/accounts/{ACCOUNT\_NAME}/publishers/twitter/{STREAM\_LABEL}.json?backfillMinutes=5

**NOTES:**

* You do have the option to always use ‘backfillMinutes=5’ when you connect, then handling any duplicate data that is provided.
    
* If you are disconnected for more than five minutes, you can recover data using the Recovery.  
     
    

Recovering from disconnect 
---------------------------

Restarting and recovering from a disconnect involves several steps:

* Determining length of disconnect time period.
    * 5 minutes or less?
        * If you have Backfill enabled for stream, prepare connection request with appropriate ‘backfillMinutes’ parameter.
    * More than 5 minutes?
        * Make a connection request using 'startTime' and 'endTime' request parameters in order to start a recovery stream. The streaming recovery feature allows you to have an extended backfill window of 24 hours. Recovery enables you to 'replay' the time period of missed data.
* Request a new connection.

Planning for high-volume social data events

Planning for high-volume social data events
-------------------------------------------

Major national and global events are often accompanied by dramatic spikes in user activity across social media platforms. Sometimes these events are known about in advance, like the Super Bowl, political elections, and New Year’s celebrations around the world. Other times, the spikes in volume are due to unexpected happenings such as natural disasters, unplanned political events, or surprise pop culture moments like Ellen’s famous selfie Tweet at the Oscars.

These bursts of user activity can be short-lived (measured in seconds) or they may be sustained over several minutes’ time. No matter their origin, it is important to consider the impact that they can have on applications consuming realtime data from Twitter.

Here are some best practices that will help your team prepare for high-volume social data events.

#### Review your current PowerTrack rules

* Certain keywords can skyrocket during high volume events, for instance brand mentions when a brand sponsors a major sporting event.
* Be careful to avoid any unnecessary or overly generic PowerTrack rules that may generate unnecessary activity volumes.
* Consider communicating with your clients prior to known high-volume events to help them plan appropriately.

#### Stress test your application

Anticipate that burst volumes may reach 5-10x average daily consumption levels. Depending on your PowerTrack rule set, the increase may be much higher.

#### Optimize to stay connected

With realtime streams, staying connected is essential to avoid missing data. Your client application should be able to detect a disconnect and have logic to immediately retry its connection, using an exponential backoff if the reconnect attempt fails.

#### Add built-in buffering on your end

Building a multi-threaded application is a key strategy for handling high-volume streams. At a high-level, a best practice for managing data streams is to have a separate thread/process that establishes the streaming connection and then writes received JSON activities to a memory structure or a buffered stream reader. This ‘light-weight’ stream processing thread is responsible for handling incoming data, which can be buffered in memory, growing and shrinking as needed. Then a different thread consumes that hash and does the ‘heavy lifting’ of parsing the JSON, preparing database writes, or whatever else your application needs to do.

#### Optional streaming data recovery tools

* [PowerTrack Replay](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/guides/powertrack_recovery_and_redundancy_features#replay) is available to recover missed activities should you experience an extended disconnection.
* [PowerTrack Backfill](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/guides/powertrack_recovery_and_redundancy_features) automates data recovery if you disconnect briefly. If you disconnect and reconnect within 5 minutes, your data will be buffered by Gnip and delivered automatically.
* If you are unsure whether your Gnip package includes these recovery features, be sure to contact your Account Manager to learn more.

#### Global events = global time zones

* The events may occur after business hours or over the weekend, so be sure that your team is prepared for spikes to occur outside your normal business hours.

#### Don’t Panic!

* As always, we recommend that you maintain your connections to Twitter real-time APIs and monitor for any changes in delivery latency.
* Twitter’s highly-scalable infrastructure ensures that none of your data will be lost or missed from any temporary increases in this latency.

Disconnections explained

Disconnections explained
------------------------

Disconnects from your PowerTrack stream can happen for a handful of reasons - whether they proactively planned or unplanned. Regardless of whether or not they were planned, any sort of disconnect can be surprising cause for data loss, but they don’t have to be. A basic understanding of the types of disconnects that you might encounter and how to quickly reconnect can mean the difference between a major issue and something that can be incorporated into your application design by reconnecting, or using Backfill or [Recovery](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/guides/powertrack_recovery_and_redundancy_features#replay). Please note that for any disconnect, forced or client-side, your [console.gnip.com dashboard](https://console.gnip.com/) will have a message that displays the kind of disconnect that you experienced and a timestamp for the disconnect.  

This article will go over the types of disconnects you might encounter, how to minimize their effects, and how to troubleshoot issues related to disconnects.  
 

### Forced disconnects  

At the highest level, forced disconnects happen when Twitter actively closes your connection to the stream. These can happen for a variety of reasons, and when you are force disconnected from your stream then Twitter will send a zero byte chunk in accordance with [HTTP chunked encoding practice](http://www.httpwatch.com/httpgallery/chunked/). In all cases of forced disconnects, you should be able to reconnect to the stream immediately and you should be sure to have [reconnect logic](https://developer.twitter.com/en/docs/tutorials/consuming-streaming-data#reconnecting) written into your code to prevent further data loss.

There are three types of forced disconnects that your app will need to be prepared for.  
 

#### **Twitter maintenance**

Twitter deploys for ongoing maintenance several times a week. During these updates, sometimes customer streams will experience one or more disconnects. This will be accompanied by a “Twitter is closing for operational reasons” message. These should be expected disconnections, and your application should be able to reconnect immediately, so make sure that you have [reconnect logic](https://developer.twitter.com/en/docs/tutorials/consuming-streaming-data#reconnecting) written into your application.  
 

#### **Full buffer disconnect**

A full buffer disconnect generally indicates that your application’s code isn’t keeping up with the amount of data that we’re streaming to you and there is a backup of cached data on the Twitter server side for your connection which needs to be flushed. This can happen after a major rule change, a [big event](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/guides/high-volume-social-data-events), or simply because your application is having trouble [consuming the stream](https://developer.twitter.com/en/docs/tutorials/consuming-streaming-data). Full buffer disconnects are triggered when your stream connection buffer hits a certain threshold of Tweets. If you are disconnected for a full buffer, reconnecting with [backfill](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/guides/powertrack_recovery_and_redundancy_features.html#backfill) is not available and data will begin streaming from the time you reconnect. It's likely that you will need to run a [Recovery](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/guides/powertrack_recovery_and_redundancy_features#replay) to recover Tweets lost in the disconnection. If you find that full buffer disconnects are happening frequently, reach out to the support team to assist you in making sure that your application is properly configured. 

Here are some suggestions to prevent these kinds of disconnects from occurring in the future:

1. Ensure nothing is slowing down the process reading from the stream. Do not do any processing in the process/thread that is reading from the stream. Instead, have this process read the message then pass off any processing (such as parsing, date calculations, etc) of the message to a separate process or thread.
2. Verify there are no network issues between your application and Twitter preventing messages from being sent.
3. Make sure you have sufficient bandwidth for the volume of activities on your stream.  Some streams can have high volumes requiring significant bandwidth (~10 Mbps is not unheard of). Keep in mind these streams require this bandwidth to be sustained 24 hours a day, including spikes that may cause 2-3 times the volume during significant world events. These spikes are often absorbed by Twitter's buffer, and are one of the reasons it is in place.  
     

#### **Too many connections**

Each stream is configured to allow for a specified number of connections. This number is determined between you and your account manager, and is available in your account agreement. If you connect to your stream with more connections than are allowed, you will be force disconnected. Any extra connections are allowed for approximately one minute. If after one minute an extra connection exists, the most recent connection is forced disconnected. Allowing an extra connection for a minute enables the customer to, for example, spin up a new server and connect with it, then teardown a server that is being ‘retired.’  
 

### Client disconnects  

A client disconnect is essentially any disconnection that occurs which isn’t initiated by our servers. There are many causes for this. Sometimes this could be caused by the code or the architecture of your application, but this often occurs when something in the internet or network layer cuts off the connection. This section provides a list of the most common causes for a client disconnects.  
 

**Issues at the network layer**

Routing issues at the networking level can cause disconnects. For example, a Border Gateway Protocol (BGP) update can go awry, and clients can disconnect as routers fail to keep up with the sudden additional load put on them when a route fails. As network operators cooperate to reroute traffic, you may notice a pattern of disconnects for some time.  
 

**Firewall configuration**

Clients may have firewalls set up with session limits that cut off the connections after a certain amount of time, which they need to create exceptions for. From our side, our servers just see the connection close, so we don’t have a way to see whether it was closed by the proactive actions of your app, or just something related to the internet connection between your client and the Twitter servers.  
 

**Data burst and packet loss**

Clients should be designed to handle spikes in the volume of Tweets received. If a client is slow to consume a stream, it will receive a [full buffer disconnect](#full_buffer_disconnect). However, there are situations where the client is not able to handle a sudden surge in volume (for example, after significant rule activity) which will cause the client to drop packets. When this happens, you may notice the client resetting a TCP/IP connection. In certain cases, the connection is terminated correctly and cleanly; however, there may be situations where the underlying networking layer doesn't close the socket properly, or does so after a set delay. In your dashboard, this event will be reported as a client disconnect. In such cases, clients must be sized to handle multiple times the average Tweet volume. It can be beneficial to examine the network traffic to detect any pattern that leads the client to drop packets.  
 

**Failure to reconnect after a disconnection**

Occasionally, some customers have trouble reconnecting to their stream after they’ve terminated a connection. Assuming there are no operational issues posted on our [Status Page](https://api.twitterstat.us/), one reason might be that something within your code is keeping the connection alive. In these scenarios, we see something in the layer outside of your app persisting, because the connection wasn’t properly terminated. Generally we see similar behavior when the HTTP client portion of the code isn’t getting proactively closed. It might also be that there is simply some network latency or delay set at the configuration level preventing the request from going through.

FAQ

Frequently asked questions
--------------------------

Enterprise

### Realtime PowerTrack API

**I am interested in Twitter data and would like to find out approximate subscription costs.**

Please fill out [this form](https://developer.twitter.com/en/enterprise-application) to get in touch with our Sales team.  
 

**What are some of the features provided by realtime PowerTrack?**  

By connecting directly to our data services, you can take advantage of many enterprise-ready features that provide reliable connectivity and full-fidelity data. As an enterprise licensed-access offering, realtime PowerTrack includes tools for dynamic filtering, consistent connection, data recovery and data compliance management. This technology, paired with operational monitoring, guaranteed support and integration services allows businesses to start with a strong foundation to serve their own customers.

These features include:

* Dynamic rule updates while connected to the stream. There is no need to disconnect your stream while you update your stream’s ruleset.
* Support for multiple connections to each stream.
* Ability to automatically recover data that is missed during brief disconnects when you reconnect within 5 minutes with Backfill.
* Availability of Recovery feature to recover missed data within the last 24 hours if you are unable to reconnect with the 5 minute backfill window.
* Availability of additional streams for testing and development.
* Status dashboard to communicate with customers about any operational issues.  
     

**How do I consume streaming data?**

Realtime streams of data are initiated by sending a HTTP GET command to your custom `https://gnip-stream.twitter.com` URL. HTTP streaming connections are requested with HTTP headers that indicate a ‘keep-alive’ connection. More information on realtime streaming is available [here](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/overview).

Given the potential of high volumes of Twitter data delivered in a stream, it is highly recommended that incoming data is processed in an asynchronous fashion. What this means is that your code that ‘hosts’ the client side of the stream simply inserts incoming Tweets into a (FIFO) queue, or similar memory structure, and then you have a separate process/thread that consumes Tweets from that queue and does more of the ‘heavy lifting’ of parsing and preparing the data for storage. With this design, you can implement a process that will bend but not break in case incoming data volumes change dramatically.  
 

**How can multiple customers, projects, and campaigns be managed in a single stream?**

The vast majority of realtime PowerTrack users manage multiple customers, projects, and campaigns within a single realtime stream by using [PowerTrack rule ‘tags’](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/overview). Rule tags have no special meaning, they are simply treated as opaque strings carried along with the rule. They will be included in the “matching rules” metadata in activities returned.

Tags provide an easy way to create logical groupings of PowerTrack rules. For example, you may generate a unique ID for a specific rule as its tag and allow your application to reference that ID within activities it processes to associate a result with specific customers, campaigns, categories, or other related groups.  
 

**How many connections to a given PowerTrack stream can I have at one time?**

PowerTrack streams support multiple connections to a single endpoint. Having multiple connections enables customers to build redundant data consumer clients, ideally on different networks. While PowerTrack streams default to a single connection, many customers prefer to have two connections per PowerTrack stream to ensure continuous delivery. If multiple connections are made to a single endpoint, and/or multiple streams exist with common rules, a given Tweet will be received multiple times. Note that for accounting purposes, the Tweet will be counted once.

Please talk to your Account Manager for more information.  
 

**How 'realtime' are the results? Is there any delay/elaboration time between the publication of a Tweet on Twitter and their release on the PowerTrack stream?**

Tweets that match your ruleset will be delivered to your stream within seconds of being published on the platform. There are variables, such as network connectivity and how your consuming application reads data off the stream; but all things being equal, you should receive Tweets within seconds of them being published.

Please note that the URL enrichment does cause an increased latency, due to the unwinding of each URL in the Tweet. 

Generally speaking, you should expect Volume streams (e.g. Firehose and [Decahose](https://developer.twitter.com/en/docs/twitter-api/enterprise/decahose-api/overview)) to be faster than [PowerTrack](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/overview), and PowerTrack to be fast than [statuses/filter](https://developer.twitter.com/en/docs/tweets/filter-realtime/api-reference/post-statuses-filter).  
 

**Is it possible to update several rules in one go?**

Yes, you can add or delete several rules with one request.  
  
However, note that the add and delete steps are separate and you will need two requests: one request to add one or several rule(s) and another request to delete one or several rule(s).

The upper limit number of rules that can either be added or be deleted in one go is a JSON body that is 5MB or less in size. Depending on the length of your rule values and tags, the upper number will be in the lower thousands.  
 

**Why isn't my rule appearing on the stream right away?**

Most rule additions take effect almost immediately. However, depending on factors such as network connectivity and rule size/complexity, it may take up to 5 minutes before you start receiving matching Tweets.  
 

**What if some Tweets are missing: I was expecting them to be returned by the stream, but they weren't?**

You can follow the next few steps to understand why some Tweets might not have been delivered:

1. Check your [rule](https://developer.twitter.com/en/docs/twitter-api/enterprise/rules-and-filtering/enterprise-operators) and ensure that you are using the correct operators.
2. Were you connected to the stream when the Tweet was created? You can use the 'Connections' tab in the [console](https://console.gnip.com/) to check your connection history.
3. Was your rule already in place when the Tweet was created?
4. Note that if the account from which the Tweet was sent was private at the time the Tweet was created, the Tweet won't be returned - even if the account is public at the time of the request.
  

**If I lose the connection to the stream and then connect back, will I lose all Tweets from that duration?**

Yes, if you lose the connection to the stream, you may be missing data for the period of time that you were disconnected from the stream. Whenever a disconnection occurs, your client app must restart the process by establishing a new connection.

Additionally, to ensure that you do not miss any data, you may need to utilize a [Redundant Connection](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/guides/powertrack_recovery_and_redundancy_features#redundant_connections), [Backfill](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/guides/powertrack_recovery_and_redundancy_features#backfill), or a [Replay stream](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/api-reference/replay-stream) to mitigate or recover data from disconnections from the stream. Please see our answer to the next question for more information.  
 

**What if I get disconnected from the stream? How can I collect any data that was missed while disconnected?**

When streaming data, the goal is to stay connected for as long as possible, recognizing that disconnects will occur. PowerTrack streams provide a 15-second heartbeat (in the form of a new-line character) that enable client applications to detect disconnects. When fresh data and the heartbeat stop arriving, reconnection logic should be triggered. In most software languages this can be easily implemented by setting a data read timeout.

Any time you disconnect from the stream, you are potentially missing data that would have been sent if connected. However, there are multiple ways to mitigate these disconnects and recover data when they occur.

There is a range of tools available for retrieving historical tweets, including:

1. [Redundant Streams](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/guides/powertrack_recovery_and_redundancy_features#redundant_connections) - With multiple connections, consume the stream from multiple servers to prevent missed data when one is disconnected.
2. [Recovery](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/api-reference/replay-stream) - Recover data within the last 24 hours.
3. [Backfill](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/guides/powertrack_recovery_and_redundancy_features#backfill) - Reconnect within 5 minutes and start from where you left off.
4. [Full Archive Search](https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/quick-start/enterprise-full-archive) - Recover data from the entire Twitter archive.

  
Please also refer to [our documentation on disconnects](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/guides/disconnections-explained).  
 

**How fast is the streaming speed of Recovery?**

Recovery will deliver up to 1000 posts per second. It is intended to deliver the posts for the period of time that a customer is disconnected.

**Do you have any realtime PowerTrack code examples I can use to get started with?**

Yes, we have several realtime code examples available, including:

* [Sample Python scripts](https://github.com/twitterdev/python-enterprise-scripts/blob/master/python_stream_sample.py)
* [Sample Ruby scripts](https://github.com/twitterdev/ruby-enterprise-scripts/tree/master/PowerTrack)

Note that these are only available to enterprise customers.

**How do Edit Tweets impact my usage and billing?**   

Only the original Tweet will count for billing purposes. Any subsequent edits will be ignored and not contribute to your overall activity count. 

###   
Error troubleshooting guide

**Code 429 - Rate Limited: Your app has exceeded the limit on requests to add, delete, or list rules for this stream**

You may be receiving the 429 error code because you are adding or deleting rules too quickly. If you are adding or deleting rules individually, this could add up and exceed the rate limit.

A workaround could be to add or delete several rules at one time.

For example, the below sample cURL command shows you how to delete several rules at once:

    curl -v -X POST -uexample@customer.com "https://gnip-api.twitter.com/rules/powertrack/accounts/:account_name/publishers/twitter/:stream_label.json?_method=delete" -d '{"rule_ids":[734938587381145604,734938587381174273]}"

  
You can learn more about adding or deleting rules and the relevant rate limits [here](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/api-reference/powertrack-rules).  
 

**Code 400**

A 400 error code normally indicates that the server was unable to process the request sent by the client due to poorly formatted JSON.

There are many reasons why this might be the case and you will need to double check the format of your JSON query.

For example, you may need to escape the quotes around the exact phrase match(es) in your rule (as in the example below):

{"rules":\[{"tag":"test1","value":"coffee OR \\"I love coffee\\""}\]}  

**  
Frequent Disconnects - I am experiencing frequent disconnections on the stream and one of the following messages is being returned. Why is this happening?**

`This stream has been disconnected because your client was unable to keep up with us.`

`This stream has been disconnected for operational reasons.`

This kind of error occurs when your stream is not keeping up with the speed at which we are delivering data and your app isn't consuming the data from the stream fast enough.

We allow delivery to get behind for a period of time, and we have a temporary staging buffer amount for each stream on our side; but if you don't catch up, we initiate a disconnect to allow you to reconnect at the current point in time. Please note that this may lead to data loss (for data that is within the buffer at the time of the full buffer disconnect).

These can occur around large spikes in data. Generally, we recommend using a buffer process for consuming data quickly that is separate from the processing process.

You can find out more about optimizing your app to prevent disconnects like this in our articles on [connection](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/guides/disconnections-explained) and on consuming streaming data [here](https://developer.twitter.com/en/docs/tutorials/consuming-streaming-data) and [here](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/guides/high-volume-social-data-events).

PowerTrack API

powertrack-stream

PowerTrack API
==============

Jump to on this page

[Methods](#Methods)

[Authentication](#Authentication)

[GET /track/:stream](#Stream)

Methods [¶](#methods- "Permalink to this headline")
---------------------------------------------------

| Method | Description |
| --- | --- |
| [GET /track/:stream](#Stream) | Connect to the data stream |

Authentication [¶](#authentication- "Permalink to this headline")
-----------------------------------------------------------------

All requests to the PowerTrack API must use HTTP Basic Authentication, constructed from a valid email address and password combination used to log into your account at console.gnip.com. Credentials must be passed as the Authorization header for each request. Make sure your client is adding the "Authentication: Basic" HTTP header (with encoded credentials over HTTPS) to all API requests.

GET /track/:stream [¶](#get-track-stream- "Permalink to this headline")
-----------------------------------------------------------------------

Establishes a persistent connection to the PowerTrack data stream, through which the social data will be delivered.

**IMPORTANT:** After you establish the connection [see here](https://developer.twitter.com/en/docs/tutorials/consuming-streaming-data) for details on consuming streaming data.

|     |     |
| --- | --- |
| **Request Method** | HTTP GET |
| **Connection Type** | Keep-Alive  <br>  <br>This should be specified in the header of the request. |
| **URL** | Found on the stream's API Help page of your console dashboard, and resembles the following structure:  <br>  <br><br>[https://gnip-stream.twitter.com/stream/powertrack/accounts/](https://gnip-stream.twitter.com/stream/powertrack/accounts/){gnip\_account\_name}/publishers/twitter/{stream\_label}.json |
| **Compression** | Gzip. To connect to the stream using Gzip compression, simply send an Accept-Encoding header in the connection request. The header should look like the following:  <br>  <br>Accept-Encoding: gzip |
| **Character Encoding** | UTF-8 |
| **Response Format** | JSON. The header of your request should specify JSON format for the response. |
| **Rate Limit** | 60 requests per minute. |
| **Read Timeout** | Set a read timeout on your client, and ensure that it is set to a value beyond 30 seconds. |
| **Support for Tweet edits** | All Tweet objects will include Tweet edit metadata describing the Tweet's edit history. See the ["Edit Tweets" fundamentals page](https://developer.twitter.com/en/docs/twitter-api/enterprise/edit-tweets) for more details. |

  

#### Responses

The following responses may be returned by the API for these requests. Most error codes are returned with a string with additional details in the body. For non-200 responses, clients should attempt to reconnect.

| Status | Text | Description |
| --- | --- | --- |
| 200 | Success | The connection was successfully opened, and new activities will be sent through as they arrive. |
| 401 | Unauthorized | HTTP authentication failed due to invalid credentials. Log in to console.gnip.com with your credentials to ensure you are using them correctly with your request. |
| 406 | Not Acceptable | Generally, this occurs where your client fails to properly include the headers to accept gzip encoding from the stream, but can occur in other circumstances as well.  <br>  <br>Will contain a JSON message similar to "This connection requires compression. To enable compression, send an 'Accept-Encoding: gzip' header in your request and be ready to uncompress the stream as it is read on the client end." |
| 429 | Rate Limited | Your app has exceeded the limit on connection requests. |
| 503 | Service Unavailable | Twitter server issue. Reconnect using an exponential backoff pattern. If no notice about this issue has been posted on the [Twitter API Status Page](https://api.twitterstat.us/), contact support or emergency if unable to connect after 10 minutes. |

  

**Example curl Request**

The following example request is accomplished using cURL on the command line. However, note that these requests may also be sent with the programming language of your choice.

curl --compressed -v -uexample@customer.com "https://gnip-stream.twitter.com/stream/powertrack/accounts/:account\_name/publishers/twitter/:stream\_label.json"

PowerTrack Rules API

powertrack-rules

PowerTrack Rules API
====================

Jump to on this page

[Methods](#Methods)

[Authentication](#Authentication)

[POST /rules](#AddRules)

[GET /rules](#ListRules)

[GET /rules/:rule\_id](#GetRule)

[POST /rules \_method=get](#GetRules)

[POST /rules \_method=delete](#DeleteRules)

[POST /validation](#ValidateRules)

Methods [¶](#methods- "Permalink to this headline")
---------------------------------------------------

| Method | Description |
| --- | --- |
| [POST /rules](#AddRules) | Add rules to the stream |
| [GET /rules](#ListRules) | Retrieve all rules currently in place on the stream |
| [GET /rules/:rule\_id](#GetRule) | Retrieve an existing rule on the stream by rule ID |
| [POST /rules \_method=get](#GetRules) | Retrieve multiple rules on the stream by rule IDs |
| [POST /rules \_method=delete](#DeleteRules) | Delete rules from the stream |
| [POST /validation](#ValidateRules) | Validate PowerTrack rule syntax |

Authentication [¶](#authentication- "Permalink to this headline")
-----------------------------------------------------------------

All requests to the PowerTrack rules API must use HTTP Basic Authentication, constructed from a valid email address and password combination used to log into your account at console.gnip.com. Credentials must be passed as the Authorization header for each request. Make sure your client is adding the "Authentication: Basic" HTTP header (with encoded credentials over HTTPS) to all API requests.

POST /rules [¶](#post-rules- "Permalink to this headline")
----------------------------------------------------------

Adds one or many rules to your PowerTrack stream's ruleset.

#### Request Specifications

|     |     |
| --- | --- |
| **Request Method** | HTTP POST |
| **Content Type** | "application/json". The request should specify this as the "Content-type". |
| **URL** | Found on the [Console - Products API Help tab](https://developer.twitter.com/en/docs/twitter-api/enterprise/console/product), and uses the following structure:  <br>  <br>`https://data-api.twitter.com/rules/powertrack/accounts/{gnip_account_name}/publishers/twitter/{stream_label}.json` |
| **Character Encoding** | UTF-8 |
| **Request Body Format** | JSON |
| **Request Body Size Limit** | 5 MB |
| **Rate Limit** | 60 requests per minute, aggregated across all requests to /rules endpoint for the specific stream's API (POST and GET). Rule addition requests will be processed serially and will be rejected if you have more than one rule request happening at the same time. |

  

#### Request Body Content

Your request should provide rule data in the following format with the defined Content-type: "application/json":

    {
        "rules":
        [
            {"value":"rule1","tag":"tag1"},
            {"value":"rule2","tag":"tag2"}
        ]
    }

  

**Example curl Request**

The following example requests demonstrate how to add rules using cURL on the command line, using JSON rules.

    curl -v -X POST -uexample@customer.com "https://data-api.twitter.com/rules/powertrack/accounts/:account_name/publishers/twitter/:stream_label.json" -d '{"rules":[{"value":"rule1","tag":"tag1"},{"value":"rule2","tag":"tag2"}]}'

  

    curl -v -X POST -uexample@customer.com "https://data-api.twitter.com/rules/powertrack/accounts/:account_name/publishers/twitter/:stream_label.json" -d @arrayofrulesfile_max5mb.json

  

    curl -v -X POST -uexample@customer.com "https://data-api.twitter.com/rules/powertrack/accounts/companyname/publishers/twitter/prod.json" -d '{"rules":[{"value":"(#snow OR snowday OR "snow day" OR from:noaa) lang:en","tag":"4581245"},{"value":"(skiing OR boarding OR "hitting the slopes" OR from:OnTheSnow) lang:en","tag":"4581267"}]}'

  

#### Responses

The following responses may be returned by the API for these requests. Non-200 responses should be retried after making any necessary modifications in the rules.

| Status | Text | Description |
| --- | --- | --- |
| 201 | Created | The rule or rules were successfully added to your PowerTrack ruleset. |
| 400 | Bad Request | Generally relates to poorly formatted JSON, and includes an "Invalid JSON" message in the response. |
| 401 | Unauthorized | HTTP authentication failed due to invalid credentials. Log in to console.gnip.com with your credentials to ensure you are using them correctly with your request. |
| 422 | Unprocessable Entity | Generally occurs due to an invalid rule, based on the PowerTrack rule restrictions. Requests fail or succeed as a batch. For these errors, each invalid rule and the reason for rejection is included in a JSON message in the response. Catch the associated exception to expose this message. |
| 429 | Rate Limited | Your app has exceeded the limit on requests to add, delete, or list rules for this stream. |
| 503 | Service Unavailable | Twitter server issue. Reconnect using an exponential backoff pattern. If no notice about this issue has been posted on the [Twitter API Status Page](https://api.twitterstat.us/) contact support or contact emergency if still unable to connect after 10 minutes. |

  

**Example Responses**

This response indicates that all rules (two in this case) were successfully created.

    HTTP/1.1 201 Created
    {
        "summary": {
            "created": 2,
            "not_created": 0
        },
        "detail": [{
            "rule": {
                "value": "(#snow OR snowday OR \"snow day\" OR from:noaa) lang:en",
                "tag": "4581245",
                "id": 734938587381145604
            },
            "created": true
        }, {
            "rule": {
                "value": "(skiing OR boarding OR \"hitting the slopes\" OR from:OnTheSnow) lang:en",
                "tag": "4581267",
                "id": 734938587381174273
            },
            "created": true
        }],
        "sent": "2016-05-24T02:46:28.402Z"
    }

This response indicates that one rule was successfully created, and two were not created because they already exist. Rules are indexed by rule value (syntax). For rules not created there is a 'message' field explaining why the rule could not be created.

    HTTP/1.1 201 Created
    {
        "summary": {
            "created": 1,
            "not_created": 2
        },
        "detail": [{
            "rule": {
                "value": "robot OR 🤖",
                "tag": "botrule123",
                "id": 734861971116285952
            },
            "created": true
        }, {
            "rule": {
                "value": "fish OR 🐟",
                "tag": "fishrule123"
            },
            "created": false,
            "message": "A rule with this value already exists"
        }, {
            "rule": {
                "value": "Pizza OR 🍕",
                "tag": "pizzarule123"
            },
            "created": false,
            "message": "A rule with this value already exists"
        }],
        "sent": "2016-05-23T21:42:01.661Z"
    }

The following responses indicate that no rules were created. In each case there is a 'message' field explaining why the rule could not be created. Note that when one or more rules are invalid, no rules are added (even rules with valid syntax).

  

    HTTP/1.1 422 Unprocessable Entity
    {
        "summary": {
            "created": 0,
            "not_created": 2
        },
        "detail": [{
            "rule": {
                "value": "streaming gnip contains:$twtr",
                "tag": null
            },
            "created": false,
            "message": "no viable alternative at input '$twtr' (at position 25)\n"
        }, {
            "rule": {
                "value": "streaming gnip contains:\"$twtr\"",
                "tag": null
            },
            "created": false
        }],
        "sent": "2016-06-01T15:41:27.451Z"
    }

  

    HTTP/1.1 422 Unprocessable Entity
    {
        "summary": {
            "created": 0,
            "not_created": 1
        },
        "detail": [{
            "rule": {
                "value": "-follow",
                "tag": null
            },
            "created": false,
            "message": "Rules must contain a non-negation term (at position 1)\nRules must contain at least one positive, non-stopword clause (at position 1)\n"
        }],
        "sent": "2016-05-23T18:34:25.218Z"
    }

  

    HTTP/1.1 422 Unprocessable Entity
    {
        "summary": {
            "created": 0,
            "not_created": 1
        },
        "detail": [{
            "rule": {
                "value": "streaming AND lang:en",
                "tag": null
            },
            "created": false,
            "message": "Ambiguous use of and as a keyword. Use a space to logically join two clauses, or \"and\" to find occurrences of and in text (at position 11)\n"
        }],
        "sent": "2016-05-23T21:39:49.612Z"
    }

  

GET /rules [¶](#get-rules- "Permalink to this headline")
--------------------------------------------------------

Retrieve all rules currently in place on the stream

#### Request Specifications

|     |     |
| --- | --- |
| **Request Method** | HTTP GET |
| **URL** | Found on the [Console - Products API Help tab](https://developer.twitter.com/en/docs/twitter-api/enterprise/console/product), and uses the following structure:  <br>  <br>`https://data-api.twitter.com/rules/powertrack/accounts/:account_name/publishers/twitter/:stream_label.json` |
| **Rate Limit** | 60 requests per minute, aggregated across all requests to /rules endpoint for the specific stream's API (POST and GET). |

  

**Example cURL Request**

The following example request demonstrates how to retrieve rules using cURL on the command line.

    curl -v -uexample@customer.com "https://data-api.twitter.com/rules/powertrack/accounts/:account_name/publishers/twitter/:stream_label.json"

#### Response

The following responses may be returned by the API for these requests. Non-200 responses should be retried, utilizing an exponential backoff for subsequent requests.

| Status | Text | Description |
| --- | --- | --- |
| 200 | OK  | The request was successful, and the current ruleset is returned in JSON format. |
| 400 | Bad Request | Generally relates to poorly formatted JSON, and includes an "Invalid JSON" message in the response. |
| 401 | Unauthorized | HTTP authentication failed due to invalid credentials. Log in to console.gnip.com with your credentials to ensure you are using them correctly with your request. |
| 429 | Rate Limited | Your app has exceeded the limit on requests to add, delete, or list rules for this stream. |
| 503 | Service Unavailable | Twitter server issue. Reconnect using an exponential backoff pattern. If no notice about this issue has been posted on the [Twitter API Status Page](https://api.twitterstat.us/) contact support. |

  

**Example Response**

    HTTP/1.1 200 OK
    {
        "rules": [{
            "value": "from:twitterdev",
            "tag": "tweetsfromtwitterdev123",
            "id": 735163830813134848
        }, {
            "value": "fish OR 🐟",
            "tag": "fishrule123",
            "id": 738034522583769088
        }, {
            "value": "Pizza OR 🍕",
            "tag": "pizzarule123",
            "id": 738034522579554304
        }, {
            "value": "robot OR 🤖",
            "tag": "botrule123",
            "id": 738034522579570689
        }],
        "sent": "2016-06-01T15:52:37.341Z"
    }

  

GET /rules/:rule\_id [¶](#get-rules-rule-id- "Permalink to this headline")
--------------------------------------------------------------------------

Retrieve an existing rule on the stream by rule ID. Note that all rules are assigned a unique ID by Twitter at the time of creation, rules that are deleted and recreated will receive a different unique rule ID.

#### Request Specifications

|     |     |
| --- | --- |
| **Request Method** | HTTP GET |
| **URL** | Found on the [Console - Products API Help tab](https://developer.twitter.com/en/docs/twitter-api/enterprise/console/product), and uses the following structure:  <br>  <br>`https://data-api.twitter.com/rules/powertrack/accounts/:account_name/publishers/twitter/:stream_label/rules/:rule_id.json` |
| **Rate Limit** | 60 requests per minute, aggregated across all requests to /rules endpoint for the specific stream's API (POST and GET). |

  

**Example cURL Request**

The following example request demonstrates how to retrieve a rule by rule\_id using cURL on the command line.

    curl -v -uexample@customer.com "https://data-api.twitter.com/rules/powertrack/accounts/:account_name/publishers/twitter/:stream_label/rules/:rule_id.json"

  

    curl -v -uexample@customer.com "https://data-api.twitter.com/rules/powertrack/accounts/companyname/publishers/twitter/prod/rules/735163830813134848.json"

#### Response

The following responses may be returned by the API for these requests. Non-200 responses should be retried, utilizing an exponential backoff for subsequent requests.

| Status | Text | Description |
| --- | --- | --- |
| 200 | OK  | The request was successful, and the current rule is returned in JSON format. |
| 400 | Bad Request | Generally relates to poorly formatted JSON, and includes an "Invalid JSON" message in the response. |
| 401 | Unauthorized | HTTP authentication failed due to invalid credentials. Log in to console.gnip.com with your credentials to ensure you are using them correctly with your request. |
| 429 | Rate Limited | Your app has exceeded the limit on requests to add, delete, or list rules for this stream. |
| 503 | Service Unavailable | Twitter server issue. Reconnect using an exponential backoff pattern. If no notice about this issue has been posted on the [Twitter API Status Page](https://api.twitterstat.us/) contact support. |

  

**Example Response**

    HTTP/1.1 200 OK
    {
        "rules": [{
            "value": "from:twitterdev",
            "tag": "tweetsfromtwitterdev123",
            "id": 735163830813134848
            "id_str":"735163830813134848"
        }],
        "sent": "2016-06-01T15:52:37.341Z"
    }

  

POST /rules \_method=get [¶](#post-rules--method-get- "Permalink to this headline")
-----------------------------------------------------------------------------------

Retrieves requested existing rules by list of rule IDs currently on a stream.

#### Request Specifications

|     |     |
| --- | --- |
| **Request Method** | HTTP POST |
| **URL** | Found on the API Help page, and uses the following structure:  <br>  <br>`https://data-api.twitter.com/rules/powertrack/accounts/{gnip_account_name}/publishers/twitter/{stream_label}.json?_method=get` |
| **Character Encoding** | UTF-8 |
| **Request Body Format** | JSON |
| **Request Body Size Limit** | 5 MB |
| **Rate Limit** | 60 requests per minute, aggregated across all requests to /rules endpoint for the specific stream's API (POST and GET). |
| **Compression** | Gzip compression is supported, but not required for these requests. |

  

**Example curl Request**

The following example request demonstrates how to add rules using cURL on the command line.

    curl -v -X POST -uexample@customer.com \
    "https://data-api.twitter.com/rules/powertrack/accounts/:account_name/publishers/twitter/:stream_label.json?_method=get" \
    -d '{"rule_ids":[734938587381145604,734938587381174273]}"

  

#### Response

The following responses may be returned by the API for these requests. Non-200 responses should be retried, utilizing an exponential backoff for subsequent requests.

| Status | Text | Description |
| --- | --- | --- |
| 200 | OK  | The request was successful, and the current ruleset is returned in JSON format. |
| 400 | Bad Request | Generally relates to poorly formatted JSON, and includes an "Invalid JSON" message in the response. |
| 401 | Unauthorized | HTTP authentication failed due to invalid credentials. Log in to console.gnip.com with your credentials to ensure you are using them correctly with your request. |
| 429 | Rate Limited | Your app has exceeded the limit on requests to add, delete, or list rules for this stream. |
| 503 | Service Unavailable | Twitter server issue. Reconnect using an exponential backoff pattern. If no notice about this issue has been posted on the [Twitter API Status Page](https://api.twitterstat.us/) contact support. |

  

**Example Response**

    HTTP/1.1 200 OK
    {
        "rules": [{
            "value": "from:furiouscamper",
            "tag": null,
            "id": 734938587381145604
        }, {
            "value": "fish 🐟",
            "tag": null,
            "id": 734938587381174273
        }],
        "sent": "2016-06-01T15:52:37.341Z"
    }

  

        {
        "error": {
            "message": "Invalid JSON. The body must be in the format {\"rules\":[{\"value\":\"rule1\", \"tag\":\"tag1\"}, {\"value\":\"rule2\"}]} or {\"rule_ids\": [rule_id1, rule_id2, rule_id3, rule_id4, rule_id5]}",
            "sent": "2013-08-16T00:50:00+00:00"
        }
    }

  

POST /rules \_method=delete [¶](#post-rules--method-delete- "Permalink to this headline")
-----------------------------------------------------------------------------------------

Deletes requested existing rules by list of rule values or rule IDs currently on a stream.

#### Request Specifications

|     |     |
| --- | --- |
| **Request Method** | HTTP POST |
| **Authentication** | Basic Authentication. Your login credentials must be included in the header of the request. |
| **Content Type** | "application/json". The request should specify this as the "Content-type". |
| **URL** | Found on the API Help page, and uses the following structure:  <br>  <br>`https://data-api.twitter.com/rules/powertrack/accounts/{gnip_account_name}/publishers/twitter/{stream_label}.json?_method=delete` |
| **Character Encoding** | UTF-8 |
| **Request Body Format** | JSON |
| **Request Body Size Limit** | 5 MB |
| **Rate Limit** | 60 requests per minute, aggregated across all requests to /rules endpoint for the specific stream's API (POST and GET). |

  

#### Request Body Content

Your request should provide rule data in the following formats:

    Content-type: "application/json"
    {
        "rules":
        [
            {"value":"rule1"},
            {"value":"rule2"}
        ]
    }

    Content-type: "application/json"
    {
        "rule_ids":
        [
            734938587381145604,
            734938587381174273
        ]
    }

**Example curl Request**

The following example request demonstrates how to add rules using cURL on the command line.

    curl -v -X POST -uexample@customer.com \
    "https://data-api.twitter.com/rules/powertrack/accounts/:account_name/publishers/twitter/:stream_label.json?_method=delete" \
    -d '{"rules":[{"value":"testrule"}]}"

    curl -v -X POST -uexample@customer.com \
    "https://data-api.twitter.com/rules/powertrack/accounts/:account_name/publishers/twitter/:stream_label.json?_method=delete" \
    -d '{"rule_ids":[734938587381145604,734938587381174273]}"

  

#### Responses

The following responses may be returned by the API for these requests. Non-200 responses should be retried following any necessary modifications to the rules being deleted.

| Status | Text | Description |
| --- | --- | --- |
| 200 | OK  | Indicates that the rule data supplied with the request consisted of valid JSON. However, note that if no rules are found in the ruleset for the PowerTrack stream based on a case-sensitive search, no rules will be deleted. |
| 400 | Bad Request | Generally relates to poorly formatted JSON, and includes an "Invalid JSON" message in the response. |
| 401 | Unauthorized | HTTP authentication failed due to invalid credentials. Log in to console.gnip.com with your credentials to ensure you are using them correctly with your request. |
| 429 | Rate Limited | Your app has exceeded the limit on requests to add, delete, or list rules for this stream. |
| 503 | Service Unavailable | Twitter server issue. Reconnect using an exponential backoff pattern. If no notice about this issue has been posted on the [Twitter API Status Page](https://api.twitterstat.us/), contact support. |

  

**Example Responses**

    HTTP/1.1 200 OK
    {
        "summary": {
            "deleted": 3,
            "not_deleted": 0
        },
        "detail": [],
        "sent": "2016-06-01T15:46:48.654Z"
    }

  

    HTTP/1.1 200 OK
    {
        "summary": {
            "deleted": 0,
            "not_deleted": 3
        },
        "detail": [{
            "rule": {
                "value": "Pizza",
                "tag": null
            },
            "deleted": false,
            "message": "Rule does not exist"
        }, {
            "rule": {
                "value": "eggplant",
                "tag": null
            },
            "deleted": false,
            "message": "Rule does not exist"
        }, {
            "rule": {
                "value": "fish",
                "tag": null
            },
            "deleted": false,
            "message": "Rule does not exist"
        }],
        "sent": "2016-06-01T15:49:15.951Z"
    }

  

    HTTP/1.1 400 Bad Request
    {
        "error": {
            "message": "Invalid JSON. The body must be in the format {\"rules\":[{\"value\":\"rule1\", \"tag\":\"tag1\"}, {\"value\":\"rule2\"}]} or {\"rule_ids\": [rule_id1, rule_id2, rule_id3, rule_id4, rule_id5]}",
            "sent": "2013-08-16T00:50:00+00:00"
        }
    }

**Important note on rule management:** Rule sets are indexed by the value or ruleID, not the tag; therefore, all rule additions must reference the rule value or ruleID. In order to to make a tag update to an existing rule, you must first delete it and then add it back with the new tag value.

Rules must be unique per stream based on rule value, see below for a rule management example scenario:

**CREATE RULE**

Action: POST rule {"value":"#TwitterData","tag":"tagtextA"} {"summary":{"created":1,"not\_created":0},"detail":\[{"rule":{"value":"#TwitterData","tag":"tagtextA","id":961664522481119232,"id\_str":"961664522481119232"},"created":true}\],"sent":"2018-02-08T18:14:23.691Z"} System: {"value":"#TwitterData","tag":"tagtextA","id":961664522481119232,"id\_str":"961664522481119232"}

**FAILED ATTEMPT TO UPDATE TAG**

Action: POST rule {"value":"#TwitterData","tag":"tagtextB"} \*\*Rule tags cannot be "updated" - This request is ignored because rule value `#TwitterData` already exists. {"summary":{"created":0,"not\_created":1},"detail":\[{"rule":{"value":"#TwitterData","tag":"tagtextB","id":961664522481119232,"id\_str":"961664522481119232"},"created":false,"message":"A rule with this value already exists"} System: {"value":"#TwitterData","tag":"tagtextA","id":961664522481119232,"id\_str":"961664522481119232"}

**FAILED ATTEMPT TO DELETE BY TAG**

Action: POST method=delete rule {"tag":"tagtextA"} \*\*Rules cannot be deleted by tag. {"summary":{"deleted":0,"not\_deleted":1},"detail":\[{"rule":{"value":"","tag":null},"deleted":false,"message":"Rule does not exist"}\],"sent":"2018-02-08T18:42:37.004Z"} System: {"value":"#TwitterData","tag":"tagtextA","id":961664522481119232,"id\_str":"961664522481119232"}

**DELETE BY ID**

Action: POST method=delete rule {"rule\_ids":\[961664522481119232\]} {"summary":{"deleted":1,"not\_deleted":0},"detail":\[\],"sent":"2018-02-08T18:53:54.185Z"}

**DELETE BY VALUE**

Action: POST method=delete rule {"value":"#TwitterData"} {"summary":{"deleted":1,"not\_deleted":0},"detail":\[\],"sent":"2018-02-08T18:53:54.185Z"}

**RECREATE RULE- NOW WITH NEW ID**

Action: POST rule {"value":"#TwitterData","tag":"tagtextB"} {"summary":{"created":1,"not\_created":0},"detail":\[{"rule":{"value":"#TwitterData","tag":"tagtextB","id":961675641140609025,"id\_str":"961675641140609025"},"created":true}\],"sent":"2018-02-08T18:58:34.586Z"} System: {"value":"#TwitterData","tag":"tagtextB","id":961675641140609025,"id\_str":"961675641140609025"}

POST /validation [¶](#post-validation- "Permalink to this headline")
--------------------------------------------------------------------

Validates PowerTrack rules.

**Note:** Using this endpoint will not impact your PowerTrack streams.

#### Request Specifications

|     |     |
| --- | --- |
| **Request Method** | HTTP POST |
| **URL** | Found on the API Help page in console, and uses the following structure:  <br>  <br>`https://data-api.twitter.com/rules/powertrack/accounts/:account_name/publishers/twitter/:stream_label/validation.json` |
| **Character Encoding** | UTF-8 |
| **Request Body Format** | JSON |
| **Request Body Size Limit** | 5 MB |
| **Rate Limit** | 60 requests per minute, aggregated across all requests to /rules endpoint for the specific stream's API (POST and GET). |

  

**Example curl Request**

The following example request demonstrates how to add rules using cURL on the command line.

    curl --compressed -v -uexample@customer.com \
    "https://data-api.twitter.com/rules/powertrack/accounts/:account_name/publishers/twitter/:stream_label/validation.json" \
    -d '{
        "rules": [{
            "value": "Pizza OR 🍕 OR \"🍕\" sample:100"
        }, {
            "value": "from:contains:heart"
        }, {
            "value": "fish AND bird"
        }, {
            "value": "(((\"#quotedhashtag\""
        }, {
            "value": "bounding_box:[-71.199636,42.230046,-70.979909,42.398619]"
        }, {
            "value": "from:jack"
        }]
    }'

#### Response

The following responses may be returned by the API for these requests. Non-200 responses should be retried, utilizing an exponential backoff for subsequent requests.

| Status | Text | Description |
| --- | --- | --- |
| 200 | OK  | The request was successful, and the rule validation result is returned. |
| 400 | Bad Request | Generally relates to poorly formatted JSON, and includes an "Invalid JSON" message in the response. |
| 401 | Unauthorized | HTTP authentication failed due to invalid credentials. Log in to console.gnip.com with your credentials to ensure you are using them correctly with your request. |
| 429 | Rate Limited | Your app has exceeded the limit on requests to add, delete, or list rules for this stream. |
| 503 | Service Unavailable | Twitter server issue. Reconnect using an exponential backoff pattern. If no notice about this issue has been posted on the [Twitter API Status Page](https://api.twitterstat.us/), contact support. |

  

**Example Response**

This response indicates that one rule is valid and five are not valid. For rules that are not valid, there is a 'message' field explaining why the rule is not valid.

    HTTP/1.1 200 OK
    {
        "summary": {
            "valid": 1,
            "not_valid": 5
        },
        "detail": [{
            "rule": {
                "value": "from:jack",
                "tag": null
            },
            "valid": true
        }, {
            "rule": {
                "value": "Pizza OR 🍕 OR \"🍕\" sample:100",
                "tag": null
            },
            "valid": false,
            "message": "The sample operator cannot be used with an OR. To use the sample operator with an OR in the rule, the ORed clauses must be grouped together with parenthesis.  For example, to get 10% of activites that have term1 or term2, the rule should be (excluding the single quotes) '(term1 OR term2) sample:10' (at position 21)\n"
        }, {
            "rule": {
                "value": "from:contains:heart",
                "tag": null
            },
            "valid": false,
            "message": "Cannot parse rule at ':' (position 14)\n"
        }, {
            "rule": {
                "value": "fish AND bird",
                "tag": null
            },
            "valid": false,
            "message": "Ambiguous use of and as a keyword. Use a space to logically join two clauses, or \"and\" to find occurrences of and in text (at position 6)\n"
        }, {
            "rule": {
                "value": "(((\"#quotedhashtag\"",
                "tag": null
            },
            "valid": false,
            "message": "mismatched input 'EOF' expecting ')' (at position 20)\n\n"
        }, {
            "rule": {
                "value": "bounding_box:[-71.199636,42.230046,-70.979909,42.398619]",
                "tag": null
            },
            "valid": false,
            "message": "Cannot parse rule at '71.199636,42.230046,-70.979909,42.398619' (position 16)\n"
        }],
        "sent": "2017-03-16T02:33:01.827Z"
    }

Replay API

replay-stream

Replay API
==========

Jump to on this page

[Methods](#Methods)

[Authentication](#Authentication)

[GET /replay](#Stream)

Methods [¶](#methods- "Permalink to this headline")
---------------------------------------------------

| Method | Description |
| --- | --- |
| [GET /replay/:stream\_type](#Stream) | Connect to the replay stream. For realtime PowerTrack, the Stream Type is 'powertrack'. For Volume Streams, Stream Types include 'sample10' (i.e. decahose), 'firehose', 'mentions', and 'compliance'. |

* * *

Authentication [¶](#authentication- "Permalink to this headline")
-----------------------------------------------------------------

All requests to the Replay API must use HTTP Basic Authentication, constructed from a valid email address and password combination used to log into your account at console.gnip.com. Credentials must be passed as the Authorization header for each request.

* * *

GET /replay [¶](#get-replay- "Permalink to this headline")
----------------------------------------------------------

Establishes a connection to the Replay data stream. Tweet data will be delivered for the time period specified, and user profile objects will reflect the referenced users at the time when the Replay API is running.

**Please see [HERE](https://developer.twitter.com/en/docs/tutorials/consuming-streaming-data) for details on consuming streaming data after the connection is established.**

|     |     |
| --- | --- |
| **Request Method** | HTTP GET |
| **Connection Type** | Keep-Alive  <br>  <br>This should be specified in the header of the request. |
| **URL** | Found on the stream's API Help page of your dashboard, the URL is built with Stream Type, Account Name and Stream Label tokens. For realtime PowerTrack, the Stream Type is 'powertrack'. For Volume Streams, Stream Types include 'sample10' (i.e. decahose), 'firehose', 'mentions', and 'compliance'.  <br>  <br>Replay URLs have the following pattern:  <br>  <br><br>[https://gnip-stream.gnip.com/replay/](https://gnip-stream.gnip.com/replay/){STREAM\_TYPE}/accounts/{ACCOUNT\_NAME}/publishers/twitter/{STREAM\_LABEL}.json<br><br>  <br>For example, the Replay URL for realtime PowerTrack has the following pattern:  <br>  <br><br>[https://gnip-stream.gnip.com/replay/powertrack/accounts/](https://gnip-stream.gnip.com/replay/powertrack/accounts/){ACCOUNT\_NAME}/publishers/twitter/{STREAM\_LABEL}.json<br><br>  <br>For example, the Replay URL for Decahose has the following pattern:  <br>  <br><br>[https://gnip-stream.gnip.com/replay/sample10/accounts/](https://gnip-stream.gnip.com/replay/sample10/accounts/){ACCOUNT\_NAME}/publishers/twitter/{STREAM\_LABEL}.json |
| **Compression** | Gzip. To connect to the stream using Gzip compression, simply send an Accept-Encoding header in the connection request. The header should look like the following:  <br>  <br>Accept-Encoding: gzip |
| **Character Encoding** | UTF-8 |
| **Response Format** | JSON. The header of your request should specify JSON format for the response. |
| **Rate Limit** | 5 requests per 5 minutes. |
| **fromDate** | The oldest (starting) UTC timestamp from which the activities will be provided, must be in 'YYYYMMDDHHMM' format. Timestamp is in minute granularity and is inclusive (i.e. 12:00 includes the 00 minute). Valid times must be within the last 5 days, UTC time, and no more recent than 31 minutes before the current point in time. It's recommended that the fromDate and toDate should be within ~2 hours. |
| **toDate** | The latest (ending) UTC timestamp to which the activities will be provided, must be in 'YYYYMMDDHHMM' format. Timestamp is in minute granularity and is exclusive (i.e. 12:30 does not include the 30th minute of the hour). Valid times must be within the last 5 days, UTC time, and no more recent than 30 minutes before the current point in time. It's recommended that the fromDate and toDate should be within ~2 hours. |
| **Read Timeout** | Set a read timeout on your client, and ensure that it is set to a value beyond 30 seconds. |
| **Support for Tweet edits** | Since all Replay requests are for Tweets posted at least 30 minutes ago, all Tweets returned by Replay will reflect their final edit state. All Tweet objects will include metadata that describes its edit history. See the ["Edit Tweets" fundamentals](https://developer.twitter.com/en/docs/twitter-api/enterprise/edit-tweets) page for more details. |

  

#### Responses

The following responses may be returned by the API for these requests. Most error codes are returned with a string with additional details in the body. For non-200 responses, clients should attempt to reconnect.

| Status | Text | Description |
| --- | --- | --- |
| 200 | Success | The connection was successfully opened, and new activities will be sent through until the end of the requested time period is reached, and a "Replay Request Completed" message is sent. |
| 401 | Unauthorized | HTTP authentication failed due to invalid credentials. Log in to console.gnip.com with your credentials to ensure you are using them correctly with your request. |
| 406 | Not Acceptable | Generally, this occurs where your client either fails to properly include the headers to accept gzip encoding from the stream, or specifies an unacceptable fromDate or toDate.  <br>  <br>Will contain a JSON message indicating the issue -- e.g. "This connection requires compression. To enable compression, send an 'Accept-Encoding: gzip' header in your request and be ready to uncompress the stream as it is read on the client end." or "Invalid date for query parameter 'toDate'. Can't ask for tweets from within the past 30 minutes." |
| 429 | Rate Limited | Your app has exceeded the limit on connection requests. |
| 503 | Service Unavailable | Twitter server issue. Reconnect using an exponential backoff pattern. If no notice about this issue has been posted on the [Twitter API Status Page](https://api.twitterstat.us/), contact support. |

  

#### "Request Completed" Message

Once a request has been completed, a "Replay Request Completed" message will be delivered through the stream prior to disconnecting inside a "info" JSON message. If your stream is disconnected prior to receiving this message, the request was not completed, and you will need to re-run the missing portion of the request.

A premature disconnection may occur especially where your client is not consuming activities quickly enough. In this scenario, the connection may send the "Completed" message, but the connection may close prior to your client receiving it due to the slow rate of consumption. In this scenario, your client should re-request the end-portion of the data to ensure completeness, based on the timestamps of the last Tweets received.

The "info" JSON message has the following structure:

{
  "info": {
    "message": "Replay Request Completed",
    "sent": "2016-05-27T22:15:50+00:00",
    "activity\_count": 8874
  }
}

If any errors are associated with a completed Replay request, the "info" message will indicate that errors occurred and also list the minutes that were effected in the "minutes\_failed" field. Here is an example:

{
  "info": {
    "message": "Replay Request Completed with Errors",
    "sent": "2016-05-27T16:00:02+00:00",
    "activity\_count": 56333,
    "minutes\_failed": \[
      "2013-02-20T00:05:00+00:00",
      "2013-02-20T00:06:00+00:00"
    \]
  }
}

Users (or their client applications) should monitor for complete success of the Replay stream, and submit new Replay requests for any minutes that failed.

#### "Request Failed to Complete" Message

If a Replay request fails to complete, the "info" message will indicate the failure and also list the time range was was not processed. Here is an example:

{
  "info": {
    "message": "Replay Request Failed to Complete",
    "sent": "2016-06-27T16:37:13+00:00",
    "unprocessed\_range": {
      "fromDate": "2016-06-26T00:00:00+00:00",
      "toDate": "2016-06-26T00:01:00+00:00"
    },
    "activity\_count": 1822
  }
}

If this message is received another Replay request should be made based on the "fromDate" and "toDate" included in the "unprocessed\_range" attribute.

#### Example curl Request

The following example request is accomplished using cURL on the command line, and requests the first hour of data from June 1, 2016.

curl --compressed -v -uexample@customer.com "https://gnip-stream.gnip.com/replay/powertrack/accounts/{ACCOUNT\_NAME}/publishers/twitter/{STREAM\_LABEL}json?fromDate=201606010000&toDate=201606010100"

  

* * *

### Sample streams Replay Examples (Stream Types include 'sample10' (i.e. decahose), 'firehose', 'mentions')[¶](#sample-streams-replay-examples-stream-types-include-sample10-i-e-decahose-firehose-mentions- "Permalink to this headline")

Decahose, firehose, mentions note- All partitions from volume streams are delievered in a single Replay connection.

    curl --compressed -v -uexample@customer.com 
"https://gnip-stream.gnip.com/replay/sample10/accounts/{ACCOUNT\_NAME}/publishers/twitter/{STREAM\_LABEL}.json?fromDate=201712312330&toDate=201801010130"

### Compliance Replay Examples[¶](#compliance-replay-examples "Permalink to this headline")

Compliance note- All partitions from Compliance Firehose are delievered in a single Replay connection.

curl --compressed -v -uexample@customer.com 
"https://gnip-stream.gnip.com/replay/compliance/accounts/{ACCOUNT\_NAME}/publishers/twitter/{STREAM\_LABEL}.json?fromDate=201712312330&toDate=201801010130"

### PowerTrack Replay Examples[¶](#powertrack-replay-examples "Permalink to this headline")

Connection to Replay to complete data during the 2018 New Year's eve disconnection:

    curl --compressed -v -uexample@customer.com 
"https://gnip-stream.gnip.com/replay/powertrack/accounts/{ACCOUNT\_NAME}/publishers/twitter/{STREAM\_LABEL}.json?fromDate=201712312330&toDate=201801010130"

Important Note: When using PowerTrack Replay, you must first add or manage the rules currently on the replay stream. PowerTrack rules are not automatically added to a Replay stream from a normal PowerTrack stream. Rules can be managed through the Rules API for a Replay stream. Please see the [PowerTrack Rules API](https://developer.twitter.com/en/docs/tweets/filter-realtime/api-reference/powertrack-rules) for specific details on managing rules.

Rules management on the PowerTrack replay:

curl -v -X POST -uexample@customer.com 
"https://gnip-api.twitter.com/rules/powertrack-replay/accounts/{ACCOUNT\_NAME}/publishers/twitter/{STREAM\_LABEL}.json" 
-d '{"rules":\[{"value":"rule1","tag":"tag1"},{"value":"rule2"}\]}'