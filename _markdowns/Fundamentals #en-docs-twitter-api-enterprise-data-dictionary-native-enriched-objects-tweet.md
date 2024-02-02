



Native Enriched Tweet object | Docs | Twitter Developer Platform 





































































































Tweet object








Interested in learning more about how the Native Enriched data format maps to the Twitter API v2 format?


Check out our comparison guide: Native Enriched compared to Twitter API v2









Tweet Object
------------


When using enterprise data products, you will notice that much of the data dictionary is similar to the native format of Tweet data, with some additional enriched metadata.  The base level of the native enriched format uses much of the same object names as the Twitter API v1.1 data format.  The Tweet object has a long list of ‘root-level’ attributes, including fundamental attributes such as `id`, `created_at`, and `text`. Tweet objects will also have nested objects to include the `user`, `entities`, and `extended_entities`. Tweet objects will also have other nested Tweet objects such as retweeted\_status, quoted\_status and extended\_tweet.  The native enriched format will additionally have a matching\_rules object.


 


### Tweet Data Dictionary


Below you will find the data dictionary for these ‘root-level’ attributes, as well as links to child object data dictionaries.




| Attribute | Type | Description |
| --- | --- | --- |
| created\_at | String | UTC time when this Tweet was created. Example:

```

"created_at": "Wed Oct 10 20:19:24 +0000 2018"

```


 |
| id | Int64 | The integer representation of the unique identifier for this Tweet. This number is greater than 53 bits and some programming languages may have difficulty/silent defects in interpreting it. Using a signed 64 bit integer for storing this identifier is safe. Use `**id\_str**` to fetch the identifier to be safe. See Twitter IDs for more information. Example:

```

"id":1050118621198921728

```


 |
| id\_str | String | The string representation of the unique identifier for this Tweet. Implementations should use this rather than the large integer in `**id**`. Example:

```

"id_str":"1050118621198921728"

```


 |
| text | String | The actual UTF-8 text of the status update. See twitter-text for details on what characters are currently considered valid. Example:

```

"text":"To make room for more expression, we will now count all emojis as equal—including those with gender‍‍‍ ‍‍and skin t… https://t.co/MkGjXf9aXm"

```


 |
| source | String | Utility used to post the Tweet, as an HTML-formatted string. Tweets from the Twitter website have a source value of `**web**`.
Example:

```

"source":"Twitter Web Client"

```


 |
| truncated | Boolean | Indicates whether the value of the `**text**` parameter was truncated, for example, as a result of a retweet exceeding the original Tweet text length limit of 140 characters. Truncated text will end in ellipsis, like this `**...**` Since Twitter now rejects long Tweets vs truncating them, the large majority of Tweets will have this set to `**false**` . Note that while native retweets may have their toplevel `**text**` property shortened, the original text will be available under the `**retweeted\_status**` object and the `**truncated**` parameter will be set to the value of the original status (in most cases, `**false**` ). Example:

```

"truncated":true

```


 |
| in\_reply\_to\_status\_id | Int64 | *Nullable.* If the represented Tweet is a reply, this field will contain the integer representation of the original Tweet’s ID. Example:

```

"in_reply_to_status_id":1051222721923756032

```


 |
| in\_reply\_to\_status\_id\_str | String | *Nullable.* If the represented Tweet is a reply, this field will contain the string representation of the original Tweet’s ID. Example:

```

"in_reply_to_status_id_str":"1051222721923756032"

```


 |
| in\_reply\_to\_user\_id | Int64 | *Nullable.* If the represented Tweet is a reply, this field will contain the integer representation of the original Tweet’s author ID. This will not necessarily always be the user directly mentioned in the Tweet. Example:

```

"in_reply_to_user_id":6253282

```


 |
| in\_reply\_to\_user\_id\_str | String | *Nullable.* If the represented Tweet is a reply, this field will contain the string representation of the original Tweet’s author ID. This will not necessarily always be the user directly mentioned in the Tweet. Example:

```

"in_reply_to_user_id_str":"6253282"

```


 |
| in\_reply\_to\_screen\_name | String | *Nullable.* If the represented Tweet is a reply, this field will contain the screen name of the original Tweet’s author. Example:

```

"in_reply_to_screen_name":"twitterapi"

```


 |
| user | User object | The user who posted this Tweet. See User data dictionary for complete list of attributes.
Example highlighting select attributes:

