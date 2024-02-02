
Activity Streams activity object | Docs | Twitter Developer Platform 

Activity object

Interested in learning more about how the Activity Streams data format maps to the Twitter API v2 format?

Check out our comparison guide: Activity Streams compared to Twitter API v2

Please note: It is highly recommended to use the Enriched Native format for enterprise data APIs. 

* The Enriched Native format includes all new metadata since 2017, such as poll metadata, and additional metrics such as reply\_count and quote\_count.
* Activity Streams format has not been updated with new metadata or enrichments since the character update in 2017.

Activity Object
---------------

Activity Streams is an object schema translation of Twitter's original data format created by Gnip to 'normalize the format' of Tweet data and other social media data using the third party Activity Base Schema described here.  Tweets are normalized into the activity streams schema, including: note, person, place and service object types as nested objects.  Tweets can have other nested Tweet activity obejcts for Retweets, or others including twitter\_quoted\_status, long\_object.

The base level object type "activity" is similar to the Tweet base level object of the native enriched format.  Example payloads in activity streams format can be found here.

### Data Dictionary

Below you will find the data dictionary for these ‘root-level’ "activity" attributes, as well as links to child object data dictionaries.

|  |  |  |
| --- | --- | --- |
| Attribute | Type | Description |
| id | string | A unique IRI for the tweet. In more detail, "tag" is the scheme, "search.twitter.com" represents the domain for the scheme, and 2005 is when the scheme was derived.
When storing Tweets, this should be used as the unique identifier or primary key.
"id": "tag:search.twitter.com,2005:1050118621198921728" |
| objectType | string | Type of object, always set to "activity"
"objectType": "activity" |
| object | object | An object representing tweet being posted or shared.
For Retweets, this will contain an entire "activity", with the pertinent fields described in this schema.
For Original Tweets, this will contain a "note" object, with the fields described here.
"object":
"object": {
"objectType": "note",
"id": "object:search.twitter.com,2005:1050118621198921728",
"summary": "To make room for more expression, we will now count all emojis as equal—including those with gender‍‍‍ ‍‍and skin t… https://t.co/MkGjXf9aXm",
"link": "http://twitter.com/TwitterAPI/statuses/1050118621198921728",
"postedTime": "2018-10-10T20:19:24.000Z"
} |
| long\_object | object | An object representing the full text body if the Tweet text extends beyond 140 characters.

"long\_object": {
"body": "To make room for more expression, we will now count all emojis as equal—including those with gender‍‍‍ ‍‍and skin tone modifiers 👍🏻👍🏽👍🏿. This is now reflected in Twitter-Text, our Open Source library. \n\nUsing Twitter-Text? See the forum post for detail: https://t.co/Nx1XZmRCXA",
"display\_text\_range": [
0,
277
],
"twitter\_entities": {
"hashtags": [],
"urls": [
{
"url": "https://t.co/Nx1XZmRCXA",
"expanded\_url": "https://twittercommunity.com/t/new-update-to-the-twitter-text-library-emoji-character-count/114607",
"display\_url": "twittercommunity.com/t/new-update-t…",
"indices": [
254,
277
]
}
],
"user\_mentions": [],
"symbols": []
}
} |
| display\_text\_range | array | if the Tweet text extends beyond 140 characters.

"display\_text\_range": [
0,
142
] |
| verb | string | The type of action being taken by the user.
 Tweets, "post"
 Retweets, "share"
 Deleted Tweets, "delete"
 The verb is the proper way to distinguish between a Tweet and a true Retweet. However, this only applies to true retweets, and not modified or quoted Tweets, which don't use Twitter's Retweet functionality. For a description of AS verbsclick here.
For Deletes, note that only a limited number of fields will be included, as shown in the sample payload below.
"verb": "post" |
| postedTime | date (ISO 8601) | The time the action occurred, e.g. the time the Tweet was posted.

