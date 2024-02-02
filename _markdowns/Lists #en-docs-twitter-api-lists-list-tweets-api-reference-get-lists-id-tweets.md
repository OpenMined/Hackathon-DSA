



GET /2/lists/:id/tweets | Docs | Twitter Developer Platform 





































































































GET /2/lists/:id/tweets



 GET /2/lists/:id/tweets
=======================

Returns a list of Tweets from the specified List.

Run in Postman ❯Try a live request ❯Build request with API Explorer ❯### Endpoint URL

`https://api.twitter.com/2/lists/:id/tweets`  
  
### Authentication and rate limits



|  |  |
| --- | --- |
| Authentication methodssupported by this endpoint | OAuth 1.0a is also available for this endpoint.OAuth 2.0 App-onlyOAuth 2.0 Authorization Code with PKCE |
| Rate limit | App rate limit (Application-only): 900 requests per 15-minute window shared among all users of your appUser rate limit (User context): 900 requests per 15-minute window per each authenticated user |

### OAuth 2.0 scopes required by this endpoint



|  |
| --- |
| `tweet.read``users.read``list.read` |
| Learn more about OAuth 2.0 Authorization Code with PKCE |

### Path parameters



| Name | Type | Description |
| --- | --- | --- |
| `id` Required  | string | The ID of the List whose Tweets you would like to retrieve. |

  
  
### Query parameters



| Name | Type | Description |
| --- | --- | --- |
| `expansions` Optional  | enum (`attachments.poll_ids`, `attachments.media_keys`, `author_id`, `edit_history_tweet_ids`, `entities.mentions.username`, `geo.place_id`, `in_reply_to_user_id`, `referenced_tweets.id`, `referenced_tweets.id.author_id`) | Expansions enable you to request additional data objects that relate to the originally returned users. The ID that represents the expanded data object will be included directly in the user data object, but the expanded object metadata will be returned within the `includes` response object, and will also include the ID so that you can match this data object to the original Tweet object. At this time, the only expansion available to endpoints that primarily return user objects is `expansions=pinned_tweet_id`. You will find the expanded Tweet data object living in the `includes` response object. |
| `max_results` Optional  | integer | The maximum number of results to be returned per page. This can be a number between 1 and 100. By default, each page will return 100 results. |
| `media.fields` Optional  | enum (`duration_ms`, `height`, `media_key`, `preview_image_url`, `type`, `url`, `width`, `public_metrics`, `non_public_metrics`, `organic_metrics`, `promoted_metrics`, `alt_text`, `variants`) | This fields parameter enables you to select which specific media fields will deliver in each returned Tweet. Specify the desired fields in a comma-separated list without spaces between commas and fields. The Tweet will only return media fields if the Tweet contains media and if you've also included the `expansions=attachments.media_keys` query parameter in your request. While the media ID will be located in the Tweet object, you will find this ID and all additional media fields in the `includes` data object. |
| `pagination_token` Optional  | string | Used to request the next page of results if all results weren't returned with the latest request, or to go back to the previous page of results. To return the next page, pass the next\_token returned in your previous response. To go back one page, pass the previous\_token returned in your previous response. |
| `place.fields` Optional  | enum (`contained_within`, `country`, `country_code`, `full_name`, `geo`, `id`, `name`, `place_type`) | This fields parameter enables you to select which specific place fields will deliver in each returned Tweet. Specify the desired fields in a comma-separated list without spaces between commas and fields. The Tweet will only return place fields if the Tweet contains a place and if you've also included the `expansions=geo.place_id` query parameter in your request. While the place ID will be located in the Tweet object, you will find this ID and all additional place fields in the `includes` data object. |
| `poll.fields` Optional  | enum (`duration_minutes`, `end_datetime`, `id`, `options`, `voting_status`) | This fields parameter enables you to select which specific poll fields will deliver in each returned Tweet. Specify the desired fields in a comma-separated list without spaces between commas and fields. The Tweet will only return poll fields if the Tweet contains a poll and if you've also included the `expansions=attachments.poll_ids` query parameter in your request. While the poll ID will be located in the Tweet object, you will find this ID and all additional poll fields in the `includes` data object. |
| `tweet.fields` Optional  | enum (`attachments`, `author_id`, `context_annotations`, `conversation_id`, `created_at`, `edit_controls`, `entities`, `geo`, `id`, `in_reply_to_user_id`, `lang`, `non_public_metrics`, `public_metrics`, `organic_metrics`, `promoted_metrics`, `possibly_sensitive`, `referenced_tweets`, `reply_settings`, `source`, `text`, `withheld`) | This fields parameter enables you to select which specific Tweet fields will deliver in each returned pinned Tweet. Specify the desired fields in a comma-separated list without spaces between commas and fields. The Tweet fields will only return if the user has a pinned Tweet and if you've also included the `expansions=pinned_tweet_id` query parameter in your request. While the referenced Tweet ID will be located in the original Tweet object, you will find this ID and all additional Tweet fields in the `includes` data object. |
| `user.fields` Optional  | enum (`created_at`, `description`, `entities`, `id`, `location`, `most_recent_tweet_id`, `name`, `pinned_tweet_id`, `profile_image_url`, `protected`, `public_metrics`, `url`, `username`, `verified`, `withheld`) | This fields parameter enables you to select which specific user fields will deliver with the users object. Specify the desired fields in a comma-separated list without spaces between commas and fields. These specified user fields will display directly in the user data objects. |

  
  
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
    const getListTweets = await twitterClient.tweets.listsIdTweets(
      //The ID of the List to list Tweets of
      84839422
    );
    console.dir(getListTweets, {
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
    const getListTweets = await twitterClient.tweets.listsIdTweets(
      //The ID of the List to list Tweets of
      84839422,
      {
        //A comma separated list of fields to expand
        expansions: ["author_id"],

        //A comma separated list of User fields to display
        "user.fields": ["verified"],
      }
    );
    console.dir(getListTweets, {
      depth: null,
    });
  } catch (error) {
    console.log(error);
  }
})();

    
```
















```

      // Set the params values

