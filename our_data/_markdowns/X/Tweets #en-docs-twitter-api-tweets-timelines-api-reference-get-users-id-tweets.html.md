
GET /2/users/:id/tweets | Docs | Twitter Developer Platform 

GET /2/users/:id/tweets

 GET /2/users/:id/tweets
=======================
Returns Tweets composed by a single user, specified by the requested user ID. By default, the most recent ten Tweets are returned per request. Using pagination, the most recent 3,200 Tweets can be retrieved.  
The Tweets returned by this endpoint count towards the Project-level Tweet cap.
Run in Postman ❯Try a live request ❯Build request with API Explorer ❯### Endpoint URL
`https://api.twitter.com/2/users/:id/tweets`  
### Authentication and rate limits

|  |  |
| --- | --- |
| Authentication methodssupported by this endpoint | OAuth 1.0a is also available for this endpoint.OAuth 2.0 App-onlyOAuth 2.0 Authorization Code with PKCE |
| Rate limit | App rate limit (Application-only): 1500 requests per 15-minute window shared among all users of your appUser rate limit (User context): 900 requests per 15-minute window per each authenticated user |
### OAuth 2.0 scopes required by this endpoint

|  |
| --- |
| `tweet.read``users.read` |
| Learn more about OAuth 2.0 Authorization Code with PKCE |
### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `id` Required  | string | Unique identifier of the Twitter account (user ID) for whom to return results. User ID can be referenced using the user/lookup endpoint. More information on Twitter IDs is here. |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| `end_time` Optional  | date (ISO 8601) | YYYY-MM-DDTHH:mm:ssZ (ISO 8601/RFC 3339). The newest or most recent UTC timestamp from which the Tweets will be provided. Only the 3200 most recent Tweets are available. Timestamp is in second granularity and is inclusive (for example, 12:00:01 includes the first second of the minute). Minimum allowable time is 2010-11-06T00:00:01ZPlease note that this parameter does not support a millisecond value. |
| `exclude` Optional  | enum (`retweets`, `replies`) | Comma-separated list of the types of Tweets to exclude from the response. When `exclude=retweets` is used, the maximum historical Tweets returned is still 3200. When the `exclude=replies` parameter is used for any value, only the most recent 800 Tweets are available. |
| `expansions` Optional  | enum (`attachments.poll_ids`, `attachments.media_keys`, `author_id`, `edit_history_tweet_ids`, `entities.mentions.username`, `geo.place_id`, `in_reply_to_user_id`, `referenced_tweets.id`, `referenced_tweets.id.author_id`) | Expansions enable you to request additional data objects that relate to the originally returned Tweets. Submit a list of desired expansions in a comma-separated list without spaces. The ID that represents the expanded data object will be included directly in the Tweet data object, but the expanded object metadata will be returned within the `includes` response object, and will also include the ID so that you can match this data object to the original Tweet object.The following data objects can be expanded using this parameter:* The Tweet author's user object
* The user object of the Tweet’s author that the original Tweet is responding to
* Any mentioned users’ object
* Any referenced Tweets’ author’s user object
* Attached media’s object
* Attached poll’s object
* Attached place’s object
* Any referenced Tweets’ object (this includes Tweet objects for previous versions of an edited Tweet).
 |
| `max_results` Optional  | integer | Specifies the number of Tweets to try and retrieve, up to a maximum of 100 per distinct request. By default, 10 results are returned if this parameter is not supplied. The minimum permitted value is 5. It is possible to receive less than the `max_results` per request throughout the pagination process. |
| `media.fields` Optional  | enum (`duration_ms`, `height`, `media_key`, `preview_image_url`, `type`, `url`, `width`, `public_metrics`, `non_public_metrics`, `organic_metrics`, `promoted_metrics`, `alt_text`, `variants`) | This fields parameter enables you to select which specific media fields will deliver in each returned Tweet. Specify the desired fields in a comma-separated list without spaces between commas and fields. The Tweet will only return media fields if the Tweet contains media and if you've also included the `expansions=attachments.media_keys` query parameter in your request. While the media ID will be located in the Tweet object, you will find this ID and all additional media fields in the `includes` data object. |
| `pagination_token` Optional  | string | This parameter is used to move forwards or backwards through 'pages' of results, based on the value of the `next_token` or `previous_token` in the response. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified. |
| `place.fields` Optional  | enum (`contained_within`, `country`, `country_code`, `full_name`, `geo`, `id`, `name`, `place_type`) | This fields parameter enables you to select which specific place fields will deliver in each returned Tweet. Specify the desired fields in a comma-separated list without spaces between commas and fields. The Tweet will only return place fields if the Tweet contains a place and if you've also included the `expansions=geo.place_id` query parameter in your request. While the place ID will be located in the Tweet object, you will find this ID and all additional place fields in the `includes` data object. |
| `poll.fields` Optional  | enum (`duration_minutes`, `end_datetime`, `id`, `options`, `voting_status`) | This fields parameter enables you to select which specific poll fields will deliver in each returned Tweet. Specify the desired fields in a comma-separated list without spaces between commas and fields. The Tweet will only return poll fields if the Tweet contains a poll and if you've also included the `expansions=attachments.poll_ids` query parameter in your request. While the poll ID will be located in the Tweet object, you will find this ID and all additional poll fields in the `includes` data object. |
| `since_id` Optional  | string | Returns results with a Tweet ID greater than (that is, more recent than) the specified 'since' Tweet ID. Only the 3200 most recent Tweets are available. The result will exclude the `since_id`. If the limit of Tweets has occurred since the `since_id`, the `since_id` will be forced to the oldest ID available. |
| `start_time` Optional  | date (ISO 8601) | YYYY-MM-DDTHH:mm:ssZ (ISO 8601/RFC 3339). The oldest or earliest UTC timestamp from which the Tweets will be provided. Only the 3200 most recent Tweets are available. Timestamp is in second granularity and is inclusive (for example, 12:00:01 includes the first second of the minute). Minimum allowable time is 2010-11-06T00:00:00ZPlease note that this parameter does not support a millisecond value. |
| `tweet.fields` Optional  | enum (`attachments`, `author_id`, `context_annotations`, `conversation_id`, `created_at`, `edit_controls`, `entities`, `geo`, `id`, `in_reply_to_user_id`, `lang`, `non_public_metrics`, `public_metrics`, `organic_metrics`, `promoted_metrics`, `possibly_sensitive`, `referenced_tweets`, `reply_settings`, `source`, `text`, `withheld`) | This fields parameter enables you to select which specific Tweet fields will deliver in each returned Tweet object. Specify the desired fields in a comma-separated list without spaces between commas and fields. You can also pass the `expansions=referenced_tweets.id` expansion to return the specified fields for both the original Tweet and any included referenced Tweets. The requested Tweet fields will display in both the original Tweet data object, as well as in the referenced Tweet expanded data object that will be located in the `includes` data object. |
| `until_id` Optional  | string | Returns results with a Tweet ID less than (that is, older than) the specified 'until' Tweet ID. Only the 3200 most recent Tweets are available. The result will exclude the `until_id`. If the limit of Tweets has occurred since the `until_id`, the `until_id` will be forced to the most recent ID available. |
| `user.fields` Optional  | enum (`created_at`, `description`, `entities`, `id`, `location`, `most_recent_tweet_id`, `name`, `pinned_tweet_id`, `profile_image_url`, `protected`, `public_metrics`, `url`, `username`, `verified`, `verified_type`, `withheld`) | This fields parameter enables you to select which specific user fields will deliver in each returned Tweet. Specify the desired fields in a comma-separated list without spaces between commas and fields. While the user ID will be located in the original Tweet object, you will find this ID and all additional user fields in the `includes` data object. You must also pass one of the user expansions to return the desired user fields:* `expansions=author_id`
* `expansions=entities.mentions.username`
* `expansions=in_reply_to_user_id`
* `expansions=referenced_tweets.id.author_id`
 |

