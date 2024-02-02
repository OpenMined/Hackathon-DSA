
GET /2/tweets/:id/quote\_tweets | Docs | Twitter Developer Platform 

GET /2/tweets/:id/quote\_tweets

 GET /2/tweets/:id/quote\_tweets
===============================
Returns Quote Tweets for a Tweet specified by the requested Tweet ID.  
The Tweets returned by this endpoint count towards the Project-level Tweet cap.
Run in Postman ❯Try a live request ❯Build request with API Explorer ❯### Endpoint URL
`https://api.twitter.com/2/tweets/:id/quote_tweets`  
### Authentication and rate limits

|  |  |
| --- | --- |
| Authentication methodssupported by this endpoint | OAuth 2.0 Authorization Code with PKCEOAuth 1.0a is also available for this endpoint.OAuth 2.0 App-only |
| Rate limit | App rate limit (Application-only): 75 requests per 15-minute window shared among all users of your appUser rate limit (User context): 75 requests per 15-minute window per each authenticated user |
### OAuth 2.0 scopes required by this endpoint

|  |
| --- |
| `tweet.read``users.read` |
| Learn more about OAuth 2.0 Authorization Code with PKCE |
### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `id` Required  | string | Unique identifier of the Tweet to request. |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| `exclude` Optional  | enum (`retweets`, `replies`) | Comma-separated list of the types of Tweets to exclude from the response. |
| `expansions` Optional  | enum (`attachments.poll_ids`, `attachments.media_keys`, `author_id`, `edit_history_tweet_ids`, `entities.mentions.username`, `geo.place_id`, `in_reply_to_user_id`, `referenced_tweets.id`, `referenced_tweets.id.author_id`) | Expansions enable you to request additional data objects that relate to the originally returned Tweets. Submit a list of desired expansions in a comma-separated list without spaces. The ID that represents the expanded data object will be included directly in the Tweet data object, but the expanded object metadata will be returned within the `includes` response object, and will also include the ID so that you can match this data object to the original Tweet object.The following data objects can be expanded using this parameter:* The Tweet author's user object
* The user object of the Tweet’s author that the original Tweet is responding to
* Any mentioned users’ object
* Any referenced Tweets’ author’s user object
* Attached media’s object
* Attached poll’s object
* Attached place’s object
* Any referenced Tweets’ object (this includes Tweet objects for previous versions of an edited Tweet)
 |
