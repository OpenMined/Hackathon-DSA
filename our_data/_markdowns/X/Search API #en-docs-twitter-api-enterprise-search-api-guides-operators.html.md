
Building search queries | Docs | Twitter Developer Platform 

Building search queries

Premium and enterprise operators
================================

Below is a list of all operators supported in Twitter's premium and enterprise search APIs:

* Enterprise 30-day search API
* Enterprise Full-archive search API

For a side-by-side comparison of available operators by product see HERE.  

|  Operator | Description |
| --- | --- |
| keyword | Matches a tokenized keyword within the body or urls of a Tweet. This is a tokenized match, meaning that your keyword string will be matched against the tokenized text of the Tweet body – tokenization is based on punctuation, symbol, and separator Unicode basic plane characters. For example, a Tweet with the text “I like coca-cola” would be split into the following tokens: I, like, coca, cola. These tokens would then be compared to the keyword string used in your rule. To match strings containing punctuation (for example, coca-cola), symbol, or separator characters, you must use a quoted exact match as described below.
**Note:** With the Search API, accented and special characters are normalized to standard latin characters, which can change meanings in foreign languages or return unexpected results:
For example, "músic" will match “music” and vice versa. 
For example, common phrases like "Feliz Año Nuevo!" in Spanish, would be indexed as "Feliz Ano Nuevo", which changes the meaning of the phrase.
**Note:** This operator will match on both URLs and unwound URLs within a Tweet. |
| emoji | Matches an emoji within the body of a Tweet. Emojis are a tokenized match, meaning that your emoji will be matched against the tokenized text of the Tweet body – tokenization is based on punctuation, symbol/emoji, and separator Unicode basic plane characters. For example, a Tweet with the text “I like 🍕” would be split into the following tokens: I, like, 🍕. These tokens would then be compared to the emoji used in your rule. Note that if an emoji has a variant, you must use “quotations” to add to a rule. |
| "exact phrase match" | Matches the tokenized and ordered phrase within the body or urls of a Tweet. This is a tokenized match, meaning that your keyword string will be matched against the tokenized text of the Tweet body – tokenization is based on punctuation, symbol, and separator Unicode basic plane characters.
**Note:** Punctuation is not tokenized and is instead treated as whitespace. 
For example, quoted “#hashtag” will match “hashtag” but not #hashtag (use the hashtag # operator without quotes to match on actual hashtags. 
For example, quoted “$cashtag” will match “cashtag” but not $cashtag (use the cashtag $ operator without quotes to match on actual cashtags. 
For example, "Love Snow" will match "#love #snow"
 For example, "#Love #Snow" will match "love snow"
**Note:** This operator will match on both URLs and unwound URLs within a Tweet. |
| "keyword1 keyword2"~N | Commonly referred to as a proximity operator, this matches a Tweet where the keywords are no more than N tokens from each other.
If the keywords are in the opposite order, they can not be more than N-2 tokens from each other. Can have any number of keywords in quotes. N cannot be greater than 6.
Note that this operator is only available in the enterprise search APIs.
 |
| from: | Matches any Tweet from a specific user.
The value must be the user’s Twitter numeric Account ID or username (excluding the @ character). See HERE or HERE for methods for looking up numeric Twitter Account IDs. |
| to: | Matches any Tweet that is in reply to a particular user.
The value must be the user’s numeric Account ID or username (excluding the @ character). See HERE for methods for looking up numeric Twitter Account IDs. |
| url: | Performs a tokenized (keyword/phrase) match on the expanded URLs of a tweet (similar to url\_contains). Tokens and phrases containing punctuation or special characters should be double-quoted. For example, url:"/developer". While generally not recommended, if you want to match on a specific protocol, enclose in double-quotes: url:"https://developer.twitter.com".
**Note:** When using PowerTrack or Historical PowerTrack, this operator will match on URLs contained within the original Tweet of a Quote Tweet. For example, if your rule includes url:"developer.twitter.com", and a Tweet contains that URL, any Quote Tweets of that Tweet will be included in the results. This is not the case when using the Search API.  |
| # | Matches any Tweet with the given hashtag.
This operator performs an exact match, NOT a tokenized match, meaning the rule “2016” will match posts with the exact hashtag “2016”, but not those with the hashtag “2016election”
Note: that the hashtag operator relies on Twitter’s entity extraction to match hashtags, rather than extracting the hashtag from the body itself. See HERE for more information on Twitter Entities JSON attributes. |
| @ | Matches any Tweet that mentions the given username.
The to: operator returns a subset match of the @mention operator. |
| $ | Matches any Tweet that contains the specified ‘cashtag’ (where the leading character of the token is the ‘$’ character).
Note that the cashtag operator relies on Twitter’s ‘symbols’ entity extraction to match cashtags, rather than trying to extract the cashtag from the body itself. See HERE for more information on Twitter Entities JSON attributes.
Note that this operator is only available in the enterprise search APIs. |
| retweets\_of: | *Available alias*: retweets\_of\_user:
Matches tweets that are retweets of a specified user. Accepts both usernames and numeric Twitter Account IDs (NOT tweet status IDs).
See HERE for methods for looking up numeric Twitter Account IDs.
 |
| lang: | Matches Tweets that have been classified by Twitter as being of a particular language (if, and only if, the tweet has been classified). It is important to note that each Tweet is currently only classified as being of one language, so AND’ing together multiple languages will yield no results.
**Note:** if no language classification can be made the provided result is ‘und’ (for undefined).
The list below represents the current supported languages and their corresponding BCP 47 language indentifier:
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
| place: | Matches Tweets tagged with the specified location *or* Twitter place ID (see examples). Multi-word place names (“New York City”, “Palo Alto”) should be enclosed in quotes.
**Note:** See the GET geo/search public API endpoint for how to obtain Twitter place IDs.
**Note:** This operator will not match on Retweets, since Retweet's places are attached to the original Tweet. It will also not match on places attached to the original Tweet of a Quote Tweet. |
| place\_country: | Matches Tweets where the country code associated with a tagged place matches the given ISO alpha-2 character code.
Valid ISO codes can be found here: http://en.wikipedia.org/wiki/ISO\_3166-1\_alpha-2
**Note:** This operator will not match on Retweets, since Retweet's places are attached to the original Tweet. It will also not match on places attached to the original Tweet of a Quote Tweet. |
| point\_radius:[lon lat radius] | Matches against the Exact Location (x,y) of the Tweet when present, and in Twitter, against a “Place” geo polygon, where the Place is fully contained within the defined region.* Units of radius supported are miles (mi) and kilometers (km).
* Radius must be less than 25mi.
* Longitude is in the range of ±180
* Latitude is in the range of ±90
* All coordinates are in decimal degrees.
* Rule arguments are contained with brackets, space delimited.
**Note:** This operator will not match on Retweets, since Retweet's places are attached to the original Tweet. It will also not match on places attached to the original Tweet of a Quote Tweet. |
| bounding\_box:[west\_long south\_lat east\_long north\_lat] | *Available alias*: geo\_bounding\_box:
Matches against the Exact Location (long, lat) of the Tweet when present, and in Twitter, against a “Place” geo polygon, where the Place is fully contained within the defined region.* west\_long south\_lat represent the southwest corner of the bounding box where west-long is the longitude of that point, and south\_lat is the latitude.
* east\_long and north\_lat represent the northeast corner of the bounding box, where east\_long is the longitude of that point, and north\_lat is the latitude.
* Width and height of the bounding box must be less than 25mi
* Longitude is in the range of ±180
* Latitude is in the range of ±90
* All coordinates are in decimal degrees.
* Rule arguments are contained with brackets, space delimited.
**Note:** This operator will not match on Retweets, since Retweet's places are attached to the original Tweet. It will also not match on places attached to the original Tweet of a Quote Tweet. |
| profile\_country: | Exact match on the “countryCode” field from the “address” object in the Profile Geo enrichment.
Uses a normalized set of two-letter country codes, based on ISO-3166-1-alpha-2 specification. This operator is provided in lieu of an operator for “country” field from the “address” object to be concise. |
| profile\_region: | Matches on the “region” field from the “address” object in the Profile Geo enrichment.
This is an exact full string match. It is not necessary to escape characters with a backslash. For example, if matching something with a slash, use “one/two”, not “one\/two”. Use double quotes to match substrings that contain whitespace or punctuation. |
| profile\_locality: | Matches on the “locality” field from the “address” object in the Profile Geo enrichment.
This is an exact full string match. It is not necessary to escape characters with a backslash. For example, if matching something with a slash, use “one/two”, not “one\/two”. Use double quotes to match substrings that contain whitespace or punctuation. |

**NOTE:** All is: and has: operators cannot be used as standalone operators when using the Search API, and must be combined with another clause.

For example, @TwitterDev has:links

|  |  |
| --- | --- |
| has:geo | Matches Tweets that have Tweet-specific geo location data provided from Twitter. This can be either “geo” lat-long coordinate, or a “location” in the form of a Twitter “Place”, with corresponding display name, geo polygon, and other fields.
**Note:** When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. |
| has:profile\_geo | *Available alias*: has:derived\_user\_geo
Matches Tweets that have any Profile Geo metadata, regardless of the actual value.
**Note:** When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`.
 |
| has:links | This operators matches Tweets which contain links in the message body.
**Note:** When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. |
| is:retweet | Deliver only explicit retweets that match a rule. Can also be negated to exclude retweets that match a rule from delivery and only original content is delivered.
This operator looks only for true Retweets, which use Twitter’s retweet functionality. Quoted Tweets and Modified Tweets which do not use Twitter’s retweet functionality will not be matched by this operator.
**Note:** When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. |
| is:reply | An operator to filter Tweets based on whether they are or are not replies to Tweets. Deliver only explicit replies that match a rule. Can also be negated to exclude replies that match a rule from delivery.
Note that this operator is available for paid premium and enterprise search and is not available in Sandbox dev environments.
**Note:** When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. |
| is:quote | Delivers only Quote Tweets, or Tweets that reference another Tweet, as identified by the "is\_quote\_status":true in Tweet payloads. Can also be negated to exclude Quote Tweets.
**Note:** When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. |
| is:verified | Deliver only Tweets where the author is “verified” by Twitter. Can also be negated to exclude Tweets where the author is verified.
**Note:** When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. |
| has:mentions | Matches Tweets that mention another Twitter user.
**Note:** When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. |
| has:hashtags | Matches Tweets that contain a hashtag.
**Note:** When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. |
| has:media | *Available alias*: has:media\_link
Matches Tweets that contain a media url classified by Twitter. For example, pic.twitter.com.

**Note:** When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`.
  |
| has:images | Matches Tweets that contain a media url classified by Twitter. For example, pic.twitter.com.
**Note:** When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. |
| has:videos | *Available alias*: has:video\_link
Matches Tweets that contain native Twitter videos, uploaded directly to Twitter. This will not match on videos created with Vine, Periscope, or Tweets with links to other video hosting sites.
**Note:** When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`.
 |
| has:symbols | Matches Tweets that contain a cashtag symbol (with a leading ‘$’ character. For example, $tag).  Note that this operator is only available in the enterprise search APIs.
**Note:** When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. |

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