### Example code with offical SDKs

* TypeScript (Default fields)
* TypeScript (Optional fields)
* Java (Default fields)
* Java (Optional fields)

 TypeScript (Default fields)

 TypeScript (Optional fields)

 Java (Default fields)

 Java (Optional fields)

```
      (async () => {
  try {
    const usersTweets = await twitterClient.tweets.usersIdTweets(
      //The ID of the User to list Tweets of
      2244994945
    );
    console.dir(usersTweets, {
      depth: null,
    });
  } catch (error) {
    console.log(error);
  }
})();

```

```
      (async () => {
  try {
    const usersTweets = await twitterClient.tweets.usersIdTweets(
      //The ID of the User to list Tweets of
      2244994945,
      {
        //A comma separated list of fields to expand
        expansions: ["author_id"],
        //A comma separated list of Tweet fields to display
        "tweet.fields": [
          "created_at",
          "author_id",
          "conversation_id",
          "public_metrics",
          "context_annotations",
        ],
        //A comma separated list of User fields to display
        "user.fields": ["username"],
        //The maximum number of results
        max_results: 5,
      }
    );
    console.dir(usersTweets, {
      depth: null,
    });
  } catch (error) {
    console.log(error);
  }
})();

```

```
      // String | The ID of the User to list Tweets of
String id = "2244994945";
try {
    GenericTweetsTimelineResponse result = apiInstance.tweets().usersIdTweets(id, null, null, null, null, null, null, null, null, null, null, null, null, null);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling TweetsApi#usersIdTweets");
    System.err.println("Status code: " + e.getCode());
    System.err.println("Reason: " + e.getResponseBody());
    System.err.println("Response headers: " + e.getResponseHeaders());
    e.printStackTrace();
}

```

```
      // Set the params values
// For full list of params visit - https://github.com/twitterdev/twitter-api-java-sdk/blob/main/docs/TweetsApi.md#usersIdTweets
// String | The ID of the User to list Tweets of
String id = "2244994945";
// Integer | The maximum number of results
Integer maxResults = 5;
// Set<String> | A comma separated list of fields to expand
Set<String> expansions = new HashSet<>(Arrays.asList("author_id"));
// Set<String> | A comma separated list of Tweet fields to display
Set<String> tweetFields = new HashSet<>(Arrays.asList("created_at","author_id","conversation_id","public_metrics","context_annotations"));
// Set<String> | A comma separated list of User fields to display
Set<String> userFields = new HashSet<>(Arrays.asList("username"));
try {
    GenericTweetsTimelineResponse result = apiInstance.tweets().usersIdTweets(id, null, null, maxResults, null, null, null, null, expansions, tweetFields, userFields, null, null, null);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling TweetsApi#usersIdTweets");
    System.err.println("Status code: " + e.getCode());
    System.err.println("Reason: " + e.getResponseBody());
    System.err.println("Response headers: " + e.getResponseHeaders());
    e.printStackTrace();
}

```

### Example responses

* Default fields
* Optional fields
* All fields

 Default fields

 Optional fields

 All fields

```
      {
  "data": [
    {
      "id": "1338971066773905408",
      "edit_history_tweet_ids": [
        "1338971066773905408"
      ],
      "text": "💡 Using Twitter data for academic research? Join our next livestream this Friday @ 9am PT on https://t.co/GrtBOXh5Y1!n n@SuhemParack will show how to get started with recent search &amp; filtered stream endpoints on the #TwitterAPI v2, the new Tweet payload, annotations, &amp; more. https://t.co/IraD2Z7wEg"
    },
    {
      "id": "1338923691497959425",
      "edit_history_tweet_ids": [
        "1338923691497959425"
      ],
      "text": "📈 Live now with @jessicagarson and @i_am_daniele! https://t.co/Y1AFzsTTxb"
    },
    {
      "id": "1337498609819021312",
      "edit_history_tweet_ids": [
        "1337498609819021312"
      ],
      "text": "Thanks to everyone who tuned in today to make music with the #TwitterAPI!nnNext week on Twitch - @iamdaniele and @jessicagarson will show you how to integrate the #TwitterAPI and Google Sheets 📈. Tuesday, Dec 15th at 2pm ET. nnhttps://t.co/SQziic6eyp"
    },
    {
      "id": "1337464482654793740",
      "edit_history_tweet_ids": [
        "1337464482654793740"
      ],
      "text": "🎧💻 We're live! Tune in! 🎶 https://t.co/FSYP4rJdHr"
    },
    {
      "id": "1337122535188652033",
      "edit_history_tweet_ids": [
        "1337122535188652033"
      ],
      "text": "👂We want to hear what you think about our plans. As we continue to build our new product tracks, your feedback is essential to shaping the future of the Twitter API. Share your thoughts on this survey: https://t.co/dkIqFGPji7"
    },
    {
      "id": "1337122534173663235",
      "edit_history_tweet_ids": [
        "1337122534173663235"
      ],
      "text": "Is 2020 over yet?nDespite everything that happened this year, thousands of you still made the time to learn, play, and build incredible things on the new #TwitterAPI.nWe want to share some of your stories and give you a preview of what’s to come next year.nhttps://t.co/VpOKT22WgF"
    },
    {
      "id": "1336463248510623745",
      "edit_history_tweet_ids": [
        "1336463248510623745"
      ],
      "text": "🎧 Headphones on: watch @jessicagarson build an interactive app to write music using SuperCollider, Python, FoxDot, and the new Twitter API. Streaming Friday 1:30 ET on our new Twitch channel 🎶💻 https://t.co/SQziic6eyp"
    },
    {
      "id": "1334987486343299072",
      "edit_history_tweet_ids": [
        "1334987486343299072"
      ],
      "text": "console.log('Happy birthday, JavaScript!');"
    },
    {
      "id": "1334920270587584521",
      "edit_history_tweet_ids": [
        "1334920270587584521"
      ],
      "text": "Live now!nJoin the first ever @Twitch stream from TwitterDev https://t.co/x33fiVIi7B"
    },
    {
      "id": "1334564488884862976",
      "edit_history_tweet_ids": [
        "1334564488884862976"
      ],
      "text": "Before we release new #TwitterAPI endpoints, we let developers test drive a prototype of our intended design. @i_am_daniele takes you behind the scenes of an endpoint in the making. https://t.co/NNTDnciwNq"
    }
  ],
  "meta": {
    "oldest_id": "1334564488884862976",
    "newest_id": "1338971066773905408",
    "result_count": 10,
    "next_token": "7140dibdnow9c7btw3w29grvxfcgvpb9n9coehpk7xz5i"
  }
}
```

