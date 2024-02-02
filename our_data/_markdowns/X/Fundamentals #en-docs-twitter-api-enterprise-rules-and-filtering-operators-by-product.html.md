
Operators by product | Docs | Twitter Developer Platform 

Operators by product

All enterprise operators are available with PowerTrack and Historical PowerTrack APIs. However, only a subset of operators are available to the enterprise Search APIs, as noted on this page.

The dark blue tags note which operators are available to different enterprise products:

PowerTrack Search

We've also noted which operators are also available to the premium Search APIs. The darker blue represents paid premium tiers, while the lighter represents the free Sandbox tier:

 Premium Sandbox  

| Operator      | Product | Description | Matches on payload element |
| --- | --- | --- | --- |
| "exact phrase match" | PowerTrack
Search
Premium
Sandbox
  | Matches an exact phrase within the body of a Tweet.
Components that can translate into a search operators will be treated as words. In other words:* `"#hashtag"` will match `hashtag` but not `#hashtag` (use the hashtag operator without quotes to match on actual hashtags)
* `"$TWTR"` will match the word `TWTR` but not the cashtag `$TWTR` (use the cashtag operator without quotes to match on actual cashtags)
**Note:** in 30 Day Search and Full Archive Search (Enterprise and Premium), punctuation is not tokenized and is instead treated as whitespace.  | `text` |
| @ | PowerTrack
Search
Premium
Sandbox
  | Matches any Tweet that mentions the given username. The value can be either the username (excluding the `@` character) or the user’s numeric ID or (obtained for example via the GET users/lookup endpoint). | `entities.user_mentions` |
| # | PowerTrack
Search
Premium
Sandbox
  | Matches any Tweet with the given hashtag.
This operator performs an exact match. For example meaning the rule `#1989` will match Tweets containing the exact hashtag `#1989`, but not those with the hashtag `#TaylorSwift1989`.
**Note:** this operator relies on Twitter’s entity extraction to match hashtags, rather than extracting the hashtag from the body itself. For more details on JSON attributes from entities, refer to Twitter Entities. | `entities.hashtags` |
| $ | PowerTrack
Search | Matches any Tweet that contains the specified cashtag (where the leading character of the token is `$`).
**Note:**this operator relies on Twitter’s entity extraction to match links, rather than extracting the link from the body itself. For more details on JSON attributes from entities, refer to Twitter Entities.
 | `entities.symbols` |
| bio: | PowerTrack | *Available alias*: user\_bio:
Matches a keyword (using tokenized match) or a phrase within the user bio of a Tweet. Use double quotes to match a phrase. In other words:* `bio:software engineer` will match Tweets with the keyword `engineer` from users with the word `software` in their bio
* `bio:"software engineer"` will match any Tweet posted by users with the phrase `software engineer` in their bio
 | `user``.description` |
| bio\_location: | PowerTrack | *Available alias*: user\_bio\_location:
Matches Tweets where the User object's location contains the specified keyword (using tokenized match) or phrase.This location is a non-normalized, user-generated, free-form string, and is different from a Tweet's location (when available). 
 | `user.location` |
| bio\_name: | PowerTrack | Matches Tweets where the User object's name contains the specified keyword (using tokenized match) or phrase. | `user.name` |
| bounding\_box: | PowerTrack
Search
Premium
Sandbox
  | *Available alias*: geo\_bounding\_box:
Matches against the exact location (long, lat) of the Tweet (when present), and against a geo polygon (where the Place is fully contained within the defined region).* west\_long south\_lat represent the southwest corner of the bounding box where west-long is the longitude of that point, and south\_lat is the latitude.
* east\_long and north\_lat represent the northeast corner of the bounding box, where east\_long is the longitude of that point, and north\_lat is the latitude.
* Width and height of the bounding box must be less than 25mi
* Longitude is in the range of ±180
* Latitude is in the range of ±90
* All coordinates are in decimal degrees.
* Rule arguments are contained within brackets, space delimited.
**Note:** operators matching on place (Tweet geo) will only include matches from original Tweets. Retweets do not contain any place data. | `place` (original Tweets only) |
| contains: | PowerTrack | Substring match for Tweets that have the given substring in the body, regardless of tokenization. In other words, this does a pure substring match and does not consider word boundaries.Use double quotes to match substrings that contain whitespace or punctuation. | `text` |
| <emoji> | PowerTrack
Search
Premium
Sandbox
  | Matches an emoji within the body of a Tweet.