```


 { "user": {
    "id": 6253282,
    "id_str": "6253282",
    "name": "Twitter API",
    "screen_name": "TwitterAPI",
    "location": "San Francisco, CA",
    "url": "https://developer.twitter.com",
    "description": "The Real Twitter API. Tweets about API changes, service issues and our Developer Platform. Don't get an answer? It's on my website.",
    "verified": true,
    "followers_count": 6129794,
    "friends_count": 12,
    "listed_count": 12899,
    "favourites_count": 31,
    "statuses_count": 3658,
    "created_at": "Wed May 23 06:01:13 +0000 2007",
    "utc_offset": null,
    "time_zone": null,
    "geo_enabled": false,
    "lang": "en",
    "contributors_enabled": false,
    "is_translator": false,
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
  }
}

```


 |
| coordinates | Coordinates | *Nullable.* Represents the geographic location of this Tweet as reported by the user or client application. The inner coordinates array is formatted as geoJSON (longitude first, then latitude). Example:

```

"coordinates":
{
    "coordinates":
    [
        -75.14310264,
        40.05701649
    ],
    "type":"Point"
}

```


 |
| place | Places | *Nullable* When present, indicates that the tweet is associated (but not necessarily originating from) a Place  Example:

```

"place":
{
  "attributes":{},
   "bounding_box":
  {
     "coordinates":
     [[
           [-77.119759,38.791645],
           [-76.909393,38.791645],
           [-76.909393,38.995548],
           [-77.119759,38.995548]
     ]],
     "type":"Polygon"
  },
   "country":"United States",
   "country_code":"US",
   "full_name":"Washington, DC",
   "id":"01fbe706f872cb32",
   "name":"Washington",
   "place_type":"city",
   "url":"http://api.twitter.com/1/geo/id/0172cb32.json"
}

```


 |
| quoted\_status\_id | Int64 | This field only surfaces when the Tweet is a quote Tweet. This field contains the integer value Tweet ID of the quoted Tweet. Example:

```

"quoted_status_id":1050119905717055488

```


 |
| quoted\_status\_id\_str | String | This field only surfaces when the Tweet is a quote Tweet. This is the string representation Tweet ID of the quoted Tweet. Example:

```

"quoted_status_id_str":"1050119905717055488"

```


 |
| is\_quote\_status | Boolean | Indicates whether this is a Quoted Tweet. Example:

```

"is_quote_status":false

```


 |
| quoted\_status | Tweet | This field only surfaces when the Tweet is a quote Tweet. This attribute contains the Tweet object of the original Tweet that was quoted. |
| retweeted\_status | Tweet | Users can amplify the broadcast of Tweets authored by other users by Retweeting . Retweets can be distinguished from typical Tweets by the existence of a `**retweeted\_status**` attribute. This attribute contains a representation of the *original* Tweet that was retweeted. Note that retweets of retweets do not show representations of the intermediary retweet, but only the original Tweet. (Users can also unretweet a retweet they created by deleting their retweet.) |
| quote\_count | Integer | *Nullable.* Indicates approximately how many times this Tweet has been quoted by Twitter users. Example:

```

"quote_count":33

```

Note: This object is only available with the Premium and Enterprise tier products. |
| reply\_count | Int | Number of times this Tweet has been replied to. Example:

```

"reply_count":30

```

Note: This object is only available with the Premium and Enterprise tier products. |
| retweet\_count | Int | Number of times this Tweet has been retweeted. Example:

```

"retweet_count":160

```


 |
| favorite\_count | Integer | *Nullable.* Indicates approximately how many times this Tweet has been liked by Twitter users. Example:

```

"favorite_count":295

```


 |
| entities | Entities | Entities which have been parsed out of the text of the Tweet. Additionally see Entities in Twitter Objects . Example:

```

"entities":
{
    "hashtags":[],
    "urls":[],
    "user_mentions":[],
    "media":[],
    "symbols":[]
    "polls":[]
}

```


 |
| extended\_entities | Extended Entities | When between one and four native photos or one video or one animated GIF are in Tweet, contains an array 'media' metadata. This is also available in Quote Tweets. Additionally see Entities in Twitter Objects . Example:

```

"entities":
{
    "media":[]
}

```


 |
| favorited | Boolean | *Nullable.* Indicates whether this Tweet has been liked by the authenticating user. Example:

```

"favorited":true

```


 |
| retweeted | Boolean | Indicates whether this Tweet has been Retweeted by the authenticating user. Example:

```

"retweeted":false

```


 |
| possibly\_sensitive | Boolean | *Nullable.* This field indicates content may be recognized as sensitive. The Tweet author can select within their own account preferences and choose “Mark media you tweet as having material that may be sensitive” so each Tweet created after has this flag set.
This may also be judged and labeled by an internal Twitter support agent.

```

"possibly_sensitive":false

```


 |
| filter\_level | String | Indicates the maximum value of the filter\_level parameter which may be used and still stream this Tweet. So a value of `**medium**` will be streamed on `**none**`, `**low**`, and `**medium**` streams.
Example:

```

"filter_level": "low"

```


 |
| lang | String | *Nullable.* When present, indicates a BCP 47 language identifier corresponding to the machine-detected language of the Tweet text, or `**und**` if no language could be detected. 
 Example:

```

"lang": "en"

```


 |
| edit\_history | Object | Unique identifiers indicating all versions of a Tweet. For Tweets with no edits, there will be one ID. For Tweets with an edit history, there will be multiple IDs, arranged in ascending order reflecting the order of edits, with the most recent version in the last position of the array. 
The Tweet IDs can be used to hydrate and view previous versions of a Tweet.
 
Example:

```

edit_history": {
    "initial_tweet_id": "1283764123"
    "edit_tweet_ids": ["1283764123", "1394263866"]
  }

```


 |
| edit\_controls | Object | When present, indicates how long a Tweet is still editable for and the number of remaining edits. Tweets are only editable for the first 30 minutes after creation and can be edited up to five times. 
The Tweet IDs can be used to hydrate and view previous versions of a Tweet.
 
Example:

```

"edit_controls": {  
     "editable_until_ms": 123
     "edits_remaining": 3   
  }

```


 |
| editable | Boolean | When present, indicates if a Tweet was eligible for edit when published. This field is not dynamic and won't toggle from True to False when a Tweet reaches its editable time limit, or maximum number of edits. The following Tweet features will cause this field to be false:* Tweets is promoted
* Tweet has a poll
* Tweet is a non-self-thread reply
* Tweet is a retweet (note that Quote Tweets are eligible for edit)
* Tweet is nullcast
* Community Tweet
* Superfollow Tweet
* Collaborative Tweet

  |
| matching\_rules | Array of Rule Objects | Present in *filtered* products such as Twitter Search and PowerTrack. Provides the *id* and *tag* associated with the rule that matched the Tweet. More on matching rules here. With PowerTrack, more than one rule can match a Tweet. 
Example:

```

"matching_rules": " [{
        "tag": "twitterapi emojis",
        "id": 1050118621198921728,
        "id_str": "1050118621198921728"
    }]"

```


 |
|  |  |  |


 


### Additional Tweet attributes


Twitter APIs that provide Tweets (e.g. the GET statuses/lookup endpoint) may include these additional Tweet attributes:




| Attribute | Type | Description |
| --- | --- | --- |
| current\_user\_retweet | Object | *Perspectival* Only surfaces on methods supporting the include\_my\_retweet parameter, when set to true. Details the Tweet ID of the user’s own retweet (if existent) of this Tweet. Example:

```

"current_user_retweet": {
  "id": 6253282,
  "id_str": "6253282"
}

```
 |
| scopes | Object | A set of key-value pairs indicating the intended contextual delivery of the containing Tweet. Currently used by Twitter’s Promoted Products. Example:

```

"scopes":{"followers":false}

```
 |
| withheld\_copyright | Boolean | When present and set to “true”, it indicates that this piece of content has been withheld due to a DMCA complaint . Example:

```

"withheld_copyright": true

```
 |
| withheld\_in\_countries | Array of String | When present, indicates a list of uppercase two-letter country codes this content is withheld from. Twitter supports the following non-country values for this field:
“XX” - Content is withheld in all countries “XY” - Content is withheld due to a DMCA request.
Example:

```

"withheld_in_countries": ["GR", "HK", "MY"]

```
 |
| withheld\_scope | String | When present, indicates whether the content being withheld is the “status” or a “user.”
Example:

```

"withheld_scope": "status"

```
 |


 


### Deprecated Attributes




| Field | Type | Description |
| --- | --- | --- |
| geo | Object | **Deprecated.** *Nullable.* Use the `coordinates` field instead. This deprecated attribute has its coordinates formatted as *[lat, long]*, while all other Tweet geo is formatted as *[long, lat]*. |


 



