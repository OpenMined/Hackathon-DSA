



Filtered stream - How to build a rule | Docs | Twitter Developer Platform 





































































































How to build a rule








**Please note:**


If you are moving an app between any Projects, any rules you have created on the filtered stream endpoint will be reset. You will need to recreate these rules once it is associated with its new Project. Prior to moving an app that has rules in place on the filtered stream endpoint, you should save a local copy of all rules using the GET /2/tweets/search/stream/rules endpoint.


 









Building rules for filtered stream
----------------------------------


The filtered stream endpoints deliver filtered Tweets to you in real-time that match on a set of rules that are applied to the stream. Rules are made up of operators that are used to match on a variety of Tweet attributes.


Multiple rules can be applied to a stream using the POST /tweets/search/stream/rules endpoint. Once you’ve added rules and connect to your stream using the GET /tweets/search/stream endpoint, only those Tweets that match your rules will be delivered in real-time through a persistent streaming connection. You do not need to disconnect from your stream to add or remove rules. 


To learn more about how to create high-quality rules, visit the following tutorial:  

Building high-quality filters for getting Twitter data  

 


### Table of contents


* Building a rule
	+ Rule limitations
	+ Operator availability
	+ Operator types: standalone and conjunction-required
	+ Boolean operators and grouping
	+ Order of operations
	+ Punctuation, diacritics, and case sensitivity
	+ Specificity and efficiency
	+ Iteratively building a rule
	+ Adding and removing rules
	+ Rule examples
* List of operators


### Building a rule


#### Rule limitations


Limits on the number of rules will depend on which access level is applied to your Project.


You can see how these limits apply via the filtered stream introduction page.  

 


#### Operator availability


While most operators are available to any developer, there are several that are reserved for those that have been approved for Basic, Pro, or Enterprise access levels. We list which access level each operator is available to in the list of operators table using the following labels:


* **Essential operators:** Available when using any access level.
* **Elevated operators:** Available when using a Project with Pro, or Enterprise access.


#### Operator types: standalone and conjunction-required


**Standalone operators** can be used alone or together with any other operators (including those that require conjunction).


For example, the following rule will work because it uses the #hashtag operator, which is standalone:


#twitterapiv2


**Conjunction required** operators cannot be used by themselves in a rule; they can only be used when at least one standalone operator is included in the rule. This is because using these operators alone would be far too general, and would match on an extremely high volume of Tweets.  




For example, the following rules are not supported since they contain only conjunction required operators:


has:media  

has:links OR is:retweet


If we add in a standalone operator, such as the phrase "twitter data", the rule would then work properly. 


"twitter data" has:mentions (has:media OR has:links)


#### 
Boolean operators and grouping


If you would like to string together multiple operators in a single rule, you have the following tools at your disposal:




|  |  |
| --- | --- |
| **AND logic** | Successive operators **with a space between them** will result in boolean "AND" logic, meaning that Tweets will match only if both conditions are met. For example, snow day #NoSchool will match Tweets containing the terms snow and day and the hashtag #NoSchool. |
| **OR logic** | Successive operators with OR between them will result in OR logic, meaning that Tweets will match if either condition is met. For example, specifying grumpy OR cat OR #meme will match any Tweets containing at least the terms grumpy or cat, or the hashtag #meme. |
| **NOT logic, negation** | Prepend a dash (-) to a keyword (or any operator) to negate it (NOT). For example, cat #meme -grumpy will match Tweets containing the hashtag #meme and the term cat, but only if they do not contain the term grumpy. One common rule clause is -is:retweet, which will not match on Retweets, thus matching only on original Tweets, Quote Tweets, and replies. All operators can be negated, but negated operators cannot be used alone. |
| **Grouping** | You can use parentheses to group operators together. For example, (grumpy cat) OR (#meme has:images) will return either Tweets containing the terms grumpy and cat, or Tweets with images containing the hashtag #meme. Note that ANDs are applied first, then ORs are applied. |











**A note on negations**


All operators can be negated except for sample:, and -is:nullcast must always be negated. Negated operators cannot be used alone.


Do not negate a set of operators grouped together in a set of parentheses. Instead, negate each individual operator.


For example, instead of using skiing -(snow OR day OR noschool), we suggest that you use skiing -snow -day -noschool. 









#### 
Order of operations


When combining AND and OR functionality, the following order of operations will dictate how your rule is evaluated.


1. Operators connected by AND logic are combined first
2. Then, operators connected with OR logic are applied


For example:


* apple OR iphone ipad would be evaluated as apple OR (iphone ipad)
* ipad iphone OR android would be evaluated as (iphone ipad) OR android


To eliminate uncertainty and ensure that your rule is evaluated as intended, group terms together with parentheses where appropriate. 


For example:


* (apple OR iphone) ipad
* iphone (ipad OR android)


#### Punctuation, diacritics, and case sensitivity


If you specify a keyword or hashtag rule with character accents or diacritics, it will match Tweets that contain the exact word with proper accents or diacritics, but not those that have the proper letters, but without the accent or diacritic. 


For example, rules with the keyword diacrítica or hashtag #cumpleaños will match Tweets that contain *diacrítica* or *#cumpleaños* because they include the accent or diacritic. However, these rules will not match Tweets that contain *Diacritica* or *#cumpleanos* without the tilde í or eñe.  

  




Characters with accents or diacritics are treated the same as normal characters and are not treated as word boundaries. For example, a rule with the keyword *cumpleaños* would only match Tweets containing the word *cumpleaños* and would not match Tweets containing *cumplea*, *cumplean*, or *os*.


All operators are evaluated in a case-insensitive manner. For example, the rule cat will match all of the following: *cat*, *CAT*, *Cat*.











The Search Tweets matching behavior acts differently from filtered stream. When building a Search Tweets query, know that keywords and hashtags that include accents or diacritics will match both the term with the accents and diacritics, as well as with normal characters. 


For example, Search Tweets queries that include a keyword Diacrítica or hashtag #cumpleaños will match both *Diacrítica* and *#cumpleaños*, as well as *Diacritica* or *#cumpleanos* without the tilde í or eñe.









#### 


#### Specificity and efficiency


When you start to build your rule, it is important to keep a few things in mind.


* Using broad, standalone operators for your rule such as a single keyword or #hashtag is generally not recommended since it will likely match on a massive volume of Tweets. Creating a more robust rule will result in a more specific set of matching Tweets, and will hopefully reduce the amount of noise in the payload that you will need to sift through to find valuable insights.
	+ For example, if your rule was just the keyword happy you will likely get anywhere from 200,000 - 300,000 Tweets per day.
	+ Adding more conditional operators narrows your search results, for example (happy OR happiness) place\_country:GB -birthday -is:retweet
* Writing efficient rules is also beneficial for staying within the characters rule length restriction. The character count includes the entire rule string including spaces and operators.
	+ For example, the following rule is 59 characters long: (happy OR happiness) place\_country:GB -birthday -is:retweet


#### 
Quote Tweet matching behavior


When using the filtered stream endpoints, operators will match on both the content from the original Tweet that was quoted, as well as the content included in the Quote Tweet.


However, please note that the Search Tweets endpoints will not match on the content from the original Tweet that was quoted, but will match on the Quote Tweet's content.  

  




#### Iteratively building a rule


##### Test your rule early and often


Getting a rule to return the "right" results the first time is rare. There is so much on Twitter that may or may not be obvious at first and the rule syntax described above may be hard to match to your desired search. As you build a rule, it is important for you to periodically test it out with the stream endpoint to see what data it returns. You can also test with one of the Search Tweet endpoints, assuming the operators that you are using are also available via that endpoint. 


For this section, we are going to start with the following rule and adjust it based on the results that we receive during our test: 


happy OR happiness


##### Use results to narrow the rule


As you test the rule, you should scan the returned Tweets to see if they include the data that you are expecting and hoping to receive. Starting with a broad rule and a superset of Tweet matches allows you to review the result and narrow the rule to filter out undesired results.  


When we tested the example rule, we noticed that we were getting Tweets in a variety of different languages. In this situation, we want to only receive Tweets that are in english, so we’re going to add the lang: operator:


(happy OR happiness) lang:en


The test delivered a number of Tweets wishing people a happy birthday, so we are going to add -birthday as a negated keyword operator. We also want to only receive original Tweets, so we’ve added the negated -is:retweet operator:


(happy OR happiness) lang:en -birthday -is:retweet


##### Adjust for inclusion where needed


If you notice that you are not receiving data that you expect and know that there are existing Tweets that should return, you may need to broaden your rule by removing operators that may be filtering out the desired data. 


For our example, we noticed that there were other Tweets in our personal timeline that expressed the emotion that we are looking for and weren’t included in the test results. To ensure we have greater coverage, we are going to add the keywords, excited and elated.


(happy OR happiness OR excited OR elated) lang:en -birthday -is:retweet


##### Adjust for popular trends/bursts over the time period


Trends come and go on Twitter quickly. Maintaining your rule should be an active process. If you plan to use a single rule for a while, we suggest that you periodically check in on the data that you are receiving to see if you need to make any adjustments.


In our example, we notice that we started to receive some Tweets that are wishing people a “happy holidays”. Since we don’t want these Tweets included in our results, we are going to add a negated -holidays keyword.


(happy OR happiness OR excited OR elated) lang:en -birthday -is:retweet -holidays 


 


#### Adding and removing rules


You will be using the POST /2/tweets/search/stream/rules endpoint when both adding and deleting rules from your stream.


To add one or more rule to your stream, submit an add JSON body with an array that contains the value parameter including the rule, and the optional tag parameter including free-form text that you can use to identify which returned Tweets match this rule. 


For example, if you were trying to add a set of rules to your stream, your cURL command might look like this:












```

      curl -X POST 'https://api.twitter.com/2/tweets/search/stream/rules' \
-H "Content-type: application/json" \
-H "Authorization: Bearer $ACCESS_TOKEN" -d \
'{
  "add": [
    {"value": "cat has:media", "tag": "cats with media"},
    {"value": "cat has:media -grumpy", "tag": "happy cats with media"},
    {"value": "meme", "tag": "funny things"},
    {"value": "meme has:images"}
  ]
}'
    
```





Code copied to clipboard








Similarly, to remove one or more rules from your stream, submit a delete JSON body with the array of that contains the id parameter including the rule IDs that you would like to delete.


For example, if you were trying to remove a set of rules from your stream, your cURL command might look like this:  














```

      curl -X POST 'https://api.twitter.com/2/tweets/search/stream/rules' \
  -H "Content-type: application/json" \
  -H "Authorization: Bearer $ACCESS_TOKEN" -d \
  '{
    "delete": {
      "ids": [
        "1165037377523306498",
        "1165037377523306499"
      ]
    }
  }'
    
```





Code copied to clipboard








We have sample code in different languages available via our Github.   

  




#### Rule examples


##### Tracking a natural disaster


The following rule matched on Tweets coming from weather agencies and gauges that discuss Hurricane Harvey, which hit Houston in 2017. Notice the use of the matching rules tag, and the JSON format that you will need to use when submitting the rule to the POST /2/tweets/search/stream/rules endpoint.












```

              {
            "value": "-is:retweet has:geo (from:NWSNHC OR from:NHC_Atlantic OR from:NWSHouston OR from:NWSSanAntonio OR from:USGS_TexasRain OR from:USGS_TexasFlood OR from:JeffLindner1)",
            "tag": "theme:info has:geo original from weather agencies and gauges"
        }

    
```





Code copied to clipboard








##### Reviewing the sentiment of a conversation


The next rule could be used to better understand the sentiment of the conversation developing around the hashtag, *#nowplaying*, but only from Tweets published within North America.












```

              {
            "value": "#nowplaying (happy OR exciting OR excited OR favorite OR fav OR amazing OR lovely OR incredible) (place_country:US OR place_country:MX OR place_country:CA) -horrible -worst -sucks -bad -disappointing",
            "tag": "#nowplaying positive"
        },
        {
            "value": "#nowplaying (horrible OR worst OR sucks OR bad OR disappointing) (place_country:US OR place_country:MX OR place_country:CA) -happy -exciting -excited -favorite -fav -amazing -lovely -incredible",
            "tag": "#nowplaying negative"
        }

    
```





Code copied to clipboard








##### Find Tweets that relate to a specific Tweet annotation


This rule was built to search for original Tweets that included an image of a pet that is not a cat, where the language identified in the Tweet is Japanese. To do this, we used the context: operator to take advantage of the Tweet annotation functionality. We first used the Tweet lookup endpoint and the tweet.fields=context\_annotations fields parameter to identify which domain.entity IDs we need to use in our query:


* Tweets that relate to cats return **domain** 66 (Interests and Hobbies category) with entity 852262932607926273 (Cats).
* Tweets that relate to pets return **domain** 65 (Interests and Hobbies Vertical) with entity 852262932607926273 (Pets).


Here is what the rule would look like:












```

              {
            "value": "context:65.852262932607926273 -context:66.852262932607926273 -is:retweet has:images lang:ja",
            "tag": "Japanese pets with images - no cats"
        }
    
```





Code copied to clipboard








### Operators


* **Essential:**Available when using any access level.
* **Elevated:**Available when using a Project with Pro, or Enterprise access.
* For some operators, an alternate name, or alias, is available.




| **Operator** | Type | Availability | Description |
| keyword | Standalone | Essential
  | Matches a keyword within the body of a Tweet. This is a tokenized match, meaning that your keyword string will be matched against the tokenized text of the Tweet body. Tokenization splits words based on punctuation, symbols, and Unicode basic plane separator characters.

For example, a Tweet with the text “I like coca-cola” would be split into the following tokens: I, like, coca, cola. These tokens would then be compared to the keyword string used in your rule. To match strings containing punctuation (for example coca-cola), symbol, or separator characters, you must wrap your keyword in double-quotes.

Example: pepsi OR cola OR "coca cola" |
| emoji | Standalone | Essential | Matches an emoji within the body of a Tweet. Similar to a keyword, emojis are a tokenized match, meaning that your emoji will be matched against the tokenized text of the Tweet body.

Note that if an emoji has a variant, you must wrap it in double quotes to add to a rule.

Example: (😃 OR 😡) 😬 |
| "exact phrase match" | Standalone | Essential | Matches the exact phrase within the body of a Tweet.

Example: ("Twitter API" OR #v2) -"filtered stream" |
| # | Standalone | Essential | Matches any Tweet containing a recognized hashtag, if the hashtag is a recognized entity in a Tweet.

This operator performs an exact match, NOT a tokenized match, meaning the rule #thanku will match posts with the exact hashtag #thanku, but not those with the hashtag #thankunext.

Example: #thankunext #fanart OR @arianagrande |
| @ | Standalone | Essential | Matches any Tweet that mentions the given username, if the username is a recognized entity (including the @ character).

Example: (@twitterdev OR @twitterapi) -@twitter |
| $ | Standalone | Essential | Matches any Tweet that contains the specified ‘cashtag’ (where the leading character of the token is the ‘$’ character).

Note that the cashtag operator relies on Twitter’s ‘symbols’ entity extraction to match cashtags, rather than trying to extract the cashtag from the body itself.

Example: $twtr OR @twitterdev -$fb |
| from: | Standalone | Essential | Matches any Tweet from a specific user.
The value can be either the username (excluding the @ character) or the user’s numeric user ID.

You can only pass a single username/ID from: operator.

Example: from:twitterdev OR from:twitterapi -from:twitter |
| to: | Standalone | Essential | Matches any Tweet that is in reply to a particular user.
The value can be either the username (excluding the @ character) or the user’s numeric user ID.

You can only pass a single username/ID per to: operator.

Example: to:twitterdev OR to:twitterapi -to:twitter |
| url: | Standalone | Essential | Performs a tokenized match on any validly-formatted URL of a Tweet.

This operator can matches on the contents of both the url or expanded\_url fields. For example, a Tweet containing "You should check out Twitter Developer Labs: https://t.co/c0A36SWil4" (with the short URL redirecting to https://developer.twitter.com) will match both the following rules:

from:TwitterDev url:"https://developer.twitter.com"
(because it will match the contents of entities.urls.expanded\_url)

from:TwitterDev url:"https://t.co"
(because it will match the contents of entities.urls.url)

Tokens and phrases containing punctuation or special characters should be double-quoted (for example, url:"/developer"). Similarly, to match on a specific protocol, enclose in double-quotes (for example, url:"https://developer.twitter.com").

You can only pass a single URL per url: operator. |
| retweets\_of: | Standalone | Essential | *Available alias:* retweets\_of\_user:
Matches Tweets that are Retweets of the specified user. The value can be either the username (excluding the @ character) or the user’s numeric user ID.

You can only pass a single username/ID per retweets\_of: operator.

Example: retweets\_of:twitterdev OR retweets\_of:twitterapi
See HERE for methods for looking up numeric Twitter Account IDs. |
| context: | Standalone | Essential | Matches Tweets with a specific domain id and/or domain id, enitity id pair where \* represents a wildcard. To learn more about this operator, please visit our page on Tweet annotations.

You can only pass a single domain/entitie per context: operator.

context:domain\_id.entity\_id
 context:domain\_id.\*
 context:\*.entity\_id

Examples:
context:10.799022225751871488
(domain\_id.entity\_id returns Tweets matching that specific domain-entity pair)

context:47.\*
(domain\_id.\* returns Tweets matching that domain ID, with any domain-entity pair)

context:\*.799022225751871488
(\*.entity\_id returns Tweets matching that entity ID, with any domain-entity pair) |
| entity: | Standalone | Essential | Matches Tweets with a specific entity string value. To learn more about this operator, please visit our page on annotations.

You can only pass a single entity per entity: operator.

entity:"string declaration of entity/place"

Examples: entity:"Michael Jordan" OR entity:"Barcelona" |
| conversation\_id: | Standalone | Essential | Matches Tweets that share a common conversation ID. A conversation ID is set to the Tweet ID of a Tweet that started a conversation. As Replies to a Tweet are posted, even Replies to Replies, the conversation\_id is added to its JSON payload.

You can only pass a single conversation ID per conversation\_id: operator.

Example: conversation\_id:1334987486343299072 (from:twitterdev OR from:twitterapi) |
| bio:
 
  | Standalone | Essential | *Available alias:*user\_bio:
Matches a keyword or phrase within the Tweet publisher's bio. This is a tokenized match within the contents of the description field within the User object.

Example: bio:developer OR bio:"data engineer" OR bio:academic |
| bio\_name: | Standalone | Essential | Matches a keyword within the Tweet publisher's user bio name. This is a tokenized match within the contents of a user’s “name” field within the User object.

Example: bio\_name:phd OR bio\_name:md |
| bio\_location:
 
  | Standalone | Essential | *Available alias:*user\_bio\_location:
Matches Tweets that are published by users whose location contains the specified keyword or phrase. This operator performs a tokenized match, similar to the normal keyword rules on the message body.

This location is part of the User object, matches on the 'location' field, and is a non-normalized, user-generated, free-form string. It is also different from a Tweet's location (see place:).

Example: bio\_location:"big apple" OR bio\_location:nyc OR bio\_location:manhattan |
| place: | Standalone | Elevated | Matches Tweets tagged with the specified location or Twitter place ID. Multi-word place names (“New York City”, “Palo Alto”) should be enclosed in quotes.

You can only pass a single place per place: operator.

Note: See the GET geo/search standard v1.1 endpoint for how to obtain Twitter place IDs.

Note: This operator will not match on Retweets, since Retweet's places are attached to the original Tweet. It will also not match on places attached to the original Tweet of a Quote Tweet.

Example: place:"new york city" OR place:seattle OR place:fd70c22040963ac7 |
| place\_country: | Standalone | Elevated | Matches Tweets where the country code associated with a tagged place/location matches the given ISO alpha-2 character code.

You can find a list of valid ISO codes on Wikipedia.

You can only pass a single ISO code per place\_country: operator.

Note: This operator will not match on Retweets, since Retweet's places are attached to the original Tweet. It will also not match on places attached to the original Tweet of a Quote Tweet.

Example: place\_country:US OR place\_country:MX OR place\_country:CA |
| point\_radius: | Standalone | Elevated | Matches against the place.geo.coordinates object of the Tweet when present, and in Twitter, against a place geo polygon, where the Place polygon is fully contained within the defined region.

point\_radius:[longitude latitude radius]
* Units of radius supported are miles (mi) and kilometers (km)
* Radius must be less than 25mi
* Longitude is in the range of ±180
* Latitude is in the range of ±90
* All coordinates are in decimal degrees
* Rule arguments are contained within brackets, space delimited


You can only pass a single geo polygon per point\_radius: operator.

Note: This operator will not match on Retweets, since Retweet's places are attached to the original Tweet. It will also not match on places attached to the original Tweet of a Quote Tweet.

Example: point\_radius:[2.355128 48.861118 16km] OR point\_radius:[-41.287336 174.761070 20mi] |
| bounding\_box:
 
  | Standalone | Elevated | *Available alias:*geo\_bounding\_box:
Matches against the place.geo.coordinates object of the Tweet when present, and in Twitter, against a place geo polygon, where the place polygon is fully contained within the defined region.


bounding\_box:[west\_long south\_lat east\_long north\_lat]

* west\_long south\_lat represent the southwest corner of the bounding box where west\_long is the longitude of that point, and south\_lat is the latitude.
* east\_long north\_lat represent the northeast corner of the bounding box, where east\_long is the longitude of that point, and north\_lat is the latitude.
* Width and height of the bounding box must be less than 25mi
* Longitude is in the range of ±180
* Latitude is in the range of ±90
* All coordinates are in decimal degrees.
* Rule arguments are contained within brackets, space delimited.


You can only pass a single geo polygons per bounding\_box: operator.

Note: This operator will not match on Retweets, since Retweet's places are attached to the original Tweet. It will also not match on places attached to the original Tweet of a Quote Tweet.

Example: bounding\_box:[-105.301758 39.964069 -105.178505 40.09455]  |
| is:retweet | Conjunction required | Essential | Matches on Retweets that match the rest of the specified rule. This operator looks only for true Retweets (for example, those generated using the Retweet button). Quote Tweets will not be matched by this operator.

Example: data @twitterdev -is:retweet |
| is:reply | Conjunction required | Essential | Deliver only explicit replies that match a rule. Can also be negated to exclude replies that match a rule from delivery.

When used with the filtered stream, this operator matches on replies to an original Tweet, replies in quoted Tweets and replies in Retweets.

Example: from:twitterdev is:reply |
| is:quote | Conjunction required | Essential | Returns all Quote Tweets, also known as Tweets with comments.

Example: "sentiment analysis" is:quote |
| is:verified | Conjunction required | Essential | Deliver only Tweets whose authors are verified by Twitter.

Example: #nowplaying is:verified |
| -is:nullcast | Conjunction required | Elevated | Removes Tweets created for promotion only on ads.twitter.com that have a "source":"Twitter for Advertisers (legacy)" or "source":"Twitter for Advertisers".
This operator must be negated.

For more info on Nullcasted Tweets, see our page on Tweet availability.

Example: "mobile games" -is:nullcast |
| has:hashtags | Conjunction required | Essential | Matches Tweets that contain at least one hashtag.

Example: from:twitterdev -has:hashtags |
| has:cashtags | Conjunction required | Essential | Matches Tweets that contain a cashtag symbol (with a leading ‘$’ character. For example, $tag).

Example: #stonks has:cashtags |
| has:links | Conjunction required | Essential | This operator matches Tweets which contain links and media in the Tweet body.

Example: from:twitterdev announcement has:links |
| has:mentions | Conjunction required | Essential | Matches Tweets that mention another Twitter user.

Example: #nowplaying has:mentions |
| has:media
 
  | Conjunction required | Essential | *Available alias:*has:media\_link
Matches Tweets that contain a media object, such as a photo, GIF, or video, as determined by Twitter. This will not match on media created with Periscope, or Tweets with links to other media hosting sites.

Example: (kittens OR puppies) has:media |
| has:images | Conjunction required | Essential | Matches Tweets that contain a recognized URL to an image.

Example: #meme has:images |
| has:video\_link
 
  | Conjunction required | Essential | *Available alias:*has:videos
Matches Tweets that contain native Twitter videos, uploaded directly to Twitter. This will not match on videos created with Periscope, or Tweets with links to other video hosting sites.

Example: #icebucketchallenge has:video\_link |
| has:geo | Conjunction required | Essential | Matches Tweets that have Tweet-specific geolocation data provided by the Twitter user. This can be either a location in the form of a Twitter place, with the corresponding display name, geo polygon, and other fields, or in rare cases, a geo lat-long coordinate.

Note: Operators matching on place (Tweet geo) will only include matches from original tweets. Retweets do not contain any place data.

Example: recommend #paris has:geo -bakery |
| sample: | Conjunction required | Essential | Returns a random percent sample of Tweets that match a rule rather than the entire set of Tweets. The percent value must be represented by an integer between 1 and 100 (for example, sample:10 will return a random 10% sample).

This operator first reduces the scope of the stream to the percentage you specified, then the rule/filter is applied to that sampled subset. In other words, if you are using, for example, sample:10, each Tweet will have a 10% chance of being in the sample.

This operator applies to the entire rule and requires all OR'd terms to be grouped.

Example: #nowplaying @spotify sample:15 |
| lang: | Conjunction required | Essential | Matches Tweets that have been classified by Twitter as being of a particular language (if, and only if, the tweet has been classified). It is important to note that each Tweet is currently only classified as being of one language, so AND’ing together multiple languages will yield no results.

You can only pass a single BCP 47 language identifier per lang: operator.

Note: if no language classification can be made the provided result is ‘und’ (for undefined).

Example: recommend #paris lang:en

The list below represents the currently supported languages and their corresponding BCP 47 language identifier:


|  |  |  |  |
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
| Georgian: ka | Lithuanian: lt |  |

 |
| followers\_count: |  | Essential | Matches Tweets when the author has a followers count within the given range.
If a single number is specified, any number equal to or higher will match.
 
Example: followers\_count:500
 
Additionally, a range can be specified to match any number in the given range.
 
Example: followers\_count:1000..10000 |
| tweets\_count:
 
  |  | Essential | *Available alias:*statuses\_count:
Matches Tweets when the author has posted a number of Tweets that falls within the given range.
If a single number is specified, any number equal to or higher will match.
 
Example: tweets\_count:1000
 
Additionally, a range can be specified to match any number in the given range.
 
Example: tweets\_count:1000..10000 |
| following\_count:
 
  |  | Essential | *Available alias:*friends\_count:
Matches Tweets when the author has a friends count (the number of users they follow) that falls within the given range.
If a single number is specified, any number equal to or higher will match.
 
Example: following\_count:500
 
Additionally, a range can be specified to match any number in the given range.
 
Example: following\_count:1000..10000 |
| listed\_count:
 
  |  | Essential | *Available alias:*user\_in\_lists\_count:
Matches Tweets when the author is included in the specified number of Lists. 
If a single number is specified, any number equal to or higher will match.
 
Example: listed\_count:10
 
Additionally, a range can be specified to match any number in the given range.
 
Example: listed\_count:10..100 |
| url\_title:
  |  | Essential | *Available alias:*within\_url\_title:
Performs a keyword/phrase match on the expanded URL HTML title metadata.
 
Example: url\_title:snow
 |
| url\_description:
 
  |  | Essential | *Available alias:*within\_url\_description:
Performs a keyword/phrase match on the expanded page description metadata.
 
Example: url\_description:weather |
| url\_contains: |  | Essential | Matches Tweets with URLs that literally contain the given phrase or keyword. To search for patterns with punctuation in them (i.e. google.com) enclose the search term in quotes.
NOTE: This will match against the expanded URL as well.
 
Example: url\_contains:photos |
| source: |  | Essential | Matches any Tweet generated by the given source application. The value must be either the name of the application or the application’s URL. Cannot be used alone.
 
Example: source:"Twitter for iPhone"
 
Note: As a Twitter app developer, Tweets created programmatically by your application will have the source of your application Name and Website URL set in your app settings. 
  |
| in\_reply\_to\_tweet\_id:
 
  |  | Essential | *Available alias:*in\_reply\_to\_status\_id:
Deliver only explicit Replies to the specified Tweet.
 
Example: in\_reply\_to\_tweet\_id:1539382664746020864 |
| retweets\_of\_tweet\_id:
 
  |  | Essential | *Available alias:*retweets\_of\_status\_id:
Deliver only explicit (or native) Retweets of the specified Tweet. Note that the status ID used should be the ID of an original Tweet and not a Retweet. 
 
Example: retweets\_of\_tweet\_id:1539382664746020864  |



















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