"postedTime": "2018-10-10T20:19:24.000Z" |
| generator | object | An object representing the utility used to post the Tweet. This will contain the name ("displayName") and a link ("link") for the source application generating the Tweet.
"generator": {
"displayName": "Twitter Web Client",
"link": "http://twitter.com"
} |
| provider | object | A JSON object representing the provider of the activity. This will contain an objectType ("service"), the name of the provider ("displayName"), and a link to the provider's website ("link").
"provider":
{
"objectType": "service",
"displayName": "Twitter",
"link": "http://www.twitter.com"
} |
| link | string | A Permalink for the tweet.
"link": "http://twitter.com/TwitterAPI/statuses/1050118621198921728" |
| body | string | The tweet text.
In Retweets, note that Twitter modifies the value of the body at the root level by adding "RT @username" at the beginning, and by truncating the original text and adding an ellipsis at the end. Thus, for Retweets, your app should look at the object.body to ensure that it is extracting the non-modified text of the original Tweet (being retweeted).
"body": "With Cardiff, Crystal Palace, and Hull City joining the EPL from the Championship it will be a great relegation battle at the end." |
| display\_text\_range | array | Describes the range of characters within the body text that indicates the displayed Tweet. Tweets with leading @mentions will start at more than 0 and Tweets with attached media or that extened beyond 140 characters will indicate the display\_text\_range in the long\_object.
"display\_text\_range": [
14,
42
]
or
"long\_object": {
"display\_text\_range": [
0,
277
]... |
| actor | object | An object representing the twitter user who tweeted. The Actor Object refers to a Twitter User, and contains all metadata relevant to that user.
 Seeactor object details |
| inReplyTo | object | A JSON object referring to the Tweet being replied to, if applicable. Contains a link to the Tweet.
"inReplyTo":
{
"link": "http:\/\/twitter.com\/GOP\/statuses\/349573991561838593"
} |
| location | object | A JSON object representing the Twitter "Place" where the tweet was created. This is an object passed through from the Twitter platform.
 Seelocation object |
| twitter\_entities | object | The entities object from Twitter's data format which contains lists of urls, mentions and hashtags. Please reference the Twitter documentation on Entities here Note that in Retweets, Twitter may truncate the values of entities that it extracts at the root level. So, for Retweets, your app should look at object.twitter\_entities to ensure that you are using non-truncated values.
See twitter\_entities object details |
| twitter\_extended\_entities | object | An object from Twitter's native data format containing "media". This will be present for any Tweet where the twitter\_entities object has data present in the "media" field, and will include multiple photos where present in the post. Note that this is the correct location to retrieve media information for multi-photo posts.
Multiple photos are represented by comma-separated JSON objects within the "media" array.
See twitter\_extended\_entities object details |
| gnip | object | An object added to the activity payload to indicate the matching rules, and added enriched data based on enrichments active on the stream or product.
See gnip object details |
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

### 
Additional Tweet attributes

| Attribute | Type | Description |
| --- | --- | --- |
| twitter\_lang | string |  |
| favoritesCount | int | *Nullable.* Indicates approximately how many times this Tweet has been liked by Twitter users.
"favoritesCount":298 |
| 
retweetCount | int | Number of times this Tweet has been retweeted. Example:
"retweetCount":153 |

### Deprecated Attributes

| Field | Type | Description |
| --- | --- | --- |
| geo | object | Point location where the Tweet was created. |
| twitter\_filter\_level | string | Deprecated field left in for non breaking change |

### 

### 

### Nested Tweet activity obejcts

In several cases, a Tweet object will included other nested Tweets.  If you are working with nested objects, then that JSON payload will contain multiple objects, and each Tweet object may contain its own objects. The root-level object will contain information on the type of action taken, i.e. whether it is a Retweet or a Quote Tweet, and may also contain an object that describes the 'original' Tweet being shared. Extended Tweets will include a nested extended object that extends beyond 140 characters, which was used to prevent breaking changes when the update was made in 2017. Each nested object dictionary is described below.

#### Retweets

Activity streams format of Retweets includes a nested object with the type "activity" and the verb "note" to represent the original Tweet being Retweeted.

```
      {
	"id": "tag:search.twitter.com,2005:222222222222",
	"objectType": "activity",
	"verb": "share",
	"body": "RT @TheOriginalTweeter: Coffee and art ☕️",
	"actor": {
		"displayName": "TheRetweeter"
	},
	"object": {
		"id": "tag:search.twitter.com,2005:11111111111",
		"objectType": "activity",
		"verb": "post",
		"body": "Coffee and art ☕️",
		"actor": {
			"displayName": "TheOriginalTweeter"
		},
		"object": {
			"objectType": "note",
			"id": "object:search.twitter.com,2005:11111111111",
			"summary": "Coffee and art ☕️",
			"link": "http://twitter.com/originaltweeter/statuses/11111111111",
			"postedTime": "2020-12-04T11:00:01.000Z"
		},
		"twitter_entities": {},
		"twitter_extended_entities": {}
	},
	"twitter_entities": {},
	"twitter_extended_entities": {},
	"gnip": {}
}
```

Code copied to clipboard

#### Twitter quoted status

Activity streams format embeded quote Tweets

```
      {
	"id": "tag:search.twitter.com,2005:222222222222",
	"objectType": "activity",
	"verb": "post",
	"body": "Quoting a Tweet: https://t.co/mxiFJ59FlB",
	"actor": {
		"displayName": "TheQuoter2"
	},
	"object": {
		"objectType": "note",
		"id": "object:search.twitter.com,2005:111111111",
		"summary": "https://t.co/mxiFJ59FlB"
	},
	"twitter_entities": {},
	"twitter_extended_entities": {},
	"gnip": {},
	"twitter_quoted_status": {
		"id": "tag:search.twitter.com,2005:111111111",
		"objectType": "activity",
		"verb": "post",
		"body": "console.log('Happy birthday, JavaScript!');",
		"actor": {
			"displayName": "TheOriginalTweeter"
		},
		"object": {
			"objectType": "note",
			"id": "object:search.twitter.com,2005:111111111"
		},
		"twitter_entities": {}
	}
}
```

Code copied to clipboard

Retweeted Quote Tweet:

```
          {
    	"id": "tag:search.twitter.com,2005:1293612267087384577",
    	"objectType": "activity",
    	"verb": "share",
    	"postedTime": "2020-08-12T18:16:13.000Z",
    	"generator": {},
    	"provider": {},
    	"link": "http://twitter.com/TwitterDev/statuses/1293612267087384577",
    	"body": "RT @compston: So excited to make this first set of endpoints available - many more to come before we're done. The @TwitterDev #DevRel team…",
    	"actor": {},
    	"object": {},
    	"favoritesCount": 0,
    	"twitter_entities": {},
    	"twitter_lang": "en",
    	"retweetCount": 13,
    	"gnip": {},
    	"twitter_filter_level": "low",
    	"twitter_quoted_status": {}
    }
```

Code copied to clipboard

### Long object

Activity streams format of the extended\_tweet

```
      {
  "id": "tag:search.twitter.com,2005:1050118621198921728",
  "objectType": "activity",
  "verb": "post",
  "postedTime": "2018-10-10T20:19:24.000Z",
  "generator": {
    "displayName": "Twitter Web Client",
    "link": "http://twitter.com"
  },
  "provider": {
    "objectType": "service",
    "displayName": "Twitter",
    "link": "http://www.twitter.com"
  },
  "link": "http://twitter.com/TwitterAPI/statuses/1050118621198921728",
  "body": "To make room for more expression, we will now count all emojis as equal—including those with gender‍‍‍ ‍‍and skin t… https://t.co/MkGjXf9aXm",
  "long_object": {
    "body": "To make room for more expression, we will now count all emojis as equal—including those with gender‍‍‍ ‍‍and skin tone modifiers 👍🏻👍🏽👍🏿. This is now reflected in Twitter-Text, our Open Source library. \n\nUsing Twitter-Text? See the forum post for detail: https://t.co/Nx1XZmRCXA",
    "display_text_range": [
      0,
      277
    ],
    "twitter_entities": {see twitter_entities object},
  "actor": {see actor object},
  "object": {
    "objectType": "note",
    "id": "object:search.twitter.com,2005:1050118621198921728",
    "summary": "To make room for more expression, we will now count all emojis as equal—including those with gender‍‍‍ ‍‍and skin t… https://t.co/MkGjXf9aXm",
    "link": "http://twitter.com/TwitterAPI/statuses/1050118621198921728",
    "postedTime": "2018-10-10T20:19:24.000Z"
  },
  "favoritesCount": 298,
  "twitter_entities": {see twitter_entities object},
  "twitter_lang": "en",
  "retweetCount": 153,
  "gnip": {see gnip object},
  "twitter_filter_level": "low"
}
```

Code copied to clipboard

### Next Steps

Explore the other nested objects of this format:

* Review actor object
* Review location object
* Review twitter\_entities object
* See migration guide from Activity Streams to Twitter API v2 format

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