Nested Tweet objects
---------------------


In several cases, a Tweet object will included other nested objects.  If you are working with nested objects, then that JSON payload will contain multiple Tweet objects, and each Tweet object may contain its own objects. The root-level object will contain information on the type of action taken, i.e. whether it is a Retweet or a Quote Tweet, and may also contain an object that describes the 'original' Tweet being shared. Extended Tweets will include a nested extended object that extends beyond 140 characters, which was used to prevent breaking changes when the update was made in 2017. Each nested object dictionary is described below.






 


#### Retweets


Retweets always contain two Tweet objects. The 'original' Tweet being Retweeted is provided in a "retweeted\_status" object. The root-level object encapsulates the Retweet itself, including a User object for the account taking the Retweet action and the time of the Retweet. Retweeting is an action to share a Tweet with your followers, and no other new content can be added. Also, a (new) location cannot be provided with a Retweet. While the 'original' Tweet may have geo-tagged, the Retweet "geo" and "place" objects will always be null.


Even before the introduction of Extended Tweets, the root-level "entities" object was in some cases truncated and incomplete due to the "RT @username " string being appended to Tweet message being Retweeted.  Note that if a Retweet gets Retweeted, the "retweet\_status" will still point to the original Tweet, meaning the intermediate Retweet is not included. Similar behavior is seen when using twitter.com to 'display' a Retweet. If you copy the unique Tweet ID assigned to the Retweet 'action', the original Tweet is displayed. 


Below is an example structure for a Retweet. Again, when parsing Retweets, it is key to parse the "retweeted\_status" object for complete (original) Tweet message and entity metadata.  

  














```

      {
	"tweet": {
		"text": "RT @author original message",
		"user": {
			"screen_name": "Retweeter"
		},
		"retweeted_status": {
			"text": "original message",
			"user": {
				"screen_name": "OriginalTweeter"
			},
			"place": {},
			"entities": {},
			"extended_entities": {}
		}
	},
	"entities": {},
	"extended_entities": {}
}
    
```





Code copied to clipboard








 


#### Quote Tweets


Quote Tweets are much like Retweets except that they include a new Tweet message. These new messages can contain their own set of hashtags, links, and other "entities" metadata. Quote Tweets can also include location information shared by the user posting the Quote Tweet, along with media such as GIFs, videos, and photos.


Quote Tweets will contain at least two Tweet objects, and in some cases, three. The Tweet being Quoted, which itself can be a Quoted Tweet, is provided in a "quoted\_status" object. The root-level object encapsulates the Quote Tweet itself, including a User object for the account taking the sharing action and the time of the Quote Tweet.


Note that Quote Tweets can now have photos, GIFs, or videos, added to them using the 'post Tweet' user-interface. When links to externally hosted media are included in the Quote Tweet message, the root-level "entities.urls" will describe those. Media attached to Quote Tweets will appear in the root-level "extended\_entities" metadata.


When Quote Tweets were first launched, a shortened link (t.co URL) was appended to the 'original' Tweet message and provided in the root-level "text" field. In addition, metadata for that t.co URL was included in the root-level 'entities.urls' array. In May 2018, we changed this so that the shortened t.co URL to the quoted Tweet *will not be included*in the root-level "text" field. Second, the metadata for the quoted Tweet*will not be included* in the "entities.urls" metadata. Instead, URL metadata for the quoted Tweet will be in a new "quoted\_status\_permalink" object on the root-level (or top-level), so at the same level of the "quoted\_status" object.


Below is an example structure for a Quote Tweet using this original formatting.   

  














```

      {
	"created_at": "Tue Feb 14 19:30:06 +0000 2017",
	"id_str": "831586333415976960",
	"text": "Definitely quotable! https:\/\/t.co\/J1LKrbHpWR",
	"user": {
		"screen_name": "happycamper"
	},
	"quoted_status_id_str": "831569219296882688",
	"quoted_status": {
		"created_at": "Tue Feb 14 18:22:06 +0000 2017",
		"id_str": "831569219296882688",
		"text": "This is a test of the tweeting system \ud83d\ude0e to update #supportdocs @twitterboulder here: https:\/\/t.co\/NRq9UrSzm0",
		"user": {
			"screen_name": "furiouscamper",
		},
		"place": {
			"id": "9a974dfc8efb32a0",
		},
		"entities": {
			"hashtags": [{
				"text": "supportdocs",
			}],
			"urls": [{
			}],
			"user_mentions": [{	}],
			"symbols": []
		},
	},
	"is_quote_status": true,
	"entities": {},
	"matching_rules": [{}]
}
    
```





