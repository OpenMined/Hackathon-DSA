



GET /2/lists/:id/members | Docs | Twitter Developer Platform 





































































































GET /2/lists/:id/members



 GET /2/lists/:id/members
========================

Returns a list of users who are members of the specified List.

Run in Postman ❯Try a live request ❯Build request with API Explorer ❯### Endpoint URL

`https://api.twitter.com/2/lists/:id/members`  
  
### Authentication and rate limits



|  |  |
| --- | --- |
| Authentication methodssupported by this endpoint | OAuth 2.0 App-onlyOAuth 1.0a is also available for this endpoint.OAuth 2.0 Authorization Code with PKCE |
| Rate limit | App rate limit (Application-only): 900 requests per 15-minute window shared among all users of your appUser rate limit (User context): 900 requests per 15-minute window per each authenticated user |

### OAuth 2.0 scopes required by this endpoint



|  |
| --- |
| `tweet.read``users.read``list.read` |
| Learn more about OAuth 2.0 Authorization Code with PKCE |

### Path parameters



| Name | Type | Description |
| --- | --- | --- |
| `id` Required  | string | The ID of the List whose members you would like to retrieve. |

  
  
### Query parameters



| Name | Type | Description |
| --- | --- | --- |
| `expansions` Optional  | enum (`pinned_tweet_id`) | Expansions enable you to request additional data objects that relate to the originally returned users. The ID that represents the expanded data object will be included directly in the user data object, but the expanded object metadata will be returned within the `includes` response object, and will also include the ID so that you can match this data object to the original Tweet object. At this time, the only expansion available to endpoints that primarily return user objects is `expansions=pinned_tweet_id`. You will find the expanded Tweet data object living in the `includes` response object. |
| `max_results` Optional  | integer | The maximum number of results to be returned per page. This can be a number between 1 and 100. By default, each page will return 100 results. |
| `pagination_token` Optional  | string | Used to request the next page of results if all results weren't returned with the latest request, or to go back to the previous page of results. To return the next page, pass the next\_token returned in your previous response. To go back one page, pass the previous\_token returned in your previous response. |
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
    const getMembers = await twitterClient.users.listGetMembers(
      //The ID of the List for which to return members
      84839422
    );
    console.dir(getMembers, {
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
    const getMembers = await twitterClient.users.listGetMembers(
      //The ID of the List for which to return members
      84839422,
      {
        //A comma separated list of fields to expand
        expansions: ["pinned_tweet_id"],

        //The maximum number of results
        max_results: 5,

        //A comma separated list of User fields to display
        "user.fields": ["username"],
      }
    );
    console.dir(getMembers, {
      depth: null,
    });
  } catch (error) {
    console.log(error);
  }
})();

    
```
















```

      // Set the params values

// String | The ID of the List for which to return members
String id = "84839422";

try {
    ListLookupMultipleUsersLookupResponse result = apiInstance.users().listGetMembers(id, null, null, null, null, null);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling UsersApi#listGetMembers");
    System.err.println("Status code: " + e.getCode());
    System.err.println("Reason: " + e.getResponseBody());
    System.err.println("Response headers: " + e.getResponseHeaders());
    e.printStackTrace();
}

    
```
















```

      // Set the params values
// For full list of params visit - https://github.com/twitterdev/twitter-api-java-sdk/blob/main/docs/UsersApi.md#listGetMembers

// String | The ID of the List for which to return members
String id = "84839422";

// Integer | The maximum number of results
Integer maxResults = 5;

// Set<String> | A comma separated list of fields to expand
Set<String> expansions = new HashSet<>(Arrays.asList("pinned_tweet_id"));

// Set<String> | A comma separated list of User fields to display
Set<String> userFields = new HashSet<>(Arrays.asList("username"));

