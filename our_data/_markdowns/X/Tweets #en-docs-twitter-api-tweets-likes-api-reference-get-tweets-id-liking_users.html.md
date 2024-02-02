
GET /2/tweets/:id/liking\_users | Docs | Twitter Developer Platform 

GET /2/tweets/:id/liking\_users

 GET /2/tweets/:id/liking\_users
===============================
Allows you to get information about a Tweet’s liking users.
Run in Postman ❯Try a live request ❯Build request with API Explorer ❯### Endpoint URL
`https://api.twitter.com/2/tweets/:id/liking_users`  
### Authentication and rate limits

|  |  |
| --- | --- |
| Authentication methodssupported by this endpoint | OAuth 2.0 App-onlyOAuth 1.0a is also available for this endpoint.OAuth 2.0 Authorization Code with PKCE |
| Rate limit | App rate limit (Application-only): 75 requests per 15-minute window shared among all users of your appUser rate limit (User context): 75 requests per 15-minute window per each authenticated user |
### OAuth 2.0 scopes required by this endpoint

|  |
| --- |
| `tweet.read``users.read``like.read` |
| Learn more about OAuth 2.0 Authorization Code with PKCE |
### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `id` Required  | string | Tweet ID of the Tweet to request liking users of. |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| `expansions` Optional  | enum (`pinned_tweet_id`) | Expansions enable you to request additional data objects that relate to the originally returned users. The ID that represents the expanded data object will be included directly in the user data object, but the expanded object metadata will be returned within the `includes` response object, and will also include the ID so that you can match this data object to the original Tweet object. At this time, the only expansion available to endpoints that primarily return user objects is `expansions=pinned_tweet_id`. You will find the expanded Tweet data object living in the `includes` response object. |
| `max_results` Optional  | integer | The maximum number of results to be returned per page. This can be a number between 1 and 100. By default, each page will return 100 results. |
| `pagination_token` Optional  | string | Used to request the next page of results if all results weren't returned with the latest request, or to go back to the previous page of results. To return the next page, pass the `next_token` returned in your previous response. To go back one page, pass the `previous_token` returned in your previous response. |
| `tweet.fields` Optional  | enum (`attachments`, `author_id`, `context_annotations`, `conversation_id`, `created_at`, `entities`, `geo`, `id`, `in_reply_to_user_id`, `lang`, `non_public_metrics`, `public_metrics`, `organic_metrics`, `promoted_metrics`, `possibly_sensitive`, `referenced_tweets`, `reply_settings`, `source`, `text`, `withheld`) | This fields parameter enables you to select which specific Tweet fields will deliver in each returned pinned Tweet. Specify the desired fields in a comma-separated list without spaces between commas and fields. The Tweet fields will only return if the user has a pinned Tweet and if you've also included the `expansions=pinned_tweet_id` query parameter in your request. While the referenced Tweet ID will be located in the original Tweet object, you will find this ID and all additional Tweet fields in the `includes` data object. |
| `user.fields` Optional  | enum (`created_at`, `description`, `entities`, `id`, `location`, `most_recent_tweet_id`, `name`, `pinned_tweet_id`, `profile_image_url`, `protected`, `public_metrics`, `url`, `username`, `verified`, `verified_type`, `withheld`) | This fields parameter enables you to select which specific user fields will deliver with each returned users objects. Specify the desired fields in a comma-separated list without spaces between commas and fields. These specified user fields will display directly in the user data objects. |

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
    const likingUsers = await twitterClient.users.tweetsIdLikingUsers(
      // Tweet ID of the Tweet to request liking users of
      "1354143047324299264"
    );
    console.dir(likingUsers, {
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
    const likingUsers = await twitterClient.users.tweetsIdLikingUsers(
      // Tweet ID of the Tweet to request liking users of
      "1354143047324299264",
      {
        // The maximum number of results
        max_results: 5,
        // A comma separated list of fields to expand.
        expansions: ["pinned_tweet_id"],
        // A comma separated list of Tweet fields to display.
        "tweet.fields": ["created_at"],
        // A comma separated list of User fields to display.
        "user.fields": ["created_at"],
      }
    );
    console.dir(likingUsers, {
      depth: null,
    });
  } catch (error) {
    console.log(error);
  }
})();

```

```
      // Set the params values
