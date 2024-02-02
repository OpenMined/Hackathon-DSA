
Building queries | Docs | Twitter Developer Platform 

Building queries

Building queries for Tweet counts
---------------------------------

The Tweet counts endpoints accept a single query with a GET request and return a set of historical Tweet counts that match the query.  Queries are made up of operators that are used to match on a variety of Tweet attributes. 

To learn more about how to create high-quality queries, visit the following tutorial:  
Building high-quality filters for getting Twitter data

### Table of contents

* Building a query
* Query limitations
* Operator availability
* Operator types: standalone and conjunction-required
* Boolean operators and grouping
* Order of operations
* Punctuation, diacritics, and case sensitivity
* Specificity and efficiency
* Quote Tweet matching behavior
* Iteratively building a query
* Adding a query to your request
* Query examples
* List of operators

### Building a query

#### Query limitations

Your queries will be limited depending on which access level you are using. 

If you have Pro access, your query can be 512 characters long.

If you have Enterprise access, please reach out to your account manager.   

#### Operator availability

While most operators are available to any developer, there are several that are reserved for those that have been approved for Enterprise access. We list which access level each operator is available to in the list of operators table using the following labels:

* Core operators: Available when using any Project.
* Advanced operators: Available when using a Project with Enterprise access

#### Operator types: standalone and conjunction-required

**Standalone operators** can be used alone or together with any other operators (including those that require conjunction).

For example, the following query will work because it uses the #hashtag operator, which is standalone:

#twitterapiv2

**Conjunction-required** operators cannot be used by themselves in a query; they can only be used when at least one standalone operator is included in the query. This is because using these operators alone would be far too general, and would match on an extremely high volume of Tweets.  

For example, the following queries are not supported since they contain only conjunction-required operators:

has:media  
has:links OR is:retweet

If we add in a standalone operator, such as the phrase "twitter data", the query would then work properly. 

"twitter data" has:mentions (has:media OR has:links)

#### 
Boolean operators and grouping

If you would like to string together multiple operators in a single query, you have the following tools at your disposal:

|  |  |
| --- | --- |
| **AND logic** | Successive operators with a space between them will result in boolean "AND" logic, meaning that Tweets will match only if both conditions are met. For example, snow day #NoSchool will match Tweets containing the terms snow and day and the hashtag #NoSchool. |
| **OR logic** | Successive operators with OR between them will result in OR logic, meaning that Tweets will match if either condition is met. For example, specifying grumpy OR cat OR #meme will match any Tweets containing at least the terms grumpy or cat, or the hashtag #meme. |
| **NOT logic, negation** | Prepend a dash (-) to a keyword (or any operator) to negate it (NOT). For example, cat #meme -grumpy will match Tweets containing the hashtag #meme and the term cat, but only if they do not contain the term grumpy. One common query clause is -is:retweet, which will not match on Retweets, thus matching only on original Tweets, Quote Tweets, and replies. All operators can be negated, but negated operators cannot be used alone.
 |