try {
    ListLookupMultipleUsersLookupResponse result = apiInstance.users().listGetMembers(id, maxResults, null, expansions, null, userFields);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling UsersApi#listGetMembers");
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
      "id": "1319036828964454402",
      "name": "Birdwatch",
      "username": "birdwatch"
    },
    {
      "id": "1244731491088809984",
      "name": "Twitter Thailand",
      "username": "TwitterThailand"
    },
    {
      "id": "1194267639100723200",
      "name": "Twitter Retweets",
      "username": "TwitterRetweets"
    },
    {
      "id": "1168976680867762177",
      "name": "Twitter Able",
      "username": "TwitterAble"
    },
    {
      "id": "1065249714214457345",
      "name": "Spaces",
      "username": "TwitterSpaces"
    }
  ],
  "meta": {
    "result_count": 5,
    "next_token": "5676935732641845249"
  }
}
    
```
















```

      {
  "data": [
    {
      "name": "Birdwatch",
      "id": "1319036828964454402",
      "username": "birdwatch",
      "pinned_tweet_id": "1353789891348475905"
    },
    {
      "name": "Twitter Thailand",
      "id": "1244731491088809984",
      "username": "TwitterThailand"
    },
    {
      "name": "Twitter Retweets",
      "id": "1194267639100723200",
      "username": "TwitterRetweets"
    },
    {
      "name": "Twitter Able",
      "id": "1168976680867762177",
      "username": "TwitterAble"
    },
    {
      "name": "Spaces",
      "id": "1065249714214457345",
      "username": "TwitterSpaces",
      "pinned_tweet_id": "1451239134798942208"
    }
  ],
  "includes": {
    "tweets": [
      {
        "id": "1353789891348475905",
        "text": "Want to help build a new community-driven approach to tackling misleading information? Join us — sign up for Birdwatch! nnhttps://t.co/FSsqNznPy1"
      },
      {
        "id": "1451239134798942208",
        "text": "the time has arrived -- we’re now rolling out the ability for everyone on iOS and Android to host a Spacennif this is your first time hosting, welcome! here’s a refresher on how https://t.co/cLH8z0bocy"
      }
    ]
  },
  "meta": {
    "result_count": 5,
    "next_token": "5676935732641845249"
  }
}
    