// String | The ID of the List to list Tweets of
String id = "84839422";

try {
    ListsIdTweetsResponse result = apiInstance.tweets().listsIdTweets(id, null, null, null, null, null, null, null, null);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling TweetsApi#listsIdTweets");
    System.err.println("Status code: " + e.getCode());
    System.err.println("Reason: " + e.getResponseBody());
    System.err.println("Response headers: " + e.getResponseHeaders());
    e.printStackTrace();
}

    
```
















```

      // Set the params values
// For full list of params visit - https://github.com/twitterdev/twitter-api-java-sdk/blob/main/docs/TweetsApi.md#listsIdTweets

// String | The ID of the List to list Tweets of
String id = "84839422";

// Set<String> | A comma separated list of fields to expand
Set<String> expansions = new HashSet<>(Arrays.asList("author_id"));

// Set<String> | A comma separated list of User fields to display
Set<String> userFields = new HashSet<>(Arrays.asList("verified"));

try {
    ListsIdTweetsResponse result = apiInstance.tweets().listsIdTweets(id, null, null, expansions, null, userFields, null, null, null);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling TweetsApi#listsIdTweets");
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
      "id": "1067094924124872705",
      "text": "Just getting started with Twitter APIs? Find out what you need in order to build an app. Watch this video! https://t.co/Hg8nkfoizN"
    }
  ],
  "meta": {
    "result_count": 1
  }
}
    
```
















```

      {
  "data": {
    "author_id": "2244994945",
    "created_at": "2018-11-26T16:37:10.000Z",
    "text": "Just getting started with Twitter APIs? Find out what you need in order to build an app. Watch this video! https://t.co/Hg8nkfoizN",
    "id": "1067094924124872705"
  },
  "includes": {
    "users": [
      {
        "verified": true,
        "username": "TwitterDev",
        "id": "2244994945",
        "name": "Twitter Dev"
      }
    ]
  },
  "meta": {
    "result_count": 1
  }
}
    