This is a tokenized match, so your emoji will be matched against the tokenized text of the Tweet body. Tokenization is based on punctuation, symbol/emoji, and separator Unicode basic plane characters. For example, a Tweet with the text “I like 🍕” would be split into the following tokens: I, like, 🍕. These tokens would then be compared to the emoji used in your rule.
**Note:** if an emoji has a variant, you must use double quotes to add to a rule. | `text` |
| followers\_count: | PowerTrack | Matches Tweets when the author has a followers count within the given range.* A single number (e.g. `followers_count:42`) will match any number equal to or greater than the value specified.
* A range (e.g. `followers_count:42..1337`) will match any number in the given range.
 | `user.followers_count` |
| friends\_count: | PowerTrack | *Available alias*: following\_count:
Matches Tweets when the author has a friends count (the number of users they follow) that falls within the given range.* A single number (e.g. `followers_count:42`) will match any number equal to or greater than the value specified.
* A range (e.g. `followers_count:42..1337`) will match any number in the given range.
 | `user.friends_count` |
| from: | PowerTrack
Search
Premium
Sandbox
  | Matches any Tweet from a specific user. The value can be either the username (excluding the `@` character) or the user’s numeric ID or (obtained for example via the GET users/lookup endpoint). | `user.id`, `user.id_str` (if using User ID)
`user.screen_name` (if using username) |
| has:geo | PowerTrack
Search
Premium | Matches Tweets that have Tweet-specific geolocation data provided from Twitter. This can be either “geo” lat-long coordinate, or a “location” in the form of a Twitter Place, with the corresponding display name, geo polygon, and other fields.
Cannot be used as a standalone operator.
**Note:** operators matching on place (Tweet geo) will only include matches from original tweets. Retweets do not contain any place data. | `place` (original Tweets only) |
| has:hashtags | PowerTrack
Search
Premium | Matches Tweets that contain at least one hashtag.
Cannot be used as a standalone operator. | `entities.hashtags` |
| has:images | PowerTrack
Search
Premium
Sandbox
  | Matches Tweets that contain at least one classified image URL.
Cannot be used as a standalone operator. | `entities.media` |
| has:lang | PowerTrack | Matches Tweets that have been classified by Twitter as being of a particular language.
If a Tweet has not been classified, the operator will not match. Each Tweet is currently only classified as being of one language, so AND’ing together multiple languages will yield no results.
Cannot be used as a standalone operator. | `lang` when value is not `und` |
| has:links | PowerTrack
Search
Premium
Sandbox
  | This operator matches Tweets which contain links in the Tweet body.
Cannot be used as a standalone operator.
**Note:** this operator relies on Twitter’s entity extraction to match links, rather than extracting the link from the body itself. For more details on JSON attributes from entities, refer to Twitter Entities. | `entities.urls` |
| has:media | PowerTrack
Search
Premium
Sandbox
  | *Available alias*: has:media\_link
Matches Tweets that contain at least one classified media URL.
Cannot be used as a standalone operator. | `entities.media` |
| has:mentions | PowerTrack
Search
Premium
Sandbox
  | Matches Tweets that mention another Twitter user.
Cannot be used as a standalone operator. | `entities.user_mentions` |
| has:profile\_geo | PowerTrack
Search
Premium | *Available alias*: has:derived\_user\_geo
Matches Tweets that have any Profile Geo metadata, regardless of the actual value.
Cannot be used as a standalone operator. | `user.location` |
| has:symbols | PowerTrack
Enterprise | Matches Tweets that contain a cashtag symbol (e.g. `$TWTR`).
Cannot be used as a standalone operator. | `entities.symbols` |
| has:videos | PowerTrack
Search
Premium
Sandbox
  | *Available alias*: has:video\_link
