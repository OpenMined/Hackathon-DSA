
Tweet object | Docs | Twitter Developer Platform 

Tweet object

Tweet
-----

Tweets are the basic building block of all things Twitter. The Tweet object has a long list of ‘root-level’ fields, such as `id`, `text`, and `created_at`. Tweet objects are also the ‘parent’ object to several child objects including `user`, `media`, `poll`, and `place`. Use the field parameter `tweet.fields` when requesting these root-level fields on the Tweet object.

The Tweet object that can be found and expanded in the user resource. Additional Tweets related to the requested Tweet can also be found and expanded in the Tweet resource. The object is available for expansion with `?expansions=pinned_tweet_id` in the user resource or `?expansions=referenced_tweets.id` in the Tweet resource to get the object with only default fields. Use the expansion with the field parameter: `tweet.fields` when requesting additional fields to complete the object.  

| Field value | Type | Description | How it can be used |
| --- | --- | --- | --- |
| id (default) | string | The unique identifier of the requested Tweet.
`"id": "1050118621198921728"` | Use this to programmatically retrieve a specific Tweet. |
| text (default) | string | The actual UTF-8 text of the Tweet. See twitter-text for details on what characters are currently considered valid.
`"text": "To make room for more expression, we will now count all emojis as equal—including those with gender‍‍‍ ‍‍and skin tone modifiers 👍🏻👍🏽👍🏿. This is now reflected in Twitter-Text, our Open Source library. \n\nUsing Twitter-Text? See the forum post for detail: https://t.co/Nx1XZmRCXA"`
 | Keyword extraction and sentiment analysis/classification. |
| edit\_history\_tweet\_ids (default) | object | Unique identifiers indicating all versions of a Tweet. For Tweets with no edits, there will be one ID. For Tweets with an edit history, there will be multiple IDs, arranged in ascending order reflecting the order of edits. The most recent version is the last position of the array.
`"edit_history_tweet_ids":`
`[`
`"1584717154800521216"`
`]` | Use this information to find the edit history of a Tweet. |
| attachments | object | Specifies the type of attachments (if any) present in this Tweet.
`"attachments": {
     "poll_ids": [
         "1199786642468413448"
     ]
 }`
`"attachments": {
     "media_keys": [
         "3_1136048009270239232"
     ]
 }` | Understanding the objects returned for requested expansions  |
| author\_id | string | The unique identifier of the User who posted this Tweet.
`"author_id": "2244994945"` | Hydrating User object, sharing dataset for peer review |
| context\_annotations | array | Contains context annotations for the Tweet.
`"context_annotations": [`
`{`
`"domain": {`
`"id": "65",`
`"name": "Interests and Hobbies Vertical",`
`"description": "Top level interests and hobbies groupings, like Food or Travel"
          },`
`"entity": {`
`"id": "834828264786898945",`
`"name": "Drinks",`
`"description": "Drinks"`
`}`
`},`
`{`
`"domain": {`
`"id": "66",`
`"name": "Interests and Hobbies Category",`
`"description": "A grouping of interests and hobbies entities, like Novelty Food or Destinations"
          },`
