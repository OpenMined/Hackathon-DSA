
GET /2/users/:id/owned\_lists | Docs | Twitter Developer Platform 

GET /2/users/:id/owned\_lists

 GET /2/users/:id/owned\_lists
=============================
Returns all Lists owned by the specified user.
Run in Postman ❯Try a live request ❯Build request with API Explorer ❯### Endpoint URL
`https://api.twitter.com/2/users/:id/owned_lists`  
### Authentication and rate limits

|  |  |
| --- | --- |
| Authentication methodssupported by this endpoint | OAuth 2.0 Authorization Code with PKCEOAuth 2.0 App-onlyOAuth 1.0a is also available for this endpoint. |
| Rate limit | App rate limit (Application-only): 15 requests per 15-minute window shared among all users of your appUser rate limit (User context): 15 requests per 15-minute window per each authenticated user |
### OAuth 2.0 scopes required by this endpoint

|  |
| --- |
| `tweet.read``users.read``list.read` |
| Learn more about OAuth 2.0 Authorization Code with PKCE |
### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `id` Required  | string | The user ID whose owned Lists you would like to retrieve. |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| `expansions` Optional  | enum (`owner_id`) | Expansions enable you to request additional data objects that relate to the originally returned List. The ID that represents the expanded data object will be included directly in the List data object, but the expanded object metadata will be returned within the `includes` response object, and will also include the ID so that you can match this data object to the original user object. At this time, the only expansion available to endpoints that primarily return List objects is `expansions=owner_id`. You will find the expanded user data object living in the `includes` response object. |
| `list.fields` Optional  | enum (`created_at`, `follower_count`, `member_count`, `private`, `description`, `owner_id`) | This fields parameter enables you to select which specific List fields will deliver with each returned List objects. Specify the desired fields in a comma-separated list without spaces between commas and fields. These specified List fields will display directly in the List data objects. |
| `max_results` Optional  | integer | The maximum number of results to be returned per page. This can be a number between 1 and 100. By default, each page will return 100 results. |
| `pagination_token` Optional  | string | Used to request the next page of results if all results weren't returned with the latest request, or to go back to the previous page of results. To return the next page, pass the next\_token returned in your previous response. To go back one page, pass the previous\_token returned in your previous response. |
| `user.fields` Optional  | enum (`created_at`, `description`, `entities`, `id`, `location`, `most_recent_tweet_id`, `name`, `pinned_tweet_id`, `profile_image_url`, `protected`, `public_metrics`, `url`, `username`, `verified`, `withheld`) | This fields parameter enables you to select which specific user fields will deliver with the users object. Specify the desired fields in a comma-separated list without spaces between commas and fields. The user fields will only be returned if you have included `expansions=owner_id` query parameter in your request. You will find this ID and all additional user fields in the `included` data object. |

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
    const getListBtId = await twitterClient.lists.listUserOwnedLists(
      //The ID of the user for whom to return results
      2244994945
    );
    console.dir(getListBtId, {
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
    const getListBtId = await twitterClient.lists.listUserOwnedLists(
      //The ID of the user for whom to return results
      2244994945,
      {
        //A comma separated list of fields to expand
        expansions: ["owner_id"],
        //A comma separated list of List fields to display
        "list.fields": ["follower_count"],
        //A comma separated list of User fields to display
        "user.fields": ["created_at"],
      }
    );
    console.dir(getListBtId, {
      depth: null,
    });
  } catch (error) {
    console.log(error);
  }
})();

```

```
      // Set the params values
// String | The ID of the user for whom to return results
String id = "2244994945";
try {
    MultiListResponse result = apiInstance.lists().listUserOwnedLists(id, null, null, null, null, null);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ListsApi#listUserOwnedLists");
    System.err.println("Status code: " + e.getCode());
    System.err.println("Reason: " + e.getResponseBody());
    System.err.println("Response headers: " + e.getResponseHeaders());
    e.printStackTrace();
}

```

```
      // Set the params values
// For full list of params visit - https://github.com/twitterdev/twitter-api-java-sdk/blob/main/docs/ListsApi.md#listUserOwnedLists
// String | The ID of the user for whom to return results
String id = "2244994945";
// Set<String> | A comma separated list of List fields to display
Set<String> listFields = new HashSet<>(Arrays.asList("follower_count"));
// Set<String> | A comma separated list of fields to expand
Set<String> expansions = new HashSet<>(Arrays.asList("owner_id"));
// Set<String> | A comma separated list of User fields to display
Set<String> userFields = new HashSet<>(Arrays.asList("created_at"));
try {
    MultiListResponse result = apiInstance.lists().listUserOwnedLists(id, null, null, listFields, expansions, userFields);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ListsApi#listUserOwnedLists");
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
      "id": "1451305624956858369",
      "name": "Test List"
    }
  ],
  "meta": {
    "result_count": 1
  }
}
```

```
      {
  "data": [
    {
      "follower_count": 0,
      "id": "1451305624956858369",
      "name": "Test List",
      "owner_id": "2244994945"
    }
  ],
  "includes": {
    "users": [
      {
        "username": "TwitterDev",
        "id": "2244994945",
        "created_at": "2013-12-14T04:35:55.000Z",
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
| `id` Default  | string | Unique identifier of this List. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. |
| `name` Default  | string | The name of this List. |
| `created_at` | date (ISO 8601) | Creation time of this List.To return this field, add `list.fields=created_at` in the request's query parameter. |
| `private` | boolean | Indicates if this List has been set to private. The List (in other words, if this is publicly viewed or not).To return this field, add `list.fields=private` in the request's query parameter. |
| `follower_count` | integer | Number of users who follow this List.To return this field, add `list.fields=follower_count` in the request's query parameter. |
| `member_count` | integer | Number of users who are a member of this List.To return this field, add `list.fields=member_count` in the request's query parameter. |
| `owner_id` | string | Unique identifier of this List's owner. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers.To return this field, add `list.fields=owner_id` in the request's query parameter. |
| `description` | string | A brief description of this List, if the owner provided one.To return this field, add `list.fields=description` in the request's query parameter. |
| `includes.users` | array | When including the `expansions=owner_id` parameter, this includes the referenced List owner in the form of a user object with their default fields and any additional fields requested using the `user.fields` parameter. |
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