Matches Tweets that contain at least one classified media URL.
Cannot be used as a standalone operator. | `entities.media`
 |
| in\_reply\_to\_status\_id: | PowerTrack | *Available alias*: in\_reply\_to\_tweet\_id:
Deliver only explicit replies to the specified Tweet. | `id`, `id_str` of the target Tweet |
| is:quote | PowerTrack | Deliver explicit Quote Tweets that match a rule.
It can also be negated (`-is:quote`) to exclude Quote Tweets that match a rule from delivery.
Cannot be used as a standalone operator. | `is_quote_status` (if `true`) |
| is:reply | PowerTrack
Search
Premium | Deliver only replies that match a rule.
It can also be negated (`-is:reply`) to exclude delivery of replies that match the specified rule.
With PowerTrack, this operator matches on:* Replies to an original Tweet
* Replies in quoted Tweets
* Replies in Retweets

When used with the Search API, this operator matches on replies to an original Tweet, but excludes replies in quoted Tweets and replies in Retweets.
You can use this operators in conjunction with `is:retweet` and `is:quote` to only deliver replies to original Tweets.
Cannot be used as a standalone operator with the Search API.
**Note**: with Premium, this operator is not available in Sandbox dev environments. | Reply elements, e.g. `in_reply_to_status_id` |
| is:retweet | PowerTrack
Search
Premium | Deliver only explicit Retweets that match a rule.
It can also be negated (`-is:retweet`) to exclude Retweets that match a rule from delivery and only original content is delivered.
This operator looks only for true Retweets (i.e. Retweets posted using the Retweet button). Quoted Tweets and modified Tweets which do not use Twitter’s Retweet functionality will not be matched by this operator.
Cannot be used as a standalone operator. | Retweet elements, e.g. `retweeted_status` |
| is:verified | PowerTrack
Search
Premium | Deliver only Tweets where the author is verified by Twitter.
It can also be negated to exclude Tweets where the author is verified.
Cannot be used as a standalone operator. | `user.verified` |
| keyword | PowerTrack
Search
Premium
Sandbox
  | Matches a keyword within the body of a Tweet.
This is a tokenized match, meaning that your keyword string will be matched against the tokenized text of the Tweet body. Tokenization is based on punctuation, symbol/emoji, and separator Unicode basic plane characters. For example, a Tweet with the text “I like coca-cola” would be split into the following tokens: `I`, `like`, `coca`, `cola`. These tokens would then be compared to the keyword string used in your rule. To match strings containing punctuation (e.g. coca-cola), symbol, or separator characters, you must use an exact phrase match operator.  | `text` |
| lang: | PowerTrack
Search
Premium
Sandbox
  | Matches Tweets that have been classified by Twitter as being of a particular language (if, and only if, the tweet has been classified). Each Tweet will be classified with only one language, so AND’ing together multiple languages will yield no results.
**Note:**if no language classification can be made the provided result is `und` (for undefined).
This operator will only match against supported languages. Providing any other value (including `und`) will result in the operator being ignored (in other words, Tweets will not be filtered by this operator). The list below represents the currently supported languages and their corresponding BCP 47 language identifier:
`am` Amharic
`hu` Hungarian
`pt` Portuguese
`ar` Arabic
`is` Icelandic
`ro` Romanian
`hy` Armenian
`in` Indonesian
`ru` Russian
`bn` Bengali
`it` Italian
`sr` Serbian
`bg` Bulgarian
`ja` Japanese
`sd` Sindhi
`my` Burmese
`kn` Kannada
`si` Sinhala
`zh` Chinese
`km` Khmer
`sk` Slovak
`cs` Czech
`ko` Korean
`sl` Slovenian
`da` Danish
`lo` Lao
`ckb` Sorani Kurdish
`nl` Dutch
`lv` Latvian
`es` Spanish
`en` English
`lt` Lithuanian
`sv` Swedish
`et` Estonian
`ml` Malayalam
`tl` Tagalog
`fi` Finnish
`dv` Maldivian
`ta` Tamil
`fr` French
`mr` Marathi
`te` Telugu
`ka` Georgian
`ne` Nepali
`th` Thai
`de` German
`no` Norwegian
`bo` Tibetan
`el` Greek
`or` Oriya
`tr` Turkish
`gu` Gujarati
`pa` Panjabi
`uk` Ukrainian
`ht` Haitian
`ps` Pashto
`ur` Urdu
`iw` Hebrew
`fa` Persian
`ug` Uyghur
`hi` Hindi
`pl` Polish
`vi` Vietnamese
`cy` Welsh
 | `lang` when value is not `und` |