`"entity": {`
`"id": "834828445238431744",`
`"name": "Generic Drinks",`
`"description": "Generic Drinks"`
`}`
`}`
`]` | Entity recognition/extraction, topical analysis  |
| conversation\_id | string | The Tweet ID of the original Tweet of the conversation (which includes direct replies, replies of replies).
`"conversation_id": "1050118621198921728"` | Use this to reconstruct the conversation from a Tweet. |
| created\_at | date (ISO 8601) | Creation time of the Tweet.
`"created_at": "2019-06-04T23:12:08.000Z"` | This field can be used to understand when a Tweet was created and used for time-series analysis etc.  |
| edit\_controls | object | When present, this indicates how much longer the Tweet can be edited and the number of remaining edits. Tweets are only editable for the first 30 minutes after creation and can be edited up to five times.
`"edit_controls": {`
`"edits_remaining": 5,`
`"is_edit_eligible": true,`
`"editable_until": "2022-10-25T01:53:06.000Z"`
`}` | Use this to determine if a Tweet is eligible for editing. |
| entities | object | Entities that have been parsed out of the text of the Tweet. Additionally, see entities in Twitter Objects.
`"entities": {
     "annotations": [
         {
            "start": 144,
            "end": 150,
            "probability": 0.626,
            "type": "Product",
            "normalized_text": "Twitter"
         }
     ],
    "cashtags": [
         {
             "start": 18,
             "end": 23,
             "tag": "twtr"
         }
     ],
     "hashtags": [
         {
             "start": 0,
             "end": 17,
             "tag": "blacklivesmatter"
         }
     ],
     "mentions": [
         {
             "start": 24,
             "end": 35,
             "tag": "TwitterDev"
         }
     ],
     "urls": [
         {
            "start": 44,
            "end": 67,
            "url": "https://t.co/crkYRdjUB0",
            "expanded_url": "https://twitter.com",
            "display_url": "twitter.com",
            "status": "200",
            "title": "bird",
            "description": "From breaking news and entertainment to sports and politics, get the full story with all the live commentary.",
             "unwound_url": "https://twitter.com"
         }
     ]
 }` | Entities are JSON objects that provide additional information about hashtags, urls, user mentions, and cashtags associated with a Tweet. Reference each respective entity for further details.
Please note that all start indices are inclusive. The majority of end indices are exclusive, except for entities.annotations.end, which is currently inclusive. We will be changing this to exclusive with our v3 bump since it is a breaking change.  |
| in\_reply\_to\_user\_id | string | If the represented Tweet is a reply, this field will contain the original Tweet’s author ID. This will not necessarily always be the user directly mentioned in the Tweet.
`"in_reply_to_user_id": "2244994945"` | Use this to determine if this Tweet was in reply to another Tweet. |
| lang | string | Language of the Tweet, if detected by Twitter. Returned as a BCP47 language tag.
`"lang": "en"` | Classify Tweets by spoken language. |
| non\_public\_metrics | object | Non-public engagement metrics for the Tweet at the time of the request. 
Requires user context authentication.
`"non_public_metrics": {
       "impression_count": 99
       "url_link_clicks": 37
       "user_profile_clicks": 22
  }`
 | Use this to determine the total number of impressions generated for the Tweet. |
| organic\_metrics | object | Engagement metrics, tracked in an organic context, for the Tweet at the time of the request.
Requires user context authentication.
`"organic_metrics": {
      "impression_count": 3880,
      "like_count": 8,
      "reply_count": 0,
      "retweet_count": 4
      "url_link_clicks": 3
      "user_profile_clicks": 2
 }` | Use this to measure organic engagement for the Tweet. |
| possibly\_sensitive | boolean | This field indicates content may be recognized as sensitive. The Tweet author can select within their own account preferences and choose “Mark media you tweet as having material that may be sensitive” so each Tweet created after has this flag set.
This may also be judged and labeled by an internal Twitter support agent.
`"possibly_sensitive": false` | Studying circulation of certain types of content. |
| promoted\_metrics | object | Engagement metrics, tracked in a promoted context, for the Tweet at the time of the request.
Requires user context authentication.
`"promoted_metrics": {
       "impression_count": 1082,
       "like_count": 187,
       "reply_count": 6,
       "retweet_count": 25
       "url_link_clicks": 30
       "user_profile_clicks": 2
  }`
 | Use this to measure engagement for the Tweet when it was promoted. |
| public\_metrics | object | Public engagement metrics for the Tweet at the time of the request.
`"public_metrics" : {
          "retweet_count": 8,
          "reply_count": 2,
          "like_count": 39,
          "quote_count": 1
  }` | Use this to measure Tweet engagement. |
| referenced\_tweets | array | A list of Tweets this Tweet refers to. For example, if the parent Tweet is a Retweet, a Retweet with comment (also known as Quoted Tweet) or a Reply, it will include the related Tweet referenced to by its parent.
`"referenced_tweets": [
        {
            "type": "replied_to",
            "id": "1242125486844604425"
        }
    ]`
