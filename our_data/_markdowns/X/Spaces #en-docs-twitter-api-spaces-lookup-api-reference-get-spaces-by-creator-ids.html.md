
GET /2/spaces/by/creator\_ids | Docs | Twitter Developer Platform 

GET /2/spaces/by/creator\_ids

 GET /2/spaces/by/creator\_ids
=============================
Returns live or scheduled Spaces created by the specified user IDs. Up to 100 comma-separated IDs can be looked up using this endpoint.
Run in Postman ❯Try a live request ❯Build request with API Explorer ❯### Endpoint URL
`https://api.twitter.com/2/spaces/by/creator_ids`  
### Authentication and rate limits

|  |  |
| --- | --- |
| Authentication methodssupported by this endpoint | OAuth 2.0 Authorization Code with PKCEOAuth 2.0 App-onlyThis is not an auth method but a shared rate limit between user and application-only |
| Rate limit | User rate limit (User context): 300 requests per 15-minute window per each authenticated userApp rate limit (Application-only): 300 requests per 15-minute window shared among all users of your appShared rate limit: 1 per second among all users of your app |
### OAuth 2.0 scopes required by this endpoint

|  |
| --- |
| `tweet.read``users.read``space.read` |
| Learn more about OAuth 2.0 Authorization Code with PKCE |
### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| `user_ids` Required  | string | A comma separated list of user IDs (up to 100). |
| `expansions` Optional  | enum (`invited_user_ids`, `speaker_ids`, `creator_id`, `host_ids`, `topics_ids`) | Expansions enable you to request additional data objects that relate to the originally returned Space. Submit a list of desired expansions in a comma-separated list. The ID that represents the expanded data object will be included directly in the Space data object, but the expanded object metadata will be returned within the `includes` response object, and will also include the ID so that you can match this data object to the original Space object.The following data objects can be expanded using this parameter:* The Spaces creator's user object
* The user objects of any Space co-host
* Any mentioned users’ object
* Any speaker's user object
 |
| `space.fields` Optional  | enum (`host_ids`, `created_at`, `creator_id`, `id`, `lang`, `invited_user_ids`, `participant_count`, `speaker_ids`, `started_at`, `ended_at`, `subscriber_count`, `topic_ids`, `state`, `title`, `updated_at`, `scheduled_start`, `is_ticketed`) | This fields parameter enables you to select which specific Space fields will deliver in each returned Space. Specify the desired fields in a comma-separated list. |
| `topic.fields` Optional  | enum (`id`, `name`, `description`) | This fields parameter enables you to select which specific topic metadata in each returned Space topic object, if the creator of the Space set one or more topics. Specify the desired fields in a comma-separated list. |
| `user.fields` Optional  | enum (`created_at`, `description`, `entities`, `id`, `location`, `most_recent_tweet_id`, `name`, `pinned_tweet_id`, `profile_image_url`, `protected`, `public_metrics`, `url`, `username`, `verified`, `verified_type`, `withheld`) | This fields parameter enables you to select which specific user fields will deliver in each returned Space. Specify the desired fields in a comma-separated list without spaces between commas and fields. While the user ID will be located in the original Space object, you will find this ID and all additional user fields in the `includes` data object. |

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
    const getSpacesByCreatorId =
      await twitterClient.spaces.findSpacesByCreatorIds({
        //A list of user ids
        user_ids: ["2244994945", "6253282"],
      });
    console.dir(getSpacesByCreatorId, {
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
    const getSpacesByCreatorId =
      await twitterClient.spaces.findSpacesByCreatorIds({
        //A list of user ids
        user_ids: ["2244994945", "6253282"],
        //A comma separated list of Space fields to display
        "space.fields": ["host_ids"],
      });
    console.dir(getSpacesByCreatorId, {
      depth: null,
    });
  } catch (error) {
    console.log(error);
  }
})();

```

```
      // Set the params values
// List<String> | The users to search through
List<String> userIds = Arrays.asList("2244994945", "6253282");
try {
    MultiSpaceLookupResponse result = apiInstance.spaces().findSpacesByCreatorIds(userIds, null, null, null, null);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling SpacesApi#findSpacesByCreatorIds");
    System.err.println("Status code: " + e.getCode());
    System.err.println("Reason: " + e.getResponseBody());
    System.err.println("Response headers: " + e.getResponseHeaders());
    e.printStackTrace();
}

```

```
      // Set the params values