```
      {
  "data": [
    {
      "public_metrics": {
        "retweet_count": 5,
        "reply_count": 2,
        "like_count": 22,
        "quote_count": 0
      },
      "text": "Live now! https://t.co/9BbWekeWq2",
      "author_id": "2244994945",
      "id": "1374405406261268481",
      "edit_history_tweet_ids": [
        "1374405406261268481"
      ],
      "created_at": "2021-03-23T16:59:18.000Z",
      "context_annotations": [
        {
          "domain": {
            "id": "46",
            "name": "Brand Category",
            "description": "Categories within Brand Verticals that narrow down the scope of Brands"
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
        }
      ],
      "conversation_id": "1374405406261268481"
    },
    {
      "public_metrics": {
        "retweet_count": 7,
        "reply_count": 1,
        "like_count": 21,
        "quote_count": 2
      },
      "text": "Hope to see you tomorrow at 1 pm EST for APIs 101! nhttps://t.co/GrtBOXyHmB https://t.co/YyQfmgiLlL",
      "author_id": "2244994945",
      "id": "1374104599456534531",
      "edit_history_tweet_ids": [
        "1374104599456534531"
      ],
      "created_at": "2021-03-22T21:04:00.000Z",
      "context_annotations": [
        {
          "domain": {
            "id": "46",
            "name": "Brand Category",
            "description": "Categories within Brand Verticals that narrow down the scope of Brands"
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
        }
      ],
      "conversation_id": "1374104599456534531"
    },
    {
      "public_metrics": {
        "retweet_count": 18,
        "reply_count": 3,
        "like_count": 92,
        "quote_count": 6
      },
      "text": "Looking to get started with the Twitter API but new to APIs in general? @jessicagarson will walk you through everything you need to know in APIs 101 session. She’ll use examples using our v2 endpoints, Tuesday, March 23rd at 1 pm EST.nnJoin us on Twitchnhttps://t.co/GrtBOXyHmB",
      "author_id": "2244994945",
      "id": "1373001119480344583",
      "edit_history_tweet_ids": [
        "1373001119480344583"
      ],
      "created_at": "2021-03-19T19:59:10.000Z",
      "context_annotations": [
        {
          "domain": {
            "id": "46",
            "name": "Brand Category",
            "description": "Categories within Brand Verticals that narrow down the scope of Brands"
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
        }
      ],
      "conversation_id": "1373001119480344583"
    },
    {
      "public_metrics": {
        "retweet_count": 4,
        "reply_count": 0,
        "like_count": 21,
        "quote_count": 1
      },
      "text": "Thanks to everyone who joined and made today a great session! 🙌 nnIf weren't able to attend, we've got you covered. Academic researchers can now sign up for office hours for help using the new product track. See how you can sign up, here 👇nhttps://t.co/duIkd27lPx https://t.co/AP9YY4F8FG",
      "author_id": "2244994945",
      "id": "1372627771717869568",
      "edit_history_tweet_ids": [
        "1372627771717869568"
      ],
      "created_at": "2021-03-18T19:15:37.000Z",
      "context_annotations": [
        {
          "domain": {
            "id": "46",
            "name": "Brand Category",
            "description": "Categories within Brand Verticals that narrow down the scope of Brands"
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
        }
      ],
      "conversation_id": "1372627771717869568"
    },
    {
      "public_metrics": {
        "retweet_count": 0,
        "reply_count": 0,
        "like_count": 1,
        "quote_count": 0
      },
      "text": "@geet_qcp @suhemparack Hey! We have good news, we just introduced Academic Research office hours. Hopefully, this lets you sign up for a day/time where you have flexibility:  https://t.co/duIkd27lPxnnWe do also have a resources page, which includes n code samples shared today https://t.co/0SfXa84EDO",
      "author_id": "2244994945",
      "id": "1372625612460810242",
      "edit_history_tweet_ids": [
        "1372625612460810242"
      ],
      "created_at": "2021-03-18T19:07:02.000Z",
      "context_annotations": [
        {
          "domain": {
            "id": "46",
            "name": "Brand Category",
            "description": "Categories within Brand Verticals that narrow down the scope of Brands"
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
        }
      ],
      "conversation_id": "1371363033352638467"
    }
  ],
  "includes": {
    "users": [
      {
        "id": "2244994945",
        "name": "Twitter Dev",
        "username": "TwitterDev"
      }
    ]
  },
  "meta": {
    "oldest_id": "1372625612460810242",
    "newest_id": "1374405406261268481",
    "result_count": 5,
    "next_token": "7140dibdnow9c7btw3w3xyyhxcirw2ov9mjp7gczc93xu"
  }
}
```