`"referenced_tweets": [
        {
            "type": "quoted",
            "id": "1265712391578214400"
        }
    ]`
 | This field can be used to understand conversational aspects of retweets etc. |
| reply\_settings | string | Shows you who can reply to a given Tweet. Fields returned are "everyone", "mentioned\_users", and "followers".
`"reply_settings": "everyone"` | This field allows you to determine whether conversation reply settings have been set for the Tweet and if so, what settings have been set. |
| withheld | object | When present, contains withholding details for withheld content.
`"withheld": {
        "copyright": false,
        "country_codes": [
           "IN"
        ]
    }` |  |

### 
Retrieving a Tweet object

#### Sample Request

In the following request, we are requesting fields for the Tweet on the Tweets lookup endpoint. Be sure to replace `$BEARER_TOKEN` with your own generated Bearer Token.  

```
      curl --request GET 'https://api.twitter.com/2/tweets?ids=1212092628029698048&tweet.fields=attachments,author_id,context_annotations,created_at,entities,geo,id,in_reply_to_user_id,lang,possibly_sensitive,public_metrics,referenced_tweets,text,withheld&expansions=referenced_tweets.id' --header 'Authorization: Bearer $BEARER_TOKEN'
```

Code copied to clipboard

 **Sample Response**

```
      {
  "data": [
    {
      "text": "We believe the best future version of our API will come from building it with YOU. Here’s to another great year with everyone who builds on the Twitter platform. We can’t wait to continue working with you in the new year. https://t.co/yvxdK6aOo2",
      "edit_history_tweet_ids": [
        "1212092628029698048"
      ],
      "lang": "en",
      "in_reply_to_user_id": "2244994945",
      "entities": {
        "urls": [
          {
            "start": 222,
            "end": 245,
            "url": "https://t.co/yvxdK6aOo2",
            "expanded_url": "https://twitter.com/LovesNandos/status/1211797914437259264/photo/1",
            "display_url": "pic.twitter.com/yvxdK6aOo2",
            "media_key": "16_1211797899316740096"
          }
        ],
        "annotations": [
          {
            "start": 42,
            "end": 44,
            "probability": 0.5359,
            "type": "Other",
            "normalized_text": "API"
          },
          {
            "start": 144,
            "end": 150,
            "probability": 0.9832,
            "type": "Other",
            "normalized_text": "Twitter"
          }
        ]
      },
      "author_id": "2244994945",
      "referenced_tweets": [
        {
          "type": "replied_to",
          "id": "1212092627178287104"
        }
      ],
      "id": "1212092628029698048",
      "public_metrics": {
        "retweet_count": 7,
        "reply_count": 3,
        "like_count": 38,
        "quote_count": 1
      },
      "context_annotations": [
        {
          "domain": {
            "id": "29",
            "name": "Events [Entity Service]",
            "description": "Real world events. "
          },
          "entity": {
            "id": "1186637514896920576",
            "name": " New Years Eve"
          }
        },
        {
          "domain": {
            "id": "29",
            "name": "Events [Entity Service]",
            "description": "Real world events. "
          },
          "entity": {
            "id": "1206982436287963136",
            "name": "Happy New Year: It’s finally 2020 everywhere!",
            "description": "Catch fireworks and other celebrations as people across the globe enter the new year.\nPhoto via @GettyImages "
          }
        },
        {
          "domain": {
            "id": "119",
            "name": "Holiday",
            "description": "Holidays like Christmas or Halloween"
          },
          "entity": {
            "id": "1186637514896920576",
            "name": " New Years Eve"
          }
        },
        {
          "domain": {
            "id": "119",
            "name": "Holiday",
            "description": "Holidays like Christmas or Halloween"
          },
          "entity": {
            "id": "1206982436287963136",
            "name": "Happy New Year: It’s finally 2020 everywhere!",
            "description": "Catch fireworks and other celebrations as people across the globe enter the new year.\nPhoto via @GettyImages "
          }
        },
        {
          "domain": {
            "id": "30",
            "name": "Entities [Entity Service]",
            "description": "Entity Service top level domain, every item that is in Entity Service should be in this domain"
          },
          "entity": {
            "id": "781974596752842752",
            "name": "Services"
          }
        },
        {
          "domain": {
            "id": "47",
            "name": "Brand",
            "description": "Brands and Companies"
          },
          "entity": {
            "id": "10045225402",
            "name": "Twitter"
          }
        },
        {
          "domain": {
            "id": "131",
            "name": "Unified Twitter Taxonomy",
            "description": "A taxonomy of user interests. "
          },
          "entity": {
            "id": "10045225402",
            "name": "Twitter"
          }
        },
        {
          "domain": {
            "id": "131",
            "name": "Unified Twitter Taxonomy",
            "description": "A taxonomy of user interests. "
          },
          "entity": {
            "id": "847868745150119936",
            "name": "Family & relationships",
            "description": "Hobbies and interests"
          }
        },
        {
          "domain": {
            "id": "131",
            "name": "Unified Twitter Taxonomy",
            "description": "A taxonomy of user interests. "
          },
          "entity": {
            "id": "1196446161223028736",
            "name": "Social media"
          }
        },
        {
          "domain": {
            "id": "29",
            "name": "Events [Entity Service]",
            "description": "Real world events. "
          },
          "entity": {
            "id": "1206982436287963136",
            "name": "Happy New Year: It’s finally 2020 everywhere!",
            "description": "Catch fireworks and other celebrations as people across the globe enter the new year.\nPhoto via @GettyImages "
          }
        },
        {
          "domain": {
            "id": "119",
            "name": "Holiday",
            "description": "Holidays like Christmas or Halloween"
          },
          "entity": {
            "id": "1206982436287963136",
            "name": "Happy New Year: It’s finally 2020 everywhere!",
            "description": "Catch fireworks and other celebrations as people across the globe enter the new year.\nPhoto via @GettyImages "
          }
        }
      ],
      "created_at": "2019-12-31T19:26:16.000Z",
      "attachments": {
        "media_keys": [
          "16_1211797899316740096"
        ]
      },
      "possibly_sensitive": false
    }
  ],
  "includes": {
    "tweets": [
      {
        "text": "These launches would not be possible without the feedback you provided along the way, so THANK YOU to everyone who has contributed your time and ideas. Have more feedback? Let us know ⬇️ https://t.co/Vxp4UKnuJ9",
        "edit_history_tweet_ids": [
          "1212092627178287104"
        ],
        "lang": "en",
        "in_reply_to_user_id": "2244994945",
        "entities": {
          "urls": [
            {
              "start": 187,
              "end": 210,
              "url": "https://t.co/Vxp4UKnuJ9",
              "expanded_url": "https://twitterdevfeedback.uservoice.com/forums/921790-twitter-developer-labs",
              "display_url": "twitterdevfeedback.uservoice.com/forums/921790-…",
              "status": 200,
              "title": "Updates on our feedback channels",
              "description": "We build our developer platform in the open, with your input and feedback. Over the past year, hearing directly from you and the users of your apps has helped us build developer products that cater to the use case you helped us identify. We want to make this the way we build products, and moving forward, we are consolidating our feedback channels. Meeting you where you are Effective today, we are going to retire our UserVoice feedback channel in favor of more frequent direct engagements with y...",
              "unwound_url": "https://twittercommunity.com/t/updates-on-our-feedback-channels/169706"
            }
          ]
        },
        "author_id": "2244994945",
        "referenced_tweets": [
          {
            "type": "replied_to",
            "id": "1212092626247110657"
          }
        ],
        "id": "1212092627178287104",
        "public_metrics": {
          "retweet_count": 2,
          "reply_count": 1,
          "like_count": 19,
          "quote_count": 0
        },
        "created_at": "2019-12-31T19:26:16.000Z",
        "possibly_sensitive": false
      }
    ]
  }
}
```

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