| listed\_count: | PowerTrack | *Available alias*: user\_in\_lists\_count:
 Matches Tweets when the author has been listed on Twitter a number of times falls within the given range.* A single number (e.g. `listed_count:42`) will match any number equal to or greater than the value specified.
* A range (e.g. `listed_count:42..1337`) will match any number in the given range.
 | `user.listed_count` |
| place\_country: | PowerTrack
Search
Premium
Sandbox
  | Matches Tweets where the country code associated with a tagged place/location matches the given ISO alpha-2 character code.
**Note:** operators matching on place (Tweet geo) will only include matches from original tweets. Retweets do not contain any place data. | `place` (original Tweets only) |
| place: | PowerTrack
Search
Premium
Sandbox
  | Matches Tweets tagged with specified location or Twitter place ID. Multi-word place names should be enclosed in quotes (e.g. `place:"San Francisco"`)
**Note:** operators matching on place (Tweet geo) will only include matches from original tweets. Retweets do not contain any place data. | `place` (original Tweets only)
 |
| point\_radius: | PowerTrack
Search
Premium
Sandbox
  | **Note:** operators matching on place (Tweet geo) will only include matches from original tweets. Retweets do not contain any place data. | `place` (original Tweets only)
 |
| profile\_bounding\_box:[west\_long south\_lat east\_long north\_lat] | PowerTrack | Matches against the user's exact Location (long, lat) in the Profile Geo enrichment where the Place is fully contained within the defined region.* west\_long south\_lat represent the southwest corner of the bounding box where west-long is the longitude of that point, and south\_lat is the latitude.
* east\_long and north\_lat represent the northeast corner of the bounding box, where east\_long is the longitude of that point, and north\_lat is the latitude.
* Width and height of the bounding box must be less than 25mi
* Longitude is in the range of ±180
* Latitude is in the range of ±90
* All coordinates are in decimal degrees.
* Rule arguments are contained within brackets, space delimited.
**Note:** operators matching on place (Tweet geo) will only include matches from original tweets. Retweets do not contain any place data. | `user.derived.locations.geo.coordinates` |
| profile\_country: | PowerTrack
Search
Premium | Exact match on the country code from the Profile Geo enrichment.
Uses a normalized set of two-letter country codes, based on ISO-3166-1-alpha-2 specification.
To be concise, this operator is provided in lieu of an operator for the country field from the address object.
**Note:** operators matching on place (Tweet geo) will only include matches from original tweets. Retweets do not contain any place data. | `user.derived.locations.country_code`
 |
| profile\_locality: | PowerTrack
Search
Premium | Exact match on the Locality field from the Profile Geo enrichment.
This is an exact full string match.
It is not necessary to escape characters with a backslash. For example, if matching something with a slash, use `one/two`.
Use double quotes to match substrings that contain whitespace or punctuation, e.g. `profile_locality:"Lower East Side"`.
  | `user.derived.locations.locality` |
