
Tweet object | Docs | Twitter Developer Platform 

Tweet object

Tweet Object
------------

Tweets are the basic atomic building block of all things Twitter. Tweets are also known as “status updates.” The Tweet object has a long list of ‘root-level’ attributes, including fundamental attributes such as `id`, `created_at`, and `text`. Tweet objects are also the ‘parent’ object to several child objects. Tweet child objects include `user`, `entities`, and `extended_entities`. Tweets that are geo-tagged will have a `place` child object.

When the following Tweet is rendered in JSON:

> 1/ To make room for more expression, we will now count all emojis as equal—including those with gender‍‍‍ ‍‍and skin t… https://t.co/MkGjXf9aXm
> 
> 
> — TwitterAPI (@TwitterAPI) Oct 10, 2018

The JSON will be a mix of ‘root-level’ attributes (here we are highlighting some of the most fundamental attributes), and child objects (which are represented here with the `{}` notation):

```
{
 "created_at": "Wed Oct 10 20:19:24 +0000 2018",
 "id": 1050118621198921728,
 "id_str": "1050118621198921728",
 "text": "To make room for more expression, we will now count all emojis as equal—including those with gender‍‍‍ ‍‍and skin t… https://t.co/MkGjXf9aXm",
 "user": {},  
 "entities": {}
}
```

### Tweet Data Dictionary

Below you will find the data dictionary for these ‘root-level’ attributes, as well as links to child object data dictionaries.

| Attribute | Type | Description |
| --- | --- | --- |
| created\_at | String | UTC time when this Tweet was created. Example:
```
"created_at": "Wed Oct 10 20:19:24 +0000 2018"
```

 |
| id | Int64 | The integer representation of the unique identifier for this Tweet. This number is greater than 53 bits and some programming languages may have difficulty/silent defects in interpreting it. Using a signed 64 bit integer for storing this identifier is safe. Use `id\_str` to fetch the identifier to be safe. See Twitter IDs for more information. Example:
```
"id":1050118621198921728
```

 |
| id\_str | String | The string representation of the unique identifier for this Tweet. Implementations should use this rather than the large integer in `id`. Example:
```
"id_str":"1050118621198921728"
```

 |
| text | String | The actual UTF-8 text of the status update. See twitter-text for details on what characters are currently considered valid. Example:
```
"text":"To make room for more expression, we will now count all emojis as equal—including those with gender‍‍‍ ‍‍and skin t… https://t.co/MkGjXf9aXm"
```

 |
| source | String | Utility used to post the Tweet, as an HTML-formatted string. Tweets from the Twitter website have a source value of `web`.
Example:
```
"source":"Twitter Web Client"
```

 |
| truncated | Boolean | Indicates whether the value of the `text` parameter was truncated, for example, as a result of a retweet exceeding the original Tweet text length limit of 140 characters. Truncated text will end in ellipsis, like this `...` Since Twitter now rejects long Tweets vs truncating them, the large majority of Tweets will have this set to `false` . Note that while native retweets may have their toplevel `text` property shortened, the original text will be available under the `retweeted\_status` object and the `truncated` parameter will be set to the value of the original status (in most cases, `false` ). Example:
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
| place | Places | *Nullable* When present, indicates that the tweet is associated (but not necessarily originating from) a Place . Example:
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
| retweeted\_status | Tweet | Users can amplify the broadcast of Tweets authored by other users by retweeting . Retweets can be distinguished from typical Tweets by the existence of a `retweeted\_status` attribute. This attribute contains a representation of the *original* Tweet that was retweeted. Note that retweets of retweets do not show representations of the intermediary retweet, but only the original Tweet. (Users can also unretweet a retweet they created by deleting their retweet.) |
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
| filter\_level | String | Indicates the maximum value of the filter\_level parameter which may be used and still stream this Tweet. So a value of `medium` will be streamed on `none`, `low`, and `medium` streams.
Example:
```
"filter_level": "low"
```

 |
| lang | String | *Nullable.* When present, indicates a BCP 47 language identifier corresponding to the machine-detected language of the Tweet text, or `und` if no language could be detected. See more documentation HERE. Example:
```
"lang": "en"
```

 |
| matching\_rules | Array of Rule Objects | Present in *filtered* products such as Twitter Search and PowerTrack. Provides the *id* and *tag* associated with the rule that matched the Tweet. With PowerTrack, more than one rule can match a Tweet. See more documentation HERE. Example:
```
"matching_rules": " [{
        "tag": "twitterapi emojis",
        "id": 1050118621198921728,
        "id_str": "1050118621198921728"
    }]"
```

 |

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