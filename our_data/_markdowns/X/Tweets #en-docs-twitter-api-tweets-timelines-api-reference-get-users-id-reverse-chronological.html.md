
GET /2/users/:id/timelines/reverse\_chronological | Docs | Twitter Developer Platform 

GET /2/users/:id/timelines/reverse\_chronological

 GET /2/users/:id/timelines/reverse\_chronological
=================================================
Allows you to retrieve a collection of the most recent Tweets and Retweets posted by you and users you follow. This endpoint can return every Tweet created on a timeline over the last 7 days as well as the most recent 800 regardless of creation date.
Run in Postman ❯Try a live request ❯Build request with API Explorer ❯### Endpoint URL
`https://api.twitter.com/2/users/:id/timelines/reverse_chronological`  
### Authentication and rate limits

|  |  |
| --- | --- |
| Authentication methodssupported by this endpoint | OAuth 1.0a is also available for this endpoint.OAuth 2.0 Authorization Code with PKCE |
| Rate limit | User rate limit (User context): 180 requests per 15-minute window per each authenticated user |
### OAuth 2.0 scopes required by this endpoint

|  |
| --- |
| `tweet.read``users.read` |
| Learn more about OAuth 2.0 Authorization Code with PKCE |
### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `id` Required  | string | Unique identifier of the user that is requesting their chronological home timeline. User ID can be referenced using the user/lookup endpoint. More information on Twitter IDs is here. |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| `end_time` Optional  | date (ISO 8601) | YYYY-MM-DDTHH:mm:ssZ (ISO 8601/RFC 3339). The new UTC timestamp from which the Tweets will be provided. Timestamp is in second granularity and is inclusive (for example, 12:00:01 includes the first second of the minute). Please note that this parameter does not support a millisecond value. |
| `exclude` Optional  | enum (`retweets`, `replies`) | Comma-separated list of the types of Tweets to exclude from the response. |
| `expansions` Optional  | enum (`attachments.poll_ids`, `attachments.media_keys`, `author_id`, `edit_history_tweet_ids`, `entities.mentions.username`, `geo.place_id`, `in_reply_to_user_id`, `referenced_tweets.id`, `referenced_tweets.id.author_id`) | Expansions enable you to request additional data objects that relate to the originally returned Tweets. Submit a list of desired expansions in a comma-separated list without spaces. The ID that represents the expanded data object will be included directly in the Tweet data object, but the expanded object metadata will be returned within the `includes` response object, and will also include the ID so that you can match this data object to the original Tweet object.The following data objects can be expanded using this parameter:* The Tweet author's user object
* The user object of the Tweet’s author that the original Tweet is responding to
* Any mentioned users’ object
* Any referenced Tweets’ author’s user object
* Attached media’s object
* Attached poll’s object
* Attached place’s object
* Any referenced Tweets’ object (this includes Tweet objects for previous versions of an edited Tweet).
 |