| `max_results` Optional  | integer | Specifies the number of Tweets to try and retrieve, up to a maximum of 100 per distinct request. By default, 10 results are returned if this parameter is not supplied. The minimum permitted value is 10. It is possible to receive less than the `max_results` per request throughout the pagination process. |
| `media.fields` Optional  | enum (`duration_ms`, `height`, `media_key`, `preview_image_url`, `type`, `url`, `width`, `public_metrics`, `non_public_metrics`, `organic_metrics`, `promoted_metrics`, `alt_text`, `variants`) | This fields parameter enables you to select which specific media fields will deliver in each returned Tweet. Specify the desired fields in a comma-separated list without spaces between commas and fields. The Tweet will only return media fields if the Tweet contains media and if you've also included the `expansions=attachments.media_keys` query parameter in your request. While the media ID will be located in the Tweet object, you will find this ID and all additional media fields in the `includes` data object. |
| `pagination_token` Optional  | string | This parameter is used to move forwards through 'pages' of results, based on the value of the `next_token`. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified. |
| `place.fields` Optional  | enum (`contained_within`, `country`, `country_code`, `full_name`, `geo`, `id`, `name`, `place_type`) | This fields parameter enables you to select which specific place fields will deliver in each returned Tweet. Specify the desired fields in a comma-separated list without spaces between commas and fields. The Tweet will only return place fields if the Tweet contains a place and if you've also included the `expansions=geo.place_id` query parameter in your request. While the place ID will be located in the Tweet object, you will find this ID and all additional place fields in the `includes` data object. |
| `poll.fields` Optional  | enum (`duration_minutes`, `end_datetime`, `id`, `options`, `voting_status`) | This fields parameter enables you to select which specific poll fields will deliver in each returned Tweet. Specify the desired fields in a comma-separated list without spaces between commas and fields. The Tweet will only return poll fields if the Tweet contains a poll and if you've also included the `expansions=attachments.poll_ids` query parameter in your request. While the poll ID will be located in the Tweet object, you will find this ID and all additional poll fields in the `includes` data object. |
| `tweet.fields` Optional  | enum (`attachments`, `author_id`, `context_annotations`, `conversation_id`, `created_at`, `edit_controls`, `entities`, `geo`, `id`, `in_reply_to_user_id`, `lang`, `non_public_metrics`, `public_metrics`, `organic_metrics`, `promoted_metrics`, `possibly_sensitive`, `referenced_tweets`, `reply_settings`, `source`, `text`, `withheld`) | This fields parameter enables you to select which specific Tweet fields will deliver in each returned Tweet object. Specify the desired fields in a comma-separated list without spaces between commas and fields. You can also pass the `expansions=referenced_tweets.id` expansion to return the specified fields for both the original Tweet and any included referenced Tweets. The requested Tweet fields will display in both the original Tweet data object, as well as in the referenced Tweet expanded data object that will be located in the `includes` data object. |
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
    const quoteTweetLookup =
      await twitterClient.tweets.findTweetsThatQuoteATweet(
        //The ID of the Tweet
        "1409931481552543749"
      );
    console.dir(quoteTweetLookup, {
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
    const quoteTweetLookup =
      await twitterClient.tweets.findTweetsThatQuoteATweet(
        //The ID of the Tweet
        "1460323737035677698",
        {
          //A comma separated list of fields to expand.
          expansions: ["author_id"],
          //A comma separated list of Tweet fields to display.
          "tweet.fields": [
            "created_at",
            "author_id",
            "conversation_id",
            "public_metrics",
            "context_annotations",
          ],
          //A comma separated list of User fields to display.
          "user.fields": ["username"],
          //The maximum number of results
          max_results: 15,
        }
      );
    console.dir(quoteTweetLookup, {
      depth: null,
    });
  } catch (error) {
    console.log(error);
  }
})();

```

```
      //The ID of the Tweet  
String id = "1460323737035677698"
try {
    QuoteTweetLookupResponse result = apiInstance.tweets().findTweetsThatQuoteATweet(id, null, null, null, null, null, null, null, null);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling TweetsApi#findTweetsThatQuoteATweet");
    System.err.println("Status code: " + e.getCode());
    System.err.println("Reason: " + e.getResponseBody());
    System.err.println("Response headers: " + e.getResponseHeaders());
    e.printStackTrace();
}

```

```
      // Set the params values
// For full list of params visit - https://github.com/twitterdev/twitter-api-java-sdk/blob/main/docs/TweetsApi.md#findTweetsThatQuoteATweet
//The ID of the Tweet  
String id = "1460323737035677698"
// Set<String> | A comma separated list of fields to expand.
Set<String> expansions = new HashSet<>(Arrays.asList("author_id"));
// Integer | The maximum number of results to be returned.
Integer maxResults = 15;
// Set<String> | A comma separated list of Tweet fields to display.
Set<String> tweetFields = new HashSet<>(Arrays.asList("created_at","author_id","conversation_id","public_metrics","context_annotations")); 
// Set<String> | A comma separated list of User fields to display.
Set<String> userFields = new HashSet<>(Arrays.asList("username"));
try {
    QuoteTweetLookupResponse result = apiInstance.tweets().findTweetsThatQuoteATweet(id, maxResults, null, expansions, tweetFields, userFields, null, null, null);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling TweetsApi#findTweetsThatQuoteATweet");
    System.err.println("Status code: " + e.getCode());
    System.err.println("Reason: " + e.getResponseBody());
    System.err.println("Response headers: " + e.getResponseHeaders());
    e.printStackTrace();
}