// For full list of params visit - https://github.com/twitterdev/twitter-api-java-sdk/blob/main/docs/SpacesApi.md#findSpacesByCreatorIds
// List<String> | The users to search through
List<String> userIds = Arrays.asList("2244994945", "6253282");
// Set<String> | A comma separated list of Space fields to display
Set<String> expansions = new HashSet<>(Arrays.asList("host_ids"));
// Set<String> | A comma separated list of Tweet fields to display.
Set<String> spaceFields = new HashSet<>(Arrays.asList("host_ids"));
try {
    MultiSpaceLookupResponse result = apiInstance.spaces().findSpacesByCreatorIds(userIds, spaceFields, expansions, null, null);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling SpacesApi#findSpacesByCreatorIds");
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
      "id": "1DXxyRYNejbKM",
      "state": "live"
    }
  ],
  "meta": {
    "result_count": 2
  }
}
```

```
      {
  "data": [
    {
      "host_ids": [
        "2244994945"
      ],
      "id": "1DXxyRYNejbKM",
      "state": "live"
    },
    {
      "host_ids": [
        "6253282"
      ],
      "id": "1nAJELYEEPvGL",
      "state": "scheduled"
    }
  ],
  "meta": {
    "result_count": 2
  }
}
```

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `id` Default  | string | Unique identifier of this Space. |
| `host_ids` | array | An array containing the user ID of each Space co-host. These IDs are returned as strings in order to avoid complications with languages and tools that cannot handle large integers.To return this field, add `space.fields=host_ids` in the request's query parameter.You can obtain the expanded object in `includes.users` by adding `expansions=host_ids` in the request's query parameter. |
| `created_at` | date (ISO 8601) | Creation date and time of this Space. For scheduled Spaces, this indicates the time the Space was created, not the time when the Space will start.To return this field, add `space.fields=created_at` in the request's query parameter. |
| `creator_id` | string | The user ID of the account that created this Space. This ID is returned as a string in order to avoid complications with languages and tools that cannot handle large integers.To return this field, add `space.fields=creator_id` in the request's query parameter.You can obtain the expanded object in `includes.users` by adding `expansions=creator_id` in the request's query parameter. |
| `ended_at` | date (ISO 8601) | End date and time of this Space. This field will be only present for Spaces in the `ended` state.To return this field, add `space.fields=ended_at` in the request's query parameter. |
| `lang` | string | Main language of the Space’s creator, as inferred by Twitter (this may differ from the language spoken in the Space). Returned as a BCP 47 language tag.Supported values:* Arabic `(ar)`
* Armenian `(hy)`
* Chinese `(zh)`
* Danish `(da)`
* English `(en)`
* Finnish `(fi)`
* French `(fr)`
* German `(de)`
* Hindi `(hi)`
* Hebrew `(iw)`
* Indonesian `(in)`
* Italian `(it)`
* Japanese `(ja)`
* Kazakh `(kk)`
* Korean `(ko)`
* Norwegian `(no)`
* Polish `(pl)`
* Portuguese `(pt)`
* Romanian `(ro)`
* Russian `(ru)`
* Spanish `(es)`
* Swedish `(sv)`
* Turkish `(tr)`
* Ukranian `(uk)`
To return this field, add `space.fields=lang` in the request's query parameter. |
| `is_ticketed` | boolean | Indicates if this is a ticketed Space.To return this field, add `space.fields=is_ticketed` in the request's query parameter. |
| `invited_user_ids` | array | The list of user IDs that can automatically join as Speakers. Usually, users in this list are invited to speak via the Invite user option and have a Speaker role when the Space starts.These IDs are returned as strings in order to avoid complications with languages and tools that cannot handle large integers.To return this field, add `space.fields=invited_user_ids` in the request's query parameter.You can obtain the expanded object in `includes.users` by adding `expansions=invited_user_ids` in the request's query parameter. |
| `participant_count` | integer | The current number of users in the Space, including Hosts and Speakers.To return this field, add `space.fields=participant_count` in the request's query parameter. |
| `scheduled_start` | date (ISO 8601) | Indicates the scheduled start time of a Space. This field is returned only if the Space has been scheduled; in other words, if the field is returned, it means the Space is a scheduled Space.To return this field, add `space.fields=scheduled_start` in the request's query parameter. |
| `speaker_ids` | array | The list of users who were speaking at any point during the Space. This list contains all the users in `invited_user_ids` in addition to any user who requested to speak and was allowed via the Add speaker option.These IDs are returned as strings in order to avoid complications with languages and tools that cannot handle large integers.These IDs are returned as strings in order to avoid complications with languages and tools that cannot handle large integers.To return this field, add `space.fields=speaker_ids` in the request's query parameter.You can obtain the expanded object in `includes.users` by adding `expansions=speaker_ids` in the request's query parameter. |
| `started_at` | date (ISO 8601) | The start date and time of the Space. Only available if the space has started.To return this field, add `space.fields=started_at` in the request's query parameter. |
| `state` Default  | enum (`live`, `scheduled`) | Indicates whether the Space is scheduled and hasn’t started yet (`scheduled`) or if it’s in progress (`live`).To return this field, add `space.fields=state` in the request's query parameter. |
| `subscriber_count` | integer | Indicates the number of people who set a remainder to this Space. This field can only be requested if your app is authentic the request using the Access Token of the creator of the Space.To return this field, add `space.fields=subscriber_count` in the request's query parameter. |
| `topic_ids` | string | A list of the Space topic IDs, if set by the creator of the Space.To return this field, add `space.fields=topic_ids` in the request's query parameter. |
| `topics.id` | string | The ID of the Space topic.To return this field, add `topic.fields=topics.id` in the request's query parameter.You can obtain the expanded object in `includes.topics` by adding `expansions=topics` in the request's query parameter. |
| `topics.id` | string | The ID of the Space topic.To return this field, add `topic.fields=topics.id` in the request's query parameter.You can obtain the expanded object in `includes.topics` by adding `expansions=topics` in the request's query parameter. |
| `topics.name` | string | The name of the Space topic.To return this field, add `topic.fields=topics.name` in the request's query parameter.You can obtain the expanded object in `includes.topics` by adding `expansions=topics` in the request's query parameter. |
| `topics.name` | string | A full text description of the Space topic.To return this field, add `topic.fields=topics.name` in the request's query parameter.You can obtain the expanded object in `includes.topics` by adding `expansions=topics` in the request's query parameter. |
| `title` | string | The title of this Space as specified by the creator.To return this field, add `space.fields=title` in the request's query parameter. |
| `updated_at` | date (ISO 8601) | The timestamp of the last update to any of this Space's metadata, such as the title or scheduled time.To return this field, add `space.fields=updated_at` in the request's query parameter. |
| `includes` | object | If you include an `expansion` parameter, the referenced objects will be returned if available. |
| `includes.users` | array | When including the `expansions=author_id` parameter, this includes a list of referenced Tweet authors in the form of user objects with their default fields and any additional fields requested using the `user.fields` parameter. |
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