| `max_results` Optional  | integer | Specifies the number of Tweets to try and retrieve, up to a maximum of 100 per distinct request. By default, 100 results are returned if this parameter is not supplied. The minimum permitted value is 1. It is possible to receive less than the `max_results` per request throughout the pagination process. |
| `media.fields` Optional  | enum (`duration_ms`, `height`, `media_key`, `preview_image_url`, `type`, `url`, `width`, `public_metrics`, `non_public_metrics`, `organic_metrics`, `promoted_metrics`, `alt_text`, `variants`) | This fields parameter enables you to select which specific media fields will deliver in each returned Tweet. Specify the desired fields in a comma-separated list without spaces between commas and fields. The Tweet will only return media fields if the Tweet contains media and if you've also included the `expansions=attachments.media_keys` query parameter in your request. While the media ID will be located in the Tweet object, you will find this ID and all additional media fields in the `includes` data object. |
| `pagination_token` Optional  | string | This parameter is used to move forwards or backwards through 'pages' of results, based on the value of the `next_token` or `previous_token` in the response. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified. |
| `place.fields` Optional  | enum (`contained_within`, `country`, `country_code`, `full_name`, `geo`, `id`, `name`, `place_type`) | This fields parameter enables you to select which specific place fields will deliver in each returned Tweet. Specify the desired fields in a comma-separated list without spaces between commas and fields. The Tweet will only return place fields if the Tweet contains a place and if you've also included the `expansions=geo.place_id` query parameter in your request. While the place ID will be located in the Tweet object, you will find this ID and all additional place fields in the `includes` data object. |
| `poll.fields` Optional  | enum (`duration_minutes`, `end_datetime`, `id`, `options`, `voting_status`) | This fields parameter enables you to select which specific poll fields will deliver in each returned Tweet. Specify the desired fields in a comma-separated list without spaces between commas and fields. The Tweet will only return poll fields if the Tweet contains a poll and if you've also included the `expansions=attachments.poll_ids` query parameter in your request. While the poll ID will be located in the Tweet object, you will find this ID and all additional poll fields in the `includes` data object. |
| `since_id` Optional  | string | Returns results with a Tweet ID greater than (that is, more recent than) the specified 'since' Tweet ID. There are limits to the number of Tweets that can be accessed through the API. If the limit of Tweets has occurred since the `since_id`, the `since_id` will be forced to the oldest ID available. More information on Twitter IDs is here. |
| `start_time` Optional  | date (ISO 8601) | YYYY-MM-DDTHH:mm:ssZ (ISO 8601/RFC 3339). The oldest UTC timestamp from which the Tweets will be provided. Timestamp is in second granularity and is inclusive (for example, 12:00:01 includes the first second of the minute). Please note that this parameter does not support a millisecond value. |
| `tweet.fields` Optional  | enum (`attachments`, `author_id`, `context_annotations`, `conversation_id`, `created_at`, `edit_controls`, `entities`, `geo`, `id`, `in_reply_to_user_id`, `lang`, `non_public_metrics`, `public_metrics`, `organic_metrics`, `promoted_metrics`, `possibly_sensitive`, `referenced_tweets`, `reply_settings`, `source`, `text`, `withheld`) | This fields parameter enables you to select which specific Tweet fields will deliver in each returned Tweet object. Specify the desired fields in a comma-separated list without spaces between commas and fields. You can also pass the `expansions=referenced_tweets.id` expansion to return the specified fields for both the original Tweet and any included referenced Tweets. The requested Tweet fields will display in both the original Tweet data object, as well as in the referenced Tweet expanded data object that will be located in the `includes` data object. |
| `until_id` Optional  | string | Returns results with a Tweet ID less than (that is, older than) the specified 'until' Tweet ID. There are limits to the number of Tweets that can be accessed through the API. If the limit of Tweets has occurred since the `until_id`, the `until_id` will be forced to the most recent ID available. More information on Twitter IDs is here. |
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
    const getReverseChronTimeline =
      await twitterClient.tweets.usersIdTimeline(
        //The ID of the User to list Reverse Chronological Timeline Tweets of
        2244994945
      );
    console.dir(getReverseChronTimeline, {
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
    const getReverseChronTimeline =
      await twitterClient.tweets.usersIdTimeline(
        //The ID of the User to list Reverse Chronological Timeline Tweets of
        2244994945,
        {
          //A comma separated list of fields to expand
          expansions: ["author_id"],
          //A comma separated list of Tweet fields to display
          "tweet.fields": ["conversation_id", "lang"],
          //A comma separated list of User fields to display
          "user.fields": ["created_at", "entities"],
          max_results: 5,
        }
      );
    console.dir(getReverseChronTimeline, {
      depth: null,
    });
  } catch (error) {
    console.log(error);
  }
})();

```

```
      // String | The ID of the User to list Reverse Chronological Timeline Tweets of