Code copied to clipboard














```

      {
	"created_at": "Fri Jan 04 18:47:16 +0000 2019",
	"id_str": "1081260794069671936",
	"text": "Quote test https://t.co/CE4m1qs3NJ",
	"user": {
		"screen_name": "furiouscamper"
	},
	"place": null,
	"quoted_status_id_str": "1079578364904648705",
	"quoted_status": {
		"created_at": "Mon Dec 31 03:21:54 +0000 2018",
		"id_str": "1079578364904648705",
		"text": "AHHHHH",
		"user": {
			"screen_name": "infinite_scream"
		},
		"place": null,
		"is_quote_status": false,
		"quote_count": 1,
		"reply_count": 0,
		"retweet_count": 3,
		"favorite_count": 6,
		"entities": {
			"hashtags": [],
			"urls": [],
			"user_mentions": [],
			"symbols": []
		}
	},
	"quoted_status_permalink": {
		"url": "https://t.co/CE4m1qs3NJ",
		"expanded": "https://twitter.com/infinite_scream/status/1079578364904648705",
		"display": "twitter.com/infinite_screa…"
	},
	"is_quote_status": true,
	"quote_count": 0,
	"reply_count": 0,
	"retweet_count": 0,
	"favorite_count": 1,
	"entities": {}
}
    
```





Code copied to clipboard








 


### Extended Tweets


JSON that describes *Extended Tweets* was introduced when 280-character Tweets were launched in November 2017. Tweet JSON was extended to encapsulate these longer messages, while not breaking the thousands of apps parsing these fundamental Twitter objects. To provide full backward compatibility, the original 140-character 'text' field, and the entity objects parsed from that, were retained. In the case of Tweets longer than 140 characters, this root-level 'text' field would become truncated and thus incomplete. Since the root-level 'entities' objects contain arrays of key metadata parsed from the 'text' message, such as included hashtags and links, these collections would be incomplete. For example, if a Tweet message was 200 characters long, with a hashtag included at the end, the legacy root-level 'entities.hashtags' array would not include it. 


A new 'extended\_tweet' field was introduced to hold the longer Tweet messages and complete entity metadata. The "extended\_tweet" object provides the "full\_text" field that contains the complete, untruncated Tweet message when longer than 140 characters. The "extended\_tweet" object also contains an "entities" object with complete arrays of hashtags, links, mentions, etc.


Extended Tweets are identified with a root-level "truncated" boolean. When true ("truncated": true), the "extended\_tweet" fields should be parsed instead of the root-level fields.


Note in the JSON example below that the root-level "text" field is truncated and the root-level "entities.hashtags" array is empty even though the Tweet message includes three hashtags. Since this is an Extended Tweet, the "truncated" field is set to true, and the "extended\_tweet" object provides complete "full\_text" and "entities" Tweet metadata.  

  














```

      {
	"created_at": "Thu May 10 17:41:57 +0000 2018",
	"id_str": "994633657141813248",
	"text": "Just another Extended Tweet with more than 140 characters, generated as a documentation example, showing that [\"tru… https://t.co/U7Se4NM7Eu",
	"display_text_range": [0, 140],
	"truncated": true,
	"user": {
		"id_str": "944480690",
		"screen_name": "FloodSocial"
	},
	"extended_tweet": {
		"full_text": "Just another Extended Tweet with more than 140 characters, generated as a documentation example, showing that [\"truncated\": true] and the presence of an \"extended_tweet\" object with complete text and \"entities\" #documentation #parsingJSON #GeoTagged https://t.co/e9yhQTJSIA",
		"display_text_range": [0, 249],
		"entities": {
			"hashtags": [{
				"text": "documentation",
				"indices": [211, 225]
			}, {
				"text": "parsingJSON",
				"indices": [226, 238]
			}, {
				"text": "GeoTagged",
				"indices": [239, 249]
			}]
		}

	},
	"entities": {
		"hashtags": []
	}
}
    
```





Code copied to clipboard








### Next Steps


Explore the other sub-objects that a Tweet contains:


* User object and data dictionary
* Entities object and data dictionary
* Extended Entities object and data dictionary
* Tweet geo objects and data dictionaries



















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