// String | The ID of the Tweet for which to return results
String id = "1354143047324299264";
try {
    GenericMultipleUsersLookupResponse result = apiInstance.users().tweetsIdLikingUsers(id, null, null, null, null, null);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling UsersApi#tweetsIdLikingUsers");
    System.err.println("Status code: " + e.getCode());
    System.err.println("Reason: " + e.getResponseBody());
    System.err.println("Response headers: " + e.getResponseHeaders());
    e.printStackTrace();
}

```

```
      // Set the params values
// For full list of params visit - https://github.com/twitterdev/twitter-api-java-sdk/blob/main/docs/UsersApi.md#tweetsIdLikingUsers
// String | The ID of the Tweet for which to return results
String id = "1354143047324299264";
// Integer | The maximum number of results
Integer maxResults = 5;
// Set<String> | A comma separated list of fields to expand.
Set<String> expansions = new HashSet<>(Arrays.asList("pinned_tweet_id"));
// Set<String> | A comma separated list of Tweet fields to display.
Set<String> tweetFields = new HashSet<>(Arrays.asList("created_at")); 
// Set<String> | A comma separated list of User fields to display.
Set<String> userFields = new HashSet<>(Arrays.asList("created_at"));
try {
    GenericMultipleUsersLookupResponse result = apiInstance.users().tweetsIdLikingUsers(id, maxResults, null, userFields, expansions, tweetFields);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling UsersApi#tweetsIdLikingUsers");
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
      "id": "1065249714214457345",
      "name": "Spaces",
      "username": "TwitterSpaces"
    },
    {
      "id": "783214",
      "name": "Twitter",
      "username": "Twitter"
    },
    {
      "id": "1526228120",
      "name": "Twitter Data",
      "username": "TwitterData"
    },
    {
      "id": "2244994945",
      "name": "Twitter Dev",
      "username": "TwitterDev"
    },
    {
      "id": "6253282",
      "name": "Twitter API",
      "username": "TwitterAPI"
    }
  ]
}
```

```
      {
  "data": [
    {
      "id": "1065249714214457345",
      "created_at": "2018-11-21T14:24:58.000Z",
      "name": "Spaces",
      "pinned_tweet_id": "1389270063807598594",
      "description": "Twitter Spaces is where live audio conversations happen.",
      "username": "TwitterSpaces"
    },
    {
      "id": "783214",
      "created_at": "2007-02-20T14:35:54.000Z",
      "name": "Twitter",
      "description": "What's happening?!",
      "username": "Twitter"
    },
    {
      "id": "1526228120",
      "created_at": "2013-06-17T23:57:45.000Z",
      "name": "Twitter Data",
      "description": "Data-driven insights about notable moments and conversations from Twitter, Inc., plus tips and tricks to help you get the most out of Twitter data.",
      "username": "TwitterData"
    },
    {
      "id": "2244994945",
      "created_at": "2013-12-14T04:35:55.000Z",
      "name": "Twitter Dev",
      "pinned_tweet_id": "1354143047324299264",
      "description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",
      "username": "TwitterDev"
    },
    {
      "id": "6253282",
      "created_at": "2007-05-23T06:01:13.000Z",
      "name": "Twitter API",
      "pinned_tweet_id": "1293595870563381249",
      "description": "Tweets about changes and service issues. Follow @TwitterDev for more.",
      "username": "TwitterAPI"
    }
  ],
  "includes": {
    "tweets": [
      {
        "id": "1389270063807598594",
        "text": "now, everyone with 600 or more followers can host a Space.nnbased on what we've learned, these accounts are likely to have a good experience hosting because of their existing audience. before bringing the ability to create a Space to everyone, we're focused on a few things. :thread:"
      },
      {
        "id": "1354143047324299264",
        "text": "Academics are one of the biggest groups using the #TwitterAPI to research what's happening. Their work helps make the world (&amp; Twitter) a better place, and now more than ever, we must enable more of it. nIntroducing :drum_with_drumsticks: the Academic Research product track!nhttps://t.co/nOFiGewAV2"
      },
      {
        "id": "1293595870563381249",
        "text": "Twitter API v2: Early Access releasednnToday we announced Early Access to the first endpoints of the new Twitter API!nn#TwitterAPI #EarlyAccess #VersionBump https://t.co/g7v3aeIbtQ"
      }
    ]
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