String id = "2244994945";
try {
    GenericTweetsTimelineResponse result = apiInstance.tweets().usersIdTimeline(id, null, null, null, null, null, null, null, null, null, null, null, null, null);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling TweetsApi#usersIdTimeline");
    System.err.println("Status code: " + e.getCode());
    System.err.println("Reason: " + e.getResponseBody());
    System.err.println("Response headers: " + e.getResponseHeaders());
    e.printStackTrace();
}

```

```
      // Set the params values
// For full list of params visit - https://github.com/twitterdev/twitter-api-java-sdk/blob/main/docs/TweetsApi.md#usersIdTimeline
// String | The ID of the User to list Reverse Chronological Timeline Tweets of
String id = "2244994945";
// Integer | The maximum number of results
Integer maxResults = 5;
// Set<String> | A comma separated list of fields to expand
Set<String> expansions = new HashSet<>(Arrays.asList("author_id"));
// Set<String> | A comma separated list of Tweet fields to display.
Set<String> tweetFields = new HashSet<>(Arrays.asList("conversation_id", "lang"));
// Set<String> | A comma separated list of User fields to display.
Set<String> userFields = new HashSet<>(Arrays.asList("created_at", "entities"));
try {
    GenericTweetsTimelineResponse result = apiInstance.tweets().usersIdTimeline(id, null, null, maxResults, null, null, null, null, expansions, tweetFields, userFields, null, null, null);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling TweetsApi#usersIdTimeline");
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
      "id": "1524796546306478083",
      "edit_history_tweet_ids": [
        "1524796546306478083"
      ],
      "text": "Today marks the launch of Devs in the Details, a technical video series made for developers by developers building with the Twitter API.  🚀nnIn this premiere episode, @jessicagarson walks us through how she built @FactualCat #WelcomeToOurTechTalkn⬇️nnhttps://t.co/nGa8JTQVBJ"
    },
    {
      "id": "1524468552404668416",
      "edit_history_tweet_ids": [
        "1524468552404668416"
      ],
      "text": "📢 Join @jessicagarson @alanbenlee and @i_am_daniele tomorrow, May 12  | 5:30 ET / 2:30pm PT as they discuss the future of bots https://t.co/sQ2bIO1fz6"
    },
    {
      "id": "1523757705436958720",
      "edit_history_tweet_ids": [
        "1523757705436958720"
      ],
      "text": "Do you make bots with the Twitter API? 🤖nnJoin @jessicagarson @alanbenlee and @iamdaniele on Thursday, May 12  | 5:30 ET / 2:30pm PT as they discuss the future of bots and answer any questions you might have. 🎙📆⬇️nnhttps://t.co/2uVt7hCcdG"
    },
    {
      "id": "1522642324781633536",
      "edit_history_tweet_ids": [
        "1522642324781633536"
      ],
      "text": "If you’d like to apply, or would like to nominate someone else for the program, please feel free to fill out the following form:nnhttps://t.co/LUuWj24HLu"
    },
    {
      "id": "1522642323535847424",
      "edit_history_tweet_ids": [
        "1522642323535847424"
      ],
      "text": "We’ve gone into more detail on each Insider in our forum post. nnJoin us in congratulating the new additions! 🥳nnhttps://t.co/0r5maYEjPJ"
    }
  ],
  "meta": {
    "result_count": 5,
    "newest_id": "1524796546306478083",
    "oldest_id": "1522642323535847424",
    "next_token": "7140dibdnow9c7btw421dyz6jism75z99gyxd8egarsc4"
  }
}
```

```
      {
  "data": [
    {
      "created_at": "2022-05-12T17:00:00.000Z",
      "text": "Today marks the launch of Devs in the Details, a technical video series made for developers by developers building with the Twitter API.  🚀nnIn this premiere episode, @jessicagarson walks us through how she built @FactualCat #WelcomeToOurTechTalkn⬇️nnhttps://t.co/nGa8JTQVBJ",
      "author_id": "2244994945",
      "edit_history_tweet_ids": [
        "1524796546306478083"
      ],
      "id": "1524796546306478083"
    },
    {
      "created_at": "2022-05-11T19:16:40.000Z",
      "text": "📢 Join @jessicagarson @alanbenlee and @i_am_daniele tomorrow, May 12  | 5:30 ET / 2:30pm PT as they discuss the future of bots https://t.co/sQ2bIO1fz6",
      "author_id": "2244994945",
      "edit_history_tweet_ids": [
        "1524468552404668416"
      ],
      "id": "1524468552404668416"
    },
    {
      "created_at": "2022-05-09T20:12:01.000Z",
      "text": "Do you make bots with the Twitter API? 🤖nnJoin @jessicagarson @alanbenlee and @iamdaniele on Thursday, May 12  | 5:30 ET / 2:30pm PT as they discuss the future of bots and answer any questions you might have. 🎙📆⬇️nnhttps://t.co/2uVt7hCcdG",
      "author_id": "2244994945",
      "edit_history_tweet_ids": [
        "1523757705436958720"
      ],
      "id": "1523757705436958720"
    },
    {
      "created_at": "2022-05-06T18:19:54.000Z",
      "text": "If you’d like to apply, or would like to nominate someone else for the program, please feel free to fill out the following form:nnhttps://t.co/LUuWj24HLu",
      "author_id": "2244994945",
      "edit_history_tweet_ids": [
        "1522642324781633536"
      ],
      "id": "1522642324781633536"
    },
    {
      "created_at": "2022-05-06T18:19:53.000Z",
      "text": "We’ve gone into more detail on each Insider in our forum post. nnJoin us in congratulating the new additions! 🥳nnhttps://t.co/0r5maYEjPJ",
      "author_id": "2244994945",
      "edit_history_tweet_ids": [
        "1522642323535847424"
      ],
      "id": "1522642323535847424"
    }
  ],
  "includes": {
    "users": [
      {
        "created_at": "2013-12-14T04:35:55.000Z",
        "name": "Twitter Dev",
        "username": "TwitterDev",
        "id": "2244994945"
      }
    ]
  },
  "meta": {
    "result_count": 5,
    "newest_id": "1524796546306478083",
    "oldest_id": "1522642323535847424",
    "next_token": "7140dibdnow9c7btw421dyz6jism75z99gyxd8egarsc4"
  }
}
```

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `id` Default  | string | Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. More information on Twitter IDs is here. |
| `text` Default  | string | The content of the Tweet.To return this field, add `tweet.fields=text` in the request's query parameter. |
| `created_at` | date (ISO 8601) | Creation time of the Tweet. For example: `2020-12-10T20:00:10.000Z`To return this field, add `tweet.fields=created_at` in the request's query parameter. |
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
 |
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
| `geo.coordinates.coordinates` | array | A pair of decimal values representing the precise location of the user (latitude, longitude). This value will be `null` unless the user explicitly shared their precise location. |
| `geo.place_id` | string | The unique identifier of the place, if this is a point of interest tagged in the Tweet.You can obtain the expanded object in `includes.places` by adding `expansions=geo.place_id` in the request's query parameter. |
| `context_annotations` | array | Contains context annotations for the Tweet.To return this field, add `tweet.fields=context_annotations` in the request's query parameter. |
| `context_annotations.domain` | object | Contains elements which identify detailed information regarding the domain classification based on Tweet text. |
| `context_annotations.domain.id` | string | Contains the numeric value of the domain. |
| `context_annotations.domain.name` | string | Domain name based on the Tweet text. |
| `context_annotations.domain.description` | string | Long form description of domain classification. |
| `context_annotations.entity` | object | Contains elements which identify detailed information regarding the domain classification bases on Tweet text. |
| `context_annotations.entity.id` | string | Unique value which correlates to an explicitly mentioned Person, Place, Product or Organization. |
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
| `non_public_metrics` | object | Non-public engagement metrics for the Tweet at the time of the request. This is a private metric and requires the use of OAuth 2.0 User Context authentication. This metric is only available for Tweets created by the authenticating user in the last 30 days.To return this field, add `tweet.fields=non_public_metrics` in the request's query parameter. |
| `non_public_metrics.impression_count` | integer | Number of times the Tweet has been viewed. This requires the use of OAuth 2.0 User Context authentication. This metric is only available for Tweets created by the authenticating user in the last 30 days. |
| `non_public_metrics.url_link_clicks` | integer | Number of times a user clicks on a URL link or URL preview card in a Tweet. This is a private metric, and requires the use of OAuth 2.0 User Context authentication. This metric is only available for Tweets created by the authenticating user in the last 30 days. |
| `non_public_metrics.user_profile_clicks` | integer | Number of times a user clicks the following portions of a Tweet - display name, user name, profile picture. This is a private metric, and requires the use of OAuth 2.0 User Context authentication. This metric is only available for Tweets created by the authenticating user in the last 30 days. |
| `organic_metrics` | object | Organic engagement metrics for the Tweet at the time of the request. Requires user context authentication. This metric is only available for Tweets created by the authenticating user in the last 30 days. |
| `organic_metrics.impression_count` | integer | Number of times the Tweet has been viewed organically. This is a private metric, and requires the use of OAuth 2.0 User Context authentication. This metric is only available for Tweets created by the authenticating user in the last 30 days. |
| `organic_metrics.url_link_clicks` | integer | Number of times a user clicks on a URL link or URL preview card in a Tweet organically. This is a private metric, and requires the use of OAuth 2.0 User Context authentication. This metric is only available for Tweets created by the authenticating user in the last 30 days. |
| `organic_metrics.user_profile_clicks` | integer | Number of times a user clicks the following portions of a Tweet organically - display name, user name, profile picture. This is a private metric, and requires the use of OAuth 2.0 User Context authentication. This metric is only available for Tweets created by the authenticating user in the last 30 days. |
| `organic_metrics.retweet_count` | integer | Number of times the Tweet has been Retweeted organically. This metric is only available for Tweets created by the authenticating user in the last 30 days. |
| `organic_metrics.reply_count` | integer | Number of replies the Tweet has received organically. This metric is only available for Tweets created by the authenticating user in the last 30 days. |
| `organic_metrics.like_count` | integer | Number of likes the Tweet has received organically. This metric is only available for Tweets created by the authenticating user in the last 30 days. |
| `promoted_metrics` | object | Engagement metrics for the Tweet at the time of the request in a promoted context. Requires user context authentication. This metric is only available for Tweets created by the authenticating user in the last 30 days. |
| `promoted_metrics.impression_count` | integer | Number of times the Tweet has been viewed when that Tweet is being promoted. This is a private metric, and requires the use of OAuth 2.0 User Context authentication. This metric is only available for Tweets created by the authenticating user in the last 30 days. |
| `promoted_metrics.url_link_clicks` | integer | Number of times a user clicks on a URL link or URL preview card in a Tweet when it is being promoted. This is a private metric, and requires the use of OAuth 2.0 User Context authentication. This metric is only available for Tweets created by the authenticating user in the last 30 days. |
| `promoted_metrics.user_profile_clicks` | integer | Number of times a user clicks the following portions of a Tweet when it is being promoted - display name, user name, profile picture. This is a private metric, and requires the use of OAuth 2.0 User Context authentication. This metric is only available for Tweets created by the authenticating user in the last 30 days. |
| `promoted_metrics.retweet_count` | integer | Number of times this Tweet has been Retweeted when that Tweet is being promoted. This metric is only available for Tweets created by the authenticating user in the last 30 days. |
| `promoted_metrics.reply_count` | integer | Number of Replies to this Tweet when that Tweet is being promoted. This metric is only available for Tweets created by the authenticating user in the last 30 days. |
| `promoted_metrics.like_count` | integer | Number of Likes of this Tweet when that Tweet is being promoted. |
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