Introduction

This is the standard v1.1 data dictionary. We also have data dictionaries for [premium v1.1](https://developer.twitter.com/en/docs/twitter-api/premium/data-dictionary), [enterprise](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary), and [Twitter API v2](https://developer.twitter.com/en/docs/twitter-api/data-dictionary). 

If you are migrating from a standard v1.1 endpoint to a v2 endpoint, we've put together a [data format migration guide](https://developer.twitter.com/en/docs/twitter-api/migrate/data-formats) that you can use to map standard v1.1 fields to v2 fields. This guide will also let you know which fields and expansions parameters you will need to include in your request to return specific v2 fields. 

Introduction
------------

Standard

All Twitter APIs that return Tweets provide that data encoded using JavaScript Object Notation (JSON). JSON is based on key-value pairs, with named attributes and associated values. These attributes, and their state are used to describe objects.  

At Twitter we serve many objects as JSON, including _Tweets and_ _Users_. These objects all encapsulate core attributes that describe the object. Each Tweet has an author, a message, a unique ID, a timestamp of when it was posted, and sometimes geo metadata shared by the user. Each User has a Twitter name, an ID, a number of followers, and most often an account bio.

With each Tweet we also generate "entity" objects, which are arrays of common Tweet contents such as hashtags, mentions, media, and links. If there are links, the JSON payload can also provide metadata such as the fully unwound URL and the webpage’s title and description.

So, in addition to the text content itself, a Tweet can have over 150 attributes associated with it. Let’s start with an example Tweet:

> 1/ Today we’re sharing our vision for the future of the Twitter API platform![https://t.co/XweGngmxlP](https://t.co/XweGngmxlP)
> 
> — Twitter Dev (@TwitterDev) [April 6, 2017](https://twitter.com/TwitterDev/status/850006245121695744)

  
The following JSON illustrates the structure for these objects and some of their attributes:

      `{   "created_at": "Thu Apr 06 15:24:15 +0000 2017",   "id_str": "850006245121695744",   "text": "1\/ Today we\u2019re sharing our vision for the future of the Twitter API platform!\nhttps:\/\/t.co\/XweGngmxlP",   "user": {     "id": 2244994945,     "name": "Twitter Dev",     "screen_name": "TwitterDev",     "location": "Internet",     "url": "https:\/\/dev.twitter.com\/",     "description": "Your official source for Twitter Platform news, updates & events. Need technical help? Visit https:\/\/twittercommunity.com\/ \u2328\ufe0f #TapIntoTwitter"   },   "place": {      },   "entities": {     "hashtags": [           ],     "urls": [       {         "url": "https:\/\/t.co\/XweGngmxlP",         "unwound": {           "url": "https:\/\/cards.twitter.com\/cards\/18ce53wgo4h\/3xo1c",           "title": "Building the Future of the Twitter API Platform"         }       }     ],     "user_mentions": [          ]   } }`
    

Next steps
----------

Review the standard v1.1 objects to better understand each field:

* [Tweet object](https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/tweet)
* [User object](https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/user)
* [Entities object](https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/entities)
* [Extended entities object](https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/extended-entities)
* [Geo object](https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/geo)

Tweet object

Tweet Object
------------

Tweets are the basic atomic building block of all things Twitter. Tweets are also known as “status updates.” The Tweet object has a long list of ‘root-level’ attributes, including fundamental attributes such as `id`, `created_at`, and `text`. Tweet objects are also the ‘parent’ object to several child objects. Tweet child objects include `user`, `entities`, and `extended_entities`. Tweets that are geo-tagged will have a `place` child object.

When the following Tweet is rendered in JSON:

> 1/ To make room for more expression, we will now count all emojis as equal—including those with gender‍‍‍ ‍‍and skin t… https://t.co/MkGjXf9aXm
> 
> — TwitterAPI (@TwitterAPI) [Oct 10, 2018](https://twitter.com/TwitterDev/status/1050118621198921728)

The JSON will be a mix of ‘root-level’ attributes (here we are highlighting some of the most fundamental attributes), and child objects (which are represented here with the `{}` notation):

{
 "created\_at": "Wed Oct 10 20:19:24 +0000 2018",
 "id": 1050118621198921728,
 "id\_str": "1050118621198921728",
 "text": "To make room for more expression, we will now count all emojis as equal—including those with gender‍‍‍ ‍‍and skin t… https://t.co/MkGjXf9aXm",
 "user": {},  
 "entities": {}
}

### Tweet Data Dictionary

Below you will find the data dictionary for these ‘root-level’ attributes, as well as links to child object data dictionaries.

| Attribute | Type | Description |
| --- | --- | --- |
| created\_at | String | UTC time when this Tweet was created. Example:<br><br>"created\_at": "Wed Oct 10 20:19:24 +0000 2018" |
| id  | Int64 | The integer representation of the unique identifier for this Tweet. This number is greater than 53 bits and some programming languages may have difficulty/silent defects in interpreting it. Using a signed 64 bit integer for storing this identifier is safe. Use `id_str` to fetch the identifier to be safe. See [Twitter IDs](https://developer.twitter.com/en/docs/twitter-ids) for more information. Example:<br><br>"id":1050118621198921728 |
| id\_str | String | The string representation of the unique identifier for this Tweet. Implementations should use this rather than the large integer in `id`. Example:<br><br>"id\_str":"1050118621198921728" |
| text | String | The actual UTF-8 text of the status update. See [twitter-text](https://github.com/twitter/twitter-text/blob/master/rb/lib/twitter-text/regex.rb) for details on what characters are currently considered valid. Example:<br><br>"text":"To make room for more expression, we will now count all emojis as equal—including those with gender‍‍‍ ‍‍and skin t… https://t.co/MkGjXf9aXm" |
| source | String | Utility used to post the Tweet, as an HTML-formatted string. Tweets from the Twitter website have a source value of `web`.<br><br>Example:<br><br>"source":"Twitter Web Client" |
| truncated | Boolean | Indicates whether the value of the `text` parameter was truncated, for example, as a result of a retweet exceeding the original Tweet text length limit of 140 characters. Truncated text will end in ellipsis, like this `...` Since Twitter now rejects long Tweets vs truncating them, the large majority of Tweets will have this set to `false` . Note that while native retweets may have their toplevel `text` property shortened, the original text will be available under the `retweeted_status` object and the `truncated` parameter will be set to the value of the original status (in most cases, `false` ). Example:<br><br>"truncated":true |
| in\_reply\_to\_status\_id | Int64 | _Nullable._ If the represented Tweet is a reply, this field will contain the integer representation of the original Tweet’s ID. Example:<br><br>"in\_reply\_to\_status\_id":1051222721923756032 |
| in\_reply\_to\_status\_id\_str | String | _Nullable._ If the represented Tweet is a reply, this field will contain the string representation of the original Tweet’s ID. Example:<br><br>"in\_reply\_to\_status\_id\_str":"1051222721923756032" |
| in\_reply\_to\_user\_id | Int64 | _Nullable._ If the represented Tweet is a reply, this field will contain the integer representation of the original Tweet’s author ID. This will not necessarily always be the user directly mentioned in the Tweet. Example:<br><br>"in\_reply\_to\_user\_id":6253282 |
| in\_reply\_to\_user\_id\_str | String | _Nullable._ If the represented Tweet is a reply, this field will contain the string representation of the original Tweet’s author ID. This will not necessarily always be the user directly mentioned in the Tweet. Example:<br><br>"in\_reply\_to\_user\_id\_str":"6253282" |
| in\_reply\_to\_screen\_name | String | _Nullable._ If the represented Tweet is a reply, this field will contain the screen name of the original Tweet’s author. Example:<br><br>"in\_reply\_to\_screen\_name":"twitterapi" |
| user | [User object](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object) | The user who posted this Tweet. See User data dictionary for complete list of attributes.<br><br>Example highlighting select attributes:<br><br> { "user": {<br>    "id": 6253282,<br>    "id\_str": "6253282",<br>    "name": "Twitter API",<br>    "screen\_name": "TwitterAPI",<br>    "location": "San Francisco, CA",<br>    "url": "https://developer.twitter.com",<br>    "description": "The Real Twitter API. Tweets about API changes, service issues and our Developer Platform. Don't get an answer? It's on my website.",<br>    "verified": true,<br>    "followers\_count": 6129794,<br>    "friends\_count": 12,<br>    "listed\_count": 12899,<br>    "favourites\_count": 31,<br>    "statuses\_count": 3658,<br>    "created\_at": "Wed May 23 06:01:13 +0000 2007",<br>    "utc\_offset": null,<br>    "time\_zone": null,<br>    "geo\_enabled": false,<br>    "lang": "en",<br>    "contributors\_enabled": false,<br>    "is\_translator": false,<br>    "profile\_background\_color": "null",<br>    "profile\_background\_image\_url": "null",<br>    "profile\_background\_image\_url\_https": "null",<br>    "profile\_background\_tile": null,<br>    "profile\_link\_color": "null",<br>    "profile\_sidebar\_border\_color": "null",<br>    "profile\_sidebar\_fill\_color": "null",<br>    "profile\_text\_color": "null",<br>    "profile\_use\_background\_image": null,<br>    "profile\_image\_url": "null",<br>    "profile\_image\_url\_https": "https://pbs.twimg.com/profile\_images/942858479592554497/BbazLO9L\_normal.jpg",<br>    "profile\_banner\_url": "https://pbs.twimg.com/profile\_banners/6253282/1497491515",<br>    "default\_profile": false,<br>    "default\_profile\_image": false,<br>    "following": null,<br>    "follow\_request\_sent": null,<br>    "notifications": null<br>  }<br>} |
| coordinates | [Coordinates](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/geo-objects#coordinates-dictionary) | _Nullable._ Represents the geographic location of this Tweet as reported by the user or client application. The inner coordinates array is formatted as [geoJSON](http://www.geojson.org/) (longitude first, then latitude). Example:<br><br>"coordinates":<br>{<br>    "coordinates":<br>    \[<br>        -75.14310264,<br>        40.05701649<br>    \],<br>    "type":"Point"<br>} |
| place | [Places](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/geo-objects#place-dictionary) | _Nullable_ When present, indicates that the tweet is associated (but not necessarily originating from) a Place . Example:<br><br>"place":<br>{<br>  "attributes":{},<br>   "bounding\_box":<br>  {<br>     "coordinates":<br>     \[\[<br>           \[-77.119759,38.791645\],<br>           \[-76.909393,38.791645\],<br>           \[-76.909393,38.995548\],<br>           \[-77.119759,38.995548\]<br>     \]\],<br>     "type":"Polygon"<br>  },<br>   "country":"United States",<br>   "country\_code":"US",<br>   "full\_name":"Washington, DC",<br>   "id":"01fbe706f872cb32",<br>   "name":"Washington",<br>   "place\_type":"city",<br>   "url":"http://api.twitter.com/1/geo/id/0172cb32.json"<br>} |
| quoted\_status\_id | Int64 | This field only surfaces when the Tweet is a quote Tweet. This field contains the integer value Tweet ID of the quoted Tweet. Example:<br><br>"quoted\_status\_id":1050119905717055488 |
| quoted\_status\_id\_str | String | This field only surfaces when the Tweet is a quote Tweet. This is the string representation Tweet ID of the quoted Tweet. Example:<br><br>"quoted\_status\_id\_str":"1050119905717055488" |
| is\_quote\_status | Boolean | Indicates whether this is a Quoted Tweet. Example:<br><br>"is\_quote\_status":false |
| quoted\_status | Tweet | This field only surfaces when the Tweet is a quote Tweet. This attribute contains the Tweet object of the original Tweet that was quoted. |
| retweeted\_status | Tweet | Users can amplify the broadcast of Tweets authored by other users by [retweeting](https://developer.twitter.com/rest/reference/post/statuses/retweet/%3Aid) . Retweets can be distinguished from typical Tweets by the existence of a `retweeted_status` attribute. This attribute contains a representation of the _original_ Tweet that was retweeted. Note that retweets of retweets do not show representations of the intermediary retweet, but only the original Tweet. (Users can also [unretweet](https://developer.twitter.com/rest/reference/post/statuses/destroy/%3Aid) a retweet they created by deleting their retweet.) |
| quote\_count | Integer | _Nullable._ Indicates approximately how many times this Tweet has been quoted by Twitter users. Example:<br><br>"quote\_count":33<br><br>Note: This object is only available with the Premium and Enterprise tier products. |
| reply\_count | Int | Number of times this Tweet has been replied to. Example:<br><br>"reply\_count":30<br><br>Note: This object is only available with the Premium and Enterprise tier products. |
| retweet\_count | Int | Number of times this Tweet has been retweeted. Example:<br><br>"retweet\_count":160 |
| favorite\_count | Integer | _Nullable._ Indicates approximately how many times this Tweet has been [liked](https://developer.twitter.com/rest/reference/post/favorites/create) by Twitter users. Example:<br><br>"favorite\_count":295 |
| entities | [Entities](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/entities-object) | Entities which have been parsed out of the text of the Tweet. Additionally see [Entities in Twitter Objects](https://developer.twitter.com/overview/api/entities-in-twitter-objects) . Example:<br><br>"entities":<br>{<br>    "hashtags":\[\],<br>    "urls":\[\],<br>    "user\_mentions":\[\],<br>    "media":\[\],<br>    "symbols":\[\]<br>    "polls":\[\]<br>} |
| extended\_entities | [Extended Entities](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/entities-object) | When between one and four native photos or one video or one animated GIF are in Tweet, contains an array 'media' metadata. This is also available in Quote Tweets. Additionally see [Entities in Twitter Objects](https://developer.twitter.com/overview/api/entities-in-twitter-objects) . Example:<br><br>"entities":<br>{<br>    "media":\[\]<br>} |
| favorited | Boolean | _Nullable._ Indicates whether this Tweet has been liked by the authenticating user. Example:<br><br>"favorited":true |
| retweeted | Boolean | Indicates whether this Tweet has been Retweeted by the authenticating user. Example:<br><br>"retweeted":false |
| possibly\_sensitive | Boolean | _Nullable._ This field indicates content may be recognized as sensitive. The Tweet author can select within their own account preferences and choose “Mark media you tweet as having material that may be sensitive” so each Tweet created after has this flag set.<br><br>This may also be judged and labeled by an internal Twitter support agent.<br><br>"possibly\_sensitive":false |
| filter\_level | String | Indicates the maximum value of the [filter\_level](https://developer.twitter.com/streaming/overview/request-parameters#filter_level) parameter which may be used and still stream this Tweet. So a value of `medium` will be streamed on `none`, `low`, and `medium` streams.<br><br>Example:<br><br>"filter\_level": "low" |
| lang | String | _Nullable._ When present, indicates a [BCP 47](http://tools.ietf.org/html/bcp47) language identifier corresponding to the machine-detected language of the Tweet text, or `und` if no language could be detected. See more documentation [HERE](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/filter-realtime/guides/premium-operators). Example:<br><br>"lang": "en" |
| matching\_rules | Array of Rule Objects | Present in _filtered_ products such as Twitter Search and PowerTrack. Provides the _id_ and _tag_ associated with the rule that matched the Tweet. With PowerTrack, more than one rule can match a Tweet. See more documentation [HERE](http://support.gnip.com/enrichments/matching_rules.html). Example:<br><br>"matching\_rules": " \[{<br>        "tag": "twitterapi emojis",<br>        "id": 1050118621198921728,<br>        "id\_str": "1050118621198921728"<br>    }\]" |

### Additional Tweet attributes

Twitter APIs that provide Tweets (e.g. the GET statuses/lookup endpoint) may include these additional Tweet attributes:

| Attribute | Type | Description |
| --- | --- | --- |
| current\_user\_retweet | Object | _Perspectival_ Only surfaces on methods supporting the include\_my\_retweet parameter, when set to true. Details the Tweet ID of the user’s own retweet (if existent) of this Tweet. Example:<br><br>"current\_user\_retweet": {<br>  "id": 6253282,<br>  "id\_str": "6253282"<br>} |
| scopes | Object | A set of key-value pairs indicating the intended contextual delivery of the containing Tweet. Currently used by Twitter’s Promoted Products. Example:<br><br>"scopes":{"followers":false} |
| withheld\_copyright | Boolean | When present and set to “true”, it indicates that this piece of content has been withheld due to a [DMCA complaint](http://en.wikipedia.org/wiki/Digital_Millennium_Copyright_Act) . Example:<br><br>"withheld\_copyright": true |
| withheld\_in\_countries | Array of String | When present, indicates a list of uppercase [two-letter country codes](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) this content is withheld from. Twitter supports the following non-country values for this field:<br><br>“XX” - Content is withheld in all countries “XY” - Content is withheld due to a DMCA request.<br><br>Example:<br><br>"withheld\_in\_countries": \["GR", "HK", "MY"\] |
| withheld\_scope | String | When present, indicates whether the content being withheld is the “status” or a “user.”<br><br>Example:<br><br>"withheld\_scope": "status" |

### Deprecated Attributes

|     |     |     |
| --- | --- | --- |
| Field | Type | Description |
| geo | Object | **Deprecated.** _Nullable._ Use the `coordinates` field instead. This deprecated attribute has its coordinates formatted as _\[lat, long\]_, while all other Tweet geo is formatted as _\[long, lat\]_. |

### Next Steps

Explore the other sub-objects that a Tweet contains:

* [User object and data dictionary](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object)
* [Entities object and data dictionary](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/entities-object)  
    
* [Extended Entities object and data dictionary](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/extended-entities-object)
* [Tweet geo objects and data dictionaries](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/geo-objects)

User object

User object
-----------

The User object contains Twitter User account metadata that describes the Twitter User referenced. Users can author Tweets, Retweet, quote other Users Tweets, reply to Tweets, follow Users, be @mentioned in Tweets and can be grouped into lists.

  

The Tweet object will also contain User objects of the Users involved within a Tweet.  In case of Retweets and Quoted Tweets, the top-level `user` object represents what account took that action, and the JSON payload will include a second `user` within the `retweeted_status` for the account that created the original Tweet.  User objects can be retireved using the `id` or `screen_name`.  

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In general these `user` metadata values are relatively constant. Some fields never change, such as the user's `id` (provided as a string `id_str`) and when the account was created. Other metadata can occasionally change, such as the `screen_name`, display`name`, `description`, `location`, and other profile details. Some metadata frequently changes, such as the number of Tweets the account has posted `statuses_count` and its number of followers `followers_count`.  
 

### User Data Dictionary

| Attribute | Type | Description |
| --- | --- | --- |
| id  | Int64 | The integer representation of the unique identifier for this User. This number is greater than 53 bits and some programming languages may have difficulty/silent defects in interpreting it. Using a signed 64 bit integer for storing this identifier is safe. Use `id_str` to fetch the identifier to be safe. See [Twitter IDs](https://developer.twitter.com/en/docs/twitter-ids) for more information. Example:<br><br>"id": 6253282 |
| id\_str | String | The string representation of the unique identifier for this User. Implementations should use this rather than the large, possibly un-consumable integer in `id`. Example:<br><br>"id\_str": "6253282" |
| name | String | The name of the user, as they’ve defined it. Not necessarily a person’s name. Typically capped at 50 characters, but subject to change. Example:<br><br>"name": "Twitter API" |
| screen\_name | String | The screen name, handle, or alias that this user identifies themselves with. screen\_names are unique but subject to change. Use `id_str` as a user identifier whenever possible. Typically a maximum of 15 characters long, but some historical accounts may exist with longer names. Example:<br><br>"screen\_name": "twitterapi" |
| location | String | _Nullable_ . The user-defined location for this account’s profile. Not necessarily a location, nor machine-parseable. This field will occasionally be fuzzily interpreted by the Search service. Example:<br><br>"location": "San Francisco, CA" |
| derived | Arrays of Enrichment Objects | Enterprise APIs only Collection of Enrichment metadata derived for user. Provides the [_Profile Geo_](https://developer.twitter.com/content/developer-twitter/en/docs/tweets/enrichments/overview/profile-geo) Enrichment metadata. See referenced documentation for more information, including JSON data dictionaries. Example:<br><br>"derived":{"locations": \[{"country":"United States","country\_code":"US","locality":"Denver"}\]} |
| url | String | _Nullable_ . A URL provided by the user in association with their profile. Example:<br><br>"url": "https://developer.twitter.com" |
| description | String | _Nullable_ . The user-defined UTF-8 string describing their account. Example:<br><br>"description": "The Real Twitter API." |
| protected | Boolean | When true, indicates that this user has chosen to protect their Tweets. See [About Public and Protected Tweets](https://support.twitter.com/articles/14016-about-public-and-protected-tweets) . Example:<br><br>"protected": true |
| verified | Boolean | When true, indicates that the user has a verified account. See [Verified Accounts](https://support.twitter.com/articles/119135-faqs-about-verified-accounts) . Example:<br><br>"verified": false |
| followers\_count | Int | The number of followers this account currently has. Under certain conditions of duress, this field will temporarily indicate “0”. Example:<br><br>"followers\_count": 21 |
| friends\_count | Int | The number of users this account is following (AKA their “followings”). Under certain conditions of duress, this field will temporarily indicate “0”. Example:<br><br>"friends\_count": 32 |
| listed\_count | Int | The number of public lists that this user is a member of. Example:<br><br>"listed\_count": 9274 |
| favourites\_count | Int | The number of Tweets this user has liked in the account’s lifetime. British spelling used in the field name for historical reasons. Example:<br><br>"favourites\_count": 13 |
| statuses\_count | Int | The number of Tweets (including retweets) issued by the user. Example:<br><br>"statuses\_count": 42 |
| created\_at | String | The UTC datetime that the user account was created on Twitter. Example:<br><br>"created\_at": "Mon Nov 29 21:18:15 +0000 2010" |
| profile\_banner\_url | String | The HTTPS-based URL pointing to the standard web representation of the user’s uploaded profile banner. By adding a final path element of the URL, it is possible to obtain different image sizes optimized for specific displays. For size variants, please see [User Profile Images and Banners](https://developer.twitter.com/en/docs/accounts-and-users/user-profile-images-and-banners) .<br><br>Example:<br><br>"profile\_banner\_url": "https://si0.twimg.com/profile\_banners/819797/1348102824" |
| profile\_image\_url\_https | String | A HTTPS-based URL pointing to the user’s profile image. Example:<br><br>"profile\_image\_url\_https":<br>"https://abs.twimg.com/sticky/default\_profile\_images/default\_profile\_normal.png" |
| default\_profile | Boolean | When true, indicates that the user has not altered the theme or background of their user profile. Example:<br><br>"default\_profile": false |
| default\_profile\_image | Boolean | When true, indicates that the user has not uploaded their own profile image and a default image is used instead. Example:<br><br>"default\_profile\_image": false |
| withheld\_in\_countries | Array of String | When present, indicates a list of uppercase [two-letter country codes](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) this content is withheld from. Twitter supports the following non-country values for this field:<br><br>“XX” - Content is withheld in all countries “XY” - Content is withheld due to a DMCA request.<br><br>Example:<br><br>"withheld\_in\_countries": \["GR", "HK", "MY"\] |
| withheld\_scope | String | When present, indicates that the content being withheld is a “user.”<br><br>Example:<br><br>"withheld\_scope": "user" |

###   
No longer supported (deprecated) attributes

| Field | Type | Description |
| --- | --- | --- |
| utc\_offset | null | Value will be set to null. Still available via [GET account/settings](https://developer.twitter.com/en/docs/accounts-and-users/manage-account-settings/api-reference/get-account-settings) |
| time\_zone | null | Value will be set to null. Still available via [GET account/settings](https://developer.twitter.com/en/docs/accounts-and-users/manage-account-settings/api-reference/get-account-settings) as tzinfo\_name |
| lang | null | Value will be set to null. Still available via [GET account/settings](https://developer.twitter.com/en/docs/accounts-and-users/manage-account-settings/api-reference/get-account-settings) as language |
| geo\_enabled | null | Value will be set to null.  Still available via [GET account/settings](https://developer.twitter.com/en/docs/accounts-and-users/manage-account-settings/api-reference/get-account-settings). This field must be true for the current user to attach geographic data when using [POST statuses / update](https://developer.twitter.com/en/docs/tweets/post-and-engage/guides/post-tweet-geo-guide) |
| following | null | Value will be set to null. Still available via [GET friendships/lookup](https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-friendships-lookup) |
| follow\_request\_sent | null | Value will be set to null. Still available via [GET friendships/lookup](https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-friendships-lookup) |
| has\_extended\_profile | null | **Deprecated**. Value will be set to null. |
| notifications | null | **Deprecated**. Value will be set to null. |
| profile\_location | null | **Deprecated**. Value will be set to null. |
| contributors\_enabled | null | **Deprecated**. Value will be set to null. |
| profile\_image\_url | null | **Deprecated**. Value will be set to null. NOTE: Profile images are only available using the profile\_image\_url\_https field. |
| profile\_background\_color | null | **Deprecated**. Value will be set to null. |
| profile\_background\_image\_url | null | **Deprecated**. Value will be set to null. |
| profile\_background\_image\_url\_https | null | **Deprecated**. Value will be set to null. |
| profile\_background\_tile | null | **Deprecated**. Value will be set to null. |
| profile\_link\_color | null | **Deprecated**. Value will be set to null. |
| profile\_sidebar\_border\_color | null | **Deprecated**. Value will be set to null. |
| profile\_sidebar\_fill\_color | null | **Deprecated**. Value will be set to null. |
| profile\_text\_color | null | **Deprecated**. Value will be set to null. |
| profile\_use\_background\_image | null | **Deprecated**. Value will be set to null. |
| is\_translator | null | **Deprecated**. Value will be set to null. |
| is\_translation\_enabled | null | **Deprecated**. Value will be set to null. |
| translator\_type | null | **Deprecated**. Value will be set to null. |

###   
Example user object:

      `{ 	"id": 6253282, 	"id_str": "6253282", 	"name": "Twitter API", 	"screen_name": "TwitterAPI", 	"location": "San Francisco, CA", 	"profile_location": null, 	"description": "The Real Twitter API. Tweets about API changes, service issues and our Developer Platform. Don't get an answer? It's on my website.", 	"url": "https:\/\/t.co\/8IkCzCDr19", 	"entities": { 		"url": { 			"urls": [{ 				"url": "https:\/\/t.co\/8IkCzCDr19", 				"expanded_url": "https:\/\/developer.twitter.com", 				"display_url": "developer.twitter.com", 				"indices": [ 					0, 					23 				] 			}] 		}, 		"description": { 			"urls": [] 		} 	}, 	"protected": false, 	"followers_count": 6133636, 	"friends_count": 12, 	"listed_count": 12936, 	"created_at": "Wed May 23 06:01:13 +0000 2007", 	"favourites_count": 31, 	"utc_offset": null, 	"time_zone": null, 	"geo_enabled": null, 	"verified": true, 	"statuses_count": 3656, 	"lang": null, 	"contributors_enabled": null, 	"is_translator": null, 	"is_translation_enabled": null, 	"profile_background_color": null, 	"profile_background_image_url": null, 	"profile_background_image_url_https": null, 	"profile_background_tile": null, 	"profile_image_url": null, 	"profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/942858479592554497\/BbazLO9L_normal.jpg", 	"profile_banner_url": null, 	"profile_link_color": null, 	"profile_sidebar_border_color": null, 	"profile_sidebar_fill_color": null, 	"profile_text_color": null, 	"profile_use_background_image": null, 	"has_extended_profile": null, 	"default_profile": false, 	"default_profile_image": false, 	"following": null, 	"follow_request_sent": null, 	"notifications": null, 	"translator_type": null }`
    

### Next Steps

Explore the other sub-objects that a Tweet contains:

* [Tweet object and data dictionary](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object.html)
* [Entities object and data dictionary](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/entities-object.html)
* [Extended Entities object and data dictionary](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/extended-entities-object.html)
* [Tweet geo objects and data dictionaries](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/geo-objects.html)

Geo objects

Tweet Location Metadata
=======================

Jump to on this page

[Introduction](#intro)

[Place object](#place)

[Coordinates object](#coordinates)

[Tweet with Twitter Place](#tweet-place)

[Tweet with exact location](#tweet-exact)

[Next steps](#next)

Introduction
------------

Tweets can be associated with a location, generating a Tweet that has been ‘geo-tagged.’ Tweet locations can be assigned by using the Twitter user-interface or when posting a Tweet using the API. Tweet locations can be an exact ‘point’ location, or a Twitter Place with a ‘bounding box’ that describes a larger area ranging from a venue to an entire region.

There are two ‘root-level’ JSON objects used to describe the location associated with a Tweet: `coordinates` and `place`.

    {
       "coordinates": {}, 
       "place": {}
    }

The `place` object is always present when a Tweet is geo-tagged, while the `coordinates` object is only present (non-null) when the Tweet is assigned an _exact location_. If an exact location is provided, the `coordinates` object will provide a \[long, lat\] array with the geographical coordinates, and a Twitter Place that corresponds to that location will be assigned.

Place object
------------

Places are specific, named locations with corresponding geo coordinates. When users decide to assign a location to their Tweet, they are presented with a list of candidate Twitter Places. When using the API to post a Tweet, a Twitter Place can be attached by specifying a **place\_id** when posting the Tweet. Tweets associated with Places are not necessarily issued from that location but could also potentially be _about_ that location.

Place data dictionary
---------------------

| Field | Type | Description |
| --- | --- | --- |
| id  | String | ID representing this place. Note that this is represented as a string, not an integer. Example:<br><br>"id":"01a9a39529b27f36" |
| url | String | URL representing the location of additional place metadata for this place. Example:<br><br>"url":"https://api.twitter.com/1.1/geo/id/01a9a39529b27f36.json" |
| place\_type | String | The type of location represented by this place. Example:<br><br>"place\_type":"city" |
| name | String | Short human-readable representation of the place’s name. Example:<br><br>"name":"Manhattan" |
| full\_name | String | Full human-readable representation of the place’s name. Example:<br><br>"full\_name":"Manhattan, NY" |
| country\_code | String | Shortened country code representing the country containing this place. Example:<br><br>"country\_code":"US" |
| country | String | Name of the country containing this place. Example:<br><br>"country":"United States" |
| bounding\_box | [Object](#obj-boundingbox) | A bounding box of coordinates which encloses this place. Example:<br><br>{<br>  "bounding\_box": {<br>    "coordinates": \[<br>      \[<br>        \[<br>          -74.026675,<br>          40.683935<br>        \],<br>        \[<br>          -74.026675,<br>          40.877483<br>        \],<br>        \[<br>          -73.910408,<br>          40.877483<br>        \],<br>        \[<br>          -73.910408,<br>          40.3935<br>        \]<br>      \]<br>    \],<br>    "type": "Polygon"<br>  }<br>} |
| attributes | Object | When using PowerTrack, 30-Day and Full-Archive Search APIs, and Volume Streams this hash is null. Example:<br><br>"attributes": {} |

### Bounding box[](#bounding-box "Permalink to this headline")

|     |     |     |
| --- | --- | --- |
| Field | Type | Description |
| coordinates | Array of Array of Array of Float | A series of longitude and latitude points, defining a box which will contain the Place entity this bounding box is related to. Each point is an array in the form of \[longitude, latitude\]. Points are grouped into an array per bounding box. Bounding box arrays are wrapped in one additional array to be compatible with the polygon notation. Example:<br><br>{<br>  "coordinates": \[<br>    \[<br>      \[<br>        -74.026675,<br>        40.683935<br>      \],<br>      \[<br>        -74.026675,<br>        40.877483<br>      \],<br>      \[<br>        -73.910408,<br>        40.877483<br>      \],<br>      \[<br>        -73.910408,<br>        40.3935<br>      \]<br>    \]<br>  \]<br>} |
| type | String | The type of data encoded in the coordinates property. This will be “Polygon” for bounding boxes and “Point” for Tweets with exact coordinates. Example:<br><br>"type":"Polygon" |

Coordinates object data dictionary
----------------------------------

|     |     |     |
| --- | --- | --- |
| Field | Type | Description |
| coordinates | Collection of Float | The longitude and latitude of the Tweet’s location, as a collection in the form **\[longitude, latitude\]**. Example:<br><br>"coordinates":\[-97.51087576,35.46500176\] |
| type | String | The type of data encoded in the coordinates property. This will be “Point” for Tweet coordinates fields. Example:<br><br>"type": "Point" |

JSON examples for geo-referenced Tweets
---------------------------------------

### Tweet with Twitter Place

    {
      "geo": null,
      "coordinates": null,
      "place": {
        "id": "07d9db48bc083000",
        "url": "https://api.twitter.com/1.1/geo/id/07d9db48bc083000.json",
        "place_type": "poi",
        "name": "McIntosh Lake",
        "full_name": "McIntosh Lake",
        "country_code": "US",
        "country": "United States",
        "bounding_box": {
          "type": "Polygon",
          "coordinates": [
            [
              [
                -105.14544,
                40.192138
              ],
              [
                -105.14544,
                40.192138
              ],
              [
                -105.14544,
                40.192138
              ],
              [
                -105.14544,
                40.192138
              ]
            ]
          ]
        },
        "attributes": {
          
        }
      }
    }
    

### Tweet with exact location

    {
      "geo": {
        "type": "Point",
        "coordinates": [
          40.74118764,
          -73.9998279
        ]
      },
      "coordinates": {
        "type": "Point",
        "coordinates": [
          -73.9998279,
          40.74118764
        ]
      },
      "place": {
        "id": "01a9a39529b27f36",
        "url": "https://api.twitter.com/1.1/geo/id/01a9a39529b27f36.json",
        "place_type": "city",
        "name": "Manhattan",
        "full_name": "Manhattan, NY",
        "country_code": "US",
        "country": "United States",
        "bounding_box": {
          "type": "Polygon",
          "coordinates": [
            [
              [
                -74.026675,
                40.683935
              ],
              [
                -74.026675,
                40.877483
              ],
              [
                -73.910408,
                40.877483
              ],
              [
                -73.910408,
                40.683935
              ]
            ]
          ]
        },
        "attributes": {
          
        }
      }
    }
    

Next steps
----------

Explore other Tweet JSON objects and data dictionaries:

* [Tweet object and data dictionary](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object)
* [User object and data dictionary](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object)
* [Entities object and data dictionary](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/entities-object)
* [Extended Entitites object and data dictionary](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/extended-entities-object)

Read more about Tweets and their location metadata:

* [Introduction to Tweet geospatial metadata](https://developer.twitter.com/en/docs/tutorials/tweet-geo-metadata) 
* [Filtering Twitter data by location](https://developer.twitter.com/en/docs/tutorials/filtering-tweets-by-location)

Entities object

Twitter entities  
------------------

Jump to on this page

[Introduction](#intro)

[Entities object](#entitiesobject)

  - [Hashtag object](#hashtags)

  - [Media object](#media)  

  - [Media size object](#media-size)  

  - [URL object](#urls)

  - [User mention object](#mentions)

  - [Symbol object](#symbols)

  - [Poll object](#polls)

[Retweet and Quote Tweet details](#retweets-quotes)

[Entities in user objects](#entities-user)

[Entities in Direct Messages](#entities-dm)

[Next Steps](#next)  

Introduction
------------

Entities provide metadata and additional contextual information about content posted on Twitter. The `entities` section provides arrays of common things included in Tweets: hashtags, user mentions, links, stock tickers (symbols), Twitter polls, and attached media. These arrays are convenient for developers when ingesting Tweets, since Twitter has essentially pre-processed, or pre-parsed, the text body. Instead of needing to explicitly search and find these entities in the Tweet body, your parser can go straight to this JSON section and there they are.

Beyond providing parsing conveniences, the `entities` section also provides useful ‘value-add’ metadata. For example, if you are using the [Enhanced URLs enrichment](https://developer.twitter.com/en/docs/tweets/enrichments/overview/expanded-and-enhanced-urls), URL metadata include fully-expanded URLs, as well as associated website titles and descriptions. Another example is when there are user mentions, the entities metadata include the numeric user ID, which are useful when making requests to many Twitter APIs.

Every Tweet JSON payload includes an `entities` section, with the minimum set of `hashtags`, `urls`, `user_mentions`, and `symbols` attributes, even if none of those entities are part of the Tweet message. For example, if you examine the JSON for a Tweet with a body of “Hello World!” and no attached media, the Tweet’s JSON will include the following content with entity arrays containing zero items:

    "entities": {
        "hashtags": [
        ],
        "urls": [
        ],
        "user_mentions": [
        ],
        "symbols": [
        ]
      }

Notes:

* media and polls entities will only appear when that type of content is part of the Tweet.
* if you are working with native media (photos, videos, or GIFs), the [Extended Entities object](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/extended-entities-object) is the way to go.

Entities object
---------------

The `entities` and `extended_entities` sections are both made up of arrays of entity _objects_. Below you will find descriptions for each of these entity objects, including data dictionaries that describe the object attribute names, types, and short description. We’ll also indicate which PowerTrack Operators match these attributes, and include some sample JSON payloads.

A collection of common entities found in Tweets, including hashtags, links, and user mentions. This `entities` object does include a `media` attribute, but its implementation in the `entiites` section is only completely accurate for Tweets with a single photo. For all Tweets with more than one photo, a video, or animated GIF, the reader is directed to the `extended_entities` section.

### Entities data dictionary

The entities object is a holder of arrays of other entity sub-objects. After illustrating the `entities` structure, data dictionaries for these sub-objects, and the Operators that match them, will be provided.

| Field | Type | Description |
| --- | --- | --- |
| hashtags | Array of [Hashtag Objects](#hashtags) | Represents hashtags which have been parsed out of the Tweet text. Example:<br><br>{<br>  "hashtags": \[<br>    {<br>      "indices": \[<br>        32,<br>        38<br>      \],<br>      "text": "nodejs"<br>    }<br>  \]<br>} |
| media | Array of [Media Objects](#media) | Represents media elements uploaded with the Tweet. Example:<br><br>{<br>  "media": \[<br>    {<br>      "display\_url": "pic.twitter.com/5J1WJSRCy9",<br>      "expanded\_url": "https://twitter.com/nolan\_test/status/930077847535812610/photo/1",<br>      "id": 9.300778475358126e17,<br>      "id\_str": "930077847535812610",<br>      "indices": \[<br>          13,<br>          36<br>      \],<br>      "media\_url": "http://pbs.twimg.com/media/DOhM30VVwAEpIHq.jpg",<br>      "media\_url\_https": "https://pbs.twimg.com/media/DOhM30VVwAEpIHq.jpg"<br>      "sizes": {<br>          "thumb": {<br>               "h": 150,<br>               "resize": "crop",<br>               "w": 150<br>          },<br>          "large": {<br>              "h": 1366,<br>              "resize": "fit",<br>              "w": 2048<br>          },<br>          "medium": {<br>              "h": 800,<br>              "resize": "fit",<br>              "w": 1200<br>          },<br>          "small": {<br>              "h": 454,<br>              "resize": "fit",<br>              "w": 680<br>          }<br>      },<br>      "type": "photo",      <br>      "url": "https://t.co/5J1WJSRCy9",<br>    }<br>  \]<br>} |
| urls | Array of [URL Objects](#urls) | Represents URLs included in the text of a Tweet.<br><br>Example (without Enhanced URLs enrichment enabled):<br><br>{<br>  "urls": \[<br>    {<br>      "indices": \[<br>        32,<br>        52<br>      \],<br>      "url": "http://t.co/IOwBrTZR",<br>      "display\_url": "youtube.com/watch?v=oHg5SJ…",<br>      "expanded\_url": "http://www.youtube.com/watch?v=oHg5SJYRHA0"<br>    }<br>  \]<br>}<br><br>Example (with Enhanced URLs enrichment enabled):<br><br>{"urls": \[<br>      {<br>        "url": "https://t.co/D0n7a53c2l",<br>        "expanded\_url": "http://bit.ly/18gECvy",<br>        "display\_url": "bit.ly/18gECvy",<br>        "unwound": {<br>          "url": "https://www.youtube.com/watch?v=oHg5SJYRHA0",<br>          "status": 200,<br>          "title": "RickRoll'D",<br>          "description": "http://www.facebook.com/rickroll548 As long as trolls are still trolling, the Rick will never stop rolling."<br>        },<br>        "indices": \[<br>          62,<br>          85<br>        \]<br>      }<br>    \]<br>} |
| user\_mentions | Array of [User Mention Objects](#mentions) | Represents other Twitter users mentioned in the text of the Tweet. Example:<br><br>{<br>  "user\_mentions": \[<br>    {<br>      "name": "Twitter API",<br>      "indices": \[<br>        4,<br>        15<br>      \],<br>      "screen\_name": "twitterapi",<br>      "id": 6253282,<br>      "id\_str": "6253282"<br>    }<br>  \]<br>} |
| symbols | Array of [Symbol Objects](#symbols) | Represents symbols, i.e. $cashtags, included in the text of the Tweet. Example:<br><br>{<br>  "symbols": \[<br>    {<br>      "indices": \[<br>        12,<br>        17<br>      \],<br>      "text": "twtr"<br>    }<br>  \]<br>} |
| polls | Array of [Poll Objects](#polls) | Represents Twitter Polls included in the Tweet. Example:<br><br>{"polls": \[<br>      {<br>        "options": \[<br>          {<br>            "position": 1,<br>            "text": "I read documentation once."<br>          },<br>          {<br>            "position": 2,<br>            "text": "I read documentation twice."<br>          },<br>          {<br>            "position": 3,<br>            "text": "I read documentation over and over again."<br>          }<br>        \],<br>        "end\_datetime": "Thu May 25 22:20:27 +0000 2017",<br>        "duration\_minutes": 60<br>      }<br>    \]<br>  } |

### Hashtag object  

The `entities` section will contain a `hashtags` array containing an object for every hashtag included in the Tweet body, and include an empty array if no hashtags are present.

The PowerTrack `#` Operator is used to match on the `text` attribute. The `has:hashtags` Operator will match if there is at least one item in the array.

|     |     |     |
| --- | --- | --- |
| Field | Type | Description |
| indices | Array of Int | An array of integers indicating the offsets within the Tweet text where the hashtag begins and ends. The first integer represents the location of the # character in the Tweet text string. The second integer represents the location of the first character after the hashtag. Therefore the difference between the two numbers will be the length of the hashtag name plus one (for the ‘#’ character). Example:<br><br>"indices":\[32,38\] |
| text | String | Name of the hashtag, minus the leading ‘#’ character. Example:<br><br>"text":"nodejs" |

### Media object  

The `entities` section will contain a `media` array containing a single media object if any media object has been ‘attached’ to the Tweet. If no native media has been attached, there will be no `media` array in the `entities`. For the following reasons the `extended_entities` section should be used to process Tweet native media:  
\+ Media `type` will always indicate ‘photo’ even in cases of a video and GIF being attached to Tweet.  
\+ Even though up to four photos can be attached, only the first one will be listed in the `entities` section.

The `has:media` Operator will match if this array is populated.

|     |     |     |
| --- | --- | --- |
| Field | Type | Description |
| display\_url | String | URL of the media to display to clients. Example:<br><br>"display\_url":"pic.twitter.com/rJC5Pxsu" |
| expanded\_url | String | An expanded version of display\_url. Links to the media display page. Example:<br><br>"expanded\_url": "http://twitter.com/yunorno/status/114080493036773378/photo/1" |
| id  | Int64 | ID of the media expressed as a 64-bit integer. Example:<br><br>"id":114080493040967680 |
| id\_str | String | ID of the media expressed as a string. Example:<br><br>"id\_str":"114080493040967680" |
| indices | Array of Int | An array of integers indicating the offsets within the Tweet text where the URL begins and ends. The first integer represents the location of the first character of the URL in the Tweet text. The second integer represents the location of the first non-URL character occurring after the URL (or the end of the string if the URL is the last part of the Tweet text). Example:<br><br>"indices":\[15,35\] |
| media\_url | String | An http:// URL pointing directly to the uploaded media file. Example:<br><br>"media\_url":"http://pbs.twimg.com/media/DOhM30VVwAEpIHq.jpg"<br><br>For media in direct messages, `media_url` is the same https URL as `media_url_https` and must be accessed by signing a request with the user’s access token using OAuth 1.0A.<br><br>It is not possible to access images via an authenticated twitter.com session. Please visit [this page](https://developer.twitter.com/en/docs/direct-messages/message-attachments/guides/retrieving-media) to learn how to account for these recent change. <br><br>You cannot directly embed these images in a web page.<br><br>See [Photo Media URL formatting](#photo_format) for how to format a photo's URL, such as `media_url_https`, based on the available `sizes`. |
| media\_url\_https | String | An https:// URL pointing directly to the uploaded media file, for embedding on https pages. Example:<br><br>"media\_url\_https":"https://p.twimg.com/AZVLmp-CIAAbkyy.jpg"<br><br>For media in direct messages, `media_url_https` must be accessed by signing a request with the user’s access token using OAuth 1.0A.<br><br>It is not possible to access images via an authenticated twitter.com session. Please visit [this page](https://developer.twitter.com/en/docs/direct-messages/message-attachments/guides/retrieving-media) to learn how to account for these recent change. <br><br>You cannot directly embed these images in a web page.<br><br>See [Photo Media URL formatting](#photo_format) for how to format a photo's URL, such as `media_url_https`, based on the available `sizes`. |
| sizes | [Size Object](#size) | An object showing available sizes for the media file. Example:<br><br>{<br>  "sizes": {<br>    "thumb": {<br>      "h": 150,<br>      "resize": "crop",<br>      "w": 150<br>    },<br>    "large": {<br>      "h": 1366,<br>      "resize": "fit",<br>      "w": 2048<br>    },<br>    "medium": {<br>      "h": 800,<br>      "resize": "fit",<br>      "w": 1200<br>    },<br>    "small": {<br>      "h": 454,<br>      "resize": "fit",<br>      "w": 680<br>    }<br>  }<br>}<br><br>See [Photo Media URL formatting](#photo_format) for how to format a photo's URL, such as `media_url_https`, based on the available `sizes`. |
| source\_status\_id | Int64 | Nullable. For Tweets containing media that was originally associated with a different tweet, this ID points to the original Tweet. Example:<br><br>"source\_status\_id": 205282515685081088 |
| source\_status\_id\_str | Int64 | Nullable. For Tweets containing media that was originally associated with a different tweet, this string-based ID points to the original Tweet. Example:<br><br>"source\_status\_id\_str": "205282515685081088" |
| type | String | Type of uploaded media. Possible types include photo, video, and animated\_gif. Example:<br><br>"type":"photo" |
| url | String | Wrapped URL for the media link. This corresponds with the URL embedded directly into the raw Tweet text, and the values for the `indices` parameter. Example:<br><br>"url":"http://t.co/rJC5Pxsu" |

### Media size objects

All Tweets with native media (photos, video, and GIFs) will include a set of ‘thumb’, ‘small’, ‘medium’, and ‘large’ sizes with height and width pixel sizes.  For photos and preview image media URLs, [Photo Media URL formatting](#photo_format) specifies how to construct different URLs for loading different sized photo media.

#### Sizes object 

|     |     |     |
| --- | --- | --- |
| Field | Type | Description |
| thumb | [Size Object](#size) | Information for a thumbnail-sized version of the media. Example:<br><br>"thumb":{"h":150, "resize":"crop", "w":150}<br><br>Thumbnail-sized photo media will be limited to _fill_ a 150x150 boundary and cropped. |
| large | [Size Object](#size) | Information for a large-sized version of the media. Example:<br><br>"large":{"h":1366, "resize":"fit", "w":2048}<br><br>Large-sized photo media will be limited to fit within a 2048x2048 boundary. |
| medium | [Size Object](#size) | Information for a medium-sized version of the media. Example:<br><br>"medium":{"h":800, "resize":"fit", "w":1200}<br><br>Medium-sized photo media will be limited to _fit_ within a 1200x1200 boundary. |
| small | [Size Object](#size) | Information for a small-sized version of the media. Example:<br><br>"small":{"h":454, "resize":"fit", "w":680}<br><br>Small-sized photo media will be limited to fit within a 680x680 boundary. |

#### Size object 

|     |     |     |
| --- | --- | --- |
| Field | Type | Description |
| w   | Int | Width in pixels of this size. Example:<br><br>"w":150 |
| h   | Int | Height in pixels of this size. Example:<br><br>"h":150 |
| resize | String | Resizing method used to obtain this size. A value of _fit_ means that the media was resized to fit one dimension, keeping its native aspect ratio. A value of _crop_ means that the media was cropped in order to fit a specific resolution. Example:<br><br>"resize":"crop" |

### Photo Media URL Formatting

Photo media on Twitter can be loaded in different sizes.  It is best to load the smallest size image that is larger enough to fit into a particular image viewport.  To load different sizes, the [Size Object](#size) and [media\_url](#media) (or [media\_url\_https](#media)) need to be combined in a particular format.  We'll use the [media entity](#entitiesobject) example object already provided for our example in constructing a photo media URL.

The `media_url` or `media_url_https` on their own can be loaded, which will result in the medium variant being loaded by default.  It is preferable, however, to provide a fully formatted photo media URL when possible.  

There are three parts of a photo media URL:

|     |     |
| --- | --- |
| Base URL | The base URL is the media URL without the file extension.<br><br>For example:  <br><br>"media\_url\_https": "https://pbs.twimg.com/media/DOhM30VVwAEpIHq.jpg",<br><br>The base URL is then:  <br><br>_https://pbs.twimg.com/media/DOhM30VVwAEpIHq_ |
| Format | The format is the type of photo the image is formatted as.  Possible formats are _jpg_ or _png_, which is provided as the extension of the media URL.<br><br>For example:  <br><br>"media\_url\_https": "https://pbs.twimg.com/media/DOhM30VVwAEpIHq.jpg",<br><br>The format is then: _jpg_ |
| Name | The name is the field name of the size to load.<br><br>For example:<br><br>{  <br> "sizes": {  <br>   "thumb": {  <br>     "h": 150,  <br>     "resize": "crop",  <br>     "w": 150  <br>   },  <br>   "large": {  <br>     "h": 1366,  <br>     "resize": "fit",  <br>     "w": 2048  <br>   },  <br>   "medium": {  <br>     "h": 800,  <br>     "resize": "fit",  <br>     "w": 1200  <br>   },  <br>   "small": {  <br>     "h": 454,  <br>     "resize": "fit",  <br>     "w": 680  <br>   }  <br> }  <br>}<br><br>The name when loading the large-sized photo would be: _large_ |

We take these three parts (base URL, format and name) and combine them into the photo media URL to load.  There are 2 formats for loading images this way, _legacy_ and _modern_.  All image loads should stop using the _legacy_ format and use the _modern_ format.  Using the _modern_ format will result in better CDN hit rate for the caller, thus improving load latencies by being less likely to have to generate and load the media from the Data Center.

|     |     |
| --- | --- |
| Legacy format | The legacy format is deprecated.  Photo media loads should all move to the modern format.<br><br>_<base\_url>.<format>:<name>_  <br><br>For example:  <br><br>_https://pbs.twimg.com/media/DOhM30VVwAEpIHq.jpg:large  <br>_ |
| Modern format | The modern format for loading photos was established at Twitter in 2015 and has been defacto since 2017.  All photo media loads should move to this format.<br><br>_<base\_url>?format=<format>&name=<name>_  <br><br>For example:  <br><br>_https://pbs.twimg.com/media/DOhM30VVwAEpIHq?format=jpg&name=large  <br>_<br><br>Note: the items in the query string for the photo media URL are in alphabetical order.  If media loading were to add any additional query items, alphabetical ordering would continue to be necessary.  For example, if there was the hypothetical new query item called _preferred\_format_, it would go after _format_ and _name_ in the query string. |

### URL object 

The `entities` section will contain a `urls` array containing an object for every link included in the Tweet body, and include an empty array if no links are present.

The `has:links` Operator will match if there is at least one item in the array. The `url:` Operator is used to match on the `expanded_url` attribute. If you are using the [Expanded URL enrichment](http://support.gnip.com/enrichments/expanded_urls.html), the `url:` Operator is used to match on the `unwound.url` (fully unwound URL) attribute. If you are using the [Enhanced URL enrichment](http://support.gnip.com/enrichments/enhanced_urls.html), the `url_title:` and `url_decription:` Operators are used to match on the `unwound.title` and `unwound.description` attributes.

|     |     |     |
| --- | --- | --- |
| Field | Type | Description |
| display\_url | String | URL pasted/typed into Tweet. Example:<br><br>"display\_url":"bit.ly/2so49n2" |
| expanded\_url | String | Expanded version of `display_url` . Example:<br><br>"expanded\_url":"http://bit.ly/2so49n2" |
| indices | Array of Int | An array of integers representing offsets within the Tweet text where the URL begins and ends. The first integer represents the location of the first character of the URL in the Tweet text. The second integer represents the location of the first non-URL character after the end of the URL. Example:<br><br>"indices":\[30,53\] |
| url | String | Wrapped URL, corresponding to the value embedded directly into the raw Tweet text, and the values for the indices parameter. Example:<br><br>"url":"https://t.co/yzocNFvJuL" |

If you are using the Expanded and/or Enhanced URL enrichments, the following metadata is available under the `unwound` attribute:

|     |     |     |
| --- | --- | --- |
| Field | Type | Description |
| url | String | The fully unwound version of the link included in the Tweet. Example:<br><br>"url":"https://blog.twitter.com/en\_us/topics/insights/2016/using-twitter-as-a-go-to-communication-channel-during-severe-weather-events.html" |
| status | Int | Final HTTP status of the unwinding process, a '200' indicating success. Example:<br><br>200 |
| title | String | HTML title for the link. Example:<br><br>"title":"Using Twitter as a ‘go-to’ communication channel during severe weather" |
| description | String | HTML description for the link. Example:<br><br>"description":"Using Twitter as a ‘go-to’ communication channel during severe weather" |

### User mention object  

The `entities` section will contain a `user_mentions` array containing an object for every user mention included in the Tweet body, and include an empty array if no user mention is present.

The PowerTrack `@` Operator is used to match on the `screen_name` attribute. The `has:mentions` Operator will match if there is at least one item in the array.

|     |     |     |
| --- | --- | --- |
| Field | Type | Description |
| id  | Int64 | ID of the mentioned user, as an integer. Example:<br><br>"id":6253282 |
| id\_str | String | If of the mentioned user, as a string. Example:<br><br>"id\_str":"6253282" |
| indices | Array of Int | An array of integers representing the offsets within the Tweet text where the user reference begins and ends. The first integer represents the location of the ‘@’ character of the user mention. The second integer represents the location of the first non-screenname character following the user mention. Example:<br><br>"indices":\[4,15\] |
| name | String | Display name of the referenced user. Example:<br><br>"name":"Twitter API" |
| screen\_name | String | Screen name of the referenced user. Example:<br><br>"screen\_name":"twitterapi" |

### Symbol object  

The `entities` section will contain a `symbols` array containing an object for every $cashtag included in the Tweet body, and include an empty array if no symbol is present.

The PowerTrack `$` Operator is used to match on the `text` attribute. The `has:symbols` Operator will match if there is at least one item in the array.

|     |     |     |
| --- | --- | --- |
| Field | Type | Description |
| indices | Array of Int | An array of integers indicating the offsets within the Tweet text where the symbol/cashtag begins and ends. The first integer represents the location of the $ character in the Tweet text string. The second integer represents the location of the first character after the cashtag. Therefore the difference between the two numbers will be the length of the hashtag name plus one (for the ‘$’ character). Example:<br><br>"indices":\[12,17\] |
| text | String | Name of the cashhtag, minus the leading ‘$’ character. Example:<br><br>"text":"twtr" |

### Poll object

The `entities` section will contain a `polls` array containing a single `poll` object if the Tweet contains a poll. If no poll is included, there will be no `polls` array in the `entities` section.

Note that these Poll metadata are only available with the following Enterprise APIs:

* Volume streams ([Decahose](https://developer.twitter.com/en/docs/tweets/sample-realtime/overview/decahose) )
* [Real-time PowerTrack](https://developer.twitter.com/en/docs/tweets/filter-realtime/overview/powertrack-api)
* [Historical PowerTrack](https://developer.twitter.com/en/docs/tweets/batch-historical/overview)
* Twitter Search APIs ([Full-Archive Search](https://developer.twitter.com/en/docs/tweets/search/overview/full-archive-search) and [30-Day Search](https://developer.twitter.com/en/docs/tweets/search/overview/30-day-search))

|     |     |     |
| --- | --- | --- |
| Field | Type | Description |
| options | Array of Option Object | An array of options, each having a poll position, and the text for that position. Example:<br><br>{"options": \[<br>          {<br>            "position": 1,<br>            "text": "I read documentation once."<br>          }<br>      \]<br>} |
| end\_datetime | String | Time stamp (UTC) of when poll ends. Example:<br><br>"end\_datetime": "Thu May 25 22:20:27 +0000 2017" |
| duration\_minutes | String | Duration of poll in minutes. Example:<br><br>"duration\_minutes": 60 |

Retweet and Quote Tweet details
-------------------------------

From the Twitter API perspective, Retweet and Quote Tweets are special kinds of Tweets that contain the original Tweet as an embedded object. So Retweets and Quote Tweet objects are parents of a child 'original' Tweet (and thus double the size). Retweets have a top-level "retweeted\_status" object, and Quoted Tweets have a "quoted\_status" object. For consistency, these top-level Retweet and Quote Tweet objects also have a text property and associated entities. However, the entities at the top level can differ from the entities provided by the embedded 'original' entities. In case of Retweets, new text is prepended to the original Tweet body. For Quoted Tweets, new text is appended to the Tweet body.

In general, the best practice is to retrieve the text, entities, original author and date from the original Tweet in retweeted\_status whenever this exists. An exception is getting Twitter entities that are part of the additive Quote. See below for more details and tips.

### Retweets  

An important detail with Retweets is that no additional Twitter _entities_ can be added to the Tweet. Users can not add hashtags, URLs or other details when they Retweet. However, the Retweet (top-level) text attribute is composed of the original Tweet text with “RT @username: ” prepended.  

In some cases, especially with accounts with long user names, the combination of these new characters and the original Tweet body can easily exceed the original Tweet text length limit of 140 characters. In order to preserve support for 140 character based display and storage, the top-level body truncates the end of the Tweet body and adds an ellipsis (“…”). Consequently, some top-level entities positioned at the end of the original Tweet might be incorrect or missing, for instance in the case of a truncated hashtag or URL entry.

This Tweet,  https://twitter.com/FloodSocial/status/907974220298125312, has the following Tweet text:

               Just another test Tweet that needs to be exactly 140 characters with trailing URL and hashtag [http://wapo.st/2w8iwPQ](https://t.co/R5iMzxWelp "http://wapo.st/2w8iwPQ")  [#Testing](https://twitter.com/hashtag/Testing?src=hash)  

In the above example, both the URL and hashtag were affected. Since the hashtag was completely truncated and the URL partially truncated, these are missing from the the top-level entities. You will also notice the additional user\_mentions top-level entity coming from the “RT @floodsocial: ” prefix on the text field.

However, the Tweet text and entities in retweeted\_status perfectly reflect the original Tweet with no truncation or incorrect entities, hence our recommendation to rely on the nested _retweeted\_status_ object for Retweets.

### Quote Tweets

Quote Tweets were introduced in 2016, and differ from Retweets in that when you "quote" a Tweet you are adding new content "on top" of a shared Tweet. This new content can include nearly anything an original Tweet can have, including new text, hashtags, mentions, and URLs.

Quote Tweets can contain native media (photos, videos, and GIFs), and will appear under the entities object.

Since Twitter entities can be added, the Quote entities are likely different from the original entities.

In this example, a new URL and hashtag were positioned at the end of the Quote Tweet.

This Tweet, https://twitter.com/FloodSocial/status/907983973225160704, has the following Tweet text:

                  strange and equally tragic when islands flood... trans-atlantic testing of quote tweets | [@thisuser](https://twitter.com/andypiper) [@thatuser](https://twitter.com/johnd) [http://bit.ly/2vMMDuu](https://t.co/fzFgMhWlPO "http://bit.ly/2vMMDuu")  [#testing](https://twitter.com/hashtag/testing?src=hash)  

In this case, the top-level entities do not reflect the Quote details. 

However, the Tweet text and entities in extended\_tweet perfectly reflect the Quote Tweet with no truncation or incorrect entities, hence our recommendation to rely on the nested _extended\_tweet_ object for Quote Tweets.

Entities for user object
------------------------

Entities for User Objects describe URLs that appear in the user defined profile URL and description fields. They do not describe hashtags or user\_mentions. Unlike Tweet entities, user entities can apply to multiple fields within its parent object — to disambiguate, you will find a parent nodes called url and description that indicate which field contains the entitized URL.

In this example, the user url field contains a t.co link that is fully expanded within the entities/url/urls\[0\] node of the response. The user does not have a wrapped URL in their description.

### JSON example

      `{   "id": 6253282,   "id_str": "6253282",   "name": "Twitter API",   "screen_name": "twitterapi",   "location": "San Francisco, CA",   "description": "The Real Twitter API. I tweet about API changes, service issues and happily answer questions about Twitter and our API. Don't get an answer? It's on my website.",   "url": "http:\/\/t.co\/78pYTvWfJd",   "entities": {     "url": {       "urls": [         {           "url": "http:\/\/t.co\/78pYTvWfJd",           "expanded_url": "http:\/\/dev.twitter.com",           "display_url": "dev.twitter.com",           "indices": [             0,             22           ]         }       ]     },     "description": {       "urls": [                ]     }   } }`
    

Entities for Direct Messages
----------------------------

Entities for Direct Messages are very similar to entities for Tweets. However, there are a few differences concerning the media entities.

Unlike media shared in Tweets, media shared in Direct Messages requires authorization to view. This authorization can be presented via an authenticated twitter.com session or by signing a request with the User’s access token using OAuth 1.0A.

Also, in Tweets, media URLs are only in the media entities, but in Direct Messages, media URLs are in both media and URLs entities.

### JSON example

      `{   "id": 411031503817039874,   "id_str": "411031503817039874",   "text": "test $TWTR @twitterapi #hashtag http:\/\/t.co\/p5dOtmnZyu https:\/\/t.co\/ZSvIEMOPb8",   "created_at": "Thu Dec 12 07:15:21 +0000 2013",   "entities": {     "hashtags": [       {         "text": "hashtag",         "indices": [           23,           31         ]       }     ],     "symbols": [       {         "text": "TWTR",         "indices": [           5,           10         ]       }     ],     "urls": [       {         "url": "http:\/\/t.co\/p5dOtmnZyu",         "expanded_url": "http:\/\/dev.twitter.com",         "display_url": "dev.twitter.com",         "indices": [           32,           54         ]       },       {         "url": "https:\/\/t.co\/ZSvIEMOPb8",         "expanded_url": "https:\/\/ton.twitter.com\/1.1\/ton\/data\/dm\/411031503817039874\/411031503833792512\/cOkcq9FS.jpg",         "display_url": "pic.twitter.com\/ZSvIEMOPb8",         "indices": [           55,           78         ]       }     ],     "user_mentions": [       {         "screen_name": "twitterapi",         "name": "Twitter API",         "id": 6253282,         "id_str": "6253282",         "indices": [           11,           22         ]       }     ],     "media": [       {         "id": 411031503833792512,         "id_str": "411031503833792512",         "indices": [           55,           78         ],         "media_url": "https:\/\/ton.twitter.com\/1.1\/ton\/data\/dm\/411031503817039874\/411031503833792512\/cOkcq9FS.jpg",         "media_url_https": "https:\/\/ton.twitter.com\/1.1\/ton\/data\/dm\/411031503817039874\/411031503833792512\/cOkcq9FS.jpg",         "url": "https:\/\/t.co\/ZSvIEMOPb8",         "display_url": "pic.twitter.com\/ZSvIEMOPb8",         "expanded_url": "https:\/\/ton.twitter.com\/1.1\/ton\/data\/dm\/411031503817039874\/411031503833792512\/cOkcq9FS.jpg",         "type": "photo",         "sizes": {           "medium": {             "w": 600,             "h": 450,             "resize": "fit"           },           "large": {             "w": 1024,             "h": 768,             "resize": "fit"           },           "thumb": {             "w": 150,             "h": 150,             "resize": "crop"           },           "small": {             "w": 340,             "h": 255,             "resize": "fit"           }         }       }     ]   } }`
    

Next steps
----------

Explore other Tweet JSON objects and data dictionaries:

* [Extended Entities object and data dictionary](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/extended-entities-object)
* [Tweet object and data dictionary](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object)
* [User object and data dictionary](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object)
* [Tweet geo objects and data dictionaries](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/geo-objects)

Extended entities object

Twitter extended entities 
--------------------------

Jump to on this page

[Introduction](#intro)

[Extended Entities object](#extended-entities-object)

[Example Tweets and JSON payloads](#example-json)

  - [Tweet with four native photos](#tweet-photos)

  - [Tweet with native video](#tweet-video)

  - [Tweet with an animated GIF](#tweet-gif)

[Next Steps](#next)

Introduction
------------

If a Tweet contains native media (shared with the Tweet user-interface as opposed via a link to elsewhere), there will also be a extended\_entities section. When it comes to any native media (photo, video, or GIF), the extended\_entities is the preferred metadata source for several reasons. Currently, up to four photos can be attached to a Tweet. The entities metadata will only contain the first photo (until 2014, only one photo could be included), while the extended\_entities section will include all attached photos. With native media, another deficiency of the entities.media metadata is that the media type will always indicate ‘photo’, even in cases where the attached media is a video or animated GIF. The actual type of media is specified in the extended\_entities.media\[\].type attribute and is set to either _photo_, _video_, or _animated\_gif_. For these reasons, if you are working with native media, the extended\_entities metadata is the way to go.

All Tweets with attached photos, videos and animated GIFs will include an `extended_entities` JSON object. The `extended_entities` object contains a single `media` array of `media` objects (see the `entities` section for its data dictionary). No other entity types, such as hashtags and links, are included in the `extended_entities` section. The `media` object in the `extended_entities` section is identical in structure to the one included in the `entities` section.  

Tweets can only have one type of media attached to it. For photos, up to four photos can be attached. For videos and GIFs, one can be attached. Since the media `type` metadata in the `extended_entities` section correctly indicates the media type (‘photo’, ‘video’ or ‘animated\_gif’), and supports up to 4 photos, it is the preferred metadata source for native media.

    {
      "extended_entities": {
        "media": [
          
        ]
      }
    }

Example Tweets and JSON payloads
--------------------------------

Below are some example Tweets and their associated entities metadata.

Tweet with four native photos

Tweet with hashtag, user mention, cashtag, URL, and four native photos:

> Test Tweet with [@mentionThis](https://twitter.com/MentionThis) [$twtr](https://twitter.com/search?q=%24twtr&src=ctag) [https://t.co/RzmrQ6wAzD](https://t.co/RzmrQ6wAzD) [#hashtag](https://twitter.com/hashtag/hashtag?src=hash) [pic.twitter.com/9r69akA484](https://t.co/9r69akA484)
> 
> — @FloodSocial (@FloodSocial) [May 8, 2017](https://twitter.com/FloodSocial/status/861627479294746624)

Here is the `entities` section for this Tweet:

    {
      "entities": {
        "hashtags": [
          {
            "text": "hashtag",
            "indices": [
              59,
              67
            ]
          }
        ],
        "urls": [
          {
            "url": "https://t.co/RzmrQ6wAzD",
            "expanded_url": "http://bit.ly/2pUk4be",
            "display_url": "bit.ly/2pUk4be",
            "unwound": {
              "url": "https://blog.gnip.com/tweeting-in-the-rain/",
              "status": 200,
              "title": "Tweeting in the Rain, Part 1 - Gnip Blog - Social Data and Data Science Blog",
              "description": "If you would have told me a few years ago that one day I’d be comparing precipitation and social media time-series data, I would have assumed you were joking.  For 13 years at OneRain I helped develop software and monitoring … Continue reading →"
            },
            "indices": [
              35,
              58
            ]
          }
        ],
        "user_mentions": [
          {
            "screen_name": "MentionThis",
            "name": "Just Me",
            "id": 50247739,
            "id_str": "50247739",
            "indices": [
              16,
              28
            ]
          }
        ],
        "symbols": [
          {
            "text": "twtr",
            "indices": [
              29,
              34
            ]
          }
        ],
        "media": [
          {
            "id": 861627472244162561,
            "id_str": "861627472244162561",
            "indices": [
              68,
              91
            ],
            "media_url": "http://pbs.twimg.com/media/C_UdnvPUwAE3Dnn.jpg",
            "media_url_https": "https://pbs.twimg.com/media/C_UdnvPUwAE3Dnn.jpg",
            "url": "https://t.co/9r69akA484",
            "display_url": "pic.twitter.com/9r69akA484",
            "expanded_url": "https://twitter.com/FloodSocial/status/861627479294746624/photo/1",
            "type": "photo",
            "sizes": {
              "medium": {
                "w": 1200,
                "h": 900,
                "resize": "fit"
              },
              "small": {
                "w": 680,
                "h": 510,
                "resize": "fit"
              },
              "thumb": {
                "w": 150,
                "h": 150,
                "resize": "crop"
              },
              "large": {
                "w": 2048,
                "h": 1536,
                "resize": "fit"
              }
            }
          }
        ]
      }
    }

Only in this ‘extended’ payload below will you find the four (maximum) native photos. Notice that the first photo in the array is the same as the single photo included in the non-extended Twitter _entities_ section. The _media_ metadata structure for photos is the same for both _entities_ and _extended\_entities_ sections.

Here is the `extented_entities` section for this Tweet:

    {
    "extended_entities": {
        "media": [
          {
            "id": 861627472244162561,
            "id_str": "861627472244162561",
            "indices": [
              68,
              91
            ],
            "media_url": "http://pbs.twimg.com/media/C_UdnvPUwAE3Dnn.jpg",
            "media_url_https": "https://pbs.twimg.com/media/C_UdnvPUwAE3Dnn.jpg",
            "url": "https://t.co/9r69akA484",
            "display_url": "pic.twitter.com/9r69akA484",
            "expanded_url": "https://twitter.com/FloodSocial/status/861627479294746624/photo/1",
            "type": "photo",
            "sizes": {
              "medium": {
                "w": 1200,
                "h": 900,
                "resize": "fit"
              },
              "small": {
                "w": 680,
                "h": 510,
                "resize": "fit"
              },
              "thumb": {
                "w": 150,
                "h": 150,
                "resize": "crop"
              },
              "large": {
                "w": 2048,
                "h": 1536,
                "resize": "fit"
              }
            }
          },
          {
            "id": 861627472244203520,
            "id_str": "861627472244203520",
            "indices": [
              68,
              91
            ],
            "media_url": "http://pbs.twimg.com/media/C_UdnvPVYAAZbEs.jpg",
            "media_url_https": "https://pbs.twimg.com/media/C_UdnvPVYAAZbEs.jpg",
            "url": "https://t.co/9r69akA484",
            "display_url": "pic.twitter.com/9r69akA484",
            "expanded_url": "https://twitter.com/FloodSocial/status/861627479294746624/photo/1",
            "type": "photo",
            "sizes": {
              "small": {
                "w": 680,
                "h": 680,
                "resize": "fit"
              },
              "thumb": {
                "w": 150,
                "h": 150,
                "resize": "crop"
              },
              "medium": {
                "w": 1200,
                "h": 1200,
                "resize": "fit"
              },
              "large": {
                "w": 2048,
                "h": 2048,
                "resize": "fit"
              }
            }
          },
          {
            "id": 861627474144149504,
            "id_str": "861627474144149504",
            "indices": [
              68,
              91
            ],
            "media_url": "http://pbs.twimg.com/media/C_Udn2UUQAADZIS.jpg",
            "media_url_https": "https://pbs.twimg.com/media/C_Udn2UUQAADZIS.jpg",
            "url": "https://t.co/9r69akA484",
            "display_url": "pic.twitter.com/9r69akA484",
            "expanded_url": "https://twitter.com/FloodSocial/status/861627479294746624/photo/1",
            "type": "photo",
            "sizes": {
              "medium": {
                "w": 1200,
                "h": 900,
                "resize": "fit"
              },
              "small": {
                "w": 680,
                "h": 510,
                "resize": "fit"
              },
              "thumb": {
                "w": 150,
                "h": 150,
                "resize": "crop"
              },
              "large": {
                "w": 2048,
                "h": 1536,
                "resize": "fit"
              }
            }
          },
          {
            "id": 861627474760708096,
            "id_str": "861627474760708096",
            "indices": [
              68,
              91
            ],
            "media_url": "http://pbs.twimg.com/media/C_Udn4nUMAAgcIa.jpg",
            "media_url_https": "https://pbs.twimg.com/media/C_Udn4nUMAAgcIa.jpg",
            "url": "https://t.co/9r69akA484",
            "display_url": "pic.twitter.com/9r69akA484",
            "expanded_url": "https://twitter.com/FloodSocial/status/861627479294746624/photo/1",
            "type": "photo",
            "sizes": {
              "small": {
                "w": 680,
                "h": 680,
                "resize": "fit"
              },
              "thumb": {
                "w": 150,
                "h": 150,
                "resize": "crop"
              },
              "medium": {
                "w": 1200,
                "h": 1200,
                "resize": "fit"
              },
              "large": {
                "w": 2048,
                "h": 2048,
                "resize": "fit"
              }
            }
          }
        ]
      }
    }

Tweet with native video
-----------------------

Below is the extended entities metadata for this Tweet with a video:

> St. Vrain River @ Crane Hollow [pic.twitter.com/TLSTTOvvmP](https://t.co/TLSTTOvvmP)
> 
> — @FloodSocial demo (@FloodSocial) [May 29, 2017](https://twitter.com/FloodSocial/status/869318041078820864)

    {
      "extended_entities": {
        "media": [
          {
            "id": 869317980307415040,
            "id_str": "869317980307415040",
            "indices": [
              31,
              54
            ],
            "media_url": "http://pbs.twimg.com/ext_tw_video_thumb/869317980307415040/pu/img/t_E6wyADk_PvxuzF.jpg",
            "media_url_https": "https://pbs.twimg.com/ext_tw_video_thumb/869317980307415040/pu/img/t_E6wyADk_PvxuzF.jpg",
            "url": "https://t.co/TLSTTOvvmP",
            "display_url": "pic.twitter.com/TLSTTOvvmP",
            "expanded_url": "https://twitter.com/FloodSocial/status/869318041078820864/video/1",
            "type": "video",
            "sizes": {
              "small": {
                "w": 340,
                "h": 604,
                "resize": "fit"
              },
              "large": {
                "w": 720,
                "h": 1280,
                "resize": "fit"
              },
              "thumb": {
                "w": 150,
                "h": 150,
                "resize": "crop"
              },
              "medium": {
                "w": 600,
                "h": 1067,
                "resize": "fit"
              }
            },
            "video_info": {
              "aspect_ratio": [
                9,
                16
              ],
              "duration_millis": 10704,
              "variants": [
                {
                  "bitrate": 320000,
                  "content_type": "video/mp4",
                  "url": "https://video.twimg.com/ext_tw_video/869317980307415040/pu/vid/180x320/FMei8yCw7yc_Z7e-.mp4"
                },
                {
                  "bitrate": 2176000,
                  "content_type": "video/mp4",
                  "url": "https://video.twimg.com/ext_tw_video/869317980307415040/pu/vid/720x1280/octt5pFbISkef8RB.mp4"
                },
                {
                  "bitrate": 832000,
                  "content_type": "video/mp4",
                  "url": "https://video.twimg.com/ext_tw_video/869317980307415040/pu/vid/360x640/2OmqK74SQ9jNX8mZ.mp4"
                },
                {
                  "content_type": "application/x-mpegURL",
                  "url": "https://video.twimg.com/ext_tw_video/869317980307415040/pu/pl/wcJQJ2nxiFU4ZZng.m3u8"
                }
              ]
            }
          }
        ]
      }
    }

When an advertiser chooses to limit video playback to just Twitter owned and operated platforms, the `video_info` object will be replaced with an `additional_media_info` object.  
  
The `additional_media_info` will contain additional media info provided by the publisher, such as `title`, `description` and `embeddable flag`. Video content is made available only to Twitter official clients when `embeddable=false`. In this case, all video URLs provided in the payload will be Twitter-based, so the user can open the video in a Twitter owned property by clicking the link.  
  
Here is an example of what the extended entities object will look like in this situation:

    {
      "extended_entities": {
        "media": [
          {
            "id": 924685332347469824,
            "id_str": "924685332347469824",
            "indices": [
              49,
              72
            ],
            "media_url": "http://pbs.twimg.com/media/DNUkdLMVwAEzj8K.jpg",
            "media_url_https": "https://pbs.twimg.com/media/DNUkdLMVwAEzj8K.jpg",
            "url": "https://t.co/90xOJqKMox",
            "display_url": "pic.twitter.com/90xOJqKMox",
            "expanded_url": "https://twitter.com/nyjets/status/924685391524798464/video/1",
            "type": "photo",
            "sizes": {
              "small": {
                "w": 680,
                "h": 383,
                "resize": "fit"
              },
              "medium": {
                "w": 1200,
                "h": 675,
                "resize": "fit"
              },
              "large": {
                "w": 1280,
                "h": 720,
                "resize": "fit"
              },
              "thumb": {
                "w": 150,
                "h": 150,
                "resize": "crop"
              }
            },
            "additional_media_info": {
              "title": "#ATLvsNYJ: Tomlinson TD from McCown",
              "description": "NFL",
              "embeddable": false,
              "monetizable": true
            }
          }
        ]
      }
    }
    

As discussed above, here is the `entities` section that incorrectly has the `type` set to ‘photo’. Again, the `extended_entities` section is preferred for all native media types, including ‘video’ and ‘animated\_gif’.

    {
    "entities": {
        "hashtags": [
          
        ],
        "urls": [
          
        ],
        "user_mentions": [
          
        ],
        "symbols": [
          
        ],
        "media": [
          {
            "id": 869317980307415040,
            "id_str": "869317980307415040",
            "indices": [
              31,
              54
            ],
            "media_url": "http://pbs.twimg.com/ext_tw_video_thumb/869317980307415040/pu/img/t_E6wyADk_PvxuzF.jpg",
            "media_url_https": "https://pbs.twimg.com/ext_tw_video_thumb/869317980307415040/pu/img/t_E6wyADk_PvxuzF.jpg",
            "url": "https://t.co/TLSTTOvvmP",
            "display_url": "pic.twitter.com/TLSTTOvvmP",
            "expanded_url": "https://twitter.com/FloodSocial/status/869318041078820864/video/1",
            "type": "photo",
            "sizes": {
              "small": {
                "w": 340,
                "h": 604,
                "resize": "fit"
              },
              "large": {
                "w": 720,
                "h": 1280,
                "resize": "fit"
              },
              "thumb": {
                "w": 150,
                "h": 150,
                "resize": "crop"
              },
              "medium": {
                "w": 600,
                "h": 1067,
                "resize": "fit"
              }
            }
          }
        ]
      }
    
    }

Tweet with an animated GIF
--------------------------

Below is the extended entities metadata for this Tweet with an animated GIF:

> Test Tweet with animated GIF [pic.twitter.com/nD6G4bWSKb](https://t.co/nD6G4bWSKb)
> 
> — @FloodSocial demo (@FloodSocial) [May 31, 2017](https://twitter.com/FloodSocial/status/870042717589340160)

    {
      "extended_entities": {
        "media": [
          {
            "id": 870042654213459968,
            "id_str": "870042654213459968",
            "indices": [
              29,
              52
            ],
            "media_url": "http://pbs.twimg.com/tweet_video_thumb/DBMDLy_U0AAqUWP.jpg",
            "media_url_https": "https://pbs.twimg.com/tweet_video_thumb/DBMDLy_U0AAqUWP.jpg",
            "url": "https://t.co/nD6G4bWSKb",
            "display_url": "pic.twitter.com/nD6G4bWSKb",
            "expanded_url": "https://twitter.com/FloodSocial/status/870042717589340160/photo/1",
            "type": "animated_gif",
            "sizes": {
              "medium": {
                "w": 350,
                "h": 262,
                "resize": "fit"
              },
              "small": {
                "w": 340,
                "h": 255,
                "resize": "fit"
              },
              "thumb": {
                "w": 150,
                "h": 150,
                "resize": "crop"
              },
              "large": {
                "w": 350,
                "h": 262,
                "resize": "fit"
              }
            },
            "video_info": {
              "aspect_ratio": [
                175,
                131
              ],
              "variants": [
                {
                  "bitrate": 0,
                  "content_type": "video/mp4",
                  "url": "https://video.twimg.com/tweet_video/DBMDLy_U0AAqUWP.mp4"
                }
              ]
            }
          }
        ]
      }
    }

Next steps
----------

Explore other Tweet JSON objects and data dictionaries:

* [Entities object and data dictionary](https://developer.twitter.com/content/developer-twitter/en/docs/tweets/data-dictionary/overview/entities-object1)
* [Tweet object and data dictionary](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object)
* [User object and data dictionary](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object)
* [Tweet geo objects and data dictionaries](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/geo-objects)

Example payloads

### Tweet

      `{   "created_at": "Fri Sep 18 18:36:15 +0000 2020",   "id": 1307025659294674945,   "id_str": "1307025659294674945",   "full_text": "Here’s an article that highlights the updates in the new Tweet payload v2 https:\/\/t.co\/oeF3ZHeKQQ",   "truncated": false,   "display_text_range": [     0,     97   ],   "entities": {     "hashtags": [],     "symbols": [],     "user_mentions": [],     "urls": [       {         "url": "https:\/\/t.co\/oeF3ZHeKQQ",         "expanded_url": "https:\/\/dev.to\/twitterdev\/understanding-the-new-tweet-payload-in-the-twitter-api-v2-1fg5",         "display_url": "dev.to\/twitterdev\/und…",         "indices": [           74,           97         ]       }     ]   },   "source": "<a href=\"https:\/\/mobile.twitter.com\" rel=\"nofollow\">Twitter Web App<\/a>",   "in_reply_to_status_id": 1304102743196356610,   "in_reply_to_status_id_str": "1304102743196356610",   "in_reply_to_user_id": 2244994945,   "in_reply_to_user_id_str": "2244994945",   "in_reply_to_screen_name": "TwitterDev",   "user": {     "id": 2244994945,     "id_str": "2244994945",     "name": "Twitter Dev",     "screen_name": "TwitterDev",     "location": "127.0.0.1",     "description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",     "url": "https:\/\/t.co\/3ZX3TNiZCY",     "entities": {       "url": {         "urls": [           {             "url": "https:\/\/t.co\/3ZX3TNiZCY",             "expanded_url": "https:\/\/developer.twitter.com\/en\/community",             "display_url": "developer.twitter.com\/en\/community",             "indices": [               0,               23             ]           }         ]       },       "description": {         "urls": []       }     },     "protected": false,     "followers_count": 513958,     "friends_count": 2039,     "listed_count": 1672,     "created_at": "Sat Dec 14 04:35:55 +0000 2013",     "favourites_count": 2145,     "utc_offset": null,     "time_zone": null,     "geo_enabled": true,     "verified": true,     "statuses_count": 3635,     "lang": null,     "contributors_enabled": false,     "is_translator": false,     "is_translation_enabled": false,     "profile_background_color": "FFFFFF",     "profile_background_image_url": "http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",     "profile_background_image_url_https": "https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",     "profile_background_tile": false,     "profile_image_url": "http:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",     "profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",     "profile_banner_url": "https:\/\/pbs.twimg.com\/profile_banners\/2244994945\/1594913664",     "profile_link_color": "0084B4",     "profile_sidebar_border_color": "FFFFFF",     "profile_sidebar_fill_color": "DDEEF6",     "profile_text_color": "333333",     "profile_use_background_image": false,     "has_extended_profile": true,     "default_profile": false,     "default_profile_image": false,     "following": null,     "follow_request_sent": null,     "notifications": null,     "translator_type": "regular"   },   "geo": null,   "coordinates": null,   "place": null,   "contributors": null,   "is_quote_status": false,   "retweet_count": 11,   "favorite_count": 70,   "favorited": false,   "retweeted": false,   "possibly_sensitive": false,   "possibly_sensitive_appealable": false,   "lang": "en" }`
    

### Tweet reply

      `{   "created_at": "Fri Aug 21 19:10:05 +0000 2020",   "id": 1296887316556980230,   "id_str": "1296887316556980230",   "text": "See how @PennMedCDH are using Twitter data to understand the COVID-19 health crisis 📊\n\nhttps:\/\/t.co\/1tdA8uDWes",   "truncated": false,   "entities": {     "hashtags": [],     "symbols": [],     "user_mentions": [       {         "screen_name": "PennMedCDH",         "name": "Penn Med CDH",         "id": 1615654896,         "id_str": "1615654896",         "indices": [           8,           19         ]       }     ],     "urls": [       {         "url": "https:\/\/t.co\/1tdA8uDWes",         "expanded_url": "https:\/\/developer.twitter.com\/en\/use-cases\/success-stories\/penn",         "display_url": "developer.twitter.com\/en\/use-cases\/s…",         "indices": [           87,           110         ]       }     ]   },   "source": "<a href=\"https:\/\/mobile.twitter.com\" rel=\"nofollow\">Twitter Web App<\/a>",   "in_reply_to_status_id": 1296887091901718529,   "in_reply_to_status_id_str": "1296887091901718529",   "in_reply_to_user_id": 2244994945,   "in_reply_to_user_id_str": "2244994945",   "in_reply_to_screen_name": "TwitterDev",   "user": {     "id": 2244994945,     "id_str": "2244994945",     "name": "Twitter Dev",     "screen_name": "TwitterDev",     "location": "127.0.0.1",     "description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",     "url": "https:\/\/t.co\/3ZX3TNiZCY",     "entities": {       "url": {         "urls": [           {             "url": "https:\/\/t.co\/3ZX3TNiZCY",             "expanded_url": "https:\/\/developer.twitter.com\/en\/community",             "display_url": "developer.twitter.com\/en\/community",             "indices": [               0,               23             ]           }         ]       },       "description": {         "urls": []       }     },     "protected": false,     "followers_count": 513958,     "friends_count": 2039,     "listed_count": 1672,     "created_at": "Sat Dec 14 04:35:55 +0000 2013",     "favourites_count": 2145,     "utc_offset": null,     "time_zone": null,     "geo_enabled": true,     "verified": true,     "statuses_count": 3635,     "lang": null,     "contributors_enabled": false,     "is_translator": false,     "is_translation_enabled": false,     "profile_background_color": "FFFFFF",     "profile_background_image_url": "http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",     "profile_background_image_url_https": "https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",     "profile_background_tile": false,     "profile_image_url": "http:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",     "profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",     "profile_banner_url": "https:\/\/pbs.twimg.com\/profile_banners\/2244994945\/1594913664",     "profile_link_color": "0084B4",     "profile_sidebar_border_color": "FFFFFF",     "profile_sidebar_fill_color": "DDEEF6",     "profile_text_color": "333333",     "profile_use_background_image": false,     "has_extended_profile": true,     "default_profile": false,     "default_profile_image": false,     "following": null,     "follow_request_sent": null,     "notifications": null,     "translator_type": "regular"   },   "geo": null,   "coordinates": null,   "place": null,   "contributors": null,   "is_quote_status": false,   "retweet_count": 9,   "favorite_count": 26,   "favorited": false,   "retweeted": false,   "possibly_sensitive": false,   "possibly_sensitive_appealable": false,   "lang": "en" }`
    

### Extended Tweet (default)

      `{   "created_at": "Wed Aug 19 16:26:16 +0000 2020",   "id": 1296121314218897408,   "id_str": "1296121314218897408",   "text": "The hide replies endpoint is launching today! \n\nDevelopers can hide replies to Tweets - a crucial way developers ca… https:\/\/t.co\/VyfXs1RTXn",   "truncated": true,   "entities": {     "hashtags": [],     "symbols": [],     "user_mentions": [],     "urls": [       {         "url": "https:\/\/t.co\/VyfXs1RTXn",         "expanded_url": "https:\/\/twitter.com\/i\/web\/status\/1296121314218897408",         "display_url": "twitter.com\/i\/web\/status\/1…",         "indices": [           117,           140         ]       }     ]   },   "source": "<a href=\"https:\/\/mobile.twitter.com\" rel=\"nofollow\">Twitter Web App<\/a>",   "in_reply_to_status_id": null,   "in_reply_to_status_id_str": null,   "in_reply_to_user_id": null,   "in_reply_to_user_id_str": null,   "in_reply_to_screen_name": null,   "user": {     "id": 2244994945,     "id_str": "2244994945",     "name": "Twitter Dev",     "screen_name": "TwitterDev",     "location": "127.0.0.1",     "description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",     "url": "https:\/\/t.co\/3ZX3TNiZCY",     "entities": {       "url": {         "urls": [           {             "url": "https:\/\/t.co\/3ZX3TNiZCY",             "expanded_url": "https:\/\/developer.twitter.com\/en\/community",             "display_url": "developer.twitter.com\/en\/community",             "indices": [               0,               23             ]           }         ]       },       "description": {         "urls": []       }     },     "protected": false,     "followers_count": 513958,     "friends_count": 2039,     "listed_count": 1672,     "created_at": "Sat Dec 14 04:35:55 +0000 2013",     "favourites_count": 2145,     "utc_offset": null,     "time_zone": null,     "geo_enabled": true,     "verified": true,     "statuses_count": 3635,     "lang": null,     "contributors_enabled": false,     "is_translator": false,     "is_translation_enabled": false,     "profile_background_color": "FFFFFF",     "profile_background_image_url": "http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",     "profile_background_image_url_https": "https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",     "profile_background_tile": false,     "profile_image_url": "http:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",     "profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",     "profile_banner_url": "https:\/\/pbs.twimg.com\/profile_banners\/2244994945\/1594913664",     "profile_link_color": "0084B4",     "profile_sidebar_border_color": "FFFFFF",     "profile_sidebar_fill_color": "DDEEF6",     "profile_text_color": "333333",     "profile_use_background_image": false,     "has_extended_profile": true,     "default_profile": false,     "default_profile_image": false,     "following": null,     "follow_request_sent": null,     "notifications": null,     "translator_type": "regular"   },   "geo": null,   "coordinates": null,   "place": null,   "contributors": null,   "is_quote_status": false,   "retweet_count": 54,   "favorite_count": 172,   "favorited": false,   "retweeted": false,   "possibly_sensitive": false,   "possibly_sensitive_appealable": false,   "lang": "en" }`
    

### Extended Tweet (with tweet\_mode=extended)

      `{   "created_at": "Wed Aug 19 16:26:16 +0000 2020",   "id": 1296121314218897408,   "id_str": "1296121314218897408",   "full_text": "The hide replies endpoint is launching today! \n\nDevelopers can hide replies to Tweets - a crucial way developers can help improve the health of the public conversation using the #TwitterAPI.\n\nhttps:\/\/t.co\/khXhTurm9x",   "truncated": false,   "display_text_range": [     0,     215   ],   "entities": {     "hashtags": [       {         "text": "TwitterAPI",         "indices": [           178,           189         ]       }     ],     "symbols": [],     "user_mentions": [],     "urls": [       {         "url": "https:\/\/t.co\/khXhTurm9x",         "expanded_url": "https:\/\/twittercommunity.com\/t\/hide-replies-now-available-in-the-new-twitter-api\/140996",         "display_url": "twittercommunity.com\/t\/hide-replies…",         "indices": [           192,           215         ]       }     ]   },   "source": "<a href=\"https:\/\/mobile.twitter.com\" rel=\"nofollow\">Twitter Web App<\/a>",   "in_reply_to_status_id": null,   "in_reply_to_status_id_str": null,   "in_reply_to_user_id": null,   "in_reply_to_user_id_str": null,   "in_reply_to_screen_name": null,   "user": {     "id": 2244994945,     "id_str": "2244994945",     "name": "Twitter Dev",     "screen_name": "TwitterDev",     "location": "127.0.0.1",     "description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",     "url": "https:\/\/t.co\/3ZX3TNiZCY",     "entities": {       "url": {         "urls": [           {             "url": "https:\/\/t.co\/3ZX3TNiZCY",             "expanded_url": "https:\/\/developer.twitter.com\/en\/community",             "display_url": "developer.twitter.com\/en\/community",             "indices": [               0,               23             ]           }         ]       },       "description": {         "urls": []       }     },     "protected": false,     "followers_count": 513958,     "friends_count": 2039,     "listed_count": 1672,     "created_at": "Sat Dec 14 04:35:55 +0000 2013",     "favourites_count": 2145,     "utc_offset": null,     "time_zone": null,     "geo_enabled": true,     "verified": true,     "statuses_count": 3635,     "lang": null,     "contributors_enabled": false,     "is_translator": false,     "is_translation_enabled": false,     "profile_background_color": "FFFFFF",     "profile_background_image_url": "http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",     "profile_background_image_url_https": "https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",     "profile_background_tile": false,     "profile_image_url": "http:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",     "profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",     "profile_banner_url": "https:\/\/pbs.twimg.com\/profile_banners\/2244994945\/1594913664",     "profile_link_color": "0084B4",     "profile_sidebar_border_color": "FFFFFF",     "profile_sidebar_fill_color": "DDEEF6",     "profile_text_color": "333333",     "profile_use_background_image": false,     "has_extended_profile": true,     "default_profile": false,     "default_profile_image": false,     "following": null,     "follow_request_sent": null,     "notifications": null,     "translator_type": "regular"   },   "geo": null,   "coordinates": null,   "place": null,   "contributors": null,   "is_quote_status": false,   "retweet_count": 54,   "favorite_count": 172,   "favorited": false,   "retweeted": false,   "possibly_sensitive": false,   "possibly_sensitive_appealable": false,   "lang": "en" }`
    

### Tweet with extended\_entities (with tweet\_mode=extended)

      `{   "created_at": "Wed Aug 12 17:01:42 +0000 2020",   "id": 1293593516040269825,   "id_str": "1293593516040269825",   "full_text": "It’s finally here! 🥁 Say hello to the new #TwitterAPI.\n\nWe’re rebuilding the Twitter API v2 from the ground up to better serve our developer community. And today’s launch is only the beginning.\n\nhttps:\/\/t.co\/32VrwpGaJw https:\/\/t.co\/KaFSbjWUA8",   "truncated": false,   "display_text_range": [     0,     218   ],   "entities": {     "hashtags": [       {         "text": "TwitterAPI",         "indices": [           42,           53         ]       }     ],     "symbols": [],     "user_mentions": [],     "urls": [       {         "url": "https:\/\/t.co\/32VrwpGaJw",         "expanded_url": "https:\/\/blog.twitter.com\/developer\/en_us\/topics\/tools\/2020\/introducing_new_twitter_api.html",         "display_url": "blog.twitter.com\/developer\/en_u…",         "indices": [           195,           218         ]       }     ],     "media": [       {         "id": 1293565706408038401,         "id_str": "1293565706408038401",         "indices": [           219,           242         ],         "media_url": "http:\/\/pbs.twimg.com\/ext_tw_video_thumb\/1293565706408038401\/pu\/img\/66P2dvbU4a02jYbV.jpg",         "media_url_https": "https:\/\/pbs.twimg.com\/ext_tw_video_thumb\/1293565706408038401\/pu\/img\/66P2dvbU4a02jYbV.jpg",         "url": "https:\/\/t.co\/KaFSbjWUA8",         "display_url": "pic.twitter.com\/KaFSbjWUA8",         "expanded_url": "https:\/\/twitter.com\/TwitterDev\/status\/1293593516040269825\/video\/1",         "type": "photo",         "sizes": {           "thumb": {             "w": 150,             "h": 150,             "resize": "crop"           },           "medium": {             "w": 1200,             "h": 675,             "resize": "fit"           },           "small": {             "w": 680,             "h": 383,             "resize": "fit"           },           "large": {             "w": 1280,             "h": 720,             "resize": "fit"           }         }       }     ]   },   "extended_entities": {     "media": [       {         "id": 1293565706408038401,         "id_str": "1293565706408038401",         "indices": [           219,           242         ],         "media_url": "http:\/\/pbs.twimg.com\/ext_tw_video_thumb\/1293565706408038401\/pu\/img\/66P2dvbU4a02jYbV.jpg",         "media_url_https": "https:\/\/pbs.twimg.com\/ext_tw_video_thumb\/1293565706408038401\/pu\/img\/66P2dvbU4a02jYbV.jpg",         "url": "https:\/\/t.co\/KaFSbjWUA8",         "display_url": "pic.twitter.com\/KaFSbjWUA8",         "expanded_url": "https:\/\/twitter.com\/TwitterDev\/status\/1293593516040269825\/video\/1",         "type": "video",         "sizes": {           "thumb": {             "w": 150,             "h": 150,             "resize": "crop"           },           "medium": {             "w": 1200,             "h": 675,             "resize": "fit"           },           "small": {             "w": 680,             "h": 383,             "resize": "fit"           },           "large": {             "w": 1280,             "h": 720,             "resize": "fit"           }         },         "video_info": {           "aspect_ratio": [             16,             9           ],           "duration_millis": 34875,           "variants": [             {               "bitrate": 256000,               "content_type": "video\/mp4",               "url": "https:\/\/video.twimg.com\/ext_tw_video\/1293565706408038401\/pu\/vid\/480x270\/Fg9lnGGsITO0uq2K.mp4?tag=10"             },             {               "bitrate": 832000,               "content_type": "video\/mp4",               "url": "https:\/\/video.twimg.com\/ext_tw_video\/1293565706408038401\/pu\/vid\/640x360\/-crbtZE4y8vKN_uF.mp4?tag=10"             },             {               "content_type": "application\/x-mpegURL",               "url": "https:\/\/video.twimg.com\/ext_tw_video\/1293565706408038401\/pu\/pl\/OvIqQojosF6sMIHR.m3u8?tag=10"             },             {               "bitrate": 2176000,               "content_type": "video\/mp4",               "url": "https:\/\/video.twimg.com\/ext_tw_video\/1293565706408038401\/pu\/vid\/1280x720\/xkxyb-VPVY4OI0j9.mp4?tag=10"             }           ]         },         "additional_media_info": {           "monetizable": false         }       }     ]   },   "source": "<a href=\"https:\/\/mobile.twitter.com\" rel=\"nofollow\">Twitter Web App<\/a>",   "in_reply_to_status_id": null,   "in_reply_to_status_id_str": null,   "in_reply_to_user_id": null,   "in_reply_to_user_id_str": null,   "in_reply_to_screen_name": null,   "user": {     "id": 2244994945,     "id_str": "2244994945",     "name": "Twitter Dev",     "screen_name": "TwitterDev",     "location": "127.0.0.1",     "description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",     "url": "https:\/\/t.co\/3ZX3TNiZCY",     "entities": {       "url": {         "urls": [           {             "url": "https:\/\/t.co\/3ZX3TNiZCY",             "expanded_url": "https:\/\/developer.twitter.com\/en\/community",             "display_url": "developer.twitter.com\/en\/community",             "indices": [               0,               23             ]           }         ]       },       "description": {         "urls": []       }     },     "protected": false,     "followers_count": 513958,     "friends_count": 2039,     "listed_count": 1672,     "created_at": "Sat Dec 14 04:35:55 +0000 2013",     "favourites_count": 2145,     "utc_offset": null,     "time_zone": null,     "geo_enabled": true,     "verified": true,     "statuses_count": 3635,     "lang": null,     "contributors_enabled": false,     "is_translator": false,     "is_translation_enabled": false,     "profile_background_color": "FFFFFF",     "profile_background_image_url": "http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",     "profile_background_image_url_https": "https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",     "profile_background_tile": false,     "profile_image_url": "http:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",     "profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",     "profile_banner_url": "https:\/\/pbs.twimg.com\/profile_banners\/2244994945\/1594913664",     "profile_link_color": "0084B4",     "profile_sidebar_border_color": "FFFFFF",     "profile_sidebar_fill_color": "DDEEF6",     "profile_text_color": "333333",     "profile_use_background_image": false,     "has_extended_profile": true,     "default_profile": false,     "default_profile_image": false,     "following": null,     "follow_request_sent": null,     "notifications": null,     "translator_type": "regular"   },   "geo": null,   "coordinates": null,   "place": null,   "contributors": null,   "is_quote_status": false,   "retweet_count": 958,   "favorite_count": 2850,   "favorited": false,   "retweeted": false,   "possibly_sensitive": false,   "possibly_sensitive_appealable": false,   "lang": "en" }`
    

### Retweet (default)

      `{   "created_at": "Tue Feb 18 19:33:59 +0000 2020",   "id": 1229851574555508737,   "id_str": "1229851574555508737",   "text": "RT @suhemparack: I built an Alexa Skill for Twitter using APL that allows you to view Tweets and Trends on the echo show!\n\nCheck it out her…",   "truncated": false,   "entities": {     "hashtags": [],     "symbols": [],     "user_mentions": [       {         "screen_name": "suhemparack",         "name": "Suhem Parack",         "id": 857699969263964161,         "id_str": "857699969263964161",         "indices": [           3,           15         ]       }     ],     "urls": []   },   "source": "<a href=\"https:\/\/mobile.twitter.com\" rel=\"nofollow\">Twitter Web App<\/a>",   "in_reply_to_status_id": null,   "in_reply_to_status_id_str": null,   "in_reply_to_user_id": null,   "in_reply_to_user_id_str": null,   "in_reply_to_screen_name": null,   "user": {     "id": 2244994945,     "id_str": "2244994945",     "name": "Twitter Dev",     "screen_name": "TwitterDev",     "location": "127.0.0.1",     "description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",     "url": "https:\/\/t.co\/3ZX3TNiZCY",     "entities": {       "url": {         "urls": [           {             "url": "https:\/\/t.co\/3ZX3TNiZCY",             "expanded_url": "https:\/\/developer.twitter.com\/en\/community",             "display_url": "developer.twitter.com\/en\/community",             "indices": [               0,               23             ]           }         ]       },       "description": {         "urls": []       }     },     "protected": false,     "followers_count": 513958,     "friends_count": 2039,     "listed_count": 1672,     "created_at": "Sat Dec 14 04:35:55 +0000 2013",     "favourites_count": 2145,     "utc_offset": null,     "time_zone": null,     "geo_enabled": true,     "verified": true,     "statuses_count": 3635,     "lang": null,     "contributors_enabled": false,     "is_translator": false,     "is_translation_enabled": false,     "profile_background_color": "FFFFFF",     "profile_background_image_url": "http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",     "profile_background_image_url_https": "https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",     "profile_background_tile": false,     "profile_image_url": "http:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",     "profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",     "profile_banner_url": "https:\/\/pbs.twimg.com\/profile_banners\/2244994945\/1594913664",     "profile_link_color": "0084B4",     "profile_sidebar_border_color": "FFFFFF",     "profile_sidebar_fill_color": "DDEEF6",     "profile_text_color": "333333",     "profile_use_background_image": false,     "has_extended_profile": true,     "default_profile": false,     "default_profile_image": false,     "following": null,     "follow_request_sent": null,     "notifications": null,     "translator_type": "regular"   },   "geo": null,   "coordinates": null,   "place": null,   "contributors": null,   "retweeted_status": {     "created_at": "Tue Feb 18 19:01:58 +0000 2020",     "id": 1229843515603144704,     "id_str": "1229843515603144704",     "text": "I built an Alexa Skill for Twitter using APL that allows you to view Tweets and Trends on the echo show!\n\nCheck it… https:\/\/t.co\/RP9NgltX7i",     "truncated": true,     "entities": {       "hashtags": [],       "symbols": [],       "user_mentions": [],       "urls": [         {           "url": "https:\/\/t.co\/RP9NgltX7i",           "expanded_url": "https:\/\/twitter.com\/i\/web\/status\/1229843515603144704",           "display_url": "twitter.com\/i\/web\/status\/1…",           "indices": [             116,             139           ]         }       ]     },     "source": "<a href=\"https:\/\/mobile.twitter.com\" rel=\"nofollow\">Twitter Web App<\/a>",     "in_reply_to_status_id": null,     "in_reply_to_status_id_str": null,     "in_reply_to_user_id": null,     "in_reply_to_user_id_str": null,     "in_reply_to_screen_name": null,     "user": {       "id": 857699969263964161,       "id_str": "857699969263964161",       "name": "Suhem Parack",       "screen_name": "suhemparack",       "location": "Seattle, WA",       "description": "Developer Relations for Academic Research @Twitter. Talk to me about research with Twitter data. Previously: Amazon Alexa. Views are my own",       "url": "https:\/\/t.co\/8IkCzClPCz",       "entities": {         "url": {           "urls": [             {               "url": "https:\/\/t.co\/8IkCzClPCz",               "expanded_url": "https:\/\/developer.twitter.com",               "display_url": "developer.twitter.com",               "indices": [                 0,                 23               ]             }           ]         },         "description": {           "urls": []         }       },       "protected": false,       "followers_count": 738,       "friends_count": 512,       "listed_count": 12,       "created_at": "Thu Apr 27 20:56:22 +0000 2017",       "favourites_count": 365,       "utc_offset": null,       "time_zone": null,       "geo_enabled": false,       "verified": false,       "statuses_count": 460,       "lang": null,       "contributors_enabled": false,       "is_translator": false,       "is_translation_enabled": false,       "profile_background_color": "F5F8FA",       "profile_background_image_url": null,       "profile_background_image_url_https": null,       "profile_background_tile": false,       "profile_image_url": "http:\/\/pbs.twimg.com\/profile_images\/1230703695051935747\/TbQKe91L_normal.jpg",       "profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/1230703695051935747\/TbQKe91L_normal.jpg",       "profile_banner_url": "https:\/\/pbs.twimg.com\/profile_banners\/857699969263964161\/1593055939",       "profile_link_color": "1DA1F2",       "profile_sidebar_border_color": "C0DEED",       "profile_sidebar_fill_color": "DDEEF6",       "profile_text_color": "333333",       "profile_use_background_image": true,       "has_extended_profile": false,       "default_profile": true,       "default_profile_image": false,       "following": null,       "follow_request_sent": null,       "notifications": null,       "translator_type": "none"     },     "geo": null,     "coordinates": null,     "place": null,     "contributors": null,     "is_quote_status": false,     "retweet_count": 19,     "favorite_count": 71,     "favorited": false,     "retweeted": false,     "possibly_sensitive": false,     "possibly_sensitive_appealable": false,     "lang": "en"   },   "is_quote_status": false,   "retweet_count": 19,   "favorite_count": 0,   "favorited": false,   "retweeted": false,   "lang": "en" }`
    

### Retweet (with tweet\_mode=extended)

      `{   "created_at": "Tue Feb 18 19:33:59 +0000 2020",   "id": 1229851574555508737,   "id_str": "1229851574555508737",   "full_text": "RT @suhemparack: I built an Alexa Skill for Twitter using APL that allows you to view Tweets and Trends on the echo show!\n\nCheck it out her…",   "truncated": false,   "display_text_range": [     0,     140   ],   "entities": {     "hashtags": [],     "symbols": [],     "user_mentions": [       {         "screen_name": "suhemparack",         "name": "Suhem Parack",         "id": 857699969263964161,         "id_str": "857699969263964161",         "indices": [           3,           15         ]       }     ],     "urls": []   },   "source": "<a href=\"https:\/\/mobile.twitter.com\" rel=\"nofollow\">Twitter Web App<\/a>",   "in_reply_to_status_id": null,   "in_reply_to_status_id_str": null,   "in_reply_to_user_id": null,   "in_reply_to_user_id_str": null,   "in_reply_to_screen_name": null,   "user": {     "id": 2244994945,     "id_str": "2244994945",     "name": "Twitter Dev",     "screen_name": "TwitterDev",     "location": "127.0.0.1",     "description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",     "url": "https:\/\/t.co\/3ZX3TNiZCY",     "entities": {       "url": {         "urls": [           {             "url": "https:\/\/t.co\/3ZX3TNiZCY",             "expanded_url": "https:\/\/developer.twitter.com\/en\/community",             "display_url": "developer.twitter.com\/en\/community",             "indices": [               0,               23             ]           }         ]       },       "description": {         "urls": []       }     },     "protected": false,     "followers_count": 513958,     "friends_count": 2039,     "listed_count": 1672,     "created_at": "Sat Dec 14 04:35:55 +0000 2013",     "favourites_count": 2145,     "utc_offset": null,     "time_zone": null,     "geo_enabled": true,     "verified": true,     "statuses_count": 3635,     "lang": null,     "contributors_enabled": false,     "is_translator": false,     "is_translation_enabled": false,     "profile_background_color": "FFFFFF",     "profile_background_image_url": "http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",     "profile_background_image_url_https": "https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",     "profile_background_tile": false,     "profile_image_url": "http:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",     "profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",     "profile_banner_url": "https:\/\/pbs.twimg.com\/profile_banners\/2244994945\/1594913664",     "profile_link_color": "0084B4",     "profile_sidebar_border_color": "FFFFFF",     "profile_sidebar_fill_color": "DDEEF6",     "profile_text_color": "333333",     "profile_use_background_image": false,     "has_extended_profile": true,     "default_profile": false,     "default_profile_image": false,     "following": null,     "follow_request_sent": null,     "notifications": null,     "translator_type": "regular"   },   "geo": null,   "coordinates": null,   "place": null,   "contributors": null,   "retweeted_status": {     "created_at": "Tue Feb 18 19:01:58 +0000 2020",     "id": 1229843515603144704,     "id_str": "1229843515603144704",     "full_text": "I built an Alexa Skill for Twitter using APL that allows you to view Tweets and Trends on the echo show!\n\nCheck it out here 👇\n\nhttps:\/\/t.co\/l5J8wq748G",     "truncated": false,     "display_text_range": [       0,       150     ],     "entities": {       "hashtags": [],       "symbols": [],       "user_mentions": [],       "urls": [         {           "url": "https:\/\/t.co\/l5J8wq748G",           "expanded_url": "https:\/\/dev.to\/twitterdev\/building-an-alexa-skill-for-twitter-using-alexa-presentation-language-1aj0",           "display_url": "dev.to\/twitterdev\/bui…",           "indices": [             127,             150           ]         }       ]     },     "source": "<a href=\"https:\/\/mobile.twitter.com\" rel=\"nofollow\">Twitter Web App<\/a>",     "in_reply_to_status_id": null,     "in_reply_to_status_id_str": null,     "in_reply_to_user_id": null,     "in_reply_to_user_id_str": null,     "in_reply_to_screen_name": null,     "user": {       "id": 857699969263964161,       "id_str": "857699969263964161",       "name": "Suhem Parack",       "screen_name": "suhemparack",       "location": "Seattle, WA",       "description": "Developer Relations for Academic Research @Twitter. Talk to me about research with Twitter data. Previously: Amazon Alexa. Views are my own",       "url": "https:\/\/t.co\/8IkCzClPCz",       "entities": {         "url": {           "urls": [             {               "url": "https:\/\/t.co\/8IkCzClPCz",               "expanded_url": "https:\/\/developer.twitter.com",               "display_url": "developer.twitter.com",               "indices": [                 0,                 23               ]             }           ]         },         "description": {           "urls": []         }       },       "protected": false,       "followers_count": 738,       "friends_count": 512,       "listed_count": 12,       "created_at": "Thu Apr 27 20:56:22 +0000 2017",       "favourites_count": 365,       "utc_offset": null,       "time_zone": null,       "geo_enabled": false,       "verified": false,       "statuses_count": 460,       "lang": null,       "contributors_enabled": false,       "is_translator": false,       "is_translation_enabled": false,       "profile_background_color": "F5F8FA",       "profile_background_image_url": null,       "profile_background_image_url_https": null,       "profile_background_tile": false,       "profile_image_url": "http:\/\/pbs.twimg.com\/profile_images\/1230703695051935747\/TbQKe91L_normal.jpg",       "profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/1230703695051935747\/TbQKe91L_normal.jpg",       "profile_banner_url": "https:\/\/pbs.twimg.com\/profile_banners\/857699969263964161\/1593055939",       "profile_link_color": "1DA1F2",       "profile_sidebar_border_color": "C0DEED",       "profile_sidebar_fill_color": "DDEEF6",       "profile_text_color": "333333",       "profile_use_background_image": true,       "has_extended_profile": false,       "default_profile": true,       "default_profile_image": false,       "following": null,       "follow_request_sent": null,       "notifications": null,       "translator_type": "none"     },     "geo": null,     "coordinates": null,     "place": null,     "contributors": null,     "is_quote_status": false,     "retweet_count": 19,     "favorite_count": 71,     "favorited": false,     "retweeted": false,     "possibly_sensitive": false,     "possibly_sensitive_appealable": false,     "lang": "en"   },   "is_quote_status": false,   "retweet_count": 19,   "favorite_count": 0,   "favorited": false,   "retweeted": false,   "lang": "en" }`
    

### Quote Tweet (default)

      `{   "created_at": "Mon Nov 16 18:09:36 +0000 2020",   "id": 1328399838128467969,   "id_str": "1328399838128467969",   "text": "As planned, the Labs v2 endpoints referenced below have now been retired. Please let us know in the forums if you h… https:\/\/t.co\/ahQvTYaOcZ",   "truncated": true,   "entities": {     "hashtags": [],     "symbols": [],     "user_mentions": [],     "urls": [       {         "url": "https:\/\/t.co\/ahQvTYaOcZ",         "expanded_url": "https:\/\/twitter.com\/i\/web\/status\/1328399838128467969",         "display_url": "twitter.com\/i\/web\/status\/1…",         "indices": [           117,           140         ]       }     ]   },   "source": "<a href=\"https:\/\/mobile.twitter.com\" rel=\"nofollow\">Twitter Web App<\/a>",   "in_reply_to_status_id": null,   "in_reply_to_status_id_str": null,   "in_reply_to_user_id": null,   "in_reply_to_user_id_str": null,   "in_reply_to_screen_name": null,   "user": {     "id": 2244994945,     "id_str": "2244994945",     "name": "Twitter Dev",     "screen_name": "TwitterDev",     "location": "127.0.0.1",     "description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",     "url": "https:\/\/t.co\/3ZX3TNiZCY",     "entities": {       "url": {         "urls": [           {             "url": "https:\/\/t.co\/3ZX3TNiZCY",             "expanded_url": "https:\/\/developer.twitter.com\/en\/community",             "display_url": "developer.twitter.com\/en\/community",             "indices": [               0,               23             ]           }         ]       },       "description": {         "urls": []       }     },     "protected": false,     "followers_count": 513958,     "friends_count": 2039,     "listed_count": 1672,     "created_at": "Sat Dec 14 04:35:55 +0000 2013",     "favourites_count": 2145,     "utc_offset": null,     "time_zone": null,     "geo_enabled": true,     "verified": true,     "statuses_count": 3635,     "lang": null,     "contributors_enabled": false,     "is_translator": false,     "is_translation_enabled": false,     "profile_background_color": "FFFFFF",     "profile_background_image_url": "http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",     "profile_background_image_url_https": "https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",     "profile_background_tile": false,     "profile_image_url": "http:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",     "profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",     "profile_banner_url": "https:\/\/pbs.twimg.com\/profile_banners\/2244994945\/1594913664",     "profile_link_color": "0084B4",     "profile_sidebar_border_color": "FFFFFF",     "profile_sidebar_fill_color": "DDEEF6",     "profile_text_color": "333333",     "profile_use_background_image": false,     "has_extended_profile": true,     "default_profile": false,     "default_profile_image": false,     "following": null,     "follow_request_sent": null,     "notifications": null,     "translator_type": "regular"   },   "geo": null,   "coordinates": null,   "place": null,   "contributors": null,   "is_quote_status": true,   "quoted_status_id": 1327011423252144128,   "quoted_status_id_str": "1327011423252144128",   "quoted_status": {     "created_at": "Thu Nov 12 22:12:32 +0000 2020",     "id": 1327011423252144128,     "id_str": "1327011423252144128",     "text": "👋 Friendly reminder that Twitter Developer Labs v2 hide replies and recent search will be retired next Monday, Nove… https:\/\/t.co\/EEWN2Q9aXh",     "truncated": true,     "entities": {       "hashtags": [],       "symbols": [],       "user_mentions": [],       "urls": [         {           "url": "https:\/\/t.co\/EEWN2Q9aXh",           "expanded_url": "https:\/\/twitter.com\/i\/web\/status\/1327011423252144128",           "display_url": "twitter.com\/i\/web\/status\/1…",           "indices": [             117,             140           ]         }       ]     },     "source": "<a href=\"https:\/\/mobile.twitter.com\" rel=\"nofollow\">Twitter Web App<\/a>",     "in_reply_to_status_id": null,     "in_reply_to_status_id_str": null,     "in_reply_to_user_id": null,     "in_reply_to_user_id_str": null,     "in_reply_to_screen_name": null,     "user": {       "id": 2244994945,       "id_str": "2244994945",       "name": "Twitter Dev",       "screen_name": "TwitterDev",       "location": "127.0.0.1",       "description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",       "url": "https:\/\/t.co\/3ZX3TNiZCY",       "entities": {         "url": {           "urls": [             {               "url": "https:\/\/t.co\/3ZX3TNiZCY",               "expanded_url": "https:\/\/developer.twitter.com\/en\/community",               "display_url": "developer.twitter.com\/en\/community",               "indices": [                 0,                 23               ]             }           ]         },         "description": {           "urls": []         }       },       "protected": false,       "followers_count": 513958,       "friends_count": 2039,       "listed_count": 1672,       "created_at": "Sat Dec 14 04:35:55 +0000 2013",       "favourites_count": 2145,       "utc_offset": null,       "time_zone": null,       "geo_enabled": true,       "verified": true,       "statuses_count": 3635,       "lang": null,       "contributors_enabled": false,       "is_translator": false,       "is_translation_enabled": false,       "profile_background_color": "FFFFFF",       "profile_background_image_url": "http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",       "profile_background_image_url_https": "https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",       "profile_background_tile": false,       "profile_image_url": "http:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",       "profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",       "profile_banner_url": "https:\/\/pbs.twimg.com\/profile_banners\/2244994945\/1594913664",       "profile_link_color": "0084B4",       "profile_sidebar_border_color": "FFFFFF",       "profile_sidebar_fill_color": "DDEEF6",       "profile_text_color": "333333",       "profile_use_background_image": false,       "has_extended_profile": true,       "default_profile": false,       "default_profile_image": false,       "following": null,       "follow_request_sent": null,       "notifications": null,       "translator_type": "regular"     },     "geo": null,     "coordinates": null,     "place": null,     "contributors": null,     "is_quote_status": false,     "retweet_count": 8,     "favorite_count": 33,     "favorited": false,     "retweeted": false,     "possibly_sensitive": false,     "possibly_sensitive_appealable": false,     "lang": "en"   },   "retweet_count": 7,   "favorite_count": 29,   "favorited": false,   "retweeted": false,   "possibly_sensitive": false,   "possibly_sensitive_appealable": false,   "lang": "en" }`
    

### Quote Tweet (with tweet\_mode=extended)

      `{   "created_at": "Mon Nov 16 18:09:36 +0000 2020",   "id": 1328399838128467969,   "id_str": "1328399838128467969",   "full_text": "As planned, the Labs v2 endpoints referenced below have now been retired. Please let us know in the forums if you have questions or need help with the Twitter API v2! https:\/\/t.co\/JaxttUMmjX",   "truncated": false,   "display_text_range": [     0,     166   ],   "entities": {     "hashtags": [],     "symbols": [],     "user_mentions": [],     "urls": [       {         "url": "https:\/\/t.co\/JaxttUMmjX",         "expanded_url": "https:\/\/twitter.com\/TwitterDev\/status\/1327011423252144128",         "display_url": "twitter.com\/TwitterDev\/sta…",         "indices": [           167,           190         ]       }     ]   },   "source": "<a href=\"https:\/\/mobile.twitter.com\" rel=\"nofollow\">Twitter Web App<\/a>",   "in_reply_to_status_id": null,   "in_reply_to_status_id_str": null,   "in_reply_to_user_id": null,   "in_reply_to_user_id_str": null,   "in_reply_to_screen_name": null,   "user": {     "id": 2244994945,     "id_str": "2244994945",     "name": "Twitter Dev",     "screen_name": "TwitterDev",     "location": "127.0.0.1",     "description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",     "url": "https:\/\/t.co\/3ZX3TNiZCY",     "entities": {       "url": {         "urls": [           {             "url": "https:\/\/t.co\/3ZX3TNiZCY",             "expanded_url": "https:\/\/developer.twitter.com\/en\/community",             "display_url": "developer.twitter.com\/en\/community",             "indices": [               0,               23             ]           }         ]       },       "description": {         "urls": []       }     },     "protected": false,     "followers_count": 513958,     "friends_count": 2039,     "listed_count": 1672,     "created_at": "Sat Dec 14 04:35:55 +0000 2013",     "favourites_count": 2145,     "utc_offset": null,     "time_zone": null,     "geo_enabled": true,     "verified": true,     "statuses_count": 3635,     "lang": null,     "contributors_enabled": false,     "is_translator": false,     "is_translation_enabled": false,     "profile_background_color": "FFFFFF",     "profile_background_image_url": "http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",     "profile_background_image_url_https": "https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",     "profile_background_tile": false,     "profile_image_url": "http:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",     "profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",     "profile_banner_url": "https:\/\/pbs.twimg.com\/profile_banners\/2244994945\/1594913664",     "profile_link_color": "0084B4",     "profile_sidebar_border_color": "FFFFFF",     "profile_sidebar_fill_color": "DDEEF6",     "profile_text_color": "333333",     "profile_use_background_image": false,     "has_extended_profile": true,     "default_profile": false,     "default_profile_image": false,     "following": null,     "follow_request_sent": null,     "notifications": null,     "translator_type": "regular"   },   "geo": null,   "coordinates": null,   "place": null,   "contributors": null,   "is_quote_status": true,   "quoted_status_id": 1327011423252144128,   "quoted_status_id_str": "1327011423252144128",   "quoted_status_permalink": {     "url": "https:\/\/t.co\/JaxttUMmjX",     "expanded": "https:\/\/twitter.com\/TwitterDev\/status\/1327011423252144128",     "display": "twitter.com\/TwitterDev\/sta…"   },   "quoted_status": {     "created_at": "Thu Nov 12 22:12:32 +0000 2020",     "id": 1327011423252144128,     "id_str": "1327011423252144128",     "full_text": "👋 Friendly reminder that Twitter Developer Labs v2 hide replies and recent search will be retired next Monday, November 16! We encourage you to migrate to the new hide replies and recent search endpoints now available in the v2 #TwitterAPI. Details: https:\/\/t.co\/r6z6CI7kEy",     "truncated": false,     "display_text_range": [       0,       273     ],     "entities": {       "hashtags": [         {           "text": "TwitterAPI",           "indices": [             228,             239           ]         }       ],       "symbols": [],       "user_mentions": [],       "urls": [         {           "url": "https:\/\/t.co\/r6z6CI7kEy",           "expanded_url": "https:\/\/twittercommunity.com\/t\/retiring-labs-v2-recent-search-and-hide-replies\/145795",           "display_url": "twittercommunity.com\/t\/retiring-lab…",           "indices": [             250,             273           ]         }       ]     },     "source": "<a href=\"https:\/\/mobile.twitter.com\" rel=\"nofollow\">Twitter Web App<\/a>",     "in_reply_to_status_id": null,     "in_reply_to_status_id_str": null,     "in_reply_to_user_id": null,     "in_reply_to_user_id_str": null,     "in_reply_to_screen_name": null,     "user": {       "id": 2244994945,       "id_str": "2244994945",       "name": "Twitter Dev",       "screen_name": "TwitterDev",       "location": "127.0.0.1",       "description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",       "url": "https:\/\/t.co\/3ZX3TNiZCY",       "entities": {         "url": {           "urls": [             {               "url": "https:\/\/t.co\/3ZX3TNiZCY",               "expanded_url": "https:\/\/developer.twitter.com\/en\/community",               "display_url": "developer.twitter.com\/en\/community",               "indices": [                 0,                 23               ]             }           ]         },         "description": {           "urls": []         }       },       "protected": false,       "followers_count": 513958,       "friends_count": 2039,       "listed_count": 1672,       "created_at": "Sat Dec 14 04:35:55 +0000 2013",       "favourites_count": 2145,       "utc_offset": null,       "time_zone": null,       "geo_enabled": true,       "verified": true,       "statuses_count": 3635,       "lang": null,       "contributors_enabled": false,       "is_translator": false,       "is_translation_enabled": false,       "profile_background_color": "FFFFFF",       "profile_background_image_url": "http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",       "profile_background_image_url_https": "https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",       "profile_background_tile": false,       "profile_image_url": "http:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",       "profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",       "profile_banner_url": "https:\/\/pbs.twimg.com\/profile_banners\/2244994945\/1594913664",       "profile_link_color": "0084B4",       "profile_sidebar_border_color": "FFFFFF",       "profile_sidebar_fill_color": "DDEEF6",       "profile_text_color": "333333",       "profile_use_background_image": false,       "has_extended_profile": true,       "default_profile": false,       "default_profile_image": false,       "following": null,       "follow_request_sent": null,       "notifications": null,       "translator_type": "regular"     },     "geo": null,     "coordinates": null,     "place": null,     "contributors": null,     "is_quote_status": false,     "retweet_count": 8,     "favorite_count": 33,     "favorited": false,     "retweeted": false,     "possibly_sensitive": false,     "possibly_sensitive_appealable": false,     "lang": "en"   },   "retweet_count": 7,   "favorite_count": 29,   "favorited": false,   "retweeted": false,   "possibly_sensitive": false,   "possibly_sensitive_appealable": false,   "lang": "en" }`
    

### Retweeted Quote Tweet (default)

      `{   "created_at": "Thu Feb 06 17:26:44 +0000 2020",   "id": 1225470895902412800,   "id_str": "1225470895902412800",   "text": "RT @AureliaSpecker: 📣 If you enjoyed the London commute tutorial I wrote in November last year, check out the refactored version that uses…",   "truncated": false,   "entities": {     "hashtags": [],     "symbols": [],     "user_mentions": [       {         "screen_name": "AureliaSpecker",         "name": "Aurelia Specker",         "id": 1102321381,         "id_str": "1102321381",         "indices": [           3,           18         ]       }     ],     "urls": []   },   "source": "<a href=\"http:\/\/twitter.com\/download\/iphone\" rel=\"nofollow\">Twitter for iPhone<\/a>",   "in_reply_to_status_id": null,   "in_reply_to_status_id_str": null,   "in_reply_to_user_id": null,   "in_reply_to_user_id_str": null,   "in_reply_to_screen_name": null,   "user": {     "id": 2244994945,     "id_str": "2244994945",     "name": "Twitter Dev",     "screen_name": "TwitterDev",     "location": "127.0.0.1",     "description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",     "url": "https:\/\/t.co\/3ZX3TNiZCY",     "entities": {       "url": {         "urls": [           {             "url": "https:\/\/t.co\/3ZX3TNiZCY",             "expanded_url": "https:\/\/developer.twitter.com\/en\/community",             "display_url": "developer.twitter.com\/en\/community",             "indices": [               0,               23             ]           }         ]       },       "description": {         "urls": []       }     },     "protected": false,     "followers_count": 513958,     "friends_count": 2039,     "listed_count": 1672,     "created_at": "Sat Dec 14 04:35:55 +0000 2013",     "favourites_count": 2145,     "utc_offset": null,     "time_zone": null,     "geo_enabled": true,     "verified": true,     "statuses_count": 3635,     "lang": null,     "contributors_enabled": false,     "is_translator": false,     "is_translation_enabled": false,     "profile_background_color": "FFFFFF",     "profile_background_image_url": "http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",     "profile_background_image_url_https": "https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",     "profile_background_tile": false,     "profile_image_url": "http:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",     "profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",     "profile_banner_url": "https:\/\/pbs.twimg.com\/profile_banners\/2244994945\/1594913664",     "profile_link_color": "0084B4",     "profile_sidebar_border_color": "FFFFFF",     "profile_sidebar_fill_color": "DDEEF6",     "profile_text_color": "333333",     "profile_use_background_image": false,     "has_extended_profile": true,     "default_profile": false,     "default_profile_image": false,     "following": null,     "follow_request_sent": null,     "notifications": null,     "translator_type": "regular"   },   "geo": null,   "coordinates": null,   "place": null,   "contributors": null,   "retweeted_status": {     "created_at": "Tue Feb 04 15:01:25 +0000 2020",     "id": 1224709550214873090,     "id_str": "1224709550214873090",     "text": "📣 If you enjoyed the London commute tutorial I wrote in November last year, check out the refactored version that u… https:\/\/t.co\/cAepHunkFp",     "truncated": true,     "entities": {       "hashtags": [],       "symbols": [],       "user_mentions": [],       "urls": [         {           "url": "https:\/\/t.co\/cAepHunkFp",           "expanded_url": "https:\/\/twitter.com\/i\/web\/status\/1224709550214873090",           "display_url": "twitter.com\/i\/web\/status\/1…",           "indices": [             117,             140           ]         }       ]     },     "source": "<a href=\"https:\/\/mobile.twitter.com\" rel=\"nofollow\">Twitter Web App<\/a>",     "in_reply_to_status_id": null,     "in_reply_to_status_id_str": null,     "in_reply_to_user_id": null,     "in_reply_to_user_id_str": null,     "in_reply_to_screen_name": null,     "user": {       "id": 1102321381,       "id_str": "1102321381",       "name": "Aurelia Specker",       "screen_name": "AureliaSpecker",       "location": "London, UK",       "description": "devrel @TwitterUK • Swiss in London • mother of houseplants • personal hairdresser to @_dormrod",       "url": null,       "entities": {         "description": {           "urls": []         }       },       "protected": false,       "followers_count": 1036,       "friends_count": 1330,       "listed_count": 26,       "created_at": "Fri Jan 18 23:45:43 +0000 2013",       "favourites_count": 4990,       "utc_offset": null,       "time_zone": null,       "geo_enabled": true,       "verified": false,       "statuses_count": 855,       "lang": null,       "contributors_enabled": false,       "is_translator": false,       "is_translation_enabled": false,       "profile_background_color": "8B542B",       "profile_background_image_url": "http:\/\/abs.twimg.com\/images\/themes\/theme8\/bg.gif",       "profile_background_image_url_https": "https:\/\/abs.twimg.com\/images\/themes\/theme8\/bg.gif",       "profile_background_tile": false,       "profile_image_url": "http:\/\/pbs.twimg.com\/profile_images\/1137517534104772608\/8FBYgc6G_normal.jpg",       "profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/1137517534104772608\/8FBYgc6G_normal.jpg",       "profile_banner_url": "https:\/\/pbs.twimg.com\/profile_banners\/1102321381\/1587552672",       "profile_link_color": "5E341C",       "profile_sidebar_border_color": "D9B17E",       "profile_sidebar_fill_color": "EADEAA",       "profile_text_color": "333333",       "profile_use_background_image": true,       "has_extended_profile": false,       "default_profile": false,       "default_profile_image": false,       "following": null,       "follow_request_sent": null,       "notifications": null,       "translator_type": "none"     },     "geo": null,     "coordinates": null,     "place": null,     "contributors": null,     "is_quote_status": true,     "quoted_status_id": 1195000047089389573,     "quoted_status_id_str": "1195000047089389573",     "quoted_status": {       "created_at": "Thu Nov 14 15:26:27 +0000 2019",       "id": 1195000047089389573,       "id_str": "1195000047089389573",       "text": "I wrote a tutorial on how to get bespoke commute information using the Twitter API🚇\n\n#DEVcommunity #Pythontutorial… https:\/\/t.co\/pL0qJ4vhtE",       "truncated": true,       "entities": {         "hashtags": [           {             "text": "DEVcommunity",             "indices": [               85,               98             ]           },           {             "text": "Pythontutorial",             "indices": [               99,               114             ]           }         ],         "symbols": [],         "user_mentions": [],         "urls": [           {             "url": "https:\/\/t.co\/pL0qJ4vhtE",             "expanded_url": "https:\/\/twitter.com\/i\/web\/status\/1195000047089389573",             "display_url": "twitter.com\/i\/web\/status\/1…",             "indices": [               116,               139             ]           }         ]       },       "source": "<a href=\"https:\/\/mobile.twitter.com\" rel=\"nofollow\">Twitter Web App<\/a>",       "in_reply_to_status_id": null,       "in_reply_to_status_id_str": null,       "in_reply_to_user_id": null,       "in_reply_to_user_id_str": null,       "in_reply_to_screen_name": null,       "user": {         "id": 1102321381,         "id_str": "1102321381",         "name": "Aurelia Specker",         "screen_name": "AureliaSpecker",         "location": "London, UK",         "description": "devrel @TwitterUK • Swiss in London • mother of houseplants • personal hairdresser to @_dormrod",         "url": null,         "entities": {           "description": {             "urls": []           }         },         "protected": false,         "followers_count": 1036,         "friends_count": 1330,         "listed_count": 26,         "created_at": "Fri Jan 18 23:45:43 +0000 2013",         "favourites_count": 4990,         "utc_offset": null,         "time_zone": null,         "geo_enabled": true,         "verified": false,         "statuses_count": 855,         "lang": null,         "contributors_enabled": false,         "is_translator": false,         "is_translation_enabled": false,         "profile_background_color": "8B542B",         "profile_background_image_url": "http:\/\/abs.twimg.com\/images\/themes\/theme8\/bg.gif",         "profile_background_image_url_https": "https:\/\/abs.twimg.com\/images\/themes\/theme8\/bg.gif",         "profile_background_tile": false,         "profile_image_url": "http:\/\/pbs.twimg.com\/profile_images\/1137517534104772608\/8FBYgc6G_normal.jpg",         "profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/1137517534104772608\/8FBYgc6G_normal.jpg",         "profile_banner_url": "https:\/\/pbs.twimg.com\/profile_banners\/1102321381\/1587552672",         "profile_link_color": "5E341C",         "profile_sidebar_border_color": "D9B17E",         "profile_sidebar_fill_color": "EADEAA",         "profile_text_color": "333333",         "profile_use_background_image": true,         "has_extended_profile": false,         "default_profile": false,         "default_profile_image": false,         "following": null,         "follow_request_sent": null,         "notifications": null,         "translator_type": "none"       },       "geo": null,       "coordinates": null,       "place": null,       "contributors": null,       "is_quote_status": false,       "retweet_count": 31,       "favorite_count": 123,       "favorited": false,       "retweeted": false,       "possibly_sensitive": false,       "possibly_sensitive_appealable": false,       "lang": "en"     },     "retweet_count": 12,     "favorite_count": 43,     "favorited": false,     "retweeted": false,     "possibly_sensitive": false,     "possibly_sensitive_appealable": false,     "lang": "en"   },   "is_quote_status": true,   "quoted_status_id": 1195000047089389573,   "quoted_status_id_str": "1195000047089389573",   "retweet_count": 12,   "favorite_count": 0,   "favorited": false,   "retweeted": false,   "lang": "en" }`
    

### Retweeted Quote Tweet (with tweet\_mode=extended)

      `{   "created_at": "Thu Feb 06 17:26:44 +0000 2020",   "id": 1225470895902412800,   "id_str": "1225470895902412800",   "full_text": "RT @AureliaSpecker: 📣 If you enjoyed the London commute tutorial I wrote in November last year, check out the refactored version that uses…",   "truncated": false,   "display_text_range": [     0,     139   ],   "entities": {     "hashtags": [],     "symbols": [],     "user_mentions": [       {         "screen_name": "AureliaSpecker",         "name": "Aurelia Specker",         "id": 1102321381,         "id_str": "1102321381",         "indices": [           3,           18         ]       }     ],     "urls": []   },   "source": "<a href=\"http:\/\/twitter.com\/download\/iphone\" rel=\"nofollow\">Twitter for iPhone<\/a>",   "in_reply_to_status_id": null,   "in_reply_to_status_id_str": null,   "in_reply_to_user_id": null,   "in_reply_to_user_id_str": null,   "in_reply_to_screen_name": null,   "user": {     "id": 2244994945,     "id_str": "2244994945",     "name": "Twitter Dev",     "screen_name": "TwitterDev",     "location": "127.0.0.1",     "description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",     "url": "https:\/\/t.co\/3ZX3TNiZCY",     "entities": {       "url": {         "urls": [           {             "url": "https:\/\/t.co\/3ZX3TNiZCY",             "expanded_url": "https:\/\/developer.twitter.com\/en\/community",             "display_url": "developer.twitter.com\/en\/community",             "indices": [               0,               23             ]           }         ]       },       "description": {         "urls": []       }     },     "protected": false,     "followers_count": 513958,     "friends_count": 2039,     "listed_count": 1672,     "created_at": "Sat Dec 14 04:35:55 +0000 2013",     "favourites_count": 2145,     "utc_offset": null,     "time_zone": null,     "geo_enabled": true,     "verified": true,     "statuses_count": 3635,     "lang": null,     "contributors_enabled": false,     "is_translator": false,     "is_translation_enabled": false,     "profile_background_color": "FFFFFF",     "profile_background_image_url": "http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",     "profile_background_image_url_https": "https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",     "profile_background_tile": false,     "profile_image_url": "http:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",     "profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",     "profile_banner_url": "https:\/\/pbs.twimg.com\/profile_banners\/2244994945\/1594913664",     "profile_link_color": "0084B4",     "profile_sidebar_border_color": "FFFFFF",     "profile_sidebar_fill_color": "DDEEF6",     "profile_text_color": "333333",     "profile_use_background_image": false,     "has_extended_profile": true,     "default_profile": false,     "default_profile_image": false,     "following": null,     "follow_request_sent": null,     "notifications": null,     "translator_type": "regular"   },   "geo": null,   "coordinates": null,   "place": null,   "contributors": null,   "retweeted_status": {     "created_at": "Tue Feb 04 15:01:25 +0000 2020",     "id": 1224709550214873090,     "id_str": "1224709550214873090",     "full_text": "📣 If you enjoyed the London commute tutorial I wrote in November last year, check out the refactored version that uses Twitter's new search endpoint 🚇 https:\/\/t.co\/87XIPZmZBJ\n\n#DEVcommunity #Pythontutorial @TwitterDev @TwitterAPI https:\/\/t.co\/dXrJYvn3hY",     "truncated": false,     "display_text_range": [       0,       229     ],     "entities": {       "hashtags": [         {           "text": "DEVcommunity",           "indices": [             176,             189           ]         },         {           "text": "Pythontutorial",           "indices": [             190,             205           ]         }       ],       "symbols": [],       "user_mentions": [         {           "screen_name": "TwitterDev",           "name": "Twitter Dev",           "id": 2244994945,           "id_str": "2244994945",           "indices": [             206,             217           ]         },         {           "screen_name": "TwitterAPI",           "name": "Twitter API",           "id": 6253282,           "id_str": "6253282",           "indices": [             218,             229           ]         }       ],       "urls": [         {           "url": "https:\/\/t.co\/87XIPZmZBJ",           "expanded_url": "https:\/\/bit.ly\/2OrnrCC",           "display_url": "bit.ly\/2OrnrCC",           "indices": [             151,             174           ]         },         {           "url": "https:\/\/t.co\/dXrJYvn3hY",           "expanded_url": "https:\/\/twitter.com\/AureliaSpecker\/status\/1195000047089389573",           "display_url": "twitter.com\/AureliaSpecker…",           "indices": [             230,             253           ]         }       ]     },     "source": "<a href=\"https:\/\/mobile.twitter.com\" rel=\"nofollow\">Twitter Web App<\/a>",     "in_reply_to_status_id": null,     "in_reply_to_status_id_str": null,     "in_reply_to_user_id": null,     "in_reply_to_user_id_str": null,     "in_reply_to_screen_name": null,     "user": {       "id": 1102321381,       "id_str": "1102321381",       "name": "Aurelia Specker",       "screen_name": "AureliaSpecker",       "location": "London, UK",       "description": "devrel @TwitterUK • Swiss in London • mother of houseplants • personal hairdresser to @_dormrod",       "url": null,       "entities": {         "description": {           "urls": []         }       },       "protected": false,       "followers_count": 1036,       "friends_count": 1330,       "listed_count": 26,       "created_at": "Fri Jan 18 23:45:43 +0000 2013",       "favourites_count": 4990,       "utc_offset": null,       "time_zone": null,       "geo_enabled": true,       "verified": false,       "statuses_count": 855,       "lang": null,       "contributors_enabled": false,       "is_translator": false,       "is_translation_enabled": false,       "profile_background_color": "8B542B",       "profile_background_image_url": "http:\/\/abs.twimg.com\/images\/themes\/theme8\/bg.gif",       "profile_background_image_url_https": "https:\/\/abs.twimg.com\/images\/themes\/theme8\/bg.gif",       "profile_background_tile": false,       "profile_image_url": "http:\/\/pbs.twimg.com\/profile_images\/1137517534104772608\/8FBYgc6G_normal.jpg",       "profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/1137517534104772608\/8FBYgc6G_normal.jpg",       "profile_banner_url": "https:\/\/pbs.twimg.com\/profile_banners\/1102321381\/1587552672",       "profile_link_color": "5E341C",       "profile_sidebar_border_color": "D9B17E",       "profile_sidebar_fill_color": "EADEAA",       "profile_text_color": "333333",       "profile_use_background_image": true,       "has_extended_profile": false,       "default_profile": false,       "default_profile_image": false,       "following": null,       "follow_request_sent": null,       "notifications": null,       "translator_type": "none"     },     "geo": null,     "coordinates": null,     "place": null,     "contributors": null,     "is_quote_status": true,     "quoted_status_id": 1195000047089389573,     "quoted_status_id_str": "1195000047089389573",     "quoted_status_permalink": {       "url": "https:\/\/t.co\/dXrJYvn3hY",       "expanded": "https:\/\/twitter.com\/AureliaSpecker\/status\/1195000047089389573",       "display": "twitter.com\/AureliaSpecker…"     },     "quoted_status": {       "created_at": "Thu Nov 14 15:26:27 +0000 2019",       "id": 1195000047089389573,       "id_str": "1195000047089389573",       "full_text": "I wrote a tutorial on how to get bespoke commute information using the Twitter API🚇\n\n#DEVcommunity #Pythontutorial \n\nCheck it out here 👇\nhttps:\/\/t.co\/sOjXW4YhbN",       "truncated": false,       "display_text_range": [         0,         160       ],       "entities": {         "hashtags": [           {             "text": "DEVcommunity",             "indices": [               85,               98             ]           },           {             "text": "Pythontutorial",             "indices": [               99,               114             ]           }         ],         "symbols": [],         "user_mentions": [],         "urls": [           {             "url": "https:\/\/t.co\/sOjXW4YhbN",             "expanded_url": "https:\/\/dev.to\/twitterdev\/using-the-twitter-api-to-make-your-commute-easier-3od0",             "display_url": "dev.to\/twitterdev\/usi…",             "indices": [               137,               160             ]           }         ]       },       "source": "<a href=\"https:\/\/mobile.twitter.com\" rel=\"nofollow\">Twitter Web App<\/a>",       "in_reply_to_status_id": null,       "in_reply_to_status_id_str": null,       "in_reply_to_user_id": null,       "in_reply_to_user_id_str": null,       "in_reply_to_screen_name": null,       "user": {         "id": 1102321381,         "id_str": "1102321381",         "name": "Aurelia Specker",         "screen_name": "AureliaSpecker",         "location": "London, UK",         "description": "devrel @TwitterUK • Swiss in London • mother of houseplants • personal hairdresser to @_dormrod",         "url": null,         "entities": {           "description": {             "urls": []           }         },         "protected": false,         "followers_count": 1036,         "friends_count": 1330,         "listed_count": 26,         "created_at": "Fri Jan 18 23:45:43 +0000 2013",         "favourites_count": 4990,         "utc_offset": null,         "time_zone": null,         "geo_enabled": true,         "verified": false,         "statuses_count": 855,         "lang": null,         "contributors_enabled": false,         "is_translator": false,         "is_translation_enabled": false,         "profile_background_color": "8B542B",         "profile_background_image_url": "http:\/\/abs.twimg.com\/images\/themes\/theme8\/bg.gif",         "profile_background_image_url_https": "https:\/\/abs.twimg.com\/images\/themes\/theme8\/bg.gif",         "profile_background_tile": false,         "profile_image_url": "http:\/\/pbs.twimg.com\/profile_images\/1137517534104772608\/8FBYgc6G_normal.jpg",         "profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/1137517534104772608\/8FBYgc6G_normal.jpg",         "profile_banner_url": "https:\/\/pbs.twimg.com\/profile_banners\/1102321381\/1587552672",         "profile_link_color": "5E341C",         "profile_sidebar_border_color": "D9B17E",         "profile_sidebar_fill_color": "EADEAA",         "profile_text_color": "333333",         "profile_use_background_image": true,         "has_extended_profile": false,         "default_profile": false,         "default_profile_image": false,         "following": null,         "follow_request_sent": null,         "notifications": null,         "translator_type": "none"       },       "geo": null,       "coordinates": null,       "place": null,       "contributors": null,       "is_quote_status": false,       "retweet_count": 31,       "favorite_count": 123,       "favorited": false,       "retweeted": false,       "possibly_sensitive": false,       "possibly_sensitive_appealable": false,       "lang": "en"     },     "retweet_count": 12,     "favorite_count": 43,     "favorited": false,     "retweeted": false,     "possibly_sensitive": false,     "possibly_sensitive_appealable": false,     "lang": "en"   },   "is_quote_status": true,   "quoted_status_id": 1195000047089389573,   "quoted_status_id_str": "1195000047089389573",   "quoted_status_permalink": {     "url": "https:\/\/t.co\/dXrJYvn3hY",     "expanded": "https:\/\/twitter.com\/AureliaSpecker\/status\/1195000047089389573",     "display": "twitter.com\/AureliaSpecker…"   },   "retweet_count": 12,   "favorite_count": 0,   "favorited": false,   "retweeted": false,   "lang": "en" }`

Rate limits: Standard v1.1

This page describes the rate limits for standard v1.1 endpoints. 

We also have a rate limits page for [premium v1.1](https://developer.twitter.com/en/docs/twitter-api/premium/rate-limits), [enterprise](https://developer.twitter.com/en/docs/twitter-api/enterprise/rate-limits), and [Twitter API v2](https://developer.twitter.com/en/docs/twitter-api/rate-limits). 

Overview
--------

Standard

Every day many thousands of developers make requests to the Twitter API. To help manage the sheer volume of these requests, limits are placed on the number of requests that can be made. These limits help us provide the reliable and scalable API that our developer community relies on. 

The maximum number of requests that are allowed is based on a time interval, some specified period or window of time. The most common request limit interval is fifteen minutes. If an endpoint has a rate limit of 900 requests/15-minutes, then up to 900 requests over any 15-minute interval is allowed. 

Rate limits are applied based on which authentication method you are using. For example, if you are using OAuth 1.0a User Context, you will have one limit per time period for each set of users’ access tokens, while if you are using OAuth 2.0 Bearer Token, you will have a separate limit per time period for requests made by your app. When these limits are exceeded, an error is returned. Keep reading to learn more about these details and tips on how to avoid being rate limited. 

### Rate limits and authentication method

Rate limits are set at both the developer App and the user access token levels:

* [OAuth 2.0 Bearer Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0): per-developer App  
    All Twitter API v1.1 endpoints accept this authentication method, and therefore will limit you to only make a certain number of requests to endpoints on behalf of your developer app. When using this authentication method, rate limits are determined by the number of requests you make using a Bearer Token. If an endpoint allows for 450 requests per rate limit window, then you can make 450 requests per window on behalf of your App by passing a Bearer Token. This limit is considered completely separate from the OAuth 1.0a User Context limit.  
      
    
* [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a): per-set of user access token  
    Tweet lookup and recent search allow for you to authenticate on behalf of a user. For example, if you would like to retrieve private metrics from Tweets, you would need to authenticate with the user tokens associated with that user, which can be generated by using the [3-legged OAuth flow](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens). If ten users have authorized your developer App, and up to 900 requests per 15-minute interval can be made on behalf of each user, you should be able to make up to 9000 requests on behalf of these users. This limit is considered completely separate from per-application Bearer Token limits.   
    

**Please note  
**

Users' rate limits are shared across all apps that they have authorized and the Twitter application. For example, if a specific user likes 20 Tweets on the Twitter mobile application and likes 20 Tweets on a third-party application within a 24 hour period of time, the 40 requests would pull out of the same per user rate limit bucket. That means that if this endpoint has a user rate limit of 1,000 requests per 24 hours, then this user would be able to like 960 more Tweets within that 24 hour period of time across all Twitter and third-party apps. 

Standard API v1.1 rate limits per window
----------------------------------------

### POST endpoints

The standard API rate limits described in this table refer to POST endpoints. These rate limits apply to the standard API endpoints only, does not apply to premium APIs.

|     |     |     |     |
| --- | --- | --- | --- |
| Endpoint | Rate limit window | Rate limit per user | Rate limit per app |
| [POST statuses/update](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-statuses-update) | 3 hours\* | 300\* | 300\* |
| [POST statuses/retweet/:id](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-statuses-retweet-id) | 3 hours\* | 300\* | 300\* |
| [POST favorites/create](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-favorites-create) | 24 hours | 1000 | 1000 |
| [POST friendships/create](https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/post-friendships-create) | 24 hours | 400 | 1000 |
| [POST direct\_messages/events/new](https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/api-reference/new-event) | 24 hours | 1000 | 15000 |

  
**Please note**

The 300 per 3 hours is with the POST statuses/update and POST statuses/retweet/:id endpoints is a combined limit. You can only post 300 Tweets or Retweets during a 3 hour period. 

For example, if your Twitter app makes 200 requests to the POST statuses/update endpoint within a three hour period, your app will only be able to make 100 requests to the POST statuses/retweet/:id endpoint during that period. 

### GET endpoints

The standard API rate limits described in this table refer to GET (read) endpoints. Note that endpoints not listed in the chart default to 15 requests per allotted user. All request windows are 15 minutes in length.  These rate limits apply to the standard API endpoints only, does not apply to premium APIs.

| Endpoint | Requests / window per user | Requests / window per app |
| --- | --- | --- |
| GET account/verify\_credentials | 75  | 0   |
| GET application/rate\_limit\_status | 180 | 180 |
| GET favorites/list | 75  | 75  |
| GET followers/ids | 15  | 15  |
| GET followers/list | 15  | 15  |
| GET friends/ids | 15  | 15  |
| GET friends/list | 15  | 15  |
| GET friendships/show | 180 | 15  |
| GET geo/id/:place\_id | 75  | 0   |
| GET help/configuration | 15  | 15  |
| GET help/languages | 15  | 15  |
| GET help/privacy | 15  | 15  |
| GET help/tos | 15  | 15  |
| GET lists/list | 15  | 15  |
| GET lists/members | 900 | 75  |
| GET lists/members/show | 15  | 15  |
| GET lists/memberships | 75  | 75  |
| GET lists/ownerships | 15  | 15  |
| GET lists/show | 75  | 75  |
| GET lists/statuses | 900 | 900 |
| GET lists/subscribers | 180 | 15  |
| GET lists/subscribers/show | 15  | 15  |
| GET lists/subscriptions | 15  | 15  |
| GET search/tweets | 180 | 450 |
| GET statuses/lookup | 900 | 300 |
| GET statuses/mentions\_timeline | 75  | 0   |
| GET statuses/retweeters/ids | 75  | 300 |
| GET statuses/retweets\_of\_me | 75  | 0   |
| GET statuses/retweets/:id | 75  | 300 |
| GET statuses/show/:id | 900 | 900 |
| GET statuses/user\_timeline | 900 | 1500 |
| GET trends/available | 75  | 75  |
| GET trends/closest | 75  | 75  |
| GET trends/place | 75  | 75  |
| GET users/lookup | 900 | 300 |
| GET users/search | 900 | 0   |
| GET users/show | 900 | 900 |
| GET users/suggestions | 15  | 15  |
| GET users/suggestions/:slug | 15  | 15  |
| GET users/suggestions/:slug/members | 15  | 15  |

Edit Tweets

Introduction
------------

Non-streaming standard endpoints have been updated to provide edited Tweet metadata. The statuses/filter and statuses/sample streaming endpoints have not been updated, while other endpoints that provide Tweet objects have been updated. The _Edit Tweets_ feature was first introduced for testing among Twitter employees on September 1, 2022. Starting on that date, eligible Tweets are editable for 30 minutes and up to 5 times. _All objects for Tweets created since September 29, 2022_ include Tweet edit metadata, even if the Tweet was never edited. Each time a Tweet is edited, a new Tweet ID is created. A Tweet's edit history can be described by chaining these IDs together, starting with the original ID. Additionally, if any Tweet in the edit chain is deleted, all Tweets in that chain are deleted as well. 

These edit metadata details are included when the include\_ext\_edit\_control request parameter is set to true: 

include\_ext\_edit\_control=true

With these new metadata, a developer can find out:  

* If a Tweet was edit eligible at the time of creation. Some Tweets, such as those with polls or scheduled Tweets, cannot be edited.
* Tweets are editable for 30 minutes, and can be edited up to 5 times. For editable Tweets, you can see if time for editing remains and how many more edits are possible.
* If you are viewing an edited version of a Tweet. In most cases, the API will return the most recent version of a Tweet, unless a specific past version is requested by Tweet

One new Tweet attribute has been added at the root level:

* **ext\_edit\_control**  - Provides all Tweet IDs associated with the edit history of the Tweet. The "edit\_tweet\_ids" attribute is an array that provides all IDs associated with its edit history. If the Tweet has not been edited, this array will contain a single ID.

      `"ext_edit_control": { 	"initial": { 	  "edit_tweet_ids":["1550220531252678656"],  	  "editable_until_msecs": "123", 	  "edits_remaining": "5", 	  "is_edit_eligible": true 	} }`
    

Most Tweets are eligible. However, the following types of Tweets are not:   

-----------------------------------------------------------------------------

* Tweet is promoted
* Tweet has a poll
* Tweet is a non-self-thread reply
* Tweet is a Retweet (note that Quote Tweets are eligible for edit)
* Tweet is nullcast
* Community Tweet
* Superfollow Tweet
* Collaborative Tweet

Example attributes for unedited Tweet  

----------------------------------------

The JSON below highlights edit metadata that is included for a Tweet posted after the edit Tweet feature was added. This example is for a Tweet that has no edit history. 

Note that the "edit\_tweet\_ids" array has a single ID. 

      `{   "created_at": "Wed Aug 16 18:29:02 +0000 2022",   "id": 1557433858676740098,   "id_str": "1557433858676740098",   "text": "I wonder if I will every use teh edit button",   "ext_edit_control": { 	"initial": { 	  "edit_tweet_ids":["1557433858676740098"],  	  "editable_until_msecs": "1658438151000", 	  "edits_remaining": "5", 	  "is_edit_eligible": true 	} }`
    

Example attributes for an edited Tweet
--------------------------------------

The JSON below highlights edit metadata that is included for a Tweet posted after the edit Tweet feature was added. This example is for a Tweet that has had a single edit. 

Note that the "edit\_tweet\_ids" array has two IDs, one for the original Tweet and one for the edited update. 

      `{   "created_at": "Wed Aug 16 18:35:42 +0000 2022",   "id": 1557445923210514432,   "id_str": "1557445923210514432",   "text": "I wonder if I will ever use the edit button",  "ext_edit_control": {         "edit": {           "edit_control_initial": {             "edit_tweet_ids": [               "1557433858676740098",               "1557445923210514432"             ],             "editable_until_msecs": "1658438151000",             "edits_remaining": "4",             "is_edit_eligible": true           },           "initial_tweet_id": "1557433858676740098"         }    }  }`