```












### Response fields



| Name | Type | Description |
| --- | --- | --- |
| `id` Default  | string | Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. |
| `text` Default  | string | The content of the Tweet.To return this field, add `tweet.fields=text` in the request's query parameter. |
| `created_at` | date (ISO 8601) | Creation time of the Tweet.To return this field, add `tweet.fields=created_at` in the request's query parameter. |
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
| `note_tweet` | string | Information about Tweets with more than 280 characters.To return this field, add `tweet.fields=note_tweet` in the request's query parameter. |
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
| `entities.hashtags.end` | integer | The end position (zero-based) of the recognized Hashtag within the Tweet. |
| `entities.hashtags.tag` | string | The text of the Hashtag. |
| `entities.mentions` | array | Contains details about text recognized as a user mention. |
| `entities.mentions.start` | integer | The start position (zero-based) of the recognized user mention within the Tweet. All start indices are inclusive. |
| `entities.mentions.end` | integer | The end position (zero-based) of the recognized user mention within the Tweet. |
| `entities.mentions.username` | string | The part of text recognized as a user mention.You can obtain the expanded object in `includes.users` by adding `expansions=entities.mentions.username` in the request's query parameter. |
| `entities.cashtags` | array | Contains details about text recognized as a Cashtag. |
| `entities.cashtags.start` | integer | The start position (zero-based) of the recognized Cashtag within the Tweet. All start indices are inclusive. |
| `entities.cashtags.end` | integer | The end position (zero-based) of the recognized Cashtag within the Tweet. |
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
| `non_public_metrics` | object | Non-public engagement metrics for the Tweet at the time of the request. This is a private metric, and requires the use of OAuth 2.0 User Context authentication.To return this field, add `tweet.fields=non_public_metrics` in the request's query parameter. |
| `non_public_metrics.impression_count` | integer | Number of times the Tweet has been viewed. This is a private metric, and requires the use of OAuth 2.0 User Context authentication. |
| `non_public_metrics.url_link_clicks` | integer | Number of times a user clicks on a URL link or URL preview card in a Tweet. This is a private metric, and requires the use of OAuth 2.0 User Context authentication. |
| `non_public_metrics.user_profile_clicks` | integer | Number of times a user clicks the following portions of a Tweet - display name, user name, profile picture. This is a private metric, and requires the use of OAuth 2.0 User Context authentication. |
| `organic_metrics` | object | Organic engagement metrics for the Tweet at the time of the request. Requires user context authentication.To return this field, add `tweet.fields=organic_metrics` in the request's query parameter. |
| `organic_metrics.impression_count` | integer | Number of times the Tweet has been viewed organically. This is a private metric, and requires the use of OAuth 2.0 User Context authentication. |
| `organic_metrics.url_link_clicks` | integer | Number of times a user clicks on a URL link or URL preview card in a Tweet organically. This is a private metric, and requires the use of OAuth 2.0 User Context authentication. |
| `organic_metrics.user_profile_clicks` | integer | Number of times a user clicks the following portions of a Tweet organically - display name, user name, profile picture. This is a private metric, and requires the use of OAuth 2.0 User Context authentication. |
| `organic_metrics.retweet_count` | integer | Number of times the Tweet has been Retweeted organically. |
| `organic_metrics.reply_count` | integer | Number of replies the Tweet has received organically. |
| `organic_metrics.like_count` | integer | Number of likes the Tweet has received organically. |
| `promoted_metrics` | object | Engagement metrics for the Tweet at the time of the request in a promoted context. Requires user context authentication.To return this field, add `tweet.fields=promoted_metrics` in the request's query parameter. |
| `promoted_metrics.impression_count` | integer | Number of times the Tweet has been viewed when that Tweet is being promoted. This is a private metric, and requires the use of OAuth 2.0 User Context authentication. |
| `promoted_metrics.url_link_clicks` | integer | Number of times a user clicks on a URL link or URL preview card in a Tweet when it is being promoted. This is a private metric, and requires the use of OAuth 2.0 User Context authentication. |
| `promoted_metrics.user_profile_clicks` | integer | Number of times a user clicks the following portions of a Tweet when it is being promoted - display name, user name, profile picture. This is a private metric, and requires the use of OAuth 2.0 User Context authentication. |
| `promoted_metrics.retweet_count` | integer | Number of times this Tweet has been Retweeted when that Tweet is being promoted. |
| `promoted_metrics.reply_count` | integer | Number of Replies to this Tweet when that Tweet is being promoted. |
| `promoted_metrics.like_count` | integer | Number of Likes of this Tweet when that Tweet is being promoted. |
| `possibly_sensitive` | boolean | Indicates if this Tweet contains URLs marked as sensitive, for example content suitable for mature audiences.To return this field, add `tweet.fields=possibly_sensitive` in the request's query parameter. |
| `lang` | string | Language of the Tweet, if detected by Twitter. Returned as a BCP47 language tag.To return this field, add `tweet.fields=lang` in the request's query parameter. |
| `reply_settings` | string | Shows who can reply to this Tweet. Fields returned are `everyone`, `mentionedUsers`, and `following`.To return this field, add `tweet.fields=reply_settings` in the request's query parameter. |
| `source` | string | The name of the app the user Tweeted from.To return this field, add `tweet.fields=source` in the request's query parameter. |
| `includes` | object | If you include an `expansion` parameter, the referenced objects will be returned if available. |
| `includes.tweets` | array | When including the `expansions=referenced_tweets.id` parameter, this includes a list of referenced Retweets, Quoted Tweets, or replies in the form of Tweet objects with their default fields and any additional fields requested using the `tweet.fields` parameter, assuming there is a referenced Tweet present in the returned Tweet(s). |
| `includes.users` | array | When including the `expansions=author_id` parameter, this includes a list of referenced Tweet authors in the form of user objects with their default fields and any additional fields requested using the `user.fields` parameter. |
| `errors` | object | Contains details about errors that affected any of the requested Tweets. See Status codes and error messages for more details. |
| `meta` Default  | object | This object contains information about the number of users returned in the current request, and pagination details. |
| `meta.result_count` Default  | integer | The number of users returned in this request. Note that this number may be lower than what was specified in the `max_results` query parameter. |
| `meta.previous_token` | string | Pagination token for the previous page of results. This value is returned when there are multiple pages of results, as the current request may only return a subset of results. To go back to the previous page, passing the value from this field in the `pagination_token` query parameter. When this field is not returned in the response, it means you are on the first page of results. |
| `meta.next_token` | string | Pagination token for the next page of results. This value is returned when there are multiple pages of results, as the current request may only return a subset of results. To retrieve the full list, keep passing the value from this field in the `pagination_token` query parameter. When this field is not returned in the response, it means you've reached the last page of results, and that there are no further pages. |



















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