| profile\_point\_radius:[lon lat radius] | PowerTrack | Matches against the Exact Location (x,y) of the user's Profile Geo enrichment.* Units of radius supported are miles (mi) and kilometers (km).
* Radius must be less than 25mi.
* Longitude is in the range of ±180
* Latitude is in the range of ±90
* All coordinates are in decimal degrees.
* Rule arguments are contained within brackets, space delimited.
**Note:** operators matching on place (Tweet geo) will only include matches from original tweets. Retweets do not contain any place data. | `user.derived.locations.geo` |
| profile\_region: | PowerTrack
Search
Premium | Exact match on the Region field from the Profile Geo enrichment.
This is an exact full string match.
It is not necessary to escape characters with a backslash. For example, if matching something with a slash, use `one/two`.
Use double quotes to match substrings that contain whitespace or punctuation, e.g. `profile_locality:"New York"`. | `user.derived.locations.region` |
| profile\_subregion: | PowerTrack | Exact match on the Subregion field from the Profile Geo enrichment.
This is an exact full string match.
It is not necessary to escape characters with a backslash. For example, if matching something with a slash, use `one/two`.
Use double quotes to match substrings that contain whitespace or punctuation, e.g. `profile_locality:"Kings County"`. | `user.derived.locations.sub_region` |
| "keyword1 keyword2"~N | PowerTrack
Search | Commonly referred to as a proximity operator, this matches a Tweet where the keywords are no more than N tokens from each other.
If the keywords are in the opposite order, they can not be more than N-2 tokens from each other.
Can have any number of keywords in quotes.
N cannot be greater than 6. | `text` |
| retweets\_of\_status\_id: | PowerTrack | *Available alias*: retweets\_of\_tweet\_id:
Deliver only explicit Retweets of the specified original Tweet. | `retweeted_status.id`, `retweeted_status.id_str` |
| retweets\_of: | PowerTrack
Search
Premium
Sandbox
  | *Available alias*: retweets\_of\_user:
Matches any Tweet that are Retweets of the given user. The value can be either the username (excluding the `@` character) or the user’s numeric ID or (obtained for example via the GET users/lookup endpoint). | `retweeted_status.id` (if present) |
| sample: | PowerTrack | Returns a random percent sample of Tweets that match a rule rather than the entire set of Tweets. The percent value must be represented by an integer between 1 and 100.
This operator applies to the entire rule and requires all OR'd terms to be grouped.
**Note:** the sample operator first reduces the scope of the firehose to X%, then the rule/filter is applied to that sampled subset. If you are using, for example, `sample:10`, each Tweet has a 10% chance of being in the sample. 
**Note:** the sampling is deterministic, and you will get the same data sample in realtime as you would if you pulled the data historically. |  |
| source: | PowerTrack | Matches any Tweet generated by the given source application. The value must be either the name of the application or the application’s URL.
Cannot be used as a standalone operator. | `source` |
| statuses\_count: | PowerTrack | *Available alias*: tweets\_count:
Matches Tweets when the author has posted a number of statuses that falls within the given range.* A single number (e.g. `statuses_count:42`) will match any number equal to or greater than the value specified.
* A range (e.g. `statuses_count:42..1337`) will match any number in the given range.
 | `user``.statuses_count` |
| to: | PowerTrack
Search
Premium
Sandbox
  | Matches any Tweet that is in reply to a particular user. The value can be either the username (excluding the `@` character) or the user’s numeric ID or (obtained for example via the GET users/lookup endpoint). | `text` |
| url: | PowerTrack
Search
Premium
Sandbox
  | Performs a tokenized match on the expanded URLs of a Tweet. Tokens and phrases containing punctuation or special characters should be double-quoted (e.g. `url:"/developer"`).
While generally not recommended, the operator can also match on a specific protocol, enclosed in double-quotes (e.g. `url:"https://developer.twitter.com"`). | `entities.urls.expanded_url` |
| url\_contains: | PowerTrack | Performs a keyword/phrase match on the (new) expanded URL title metadata enrichment. | `entities.urls.expanded_url` |
| url\_description: | PowerTrack | *Available alias*: within\_url\_description:
Performs a keyword/phrase match on the (new) expanded page description metadata enrichment.  | `entities.urls.unwound.description` |
| url\_title: | PowerTrack | *Available alias*: within\_url\_title:
Performs a keyword/phrase match on the (new) expanded URL title metadata enrichment.  | `entities.urls.title` |

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