| **Grouping** | You can use parentheses to group operators together. For example, (grumpy cat) OR (#meme has:images) will return either Tweets containing the terms grumpy and cat, or Tweets with images containing the hashtag #meme. Note that ANDs are applied first, then ORs are applied. |

**A note on negations**

The operators -is:nullcast must always be negated.

Negated operators cannot be used alone.

Do not negate a set of operators grouped together in a set of parentheses. Instead, negate each individual operator. For example, instead of using skiing -(snow OR day OR noschool), we suggest that you use skiing -snow -day -noschool. 

#### 
Order of operations

When combining AND and OR functionality, the following order of operations will dictate how your query is evaluated.

1. Operators connected by AND logic are combined first
2. Then, operators connected with OR logic are applied

For example:

* apple OR iphone ipad would be evaluated as apple OR (iphone ipad)
* ipad iphone OR android would be evaluated as (iphone ipad) OR android

To eliminate uncertainty and ensure that your query is evaluated as intended, group terms together with parentheses where appropriate. 

For example:

* (apple OR iphone) ipad
* iphone (ipad OR android)

#### Punctuation, diacritics, and case sensitivity

If you specify a keyword or hashtag query with character accents or diacritics, it will match Tweet text that contains both the term with the accents and diacritics, as well as those terms with normal characters. For example, queries with a keyword Diacrítica or hashtag #cumpleaños will match *Diacrítica* or *#cumpleaños*, as well as with *Diacritica* or *#cumpleanos* without the tilde í or eñe.

Characters with accents or diacritics are treated the same as normal characters and are not treated as word boundaries. For example, a query with the keyword cumpleaños would only match activities containing the word *cumpleaños* and would not match activities containing *cumplea*, *cumplean*, or *os*.

All operators are evaluated in a case-insensitive manner. For example, the query cat will match Tweets with all of the following: *cat*, *CAT*, *Cat*.

The filtered stream matching behavior acts differently from Tweet counts. When building a filtered stream rule, know that keywords and hashtags that include accents and diacritics will only match on terms that also include the accent and diacritic, and will not match on terms that use normal characters instead. 

For example, filtered stream rules that include a keyword Diacrítica or hashtag #cumpleaños will only match the terms *Diacrítica* and *#cumpleaños*, and will not match on *Diacritica* or *#cumpleanos* without the tilde í or eñe

#### 

#### Specificity and efficiency

When you start to build your query, it is important to keep a few things in mind.

* Using broad, standalone operators for your query such as a single keyword or #hashtag is generally not recommended since it will likely match on a massive volume of Tweets. Creating a more robust query will result in a more specific set of matching Tweets, and will hopefully increase the accuracy of your Tweet counts to help you find more valuable insights.
	+ For example, if your query was just the keyword happy you will likely get anywhere from 200,000 - 300,000 Tweets per day.
	+ Adding more conditional operators narrows your results, for example (happy OR happiness) place\_country:GB -birthday -is:retweet
* Writing efficient queries is also beneficial for staying within the characters query length restriction. The character count includes the entire query string including spaces and operators.
	+ For example, the following query is 59 characters long: (happy OR happiness) place\_country:GB -birthday -is:retweet

#### 
Quote Tweet matching behavior

When using the Tweet counts endpoints, operators will not match on the content from the original Tweet that was quoted, but will match on the content included in the Quote Tweet.

However, please note that filtered stream will match on both the content from the original Tweet that was quoted and the Quote Tweet's content.  

#### Iteratively building a query

##### Test your query early and often

Getting a query to return the "right" results the first time is rare. There is so much on Twitter that may or may not be obvious at first and the query syntax described above may be hard to match to your desired query.

As you build a query, it is important for you to periodically test it out using one of the Search Tweet endpoints to ensure that the Tweets that are matching your query are relevant to your use case.

For this section, we are going to start with the following query and adjust it based on the results that we receive during our test: 

happy OR happiness

##### Use results to narrow the query

As you test the query with Search Tweets, you should scan the returned Tweets to see if they include the data that you are expecting and hoping to receive. Starting with a broad query and a superset of Tweet matches allows you to review the result and narrow the query to filter out undesired results.  

When we tested the example query, we noticed that we were getting Tweets in a variety of different languages. In this situation, we want to only receive Tweets that are in english, so we’re going to add the lang: operator:

(happy OR happiness) lang:en

The test delivered a number of Tweets wishing people a happy birthday, so we are going to add -birthday as a negated keyword operator. We also want to only receive original Tweets, so we’ve added the negated -is:retweet operator:

(happy OR happiness) lang:en -birthday -is:retweet

##### Adjust for inclusion where needed

If you notice that you are not receiving data via Search Tweets that you expect and know that there are existing Tweets that should return, you may need to broaden your query by removing operators that may be filtering out the desired data. 

For our example, we noticed that there were other Tweets in our personal timeline that expressed the emotion that we are looking for and weren’t included in the test results. To ensure we have greater coverage, we are going to add the keywords, excited and elated.

(happy OR happiness OR excited OR elated) lang:en -birthday -is:retweet

##### Adjust for popular trends/bursts over the time period

Trends come and go on Twitter quickly. Maintaining your query should be an active process. If you plan to use a query for a while, we suggest that you periodically check in on the data that you are receiving to see if you need to make any adjustments.

In our example, we notice that we started to receive some Tweets that are wishing people a “happy holidays”. Since we don’t want these Tweets included in our results, we are going to add a negated -holidays keyword.

(happy OR happiness OR excited OR elated) lang:en -birthday -is:retweet -holidays 

Once you've properly tested and iterated upon your query, you can start sending it with the Tweet counts endpoints to start to receive just the volume of Tweets rather than the full Tweet payloads.

### Adding a query to your request

To add your query to your request, you must use the query parameter. As with any query parameters, you must make sure to HTTP encode the query that you developed.

Here is an example of what this might look like using a cURL command. If you would like to use this command, please make sure to replace $BEARER\_TOKEN with your own Bearer Token:

```
      curl https://api.twitter.com/2/tweets/counts/recent?query=cat%20has%3Amedia%20-grumpy&tweet.fields=created_at&max_results=100 -H "Authorization: Bearer $BEARER_TOKEN"
```

Code copied to clipboard

### 
Query examples

#### Tracking a natural disaster

The following query matched on original Tweets coming from weather agencies and gauges that discuss Hurricane Harvey, which hit Houston in 2017.

Here is what the query would look like without the HTTP encoding:

has:geo (from:NWSNHC OR from:NHC\_Atlantic OR from:NWSHouston OR from:NWSSanAntonio OR from:USGS\_TexasRain OR from:USGS\_TexasFlood OR from:JeffLindner1) -is:retweet

And here is what the query would look like with the HTTP encoding, the query parameter, and the recent Tweet counts URI:

https://api.twitter.com/2/tweets/counts/recent?query=-is%3Aretweet%20has%3Ageo%20(from%3ANWSNHC%20OR%20from%3ANHC\_Atlantic%20OR%20from%3ANWSHouston%20OR%20from%3ANWSSanAntonio%20OR%20from%3AUSGS\_TexasRain%20OR%20from%3AUSGS\_TexasFlood%20OR%20from%3AJeffLindner1)

#### 
Reviewing the sentiment of a conversation

The next rule could be used to better understand the sentiment of the conversation developing around the hashtag, *#nowplaying*, but scoped to just Tweets published within North America.

Here is what the two different queries, one for positive and one for negative, would look like without the HTTP encoding:

#nowplaying (happy OR exciting OR excited OR favorite OR fav OR amazing OR lovely OR incredible) (place\_country:US OR place\_country:MX OR place\_country:CA) -horrible -worst -sucks -bad -disappointing

#nowplaying (horrible OR worst OR sucks OR bad OR disappointing) (place\_country:US OR place\_country:MX OR place\_country:CA) -happy -exciting -excited -favorite -fav -amazing -lovely -incredible

And here is what the query would look like with the HTTP encoding, the query parameter, and the recent Tweet counts URI:

https://api.twitter.com/2/tweets/counts/recent?query=%23nowplaying%20(happy%20OR%20exciting%20OR%20excited%20OR%20favorite%20OR%20fav%20OR%20amazing%20OR%20lovely%20OR%20incredible)%20(place\_country%3AUS%20OR%20place\_country%3AMX%20OR%20place\_country%3ACA)%20-horrible%20-worst%20-sucks%20-bad%20-disappointing

https://api.twitter.com/2/tweets/counts/recent?query=%23nowplaying%20(horrible%20OR%20worst%20OR%20sucks%20OR%20bad%20OR%20disappointing)%20(place\_country%3AUS%20OR%20place\_country%3AMX%20OR%20place\_country%3ACA)%20-happy%20-exciting%20-excited%20-favorite%20-fav%20-amazing%20-lovely%20-incredible

#### 

#### 
Find Tweets that relate to a specific Tweet annotation

This rule was built to filter for original Tweets that included an image of a pet that is not a cat, where the language identified in the Tweet is Japanese. To do this, we used the context: operator to take advantage of the Tweet annotation functionality. We first used the Tweet lookup endpoint and the tweet.fields=context\_annotations fields parameter to identify which domain.entity IDs we need to use in our query:

* Tweets that relate to cats return **domain** 66 (Interests and Hobbies category) with entity 852262932607926273 (Cats).
* Tweets that relate to pets return **domain** 65 (Interests and Hobbies Vertical) with entity 852262932607926273 (Pets).

Here is what the query would look like without the HTTP encoding:

context:65.852262932607926273 -context:66.852262932607926273 -is:retweet has:images lang:ja

And here is what the query would look like with the HTTP encoding, the query parameter, and the recent Tweet counts URI:

https://api.twitter.com/2/tweets/counts/recent?query=context%3A65.852262932607926273%20-context%3A66.852262932607926273%20-is%3Aretweet%20has%3Aimages%20lang%3Aja

### 

### Operators

| **Operator** | Type | Availability | Description |
| **keyword** | Standalone | Core | Matches a keyword within the body of a Tweet. This is a tokenized match, meaning that your keyword string will be matched against the tokenized text of the Tweet body. Tokenization splits words based on punctuation, symbols, and Unicode basic plane separator characters.
For example, a Tweet with the text “I like coca-cola” would be split into the following tokens: I, like, coca, cola. These tokens would then be compared to the keyword string used in your query. To match strings containing punctuation (for example coca-cola), symbol, or separator characters, you must wrap your keyword in double-quotes.
Example: **pepsi OR cola OR "coca cola"** |
| **emoji** | Standalone | Core | Matches an emoji within the body of a Tweet. Similar to a keyword, emojis are a tokenized match, meaning that your emoji will be matched against the tokenized text of the Tweet body.
Note that if an emoji has a variant, you must wrap it in double quotes to add to a query.
Example: **(😃 OR 😡) 😬** |
| **"exact phrase match"** | Standalone | Core | Matches the exact phrase within the body of a Tweet.
Example: **("Twitter API" OR #v2) -"recent counts"** |
| **#** | Standalone | Core | Matches any Tweet containing a recognized hashtag, if the hashtag is a recognized entity in a Tweet.
This operator performs an exact match, NOT a tokenized match, meaning the rule **#thanku** will match posts with the exact hashtag #thanku, but not those with the hashtag #thankunext.
Example: **#thankunext #fanart OR @arianagrande** |
| **@** | Standalone | Core | Matches any Tweet that mentions the given username, if the username is a recognized entity (including the @ character).
Example: **(@twitterdev OR @twitterapi) -@twitter** |
| **$** | Standalone | Advanced | Matches any Tweet that contains the specified ‘cashtag’ (where the leading character of the token is the ‘$’ character).
Note that the cashtag operator relies on Twitter’s ‘symbols’ entity extraction to match cashtags, rather than trying to extract the cashtag from the body itself.
Example: **$twtr OR @twitterdev -$fb** |
| **from:** | Standalone | Core | Matches any Tweet from a specific user.
The value can be either the username (excluding the @ character) or the user’s numeric user ID.
You can only pass a single username/ID per **from:** operator.
Example: **from:twitterdev OR from:twitterapi -from:twitter** |
| **to:** | Standalone | Core | Matches any Tweet that is in reply to a particular user.
The value can be either the username (excluding the @ character) or the user’s numeric user ID.
You can only pass a single username/ID per **to:** operator.
Example: **to:twitterdev OR to:twitterapi -to:twitter** |
| **url:** | Standalone | Core | Performs a tokenized match on any validly-formatted URL of a Tweet.
This operator can matches on the contents of both the **url** or **expanded\_url** fields. For example, a Tweet containing "You should check out Twitter Developer Labs: https://t.co/c0A36SWil4" (with the short URL redirecting to https://developer.twitter.com) will match both the following rules:
**from:TwitterDev url:"https://developer.twitter.com"**(because it will match the contents of **entities.urls.expanded\_url**)
**from:TwitterDev url:"https://t.co"**(because it will match the contents of **entities.urls.url**)
Tokens and phrases containing punctuation or special characters should be double-quoted (for example, **url:"/developer"**). Similarly, to match on a specific protocol, enclose in double-quotes (for example, **url:"https://developer.twitter.com"**). |
| **retweets\_of:** | Standalone | Core | Matches Tweets that are Retweets of the specified user. The value can be either the username (excluding the @ character) or the user’s numeric user ID.
You can only pass a single username/ID per **retweets\_of:** operator.
Example: **retweets\_of:twitterdev OR retweets\_of:twitterapi** |
| **context:** | Standalone | Core | Matches Tweets with a specific domain id/enitity id pair. To learn more about this operator, please visit our page on annotations.
You can only pass a single domain/entity per **context:** operator.
**context:domain\_id.entity\_id**
However, you can combine multiple domain/entities using the OR operator:
`(context:47.1139229372198469633 OR context:11.1088514520308342784)`
Examples:
**context:10.799022225751871488**(**domain\_id.entity\_id** returns Tweets matching that specific domain-entity pair)
 |
| **entity:** | Standalone | Core | Matches Tweets with a specific entity string value. To learn more about this operator, please visit our page on annotations.
**Please note** that this is only available with recent search.
You can only pass a single **entity:** operator.
**entity:"string declaration of entity/place"**
Examples: **entity:"Michael Jordan" OR entity:"Barcelona"** |
| **conversation\_id:** | Standalone | Core | Matches Tweets that share a common conversation ID. A conversation ID is set to the Tweet ID of a Tweet that started a conversation. As Replies to a Tweet are posted, even Replies to Replies, the **conversation\_id** is added to its JSON payload.
You can only pass a single conversation ID per **conversation\_id:** operator.
Example: **conversation\_id:1334987486343299072 (from:twitterdev OR from:twitterapi)** |
| list: | Standalone | Advanced | **NEW** Matches Tweets posted by users who are members of a specified list. 
For example, if @twitterdev and @twitterapi were members of List 123, and you included list:123 in your query, your response will only contain Tweets that have been published by those accounts. You can find List IDs by using the List lookup endpoint.
**Please note** that you can only use a single list: operator per query, and you can only specify a single List per list: operator.
Example: list:123 |
| **place:** | Standalone | Advanced | Matches Tweets tagged with the specified location or Twitter place ID. Multi-word place names (“New York City”, “Palo Alto”) should be enclosed in quotes.
You can only pass a single place per **place:** operator.
Note: See the GET geo/search standard v1.1 endpoint for how to obtain Twitter place IDs.
Note: This operator will not match on Retweets, since Retweet's places are attached to the original Tweet. It will also not match on places attached to the original Tweet of a Quote Tweet.
Example: **place:"new york city" OR place:seattle OR place:fd70c22040963ac7** |
| **place\_country:** | Standalone | Advanced | Matches Tweets where the country code associated with a tagged place/location matches the given ISO alpha-2 character code.
You can find a list of valid ISO codes on Wikipedia.
You can only pass a single ISO code per **place\_country:** operator.
Note: This operator will not match on Retweets, since Retweet's places are attached to the original Tweet. It will also not match on places attached to the original Tweet of a Quote Tweet.
Example: **place\_country:US OR place\_country:MX OR place\_country:CA** |
| **point\_radius:** | Standalone | Advanced | Matches against the **place.geo.coordinates** object of the Tweet when present, and in Twitter, against a place geo polygon, where the Place polygon is fully contained within the defined region.
**point\_radius:[longitude latitude radius]*** Units of radius supported are miles (mi) and kilometers (km)
* Radius must be less than 25mi
* Longitude is in the range of ±180
* Latitude is in the range of ±90
* All coordinates are in decimal degrees
* Rule arguments are contained within brackets, space delimited

You can only pass a single geo polygon per **point\_radius:** operator.
Note: This operator will not match on Retweets, since Retweet's places are attached to the original Tweet. It will also not match on places attached to the original Tweet of a Quote Tweet.
Example: **point\_radius:[2.355128 48.861118 16km] OR point\_radius:[-41.287336 174.761070 20mi]**  |
| **bounding\_box:** | Standalone | Advanced | Matches against the place.geo.coordinates object of the Tweet when present, and in Twitter, against a place geo polygon, where the place polygon is fully contained within the defined region.
**bounding\_box:[west\_long south\_lat east\_long north\_lat]*** **west\_long south\_lat** represent the southwest corner of the bounding box where **west\_long** is the longitude of that point, and **south\_lat** is the latitude.
* **east\_long north\_lat** represent the northeast corner of the bounding box, where **east\_long** is the longitude of that point, and **north\_lat** is the latitude.
* Width and height of the bounding box must be less than 25mi
* Longitude is in the range of ±180
* Latitude is in the range of ±90
* All coordinates are in decimal degrees.
* Rule arguments are contained within brackets, space delimited.

You can only pass a single geo polygons per **bounding\_box:** operator. 
Note: This operator will not match on Retweets, since Retweet's places are attached to the original Tweet. It will also not match on places attached to the original Tweet of a Quote Tweet.
Example: **bounding\_box:[-105.301758 39.964069 -105.178505 40.09455]** |
| **is:retweet** | Conjunction required | Core | Matches on Retweets that match the rest of the specified rule. This operator looks only for true Retweets (for example, those generated using the Retweet button). Quote Tweets will not be matched by this operator.
Example: **data @twitterdev -is:retweet** |
| **is:reply** | Conjunction required | Core | Deliver only explicit replies that match a rule. Can also be negated to exclude replies that match a query from delivery.
Note: This operator is also available with the filtered stream endpoint. When used with filtered stream, this operator matches on replies to an original Tweet, replies in quoted Tweets, and replies in Retweets.
Example: **from:twitterdev is:reply** |
| **is:quote** | Conjunction required | Core | Returns all Quote Tweets, also known as Tweets with comments.
Example: **"sentiment analysis" is:quote** |
| **is:verified** | Conjunction required | Core | Deliver only Tweets whose authors are verified by Twitter.
Example: **#nowplaying is:verified** |
| **-is:nullcast** | Conjunction required | Advanced | Removes Tweets created for promotion only on ads.twitter.com that have a **"source":"Twitter for Advertisers (legacy)"** or **"source":"Twitter for Advertisers".**
This operator must be negated.
For more info on Nullcasted Tweets, see our page on Tweet availability.
Example: **"mobile games" -is:nullcast** |
| **has:hashtags** | Conjunction required | Core | Matches Tweets that contain at least one hashtag.
Example: **from:twitterdev -has:hashtags** |
| **has:cashtags** | Conjunction required | Advanced | Matches Tweets that contain a cashtag symbol (with a leading ‘$’ character. For example, **$tag**).
Example: **#stonks has:cashtags** |
| **has:links** | Conjunction required | Core | This operator matches Tweets which contain links and media in the Tweet body.
Example: **from:twitterdev announcement has:links** |
| **has:mentions** | Conjunction required | Core | Matches Tweets that mention another Twitter user.
Example: **#nowplaying has:mentions** |
| **has:media** | Conjunction required | Core | Matches Tweets that contain a media object, such as a photo, GIF, or video, as determined by Twitter. This will not match on media created with Periscope, or Tweets with links to other media hosting sites.
Example: **(kittens OR puppies) has:media** |
| **has:images** | Conjunction required | Core | Matches Tweets that contain a recognized URL to an image.
Example: **#meme has:images** |
| **has:videos** | Conjunction required | Core | Matches Tweets that contain native Twitter videos, uploaded directly to Twitter. This will not match on videos created with Periscope, or Tweets with links to other video hosting sites.
Example: **#icebucketchallenge has:videos** |
| **has:geo** | Conjunction required | Advanced | Matches Tweets that have Tweet-specific geolocation data provided by the Twitter user. This can be either a location in the form of a Twitter place, with the corresponding display name, geo polygon, and other fields, or in rare cases, a geo lat-long coordinate.
Note: Operators matching on place (Tweet geo) will only include matches from original tweets. Retweets do not contain any place data.
Example: **recommend #paris has:geo -bakery** |
| **lang:** | Conjunction required | Core | Matches Tweets that have been classified by Twitter as being of a particular language (if, and only if, the Tweet has been classified). It is important to note that each Tweet is currently only classified as being of one language, so AND’ing together multiple languages will yield no results.
You can only pass a single BCP 47 language identifier per **lang:** operator.
Note: if no language classification can be made the provided result is ‘und’ (for undefined).
Example: **recommend #paris lang:en**
The list below represents the currently supported languages and their corresponding BCP 47 language identifier:

|  |  |  |  |
| --- | --- | --- | --- |
| Amharic: **am** | German: **de** | Malayalam: **ml** | Slovak: **sk** |
| Arabic: **ar** | Greek: **el** | Maldivian: **dv** | Slovenian: **sl** |
| Armenian: **hy** | Gujarati: **gu** | Marathi: **mr** | Sorani Kurdish: **ckb** |
| Basque: **eu** | Haitian Creole: **ht** | Nepali: **ne** | Spanish: **es** |
| Bengali: **bn** | Hebrew: **iw** | Norwegian: **no** | Swedish: **sv** |
| Bosnian: **bs** | Hindi: **hi** | Oriya: **or** | Tagalog: **tl** |
| Bulgarian: **bg** | Latinized Hindi: **hi-Latn** | Panjabi: **pa** | Tamil: **ta** |
| Burmese: **my** | Hungarian: **hu** | Pashto: **ps** | Telugu: **te** |
| Croatian: **hr** | Icelandic: **is** | Persian: **fa** | Thai: **th** |
| Catalan: **ca** | Indonesian: **in** | Polish: **pl** | Tibetan: **bo** |
| Czech: **cs** | Italian: **it** | Portuguese: **pt** | Traditional Chinese: **zh-TW** |
| Danish: **da** | Japanese: **ja** | Romanian: **ro** | Turkish: **tr** |
| Dutch: **nl** | Kannada: **kn** | Russian: **ru** | Ukrainian: **uk** |
| English: **en** | Khmer: **km** | Serbian: **sr** | Urdu: **ur** |
| Estonian: **et** | Korean: **ko** | Simplified Chinese: **zh-CN** | Uyghur: **ug** |
| Finnish: **fi** | Lao: **lo** | Sindhi: **sd** | Vietnamese: **vi** |
| French: **fr** | Latvian: **lv** | Sinhala: **si** | Welsh: **cy** |
| Georgian: **ka** | Lithuanian: **lt** |  |
 |

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