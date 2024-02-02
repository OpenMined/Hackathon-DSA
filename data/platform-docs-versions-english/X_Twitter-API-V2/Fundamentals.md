Introduction

Across the Twitter API endpoints, there are a variety of objects available to request such as Tweets and users. Each GET endpoint will have a top-level resource and object, such as Tweets in [recent search](https://developer.twitter.com/en/docs/twitter-api/tweets/search/introduction.html) and [filtered stream](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/introduction.html), and users in [users lookup](https://developer.twitter.com/en/docs/twitter-api/users/lookup/introduction.html).

To see each object and it's included fields, please visit the following:

* [Tweets](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet)
* [Users](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user)
* [Spaces](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/space)
* [Lists](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/list)
* [Media](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/media)
* [Polls](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/poll)
* [Places](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/place)  
      
      
    

### Expanded objects

Additional objects related to the top-level object, such as media, place, poll, author (user) of the Tweet, and user's pinned-Tweet are available as expansions, which you can request using the [expansions](https://developer.twitter.com/en/docs/twitter-api/expansions.html) query parameter.   
 

### Fields: defaults and requesting additional fields

If you make a request without any [fields](https://developer.twitter.com/en/docs/twitter-api/fields.html) parameters, you will receive just a few default fields for your top-level object and any expansion objects. For example, Tweets will return just the id and text of a Tweet by default. If you would like to request additional fields, such as the Tweet created\_at or lang fields, you will have to use the fields parameters.   
 

### Key fields

Other useful fields that you should expect in the Twitter API v2 data format:

* [Metrics](https://developer.twitter.com/en/docs/twitter-api/metrics.html) available in the Tweet, user, Spaces, lists objects
* [Annotation](https://developer.twitter.com/en/docs/twitter-api/annotations.html) topics available in the Tweet payload  
    
* A new [conversation\_id](https://developer.twitter.com/en/docs/twitter-api/conversation-id) field to help you track Tweets included in a conversation
* A new reply\_settings field to help you understand who has the ability to reply to specific Tweets  
     

### Migrating to the Twitter API v2 data format

Interested in learning more about how the Twitter API v2 data format compares to standard, premium, or enterprises' formats? Check out our data format comparison guides:

* [Standard v1.1 Native format to Twitter API v2 format migration guide](https://developer.twitter.com/en/docs/twitter-api/migrate/data-formats/standard-v1-1-to-v2)
* [Native Enriched to Twitter API v2 format migration guide](https://developer.twitter.com/en/docs/twitter-api/migrate/data-formats/native-enriched-to-v2)
* [Activity Streams to Twitter API v2 format migration guide](https://developer.twitter.com/en/docs/twitter-api/migrate/data-formats/activity-streams-to-v2)

Tweet object

Tweet
-----

Tweets are the basic building block of all things Twitter. The Tweet object has a long list of ‘root-level’ fields, such as `id`, `text`, and `created_at`. Tweet objects are also the ‘parent’ object to several child objects including `user`, `media`, `poll`, and `place`. Use the field parameter `tweet.fields` when requesting these root-level fields on the Tweet object.

The Tweet object that can be found and expanded in the user resource. Additional Tweets related to the requested Tweet can also be found and expanded in the Tweet resource. The object is available for expansion with `?expansions=pinned_tweet_id` in the user resource or `?expansions=referenced_tweets.id` in the Tweet resource to get the object with only default fields. Use the expansion with the field parameter: `tweet.fields` when requesting additional fields to complete the object.  
 

| Field value | Type | Description | How it can be used |
| --- | --- | --- | --- |
| id (default) | string | The unique identifier of the requested Tweet.<br><br>`"id": "1050118621198921728"` | Use this to programmatically retrieve a specific Tweet. |
| text (default) | string | The actual UTF-8 text of the Tweet. See [twitter-text](https://github.com/twitter/twitter-text/) for details on what characters are currently considered valid.<br><br>`"text": "To make room for more expression, we will now count all emojis as equal—including those with gender‍‍‍ ‍‍and skin tone modifiers 👍🏻👍🏽👍🏿. This is now reflected in Twitter-Text, our Open Source library. \n\nUsing Twitter-Text? See the forum post for detail: https://t.co/Nx1XZmRCXA"` | Keyword extraction and sentiment analysis/classification. |
| edit\_history\_tweet\_ids (default) | object | Unique identifiers indicating all versions of a Tweet. For Tweets with no edits, there will be one ID. For Tweets with an edit history, there will be multiple IDs, arranged in ascending order reflecting the order of edits. The most recent version is the last position of the array.  <br>`"edit_history_tweet_ids":`<br><br>  `[`<br><br>  `"1584717154800521216"`<br><br>`]` | Use this information to find the edit history of a Tweet. |
| attachments | object | Specifies the type of attachments (if any) present in this Tweet.<br><br>`"attachments": {       "poll_ids": [           "1199786642468413448"       ]   }`<br><br>`"attachments": {       "media_keys": [           "3_1136048009270239232"       ]   }` | Understanding the objects returned for requested expansions |
| author\_id | string | The unique identifier of the User who posted this Tweet.<br><br>`"author_id": "2244994945"` | Hydrating User object, sharing dataset for peer review |
| context\_annotations | array | Contains context annotations for the Tweet.<br><br>`"context_annotations": [`<br><br>    `{`<br><br>        `"domain": {`<br><br>            `"id": "65",`<br><br>            `"name": "Interests and Hobbies Vertical",`<br><br>            `"description": "Top level interests and hobbies groupings, like Food or Travel"            },`<br><br>        `"entity": {`<br><br>            `"id": "834828264786898945",`<br><br>            `"name": "Drinks",`<br><br>            `"description": "Drinks"`<br><br>        `}`<br><br>    `},`<br><br>    `{`<br><br>        `"domain": {`<br><br>            `"id": "66",`<br><br>            `"name": "Interests and Hobbies Category",`<br><br>            `"description": "A grouping of interests and hobbies entities, like Novelty Food or Destinations"            },`<br><br>        `"entity": {`<br><br>            `"id": "834828445238431744",`<br><br>            `"name": "Generic Drinks",`<br><br>            `"description": "Generic Drinks"`<br><br>        `}`<br><br>    `}`<br><br>`]` | Entity recognition/extraction, topical analysis |
| conversation\_id | string | The Tweet ID of the original Tweet of the conversation (which includes direct replies, replies of replies).<br><br>`"conversation_id": "1050118621198921728"` | Use this to reconstruct the conversation from a Tweet. |
| created\_at | date (ISO 8601) | Creation time of the Tweet.<br><br>`"created_at": "2019-06-04T23:12:08.000Z"` | This field can be used to understand when a Tweet was created and used for time-series analysis etc. |
| edit\_controls | object | When present, this indicates how much longer the Tweet can be edited and the number of remaining edits. Tweets are only editable for the first 30 minutes after creation and can be edited up to five times.  <br>  <br>`"edit_controls": {`<br><br>  `"edits_remaining": 5,`<br><br>  `"is_edit_eligible": true,`<br><br>  `"editable_until": "2022-10-25T01:53:06.000Z"`<br><br>`}` | Use this to determine if a Tweet is eligible for editing. |
| entities | object | Entities that have been parsed out of the text of the Tweet. Additionally, see entities in Twitter Objects.<br><br>`"entities": {       "annotations": [           {              "start": 144,              "end": 150,              "probability": 0.626,              "type": "Product",              "normalized_text": "Twitter"           }       ],      "cashtags": [           {               "start": 18,               "end": 23,               "tag": "twtr"           }       ],       "hashtags": [           {               "start": 0,               "end": 17,               "tag": "blacklivesmatter"           }       ],       "mentions": [           {               "start": 24,               "end": 35,               "tag": "TwitterDev"           }       ],       "urls": [           {              "start": 44,              "end": 67,              "url": "https://t.co/crkYRdjUB0",              "expanded_url": "https://twitter.com",              "display_url": "twitter.com",              "status": "200",              "title": "bird",              "description": "From breaking news and entertainment to sports and politics, get the full story with all the live commentary.",               "unwound_url": "https://twitter.com"           }       ]   }` | Entities are JSON objects that provide additional information about hashtags, urls, user mentions, and cashtags associated with a Tweet. Reference each respective entity for further details.<br><br>Please note that all start indices are inclusive. The majority of end indices are exclusive, except for entities.annotations.end, which is currently inclusive. We will be changing this to exclusive with our v3 bump since it is a breaking change. |
| in\_reply\_to\_user\_id | string | If the represented Tweet is a reply, this field will contain the original Tweet’s author ID. This will not necessarily always be the user directly mentioned in the Tweet.<br><br>`"in_reply_to_user_id": "2244994945"` | Use this to determine if this Tweet was in reply to another Tweet. |
| lang | string | Language of the Tweet, if detected by Twitter. Returned as a BCP47 language tag.<br><br>`"lang": "en"` | Classify Tweets by spoken language. |
| non\_public\_metrics | object | Non-public engagement metrics for the Tweet at the time of the request. <br><br>Requires user context authentication.<br><br>`"non_public_metrics": {         "impression_count": 99         "url_link_clicks": 37         "user_profile_clicks": 22    }` | Use this to determine the total number of impressions generated for the Tweet. |
| organic\_metrics | object | Engagement metrics, tracked in an organic context, for the Tweet at the time of the request.<br><br>Requires user context authentication.<br><br>`"organic_metrics": {        "impression_count": 3880,        "like_count": 8,        "reply_count": 0,        "retweet_count": 4        "url_link_clicks": 3        "user_profile_clicks": 2   }` | Use this to measure organic engagement for the Tweet. |
| possibly\_sensitive | boolean | This field indicates content may be recognized as sensitive. The Tweet author can select within their own account preferences and choose “Mark media you tweet as having material that may be sensitive” so each Tweet created after has this flag set.<br><br>This may also be judged and labeled by an internal Twitter support agent.<br><br>`"possibly_sensitive": false` | Studying circulation of certain types of content. |
| promoted\_metrics | object | Engagement metrics, tracked in a promoted context, for the Tweet at the time of the request.<br><br>Requires user context authentication.<br><br>`"promoted_metrics": {         "impression_count": 1082,         "like_count": 187,         "reply_count": 6,         "retweet_count": 25         "url_link_clicks": 30         "user_profile_clicks": 2    }` | Use this to measure engagement for the Tweet when it was promoted. |
| public\_metrics | object | Public engagement metrics for the Tweet at the time of the request.<br><br>`"public_metrics" : {            "retweet_count": 8,            "reply_count": 2,            "like_count": 39,            "quote_count": 1    }` | Use this to measure Tweet engagement. |
| referenced\_tweets | array | A list of Tweets this Tweet refers to. For example, if the parent Tweet is a Retweet, a Retweet with comment (also known as Quoted Tweet) or a Reply, it will include the related Tweet referenced to by its parent.<br><br>`"referenced_tweets": [          {              "type": "replied_to",              "id": "1242125486844604425"          }      ]`<br><br>  <br>`` "referenced_tweets": [          {              "type": "quoted",              "id": "1265712391578214400"          }      ]`   ` ``<br><br>`` `   ` `` | This field can be used to understand conversational aspects of retweets etc. |
| reply\_settings | string | Shows you who can reply to a given Tweet. Fields returned are "everyone", "mentioned\_users", and "followers".  <br>`   "reply_settings": "everyone"` | This field allows you to determine whether conversation reply settings have been set for the Tweet and if so, what settings have been set. |
| source | string | The name of the app the user Tweeted from.<br><br>`"source": "Twitter Web App"` | Determine if a Twitter user posted from the web, mobile device, or other app. |
| withheld | object | When present, contains withholding details for [withheld content](https://help.twitter.com/en/rules-and-policies/tweet-withheld-by-country).<br><br>`"withheld": {          "copyright": false,          "country_codes": [             "IN"          ]      }` |     |

###   
Retrieving a Tweet object

#### Sample Request

In the following request, we are requesting fields for the Tweet on the [Tweets lookup](https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/introduction.html) endpoint. Be sure to replace `$BEARER_TOKEN` with your own generated [Bearer Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens).  
 

      `curl --request GET 'https://api.twitter.com/2/tweets?ids=1212092628029698048&tweet.fields=attachments,author_id,context_annotations,created_at,entities,geo,id,in_reply_to_user_id,lang,possibly_sensitive,public_metrics,referenced_tweets,source,text,withheld&expansions=referenced_tweets.id' --header 'Authorization: Bearer $BEARER_TOKEN'`
    

**Sample Response** 

      `{   "data": [     {       "text": "We believe the best future version of our API will come from building it with YOU. Here’s to another great year with everyone who builds on the Twitter platform. We can’t wait to continue working with you in the new year. https://t.co/yvxdK6aOo2",       "edit_history_tweet_ids": [         "1212092628029698048"       ],       "lang": "en",       "source": "Twitter Web App",       "in_reply_to_user_id": "2244994945",       "entities": {         "urls": [           {             "start": 222,             "end": 245,             "url": "https://t.co/yvxdK6aOo2",             "expanded_url": "https://twitter.com/LovesNandos/status/1211797914437259264/photo/1",             "display_url": "pic.twitter.com/yvxdK6aOo2",             "media_key": "16_1211797899316740096"           }         ],         "annotations": [           {             "start": 42,             "end": 44,             "probability": 0.5359,             "type": "Other",             "normalized_text": "API"           },           {             "start": 144,             "end": 150,             "probability": 0.9832,             "type": "Other",             "normalized_text": "Twitter"           }         ]       },       "author_id": "2244994945",       "referenced_tweets": [         {           "type": "replied_to",           "id": "1212092627178287104"         }       ],       "id": "1212092628029698048",       "public_metrics": {         "retweet_count": 7,         "reply_count": 3,         "like_count": 38,         "quote_count": 1       },       "context_annotations": [         {           "domain": {             "id": "29",             "name": "Events [Entity Service]",             "description": "Real world events. "           },           "entity": {             "id": "1186637514896920576",             "name": " New Years Eve"           }         },         {           "domain": {             "id": "29",             "name": "Events [Entity Service]",             "description": "Real world events. "           },           "entity": {             "id": "1206982436287963136",             "name": "Happy New Year: It’s finally 2020 everywhere!",             "description": "Catch fireworks and other celebrations as people across the globe enter the new year.\nPhoto via @GettyImages "           }         },         {           "domain": {             "id": "119",             "name": "Holiday",             "description": "Holidays like Christmas or Halloween"           },           "entity": {             "id": "1186637514896920576",             "name": " New Years Eve"           }         },         {           "domain": {             "id": "119",             "name": "Holiday",             "description": "Holidays like Christmas or Halloween"           },           "entity": {             "id": "1206982436287963136",             "name": "Happy New Year: It’s finally 2020 everywhere!",             "description": "Catch fireworks and other celebrations as people across the globe enter the new year.\nPhoto via @GettyImages "           }         },         {           "domain": {             "id": "30",             "name": "Entities [Entity Service]",             "description": "Entity Service top level domain, every item that is in Entity Service should be in this domain"           },           "entity": {             "id": "781974596752842752",             "name": "Services"           }         },         {           "domain": {             "id": "47",             "name": "Brand",             "description": "Brands and Companies"           },           "entity": {             "id": "10045225402",             "name": "Twitter"           }         },         {           "domain": {             "id": "131",             "name": "Unified Twitter Taxonomy",             "description": "A taxonomy of user interests. "           },           "entity": {             "id": "10045225402",             "name": "Twitter"           }         },         {           "domain": {             "id": "131",             "name": "Unified Twitter Taxonomy",             "description": "A taxonomy of user interests. "           },           "entity": {             "id": "847868745150119936",             "name": "Family & relationships",             "description": "Hobbies and interests"           }         },         {           "domain": {             "id": "131",             "name": "Unified Twitter Taxonomy",             "description": "A taxonomy of user interests. "           },           "entity": {             "id": "1196446161223028736",             "name": "Social media"           }         },         {           "domain": {             "id": "29",             "name": "Events [Entity Service]",             "description": "Real world events. "           },           "entity": {             "id": "1206982436287963136",             "name": "Happy New Year: It’s finally 2020 everywhere!",             "description": "Catch fireworks and other celebrations as people across the globe enter the new year.\nPhoto via @GettyImages "           }         },         {           "domain": {             "id": "119",             "name": "Holiday",             "description": "Holidays like Christmas or Halloween"           },           "entity": {             "id": "1206982436287963136",             "name": "Happy New Year: It’s finally 2020 everywhere!",             "description": "Catch fireworks and other celebrations as people across the globe enter the new year.\nPhoto via @GettyImages "           }         }       ],       "created_at": "2019-12-31T19:26:16.000Z",       "attachments": {         "media_keys": [           "16_1211797899316740096"         ]       },       "possibly_sensitive": false     }   ],   "includes": {     "tweets": [       {         "text": "These launches would not be possible without the feedback you provided along the way, so THANK YOU to everyone who has contributed your time and ideas. Have more feedback? Let us know ⬇️ https://t.co/Vxp4UKnuJ9",         "edit_history_tweet_ids": [           "1212092627178287104"         ],         "lang": "en",         "source": "Twitter Web App",         "in_reply_to_user_id": "2244994945",         "entities": {           "urls": [             {               "start": 187,               "end": 210,               "url": "https://t.co/Vxp4UKnuJ9",               "expanded_url": "https://twitterdevfeedback.uservoice.com/forums/921790-twitter-developer-labs",               "display_url": "twitterdevfeedback.uservoice.com/forums/921790-…",               "status": 200,               "title": "Updates on our feedback channels",               "description": "We build our developer platform in the open, with your input and feedback. Over the past year, hearing directly from you and the users of your apps has helped us build developer products that cater to the use case you helped us identify. We want to make this the way we build products, and moving forward, we are consolidating our feedback channels. Meeting you where you are Effective today, we are going to retire our UserVoice feedback channel in favor of more frequent direct engagements with y...",               "unwound_url": "https://twittercommunity.com/t/updates-on-our-feedback-channels/169706"             }           ]         },         "author_id": "2244994945",         "referenced_tweets": [           {             "type": "replied_to",             "id": "1212092626247110657"           }         ],         "id": "1212092627178287104",         "public_metrics": {           "retweet_count": 2,           "reply_count": 1,           "like_count": 19,           "quote_count": 0         },         "created_at": "2019-12-31T19:26:16.000Z",         "possibly_sensitive": false       }     ]   } }`

User object

User
----

The user object contains Twitter user account metadata describing the referenced user. The user object is the primary object returned in the [users lookup](https://developer.twitter.com/en/docs/twitter-api/users/lookup/introduction.html) endpoint. When requesting additional user fields on this endpoint, simply use the fields parameter `user.fields`.

The user object can also be found as a child object and expanded in the Tweet object. The object is available for expansion with `?expansions=author_id` or `?expansions=in_reply_to_user_id` to get the condensed object with only default fields. Use the expansion with the field parameter: `user.fields` when requesting additional fields to complete the object.  
 

| Field value | Type | Description | How it can be used |
| --- | --- | --- | --- |
| id (default) | string | The unique identifier of this user.<br><br>`"id": "2244994945"` | Use this to programmatically retrieve information about a specific Twitter user. |
| name (default) | string | The name of the user, as they’ve defined it on their profile. Not necessarily a person’s name. Typically capped at 50 characters, but subject to change.<br><br>`"name": "Twitter Dev"` |     |
| username (default) | string | The Twitter screen name, handle, or alias that this user identifies themselves with. Usernames are unique but subject to change. Typically a maximum of 15 characters long, but some historical accounts may exist with longer names.<br><br>`"username": "TwitterDev"` |     |
| created\_at | date (ISO 8601) | The UTC datetime that the user account was created on Twitter.<br><br>`"created_at": "2013-12-14T04:35:55.000Z"` | Can be used to determine how long a someone has been using Twitter |
| description | string | The text of this user's profile description (also known as bio), if the user provided one.<br><br>`"description": "The voice of Twitter's #DevRel team, and your official source for updates, news, & events about Twitter's API. \n\n#BlackLivesMatter"` |     |
| entities | object | Contains details about text that has a special meaning in the user's description.<br><br>`"entities": {          "url": {              "urls": [                  {                      "start": 0,                      "end": 23,                      "url": "https://t.co/3ZX3TNiZCY",                      "expanded_url": "/content/developer-twitter/en/community",                      "display_url": "developer.twitter.com/en/community"                  }              ]          },          "description": {              "urls": [                  {                      "start": 0,                      "end": 23,                      "url": "https://t.co/3ZX3TNiZCY",                      "expanded_url": "/content/developer-twitter/en/community",                      "display_url": "developer.twitter.com/en/community"                  },              "hashtags": [                  {                      "start": 23,                      "end": 30,                      "tag": "DevRel"                  },                  {                      "start": 113,                      "end": 130,                      "tag": "BlackLivesMatter"                  },              "mentions": [                  {                      "start": 0,                      "end": 10,                      "tag": "TwitterDev"                  },              "cashtags": [                  {                      "start": 12,                      "end": 16,                      "tag": "twtr"                  }              ]          }      }` | Entities are JSON objects that provide additional information about hashtags, urls, user mentions, and cashtags associated with the description. Reference each respective entity for further details.<br><br>All user start indices are inclusive, while all user end indices are exclusive. |
| location | string | The location specified in the user's profile, if the user provided one. As this is a freeform value, it may not indicate a valid location, but it may be fuzzily evaluated when performing searches with location queries.<br><br>`"location": "127.0.0.1"` |     |
| pinned\_tweet\_id | string | Unique identifier of this user's pinned Tweet.<br><br>`"pinned_tweet_id": "1255542774432063488"` | Determine the Tweet pinned to the top of the user’s profile. Can potentially be used to determine the user’s language. |
| profile\_image\_url | string | The URL to the profile image for this user, as shown on the user's profile.<br><br>`"profile_image_url": "https://pbs.twimg.com/profile_images/1267175364003901441/tBZNFAgA_normal.jpg"` | Can be used to download this user's profile image. |
| protected | boolean | Indicates if this user has chosen to protect their Tweets (in other words, if this user's Tweets are private).<br><br>`"protected": false` |     |
| public\_metrics | object | Contains details about activity for this user.<br><br>`"public_metrics": {             "followers_count": 507902,             "following_count": 1863,             "tweet_count": 3561,             "listed_count": 1550         }` | Can potentially be used to determine a Twitter user’s reach or influence, quantify the user’s range of interests, and the user’s level of engagement on Twitter. |
| url | string | The URL specified in the user's profile, if present.<br><br>`"url": "https://t.co/3ZX3TNiZCY"` | A URL provided by a Twitter user in their profile. This could be a homepage, but is not always the case. |
| verified | boolean | Indicates if this user is a verified Twitter User.<br><br>`"verified": true` | Indicates whether or not this Twitter user has a verified account. A verified account lets people know that an account of public interest is authentic. |
| withheld | object | Contains withholding details for [withheld content](https://help.twitter.com/en/rules-and-policies/tweet-withheld-by-country), if applicable. |     |

### Retrieving a user object

#### Sample Request

In the following request, we are requesting fields for the user on the [users lookup](https://developer.twitter.com/en/docs/twitter-api/users/lookup/introduction.html) endpoint. Be sure to replace `$BEARER_TOKEN` with your own generated [Bearer Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens).  
 

      `curl --request GET 'https://api.twitter.com/2/users?ids=2244994945&user.fields=created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,url,username,verified,withheld&expansions=pinned_tweet_id' --header 'Authorization: Bearer $BEARER_TOKEN'`
    

####   
Sample Response  
 

      `{     "data": [         {             "id": "2244994945",             "name": "Twitter Dev",             "username": "TwitterDev",             "location": "127.0.0.1",             "entities": {                 "url": {                     "urls": [                         {                             "start": 0,                             "end": 23,                             "url": "https://t.co/3ZX3TNiZCY",                             "expanded_url": "/content/developer-twitter/en/community",                             "display_url": "developer.twitter.com/en/community"                         }                     ]                 },                 "description": {                     "hashtags": [                         {                             "start": 23,                             "end": 30,                             "tag": "DevRel"                         },                         {                             "start": 113,                             "end": 130,                             "tag": "BlackLivesMatter"                         }                     ]                 }             },             "verified": true,             "description": "The voice of Twitter's #DevRel team, and your official source for updates, news, & events about Twitter's API. \n\n#BlackLivesMatter",             "url": "https://t.co/3ZX3TNiZCY",             "profile_image_url": "https://pbs.twimg.com/profile_images/1267175364003901441/tBZNFAgA_normal.jpg",             "protected": false,             "pinned_tweet_id": "1255542774432063488",             "created_at": "2013-12-14T04:35:55.000Z"         }     ],     "includes": {         "tweets": [             {                 "id": "1255542774432063488",                 "text": "During these unprecedented times, what’s happening on Twitter can help the world better understand &amp; respond to the pandemic. \n\nWe're launching a free COVID-19 stream endpoint so qualified devs &amp; researchers can study the public conversation in real-time. https://t.co/BPqMcQzhId"             }         ]     } }`

Space object

Space
-----

Spaces allow expression and interaction via live audio conversations. The Space data dictionary contains relevant metadata about a Space; all the details are updated in real time.

User objects can found and expanded in the user resource. These objects are available for expansion by adding at least one of host\_ids, creator\_id, speaker\_ids, mentioned\_user\_ids to the expansions query parameter.

Unlike Tweets, Spaces are ephemeral and become unavailable after they end or when they are canceled by their creator. When your app handles Spaces data, you are responsible for returning the most up-to-date information, and must remove data that is no longer available from the platform. The [Spaces lookup endpoints](https://developer.twitter.com/en/docs/twitter-api/spaces/lookup/introduction) can help you ensure you respect the users’ expectations and intent.

| Field value | Type | Description | How it can be used |
| --- | --- | --- | --- |
| id (default) | string | The unique identifier of the requested Space.<br><br>`"id": "1zqKVXPQhvZJB"` | Uniquely identify a Space returned in the response. |
| state (default) | string | Indicates if the Space has started or will start in the future, or if it has ended.<br><br>`"state": "live"` | Filter live or scheduled Spaces. |
| created\_at | date (ISO 8601) | Creation time of this Space.<br><br>`"created_at": "2021-07-04T23:12:08.000Z"` | Understand when a Space was first created and sort Spaces by creation time. |
| ended\_at | date (ISO 8601) | Time when the Space was ended. Only available for ended Spaces. <br><br>`"ended_at": "2021-07-04T00:11:44.000Z"` | Understand when a live Space ended in order to comput its runtime duration. |
| host\_ids | array | The unique identifier of the users who are hosting this Space.<br><br>`"host_ids": [`  <br>  `"2244994945",      "6253282"   ]` | Expand User objects, understand engagement. |
| lang | string | Language of the Space, if detected by Twitter. Returned as a BCP47 language tag.<br><br>`"lang": "en"` | Classify Spaces by inferred language. |
| is\_ticketed | boolean | Indicates is this is a ticketed Space.<br><br>`"is_ticketed": false` | Create user experiences to highlight content of interest. |
| invited\_user\_ids | array | The list of user IDs that were invited to join as speakers. Usually, users in this list are invited to speak via the Invite user option.<br><br>`"mentioned_user_ids": [     "2244994945",      "6253282"   ]` | Expand User objects, understand engagement. |
| participant\_count | integer | The current number of users in the Space, including Hosts and Speakers.<br><br>`"participant_count": 420` | Understand engagement, and create reports and visualizations for creators. |
| subscriber\_count | integer | The number of people who set a reminder to a Space.  <br>`"subscriber_count": 36` | Understand how many people are interested in attending the event. This metric is available for scheduled Spaces and Spaces scheduled in the past that are currently live. |
| scheduled\_start | date (ISO 8601) | Indicates the start time of a scheduled Space, as set by the creator of the Space. This field is returned only if the Space has been scheduled; in other words, if the field is returned, it means the Space is a scheduled Space.<br><br>`"scheduled_start": "2021-07-14T08:00:00.000Z"` | Integrate with calendar notifications, filter and sort Spaces by time. |
| speaker\_ids | array | The list of users who were speaking at any point during the Space. This list contains all the users in **invited\_user\_ids** in addition to any user who requested to speak and was allowed via the Add speaker option.<br><br>`"speaker_ids": [     "2244994945",      "6253282"   ]` | Expand User objects, understand engagement. |
| started\_at | date (ISO 8601) | Indicates the actual start time of a Space.<br><br>`"started_at": "2021-07-14T08:00:12.000Z"` | Determine start time of a Space. |
| title | string | The title of the Space as specified by the creator.<br><br>`"title": "Say hello to the Space data object!"` | Determine the title of a Space, understand referenced keywords, hashtags, and mentions. |
| topic\_ids | array | A list of IDs of the topics selected by the creator of the Space.<br><br>`"topic_ids": [     "2244994945",      "6253282"   ]` | Determine the title of a Space, understand referenced keywords, hashtags, and mentions. |
| updated\_at | date (ISO 8601) | Specifies the date and time of the last update to any of the Space's metadata, such as its title or scheduled time.  <br>`   "updated_at": "2021-07-11T14:44:44.000Z"` | Keep information up to date. |

###   
Retrieving a Space object

#### Sample Request

In the following request, we are requesting fields for the Space on the [Spaces lookup](https://developer.twitter.com/en/docs/twitter-api/spaces/lookup/introduction.html) endpoint. Be sure to replace `$BEARER_TOKEN` with your own generated [Bearer Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens).  
 

      `curl "https://api.twitter.com/2/spaces/1DXxyRYNejbKM?space.fields=created_at,creator_id,created_athost_ids,lang,is_ticketed,invited_user_ids,participant_count,scheduled_start,speaker_ids,started_at,state,title,updated_at&expansions=creator_id,host_ids,invited_user_ids,speaker_ids" --header "Authorization: Bearer $BEARER_TOKEN"`
    

**Sample Response** 

      `{     "data": {         "id": "1zqKVXPQhvZJB",         "state": "live",         "created_at": "2021-07-04T23:12:08.000Z",         "host_ids": [           "2244994945",           "6253282"         ],         "lang": "en",         "is_ticketed": false,         "invited_user_ids": [           "2244994945",           "6253282"         ],         "participant_count": 420,         "scheduled_start": "2021-07-14T08:00:00.000Z",         "speaker_ids": [           "2244994945",           "6253282"         ],                 "started_at": "2021-07-14T08:00:12.000Z",         "title": "Say hello to the Space data object!",         "updated_at": "2021-07-11T14:44:44.000Z"     },     "includes": {         "users": [             {                 "id": "2244994945",                 "name": "Twitter Dev",                 "username": "TwitterDev"            },            {             "id": "6253282",             "name": "Twitter API",             "username": "TwitterAPI"           }     ]     } }`

List object

List
----

The list object contains [Twitter Lists](https://help.twitter.com/en/using-twitter/twitter-lists) metadata describing the referenced List. The List object is the primary object returned in the List lookup endpoint. When requesting additional List fields on this endpoint, simply use the fields parameter `list.fields`.

At the moment, the List object cannot be found as a child object from any other data object. However, user objects can be found and expanded in the user resource. These objects are available for expansion by adding owner\_id to the expansions query parameter. Use the expansion with the field parameter: `list.fields` when requesting additional fields to complete the primary List object and user.fields to complete the expansion object.  
 

| Field value | Type | Description | How it can be used |
| --- | --- | --- | --- | --- |
| id (default) | string | The unique identifier of this List.<br><br>`"id": "2244994945"` | Use this to programmatically retrieve information about a specific Twitter List. |
| name (default) | string | The name of the List, as defined when creating the List. <br><br>`"name": "Twitter Lists"` |     |
| created\_at | date (ISO 8601) | The UTC datetime that the List was created on Twitter.<br><br>`"created_at": "2013-12-14T04:35:55.000Z"` | Can be used to determine how long a List has been on Twitter |
| description | string | A brief description to let users know about the List.<br><br>`"description": "People that are active members of the Bay area cycling community on Twitter."` |     |
| follower\_count | integer | Shows how many users follow this List,<br><br>"follower\_count": 198 |     |
| member\_count | integer | Shows how many members are part of this List.<br><br>"member\_count": 60 |     |
| private | boolean | Indicates if the List is private.<br><br>"private": false |     |
| owner\_id | string | Unique identifier of this List's owner.<br><br>`"owner_id": "1255542774432063488"` | Returns the List owner ID. Can potentially be used to find out if this specifc user owns any other Lists.<br><br>Can also be used to expand user objects. |     |

### Retrieving a user object

#### Sample Request

In the following request, we are requesting fields for the user on the [List lookup by ID](https://developer.twitter.com/en/docs/twitter-api/lists/list-lookup/introduction.html) endpoint. Be sure to replace `$BEARER_TOKEN` with your own generated [Bearer Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens).  
 

      `curl --request GET 'https://api.twitter.com/2/lists/1355797419175383040?list.fields=created_at,description,private,follower_count,member_count,owner_id&expansions=owner_id' --header 'Authorization: Bearer $BEARER_TOKEN'`
    

####   
Sample Response  
 

      `{   "data": {     "name": "Twitter Comms",     "member_count": 60,     "id": "1355797419175383040",     "private": false,     "description": "",     "follower_count": 198,     "owner_id": "257366942",     "created_at": "2021-01-31T08:37:48.000Z"   },   "includes": {     "users": [       {         "created_at": "2011-02-25T07:51:26.000Z",         "name": "Ashleigh Hay 🤸🏼‍♀️",         "id": "257366942",         "username": "shleighhay",         "verified": false       }     ]   } }`

Media object

Media
-----

Media refers to any image, GIF, or video attached to a Tweet. The media object is not a primary object on any endpoint, but can be found and expanded in the Tweet object. 

The object is available for expansion with `?expansions=attachments.media_keys` to get the condensed object with only default fields. Use the expansion with the field parameter: `media.fields` when requesting additional fields to complete the object.

| Field value | Type | Description | How it can be used |
| --- | --- | --- | --- |
| media\_key (default) | string | Unique identifier of the expanded media content.<br><br>`"media_key": "13_1263145212760805376"` | Can be used to programmatically retrieve media |
| type (default) | string | Type of content (animated\_gif, photo, video).<br><br>`"type": "video"` | Classify the media as a photo, GIF, or video |
| url | string | A direct URL to the media file on Twitter. | Returns a Media object with a URL field for photos |
| duration\_ms | integer | Available when type is video. Duration in milliseconds of the video.<br><br>`"duration_ms": 46947` |     |
| height | integer | Height of this content in pixels.<br><br>`"height": 1080` |     |
| non\_public\_metrics | object | Non-public engagement metrics for the media content at the time of the request. <br><br>Requires user context authentication.<br><br>`"non_public_metrics": {            "playback_0_count": 1561,            "playback_100_count": 116,            "playback_25_count": 559,            "playback_50_count": 305,            "playback_75_count": 183,          }` | Determine video engagement: how many users played through to each quarter of the video. |
| organic\_metrics | object | Engagement metrics for the media content, tracked in an organic context, at the time of the request. <br><br>Requires user context authentication.<br><br>`"organic_metrics": {            "playback_0_count": 1561,            "playback_100_count": 116,            "playback_25_count": 559,            "playback_50_count": 305,            "playback_75_count": 183,            "view_count": 629          }` | Determine organic media engagement. |
| preview\_image\_url | string | URL to the static placeholder preview of this content.<br><br>`"preview_image_url": "https://pbs.twimg.com/media/EYeX7akWsAIP1_1.jpg"` |     |
| promoted\_metrics | object | Engagement metrics for the media content, tracked in a promoted context, at the time of the request. <br><br>Requires user context authentication.<br><br>`"promoted_metrics": {            "playback_0_count": 259,            "playback_100_count": 15,            "playback_25_count": 113,            "playback_50_count": 57,            "playback_75_count": 25,            "view_count": 124          }` | Determine media engagement when the Tweet was promoted. |
| public\_metrics | object | Public engagement metrics for the media content at the time of the request.<br><br>`"public_metrics": {            "view_count": 6865141          }` | Determine total number of views for the video attached to the Tweet. |
| width | integer | Width of this content in pixels.<br><br>`"width": 1920` |     |
| alt\_text | string | A description of an image to enable and support accessibility. Can be up to 1000 characters long. Alt text can only be added to images at the moment. <br><br>"alt\_text": “Rugged hills along the Na Pali coast on the island of Kauai” | Can be used to provide a written description of an image in case a user is visually impaired. |
| variants | array | Each media object may have multiple display or playback variants, with different resolutions or formats<br><br>`"variants": [`<br><br>  `{        "bit_rate": 632000,        "content_type":"video/mp4",        "url": "https://video.twimg.com/ext_tw_video/1527322141724532740/pu/vid/320x568/lnBaR2hCqE-R_90a.mp4?tag=12"       }`<br><br> `]` |     |

### Retrieving a media object

#### Sample Request

In the following request, we are requesting fields for the media object attached to the Tweet on the [Tweet lookup](https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/introduction.html) endpoint. Since media is a child object of a Tweet, the `attachment.media_keys` expansion is required. Be sure to replace `$BEARER_TOKEN` with your own generated [Bearer Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens).  
 

      `curl --request GET 'https://api.twitter.com/2/tweets?ids=1263145271946551300&expansions=attachments.media_keys&media.fields=duration_ms,height,media_key,preview_image_url,public_metrics,type,url,width,alt_text' --header 'Authorization: Bearer $BEARER_TOKEN'`
    

**Sample Response** 

      `{     "data": [         {             "text": "Testing, testing...\n\nA new way to have a convo with exactly who you want. We’re starting with a small % globally, so keep your 👀 out to see it in action. https://t.co/pV53mvjAVT",             "id": "1263145271946551300",             "attachments": {                 "media_keys": [                     "13_1263145212760805376"                 ]             }         }     ],     "includes": {         "media": [             {                 "duration_ms": 46947,                 "type": "video",                 "height": 1080,                 "media_key": "13_1263145212760805376",                 "public_metrics": {                     "view_count": 6909260                 },                 "preview_image_url": "https://pbs.twimg.com/media/EYeX7akWsAIP1_1.jpg",                 "width": 1920             }         ]     } }`

Poll object

Poll
----

A poll included in a Tweet is not a primary object on any endpoint, but can be found and expanded in the Tweet object. 

The object is available for expansion with `?expansions=attachments.poll_ids` to get the condensed object with only default fields. Use the expansion with the field parameter: `poll.fields` when requesting additional fields to complete the object.

| Field value | Type | Description |
| --- | --- | --- |
| id (default) | string | Unique identifier of the expanded poll.<br><br>`"id": "1199786642791452673"` |
| options (default) | array | Contains objects describing each choice in the referenced poll.<br><br>`"options": [                      {                          "position": 1,                          "label": "“C Sharp”",                          "votes": 795                      },                      {                          "position": 2,                          "label": "“C Hashtag”",                          "votes": 156                      }                  ]` |
| duration\_minutes | integer | Specifies the total duration of this poll.<br><br>`"duration_minutes": 1440` |
| end\_datetime | date (ISO 8601) | Specifies the end date and time for this poll.<br><br>`"end_datetime": "2019-11-28T20:26:41.000Z"` |
| voting\_status | string | Indicates if this poll is still active and can receive votes, or if the voting is now closed.<br><br>`"voting_status": "closed"` |

### Retrieving a poll object

#### Sample Request

In the following request, we are requesting fields for the poll object attached to the Tweet on the [Tweets lookup](https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/introduction.html) endpoint. Since poll is a child object of a Tweet, the `attachments.poll_id` expansion is required. Be sure to replace `$BEARER_TOKEN` with your own generated [Bearer Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens).  
 

      `curl --request GET 'https://api.twitter.com/2/tweets?ids=1199786642791452673&expansions=attachments.poll_ids&poll.fields=duration_minutes,end_datetime,id,options,voting_status' --header 'Authorization: Bearer $BEARER_TOKEN'`
    

####   
Sample Response  
 

      `{     "data": [         {             "text": "C#",             "id": "1199786642791452673",             "attachments": {                 "poll_ids": [                     "1199786642468413448"                 ]             }         }     ],     "includes": {         "polls": [             {                 "id": "1199786642468413448",                 "voting_status": "closed",                 "duration_minutes": 1440,                 "options": [                     {                         "position": 1,                         "label": "“C Sharp”",                         "votes": 795                     },                     {                         "position": 2,                         "label": "“C Hashtag”",                         "votes": 156                     }                 ],                 "end_datetime": "2019-11-28T20:26:41.000Z"             }         ]     } }`

Place objects

Place
-----

The place tagged in a Tweet is not a primary object on any endpoint, but can be found and expanded in the Tweet resource. 

The object is available for expansion with `?expansions=geo.place_id` to get the condensed object with only default fields. Use the expansion with the field parameter: `place.fields` when requesting additional fields to complete the object.

| Field value | Type | Description | How it can be used |
| --- | --- | --- | --- |
| full\_name (default) | string | A longer-form detailed place name.<br><br>`"full_name": "Manhattan, NY"` | Classify a Tweet by a specific place name |
| id (default) | string | The unique identifier of the expanded place, if this is a point of interest tagged in the Tweet.<br><br>`"id": "01a9a39529b27f36"` | Use this to programmatically retrieve a place |
| contained\_within | array | Returns the identifiers of known places that contain the referenced place. |     |
| country | string | The full-length name of the country this place belongs to.<br><br>`"country": "United States"` | Classify a Tweet by country name |
| country\_code | string | The ISO Alpha-2 country code this place belongs to.<br><br>`"country_code": "US"` | Classify a Tweet by country code |
| geo | object | Contains place details in GeoJSON format.<br><br>`"geo": {        "type": "Feature",        "bbox": [              -74.026675,              40.683935,              -73.910408,              40.877483         ],         "properties": {}      }` |     |
| name | string | The short name of this place.<br><br>`"name": "Manhattan"` | Classify a Tweet by a specific place name |
| place\_type | string | Specified the particular type of information represented by this place information, such as a city name, or a point of interest.<br><br>`"place_type": "city"` | Classify a Tweet by a specific type of place |

###   
Retrieving a place object

#### Sample Request

In the following request, we are requesting fields for the place object attached to the Tweet on the [Tweets lookup](https://developer.twitter.com/en/docs/twitter-api/tweets/lookup) endpoint. Since place is a child object of a Tweet, the `geo.place_id` expansion is required. Be sure to replace `$BEARER_TOKEN` with your own generated [Bearer Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens).  
 

      `curl --request GET 'https://api.twitter.com/2/tweets?ids=1136048014974423040&expansions=geo.place_id&place.fields=contained_within,country,country_code,full_name,geo,id,name,place_type' --header 'Authorization: Bearer $BEARER_TOKEN'`
    

####   
Sample Response  
 

      `{     "data": [         {             "text": "We’re sharing a live demo of the new Twitter Developer Labs program, led by a member of our DevRel team, @jessicagarson #TapIntoTwitter https://t.co/ghv7f4dW5M",             "id": "1136048014974423040",             "geo": {                 "place_id": "01a9a39529b27f36"             }         }     ],     "includes": {         "places": [             {                 "geo": {                     "type": "Feature",                     "bbox": [                         -74.026675,                         40.683935,                         -73.910408,                         40.877483                     ],                     "properties": {}                 },                 "country_code": "US",                 "name": "Manhattan",                 "id": "01a9a39529b27f36",                 "place_type": "city",                 "country": "United States",                 "full_name": "Manhattan, NY"             }         ]     } }`

Direct Message events

Direct Message events
=====================

Direct Message (DM) conversations are made up of events. The Twitter API v2 currently supports three event types: MessageCreate, ParticipantsJoin, and ParticipantsLeave.

DM event objects are returned by the [Direct Message lookup](https://developer.twitter.com/en/docs/twitter-api/direct-messages/lookup/introduction) endpoints, and a MessageCreate event is created when Direct Messages are successfully created with the [Manage Direct Messages](https://developer.twitter.com/en/docs/twitter-api/direct-messages/manage/introduction) endpoints.

When requesting DM events, there are three default event object attributes, or fields, included: id, event\_type, and text. To receive additional event fields, use the [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter dm\_event.fields to select others. Other available event fields include the following: dm\_conversation\_id, created\_at, sender\_id, attachments, participant\_ids, and referenced\_tweets.

Several of these fields provide the IDs of other Twitter objects related to the Direct Message event:

* sender\_id - The ID of the account that sent the message, or who invited a participant to a group conversation
* partricipants\_ids - An array of account IDs. For ParticipantsJoin and ParticipantsLeave events this array will contain a single ID of the account that created the event
* attachments - Provides media IDs for content that has been uploaded to Twitter by the sender
* referenced\_tweets - If a Tweet URL is found in the text field, the ID of that Tweet is included in the response

The sender\_id, participant\_ids, referenced\_tweets.id, and attachments.media\_keys [expansions](https://developer.twitter.com/en/docs/twitter-api/expansions) are available to expand on these Twitter object IDs.

|     |     |     |     |
| --- | --- | --- | --- |
| **Field value** | **Type** | **Description** | **How it can be used** |
| id (default) | string | The unique identifier of the event.<br><br>"id": "1050118621198921728" | Use this to programmatically retrieve a specific conversation event (available with v1.1 endpoints). |
| event\_type (default) | string | Describes the type of event. Three types are currently supported: <br><br>* MessageCreate<br>    <br>* ParticipantsJoin<br>    <br>* ParticipantsLeave<br>    <br><br>"event\_type": "MessageCreate" | When retrieving a conversation's history, understanding when messages were created, and for group conversations, understanding when participants joined and left. All GET methods support filtering on specific event types with the event\_type= query parameter. . |
| text (default) | string | The actual UTF-8 text of the Direct Message. <br><br>"text": "Hello, just you!" | With chatbots, this can be used to analyze message contents and determining automated responses. Could be used to build conversation search features. |
| sender\_id | string | ID of the User creating the event. To expand this object in the response, include sender\_id as an expansion  and use the user.fields query parameter to specify User object attributes of interest.<br><br>"sender\_id": "906948460078698496" | Retrieve the User object of who created the MessageCreate or ParticipantsJoin event. |
| participant\_id | array (of strings) | IDs of the participants joining and leaving a group conversation. Also used when creating new group conversations. To expand this object in the response, include participant\_ids as an expansion and use the user.fields query parameter to specify User object attributes of interest.<br><br>"participant\_ids": \[<br><br>     "906948460078698496"<br><br>\] | Used to retrieve User objects for participants joining and leaving group conversations. |
| dm\_conversation\_id | string | The unique identifier of the conversation the event is apart of.<br><br>"dm\_conversation\_id": "1584988213961031680" | Use this to programmatically retrieve events from a conversation, and add Direct Messages to it. |
| created\_at | date (ISO 8601) | Creation time (UTC) of the Tweet.<br><br>"created\_at": "2019-06-04T23:12:08.000Z" | This field can be used to understand when a Direct Message was created or when conversation participants joined or left. |
| referenced\_tweets | array | ID for any Tweet mentioned in the Direct Message text. To expand this object in the response, include referenced\_tweets.id as an expansion and use the tweet.fields query parameter to specify Tweet object attributes of interest.<br><br>"referenced\_tweets": \[<br><br>    {<br><br>        "id": "1578868150510456833"<br><br>    }<br><br>\] | When Direct Messages reference a Tweet, these IDs can be used to lookup the Tweet's details. |
| attachments | object | For Direct Messages with attached Media, provides the media key of the uploaded content (photo, video, or GIF. To expand this object in the response, include attachments.media\_keys as an expansion and use the media.fields query parameter to specify media object attributes of interest. Currently, one attachment is supported. <br><br>"attachments": {<br><br>    "media\_keys": \[<br><br>        "3\_1136048009270239232"<br><br>    \]<br><br>} | Understanding the media objects attached to Direct Messages. |

Retrieving a Direct Message event object
----------------------------------------

### Sample Request

For this example, we will build a request that retrieves events associated with a one-to-one conversation. This request will return fundamental Direct Message event fields, along with additional fields for referenced Tweets and their authors. Let's build a query that asks for:

* Fundamental event attributes such as when it was created and what conversation it is part of (dm\_conversation).
* The account ID and description of who sent the Direct Message.
* The text of any referenced Tweet, and when it was posted.
* The account ID and description of any referenced Tweet author.

To return those attributes, your request query would include the following:

      `?dm_event.fields=id,sender_id,text,created_at,dm_conversation_id&expansions=sender_id,referenced_tweets.id&tweet.fields=created_at,text,author_id&user.fields=description`
    

      `curl --request GET 'https://api.twitter.com/2/dm_conversations/with/:participant_id/dm_events?tweet.fields=created_at,text,author_id&user.fields=description&expansions=sender_id,participant_ids,referenced_tweets.id&dm_event.fields=id,sender_id,text,participant_ids,created_at,'      --header 'Authorization: Bearer $BEARER_TOKEN'`
    

Be sure to replace $BEARER\_TOKEN with your own generated [Bearer Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens).

### Sample Response

      `{ 	"data": [{ 			"id": "1585047616894574596", 			"sender_id": "944480690", 			"text": "Hello, just you!", 			"created_at": "2022-10-25T23:16:15.000Z", 			"event_type": "MessageCreate", 			"dm_conversation_id": "944480690-906948460078698496" 		}, 		{ 			"id": "1581048670673260549", 			"sender_id": "944480690", 			"text": "Simple Tweet link: https://t.co/IYFbRIdXHg", 			"referenced_tweets": [{ 				"id": "1578900353814519810" 			}], 			"created_at": "2022-10-14T22:25:52.000Z", 			"event_type": "MessageCreate", 			"dm_conversation_id": "944480690-906948460078698496" 		}, 		{ 			"id": "1580705121553420292", 			"sender_id": "944480690", 			"text": "Adding a new 1-to-1 Direct Message.", 			"created_at": "2022-10-13T23:40:43.000Z", 			"event_type": "MessageCreate", 			"dm_conversation_id": "944480690-906948460078698496" 		} 	], 	"includes": { 		"users": [{ 				"name": "API Demos", 				"description": "Hosting TwitterDev integrations... @TwitterDev #DevRel", 				"id": "944480690", 				"username": "FloodSocial" 			}, 			{ 				"name": "the SnowBot", 				"description": "Home of the @TwitterDev SnowBot... Serving snow reports, snow photos, and snow research links... Chatbot is currently being remodeled for Twitter APIv2.", 				"id": "906948460078698496", 				"username": "SnowBotDev" 			} 		], 		"tweets": [{ 				"text": "Feeling kind of bad that I didn’t wish everybody a happy new Colorado Water Year…\n\nHappy Water Year to all my Colorado friends and colleagues, new and old… \n\nMay this be a generous water year, although not too generous…", 				"id": "1578900353814519810", 				"created_at": "2022-10-09T00:09:13.000Z", 				"author_id": "944480690", 				"edit_history_tweet_ids": [ 					"1578900353814519810" 				] 			} 		] 	}, 	"meta": { 		"result_count": 3, 		"next_token": "18LAA581J5II7LA00C00ZZZZ", 		"previous_token": "1BLC45G1H8CAL5DG0G00ZZZZ" 	} }`

Using fields and expansions

How to use fields and expansions
--------------------------------

By default, the Twitter API v2 data objects include a small number of default fields when making a request without the use of the [fields](https://developer.twitter.com/en/docs/twitter-api/fields.html) or [expansions](https://developer.twitter.com/en/docs/twitter-api/expansions.html) parameters. This guide will show you how to use the `fields` and `expansions` query parameters in your request to receive additional objects and fields in your response.

In this guide, we will be requesting several fields in the following Tweet screenshot.  
 

  

As you can see in the screenshot, there are several visible pieces of information related to the Tweet, including the Tweet author, Tweet metrics, created timestamp, video, and video view count. There are also several pieces of data that are not visible within the screenshot, but are still available to request. 

When making a request to the API, the default response is simple, containing only the default Tweet fields (id and text). You will also only receive the primary object that returns with the given endpoint that you are using, and not any of the associated data objects that might relate to the primary object.

This simplicity, along with the fields and expansions parameters, enable you to request only those fields you require, depending on your use case.  

### Requesting additional fields and objects.

First off, we will be requesting a [Tweet object](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) using a Tweet ID and the [GET /tweets endpoint](https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/introduction.html).  

Request:

      `curl --request GET --url 'https://api.twitter.com/2/tweets?ids=1260294888811347969' \   --header 'Authorization: Bearer $BEARER_TOKEN'`
    

Response:

      `{     "data": [         {             "id": "1260294888811347969",             "text": "Don’t miss the Tweets about your Tweet. \n\nNow on iOS, you can see Retweets with comments all in one place. https://t.co/oanjZfzC6y"         }     ] }`
    

The following step-by-step guide will show you how to retrieve the additional data we can see in the screenshot.  

1. Identify the additional fields that you would like to request by using our [object model](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model.html), or by reviewing the list of fields in the endpoints’ API reference pages.  
      
    In this case, we will be requesting the following additional fields:  
    attachments, author\_id, created\_at, public\_metrics, and source.  
      
    
2. Build the `tweet.fields` query parameter with the above fields as its value using a comma-separated list:  
    `?tweet.fields=attachments,author_id,created_at,public_metrics,source`
    
3. Add the query parameter to the GET /tweets request that you made earlier.

Request:

      `curl --request GET --url 'https://api.twitter.com/2/tweets?ids=1260294888811347969&tweet.fields=attachments,author_id,created_at,public_metrics,source' \   --header 'Authorization: Bearer $BEARER_TOKEN'`
    

  
Response:  
 

      `{     "data": [         {             "id": "1260294888811347969",             "text": "Don’t miss the Tweets about your Tweet. \n\nNow on iOS, you can see Retweets with comments all in one place. https://t.co/oanjZfzC6y",             "author_id": "783214",             "public_metrics": {                 "retweet_count": 5219,                 "reply_count": 1828,                 "like_count": 17141,                 "quote_count": 3255             },             "source": "Sprinklr",             "attachments": {                 "media_keys": [                     "13_1260294804770041858"                 ]             },             "created_at": "2020-05-12T19:44:51.000Z"         }     ] }`
    

  
4. Next, we are going to request fields related to the video that was included in the Tweet. To do so, we will use the `expansions` parameter with `attachments.media_keys` as the value, and add this to the request.

?expansions=attachments.media\_keys

Request:  
 

      `curl --request GET --url 'https://api.twitter.com/2/tweets?ids=1260294888811347969&tweet.fields=attachments,author_id,created_at,public_metrics,source&expansions=attachments.media_keys' \   --header 'Authorization: Bearer $BEARER_TOKEN'`
    

  
Response, with the media object represented in the includes object:  
 

      `{     "data": [         {             "id": "1260294888811347969",             "text": "Don’t miss the Tweets about your Tweet. \n\nNow on iOS, you can see Retweets with comments all in one place. https://t.co/oanjZfzC6y",             "public_metrics": {                 "retweet_count": 5219,                 "reply_count": 1828,                 "like_count": 17141,                 "quote_count": 3255             },             "created_at": "2020-05-12T19:44:51.000Z",             "attachments": {                 "media_keys": [                     "13_1260294804770041858"                 ]             },             "author_id": "783214",             "source": "Sprinklr"         }     ],     "includes": {         "media": [             {                 "media_key": "13_1260294804770041858",                 "type": "video"             }         ]     } }`
    

  
5. And finally, we are going to request the view count and duration of the video. These aren’t default fields so we have to specifically request them. Use the `media.fields` parameter with the comma-separated values, `public_metrics` and `duration_ms` in your request.

?media.fields=public\_metrics,duration\_ms

  
Request:  
 

      `curl --request GET --url 'https://api.twitter.com/2/tweets?ids=1260294888811347969&tweet.fields=attachments,author_id,created_at,public_metrics,source&expansions=attachments.media_keys&media.fields=duration_ms,public_metrics' --header 'Authorization: Bearer $BEARER_TOKEN'`
    

  
Response, which now includes all the data that can be seen in the Tweet screenshot:  
 

      `{     "data": [         {             "id": "1260294888811347969",             "text": "Don’t miss the Tweets about your Tweet. \n\nNow on iOS, you can see Retweets with comments all in one place. https://t.co/oanjZfzC6y",             "author_id": "783214",             "public_metrics": {                 "retweet_count": 5219,                 "reply_count": 1828,                 "like_count": 17141,                 "quote_count": 3255             },             "created_at": "2020-05-12T19:44:51.000Z",             "source": "Sprinklr",             "attachments": {                 "media_keys": [                     "13_1260294804770041858"                 ]             }         }     ],     "includes": {         "media": [             {                 "duration_ms": 36503,                 "media_key": "13_1260294804770041858",                 "public_metrics": {                     "view_count": 1534703                 },                 "type": "video"             }         ]     } }`
    

In total, we included the following parameters in this example:

* ids=1260294888811347969
* tweet.fields=attachments,author\_id,created\_at,public\_metrics,source
* expansions=attachments.media\_keys
* media.fields=public\_metrics,duration\_ms  
     

When tied together, here is what the full query string looks like:

?ids=1260294888811347969&tweet.fields=attachments,author\_id,created\_at,public\_metrics,source&expansions=attachments.media\_keys&media.fields=public\_metrics,duration\_ms

Next steps
----------

[Try building a query string on your own with the tweets lookup endpoint](https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/api-reference/get-tweets "Try building a query string on your own with the tweets lookup endpoint")

[Review a full list of the Tweet object fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet "Review a full list of the Tweet object fields")

[Review a full list of available expansions](https://developer.twitter.com/en/docs/twitter-api/expansions "Review a full list of available expansions")

Example payloads

### Tweet

      `{   "data": [     {       "conversation_id": "1304102743196356610",       "id": "1307025659294674945",       "possibly_sensitive": false,       "public_metrics": {         "retweet_count": 11,         "reply_count": 2,         "like_count": 70,         "quote_count": 1       },       "entities": {         "urls": [           {             "start": 74,             "end": 97,             "url": "https://t.co/oeF3ZHeKQQ",             "expanded_url": "https://dev.to/twitterdev/understanding-the-new-tweet-payload-in-the-twitter-api-v2-1fg5",             "display_url": "dev.to/twitterdev/und…",             "images": [               {                 "url": "https://pbs.twimg.com/news_img/1317156296982867969/2uLfv-Bh?format=jpg&name=orig",                 "width": 1128,                 "height": 600               },               {                 "url": "https://pbs.twimg.com/news_img/1317156296982867969/2uLfv-Bh?format=jpg&name=150x150",                 "width": 150,                 "height": 150               }             ],             "status": 200,             "title": "Understanding the new Tweet payload in the Twitter API v2",             "description": "Twitter recently announced the new Twitter API v2, rebuilt from the ground up to deliver new features...",             "unwound_url": "https://dev.to/twitterdev/understanding-the-new-tweet-payload-in-the-twitter-api-v2-1fg5"           }         ]       },       "text": "Here’s an article that highlights the updates in the new Tweet payload v2 https://t.co/oeF3ZHeKQQ",       "in_reply_to_user_id": "2244994945",       "created_at": "2020-09-18T18:36:15.000Z",       "author_id": "2244994945",       "referenced_tweets": [         {           "type": "replied_to",           "id": "1304102743196356610"         }       ],       "lang": "en",       "source": "Twitter Web App"     }   ],   "includes": {     "users": [       {         "created_at": "2013-12-14T04:35:55.000Z",         "profile_image_url": "https://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg",         "entities": {           "url": {             "urls": [               {                 "start": 0,                 "end": 23,                 "url": "https://t.co/3ZX3TNiZCY",                 "expanded_url": "https://developer.twitter.com/en/community",                 "display_url": "developer.twitter.com/en/community"               }             ]           },           "description": {             "hashtags": [               {                 "start": 17,                 "end": 28,                 "tag": "TwitterDev"               },               {                 "start": 105,                 "end": 116,                 "tag": "TwitterAPI"               }             ]           }         },         "id": "2244994945",         "verified": true,         "location": "127.0.0.1",         "description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",         "pinned_tweet_id": "1293593516040269825",         "username": "TwitterDev",         "public_metrics": {           "followers_count": 513961,           "following_count": 2039,           "tweet_count": 3635,           "listed_count": 1672         },         "name": "Twitter Dev",         "url": "https://t.co/3ZX3TNiZCY",         "protected": false       }     ],     "tweets": [       {         "conversation_id": "1304102743196356610",         "id": "1304102743196356610",         "possibly_sensitive": false,         "public_metrics": {           "retweet_count": 31,           "reply_count": 12,           "like_count": 104,           "quote_count": 4         },         "entities": {           "mentions": [             {               "start": 146,               "end": 158,               "username": "suhemparack"             }           ],           "urls": [             {               "start": 237,               "end": 260,               "url": "https://t.co/CjneyMpgCq",               "expanded_url": "https://twitter.com/TwitterDev/status/1304102743196356610/video/1",               "display_url": "pic.twitter.com/CjneyMpgCq"             }           ],           "hashtags": [             {               "start": 8,               "end": 19,               "tag": "TwitterAPI"             }           ]         },         "attachments": {           "media_keys": [             "13_1303848070984024065"           ]         },         "text": "The new #TwitterAPI includes some improvements to the Tweet payload. You’re probably wondering — what are the main differences? 🧐\n\nIn this video, @SuhemParack compares the v1.1 Tweet payload with what you’ll find using our v2 endpoints. https://t.co/CjneyMpgCq",         "created_at": "2020-09-10T17:01:37.000Z",         "author_id": "2244994945",         "lang": "en",         "source": "Twitter Media Studio"       }     ]   } }`
    

### Tweet reply

      `{   "data": [     {       "lang": "en",       "conversation_id": "1296887091901718529",       "text": "See how @PennMedCDH are using Twitter data to understand the COVID-19 health crisis 📊\n\nhttps://t.co/1tdA8uDWes",       "referenced_tweets": [         {           "type": "replied_to",           "id": "1296887091901718529"         }       ],       "possibly_sensitive": false,       "entities": {         "annotations": [           {             "start": 30,             "end": 36,             "probability": 0.6318,             "type": "Product",             "normalized_text": "Twitter"           }         ],         "mentions": [           {             "start": 8,             "end": 19,             "username": "PennMedCDH"           }         ],         "urls": [           {             "start": 87,             "end": 110,             "url": "https://t.co/1tdA8uDWes",             "expanded_url": "https://developer.twitter.com/en/use-cases/success-stories/penn",             "display_url": "developer.twitter.com/en/use-cases/s…",             "status": 200,             "title": "Penn Medicine Center for Digital Health",             "description": "Penn Med Center for Digital Health has created a COVID-19 Twitter map that includes charts detailing sentiment, symptoms reported, state-by-state data cuts, and border data on the COVID-19 outbreak. In addition, their Penn Med With You initiative uses aggregate regional information from Twitter to inform their website and text-messaging service. The service uses this information to disseminate relevant and timely resources.",             "unwound_url": "https://developer.twitter.com/en/use-cases/success-stories/penn"           }         ]       },       "id": "1296887316556980230",       "public_metrics": {         "retweet_count": 9,         "reply_count": 3,         "like_count": 26,         "quote_count": 2       },       "author_id": "2244994945",       "in_reply_to_user_id": "2244994945",       "context_annotations": [         {           "domain": {             "id": "46",             "name": "Brand Category",             "description": "Categories within Brand Verticals that narrow down the scope of Brands"           },           "entity": {             "id": "781974596752842752",             "name": "Services"           }         },         {           "domain": {             "id": "47",             "name": "Brand",             "description": "Brands and Companies"           },           "entity": {             "id": "10045225402",             "name": "Twitter"           }         },         {           "domain": {             "id": "123",             "name": "Ongoing News Story",             "description": "Ongoing News Stories like 'Brexit'"           },           "entity": {             "id": "1220701888179359745",             "name": "COVID-19"           }         }       ],       "source": "Twitter Web App",       "created_at": "2020-08-21T19:10:05.000Z"     }   ],   "includes": {     "users": [       {         "created_at": "2013-12-14T04:35:55.000Z",         "id": "2244994945",         "protected": false,         "username": "TwitterDev",         "verified": true,         "entities": {           "url": {             "urls": [               {                 "start": 0,                 "end": 23,                 "url": "https://t.co/3ZX3TNiZCY",                 "expanded_url": "https://developer.twitter.com/en/community",                 "display_url": "developer.twitter.com/en/community"               }             ]           },           "description": {             "hashtags": [               {                 "start": 17,                 "end": 28,                 "tag": "TwitterDev"               },               {                 "start": 105,                 "end": 116,                 "tag": "TwitterAPI"               }             ]           }         },         "description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",         "pinned_tweet_id": "1293593516040269825",         "public_metrics": {           "followers_count": 513962,           "following_count": 2039,           "tweet_count": 3635,           "listed_count": 1672         },         "location": "127.0.0.1",         "name": "Twitter Dev",         "profile_image_url": "https://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg",         "url": "https://t.co/3ZX3TNiZCY"       },       {         "created_at": "2013-07-23T16:58:03.000Z",         "id": "1615654896",         "protected": false,         "username": "PennMedCDH",         "verified": false,         "entities": {           "url": {             "urls": [               {                 "start": 0,                 "end": 23,                 "url": "https://t.co/7eS9RuwIb9",                 "expanded_url": "http://centerfordigitalhealth.upenn.edu/",                 "display_url": "centerfordigitalhealth.upenn.edu"               }             ]           },           "description": {             "mentions": [               {                 "start": 0,                 "end": 13,                 "username": "PennMedicine"               }             ]           }         },         "description": "@PennMedicine's Center for Digital Health advances science by researching the implications of the advancement of digital health technology in health care.",         "public_metrics": {           "followers_count": 1348,           "following_count": 455,           "tweet_count": 1288,           "listed_count": 92         },         "location": "Philadelphia, PA",         "name": "Penn Med CDH",         "profile_image_url": "https://pbs.twimg.com/profile_images/1067488849725726723/MoO3FQ44_normal.jpg",         "url": "https://t.co/7eS9RuwIb9"       }     ],     "tweets": [       {         "lang": "en",         "conversation_id": "1296887091901718529",         "text": "Dr. @RainaMerchant and her team at the Penn Medicine CDH are helping build the future of health care.\n\nThe team is using insights from social data in many different ways — ranging from uncovering risk factors to shedding light on public sentiment. 🔎",         "possibly_sensitive": false,         "entities": {           "annotations": [             {               "start": 39,               "end": 55,               "probability": 0.8274,               "type": "Organization",               "normalized_text": "Penn Medicine CDH"             }           ],           "mentions": [             {               "start": 4,               "end": 18,               "username": "RainaMerchant"             }           ]         },         "id": "1296887091901718529",         "public_metrics": {           "retweet_count": 9,           "reply_count": 7,           "like_count": 32,           "quote_count": 0         },         "author_id": "2244994945",         "source": "Twitter Web App",         "created_at": "2020-08-21T19:09:12.000Z"       }     ]   } }`
    

### Extended Tweet

      `{   "data": [     {       "conversation_id": "1296121314218897408",       "id": "1296121314218897408",       "possibly_sensitive": false,       "public_metrics": {         "retweet_count": 54,         "reply_count": 9,         "like_count": 172,         "quote_count": 23       },       "entities": {         "urls": [           {             "start": 192,             "end": 215,             "url": "https://t.co/khXhTurm9x",             "expanded_url": "https://twittercommunity.com/t/hide-replies-now-available-in-the-new-twitter-api/140996",             "display_url": "twittercommunity.com/t/hide-replies…",             "images": [               {                 "url": "https://pbs.twimg.com/news_img/1296121315514957825/3CI24hSI?format=png&name=orig",                 "width": 400,                 "height": 400               },               {                 "url": "https://pbs.twimg.com/news_img/1296121315514957825/3CI24hSI?format=png&name=150x150",                 "width": 150,                 "height": 150               }             ],             "status": 200,             "title": "Hide replies now available in the new Twitter API",             "description": "Today, we’re happy to announce the general availability of the hide replies endpoint in the new Twitter API. The hide replies endpoint allows you to build tools that help people hide or unhide replies to their Tweets. People manage their replies for many reasons, including to give less attention to comments that are abusive, distracting, misleading, or to make conversations more engaging. Through this endpoint, you can build tools to help people on Twitter hide or unhide replies faster and more...",             "unwound_url": "https://twittercommunity.com/t/hide-replies-now-available-in-the-new-twitter-api/140996"           }         ],         "hashtags": [           {             "start": 178,             "end": 189,             "tag": "TwitterAPI"           }         ]       },       "text": "The hide replies endpoint is launching today! \n\nDevelopers can hide replies to Tweets - a crucial way developers can help improve the health of the public conversation using the #TwitterAPI.\n\nhttps://t.co/khXhTurm9x",       "created_at": "2020-08-19T16:26:16.000Z",       "context_annotations": [         {           "domain": {             "id": "65",             "name": "Interests and Hobbies Vertical",             "description": "Top level interests and hobbies groupings, like Food or Travel"           },           "entity": {             "id": "848920371311001600",             "name": "Technology",             "description": "Technology and computing"           }         },         {           "domain": {             "id": "66",             "name": "Interests and Hobbies Category",             "description": "A grouping of interests and hobbies entities, like Novelty Food or Destinations"           },           "entity": {             "id": "848921413196984320",             "name": "Computer programming",             "description": "Computer programming"           }         }       ],       "author_id": "2244994945",       "lang": "en",       "source": "Twitter Web App"     }   ],   "includes": {     "users": [       {         "created_at": "2013-12-14T04:35:55.000Z",         "profile_image_url": "https://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg",         "entities": {           "url": {             "urls": [               {                 "start": 0,                 "end": 23,                 "url": "https://t.co/3ZX3TNiZCY",                 "expanded_url": "https://developer.twitter.com/en/community",                 "display_url": "developer.twitter.com/en/community"               }             ]           },           "description": {             "hashtags": [               {                 "start": 17,                 "end": 28,                 "tag": "TwitterDev"               },               {                 "start": 105,                 "end": 116,                 "tag": "TwitterAPI"               }             ]           }         },         "id": "2244994945",         "verified": true,         "location": "127.0.0.1",         "description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",         "pinned_tweet_id": "1293593516040269825",         "username": "TwitterDev",         "public_metrics": {           "followers_count": 513962,           "following_count": 2039,           "tweet_count": 3635,           "listed_count": 1672         },         "name": "Twitter Dev",         "url": "https://t.co/3ZX3TNiZCY",         "protected": false       }     ]   } }`
    

### Tweet with media

      `{   "data": [     {       "lang": "en",       "conversation_id": "1293593516040269825",       "text": "It’s finally here! 🥁 Say hello to the new #TwitterAPI.\n\nWe’re rebuilding the Twitter API v2 from the ground up to better serve our developer community. And today’s launch is only the beginning.\n\nhttps://t.co/32VrwpGaJw https://t.co/KaFSbjWUA8",       "attachments": {         "media_keys": [           "7_1293565706408038401"         ]       },       "possibly_sensitive": false,       "entities": {         "annotations": [           {             "start": 78,             "end": 88,             "probability": 0.4381,             "type": "Product",             "normalized_text": "Twitter API"           }         ],         "hashtags": [           {             "start": 42,             "end": 53,             "tag": "TwitterAPI"           }         ],         "urls": [           {             "start": 195,             "end": 218,             "url": "https://t.co/32VrwpGaJw",             "expanded_url": "https://blog.twitter.com/developer/en_us/topics/tools/2020/introducing_new_twitter_api.html",             "display_url": "blog.twitter.com/developer/en_u…",             "images": [               {                 "url": "https://pbs.twimg.com/news_img/1336475659279818754/_cmRh7QE?format=jpg&name=orig",                 "width": 1200,                 "height": 627               },               {                 "url": "https://pbs.twimg.com/news_img/1336475659279818754/_cmRh7QE?format=jpg&name=150x150",                 "width": 150,                 "height": 150               }             ],             "status": 200,             "title": "Introducing a new and improved Twitter API",             "description": "Introducing the new Twitter API - rebuilt from the ground up to deliver new features faster so developers can help the world connect to the public conversation happening on Twitter.",             "unwound_url": "https://blog.twitter.com/developer/en_us/topics/tools/2020/introducing_new_twitter_api.html"           },           {             "start": 219,             "end": 242,             "url": "https://t.co/KaFSbjWUA8",             "expanded_url": "https://twitter.com/TwitterDev/status/1293593516040269825/video/1",             "display_url": "pic.twitter.com/KaFSbjWUA8"           }         ]       },       "id": "1293593516040269825",       "public_metrics": {         "retweet_count": 958,         "reply_count": 171,         "like_count": 2848,         "quote_count": 333       },       "author_id": "2244994945",       "context_annotations": [         {           "domain": {             "id": "46",             "name": "Brand Category",             "description": "Categories within Brand Verticals that narrow down the scope of Brands"           },           "entity": {             "id": "781974596752842752",             "name": "Services"           }         },         {           "domain": {             "id": "47",             "name": "Brand",             "description": "Brands and Companies"           },           "entity": {             "id": "10045225402",             "name": "Twitter"           }         },         {           "domain": {             "id": "65",             "name": "Interests and Hobbies Vertical",             "description": "Top level interests and hobbies groupings, like Food or Travel"           },           "entity": {             "id": "848920371311001600",             "name": "Technology",             "description": "Technology and computing"           }         },         {           "domain": {             "id": "66",             "name": "Interests and Hobbies Category",             "description": "A grouping of interests and hobbies entities, like Novelty Food or Destinations"           },           "entity": {             "id": "848921413196984320",             "name": "Computer programming",             "description": "Computer programming"           }         }       ],       "source": "Twitter Web App",       "created_at": "2020-08-12T17:01:42.000Z"     }   ],   "includes": {     "media": [       {         "height": 720,         "duration_ms": 34875,         "media_key": "7_1293565706408038401",         "type": "video",         "preview_image_url": "https://pbs.twimg.com/ext_tw_video_thumb/1293565706408038401/pu/img/66P2dvbU4a02jYbV.jpg",         "public_metrics": {           "view_count": 279438         },         "width": 1280       }     ],     "users": [       {         "created_at": "2013-12-14T04:35:55.000Z",         "id": "2244994945",         "protected": false,         "username": "TwitterDev",         "verified": true,         "entities": {           "url": {             "urls": [               {                 "start": 0,                 "end": 23,                 "url": "https://t.co/3ZX3TNiZCY",                 "expanded_url": "https://developer.twitter.com/en/community",                 "display_url": "developer.twitter.com/en/community"               }             ]           },           "description": {             "hashtags": [               {                 "start": 17,                 "end": 28,                 "tag": "TwitterDev"               },               {                 "start": 105,                 "end": 116,                 "tag": "TwitterAPI"               }             ]           }         },         "description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",         "pinned_tweet_id": "1293593516040269825",         "public_metrics": {           "followers_count": 513962,           "following_count": 2039,           "tweet_count": 3635,           "listed_count": 1672         },         "location": "127.0.0.1",         "name": "Twitter Dev",         "profile_image_url": "https://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg",         "url": "https://t.co/3ZX3TNiZCY"       }     ]   } }`
    

### Retweet

      `{   "data": [     {       "public_metrics": {         "retweet_count": 19,         "reply_count": 0,         "like_count": 0,         "quote_count": 0       },       "conversation_id": "1229851574555508737",       "id": "1229851574555508737",       "entities": {         "annotations": [           {             "start": 28,             "end": 38,             "probability": 0.261,             "type": "Product",             "normalized_text": "Alexa Skill"           },           {             "start": 44,             "end": 50,             "probability": 0.7332,             "type": "Product",             "normalized_text": "Twitter"           }         ],         "mentions": [           {             "start": 3,             "end": 15,             "username": "suhemparack"           }         ]       },       "text": "RT @suhemparack: I built an Alexa Skill for Twitter using APL that allows you to view Tweets and Trends on the echo show!\n\nCheck it out her…",       "created_at": "2020-02-18T19:33:59.000Z",       "possibly_sensitive": false,       "author_id": "2244994945",       "referenced_tweets": [         {           "type": "retweeted",           "id": "1229843515603144704"         }       ],       "context_annotations": [         {           "domain": {             "id": "47",             "name": "Brand",             "description": "Brands and Companies"           },           "entity": {             "id": "10026792024",             "name": "Amazon"           }         },         {           "domain": {             "id": "48",             "name": "Product",             "description": "Products created by Brands.  Examples: Ford Explorer, Apple iPhone."           },           "entity": {             "id": "968221983803494400",             "name": "Amazon - Alexa",             "description": "Alexa"           }         },         {           "domain": {             "id": "46",             "name": "Brand Category",             "description": "Categories within Brand Verticals that narrow down the scope of Brands"           },           "entity": {             "id": "781974596752842752",             "name": "Services"           }         },         {           "domain": {             "id": "47",             "name": "Brand",             "description": "Brands and Companies"           },           "entity": {             "id": "10045225402",             "name": "Twitter"           }         }       ],       "source": "Twitter Web App",       "lang": "en"     }   ],   "includes": {     "users": [       {         "profile_image_url": "https://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg",         "username": "TwitterDev",         "name": "Twitter Dev",         "location": "127.0.0.1",         "url": "https://t.co/3ZX3TNiZCY",         "entities": {           "url": {             "urls": [               {                 "start": 0,                 "end": 23,                 "url": "https://t.co/3ZX3TNiZCY",                 "expanded_url": "https://developer.twitter.com/en/community",                 "display_url": "developer.twitter.com/en/community"               }             ]           },           "description": {             "hashtags": [               {                 "start": 17,                 "end": 28,                 "tag": "TwitterDev"               },               {                 "start": 105,                 "end": 116,                 "tag": "TwitterAPI"               }             ]           }         },         "id": "2244994945",         "description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",         "verified": true,         "public_metrics": {           "followers_count": 513962,           "following_count": 2039,           "tweet_count": 3635,           "listed_count": 1672         },         "pinned_tweet_id": "1293593516040269825",         "created_at": "2013-12-14T04:35:55.000Z",         "protected": false       },       {         "profile_image_url": "https://pbs.twimg.com/profile_images/1230703695051935747/TbQKe91L_normal.jpg",         "username": "suhemparack",         "name": "Suhem Parack",         "location": "Seattle, WA",         "url": "https://t.co/8IkCzClPCz",         "entities": {           "url": {             "urls": [               {                 "start": 0,                 "end": 23,                 "url": "https://t.co/8IkCzClPCz",                 "expanded_url": "https://developer.twitter.com",                 "display_url": "developer.twitter.com"               }             ]           },           "description": {             "mentions": [               {                 "start": 42,                 "end": 50,                 "username": "Twitter"               }             ]           }         },         "id": "857699969263964161",         "description": "Developer Relations for Academic Research @Twitter. Talk to me about research with Twitter data. Previously: Amazon Alexa. Views are my own",         "verified": false,         "public_metrics": {           "followers_count": 738,           "following_count": 512,           "tweet_count": 460,           "listed_count": 12         },         "pinned_tweet_id": "1296498078233571329",         "created_at": "2017-04-27T20:56:22.000Z",         "protected": false       }     ],     "tweets": [       {         "public_metrics": {           "retweet_count": 19,           "reply_count": 1,           "like_count": 71,           "quote_count": 6         },         "conversation_id": "1229843515603144704",         "id": "1229843515603144704",         "entities": {           "annotations": [             {               "start": 11,               "end": 21,               "probability": 0.3342,               "type": "Product",               "normalized_text": "Alexa Skill"             },             {               "start": 27,               "end": 33,               "probability": 0.6727,               "type": "Product",               "normalized_text": "Twitter"             }           ],           "urls": [             {               "start": 127,               "end": 150,               "url": "https://t.co/l5J8wq748G",               "expanded_url": "https://dev.to/twitterdev/building-an-alexa-skill-for-twitter-using-alexa-presentation-language-1aj0",               "display_url": "dev.to/twitterdev/bui…",               "status": 200,               "unwound_url": "https://dev.to/twitterdev/building-an-alexa-skill-for-twitter-using-alexa-presentation-language-1aj0"             }           ]         },         "text": "I built an Alexa Skill for Twitter using APL that allows you to view Tweets and Trends on the echo show!\n\nCheck it out here 👇\n\nhttps://t.co/l5J8wq748G",         "created_at": "2020-02-18T19:01:58.000Z",         "possibly_sensitive": false,         "author_id": "857699969263964161",         "context_annotations": [           {             "domain": {               "id": "47",               "name": "Brand",               "description": "Brands and Companies"             },             "entity": {               "id": "10026792024",               "name": "Amazon"             }           },           {             "domain": {               "id": "48",               "name": "Product",               "description": "Products created by Brands.  Examples: Ford Explorer, Apple iPhone."             },             "entity": {               "id": "968221983803494400",               "name": "Amazon - Alexa",               "description": "Alexa"             }           },           {             "domain": {               "id": "46",               "name": "Brand Category",               "description": "Categories within Brand Verticals that narrow down the scope of Brands"             },             "entity": {               "id": "781974596752842752",               "name": "Services"             }           },           {             "domain": {               "id": "47",               "name": "Brand",               "description": "Brands and Companies"             },             "entity": {               "id": "10045225402",               "name": "Twitter"             }           }         ],         "source": "Twitter Web App",         "lang": "en"       }     ]   } }`
    

### Quote Tweet

      `{   "data": [     {       "lang": "en",       "conversation_id": "1328399838128467969",       "text": "As planned, the Labs v2 endpoints referenced below have now been retired. Please let us know in the forums if you have questions or need help with the Twitter API v2! https://t.co/JaxttUMmjX",       "referenced_tweets": [         {           "type": "quoted",           "id": "1327011423252144128"         }       ],       "possibly_sensitive": false,       "entities": {         "annotations": [           {             "start": 151,             "end": 157,             "probability": 0.8115,             "type": "Product",             "normalized_text": "Twitter"           }         ],         "urls": [           {             "start": 167,             "end": 190,             "url": "https://t.co/JaxttUMmjX",             "expanded_url": "https://twitter.com/TwitterDev/status/1327011423252144128",             "display_url": "twitter.com/TwitterDev/sta…"           }         ]       },       "id": "1328399838128467969",       "public_metrics": {         "retweet_count": 7,         "reply_count": 4,         "like_count": 29,         "quote_count": 1       },       "author_id": "2244994945",       "context_annotations": [         {           "domain": {             "id": "46",             "name": "Brand Category",             "description": "Categories within Brand Verticals that narrow down the scope of Brands"           },           "entity": {             "id": "781974596752842752",             "name": "Services"           }         },         {           "domain": {             "id": "47",             "name": "Brand",             "description": "Brands and Companies"           },           "entity": {             "id": "10045225402",             "name": "Twitter"           }         },         {           "domain": {             "id": "65",             "name": "Interests and Hobbies Vertical",             "description": "Top level interests and hobbies groupings, like Food or Travel"           },           "entity": {             "id": "848920371311001600",             "name": "Technology",             "description": "Technology and computing"           }         },         {           "domain": {             "id": "66",             "name": "Interests and Hobbies Category",             "description": "A grouping of interests and hobbies entities, like Novelty Food or Destinations"           },           "entity": {             "id": "848921413196984320",             "name": "Computer programming",             "description": "Computer programming"           }         }       ],       "source": "Twitter Web App",       "created_at": "2020-11-16T18:09:36.000Z"     }   ],   "includes": {     "users": [       {         "created_at": "2013-12-14T04:35:55.000Z",         "id": "2244994945",         "protected": false,         "username": "TwitterDev",         "verified": true,         "entities": {           "url": {             "urls": [               {                 "start": 0,                 "end": 23,                 "url": "https://t.co/3ZX3TNiZCY",                 "expanded_url": "https://developer.twitter.com/en/community",                 "display_url": "developer.twitter.com/en/community"               }             ]           },           "description": {             "hashtags": [               {                 "start": 17,                 "end": 28,                 "tag": "TwitterDev"               },               {                 "start": 105,                 "end": 116,                 "tag": "TwitterAPI"               }             ]           }         },         "description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",         "pinned_tweet_id": "1293593516040269825",         "public_metrics": {           "followers_count": 513962,           "following_count": 2039,           "tweet_count": 3635,           "listed_count": 1672         },         "location": "127.0.0.1",         "name": "Twitter Dev",         "profile_image_url": "https://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg",         "url": "https://t.co/3ZX3TNiZCY"       }     ],     "tweets": [       {         "lang": "en",         "conversation_id": "1327011423252144128",         "text": "👋 Friendly reminder that Twitter Developer Labs v2 hide replies and recent search will be retired next Monday, November 16! We encourage you to migrate to the new hide replies and recent search endpoints now available in the v2 #TwitterAPI. Details: https://t.co/r6z6CI7kEy",         "possibly_sensitive": false,         "entities": {           "annotations": [             {               "start": 26,               "end": 50,               "probability": 0.4387,               "type": "Product",               "normalized_text": "Twitter Developer Labs v2"             }           ],           "hashtags": [             {               "start": 228,               "end": 239,               "tag": "TwitterAPI"             }           ],           "urls": [             {               "start": 250,               "end": 273,               "url": "https://t.co/r6z6CI7kEy",               "expanded_url": "https://twittercommunity.com/t/retiring-labs-v2-recent-search-and-hide-replies/145795",               "display_url": "twittercommunity.com/t/retiring-lab…",               "images": [                 {                   "url": "https://pbs.twimg.com/news_img/1327011425240313856/PkurOyu1?format=jpg&name=orig",                   "width": 1200,                   "height": 630                 },                 {                   "url": "https://pbs.twimg.com/news_img/1327011425240313856/PkurOyu1?format=jpg&name=150x150",                   "width": 150,                   "height": 150                 }               ],               "status": 200,               "title": "Retiring Labs v2 recent search and hide replies",               "description": "As we said in our Early Access and hide replies announcements, the following Twitter Developer Labs v2 endpoints will be retired on November 16th. Labs v2 recent search Labs v2 hide replies If called, these endpoints will respond with an HTTP 410 status and return no data. Based on your feedback from Labs, we incorporated corresponding functionality into the Twitter API v2. The relevant documentation can be found using the links below. Click here to enroll in v2 access if you haven’t already...",               "unwound_url": "https://twittercommunity.com/t/retiring-labs-v2-recent-search-and-hide-replies/145795"             }           ]         },         "id": "1327011423252144128",         "public_metrics": {           "retweet_count": 8,           "reply_count": 2,           "like_count": 33,           "quote_count": 4         },         "author_id": "2244994945",         "context_annotations": [           {             "domain": {               "id": "46",               "name": "Brand Category",               "description": "Categories within Brand Verticals that narrow down the scope of Brands"             },             "entity": {               "id": "781974596752842752",               "name": "Services"             }           },           {             "domain": {               "id": "47",               "name": "Brand",               "description": "Brands and Companies"             },             "entity": {               "id": "10045225402",               "name": "Twitter"             }           },           {             "domain": {               "id": "65",               "name": "Interests and Hobbies Vertical",               "description": "Top level interests and hobbies groupings, like Food or Travel"             },             "entity": {               "id": "848920371311001600",               "name": "Technology",               "description": "Technology and computing"             }           },           {             "domain": {               "id": "66",               "name": "Interests and Hobbies Category",               "description": "A grouping of interests and hobbies entities, like Novelty Food or Destinations"             },             "entity": {               "id": "848921413196984320",               "name": "Computer programming",               "description": "Computer programming"             }           }         ],         "source": "Twitter Web App",         "created_at": "2020-11-12T22:12:32.000Z"       }     ]   } }`
    

### Retweeted quote Tweet

      `{   "data": [     {       "lang": "en",       "conversation_id": "1225470895902412800",       "text": "RT @AureliaSpecker: 📣 If you enjoyed the London commute tutorial I wrote in November last year, check out the refactored version that uses…",       "referenced_tweets": [         {           "type": "retweeted",           "id": "1224709550214873090"         }       ],       "possibly_sensitive": false,       "entities": {         "annotations": [           {             "start": 42,             "end": 47,             "probability": 0.6999,             "type": "Place",             "normalized_text": "London"           }         ],         "mentions": [           {             "start": 3,             "end": 18,             "username": "AureliaSpecker"           }         ]       },       "id": "1225470895902412800",       "public_metrics": {         "retweet_count": 12,         "reply_count": 0,         "like_count": 0,         "quote_count": 0       },       "author_id": "2244994945",       "context_annotations": [         {           "domain": {             "id": "46",             "name": "Brand Category",             "description": "Categories within Brand Verticals that narrow down the scope of Brands"           },           "entity": {             "id": "781974596752842752",             "name": "Services"           }         },         {           "domain": {             "id": "47",             "name": "Brand",             "description": "Brands and Companies"           },           "entity": {             "id": "10045225402",             "name": "Twitter"           }         },         {           "domain": {             "id": "65",             "name": "Interests and Hobbies Vertical",             "description": "Top level interests and hobbies groupings, like Food or Travel"           },           "entity": {             "id": "848920371311001600",             "name": "Technology",             "description": "Technology and computing"           }         },         {           "domain": {             "id": "66",             "name": "Interests and Hobbies Category",             "description": "A grouping of interests and hobbies entities, like Novelty Food or Destinations"           },           "entity": {             "id": "848921413196984320",             "name": "Computer programming",             "description": "Computer programming"           }         }       ],       "source": "Twitter for iPhone",       "created_at": "2020-02-06T17:26:44.000Z"     }   ],   "includes": {     "users": [       {         "created_at": "2013-12-14T04:35:55.000Z",         "id": "2244994945",         "protected": false,         "username": "TwitterDev",         "verified": true,         "entities": {           "url": {             "urls": [               {                 "start": 0,                 "end": 23,                 "url": "https://t.co/3ZX3TNiZCY",                 "expanded_url": "https://developer.twitter.com/en/community",                 "display_url": "developer.twitter.com/en/community"               }             ]           },           "description": {             "hashtags": [               {                 "start": 17,                 "end": 28,                 "tag": "TwitterDev"               },               {                 "start": 105,                 "end": 116,                 "tag": "TwitterAPI"               }             ]           }         },         "description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",         "pinned_tweet_id": "1293593516040269825",         "public_metrics": {           "followers_count": 513962,           "following_count": 2039,           "tweet_count": 3635,           "listed_count": 1672         },         "location": "127.0.0.1",         "name": "Twitter Dev",         "profile_image_url": "https://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg",         "url": "https://t.co/3ZX3TNiZCY"       },       {         "created_at": "2013-01-18T23:45:43.000Z",         "id": "1102321381",         "protected": false,         "username": "AureliaSpecker",         "verified": false,         "entities": {           "description": {             "mentions": [               {                 "start": 7,                 "end": 17,                 "username": "TwitterUK"               },               {                 "start": 86,                 "end": 95,                 "username": "_dormrod"               }             ]           }         },         "description": "devrel @TwitterUK • Swiss in London • mother of houseplants • personal hairdresser to @_dormrod",         "pinned_tweet_id": "1253069421322567681",         "public_metrics": {           "followers_count": 1036,           "following_count": 1330,           "tweet_count": 855,           "listed_count": 26         },         "location": "London, UK",         "name": "Aurelia Specker",         "profile_image_url": "https://pbs.twimg.com/profile_images/1137517534104772608/8FBYgc6G_normal.jpg",         "url": ""       }     ],     "tweets": [       {         "lang": "en",         "conversation_id": "1224709550214873090",         "text": "📣 If you enjoyed the London commute tutorial I wrote in November last year, check out the refactored version that uses Twitter's new search endpoint 🚇 https://t.co/87XIPZmZBJ\n\n#DEVcommunity #Pythontutorial @TwitterDev @TwitterAPI https://t.co/dXrJYvn3hY",         "referenced_tweets": [           {             "type": "quoted",             "id": "1195000047089389573"           }         ],         "possibly_sensitive": false,         "entities": {           "annotations": [             {               "start": 22,               "end": 27,               "probability": 0.7075,               "type": "Place",               "normalized_text": "London"             },             {               "start": 120,               "end": 126,               "probability": 0.7355,               "type": "Product",               "normalized_text": "Twitter"             }           ],           "mentions": [             {               "start": 206,               "end": 217,               "username": "TwitterDev"             },             {               "start": 218,               "end": 229,               "username": "TwitterAPI"             }           ],           "hashtags": [             {               "start": 176,               "end": 189,               "tag": "DEVcommunity"             },             {               "start": 190,               "end": 205,               "tag": "Pythontutorial"             }           ],           "urls": [             {               "start": 151,               "end": 174,               "url": "https://t.co/87XIPZmZBJ",               "expanded_url": "https://bit.ly/2OrnrCC",               "display_url": "bit.ly/2OrnrCC",               "status": 200,               "unwound_url": "https://dev.to/twitterdev/migrate-to-twitter-s-newly-released-labs-recent-search-endpoint-3npe"             },             {               "start": 230,               "end": 253,               "url": "https://t.co/dXrJYvn3hY",               "expanded_url": "https://twitter.com/AureliaSpecker/status/1195000047089389573",               "display_url": "twitter.com/AureliaSpecker…"             }           ]         },         "id": "1224709550214873090",         "public_metrics": {           "retweet_count": 12,           "reply_count": 0,           "like_count": 43,           "quote_count": 2         },         "author_id": "1102321381",         "context_annotations": [           {             "domain": {               "id": "46",               "name": "Brand Category",               "description": "Categories within Brand Verticals that narrow down the scope of Brands"             },             "entity": {               "id": "781974596752842752",               "name": "Services"             }           },           {             "domain": {               "id": "47",               "name": "Brand",               "description": "Brands and Companies"             },             "entity": {               "id": "10045225402",               "name": "Twitter"             }           },           {             "domain": {               "id": "65",               "name": "Interests and Hobbies Vertical",               "description": "Top level interests and hobbies groupings, like Food or Travel"             },             "entity": {               "id": "848920371311001600",               "name": "Technology",               "description": "Technology and computing"             }           },           {             "domain": {               "id": "66",               "name": "Interests and Hobbies Category",               "description": "A grouping of interests and hobbies entities, like Novelty Food or Destinations"             },             "entity": {               "id": "848921413196984320",               "name": "Computer programming",               "description": "Computer programming"             }           }         ],         "source": "Twitter Web App",         "created_at": "2020-02-04T15:01:25.000Z"       }     ]   } }`

Fields

The Twitter API v2 endpoints are equipped with a set of parameters called _fields,_ which allows you to select just the data that you want from each of the objects in your endpoint response.

By default, the Tweet object only returns the id and the text fields, and for Tweets created since September 29, 2022, the edit\_history\_tweet\_ids field. If you need the Tweet’s created date or public metrics, you will need to use the tweet.fields parameters to request them. This provides a higher degree of customization by enabling you to only request the fields you require depending on your use case. For example, you would include this query string in your request 

?tweet.fields=created\_at,public\_metrics

Each object has its own parameter which is used to specifically request the fields that are associated with that object. Here are the different fields parameters that are currently available:  

* [Tweet](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) → `tweet.fields`
* [User](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) → `user.fields`
* [Media](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/media) → `media.fields`
* [Poll](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/poll) → `poll.fields`
* [Place](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/place) → `place.fields`

  
When using an endpoint that primarily returns a particular object, simply use the matching field parameter and specify the field(s) desired in a comma-separated list as the value to that parameter to retrieve those fields in the response.  
 

### Example

If you are using the [GET /tweets/search/recent](https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent) endpoint, you will primarily receive [Tweet objects](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) in that response. Without specifying any fields parameters, you will just receive the default values, `id` and `text`. If you are interested in receiving the public metrics of the Tweets that are returned in the response, you will want to include the `tweet.fields` parameter in your request, with `public_metrics` set as the value. 

This request would look like the following. If you would like to use this request, make sure to replace $BEARER\_TOKEN with your [Bearer Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens) and send it using your command line tool.  

      `curl --request GET \   --url 'https://api.twitter.com/2/tweets/search/recent?query=from%3Atwitterdev&tweet.fields=public_metrics' \   --header 'Authorization: Bearer $BEARER_TOKEN'`
    

  
If you send this request in your terminal, then each of the Tweets that return will include the following fields:

      `{    "data": {        "id": "1263150595717730305",        "public_metrics": {            "retweet_count": 12,            "reply_count": 14,            "like_count": 49,            "quote_count": 7        },        "text": "Do you 👀our new Tweet settings?\n\nWe want to know how and why you’d use a feature like this in the API. Get the details and let us know what you think👇\nhttps://t.co/RtMhhfAcIB https://t.co/8wxeZ9fJER"    } }`
    

If you would like to retrieve a set of fields from a secondary object that is associated with the primary object returned by an endpoint, you will need to include an additional `[expansions](https://developer.twitter.com/en/docs/twitter-api/expansions.html)` parameter. 

For example, if you were using the same GET search/tweets/recent endpoint as earlier, and you wanted to retrieve the author's profile description, you will have to pass the expansions=author\_id and user.fields=description with your request. Here is an example of what this might look like. If you would like to try this request, make sure to replace the $BEARER\_TOKEN with your [Bearer Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens) before pasting it into your command line tool.

      `curl --request GET \   --url 'https://api.twitter.com/2/tweets/search/recent?query=from%3Atwitterdev&tweet.fields=public_metrics&expansions=author_id&user.fields=description' \   --header 'Authorization: Bearer $BEARER_TOKEN'`
    

  
If you specify this in the request, then each of the Tweets that deliver will have the following fields, and the related [user object's](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) default and specified fields will return within includes. The user object can be mapped back to the corresponding Tweet(s) by matching the tweet.author\_id and users.id fields.  
 

      `{   "data": [     {       "id": "1263150595717730305",       "author_id": "2244994945",       "text": "Do you 👀our new Tweet settings?\n\nWe want to know how and why you’d use a feature like this in the API. Get the details and let us know what you think👇\nhttps://t.co/RtMhhfAcIB https://t.co/8wxeZ9fJER",       "public_metrics": {         "retweet_count": 12,         "reply_count": 13,         "like_count": 51,         "quote_count": 7       }     }   ],   "includes": {     "users": [       {         "id": "2244994945",         "username": "TwitterDev",         "description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",         "name": "Twitter Dev"       }     ]   } }`
    

Bear in mind that you cannot request specific subfields (for example, `public_metrics.retweet_count`). All subfields will be returned when the top-level field (`public_metrics`) is specified. We have listed all possible fields that you can request in each endpoints' API reference page's parameters table. 

A full list of fields are listed in the [object model](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model.html). To expand and request fields on an object that is not that endpoint’s primary resource, use the [expansions](https://developer.twitter.com/en/docs/twitter-api/expansions.html) parameter with fields.

Next step
---------

[Learn how to use fields with expansions](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/using-fields-and-expansions "Learn how to use fields with expansions")

[Review the different data objects available with Twitter API v2](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/introduction "Review the different data objects available with Twitter API v2")

[Make your first request with fields and expansions](https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/quick-start "Make your first request with fields and expansions")

Expansions

Overview
--------

With expansions, developers can expand objects referenced in the payload. Objects available for expansion are referenced by ID. For example, the `referenced_tweets.id` and `author_id` fields returned in the [Tweets lookup](https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/introduction.html) payload can be expanded into complete objects. If you would like to request fields related to the user that posted that Tweet, or the media, poll, or place that was included in that Tweet, you will need to pass the related expansion query parameter in your request to receive that data in your response. Currently, v2 endpoints that return Tweets, Users, Lists, Spaces, and Direct Message event objects all support expansions (see examples below). 

When including an expansion in your request, we will include that expanded object’s default fields within the same response. It helps return additional data in the same response without the need for separate requests. If you would like to request additional [fields](https://developer.twitter.com/en/docs/twitter-api/fields.html) related to the expanded object, you can include the field parameter associated with that expanded object, along with a comma-separated list of fields that you would like to receive in your response. Please note fields are not always returned in the same order they were requested in the query.

The Tweet payload below contains reference IDs for complementary objects we can expand on, including the author\_id of who posted the Tweet, the id of a _referenced_ Tweet, and a media\_key for a media attachment. 

      `{     "data": {         "attachments": {             "media_keys": [                 "16_1211797899316740096"             ]         },         "author_id": "2244994945",         "id": "1212092628029698048",         "referenced_tweets": [             {                 "type": "replied_to",                 "id": "1212092627178287104"             }         ],         "text": "We believe the best future version of our API will come from building it with YOU. Here’s to another great year with everyone who builds on the Twitter platform. We can’t wait to continue working with you in the new year. https://t.co/yvxdK6aOo2"     } }`
    

We can expand on `attachments.media_keys` to view the media object, `author_id` to view the user object, and `referenced_tweets.id` to view the Tweet object the originally requested Tweet was referencing. Expanded objects will be nested in the `"includes"` object, as can be seen in the sample response below.  

### Available expansions for Tweet payloads

| Expansion | Description |
| --- | --- |
| `author_id` | Returns a user object representing the Tweet’s author |
| `referenced_tweets.id` | Returns a Tweet object that this Tweet is referencing (either as a Retweet, Quoted Tweet, or reply) |
| edit\_history\_tweet\_ids | Returns Tweet objects that are part of a Tweet's edit history |
| `in_reply_to_user_id` | Returns a user object representing the Tweet author this requested Tweet is a reply of |
| `attachments.media_keys` | Returns a media object representing the images, videos, GIFs included in the Tweet |
| `attachments.poll_ids` | Returns a poll object containing metadata for the poll included in the Tweet |
| `geo.place_id` | Returns a place object containing metadata for the location tagged in the Tweet |
| `entities.mentions.username` | Returns a user object for the user mentioned in the Tweet |
| `referenced_tweets.id.author_id` | Returns a user object for the author of the referenced Tweet |

### Available expansion for User payloads

| Expansion | Description |
| --- | --- |
| `pinned_tweet_id` | Returns a Tweet object representing the Tweet pinned to the top of the user’s profile |

### Available expansions for Direct Message event payloads

| Expansion | Description |
| --- | --- |
| `attachments.media_keys` | Returns a Media object that was attached to a Direct Message |
| `referenced_tweets.id` | Returns a Tweet object that was referenced in a Direct Message |
| `sender_id` | Returns a User object representing the author of a Direct Message and who invited a participant to join a conversation |
| `participant_ids` | Returns a User object representing a participant that joined or left a conversation |

### Available expansions for Spaces payloads

| Expansion | Description |
| --- | --- |
| `invited_user_ids` | Returns User objects representing what accounts were invited |
| `speaker_ids` | Returns User objects representing what accounts spoke during a Space |
| `creator_id` | Returns a User object representing what account created the Space |
| `host_ids` | Returns User objects representing what accounts were set up as hosts |
| `topics_ids` | Returns topic descriptions that were set up by the creator |

### Available expansion for Lists payloads

| Expansion | Description |
| --- | --- |
| `owner_id` | Returns a User object representing what account created and maintains the List |

Expanding the media, Tweet, and user objects
--------------------------------------------

#### In the following request, we are requesting the following expansions to include alongside the default Tweet fields.  Be sure to replace `$ACCESS_TOKEN` with your own generated [App-only Token](https://developer.twitter.com/content/developer-twitter/en/docs/authentication/app-only).

* `attachments.media_keys`
* `referenced_tweets.id`
* `author_id`

**Sample Request**

      `curl 'https://api.twitter.com/2/tweets/1212092628029698048?expansions=attachments.media_keys,referenced_tweets.id,author_id' --header 'Authorization: Bearer $ACCESS_TOKEN'`
    

**Sample Response**

      `{     "data": {         "attachments": {             "media_keys": [                 "16_1211797899316740096"             ]         },         "author_id": "2244994945",         "id": "1212092628029698048",         "referenced_tweets": [             {                 "type": "replied_to",                 "id": "1212092627178287104"             }         ],         "text": "We believe the best future version of our API will come from building it with YOU. Here’s to another great year with everyone who builds on the Twitter platform. We can’t wait to continue working with you in the new year. https://t.co/yvxdK6aOo2"     },     "includes": {         "media": [             {                 "media_key": "16_1211797899316740096",                 "type": "animated_gif"             }         ],         "users": [             {                 "id": "2244994945",                 "name": "Twitter Dev",                 "username": "TwitterDev"             }         ],         "tweets": [             {                 "author_id": "2244994945",                 "id": "1212092627178287104",                 "referenced_tweets": [                     {                         "type": "replied_to",                         "id": "1212092626247110657"                     }                 ],                 "text": "These launches would not be possible without the feedback you provided along the way, so THANK YOU to everyone who has contributed your time and ideas. Have more feedback? Let us know ⬇️ https://t.co/Vxp4UKnuJ9"             }         ]     } }`
    

Expanding the poll object
-------------------------

In the following request, we are requesting the following expansions to include alongside the default Tweet fields:

* `attachments.poll_ids`

**Sample Request**

      `curl 'https://api.twitter.com/2/tweets/1199786642791452673?expansions=attachments.poll_ids' --header 'Authorization: Bearer $ACCESS_TOKEN'`
    

**Sample Response**

      `{     "data": {         "attachments": {             "poll_ids": [                 "1199786642468413448"             ]         },         "id": "1199786642791452673",         "text": "C#"     },     "includes": {         "polls": [             {                 "id": "1199786642468413448",                 "options": [                     {                         "position": 1,                         "label": "“C Sharp”",                         "votes": 795                     },                     {                         "position": 2,                         "label": "“C Hashtag”",                         "votes": 156                     }                 ]             }         ]     } }`
    

Expanding the place object
--------------------------

In the following request, we are requesting the following expansions to include alongside the default Tweet fields:

* `geo.place_id`

**Sample Request**

      `curl 'https://api.twitter.com/2/tweets/:ID?expansions=geo.place_id’ --header 'Authorization: Bearer $ACCESS_TOKEN'`
    

**Sample Response**

      `{     "data": {         "geo": {             "place_id": "01a9a39529b27f36"         },         "id": "ID",         "text": "Test"     },     "includes": {         "places": [             {                 "full_name": "Manhattan, NY",                 "id": "01a9a39529b27f36"             }         ]     } }`
    

Next step
---------

[Learn how to use Fields with Expansions](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/using-fields-and-expansions "Learn how to use Fields with Expansions")

[Review the different data objects available with Twitter API v2](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/introduction "Review the different data objects available with Twitter API v2")

Overview

Overview
--------

Annotations have been added to the Tweet object from all v2 endpoints that return a Tweet object. Tweet annotations offer a way to understand contextual information about the Tweet itself. Though 100% of Tweets are reviewed, due to the contents of Tweet text, only a portion are annotated.

**Entity annotations (NER):** Entities are comprised of people, places, products, and organizations. Entities are delivered as part of the entity payload section. They are programmatically assigned based on what is explicitly mentioned (named-entity recognition) in the Tweet text.

**Context annotations:** Derived from the analysis of a Tweet’s text and will include a domain and entity pairing which can be used to discover Tweets on topics that may have been previously difficult to surface. At present, we’re using a list of 80+ domains to categorize Tweets. A CSV file of the available context annotation entities is available for download at our [Github repository](https://github.com/twitterdev/twitter-context-annotations).

Tweet annotation types
----------------------

### Entities

Entity annotations are programmatically defined entities that are nested within the entities field and are reflected as annotations in the payload. Each annotation has a confidence score and an indication of where in the Tweet text the entities were identified (start and end fields).

The entity annotations can have the following types:

**Person** - Barack Obama, Daniel, or George W. Bush

**Place** - Detroit, Cali, or "San Francisco, California"

**Product** - Mountain Dew, Mozilla Firefox

**Organization** - Chicago White Sox, IBM

**Other** - Diabetes, Super Bowl 50

### Context

_Last updated: June 2022_

Context annotations are delivered as a context\_annotations field in the payload. These annotations are inferred based on semantic analysis (keywords, hashtags, handles, etc) of the Tweet text and result in domain and/or entity labels. Context annotations can yield one or many domains. At present, we’re using a list of 80+ domains reflected in the table below.

|     |     |     |     |
| --- | --- | --- | --- |
| 3: TV Shows<br><br>4: TV Episodes<br><br>6: Sports Events<br><br>10: Person<br><br>11: Sport<br><br>12: Sports Team<br><br>13: Place<br><br>22: TV Genres<br><br>23: TV Channels<br><br>26: Sports League<br><br>27: American Football Game<br><br>28: NFL Football Game<br><br>29: Events<br><br>31: Community<br><br>35: Politicians<br><br>38: Political Race<br><br>39: Basketball Game<br><br>40: Sports Series<br><br>43: Soccer Match<br><br>44: Baseball Game<br><br>45: Brand Vertical | 46: Brand Category<br><br>47: Brand<br><br>48: Product<br><br>54: Musician<br><br>55: Music Genre<br><br>56: Actor<br><br>58: Entertainment Personality<br><br>60: Athlete<br><br>65: Interests and Hobbies Vertical<br><br>66: Interests and Hobbies Category<br><br>67: Interests and Hobbies<br><br>68: Hockey Game<br><br>71: Video Game<br><br>78: Video Game Publisher<br><br>79: Video Game Hardware<br><br>83: Cricket Match<br><br>84: Book<br><br>85: Book Genre<br><br>86: Movie<br><br>87: Movie Genre<br><br>88: Political Body | 89: Music Album<br><br>90: Radio Station<br><br>91: Podcast<br><br>92: Sports Personality<br><br>93: Coach<br><br>94: Journalist<br><br>95: TV Channel \[Entity Service\]<br><br>109: Reoccurring Trends<br><br>110: Viral Accounts<br><br>114: Concert<br><br>115: Video Game Conference<br><br>116: Video Game Tournament<br><br>117: Movie Festival<br><br>118: Award Show<br><br>119: Holiday<br><br>120: Digital Creator<br><br>122: Fictional Character<br><br>130: Multimedia Franchise<br><br>131: Unified Twitter Taxonomy<br><br>136: Video Game Personality | 137: eSports Team<br><br>138: eSports Player  <br><br>139: Fan Community<br><br>149: Esports League<br><br>152: Food<br><br>155: Weather<br><br>156: Cities<br><br>157: Colleges & Universities<br><br>158: Points of Interest<br><br>159: States<br><br>160: Countries<br><br>162: Exercise & fitness<br><br>163: Travel<br><br>164: Fields of study<br><br>165: Technology<br><br>166: Stocks<br><br>167: Animals<br><br>171: Local News<br><br>172: Global TV Show<br><br>173: Google Product Taxonomy<br><br>174: Digital Assets & Crypto<br><br>175: Emergency Events |

_Note:_ Domain 131 (Unified Twitter Taxonomy) refers to Twitter's User Facing Interest Taxonomy. This taxonomy helps to power features on the platform such as, [Topics](https://blog.twitter.com/en_us/topics/product/2020/topics-behind-the-tweets).  

Requesting annotations
----------------------

### **Sample Request**

      `curl --location --request GET 'https://api.twitter.com/2/tweets/1212092628029698048?tweet.fields=context_annotations,entities' --header 'Authorization: Bearer $BEARER_TOKEN'`
    

**  
Sample Response**

      `{     "data": {         "context_annotations": [             {                 "domain": {                     "id": "119",                     "name": "Holiday",                     "description": "Holidays like Christmas or Halloween"                 },                 "entity": {                     "id": "1186637514896920576",                     "name": " New Years Eve"                 }             },             {                 "domain": {                     "id": "119",                     "name": "Holiday",                     "description": "Holidays like Christmas or Halloween"                 },                 "entity": {                     "id": "1206982436287963136",                     "name": "Happy New Year: It’s finally 2020 everywhere!",                     "description": "Catch fireworks and other celebrations as people across the globe enter the new year.\nPhoto via @GettyImages "                 }             },             {                 "domain": {                     "id": "45",                     "name": "Brand Vertical",                     "description": "Top level entities that describe a Brands industry"                 }             },             {                 "domain": {                     "id": "46",                     "name": "Brand Category",                     "description": "Categories within Brand Verticals that narrow down the scope of Brands"                 },                 "entity": {                     "id": "781974596752842752",                     "name": "Services"                 }             },             {                 "domain": {                     "id": "47",                     "name": "Brand",                     "description": "Brands and Companies"                 },                 "entity": {                     "id": "10045225402",                     "name": "Twitter"                 }             },             {                 "domain": {                     "id": "119",                     "name": "Holiday",                     "description": "Holidays like Christmas or Halloween"                 },                 "entity": {                     "id": "1206982436287963136",                     "name": "Happy New Year: It’s finally 2020 everywhere!",                     "description": "Catch fireworks and other celebrations as people across the globe enter the new year.\nPhoto via @GettyImages "                 }             }         ],         "entities": {             "annotations": [                 {                     "start": 144,                     "end": 150,                     "probability": 0.626,                     "type": "Product",                     "normalized_text": "Twitter"                 }             ],             "urls": [                 {                     "start": 222,                     "end": 245,                     "url": "https://t.co/yvxdK6aOo2",                     "expanded_url": "https://twitter.com/LovesNandos/status/1211797914437259264/photo/1",                     "display_url": "pic.twitter.com/yvxdK6aOo2"                 }             ]         },         "id": "1212092628029698048",         "text": "We believe the best future version of our API will come from building it with YOU. Here’s to another great year with everyone who builds on the Twitter platform. We can’t wait to continue working with you in the new year. https://t.co/yvxdK6aOo2"     } }`
    

**  
Sample App**

See the [Tweet Entity Extractor on Glitch](https://tweet-entity-extractor.glitch.me/) to easily discover context annotations in Tweets and see how this feature works.

FAQ

Frequently asked questions
--------------------------

### Context annotations

The questions below are specific to the context annotations element of Tweet annotations. For more details, please see the [Overview](https://developer.twitter.com/en/docs/twitter-api/annotations/overview.html) page.

**How does Twitter context annotations work?**

Twitter classifies Tweets semantically, meaning that we curate lists of keywords, hashtags, and @handles that are relevant to a given topic. If a Tweet contains the text we’ve specified, it will be labeled appropriately. This differs from a machine learning approach where a model is trained specifically to classify text (in this case, Tweets) and produce a probability score alongside the output/classification.  
  

**How do I know that your data is complete and trustworthy?**  

Twitter's annotations are curated by domain experts using research and QA processes that have been refined over the course of several years. The process is supported by custom tooling to scale data tracking as far as we are able to maintain excellent precision and recall. In addition, our data is audited regularly by an internal team, having received a precision score of ~80% for the past several quarters.

 **How do you ensure precision?**

Team members QA our entities on a daily basis to ensure high precision and recall. Additionally, our work is audited quarterly by an internal team, which manually reviews 10,000 Tweets across all of our domains to calculate a precision score.

**How do you decide what to track?**

For some domains, like sports and TV, we rely on automated ingest to build out our graph. In the News domain, we track data around stories published by the Twitter Moments team. Otherwise, the team uses a variety of research methods to identify topics to track that garner a high amount of conversation on the platform.

**What historical support is available with Tweet Annotations?**

Data tracking begins the moment an entity is published; therefore, we do not annotate Tweets that were published prior to a given entity being tracked. For example, if an upstart brand/company is added to the taxonomy, we will not retroactively annotate Tweets about that brand prior to when the annotation was added.

**Is Twitter able to annotate Tweets in non-english languages? If so, which languages and does the coverage of Tweets being annotated change?**

Yes. Language coverage can vary depending on the domain and the market. English and Japanese are included in the majority of the biggest entities. Below, is a list of the languages and main markets that are covered today:

1. English (US, UK)
2. Japanese (Japan)
3. Portuguese (Brazil)
4. Spanish (Argentina, Mexico, Spain)
5. Hindi (India)
6. Arabic (Saudi Arabia)
7. Turkish (Turkey)
8. Indonesian (Indonesia)
9. Russian (Russia)
10. French (France)

Coming soon (~H2 2021):

1. German (Germany)
2. Tamil (India)

Below is a table of the top 15 countries ordered by the most coverage of annotated Tweets:

| Rank | Country code | Country | % of Tweets annotated |
| --- | --- | --- | --- |
| 1   | IN  | India | 41% |
| 2   | VN  | Vietnam | 36% |
| 3   | GB  | Great Britain | 36% |
| 4   | EC  | Ecuador | 35% |
| 5   | PE  | Peru | 33% |
| 6   | US  | United States | 32% |
| 7   | CA  | Canada | 32% |
| 8   | AU  | Australia | 31% |
| 9   | JP  | Japan | 31% |
| 10  | PH  | Philippines | 30% |
| 11  | SG  | Singapore | 30% |
| 12  | MY  | Malaysia | 30% |
| 13  | MX  | Mexico | 30% |
| 14  | gb  | Great Britain | 29% |
| 15  | NG  | Nigeria | 29% |

**What underlying "semantics" does Twitter rely on to annotate a Tweet?**

Tweet annotations consist of the following semantics to annotate a Tweet:

* Accounts - we can annotate tweets from a given handle or mentioning this handle
* Hashtags
* Keywords/phrases

For customers that are familiar with the filtered steaming APIs such as PowerTrack, the semantics used by annotations are similar in principle to the boolean rules defined to filter a stream of Tweets. If a Tweet matches the underlying semantic conditions, it will be tagged accordingly.

**Why do some Tweets have entities associated with them while others do not?**

The goal is to annotate as many Tweets as possible; however, there are several reasons why some Tweets are not annotated:

* Some Tweets aren't semantically rich enough to be labelled and can't be tagged with our current annotation rules
* Some Tweets aren't topical
* The Tweet is about a very ephemeral topic that's not in our graph
* We don't cover the language/market
* We cover the language/market but we're missing a topic or a specific term/account/hashtag related to a topic we already track"

**When there are multiple domains (for example, \[3,30\]), does the Entity ID remain the same?**

An entity can be part of multiple domains. The domain IDs will change but the entity ID remains the same. Donald Glover is a person (domain 10), an actor (domain 56)  and a musician (domain 54) but his entity ID is still 875072662527029248.

**Do you have an established timeline for show/movie tracking? In other words, how long is a show/movie tracked before/after release?**

Tracking starts a month prior to the release. For popular blockbusters, like a Marvel movie, we can start tracking them as soon as they start teasing about an upcoming release.

**Do movies have a locale filter similar to the one for TV shows?**

No, they do not.

Metrics

Overview
--------

The metrics field allows developers to access public and private engagement metrics for Tweet and media objects. Public metrics are accessible by anyone with a developer account while private metrics are accessible from owned/authorized accounts (definition below). By metrics, we mean the total count of impressions, Retweets, Quote Tweets, likes, replies, video views, video view quartiles, URL and profile link clicks for each Tweet specified in the request. There is also the option to view a breakdown of metrics earned in an organic or promoted context, if the Tweet was promoted as an [Ad](https://ads.twitter.com/).

Public metrics can be requested with [App only Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0) authentication. Non-public metrics can be requested for owned/authorized Tweets only. This means developers are required to authenticate using [OAuth 2.0](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code) or [OAuth 1.0a](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) user context authorization.

**Non-public, organic, and promoted metrics are only available for Tweets that have been created within the last 30 days.  
** 

### Terminology

* **Authorized account**: Twitter account that has authorized your [Twitter developer app](https://developer.twitter.com/en/docs/apps/overview) by granting it access to that account (any [app permission level](https://developer.twitter.com/en/docs/apps/app-permissions) will permit access to Tweet metrics). This can be achieved using the [Authorization Code Flow with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/user-access-token) or [3-legged OAuth](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens) process.
* **Owned account**: Twitter account linked to your [Twitter developer app](https://developer.twitter.com/en/docs/apps/overview).
* **Public metrics**: Metrics’ totals that are available for anyone to access on [Twitter](https://twitter.com/home), such as number of likes and number of Retweets.
* **Non-public metrics**: Metrics’ totals that are not available for anyone to view on [Twitter](https://twitter.com/home), such as number of impressions and video view quartiles. Requires [OAuth 2.0](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code) or [OAuth 1.0a](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) user context authentication.
* **Organic metrics**: Grouping of public and non-public metrics attributed to an organic context (posted and viewed in a regular manner). Requires [OAuth 2.0](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code) or [OAuth 1.0a](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) user context authentication.
* **Promoted metrics**: Grouping of public and non-public metrics attributed to a promoted context (posted or viewed as part of an Ads campaign). Requires [OAuth 2.0](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code) or [OAuth 1.0a](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) user context authentication and that the Tweet was promoted in an Ad. Promoted metrics are not included in these counts when a Twitter user is using their own Ads account to promote another Twitter user's Tweets. Promoted metrics are included in these counts when:
    * a Twitter user promotes their own Tweets
    * in an Ads account for a specific handle, the admin for that account may add another Twitter user as an account user so this second account user can promote Tweets for the handle

Available Metrics
-----------------

|     |     |     |
| --- | --- | --- |
| **Metric** | **API Representations** | **Description** |
| Impressions | `data.non_public_metrics.impression_count      data.organic_metrics.impression_count      data.promoted_metrics.impression_count` | A count of how many times the Tweet has been viewed (not unique by user). A view is counted if any part of the Tweet is visible on the screen.<br><br>This is a private, or non-public, metric and always requires OAuth 1.0a User Context authentication.<br><br>Using the `non_public_metrics` field, this returns the total count of impressions from both organic and paid contexts.<br><br>Using the `organic_metrics` field, this returns the count of impressions from organic contexts.<br><br>Using the `promoted_metrics` field, this returns the count of impressions from promoted contexts. |
| Retweets | `data.public_metrics.retweet_count      data.organic_metrics.retweet_count      data.promoted_metrics.retweet_count` | A count of how many times the Tweet has been Retweeted. Please note: This does not include Quote Tweets (“Retweets with comment”). To get the "Retweets and comments" total as displayed on the Twitter clients, simply add `retweet_count` and `quote_count`.<br><br>Using the `public_metrics` field, this will return the total count of Retweets from both organic and paid contexts, in order to maintain consistency with the counts shown publicly on Twitter.<br><br>Using the `organic_metrics` field, this returns the total count of Retweets from organic contexts.<br><br>Using the `promoted_metrics` field, this returns the total count of Retweets from paid contexts. |
| Quote Tweets | `data.public_metrics.quote_count` | A count of how many times the Tweet has been Retweeted with a new comment (message). Please note: This does not include Retweets. To get the “Retweets and comments” total as displayed on the Twitter clients, simply add `retweet_count` and `quote_count`.<br><br>This will return the total count of Quote Tweets. There are no Quote Tweets from a paid context so all Quote Tweets are organic. |
| Likes | `data.public_metrics.like_count      data.organic_metrics.like_count      data.promoted_metrics.like_count` | A count of how many times the Tweet has been liked.<br><br>Using the `public_metrics` field, this will return the total count of likes from both organic and paid contexts, in order to maintain consistency with the counts shown publicly on Twitter.<br><br>Using the `organic_metrics` field, this returns the total count of Retweets from organic contexts.<br><br>Using the `promoted_metrics` field, this returns the total count of Retweets from paid contexts. |
| Replies | `data.public_metrics.reply_count      data.organic_metrics.reply_count      data.promoted_metrics.reply_count` | A count of how many times the Tweet has been replied to.<br><br>Using the `public_metrics` field, this will return the total count of replies from both organic and paid contexts, in order to maintain consistency with the counts shown publicly on Twitter.<br><br>Using the `organic_metrics` field, this returns the total count of replies from organic contexts.<br><br>Using the `promoted_metrics` field, this returns the total count of replies from paid contexts. |
| URL Link Clicks | `data.non_public_metrics.url_link_clicks      data.organic_metrics.url_link_clicks      data.promoted_metrics.url_link_clicks` | A count of the number of times a user clicks on a URL link or URL preview card in a Tweet.<br><br>This is a private, or non-public, metric and always requires OAuth 1.0a User Context authentication.<br><br>Using the `non_public_metrics` field, this returns the total count of URL link clicks from both organic and paid contexts.<br><br>Using the `organic_metrics` field, this returns the count of URL link clicks from organic contexts.<br><br>Using the `promoted_metrics` field, this returns the count of URL link clicks from paid contexts. |
| User Profile Clicks | `data.non_public_metrics.user_profile_clicks      data.organic_metrics.user_profile_clicks      data.promoted_metrics.user_profile_clicks` | A count of the number of times a user clicks the following portions of a Tweet: display name, user name, profile picture.<br><br>This is a private, or non-public, metric and always requires OAuth 1.0a User Context authentication.<br><br>Using the `non_public_metrics` field, this returns the total count of user profile clicks from both organic and paid contexts.<br><br>Using the `organic_metrics` field, this returns the count of user profile clicks from organic contexts.<br><br>Using the `promoted_metrics` field, this returns the count of user profile clicks from paid contexts. |
| Video views | `includes.media.public_metrics.view_count      includes.media.organic_metrics.view_count      includes.media.promoted_metrics.view_count` | A count of how many times the video included in the Tweet has been viewed.<br><br>This is the number of video views aggregated across all Tweets in which the given video has been posted. That means that the metric includes the combined views from any instance where the video has been Retweeted or reposted in separate Tweets.<br><br>Use expansion for media objects, `expansions=attachment.media_keys`.<br><br>Using the `public_metrics` field, this returns the total count of video views from both organic and paid contexts, in order to maintain consistency with the counts shown publicly on Twitter.<br><br>Using the `organic_metrics` field, this returns the total count of video views from organic contexts.<br><br>Using the `promoted_metrics` field, this returns the total count of video views from paid contexts. |
| Video view quartiles | `includes.media.non_public_metrics.playback_0_count   includes.media.non_public_metrics.playback_25_count   includes.media.non_public_metrics.playback_50_count   includes.media.non_public_metrics.playback_75_count   includes.media.non_public_metrics.playback_100_count`<br><br>  <br><br>`includes.media.organic_metrics.playback_0_count   includes.media.organic_metrics.playback_25_count   includes.media.organic_metrics.playback_50_count   includes.media.organic_metrics.playback_75_count   includes.media.organic_metrics.playback_100_count`<br><br>  <br><br>`includes.media.promoted_metrics.playback_0_count   includes.media.promoted_metrics.playback_25_count   includes.media.promoted_metrics.playback_50_count   includes.media.promoted_metrics.playback_75_count   includes.media.promoted_metrics.playback_100_count   ` | The number of users who played through to each quartile in a video. This reflects the number of quartile views across all Tweets in which the given video has been posted.<br><br>This is a private, or non-public, metric and always requires OAuth 1.0a User Context authentication.<br><br>Use expansion for media objects, `expansions=attachment.media_keys`.<br><br>Using the `non_public_metrics` field, this returns the total count of video view quartiles from both organic and paid contexts.<br><br>Using the `organic_metrics` field, this returns the total count of video view quartiles from organic contexts.<br><br>Using the `promoted_metrics` field, this returns the total count of video view quartiles from paid contexts. |

Requesting metrics
------------------

### Public metrics

In the following request, we are requesting public metrics on the Tweet and on the attached video with the following fields and expansion. Be sure to replace `$BEARER_TOKEN` with your own generated bearer token.

* tweet.fields=public\_metrics
* expansions=attachments.media\_keys&media.fields=public\_metrics

#### Sample Request

      `curl 'https://api.twitter.com/2/tweets?ids=1204084171334832128&tweet.fields=public_metrics&expansions=attachments.media_keys&media.fields=public_metrics' --header 'Authorization: Bearer $BEARER_TOKEN'`
    

**Sample Response**

      `{     "data": [         {             "id": "1204084171334832128",             "text": "Tired of reading? We’ve got you covered. Learn about the capabilities of the Account Activity API in this video walkthrough with @tonyv00 from our DevRel team. 🍿 ⬇️ https://t.co/LdHy4aLu0i",             "public_metrics": {                 "retweet_count": 9,                 "reply_count": 2,                 "like_count": 49,                 "quote_count": 1             },             "attachments": {                 "media_keys": [                     "13_1204080851740315648"                 ]             }         }     ],     "includes": {         "media": [             {                 "media_key": "13_1204080851740315648",                 "public_metrics": {                     "view_count": 1808                 },                 "type": "video"             }         ]     } }`
    

### Private metrics (non-public, organic metrics)

In the following request, we are requesting non-public metrics with more details or organic metrics, meaning which of these metrics were generated in an organic context, on the Tweet and attached video with the following fields and expansion. Since these fields are private (not available to view on Twitter.com),Requires [OAuth 2.0](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code) or [OAuth 1.0a](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) user context authentication. is required for the request. Check out our [guide](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/creating-a-signature) that explains how to generate the OAuth 1.0a signature sampled below.

* `tweet.fields=non_public_metrics,organic_metrics`
* `expansions=attachments.media_keys&media.fields=non_public_metrics,organic_metrics`

**Sample Request**

      `curl 'https://api.twitter.com/2/tweets/1204084171334832128?tweet.fields=non_public_metrics,organic_metrics&media.fields=non_public_metrics,organic_metrics&expansions=attachments.media_keys' --header 'authorization: OAuth oauth_consumer_key="CONSUMER_API_KEY", oauth_nonce="OAUTH_NONCE", oauth_signature="OAUTH_SIGNATURE", oauth_signature_method="HMAC-SHA1", oauth_timestamp="OAUTH_TIMESTAMP", oauth_token="ACCESS_TOKEN", oauth_version="1.0"'`
    

**Sample Response**

      `{   "data": {     "attachments": {       "media_keys": [         "13_1204080851740315648"       ]     },     "id": "1263145271946551300",     "non_public_metrics": {       "impression_count": 956,       "url_link_clicks": 9,        "user_profile_clicks": 34     },     "organic_metrics": {       "impression_count": 956,       "like_count": 49,       "reply_count": 2,       "retweet_count": 9,       "url_link_clicks": 9,        "user_profile_clicks": 34     },     "text": "test"   },   "includes": {     "media": [       {         "media_key": "13_1204080851740315648",         "non_public_metrics": {           "playback_0_count": 0,           "playback_100_count": 1,           "playback_25_count": 2,           "playback_50_count": 1,           "playback_75_count": 1         },         "organic_metrics": {           "playback_0_count": 0,           "playback_100_count": 1,           "playback_25_count": 2,           "playback_50_count": 1,           "playback_75_count": 1,           "view_count": 1         },         "type": "video"       }     ]   } }`

Conversation ID

Conversation threads using the Twitter API
------------------------------------------

If you look at how conversations evolve on Twitter, one Tweet can spark several conversation threads, each of which can grow in length and complexity as more people chime in. Identifying relationships between Tweets and understanding conversation threads is a feature of the Twitter API v2 payload and search capabilities.  When Tweets are posted in response to a Tweet (known as a reply), or in response to a reply, there is now a defined conversation\_id on each reply, which matches the Tweet ID of the original Tweet that started the conversation. 

Replies to a given Tweet, as well as replies to those replies, are all included in the conversation stemming from the single original Tweet. Regardless of how many reply threads result, they will all share a common conversation\_id to the original Tweet that sparked the conversation. Using the Twitter API v2, you have the ability to retrieve and reconstruct an entire conversation thread, so that you can better understand what is being said, and how conversations and ideas evolve.   
 

#### The example below shows a conversation thread of five different people, including one reply to a reply:  
 

      `{ 	"data": [{ 			"conversation_id": "1279944223114900000", 			"in_reply_to_user_id": "1102323333", 			"author_id": "63044444", 			"created_at": "2020-07-06T15:58:10.000Z", 			"id": "1280169177479744444", 			"referenced_tweets": [{ 				"type": "replied_to", 				"id": "1280155225706433333" 			}], 			"text": "@ThirdPerson333 @OriginalPerson000 Reply to the third reply!" 		}, 		{ 			"conversation_id": "1279944223114900000", 			"in_reply_to_user_id": "3001960000", 			"author_id": "1102323333", 			"created_at": "2020-07-06T15:02:44.000Z", 			"id": "1280155225706433333", 			"referenced_tweets": [{ 				"type": "replied_to", 				"id": "1279944223114900000" 			}], 			"text": "@OriginalPerson000 Third reply" 		}, 		{ 			"conversation_id": "1279944223114900000", 			"in_reply_to_user_id": "3001960000", 			"author_id": "199562222", 			"created_at": "2020-07-06T15:02:36.000Z", 			"id": "1280155190306340864", 			"referenced_tweets": [{ 				"type": "replied_to", 				"id": "1279944223114900000" 			}], 			"text": "@OriginalPerson000 Second Reply" 		}, 		{ 			"conversation_id": "1279944223114900000", 			"in_reply_to_user_id": "3001960000", 			"author_id": "179201111", 			"created_at": "2020-07-06T01:10:15.000Z", 			"id": "1279945722494811111", 			"referenced_tweets": [{ 				"type": "replied_to", 				"id": "1279944223114900000" 			}], 			"text": "@OriginalPerson000 First Reply" 		} 	], 	"includes": { 		"users": [{ 				"name": "Original person", 				"id": "3001960000", 				"username": "OriginalPerson000" 			}, 			{ 				"name": "First person", 				"id": "179201111", 				"username": "FirstPerson111" 			}, { 				"name": "Second person", 				"id": "199562222", 				"username": "SecondPerson222" 			}, { 				"name": "Third person", 				"id": "1102323333", 				"username": "ThirdPerson333" 			}, { 				"name": "Fourth person", 				"id": "63044444", 				"username": "FourthPerson444" 			}  		], 		"tweets": [{ 				"conversation_id": "1279944223114900000", 				"in_reply_to_user_id": "3001960000", 				"author_id": "1102323333", 				"created_at": "2020-07-06T15:02:44.000Z", 				"id": "1280155225706433333", 				"referenced_tweets": [{ 					"type": "replied_to", 					"id": "1279944223114900000" 				}], 				"text": "@OriginalPerson000 Third reply" 			}, 			{ 				"conversation_id": "1279944223114900000", 				"author_id": "3001960000", 				"created_at": "2020-07-06T01:04:17.000Z", 				"id": "1279944223114900000", 				"text": "This is the original post" 			} 		] 	}, 	"meta": { 		"newest_id": "1280169177479744444", 		"oldest_id": "1279945722494811111", 		"result_count": 4 	} }`
    

###   
Retrieving conversation\_id as a tweet.fields parameter

To request the conversation\_id for all Tweets returned on a v2 endpoint, the tweet.fields=conversation\_id field can be added to the request parameters.  The conversation\_id field is always the Tweet ID of the original Tweet in the conversation reply thread.  All Tweets within the same reply thread, including reply threads that are created from earlier reply threads, will show the same conversation\_id.  
 

#### Request with conversation\_id parameter  
 

      `curl --request GET \   --url 'https://api.twitter.com/2/tweets?ids=1225917697675886593&tweet.fields=author_id,conversation_id,created_at,in_reply_to_user_id,referenced_tweets&expansions=author_id,in_reply_to_user_id,referenced_tweets.id&user.fields=name,username' \   --header 'Authorization: Bearer $ACCESS_TOKEN'` 
    

####   
Response  
 

      `{     "data": [         {             "id": "1225917697675886593",             "text": "@TwitterEng *ahem* https://t.co/aroJHt2zQ1",             "created_at": "2020-02-07T23:02:10.000Z",             "author_id": "2244994945",             "in_reply_to_user_id": "6844292",             "conversation_id": "1225912275971657728",             "referenced_tweets": [                 {                     "type": "quoted",                     "id": "1200517737669378053"                 },                 {                     "type": "replied_to",                     "id": "1225912275971657728"                 }             ]         }     ],     "includes": {         "users": [             {                 "username": "TwitterDev",                 "name": "Twitter Dev",                 "id": "2244994945"             },             {                 "username": "TwitterEng",                 "name": "Twitter Engineering",                 "id": "6844292"             }         ],         "tweets": [             {                 "id": "1200517737669378053",                 "text": "|￣￣￣￣￣￣￣￣￣￣￣|\n             don't push            \n             to prod on            \n               Fridays                  \n|＿＿＿＿＿＿＿＿＿＿＿| \n(\\__/)  ||\n(•ㅅ•) ||\n/ 　 づ",                 "created_at": "2019-11-29T20:51:47.000Z",                 "author_id": "2244994945",                 "conversation_id": "1200517737669378053"             },             {                 "id": "1225912275971657728",                 "text": "Note to self: Don't deploy on Fridays",                 "created_at": "2020-02-07T22:40:37.000Z",                 "author_id": "6844292",                 "conversation_id": "1225912275971657728"             }         ]     } }`
    

###   
Using conversation\_id as a filter operator

The conversation\_id can be used as a search query parameter when using either recent search or as an operator within a rule for filtered stream.  Using the operator on its own will result in the entire conversation thread of Tweets being returned in either real time through [filtered stream](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/introduction.html), or paginated in reverse chronological order from [search Tweets](https://developer.twitter.com/en/docs/twitter-api/tweets/search/introduction.html). You can also receive a count of the Tweets in a conversation using this operator with [Tweet counts](https://developer.twitter.com/en/docs/twitter-api/tweets/counts).

Additional operators can be added to the query/rule, in conjunction with the conversation\_id operator, however these will apply only to the Tweets that are part of that conversation.  Only one conversation\_id can be specified at a time without an OR clause within the query/rule.

Reconstructing the conversation can be done by ordering the Tweets with a matching conversation\_id by timestamp, and taking note of which Tweets are directly in reply to other Tweets in the conversation thread. This can be accomplished by also requesting the in\_reply\_to\_user\_id field and referenced\_tweets.id and in\_reply\_to\_user\_id expansions.

  
Request to query by conversation\_id  

      `curl --request GET \   --url 'https://api.twitter.com/2/tweets/search/recent?query=conversation_id:1279940000004973111&tweet.fields=in_reply_to_user_id,author_id,created_at,conversation_id' \   --header 'Authorization: Bearer $ACCESS_TOKEN'` 
    

####   
Response

_**Note**: Results for search Tweets are in reverse chronological order._ 

      `{ 	"data": [{ 			"id": "1280169000000704333", 			"text": "@attributeisland @iterationjoe What beautiful creatures! Happy #seaturtleweek", 			"conversation_id": "1279940000004973111", 			"public_metrics": { 				"retweet_count": 0, 				"reply_count": 0, 				"like_count": 7, 				"quote_count": 0 			} 		}, 		{ 			"id": "1280166000000519222", 			"text": "@attributeisland \"One touch of nature makes the whole world kin.\" -John Muir", 			"conversation_id": "1279940000004973111", 			"public_metrics": { 				"retweet_count": 0, 				"reply_count": 1, 				"like_count": 1, 				"quote_count": 0 			} 		}, 		{ 			"id": "1280166000000519221", 			"text": "@attributeisland I love turtles!", 			"conversation_id": "1279940000004973111", 			"public_metrics": { 				"retweet_count": 1, 				"reply_count": 0, 				"like_count": 4, 				"quote_count": 0 			} 		}, 		{ 			"id": "1280166000000519220", 			"text": "@attributeisland Turtlemoji🐢", 			"conversation_id": "1279940000004973111", 			"public_metrics": { 				"retweet_count": 0, 				"reply_count": 0, 				"like_count": 1, 				"quote_count": 0 			} 		}, 		{ 			"id": "1279940000004973111", 			"text": "Sea turtles are roaming in our waters!", 			"conversation_id": "1279940000004973111", 			"public_metrics": { 				"retweet_count": 67, 				"reply_count": 11, 				"like_count": 396, 				"quote_count": 2 			} 		} 	], 	"meta": { 		"newest_id": "1280169000000704333", 		"oldest_id": "1279940000004973111", 		"result_count": 5 	} }`

Pagination

Introduction
------------

Pagination is a feature in Twitter API v2 endpoints that return more results than can be returned in a single response. When that happens, the data is returned in a series of 'pages'. Pagination refers to methods for programatically requesting all of the pages, in order to retrieve the entire result data set. Not all API endpoints support or require pagination, but it is often used when result sets are large.  
  

### Use cases for pagination

**To retrieve all results for a request:** Pagination should most often be used to receive all relevant data related to a specific request and parameters. Pagination is required in cases where there are more matching results than the max\_results for a request. Integrating pagination token data into looping requests will allow you to retrieve all results. Once a response is returned without a next\_token value, it can be assumed that all results have been paged through. Pagination should not be used for polling purposes. To get the most recent results since a previous request, review polling with since\_id.

**To traverse through the results of a request:** Pagination provides directional options for navigating through results from a request, using next\_token and previous\_token values from responses. These tokens can be set as the pagination\_token in the following request, to go to the next or the previous page of results.  
  

### Pagination token definitions

next\_token - Opaque string returned within the meta object response on endpoints which support pagination. Indicates that more results are available and can be used as the pagination\_token parameter in the next request to return the next page of results. The last page of results will not have a next\_token present.

previous\_token - Opaque string returned within the meta object response on endpoints which support pagination. Indicates that there is a previous page of results available, and can be set as the pagination\_token parameter in the next request to return the previous page of results.

pagination\_token - Parameter used in pagination requests. Set to the value of next\_token for the next page of results. Set to the value of previous\_token for the previous page of results.  
  

### Fundamentals of pagination

* Endpoints which use pagination, will respond to an initial request with the first page of results, and provide a next\_token within the meta object in the JSON response if additional pages of results are available. To receive all results, this process can be repeated until no next\_token is included in the response.

* Results are delivered in reverse-chronological order. This is true within individual pages, as well as across multiple pages:
    * The first Tweet in the first response will be the most recent.
    * The last Tweet in the last response will be the oldest.

* The max\_results request parameter enables you to configure the number of Tweets returned per response page. There will be a default max\_results and a maximum max\_results.
    
* Every pagination implementation will involve parsing tokens from the response payload, which can be used in subsequent requests. See below for more details on how to construct these requests.

* In some circumstances you may get less than the max\_results page of results. Do not rely on the results per page to always equal the max\_results parameter value.
    
* The best ways to successfully use pagination for complete results are by using loop logic within integration code, or by using a [library](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries) that supports Twitter API v2.  
     
    

### Pagination example

Here, there are three pages of results because max\_results is set to 100 and there are a total of ~295 Tweets created by user ID 2244994945 (@TwitterDev) between January 1st, 2019 at 17:00:00 UTC and December 12th at 00:00:00 UTC. The first Tweet on the first page (1337498609819021312) is the most recent, and the last Tweet on the third page of results (1082718487011885056) is the oldest.  
 

#### Initial request

      `https://api.twitter.com/2/users/2244994945/tweets?tweet.fields=created_at&max_results=100&start_time=2019-01-01T17:00:00Z&end_time=2020-12-12T01:00:00Z`
    

#### Sequence

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
|     | **First Request** | **Second page** | **Third page** | **Fourth page** |
| **Request Parameters** | max\_results\=100<br><br>tweet.fields\=created\_at<br><br>start\_time\=2019-01-01T17:00:00Z<br><br>end\_time\=2020-12-12T01:00:00Z | max\_results\=100<br><br>tweet.fields\=created\_at<br><br>start\_time\=2019-01-01T17:00:00Z<br><br>end\_time\=2020-12-12T01:00:00Z<br><br>pagination\_token\=7140w | max\_results\=100<br><br>tweet.fields\=created\_at<br><br>start\_time\=2019-01-01T17:00:00Z<br><br>end\_time\=2020-12-12T01:00:00Z<br><br>pagination\_token\=7140k9 | max\_results\=100<br><br>tweet.fields\=created\_at<br><br>start\_time\=2019-01-01T17:00:00Z<br><br>end\_time\=2020-12-12T01:00:00Z<br><br>pagination\_token\=71408hi |
| **Response** | {<br>  "data": \[<br>    {<br>      "created\_at": "2020-12-11T20:44:52.000Z",<br>      "id": "1337498609819021312",<br>      "text": "Thanks to everyone who tuned in today..."<br>    },<br>    .<br>    .<br>    .<br>   {<br>      "created\_at": "2020-05-06T17:24:31.000Z",<br>      "id": "1258085245091368960",<br>      "text": "It’s now easier to understand Tweet impact..."<br>    }<br>  \],<br>  "meta": {<br>    "oldest\_id": "1258085245091368960",<br>    "newest\_id": "1337498609819021312",<br>    "result\_count": 100,<br>    "next\_token": "7140w"<br>  }<br>} | {<br>  "data": \[<br>    {<br>      "created\_at": "2020-04-29T17:01:44.000Z",<br>      "id": "1255542797765013504",<br>      "text": "Our developer community is full of inspiring ideas..."<br>    },<br>    .<br>    .<br>    .<br>    {<br>      "created\_at": "2019-11-21T16:17:23.000Z",<br>      "id": "1197549579035496449",<br>      "text": "Soon, we'll be releasing tools in..."<br>    }<br>  \],<br>  "meta": {<br>    "oldest\_id": "1197549579035496449",<br>    "newest\_id": "1255542797765013504",<br>    "result\_count": 100,<br>    "next\_token": "7140k9",<br>    "previous\_token": "77qp8"<br>  }<br>} | {<br>  "data": \[<br>    {<br>      "created\_at": "2019-11-21T16:17:23.000Z",<br>      "id": "1197549578418941952",<br>      "text": "We know that some people who receive a large volume of replies may..."<br>    },<br>    .<br>    .<br>    .<br>    { <br>      "created\_at": "2019-01-08T19:19:37.000Z",<br>      "id": "1082718487011885056",<br>      "text": "Updates to Grid embeds..."<br>    }<br>  \],<br>  "meta": {<br>    "oldest\_id": "1082718487011885056",<br>    "newest\_id": "1197549578418941952",<br>    "result\_count": 95,<br>    "next\_token": "71408hi",<br>    "previous\_token": "77qplte"<br>  }<br>} | {<br> "meta": {<br>    "result\_count": 0,<br>    "previous\_token": "77qpw8l"<br>  }<br>} |
| **Actions to take for next request** | To get the next page, take the next\_token value directly from the response (7140w) and set it as the pagination\_token for the next request call. | To continue to get all results: take the next\_token value directly from the response (7140k9) and set it as the pagination\_token for the next request call.  <br>  <br>  <br>To traverse to previous page: take the previous\_token value directly from the response (77qp8) and set it as the pagination\_token for the next request call. | To continue to get all results: take the next\_token value directly from the response (71408hi) and set it as the pagination\_token for the next request call.  <br>  <br>  <br>To traverse to previous page: take the previous\_token value directly from the response (77qplte) and set it as the pagination\_token for the next request call. | Note that there is no next\_token, which indicates that all results have been received.  <br>  <br>  <br>To traverse to previous page: take the previous\_token value directly from the response (77qpw8l) and set it as the pagination\_token for the next request call. |

Versioning

Along with Twitter API v2, we launched a new versioning strategy that enables developers to better understand when to expect changes to Twitter’s public APIs, and when they will need to migrate to new versions. 

Developers will be notified of deprecations, retirements, changes, and additions to the Twitter API via our [communication channels](https://developer.twitter.com/en/updates/stay-informed) so they can appropriately plan to accommodate these changes in their development roadmap. All changes to the API will be noted in the changelog.

The Twitter API currently has three different versions. We strongly encourage users to utilize Twitter API v2 when planning their integration unless we have not released functionality to v2 that is required by your use case. 

To learn more about each version, please visit the following pages:

* [Twitter API v2](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api)
* Twitter API v1.1 ([standard](https://developer.twitter.com/en/docs/twitter-api/v1) and [premium](https://developer.twitter.com/en/docs/twitter-api/premium))
* Gnip 2.0 ([enterprise](https://developer.twitter.com/en/docs/twitter-api/enterprise))

Versioning Strategy
-------------------

Versioning for the Twitter API will be represented by version numbers declared in the route path for our endpoints:

https://api.twitter.com/2/tweets

We aim to release major versions of the Twitter API as necessary but no more frequently than every 12 months. A major version will be released when breaking changes are introduced in the API. We will publish migration guides when launching a new major version to help developers migrate over to the new version. 

A breaking change requires developers to change their code to maintain existing functionality in their app. Non-breaking changes will be additive and rolled out to the most recent version when ready, requiring no work on a developer’s end unless you would like to take advantage of the new functionality.

If a breaking change must be rolled out mid-cycle (for security or privacy reasons), this change will be made to the most recent version.  
 

### Breaking changes

These changes require developers to change their code to maintain existing functionality of their application.

* Addition of a new required parameter
* Removal of an existing endpoint
* Removal of any field in the response (either required or optional)
* Removal of a query parameter
* Restructuring of the input or output format (for example, making a top-level field a sub-field, or changing the location of errors to be inline)
* Changing the name or data type of an existing input parameter or output value
* Changing the name of a field
* Changing the resource name
* Changing a response code
* Changing error types
* Changes to existing authorization scopes  
    

### Non-breaking changes

* Addition of a new endpoint
* Addition of a new optional parameter
* Addition of a new response field
* Changing text in error messages
* Availability of new scopes
* “Nulling” of fields (changing the value of a to null for privacy/security reasons as an alternative to removing it altogether)

### Deprecation and retirement

First of all, here is our definition of what deprecation and retirement mean to the Twitter API:

* **Deprecation:** The feature is no longer supported by the team. No new functionality will be released around that feature, and if there are any bugs or issues with the product, the chances that we will explore a fix are extremely low. 
* **Retired:** The feature will no longer be accessible.

In most cases, as soon as a new version is released, the previous version will be marked as deprecated. Versions will remain in a deprecated state for a period of time, after which they will be retired. 

Please [stay informed](https://developer.twitter.com/en/updates/stay-informed) to learn more about future deprecations and retirements.

Consistency

Consistency across the Twitter API v2 endpoints
-----------------------------------------------

One of the main aspects of the new v2 version of the Twitter API is consistency across endpoints. This means that objects returned, features, and behaviors of the API are uniform across similar endpoints.

You can expect the following elements to be the same across all endpoints:

* **Path naming** always includes the endpoint [version](https://developer.twitter.com/en/docs/twitter-api/versioning.html), followed by the **resource**. Beyond that, the path can contain an **ID** that relates to the earlier resource, a **selection verb** which helps to determine which data to return (for example, `search` or `sample`), a **delivery verb** which helps to determine how the data will deliver (for example, `stream`), or other resources that have a **relationship** with the primary resource (for example, /user/12/tweets). Finally, you can append a **query parameter** to the end if the endpoint includes any query parameters.  
      
    Here are some examples of how these path and query items could be organized:  
      
    `/version/resource/id?param1=value&param2=value`  
      
    `/version/resource/delivery/selection?param1=value&param2=value`  
      
    Here are some examples of what this might look like in your actual requests:  
      
    `/2/tweets/1067094924124872705?expansions=attachments.media_keys&tweet.fields=author_id`  
      
    `/2/users/2244994945?user.fields=created_at,description`  
      
    `/2/tweets/search/stream`  
      
    `/2/tweets/search/recent?query=snow`  
    

* **JSON Schema**  
    Responses to requests are defined using [JSON Schema](http://json-schema.org/). This means that requests consistently return sets of objects as arrays, with each element having an ID. Requests do not return maps with IDs as keys.  
    
* **Response object and parameters**  
    The default object returned is the same for each endpoint of that object type:
    
    * `id` objects are always strings.
    * Parameters and response fields consistently use American-English spelling.
    * Fields are empty or not returned if there is no value.
    * The `entities` object only contains entities sourced from the Tweet text: this includes `urls`, `hashtags`, `mentions` and `cashtags`.
    * All cards-related information, including the `media_keys` and `poll_ids` fields, are returned in the `attachments` object.

Here is an example response object from the [single Tweet lookup](https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/api-reference/get-tweets-id.html) endpoint (with the [tweet.fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet.html) parameter set to `author_id,``entities`):

      `{    "data": {        "id": "1278747501642657792",        "text": "It's been a year since Twitter's Developer Labs launched.\n\nAs we build towards the next generation of the #TwitterAPI (coming VERY soon), see what we've learned and changed along the way. https://t.co/WvjuEWCa6G",        "author_id": "2244994945",        "entities": {            "urls": [                {                    "start": 188,                    "end": 211,                    "url": "https://t.co/WvjuEWCa6G",                    "expanded_url": "https://blog.twitter.com/developer/en_us/topics/tools/2020/a-year-with-twitter-developer-labs.html",                    "display_url": "blog.twitter.com/developer/en_u…",                    "images": [                        {                            "url": "https://pbs.twimg.com/news_img/1278747527043362816/7HQRkQeV?format=jpg&name=orig",                            "width": 1600,                            "height": 600                        },                        {                            "url": "https://pbs.twimg.com/news_img/1278747527043362816/7HQRkQeV?format=jpg&name=150x150",                            "width": 150,                            "height": 150                        }                    ],                    "status": 200,                    "title": "A year with Twitter Developer Labs: What we've learned and changed",                    "description": "Labs has been invaluable in helping us understand what works well and what doesn’t, what you liked and what you didn’t.",                    "unwound_url": "https://blog.twitter.com/developer/en_us/topics/tools/2020/a-year-with-twitter-developer-labs.html"                }            ],            "hashtags": [                {                    "start": 106,                    "end": 117,                    "tag": "TwitterAPI"                }            ]        }    } }`
    

* **Authentication**  
    All Twitter API v2 endpoints require authentication. Many of them accept the [OAuth 2.0 Bearer Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0.html) method. This means that you will have to pass along a Bearer Token with your request to the endpoint to make a successful request.  
      
    For those endpoints that require you to be authorized to create, manipulate, or retrieve data on behalf of another user, you will have to use [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/basics/authentication/oauth-1-0a). This means that you have to provide your [developer App’](https://developer.twitter.com/content/developer-twitter/en/docs/basics/apps/overview)s [API keys and tokens](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/api-key-and-secret), as well as a set of user [Access Tokens](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens) that you generate for the user that you are making a request on behalf of. You can use the [3-legged OAuth flow](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens) to retrieve a set of Access Tokens from a user to make requests on behalf of them. If you are building a request from scratch for and endpoint that requires OAuth 1.0a User Context, you will need to [authorize your request](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/authorizing-a-request), however, we recommend that you use a [tool or library](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries) that automatically builds this authorization header for you.  
      
    More information on authentication can be found in our documentation on [authentication](https://developer.twitter.com/en/docs/authentication).  
    
* **Fields**

The object returned on each endpoint is condensed. To allow developers more customization in the response they get back from the API, the `[fields](https://developer.twitter.com/en/docs/twitter-api/fields.html)` parameter is used to request the fields desired. Fields will remain consistent across endpoints. The Tweet object will return the same fields across all endpoints the Tweet object is returned. The same set of fields can be queried across similar endpoints. For example, the same Tweet fields can be queried in the [Tweets lookup](https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/introduction.html) and for the expanded pinned Tweet in the [Users lookup](https://developer.twitter.com/en/docs/twitter-api/users/lookup/introduction.html).

* **Expansions**  
    Where appropriate, [expansions](https://developer.twitter.com/en/docs/twitter-api/expansions.html) are available for all nested id fields (for example, all fields named `*_id`, such as `author_id`). Expansions are also available for all fields that have an id that is not the top-level identifier of the current object. For example, in the [Tweets lookup](https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/introduction.html), the Tweet is the current object with field `id` as the top-level identifier. The `author_id` or `referenced_tweets.id` fields are available to expand into complete user or Tweet objects by adding these comma-separated values to the `expansions` parameter.  
      
    

Please [report any inconsistencies](https://twitterdevfeedback.uservoice.com/) that you notice, related to these fields.

Rate limits

Every day many thousands of developers make requests to the Twitter API. To help manage the sheer volume of these requests, limits are placed on the number of requests that can be made. These limits help us provide the reliable and scalable API that our developer community relies on. 

The maximum number of requests that are allowed is based on a time interval, some specified period or window of time. The most common request limit interval is fifteen minutes. If an endpoint has a rate limit of 900 requests/15-minutes, then up to 900 requests over any 15-minute interval is allowed. 

Rate limits are applied based on which authentication method you are using. For example, if you are using [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a), you will have one limit per time period for each set of users’ [Access Tokens](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens), while if you are using [OAuth 2.0 Bearer Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0), you will have a separate limit per time period for requests made by your app. When these limits are exceeded, an error is returned. Keep reading to learn more about these details and tips on how to avoid being rate limited.   
 

### Table of contents

* [Twitter API v2 Free rate limits](#v2-limits-free)  
* [Twitter API v2 Basic rate limits](#v2-limits-basic)  
* [Twitter API v2 Pro rate limits](#v2-limits-pro)  
* [Twitter API Enterprise rate limits](#v2-limits-enterprise)  
* [Rate limits and authentication method](#auth)
* [HTTP headers and response codes](#headers-and-codes)
* [Recovering from rate limits](#recovering)
* [Tips to avoid being rate limited](#tips)

### Twitter API v2 rate limits - Free

The following table lists the rate limits for the Twitter API v2 Free access. These rate limits are also documented on each endpoint's API Reference page and also displayed in the  [developer portal](https://developer.twitter.com/en/docs/developer-portal)'s products section.

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
| **Endpoint** | **#Requests** | **Window of time** | **Per** | **Part of the Tweet pull cap?** | **Effective 30-day limit** |
| POST\_2\_tweets | 50  | 24 hours | per user | no  | 1,500 |
| 50  | 24 hours | per app | no  | 1,500 |
| DELETE\_2\_tweets\_id | 50  | 24 hours | per user | no  | 1,500 |
| 50  | 24 hours | per app | no  | 1,500 |
| GET\_2\_users\_me | 25  | 24 hours | per user | no  | 750 |

### Twitter API v2 rate limits - Basic

The following table lists the rate limits for the Twitter API v2 Basic access. These rate limits are also documented on each endpoint's API Reference page and also displayed in the  [developer portal](https://developer.twitter.com/en/docs/developer-portal)'s products section.

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
| **Endpoint** | **#Requests** | **Window of time** | **Per** | **Part of the Tweet pull cap?** | **Effective 30-day limit** |
| DELETE\_2\_lists\_param | 5   | 15 minutes | per user | no  | 14,400 |
| DELETE\_2\_lists\_param\_members\_param | 5   | 15 minutes | per user | no  | 14,400 |
| DELETE\_2\_tweets\_param | 5   | 15 minutes | per user | no  | 14,400 |
| DELETE\_2\_users\_id\_bookmarks\_tweet\_id | 5   | 15 minutes | per user | no  | 14,400 |
| DELETE\_2\_users\_param\_blocking\_param | 5   | 15 minutes | per user | no  | 14,400 |
| DELETE\_2\_users\_param\_followed\_lists\_param | 5   | 15 minutes | per user | no  | 14,400 |
| DELETE\_2\_users\_param\_following\_param | 5   | 15 minutes | per user | no  | 14,400 |
| DELETE\_2\_users\_param\_likes\_param | 5   | 15 minutes | per user | no  | 14,400 |
| 100 | 24 hours | per user | no  | 3,000 |
| DELETE\_2\_users\_param\_muting\_param | 5   | 15 minutes | per user | no  | 14,400 |
| DELETE\_2\_users\_param\_pinned\_lists\_param | 5   | 15 minutes | per user | no  | 14,400 |
| DELETE\_2\_users\_param\_retweets\_param | 5   | 15 minutes | per user | no  | 14,400 |
| GET\_2\_compliance\_jobs | 5   | 15 minutes | per app | no  | 14,400 |
| GET\_2\_compliance\_jobs\_param | 5   | 15 minutes | per app | no  | 14,400 |
| GET\_2\_dm\_conversations\_param\_dm\_events | 3   | 15 minutes | per user | no  | 8,640 |
| GET\_2\_dm\_conversations\_with\_param\_dm\_events | 3   | 15 minutes | per user | no  | 8,640 |
| GET\_2\_dm\_events | 5   | 15 minutes | per user | no  | 14,400 |
| GET\_2\_lists\_id | 5   | 15 minutes | per user | no  | 14,400 |
| 5   | 15 minutes | per app | no  | 14,400 |     |
| GET\_2\_lists\_id\_members | 5   | 15 minutes | per user | no  | 14,400 |
| 25  | 15 minutes | per app | no  | 72,000 |
| GET\_2\_lists\_id\_tweets | 5   | 15 minutes | per user | yes | 10,000 |
| 25  | 15 minutes | per app | yes | 10,000 |
| GET\_2\_spaces | 5   | 15 minutes | per user | no  | 14,400 |
| 25  | 15 minutes | per app | no  | 72,000 |
| GET\_2\_spaces\_by\_creator\_ids | 5   | 15 minutes | per user | no  | 14,400 |
| 25  | 15 minutes | per app | no  | 72,000 |
| GET\_2\_spaces\_param | 25  | 15 minutes | per app | no  | 72,000 |
| 5   | 15 minutes | per user | no  | 14,400 |
| GET\_2\_spaces\_param\_buyers | 5   | 15 minutes | per user | no  | 14,400 |
| 25  | 15 minutes | per app | no  | 72,000 |
| GET\_2\_spaces\_param\_tweets | 5   | 15 minutes | per user | no  | 14,400 |
| 25  | 15 minutes | per app | no  | 72,000 |
| GET\_2\_spaces\_search | 5   | 15 minutes | per user | no  | 14,400 |
| 25  | 15 minutes | per app | no  | 72,000 |
| GET\_2\_tweets | 15  | 15 minutes | per user | yes | 10,000 |
| 15  | 15 minutes | per app | yes | 10,000 |
| GET\_2\_tweets\_counts\_recent | 5   | 15 minutes | per app | no  | 14,400 |
| GET\_2\_tweets\_param | 15  | 15 minutes | per user | yes | 10,000 |
| 15  | 15 minutes | per app | yes | 10,000 |
| GET\_2\_tweets\_param\_liking\_users | 5   | 15 minutes | per user | no  | 14,400 |
| 25  | 15 minutes | per app | no  | 72,000 |
| GET\_2\_tweets\_param\_quote\_tweets | 5   | 15 minutes | per user | yes | 10,000 |
| 5   | 15 minutes | per app | yes | 10,000 |
| GET\_2\_tweets\_param\_retweeted\_by | 5   | 15 minutes | per app | yes | 10,000 |
| 5   | 15 minutes | per user | yes | 10,000 |     |
| GET\_2\_tweets\_search\_recent | 60  | 15 minutes | per app | yes | 10,000 |
| 60  | 15 minutes | per user | yes |     |
| GET\_2\_users | 500 | 24 hours | per app | no  | 15,000 |
| 100 | 24 hours | per user | no  | 3,000 |
| GET\_2\_users\_by | 100 | 24 hours | per user | no  | 3,000 |
| 500 | 24 hours | per app | no  | 15,000 |
| GET\_2\_users\_by\_username\_param | 100 | 24 hours | per user | no  | 3,000 |
| 500 | 24 hours | per app | no  | 15,000 |
| GET\_2\_users\_by\_username\_param\_followers | 100 | 24 hours | per user | no  | 3,000 |
| 500 | 24 hours | per app | no  | 15,000 |
| GET\_2\_users\_by\_username\_param\_mentions | 25  | 15 minutes | per app | no  | 72,000 |
| 5   | 15 minutes | per user | no  | 14,400 |
| GET\_2\_users\_by\_username\_param\_tweets | 25  | 15 minutes | per app | yes | 10,000 |
| 5   | 15 minutes | per user | yes | 10,000 |
| GET\_2\_users\_id\_bookmarks | 10  | 15 minutes | per user | no  | 28,800 |
| GET\_2\_users\_id\_list\_memberships | 25  | 15 minutes | per app | no  | 72,000 |
| 5   | 15 minutes | per user | no  | 14,400 |
| GET\_2\_users\_id\_owned\_lists | 500 | 24 hours | per app | no  | 15,000 |
| 100 | 24 hours | per user | no  | 3,000 |
| GET\_2\_users\_id\_pinned\_lists | 100 | 24 hours | per user | no  | 3,000 |
| 500 | 24 hours | per app | no  | 15,000 |
| GET\_2\_users\_me | 250 | 24 hours | per user | no  | 7,500 |
| GET\_2\_users\_param | 500 | 24 hours | per user | no  | 15,000 |
| 100 | 24 hours | per app | no  | 3,000 |
| GET\_2\_users\_param\_blocking | 5   | 15 minutes | per user | no  | 14,400 |
| GET\_2\_users\_param\_following\_spaces | 5   | 15 minutes | per user | no  | 14,400 |
| 25  | 15 minutes | per app | no  | 72,000 |
| GET\_2\_users\_param\_liked\_tweets | 5   | 15 minutes | per app | yes | 10,000 |
| 5   | 15 minutes | per user | yes | 10,000 |
| GET\_2\_users\_param\_mentions | 15  | 15 minutes | per app | yes | 10,000 |
| 10  | 15 minutes | per user | yes | 10,000 |
| GET\_2\_users\_param\_muting | 100 | 24 hours | per user | no  | 3,000 |
| GET\_2\_users\_param\_timelines\_reverse\_chronological | 5   | 15 minutes | per user | no  | 14,400 |
| GET\_2\_users\_param\_tweets | 10  | 15 minutes | per app | yes | 10,000 |
| 5   | 15 minutes | per user | yes | 10,000 |
| POST\_2\_compliance\_jobs | 15  | 15 minutes | per app | no  | 43,200 |
| POST\_2\_dm\_conversations | 5   | 15 minutes | per user | no  | 14,400 |
| 500 | 24 hours | per app | no  | 15,000 |
| 50  | 24 hours | per user | no  | 1,500 |
| POST\_2\_dm\_conversations\_param\_messages | 500 | 24 hours | per app | no  | 15,000 |
| 50  | 24 hours | per user | no  | 1,500 |
| 5   | 15 minutes | per user | no  | 14,400 |
| POST\_2\_dm\_conversations\_with\_param\_messages | 500 | 24 hours | per app | no  | 15,000 |
| 50  | 24 hours | per user | no  | 1,500 |
| 5   | 15 minutes | per user | no  | 14,400 |
| POST\_2\_lists | 100 | 24 hours | per user | no  | 3,000 |
| POST\_2\_lists\_param\_members | 5   | 15 minutes | per user | no  | 14,400 |
| POST\_2\_tweets | 100 | 24 hours | per user | no  | 3,000 |
| 1667 | 24 hours | per app | no  | 50,010 |
| POST\_2\_users\_id\_bookmarks | 5   | 15 minutes | per user | no  | 14,400 |
| POST\_2\_users\_param\_blocking | 5   | 15 minutes | per user | no  | 14,400 |
| POST\_2\_users\_param\_followed\_lists | 5   | 15 minutes | per user | no  | 14,400 |
| POST\_2\_users\_param\_following | 5   | 15 minutes | per user | no  | 14,400 |
| POST\_2\_users\_param\_likes | 200 | 24 hours | per user | no  | 6,000 |
| 5   | 15 minutes | per user | no  | 14,400 |
| POST\_2\_users\_param\_muting | 5   | 15 minutes | per user | no  | 14,400 |
| POST\_2\_users\_param\_pinned\_lists | 5   | 15 minutes | per user | no  | 14,400 |
| POST\_2\_users\_param\_retweets | 5   | 15 minutes | per user | no  | 14,400 |
| PUT\_2\_lists\_param | 5   | 15 minutes | per user | no  | 14,400 |
| PUT\_2\_tweets\_param\_hidden | 5   | 15 minutes | per user | no  | 14,400 |

### Twitter API v2 rate limits - Pro

The following table lists the rate limits for the Twitter API v2 Pro access. These rate limits are also documented on each endpoint's API Reference page and also displayed in the  [developer portal](https://developer.twitter.com/en/docs/developer-portal)'s products section.

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
| **Endpoint** | **#Requests** | **Window of time** | **Per** | **Part of the Tweet pull cap?** | **Effective 30-day limit** |
| DELETE\_2\_lists\_param | 300 | 15 minutes | per user | no  | 864,000 |
| DELETE\_2\_lists\_param\_members\_param | 300 | 15 minutes | per user | no  | 864,000 |
| DELETE\_2\_tweets\_param | 50  | 15 minutes | per user | no  | 144,000 |
| DELETE\_2\_users\_id\_bookmarks\_tweet\_id | 50  | 15 minutes | per user | no  | 144,000 |
| DELETE\_2\_users\_param\_blocking\_param | 50  | 15 minutes | per user | no  | 144,000 |
| DELETE\_2\_users\_param\_followed\_lists\_param | 50  | 15 minutes | per user | no  | 144,000 |
| DELETE\_2\_users\_param\_following\_param | 50  | 15 minutes | per user | no  | 144,000 |
| DELETE\_2\_users\_param\_likes\_param | 50  | 15 minutes | per user | no  | 144,000 |
| 1000 | 24 hours | per user | no  | 30,000 |
| DELETE\_2\_users\_param\_muting\_param | 50  | 15 minutes | per user | no  | 144,000 |
| DELETE\_2\_users\_param\_pinned\_lists\_param | 50  | 15 minutes | per user | no  | 144,000 |
| DELETE\_2\_users\_param\_retweets\_param | 50  | 15 minutes | per user | no  | 144,000 |
| GET\_2\_compliance\_jobs | 150 | 15 minutes | per app | no  | 432,000 |
| GET\_2\_compliance\_jobs\_param | 150 | 15 minutes | per app | no  | 432,000 |
| GET\_2\_dm\_conversations\_param\_dm\_events | 100 | 15 minutes | per user | no  | 288,000 |
| GET\_2\_dm\_conversations\_with\_param\_dm\_events | 100 | 15 minutes | per user | no  | 288,000 |
| GET\_2\_dm\_events | 100 | 15 minutes | per user | no  | 288,000 |
| GET\_2\_lists\_id | 75  | 15 minutes | per user | no  | 216,000 |
| 75  | 15 minutes | per app | no  | 216,000 |
| GET\_2\_lists\_id\_members | 900 | 15 minutes | per user | no  | 2,592,000 |
| 900 | 15 minutes | per app | no  | 2,592,000 |
| GET\_2\_lists\_id\_tweets | 900 | 15 minutes | per user | yes | 2,592,000 |
| 900 | 15 minutes | per app | yes | 2,592,000 |
| GET\_2\_spaces | 300 | 15 minutes | per user | no  | 864,000 |
| 300 | 15 minutes | per app | no  | 864,000 |
| GET\_2\_spaces\_by\_creator\_ids | 300 | 15 minutes | per user | no  | 864,000 |
| 1   | 1 second | per app | no  | 2,592,000 |
| 1   | 1 second | per user | no  | 2,592,000 |
| 300 | 15 minutes | per app | no  | 864,000 |
| GET\_2\_spaces\_param | 300 | 15 minutes | per app | no  | 864,000 |
| 300 | 15 minutes | per user | no  | 864,000 |
| GET\_2\_spaces\_param\_buyers | 300 | 15 minutes | per user | no  | 864,000 |
| 300 | 15 minutes | per app | no  | 864,000 |
| GET\_2\_spaces\_param\_tweets | 300 | 15 minutes | per user | no  | 864,000 |
| 300 | 15 minutes | per app | no  | 864,000 |
| GET\_2\_spaces\_search | 300 | 15 minutes | per user | no  | 864,000 |
| 300 | 15 minutes | per app | no  | 864,000 |
| GET\_2\_tweets | 900 | 15 minutes | per user | yes | 2,592,000 |
| 450 | 15 minutes | per app | yes | 1,296,000 |
| GET\_2\_tweets\_counts\_recent | 300 | 15 minutes | per app | no  | 864,000 |
| GET\_2\_tweets\_param | 900 | 15 minutes | per user | yes | 2,592,000 |
| 450 | 15 minutes | per app | yes | 1,296,000 |
| GET\_2\_tweets\_param\_liking\_users | 75  | 15 minutes | per user | no  | 216,000 |
| 75  | 15 minutes | per app | no  | 216,000 |
| GET\_2\_tweets\_param\_quote\_tweets | 75  | 15 minutes | per user | yes | 216,000 |
| 75  | 15 minutes | per app | yes | 216,000 |
| GET\_2\_tweets\_param\_retweeted\_by | 75  | 15 minutes | per app | yes | 216,000 |
| 75  | 15 minutes | per user | yes | 216,000 |
| GET\_2\_tweets\_search\_recent | 450 | 15 minutes | per app | yes | 1,296,000 |
| 300 | 15 minutes | per user | yes | 864,000 |
| GET\_2\_tweets\_search\_stream | 50  | 15 minutes | per app | yes | 144,000 |
| GET\_2\_tweets\_search\_stream\_rules | 450 | 15 minutes | per app | no  | 1,296,000 |
| GET\_2\_users | 300 | 15 minutes | per app | no  | 864,000 |
| 900 | 15 minutes | per user | no  | 2,592,000 |
| GET\_2\_users\_by | 900 | 15 minutes | per user | no  | 2,592,000 |
| 300 | 15 minutes | per app | no  | 864,000 |
| GET\_2\_users\_by\_username\_param | 900 | 15 minutes | per user | no  | 2,592,000 |
| 300 | 15 minutes | per app | no  | 864,000 |
| GET\_2\_users\_by\_username\_param\_followers | 15  | 15 minutes | per user | no  | 43,200 |
| 15  | 15 minutes | per app | no  | 43,200 |
| GET\_2\_users\_by\_username\_param\_mentions | 450 | 15 minutes | per app | no  | 1,296,000 |
| 180 | 15 minutes | per user | no  | 518,400 |
| GET\_2\_users\_by\_username\_param\_tweets | 1500 | 15 minutes | per app | yes | 4,320,000 |
| 900 | 15 minutes | per user | yes | 2,592,000 |
| GET\_2\_users\_id\_bookmarks | 180 | 15 minutes | per user | no  | 518,400 |
| GET\_2\_users\_id\_list\_memberships | 75  | 15 minutes | per app | no  | 216,000 |
| 75  | 15 minutes | per user | no  | 216,000 |
| GET\_2\_users\_id\_owned\_lists | 15  | 15 minutes | per app | no  | 43,200 |
| 15  | 15 minutes | per user | no  | 43,200 |
| GET\_2\_users\_id\_pinned\_lists | 15  | 15 minutes | per user | no  | 43,200 |
| 15  | 15 minutes | per app | no  | 43,200 |
| GET\_2\_users\_me | 75  | 15 minutes | per user | no  | 216,000 |
| GET\_2\_users\_param | 900 | 15 minutes | per user | no  | 2,592,000 |
| 300 | 15 minutes | per app | no  | 864,000 |
| GET\_2\_users\_param\_blocking | 15  | 15 minutes | per user | no  | 43,200 |
| GET\_2\_users\_param\_following\_spaces | 300 | 15 minutes | per user | no  | 864,000 |
| 300 | 15 minutes | per app | no  | 864,000 |
| GET\_2\_users\_param\_liked\_tweets | 75  | 15 minutes | per app | yes | 216,000 |
| 75  | 15 minutes | per user | yes | 216,000 |
| GET\_2\_users\_param\_mentions | 450 | 15 minutes | per app | yes | 1,296,000 |
| 300 | 15 minutes | per user | yes | 864,000 |
| GET\_2\_users\_param\_muting | 15  | 15 minutes | per user | no  | 43,200 |
| GET\_2\_users\_param\_timelines\_reverse\_chronological | 180 | 15 minutes | per user | no  | 518,400 |
| GET\_2\_users\_param\_tweets | 1500 | 15 minutes | per app | yes | 4,320,000 |
| 900 | 15 minutes | per user | yes | 2,592,000 |
| POST\_2\_compliance\_jobs | 150 | 15 minutes | per app | no  | 432,000 |
| POST\_2\_dm\_conversations | 200 | 15 minutes | per user | no  | 576,000 |
| 2500 | 24 hours | per app | no  | 75,000 |
| 1000 | 24 hours | per user | no  | 30,000 |
| POST\_2\_dm\_conversations\_param\_messages | 2500 | 24 hours | per app | no  | 75,000 |
| 1000 | 24 hours | per user | no  | 30,000 |
| 200 | 15 minutes | per user | no  | 576,000 |
| POST\_2\_dm\_conversations\_with\_param\_messages | 2500 | 24 hours | per app | no  | 75,000 |
| 1000 | 24 hours | per user | no  | 30,000 |
| 200 | 15 minutes | per user | no  | 576,000 |
| POST\_2\_lists | 300 | 15 minutes | per user | no  | 864,000 |
| POST\_2\_lists\_param\_members | 300 | 15 minutes | per user | no  | 864,000 |
| POST\_2\_tweets | 100 | 15 minutes | per user | no  | 288,000 |
| 10000 | 24 hours | per app | no  | 300,000 |
| POST\_2\_tweets\_search\_stream\_rules | 100 | 15 minutes | per user | no  | 288,000 |
| POST\_2\_users\_id\_bookmarks | 50  | 15 minutes | per user | no  | 144,000 |
| POST\_2\_users\_param\_blocking | 50  | 15 minutes | per user | no  | 144,000 |
| POST\_2\_users\_param\_followed\_lists | 50  | 15 minutes | per user | no  | 144,000 |
| POST\_2\_users\_param\_following | 50  | 15 minutes | per user | no  | 144,000 |
| POST\_2\_users\_param\_likes | 1000 | 24 hours | per user | no  | 30,000 |
| 50  | 15 minutes | per user | no  | 144,000 |
| POST\_2\_users\_param\_muting | 50  | 15 minutes | per user | no  | 144,000 |
| POST\_2\_users\_param\_pinned\_lists | 50  | 15 minutes | per user | no  | 144,000 |
| POST\_2\_users\_param\_retweets | 50  | 15 minutes | per user | no  | 144,000 |
| PUT\_2\_lists\_param | 300 | 15 minutes | per user | no  | 864,000 |
| PUT\_2\_tweets\_param\_hidden | 50  | 15 minutes | per user | no  | 144,00 |

### Twitter API v2 rate limits - Enterprise

To learn more about enterprise access rate limits reach out to your account manager.

**Please note**  

In addition to rate limits, we also have [Tweet caps](https://developer.twitter.com/en/docs/twitter-api/tweet-caps) that limit the number of Tweets that any [Project](https://developer.twitter.com/en/docs/projects) can retrieve from certain endpoints in a given month, which is based on your [access level](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api#v2-access-level).

###   
Rate limits and authentication method

Rate limits are set at both the developer App and the user access token levels:

* **[OAuth 2.0 Bearer Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0): App rate limit  
    **This authentication method and rate limit allows you to make a certain number of requests to endpoints on behalf of your developer App. When using this authentication method, rate limits are determined by the number of requests you make using a Bearer Token.  
      
    If an endpoint has an App rate limit of 450 requests per 15 minute interval, then you can make 450 requests per window on behalf of your App when you use your Bearer Token.  
      
    This limit is considered completely separate from the user rate limit.  
      
    
* **[OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a): User rate limit**  
    This authentication method and rate limit allows for you to make a certain number of requests to endpoints on behalf of a Twitter user, identified by the user Access Token used when authenticating the request. For example, if you would like to retrieve private metrics from Tweets, you would need to authenticate with the user Access Tokens associated with that user, which can be generated by using the [3-legged OAuth flow](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens).   
      
    If ten users have authorized your developer App, and the endpoint you are making a request to has a user rate limit of 900 requests per 15-minute interval, then you can make up to 900 requests per user in that 15 minute time period, for a total of 9000 requests.  
      
    This limit is considered completely separate from App rate limit.   
     

**Please note  
**

Users' rate limits are shared across all Apps that they have authorized. For example, if a specific user likes 20 Tweets using one developer App and likes 20 Tweets on a separate developer App within a 15 minute time period, the 40 requests would pull out of the same per user rate limit bucket. That means that if this endpoint has a user rate limit of 1,000 requests per 15 minutes, then this user would be able to like 960 more Tweets within that 24 hour period of time across all Twitter and third-party apps. 

### HTTP headers and response codes

Use the HTTP headers in order to understand where the application is at for a given rate limit, on the method that was just utilized.  

Note that the HTTP headers are contextual. When using application-only authentication, they indicate the rate limit for the application context. When using user-based authentication, they indicate the rate limit for that user context.  

* x-rate-limit-limit: the rate limit ceiling for that given endpoint
* x-rate-limit-remaining: the number of requests left for the 15-minute window
* x-rate-limit-reset: the remaining window before the rate limit resets, in UTC [epoch seconds](http://en.wikipedia.org/wiki/Unix_time)  
     

When an application exceeds the rate limit for a given Twitter API endpoint, the API will return a [HTTP 429 “Too Many Requests”](http://tools.ietf.org/html/rfc6585) response code, and the following error will be returned in the response body:

{ "errors": \[ { "code": 88, "message": "Rate limit exceeded" } \] } 

### Recovering from a rate limit

When these rate limits are exceeded, a 429 'Too many requests' error is returned from the endpoint.  As discussed below, when rate limit errors occur, a best practice is to examine HTTP headers that indicate when the limit resets and pause requests until then.    

When a "too many requests" or rate-limiting error occurs, the frequency of making requests needs to be slowed down. When a rate limit error is hit, the x-rate-limit-reset: HTTP header can be checked to learn when the rate-limiting will reset.   

Another common pattern is based on exponential backoff, where the time between requests starts off small (for example, a few seconds), then doubled before each retry. This is continued until a request is successful, or some reasonable maximum time between requests is reached (for example, a few minutes).    

Ideally, the client-side is self-aware of existing rate limits and can pause requests until the currently exceeded window expires. If you exceed a 15-minute limit, then waiting a minute or two before retrying makes sense.

Note that beyond these limits on the number of requests, the Standard Basic level of access provides up to 500,000 Tweets per month from the recent search and filtered stream endpoints. If you have exceeded the monthly limit on the number of Tweets, then it makes more sense for your app to raise a notification and know its enrollment day of the month and hold off requests until that day.    
 

### Tips to avoid being rate limited

The tips below are there to help you code defensively and reduce the possibility of being rate limited. Some application features that you may want to provide are simply impossible in light of rate-limiting, especially around the freshness of results. If real-time information is an aim of your application, look into the filtered and sampled stream endpoints.   
 

#### Caching

Store API responses in your application or on your site if you expect a lot of use. For example, don’t try to call the Twitter API on every page load of your website landing page. Instead, call the API infrequently and load the response into a local cache. When users hit your website load the cached version of the results.  
 

#### Prioritize active users

If your site keeps track of many Twitter users (for example, fetching their current status or statistics about their Twitter usage), consider only requesting data for users who have recently signed into your site.  
 

#### Adapt to the search results

If your application monitors a high volume of search terms, query less often for searches that have no results than for those that do. By using a back-off you can keep up to date on queries that are popular but not waste cycles requesting queries that very rarely change. Alternatively, consider using the filtered stream endpoint and filter with your search queries. 

#### Denylist

If an application abuses the rate limits, it will be denied. Denied apps are unable to get a response from the Twitter API. If you or your application has been denied and you think there has been a mistake, you can use our [Platform Support forms](https://support.twitter.com/forms/platform) to request assistance. Please include the following information:

1. Explain why you think your application was denied.
2. If you are no longer being rate limited, describe in detail how you fixed the problem.

Next steps
----------

[Learn more about Tweet caps](https://developer.twitter.com/en1/docs/twitter-api/tweet-caps "Learn more about Tweet caps")

Tweet caps

Twitter API v2 has a Tweet consumption cap that limits the number of Tweets that you can receive from a set of endpoints on a monthly basis. Tweet caps apply at the [Project](https://developer.twitter.com/en/docs/projects)\-level, meaning that any requests to the endpoints listed below using the keys and tokens from [developer Apps](https://developer.twitter.com/en/docs/apps) within that Project will count towards the Project Tweet cap.   
 

### Limited v2 endpoints

Tweets you receive from any of the following endpoints count towards this monthly Tweet cap:

* [Tweets Lookup](https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/introduction)
* [Recent search](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/tweets/search)
* [Full-archive search](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/tweets/search) 
* [Filtered stream](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/tweets/filtered-stream)
* [User Tweet timeline](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/tweets/timelines)
* [User mention timeline](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/tweets/timelines)
* [Likes lookup - Tweets liked by a user](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/tweets/likes)  
    
* [List Tweets lookup](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/lists/list-tweets)  
      
    

### Note:

If the same Tweet is returned from multiple queries during the billing cycle, then the Tweet is only counted once against the monthly cap - i.e, the Tweets are deduplicated.

**Dedupe** Counter gets reset on a monthly basis  (at the end of the billing cycle).

### Tweet cap volumes

The Tweet cap volume depends on your access level:

|     |     |
| --- | --- |
| **Free** tier | 1,500 Tweets per month |
| **Basic** tier | 10,000 Tweets per month |
| **Pro** tier | 1,000,000 Tweets per month |
| **Enterprise** tier | 50+ million Tweets per month |

  
You can check your usage towards the monthly Tweet cap by viewing the [main dashboard page](https://developer.twitter.com/content/developer-twitter/en/portal/dashboard) in the [developer portal](https://developer.twitter.com/en/docs/developer-portal). Under the name of your Project, you'll see a status bar that illustrates your current month’s usage in relation to the Tweet cap. You will also see the number of Tweets you pulled this month, the percentage of Tweets used in relation to the cap, and the date your Tweet cap usage resets.

Next steps
----------

[Learn more about Twitter Apps](https://developer.twitter.com/en/docs/apps "Learn more about Twitter Apps")

[Learn more about Projects](https://developer.twitter.com/en/docs/projects "Learn more about Projects")

[Learn more about Twitter API v2 access levels](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api "Learn more about Twitter API v2 access levels")

Edit Tweets

Introduction
------------

The Twitter API v2 endpoints provide edited Tweet metadata. The _Edit Tweets_ feature was first introduced for testing among Twitter employees on September 1, 2022. Starting on that date, eligible Tweets are editable for 30 minutes and up to 5 times. _All objects for Tweets created since September 29, 2022_ include Tweet edit metadata, even if the Tweet was never edited. Each time a Tweet is edited, a new Tweet ID is created. A Tweet's edit history can be described by chaining these IDs together, starting with the original ID.  Additionally, if any Tweet in the edit chain is deleted, all Tweets in that chain are deleted as well.

Using the Twitter API v2, a developer can find out:

* If a Tweet was edit eligible at the time of creation. Some Tweets, such as those with polls or scheduled Tweets, can not be edited.
* Tweets are editable for 30 minutes, and can be edited up to 5 times. For editable Tweets you can see if time for editing remains and how many more edits are possible.
* If you are viewing an edited version of a Tweet (in most cases the API will return the most recent version of a Tweet, unless a specific past version is requested by Tweet ID).
* The entire edit history of the Tweet.
* The engagement attributed to each version of the Tweet.

There are three components to a Tweet’s edit history:

1. By default, the Tweet payload will contain an array of Tweet IDs that are part of a Tweet’s edit history. This information is specified by the edit\_history\_tweet\_ids, which is a default field in the Tweet payload. This array will contain at least one ID, the ID of the original, unedited Tweet. When there is only one ID that means the Tweet has no edit history. 
2. You can get information such as whether a Tweet was editable at the time it was created, how much time, if any, is remaining for a Tweet to be edited, and how many edits remain by specifying edit\_controls in your [tweet.fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter.
3. Finally, you can get the Tweet objects for each Tweet in a Tweet’s edit history, by specifying the edit\_history\_tweet\_ids using the [expansion](https://developer.twitter.com/en/docs/twitter-api/expansions) parameter

Most Tweets are eligible for editing. However, the following types of Tweets are not:   

* Tweet is promoted
* Tweet has a poll
* Tweet is a non-self-thread reply
* Tweet is a Retweet (note that Quote Tweets are eligible for edit)
* Tweet is nullcast
* Community Tweet
* Superfollow Tweet
* Collaborative Tweet

Examples  

-----------

The examples below demonstrate how a developer can request edited Tweet metadata using the Twitter API v2. 

**Note:** The examples below use the User Tweet Timeline endpoint, but you can request this metadata using the same parameters (with fields and expansions) for all endpoints that return Tweets (e.g. Tweets lookup, search, filtered stream,  etc.)

### Default behavior

By default, an API request to any endpoint that returns Tweet objects in the Twitter API v2, you get:

* The Tweet ID
* The Tweet Text
* An array of Tweet IDs that are part of a Tweet’s edit history. If there is only one ID provided, that means the Tweet has not been edited.

**Request:**

      `curl --request GET 'https://api.twitter.com/2/users/:id/tweets' --header 'Authorization: Bearer $BEARER_TOKEN'`
    

**Sample Response:**

      `{   "data": [     {       "id": "1514991667853602823",       "text": "we have an edit button",       "edit_history_tweet_ids": ["1514991667853602822", "1514991667853602823"]     }   ] }`
    

### Getting additional data with edit\_controls

If you want additional edited Tweet metadata such as whether a Tweet was eligible to be edited when it was created and how much time is remaining for a Tweet to be editable, you can request this information using the tweet.fields parameter and setting it to edit\_control.

**Request:**

      `curl --request GET 'https://api.twitter.com/2/users/:id/tweets?tweet.fields=edit_control' --header 'Authorization: Bearer $BEARER_TOKEN'`
    

**Sample Response:**

      `{   "data": [     {       "id": "1514991667853602823",       "text": "we have an edit button",       "edit_history_tweet_ids": ["1514991667853602822", "1514991667853602823"],       "edit_controls": {         "is_edit_eligible": true,         "editable_until": "2022-04-21 09:35:20.311",         "edits_remaining": 4       }     }   ] }`
    

### Getting Tweet objects for all Tweets in a Tweet’s edit history

The examples above provide an array of Tweet IDs in a Tweet’s edit history. If you want the actual Tweet object for each of these Tweet IDs, you can use the expansion parameter and set it to edit\_history\_tweet\_ids. The Tweet objects that make up the edit history will be provided in the "includes" object. 

**Request:**

      `curl --location --request GET 'https://api.twitter.com/2/users/:id/tweets?tweet.fields=edit_control&expansions=edit_history_tweet_ids' --header 'Authorization: Bearer $BEARER_TOKEN'`
    

**Sample Response:**

      `{   "data": [     {       "id": "1514991667853602823",       "text": "we have an edit button",       "edit_history_tweet_ids": ["1514991667853602822", "1514991667853602823"],       "edit_controls": {         "is_edit_eligible": true,         "editable_until": "2022-04-21 09:35:20.311",         "edits_remaining": 4       }     }   ],   "includes": {     "tweets": [       {         "id": "1514991667853602822",         "text": "we need an eidt button",         "edit_history_tweet_ids": [           "1514991667853602822",           "1514991667853602823"         ],         "edit_controls": {           "is_edit_eligible": true,           "editable_until": "2022-04-21 09:35:20.311",           "edits_remaining": 4         }       }     ]   } }`