```
      {
  "data": [
    {
      "public_metrics": {
        "retweet_count": 5,
        "reply_count": 2,
        "like_count": 22,
        "quote_count": 0
      },
      "source": "Twitter Web App",
      "entities": {
        "urls": [
          {
            "start": 10,
            "end": 33,
            "url": "https://t.co/9BbWekeWq2",
            "expanded_url": "https://twitter.com/TwitterDev/status/1374104599456534531",
            "display_url": "twitter.com/TwitterDev/sta…"
          }
        ]
      },
      "id": "1374405406261268481",
      "edit_history_tweet_ids": [
        "1374405406261268481"
      ],
      "referenced_tweets": [
        {
          "type": "quoted",
          "id": "1374104599456534531"
        }
      ],
      "conversation_id": "1374405406261268481",
      "text": "Live now! https://t.co/9BbWekeWq2",
      "author_id": "2244994945",
      "created_at": "2021-03-23T16:59:18.000Z",
      "reply_settings": "everyone",
      "lang": "en",
      "context_annotations": [
        {
          "domain": {
            "id": "46",
            "name": "Brand Category",
            "description": "Categories within Brand Verticals that narrow down the scope of Brands"
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
        }
      ],
      "possibly_sensitive": false
    },
    {
      "public_metrics": {
        "retweet_count": 7,
        "reply_count": 1,
        "like_count": 21,
        "quote_count": 2
      },
      "source": "Twitter Web App",
      "entities": {
        "annotations": [
          {
            "start": 41,
            "end": 48,
            "probability": 0.411,
            "type": "Product",
            "normalized_text": "APIs 101"
          }
        ],
        "urls": [
          {
            "start": 52,
            "end": 75,
            "url": "https://t.co/GrtBOXyHmB",
            "expanded_url": "http://twitch.tv/twitterdev",
            "display_url": "twitch.tv/twitterdev"
          },
          {
            "start": 76,
            "end": 99,
            "url": "https://t.co/YyQfmgiLlL",
            "expanded_url": "https://twitter.com/TwitterDev/status/1373001119480344583",
            "display_url": "twitter.com/TwitterDev/sta…"
          }
        ]
      },
      "id": "1374104599456534531",
      "edit_history_tweet_ids": [
        "1374104599456534531"
      ],
      "referenced_tweets": [
        {
          "type": "quoted",
          "id": "1373001119480344583"
        }
      ],
      "conversation_id": "1374104599456534531",
      "text": "Hope to see you tomorrow at 1 pm EST for APIs 101! nhttps://t.co/GrtBOXyHmB https://t.co/YyQfmgiLlL",
      "author_id": "2244994945",
      "created_at": "2021-03-22T21:04:00.000Z",
      "reply_settings": "everyone",
      "lang": "en",
      "context_annotations": [
        {
          "domain": {
            "id": "46",
            "name": "Brand Category",
            "description": "Categories within Brand Verticals that narrow down the scope of Brands"
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
        }
      ],
      "possibly_sensitive": false
    },
    {
      "public_metrics": {
        "retweet_count": 18,
        "reply_count": 3,
        "like_count": 92,
        "quote_count": 6
      },
      "source": "Twitter Web App",
      "entities": {
        "annotations": [
          {
            "start": 32,
            "end": 42,
            "probability": 0.5425,
            "type": "Product",
            "normalized_text": "Twitter API"
          },
          {
            "start": 140,
            "end": 147,
            "probability": 0.521,
            "type": "Product",
            "normalized_text": "APIs 101"
          }
        ],
        "urls": [
          {
            "start": 254,
            "end": 277,
            "url": "https://t.co/GrtBOXyHmB",
            "expanded_url": "http://twitch.tv/twitterdev",
            "display_url": "twitch.tv/twitterdev"
          }
        ],
        "mentions": [
          {
            "start": 72,
            "end": 86,
            "username": "jessicagarson"
          }
        ]
      },
      "id": "1373001119480344583",
      "edit_history_tweet_ids": [
        "1373001119480344583"
      ],
      "conversation_id": "1373001119480344583",
      "text": "Looking to get started with the Twitter API but new to APIs in general? @jessicagarson will walk you through everything you need to know in APIs 101 session. She’ll use examples using our v2 endpoints, Tuesday, March 23rd at 1 pm EST.nnJoin us on Twitchnhttps://t.co/GrtBOXyHmB",
      "author_id": "2244994945",
      "created_at": "2021-03-19T19:59:10.000Z",
      "reply_settings": "everyone",
      "lang": "en",
      "context_annotations": [
        {
          "domain": {
            "id": "46",
            "name": "Brand Category",
            "description": "Categories within Brand Verticals that narrow down the scope of Brands"
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
        }
      ],
      "possibly_sensitive": false
    },
    {
      "public_metrics": {
        "retweet_count": 4,
        "reply_count": 0,
        "like_count": 21,
        "quote_count": 1
      },
      "source": "Twitter Web App",
      "entities": {
        "urls": [
          {
            "start": 240,
            "end": 263,
            "url": "https://t.co/duIkd27lPx",
            "expanded_url": "https://twittercommunity.com/t/announcing-monthly-office-hours-for-the-academic-research-product-track/151028",
            "display_url": "twittercommunity.com/t/announcing-m…",
            "images": [
              {
                "url": "https://pbs.twimg.com/news_img/1372625618605469698/6E0uKJr7?format=jpg&name=orig",
                "width": 1200,
                "height": 630
              },
              {
                "url": "https://pbs.twimg.com/news_img/1372625618605469698/6E0uKJr7?format=jpg&name=150x150",
                "width": 150,
                "height": 150
              }
            ],
            "status": 200,
            "title": "Announcing monthly office hours for the academic research product track",
            "description": "We are excited to offer office hours for academic researchers that are using the Academic Research product track on the new Twitter API. This is an opportunity for users of this new product track to get their technical questions answered, and helping you get research data with the v2 API. Most office hours will be held on the last Thursday of every month, from 10:00 am PST to 11:30 am PST. We will also try and accommodate other timezones for some of these sessions. How does it work? First, re...",
            "unwound_url": "https://twittercommunity.com/t/announcing-monthly-office-hours-for-the-academic-research-product-track/151028"
          },
          {
            "start": 264,
            "end": 287,
            "url": "https://t.co/AP9YY4F8FG",
            "expanded_url": "https://twitter.com/TwitterDev/status/1371363033352638467",
            "display_url": "twitter.com/TwitterDev/sta…"
          }
        ]
      },
      "id": "1372627771717869568",
      "edit_history_tweet_ids": [
        "1372627771717869568"
      ],
      "referenced_tweets": [
        {
          "type": "quoted",
          "id": "1371363033352638467"
        }
      ],
      "conversation_id": "1372627771717869568",
      "text": "Thanks to everyone who joined and made today a great session! 🙌 nnIf weren't able to attend, we've got you covered. Academic researchers can now sign up for office hours for help using the new product track. See how you can sign up, here 👇nhttps://t.co/duIkd27lPx https://t.co/AP9YY4F8FG",
      "author_id": "2244994945",
      "created_at": "2021-03-18T19:15:37.000Z",
      "reply_settings": "everyone",
      "lang": "en",
      "context_annotations": [
        {
          "domain": {
            "id": "46",
            "name": "Brand Category",
            "description": "Categories within Brand Verticals that narrow down the scope of Brands"
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
        }
      ],
      "possibly_sensitive": false
    },
    {
      "public_metrics": {
        "retweet_count": 0,
        "reply_count": 0,
        "like_count": 1,
        "quote_count": 0
      },
      "source": "Twitter Web App",
      "entities": {
        "urls": [
          {
            "start": 175,
            "end": 198,
            "url": "https://t.co/duIkd27lPx",
            "expanded_url": "https://twittercommunity.com/t/announcing-monthly-office-hours-for-the-academic-research-product-track/151028",
            "display_url": "twittercommunity.com/t/announcing-m…",
            "images": [
              {
                "url": "https://pbs.twimg.com/news_img/1372625618605469698/6E0uKJr7?format=jpg&name=orig",
                "width": 1200,
                "height": 630
              },
              {
                "url": "https://pbs.twimg.com/news_img/1372625618605469698/6E0uKJr7?format=jpg&name=150x150",
                "width": 150,
                "height": 150
              }
            ],
            "status": 200,
            "title": "Announcing monthly office hours for the academic research product track",
            "description": "We are excited to offer office hours for academic researchers that are using the Academic Research product track on the new Twitter API. This is an opportunity for users of this new product track to get their technical questions answered, and helping you get research data with the v2 API. Most office hours will be held on the last Thursday of every month, from 10:00 am PST to 11:30 am PST. We will also try and accommodate other timezones for some of these sessions. How does it work? First, re...",
            "unwound_url": "https://twittercommunity.com/t/announcing-monthly-office-hours-for-the-academic-research-product-track/151028"
          },
          {
            "start": 277,
            "end": 300,
            "url": "https://t.co/0SfXa84EDO",
            "expanded_url": "https://developer.twitter.com/en/solutions/academic-research/resources",
            "display_url": "developer.twitter.com/en/solutions/a…"
          }
        ],
        "mentions": [
          {
            "start": 0,
            "end": 9,
            "username": "geet_qcp"
          },
          {
            "start": 10,
            "end": 22,
            "username": "suhemparack"
          }
        ]
      },
      "id": "1372625612460810242",
      "edit_history_tweet_ids": [
        "1372625612460810242"
      ],
      "referenced_tweets": [
        {
          "type": "replied_to",
          "id": "1371363774729363460"
        }
      ],
      "conversation_id": "1371363033352638467",
      "text": "@geet_qcp @suhemparack Hey! We have good news, we just introduced Academic Research office hours. Hopefully, this lets you sign up for a day/time where you have flexibility:  https://t.co/duIkd27lPxnnWe do also have a resources page, which includes n code samples shared today https://t.co/0SfXa84EDO",
      "author_id": "2244994945",
      "created_at": "2021-03-18T19:07:02.000Z",
      "reply_settings": "everyone",
      "lang": "en",
      "in_reply_to_user_id": "3117973774",
      "context_annotations": [
        {
          "domain": {
            "id": "46",
            "name": "Brand Category",
            "description": "Categories within Brand Verticals that narrow down the scope of Brands"
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
        }
      ],
      "possibly_sensitive": false
    }
  ],
  "includes": {
    "users": [
      {
        "profile_image_url": "https://pbs.twimg.com/profile_images/1354494203451961345/d8HkZl6p_normal.jpg",
        "id": "2244994945",
        "url": "https://t.co/3ZX3TNiZCY",
        "public_metrics": {
          "followers_count": 517602,
          "following_count": 2033,
          "tweet_count": 3689,
          "listed_count": 1732
        },
        "name": "Twitter Dev",
        "entities": {
          "url": {
            "urls": [
              {
                "start": 0,
                "end": 23,
                "url": "https://t.co/3ZX3TNiZCY",
                "expanded_url": "https://developer.twitter.com/en/community",
                "display_url": "developer.twitter.com/en/community"
              }
            ]
          },
          "description": {
            "hashtags": [
              {
                "start": 17,
                "end": 28,
                "tag": "TwitterDev"
              },
              {
                "start": 105,
                "end": 116,
                "tag": "TwitterAPI"
              }
            ]
          }
        },
        "username": "TwitterDev",
        "location": "127.0.0.1",
        "verified": true,
        "protected": false,
        "description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",
        "pinned_tweet_id": "1354143047324299264",
        "created_at": "2013-12-14T04:35:55.000Z"
      },
      {
        "profile_image_url": "https://pbs.twimg.com/profile_images/1357142766933917699/uvTbiTAs_normal.jpg",
        "id": "15772978",
        "url": "https://t.co/7o2d6oAKln",
        "public_metrics": {
          "followers_count": 3517,
          "following_count": 2723,
          "tweet_count": 6969,
          "listed_count": 129
        },
        "name": "Jessica Garson",
        "entities": {
          "url": {
            "urls": [
              {
                "start": 0,
                "end": 23,
                "url": "https://t.co/7o2d6oAKln",
                "expanded_url": "http://github.com/JessicaGarson",
                "display_url": "github.com/JessicaGarson"
              }
            ]
          },
          "description": {
            "mentions": [
              {
                "start": 19,
                "end": 27,
                "username": "Twitter"
              }
            ]
          }
        },
        "username": "jessicagarson",
        "location": "Brooklyn, NY",
        "verified": false,
        "protected": false,
        "description": "Developer Advocate @Twitter. Python programmer.  Noted thought leader on vegan snacks. Makes music as Messica Arson.",
        "created_at": "2008-08-08T02:16:23.000Z"
      },
      {
        "profile_image_url": "https://pbs.twimg.com/profile_images/1230703695051935747/TbQKe91L_normal.jpg",
        "id": "857699969263964161",
        "url": "https://t.co/8IkCzCDr19",
        "public_metrics": {
          "followers_count": 917,
          "following_count": 540,
          "tweet_count": 470,
          "listed_count": 16
        },
        "name": "Suhem Parack",
        "entities": {
          "url": {
            "urls": [
              {
                "start": 0,
                "end": 23,
                "url": "https://t.co/8IkCzCDr19",
                "expanded_url": "https://developer.twitter.com",
                "display_url": "developer.twitter.com"
              }
            ]
          },
          "description": {
            "mentions": [
              {
                "start": 42,
                "end": 50,
                "username": "Twitter"
              }
            ]
          }
        },
        "username": "suhemparack",
        "location": "Seattle, WA",
        "verified": false,
        "protected": false,
        "description": "Developer Relations for Academic Research @Twitter. Talk to me about research with Twitter data. Views are my own",
        "pinned_tweet_id": "1296498078233571329",
        "created_at": "2017-04-27T20:56:22.000Z"
      }
    ],
    "tweets": [
      {
        "public_metrics": {
          "retweet_count": 7,
          "reply_count": 1,
          "like_count": 21,
          "quote_count": 2
        },
        "source": "Twitter Web App",
        "entities": {
          "annotations": [
            {
              "start": 41,
              "end": 48,
              "probability": 0.411,
              "type": "Product",
              "normalized_text": "APIs 101"
            }
          ],
          "urls": [
            {
              "start": 52,
              "end": 75,
              "url": "https://t.co/GrtBOXyHmB",
              "expanded_url": "http://twitch.tv/twitterdev",
              "display_url": "twitch.tv/twitterdev"
            },
            {
              "start": 76,
              "end": 99,
              "url": "https://t.co/YyQfmgiLlL",
              "expanded_url": "https://twitter.com/TwitterDev/status/1373001119480344583",
              "display_url": "twitter.com/TwitterDev/sta…"
            }
          ]
        },
        "id": "1374104599456534531",
        "edit_history_tweet_ids": [
          "1374104599456534531"
        ],
        "referenced_tweets": [
          {
            "type": "quoted",
            "id": "1373001119480344583"
          }
        ],
        "conversation_id": "1374104599456534531",
        "text": "Hope to see you tomorrow at 1 pm EST for APIs 101! nhttps://t.co/GrtBOXyHmB https://t.co/YyQfmgiLlL",
        "author_id": "2244994945",
        "created_at": "2021-03-22T21:04:00.000Z",
        "reply_settings": "everyone",
        "lang": "en",
        "context_annotations": [
          {
            "domain": {
              "id": "46",
              "name": "Brand Category",
              "description": "Categories within Brand Verticals that narrow down the scope of Brands"
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
          }
        ],
        "possibly_sensitive": false
      },
      {
        "public_metrics": {
          "retweet_count": 18,
          "reply_count": 3,
          "like_count": 92,
          "quote_count": 6
        },
        "source": "Twitter Web App",
        "entities": {
          "annotations": [
            {
              "start": 32,
              "end": 42,
              "probability": 0.5425,
              "type": "Product",
              "normalized_text": "Twitter API"
            },
            {
              "start": 140,
              "end": 147,
              "probability": 0.521,
              "type": "Product",
              "normalized_text": "APIs 101"
            }
          ],
          "urls": [
            {
              "start": 254,
              "end": 277,
              "url": "https://t.co/GrtBOXyHmB",
              "expanded_url": "http://twitch.tv/twitterdev",
              "display_url": "twitch.tv/twitterdev"
            }
          ],
          "mentions": [
            {
              "start": 72,
              "end": 86,
              "username": "jessicagarson"
            }
          ]
        },
        "id": "1373001119480344583",
        "edit_history_tweet_ids": [
          "1373001119480344583"
        ],
        "conversation_id": "1373001119480344583",
        "text": "Looking to get started with the Twitter API but new to APIs in general? @jessicagarson will walk you through everything you need to know in APIs 101 session. She’ll use examples using our v2 endpoints, Tuesday, March 23rd at 1 pm EST.nnJoin us on Twitchnhttps://t.co/GrtBOXyHmB",
        "author_id": "2244994945",
        "created_at": "2021-03-19T19:59:10.000Z",
        "reply_settings": "everyone",
        "lang": "en",
        "context_annotations": [
          {
            "domain": {
              "id": "46",
              "name": "Brand Category",
              "description": "Categories within Brand Verticals that narrow down the scope of Brands"
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
          }
        ],
        "possibly_sensitive": false
      },
      {
        "public_metrics": {
          "retweet_count": 8,
          "reply_count": 1,
          "like_count": 36,
          "quote_count": 2
        },
        "source": "Twitter Web App",
        "entities": {
          "urls": [
            {
              "start": 188,
              "end": 211,
              "url": "https://t.co/GrtBOXyHmB",
              "expanded_url": "http://twitch.tv/twitterdev",
              "display_url": "twitch.tv/twitterdev",
              "images": [
                {
                  "url": "https://pbs.twimg.com/news_img/1373001120851841025/8EmQiIf3?format=png&name=orig",
                  "width": 300,
                  "height": 300
                },
                {
                  "url": "https://pbs.twimg.com/news_img/1373001120851841025/8EmQiIf3?format=png&name=150x150",
                  "width": 150,
                  "height": 150
                }
              ],
              "status": 200,
              "title": "TwitterDev - Twitch",
              "description": "Brought to you by Twitter's Developer Relations team",
              "unwound_url": "https://www.twitch.tv/twitterdev"
            },
            {
              "start": 250,
              "end": 273,
              "url": "https://t.co/SpuOoD7Dm8",
              "expanded_url": "https://twitter.com/suhemparack/status/1367897834758934530",
              "display_url": "twitter.com/suhemparack/st…"
            }
          ],
          "mentions": [
            {
              "start": 139,
              "end": 151,
              "username": "suhemparack"
            }
          ]
        },
        "id": "1371363033352638467",
        "edit_history_tweet_ids": [
          "1371363033352638467"
        ],
        "referenced_tweets": [
          {
            "type": "quoted",
            "id": "1367897834758934530"
          }
        ],
        "conversation_id": "1371363033352638467",
        "text": "🔎 If you're using v2 full-archive search for Academic Research, you won't want to miss this livestream hosted by our research dev advocate @suhemparack.nnMark your calendars to join us on https://t.co/GrtBOXyHmB Thursday March 18th, 10AM PT/ 1PM ET. https://t.co/SpuOoD7Dm8",
        "author_id": "2244994945",
        "created_at": "2021-03-15T07:30:00.000Z",
        "reply_settings": "everyone",
        "lang": "en",
        "context_annotations": [
          {
            "domain": {
              "id": "46",
              "name": "Brand Category",
              "description": "Categories within Brand Verticals that narrow down the scope of Brands"
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
              "id": "47",
              "name": "Brand",
              "description": "Brands and Companies"
            },
            "entity": {
              "id": "1054826545758396416",
              "name": "Twitch",
              "description": "Twitch"
            }
          }
        ],
        "possibly_sensitive": false
      }
    ]
  },
  "errors": [
    {
      "resource_id": "geet_qcp",
      "parameter": "entities.mentions.username",
      "resource_type": "user",
      "section": "includes",
      "title": "Authorization Error",
      "value": "geet_qcp",
      "detail": "Sorry, you are not authorized to see the user with entities.mentions.username: [geet_qcp].",
      "type": "https://api.twitter.com/2/problems/not-authorized-for-resource"
    },
    {
      "resource_id": "3117973774",
      "parameter": "in_reply_to_user_id",
      "resource_type": "user",
      "section": "includes",
      "title": "Authorization Error",
      "value": "3117973774",
      "detail": "Sorry, you are not authorized to see the user with in_reply_to_user_id: [3117973774].",
      "type": "https://api.twitter.com/2/problems/not-authorized-for-resource"
    },
    {
      "value": "1371363774729363460",
      "detail": "Could not find tweet with referenced_tweets.id: [1371363774729363460].",
      "title": "Not Found Error",
      "resource_type": "tweet",
      "parameter": "referenced_tweets.id",
      "resource_id": "1371363774729363460",
      "type": "https://api.twitter.com/2/problems/resource-not-found"
    }
  ],
  "meta": {
    "oldest_id": "1372625612460810242",
    "newest_id": "1374405406261268481",
    "result_count": 5,
    "next_token": "7140dibdnow9c7btw3w3xyyhxcirw2ov9mjp7gczc93xu"
  }
}
```

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `id` Default  | string | Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. |
| `text` Default  | string | The content of the Tweet.To return this field, add `tweet.fields=text` in the request's query parameter. |
| `created_at` | date (ISO 8601) | Creation time of the Tweet. For example: `2020-12-10T20:00:10Z`To return this field, add `tweet.fields=created_at` in the request's query parameter. |
| `author_id` | string | Unique identifier of this user. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers.You can obtain the expanded object in `includes.users` by adding `expansions=author_id` in the request's query parameter. |
| `edit_history_tweet_ids` Default  | array | Unique identifiers indicating all versions of an edited Tweet. For Tweets with no edits, there will be one ID. For Tweets with an edit history, there will be multiple IDs, arranged in ascending order reflecting the order of edit, with the most recent version in the last position of the array. |
| `edit_controls` | object | Indicates if a Tweet is eligible for edit, how long it is editable for, and the number of remaining edits.The `is_edit_eligible` field indicates if a Tweet was eligible for edit when published. This field is not dynamic and won't toggle from True to False when a Tweet reaches its editable time limit, or maximum number of edits. The following Tweet features will cause this field to be false:* Tweet is promoted
* Tweet has a poll
* Tweet is a non-self-thread reply
* Tweet is a Retweet (note that Quote Tweets are eligible for edit)
* Tweet is nullcast
* Community Tweet
* Superfollow Tweet
* Collaborative Tweet
`{
   "edit_controls": {
    "is_edit_eligible": true,
    "editable_until": "2022-08-21 09:35:20.311",
    "edits_remaining": 4
  }
}`
Editable Tweets can be edited for the first 30 minutes after creation and can be edited up to five times.
To return this field, add `tweet.fields=edit_controls` in the request's query parameter. |
| `conversation_id` | string | The Tweet ID of the original Tweet of the conversation (which includes direct replies, replies of replies).To return this field, add `tweet.fields=conversation_id` in the request's query parameter. |
| `note_tweet` | object | Information about Tweets with more than 280 characters.To return this field, add `tweet.fields=note_tweet` in the request's query parameter. |
| `in_reply_to_user_id` | string | If this Tweet is a Reply, indicates the user ID of the parent Tweet's author. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers.You can obtain the expanded object in `includes.users` by adding `expansions=in_reply_to_user_id` in the request's query parameter. |
| `referenced_tweets` | array | A list of Tweets this Tweet refers to. For example, if the parent Tweet is a Retweet, a Retweet with comment (also known as Quoted Tweet) or a Reply, it will include the related Tweet referenced to by its parent.To return this field, add `tweet.fields=referenced_tweets` in the request's query parameter. |
| `referenced_tweets.type` | enum (`retweeted`, `quoted`, `replied_to`) | Indicates the type of relationship between this Tweet and the Tweet returned in the response: `retweeted` (this Tweet is a Retweet), `quoted` (a Retweet with comment, also known as Quoted Tweet), or `replied_to` (this Tweet is a reply). |
| `referenced_tweets.id` | string | The unique identifier of the referenced Tweet.You can obtain the expanded object in `includes.tweets` by adding `expansions=referenced_tweets.id` in the request's query parameter. |
| `attachments` | object | Specifies the type of attachments (if any) present in this Tweet.To return this field, add `tweet.fields=attachments` in the request's query parameter. |
| `attachments.media_keys` | array | List of unique identifiers of media attached to this Tweet. These identifiers use the same media key format as those returned by the Media Library.You can obtain the expanded object in `includes.media` by adding `expansions=attachments.media_keys` in the request's query parameter. |
| `attachments.poll_ids` | array | List of unique identifiers of polls present in the Tweets returned. These are returned as a string in order to avoid complications with languages and tools that cannot handle large integers.You can obtain the expanded object in `includes.polls` by adding `expansions=attachments.polls_ids` in the request's query parameter. |
| `geo` | object | Contains details about the location tagged by the user in this Tweet, if they specified one.To return this field, add `tweet.fields=geo` in the request's query parameter. |
| `geo.coordinates` | object | Contains details about the coordinates of the location tagged by the user in this Tweet, if they specified one.To return this field, add `tweet.fields=geo.coordinates` in the request's query parameter. |
| `geo.coordinates.type` | string | Describes the type of coordinate. The only value supported at present is `Point`. |
| `geo.coordinates.coordinates` | array | A pair of decimal values representing the precise location of the user (latitude, longitude). This value be `null` unless the user explicitly shared their precise location. |
| `geo.place_id` | string | The unique identifier of the place, if this is a point of interest tagged in the Tweet.You can obtain the expanded object in `includes.places` by adding `expansions=geo.place_id` in the request's query parameter. |
| `context_annotations` | array | Contains context annotations for the Tweet.To return this field, add `tweet.fields=context_annotations` in the request's query parameter. |
| `context_annotations.domain` | object | Contains elements which identify detailed information regarding the domain classification based on Tweet text. |
| `context_annotations.domain.id` | string | Contains the numeric value of the domain. |
| `context_annotations.domain.name` | string | Domain name based on the Tweet text. |
| `context_annotations.domain.description` | string | Long form description of domain classification. |
| `context_annotations.entity` | object | Contains elements which identify detailed information regarding the domain classification bases on Tweet text. |
| `context_annotations.entity.id` | string | Unique value which correlates to an explicitly mentioned Person, Place, Product or Organization |
| `context_annotations.entity.name` | string | Name or reference of entity referenced in the Tweet. |
| `context_annotations.entity.description` | string | Additional information regarding referenced entity. |
| `entities` | object | Contains details about text that has a special meaning in a Tweet.To return this field, add `tweet.fields=entities` in the request's query parameter. |
| `entities.annotations` | array | Contains details about annotations relative to the text within a Tweet. |
| `entities.annotations.start` | integer | The start position (zero-based) of the text used to annotate the Tweet. All start indices are inclusive. |
| `entities.annotations.end` | integer | The end position (zero based) of the text used to annotate the Tweet. While all other end indices are exclusive, this one is inclusive. |
| `entities.annotations.probability` | number | The confidence score for the annotation as it correlates to the Tweet text. |
| `entities.annotations.type` | string | The description of the type of entity identified when the Tweet text was interpreted. |
| `entities.annotations.normalized_text` | string | The text used to determine the annotation type. |
| `entities.urls` | array | Contains details about text recognized as a URL. |
| `entities.urls.start` | integer | The start position (zero-based) of the recognized URL within the Tweet. All start indices are inclusive. |
| `entities.urls.end` | integer | The end position (zero-based) of the recognized URL within the Tweet. This end index is exclusive. |
| `entities.urls.url` | string | The URL in the format tweeted by the user. |
| `entities.urls.expanded_url` | string | The fully resolved URL. |
| `entities.urls.display_url` | string | The URL as displayed in the Twitter client. |
| `entities.urls.unwound_url` | string | The full destination URL. |
| `entities.hashtags` | array | Contains details about text recognized as a Hashtag. |
| `entities.hashtags.start` | integer | The start position (zero-based) of the recognized Hashtag within the Tweet. All start indices are inclusive. |
| `entities.hashtags.end` | integer | The end position (zero-based) of the recognized Hashtag within the Tweet. This end index is exclusive. |
| `entities.hashtags.tag` | string | The text of the Hashtag. |
| `entities.mentions` | array | Contains details about text recognized as a user mention. |
| `entities.mentions.start` | integer | The start position (zero-based) of the recognized user mention within the Tweet. All start indices are inclusive. |
| `entities.mentions.end` | integer | The end position (zero-based) of the recognized user mention within the Tweet. This end index is exclusive. |
| `entities.mentions.username` | string | The part of text recognized as a user mention.You can obtain the expanded object in `includes.users` by adding `expansions=entities.mentions.username` in the request's query parameter. |
| `entities.cashtags` | array | Contains details about text recognized as a Cashtag. |
| `entities.cashtags.start` | integer | The start position (zero-based) of the recognized Cashtag within the Tweet. All start indices are inclusive. |
| `entities.cashtags.end` | integer | The end position (zero-based) of the recognized Cashtag within the Tweet. This end index is exclusive. |
| `entities.cashtags.tag` | string | The text of the Cashtag. |
| `withheld` | object | Contains withholding details for withheld content.To return this field, add `tweet.fields=withheld` in the request's query parameter. |
| `withheld.copyright` | boolean | Indicates if the content is being withheld for on the basis of copyright infringement. |
| `withheld.country_codes` | array | Provides a list of countries where this content is not available. |
| `withheld.scope` | enum (`tweet`, `user`) | Indicates whether the content being withheld is a Tweet or a user. |
| `note_tweet` | object | Information for Tweets longer than 280 characters.To return this field, add `tweet.fields=note_tweet` in the request's query parameter. |
| `note_tweet.text` | string | The text for Tweets longer than 280 characters. |
| `note_tweet.entities` | object | Contains details about text that has a special meaning in a Tweet. |
| `note_tweet.entities.urls` | array | Contains details about text recognized as a URL. |
| `note_tweet.entities.mentions` | array | Contains details about text recognized as a user mention. |
| `note_tweet.entities.hashtags` | array | Contains details about text recognized as a Hashtag. |
| `note_tweet.entities.cashtags` | array | Contains details about text recognized as a Cashtag. |
| `public_metrics` | object | Engagement metrics for the Tweet at the time of the request.To return this field, add `tweet.fields=public_metrics` in the request's query parameter. |
| `public_metrics.retweet_count` | integer | Number of times this Tweet has been Retweeted. |
| `public_metrics.reply_count` | integer | Number of Replies of this Tweet. |
| `public_metrics.like_count` | integer | Number of Likes of this Tweet. |
| `public_metrics.quote_count` | integer | Number of times this Tweet has been Retweeted with a comment (also known as Quote). |
| `public_metrics.impression_count` | integer | Number of times this Tweet has been viewed. |
| `public_metrics.bookmark_count` | integer | Number of times this Tweet has been bookmarked. |
| `non_public_metrics` | object | Non-public engagement metrics for the Tweet at the time of the request. This is a private metric, and requires the use of OAuth 2.0 User Context authentication. All non\_public\_metrics are only available for Tweets created the last 30 days.To return this field, add `tweet.fields=non_public_metrics` in the request's query parameter. |
| `non_public_metrics.impression_count` | integer | Number of times the Tweet has been viewed. This uses OAuth 2.0 User Context authentication. All non\_public\_metrics are only available for Tweets created the last 30 days. |
| `non_public_metrics.url_link_clicks` | integer | Number of times a user clicks on a URL link or URL preview card in a Tweet. This is a private metric, and requires the use of OAuth 2.0 User Context authentication. All non\_public\_metrics are only available for Tweets created the last 30 days. |
| `non_public_metrics.user_profile_clicks` | integer | Number of times a user clicks the following portions of a Tweet - display name, user name, profile picture. This is a private metric, and requires the use of OAuth 2.0 User Context authentication. All non\_public\_metrics are only available for Tweets created the last 30 days. |
| `organic_metrics` | object | Organic engagement metrics for the Tweet at the time of the request. Requires user context authentication. All organic\_metrics are only available for Tweets created the last 30 days. |
| `organic_metrics.impression_count` | integer | Number of times the Tweet has been viewed organically (not in Ad placement). This is a private metric, and requires the use of OAuth 2.0 User Context authentication. All organic\_metrics are only available for Tweets created the last 30 days. |
| `organic_metrics.url_link_clicks` | integer | Number of times a user clicks on a URL link or URL preview card in a Tweet organically. This is a private metric, and requires the use of OAuth 2.0 User Context authentication. All organic\_metrics are only available for Tweets created the last 30 days. |
| `organic_metrics.user_profile_clicks` | integer | Number of times a user clicks the following portions of a Tweet organically - display name, user name, profile picture. This is a private metric, and requires the use of OAuth 2.0 User Context authentication. All organic\_metrics are only available for Tweets created the last 30 days. |
| `organic_metrics.retweet_count` | integer | Number of times the Tweet has been Retweeted organically. All organic\_metrics are only available for Tweets created the last 30 days. |
| `organic_metrics.reply_count` | integer | Number of replies the Tweet has received organically. All organic\_metrics are only available for Tweets created the last 30 days. |
| `organic_metrics.like_count` | integer | Number of likes the Tweet has received organically. All organic\_metrics are only available for Tweets created the last 30 days. |
| `promoted_metrics` | object | Engagement metrics for the Tweet at the time of the request in a promoted context. Requires user context authentication. All promoted\_metrics are only available for Tweets created the last 30 days. |
| `promoted_metrics.impression_count` | integer | Number of times the Tweet has been viewed when that Tweet is being promoted. This is a private metric, and requires the use of OAuth 2.0 User Context authentication. All promoted\_metrics are only available for Tweets created the last 30 days. |
| `promoted_metrics.url_link_clicks` | integer | Number of times a user clicks on a URL link or URL preview card in a Tweet when it is being promoted. This is a private metric, and requires the use of OAuth 2.0 User Context authentication. All promoted\_metrics are only available for Tweets created the last 30 days. |
| `promoted_metrics.user_profile_clicks` | integer | Number of times a user clicks the following portions of a Tweet when it is being promoted - display name, user name, profile picture. This is a private metric, and requires the use of OAuth 2.0 User Context authentication. All promoted\_metrics are only available for Tweets created the last 30 days. |
| `promoted_metrics.retweet_count` | integer | Number of times this Tweet has been Retweeted when that Tweet is being promoted. All promoted\_metrics are only available for Tweets created the last 30 days. |
| `promoted_metrics.reply_count` | integer | Number of Replies to this Tweet when that Tweet is being promoted. All promoted\_metrics are only available for Tweets created the last 30 days. |
| `promoted_metrics.like_count` | integer | Number of Likes of this Tweet when that Tweet is being promoted. All promoted\_metrics are only available for Tweets created the last 30 days. |
| `possibly_sensitive` | boolean | Indicates if this Tweet contains URLs marked as sensitive, for example content suitable for mature audiences.To return this field, add `tweet.fields=possibly_sensitive` in the request's query parameter. |
| `lang` | string | Language of the Tweet, if detected by Twitter. Returned as a BCP47 language tag.To return this field, add `tweet.fields=lang` in the request's query parameter. |
| `reply_settings` | string | Shows who can reply to this Tweet. Fields returned are `everyone`, `mentionedUsers`, and `following`.To return this field, add `tweet.fields=reply_settings` in the request's query parameter. |
| `source` | string | The name of the app the user Tweeted from.To return this field, add `tweet.fields=source` in the request's query parameter. |
| `includes` | object | If you include an `expansion` parameter, the referenced objects will be returned if available. |
| `includes.tweets` | array | When including the `expansions=referenced_tweets.id` parameter, this includes a list of referenced Retweets, Quoted Tweets, or replies in the form of Tweet objects with their default fields and any additional fields requested using the `tweet.fields` parameter, assuming there is a referenced Tweet present in the returned Tweet(s). |
| `includes.users` | array | When including the `expansions=author_id` parameter, this includes a list of referenced Tweet authors in the form of user objects with their default fields and any additional fields requested using the `user.fields` parameter. |
| `includes.places` | array | When including the `expansions=geo.place_id` parameter, this includes a list of referenced places in Tweets in the form of place objects with their default fields and any additional fields requested using the `place.fields` parameter, assuming there is a place present in the returned Tweet(s). |
| `includes.media` | array | When including the `expansions=attachments.media_keys` parameter, this includes a list of images, videos, and GIFs included in Tweets in the form of media objects with their default fields and any additional fields requested using the `media.fields` parameter, assuming there is a media attachment present in the returned Tweet(s). |
| `includes.polls` | string | When including the `expansions=attachments.poll_ids` parameter, this includes a list of polls that are attached to Tweets in the form of poll objects with their default fields and any additional fields requested using the `poll.fields` parameter, assuming there is a poll present in the returned Tweet(s). |
| `meta` Default  | object | This object contains information about the number of users returned in the current request and pagination details. |
| `meta.count` Default  | integer | The number of Tweet results returned in the response. |
| `meta.newest_id` Default  | string | The Tweet ID of the most recent Tweet returned in the response. |
| `meta.oldest_id` Default  | string | The Tweet ID of the oldest Tweet returned in the response. |
| `meta.next_token` | string | A value that encodes the next 'page' of results that can be requested, via the `pagination_token` request parameter. |
| `meta.previous_token` | string | A value that encodes the previous 'page' of results that can be requested, via the `pagination_token` request parameter. |
| `errors` | object | Contains details about errors that affected any of the requested Tweets. See Status codes and error messages for more details. |

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