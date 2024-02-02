Overview

Overview
--------

The enterprise console (at console.gnip.com) is available to enterprise data customers with contracted enterprise API access. If you are not currently an enterprise data customer but would like more information, you can learn more about [enterprise data](https://developer.twitter.com/en/products/twitter-api/enterprise.html) here.  

This is an overview of Twitter’s enterprise console dashboard. The sections that are covered pertain to each specific area of the console for product details, usage, and general account management. If you have any questions regarding your specific account, please contact your designated account manager, or review our [technical documentation for enterprise products](https://developer.twitter.com/en/docs/twitter-api/enterprise.html).

As part of the enterprise trial and onboarding process with your account manager, enterprise customers will receive a login to [console.gnip.com](http://console.gnip.com/), which is the user interface where enterprise product access can be reviewed and configured. Initial access to the console for customer admin is set up by Twitter as part of the enterprise onboarding process, and admins can then add additional users. The enterprise console allows you to manage and access more details related to your enterprise products. 

The following video provides an overview of the various portions of the console.gnip.com dashboard. 

**Disclaimer: Please note that some of the features shown in the video, including certain stream enrichments and non-Twitter data source products, may no longer be available.**

 Your browser does not support the <code>video</code> element.

### Next Steps:

* [Review products tab](https://developer.twitter.com/en/docs/twitter-api/enterprise/console/product.html)
* [Review usage tab](https://developer.twitter.com/en/docs/twitter-api/enterprise/console/usage.html)
* [Review account tab](https://developer.twitter.com/en/docs/twitter-api/enterprise/console/account.html)

Products tab

Products tab
------------

Upon logging into your account at [console.gnip.com](http://console.gnip.com/), you will land on the products tab of the dashboard.  This page includes an overview of the enterprise products currently available on your account.

For products using streaming delivery like PowerTrack or Decahose, this page lists the product name, and stream label,  the number of current active connections, the number of rules currently active for each (where applicable), and the raw count of activities (for example, Tweets) delivered in the most recent 24 hours.

For products with REST delivery, like Search API, this page lists the product name,labels (also shown as "streams"), current activities (for example, Tweets) returned through these endpoints, and a few different request counts per endpoint.

Note that the [Usage API](https://developer.twitter.com/en/docs/twitter-api/enterprise/usage-api/overview.html) delivers much of this data programatically.

Specific details per stream are available by clicking the name, or the settings button.

  

### Overview

Clicking on one of the streams in the main dashboard will take you to an overview page for that stream.

For streaming delivery products, this page includes the following:

1. A volume chart of the number of activities being delivered to you through each specific stream connection 
    
2. Details (connection ID and IP address) on currently active connections on the stream 
    
3. A log of recent connection, disconnection, and rule-update events for your stream
    

Note that the scale of the chart may be adjusted with the links in the top-right corner. The visibility of individual connections and disconnections can be toggled by clicking the appropriate key in the legend directly below the chart.

  

  
  

### Connections

The Connections page provides details on recent connection events on your stream. This includes the start and end times for each connection (in 24 hour UTC), the duration of each connection, the IP of the server that made the connection, a unique connection ID for reference purposes, and the current connection status. The status corresponds to the most recent event for the specified connection – i.e. Client Connected, or a disconnect, with the type of disconnect specified.   For more details on connection debugging, visit the [disconnections explained guide](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/guides.html).

  

  
  

### API Help

The API Help page provides the API endpoint URLs for your stream, as well as the Rules API endpoint for the stream, where applicable. In addition, it includes sample curl commands and instructions on how to connect to the stream endpoint, and how to programmatically add, delete, and list rules from your stream's Rules API endpoint.

  

  
  

### Rules

The Rules tab is available for PowerTrack streams, and provides a quick way to get started by manually entering plain text rules via a user interface. Note that the interface only supports adding up to 1000 rules via this manual method, and should be only used for initial testing. We recommend managing your rules programmatically via the [Rules API](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/api-reference.html) in any production setting.

  

  
  

### Settings

The Settings tab allows you to switch the output format of the data in your stream, where multiple format options are supported. To switch the format, just use the radio buttons indicating the different options. The change will take effect upon reconnecting to the stream.  Note that updating this setting will take place immediately on the next request or connection and may break your parser with the new format. 

**Please note:** The recommended setting for getting the most data is "Leave data in the original format" which will return data in the enriched native format [here](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects.html).  Activity streams format is described [here](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/activity-streams-objects.html).

  

  
  

### Next Steps:

* [Review usage tab](https://developer.twitter.com/en/docs/twitter-api/enterprise/console/usage.html)
* [Review account tab](https://developer.twitter.com/en/docs/twitter-api/enterprise/console/account.html)

Usage tab

Usage tab
---------

The Usage Tab provides insight into your use of your streams over various time periods. For programmatic access to usage information, see the [Usage API](https://developer.twitter.com/en/docs/twitter-api/enterprise/usage-api/overview.html).

### Monthly

The Monthly Usage page displays your stream usage broken down by product. For example, coverage products (for example, PowerTrack, Historical PowerTrack, and PowerTrack Replay) for a given data source will be grouped together to provide separate data, as well as a combined roll-up count. The counts include a current month-to-date, estimated end-of-month (based on this month’s usage so far, and remaining time in the month), and the previous two months’ counts.

Notably, these counts are deduplicated for each product and stream. If you received the same Tweet through multiple connections to the same PowerTrack stream, that Tweet will be counted once for these purposes. Counts will be updated every 24 hours at 00:00 UTC.

### Daily

The Daily Usage page provides daily deduplicated counts for each day in the current month, broken down by product. Counts are updated every 24 hours at 00:00 UTC.

### Rules

Rule limits are based on your contracted PowerTrack rule package and are applied across all streams of a given "type". Counts are updated whenever a new rule is added or deleted.

  
  

### Next Steps:

* [Review account tab](https://developer.twitter.com/en/docs/twitter-api/enterprise/console/account.html)
* [Review the Usage API documentation](https://developer.twitter.com/en/docs/twitter-api/enterprise/usage-api/overview.html)

Account tab

Account tab
-----------

### My Profile

View details about your individual user profile, and change your password here. Additionally, you may configure account usage threshold notices specific to your account.  API status notices are available through the status page at https://api.twitterstat.us.

### Account Settings

You may add, remove, and edit users, and configure email notifications for individual users and usage threshold alerts.

  

Please note that there are three types of users – Account Admin, User, and Email Only.  

* Account admins are allowed to create/delete/edit other users, and can use basic authentication with username (email) and password to connect to the enterprise APIs
    
* Users cannot create or modify other users, but can use basic authentication with username (email) and password to connect to the enterprise APIs
    
* Email Only users do not have access to the dashboard, are not authorized to connect to the enterprise APIs  and only receive notifications, if they are configured to receive them in the Notifications section.
    

### Usage Thresholds

Configure volume thresholds for your products. These will initiate email alerts for the users who have configured those notifications in their profiles, both for the warning threshold and critical threshold for each product.

  

Please note that these thresholds are evaluated once per day at 19:30 (UTC), and are not evaluated in real-time.

  
  

### Next Steps:

* [Review enterprise data formats](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/overview.html)
* [Explore the Twitter API v2 developer portal](https://developer.twitter.com/en/docs/developer-portal/overview.html)
* [See enterprise support resources](https://developer.twitter.com/en/support/twitter-api.html#item6)

Introduction

Interested in learning more about how the enterprise data formats map to the Twitter API v2 format?

Check out our comparison guides:

* [Native Enriched compared to Twitter API v2](https://developer.twitter.com/en/docs/twitter-api/migrate/data-formats/native-enriched-to-v2)
* [Activity Streams compared to Twitter API v2](https://developer.twitter.com/en/docs/twitter-api/migrate/data-formats/activity-streams-to-v2)

Introduction
------------

Enterprise

Tweets are the basic atomic building block of all things Twitter. All Twitter APIs that return Tweets provide that data encoded using JavaScript Object Notation (JSON). JSON is based on key-value pairs, with named attributes and associated values. Tweet objects retrieved from the API include a Twitter User's "status update" but Retweets, replies, and quote Tweets are all also Tweet objects.  If a Tweet is related to another Tweet, as a Retweet, reply or quote Tweet, each will be identified or embedded into the Tweet object.  Even the simplest Tweet in the native Twitter data format, will have nested JSON objects to represent the other attributes of a Tweet, such as the author, mentioned users, tagged place location, hashtags, cashtag symbols, media or URL links.  When working with Twitter data, this is an important concept to understand. The format of the Tweet data you will receive from the Twitter API depends on the type of Tweet received, the Twitter API you are using, and the format settings.

Enterprise endpoints that return Tweet objects have been updated to provide the metadata needed to understand the Tweet's edit history. Learn more about these metadata on the ["Edit Tweets" fundamentals](https://developer.twitter.com/en/docs/twitter-api/edit-tweets) page.

> What did the developer write in their Valentine’s card?  
>   
> while(true) {  
> I = Love(You);  
> }
> 
> — Twitter Dev (@TwitterDev) [February 14, 2020](https://twitter.com/TwitterDev/status/1228393702244134912?ref_src=twsrc%5Etfw)

In native Twitter format, the JSON payload will include of ‘root-level’ attributes, and nested JSON objects (which are represented here with the `{}` notation):

      `{ 	"created_at": "Fri Feb 14 19:00:55 +0000 2020", 	"id_str": "1228393702244134912", 	"text": "What did the developer write in their Valentine’s card?\n  \nwhile(true) {\n    I = Love(You);  \n}", 	"entities": { 		"hashtags": [], 		"symbols": [], 		"user_mentions": [], 		"urls": [] 	}, 	"user": { 		"entities": { 			"url": {} 		} 	}, 	"place": {} }`
    

Available data formats
----------------------

Please note: It is highly recommended to use the [Enriched Native](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/tweet.html) format for enterprise data APIs. 

* The Enriched Native format includes all new metadata since 2017, such as [poll metadata](https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/poll-metadata.html), and additional metrics such as reply\_count and quote\_count.
    
* Activity Streams format has not been updated with new metadata or enrichments since the [character update](https://blog.twitter.com/official/en_us/topics/product/2017/Giving-you-more-characters-to-express-yourself.html) in 2017.
    

Enterprise data APIs deliver data in two different formats.  The enterprise format closest to the standard v1.1 native format is Native Enriched.  The legacy enterprise data format is Activity Streams, orignially implimented and used by Gnip as a normalized format across Twitter and other social media data providers at the time. While this format is still available, Twitter has only invested new features and developments on the native enriched format since 2017.  

The enriched native format is exactly how it sounds, it includes native Twitter objects as well as additional enrichments avialable for enterprise data products such as URL unwinding metadata, profile geo, poll metadata and additional engagement metrics.  

* [Expanded and enhanced URLs enrichment](https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/expanded-and-enhanced-urls)
* [Matching rules enrichment](https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/matching-rules)
* [Poll metadata enrichment](https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/poll-metadata)
* [Profile geo enrichment](https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/profile-geo)

### Object comparison per data format 

Whatever your Twitter use case, understanding what these JSON-encoded Tweet objects and attributes _represent_ is critical to successfully finding your data signals of interest. To help in that effort, there are a set of pages dedicated to each object in each data format_._

Reflecting the JSON hierarchy above, here are links to each of these objects:

| Native Enriched | Activity Streams |
| --- | --- |
| [Link](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/tweet) Tweet object | [Link](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/activity-streams-objects/tweet) Activity object |
| [Link](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/user) User object | [Link](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/activity-streams-objects/user) Actor object |
| [Link](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/entities) Entities object | [Link](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/activity-streams-objects/entities) Twitter entities object |
| [Link](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/extended-entities) Extended entities object | [Link](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/extended-entities) Twitter extended entitites object |
| [Link](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/geo) Geo object | [Link](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/activity-streams-objects/geo) Location object |
| n/a | [Link](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/activity-streams-objects/gnip.html) Gnip object |

Parsing best-practices
----------------------

* Twitter JSON is encoded using UTF-8 characters.
* Parsers should tolerate variance in the ordering of fields with ease. It should be assumed that Tweet JSON is served as an unordered hash of data.
* Parsers should tolerate the addition of 'new' fields. 
* JSON parsers must be tolerant of ‘missing’ fields, since not all fields appear in all contexts.
* It is generally safe to consider a nulled field, an empty set, and the absence of a field as the same thing

### Next Steps:

* Review the enterprise [enriched native data dictionary](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/tweet.html)

Tweet object

Interested in learning more about how the Native Enriched data format maps to the Twitter API v2 format?

Check out our comparison guide: [Native Enriched compared to Twitter API v2](https://developer.twitter.com/en/docs/twitter-api/migrate/data-formats/native-enriched-to-v2)

Tweet Object
------------

When using enterprise data products, you will notice that much of the data dictionary is similar to the native format of Tweet data, with some additional enriched metadata.  The base level of the native enriched format uses much of the same object names as the [Twitter API v1.1 data format](https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/overview/intro-to-tweet-json.html).  The Tweet object has a long list of ‘root-level’ attributes, including fundamental attributes such as `id`, `created_at`, and `text`. Tweet objects will also have nested objects to include the `user`, `entities`, and `extended_entities`. Tweet objects will also have other [nested Tweet objects](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/nested-tweet-objects) such as retweeted\_status, quoted\_status and extended\_tweet.  The native enriched format will additionally have a matching\_rules object.

### Tweet Data Dictionary

Below you will find the data dictionary for these ‘root-level’ attributes, as well as links to child object data dictionaries.

| Attribute | Type | Description |
| --- | --- | --- |
| created\_at | String | UTC time when this Tweet was created. Example:<br><br>"created\_at": "Wed Oct 10 20:19:24 +0000 2018" |
| id  | Int64 | The integer representation of the unique identifier for this Tweet. This number is greater than 53 bits and some programming languages may have difficulty/silent defects in interpreting it. Using a signed 64 bit integer for storing this identifier is safe. Use `**id_str**` to fetch the identifier to be safe. See [Twitter IDs](https://developer.twitter.com/en/docs/twitter-ids) for more information. Example:<br><br>"id":1050118621198921728 |
| id\_str | String | The string representation of the unique identifier for this Tweet. Implementations should use this rather than the large integer in `**id**`. Example:<br><br>"id\_str":"1050118621198921728" |
| text | String | The actual UTF-8 text of the status update. See [twitter-text](https://github.com/twitter/twitter-text/blob/master/rb/lib/twitter-text/regex.rb) for details on what characters are currently considered valid. Example:<br><br>"text":"To make room for more expression, we will now count all emojis as equal—including those with gender‍‍‍ ‍‍and skin t… https://t.co/MkGjXf9aXm" |
| source | String | Utility used to post the Tweet, as an HTML-formatted string. Tweets from the Twitter website have a source value of `**web**`.<br><br>Example:<br><br>"source":"Twitter Web Client" |
| truncated | Boolean | Indicates whether the value of the `**text**` parameter was truncated, for example, as a result of a retweet exceeding the original Tweet text length limit of 140 characters. Truncated text will end in ellipsis, like this `**...**` Since Twitter now rejects long Tweets vs truncating them, the large majority of Tweets will have this set to `**false**` . Note that while native retweets may have their toplevel `**text**` property shortened, the original text will be available under the `**retweeted_status**` object and the `**truncated**` parameter will be set to the value of the original status (in most cases, `**false**` ). Example:<br><br>"truncated":true |
| in\_reply\_to\_status\_id | Int64 | _Nullable._ If the represented Tweet is a reply, this field will contain the integer representation of the original Tweet’s ID. Example:<br><br>"in\_reply\_to\_status\_id":1051222721923756032 |
| in\_reply\_to\_status\_id\_str | String | _Nullable._ If the represented Tweet is a reply, this field will contain the string representation of the original Tweet’s ID. Example:<br><br>"in\_reply\_to\_status\_id\_str":"1051222721923756032" |
| in\_reply\_to\_user\_id | Int64 | _Nullable._ If the represented Tweet is a reply, this field will contain the integer representation of the original Tweet’s author ID. This will not necessarily always be the user directly mentioned in the Tweet. Example:<br><br>"in\_reply\_to\_user\_id":6253282 |
| in\_reply\_to\_user\_id\_str | String | _Nullable._ If the represented Tweet is a reply, this field will contain the string representation of the original Tweet’s author ID. This will not necessarily always be the user directly mentioned in the Tweet. Example:<br><br>"in\_reply\_to\_user\_id\_str":"6253282" |
| in\_reply\_to\_screen\_name | String | _Nullable._ If the represented Tweet is a reply, this field will contain the screen name of the original Tweet’s author. Example:<br><br>"in\_reply\_to\_screen\_name":"twitterapi" |
| user | [User object](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/user) | The user who posted this Tweet. See User data dictionary for complete list of attributes.<br><br>Example highlighting select attributes:<br><br> { "user": {<br>    "id": 6253282,<br>    "id\_str": "6253282",<br>    "name": "Twitter API",<br>    "screen\_name": "TwitterAPI",<br>    "location": "San Francisco, CA",<br>    "url": "https://developer.twitter.com",<br>    "description": "The Real Twitter API. Tweets about API changes, service issues and our Developer Platform. Don't get an answer? It's on my website.",<br>    "verified": true,<br>    "followers\_count": 6129794,<br>    "friends\_count": 12,<br>    "listed\_count": 12899,<br>    "favourites\_count": 31,<br>    "statuses\_count": 3658,<br>    "created\_at": "Wed May 23 06:01:13 +0000 2007",<br>    "utc\_offset": null,<br>    "time\_zone": null,<br>    "geo\_enabled": false,<br>    "lang": "en",<br>    "contributors\_enabled": false,<br>    "is\_translator": false,<br>    "profile\_background\_color": "null",<br>    "profile\_background\_image\_url": "null",<br>    "profile\_background\_image\_url\_https": "null",<br>    "profile\_background\_tile": null,<br>    "profile\_link\_color": "null",<br>    "profile\_sidebar\_border\_color": "null",<br>    "profile\_sidebar\_fill\_color": "null",<br>    "profile\_text\_color": "null",<br>    "profile\_use\_background\_image": null,<br>    "profile\_image\_url": "null",<br>    "profile\_image\_url\_https": "https://pbs.twimg.com/profile\_images/942858479592554497/BbazLO9L\_normal.jpg",<br>    "profile\_banner\_url": "https://pbs.twimg.com/profile\_banners/6253282/1497491515",<br>    "default\_profile": false,<br>    "default\_profile\_image": false,<br>    "following": null,<br>    "follow\_request\_sent": null,<br>    "notifications": null<br>  }<br>} |
| coordinates | [Coordinates](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/geo#coordinates-dictionary) | _Nullable._ Represents the geographic location of this Tweet as reported by the user or client application. The inner coordinates array is formatted as [geoJSON](http://www.geojson.org/) (longitude first, then latitude). Example:<br><br>"coordinates":<br>{<br>    "coordinates":<br>    \[<br>        -75.14310264,<br>        40.05701649<br>    \],<br>    "type":"Point"<br>} |
| place | [Places](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/geo#place-dictionary) | _Nullable_ When present, indicates that the tweet is associated (but not necessarily originating from) a Place  Example:<br><br>"place":<br>{<br>  "attributes":{},<br>   "bounding\_box":<br>  {<br>     "coordinates":<br>     \[\[<br>           \[-77.119759,38.791645\],<br>           \[-76.909393,38.791645\],<br>           \[-76.909393,38.995548\],<br>           \[-77.119759,38.995548\]<br>     \]\],<br>     "type":"Polygon"<br>  },<br>   "country":"United States",<br>   "country\_code":"US",<br>   "full\_name":"Washington, DC",<br>   "id":"01fbe706f872cb32",<br>   "name":"Washington",<br>   "place\_type":"city",<br>   "url":"http://api.twitter.com/1/geo/id/0172cb32.json"<br>} |
| quoted\_status\_id | Int64 | This field only surfaces when the Tweet is a quote Tweet. This field contains the integer value Tweet ID of the quoted Tweet. Example:<br><br>"quoted\_status\_id":1050119905717055488 |
| quoted\_status\_id\_str | String | This field only surfaces when the Tweet is a quote Tweet. This is the string representation Tweet ID of the quoted Tweet. Example:<br><br>"quoted\_status\_id\_str":"1050119905717055488" |
| is\_quote\_status | Boolean | Indicates whether this is a Quoted Tweet. Example:<br><br>"is\_quote\_status":false |
| quoted\_status | Tweet | This field only surfaces when the Tweet is a quote Tweet. This attribute contains the Tweet object of the original Tweet that was quoted. |
| retweeted\_status | Tweet | Users can amplify the broadcast of Tweets authored by other users by Retweeting . Retweets can be distinguished from typical Tweets by the existence of a `**retweeted_status**` attribute. This attribute contains a representation of the _original_ Tweet that was retweeted. Note that retweets of retweets do not show representations of the intermediary retweet, but only the original Tweet. (Users can also unretweet a retweet they created by deleting their retweet.) |
| quote\_count | Integer | _Nullable._ Indicates approximately how many times this Tweet has been quoted by Twitter users. Example:<br><br>"quote\_count":33<br><br>Note: This object is only available with the Premium and Enterprise tier products. |
| reply\_count | Int | Number of times this Tweet has been replied to. Example:<br><br>"reply\_count":30<br><br>Note: This object is only available with the Premium and Enterprise tier products. |
| retweet\_count | Int | Number of times this Tweet has been retweeted. Example:<br><br>"retweet\_count":160 |
| favorite\_count | Integer | _Nullable._ Indicates approximately how many times this Tweet has been liked by Twitter users. Example:<br><br>"favorite\_count":295 |
| entities | [Entities](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/entities) | Entities which have been parsed out of the text of the Tweet. Additionally see [Entities in Twitter Objects](https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/entities.html) . Example:<br><br>"entities":<br>{<br>    "hashtags":\[\],<br>    "urls":\[\],<br>    "user\_mentions":\[\],<br>    "media":\[\],<br>    "symbols":\[\]<br>    "polls":\[\]<br>} |
| extended\_entities | [Extended Entities](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/entities) | When between one and four native photos or one video or one animated GIF are in Tweet, contains an array 'media' metadata. This is also available in Quote Tweets. Additionally see [Entities in Twitter Objects](https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/extended-entities.html) . Example:<br><br>"entities":<br>{<br>    "media":\[\]<br>} |
| favorited | Boolean | _Nullable._ Indicates whether this Tweet has been liked by the authenticating user. Example:<br><br>"favorited":true |
| retweeted | Boolean | Indicates whether this Tweet has been Retweeted by the authenticating user. Example:<br><br>"retweeted":false |
| possibly\_sensitive | Boolean | _Nullable._ This field indicates content may be recognized as sensitive. The Tweet author can select within their own account preferences and choose “Mark media you tweet as having material that may be sensitive” so each Tweet created after has this flag set.<br><br>This may also be judged and labeled by an internal Twitter support agent.<br><br>"possibly\_sensitive":false |
| filter\_level | String | Indicates the maximum value of the filter\_level parameter which may be used and still stream this Tweet. So a value of `**medium**` will be streamed on `**none**`, `**low**`, and `**medium**` streams.<br><br>Example:<br><br>"filter\_level": "low" |
| lang | String | _Nullable._ When present, indicates a [BCP 47](http://tools.ietf.org/html/bcp47) language identifier corresponding to the machine-detected language of the Tweet text, or `**und**` if no language could be detected. <br><br> Example:<br><br>"lang": "en" |
| edit\_history | Object | Unique identifiers indicating all versions of a Tweet. For Tweets with no edits, there will be one ID. For Tweets with an edit history, there will be multiple IDs, arranged in ascending order reflecting the order of edits, with the most recent version in the last position of the array. <br><br>The Tweet IDs can be used to hydrate and view previous versions of a Tweet.<br><br>Example:<br><br>edit\_history": {<br>    "initial\_tweet\_id": "1283764123"<br>    "edit\_tweet\_ids": \["1283764123", "1394263866"\]<br>  } |
| edit\_controls | Object | When present, indicates how long a Tweet is still editable for and the number of remaining edits. Tweets are only editable for the first 30 minutes after creation and can be edited up to five times. <br><br>The Tweet IDs can be used to hydrate and view previous versions of a Tweet.<br><br>Example:<br><br>"edit\_controls": {  <br>     "editable\_until\_ms": 123<br>     "edits\_remaining": 3   <br>  } |
| editable | Boolean | When present, indicates if a Tweet was eligible for edit when published. This field is not dynamic and won't toggle from True to False when a Tweet reaches its editable time limit, or maximum number of edits. The following Tweet features will cause this field to be false:<br><br>* Tweets is promoted<br>* Tweet has a poll<br>* Tweet is a non-self-thread reply<br>* Tweet is a retweet (note that Quote Tweets are eligible for edit)<br>* Tweet is nullcast<br>* Community Tweet<br>* Superfollow Tweet<br>* Collaborative Tweet |
| matching\_rules | Array of Rule Objects | Present in _filtered_ products such as Twitter Search and PowerTrack. Provides the _id_ and _tag_ associated with the rule that matched the Tweet. More on matching rules [here](https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/matching-rules.html). With PowerTrack, more than one rule can match a Tweet. <br><br>Example:<br><br>"matching\_rules": " \[{<br>        "tag": "twitterapi emojis",<br>        "id": 1050118621198921728,<br>        "id\_str": "1050118621198921728"<br>    }\]" |
|     |     |     |

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

  
Nested Tweet objects
-----------------------

In several cases, a Tweet object will included other nested objects.  If you are working with nested objects, then that JSON payload will contain multiple Tweet objects, and each Tweet object may contain its own objects. The root-level object will contain information on the type of action taken, i.e. whether it is a Retweet or a Quote Tweet, and may also contain an object that describes the 'original' Tweet being shared. Extended Tweets will include a nested extended object that extends beyond 140 characters, which was used to prevent breaking changes when the update was made in 2017. Each nested object dictionary is described below.

#### Retweets

Retweets always contain two Tweet objects. The 'original' Tweet being Retweeted is provided in a "retweeted\_status" object. The root-level object encapsulates the Retweet itself, including a User object for the account taking the Retweet action and the time of the Retweet. Retweeting is an action to share a Tweet with your followers, and no other new content can be added. Also, a (new) location cannot be provided with a Retweet. While the 'original' Tweet may have geo-tagged, the Retweet "geo" and "place" objects will always be null.

Even before the introduction of Extended Tweets, the root-level "entities" object was in some cases truncated and incomplete due to the "RT @username " string being appended to Tweet message being Retweeted.  Note that if a Retweet gets Retweeted, the "retweet\_status" will still point to the original Tweet, meaning the intermediate Retweet is not included. Similar behavior is seen when using twitter.com to 'display' a Retweet. If you copy the unique Tweet ID assigned to the Retweet 'action', the original Tweet is displayed. 

Below is an example structure for a Retweet. Again, when parsing Retweets, it is key to parse the "retweeted\_status" object for complete (original) Tweet message and entity metadata.  
  

      `{ 	"tweet": { 		"text": "RT @author original message", 		"user": { 			"screen_name": "Retweeter" 		}, 		"retweeted_status": { 			"text": "original message", 			"user": { 				"screen_name": "OriginalTweeter" 			}, 			"place": {}, 			"entities": {}, 			"extended_entities": {} 		} 	}, 	"entities": {}, 	"extended_entities": {} }`
    

#### Quote Tweets

Quote Tweets are much like Retweets except that they include a new Tweet message. These new messages can contain their own set of hashtags, links, and other "entities" metadata. Quote Tweets can also include location information shared by the user posting the Quote Tweet, along with media such as GIFs, videos, and photos.

Quote Tweets will contain at least two Tweet objects, and in some cases, three. The Tweet being Quoted, which itself can be a Quoted Tweet, is provided in a "quoted\_status" object. The root-level object encapsulates the Quote Tweet itself, including a User object for the account taking the sharing action and the time of the Quote Tweet.

Note that Quote Tweets can now have photos, GIFs, or videos, added to them using the 'post Tweet' user-interface. When links to externally hosted media are included in the Quote Tweet message, the root-level "entities.urls" will describe those. Media attached to Quote Tweets will appear in the root-level "extended\_entities" metadata.

When Quote Tweets were first launched, a shortened link (t.co URL) was appended to the 'original' Tweet message and provided in the root-level "text" field. In addition, metadata for that t.co URL was included in the root-level 'entities.urls' array. In May 2018, we changed this so that the shortened t.co URL to the quoted Tweet _will not be included_ in the root-level "text" field. Second, the metadata for the quoted Tweet _will not be included_ in the "entities.urls" metadata. Instead, URL metadata for the quoted Tweet will be in a new "quoted\_status\_permalink" object on the root-level (or top-level), so at the same level of the "quoted\_status" object.

Below is an example structure for a Quote Tweet using this original formatting.   
  

      `{ 	"created_at": "Tue Feb 14 19:30:06 +0000 2017", 	"id_str": "831586333415976960", 	"text": "Definitely quotable! https:\/\/t.co\/J1LKrbHpWR", 	"user": { 		"screen_name": "happycamper" 	}, 	"quoted_status_id_str": "831569219296882688", 	"quoted_status": { 		"created_at": "Tue Feb 14 18:22:06 +0000 2017", 		"id_str": "831569219296882688", 		"text": "This is a test of the tweeting system \ud83d\ude0e to update #supportdocs @twitterboulder here: https:\/\/t.co\/NRq9UrSzm0", 		"user": { 			"screen_name": "furiouscamper", 		}, 		"place": { 			"id": "9a974dfc8efb32a0", 		}, 		"entities": { 			"hashtags": [{ 				"text": "supportdocs", 			}], 			"urls": [{ 			}], 			"user_mentions": [{	}], 			"symbols": [] 		}, 	}, 	"is_quote_status": true, 	"entities": {}, 	"matching_rules": [{}] }`
    

      `{ 	"created_at": "Fri Jan 04 18:47:16 +0000 2019", 	"id_str": "1081260794069671936", 	"text": "Quote test https://t.co/CE4m1qs3NJ", 	"user": { 		"screen_name": "furiouscamper" 	}, 	"place": null, 	"quoted_status_id_str": "1079578364904648705", 	"quoted_status": { 		"created_at": "Mon Dec 31 03:21:54 +0000 2018", 		"id_str": "1079578364904648705", 		"text": "AHHHHH", 		"user": { 			"screen_name": "infinite_scream" 		}, 		"place": null, 		"is_quote_status": false, 		"quote_count": 1, 		"reply_count": 0, 		"retweet_count": 3, 		"favorite_count": 6, 		"entities": { 			"hashtags": [], 			"urls": [], 			"user_mentions": [], 			"symbols": [] 		} 	}, 	"quoted_status_permalink": { 		"url": "https://t.co/CE4m1qs3NJ", 		"expanded": "https://twitter.com/infinite_scream/status/1079578364904648705", 		"display": "twitter.com/infinite_screa…" 	}, 	"is_quote_status": true, 	"quote_count": 0, 	"reply_count": 0, 	"retweet_count": 0, 	"favorite_count": 1, 	"entities": {} }`
    

### Extended Tweets

JSON that describes _Extended Tweets_ was introduced when 280-character Tweets were launched in November 2017. Tweet JSON was extended to encapsulate these longer messages, while not breaking the thousands of apps parsing these fundamental Twitter objects. To provide full backward compatibility, the original 140-character 'text' field, and the entity objects parsed from that, were retained. In the case of Tweets longer than 140 characters, this root-level 'text' field would become truncated and thus incomplete. Since the root-level 'entities' objects contain arrays of key metadata parsed from the 'text' message, such as included hashtags and links, these collections would be incomplete. For example, if a Tweet message was 200 characters long, with a hashtag included at the end, the legacy root-level 'entities.hashtags' array would not include it. 

A new 'extended\_tweet' field was introduced to hold the longer Tweet messages and complete entity metadata. The "extended\_tweet" object provides the "full\_text" field that contains the complete, untruncated Tweet message when longer than 140 characters. The "extended\_tweet" object also contains an "entities" object with complete arrays of hashtags, links, mentions, etc.

Extended Tweets are identified with a root-level "truncated" boolean. When true ("truncated": true), the "extended\_tweet" fields should be parsed instead of the root-level fields.

Note in the JSON example below that the root-level "text" field is truncated and the root-level "entities.hashtags" array is empty even though the Tweet message includes three hashtags. Since this is an Extended Tweet, the "truncated" field is set to true, and the "extended\_tweet" object provides complete "full\_text" and "entities" Tweet metadata.  
  

      `{ 	"created_at": "Thu May 10 17:41:57 +0000 2018", 	"id_str": "994633657141813248", 	"text": "Just another Extended Tweet with more than 140 characters, generated as a documentation example, showing that [\"tru… https://t.co/U7Se4NM7Eu", 	"display_text_range": [0, 140], 	"truncated": true, 	"user": { 		"id_str": "944480690", 		"screen_name": "FloodSocial" 	}, 	"extended_tweet": { 		"full_text": "Just another Extended Tweet with more than 140 characters, generated as a documentation example, showing that [\"truncated\": true] and the presence of an \"extended_tweet\" object with complete text and \"entities\" #documentation #parsingJSON #GeoTagged https://t.co/e9yhQTJSIA", 		"display_text_range": [0, 249], 		"entities": { 			"hashtags": [{ 				"text": "documentation", 				"indices": [211, 225] 			}, { 				"text": "parsingJSON", 				"indices": [226, 238] 			}, { 				"text": "GeoTagged", 				"indices": [239, 249] 			}] 		}  	}, 	"entities": { 		"hashtags": [] 	} }`
    

### Next Steps

Explore the other sub-objects that a Tweet contains:

* [User object and data dictionary](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/user)
* [Entities object and data dictionary](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/entities)
* [Extended Entities object and data dictionary](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/extended-entities)
* [Tweet geo objects and data dictionaries](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/geo)

User object

User object
-----------

The User object contains Twitter User account metadata that describes the Twitter User referenced. 

### User Data Dictionary

| Attribute | Type | Description |
| --- | --- | --- |
| id  | Int64 | The integer representation of the unique identifier for this User. This number is greater than 53 bits and some programming languages may have difficulty/silent defects in interpreting it. Using a signed 64 bit integer for storing this identifier is safe. Use `id_str` to fetch the identifier to be safe. See [Twitter IDs](https://developer.twitter.com/en/docs/twitter-ids) for more information. Example:<br><br>"id": 6253282 |
| id\_str | String | The string representation of the unique identifier for this User. Implementations should use this rather than the large, possibly un-consumable integer in `id`. Example:<br><br>"id\_str": "6253282" |
| name | String | The name of the user, as they’ve defined it. Not necessarily a person’s name. Typically capped at 50 characters, but subject to change. Example:<br><br>"name": "Twitter API" |
| screen\_name | String | The screen name, handle, or alias that this user identifies themselves with. screen\_names are unique but subject to change. Use `id_str` as a user identifier whenever possible. Typically a maximum of 15 characters long, but some historical accounts may exist with longer names. Example:<br><br>"screen\_name": "twitterapi" |
| location | String | _Nullable_ . The user-defined location for this account’s profile. Not necessarily a location, nor machine-parseable. This field will occasionally be fuzzily interpreted by the Search service. Example:<br><br>"location": "San Francisco, CA" |
| derived | Arrays of Enrichment Objects | Enterprise APIs only Collection of Enrichment metadata derived for user. Provides the [_Profile Geo_](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/enrichments/overview/profile-geo) Enrichment metadata. See referenced documentation for more information, including JSON data dictionaries. Example:<br><br>"derived":{"locations": \[{"country":"United States","country\_code":"US","locality":"Denver"}\]} |
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

      `"user": { 		"id": 2244994945, 		"id_str": "2244994945", 		"name": "Twitter Dev", 		"screen_name": "TwitterDev", 		"location": "127.0.0.1", 		"url": "https://developer.twitter.com/en/community", 		"description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.", 		"translator_type": "regular", 		"protected": false, 		"verified": true, 		"followers_count": 512292, 		"friends_count": 2038, 		"listed_count": 1666, 		"favourites_count": 2147, 		"statuses_count": 3634, 		"created_at": "Sat Dec 14 04:35:55 +0000 2013", 		"utc_offset": null, 		"time_zone": null, 		"geo_enabled": true, 		"lang": null, 		"contributors_enabled": false, 		"is_translator": false, 		"profile_background_color": "FFFFFF", 		"profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png", 		"profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png", 		"profile_background_tile": false, 		"profile_link_color": "0084B4", 		"profile_sidebar_border_color": "FFFFFF", 		"profile_sidebar_fill_color": "DDEEF6", 		"profile_text_color": "333333", 		"profile_use_background_image": false, 		"profile_image_url": "http://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg", 		"profile_image_url_https": "https://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg", 		"profile_banner_url": "https://pbs.twimg.com/profile_banners/2244994945/1594913664", 		"default_profile": false, 		"default_profile_image": false, 		"following": null, 		"follow_request_sent": null, 		"notifications": null 	}`
    

### Next Steps

Explore the other sub-objects that a Tweet contains:

* [Tweet object and data dictionary](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/tweet)
* [Entities object and data dictionary](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/entities)
* [Extended Entities object and data dictionary](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/extended-entities)
* [Tweet geo objects and data dictionaries](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/geo)

Geo objects

Geo Objects
-----------

Tweets can be associated with a location, generating a Tweet that has been ‘geo-tagged.’ Tweet locations can be assigned by using the Twitter user-interface or when posting a Tweet using the API. Tweet locations can be an exact ‘point’ location, or a Twitter Place with a ‘bounding box’ that describes a larger area ranging from a venue to an entire region.

There are three ‘root-level’ JSON objects used to describe the location associated with a Tweet: [place](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/place-dictionary), [geo](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/geo) and [coordinates](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/coordinates). 

Additionally, the native enriched format includes the [profile geo enrichment's](https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/profile-geo.html) [derived location](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/derived-location) within the user object.

The `place` object is always present when a Tweet is geo-tagged with a place,. Places are specific, named locations with corresponding geo coordinates. When users decide to assign a location to their Tweet, they are presented with a list of candidate Twitter Places. When using the API to post a Tweet, a Twitter Place can be attached by specifying a place\_id when posting the Tweet. Tweets associated with Places are not necessarily issued from that location but could also potentially be _about_ that location.

The geo and `coordinates` objects only present (non-null) when the Tweet is assigned an _exact location_. If an exact location is provided, the `coordinates` object will provide a \[long, lat\] array with the geographical coordinates, and a Twitter Place that corresponds to that location will be assigned.

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

### Geo object data dictionary

|     |     |     |
| --- | --- | --- |
| Field | Type | Description |
| coordinates | Collection of Float | The longitude and latitude of the Tweet’s location, as a collection in the form **\[latitude, longitude\]**. Example:<br><br>  **"geo": {**<br><br>    **"type":** "Point"**,**<br><br>    **"coordinates": \[**<br><br>      54.27784**,**<br><br>      \-0.41068<br><br>    **\]**<br><br>  **}** |
| type | String | The type of data encoded in the coordinates property. This will be “Point” for Tweet coordinates fields. Example:<br><br>"type": "Point" |

Coordinates object data dictionary
----------------------------------

|     |     |     |
| --- | --- | --- |
| Field | Type | Description |
| coordinates | Collection of Float | The longitude and latitude of the Tweet’s location, as a collection in the form **\[longitude, latitude\]**. Example:<br><br>  **"coordinates": {**<br><br>    **"type":** "Point"**,**<br><br>    **"coordinates": \[**<br><br>      \-0.41068**,**<br><br>      54.27784<br><br>    **\]**<br><br>  **}** |
| type | String | The type of data encoded in the coordinates property. This will be “Point” for Tweet coordinates fields. Example:<br><br>"type": "Point" |

### Derived locations

|     |     |     |
| --- | --- | --- |
| Field | Type | Description |
| derived | locations object | Derived location from the profile geo enrichement  <br>  <br>    **"derived": {**<br><br>      **"locations": \[**<br><br>        **{**<br><br>          **"country":** "United Kingdom"**,**<br><br>          **"country\_code":** "GB"**,**<br><br>          **"locality":** "Yorkshire"**,**<br><br>          **"region":** "England"**,**<br><br>          **"full\_name":** "Yorkshire, England, United Kingdom"**,**<br><br>          **"geo": {**<br><br>            **"coordinates": \[**<br><br>              \-1.5**,**<br><br>              54<br><br>            **\],**<br><br>            **"type":** "point"<br><br>          **}**<br><br>        **}**<br><br>      **\]**<br><br>    **}** |

### Examples:

      `{   "geo": null,   "coordinates": null,   "place": {     "id": "07d9db48bc083000",     "url": "https://api.twitter.com/1.1/geo/id/07d9db48bc083000.json",     "place_type": "poi",     "name": "McIntosh Lake",     "full_name": "McIntosh Lake",     "country_code": "US",     "country": "United States",     "bounding_box": {       "type": "Polygon",       "coordinates": [         [           [             -105.14544,             40.192138           ],           [             -105.14544,             40.192138           ],           [             -105.14544,             40.192138           ],           [             -105.14544,             40.192138           ]         ]       ]     },     "attributes": {            }   } }`
    

      `{   "geo": {     "type": "Point",     "coordinates": [       40.74118764,       -73.9998279     ]   },   "coordinates": {     "type": "Point",     "coordinates": [       -73.9998279,       40.74118764     ]   },   "place": {     "id": "01a9a39529b27f36",     "url": "https://api.twitter.com/1.1/geo/id/01a9a39529b27f36.json",     "place_type": "city",     "name": "Manhattan",     "full_name": "Manhattan, NY",     "country_code": "US",     "country": "United States",     "bounding_box": {       "type": "Polygon",       "coordinates": [         [           [             -74.026675,             40.683935           ],           [             -74.026675,             40.877483           ],           [             -73.910408,             40.877483           ],           [             -73.910408,             40.683935           ]         ]       ]     },     "attributes": {            }   } }`
    

### Next Steps

Explore the other sub-objects that a Tweet contains:

* [Tweet object and data dictionary](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/tweet)
* [User object and data dictionary](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/user)
* [Entities object and data dictionary](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/entities)
* [Extended Entities object and data dictionary](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/extended-entities)

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

Beyond providing parsing conveniences, the `entities` section also provides useful ‘value-add’ metadata. For example, if you are using the [Enhanced URLs enrichment](https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/expanded-and-enhanced-urls), URL metadata include fully-expanded URLs, as well as associated website titles and descriptions. Another example is when there are user mentions, the entities metadata include the numeric user ID, which are useful when making requests to many Twitter APIs.

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
* if you are working with native media (photos, videos, or GIFs), the [Extended Entities object](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/extended-entities) is the way to go.

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
| large | [Size Object](#size) | Information for a large-sized version of the media. Example:<br><br>"large":{"h":454, "resize":"fit", "w":680}<br><br>Small-sized photo media will be limited to _fit_ within a 680x680 boundary. |
| medium | [Size Object](#size) | Information for a medium-sized version of the media. Example:<br><br>"medium":{"h":800, "resize":"fit", "w":1200}<br><br>Medium-sized photo media will be limited to _fit_ within a 1200x1200 boundary. |
| small | [Size Object](#size) | Information for a small-sized version of the media. Example:<br><br>"small":{"h":1366, "resize":"fit", "w":2048}<br><br>Large-sized photo media will be limited to _fit_ within a 2048x2048 boundary. |

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

The `has:links` Operator will match if there is at least one item in the array. The `url:` Operator is used to match on the `expanded_url` attribute. If you are using the [Expanded URL enrichment](http://support.gnip.com/enrichments/expanded_urls.html), the `url:` Operator is used to match on the `unwound.url` (fully unwound URL) attribute. If you are using the [Exhanced URL enrichment](http://support.gnip.com/enrichments/enhanced_urls.html), the `url_title:` and `url_decription:` Operators are used to match on the `unwound.title` and `unwound.description` attributes.

|     |     |     |
| --- | --- | --- |
| Field | Type | Description |
| display\_url | String | URL pasted/typed into Tweet. Example:<br><br>"display\_url":"bit.ly/2so49n2" |
| expanded\_url | String | Expanded version of \`\` display\_url\`\` . Example:<br><br>"expanded\_url":"http://bit.ly/2so49n2" |
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

* Volume streams ([Decahose](https://developer.twitter.com/en/docs/twitter-api/enterprise/decahose-api/overview) )
* [Real-time PowerTrack](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/overview)
* [Historical PowerTrack](https://developer.twitter.com/en/docs/twitter-api/enterprise/historical-powertrack-api/overview)
* Twitter Search APIs ([Full-Archive Search](https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/overview) and [30-Day Search](https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/overview))

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
    

### Next Steps

Explore the other sub-objects that a Tweet contains:

* [Tweet object and data dictionary](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/tweet)
* [User object and data dictionary](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/user)
* [Extended Entities object and data dictionary](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/extended-entities)
* [Tweet geo objects and data dictionaries](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/geo)

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

### Next Steps

Explore the other sub-objects that a Tweet contains:

* [Tweet object and data dictionary](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/tweet)
* [User object and data dictionary](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/user)
* [Entities object and data dictionary](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/entities)
* [Tweet geo objects and data dictionaries](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/geo)

Native Enriched example payloads

### Tweet

      `{ 	"created_at": "Fri Sep 18 18:36:15 +0000 2020", 	"id": 1307025659294675000, 	"id_str": "1307025659294674945", 	"text": "Here’s an article that highlights the updates in the new Tweet payload v2 https://t.co/oeF3ZHeKQQ", 	"source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>", 	"truncated": false, 	"in_reply_to_status_id": 1304102743196356600, 	"in_reply_to_status_id_str": "1304102743196356610", 	"in_reply_to_user_id": 2244994945, 	"in_reply_to_user_id_str": "2244994945", 	"in_reply_to_screen_name": "TwitterDev", 	"user": { 		"id": 2244994945, 		"id_str": "2244994945", 		"name": "Twitter Dev", 		"screen_name": "TwitterDev", 		"location": "127.0.0.1", 		"url": "https://developer.twitter.com/en/community", 		"description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.", 		"translator_type": "regular", 		"protected": false, 		"verified": true, 		"followers_count": 512292, 		"friends_count": 2038, 		"listed_count": 1666, 		"favourites_count": 2147, 		"statuses_count": 3634, 		"created_at": "Sat Dec 14 04:35:55 +0000 2013", 		"utc_offset": null, 		"time_zone": null, 		"geo_enabled": true, 		"lang": null, 		"contributors_enabled": false, 		"is_translator": false, 		"profile_background_color": "FFFFFF", 		"profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png", 		"profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png", 		"profile_background_tile": false, 		"profile_link_color": "0084B4", 		"profile_sidebar_border_color": "FFFFFF", 		"profile_sidebar_fill_color": "DDEEF6", 		"profile_text_color": "333333", 		"profile_use_background_image": false, 		"profile_image_url": "http://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg", 		"profile_image_url_https": "https://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg", 		"profile_banner_url": "https://pbs.twimg.com/profile_banners/2244994945/1594913664", 		"default_profile": false, 		"default_profile_image": false, 		"following": null, 		"follow_request_sent": null, 		"notifications": null 	}, 	"geo": null, 	"coordinates": null, 	"place": null, 	"contributors": null, 	"is_quote_status": false, 	"quote_count": 1, 	"reply_count": 2, 	"retweet_count": 11, 	"favorite_count": 70, 	"entities": { 		"hashtags": [], 		"urls": [{ 			"url": "https://t.co/oeF3ZHeKQQ", 			"expanded_url": "https://dev.to/twitterdev/understanding-the-new-tweet-payload-in-the-twitter-api-v2-1fg5", 			"display_url": "dev.to/twitterdev/und…", 			"unwound": { 				"url": "https://dev.to/twitterdev/understanding-the-new-tweet-payload-in-the-twitter-api-v2-1fg5", 				"status": 200, 				"title": "Understanding the new Tweet payload in the Twitter API v2", 				"description": "Twitter recently announced the new Twitter API v2, rebuilt from the ground up to deliver new features..." 			}, 			"indices": [ 				74, 				97 			] 		}], 		"user_mentions": [], 		"symbols": [] 	}, 	"favorited": false, 	"retweeted": false, 	"possibly_sensitive": false, 	"filter_level": "low", 	"lang": "en", 	"matching_rules": [{ 		"tag": null 	}] }`
    

### Tweet reply

      `{ 	"created_at": "Fri Aug 21 19:10:05 +0000 2020", 	"id": 1296887316556980200, 	"id_str": "1296887316556980230", 	"text": "See how @PennMedCDH are using Twitter data to understand the COVID-19 health crisis 📊\n\nhttps://t.co/1tdA8uDWes", 	"source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>", 	"truncated": false, 	"in_reply_to_status_id": 1296887091901718500, 	"in_reply_to_status_id_str": "1296887091901718529", 	"in_reply_to_user_id": 2244994945, 	"in_reply_to_user_id_str": "2244994945", 	"in_reply_to_screen_name": "TwitterDev", 	"user": { 		"id": 2244994945, 		"id_str": "2244994945", 		"name": "Twitter Dev", 		"screen_name": "TwitterDev", 		"location": "127.0.0.1", 		"url": "https://developer.twitter.com/en/community", 		"description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.", 		"translator_type": "regular", 		"protected": false, 		"verified": true, 		"followers_count": 512292, 		"friends_count": 2038, 		"listed_count": 1666, 		"favourites_count": 2147, 		"statuses_count": 3634, 		"created_at": "Sat Dec 14 04:35:55 +0000 2013", 		"utc_offset": null, 		"time_zone": null, 		"geo_enabled": true, 		"lang": null, 		"contributors_enabled": false, 		"is_translator": false, 		"profile_background_color": "FFFFFF", 		"profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png", 		"profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png", 		"profile_background_tile": false, 		"profile_link_color": "0084B4", 		"profile_sidebar_border_color": "FFFFFF", 		"profile_sidebar_fill_color": "DDEEF6", 		"profile_text_color": "333333", 		"profile_use_background_image": false, 		"profile_image_url": "http://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg", 		"profile_image_url_https": "https://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg", 		"profile_banner_url": "https://pbs.twimg.com/profile_banners/2244994945/1594913664", 		"default_profile": false, 		"default_profile_image": false, 		"following": null, 		"follow_request_sent": null, 		"notifications": null 	}, 	"geo": null, 	"coordinates": null, 	"place": null, 	"contributors": null, 	"is_quote_status": false, 	"quote_count": 2, 	"reply_count": 3, 	"retweet_count": 9, 	"favorite_count": 26, 	"entities": { 		"hashtags": [], 		"urls": [{ 			"url": "https://t.co/1tdA8uDWes", 			"expanded_url": "https://developer.twitter.com/en/use-cases/success-stories/penn", 			"display_url": "developer.twitter.com/en/use-cases/s…", 			"unwound": { 				"url": "https://developer.twitter.com/en/use-cases/success-stories/penn", 				"status": 200, 				"title": "Penn Medicine Center for Digital Health", 				"description": "Penn Med Center for Digital Health has created a COVID-19 Twitter map that includes charts detailing sentiment, symptoms reported, state-by-state data cuts, and border data on the COVID-19 outbreak. In addition, their Penn Med With You initiative uses aggregate regional information from Twitter to inform their website and text-messaging service. The service uses this information to disseminate relevant and timely resources." 			}, 			"indices": [ 				87, 				110 			] 		}], 		"user_mentions": [{ 			"screen_name": "PennMedCDH", 			"name": "Penn Med CDH", 			"id": 1615654896, 			"id_str": "1615654896", 			"indices": [ 				8, 				19 			] 		}], 		"symbols": [] 	}, 	"favorited": false, 	"retweeted": false, 	"possibly_sensitive": false, 	"filter_level": "low", 	"lang": "en", 	"matching_rules": [{ 		"tag": null 	}] }`
    

### Extended Tweet

      `{ 	"created_at": "Wed Aug 19 16:26:16 +0000 2020", 	"id": 1296121314218897400, 	"id_str": "1296121314218897408", 	"text": "The hide replies endpoint is launching today! \n\nDevelopers can hide replies to Tweets - a crucial way developers ca… https://t.co/VyfXs1RTXn", 	"source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>", 	"truncated": true, 	"in_reply_to_status_id": null, 	"in_reply_to_status_id_str": null, 	"in_reply_to_user_id": null, 	"in_reply_to_user_id_str": null, 	"in_reply_to_screen_name": null, 	"user": { 		"id": 2244994945, 		"id_str": "2244994945", 		"name": "Twitter Dev", 		"screen_name": "TwitterDev", 		"location": "127.0.0.1", 		"url": "https://developer.twitter.com/en/community", 		"description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.", 		"translator_type": "regular", 		"protected": false, 		"verified": true, 		"followers_count": 512292, 		"friends_count": 2038, 		"listed_count": 1666, 		"favourites_count": 2147, 		"statuses_count": 3634, 		"created_at": "Sat Dec 14 04:35:55 +0000 2013", 		"utc_offset": null, 		"time_zone": null, 		"geo_enabled": true, 		"lang": null, 		"contributors_enabled": false, 		"is_translator": false, 		"profile_background_color": "FFFFFF", 		"profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png", 		"profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png", 		"profile_background_tile": false, 		"profile_link_color": "0084B4", 		"profile_sidebar_border_color": "FFFFFF", 		"profile_sidebar_fill_color": "DDEEF6", 		"profile_text_color": "333333", 		"profile_use_background_image": false, 		"profile_image_url": "http://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg", 		"profile_image_url_https": "https://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg", 		"profile_banner_url": "https://pbs.twimg.com/profile_banners/2244994945/1594913664", 		"default_profile": false, 		"default_profile_image": false, 		"following": null, 		"follow_request_sent": null, 		"notifications": null 	}, 	"geo": null, 	"coordinates": null, 	"place": null, 	"contributors": null, 	"is_quote_status": false, 	"extended_tweet": { 		"full_text": "The hide replies endpoint is launching today! \n\nDevelopers can hide replies to Tweets - a crucial way developers can help improve the health of the public conversation using the #TwitterAPI.\n\nhttps://t.co/khXhTurm9x", 		"display_text_range": [ 			0, 			215 		], 		"entities": { 			"hashtags": [{ 				"text": "TwitterAPI", 				"indices": [ 					178, 					189 				] 			}], 			"urls": [{ 				"url": "https://t.co/khXhTurm9x", 				"expanded_url": "https://twittercommunity.com/t/hide-replies-now-available-in-the-new-twitter-api/140996", 				"display_url": "twittercommunity.com/t/hide-replies…", 				"unwound": { 					"url": "https://twittercommunity.com/t/hide-replies-now-available-in-the-new-twitter-api/140996", 					"status": 200, 					"title": "Hide replies now available in the new Twitter API", 					"description": "Today, we’re happy to announce the general availability of the hide replies endpoint in the new Twitter API. The hide replies endpoint allows you to build tools that help people hide or unhide replies to their Tweets. People manage their replies for many reasons, including to give less attention to comments that are abusive, distracting, misleading, or to make conversations more engaging. Through this endpoint, you can build tools to help people on Twitter hide or unhide replies faster and more..." 				}, 				"indices": [ 					192, 					215 				] 			}], 			"user_mentions": [], 			"symbols": [] 		} 	}, 	"quote_count": 23, 	"reply_count": 9, 	"retweet_count": 54, 	"favorite_count": 172, 	"entities": { 		"hashtags": [], 		"urls": [{ 			"url": "https://t.co/VyfXs1RTXn", 			"expanded_url": "https://twitter.com/i/web/status/1296121314218897408", 			"display_url": "twitter.com/i/web/status/1…", 			"indices": [ 				117, 				140 			] 		}], 		"user_mentions": [], 		"symbols": [] 	}, 	"favorited": false, 	"retweeted": false, 	"possibly_sensitive": false, 	"filter_level": "low", 	"lang": "en", 	"matching_rules": [{ 		"tag": null 	}] }`
    

### Tweet with extended\_entitites

      `{ 	"created_at": "Wed Aug 12 17:01:42 +0000 2020", 	"id": 1293593516040269800, 	"id_str": "1293593516040269825", 	"text": "It’s finally here! 🥁 Say hello to the new #TwitterAPI.\n\nWe’re rebuilding the Twitter API v2 from the ground up to b… https://t.co/UeCndQGMjx", 	"display_text_range": [ 		0, 		140 	], 	"source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>", 	"truncated": true, 	"in_reply_to_status_id": null, 	"in_reply_to_status_id_str": null, 	"in_reply_to_user_id": null, 	"in_reply_to_user_id_str": null, 	"in_reply_to_screen_name": null, 	"user": { 		"id": 2244994945, 		"id_str": "2244994945", 		"name": "Twitter Dev", 		"screen_name": "TwitterDev", 		"location": "127.0.0.1", 		"url": "https://developer.twitter.com/en/community", 		"description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.", 		"translator_type": "regular", 		"protected": false, 		"verified": true, 		"followers_count": 512292, 		"friends_count": 2038, 		"listed_count": 1666, 		"favourites_count": 2147, 		"statuses_count": 3634, 		"created_at": "Sat Dec 14 04:35:55 +0000 2013", 		"utc_offset": null, 		"time_zone": null, 		"geo_enabled": true, 		"lang": null, 		"contributors_enabled": false, 		"is_translator": false, 		"profile_background_color": "FFFFFF", 		"profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png", 		"profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png", 		"profile_background_tile": false, 		"profile_link_color": "0084B4", 		"profile_sidebar_border_color": "FFFFFF", 		"profile_sidebar_fill_color": "DDEEF6", 		"profile_text_color": "333333", 		"profile_use_background_image": false, 		"profile_image_url": "http://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg", 		"profile_image_url_https": "https://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg", 		"profile_banner_url": "https://pbs.twimg.com/profile_banners/2244994945/1594913664", 		"default_profile": false, 		"default_profile_image": false, 		"following": null, 		"follow_request_sent": null, 		"notifications": null 	}, 	"geo": null, 	"coordinates": null, 	"place": null, 	"contributors": null, 	"is_quote_status": false, 	"extended_tweet": { 		"full_text": "It’s finally here! 🥁 Say hello to the new #TwitterAPI.\n\nWe’re rebuilding the Twitter API v2 from the ground up to better serve our developer community. And today’s launch is only the beginning.\n\nhttps://t.co/32VrwpGaJw https://t.co/KaFSbjWUA8", 		"display_text_range": [ 			0, 			218 		], 		"entities": { 			"hashtags": [{ 				"text": "TwitterAPI", 				"indices": [ 					42, 					53 				] 			}], 			"urls": [{ 				"url": "https://t.co/32VrwpGaJw", 				"expanded_url": "https://blog.twitter.com/developer/en_us/topics/tools/2020/introducing_new_twitter_api.html", 				"display_url": "blog.twitter.com/developer/en_u…", 				"unwound": { 					"url": "https://blog.twitter.com/developer/en_us/topics/tools/2020/introducing_new_twitter_api.html", 					"status": 200, 					"title": "Introducing a new and improved Twitter API", 					"description": "Introducing the new Twitter API - rebuilt from the ground up to deliver new features faster so developers can help the world connect to the public conversation happening on Twitter." 				}, 				"indices": [ 					195, 					218 				] 			}], 			"user_mentions": [], 			"symbols": [], 			"media": [{ 				"id": 1293565706408038400, 				"id_str": "1293565706408038401", 				"indices": [ 					219, 					242 				], 				"additional_media_info": { 					"monetizable": false 				}, 				"media_url": "http://pbs.twimg.com/ext_tw_video_thumb/1293565706408038401/pu/img/66P2dvbU4a02jYbV.jpg", 				"media_url_https": "https://pbs.twimg.com/ext_tw_video_thumb/1293565706408038401/pu/img/66P2dvbU4a02jYbV.jpg", 				"url": "https://t.co/KaFSbjWUA8", 				"display_url": "pic.twitter.com/KaFSbjWUA8", 				"expanded_url": "https://twitter.com/TwitterDev/status/1293593516040269825/video/1", 				"type": "video", 				"video_info": { 					"aspect_ratio": [ 						16, 						9 					], 					"duration_millis": 34875, 					"variants": [{ 							"bitrate": 256000, 							"content_type": "video/mp4", 							"url": "https://video.twimg.com/ext_tw_video/1293565706408038401/pu/vid/480x270/Fg9lnGGsITO0uq2K.mp4?tag=10" 						}, 						{ 							"bitrate": 832000, 							"content_type": "video/mp4", 							"url": "https://video.twimg.com/ext_tw_video/1293565706408038401/pu/vid/640x360/-crbtZE4y8vKN_uF.mp4?tag=10" 						}, 						{ 							"content_type": "application/x-mpegURL", 							"url": "https://video.twimg.com/ext_tw_video/1293565706408038401/pu/pl/OvIqQojosF6sMIHR.m3u8?tag=10" 						}, 						{ 							"bitrate": 2176000, 							"content_type": "video/mp4", 							"url": "https://video.twimg.com/ext_tw_video/1293565706408038401/pu/vid/1280x720/xkxyb-VPVY4OI0j9.mp4?tag=10" 						} 					] 				}, 				"sizes": { 					"thumb": { 						"w": 150, 						"h": 150, 						"resize": "crop" 					}, 					"medium": { 						"w": 1200, 						"h": 675, 						"resize": "fit" 					}, 					"small": { 						"w": 680, 						"h": 383, 						"resize": "fit" 					}, 					"large": { 						"w": 1280, 						"h": 720, 						"resize": "fit" 					} 				} 			}] 		}, 		"extended_entities": { 			"media": [{ 				"id": 1293565706408038400, 				"id_str": "1293565706408038401", 				"indices": [ 					219, 					242 				], 				"additional_media_info": { 					"monetizable": false 				}, 				"media_url": "http://pbs.twimg.com/ext_tw_video_thumb/1293565706408038401/pu/img/66P2dvbU4a02jYbV.jpg", 				"media_url_https": "https://pbs.twimg.com/ext_tw_video_thumb/1293565706408038401/pu/img/66P2dvbU4a02jYbV.jpg", 				"url": "https://t.co/KaFSbjWUA8", 				"display_url": "pic.twitter.com/KaFSbjWUA8", 				"expanded_url": "https://twitter.com/TwitterDev/status/1293593516040269825/video/1", 				"type": "video", 				"video_info": { 					"aspect_ratio": [ 						16, 						9 					], 					"duration_millis": 34875, 					"variants": [{ 							"bitrate": 256000, 							"content_type": "video/mp4", 							"url": "https://video.twimg.com/ext_tw_video/1293565706408038401/pu/vid/480x270/Fg9lnGGsITO0uq2K.mp4?tag=10" 						}, 						{ 							"bitrate": 832000, 							"content_type": "video/mp4", 							"url": "https://video.twimg.com/ext_tw_video/1293565706408038401/pu/vid/640x360/-crbtZE4y8vKN_uF.mp4?tag=10" 						}, 						{ 							"content_type": "application/x-mpegURL", 							"url": "https://video.twimg.com/ext_tw_video/1293565706408038401/pu/pl/OvIqQojosF6sMIHR.m3u8?tag=10" 						}, 						{ 							"bitrate": 2176000, 							"content_type": "video/mp4", 							"url": "https://video.twimg.com/ext_tw_video/1293565706408038401/pu/vid/1280x720/xkxyb-VPVY4OI0j9.mp4?tag=10" 						} 					] 				}, 				"sizes": { 					"thumb": { 						"w": 150, 						"h": 150, 						"resize": "crop" 					}, 					"medium": { 						"w": 1200, 						"h": 675, 						"resize": "fit" 					}, 					"small": { 						"w": 680, 						"h": 383, 						"resize": "fit" 					}, 					"large": { 						"w": 1280, 						"h": 720, 						"resize": "fit" 					} 				} 			}] 		} 	}, 	"quote_count": 332, 	"reply_count": 172, 	"retweet_count": 958, 	"favorite_count": 2844, 	"entities": { 		"hashtags": [{ 			"text": "TwitterAPI", 			"indices": [ 				42, 				53 			] 		}], 		"urls": [{ 			"url": "https://t.co/UeCndQGMjx", 			"expanded_url": "https://twitter.com/i/web/status/1293593516040269825", 			"display_url": "twitter.com/i/web/status/1…", 			"indices": [ 				117, 				140 			] 		}], 		"user_mentions": [], 		"symbols": [] 	}, 	"favorited": false, 	"retweeted": false, 	"possibly_sensitive": false, 	"filter_level": "low", 	"lang": "en", 	"matching_rules": [{ 		"tag": null 	}] }`
    

### Retweet

      `{ 	"created_at": "Tue Feb 18 19:33:59 +0000 2020", 	"id": 1229851574555508700, 	"id_str": "1229851574555508737", 	"text": "RT @suhemparack: I built an Alexa Skill for Twitter using APL that allows you to view Tweets and Trends on the echo show!\n\nCheck it out her…", 	"source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>", 	"truncated": false, 	"in_reply_to_status_id": null, 	"in_reply_to_status_id_str": null, 	"in_reply_to_user_id": null, 	"in_reply_to_user_id_str": null, 	"in_reply_to_screen_name": null, 	"user": { 		"id": 2244994945, 		"id_str": "2244994945", 		"name": "Twitter Dev", 		"screen_name": "TwitterDev", 		"location": "127.0.0.1", 		"url": "https://developer.twitter.com/en/community", 		"description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.", 		"translator_type": "regular", 		"protected": false, 		"verified": true, 		"followers_count": 512292, 		"friends_count": 2038, 		"listed_count": 1666, 		"favourites_count": 2147, 		"statuses_count": 3634, 		"created_at": "Sat Dec 14 04:35:55 +0000 2013", 		"utc_offset": null, 		"time_zone": null, 		"geo_enabled": true, 		"lang": null, 		"contributors_enabled": false, 		"is_translator": false, 		"profile_background_color": "FFFFFF", 		"profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png", 		"profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png", 		"profile_background_tile": false, 		"profile_link_color": "0084B4", 		"profile_sidebar_border_color": "FFFFFF", 		"profile_sidebar_fill_color": "DDEEF6", 		"profile_text_color": "333333", 		"profile_use_background_image": false, 		"profile_image_url": "http://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg", 		"profile_image_url_https": "https://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg", 		"profile_banner_url": "https://pbs.twimg.com/profile_banners/2244994945/1594913664", 		"default_profile": false, 		"default_profile_image": false, 		"following": null, 		"follow_request_sent": null, 		"notifications": null 	}, 	"geo": null, 	"coordinates": null, 	"place": null, 	"contributors": null, 	"retweeted_status": { 		"created_at": "Tue Feb 18 19:01:58 +0000 2020", 		"id": 1229843515603144700, 		"id_str": "1229843515603144704", 		"text": "I built an Alexa Skill for Twitter using APL that allows you to view Tweets and Trends on the echo show!\n\nCheck it… https://t.co/RP9NgltX7i", 		"source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>", 		"truncated": true, 		"in_reply_to_status_id": null, 		"in_reply_to_status_id_str": null, 		"in_reply_to_user_id": null, 		"in_reply_to_user_id_str": null, 		"in_reply_to_screen_name": null, 		"user": { 			"id": 857699969263964200, 			"id_str": "857699969263964161", 			"name": "Suhem Parack", 			"screen_name": "suhemparack", 			"location": "Seattle, WA", 			"url": "https://developer.twitter.com", 			"description": "Developer Relations for Academic Research @Twitter. Talk to me about research with Twitter data. Previously: Amazon Alexa. Views are my own", 			"translator_type": "none", 			"protected": false, 			"verified": false, 			"followers_count": 732, 			"friends_count": 501, 			"listed_count": 12, 			"favourites_count": 358, 			"statuses_count": 458, 			"created_at": "Thu Apr 27 20:56:22 +0000 2017", 			"utc_offset": null, 			"time_zone": null, 			"geo_enabled": false, 			"lang": null, 			"contributors_enabled": false, 			"is_translator": false, 			"profile_background_color": "F5F8FA", 			"profile_background_image_url": "", 			"profile_background_image_url_https": "", 			"profile_background_tile": false, 			"profile_link_color": "1DA1F2", 			"profile_sidebar_border_color": "C0DEED", 			"profile_sidebar_fill_color": "DDEEF6", 			"profile_text_color": "333333", 			"profile_use_background_image": true, 			"profile_image_url": "http://pbs.twimg.com/profile_images/1230703695051935747/TbQKe91L_normal.jpg", 			"profile_image_url_https": "https://pbs.twimg.com/profile_images/1230703695051935747/TbQKe91L_normal.jpg", 			"profile_banner_url": "https://pbs.twimg.com/profile_banners/857699969263964161/1593055939", 			"default_profile": true, 			"default_profile_image": false, 			"following": null, 			"follow_request_sent": null, 			"notifications": null 		}, 		"geo": null, 		"coordinates": null, 		"place": null, 		"contributors": null, 		"is_quote_status": false, 		"extended_tweet": { 			"full_text": "I built an Alexa Skill for Twitter using APL that allows you to view Tweets and Trends on the echo show!\n\nCheck it out here 👇\n\nhttps://t.co/l5J8wq748G", 			"display_text_range": [ 				0, 				150 			], 			"entities": { 				"hashtags": [], 				"urls": [{ 					"url": "https://t.co/l5J8wq748G", 					"expanded_url": "https://dev.to/twitterdev/building-an-alexa-skill-for-twitter-using-alexa-presentation-language-1aj0", 					"display_url": "dev.to/twitterdev/bui…", 					"unwound": { 						"url": "https://dev.to/twitterdev/building-an-alexa-skill-for-twitter-using-alexa-presentation-language-1aj0", 						"status": 200, 						"title": null, 						"description": null 					}, 					"indices": [ 						127, 						150 					] 				}], 				"user_mentions": [], 				"symbols": [] 			} 		}, 		"quote_count": 6, 		"reply_count": 1, 		"retweet_count": 19, 		"favorite_count": 71, 		"entities": { 			"hashtags": [], 			"urls": [{ 				"url": "https://t.co/RP9NgltX7i", 				"expanded_url": "https://twitter.com/i/web/status/1229843515603144704", 				"display_url": "twitter.com/i/web/status/1…", 				"indices": [ 					116, 					139 				] 			}], 			"user_mentions": [], 			"symbols": [] 		}, 		"favorited": false, 		"retweeted": false, 		"possibly_sensitive": false, 		"filter_level": "low", 		"lang": "en" 	}, 	"is_quote_status": false, 	"quote_count": 0, 	"reply_count": 0, 	"retweet_count": 0, 	"favorite_count": 0, 	"entities": { 		"hashtags": [], 		"urls": [], 		"user_mentions": [{ 			"screen_name": "suhemparack", 			"name": "Suhem Parack", 			"id": 857699969263964200, 			"id_str": "857699969263964161", 			"indices": [ 				3, 				15 			] 		}], 		"symbols": [] 	}, 	"favorited": false, 	"retweeted": false, 	"filter_level": "low", 	"lang": "en", 	"matching_rules": [{ 		"tag": null 	}] }`
    

### Quote Tweet

      `{ 	"created_at": "Mon Nov 16 18:09:36 +0000 2020", 	"id": 1328399838128468000, 	"id_str": "1328399838128467969", 	"text": "As planned, the Labs v2 endpoints referenced below have now been retired. Please let us know in the forums if you h… https://t.co/ahQvTYaOcZ", 	"display_text_range": [ 		0, 		140 	], 	"source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>", 	"truncated": true, 	"in_reply_to_status_id": null, 	"in_reply_to_status_id_str": null, 	"in_reply_to_user_id": null, 	"in_reply_to_user_id_str": null, 	"in_reply_to_screen_name": null, 	"user": { 		"id": 2244994945, 		"id_str": "2244994945", 		"name": "Twitter Dev", 		"screen_name": "TwitterDev", 		"location": "127.0.0.1", 		"url": "https://developer.twitter.com/en/community", 		"description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.", 		"translator_type": "regular", 		"protected": false, 		"verified": true, 		"followers_count": 512292, 		"friends_count": 2038, 		"listed_count": 1666, 		"favourites_count": 2147, 		"statuses_count": 3634, 		"created_at": "Sat Dec 14 04:35:55 +0000 2013", 		"utc_offset": null, 		"time_zone": null, 		"geo_enabled": true, 		"lang": null, 		"contributors_enabled": false, 		"is_translator": false, 		"profile_background_color": "FFFFFF", 		"profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png", 		"profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png", 		"profile_background_tile": false, 		"profile_link_color": "0084B4", 		"profile_sidebar_border_color": "FFFFFF", 		"profile_sidebar_fill_color": "DDEEF6", 		"profile_text_color": "333333", 		"profile_use_background_image": false, 		"profile_image_url": "http://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg", 		"profile_image_url_https": "https://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg", 		"profile_banner_url": "https://pbs.twimg.com/profile_banners/2244994945/1594913664", 		"default_profile": false, 		"default_profile_image": false, 		"following": null, 		"follow_request_sent": null, 		"notifications": null 	}, 	"geo": null, 	"coordinates": null, 	"place": null, 	"contributors": null, 	"quoted_status_id": 1327011423252144000, 	"quoted_status_id_str": "1327011423252144128", 	"quoted_status": { 		"created_at": "Thu Nov 12 22:12:32 +0000 2020", 		"id": 1327011423252144000, 		"id_str": "1327011423252144128", 		"text": "👋 Friendly reminder that Twitter Developer Labs v2 hide replies and recent search will be retired next Monday, Nove… https://t.co/EEWN2Q9aXh", 		"source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>", 		"truncated": true, 		"in_reply_to_status_id": null, 		"in_reply_to_status_id_str": null, 		"in_reply_to_user_id": null, 		"in_reply_to_user_id_str": null, 		"in_reply_to_screen_name": null, 		"user": { 			"id": 2244994945, 			"id_str": "2244994945", 			"name": "Twitter Dev", 			"screen_name": "TwitterDev", 			"location": "127.0.0.1", 			"url": "https://developer.twitter.com/en/community", 			"description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.", 			"translator_type": "regular", 			"protected": false, 			"verified": true, 			"followers_count": 512292, 			"friends_count": 2038, 			"listed_count": 1666, 			"favourites_count": 2147, 			"statuses_count": 3634, 			"created_at": "Sat Dec 14 04:35:55 +0000 2013", 			"utc_offset": null, 			"time_zone": null, 			"geo_enabled": true, 			"lang": null, 			"contributors_enabled": false, 			"is_translator": false, 			"profile_background_color": "FFFFFF", 			"profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png", 			"profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png", 			"profile_background_tile": false, 			"profile_link_color": "0084B4", 			"profile_sidebar_border_color": "FFFFFF", 			"profile_sidebar_fill_color": "DDEEF6", 			"profile_text_color": "333333", 			"profile_use_background_image": false, 			"profile_image_url": "http://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg", 			"profile_image_url_https": "https://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg", 			"profile_banner_url": "https://pbs.twimg.com/profile_banners/2244994945/1594913664", 			"default_profile": false, 			"default_profile_image": false, 			"following": null, 			"follow_request_sent": null, 			"notifications": null 		}, 		"geo": null, 		"coordinates": null, 		"place": null, 		"contributors": null, 		"is_quote_status": false, 		"extended_tweet": { 			"full_text": "👋 Friendly reminder that Twitter Developer Labs v2 hide replies and recent search will be retired next Monday, November 16! We encourage you to migrate to the new hide replies and recent search endpoints now available in the v2 #TwitterAPI. Details: https://t.co/r6z6CI7kEy", 			"display_text_range": [ 				0, 				273 			], 			"entities": { 				"hashtags": [{ 					"text": "TwitterAPI", 					"indices": [ 						228, 						239 					] 				}], 				"urls": [{ 					"url": "https://t.co/r6z6CI7kEy", 					"expanded_url": "https://twittercommunity.com/t/retiring-labs-v2-recent-search-and-hide-replies/145795", 					"display_url": "twittercommunity.com/t/retiring-lab…", 					"unwound": { 						"url": "https://twittercommunity.com/t/retiring-labs-v2-recent-search-and-hide-replies/145795", 						"status": 200, 						"title": "Retiring Labs v2 recent search and hide replies", 						"description": "As we said in our Early Access and hide replies announcements, the following Twitter Developer Labs v2 endpoints will be retired on November 16th. Labs v2 recent search Labs v2 hide replies If called, these endpoints will respond with an HTTP 410 status and return no data. Based on your feedback from Labs, we incorporated corresponding functionality into the Twitter API v2. The relevant documentation can be found using the links below. Click here to enroll in v2 access if you haven’t already..." 					}, 					"indices": [ 						250, 						273 					] 				}], 				"user_mentions": [], 				"symbols": [] 			} 		}, 		"quote_count": 4, 		"reply_count": 2, 		"retweet_count": 8, 		"favorite_count": 33, 		"entities": { 			"hashtags": [], 			"urls": [{ 				"url": "https://t.co/EEWN2Q9aXh", 				"expanded_url": "https://twitter.com/i/web/status/1327011423252144128", 				"display_url": "twitter.com/i/web/status/1…", 				"indices": [ 					117, 					140 				] 			}], 			"user_mentions": [], 			"symbols": [] 		}, 		"favorited": false, 		"retweeted": false, 		"possibly_sensitive": false, 		"filter_level": "low", 		"lang": "en" 	}, 	"quoted_status_permalink": { 		"url": "https://t.co/JaxttUMmjX", 		"expanded": "https://twitter.com/TwitterDev/status/1327011423252144128", 		"display": "twitter.com/TwitterDev/sta…" 	}, 	"is_quote_status": true, 	"extended_tweet": { 		"full_text": "As planned, the Labs v2 endpoints referenced below have now been retired. Please let us know in the forums if you have questions or need help with the Twitter API v2! https://t.co/JaxttUMmjX", 		"display_text_range": [ 			0, 			166 		], 		"entities": { 			"hashtags": [], 			"urls": [{ 				"url": "https://t.co/JaxttUMmjX", 				"expanded_url": "https://twitter.com/TwitterDev/status/1327011423252144128", 				"display_url": "twitter.com/TwitterDev/sta…", 				"indices": [ 					167, 					190 				] 			}], 			"user_mentions": [], 			"symbols": [] 		} 	}, 	"quote_count": 1, 	"reply_count": 4, 	"retweet_count": 7, 	"favorite_count": 29, 	"entities": { 		"hashtags": [], 		"urls": [{ 			"url": "https://t.co/ahQvTYaOcZ", 			"expanded_url": "https://twitter.com/i/web/status/1328399838128467969", 			"display_url": "twitter.com/i/web/status/1…", 			"indices": [ 				117, 				140 			] 		}], 		"user_mentions": [], 		"symbols": [] 	}, 	"favorited": false, 	"retweeted": false, 	"possibly_sensitive": false, 	"filter_level": "low", 	"lang": "en", 	"matching_rules": [{ 		"tag": null 	}] }`
    

### Retweeted Quote Tweet

      ` {  	"created_at": "Thu Feb 06 17:26:44 +0000 2020",  	"id": 1225470895902412800,  	"id_str": "1225470895902412800",  	"text": "RT @AureliaSpecker: 📣 If you enjoyed the London commute tutorial I wrote in November last year, check out the refactored version that uses…",  	"source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",  	"truncated": false,  	"in_reply_to_status_id": null,  	"in_reply_to_status_id_str": null,  	"in_reply_to_user_id": null,  	"in_reply_to_user_id_str": null,  	"in_reply_to_screen_name": null,  	"user": {  		"id": 2244994945,  		"id_str": "2244994945",  		"name": "Twitter Dev",  		"screen_name": "TwitterDev",  		"location": "127.0.0.1",  		"url": "https://developer.twitter.com/en/community",  		"description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",  		"translator_type": "regular",  		"protected": false,  		"verified": true,  		"followers_count": 512292,  		"friends_count": 2038,  		"listed_count": 1666,  		"favourites_count": 2147,  		"statuses_count": 3634,  		"created_at": "Sat Dec 14 04:35:55 +0000 2013",  		"utc_offset": null,  		"time_zone": null,  		"geo_enabled": true,  		"lang": null,  		"contributors_enabled": false,  		"is_translator": false,  		"profile_background_color": "FFFFFF",  		"profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",  		"profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",  		"profile_background_tile": false,  		"profile_link_color": "0084B4",  		"profile_sidebar_border_color": "FFFFFF",  		"profile_sidebar_fill_color": "DDEEF6",  		"profile_text_color": "333333",  		"profile_use_background_image": false,  		"profile_image_url": "http://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg",  		"profile_image_url_https": "https://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg",  		"profile_banner_url": "https://pbs.twimg.com/profile_banners/2244994945/1594913664",  		"default_profile": false,  		"default_profile_image": false,  		"following": null,  		"follow_request_sent": null,  		"notifications": null  	},  	"geo": null,  	"coordinates": null,  	"place": null,  	"contributors": null,  	"retweeted_status": {  		"created_at": "Tue Feb 04 15:01:25 +0000 2020",  		"id": 1224709550214873000,  		"id_str": "1224709550214873090",  		"text": "📣 If you enjoyed the London commute tutorial I wrote in November last year, check out the refactored version that u… https://t.co/cAepHunkFp",  		"display_text_range": [  			0,  			140  		],  		"source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",  		"truncated": true,  		"in_reply_to_status_id": null,  		"in_reply_to_status_id_str": null,  		"in_reply_to_user_id": null,  		"in_reply_to_user_id_str": null,  		"in_reply_to_screen_name": null,  		"user": {  			"id": 1102321381,  			"id_str": "1102321381",  			"name": "Aurelia Specker",  			"screen_name": "AureliaSpecker",  			"location": "London, UK",  			"url": null,  			"description": "devrel @TwitterUK • Swiss in London • mother of houseplants • personal hairdresser to @_dormrod",  			"translator_type": "none",  			"protected": false,  			"verified": false,  			"followers_count": 1032,  			"friends_count": 1331,  			"listed_count": 26,  			"favourites_count": 4979,  			"statuses_count": 854,  			"created_at": "Fri Jan 18 23:45:43 +0000 2013",  			"utc_offset": null,  			"time_zone": null,  			"geo_enabled": true,  			"lang": null,  			"contributors_enabled": false,  			"is_translator": false,  			"profile_background_color": "8B542B",  			"profile_background_image_url": "http://abs.twimg.com/images/themes/theme8/bg.gif",  			"profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme8/bg.gif",  			"profile_background_tile": false,  			"profile_link_color": "5E341C",  			"profile_sidebar_border_color": "D9B17E",  			"profile_sidebar_fill_color": "EADEAA",  			"profile_text_color": "333333",  			"profile_use_background_image": true,  			"profile_image_url": "http://pbs.twimg.com/profile_images/1137517534104772608/8FBYgc6G_normal.jpg",  			"profile_image_url_https": "https://pbs.twimg.com/profile_images/1137517534104772608/8FBYgc6G_normal.jpg",  			"profile_banner_url": "https://pbs.twimg.com/profile_banners/1102321381/1587552672",  			"default_profile": false,  			"default_profile_image": false,  			"following": null,  			"follow_request_sent": null,  			"notifications": null  		},  		"geo": null,  		"coordinates": null,  		"place": null,  		"contributors": null,  		"quoted_status_id": 1195000047089389600,  		"quoted_status_id_str": "1195000047089389573",  		"quoted_status": {  			"created_at": "Thu Nov 14 15:26:27 +0000 2019",  			"id": 1195000047089389600,  			"id_str": "1195000047089389573",  			"text": "I wrote a tutorial on how to get bespoke commute information using the Twitter API🚇\n\n#DEVcommunity #Pythontutorial… https://t.co/pL0qJ4vhtE",  			"source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",  			"truncated": true,  			"in_reply_to_status_id": null,  			"in_reply_to_status_id_str": null,  			"in_reply_to_user_id": null,  			"in_reply_to_user_id_str": null,  			"in_reply_to_screen_name": null,  			"user": {  				"id": 1102321381,  				"id_str": "1102321381",  				"name": "Aurelia Specker",  				"screen_name": "AureliaSpecker",  				"location": "London, UK",  				"url": null,  				"description": "devrel @TwitterUK • Swiss in London • mother of houseplants • personal hairdresser to @_dormrod",  				"translator_type": "none",  				"protected": false,  				"verified": false,  				"followers_count": 1032,  				"friends_count": 1331,  				"listed_count": 26,  				"favourites_count": 4979,  				"statuses_count": 854,  				"created_at": "Fri Jan 18 23:45:43 +0000 2013",  				"utc_offset": null,  				"time_zone": null,  				"geo_enabled": true,  				"lang": null,  				"contributors_enabled": false,  				"is_translator": false,  				"profile_background_color": "8B542B",  				"profile_background_image_url": "http://abs.twimg.com/images/themes/theme8/bg.gif",  				"profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme8/bg.gif",  				"profile_background_tile": false,  				"profile_link_color": "5E341C",  				"profile_sidebar_border_color": "D9B17E",  				"profile_sidebar_fill_color": "EADEAA",  				"profile_text_color": "333333",  				"profile_use_background_image": true,  				"profile_image_url": "http://pbs.twimg.com/profile_images/1137517534104772608/8FBYgc6G_normal.jpg",  				"profile_image_url_https": "https://pbs.twimg.com/profile_images/1137517534104772608/8FBYgc6G_normal.jpg",  				"profile_banner_url": "https://pbs.twimg.com/profile_banners/1102321381/1587552672",  				"default_profile": false,  				"default_profile_image": false,  				"following": null,  				"follow_request_sent": null,  				"notifications": null  			},  			"geo": null,  			"coordinates": null,  			"place": null,  			"contributors": null,  			"is_quote_status": false,  			"extended_tweet": {  				"full_text": "I wrote a tutorial on how to get bespoke commute information using the Twitter API🚇\n\n#DEVcommunity #Pythontutorial \n\nCheck it out here 👇\nhttps://t.co/sOjXW4YhbN",  				"display_text_range": [  					0,  					160  				],  				"entities": {  					"hashtags": [{  							"text": "DEVcommunity",  							"indices": [  								85,  								98  							]  						},  						{  							"text": "Pythontutorial",  							"indices": [  								99,  								114  							]  						}  					],  					"urls": [{  						"url": "https://t.co/sOjXW4YhbN",  						"expanded_url": "https://dev.to/twitterdev/using-the-twitter-api-to-make-your-commute-easier-3od0",  						"display_url": "dev.to/twitterdev/usi…",  						"unwound": {  							"url": "https://dev.to/twitterdev/using-the-twitter-api-to-make-your-commute-easier-3od0",  							"status": 200,  							"title": null,  							"description": null  						},  						"indices": [  							137,  							160  						]  					}],  					"user_mentions": [],  					"symbols": []  				}  			},  			"quote_count": 4,  			"reply_count": 5,  			"retweet_count": 31,  			"favorite_count": 123,  			"entities": {  				"hashtags": [{  						"text": "DEVcommunity",  						"indices": [  							85,  							98  						]  					},  					{  						"text": "Pythontutorial",  						"indices": [  							99,  							114  						]  					}  				],  				"urls": [{  					"url": "https://t.co/pL0qJ4vhtE",  					"expanded_url": "https://twitter.com/i/web/status/1195000047089389573",  					"display_url": "twitter.com/i/web/status/1…",  					"indices": [  						116,  						139  					]  				}],  				"user_mentions": [],  				"symbols": []  			},  			"favorited": false,  			"retweeted": false,  			"possibly_sensitive": false,  			"filter_level": "low",  			"lang": "en"  		},  		"quoted_status_permalink": {  			"url": "https://t.co/dXrJYvn3hY",  			"expanded": "https://twitter.com/AureliaSpecker/status/1195000047089389573",  			"display": "twitter.com/AureliaSpecker…"  		},  		"is_quote_status": true,  		"extended_tweet": {  			"full_text": "📣 If you enjoyed the London commute tutorial I wrote in November last year, check out the refactored version that uses Twitter's new search endpoint 🚇 https://t.co/87XIPZmZBJ\n\n#DEVcommunity #Pythontutorial @TwitterDev @TwitterAPI https://t.co/dXrJYvn3hY",  			"display_text_range": [  				0,  				229  			],  			"entities": {  				"hashtags": [{  						"text": "DEVcommunity",  						"indices": [  							176,  							189  						]  					},  					{  						"text": "Pythontutorial",  						"indices": [  							190,  							205  						]  					}  				],  				"urls": [{  						"url": "https://t.co/87XIPZmZBJ",  						"expanded_url": "https://bit.ly/2OrnrCC",  						"display_url": "bit.ly/2OrnrCC",  						"unwound": {  							"url": "https://dev.to/twitterdev/migrate-to-twitter-s-newly-released-labs-recent-search-endpoint-3npe",  							"status": 200,  							"title": null,  							"description": null  						},  						"indices": [  							151,  							174  						]  					},  					{  						"url": "https://t.co/dXrJYvn3hY",  						"expanded_url": "https://twitter.com/AureliaSpecker/status/1195000047089389573",  						"display_url": "twitter.com/AureliaSpecker…",  						"indices": [  							230,  							253  						]  					}  				],  				"user_mentions": [{  						"screen_name": "TwitterDev",  						"name": "Twitter Dev",  						"id": 2244994945,  						"id_str": "2244994945",  						"indices": [  							206,  							217  						]  					},  					{  						"screen_name": "TwitterAPI",  						"name": "Twitter API",  						"id": 6253282,  						"id_str": "6253282",  						"indices": [  							218,  							229  						]  					}  				],  				"symbols": []  			}  		},  		"quote_count": 2,  		"reply_count": 0,  		"retweet_count": 12,  		"favorite_count": 43,  		"entities": {  			"hashtags": [],  			"urls": [{  				"url": "https://t.co/cAepHunkFp",  				"expanded_url": "https://twitter.com/i/web/status/1224709550214873090",  				"display_url": "twitter.com/i/web/status/1…",  				"indices": [  					117,  					140  				]  			}],  			"user_mentions": [],  			"symbols": []  		},  		"favorited": false,  		"retweeted": false,  		"possibly_sensitive": false,  		"filter_level": "low",  		"lang": "en"  	},  	"quoted_status_id": 1195000047089389600,  	"quoted_status_id_str": "1195000047089389573",  	"quoted_status": {  		"created_at": "Thu Nov 14 15:26:27 +0000 2019",  		"id": 1195000047089389600,  		"id_str": "1195000047089389573",  		"text": "I wrote a tutorial on how to get bespoke commute information using the Twitter API🚇\n\n#DEVcommunity #Pythontutorial… https://t.co/pL0qJ4vhtE",  		"source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",  		"truncated": true,  		"in_reply_to_status_id": null,  		"in_reply_to_status_id_str": null,  		"in_reply_to_user_id": null,  		"in_reply_to_user_id_str": null,  		"in_reply_to_screen_name": null,  		"user": {  			"id": 1102321381,  			"id_str": "1102321381",  			"name": "Aurelia Specker",  			"screen_name": "AureliaSpecker",  			"location": "London, UK",  			"url": null,  			"description": "devrel @TwitterUK • Swiss in London • mother of houseplants • personal hairdresser to @_dormrod",  			"translator_type": "none",  			"protected": false,  			"verified": false,  			"followers_count": 1032,  			"friends_count": 1331,  			"listed_count": 26,  			"favourites_count": 4979,  			"statuses_count": 854,  			"created_at": "Fri Jan 18 23:45:43 +0000 2013",  			"utc_offset": null,  			"time_zone": null,  			"geo_enabled": true,  			"lang": null,  			"contributors_enabled": false,  			"is_translator": false,  			"profile_background_color": "8B542B",  			"profile_background_image_url": "http://abs.twimg.com/images/themes/theme8/bg.gif",  			"profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme8/bg.gif",  			"profile_background_tile": false,  			"profile_link_color": "5E341C",  			"profile_sidebar_border_color": "D9B17E",  			"profile_sidebar_fill_color": "EADEAA",  			"profile_text_color": "333333",  			"profile_use_background_image": true,  			"profile_image_url": "http://pbs.twimg.com/profile_images/1137517534104772608/8FBYgc6G_normal.jpg",  			"profile_image_url_https": "https://pbs.twimg.com/profile_images/1137517534104772608/8FBYgc6G_normal.jpg",  			"profile_banner_url": "https://pbs.twimg.com/profile_banners/1102321381/1587552672",  			"default_profile": false,  			"default_profile_image": false,  			"following": null,  			"follow_request_sent": null,  			"notifications": null  		},  		"geo": null,  		"coordinates": null,  		"place": null,  		"contributors": null,  		"is_quote_status": false,  		"extended_tweet": {  			"full_text": "I wrote a tutorial on how to get bespoke commute information using the Twitter API🚇\n\n#DEVcommunity #Pythontutorial \n\nCheck it out here 👇\nhttps://t.co/sOjXW4YhbN",  			"display_text_range": [  				0,  				160  			],  			"entities": {  				"hashtags": [{  						"text": "DEVcommunity",  						"indices": [  							85,  							98  						]  					},  					{  						"text": "Pythontutorial",  						"indices": [  							99,  							114  						]  					}  				],  				"urls": [{  					"url": "https://t.co/sOjXW4YhbN",  					"expanded_url": "https://dev.to/twitterdev/using-the-twitter-api-to-make-your-commute-easier-3od0",  					"display_url": "dev.to/twitterdev/usi…",  					"unwound": {  						"url": "https://dev.to/twitterdev/using-the-twitter-api-to-make-your-commute-easier-3od0",  						"status": 200,  						"title": null,  						"description": null  					},  					"indices": [  						137,  						160  					]  				}],  				"user_mentions": [],  				"symbols": []  			}  		},  		"quote_count": 4,  		"reply_count": 5,  		"retweet_count": 31,  		"favorite_count": 123,  		"entities": {  			"hashtags": [{  					"text": "DEVcommunity",  					"indices": [  						85,  						98  					]  				},  				{  					"text": "Pythontutorial",  					"indices": [  						99,  						114  					]  				}  			],  			"urls": [{  				"url": "https://t.co/pL0qJ4vhtE",  				"expanded_url": "https://twitter.com/i/web/status/1195000047089389573",  				"display_url": "twitter.com/i/web/status/1…",  				"indices": [  					116,  					139  				]  			}],  			"user_mentions": [],  			"symbols": []  		},  		"favorited": false,  		"retweeted": false,  		"possibly_sensitive": false,  		"filter_level": "low",  		"lang": "en"  	},  	"quoted_status_permalink": {  		"url": "https://t.co/dXrJYvn3hY",  		"expanded": "https://twitter.com/AureliaSpecker/status/1195000047089389573",  		"display": "twitter.com/AureliaSpecker…"  	},  	"is_quote_status": true,  	"quote_count": 0,  	"reply_count": 0,  	"retweet_count": 0,  	"favorite_count": 0,  	"entities": {  		"hashtags": [],  		"urls": [],  		"user_mentions": [{  			"screen_name": "AureliaSpecker",  			"name": "Aurelia Specker",  			"id": 1102321381,  			"id_str": "1102321381",  			"indices": [  				3,  				18  			]  		}],  		"symbols": []  	},  	"favorited": false,  	"retweeted": false,  	"filter_level": "low",  	"lang": "en",  	"matching_rules": [{  		"tag": null  	}]  }`

Activity object

Interested in learning more about how the Activity Streams data format maps to the Twitter API v2 format?

Check out our comparison guide: [Activity Streams compared to Twitter API v2](https://developer.twitter.com/en/docs/twitter-api/migrate/data-formats/activity-streams-to-v2)

Please note: It is highly recommended to use the [Enriched Native](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/tweet.html) format for enterprise data APIs. 

* The Enriched Native format includes all new metadata since 2017, such as [poll metadata](https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/poll-metadata.html), and additional metrics such as reply\_count and quote\_count.
    
* Activity Streams format has not been updated with new metadata or enrichments since the [character update](https://blog.twitter.com/official/en_us/topics/product/2017/Giving-you-more-characters-to-express-yourself.html) in 2017.
    

Activity Object
---------------

Activity Streams is an object schema translation of Twitter's [original data format](https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/overview/intro-to-tweet-json) created by Gnip to 'normalize the format' of Tweet data and other social media data using the third party [Activity Base Schema described here](https://activitystrea.ms/head/activity-schema.html).  Tweets are normalized into the activity streams schema, including: note, person, place and service object types as nested objects.  Tweets can have other nested Tweet activity obejcts for Retweets, or others including twitter\_quoted\_status, long\_object.

The base level object type "activity" is similar to the [Tweet base level object](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/tweet.html) of the native enriched format.  Example payloads in activity streams format can be found [here](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/activity-streams-objects/example-payloads.html).

### Data Dictionary

Below you will find the data dictionary for these ‘root-level’ "activity" attributes, as well as links to child object data dictionaries.

|     |     |     |
| --- | --- | --- |
| Attribute | Type | Description |
| id  | string | A unique IRI for the tweet. In more detail, "tag" is the scheme, "search.twitter.com" represents the domain for the scheme, and 2005 is when the scheme was derived.  <br>When storing Tweets, this should be used as the unique identifier or primary key.  <br>"id": "tag:search.twitter.com,2005:1050118621198921728" |
| objectType | string | Type of object, always set to "activity"  <br>"objectType": "activity" |
| object | object | An object representing tweet being posted or shared.  <br>For Retweets, this will contain an entire "activity", with the pertinent fields described in this schema.  <br>For Original Tweets, this will contain a "note" object, with the fields described here.  <br>"object":  <br>"object": {  <br>"objectType": "note",  <br>"id": "object:search.twitter.com,2005:1050118621198921728",  <br>"summary": "To make room for more expression, we will now count all emojis as equal—including those with gender‍‍‍ ‍‍and skin t… https://t.co/MkGjXf9aXm",  <br>"link": "http://twitter.com/TwitterAPI/statuses/1050118621198921728",  <br>"postedTime": "2018-10-10T20:19:24.000Z"  <br>} |
| long\_object | object | An object representing the full text body if the Tweet text extends beyond 140 characters.  <br>  <br>  <br>"long\_object": {  <br>"body": "To make room for more expression, we will now count all emojis as equal—including those with gender‍‍‍ ‍‍and skin tone modifiers 👍🏻👍🏽👍🏿. This is now reflected in Twitter-Text, our Open Source library. \\n\\nUsing Twitter-Text? See the forum post for detail: https://t.co/Nx1XZmRCXA",  <br>"display\_text\_range": \[  <br>0,  <br>277  <br>\],  <br>"twitter\_entities": {  <br>"hashtags": \[\],  <br>"urls": \[  <br>{  <br>"url": "https://t.co/Nx1XZmRCXA",  <br>"expanded\_url": "https://twittercommunity.com/t/new-update-to-the-twitter-text-library-emoji-character-count/114607",  <br>"display\_url": "twittercommunity.com/t/new-update-t…",  <br>"indices": \[  <br>254,  <br>277  <br>\]  <br>}  <br>\],  <br>"user\_mentions": \[\],  <br>"symbols": \[\]  <br>}  <br>} |
| display\_text\_range | array | if the Tweet text extends beyond 140 characters.  <br>  <br>  <br>"display\_text\_range": \[  <br>0,  <br>142  <br>\] |
| verb | string | [The type of action being taken by the user.  <br>Tweets, "post"  <br>Retweets, "share"  <br>Deleted Tweets, "delete"  <br>The verb is the proper way to distinguish between a Tweet and a true Retweet. However, this only applies to true retweets, and not modified or quoted Tweets, which don't use Twitter's Retweet functionality. For a description of AS verbs](http://activitystrea.ms/head/activity-schema.html#verbs) [click here](http://activitystrea.ms/head/activity-schema.html#verbs).  <br>For Deletes, note that only a limited number of fields will be included, as shown in the sample payload below.  <br>"verb": "post" |
| postedTime | date (ISO 8601) | The time the action occurred, e.g. the time the Tweet was posted.  <br>  <br>  <br>"postedTime": "2018-10-10T20:19:24.000Z" |
| generator | object | An object representing the utility used to post the Tweet. This will contain the name ("displayName") and a link ("link") for the source application generating the Tweet.  <br>"generator": {  <br>"displayName": "Twitter Web Client",  <br>"link": "http://twitter.com"  <br>} |
| provider | object | A JSON object representing the provider of the activity. This will contain an objectType ("service"), the name of the provider ("displayName"), and a link to the provider's website ("link").  <br>"provider":  <br>{  <br>"objectType": "service",  <br>"displayName": "Twitter",  <br>"link": "http://www.twitter.com"  <br>} |
| link | string | A Permalink for the tweet.  <br>"link": "http://twitter.com/TwitterAPI/statuses/1050118621198921728" |
| body | string | The tweet text.  <br>  <br>In Retweets, note that Twitter modifies the value of the body at the root level by adding "RT @username" at the beginning, and by truncating the original text and adding an ellipsis at the end. Thus, for Retweets, your app should look at the object.body to ensure that it is extracting the non-modified text of the original Tweet (being retweeted).  <br>"body": "With Cardiff, Crystal Palace, and Hull City joining the EPL from the Championship it will be a great relegation battle at the end." |
| display\_text\_range | array | Describes the range of characters within the body text that indicates the displayed Tweet. Tweets with leading @mentions will start at more than 0 and Tweets with attached media or that extened beyond 140 characters will indicate the display\_text\_range in the long\_object.  <br>  <br>"display\_text\_range": \[  <br>14,  <br>42  <br>\]  <br>or  <br>"long\_object": {  <br>"display\_text\_range": \[  <br>0,  <br>277  <br>\]... |
| actor | object | [An object representing the twitter user who tweeted. The Actor Object refers to a Twitter User, and contains all metadata relevant to that user.  <br>See](https://aem.twitter.biz/en/docs/twitter-api/enterprise/data-dictionary/activity-streams-objects/actor.html) [actor object details](https://aem.twitter.biz/en/docs/twitter-api/enterprise/data-dictionary/activity-streams-objects/actor.html) |
| inReplyTo | object | A JSON object referring to the Tweet being replied to, if applicable. Contains a link to the Tweet.  <br>"inReplyTo":  <br>{  <br>"link": "http:\\/\\/twitter.com\\/GOP\\/statuses\\/349573991561838593"  <br>} |
| location | object | [A JSON object representing the Twitter "Place" where the tweet was created. This is an object passed through from the Twitter platform.  <br>  <br>See](https://aem.twitter.biz/en/docs/twitter-api/enterprise/data-dictionary/activity-streams-objects/location.html) [location object](https://aem.twitter.biz/en/docs/twitter-api/enterprise/data-dictionary/activity-streams-objects/location.html) |
| twitter\_entities | object | The entities object from Twitter's data format which contains lists of urls, mentions and hashtags. Please reference the Twitter documentation on Entities here Note that in Retweets, Twitter may truncate the values of entities that it extracts at the root level. So, for Retweets, your app should look at object.twitter\_entities to ensure that you are using non-truncated values.  <br>  <br>See twitter\_entities object details |
| twitter\_extended\_entities | object | An object from Twitter's native data format containing "media". This will be present for any Tweet where the twitter\_entities object has data present in the "media" field, and will include multiple photos where present in the post. Note that this is the correct location to retrieve media information for multi-photo posts.  <br>  <br>Multiple photos are represented by comma-separated JSON objects within the "media" array.  <br>  <br>See [twitter\_extended\_entities object details](https://aem.twitter.biz/en/docs/twitter-api/enterprise/data-dictionary/activity-streams-objects/twitter-extended-entities.html) |
| gnip | object | An object added to the activity payload to indicate the matching rules, and added enriched data based on enrichments active on the stream or product.  <br>  <br>See [gnip object details](https://aem.twitter.biz/en/docs/twitter-api/enterprise/data-dictionary/activity-streams-objects/gnip.html) |
| edit\_history | Object | Unique identifiers indicating all versions of a Tweet. For Tweets with no edits, there will be one ID. For Tweets with an edit history, there will be multiple IDs, arranged in ascending order reflecting the order of edits, with the most recent version in the last position of the array. <br><br>The Tweet IDs can be used to hydrate and view previous versions of a Tweet.<br><br>Example:<br><br>edit\_history": {<br>    "initial\_tweet\_id": "1283764123"<br>    "edit\_tweet\_ids": \["1283764123", "1394263866"\]<br>  } |
| edit\_controls | Object | When present, indicates how long a Tweet is still editable for and the number of remaining edits. Tweets are only editable for the first 30 minutes after creation and can be edited up to five times. <br><br>The Tweet IDs can be used to hydrate and view previous versions of a Tweet.<br><br>Example:<br><br>"edit\_controls": {  <br>     "editable\_until\_ms": 123<br>     "edits\_remaining": 3   <br>  } |
| editable | Boolean | When present, indicates if a Tweet was eligible for edit when published. This field is not dynamic and won't toggle from True to False when a Tweet reaches its editable time limit, or maximum number of edits. The following Tweet features will cause this field to be false:<br><br>* Tweets is promoted<br>* Tweet has a poll<br>* Tweet is a non-self-thread reply<br>* Tweet is a retweet (note that Quote Tweets are eligible for edit)<br>* Tweet is nullcast<br>* Community Tweet<br>* Superfollow Tweet<br>* Collaborative Tweet |

###   
Additional Tweet attributes

| Attribute | Type | Description |
| --- | --- | --- |
| twitter\_lang | string |     |
| favoritesCount | int | _Nullable._ Indicates approximately how many times this Tweet has been liked by Twitter users.  <br>  <br>"favoritesCount":298 |
| retweetCount | int | Number of times this Tweet has been retweeted. Example:<br><br>"retweetCount":153 |

### Deprecated Attributes

|     |     |     |
| --- | --- | --- |
| Field | Type | Description |
| geo | object | Point location where the Tweet was created. |
| twitter\_filter\_level | string | Deprecated field left in for non breaking change |

### Nested Tweet activity obejcts

In several cases, a Tweet object will included other nested Tweets.  If you are working with nested objects, then that JSON payload will contain multiple objects, and each Tweet object may contain its own objects. The root-level object will contain information on the type of action taken, i.e. whether it is a Retweet or a Quote Tweet, and may also contain an object that describes the 'original' Tweet being shared. Extended Tweets will include a nested extended object that extends beyond 140 characters, which was used to prevent breaking changes when the update was made in 2017. Each nested object dictionary is described below.

#### Retweets

Activity streams format of Retweets includes a nested object with the type "activity" and the verb "note" to represent the original Tweet being Retweeted.

      `{ 	"id": "tag:search.twitter.com,2005:222222222222", 	"objectType": "activity", 	"verb": "share", 	"body": "RT @TheOriginalTweeter: Coffee and art ☕️", 	"actor": { 		"displayName": "TheRetweeter" 	}, 	"object": { 		"id": "tag:search.twitter.com,2005:11111111111", 		"objectType": "activity", 		"verb": "post", 		"body": "Coffee and art ☕️", 		"actor": { 			"displayName": "TheOriginalTweeter" 		}, 		"object": { 			"objectType": "note", 			"id": "object:search.twitter.com,2005:11111111111", 			"summary": "Coffee and art ☕️", 			"link": "http://twitter.com/originaltweeter/statuses/11111111111", 			"postedTime": "2020-12-04T11:00:01.000Z" 		}, 		"twitter_entities": {}, 		"twitter_extended_entities": {} 	}, 	"twitter_entities": {}, 	"twitter_extended_entities": {}, 	"gnip": {} }`
    

#### Twitter quoted status

Activity streams format embeded quote Tweets

      `{ 	"id": "tag:search.twitter.com,2005:222222222222", 	"objectType": "activity", 	"verb": "post", 	"body": "Quoting a Tweet: https://t.co/mxiFJ59FlB", 	"actor": { 		"displayName": "TheQuoter2" 	}, 	"object": { 		"objectType": "note", 		"id": "object:search.twitter.com,2005:111111111", 		"summary": "https://t.co/mxiFJ59FlB" 	}, 	"twitter_entities": {}, 	"twitter_extended_entities": {}, 	"gnip": {}, 	"twitter_quoted_status": { 		"id": "tag:search.twitter.com,2005:111111111", 		"objectType": "activity", 		"verb": "post", 		"body": "console.log('Happy birthday, JavaScript!');", 		"actor": { 			"displayName": "TheOriginalTweeter" 		}, 		"object": { 			"objectType": "note", 			"id": "object:search.twitter.com,2005:111111111" 		}, 		"twitter_entities": {} 	} }`
    

Retweeted Quote Tweet:

      `    {     	"id": "tag:search.twitter.com,2005:1293612267087384577",     	"objectType": "activity",     	"verb": "share",     	"postedTime": "2020-08-12T18:16:13.000Z",     	"generator": {},     	"provider": {},     	"link": "http://twitter.com/TwitterDev/statuses/1293612267087384577",     	"body": "RT @compston: So excited to make this first set of endpoints available - many more to come before we're done. The @TwitterDev #DevRel team…",     	"actor": {},     	"object": {},     	"favoritesCount": 0,     	"twitter_entities": {},     	"twitter_lang": "en",     	"retweetCount": 13,     	"gnip": {},     	"twitter_filter_level": "low",     	"twitter_quoted_status": {}     }`
    

### Long object

Activity streams format of the extended\_tweet

      `{   "id": "tag:search.twitter.com,2005:1050118621198921728",   "objectType": "activity",   "verb": "post",   "postedTime": "2018-10-10T20:19:24.000Z",   "generator": {     "displayName": "Twitter Web Client",     "link": "http://twitter.com"   },   "provider": {     "objectType": "service",     "displayName": "Twitter",     "link": "http://www.twitter.com"   },   "link": "http://twitter.com/TwitterAPI/statuses/1050118621198921728",   "body": "To make room for more expression, we will now count all emojis as equal—including those with gender‍‍‍ ‍‍and skin t… https://t.co/MkGjXf9aXm",   "long_object": {     "body": "To make room for more expression, we will now count all emojis as equal—including those with gender‍‍‍ ‍‍and skin tone modifiers 👍🏻👍🏽👍🏿. This is now reflected in Twitter-Text, our Open Source library. \n\nUsing Twitter-Text? See the forum post for detail: https://t.co/Nx1XZmRCXA",     "display_text_range": [       0,       277     ],     "twitter_entities": {see twitter_entities object},   "actor": {see actor object},   "object": {     "objectType": "note",     "id": "object:search.twitter.com,2005:1050118621198921728",     "summary": "To make room for more expression, we will now count all emojis as equal—including those with gender‍‍‍ ‍‍and skin t… https://t.co/MkGjXf9aXm",     "link": "http://twitter.com/TwitterAPI/statuses/1050118621198921728",     "postedTime": "2018-10-10T20:19:24.000Z"   },   "favoritesCount": 298,   "twitter_entities": {see twitter_entities object},   "twitter_lang": "en",   "retweetCount": 153,   "gnip": {see gnip object},   "twitter_filter_level": "low" }`
    

### Next Steps

Explore the other nested objects of this format:

* Review actor object
* Review location object
* Review twitter\_entities object
* See migration guide from Activity Streams to Twitter API v2 format

Actor object

Actor object
------------

The actor object contains Twitter User account metadata that describes the Twitter User which created the activity.

### Data Dictionary

| Attribute | Type | Description |
| --- | --- | --- |
| objectType | string | **"objectType":** "person" |
| id  | string | The string representation of the unique identifier for this author. Example:<br><br>"id:twitter.com:2244994945" |
| link |     | "http://www.twitter.com/TwitterDev |
| displayName | String | The name of the user, as they’ve defined it. Not necessarily a person’s name. Typically capped at 50 characters, but subject to change. Example:<br><br>**"displayName":** "Twitter Dev" |
| preferredUsername | string | The screen name, handle, or alias that this user identifies themselves with. Unique but subject to change. Use `id` as a user identifier whenever possible. Typically a maximum of 15 characters long, but some historical accounts may exist with longer names. Example:<br><br>**"preferredUsername":** "TwitterDev" |
| location | object | **"location": {**<br><br>          **"objectType":** "place"**,**<br><br>          **"displayName":** "127.0.0.1"<br><br>        **}** |
| links | array | _Nullable_ . A URL provided by the user in association with their profile. Example:<br><br>       **"links": \[**<br><br>          **{**<br><br>            **"href":** "https://developer.twitter.com/en/community"**,**<br><br>            **"rel":** "me"<br><br>          **}**<br><br>        **\]** |
| summary | string | _Nullable_ . The user-defined UTF-8 string describing their account. Example:<br><br>**"summary":** "The voice of the #TwitterDev team..." |
| protected | Boolean | When true, indicates that this user has chosen to protect their Tweets. See [About Public and Protected Tweets](https://support.twitter.com/articles/14016-about-public-and-protected-tweets) . Example:<br><br>"protected": true |
| verified | Boolean | When true, indicates that the user has a verified account. See [Verified Accounts](https://support.twitter.com/articles/119135-faqs-about-verified-accounts) . Example:<br><br>"verified": false |
| followersCount | Int | The number of followers this account currently has. Under certain conditions of duress, this field will temporarily indicate “0”. Example:<br><br>"followers\_count": 21 |
| friendsCount | Int | The number of users this account is following (AKA their “followings”). Under certain conditions of duress, this field will temporarily indicate “0”. Example:<br><br>"friends\_count": 32 |
| listedCount | Int | The number of public lists that this user is a member of. Example:<br><br>"listed\_count": 9274 |
| favoritesCount | Int | The number of Tweets this user has liked in the account’s lifetime. British spelling used in the field name for historical reasons. Example:<br><br>"favourites\_count": 13 |
| statusesCount | Int | The number of Tweets (including retweets) issued by the user. Example:<br><br>"statuses\_count": 42 |
| postedTime | date | The UTC datetime that the user account was created on Twitter. Example:<br><br>**"postedTime":** "2013-12-14T04:35:55.036Z" |
| image | string | A HTTPS-based URL pointing to the user’s profile image. Example:<br><br>**"image":** "https://pbs.twimg.com/profile\_images/1283786620521652229/lEODkLTh\_normal.jpg" |

###   
No longer supported (deprecated) attributes

| Field | Type | Description |
| --- | --- | --- |
| utcOffset | null | Value will be set to null. Still available via [GET account/settings](https://developer.twitter.com/en/docs/accounts-and-users/manage-account-settings/api-reference/get-account-settings) |
| twitterTimeZone | null | Value will be set to null. Still available via [GET account/settings](https://developer.twitter.com/en/docs/accounts-and-users/manage-account-settings/api-reference/get-account-settings) as tzinfo\_name |
| languages | null | Value will be set to null. Still available via [GET account/settings](https://developer.twitter.com/en/docs/accounts-and-users/manage-account-settings/api-reference/get-account-settings) as language |

###   
Examples:

      `      "actor": {         "objectType": "person",         "id": "id:twitter.com:2244994945",         "link": "http://www.twitter.com/TwitterDev",         "displayName": "Twitter Dev",         "postedTime": "2013-12-14T04:35:55.036Z",         "image": "https://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg",         "summary": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",         "friendsCount": 2039,         "followersCount": 512197,         "listedCount": 1662,         "statusesCount": 3632,         "twitterTimeZone": null,         "verified": true,         "utcOffset": null,         "preferredUsername": "TwitterDev",         "languages": [],         "links": [           {             "href": "https://developer.twitter.com/en/community",             "rel": "me"           }         ],         "location": {           "objectType": "place",           "displayName": "127.0.0.1"         },         "favoritesCount": 2147       }`
    

      `"actor": {     "objectType": "person",     "id": "id:twitter.com:6253282",     "link": "http://www.twitter.com/TwitterAPI",     "displayName": "Twitter API",     "postedTime": "2007-05-23T06:01:13.000Z",     "image": "https://pbs.twimg.com/profile_images/942858479592554497/BbazLO9L_normal.jpg",     "summary": "Tweets about changes and service issues. Follow @TwitterDev for more.",     "friendsCount": 39,     "followersCount": 6054164,     "listedCount": 12285,     "statusesCount": 3689,     "twitterTimeZone": null,     "verified": true,     "utcOffset": null,     "preferredUsername": "TwitterAPI",     "languages": [            ],     "links": [       {         "href": "https://developer.twitter.com",         "rel": "me"       }     ],     "favoritesCount": 4   }`
    

### Next Steps

Explore the other sub-objects that a Tweet contains:

* [Tweet object and data dictionary](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object.html)
* [Entities object and data dictionary](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/entities-object.html)
* [Extended Entities object and data dictionary](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/extended-entities-object.html)
* [Tweet geo objects and data dictionaries](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/geo-objects.html)

Location object

Location Object
---------------

Location obejcts can exist within the actor obejct set on the Twitter account level or within the profileLocations object of the [gnip object](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/activity-streams-objects/gnip.html). Location objects have a place object type and can have a name, address, or geo coordinates. Location objects are similar to [Geo](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/geo.html) in native enriched format.

### Location data dictionary

| Field | Type | Description |
| --- | --- | --- |
| objectType | string | See [here](http://activitystrea.ms/head/activity-schema.html#place) for more detailed information. Example:<br><br>**"objectType":** "place" |
| displayName | string | **The full name of the location.  <br>  <br>****"displayName":** "United States" |
| name | string | Name of the location from Twitter's place JSON format. |
| link | string | A link to the full Twitter JSON representation of the place.  <br>  <br>**"link":** "https://api.twitter.com/1.1/geo/id/27c45d804c777999.json" |
| geo | object | The geo coordintates object from Twitter.  Either a polygon, or point.<br><br>See [geo](https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/geo.html#coordinates) |
| countryCode | String | Shortened country code representing the country containing this place. Example:<br><br>**"countryCode": "US** |
| country | String | Name of the country containing this place. Example:<br><br>**"country":** "United States" |

  
profileLocations derived obejcts
-----------------------------------

|     |     |     |
| --- | --- | --- |
| Field | Type | Description |
| address | object | Within profileLocation location object within the [gnip object](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/activity-streams-objects/gnip.html).  Address of location derived by the [profile geo enrichement](https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/profile-geo.html).  Level of granularity will vary. <br><br>**"address": {**<br><br>          **"country":** "United States"**,**<br><br>          **"countryCode":** "US"**,**<br><br>          **"locality":** "Providence"**,**<br><br>          **"region":** "Rhode Island"**,**<br><br>          **"subRegion":** "Providence County"<br><br>        **}** |
| geo | object | Within profileLocation location object within the [gnip objec](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/activity-streams-objects/gnip.html)t. Centroid coordinates of the location derived by the [profile geo enrichement](https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/profile-geo.html).<br><br>**"geo": {**<br><br>          **"coordinates": \[**<br><br>            \-98.5**,**<br><br>            39.76<br><br>          **\],**<br><br>          **"type":** "point"<br><br>        **}** |

Examples
--------

      `"location": {     "objectType": "place",     "displayName": "Kansas, USA",     "name": "Kansas",     "country_code": "United States",     "twitter_country_code": "US",     "twitter_place_type": "admin",     "link": "https://api.twitter.com/1.1/geo/id/27c45d804c777999.json",     "geo": {       "type": "Polygon",       "coordinates": [         [           [             -102.051769,             36.99311           ],           [             -102.051769,             40.003282           ],           [             -94.588081,             40.003282           ],           [             -94.588081,             36.99311           ]         ]       ]     }`
    

      `    "location": {       "objectType": "place",       "displayName": "California, USA"     }`
    

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

Twitter entities object
-----------------------

For Activity streams format, the twitter\_entities is the same format and data dictionary shown on the native enriched format [entities object here](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/entities.html#entitiesobject).

### Example:

      `"twitter_entities": { 	"hashtags": [{ 		"text": "TwitterAPI", 		"indices": [ 			228, 			239 		] 	}], 	"urls": [{ 		"url": "https://t.co/r6z6CI7kEy", 		"expanded_url": "https://twittercommunity.com/t/retiring-labs-v2-recent-search-and-hide-replies/145795", 		"display_url": "twittercommunity.com/t/retiring-lab…", 		"indices": [ 			250, 			273 		] 	}], 	"user_mentions": [], 	"symbols": [] }`
    

Next steps
----------

Explore other Tweet JSON objects and data dictionaries:

* [Extended Entities object and data dictionary](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/extended-entities-object)
* [Tweet object and data dictionary](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object)
* [User object and data dictionary](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object)
* [Tweet geo objects and data dictionaries](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/geo-objects)

Extended entities object

Twitter extended entities object
--------------------------------

For Activity streams format, the twitter\_extended\_entities is the same format and data dictionary shown on the native enriched format [extended\_entities object here](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/extended-entities.html).

### Example:

      `"twitter_extended_entities":{ 	"media": [{ 		"id": 1293565706408038400, 		"id_str": "1293565706408038401", 		"indices": [ 			219, 			242 		], 		"additional_media_info": { 			"monetizable": false 		}, 		"media_url": "http://pbs.twimg.com/ext_tw_video_thumb/1293565706408038401/pu/img/66P2dvbU4a02jYbV.jpg", 		"media_url_https": "https://pbs.twimg.com/ext_tw_video_thumb/1293565706408038401/pu/img/66P2dvbU4a02jYbV.jpg", 		"url": "https://t.co/KaFSbjWUA8", 		"display_url": "pic.twitter.com/KaFSbjWUA8", 		"expanded_url": "https://twitter.com/TwitterDev/status/1293593516040269825/video/1", 		"type": "video", 		"video_info": { 			"aspect_ratio": [ 				16, 				9 			], 			"duration_millis": 34875, 			"variants": [{ 					"bitrate": 256000, 					"content_type": "video/mp4", 					"url": "https://video.twimg.com/ext_tw_video/1293565706408038401/pu/vid/480x270/Fg9lnGGsITO0uq2K.mp4?tag=10" 				}, 				{ 					"bitrate": 832000, 					"content_type": "video/mp4", 					"url": "https://video.twimg.com/ext_tw_video/1293565706408038401/pu/vid/640x360/-crbtZE4y8vKN_uF.mp4?tag=10" 				}, 				{ 					"content_type": "application/x-mpegURL", 					"url": "https://video.twimg.com/ext_tw_video/1293565706408038401/pu/pl/OvIqQojosF6sMIHR.m3u8?tag=10" 				}, 				{ 					"bitrate": 2176000, 					"content_type": "video/mp4", 					"url": "https://video.twimg.com/ext_tw_video/1293565706408038401/pu/vid/1280x720/xkxyb-VPVY4OI0j9.mp4?tag=10" 				} 			] 		}, 		"sizes": { 			"thumb": { 				"w": 150, 				"h": 150, 				"resize": "crop" 			}, 			"medium": { 				"w": 1200, 				"h": 675, 				"resize": "fit" 			}, 			"small": { 				"w": 680, 				"h": 383, 				"resize": "fit" 			}, 			"large": { 				"w": 1280, 				"h": 720, 				"resize": "fit" 			} 		} 	}] }`

Gnip object

Gnip object
-----------

The gnip object, within Activity streams format, contains the metadata added by the active enrichments, as well as indication of the matching rules for the activity.

### Data dictionary

|     |     |     |
| --- | --- | --- |
| **Field** | **Type** | **Description** |
| matching\_rules | array | Contains an array of matching rule objects which indicate the rule which the activity matches on.  <br>    **"matching\_rules": \[**<br><br>      **{**<br><br>        **"tag": null,**<br><br>        **"id":** 1026514022567358500**,**<br><br>        **"id\_str":** "1026514022567358464"<br><br>      **}**<br><br>    **\]** |
| urls | array | Contains an array of the links within the activity, and the expanded url metadata for the \*\*\*URL unwinding enrichement  <br>  <br>    **"urls": \[**<br><br>      **{**<br><br>        **"url":** "https://t.co/tGQqNxxyhU"**,**<br><br>        **"expanded\_url":** "https://www.youtube.com/channel/UCwUxW2CV2p5mzjMBqvqLzJA"**,**<br><br>        **"expanded\_status":** 200**,**<br><br>        **"expanded\_url\_title":** "Birdys Daughter"**,**<br><br>        **"expanded\_url\_description":** "Premium, single-origin, handpicked Jamaica Blue Mountain Coffee"<br><br>      **}**<br><br>    **\]** |
| profileLocations | array of location objects | Contains the derived location object from the Profile Geo enrichment  <br>  <br>    **"profileLocations": \[**<br><br>      **{**<br><br>        **"address": {**<br><br>          **"country":** "Canada"**,**<br><br>          **"countryCode":** "CA"**,**<br><br>          **"locality":** "Toronto"**,**<br><br>          **"region":** "Ontario"<br><br>        **},**<br><br>        **"displayName":** "Toronto, Ontario, Canada"**,**<br><br>        **"geo": {**<br><br>          **"coordinates": \[**<br><br>            \-79.4163**,**<br><br>            43.70011<br><br>          **\],**<br><br>          **"type":** "point"<br><br>        **},**<br><br>        **"objectType":** "place"<br><br>      **}**<br><br>    **\]**<br><br>  **}** |

### Example:

      `  "gnip": {     "matching_rules": [       {         "tag": null       }     ],     "urls": [       {         "url": "https://t.co/Nx1XZmRCXA",         "expanded_url": "https://twittercommunity.com/t/new-update-to-the-twitter-text-library-emoji-character-count/114607",         "expanded_status": 200,         "expanded_url_title": null,         "expanded_url_description": null       }     ]   }`

Activity Streams example payloads

Activity streams payload examples
---------------------------------

Tweet activity

      `{ 	"id": "tag:search.twitter.com,2005:1307025659294674945", 	"objectType": "activity", 	"verb": "post", 	"postedTime": "2020-09-18T18:36:15.000Z", 	"generator": { 		"displayName": "Twitter Web App", 		"link": "https://mobile.twitter.com" 	}, 	"provider": { 		"objectType": "service", 		"displayName": "Twitter", 		"link": "http://www.twitter.com" 	}, 	"link": "http://twitter.com/TwitterDev/statuses/1307025659294674945", 	"body": "Here’s an article that highlights the updates in the new Tweet payload v2 https://t.co/oeF3ZHeKQQ", 	"actor": { 		"objectType": "person", 		"id": "id:twitter.com:2244994945", 		"link": "http://www.twitter.com/TwitterDev", 		"displayName": "Twitter Dev", 		"postedTime": "2013-12-14T04:35:55.036Z", 		"image": "https://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg", 		"summary": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.", 		"friendsCount": 2038, 		"followersCount": 512292, 		"listedCount": 1666, 		"statusesCount": 3634, 		"twitterTimeZone": null, 		"verified": true, 		"utcOffset": null, 		"preferredUsername": "TwitterDev", 		"languages": [], 		"links": [{ 			"href": "https://developer.twitter.com/en/community", 			"rel": "me" 		}], 		"location": { 			"objectType": "place", 			"displayName": "127.0.0.1" 		}, 		"favoritesCount": 2147 	}, 	"object": { 		"objectType": "note", 		"id": "object:search.twitter.com,2005:1307025659294674945", 		"summary": "Here’s an article that highlights the updates in the new Tweet payload v2 https://t.co/oeF3ZHeKQQ", 		"link": "http://twitter.com/TwitterDev/statuses/1307025659294674945", 		"postedTime": "2020-09-18T18:36:15.000Z" 	}, 	"inReplyTo": { 		"link": "http://twitter.com/TwitterDev/statuses/1304102743196356610" 	}, 	"favoritesCount": 70, 	"twitter_entities": { 		"hashtags": [], 		"urls": [{ 			"url": "https://t.co/oeF3ZHeKQQ", 			"expanded_url": "https://dev.to/twitterdev/understanding-the-new-tweet-payload-in-the-twitter-api-v2-1fg5", 			"display_url": "dev.to/twitterdev/und…", 			"indices": [ 				74, 				97 			] 		}], 		"user_mentions": [], 		"symbols": [] 	}, 	"twitter_lang": "en", 	"retweetCount": 11, 	"gnip": { 		"matching_rules": [{ 			"tag": null 		}], 		"urls": [{ 			"url": "https://t.co/oeF3ZHeKQQ", 			"expanded_url": "https://dev.to/twitterdev/understanding-the-new-tweet-payload-in-the-twitter-api-v2-1fg5", 			"expanded_status": 200, 			"expanded_url_title": "Understanding the new Tweet payload in the Twitter API v2", 			"expanded_url_description": "Twitter recently announced the new Twitter API v2, rebuilt from the ground up to deliver new features..." 		}] 	}, 	"twitter_filter_level": "low" }`
    

Reply Tweet activity

      `{ 	"id": "tag:search.twitter.com,2005:1296887316556980230", 	"objectType": "activity", 	"verb": "post", 	"postedTime": "2020-08-21T19:10:05.000Z", 	"generator": { 		"displayName": "Twitter Web App", 		"link": "https://mobile.twitter.com" 	}, 	"provider": { 		"objectType": "service", 		"displayName": "Twitter", 		"link": "http://www.twitter.com" 	}, 	"link": "http://twitter.com/TwitterDev/statuses/1296887316556980230", 	"body": "See how @PennMedCDH are using Twitter data to understand the COVID-19 health crisis 📊\n\nhttps://t.co/1tdA8uDWes", 	"actor": { 		"objectType": "person", 		"id": "id:twitter.com:2244994945", 		"link": "http://www.twitter.com/TwitterDev", 		"displayName": "Twitter Dev", 		"postedTime": "2013-12-14T04:35:55.036Z", 		"image": "https://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg", 		"summary": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.", 		"friendsCount": 2038, 		"followersCount": 512292, 		"listedCount": 1666, 		"statusesCount": 3634, 		"twitterTimeZone": null, 		"verified": true, 		"utcOffset": null, 		"preferredUsername": "TwitterDev", 		"languages": [], 		"links": [{ 			"href": "https://developer.twitter.com/en/community", 			"rel": "me" 		}], 		"location": { 			"objectType": "place", 			"displayName": "127.0.0.1" 		}, 		"favoritesCount": 2147 	}, 	"object": { 		"objectType": "note", 		"id": "object:search.twitter.com,2005:1296887316556980230", 		"summary": "See how @PennMedCDH are using Twitter data to understand the COVID-19 health crisis 📊\n\nhttps://t.co/1tdA8uDWes", 		"link": "http://twitter.com/TwitterDev/statuses/1296887316556980230", 		"postedTime": "2020-08-21T19:10:05.000Z" 	}, 	"inReplyTo": { 		"link": "http://twitter.com/TwitterDev/statuses/1296887091901718529" 	}, 	"favoritesCount": 26, 	"twitter_entities": { 		"hashtags": [], 		"urls": [{ 			"url": "https://t.co/1tdA8uDWes", 			"expanded_url": "https://developer.twitter.com/en/use-cases/success-stories/penn", 			"display_url": "developer.twitter.com/en/use-cases/s…", 			"indices": [ 				87, 				110 			] 		}], 		"user_mentions": [{ 			"screen_name": "PennMedCDH", 			"name": "Penn Med CDH", 			"id": 1615654896, 			"id_str": "1615654896", 			"indices": [ 				8, 				19 			] 		}], 		"symbols": [] 	}, 	"twitter_lang": "en", 	"retweetCount": 9, 	"gnip": { 		"matching_rules": [{ 			"tag": null 		}], 		"urls": [{ 			"url": "https://t.co/1tdA8uDWes", 			"expanded_url": "https://developer.twitter.com/en/use-cases/success-stories/penn", 			"expanded_status": 200, 			"expanded_url_title": "Penn Medicine Center for Digital Health", 			"expanded_url_description": "Penn Med Center for Digital Health has created a COVID-19 Twitter map that includes charts detailing sentiment, symptoms reported, state-by-state data cuts, and border data on the COVID-19 outbreak. In addition, their Penn Med With You initiative uses aggregate regional information from Twitter to inform their website and text-messaging service. The service uses this information to disseminate relevant and timely resources." 		}] 	}, 	"twitter_filter_level": "low" }`
    

Tweet activity with long\_object

      `{ 	"id": "tag:search.twitter.com,2005:1296121314218897408", 	"objectType": "activity", 	"verb": "post", 	"postedTime": "2020-08-19T16:26:16.000Z", 	"generator": { 		"displayName": "Twitter Web App", 		"link": "https://mobile.twitter.com" 	}, 	"provider": { 		"objectType": "service", 		"displayName": "Twitter", 		"link": "http://www.twitter.com" 	}, 	"link": "http://twitter.com/TwitterDev/statuses/1296121314218897408", 	"body": "The hide replies endpoint is launching today! \n\nDevelopers can hide replies to Tweets - a crucial way developers ca… https://t.co/VyfXs1RTXn", 	"long_object": { 		"body": "The hide replies endpoint is launching today! \n\nDevelopers can hide replies to Tweets - a crucial way developers can help improve the health of the public conversation using the #TwitterAPI.\n\nhttps://t.co/khXhTurm9x", 		"display_text_range": [ 			0, 			215 		], 		"twitter_entities": { 			"hashtags": [{ 				"text": "TwitterAPI", 				"indices": [ 					178, 					189 				] 			}], 			"urls": [{ 				"url": "https://t.co/khXhTurm9x", 				"expanded_url": "https://twittercommunity.com/t/hide-replies-now-available-in-the-new-twitter-api/140996", 				"display_url": "twittercommunity.com/t/hide-replies…", 				"indices": [ 					192, 					215 				] 			}], 			"user_mentions": [], 			"symbols": [] 		} 	}, 	"actor": { 		"objectType": "person", 		"id": "id:twitter.com:2244994945", 		"link": "http://www.twitter.com/TwitterDev", 		"displayName": "Twitter Dev", 		"postedTime": "2013-12-14T04:35:55.036Z", 		"image": "https://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg", 		"summary": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.", 		"friendsCount": 2038, 		"followersCount": 512292, 		"listedCount": 1666, 		"statusesCount": 3634, 		"twitterTimeZone": null, 		"verified": true, 		"utcOffset": null, 		"preferredUsername": "TwitterDev", 		"languages": [], 		"links": [{ 			"href": "https://developer.twitter.com/en/community", 			"rel": "me" 		}], 		"location": { 			"objectType": "place", 			"displayName": "127.0.0.1" 		}, 		"favoritesCount": 2147 	}, 	"object": { 		"objectType": "note", 		"id": "object:search.twitter.com,2005:1296121314218897408", 		"summary": "The hide replies endpoint is launching today! \n\nDevelopers can hide replies to Tweets - a crucial way developers ca… https://t.co/VyfXs1RTXn", 		"link": "http://twitter.com/TwitterDev/statuses/1296121314218897408", 		"postedTime": "2020-08-19T16:26:16.000Z" 	}, 	"favoritesCount": 172, 	"twitter_entities": { 		"hashtags": [], 		"urls": [{ 			"url": "https://t.co/VyfXs1RTXn", 			"expanded_url": "https://twitter.com/i/web/status/1296121314218897408", 			"display_url": "twitter.com/i/web/status/1…", 			"indices": [ 				117, 				140 			] 		}], 		"user_mentions": [], 		"symbols": [] 	}, 	"twitter_lang": "en", 	"retweetCount": 54, 	"gnip": { 		"matching_rules": [{ 			"tag": null 		}], 		"urls": [{ 			"url": "https://t.co/khXhTurm9x", 			"expanded_url": "https://twittercommunity.com/t/hide-replies-now-available-in-the-new-twitter-api/140996", 			"expanded_status": 200, 			"expanded_url_title": "Hide replies now available in the new Twitter API", 			"expanded_url_description": "Today, we’re happy to announce the general availability of the hide replies endpoint in the new Twitter API. The hide replies endpoint allows you to build tools that help people hide or unhide replies to their Tweets. People manage their replies for many reasons, including to give less attention to comments that are abusive, distracting, misleading, or to make conversations more engaging. Through this endpoint, you can build tools to help people on Twitter hide or unhide replies faster and more..." 		}] 	}, 	"twitter_filter_level": "low" }`
    

Tweet activity with twitter\_extended\_entities

      `{ 	"id": "tag:search.twitter.com,2005:1293593516040269825", 	"objectType": "activity", 	"verb": "post", 	"postedTime": "2020-08-12T17:01:42.000Z", 	"generator": { 		"displayName": "Twitter Web App", 		"link": "https://mobile.twitter.com" 	}, 	"provider": { 		"objectType": "service", 		"displayName": "Twitter", 		"link": "http://www.twitter.com" 	}, 	"link": "http://twitter.com/TwitterDev/statuses/1293593516040269825", 	"body": "It’s finally here! 🥁 Say hello to the new #TwitterAPI.\n\nWe’re rebuilding the Twitter API v2 from the ground up to b… https://t.co/UeCndQGMjx", 	"long_object": { 		"body": "It’s finally here! 🥁 Say hello to the new #TwitterAPI.\n\nWe’re rebuilding the Twitter API v2 from the ground up to better serve our developer community. And today’s launch is only the beginning.\n\nhttps://t.co/32VrwpGaJw https://t.co/KaFSbjWUA8", 		"display_text_range": [ 			0, 			218 		], 		"twitter_entities": { 			"hashtags": [{ 				"text": "TwitterAPI", 				"indices": [ 					42, 					53 				] 			}], 			"urls": [{ 				"url": "https://t.co/32VrwpGaJw", 				"expanded_url": "https://blog.twitter.com/developer/en_us/topics/tools/2020/introducing_new_twitter_api.html", 				"display_url": "blog.twitter.com/developer/en_u…", 				"indices": [ 					195, 					218 				] 			}], 			"user_mentions": [], 			"symbols": [], 			"media": [{ 				"id": 1293565706408038400, 				"id_str": "1293565706408038401", 				"indices": [ 					219, 					242 				], 				"additional_media_info": { 					"monetizable": false 				}, 				"media_url": "http://pbs.twimg.com/ext_tw_video_thumb/1293565706408038401/pu/img/66P2dvbU4a02jYbV.jpg", 				"media_url_https": "https://pbs.twimg.com/ext_tw_video_thumb/1293565706408038401/pu/img/66P2dvbU4a02jYbV.jpg", 				"url": "https://t.co/KaFSbjWUA8", 				"display_url": "pic.twitter.com/KaFSbjWUA8", 				"expanded_url": "https://twitter.com/TwitterDev/status/1293593516040269825/video/1", 				"type": "video", 				"video_info": { 					"aspect_ratio": [ 						16, 						9 					], 					"duration_millis": 34875, 					"variants": [{ 							"bitrate": 256000, 							"content_type": "video/mp4", 							"url": "https://video.twimg.com/ext_tw_video/1293565706408038401/pu/vid/480x270/Fg9lnGGsITO0uq2K.mp4?tag=10" 						}, 						{ 							"bitrate": 832000, 							"content_type": "video/mp4", 							"url": "https://video.twimg.com/ext_tw_video/1293565706408038401/pu/vid/640x360/-crbtZE4y8vKN_uF.mp4?tag=10" 						}, 						{ 							"content_type": "application/x-mpegURL", 							"url": "https://video.twimg.com/ext_tw_video/1293565706408038401/pu/pl/OvIqQojosF6sMIHR.m3u8?tag=10" 						}, 						{ 							"bitrate": 2176000, 							"content_type": "video/mp4", 							"url": "https://video.twimg.com/ext_tw_video/1293565706408038401/pu/vid/1280x720/xkxyb-VPVY4OI0j9.mp4?tag=10" 						} 					] 				}, 				"sizes": { 					"thumb": { 						"w": 150, 						"h": 150, 						"resize": "crop" 					}, 					"medium": { 						"w": 1200, 						"h": 675, 						"resize": "fit" 					}, 					"small": { 						"w": 680, 						"h": 383, 						"resize": "fit" 					}, 					"large": { 						"w": 1280, 						"h": 720, 						"resize": "fit" 					} 				} 			}] 		}, 		"twitter_extended_entities": { 			"media": [{ 				"id": 1293565706408038400, 				"id_str": "1293565706408038401", 				"indices": [ 					219, 					242 				], 				"additional_media_info": { 					"monetizable": false 				}, 				"media_url": "http://pbs.twimg.com/ext_tw_video_thumb/1293565706408038401/pu/img/66P2dvbU4a02jYbV.jpg", 				"media_url_https": "https://pbs.twimg.com/ext_tw_video_thumb/1293565706408038401/pu/img/66P2dvbU4a02jYbV.jpg", 				"url": "https://t.co/KaFSbjWUA8", 				"display_url": "pic.twitter.com/KaFSbjWUA8", 				"expanded_url": "https://twitter.com/TwitterDev/status/1293593516040269825/video/1", 				"type": "video", 				"video_info": { 					"aspect_ratio": [ 						16, 						9 					], 					"duration_millis": 34875, 					"variants": [{ 							"bitrate": 256000, 							"content_type": "video/mp4", 							"url": "https://video.twimg.com/ext_tw_video/1293565706408038401/pu/vid/480x270/Fg9lnGGsITO0uq2K.mp4?tag=10" 						}, 						{ 							"bitrate": 832000, 							"content_type": "video/mp4", 							"url": "https://video.twimg.com/ext_tw_video/1293565706408038401/pu/vid/640x360/-crbtZE4y8vKN_uF.mp4?tag=10" 						}, 						{ 							"content_type": "application/x-mpegURL", 							"url": "https://video.twimg.com/ext_tw_video/1293565706408038401/pu/pl/OvIqQojosF6sMIHR.m3u8?tag=10" 						}, 						{ 							"bitrate": 2176000, 							"content_type": "video/mp4", 							"url": "https://video.twimg.com/ext_tw_video/1293565706408038401/pu/vid/1280x720/xkxyb-VPVY4OI0j9.mp4?tag=10" 						} 					] 				}, 				"sizes": { 					"thumb": { 						"w": 150, 						"h": 150, 						"resize": "crop" 					}, 					"medium": { 						"w": 1200, 						"h": 675, 						"resize": "fit" 					}, 					"small": { 						"w": 680, 						"h": 383, 						"resize": "fit" 					}, 					"large": { 						"w": 1280, 						"h": 720, 						"resize": "fit" 					} 				} 			}] 		} 	}, 	"display_text_range": [ 		0, 		140 	], 	"actor": { 		"objectType": "person", 		"id": "id:twitter.com:2244994945", 		"link": "http://www.twitter.com/TwitterDev", 		"displayName": "Twitter Dev", 		"postedTime": "2013-12-14T04:35:55.036Z", 		"image": "https://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg", 		"summary": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.", 		"friendsCount": 2038, 		"followersCount": 512292, 		"listedCount": 1666, 		"statusesCount": 3634, 		"twitterTimeZone": null, 		"verified": true, 		"utcOffset": null, 		"preferredUsername": "TwitterDev", 		"languages": [], 		"links": [{ 			"href": "https://developer.twitter.com/en/community", 			"rel": "me" 		}], 		"location": { 			"objectType": "place", 			"displayName": "127.0.0.1" 		}, 		"favoritesCount": 2147 	}, 	"object": { 		"objectType": "note", 		"id": "object:search.twitter.com,2005:1293593516040269825", 		"summary": "It’s finally here! 🥁 Say hello to the new #TwitterAPI.\n\nWe’re rebuilding the Twitter API v2 from the ground up to b… https://t.co/UeCndQGMjx", 		"link": "http://twitter.com/TwitterDev/statuses/1293593516040269825", 		"postedTime": "2020-08-12T17:01:42.000Z" 	}, 	"favoritesCount": 2844, 	"twitter_entities": { 		"hashtags": [{ 			"text": "TwitterAPI", 			"indices": [ 				42, 				53 			] 		}], 		"urls": [{ 			"url": "https://t.co/UeCndQGMjx", 			"expanded_url": "https://twitter.com/i/web/status/1293593516040269825", 			"display_url": "twitter.com/i/web/status/1…", 			"indices": [ 				117, 				140 			] 		}], 		"user_mentions": [], 		"symbols": [] 	}, 	"twitter_lang": "en", 	"retweetCount": 958, 	"gnip": { 		"matching_rules": [{ 			"tag": null 		}], 		"urls": [{ 			"url": "https://t.co/32VrwpGaJw", 			"expanded_url": "https://blog.twitter.com/developer/en_us/topics/tools/2020/introducing_new_twitter_api.html", 			"expanded_status": 200, 			"expanded_url_title": "Introducing a new and improved Twitter API", 			"expanded_url_description": "Introducing the new Twitter API - rebuilt from the ground up to deliver new features faster so developers can help the world connect to the public conversation happening on Twitter." 		}] 	}, 	"twitter_filter_level": "low" }`
    

Retweet activity

      `{ 	"id": "tag:search.twitter.com,2005:1229851574555508737", 	"objectType": "activity", 	"verb": "share", 	"postedTime": "2020-02-18T19:33:59.000Z", 	"generator": { 		"displayName": "Twitter Web App", 		"link": "https://mobile.twitter.com" 	}, 	"provider": { 		"objectType": "service", 		"displayName": "Twitter", 		"link": "http://www.twitter.com" 	}, 	"link": "http://twitter.com/TwitterDev/statuses/1229851574555508737", 	"body": "RT @suhemparack: I built an Alexa Skill for Twitter using APL that allows you to view Tweets and Trends on the echo show!\n\nCheck it out her…", 	"actor": { 		"objectType": "person", 		"id": "id:twitter.com:2244994945", 		"link": "http://www.twitter.com/TwitterDev", 		"displayName": "Twitter Dev", 		"postedTime": "2013-12-14T04:35:55.036Z", 		"image": "https://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg", 		"summary": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.", 		"friendsCount": 2038, 		"followersCount": 512292, 		"listedCount": 1666, 		"statusesCount": 3634, 		"twitterTimeZone": null, 		"verified": true, 		"utcOffset": null, 		"preferredUsername": "TwitterDev", 		"languages": [], 		"links": [{ 			"href": "https://developer.twitter.com/en/community", 			"rel": "me" 		}], 		"location": { 			"objectType": "place", 			"displayName": "127.0.0.1" 		}, 		"favoritesCount": 2147 	}, 	"object": { 		"id": "tag:search.twitter.com,2005:1229843515603144704", 		"objectType": "activity", 		"verb": "post", 		"postedTime": "2020-02-18T19:01:58.000Z", 		"generator": { 			"displayName": "Twitter Web App", 			"link": "https://mobile.twitter.com" 		}, 		"provider": { 			"objectType": "service", 			"displayName": "Twitter", 			"link": "http://www.twitter.com" 		}, 		"link": "http://twitter.com/suhemparack/statuses/1229843515603144704", 		"body": "I built an Alexa Skill for Twitter using APL that allows you to view Tweets and Trends on the echo show!\n\nCheck it… https://t.co/RP9NgltX7i", 		"long_object": { 			"body": "I built an Alexa Skill for Twitter using APL that allows you to view Tweets and Trends on the echo show!\n\nCheck it out here 👇\n\nhttps://t.co/l5J8wq748G", 			"display_text_range": [ 				0, 				150 			], 			"twitter_entities": { 				"hashtags": [], 				"urls": [{ 					"url": "https://t.co/l5J8wq748G", 					"expanded_url": "https://dev.to/twitterdev/building-an-alexa-skill-for-twitter-using-alexa-presentation-language-1aj0", 					"display_url": "dev.to/twitterdev/bui…", 					"indices": [ 						127, 						150 					] 				}], 				"user_mentions": [], 				"symbols": [] 			} 		}, 		"actor": { 			"objectType": "person", 			"id": "id:twitter.com:857699969263964161", 			"link": "http://www.twitter.com/suhemparack", 			"displayName": "Suhem Parack", 			"postedTime": "2017-04-27T20:56:22.883Z", 			"image": "https://pbs.twimg.com/profile_images/1230703695051935747/TbQKe91L_normal.jpg", 			"summary": "Developer Relations for Academic Research @Twitter. Talk to me about research with Twitter data. Previously: Amazon Alexa. Views are my own", 			"friendsCount": 501, 			"followersCount": 732, 			"listedCount": 12, 			"statusesCount": 458, 			"twitterTimeZone": null, 			"verified": false, 			"utcOffset": null, 			"preferredUsername": "suhemparack", 			"languages": [], 			"links": [{ 				"href": "https://developer.twitter.com", 				"rel": "me" 			}], 			"location": { 				"objectType": "place", 				"displayName": "Seattle, WA" 			}, 			"favoritesCount": 358 		}, 		"object": { 			"objectType": "note", 			"id": "object:search.twitter.com,2005:1229843515603144704", 			"summary": "I built an Alexa Skill for Twitter using APL that allows you to view Tweets and Trends on the echo show!\n\nCheck it… https://t.co/RP9NgltX7i", 			"link": "http://twitter.com/suhemparack/statuses/1229843515603144704", 			"postedTime": "2020-02-18T19:01:58.000Z" 		}, 		"favoritesCount": 71, 		"twitter_entities": { 			"hashtags": [], 			"urls": [{ 				"url": "https://t.co/RP9NgltX7i", 				"expanded_url": "https://twitter.com/i/web/status/1229843515603144704", 				"display_url": "twitter.com/i/web/status/1…", 				"indices": [ 					116, 					139 				] 			}], 			"user_mentions": [], 			"symbols": [] 		}, 		"twitter_lang": "en", 		"twitter_filter_level": "low" 	}, 	"favoritesCount": 0, 	"twitter_entities": { 		"hashtags": [], 		"urls": [], 		"user_mentions": [{ 			"screen_name": "suhemparack", 			"name": "Suhem Parack", 			"id": 857699969263964200, 			"id_str": "857699969263964161", 			"indices": [ 				3, 				15 			] 		}], 		"symbols": [] 	}, 	"twitter_lang": "en", 	"retweetCount": 19, 	"gnip": { 		"matching_rules": [{ 			"tag": null 		}], 		"urls": [{ 			"url": "https://t.co/l5J8wq748G", 			"expanded_url": "https://dev.to/twitterdev/building-an-alexa-skill-for-twitter-using-alexa-presentation-language-1aj0", 			"expanded_status": 200, 			"expanded_url_title": null, 			"expanded_url_description": null 		}] 	}, 	"twitter_filter_level": "low" }`
    

Quote Tweet activity

      ` {  	"id": "tag:search.twitter.com,2005:1328399838128467969",  	"objectType": "activity",  	"verb": "post",  	"postedTime": "2020-11-16T18:09:36.000Z",  	"generator": {  		"displayName": "Twitter Web App",  		"link": "https://mobile.twitter.com"  	},  	"provider": {  		"objectType": "service",  		"displayName": "Twitter",  		"link": "http://www.twitter.com"  	},  	"link": "http://twitter.com/TwitterDev/statuses/1328399838128467969",  	"body": "As planned, the Labs v2 endpoints referenced below have now been retired. Please let us know in the forums if you h… https://t.co/ahQvTYaOcZ",  	"long_object": {  		"body": "As planned, the Labs v2 endpoints referenced below have now been retired. Please let us know in the forums if you have questions or need help with the Twitter API v2! https://t.co/JaxttUMmjX",  		"display_text_range": [  			0,  			166  		],  		"twitter_entities": {  			"hashtags": [],  			"urls": [{  				"url": "https://t.co/JaxttUMmjX",  				"expanded_url": "https://twitter.com/TwitterDev/status/1327011423252144128",  				"display_url": "twitter.com/TwitterDev/sta…",  				"indices": [  					167,  					190  				]  			}],  			"user_mentions": [],  			"symbols": []  		}  	},  	"display_text_range": [  		0,  		140  	],  	"actor": {  		"objectType": "person",  		"id": "id:twitter.com:2244994945",  		"link": "http://www.twitter.com/TwitterDev",  		"displayName": "Twitter Dev",  		"postedTime": "2013-12-14T04:35:55.036Z",  		"image": "https://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg",  		"summary": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",  		"friendsCount": 2038,  		"followersCount": 512292,  		"listedCount": 1666,  		"statusesCount": 3634,  		"twitterTimeZone": null,  		"verified": true,  		"utcOffset": null,  		"preferredUsername": "TwitterDev",  		"languages": [],  		"links": [{  			"href": "https://developer.twitter.com/en/community",  			"rel": "me"  		}],  		"location": {  			"objectType": "place",  			"displayName": "127.0.0.1"  		},  		"favoritesCount": 2147  	},  	"object": {  		"objectType": "note",  		"id": "object:search.twitter.com,2005:1328399838128467969",  		"summary": "As planned, the Labs v2 endpoints referenced below have now been retired. Please let us know in the forums if you h… https://t.co/ahQvTYaOcZ",  		"link": "http://twitter.com/TwitterDev/statuses/1328399838128467969",  		"postedTime": "2020-11-16T18:09:36.000Z"  	},  	"favoritesCount": 29,  	"twitter_entities": {  		"hashtags": [],  		"urls": [{  			"url": "https://t.co/ahQvTYaOcZ",  			"expanded_url": "https://twitter.com/i/web/status/1328399838128467969",  			"display_url": "twitter.com/i/web/status/1…",  			"indices": [  				117,  				140  			]  		}],  		"user_mentions": [],  		"symbols": []  	},  	"twitter_lang": "en",  	"retweetCount": 7,  	"gnip": {  		"matching_rules": [{  			"tag": null  		}],  		"urls": [{  			"url": "https://t.co/r6z6CI7kEy",  			"expanded_url": "https://twittercommunity.com/t/retiring-labs-v2-recent-search-and-hide-replies/145795",  			"expanded_status": 200,  			"expanded_url_title": "Retiring Labs v2 recent search and hide replies",  			"expanded_url_description": "As we said in our Early Access and hide replies announcements, the following Twitter Developer Labs v2 endpoints will be retired on November 16th. Labs v2 recent search Labs v2 hide replies If called, these endpoints will respond with an HTTP 410 status and return no data. Based on your feedback from Labs, we incorporated corresponding functionality into the Twitter API v2. The relevant documentation can be found using the links below. Click here to enroll in v2 access if you haven’t already..."  		}]  	},  	"twitter_filter_level": "low",  	"twitter_quoted_status": {  		"id": "tag:search.twitter.com,2005:1327011423252144128",  		"objectType": "activity",  		"verb": "post",  		"postedTime": "2020-11-12T22:12:32.000Z",  		"generator": {  			"displayName": "Twitter Web App",  			"link": "https://mobile.twitter.com"  		},  		"provider": {  			"objectType": "service",  			"displayName": "Twitter",  			"link": "http://www.twitter.com"  		},  		"link": "http://twitter.com/TwitterDev/statuses/1327011423252144128",  		"body": "👋 Friendly reminder that Twitter Developer Labs v2 hide replies and recent search will be retired next Monday, Nove… https://t.co/EEWN2Q9aXh",  		"long_object": {  			"body": "👋 Friendly reminder that Twitter Developer Labs v2 hide replies and recent search will be retired next Monday, November 16! We encourage you to migrate to the new hide replies and recent search endpoints now available in the v2 #TwitterAPI. Details: https://t.co/r6z6CI7kEy",  			"display_text_range": [  				0,  				273  			],  			"twitter_entities": {  				"hashtags": [{  					"text": "TwitterAPI",  					"indices": [  						228,  						239  					]  				}],  				"urls": [{  					"url": "https://t.co/r6z6CI7kEy",  					"expanded_url": "https://twittercommunity.com/t/retiring-labs-v2-recent-search-and-hide-replies/145795",  					"display_url": "twittercommunity.com/t/retiring-lab…",  					"indices": [  						250,  						273  					]  				}],  				"user_mentions": [],  				"symbols": []  			}  		},  		"actor": {  			"objectType": "person",  			"id": "id:twitter.com:2244994945",  			"link": "http://www.twitter.com/TwitterDev",  			"displayName": "Twitter Dev",  			"postedTime": "2013-12-14T04:35:55.036Z",  			"image": "https://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg",  			"summary": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",  			"friendsCount": 2038,  			"followersCount": 512292,  			"listedCount": 1666,  			"statusesCount": 3634,  			"twitterTimeZone": null,  			"verified": true,  			"utcOffset": null,  			"preferredUsername": "TwitterDev",  			"languages": [],  			"links": [{  				"href": "https://developer.twitter.com/en/community",  				"rel": "me"  			}],  			"location": {  				"objectType": "place",  				"displayName": "127.0.0.1"  			},  			"favoritesCount": 2147  		},  		"object": {  			"objectType": "note",  			"id": "object:search.twitter.com,2005:1327011423252144128",  			"summary": "👋 Friendly reminder that Twitter Developer Labs v2 hide replies and recent search will be retired next Monday, Nove… https://t.co/EEWN2Q9aXh",  			"link": "http://twitter.com/TwitterDev/statuses/1327011423252144128",  			"postedTime": "2020-11-12T22:12:32.000Z"  		},  		"favoritesCount": 33,  		"twitter_entities": {  			"hashtags": [],  			"urls": [{  				"url": "https://t.co/EEWN2Q9aXh",  				"expanded_url": "https://twitter.com/i/web/status/1327011423252144128",  				"display_url": "twitter.com/i/web/status/1…",  				"indices": [  					117,  					140  				]  			}],  			"user_mentions": [],  			"symbols": []  		},  		"twitter_lang": "en",  		"twitter_filter_level": "low"  	}  }`
    

Retweetd Quote Tweet activity

      `{ 	"id": "tag:search.twitter.com,2005:1225470895902412800", 	"objectType": "activity", 	"verb": "share", 	"postedTime": "2020-02-06T17:26:44.000Z", 	"generator": { 		"displayName": "Twitter for iPhone", 		"link": "http://twitter.com/download/iphone" 	}, 	"provider": { 		"objectType": "service", 		"displayName": "Twitter", 		"link": "http://www.twitter.com" 	}, 	"link": "http://twitter.com/TwitterDev/statuses/1225470895902412800", 	"body": "RT @AureliaSpecker: 📣 If you enjoyed the London commute tutorial I wrote in November last year, check out the refactored version that uses…", 	"actor": { 		"objectType": "person", 		"id": "id:twitter.com:2244994945", 		"link": "http://www.twitter.com/TwitterDev", 		"displayName": "Twitter Dev", 		"postedTime": "2013-12-14T04:35:55.036Z", 		"image": "https://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg", 		"summary": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.", 		"friendsCount": 2038, 		"followersCount": 512292, 		"listedCount": 1666, 		"statusesCount": 3634, 		"twitterTimeZone": null, 		"verified": true, 		"utcOffset": null, 		"preferredUsername": "TwitterDev", 		"languages": [], 		"links": [{ 			"href": "https://developer.twitter.com/en/community", 			"rel": "me" 		}], 		"location": { 			"objectType": "place", 			"displayName": "127.0.0.1" 		}, 		"favoritesCount": 2147 	}, 	"object": { 		"id": "tag:search.twitter.com,2005:1224709550214873090", 		"objectType": "activity", 		"verb": "post", 		"postedTime": "2020-02-04T15:01:25.000Z", 		"generator": { 			"displayName": "Twitter Web App", 			"link": "https://mobile.twitter.com" 		}, 		"provider": { 			"objectType": "service", 			"displayName": "Twitter", 			"link": "http://www.twitter.com" 		}, 		"link": "http://twitter.com/AureliaSpecker/statuses/1224709550214873090", 		"body": "📣 If you enjoyed the London commute tutorial I wrote in November last year, check out the refactored version that u… https://t.co/cAepHunkFp", 		"long_object": { 			"body": "📣 If you enjoyed the London commute tutorial I wrote in November last year, check out the refactored version that uses Twitter's new search endpoint 🚇 https://t.co/87XIPZmZBJ\n\n#DEVcommunity #Pythontutorial @TwitterDev @TwitterAPI https://t.co/dXrJYvn3hY", 			"display_text_range": [ 				0, 				229 			], 			"twitter_entities": { 				"hashtags": [{ 						"text": "DEVcommunity", 						"indices": [ 							176, 							189 						] 					}, 					{ 						"text": "Pythontutorial", 						"indices": [ 							190, 							205 						] 					} 				], 				"urls": [{ 						"url": "https://t.co/87XIPZmZBJ", 						"expanded_url": "https://bit.ly/2OrnrCC", 						"display_url": "bit.ly/2OrnrCC", 						"indices": [ 							151, 							174 						] 					}, 					{ 						"url": "https://t.co/dXrJYvn3hY", 						"expanded_url": "https://twitter.com/AureliaSpecker/status/1195000047089389573", 						"display_url": "twitter.com/AureliaSpecker…", 						"indices": [ 							230, 							253 						] 					} 				], 				"user_mentions": [{ 						"screen_name": "TwitterDev", 						"name": "Twitter Dev", 						"id": 2244994945, 						"id_str": "2244994945", 						"indices": [ 							206, 							217 						] 					}, 					{ 						"screen_name": "TwitterAPI", 						"name": "Twitter API", 						"id": 6253282, 						"id_str": "6253282", 						"indices": [ 							218, 							229 						] 					} 				], 				"symbols": [] 			} 		}, 		"display_text_range": [ 			0, 			140 		], 		"actor": { 			"objectType": "person", 			"id": "id:twitter.com:1102321381", 			"link": "http://www.twitter.com/AureliaSpecker", 			"displayName": "Aurelia Specker", 			"postedTime": "2013-01-18T23:45:43.000Z", 			"image": "https://pbs.twimg.com/profile_images/1137517534104772608/8FBYgc6G_normal.jpg", 			"summary": "devrel @TwitterUK • Swiss in London • mother of houseplants • personal hairdresser to @_dormrod", 			"friendsCount": 1331, 			"followersCount": 1032, 			"listedCount": 26, 			"statusesCount": 854, 			"twitterTimeZone": null, 			"verified": false, 			"utcOffset": null, 			"preferredUsername": "AureliaSpecker", 			"languages": [], 			"links": [{ 				"href": null, 				"rel": "me" 			}], 			"location": { 				"objectType": "place", 				"displayName": "London, UK" 			}, 			"favoritesCount": 4979 		}, 		"object": { 			"objectType": "note", 			"id": "object:search.twitter.com,2005:1224709550214873090", 			"summary": "📣 If you enjoyed the London commute tutorial I wrote in November last year, check out the refactored version that u… https://t.co/cAepHunkFp", 			"link": "http://twitter.com/AureliaSpecker/statuses/1224709550214873090", 			"postedTime": "2020-02-04T15:01:25.000Z" 		}, 		"favoritesCount": 43, 		"twitter_entities": { 			"hashtags": [], 			"urls": [{ 				"url": "https://t.co/cAepHunkFp", 				"expanded_url": "https://twitter.com/i/web/status/1224709550214873090", 				"display_url": "twitter.com/i/web/status/1…", 				"indices": [ 					117, 					140 				] 			}], 			"user_mentions": [], 			"symbols": [] 		}, 		"twitter_lang": "en", 		"twitter_filter_level": "low" 	}, 	"favoritesCount": 0, 	"twitter_entities": { 		"hashtags": [], 		"urls": [], 		"user_mentions": [{ 			"screen_name": "AureliaSpecker", 			"name": "Aurelia Specker", 			"id": 1102321381, 			"id_str": "1102321381", 			"indices": [ 				3, 				18 			] 		}], 		"symbols": [] 	}, 	"twitter_lang": "en", 	"retweetCount": 12, 	"gnip": { 		"matching_rules": [{ 			"tag": null 		}], 		"urls": [{ 				"url": "https://t.co/87XIPZmZBJ", 				"expanded_url": "https://dev.to/twitterdev/migrate-to-twitter-s-newly-released-labs-recent-search-endpoint-3npe", 				"expanded_status": 200, 				"expanded_url_title": null, 				"expanded_url_description": null 			}, 			{ 				"url": "https://t.co/sOjXW4YhbN", 				"expanded_url": "https://dev.to/twitterdev/using-the-twitter-api-to-make-your-commute-easier-3od0", 				"expanded_status": 200, 				"expanded_url_title": null, 				"expanded_url_description": null 			} 		] 	}, 	"twitter_filter_level": "low", 	"twitter_quoted_status": { 		"id": "tag:search.twitter.com,2005:1195000047089389573", 		"objectType": "activity", 		"verb": "post", 		"postedTime": "2019-11-14T15:26:27.000Z", 		"generator": { 			"displayName": "Twitter Web App", 			"link": "https://mobile.twitter.com" 		}, 		"provider": { 			"objectType": "service", 			"displayName": "Twitter", 			"link": "http://www.twitter.com" 		}, 		"link": "http://twitter.com/AureliaSpecker/statuses/1195000047089389573", 		"body": "I wrote a tutorial on how to get bespoke commute information using the Twitter API🚇\n\n#DEVcommunity #Pythontutorial… https://t.co/pL0qJ4vhtE", 		"long_object": { 			"body": "I wrote a tutorial on how to get bespoke commute information using the Twitter API🚇\n\n#DEVcommunity #Pythontutorial \n\nCheck it out here 👇\nhttps://t.co/sOjXW4YhbN", 			"display_text_range": [ 				0, 				160 			], 			"twitter_entities": { 				"hashtags": [{ 						"text": "DEVcommunity", 						"indices": [ 							85, 							98 						] 					}, 					{ 						"text": "Pythontutorial", 						"indices": [ 							99, 							114 						] 					} 				], 				"urls": [{ 					"url": "https://t.co/sOjXW4YhbN", 					"expanded_url": "https://dev.to/twitterdev/using-the-twitter-api-to-make-your-commute-easier-3od0", 					"display_url": "dev.to/twitterdev/usi…", 					"indices": [ 						137, 						160 					] 				}], 				"user_mentions": [], 				"symbols": [] 			} 		}, 		"actor": { 			"objectType": "person", 			"id": "id:twitter.com:1102321381", 			"link": "http://www.twitter.com/AureliaSpecker", 			"displayName": "Aurelia Specker", 			"postedTime": "2013-01-18T23:45:43.000Z", 			"image": "https://pbs.twimg.com/profile_images/1137517534104772608/8FBYgc6G_normal.jpg", 			"summary": "devrel @TwitterUK • Swiss in London • mother of houseplants • personal hairdresser to @_dormrod", 			"friendsCount": 1331, 			"followersCount": 1032, 			"listedCount": 26, 			"statusesCount": 854, 			"twitterTimeZone": null, 			"verified": false, 			"utcOffset": null, 			"preferredUsername": "AureliaSpecker", 			"languages": [], 			"links": [{ 				"href": null, 				"rel": "me" 			}], 			"location": { 				"objectType": "place", 				"displayName": "London, UK" 			}, 			"favoritesCount": 4979 		}, 		"object": { 			"objectType": "note", 			"id": "object:search.twitter.com,2005:1195000047089389573", 			"summary": "I wrote a tutorial on how to get bespoke commute information using the Twitter API🚇\n\n#DEVcommunity #Pythontutorial… https://t.co/pL0qJ4vhtE", 			"link": "http://twitter.com/AureliaSpecker/statuses/1195000047089389573", 			"postedTime": "2019-11-14T15:26:27.000Z" 		}, 		"favoritesCount": 123, 		"twitter_entities": { 			"hashtags": [{ 					"text": "DEVcommunity", 					"indices": [ 						85, 						98 					] 				}, 				{ 					"text": "Pythontutorial", 					"indices": [ 						99, 						114 					] 				} 			], 			"urls": [{ 				"url": "https://t.co/pL0qJ4vhtE", 				"expanded_url": "https://twitter.com/i/web/status/1195000047089389573", 				"display_url": "twitter.com/i/web/status/1…", 				"indices": [ 					116, 					139 				] 			}], 			"user_mentions": [], 			"symbols": [] 		}, 		"twitter_lang": "en", 		"twitter_filter_level": "low" 	} }`

Tweet metadata timeline

Jump to on this page

[Introduction](#intro)

[Key concepts](#key_concepts)

[Twitter timeline](#twitter_timeline)

[Filtering tips](#filtering_tips)

[Next steps](#next)

Introduction
------------

At its core, Twitter is a public, real-time, and global communication network. Since 2006, Twitter’s evolution has been driven by both user use-patterns and conventions and new product features and enhancements. If you are using Twitter data for historical research, understanding the timeline of this evolution is important for surfacing Tweets of interest from the data archive.

Twitter was launched as a simple SMS mobile app, and has grown into a comprehensive communication platform. A platform with a complete set of APIs. APIs have always been a pillar of the Twitter network. The [first API hit the streets soon after Twitter was launched](https://blog.twitter.com/2006/introducing-the-twitter-api). When geo-tagging Tweets was first introduced in 2009, it was made available through a [Geo API](https://blog.twitter.com/2009/think-globally-tweet-locally) (and later the ability to ‘geo-tag’ a Tweet was integrated into the Twitter.com user-interface). Today, Twitter’s APIs drive the two-way communication network that has become the source of breaking news and sharing information. The opportunities to build on top of this global, real-time communication channel are endless.  

Twitter makes available two historical APIs that provide access to every publicly available Tweet: [Historical PowerTrack](https://developer.twitter.com/en/docs/tweets/batch-historical) and the [Full-Archive Search API](https://developer.twitter.com/en/docs/tweets/search). Both APIs provide a set of _operators_ used to query and collect Tweets of interest. These operators match on a variety of attributes associated with every Tweet, hundreds of attributes such as the Tweet’s text content, the author’s account name, and links shared in the Tweet. Tweets and their attributes are encoded in JSON, a common text-based data-interchange format. So as new features were introduced, new JSON attributes appeared, and typically new API operators were introduced to match on those attributes. If your use-case includes a need to _listen_ to what the world has said on Twitter, the better you understand when operators started having JSON metadata to match on, the more effective your historical PowerTrack filters can be.  

Next, we will introduce some key concepts that set the stage for understanding how updates in Tweet metadata affect finding your data signal of interest.  

Key concepts
------------

#### From user-conventions to Twitter _first-class objects_

Twitter users organically introduced new, and now fundamental, communication patterns to the Twitter network. A seminal example is the hashtag, now nearly universally used across all social networks. Hashtags were introduced as a way to organize conversations and topics. On a network with hundreds of millions messages a day, tools to find Tweets of interest are key, and hashtags have become a fundamental method. Soon after the use of hashtags grew, they received official status and support from Twitter. As hashtags became a _‘first-class’ object_, this meant many things. It meant hashtags became clickable/searchable in the Twitter.com user interface. It also meant hashtags became a member of the Twitter _entities_ family, along with @mentions, attached media, stock symbols, and shared links. These entities are conveniently encoded in a pre-parsed JSON array, making it easier for developers to process, scan, and store them.

Retweets are another example of user-driven conventions becoming official objects. Retweeting emerged as a way of ‘forwarding’ content to others. It started as a manual process of copying/pasting a Tweet and prepending it with a “RT @” pattern. This process was eventually automated via a new Retweet button, complete with new JSON metadata. The ‘official’ Retweet was born. Other examples include ‘mentions’, sharing of media and web links, and sharing a location with your Tweet. Each of these use-patterns resulted in new [twitter.com](https://twitter.com/) user-interface features, new supporting JSON, and thus new ways to match on Tweets. All of these fundamental Tweet attributes have resulted in PowerTrack Operators used to match on them.  

#### Tweet metadata, mutability, updates, and currency

While Tweet messages can be up to a fixed number of characters long, the JSON description of a Tweet consists of over 100 attributes. Attributes such as who posted, at what time, whether it’s an original Tweet or a Retweet, and an array of first-class objects such as hashtags, mentions, and shared links. For the account that posted, there is a User (or Actor) object with a variety of attributes that provide the user’s Profile and other account metadata. Profiles include a short biographical description, a home location (freeform text), preferred language, and an optional web site link.

Some account metadata never change (e.g. numeric user ID and created date), some change slowly over time, while other attributes change more frequently. People change jobs and move. Companies updates their information. When you are collecting historical Tweets, it is important to understand how some metadata is _as it was when Tweeted_, and other metadata is _as it is when the query is submitted_. 

With all historical APIs, the user's profile description, display name, and profile 'home' attributes are updated to the values at the time of query.

#### “Native” media

Twitter.com and Twitter mobile apps support adding photos and videos to Tweets by clicking a button and browsing your photo galleries. Now that they are integrated as first-class actions, videos and photos shared this way are referred to as ‘native’ media.

Many querying Operators work with these ‘native’ resources, including `has:videos`, `has:images`, and `has:media`. These will match only on media content that was shared via Twitter features. To match on other media hosted off of the Twitter platform, you’ll want to use Operators that match on URL metadata.  

So, before we dig into the Historical PowerTrack and Full-Archive Search product details, let’s take a tour of how Twitter, as a product and platform, evolved over time.  

Twitter timeline
----------------

Below you will find a select _timeline_ of Twitter. Most of these Twitter updates in some way fundamentally affected either user behavior, Tweet JSON contents, query Operators, or all three. Looking at Twitter as a API platform, the following events in some way affected the JSON payloads that are used to encode Tweets. In turn, those JSON details affect how Twitter historical API match on them.

Note that this timeline list is generally precise and not exhaustive.  

#### 2006

* October
    * @replies becomes a convention.
    * $cashtags first emerge, but using for stock ticker mentions does not become common until early 2009. $Cashtags became a clickable/searchable link in June 2012.
* November - Favorites introduced.

#### 2007

* January - @replies become a first-class object with a UI reply button with `in_reply_to` metadata.
* April - Retweets become a convention.
* August - #hashtags emerge as a primary tool for searching and organizing Tweets.

#### 2009

* February - $cashtags become a common convention for discussing stock ticker symbols.
* May - Retweet ‘beta’ is introduced with “Via @” prepended to Tweet body.
* June - Verified accounts introduced.
* August - Retweets a first-class object with “RT @” pattern and new `retweet_status` metadata.
* October - List feature launched.
* November - [Tweet Geotagging API is launched](https://blog.twitter.com/2009/think-globally-tweet-locally), providing the first method for users to share location via third-party apps.

#### 2010

* June - Twitter Places introduced for geo-tagging Tweets.
* August - Tweet button for websites is launched. Made sharing links easier.

#### 2011

* May - Follow button introduced, making it easier to follow accounts associated with websites.
* August - Native photos introduced.

#### 2012

* June - $Cashtags become a clickable/searchable link.

#### 2014

* March - [Photo tagging and up to four photos supported](https://blog.twitter.com/2014/photos-just-got-more-social). _Extended_ Twitter Entities metadata was introduced.
* April - Emojis are natively supported in Twitter UI. Emojis were commonly used in Tweets since at least 2008.

#### 2015

* April - A change in Twitter’s ‘post Tweet’ user-interface design results in fewer Tweets being geo-tagged.
* October - [Twitter Polls introduced](https://blog.twitter.com/2015/introducing-twitter-polls). Polls originally supported two choices with a 24-hour voting period. In November, Polls started supporting four choices with voting periods from 5 minutes to seven days. Poll metadata made available (enriched native format only) in February 2017.

#### 2016

* February - [Searchable GIFs natively hosted in Tweet compose](https://blog.twitter.com/2016/introducing-gif-search-on-twitter).
* May - [“Doing More with 140”](https://blog.twitter.com/express-even-more-in-140-characters) (dmw140) announced, stating plans for new ways of handling Replies and attached media with respect to a Tweet’s 140-character message.
* June - [Native video support](https://blog.twitter.com/official/en_us/a/2016/new-ways-to-tap-into-video-on-twitter.html)
* June - Quoted Retweets generally available.
* June - [Stickers introduced for adding to photos](https://blog.twitter.com/2016/introducing-stickers-on-twitter).
* September - [‘Native attachments’ introduced](https://twitter.com/Twitter/status/777915304261193728) with trailing URL not counted towards 140 characters (“dmw140, part 1”).

#### 2017

* February - Twitter Poll metadata included in Tweet metadata (enriched native format only).
* April - [‘Simplified Replies’](https://blog.twitter.com/2017/now-on-twitter-140-characters-for-your-replies) introduced with replied-to-accounts not counted towards 140 characters (“dmw140, part 2”).

2018

* May - [GDPR updates](https://twittercommunity.com/t/upcoming-changes-to-the-developer-platform/104603) user.time\_zone set to null, user.utc\_offset set to null, user.profile\_background\_image\_url set to default value
* June - Updating [quoteTweet formatting changes](https://twittercommunity.com/t/updating-how-urls-are-rendered-in-the-quote-tweet-payload/105473)

2022

* September 29 - The ability to edit Tweets is rolled out to a small test group. Edited Tweet metadata are added to the Tweet object where relevant. This includes edit\_history and edit\_controls objects. These metadata will not be returned for Tweets that were created before editable functionality was added. No associated Operators for these metadata. To learn more about how Tweet edits work, see the [Edit Tweets fundamentals](https://developer.twitter.com/en/docs/twitter-api/edit-tweets)

Filtering tips
--------------

Being familiar with the Twitter timeline of when and how new features were added can help you create more effective queries. Here, a query means a _filter_ or _rule_ that is applied by the Twitter historical APIs to the Tweet archive, using PowerTrack Operators to match on Tweet JSON. An example is the `lang:` Operator, which is used to match Tweets in a specified language. Twitter provides a language classification service (supporting over 50 languages), and Twitter APIs provide this metadata in the JSON that is generated for every Tweet. So, if a Tweet is written in Spanish the “lang” JSON attribute is set to “es”. So, if you build a filter with the `lang:es` clause, it will only match on Tweet messages classified as Spanish.

The timeline information can also help better interpret the Tweet data received. Say you were researching the sharing of content about the 2008 and 2012 Summer Olympics. If you applied only the `is:retweet` Operator to match on Retweets, no data would match in 2008. However, for 2012 there would likely be millions of Retweets. From this you potentially could erroneously conclude that in 2008 Retweets were not a user convention, or that simply no one Retweeted about those Olympics. Since Retweets became a first-class object in 2009, you need to add a `”RT @”` rule clause to help identify them in 2008.  

Both Retweets and Tweet language classifying are examples of Tweet attributes with a long history and many product details. Below we will discuss more details of these and other attribute classes important to matching on and understanding Twitter Data.  

#### Recognizing false negatives

When it comes to writing filters, one important takeaway is that the metadata Operators match on all have “born on” dates. If you build a filter with an Operator that acts on metadata introduced after the Tweet was posted, you’ll have a false negative. For example, say you are interested in all Tweets that mention ‘snow’ and share a video. If you build a rule with the `has:videos` Operator, which matches on Tweets with _native_ videos, that clause will not match any Tweets before 2015.

However, sharing of videos has been common on Twitter long before 2015. Before then users shared links to videos hosted elsewhere, but in 2015, Twitter built new ‘sharing video’ features directly into the platform. For finding these earlier Tweets of interest, you would include a rule clause such as `url:”youtube.com”`.  

Note, with the Search APIs, there are some examples of metadata being ‘backfilled’ as its index was rebuilt. One good example are $cashtags, which became widely used to discuss stock symbols in 2009. After the $cashtag operator was introduced in 2015, the Search index was rebuilt, and in the process the symbol entity was extracted from all Tweet bodies, including early 2006 when `$` was used mainly for slang; “I hope it $now$ $oon!”.  

#### Identifying and filtering on Tweet attributes important to your use-case

Some metadata, such as Twitter account numeric IDs, have existed since day one (and are an example of account metadata that never changes). Other metadata was not introduced until well after Twitter started in 2006. Examples of new metadata being introduced include Retweets metadata, Tweet locations, URL titles and descriptions, and ‘native’ media. Below are some of the most common types of Tweet attributes that have been fundamentally affected by these Twitter platform updates.

Filtering/matching behavior for these depends, in most cases, on which historical Tweet API is used. To help determine which product is the best fit for your research and use-case, the attribute details provided below include high-level product information.  

#### Twitter Profiles

Since at its core Twitter is a global real-time communication channel, research with Tweet data commonly has an emphasis on who is communicating. Often it is helpful to know where a Twitter user calls home. Often knowing that an account bio includes mentions of interests and hobbies can lead you to Tweets of interest. It is very common to want to listen for Tweets from accounts of interest. Profile attributes are key to all of these use-cases.

Every account on Twitter has a Profile that includes metadata such as Twitter @handle, display name, a short bio, home location (freeform text entered by a user), number of followers and many others. Some attributes never change, such as numeric user ID and when the account was created. Others usually change day-to-day, week-to-week, or month-to-month, such as number of Tweets posted and number of accounts followed and followers. Other account attributes can also change at any time, but tend to change less frequently: display name, home location, and bio.  

The JSON payload for every Tweet includes _account profile_ metadata for the Tweet’s author. If it is a Retweet, it also includes profile metadata for the account that posted the original Tweet.  

The mutability of a Tweet’s profile metadata depends entirely on the historical product used. The Search APIs serve up historical Tweets with the profile settings _as it is at the time of retrieval_. For Historical PowerTrack, the profile is _as it was at the time the Tweet was posted_, except for data before 2011. For Tweets older than 2011, the profile metadata reflects the profile as it was in September 2011.

#### Original Tweets and Retweets

Retweets are another example of user-driven conventions becoming official objects. Retweeting emerged as a way of ‘forwarding’ content to others. It started as a manual process of copying/pasting a Tweet and prepending it with a “RT @” pattern. This process was eventually automated via a new Retweet button, complete with new JSON metadata. The ‘official’ Retweet was born and the action of retweeting became a first-class Tweet event. Along with the new Retweet button, new metadata was introduced such as the complete payload of the original Tweet.

Whether a Tweet is original or shared is a common filtering ‘switch.’ In some cases, only original content is needed. In other cases, Tweet engagement is of primary importance so Retweets are key. The PowerTrack `is:retweet` Operator enables users to either include or exclude Retweets. If pulling data from before August 2009, users need to have _two_ strategies for Retweet matching (or not matching). Before August 2009, the Tweet message itself needs to be checked, using exact phrase matching, for matches on the “@RT ” pattern. For periods after August 2009, the `is:retweet` Operator is available.  

#### Tweet language classifications

The language a Tweet is written in is a common interest. Tweet language can help infer a Tweet’s location and often only a specific language is needed for analysis or display. (Twitter profiles also have a preferred language setting.)

For filtering on a Tweet’s language classification, Twitter’s historical products ([Search API](https://developer.twitter.com/content/developer-twitter/en/docs/tweets/search/overview/enterprise) and [Historical PowerTrack](https://developer.twitter.com/content/developer-twitter/en/docs/tweets/batch-historical/overview)) are quite different. When the Search archive was built, all Tweets were backfilled with the Twitter language classification. Therefore the `lang:` Operator is available for the entire Tweet archive. With Historical PowerTrack, Twitter’s language classification metadata is available in the archive beginning on March 26, 2013. 

#### Geo-referencing Tweets

Being able to tell where a Tweet was posted (i.e., geo-referencing it) is important to many use-cases. There are three primary methods for geo-referencing Tweets:

* Geographical references in a Tweet message
* Tweets geo-tagged by the user.
* Account profile ‘home’ location set by a user

If geo-referencing is key to your use-case, be sure to review our [filtering tweets by location](https://developer.twitter.com/content/developer-twitter/en/docs/tutorials/filtering-tweets-by-location)and [tweet geo metadata](https://developer.twitter.com/content/developer-twitter/en/docs/tutorials/tweet-geo-metadata) tutorials.

##### Geographical references in a Tweet message

Matching on geographic references in the Tweet message, while often the most challenging method since it depends on local knowledge, is an option for the entire Tweet archive. Here is an example geo-referenced match from 2006 for the San Francisco area based on a ‘golden gate’ filter:

https://twitter.com/biz/statuses/28311

##### Tweets geo-tagged by the user

In November 2009 Twitter introduced its Tweet Geotagging API that enabled Tweets to be geo-tagged with an exact location. In June 2010 Twitter introduced Twitter Places that represent a geographic area on the venue, neighborhood, or town scale. Approximately 1-2% of Tweets are geo-tagged using either method.

The available geo-tagging history is dependent on the Historical API you are using. With the Search APIs the ability to start matching on Tweets with some Geo Operators started in March 2010, and with others on February 2015. If you are using Historical PowerTrack, geo-referencing starts on September 1, 2011. When the Historical PowerTrack archive was built, all geo-tagging before this date was not included.  

##### Account profile ‘home’ location set by a user

All Twitter users have the opportunity to set their Profile Location, indicating their home location. Millions of Twitter users provide this information, and it significantly increases the amount of geodata in the Twitter Firehose. This location metadata is a non-normalized, user-generated, free-form string. Approximately 30% of accounts have Profile Geo metadata that can be resolved to the country level.

As with Tweet geo, the methods to match and the time periods available depends on the Historical API you are using. Historical PowerTrack enables users to attempt their own custom matching on these free-form strings. To help make that process easier, Twitter also provides a [Profile Geo Enrichment](https://developer.twitter.com/content/developer-twitter/en/docs/tweets/enrichments/overview/profile-geo) that performs the geocoding where possible, providing normalized metadata and corresponding Operators. Profile Geo Operators are available in both Historical PowerTrack and the Search APIs. With Historical PowerTrack, these Profile Geo metadata is available starting in June 2014. With the Search APIs, this metadata is available starting in February 2015.  

#### Shared links and media

Sharing web page links, photos and videos have always been a fundamental Twitter use-case. Early in its history, all of these actions involved including a URL link in the Tweet message itself. In 2011 Twitter integrated sharing photos directly into its user-interface. In 2016, native videos were added.

Given this history, there are a variety of filtering Operators used for matching on this content. There are a set of Operators that match on whether Tweets have shared links, photos, and videos. Also, since most URLs shared on Twitter are shortened to use up fewer of a Tweet’s characters (e.g. generated by a service such as bitly or tinyurl), Twitter provides data enrichments that generate a complete, expanded URL that can be matched on. For example, if you wanted to match on Tweets that included links discussing Twitter and Early-warning systems, a filter that references ‘severe weather communication’ would match a Tweet containing this [http://bit.ly/1XV1tG4](http://bit.ly/1XV1tG4) URL.  

In March 2012, the [expanded URL enrichment](https://developer.twitter.com/content/developer-twitter/en/docs/tweets/enrichments/overview/expanded-and-enhanced-urls) was introduced. Before this time, the Tweet payloads included only the URL as provided by the user. So, if the user included a shortened URL it can be challenging to match on (expanded) URLs of interest. With both Historical PowerTrack and the Search APIs, these metadata are available starting in March 2012.  

In July 2016, the enhanced URL enrichment was introduced. This enhanced version provides a web site’s HTML title and description in the Tweet payload, along with Operators for matching on those. With Historical PowerTrack, these metadata become available in July 2016. With the Search APIs, these metadata begin emerging in December 2014.  

In September 2016 Twitter introduced ‘native attachments’ where a trailing shared link is not counted against the 140 Tweet character limit. Both URL enrichments still apply to these shared links.  

For other URL product-specific details on URL filtering, see the corresponding articles for more information.

Next steps
----------

Now that we’ve explored the timeline of when key Twitter features were introduced and learned how these metadata changes affect filtering at a high-level, the next step is to get into the many product-specific details:

* [Learn more about the Historical PowerTrack API and its metadata and filtering timeline](https://developer.twitter.com/en/docs/tweets/batch-historical/guides/hpt-timeline)
* [Learn more about the Full-Archive Search API and its metadata and filtering timeline](https://developer.twitter.com/en/docs/tweets/search/guides/fas-timeline)
* [Choosing between Historical PowerTrack and Full-Archive Search APIs](https://developer.twitter.com/en/docs/tutorials/choosing-historical-api)

Expanded and Enhanced URLs

Expanded and Enhanced URLs
--------------------------

The Expanded and Enhanced URL enrichment automatically expands shortened URLs that are included in the body of a Tweet, and includes the resulting URL as metadata within the payload. In addition, this enrichment also provides HTML page metadata from the `title` and `description` of the destination page.

**Important Details:**

* To resolve a shortened link, our system sends HTTP HEAD requests to the URL provided and follows any redirects until it arrives at the final URL. This final URL (NOT the content of the page itself) is then included in the response payload.  
    
* The URL enrichment does add between 5-10 seconds latency to realtime streams
* For requests made to the Full Archive Search API, expanded URL enrichment data is only available for Tweets 13 months old or newer.  
    
* The URL enrichment is not available for Tweet links (including quote Tweets), Moments links, and profile links that are included within a Tweet.   
     

### Tweet payload

The Expanded and Enhanced URL enrichment can be found within the `entities` object of the Tweet payload - specifically in the `entitites.urls.unwound` object. It provides the following fields of metadata:

* Expanded URL - `unwound.url`
* Expanded HTTP Status - `unwound.status`
* Expanded URL HTML title - 300 character limit - `unwound.title`
* Expanded URL HTML description - 1000 character limit - `unwound.description`

  
**This is an example of an [entities object](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/entities) with the URL enrichment:**

      `"entities": {     "hashtags": [            ],     "urls": [       {         "url": "https:\/\/t.co\/HkTkwFq8UT",         "expanded_url": "http:\/\/bit.ly\/2wYTb9y",         "display_url": "bit.ly\/2wYTb9y",         "unwound": {           "url": "https:\/\/www.forbes.com\/sites\/laurencebradford\/2016\/12\/08\/11-websites-to-learn-to-code-for-free-in-2017\/",           "status": 200,           "title": "11 Websites To Learn To Code For Free In 2017",           "description": "It\u2019s totally possible to learn to code for free...but what are the best resources to achieve that? Here are 11 websites where you can get started."         },         "indices": [           10,           33         ]       }     ],     "user_mentions": [            ],     "symbols": [            ]   },`
    

  
**This is an example of an entities object containing a Tweet link that is not enriched:  
**

      `"entities": {   "urls": [{      "url": "https://t.co/SywNbZdDmb",      "expanded_url": "https://twitter.com/TwitterDev/status/1050118621198921728",      "display_url": "twitter.com/TwitterDev/s…",      "indices": [          142,          165      ]    }   ] }`
    

### Filtering operators

The following operators will filter and provide a tokenized match on the related fields of URL metadata:

**url:**

* Example: “url:tennis”
* Tokenized match on any Expanded URL that includes the word tennis
* Could also be used as a filter to include or exclude links from a specific website using something like “url:npr.org”

**url\_title:**

* Example: “url\_title:tennis”
* Tokenized match on any Expanded URL HTML title that includes the word tennis
* Matches on the HTML title data included in the payload, which is limited to 300 characters.

**url\_description:**

* Example: “url\_description:tennis”
* Tokenized match on any Expanded URL HTML description that includes the word tennis
* Matches on the HTML description included in the payload, which is limited to 1000 characters.  
     

### HTTP Status Codes

The expanded URL enrichment also provides the HTTP status code for the final URL we are attempting to unwind. In normal cases, this will be a 200 value. Other 400-series values indicate problems with resolving the URL.

Various status codes may be returned when attempting to unwind a URL. During the process of unwinding a URL, if we get a redirect, we will follow them indefinitely until we either:

* Hit a 200 series code (success)
* Hit a non-redirect series code (failures)
* Timeout because the final URL could not be resolved in a reasonable amount of time (returns a 408 - timeout)
* Hit an exception of some sort  
     

If an exception is hit, we use the following mapping between reasons and status codes returned:

| Reason | Status Code Returned |
| --- | --- |
| SSL Exceptions | 403 (Forbidden) |
| Unwinding not allowed by URL | 405 |
| Socket Timeout | 408 (Timeout) |
| Unknown Host Exception | 404 (Not Found) |
| Unsupported Operation | 404 (Not Found) |
| Connect Exception | 404 (Not Found) |
| Illegal Argument | 400 (Bad Request) |
| Everything else | 400 (Bad Request) |

Matching rules object

Matching rules
==============

The matching rules enrichment is an object of metadata that indicates which rule or rules matched the Tweets received. This is most commonly used with the PowerTrack stream.

Matching will be done via exact match on the terms contained in a rule, scanning the content of the activity with and without punctuation. Matching is not case sensitive. When the content is found to contain all terms defined in the rule, there will be a root-level a matching\_rules object indicating the rule(s) that led to the match.

PowerTrack
----------

Tweets delivered through PowerTrack (realtime, Replay, and Historical) will contain the matching\_rules object as follows:

      `"matching_rules": [{         "tag": null,         "id": 907728589029646336,         "id_str": "907728589029646336"     }]`
    

  
In PowerTrack, the matching\_rules object reflects _all_ rules that matched the given result. In other words, if more than one rule matches a specific Tweet, it will only be delivered once, but the matching\_rules element will contain all the rules that matched.

Poll metadata

Poll metadata  

================

Poll metadata is a free enrichment available across all products (Realtime & Historical APIs) in enriched native format payloads. The metadata notes the presence of the poll in a Tweet, includes the list of poll choices, and includes both the poll duration and expiration time. This enrichment makes it easy to acknowledge the presence of a poll and enables proper rendering of a poll Tweet for display.

##### Important Details:

* Available across all enterprise APIs (PowerTrack, Replay, Search, Historical PowerTrack)
    * _Note:_ For Replay and Historical PowerTrack, this metadata was first made available on 02/22/17 - see documented [enrichment availability](https://developer.twitter.com/content/developer-twitter/en/docs/tweets/batch-historical/guides/hpt-timeline).
* Does not include vote information or poll results
* Does not currently have filter/operator support
* Available in **enriched native format** only
    * Enriched native format is a user-controlled setting that can be changed at any time through the Console: _Select a Product (PowerTrack, Replay, Search) > Settings tab > Output Format (Leave data in its original format)_

### Tweet Payload

Poll Tweets will contain the following metadata in the “entities.polls” object in the payload:

* An “options” array with up to four options that include the position (1-4) and option text
* Poll expiration date
* Poll duration

See the sample payload below for further reference.

### Sample Payload

Below is a snippet of the enriched native format payload highlighting the added poll metadata:

    "entities":{  
          "hashtags":[],
          "urls":[],
          "user_mentions":[],
          "symbols":[],
          "polls":[  
             {  
                "options":[  
                   {  
                      "position":1,
                      "text":"The better answer"
                   },
                   {  
                      "position":2,
                      "text":"The best answer"
                   }
                ],
                "end_datetime":"Sat Feb 04 15:33:11 +0000 2017",
                "duration_minutes":1440
             }
          ]
       },

* * *

Profile geo

Profile Geo
-----------

### Introduction

Many Twitter user profiles include public location information provided by the user. This data is returned as a normal string in user.location (see [User object data dictionary](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-object/user.html)). The Profile Geo Enrichment adds structured geodata relevant to the user.location value by geocoding and normalizing location strings where possible. Both latitude/longitude coordinates and related place metadata are added to user.derived.locations _only_ when included as part of the Tweet payload in enterprise API products. This data is available when using [the enriched native format](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/overview.html) and can be filtered with a combination of [PowerTrack rules](https://developer.twitter.com/en/docs/twitter-api/enterprise/rules-and-filtering/enterprise-operators).  

**Note:** Some of the supporting geodata used to create the Profile Geo enrichment comes from GeoNames.org and is used by Twitter under the [Creative Commons Attribution 3.0 License](https://creativecommons.org/licenses/by/3.0/us/legalcode).

Profile Geo data will be included in Twitter's PowerTrack, Replay, Volume Stream, Search, and Historical PowerTrack APIs.

### Profile Geo Data

| Enriched native field name | Example value | Description |
| --- | --- | --- |
| user.derived.locations.country | United States | The country location for where the user that created the Tweet is from. |
| user.derived.locations.country\_code | US  | A two-letter ISO-3166 country code that corresponds to the country location for where the user that created the Tweet is from. |
| user.derived.locations.locality | Birmingham | The locality location (generally city) for where the user that created the Tweet is from. |
| user.derived.locations.region | Alabama | The region location (generally state/province) for where the user that created the Tweet is from. |
| user.derived.locations.sub\_region | Jefferson County | The sub-region location (generally county) for where the user that created the Tweet is from. |
| user.derived.locations.full\_name | Birmingham, Alabama, United States | The full name (excluding sub-region) for where the user that created the Tweet is from. |
| User.derived.locations.geo | See Below | An array that includes a lat/long value for a coordinate that corresponds to the lowers granularity location for where the user that created the Tweet is from. |

The Historical PowerTrack, Search, and PowerTrack APIs supports filtering based on Profile Geo data. See the appropriate product documentation for more details on what operators are available for filtering on Profile Geo data.

### Sample Payload

{
    "user": {
        "derived": {
            "locations": \[
                {
                    "country": "United States",
                    "country\_code": "US",
                    "locality": "Birmingham",
                    "region": "Alabama",
                    "sub\_region": "Jefferson County",
                    "full\_name": "Birmingham, Alabama, United States",
                    "geo": {
                        "coordinates": \[
                            -86.80249,
                            33.52066
                        \],
                        "type": "point"
                    }
                }
            \]
        }
    }
}

### Limitations

* The Profile Geo enrichment attempts to determine the best choice for the geographic place described in the profile location string. The result may not be accurate in all cases due to factors such as multiple places with similar names or ambiguous names.
* If a value is not provided in a user’s profile location field (actor.location), we will not attempt to make a classification.
* Precision Level: If a Profile Geo Enrichment can only be determined with confidence at the country or region level, lower-level geographies such as subRegion and locality will be omitted from the payload.
* The Profile Geo enrichment provides lat/long coordinates (a single point) that corresponds to the Precision Level of the enrichment’s results. These coordinates represent the geographic center of the enrichment location results. For example, if the Precision Level is at the Country level, then those coordinates are set to the geographic center of that Country.
* The PowerTrack operators provided for address properties (locality/region/country/country code) are intentionally granular to allow for many rule combinations. When attempting to target a specific location that shares a name with another location, consider combining address rules. For instance, the following would avoid matches for “San Francisco, Philippines”: profile\_locality:”San Francisco” profile\_region:California When building rules that target individual Profile Geo fields, keep in mind that each increased level of granularity will limit the results you see. In some cases when attempting to look at data from a city, you may wish to only rely on a region rule where the region offers significant overlap with the city, e.g. the city of Zurich, Switzerland can be effectively targeted along with surrounding areas with profile\_region:”Zurich”.
* Use with Native Geo Tweets: The Profile Geo enrichment provides an alternative type of geography for a Tweet, different from the native geo value in the payload. These two types of geography can be combined together to capture all of the possible tweets related to a given area (based on available geodata), though they are not conceptually equivalent.

Building an enterprise rule

Getting started with enterprise rules and queries
-------------------------------------------------

Products utilizing enterprise operators deliver social data to you based on filtering rules you set up. Rules are made up of one or more ‘clauses’, where a clause is a keyword, exact phrase, or one of the many enterprise operators. Before beginning to build rules with enterprise operators, be sure to review the syntax described below, look through the list of available operators, and understand the restrictions around building rules. You should also be sure to understand the nuances of how rules are evaluated logically, in the "[Order of operations](#orderofoperations)" section.

Multiple clauses can be combined with both "and" and "or" logic.

**Please note:** "And" logic is specified with a space between clauses, while or logic is specified with an upper-case `OR`. 

Each rule can be up to 2,048 characters long with no limits on the number of positive clauses (things you want to match or filter on) and negative clauses (things you want to exclude and not match on).  
 

### Building rules and queries 

**Keyword match**

Keyword matches are similar to queries in a search interface. For example, the following enterprise operator rule would match activities with the term "social" in the text body.

`social`

**ANDing terms with white space**

Adding another keyword is the same as adding another requirement for finding matches. For example, this rule would only match activities where both "social" and "media" were present in the text, in either order – _having a space between terms operates as boolean AND logic_. If you include an explicit AND in your rule, it will rejected by the rules endpoint.

`social media`

**ORing terms with upper-case OR**

Many situations actually call for boolean OR logic, however. This is easily accomplished as well. _Note that the OR operator must be upper-case and a lower-case ‘or’ will be treated as a regular keyword._

`social OR data`

**Negating terms**

Still other scenarios might call for excluding results with certain keywords (a boolean NOT logic). For instance, activities with ‘happy’, but excluding any with ‘birthday’ in the text.

`social -personality`

**Grouping with parentheses**

These types of logic can be combined using grouping with parentheses, and expanded to much more complex queries.

`(social OR data) (academic OR research) -personality -information -university`

This is just the beginning though – while the above examples rely simply on tokenized matching for keywords, enterprise products also offer operators to perform different types of matching on the text.

**Exact match**

`"social media research"`

**Substring match**

`contains:info`

**Proximity match**

`"social media research"~3`

  
Further, other operators allow you to filter on unique aspects of social data, besides just the text. 

**The user who is posting a Tweet**

`from:twitterdev`

**Geo-tagged Tweets within 10 miles of Pearl St. in Boulder, CO, United States**

`point_radius:[-105.27346517 40.01924738 10.0mi]`

**Putting it all together**

These can be combined with text filters using the same types of logic described above.

`(social OR data) (academic OR research OR "social media research") point_radius:[-105.27346517 40.01924738 10.0mi] lang:en -personality -information -university`

###   
Boolean Syntax

The examples in the previous section, utilized various types of boolean logic and grouping. See the table below for additional detail regarding the syntax and requirements for each.

|     |     |     |
| --- | --- | --- |
| **Logic type** | **Operator syntax** | Description |
| AND | social data | Whitespace between two operators results in AND logic between them  <br>  <br>Matches activities containing both keywords ("social", "data").  <br>  <br>**Do not use AND explicitly in your rule. Only use whitespace. An explicit AND will be treated like a regular keyword.** |
| OR  | social OR data | To OR together two operators, insert an all-caps OR, enclosed in whitespace between them  <br>  <br>Matches activities with EITHER keyword ("social" OR "data")  <br>  <br>Note that if you combine OR and AND functionality in a single rule, you should understand the order of operations described in our "[Order of operations](#OrderOfOperations)" section, and consider grouping non-negated operators together using parentheses as described below to ensure your rule behaves as expected.  <br>  <br>You must use upper-case "OR" in your rule. Lower-case 'or' will be treated as a regular keyword. |
| NOT | social data  <br>\-apple -android -phone | Insert a `-` character immediately in front of the operator or group of operators.  <br>  <br>The example rule shown matches activities containing keyword "social", but excludes those which contain the keyword "data."  <br>  <br>Negated ORs are not allowed where the rule would request "everything in the firehose except the negation." For example, `apple OR -ipad` is invalid because it would match all activities except those mentioning "ipad". |
| Grouping | (social OR data) -twitterdev -twitterapi | Parentheses around multiple operators create a functional "group".<br><br>Groups can be connected to clauses in the same manner as an individual clause via whitespace (AND) or ORs. However, note that it is a best practice to not group together negations by applying the negating \- to the entire group. Instead, you should negate each individual operator, stringing them together via whitespace (AND). <br><br>For example, instead of using \-(iphone OR imac OR macbook), use the following: \-iphone -imac -macbook  <br>  <br>Grouping is especially important where a single rule combines AND and OR functionality, due to the order of operations used to evaluate the rule. See below for more details. |

**Please note:** that operators may be either positive or negative.

**Positive Operators** define what you want to **include** in the results. E.g. the `has:hashtags` operator says “I want activities containing hashtags.”

**Negative Operators** define what you want to **exclude** from the results, and are created by using the Boolean NOT logic described above. For example, `-has:hashtags` says “Exclude any activities containing hashtagss, even if they otherwise match my rule.”

Premum operator products have no restriction on the number of positive and negative clauses, subject to a maximum length of 2,048 characters.  
 

#### Order of Operations

When combining AND and OR functionality in a single rule, the following order of operations will dictate how your rule is evaluated.

1. Operators connected by AND logic are combined first
2. Then, operators connected with OR logic are applied

**Example:**

* `apple OR iphone ipad` would be evaluated as `apple OR (iphone ipad)`
* `ipad iphone OR android` would be evaluated as `(iphone ipad) OR android`

To eliminate uncertainty and ensure that your rules are evaluated as intended, group terms together with parentheses where appropriate. For example:

* `(apple OR iphone) ipad`
* `iphone (ipad OR android)`

####   
Punctuation, Diacritics, and Case Sensitivity

If you specify a keyword or hashtag rule with character accents or diacritics for enterprise operators, it will match Tweet text honoring the diacritics (hashtags or keywords). Rule with a keyword `Diacr**í**tica` or hashtag `#cumplea**ñ**os` will match "Diacr**í**tica" or "#cumplea**ñ**os" but not "Diacritica" or "#cumpleanos" without the tilde **í** or **eñe**.

Characters with accents or diacritics are treated the same as normal characters and are not treated as word boundaries. For example, a rule of cumplea**ñ**os would only match activities containing the word cumpleaños and would not match activities containing cumplea, cumplean, or os.

All operators are evaluated in a case-insensitive manner. For example, the rule `Cat` will match all of the following: "cat", "CAT", "Cat".

####   
PowerTrack rule tags

As described on our "[Matching rules](https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/matching-rules)" page, each rule may be created with a tag. These tags have no effect on filtering, but can be used to create logical groupings of rules within your app. Each rule may have only one tag, with a maximum of 255 characters. Tags are included with the JSON formatted rule at the time of creation via the API, as described on our "Matching rules" page.

####   
Putting Rules in JSON Format

In order to add or delete a rule from a stream via the API, the rules must utilize JSON format. Essentially, this requires putting each rule into the following structure:

`{"value":"insert_rule_here"}`

**Rules with double-quotes**

If the rule contains double-quote characters (`“`) associated with exact-match or other operators, they must be escaped using a backslash to distinguish them from the structure of the JSON format.

`"social data" @twitterdev`

The JSON formatted rule would be:

`{"value":"\"social data\" @twitterdev"}`

**Rules with double-quote string literals**

To include a double-quote character as a string literal within an exact-match, it must be double-escaped. For example, for a rule matching on the exact phrase "Toys “R” Us", including the double-quotes around "R", the plain-text representation of this would look like the following:

`"Toys \"R\" Us"`

Translating this to JSON format, you should use the following structure:

`{"value":"\"Toys \\\"R\\\" Us\""}`

**Rules with Tags**

To include an optional tag with your rule, as described above, simply include an additional `tag` field with the rule value.

`{"value":"\"social data\" @twitterdev","tag":"RULE-TAG-01"}`

**Formatting for API Requests**

When adding or deleting rules from the stream via the API, multiple JSON formatted rules should be comma delimited, and wrapped in a JSON “rules” array, as shown below:

`{"rules":[{"value":"from:twitterdev"},{"value":"\social data\" @twitterdev","tag":"RULE-TAG-01"}]}`

####   
Operators that match Quote Tweets

When using the [PowerTrack API](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api) and [Historical PowerTrack API](https://developer.twitter.com/en/docs/twitter-api/enterprise/historical-powertrack-api), the operators below will match on content from both the original Tweet that was quoted and the new Quote Tweet.

However, if you are using the [Search API](https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api), these operators will only match the contents of the Quote Tweet, and will not match on any content from the original Tweet that was quoted.

* `Keywords`
* `Phrases`
* `Proximity`
* `#hashtags`
* `@mentions`
* `$cashtags`
* `url:`
* `url_contains:`
* `has:links`
* `has:mentions`
* `has:hashtags`
* `has:media`
* `has:symbols`
* `is:quote`
* `is:reply`

Enterprise operators

Enterprise operators
--------------------

Below are the operators available with PowerTrack and Historical PowerTrack. A subset of these are available with the 30-Day and Full-Archive search APIs. See [this table](https://developer.twitter.com/en/docs/twitter-api/enterprise/rules-and-filtering/operators-by-product) for a product-by-product list of available operators. 

**Operator**  

Descriptionkeyword  

Matches a keyword within the text body or URL of a Tweet. Keywords must start with either a digit (0-9) or any non-puncutation character.  Keyword matching is a tokenized match, meaning that your keyword will be matched against the tokenized text of the Tweet body – tokenization is based on punctuation, symbol, and separator Unicode basic plane characters.  To match strings containing punctuation (for example, coca-cola), symbol, or separator characters, you must use a quoted "exact phrase match".  
  
Example:  
(social OR pizza OR wildfire) -planet  
  
**Note:** With the Search API, accented and special characters are normalized to standard latin characters, which can change meanings in foreign languages or return unexpected results:  
For example, "músic" will match “music” and vice versa.   
For example, common phrases like "Feliz Año Nuevo!" in Spanish, would be indexed as "Feliz Ano Nuevo", which changes the meaning of the phrase.

**Note:** This operator will match on both URLs and unwound URLs within a Tweet.  

emoji  
Matches an emoji within the body of a Tweet. Emojis are a tokenized match, meaning that your emoji will be matched against the tokenized text of the Tweet body – tokenization is based on punctuation, symbol/emoji, and separator Unicode basic plane characters. For example, a Tweet with the text “I like 🍕” would be split into the following tokens: I, like, 🍕. These tokens would then be compared to the emoji used in your rule. Note that if an emoji has a variant, you must use “quotations” to add to a rule.  
  
Example:  
(🍕 OR 💜 OR 🐢) -🤖  
"exact phrase match"  

Matches an exact phrase within the body of a Tweet.

Example:  
("social media" OR "developer.twitter.com" OR "wildfire911" OR "coca-cola") -"planet earth"

**Note:** In 30 Day Search and Full Archive Search, punctuation is not tokenized and is instead treated as whitespace.   
For example, quoted “#hashtag” will match “hashtag” but not #hashtag (use the hashtag # operator without quotes to match on actual hashtags)  
For example, quoted “$cashtag” will match “cashtag” but not $cashtag (use the cashtag $ operator without quotes to match on actual cashtags)

**Note:** This operator will match on both URLs and unwound URLs within a Tweet.

#  

Matches any Tweet with the given hashtag.

This operator performs an exact match, NOT a tokenized match, meaning the rule “2016” will match posts with the exact hashtag “2016”, but not those with the hashtag “2016election”

Example:  
(#social OR #pizza OR #2016election) -#planet

**Note**: that the hashtag operator relies on Twitter’s entity extraction to match hashtags, rather than extracting the hashtag from the body itself. See [HERE](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/entities) for more information on Twitter Entities JSON attributes.

@  

Matches any Tweet that mentions the given username.

The to: operator returns a subset match of the @mention operator.

Example:  
(@twitterdev OR @twitterapi OR @twittereng) -@jack

**Note**: that the mention operator relies on Twitter’s entity extraction to match mentioned users, rather than extracting the mention from the body itself. See [HERE](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/entities) for more information on Twitter Entities JSON attributes.  

"keyword1 keyword2"~N  

Commonly referred to as a proximity operator, this matches a Tweet where the keywords are no more than N tokens from each other.

If the keywords are in the opposite order, they can not be more than N-2 tokens from each other.

Can have any number of keywords in quotes.

N cannot be greater than 6.

Example:  
"social media"~5 OR "twitter API"~3 

  
**Note**: Only available with PowerTrack and Historical PowerTrack.

contains:

Substring match for Tweets that have the given substring in the body, regardless of tokenization. In other words, this does a pure substring match, and does not consider word boundaries.

Use double quotes to match substrings that contain whitespace or punctuation.

Example:  
(contains:social OR contains:"wikipedia.com") -contains:"buy now"

**Note**: Only available with PowerTrack and Historical PowerTrack.

from:  

Matches any Tweet from a specific user.

Example:  
(from:2244994945 OR from:twitterapi OR from:twittereng) -from:jack

The value must be the user’s Twitter numeric Account ID or username (excluding the @ character). See [HERE](https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-lookup) for looking up numeric Twitter Account IDs.

to:  

Matches any Tweet that is in reply to a particular user.

Example:  
(to:2244994945 OR to:twitterapi OR to:twittereng) -to:jack

The value must be the user’s numeric Account ID or username (excluding the @ character). See [HERE](https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-lookup)  for looking up numeric Twitter Account IDs.  

url:  
Performs a tokenized (keyword/phrase) match on the expanded URLs of a Tweet (similar to url\_contains).  
  
Example:  
@twitterdev url:"developer.twitter.com"  
  
**Note:** When using PowerTrack or Historical PowerTrack, this operator will match on URLs contained within the original Tweet of a Quote Tweet. For example, if your rule includes url:"developer.twitter.com", and a Tweet contains that URL, any Quote Tweets of that Tweet will be included in the results. This is not the case when using the Search API.   
url\_title:  

_Available alias_: within\_url\_title: 

Performs a keyword/phrase match on the (new) expanded URL HTML title metadata. See [HERE](https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/expanded-and-enhanced-urls) for more information on expanded URL enrichment.  
  
**Note**: Only available with PowerTrack and Historical PowerTrack.

url\_description:  

_Available alias_: within\_url\_description: 

Performs a keyword/phrase match on the (new) expanded page description metadata. See [HERE](https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/expanded-and-enhanced-urls) for more information on expanded URL enrichment.  
  
  
**Note:** Only available with PowerTrack and Historical PowerTrack.

url\_contains:  

Matches Tweets with URLs that literally contain the given phrase or keyword. To search for patterns with punctuation in them (for example, google.com) enclose the search term in quotes.

Example:  
(url\_contains:"developer.twitter.com" OR url\_contains:wildfire) -url\_contains:reddit

**Note**: If you’re using the [Expanded URL](https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/expanded-and-enhanced-urls) output format, we will match against the expanded URL as well.

bio:  

_Available alias_: user\_bio:

Matches a keyword or phrase within the user bio of a Tweet. This is a tokenized match within the contents of the 'description' field within the [User object](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/user).  
  
Example:  
(bio:engineer OR bio:"wordpress.com" OR bio:🚀) -bio:troll  
  
  
**Note:** Only available with PowerTrack and Historical PowerTrack.

bio\_name:  
Matches a keyword within the user bio name of a Tweet. This is a tokenized match within the contents of a user’s “name” field within the [User object](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/user).  
  
**Note:** Only available with PowerTrack and Historical PowerTrack.bio\_location:  

_Available alias_: user\_bio\_location:

Matches tweets where the User object's location contains the specified keyword or phrase. This operator performs a tokenized match, similar to the normal keyword rules on the message body.

This location is part of the [User object](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/user), and is the account's 'home' lcoation, is a non-normalized, user-generated, free-form string, and is different from a Tweet's location (when available). 

**Note:** Only available with PowerTrack and Historical PowerTrack.

statuses\_count:  

_Available alias_: tweets\_count:

Matches Tweets when the author has posted a number of statuses that falls within the given range.

If a single number is specified, any number equal to or higher will match.

Additionally, a range can be specified to match any number in the given range  (for example, statuses\_count:1000..10000).  

Example:  
to:twitterapi statuses\_count:10

@twitterdev statuses\_count:1..10

**Note:** Only available with PowerTrack and Historical PowerTrack.

followers\_count:  

Matches Tweets when the author has a followers count within the given range.

If a single number is specified, any number equal to or higher will match.

Additionally, a range can be specified to match any number in the given range (for example, followers\_count:1000..10000).'

**Note:** Only available with PowerTrack and Historical PowerTrack.

friends\_count:  

_Available alias_: following\_count: 

Matches Tweets when the author has a friends count (the number of users they follow) that falls within the given range.

If a single number is specified, any number equal to or higher will match.

Additionally, a range can be specified to match any number in the given range (for example, friends\_count:1000..10000).

**Note:** Only available with PowerTrack and Historical PowerTrack.

listed\_count:  

_Available alias_: user\_in\_lists\_count:

Matches Tweets when the author has been listed within Twitter a number of times falls within the given range.

If a single number is specified, any number equal to or higher will match.

Additionally, a range can be specified to match any number in the given range (for example, listed\_count:10..100).

**Note:** Only available with PowerTrack and Historical PowerTrack.  

$

Matches any Tweet that contains the specified ‘cashtag’ entity.

Example:  
($TWTR OR $TSLA OR $BRK.A) -$F

**Note**: The cashtag operator relies on Twitter’s ‘symbols’ entity extraction to match cashtags, rather than trying to extract the cashtag from the body itself. See [HERE](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/entities) for more information on Twitter Entities JSON attributes.

retweets\_of:  

_Available alias_: retweets\_of\_user:

Matches Tweets that are Retweets of a specified user. Accepts both usernames and numeric Twitter Account IDs (NOT Tweet status IDs).  
  
Example:  
(retweets\_of:2244994945 OR retweets\_of:twitterapi OR retweets\_of:twittereng) -retweets\_of:jack  
  
See [HERE](https://dev.twitter.com/rest/reference/get/users/lookup) for looking up numeric Twitter Account IDs.  

retweets\_of\_status\_id:  

_Available alias_: retweets\_of\_tweet\_id:

Deliver only explicit Retweets of the specified Tweet. Note that the status ID used should be the ID of an original Tweet and not a Retweet.   
  
Example:  
retweets\_of\_status\_id:1293593516040269825  
  
**Note:** Only available with PowerTrack and Historical PowerTrack.

in\_reply\_to\_status\_id:  

_Available alias_: in\_reply\_to\_tweet\_id:

Deliver only explicit replies to the specified Tweet.  
  
Example:  
in\_reply\_to\_status\_id:1293593516040269825  
  
**Note:** Only available with PowerTrack and Historical PowerTrack.

sample:

Returns a random sample of Tweets that match a rule rather than the entire set of Tweets. Sample percent must be represented by an integer value between 1 and 100. This operator applies to the entire rule and requires any “OR’d” terms be grouped.

**Important Note:** The sample operator first reduces the scope of the firehose to X%, then the rule/filter is applied tio that sampled subset. If you are using, for example, **sample:10**, each Tweet has a 10% chance of being in the sample. 

The sampling is deterministic, and you will get the same data sample in realtime as you would if you pulled the data historically.

Example:  
#happybirthday sample:5  
"happy birthday"~5 sample:80

**Note:** Only available with PowerTrack and Historical PowerTrack.

source:Matches any Tweet generated by the given source application. The value must be either the name of the application, or the application’s URL.  **Cannot be used alone.  
**  
Example:  
#happybirthday source:"Twitter for iPhone"  
"This is a test Tweet from my TestingApp" source:MyTestAppName  
  
**Note**: As a Twitter app developer, Tweets created programattically by your application will have the source of your application Name and Website URL set in your [app settings](https://developer.twitter.com/en/docs/apps/app-management.html). The source operator seraches on the Tweet source attribute.  See [HERE](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/entities) for more information on Twitter Entities JSON attributes.  
lang:  

Matches Tweets that have been classified by Twitter as being of a particular language (if, and only if, the tweet has been classified). It is important to note that each Tweet is currently only classified as being of one language, so AND’ing together multiple languages will yield no results. This operator is not recommended to be used alone, matching volume will be very high. 

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

Example:  

(@twitterdev OR to:twitterdev) lang:es  

**Note:** The language operator matches on the specific Tweet language determined by Twitter and set as the lang Tweet attribute.  See [HERE](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/entities) for more information on Twitter Entities JSON attributes.  If no language classification can be made for a Tweet, the Tweet lang will be set as ‘und’ (for undefined).

place:  

Matches Tweets tagged with the specified location _or_ Twitter place ID (see examples). Multi-word place names (“New York City”, “Palo Alto”) should be enclosed in quotes.

Example:  
(place:London OR place:"Great Britain") -place:USA  
place:fd70c22040963ac7

**Note:** See the [GET geo/search](https://developer.twitter.com/en/docs/geo/places-near-location/api-reference/get-geo-search) public API endpoint for how to obtain Twitter place IDs.

**Note:** This operator will not match on Retweets, since Retweet's places are attached to the original Tweet. It will also not match on places attached to the original Tweet of a Quote Tweet.

place\_country:  

Matches Tweets where the country code associated with a tagged [place/location](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/geo) matches the given ISO alpha-2 character code.

Example:  
place\_country:GB OR place\_country:AU OR place\_country:CA  

Valid ISO codes can be found here: [http://en.wikipedia.org/wiki/ISO\_3166-1\_alpha-2](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

**Note:** This operator will not match on Retweets, since Retweet's places are attached to the original Tweet. It will also not match on places attached to the original Tweet of a Quote Tweet.

point\_radius:\[lon lat radius\]  

Matches against the Exact Location (x,y) of the Tweet when present, and in Twitter, against a “Place” geo polygon, where the Place is fully contained within the defined region.

* Radius must be less than 25mi.
* Units of radius supported are miles (mi) and kilometers (km).
* Longitude is in the range of ±180
* Latitude is in the range of ±90
* All coordinates are in decimal degrees.
* Rule arguments are contained with brackets, space delimited.

Example:  
point\_radius:\[-105.27346517 40.01924738 0.5mi\]

point\_radius:\[2.355128 48.861118 16km\]

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

Example:  
bounding\_box:\[-105.301758 39.964069 -105.178505 40.09455\]

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

profile\_subregion:  

Matches on the “subRegion” field from the “address” object in the [Profile Geo](https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/profile-geo) enrichment. In addition to targeting specific counties, these operators can be helpful to filter on a metro area without defining filters for every city and town within the region.

This is an exact full string match. It is not necessary to escape characters with a backslash. For example, if matching something with a slash, use “one/two”, not “one\\/two”. Use double quotes to match substrings that contain whitespace or punctuation.

has:geo  

Matches Tweets that have Tweet-specific geo location data provided from Twitter. This can be either “geo” lat-long coordinate, or a “location” in the form of a Twitter [“Place”](https://dev.twitter.com/overview/api/places), with corresponding display name, geo polygon, and other fields.

**Note**: When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. You can include this as a standalone operator when using PowerTrack and Historical PowerTrack.

has:profile\_geo  

_Available alias_: has:derived\_user\_geo

Matches Tweets that have any [Profile Geo](https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/profile-geo) metadata, regardless of the actual value.  
  

**Note**: When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. You can include this as a standalone operator when using PowerTrack and Historical PowerTrack.

has:links

This operator matches Tweets that contain a link or referenced media in the "text" object of the payload.  

**Note:** In addition to this operator matching Tweets with a link in their text, it also matches Tweets with media (image, video, gif), and Quote Tweets.

**Note:** When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. You can include this as a standalone operator when using PowerTrack and Historical PowerTrack.

is:retweet  

Deliver only explicit retweets that match a rule. Can also be negated to exclude retweets that match a rule from delivery and only original content is delivered.

This operator looks only for true Retweets. Quoted Tweets which do not use Twitter’s Retweet functionality will not be matched by this operator.

**Note:** When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. You can include this as a standalone operator when using PowerTrack and Historical PowerTrack.

is:reply  
Delivers only explicit replies that match a rule. Can also be negated to exclude replies that match a rule from delivery (see example request below).  
  
When used with PowerTrack, this operator matches on replies to an original Tweet, replies in quoted Tweets and replies in Retweets. When used with the Search API, this operator only matches on replies to an original Tweet and excludes replies in quoted Tweets and replies in Retweets.  
  
Example:  
#contest123 is:reply  
@twitterdev -is:reply  
  

**Note**: When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. You can include this as a standalone operator when using PowerTrack and Historical PowerTrack.

is:quote

Delivers only Quote Tweets, or Tweets that reference another Tweet, as identified by the "is\_quote\_status":true in Tweet payloads. Can also be negated to exclude Quote Tweets. 

Example:  
@twitterdev is:quote  
  

**Note:** When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. You can include this as a standalone operator when using PowerTrack and Historical PowerTrack.

is:verified  
Deliver only Tweets where the author is “verified” by Twitter. Can also be negated to exclude Tweets where the author is verified.  
  
Example:  
@twitterdev is:verified  
  

**Note:** When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. You can include this as a standalone operator when using PowerTrack and Historical PowerTrack.

has:mentions  
Matches Tweets that mention another Twitter user.  
  

**Note:** When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. You can include this as a standalone operator when using PowerTrack and Historical PowerTrack.

has:hashtags  
Matches Tweets that contain a hashtag.  
  

**Note:** When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. You can include this as a standalone operator when using PowerTrack and Historical PowerTrack.

has:media  

_Available alias_: has:media\_link

Matches Tweets that contain a media url classified by Twitter. For example, pic.twitter.com.  
  

**Note:** When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. You can include this as a standalone operator when using PowerTrack and Historical PowerTrack.

has:images  
Matches Tweets that contain a media url classified by Twitter. For example, pic.twitter.com.  
  

**Note:** When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. You can include this as a standalone operator when using PowerTrack and Historical PowerTrack.

has:videos  

_Available alias_: has:video\_link

Matches Tweets that contain native Twitter videos, uploaded directly to Twitter. This will not match on videos created with YouTube, Periscope, or Tweets with links to other video hosting sites.  
  

**Note:** When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. You can include this as a standalone operator when using PowerTrack and Historical PowerTrack.

has:symbols  

Matches Tweets that contain a cashtag symbol (with a leading ‘$’ character. For example, $tag).

**Note:** When using the Search API, this operator must be used in conjunction with other operators that don't include `is:` or `has:`. You can include this as a standalone operator when using PowerTrack and Historical PowerTrack.

Operators by product

All enterprise operators are available with PowerTrack and Historical PowerTrack APIs. However, only a subset of operators are available to the enterprise Search APIs, as noted on this page.

The dark blue tags note which operators are available to different enterprise products:

PowerTrack Search

We've also noted which operators are also available to the premium Search APIs. The darker blue represents paid premium tiers, while the lighter represents the free Sandbox tier:

 Premium Sandbox  
 

| Operator | Product | Description | Matches on payload element |
| --- | --- | --- | --- |
| "exact phrase match" | PowerTrack<br><br>Search<br><br>Premium<br><br>Sandbox | Matches an exact phrase within the body of a Tweet.<br><br>Components that can translate into a search operators will be treated as words. In other words:<br><br>* `"#hashtag"` will match `hashtag` but not `#hashtag` (use the [hashtag operator](#hashtag-operator) without quotes to match on actual hashtags) <br>* `"$TWTR"` will match the word `TWTR` but not the cashtag `$TWTR` (use the [cashtag operator](#cashtag-operator) without quotes to match on actual cashtags)<br><br>**Note:** in 30 Day Search and Full Archive Search (Enterprise and Premium), punctuation is not tokenized and is instead treated as whitespace. | `text` |
| @   | PowerTrack<br><br>Search<br><br>Premium<br><br>Sandbox | Matches any Tweet that mentions the given username. The value can be either the username (excluding the `@` character) or the user’s numeric ID or (obtained for example via the [GET users/lookup](https://developer.twitter.com/content/developer-twitter/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-lookup) endpoint). | `entities.user_mentions` |
| #   | PowerTrack<br><br>Search<br><br>Premium<br><br>Sandbox | Matches any Tweet with the given hashtag.<br><br>This operator performs an exact match. For example meaning the rule `#1989` will match Tweets containing the exact hashtag `#1989`, but not those with the hashtag `#TaylorSwift1989`.<br><br>**Note:** this operator relies on Twitter’s entity extraction to match hashtags, rather than extracting the hashtag from the body itself. For more details on JSON attributes from entities, refer to [Twitter Entities](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/entities). | `entities.hashtags` |
| $   | PowerTrack<br><br>Search | Matches any Tweet that contains the specified cashtag (where the leading character of the token is `$`).<br><br>**Note:** this operator relies on Twitter’s entity extraction to match links, rather than extracting the link from the body itself. For more details on JSON attributes from entities, refer to [Twitter Entities](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/entities). | `entities.symbols` |
| bio: | PowerTrack | _Available alias_: user\_bio:<br><br>Matches a keyword (using tokenized match) or a phrase within the user bio of a Tweet. Use double quotes to match a phrase. In other words:<br><br>* `bio:software engineer` will match Tweets with the keyword `engineer` from users with the word `software` in their bio<br>* `bio:"software engineer"` will match any Tweet posted by users with the phrase `software engineer` in their bio | `user``.description` |
| bio\_location: | PowerTrack | _Available alias_: user\_bio\_location:<br><br>Matches Tweets where the [User object](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/user)'s location contains the specified keyword (using tokenized match) or phrase.<br><br>This location is a non-normalized, user-generated, free-form string, and is different from a Tweet's location (when available). | `user.location` |
| bio\_name: | PowerTrack | Matches Tweets where the [User object](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/entities/user)'s name contains the specified keyword (using tokenized match) or phrase. | `user.name` |
| bounding\_box: | PowerTrack<br><br>Search<br><br>Premium<br><br>Sandbox | _Available alias_: geo\_bounding\_box:<br><br>Matches against the exact location (long, lat) of the Tweet (when present), and against a geo polygon (where the Place is fully contained within the defined region).<br><br>* west\_long south\_lat represent the southwest corner of the bounding box where west-long is the longitude of that point, and south\_lat is the latitude.<br>* east\_long and north\_lat represent the northeast corner of the bounding box, where east\_long is the longitude of that point, and north\_lat is the latitude.<br>* Width and height of the bounding box must be less than 25mi<br>* Longitude is in the range of ±180<br>* Latitude is in the range of ±90<br>* All coordinates are in decimal degrees.<br>* Rule arguments are contained within brackets, space delimited.<br><br>**Note:** operators matching on place (Tweet geo) will only include matches from original Tweets. Retweets do not contain any place data. | `place` (original Tweets only) |
| contains: | PowerTrack | Substring match for Tweets that have the given substring in the body, regardless of tokenization. In other words, this does a pure substring match and does not consider word boundaries.<br><br>Use double quotes to match substrings that contain whitespace or punctuation. | `text` |
| <emoji> | PowerTrack<br><br>Search<br><br>Premium<br><br>Sandbox | Matches an emoji within the body of a Tweet.<br><br>This is a tokenized match, so your emoji will be matched against the tokenized text of the Tweet body. Tokenization is based on punctuation, symbol/emoji, and separator Unicode basic plane characters. For example, a Tweet with the text “I like 🍕” would be split into the following tokens: I, like, 🍕. These tokens would then be compared to the emoji used in your rule.<br><br>**Note:** if an emoji has a variant, you must use double quotes to add to a rule. | `text` |
| followers\_count: | PowerTrack | Matches Tweets when the author has a followers count within the given range.<br><br>* A single number (e.g. `followers_count:42`) will match any number equal to or greater than the value specified.<br>* A range (e.g. `followers_count:42..1337`) will match any number in the given range. | `user.followers_count` |
| friends\_count: | PowerTrack | _Available alias_: following\_count:<br><br>Matches Tweets when the author has a friends count (the number of users they follow) that falls within the given range.<br><br>* A single number (e.g. `followers_count:42`) will match any number equal to or greater than the value specified.<br>* A range (e.g. `followers_count:42..1337`) will match any number in the given range. | `user.friends_count` |
| from: | PowerTrack<br><br>Search<br><br>Premium<br><br>Sandbox | Matches any Tweet from a specific user. The value can be either the username (excluding the `@` character) or the user’s numeric ID or (obtained for example via the [GET users/lookup](https://developer.twitter.com/content/developer-twitter/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-lookup) endpoint). | `user.id`, `user.id_str` (if using User ID)<br><br>`user.screen_name` (if using username) |
| has:geo | PowerTrack<br><br>Search<br><br>Premium | Matches Tweets that have Tweet-specific geolocation data provided from Twitter. This can be either “geo” lat-long coordinate, or a “location” in the form of a Twitter [Place](https://dev.twitter.com/overview/api/places), with the corresponding display name, geo polygon, and other fields.<br><br>Cannot be used as a standalone operator.<br><br>**Note:** operators matching on place (Tweet geo) will only include matches from original tweets. Retweets do not contain any place data. | `place` (original Tweets only) |
| has:hashtags | PowerTrack<br><br>Search<br><br>Premium | Matches Tweets that contain at least one hashtag.<br><br>Cannot be used as a standalone operator. | `entities.hashtags` |
| has:images | PowerTrack<br><br>Search<br><br>Premium<br><br>Sandbox | Matches Tweets that contain at least one classified image URL.<br><br>Cannot be used as a standalone operator. | `entities.media` |
| has:lang | PowerTrack | Matches Tweets that have been classified by Twitter as being of a particular language.<br><br>If a Tweet has not been classified, the operator will not match. Each Tweet is currently only classified as being of one language, so AND’ing together multiple languages will yield no results.<br><br>Cannot be used as a standalone operator. | `lang` when value is not `und` |
| has:links | PowerTrack<br><br>Search<br><br>Premium<br><br>Sandbox | This operator matches Tweets which contain links in the Tweet body.<br><br>Cannot be used as a standalone operator.<br><br>**Note:** this operator relies on Twitter’s entity extraction to match links, rather than extracting the link from the body itself. For more details on JSON attributes from entities, refer to [Twitter Entities](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/entities). | `entities.urls` |
| has:media | PowerTrack<br><br>Search<br><br>Premium<br><br>Sandbox | _Available alias_: has:media\_link<br><br>Matches Tweets that contain at least one classified media URL.<br><br>Cannot be used as a standalone operator. | `entities.media` |
| has:mentions | PowerTrack<br><br>Search<br><br>Premium<br><br>Sandbox | Matches Tweets that mention another Twitter user.<br><br>Cannot be used as a standalone operator. | `entities.user_mentions` |
| has:profile\_geo | PowerTrack<br><br>Search<br><br>Premium | _Available alias_: has:derived\_user\_geo<br><br>Matches Tweets that have any [Profile Geo](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/enrichments/overview/profile-geo) metadata, regardless of the actual value.<br><br>Cannot be used as a standalone operator. | `user.location` |
| has:symbols | PowerTrack<br><br>Enterprise | Matches Tweets that contain a cashtag symbol (e.g. `$TWTR`).<br><br>Cannot be used as a standalone operator. | `entities.symbols` |
| has:videos | PowerTrack<br><br>Search<br><br>Premium<br><br>Sandbox | _Available alias_: has:video\_link<br><br>Matches Tweets that contain at least one classified media URL.<br><br>Cannot be used as a standalone operator. | `entities.media` |
| in\_reply\_to\_status\_id: | PowerTrack | _Available alias_: in\_reply\_to\_tweet\_id:<br><br>Deliver only explicit replies to the specified Tweet. | `id`, `id_str` of the target Tweet |
| is:quote | PowerTrack | Deliver explicit Quote Tweets that match a rule.<br><br>It can also be negated (`-is:quote`) to exclude Quote Tweets that match a rule from delivery.<br><br>Cannot be used as a standalone operator. | `is_quote_status` (if `true`) |
| is:reply | PowerTrack<br><br>Search<br><br>Premium | Deliver only replies that match a rule.<br><br>It can also be negated (`-is:reply`) to exclude delivery of replies that match the specified rule.<br><br>With PowerTrack, this operator matches on:<br><br>* Replies to an original Tweet<br>* Replies in quoted Tweets<br>* Replies in Retweets<br><br>  <br>When used with the Search API, this operator matches on replies to an original Tweet, but excludes replies in quoted Tweets and replies in Retweets.<br><br>You can use this operators in conjunction with `is:retweet` and `is:quote` to only deliver replies to original Tweets.<br><br>Cannot be used as a standalone operator with the Search API.<br><br>**Note**: with Premium, this operator is not available in Sandbox dev environments. | Reply elements, e.g. `in_reply_to_status_id` |
| is:retweet | PowerTrack<br><br>Search<br><br>Premium | Deliver only explicit Retweets that match a rule.<br><br>It can also be negated (`-is:retweet`) to exclude Retweets that match a rule from delivery and only original content is delivered.<br><br>This operator looks only for true Retweets (i.e. Retweets posted using the Retweet button). Quoted Tweets and modified Tweets which do not use Twitter’s Retweet functionality will not be matched by this operator.<br><br>Cannot be used as a standalone operator. | Retweet elements, e.g. `retweeted_status` |
| is:verified | PowerTrack<br><br>Search<br><br>Premium | Deliver only Tweets where the author is verified by Twitter.<br><br>It can also be negated to exclude Tweets where the author is verified.<br><br>Cannot be used as a standalone operator. | `user.verified` |
| keyword | PowerTrack<br><br>Search<br><br>Premium<br><br>Sandbox | Matches a keyword within the body of a Tweet.<br><br>This is a tokenized match, meaning that your keyword string will be matched against the tokenized text of the Tweet body. Tokenization is based on punctuation, symbol/emoji, and separator Unicode basic plane characters. For example, a Tweet with the text “I like coca-cola” would be split into the following tokens: `I`, `like`, `coca`, `cola`. These tokens would then be compared to the keyword string used in your rule. To match strings containing punctuation (e.g. coca-cola), symbol, or separator characters, you must use an [exact phrase match](#exact-match) operator. | `text` |
| lang: | PowerTrack<br><br>Search<br><br>Premium<br><br>Sandbox | Matches Tweets that have been classified by Twitter as being of a particular language (if, and only if, the tweet has been classified). Each Tweet will be classified with only one language, so AND’ing together multiple languages will yield no results.<br><br>**Note:** if no language classification can be made the provided result is `und` (for undefined).<br><br>This operator will only match against supported languages. Providing any other value (including `und`) will result in the operator being ignored (in other words, Tweets will not be filtered by this operator). The list below represents the currently supported languages and their corresponding BCP 47 language identifier:<br><br>`am` Amharic<br><br>`hu` Hungarian<br><br>`pt` Portuguese<br><br>`ar` Arabic<br><br>`is` Icelandic<br><br>`ro` Romanian<br><br>`hy` Armenian<br><br>`in` Indonesian<br><br>`ru` Russian<br><br>`bn` Bengali<br><br>`it` Italian<br><br>`sr` Serbian<br><br>`bg` Bulgarian<br><br>`ja` Japanese<br><br>`sd` Sindhi<br><br>`my` Burmese<br><br>`kn` Kannada<br><br>`si` Sinhala<br><br>`zh` Chinese<br><br>`km` Khmer<br><br>`sk` Slovak<br><br>`cs` Czech<br><br>`ko` Korean<br><br>`sl` Slovenian<br><br>`da` Danish<br><br>`lo` Lao<br><br>`ckb` Sorani Kurdish<br><br>`nl` Dutch<br><br>`lv` Latvian<br><br>`es` Spanish<br><br>`en` English<br><br>`lt` Lithuanian<br><br>`sv` Swedish<br><br>`et` Estonian<br><br>`ml` Malayalam<br><br>`tl` Tagalog<br><br>`fi` Finnish<br><br>`dv` Maldivian<br><br>`ta` Tamil<br><br>`fr` French<br><br>`mr` Marathi<br><br>`te` Telugu<br><br>`ka` Georgian<br><br>`ne` Nepali<br><br>`th` Thai<br><br>`de` German<br><br>`no` Norwegian<br><br>`bo` Tibetan<br><br>`el` Greek<br><br>`or` Oriya<br><br>`tr` Turkish<br><br>`gu` Gujarati<br><br>`pa` Panjabi<br><br>`uk` Ukrainian<br><br>`ht` Haitian<br><br>`ps` Pashto<br><br>`ur` Urdu<br><br>`iw` Hebrew<br><br>`fa` Persian<br><br>`ug` Uyghur<br><br>`hi` Hindi<br><br>`pl` Polish<br><br>`vi` Vietnamese<br><br>`cy` Welsh | `lang` when value is not `und` |
| listed\_count: | PowerTrack | _Available alias_: user\_in\_lists\_count:<br><br>Matches Tweets when the author has been listed on Twitter a number of times falls within the given range.<br><br>* A single number (e.g. `listed_count:42`) will match any number equal to or greater than the value specified.<br>* A range (e.g. `listed_count:42..1337`) will match any number in the given range. | `user.listed_count` |
| place\_country: | PowerTrack<br><br>Search<br><br>Premium<br><br>Sandbox | Matches Tweets where the country code associated with a tagged [place/location](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/geo) matches the given [ISO alpha-2 character code](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).<br><br>**Note:** operators matching on place (Tweet geo) will only include matches from original tweets. Retweets do not contain any place data. | `place` (original Tweets only) |
| place: | PowerTrack<br><br>Search<br><br>Premium<br><br>Sandbox | Matches Tweets tagged with specified location or [Twitter place ID](https://developer.twitter.com/content/developer-twitter/en/docs/geo/places-near-location/api-reference/get-geo-search). Multi-word place names should be enclosed in quotes (e.g. `place:"San Francisco"`)<br><br>**Note:** operators matching on place (Tweet geo) will only include matches from original tweets. Retweets do not contain any place data. | `place` (original Tweets only) |
| point\_radius: | PowerTrack<br><br>Search<br><br>Premium<br><br>Sandbox | **Note:** operators matching on place (Tweet geo) will only include matches from original tweets. Retweets do not contain any place data. | `place` (original Tweets only) |
| profile\_bounding\_box:\[west\_long south\_lat east\_long north\_lat\] | PowerTrack | Matches against the user's exact Location (long, lat) in the [Profile Geo enrichment](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/enrichments/overview) where the Place is fully contained within the defined region.<br><br>* west\_long south\_lat represent the southwest corner of the bounding box where west-long is the longitude of that point, and south\_lat is the latitude.<br>* east\_long and north\_lat represent the northeast corner of the bounding box, where east\_long is the longitude of that point, and north\_lat is the latitude.<br>* Width and height of the bounding box must be less than 25mi<br>* Longitude is in the range of ±180<br>* Latitude is in the range of ±90<br>* All coordinates are in decimal degrees.<br>* Rule arguments are contained within brackets, space delimited.<br><br>**Note:** operators matching on place (Tweet geo) will only include matches from original tweets. Retweets do not contain any place data. | `user.derived.locations.geo.coordinates` |
| profile\_country: | PowerTrack<br><br>Search<br><br>Premium | Exact match on the country code from the [Profile Geo enrichment](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/enrichments/overview).<br><br>Uses a normalized set of two-letter country codes, based on [ISO-3166-1-alpha-2 specification](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).<br><br>To be concise, this operator is provided in lieu of an operator for the country field from the address object.<br><br>**Note:** operators matching on place (Tweet geo) will only include matches from original tweets. Retweets do not contain any place data. | `user.derived.locations.country_code` |
| profile\_locality: | PowerTrack<br><br>Search<br><br>Premium | Exact match on the Locality field from the [Profile Geo enrichment](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/enrichments/overview).<br><br>This is an exact full string match.<br><br>It is not necessary to escape characters with a backslash. For example, if matching something with a slash, use `one/two`.<br><br>Use double quotes to match substrings that contain whitespace or punctuation, e.g. `profile_locality:"Lower East Side"`. | `user.derived.locations.locality` |
| profile\_point\_radius:\[lon lat radius\] | PowerTrack | Matches against the Exact Location (x,y) of the user's [Profile Geo enrichment](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/enrichments/overview).<br><br>* Units of radius supported are miles (mi) and kilometers (km).<br>* Radius must be less than 25mi.<br>* Longitude is in the range of ±180<br>* Latitude is in the range of ±90<br>* All coordinates are in decimal degrees.<br>* Rule arguments are contained within brackets, space delimited.<br><br>**Note:** operators matching on place (Tweet geo) will only include matches from original tweets. Retweets do not contain any place data. | `user.derived.locations.geo` |
| profile\_region: | PowerTrack<br><br>Search<br><br>Premium | Exact match on the Region field from the [Profile Geo enrichment](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/enrichments/overview).<br><br>This is an exact full string match.<br><br>It is not necessary to escape characters with a backslash. For example, if matching something with a slash, use `one/two`.<br><br>Use double quotes to match substrings that contain whitespace or punctuation, e.g. `profile_locality:"New York"`. | `user.derived.locations.region` |
| profile\_subregion: | PowerTrack | Exact match on the Subregion field from the [Profile Geo enrichment](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/enrichments/overview).<br><br>This is an exact full string match.<br><br>It is not necessary to escape characters with a backslash. For example, if matching something with a slash, use `one/two`.<br><br>Use double quotes to match substrings that contain whitespace or punctuation, e.g. `profile_locality:"Kings County"`. | `user.derived.locations.sub_region` |
| "keyword1 keyword2"~N | PowerTrack<br><br>Search | Commonly referred to as a proximity operator, this matches a Tweet where the keywords are no more than N tokens from each other.<br><br>If the keywords are in the opposite order, they can not be more than N-2 tokens from each other.<br><br>Can have any number of keywords in quotes.<br><br>N cannot be greater than 6. | `text` |
| retweets\_of\_status\_id: | PowerTrack | _Available alias_: retweets\_of\_tweet\_id:<br><br>Deliver only explicit Retweets of the specified original Tweet. | `retweeted_status.id`, `retweeted_status.id_str` |
| retweets\_of: | PowerTrack<br><br>Search<br><br>Premium<br><br>Sandbox | _Available alias_: retweets\_of\_user:<br><br>Matches any Tweet that are Retweets of the given user. The value can be either the username (excluding the `@` character) or the user’s numeric ID or (obtained for example via the [GET users/lookup](https://developer.twitter.com/content/developer-twitter/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-lookup) endpoint). | `retweeted_status.id` (if present) |
| sample: | PowerTrack | Returns a random percent sample of Tweets that match a rule rather than the entire set of Tweets. The percent value must be represented by an integer between 1 and 100.<br><br>This operator applies to the entire rule and requires all OR'd terms to be grouped.<br><br>**Note:** the sample operator first reduces the scope of the firehose to X%, then the rule/filter is applied to that sampled subset. If you are using, for example, `sample:10`, each Tweet has a 10% chance of being in the sample. <br><br>**Note:** the sampling is deterministic, and you will get the same data sample in realtime as you would if you pulled the data historically. |     |
| source: | PowerTrack | Matches any Tweet generated by the given source application. The value must be either the name of the application or the application’s URL.<br><br>Cannot be used as a standalone operator. | `source` |
| statuses\_count: | PowerTrack | _Available alias_: tweets\_count:<br><br>Matches Tweets when the author has posted a number of statuses that falls within the given range.<br><br>* A single number (e.g. `statuses_count:42`) will match any number equal to or greater than the value specified.<br>* A range (e.g. `statuses_count:42..1337`) will match any number in the given range. | `user``.statuses_count` |
| to: | PowerTrack<br><br>Search<br><br>Premium<br><br>Sandbox | Matches any Tweet that is in reply to a particular user. The value can be either the username (excluding the `@` character) or the user’s numeric ID or (obtained for example via the [GET users/lookup](https://developer.twitter.com/content/developer-twitter/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-lookup) endpoint). | `text` |
| url: | PowerTrack<br><br>Search<br><br>Premium<br><br>Sandbox | Performs a tokenized match on the expanded URLs of a Tweet. Tokens and phrases containing punctuation or special characters should be double-quoted (e.g. `url:"/developer"`).<br><br>While generally not recommended, the operator can also match on a specific protocol, enclosed in double-quotes (e.g. `url:"https://developer.twitter.com"`). | `entities.urls.expanded_url` |
| url\_contains: | PowerTrack | Performs a keyword/phrase match on the (new) [expanded URL title metadata enrichment](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/enrichments/overview/expanded-and-enhanced-urls). | `entities.urls.expanded_url` |
| url\_description: | PowerTrack | _Available alias_: within\_url\_description:<br><br>Performs a keyword/phrase match on the (new) [expanded page description metadata enrichment](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/enrichments/overview/expanded-and-enhanced-urls). | `entities.urls.unwound.description` |
| url\_title: | PowerTrack | _Available alias_: within\_url\_title:<br><br>Performs a keyword/phrase match on the (new) [expanded URL title metadata enrichment](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/enrichments/overview/expanded-and-enhanced-urls). | `entities.urls.title` |

Rate limits: Enterprise

Overview
--------

Every day many thousands of developers make requests to the Twitter API. To help manage the sheer volume of these requests, limits are placed on the number of requests that can be made. These limits help us provide the reliable and scalable API that our developer community relies on. 

The maximum number of requests that are allowed is based on a time interval, some specified period or window of time. If an endpoint has a rate limit of 900 requests/15-minutes, then up to 900 requests over any 15-minute interval is allowed. 

###   
Enterprise rate limits per window

| Product | Endpoint | Rate limit |
| --- | --- | --- |
| PowerTrack API | Streaming endpoint | 60 requests per minute |
| Rules endpoint | 60 requests per minute aggregated across all /rules endpoints |
| Replay endpoint | 5 requests per 5 minutes |
| Historical PowerTrack API |     | 60 Jobs can be created per (UTC) day. |
|     | 30 Jobs can be created per hour. |
|     | 2 Jobs can be estimating concurrently. |
|     | 2 Jobs can be running concurrently. |
| Decahose API |     | 10 requests per minute |
| Streaming likes API |     | 10 requests per minute |
| Firehose API |     | 10 requests per minute |
| Account Activity API | POST account\_activity/webhooks | 15 requests per 15 minutes |
| GET account\_activity/webhooks | 15 requests per 15 minutes |
| PUT account\_activity/webhooks/:webhook\_id | 15 requests per 15 minutes |
| POST account\_activity/webhooks/:webhook\_id/subscriptions/all | 500 requests per 15 minutes |
| GET account\_activity/subscriptions/count | 15 requests per 15 minutes |
| GET account\_activity/webhooks/:webhook\_id/subscriptions/all | 500 requests per 15 minutes |
| GET account\_activity/webhooks/:webhook\_id/subscriptions/all/list | 50 requests per 15 minutes |
| DELETE account\_activity/webhooks/:webhook\_id | 15 requests per 15 minutes |
| DELETE /account\_activity/webhooks/:webhook\_id/subscriptions/:user\_id/all.json | 500 requests per 15 minutes |
| Replay | 5 requests per 15 minutes |
| Search API |     | Per minute rate limit will vary by contract |
|     | 20 requests per second aggregated across either the 30 day data and counts endpoints, or across the full-archive data and counts endpoints |
| Engagement API |     | Per minute rate limit will vary by contract |
| Compliance Firehose API |     | 10 requests per minute |
| Usage API |     | 2 requests per minute |

Edit Tweets

Introduction
------------

Enterprise endpoints have been updated to provide edited Tweet metadata. The _Edit Tweets_ feature was first introduced for testing among Twitter employees on September 1, 2022. Starting on that date, eligible Tweets were editable for 30 minutes and up to 5 times. _All objects for Tweets created since September 29, 2022_ include Tweet edit metadata, even if the Tweet was never edited. Each time a Tweet is edited, a new Tweet ID is created. A Tweet's edit history can be described by chaining these IDs together, starting with the original ID. Additionally, if any Tweet in the edit chain is deleted, all Tweets in that chain are deleted as well. 

These metadata details are included automatically. No request parameters are needed to include available edit history as part of the Tweet object. 

With these new metadata, a developer can find out:

* If a Tweet was edit eligible at the time of creation. Some Tweets, such as those with polls or scheduled Tweets, cannot be edited.
* Tweets are editable for 30 minutes, and can be edited up to 5 times. For editable Tweets, you can see if time for editing remains and how many more edits are possible.
* If you are viewing an edited version of a Tweet. In most cases, the API will return the most recent version of a Tweet, unless a specific past version is requested by Tweet ID.

Three new Tweet attributes have been added at the root level:

* **edit\_history**  - Provides all Tweet IDs associated with the edit history of the Tweet. The "initial\_tweet\_id" attribute indicates the original Tweet and the "edit\_tweet\_ids" attribute is an array that provides all IDs associated with its edit history. If the Tweet has not been edited, this array will contain a single ID.

"edit\_history": {
    "initial\_tweet\_id": "1283764123"
    "edit\_tweet\_ids": \["1283764123"\]
  }

* **edit\_controls** - Provides attributes that indicate when the 30-minute edit window ends and how many potential edits remain. 

"edit\_controls": {  
     "editable\_until\_ms": 1660155761384
     "edits\_remaining": 3   
  }

* **editable** - Indicates whether a Tweet was eligible for editing when created. 

"editable": true

Most Tweets are eligible. However, the following types of Tweets are not: 

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

      `{   "created_at": "Wed Aug 16 18:29:02 +0000 2022",   "id": 1557433858676740098,   "id_str": "1557433858676740098",   "text": "I wonder if I will every use teh edit button",   "edit_history": {     "initial_tweet_id": "1557433858676740098",     "edit_tweet_ids": ["1557433858676740098"]   },   "edit_controls": {     "editable_until_ms": 1660155761384,     "edits_remaining": 5   },   "editable": true }`
    

Example attributes for an edited Tweet
--------------------------------------

The JSON below highlights edit metadata that is included for a Tweet posted after the edit Tweet feature was added. This example is for a Tweet that has had a single edit. 

Note that the "edit\_tweet\_ids" array has two IDs, one for the original Tweet and one for the edited update. 

      `{   "created_at": "Wed Aug 16 18:35:42 +0000 2022",   "id": 1557445923210514432,   "id_str": "1557445923210514432",   "text": "I wonder if I will ever use the edit button",   "edit_history": {     "initial_tweet_id": "1557433858676740098",     "edit_tweet_ids": ["1557433858676740098", "1557445923210514432"]   },   "edit_controls": {     "editable_until_ms": 1660155761384,     "edits_remaining": 4   },   "editable": true }`
    

Compliance support
------------------

The [Compliance Firehose](https://developer-staging.twitter.com/en/docs/twitter-api/enterprise/compliance-firehose-api/overview) and the v2 [batch compliance endpoint](https://developer.twitter.com/en/docs/twitter-api/compliance/batch-compliance) have both been updated to provide edit Tweet support: 

A new "tweet\_edit" event type has been added to the Compliance Firehose. 

      `{   "tweet_edit": {     "id": <tweetId>,     "initial_tweet_id": <tweetId>,     "edit_tweet_ids": [<tweetId1>, <tweetId2>, <tweetId3> ...],     "timestamp_ms": "<timestampMsStr>"   } }`