```

### Example responses

* Default fields
* Optional fields

 Default fields

 Optional fields

```
      {
  "data": [
    {
      "id": "1495979553889697792",
      "edit_history_tweet_ids": [
        "1495979553889697792"
      ],
      "text": "RT @chris_bail: Twitter has created an entire course (with videos, code, and other materials) to help researchers learn how to collect data…"
    },
    {
      "id": "1486385372401737728",
      "edit_history_tweet_ids": [
        "1486385372401737728"
      ],
      "text": "RT @suhemparack: Super excited to share our course on Getting started with the #TwitterAPI v2 for academic researchnnIf you know students w…"
    },
    {
      "id": "1480954678447857669",
      "edit_history_tweet_ids": [
        "1480954678447857669"
      ],
      "text": "RT @suhemparack: Super excited to share our course on Getting started with the #TwitterAPI v2 for academic researchnnIf you know students w…"
    },
    {
      "id": "1480639272721940486",
      "edit_history_tweet_ids": [
        "1480639272721940486"
      ],
      "text": "RT @suhemparack: Super excited to share our course on Getting started with the #TwitterAPI v2 for academic researchnnIf you know students w…"
    },
    {
      "id": "1471614967207976961",
      "edit_history_tweet_ids": [
        "1471614967207976961"
      ],
      "text": "RT @chris_bail: Twitter has created an entire course (with videos, code, and other materials) to help researchers learn how to collect data…"
    },
    {
      "id": "1470423243513372679",
      "edit_history_tweet_ids": [
        "1470423243513372679"
      ],
      "text": "RT @suhemparack: Super excited to share our course on Getting started with the #TwitterAPI v2 for academic researchnnIf you know students w…"
    },
    {
      "id": "1469125403373568001",
      "edit_history_tweet_ids": [
        "1469125403373568001"
      ],
      "text": "RT @suhemparack: Super excited to share our course on Getting started with the #TwitterAPI v2 for academic researchnnIf you know students w…"
    },
    {
      "id": "1468633446935318529",
      "edit_history_tweet_ids": [
        "1468633446935318529"
      ],
      "text": "RT @suhemparack: Super excited to share our course on Getting started with the #TwitterAPI v2 for academic researchnnIf you know students w…"
    },
    {
      "id": "1438256410417143809",
      "edit_history_tweet_ids": [
        "1438256410417143809"
      ],
      "text": "RT @suhemparack: Super excited to share our course on Getting started with the #TwitterAPI v2 for academic researchnnIf you know students w…"
    },
    {
      "id": "1430934381829492746",
      "edit_history_tweet_ids": [
        "1430934381829492746"
      ],
      "text": "RT @suhemparack: Super excited to share our course on Getting started with the #TwitterAPI v2 for academic researchnnIf you know students w…"
    }
  ],
  "meta": {
    "result_count": 10,
    "next_token": "avdjwk0udyx6"
  }
}
```

```
      {
  "data": [
    {
      "id": "1495979553889697792",
      "edit_history_tweet_ids": [
        "1495979553889697792"
      ],
      "author_id": "29757971",
      "created_at": "2022-02-22T04:31:34.000Z",
      "context_annotations": [
        {
          "domain": {
            "id": "65",
            "name": "Interests and Hobbies Vertical",
            "description": "Top level interests and hobbies groupings, like Food or Travel"
          },
          "entity": {
            "id": "848920371311001600",
            "name": "Technology",
            "description": "Technology and computing"
          }
        },
        {
          "domain": {
            "id": "66",
            "name": "Interests and Hobbies Category",
            "description": "A grouping of interests and hobbies entities, like Novelty Food or Destinations"
          },
          "entity": {
            "id": "848921413196984320",
            "name": "Computer programming",
            "description": "Computer programming"
          }
        },
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
      "text": "RT @chris_bail: Twitter has created an entire course (with videos, code, and other materials) to help researchers learn how to collect data…",
      "conversation_id": "1495979553889697792",
      "public_metrics": {
        "retweet_count": 160,
        "reply_count": 0,
        "like_count": 0,
        "quote_count": 0
      }
    },
    {
      "id": "1486385372401737728",
      "edit_history_tweet_ids": [
        "1486385372401737728"
      ],
      "author_id": "241588187",
      "created_at": "2022-01-26T17:07:43.000Z",
      "context_annotations": [
        {
          "domain": {
            "id": "65",
            "name": "Interests and Hobbies Vertical",
            "description": "Top level interests and hobbies groupings, like Food or Travel"
          },
          "entity": {
            "id": "848920371311001600",
            "name": "Technology",
            "description": "Technology and computing"
          }
        },
        {
          "domain": {
            "id": "66",
            "name": "Interests and Hobbies Category",
            "description": "A grouping of interests and hobbies entities, like Novelty Food or Destinations"
          },
          "entity": {
            "id": "848921413196984320",
            "name": "Computer programming",
            "description": "Computer programming"
          }
        }
      ],
      "text": "RT @suhemparack: Super excited to share our course on Getting started with the #TwitterAPI v2 for academic researchnnIf you know students w…",
      "conversation_id": "1486385372401737728",
      "public_metrics": {
        "retweet_count": 43,
        "reply_count": 0,
        "like_count": 0,
        "quote_count": 0
      }
    },
    {
      "id": "1480954678447857669",
      "edit_history_tweet_ids": [
        "1480954678447857669"
      ],
      "author_id": "24961055",
      "created_at": "2022-01-11T17:28:04.000Z",
      "context_annotations": [
        {
          "domain": {
            "id": "65",
            "name": "Interests and Hobbies Vertical",
            "description": "Top level interests and hobbies groupings, like Food or Travel"
          },
          "entity": {
            "id": "848920371311001600",
            "name": "Technology",
            "description": "Technology and computing"
          }
        },
        {
          "domain": {
            "id": "66",
            "name": "Interests and Hobbies Category",
            "description": "A grouping of interests and hobbies entities, like Novelty Food or Destinations"
          },
          "entity": {
            "id": "848921413196984320",
            "name": "Computer programming",
            "description": "Computer programming"
          }
        }
      ],
      "text": "RT @suhemparack: Super excited to share our course on Getting started with the #TwitterAPI v2 for academic researchnnIf you know students w…",
      "conversation_id": "1480954678447857669",
      "public_metrics": {
        "retweet_count": 43,
        "reply_count": 0,
        "like_count": 0,
        "quote_count": 0
      }
    },
    {
      "id": "1480639272721940486",
      "edit_history_tweet_ids": [
        "1480639272721940486"
      ],
      "author_id": "1441574419789324291",
      "created_at": "2022-01-10T20:34:46.000Z",
      "context_annotations": [
        {
          "domain": {
            "id": "65",
            "name": "Interests and Hobbies Vertical",
            "description": "Top level interests and hobbies groupings, like Food or Travel"
          },
          "entity": {
            "id": "848920371311001600",
            "name": "Technology",
            "description": "Technology and computing"
          }
        },
        {
          "domain": {
            "id": "66",
            "name": "Interests and Hobbies Category",
            "description": "A grouping of interests and hobbies entities, like Novelty Food or Destinations"
          },
          "entity": {
            "id": "848921413196984320",
            "name": "Computer programming",
            "description": "Computer programming"
          }
        }
      ],
      "text": "RT @suhemparack: Super excited to share our course on Getting started with the #TwitterAPI v2 for academic researchnnIf you know students w…",
      "conversation_id": "1480639272721940486",
      "public_metrics": {
        "retweet_count": 43,
        "reply_count": 0,
        "like_count": 0,
        "quote_count": 0
      }
    },
    {
      "id": "1471614967207976961",
      "edit_history_tweet_ids": [
        "1471614967207976961"
      ],
      "author_id": "1623598771",
      "created_at": "2021-12-16T22:55:24.000Z",
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
            "id": "65",
            "name": "Interests and Hobbies Vertical",
            "description": "Top level interests and hobbies groupings, like Food or Travel"
          },
          "entity": {
            "id": "848920371311001600",
            "name": "Technology",
            "description": "Technology and computing"
          }
        },
        {
          "domain": {
            "id": "66",
            "name": "Interests and Hobbies Category",
            "description": "A grouping of interests and hobbies entities, like Novelty Food or Destinations"
          },
          "entity": {
            "id": "848921413196984320",
            "name": "Computer programming",
            "description": "Computer programming"
          }
        }
      ],
      "text": "RT @chris_bail: Twitter has created an entire course (with videos, code, and other materials) to help researchers learn how to collect data…",
      "conversation_id": "1471614967207976961",
      "public_metrics": {
        "retweet_count": 160,
        "reply_count": 0,
        "like_count": 0,
        "quote_count": 0
      }
    },
    {
      "id": "1470423243513372679",
      "edit_history_tweet_ids": [
        "1470423243513372679"
      ],
      "author_id": "1506401233",
      "created_at": "2021-12-13T15:59:55.000Z",
      "context_annotations": [
        {
          "domain": {
            "id": "65",
            "name": "Interests and Hobbies Vertical",
            "description": "Top level interests and hobbies groupings, like Food or Travel"
          },
          "entity": {
            "id": "848920371311001600",
            "name": "Technology",
            "description": "Technology and computing"
          }
        },
        {
          "domain": {
            "id": "66",
            "name": "Interests and Hobbies Category",
            "description": "A grouping of interests and hobbies entities, like Novelty Food or Destinations"
          },
          "entity": {
            "id": "848921413196984320",
            "name": "Computer programming",
            "description": "Computer programming"
          }
        }
      ],
      "text": "RT @suhemparack: Super excited to share our course on Getting started with the #TwitterAPI v2 for academic researchnnIf you know students w…",
      "conversation_id": "1470423243513372679",
      "public_metrics": {
        "retweet_count": 43,
        "reply_count": 0,
        "like_count": 0,
        "quote_count": 0
      }
    },
    {
      "id": "1469125403373568001",
      "edit_history_tweet_ids": [
        "1469125403373568001"
      ],
      "author_id": "40103034",
      "created_at": "2021-12-10T02:02:45.000Z",
      "context_annotations": [
        {
          "domain": {
            "id": "65",
            "name": "Interests and Hobbies Vertical",
            "description": "Top level interests and hobbies groupings, like Food or Travel"
          },
          "entity": {
            "id": "848920371311001600",
            "name": "Technology",
            "description": "Technology and computing"
          }
        },
        {
          "domain": {
            "id": "66",
            "name": "Interests and Hobbies Category",
            "description": "A grouping of interests and hobbies entities, like Novelty Food or Destinations"
          },
          "entity": {
            "id": "848921413196984320",
            "name": "Computer programming",
            "description": "Computer programming"
          }
        }
      ],
      "text": "RT @suhemparack: Super excited to share our course on Getting started with the #TwitterAPI v2 for academic researchnnIf you know students w…",
      "conversation_id": "1469125403373568001",
      "public_metrics": {
        "retweet_count": 43,
        "reply_count": 0,
        "like_count": 0,
        "quote_count": 0
      }
    },
    {
      "id": "1468633446935318529",
      "edit_history_tweet_ids": [
        "1468633446935318529"
      ],
      "author_id": "1436400156006567936",
      "created_at": "2021-12-08T17:27:54.000Z",
      "context_annotations": [
        {
          "domain": {
            "id": "65",
            "name": "Interests and Hobbies Vertical",
            "description": "Top level interests and hobbies groupings, like Food or Travel"
          },
          "entity": {
            "id": "848920371311001600",
            "name": "Technology",
            "description": "Technology and computing"
          }
        },
        {
          "domain": {
            "id": "66",
            "name": "Interests and Hobbies Category",
            "description": "A grouping of interests and hobbies entities, like Novelty Food or Destinations"
          },
          "entity": {
            "id": "848921413196984320",
            "name": "Computer programming",
            "description": "Computer programming"
          }
        }
      ],
      "text": "RT @suhemparack: Super excited to share our course on Getting started with the #TwitterAPI v2 for academic researchnnIf you know students w…",
      "conversation_id": "1468633446935318529",
      "public_metrics": {
        "retweet_count": 43,
        "reply_count": 0,
        "like_count": 0,
        "quote_count": 0
      }
    },
    {
      "id": "1438256410417143809",
      "edit_history_tweet_ids": [
        "1438256410417143809"
      ],
      "author_id": "81650379",
      "created_at": "2021-09-15T21:40:24.000Z",
      "context_annotations": [
        {
          "domain": {
            "id": "65",
            "name": "Interests and Hobbies Vertical",
            "description": "Top level interests and hobbies groupings, like Food or Travel"
          },
          "entity": {
            "id": "848920371311001600",
            "name": "Technology",
            "description": "Technology and computing"
          }
        },
        {
          "domain": {
            "id": "66",
            "name": "Interests and Hobbies Category",
            "description": "A grouping of interests and hobbies entities, like Novelty Food or Destinations"
          },
          "entity": {
            "id": "848921413196984320",
            "name": "Computer programming",
            "description": "Computer programming"
          }
        }
      ],
      "text": "RT @suhemparack: Super excited to share our course on Getting started with the #TwitterAPI v2 for academic researchnnIf you know students w…",
      "conversation_id": "1438256410417143809",
      "public_metrics": {
        "retweet_count": 43,
        "reply_count": 0,
        "like_count": 0,
        "quote_count": 0
      }
    },
    {
      "id": "1430934381829492746",
      "edit_history_tweet_ids": [
        "1430934381829492746"
      ],
      "author_id": "40462535",
      "created_at": "2021-08-26T16:45:16.000Z",
      "context_annotations": [
        {
          "domain": {
            "id": "65",
            "name": "Interests and Hobbies Vertical",
            "description": "Top level interests and hobbies groupings, like Food or Travel"
          },
          "entity": {
            "id": "848920371311001600",
            "name": "Technology",
            "description": "Technology and computing"
          }
        },
        {
          "domain": {
            "id": "66",
            "name": "Interests and Hobbies Category",
            "description": "A grouping of interests and hobbies entities, like Novelty Food or Destinations"
          },
          "entity": {
            "id": "848921413196984320",
            "name": "Computer programming",
            "description": "Computer programming"
          }
        }
      ],
      "text": "RT @suhemparack: Super excited to share our course on Getting started with the #TwitterAPI v2 for academic researchnnIf you know students w…",
      "conversation_id": "1430934381829492746",
      "public_metrics": {
        "retweet_count": 43,
        "reply_count": 0,
        "like_count": 0,
        "quote_count": 0
      }
    },
    {
      "id": "1430373406545960964",
      "edit_history_tweet_ids": [
        "1430373406545960964"
      ],
      "author_id": "3349011202",
      "created_at": "2021-08-25T03:36:09.000Z",
      "context_annotations": [
        {
          "domain": {
            "id": "65",
            "name": "Interests and Hobbies Vertical",
            "description": "Top level interests and hobbies groupings, like Food or Travel"
          },
          "entity": {
            "id": "848920371311001600",
            "name": "Technology",
            "description": "Technology and computing"
          }
        },
        {
          "domain": {
            "id": "66",
            "name": "Interests and Hobbies Category",
            "description": "A grouping of interests and hobbies entities, like Novelty Food or Destinations"
          },
          "entity": {
            "id": "848921413196984320",
            "name": "Computer programming",
            "description": "Computer programming"
          }
        }
      ],
      "text": "RT @suhemparack: Super excited to share our course on Getting started with the #TwitterAPI v2 for academic researchnnIf you know students w…",
      "conversation_id": "1430373406545960964",
      "public_metrics": {
        "retweet_count": 43,
        "reply_count": 0,
        "like_count": 0,
        "quote_count": 0
      }
    },
    {
      "id": "1429820327463378946",
      "edit_history_tweet_ids": [
        "1429820327463378946"
      ],
      "author_id": "1572113804",
      "created_at": "2021-08-23T14:58:25.000Z",
      "context_annotations": [
        {
          "domain": {
            "id": "65",
            "name": "Interests and Hobbies Vertical",
            "description": "Top level interests and hobbies groupings, like Food or Travel"
          },
          "entity": {
            "id": "848920371311001600",
            "name": "Technology",
            "description": "Technology and computing"
          }
        },
        {
          "domain": {
            "id": "66",
            "name": "Interests and Hobbies Category",
            "description": "A grouping of interests and hobbies entities, like Novelty Food or Destinations"
          },
          "entity": {
            "id": "848921413196984320",
            "name": "Computer programming",
            "description": "Computer programming"
          }
        }
      ],
      "text": "RT @dgarcia_eu: Amazing resource for those who want to learn how to use Twitter's academic API. We are very grateful to @suhemparack for th…",
      "conversation_id": "1429820327463378946",
      "public_metrics": {
        "retweet_count": 19,
        "reply_count": 0,
        "like_count": 0,
        "quote_count": 0
      }
    },
    {
      "id": "1427332549479526400",
      "edit_history_tweet_ids": [
        "1427332549479526400"
      ],
      "author_id": "857699969263964161",
      "created_at": "2021-08-16T18:12:53.000Z",
      "context_annotations": [
        {
          "domain": {
            "id": "65",
            "name": "Interests and Hobbies Vertical",
            "description": "Top level interests and hobbies groupings, like Food or Travel"
          },
          "entity": {
            "id": "848920371311001600",
            "name": "Technology",
            "description": "Technology and computing"
          }
        },
        {
          "domain": {
            "id": "66",
            "name": "Interests and Hobbies Category",
            "description": "A grouping of interests and hobbies entities, like Novelty Food or Destinations"
          },
          "entity": {
            "id": "848921413196984320",
            "name": "Computer programming",
            "description": "Computer programming"
          }
        }
      ],
      "text": "@JosephAllen1234 https://t.co/kbDnRNU0mj this course uses Twarc2 and has code samples available",
      "conversation_id": "1427290387194974213",
      "public_metrics": {
        "retweet_count": 0,
        "reply_count": 0,
        "like_count": 0,
        "quote_count": 0
      }
    },
    {
      "id": "1426794955905769476",
      "edit_history_tweet_ids": [
        "1426794955905769476"
      ],
      "author_id": "62185076",
      "created_at": "2021-08-15T06:36:40.000Z",
      "context_annotations": [
        {
          "domain": {
            "id": "65",
            "name": "Interests and Hobbies Vertical",
            "description": "Top level interests and hobbies groupings, like Food or Travel"
          },
          "entity": {
            "id": "848920371311001600",
            "name": "Technology",
            "description": "Technology and computing"
          }
        },
        {
          "domain": {
            "id": "66",
            "name": "Interests and Hobbies Category",
            "description": "A grouping of interests and hobbies entities, like Novelty Food or Destinations"
          },
          "entity": {
            "id": "848921413196984320",
            "name": "Computer programming",
            "description": "Computer programming"
          }
        }
      ],
      "text": "RT @suhemparack: Super excited to share our course on Getting started with the #TwitterAPI v2 for academic researchnnIf you know students w…",
      "conversation_id": "1426794955905769476",
      "public_metrics": {
        "retweet_count": 43,
        "reply_count": 0,
        "like_count": 0,
        "quote_count": 0
      }
    },
    {
      "id": "1422638903412940805",
      "edit_history_tweet_ids": [
        "1422638903412940805"
      ],
      "author_id": "857699969263964161",
      "created_at": "2021-08-03T19:22:00.000Z",
      "context_annotations": [
        {
          "domain": {
            "id": "65",
            "name": "Interests and Hobbies Vertical",
            "description": "Top level interests and hobbies groupings, like Food or Travel"
          },
          "entity": {
            "id": "848920371311001600",
            "name": "Technology",
            "description": "Technology and computing"
          }
        },
        {
          "domain": {
            "id": "66",
            "name": "Interests and Hobbies Category",
            "description": "A grouping of interests and hobbies entities, like Novelty Food or Destinations"
          },
          "entity": {
            "id": "848921413196984320",
            "name": "Computer programming",
            "description": "Computer programming"
          }
        }
      ],
      "text": "@katypearce Understandable. I’d be happy to do an intro webinar etc for any of the classes too. Plus we have monthly office hours that students can sign up for for 1:1 support and a course that helps students learn how to get started with the new academic product track using Python or R https://t.co/6xTDiwfZTI",
      "conversation_id": "1422610092571041793",
      "public_metrics": {
        "retweet_count": 0,
        "reply_count": 2,
        "like_count": 2,
        "quote_count": 0
      }
    }
  ],
  "includes": {
    "users": [
      {
        "id": "29757971",
        "name": "Joshua Tucker",
        "username": "j_a_tucker"
      },
      {
        "id": "241588187",
        "name": "whimchic",
        "username": "whimchic"
      },
      {
        "id": "24961055",
        "name": "Matthias Biehl",
        "username": "mattbiehl"
      },
      {
        "id": "1441574419789324291",
        "name": "J",
        "username": "weixinac"
      },
      {
        "id": "1623598771",
        "name": "Richard Sangeleer",
        "username": "RSangeleer"
      },
      {
        "id": "1506401233",
        "name": "Giz Gulnerman",
        "username": "Gulnerman"
      },
      {
        "id": "40103034",
        "name": "Elishema Fishman",
        "username": "efishman123"
      },
      {
        "id": "1436400156006567936",
        "name": "Hüseyin Ateş",
        "username": "dtcxwz"
      },
      {
        "id": "81650379",
        "name": "Dr. Brenda Berkelaar",
        "username": "brendaberkelaar"
      },
      {
        "id": "40462535",
        "name": "Michael Soto",
        "username": "misoca"
      },
      {
        "id": "3349011202",
        "name": "Özgür Aksoy",
        "username": "OzgurLotus"
      },
      {
        "id": "1572113804",
        "name": "Ama Owusu-Darko",
        "username": "aowusuda"
      },
      {
        "id": "857699969263964161",
        "name": "Suhem Parack",
        "username": "suhemparack"
      },
      {
        "id": "62185076",
        "name": "Annajiat Alim Rasel",
        "username": "annajiat"
      }
    ]
  },
  "meta": {
    "result_count": 15,
    "next_token": "at3vehuk2txh"
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
| `non_public_metrics.impression_count` | integer | Number of times the Tweet has been viewed. This requires the use of OAuth 2.0 User Context authentication. All non\_public\_metrics are only available for Tweets created the last 30 days. |
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
| `includes.tweets` | array | When including the `expansions=referenced_tweets.id` parameter, this includes a list of referenced Retweets, Quoted Tweets, or replies in the form of Tweet objects with their default fields and any additional fields requested using the `tweet.fields` parameter, assuming there is a referenced Tweet present in the returned Tweet(s). Similarly, when including the `expansions=edit_history_tweet_ids` parameter, a Tweet’s edit history will be referenced in the form of Tweet objects. |
| `includes.users` | array | When including the `expansions=author_id` parameter, this includes a list of referenced Tweet authors in the form of user objects with their default fields and any additional fields requested using the `user.fields` parameter. |
| `includes.places` | array | When including the `expansions=geo.place_id` parameter, this includes a list of referenced places in Tweets in the form of place objects with their default fields and any additional fields requested using the `place.fields` parameter, assuming there is a place present in the returned Tweet(s). |
| `includes.media` | array | When including the `expansions=attachments.media_keys` parameter, this includes a list of images, videos, and GIFs included in Tweets in the form of media objects with their default fields and any additional fields requested using the `media.fields` parameter, assuming there is a media attachment present in the returned Tweet(s). |
| `includes.polls` | string | When including the `expansions=attachments.poll_ids` parameter, this includes a list of polls that are attached to Tweets in the form of poll objects with their default fields and any additional fields requested using the `poll.fields` parameter, assuming there is a poll present in the returned Tweet(s). |
| `meta` Default  | object | This object contains information about the number of users returned in the current request and pagination details. |
| `meta.count` Default  | integer | The number of Tweet results returned in the response. |
| `meta.next_token` | string | A value that encodes the next 'page' of results that can be requested, via the `pagination_token` request parameter. |
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