```












### Response fields



| Name | Type | Description |
| --- | --- | --- |
| `id` Default  | string | Unique identifier of this user. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. |
| `name` Default  | string | The friendly name of this user, as shown on their profile. |
| `username` Default  | string | The Twitter handle (screen name) of this user. |
| `created_at` | date (ISO 8601) | Creation time of this account.To return this field, add `user.fields=created_at` in the request's query parameter. |
| `most_recent_tweet_id` | string | The ID of the User's most recent TweetTo return this field, add `user.fields=most_recent_tweet_id` in the request's query parameter. |
| `protected` | boolean | Indicates if this user has chosen to protect their Tweets (in other words, if this user's Tweets are private).To return this field, add `user.fields=protected` in the request's query parameter. |
| `withheld` | object | Contains withholding details for withheld content.To return this field, add `user.fields=withheld` in the request's query parameter. |
| `withheld.country_codes` | array | Provides a list of countries where this user is not available.To return this field, add `user.fields=withheld.country_codes` in the request's query parameter. |
| `withheld.scope` | enum (`tweet`, `user`) | Indicates whether the content being withheld is a Tweet or a user (this API will return `user`).To return this field, add `user.fields=withheld.scope` in the request's query parameter. |
| `location` | string | The location specified in the user's profile, if the user provided one. As this is a freeform value, it may not indicate a valid location, but it may be fuzzily evaluated when performing searches with location queries.To return this field, add `user.fields=location` in the request's query parameter. |
| `url` | string | The URL specified in the user's profile, if present.To return this field, add `user.fields=url` in the request's query parameter. |
| `description` | string | The text of this user's profile description (also known as bio), if the user provided one.To return this field, add `user.fields=description` in the request's query parameter. |
| `verified` | boolean | Indicate if this user is a verified Twitter user.To return this field, add `user.fields=verified` in the request's query parameter. |
| `entities` | object | This object and its children fields contain details about text that has a special meaning in the user's description.To return this field, add `user.fields=entities` in the request's query parameter. |
| `entities.url` | array | Contains details about the user's profile website. |
| `entities.url.urls` | array | Contains details about the user's profile website. |
| `entities.url.urls.start` | integer | The start position (zero-based) of the recognized user's profile website. All start indices are inclusive. |
| `entities.url.urls.end` | integer | The end position (zero-based) of the recognized user's profile website. This end index is exclusive. |
| `entities.url.urls.url` | string | The URL in the format entered by the user. |
| `entities.url.urls.expanded_url` | string | The fully resolved URL. |
| `entities.url.urls.display_url` | string | The URL as displayed in the user's profile. |
| `entities.description` | array | Contains details about URLs, Hashtags, Cashtags, or mentions located within a user's description. |
| `entities.description.urls` | array | Contains details about any URLs included in the user's description. |
| `entities.description.urls.start` | integer | The start position (zero-based) of the recognized URL in the user's description. All start indices are inclusive. |
| `entities.description.urls.end` | integer | The end position (zero-based) of the recognized URL in the user's description. This end index is exclusive. |
| `entities.description.urls.url` | string | The URL in the format entered by the user. |
| `entities.description.urls.expanded_url` | string | The fully resolved URL. |
| `entities.description.urls.display_url` | string | The URL as displayed in the user's description. |
| `entities.description.hashtags` | array | Contains details about text recognized as a Hashtag. |
| `entities.description.hashtags.start` | integer | The start position (zero-based) of the recognized Hashtag within the Tweet. All start indices are inclusive. |
| `entities.description.hashtags.end` | integer | The end position (zero-based) of the recognized Hashtag within the Tweet. This end index is exclusive. |
| `entities.description.hashtags.hashtag` | string | The text of the Hashtag. |
| `entities.description.mentions` | array | Contains details about text recognized as a user mention. |
| `entities.description.mentions.start` | integer | The start position (zero-based) of the recognized user mention within the Tweet. All start indices are inclusive. |
| `entities.description.mentions.end` | integer | The end position (zero-based) of the recognized user mention within the Tweet. This end index is exclusive. |
| `entities.description.mentions.username` | string | The part of text recognized as a user mention. |
| `entities.description.cashtags` | array | Contains details about text recognized as a Cashtag. |
| `entities.description.cashtags.start` | integer | The start position (zero-based) of the recognized Cashtag within the Tweet. All start indices are inclusive. |
| `entities.description.cashtags.end` | integer | The end position (zero-based) of the recognized Cashtag within the Tweet. This end index is exclusive. |
| `entities.description.cashtags.cashtag` | string | The text of the Cashtag. |
| `profile_image_url` | string | The URL to the profile image for this user, as shown on the user's profile. |
| `public_metrics` | object | Contains details about activity for this user. |
| `public_metrics.followers_count` | integer | Number of users who follow this user. |
| `public_metrics.following_count` | integer | Number of users this user is following. |
| `public_metrics.tweet_count` | integer | Number of Tweets (including Retweets) posted by this user. |
| `public_metrics.listed_count` | integer | Number of lists that include this user. |
| `pinned_tweet_id` | string | Unique identifier of this user's pinned Tweet.You can obtain the expanded object in `includes.tweets` by adding `expansions=pinned_tweet_id` in the request's query parameter. |
| `includes.tweets` | array | When including the `expansions=pinned_tweet_id` parameter, this includes the pinned Tweets attached to the returned users' profiles in the form of Tweet objects with their default fields and any additional fields requested using the `tweet.fields` parameter, assuming there is a referenced Tweet present in the returned Tweet(s). |
| `errors` | object | Contains details about errors that affected any of the requested users. See Status codes and error messages for more details. |
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















