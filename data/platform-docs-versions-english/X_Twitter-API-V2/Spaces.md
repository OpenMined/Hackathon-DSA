Spaces overview

Introduction
------------

The following page describes the Spaces endpoints included in the Twitter API. To learn more about Spaces in general, please visit [help.twitter.com](https://help.twitter.com/en/using-twitter/spaces). 

Spaces allow expression and interaction via live audio conversation. The Spaces endpoints provide the tools to create new functionality around Spaces. You can use these endpoints to lookup live or scheduled Spaces, or to build discovery experiences to give your users ways to find Spaces they may be interested in.

We encourage you to use your creativity to extend Spaces beyond the way we built it. With these endpoints you can build experiences to suggest Spaces to listeners based on keywords present in the title, or by surfacing accounts who host live or upcoming Spaces and are followed by a user; you can also help Hosts better understand how their Spaces are performing and get more insights on their audience.  
 

### Important resources

The following resources will help you get started and integrate with the Spaces endpoints:

* [Getting access to Twitter API v2](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api)
* [Spaces data dictionary](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/spaces)
* [Make your first request to a Spaces endpoint](https://developer.twitter.com/en/docs/twitter-api/spaces/lookup/quick-start)  
      
     

What's currently available
--------------------------

|     |     |
| --- | --- |
| **Spaces lookup** | [Lookup by a single Spaces ID](https://developer.twitter.com/en/docs/twitter-api/spaces/lookup/api-reference/get-spaces-id)<br><br>[Lookup using multiple Spaces IDs](https://developer.twitter.com/en/docs/twitter-api/spaces/lookup/api-reference/get-spaces)<br><br>[Lookup by their creator ID](https://developer.twitter.com/en/docs/twitter-api/spaces/lookup/api-reference/get-spaces-by-creator-ids)<br><br>[Lookup list of user who purchased a ticket](https://developer.twitter.com/en/docs/twitter-api/spaces/lookup/api-reference/get-spaces-id-buyers) |
| **Search Spaces** | [Search for spaces using a keyword](https://developer.twitter.com/en/docs/twitter-api/spaces/search/api-reference/get-spaces-search) |

  
Understanding the lifecycle of Spaces
----------------------------------------

Unlike other resources of the Twitter Developer Platform, Spaces have a set lifecycle. Spaces can be scheduled up to 14 days in advance of their intended start date, and become unavailable after they end. A host can also cancel a previously scheduled Space anytime before it starts.

Spaces are accessible while they are live; once ended, they will no longer be available for retrieval using the Spaces endpoints, and an error message will be returned to indicate this condition.

When your app handles Spaces data, you are responsible for returning the most up-to-date information, and that you remove data that is no longer available from the platform. The [Spaces lookup endpoint](https://developer.twitter.com/en/docs/twitter-api/spaces/lookup/introduction) can help you ensure you respect the expectations and intent of your users.  
 

Roles in Spaces
---------------

These endpoints reflect the way Spaces work on the Twitter app. In Spaces, Twitter users can have defined roles depending on how they interact with and interact in a Space.  
 

### Creator (or primary host)

The primary Host is the user who created a Space, and the owner of the Space itself. Currently, Spaces can only have one Host, so the primary Host will be the only Host. In the [Spaces data dictionary](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/spaces), the primary Host information will be in the creator\_id field, which can be expanded into a [user object](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user).  
 

### Hosts

The primary Hosts can make one or more users co-hosts. In the Spaces data dictionary, these Hosts will appear as host\_ids, which can be expanded into a list of user objects. Host designation can change throughout the duration of a Space, and the metadata returned by these endpoints will reflect the status at the time of the request.

Your app will know the primary host by checking the creator\_id value, and who are the co-hosts by checking the host\_ids values.  
 

### Speaker

Speakers are users who have permission to talk in the Space. Zero or more Speakers can be present at any time, and there may be up to 10 Speakers (including the Hosts) in a Space. In the Space data dictionary, speakers will be returned in the speaker\_ids list, which you can expand into a list of user objects.  
 

### Listener

A Listener can listen to a Space, react anytime using the predefined reactions, and ask to become a speaker (when the Hosts allows this in the Space settings). Listener information will only be returned as an aggregate count of participants (including Hosts) in the participant\_count field.

Introduction

Introduction
------------

The Spaces lookup endpoints help you lookup live or scheduled Spaces, and enable you to build discovery experiences to give your users ways to find Spaces they may be interested in.

The lookup by ID endpoints return data you can use to build experiences to display Spaces information to your users, or return details about one or more Spaces. You can lookup one or more Spaces in the same request.

You can also lookup Spaces by their creator ID. This endpoint is useful to lookup Spaces from users in a list, or to determine if multiple recurring hosts are live now or have an upcoming Space scheduled. Up to 100 users can be looked up in a single request.

**Account setup**

To access these endpoints, you will need:

* An approved [developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info).
* To authenticate using the keys and tokens from a [developer App](https://developer.twitter.com/en/docs/apps) that is located within a [Project](https://developer.twitter.com/en/docs/projects). 

Learn more about getting access to the Twitter API v2 endpoints in our [getting started guide](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api).

[Quick start](https://developer.twitter.com/en/docs/twitter-api/spaces/lookup/quick-start)

[Sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code)

[Run in Postman](https://t.co/twitter-api-postman)

[Try with API Explorer](https://developer.twitter.com/apitools/api?endpoint=/2/spaces&method=get)

Supporting resources
--------------------

[Learn how to use Postman to make requests](https://developer.twitter.com/en/docs/tutorials/postman-getting-started "Learn how to use Postman to make requests")

[Troubleshoot an error](https://developer.twitter.com/en/support/twitter-api "Troubleshoot an error")

[Visit the API reference page for this endpoint](https://developer.twitter.com/en/docs/twitter-api/spaces/lookup/api-reference "Visit the API reference page for this endpoint")

Quick start

Getting started with the Spaces lookup endpoints
------------------------------------------------

This quick start guide will help you make your first request to one of the Spaces lookup endpoints with a set of specified fields using Postman.

If you would like to see sample code in different programming languages, please visit our [Twitter API v2 sample code GitHub](https://github.com/twitterdev/Twitter-API-v2-sample-code) repository.  

### Prerequisites

To complete this guide, you will need to have a set of [keys and tokens](https://developer.twitter.com/en/docs/authentication) to authenticate your request. You can generate these keys and tokens by following these steps:

* [Sign up for a developer account](https://developer.twitter.com/en/apply-for-access) and receive approval.
* Create a [Project](https://developer.twitter.com/en/docs/projects) and an associated [developer App](https://developer.twitter.com/en/docs/apps) in the developer portal.
* Navigate to your App's “Keys and tokens” page to generate the required credentials. Make sure to save all credentials in a secure location.

### Steps to build a Spaces lookup request

_For this example, we will make a request to the user Spaces lookup by creator ID endpoint, but you can apply the learnings from this quick start to other lookup requests as well._ 

**Step one: Start with a tool or library**

There are several different tools, code examples, and libraries that you can use to make a request to this endpoint, but we are going to use the Postman tool here to simplify the process.

To load Twitter API v2 Postman collection into your environment, please click on the following button:

[Add Twitter API v2 to Postman](https://t.co/twitter-api-postman)

Once you have the Twitter API v2 collection loaded in Postman, navigate to the Spaces folder and find the "Lookup Spaces created by one or more users" request.  
 

**Step two: Authenticate your request**

To properly make a request to the Twitter API, you need to verify that you have permission. To do so, this endpoint requires you to authenticate your request with either [OAuth 2.0 App-Only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only) or [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code) authentication methods.

For simplicity's sake, we will utilize OAuth 2.0 App-Only with this request, but you will need to use one of the other authentication methods if you'd like to request private [metrics](https://developer.twitter.com/en/docs/twitter-api/metrics) or Spaces from a private user. 

To utilize OAuth 2.0 App-Only, you must add your keys and tokens, specifically the [App Access Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens) (also known as the App-only Bearer Token) to Postman. You can do this by selecting the environment named “Twitter API v2” in the top-right corner of Postman and adding your keys and tokens to the "initial value" and "current value" fields (by clicking the eye icon next to the environment dropdown).

These variables will automatically be pulled into the request's authorization tab if you've done this correctly.  
 

**Step three: Identify and specify which user from which you would like to retrieve Tweets**

You must specify a user you would like to retrieve live or upcoming Spaces for within the request. In this example, we will be passing a single user ID.

User IDs are simply the numerical value that represents an account handle that you can find within an account's profile URL. For example, the following account’s username is TwitterDev.

https://twitter.com/TwitterDev

To convert this username to the user ID, you will have to use the user lookup endpoint with the username and find the numerical user ID in the payload. In the case of @TwitterDev, the user ID is 2244994945.

In Postman, navigate to the "Params" tab and enter this user ID into the "Value" column of the id parameter.

|     |     |
| --- | --- |
| **Key** | **Value** |
| id  | 2244994945 |

#### Step four: Identify and specify which fields you would like to retrieve

If you click the "Send" button after step three, you will receive an id, which is the only [Space object](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/space) field returned by default in your response.

If you would like to receive additional fields, you will have to specify them in your request with the space.fields or expansions parameters.

For this exercise, we will requested three additional sets of fields from different objects:

* The additional title field in the primary Spaces object.
* The full [user object](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) of the specified creator ID
* The additional user.created\_at field in the associated user object.

In Postman, navigate to the “Params” tab and add the following key:value pair to the “Query Params” table:

|     |     |     |
| --- | --- | --- |
| **Key** | **Value** | **Returned fields** |
| space.fields | title | creator\_id |
| expansions | creator\_id | includes.users.id, includes.users.name, includes.users.username |
| user.fields | created\_at | includes.users.created\_at |

You should now see the following URL next to the “Send” button:

https://api.twitter.com/2/spaces/by/creator\_ids?user\_ids=2244994945&space.fields=creator\_id&expansions=creator\_id&user.fields=created\_at

**  
Step five: Make your request and review your response**

Once you have everything set up, hit the “Send” button and you will receive the following response:

      `{    "data": [     {         "creator_id": "2244994945",         "id": "1zqKVXPQhvZJB",         "title": "Hello world 👋",         "state": "Running"    },    "includes": {        "users": [            {                "created_at": "2013-12-14T04:35:55.000Z",                "name": "Twitter Dev",                "id": "2244994945",                "username": "TwitterDev"            }        ]    } ] }`
    

Next steps
----------

[Customize your request using the API Reference](https://developer.twitter.com/en/docs/twitter-api/spaces/lookup/api-reference "Customize your request using the API Reference")

API reference

API reference index
-------------------

For the complete API reference, select an endpoint from the list:

### Spaces lookup

|     |     |
| --- | --- |
| **Lookup Space by ID** | `[GET /2/spaces/:id](https://developer.twitter.com/en/docs/twitter-api/spaces/lookup/api-reference/get-spaces-id)` |
| **Lookup multiple Spaces by ID** | `[GET /2/spaces](https://developer.twitter.com/en/docs/twitter-api/spaces/lookup/api-reference/get-spaces)` |
| **Get users who purchased a ticket to a Space** | `[GET /2/spaces/:id/buyers](https://developer.twitter.com/en/docs/twitter-api/spaces/lookup/api-reference/get-spaces-id-buyers)` |

###   
  
Discover

|     |     |
| --- | --- |
| **Discover Spaces created by user ID** | `[GET /2/spaces/by/creator_ids](https://developer.twitter.com/en/docs/twitter-api/spaces/lookup/api-reference/get-spaces-by-creator-ids)` |
|     |     |

GET /2/spaces/:id

GET /2/spaces/:id
=================

Returns a variety of information about a single Space specified by the requested ID.

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Try a live request ❯](https://oauth-playground.glitch.me/?id=findSpaceById&params=%28%27query%21%28%27space.fields%21%27lang%2Ctitle%2Ccreated_at%27%7Eexpansions%21%27creator_id%27%29%7Ebody%21%28%29%7Epath%21%28%21id%21%271OwxWzlwbrnJQ%27%29%29_) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Fspaces%2F%7Bid%7D&method=get) 

### Endpoint URL

`https://api.twitter.com/2/spaces/:id`  
  

### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code "This method allows an authorized app to act on behalf of the user, as the user. It is typically used to access or post public information for a specific user, and it us useful when your app needs to be aware of the relationship between a user and what this endpoint returns. Click to learn how to authenticate with OAuth 2.0 Authorization Code with PKCE.")<br><br>[OAuth 2.0 App-only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only "Use this method to obtain information in the context of an unauthenticated public user. This method is for developers that just need read-only access to public information. Click to learn how to obtain an OAuth 2.0 App Access Token.") |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | User rate limit (User context): 300 requests per 15-minute window per each authenticated user<br><br>App rate limit (Application-only): 300 requests per 15-minute window shared among all users of your app |

### OAuth 2.0 scopes required by this endpoint

|     |
| --- |
| `tweet.read`<br><br>`users.read`<br><br>`space.read` |
| [Learn more about OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/twitter-api/oauth2) |

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Required | string | Unique identifier of the Space to request. |

  
  

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| `expansions`  <br> Optional | enum (`invited_user_ids`, `speaker_ids`, `creator_id`, `host_ids`, `topics_ids`) | [Expansions](https://developer.twitter.com/en/docs/twitter-api/expansions) enable you to request additional data objects that relate to the originally returned Space. Submit a list of desired expansions in a comma-separated list. The ID that represents the expanded data object will be included directly in the Space data object, but the expanded object metadata will be returned within the `includes` response object, and will also include the ID so that you can match this data object to the original Space object.  <br>  <br>The following data objects can be expanded using this parameter:  <br><br>* The Spaces creator's user object<br>* The user objects of any Space co-host<br>* Any mentioned users’ object<br>* Any speaker's user object |
| `space.fields`  <br> Optional | enum (`host_ids`, `created_at`, `creator_id`, `id`, `lang`, `invited_user_ids`, `participant_count`, `speaker_ids`, `started_at`, `ended_at`, `subscriber_count`, `topic_ids`, `state`, `title`, `updated_at`, `scheduled_start`, `is_ticketed`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [Space fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/space) will deliver in each returned Space. Specify the desired fields in a comma-separated list. |
| `topic.fields`  <br> Optional | enum (`id`, `name`, `description`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific topic metadata in each returned Space topic object, if the creator of the Space set one or more topics. Specify the desired fields in a comma-separated list. |
| `user.fields`  <br> Optional | enum (`created_at`, `description`, `entities`, `id`, `location`, `most_recent_tweet_id`, `name`, `pinned_tweet_id`, `profile_image_url`, `protected`, `public_metrics`, `url`, `username`, `verified`, `verified_type`, `withheld`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [user fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) will deliver in each returned Space. Specify the desired fields in a comma-separated list without spaces between commas and fields. While the user ID will be located in the original Space object, you will find this ID and all additional user fields in the `includes` data object. |

  
  

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript (Default fields)](#tab0)
* [TypeScript (Optional fields)](#tab1)
* [Java (Default fields)](#tab2)
* [Java (Optional fields)](#tab3)

TypeScript (Default fields)

TypeScript (Optional fields)

Java (Default fields)

Java (Optional fields)

      `(async () => {   try {     const searchSpacesById = await twitterClient.spaces.findSpaceById(       //The space id to be retrieved       "1DXxyRYNejbKM"     );     console.dir(searchSpacesById, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `(async () => {   try {     const searchSpacesByIds = await twitterClient.spaces.findSpaceById(       //The space id to be retrieved       "1DXxyRYNejbKM",        //A comma separated list of Space fields to display.       { "space.fields": ["host_ids"] }     );     console.dir(searchSpacesByIds, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  // String | The space id to be retrieved String id = "1DXxyRYNejbKM";  try {     SingleSpaceLookupResponse result = apiInstance.spaces().findSpaceById(id, null, null, null, null);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling SpacesApi#findSpaceById");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

      `// Set the params values // For full list of params visit - https://github.com/twitterdev/twitter-api-java-sdk/blob/main/docs/SpacesApi.md#findSpaceById  // String | The space id to be retrieved String id = "1DXxyRYNejbKM";  // Set<String> | A comma separated list of Space fields to display. Set<String> spaceFields = new HashSet<>(Arrays.asList("host_ids"));  try {     SingleSpaceLookupResponse result = apiInstance.spaces().findSpaceById(id, spaceFields, null, null, null);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling SpacesApi#findSpaceById");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

### Example responses

* [Default fields](#tab0)
* [Optional fields](#tab1)

Default fields

Optional fields

      `{   "data": {     "id": "1DXxyRYNejbKM",     "state": "live"   } }`
    

      `{   "data": {     "host_ids": [       "872212934402899973"     ],     "id": "1DXxyRYNejbKM",     "state": "live"   } }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Default | string | Unique identifier of this Space. |
| `host_ids` | array | An array containing the user ID of each Space co-host. These IDs are returned as strings in order to avoid complications with languages and tools that cannot handle large integers.  <br>  <br>To return this field, add `space.fields=host_ids` in the request's query parameter.  <br>  <br>You can obtain the expanded object in `includes.users` by adding `expansions=host_ids` in the request's query parameter. |
| `created_at` | date (ISO 8601) | Creation date and time of this Space. For scheduled Spaces, this indicates the time the Space was created, not the time when the Space will start.  <br>  <br>To return this field, add `space.fields=created_at` in the request's query parameter. |
| `creator_id` | string | The user ID of the account that created this Space. This ID is returned as a string in order to avoid complications with languages and tools that cannot handle large integers.  <br>  <br>To return this field, add `space.fields=creator_id` in the request's query parameter.  <br>  <br>You can obtain the expanded object in `includes.users` by adding `expansions=creator_id` in the request's query parameter. |
| `ended_at` | date (ISO 8601) | End date and time of this Space. This field will be only present for Spaces in the `ended` state.  <br>  <br>To return this field, add `space.fields=ended_at` in the request's query parameter. |
| `lang` | string | Main language of the Space’s creator, as inferred by Twitter (this may differ from the language spoken in the Space). Returned as a BCP 47 language tag.  <br>  <br>Supported values:  <br><br>* Arabic `(ar)`<br>* Armenian `(hy)`<br>* Chinese `(zh)`<br>* Danish `(da)`<br>* English `(en)`<br>* Finnish `(fi)`<br>* French `(fr)`<br>* German `(de)`<br>* Hindi `(hi)`<br>* Hebrew `(iw)`<br>* Indonesian `(in)`<br>* Italian `(it)`<br>* Japanese `(ja)`<br>* Kazakh `(kk)`<br>* Korean `(ko)`<br>* Norwegian `(no)`<br>* Polish `(pl)`<br>* Portuguese `(pt)`<br>* Romanian `(ro)`<br>* Russian `(ru)`<br>* Spanish `(es)`<br>* Swedish `(sv)`<br>* Turkish `(tr)`<br>* Ukranian `(uk)`<br><br>  <br>  <br>To return this field, add `space.fields=lang` in the request's query parameter. |
| `is_ticketed` | boolean | Indicates if this is a ticketed Space.  <br>  <br>To return this field, add `space.fields=is_ticketed` in the request's query parameter. |
| `invited_user_ids` | array | The list of user IDs that can automatically join as Speakers. Usually, users in this list are invited to speak via the Invite user option and have a Speaker role when the Space starts.  <br>  <br>These IDs are returned as strings in order to avoid complications with languages and tools that cannot handle large integers.  <br>  <br>To return this field, add `space.fields=invited_user_ids` in the request's query parameter.  <br>  <br>You can obtain the expanded object in `includes.users` by adding `expansions=invited_user_ids` in the request's query parameter. |
| `participant_count` | integer | The current number of users in the Space, including Hosts and Speakers.  <br>  <br>To return this field, add `space.fields=participant_count` in the request's query parameter. |
| `scheduled_start` | date (ISO 8601) | Indicates the scheduled start time of a Space. This field is returned only if the Space has been scheduled; in other words, if the field is returned, it means the Space is a scheduled Space.  <br>  <br>To return this field, add `space.fields=scheduled_start` in the request's query parameter. |
| `speaker_ids` | array | The list of users who were speaking at any point during the Space. This list contains all the users in `invited_user_ids` in addition to any user who requested to speak and was allowed via the Add speaker option.  <br>  <br>These IDs are returned as strings in order to avoid complications with languages and tools that cannot handle large integers.These IDs are returned as strings in order to avoid complications with languages and tools that cannot handle large integers.  <br>  <br>To return this field, add `space.fields=speaker_ids` in the request's query parameter.  <br>  <br>You can obtain the expanded object in `includes.users` by adding `expansions=speaker_ids` in the request's query parameter. |
| `started_at` | date (ISO 8601) | The start date and time of the Space. Only available if the space has started.  <br>  <br>To return this field, add `space.fields=started_at` in the request's query parameter. |
| `state`  <br> Default | enum (`live`, `scheduled`) | Indicates whether the Space is scheduled and hasn’t started yet (`scheduled`) or if it’s in progress (`live`).  <br>  <br>To return this field, add `space.fields=state` in the request's query parameter. |
| `subscriber_count` | integer | Indicates the number of people who set a remainder to this Space. This field can only be requested if your app is authentic the request using the Access Token of the creator of the Space.  <br>  <br>To return this field, add `space.fields=subscriber_count` in the request's query parameter. |
| `topic_ids` | string | A list of the Space topic IDs, if set by the creator of the Space.  <br>  <br>To return this field, add `space.fields=topic_ids` in the request's query parameter. |
| `topics.id` | string | The ID of the Space topic.  <br>  <br>To return this field, add `topic.fields=topics.id` in the request's query parameter.  <br>  <br>You can obtain the expanded object in `includes.topics` by adding `expansions=topics` in the request's query parameter. |
| `topics.name` | string | A full text description of the Space topic.  <br>  <br>To return this field, add `topic.fields=topics.name` in the request's query parameter.  <br>  <br>You can obtain the expanded object in `includes.topics` by adding `expansions=topics` in the request's query parameter. |
| `title` | string | The title of this Space as specified by the creator.  <br>  <br>To return this field, add `space.fields=title` in the request's query parameter. |
| `updated_at` | date (ISO 8601) | The timestamp of the last update to any of this Space's metadata, such as the title or scheduled time.  <br>  <br>To return this field, add `space.fields=updated_at` in the request's query parameter. |
| `includes` | object | If you include an `[expansion](https://developer.twitter.com/en/docs/twitter-api/expansions)` parameter, the referenced objects will be returned if available. |
| `includes.users` | array | When including the `expansions=author_id` parameter, this includes a list of referenced Tweet authors in the form of [user objects](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) with their default fields and any additional fields requested using the `user.fields` parameter. |
| `errors` | object | Contains details about errors that affected any of the requested Tweets. See [Status codes and error messages](https://developer.twitter.com/en/support/twitter-api/error-troubleshooting) for more details. |

GET /2/spaces

GET /2/spaces
=============

Returns details about multiple Spaces. Up to 100 comma-separated Spaces IDs can be looked up using this endpoint.

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Try a live request ❯](https://oauth-playground.glitch.me/?id=findSpacesByIds&params=%28%27query%21%28%29~body%21%27%27~path%21%28%29%29_) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Fspaces&method=get) 

### Endpoint URL

`https://api.twitter.com/2/spaces`  
  

### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 2.0 App-only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only "Use this method to obtain information in the context of an unauthenticated public user. This method is for developers that just need read-only access to public information. Click to learn how to obtain an OAuth 2.0 App Access Token.")<br><br>[OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code "This method allows an authorized app to act on behalf of the user, as the user. It is typically used to access or post public information for a specific user, and it us useful when your app needs to be aware of the relationship between a user and what this endpoint returns. Click to learn how to authenticate with OAuth 2.0 Authorization Code with PKCE.") |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | User rate limit (User context): 300 requests per 15-minute window per each authenticated user<br><br>App rate limit (Application-only): 300 requests per 15-minute window shared among all users of your app |

### OAuth 2.0 scopes required by this endpoint

|     |
| --- |
| `tweet.read`<br><br>`users.read`<br><br>`space.read` |
| [Learn more about OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/twitter-api/oauth2) |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| `ids`  <br> Required | string | A comma separated list of Spaces (up to 100). |
| `expansions`  <br> Optional | enum (`invited_user_ids`, `speaker_ids`, `creator_id`, `host_ids`, `topics_ids`) | [Expansions](https://developer.twitter.com/en/docs/twitter-api/expansions) enable you to request additional data objects that relate to the originally returned Space. Submit a list of desired expansions in a comma-separated list. The ID that represents the expanded data object will be included directly in the Space data object, but the expanded object metadata will be returned within the `includes` response object, and will also include the ID so that you can match this data object to the original Space object.  <br>  <br>The following data objects can be expanded using this parameter:  <br><br>* The Spaces creator's user object<br>* The user objects of any Space co-host<br>* Any mentioned users’ object<br>* Any speaker's user object |
| `space.fields`  <br> Optional | enum (`host_ids`, `created_at`, `creator_id`, `id`, `lang`, `invited_user_ids`, `participant_count`, `speaker_ids`, `started_at`, `ended_at`, `subscriber_count`, `topic_ids`, `state`, `title`, `updated_at`, `scheduled_start`, `is_ticketed`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [Space fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/space) will deliver in each returned Space. Specify the desired fields in a comma-separated list. |
| `topic.fields`  <br> Optional | enum (`id`, `name`, `description`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific topic metadata in each returned Space topic object, if the creator of the Space set one or more topics. Specify the desired fields in a comma-separated list. |
| `user.fields`  <br> Optional | enum (`created_at`, `description`, `entities`, `id`, `location`, `most_recent_tweet_id`, `name`, `pinned_tweet_id`, `profile_image_url`, `protected`, `public_metrics`, `url`, `username`, `verified`, `verified_type`, `withheld`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [user fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) will deliver in each returned Space. Specify the desired fields in a comma-separated list without spaces between commas and fields. While the user ID will be located in the original Space object, you will find this ID and all additional user fields in the `includes` data object. |

  
  

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript (Default fields)](#tab0)
* [TypeScript (Optional fields)](#tab1)
* [Java (Default fields)](#tab2)
* [Java (Optional fields)](#tab3)

TypeScript (Default fields)

TypeScript (Optional fields)

Java (Default fields)

Java (Optional fields)

      `(async () => {   try {     const searchSpacesByIds = await twitterClient.spaces.findSpacesByIds({       //A list of space ids       ids: ["1DXxyRYNejbKM", "1nAJELYEEPvGL"],     });     console.dir(searchSpacesByIds, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `(async () => {   try {     const searchSpacesByIds = await twitterClient.spaces.findSpacesByIds({       //A list of space ids       ids: ["1DXxyRYNejbKM", "1nAJELYEEPvGL"],        //A comma separated list of Space fields to display.       "space.fields": ["host_ids"],     });     console.dir(searchSpacesByIds, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  // List<String> | A list of space ids List<String> ids = Arrays.asList("1DXxyRYNejbKM", "1nAJELYEEPvGL");  try {     MultiSpaceLookupResponse result = apiInstance.spaces().findSpacesByIds(ids, null, null, null, null);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling SpacesApi#findSpacesByIds");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

      `// Set the params values // For full list of params visit - https://github.com/twitterdev/twitter-api-java-sdk/blob/main/docs/SpacesApi.md#findSpacesByIds  // String | The search query String query = "hello";  // Set<String> | A comma separated list of Space fields to display. Set<String> spaceFields = new HashSet<>(Arrays.asList("title", "host_ids"));  try {     MultiSpaceLookupResponse result = apiInstance.spaces().findSpacesByIds(ids, spaceFields, null, null, null);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling SpacesApi#findSpacesByIds");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

### Example responses

* [Default fields](#tab0)
* [Optional fields](#tab1)

Default fields

Optional fields

      `{   "data": [     {       "id": "1DXxyRYNejbKM",       "state": "live"     }   ] }`
    

      `{   "data": [     {       "host_ids": [         "2244994945"       ],       "id": "1DXxyRYNejbKM",       "state": "live"     },     {       "host_ids": [         "6253282"       ],       "id": "1nAJELYEEPvGL",       "state": "scheduled"     }   ] }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Default | string | Unique identifier of this Space. |
| `host_ids` | array | An array containing the user ID of each Space co-host. These IDs are returned as strings in order to avoid complications with languages and tools that cannot handle large integers.  <br>  <br>To return this field, add `space.fields=host_ids` in the request's query parameter.  <br>  <br>You can obtain the expanded object in `includes.users` by adding `expansions=host_ids` in the request's query parameter. |
| `created_at` | date (ISO 8601) | Creation date and time of this Space. For scheduled Spaces, this indicates the time the Space was created, not the time when the Space will start.  <br>  <br>To return this field, add `space.fields=created_at` in the request's query parameter. |
| `creator_id` | string | The user ID of the account that created this Space. This ID is returned as a string in order to avoid complications with languages and tools that cannot handle large integers.  <br>  <br>To return this field, add `space.fields=creator_id` in the request's query parameter.  <br>  <br>You can obtain the expanded object in `includes.users` by adding `expansions=creator_id` in the request's query parameter. |
| `ended_at` | date (ISO 8601) | End date and time of this Space. This field will be only present for Spaces in the `ended` state.  <br>  <br>To return this field, add `space.fields=ended_at` in the request's query parameter. |
| `lang` | string | Main language of the Space’s creator, as inferred by Twitter (this may differ from the language spoken in the Space). Returned as a BCP 47 language tag.  <br>  <br>Supported values:  <br><br>* Arabic `(ar)`<br>* Armenian `(hy)`<br>* Chinese `(zh)`<br>* Danish `(da)`<br>* English `(en)`<br>* Finnish `(fi)`<br>* French `(fr)`<br>* German `(de)`<br>* Hindi `(hi)`<br>* Hebrew `(iw)`<br>* Indonesian `(in)`<br>* Italian `(it)`<br>* Japanese `(ja)`<br>* Kazakh `(kk)`<br>* Korean `(ko)`<br>* Norwegian `(no)`<br>* Polish `(pl)`<br>* Portuguese `(pt)`<br>* Romanian `(ro)`<br>* Russian `(ru)`<br>* Spanish `(es)`<br>* Swedish `(sv)`<br>* Turkish `(tr)`<br>* Ukranian `(uk)`<br><br>  <br>  <br>To return this field, add `space.fields=lang` in the request's query parameter. |
| `is_ticketed` | boolean | Indicates if this is a ticketed Space.  <br>  <br>To return this field, add `space.fields=is_ticketed` in the request's query parameter. |
| `invited_user_ids` | array | The list of user IDs that can automatically join as Speakers. Usually, users in this list are invited to speak via the Invite user option and have a Speaker role when the Space starts.  <br>  <br>These IDs are returned as strings in order to avoid complications with languages and tools that cannot handle large integers.  <br>  <br>To return this field, add `space.fields=invited_user_ids` in the request's query parameter.  <br>  <br>You can obtain the expanded object in `includes.users` by adding `expansions=invited_user_ids` in the request's query parameter. |
| `participant_count` | integer | The current number of users in the Space, including Hosts and Speakers.  <br>  <br>To return this field, add `space.fields=participant_count` in the request's query parameter. |
| `scheduled_start` | date (ISO 8601) | Indicates the scheduled start time of a Space. This field is returned only if the Space has been scheduled; in other words, if the field is returned, it means the Space is a scheduled Space.  <br>  <br>To return this field, add `space.fields=scheduled_start` in the request's query parameter. |
| `speaker_ids` | array | The list of users who were speaking at any point during the Space. This list contains all the users in `invited_user_ids` in addition to any user who requested to speak and was allowed via the Add speaker option.  <br>  <br>These IDs are returned as strings in order to avoid complications with languages and tools that cannot handle large integers.These IDs are returned as strings in order to avoid complications with languages and tools that cannot handle large integers.  <br>  <br>To return this field, add `space.fields=speaker_ids` in the request's query parameter.  <br>  <br>You can obtain the expanded object in `includes.users` by adding `expansions=speaker_ids` in the request's query parameter. |
| `started_at` | date (ISO 8601) | The start date and time of the Space. Only available if the space has started.  <br>  <br>To return this field, add `space.fields=started_at` in the request's query parameter. |
| `state`  <br> Default | enum (`live`, `scheduled`) | Indicates whether the Space is scheduled and hasn’t started yet (`scheduled`) or if it’s in progress (`live`).  <br>  <br>To return this field, add `space.fields=state` in the request's query parameter. |
| `subscriber_count` | integer | Indicates the number of people who set a remainder to this Space. This field can only be requested if your app is authentic the request using the Access Token of the creator of the Space.  <br>  <br>To return this field, add `space.fields=subscriber_count` in the request's query parameter. |
| `topic_ids` | string | A list of the Space topic IDs, if set by the creator of the Space.  <br>  <br>To return this field, add `space.fields=topic_ids` in the request's query parameter. |
| `topics.id` | string | The ID of the Space topic.  <br>  <br>To return this field, add `topic.fields=topics.id` in the request's query parameter.  <br>  <br>You can obtain the expanded object in `includes.topics` by adding `expansions=topics` in the request's query parameter. |
| `topics.name` | string | A full text description of the Space topic.  <br>  <br>To return this field, add `topic.fields=topics.name` in the request's query parameter.  <br>  <br>You can obtain the expanded object in `includes.topics` by adding `expansions=topics` in the request's query parameter. |
| `title` | string | The title of this Space as specified by the creator.  <br>  <br>To return this field, add `space.fields=title` in the request's query parameter. |
| `updated_at` | date (ISO 8601) | The timestamp of the last update to any of this Space's metadata, such as the title or scheduled time.  <br>  <br>To return this field, add `space.fields=updated_at` in the request's query parameter. |
| `includes` | object | If you include an `[expansion](https://developer.twitter.com/en/docs/twitter-api/expansions)` parameter, the referenced objects will be returned if available. |
| `includes.users` | array | When including the `expansions=author_id` parameter, this includes a list of referenced Tweet authors in the form of [user objects](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) with their default fields and any additional fields requested using the `user.fields` parameter. |
| `errors` | object | Contains details about errors that affected any of the requested Tweets. See [Status codes and error messages](https://developer.twitter.com/en/support/twitter-api/error-troubleshooting) for more details. |

GET /2/spaces/by/creator\_ids

GET /2/spaces/by/creator\_ids
=============================

Returns live or scheduled Spaces created by the specified user IDs. Up to 100 comma-separated IDs can be looked up using this endpoint.

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Try a live request ❯](https://oauth-playground.glitch.me/?id=findSpacesByCreatorIds&params=%28%27query%21%28%27user_ids%21%271065249714214457345%2C2328002822%2C2548985366%27%7Espace.fields%21%27%27%7Eexpansions%21%27creator_id%27%29%7Ebody%21%28%29%7Epath%21%28%29%29_) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Fspaces%2Fby%2Fcreator_ids&method=get) 

### Endpoint URL

`https://api.twitter.com/2/spaces/by/creator_ids`  
  

### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code "This method allows an authorized app to act on behalf of the user, as the user. It is typically used to access or post public information for a specific user, and it us useful when your app needs to be aware of the relationship between a user and what this endpoint returns. Click to learn how to authenticate with OAuth 2.0 Authorization Code with PKCE.")<br><br>[OAuth 2.0 App-only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only "Use this method to obtain information in the context of an unauthenticated public user. This method is for developers that just need read-only access to public information. Click to learn how to obtain an OAuth 2.0 App Access Token.")<br><br>This is not an auth method but a shared rate limit between user and application-only |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | User rate limit (User context): 300 requests per 15-minute window per each authenticated user<br><br>App rate limit (Application-only): 300 requests per 15-minute window shared among all users of your app<br><br>Shared rate limit: 1 per second among all users of your app |

### OAuth 2.0 scopes required by this endpoint

|     |
| --- |
| `tweet.read`<br><br>`users.read`<br><br>`space.read` |
| [Learn more about OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/twitter-api/oauth2) |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| `user_ids`  <br> Required | string | A comma separated list of user IDs (up to 100). |
| `expansions`  <br> Optional | enum (`invited_user_ids`, `speaker_ids`, `creator_id`, `host_ids`, `topics_ids`) | [Expansions](https://developer.twitter.com/en/docs/twitter-api/expansions) enable you to request additional data objects that relate to the originally returned Space. Submit a list of desired expansions in a comma-separated list. The ID that represents the expanded data object will be included directly in the Space data object, but the expanded object metadata will be returned within the `includes` response object, and will also include the ID so that you can match this data object to the original Space object.  <br>  <br>The following data objects can be expanded using this parameter:  <br><br>* The Spaces creator's user object<br>* The user objects of any Space co-host<br>* Any mentioned users’ object<br>* Any speaker's user object |
| `space.fields`  <br> Optional | enum (`host_ids`, `created_at`, `creator_id`, `id`, `lang`, `invited_user_ids`, `participant_count`, `speaker_ids`, `started_at`, `ended_at`, `subscriber_count`, `topic_ids`, `state`, `title`, `updated_at`, `scheduled_start`, `is_ticketed`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [Space fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/space) will deliver in each returned Space. Specify the desired fields in a comma-separated list. |
| `topic.fields`  <br> Optional | enum (`id`, `name`, `description`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific topic metadata in each returned Space topic object, if the creator of the Space set one or more topics. Specify the desired fields in a comma-separated list. |
| `user.fields`  <br> Optional | enum (`created_at`, `description`, `entities`, `id`, `location`, `most_recent_tweet_id`, `name`, `pinned_tweet_id`, `profile_image_url`, `protected`, `public_metrics`, `url`, `username`, `verified`, `verified_type`, `withheld`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [user fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) will deliver in each returned Space. Specify the desired fields in a comma-separated list without spaces between commas and fields. While the user ID will be located in the original Space object, you will find this ID and all additional user fields in the `includes` data object. |

  
  

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript (Default fields)](#tab0)
* [TypeScript (Optional fields)](#tab1)
* [Java (Default fields)](#tab2)
* [Java (Optional fields)](#tab3)

TypeScript (Default fields)

TypeScript (Optional fields)

Java (Default fields)

Java (Optional fields)

      `(async () => {   try {     const getSpacesByCreatorId =       await twitterClient.spaces.findSpacesByCreatorIds({         //A list of user ids         user_ids: ["2244994945", "6253282"],       });     console.dir(getSpacesByCreatorId, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `(async () => {   try {     const getSpacesByCreatorId =       await twitterClient.spaces.findSpacesByCreatorIds({         //A list of user ids         user_ids: ["2244994945", "6253282"],          //A comma separated list of Space fields to display         "space.fields": ["host_ids"],       });     console.dir(getSpacesByCreatorId, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  // List<String> | The users to search through List<String> userIds = Arrays.asList("2244994945", "6253282");  try {     MultiSpaceLookupResponse result = apiInstance.spaces().findSpacesByCreatorIds(userIds, null, null, null, null);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling SpacesApi#findSpacesByCreatorIds");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

      `// Set the params values // For full list of params visit - https://github.com/twitterdev/twitter-api-java-sdk/blob/main/docs/SpacesApi.md#findSpacesByCreatorIds  // List<String> | The users to search through List<String> userIds = Arrays.asList("2244994945", "6253282");  // Set<String> | A comma separated list of Space fields to display Set<String> expansions = new HashSet<>(Arrays.asList("host_ids"));  // Set<String> | A comma separated list of Tweet fields to display. Set<String> spaceFields = new HashSet<>(Arrays.asList("host_ids"));  try {     MultiSpaceLookupResponse result = apiInstance.spaces().findSpacesByCreatorIds(userIds, spaceFields, expansions, null, null);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling SpacesApi#findSpacesByCreatorIds");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

### Example responses

* [Default fields](#tab0)
* [Optional fields](#tab1)

Default fields

Optional fields

      `{   "data": [     {       "id": "1DXxyRYNejbKM",       "state": "live"     }   ],   "meta": {     "result_count": 2   } }`
    

      `{   "data": [     {       "host_ids": [         "2244994945"       ],       "id": "1DXxyRYNejbKM",       "state": "live"     },     {       "host_ids": [         "6253282"       ],       "id": "1nAJELYEEPvGL",       "state": "scheduled"     }   ],   "meta": {     "result_count": 2   } }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Default | string | Unique identifier of this Space. |
| `host_ids` | array | An array containing the user ID of each Space co-host. These IDs are returned as strings in order to avoid complications with languages and tools that cannot handle large integers.  <br>  <br>To return this field, add `space.fields=host_ids` in the request's query parameter.  <br>  <br>You can obtain the expanded object in `includes.users` by adding `expansions=host_ids` in the request's query parameter. |
| `created_at` | date (ISO 8601) | Creation date and time of this Space. For scheduled Spaces, this indicates the time the Space was created, not the time when the Space will start.  <br>  <br>To return this field, add `space.fields=created_at` in the request's query parameter. |
| `creator_id` | string | The user ID of the account that created this Space. This ID is returned as a string in order to avoid complications with languages and tools that cannot handle large integers.  <br>  <br>To return this field, add `space.fields=creator_id` in the request's query parameter.  <br>  <br>You can obtain the expanded object in `includes.users` by adding `expansions=creator_id` in the request's query parameter. |
| `ended_at` | date (ISO 8601) | End date and time of this Space. This field will be only present for Spaces in the `ended` state.  <br>  <br>To return this field, add `space.fields=ended_at` in the request's query parameter. |
| `lang` | string | Main language of the Space’s creator, as inferred by Twitter (this may differ from the language spoken in the Space). Returned as a BCP 47 language tag.  <br>  <br>Supported values:  <br><br>* Arabic `(ar)`<br>* Armenian `(hy)`<br>* Chinese `(zh)`<br>* Danish `(da)`<br>* English `(en)`<br>* Finnish `(fi)`<br>* French `(fr)`<br>* German `(de)`<br>* Hindi `(hi)`<br>* Hebrew `(iw)`<br>* Indonesian `(in)`<br>* Italian `(it)`<br>* Japanese `(ja)`<br>* Kazakh `(kk)`<br>* Korean `(ko)`<br>* Norwegian `(no)`<br>* Polish `(pl)`<br>* Portuguese `(pt)`<br>* Romanian `(ro)`<br>* Russian `(ru)`<br>* Spanish `(es)`<br>* Swedish `(sv)`<br>* Turkish `(tr)`<br>* Ukranian `(uk)`<br><br>  <br>  <br>To return this field, add `space.fields=lang` in the request's query parameter. |
| `is_ticketed` | boolean | Indicates if this is a ticketed Space.  <br>  <br>To return this field, add `space.fields=is_ticketed` in the request's query parameter. |
| `invited_user_ids` | array | The list of user IDs that can automatically join as Speakers. Usually, users in this list are invited to speak via the Invite user option and have a Speaker role when the Space starts.  <br>  <br>These IDs are returned as strings in order to avoid complications with languages and tools that cannot handle large integers.  <br>  <br>To return this field, add `space.fields=invited_user_ids` in the request's query parameter.  <br>  <br>You can obtain the expanded object in `includes.users` by adding `expansions=invited_user_ids` in the request's query parameter. |
| `participant_count` | integer | The current number of users in the Space, including Hosts and Speakers.  <br>  <br>To return this field, add `space.fields=participant_count` in the request's query parameter. |
| `scheduled_start` | date (ISO 8601) | Indicates the scheduled start time of a Space. This field is returned only if the Space has been scheduled; in other words, if the field is returned, it means the Space is a scheduled Space.  <br>  <br>To return this field, add `space.fields=scheduled_start` in the request's query parameter. |
| `speaker_ids` | array | The list of users who were speaking at any point during the Space. This list contains all the users in `invited_user_ids` in addition to any user who requested to speak and was allowed via the Add speaker option.  <br>  <br>These IDs are returned as strings in order to avoid complications with languages and tools that cannot handle large integers.These IDs are returned as strings in order to avoid complications with languages and tools that cannot handle large integers.  <br>  <br>To return this field, add `space.fields=speaker_ids` in the request's query parameter.  <br>  <br>You can obtain the expanded object in `includes.users` by adding `expansions=speaker_ids` in the request's query parameter. |
| `started_at` | date (ISO 8601) | The start date and time of the Space. Only available if the space has started.  <br>  <br>To return this field, add `space.fields=started_at` in the request's query parameter. |
| `state`  <br> Default | enum (`live`, `scheduled`) | Indicates whether the Space is scheduled and hasn’t started yet (`scheduled`) or if it’s in progress (`live`).  <br>  <br>To return this field, add `space.fields=state` in the request's query parameter. |
| `subscriber_count` | integer | Indicates the number of people who set a remainder to this Space. This field can only be requested if your app is authentic the request using the Access Token of the creator of the Space.  <br>  <br>To return this field, add `space.fields=subscriber_count` in the request's query parameter. |
| `topic_ids` | string | A list of the Space topic IDs, if set by the creator of the Space.  <br>  <br>To return this field, add `space.fields=topic_ids` in the request's query parameter. |
| `topics.id` | string | The ID of the Space topic.  <br>  <br>To return this field, add `topic.fields=topics.id` in the request's query parameter.  <br>  <br>You can obtain the expanded object in `includes.topics` by adding `expansions=topics` in the request's query parameter. |
| `topics.id` | string | The ID of the Space topic.  <br>  <br>To return this field, add `topic.fields=topics.id` in the request's query parameter.  <br>  <br>You can obtain the expanded object in `includes.topics` by adding `expansions=topics` in the request's query parameter. |
| `topics.name` | string | The name of the Space topic.  <br>  <br>To return this field, add `topic.fields=topics.name` in the request's query parameter.  <br>  <br>You can obtain the expanded object in `includes.topics` by adding `expansions=topics` in the request's query parameter. |
| `topics.name` | string | A full text description of the Space topic.  <br>  <br>To return this field, add `topic.fields=topics.name` in the request's query parameter.  <br>  <br>You can obtain the expanded object in `includes.topics` by adding `expansions=topics` in the request's query parameter. |
| `title` | string | The title of this Space as specified by the creator.  <br>  <br>To return this field, add `space.fields=title` in the request's query parameter. |
| `updated_at` | date (ISO 8601) | The timestamp of the last update to any of this Space's metadata, such as the title or scheduled time.  <br>  <br>To return this field, add `space.fields=updated_at` in the request's query parameter. |
| `includes` | object | If you include an `[expansion](https://developer.twitter.com/en/docs/twitter-api/expansions)` parameter, the referenced objects will be returned if available. |
| `includes.users` | array | When including the `expansions=author_id` parameter, this includes a list of referenced Tweet authors in the form of [user objects](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) with their default fields and any additional fields requested using the `user.fields` parameter. |
| `errors` | object | Contains details about errors that affected any of the requested Tweets. See [Status codes and error messages](https://developer.twitter.com/en/support/twitter-api/error-troubleshooting) for more details. |

GET /2/spaces/:id/buyers

GET /2/spaces/:id/buyers
========================

Returns a list of user who purchased a ticket to the requested Space. You must authenticate the request using the Access Token of the creator of the requested Space.

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Try a live request ❯](https://oauth-playground.glitch.me/?id=spaceBuyers&params=%28%27query%21%28%29%7Ebody%21%27%27%7Epath%21%28%27id%21%271nAKEYqvyoAKL%27%29%29_) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Fspaces%2F%7Bid%7D%2Fbuyers&method=get) 

### Endpoint URL

`https://api.twitter.com/2/spaces/:id/buyers`  
  

### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code "This method allows an authorized app to act on behalf of the user, as the user. It is typically used to access or post public information for a specific user, and it us useful when your app needs to be aware of the relationship between a user and what this endpoint returns. Click to learn how to authenticate with OAuth 2.0 Authorization Code with PKCE.") |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | User rate limit (User context): 300 requests per 15-minute window per each authenticated user |

### OAuth 2.0 scopes required by this endpoint

|     |
| --- |
| `tweet.read`<br><br>`users.read`<br><br>`space.read` |
| [Learn more about OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/twitter-api/oauth2) |

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Required | string | Unique identifier of the Space for which you want to request Tweets. |

  
  

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| `expansions`  <br> Optional | enum (`pinned_tweet_id`) | [Expansions](https://developer.twitter.com/en/docs/twitter-api/expansions) enable you to request additional data objects that relate to the originally returned users. The ID that represents the expanded data object will be included directly in the user data object, but the expanded object metadata will be returned within the `includes` response object, and will also include the ID so that you can match this data object to the original Tweet object. At this time, the only expansion available to endpoints that primarily return user objects is `expansions=pinned_tweet_id`. You will find the expanded Tweet data object living in the `includes` response object. |
| `max_results`  <br> Optional | integer | The maximum number of results to be returned per page. This can be a number between 1 and 100. By default, each page will return 100 results. |
| `pagination_token`  <br> Optional | string | Used to request the next page of results if all results weren't returned with the latest request, or to go back to the previous page of results. To return the next page, pass the `next_token` returned in your previous response. To go back one page, pass the `previous_token` returned in your previous response. |
| `tweet.fields`  <br> Optional | enum (`attachments`, `author_id`, `context_annotations`, `conversation_id`, `created_at`, `edit_controls`, `entities`, `geo`, `id`, `in_reply_to_user_id`, `lang`, `non_public_metrics`, `public_metrics`, `organic_metrics`, `promoted_metrics`, `possibly_sensitive`, `referenced_tweets`, `reply_settings`, `source`, `text`, `withheld`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [Tweet fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) will deliver in each returned pinned Tweet. Specify the desired fields in a comma-separated list without spaces between commas and fields. The Tweet fields will only return if the user has a pinned Tweet and if you've also included the `expansions=pinned_tweet_id` query parameter in your request. While the referenced Tweet ID will be located in the original Tweet object, you will find this ID and all additional Tweet fields in the `includes` data object. |
| `user.fields`  <br> Optional | enum (`created_at`, `description`, `entities`, `id`, `location`, `most_recent_tweet_id`, `name`, `pinned_tweet_id`, `profile_image_url`, `protected`, `public_metrics`, `url`, `username`, `verified`, `verified_type`, `withheld`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [user fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) will deliver with each returned users objects. Specify the desired fields in a comma-separated list without spaces between commas and fields. These specified user fields will display directly in the user data objects. |

  
  

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript (Default fields)](#tab0)
* [TypeScript (Optional fields)](#tab1)
* [Java (Default fields)](#tab2)
* [Java (Optional fields)](#tab3)

TypeScript (Default fields)

TypeScript (Optional fields)

Java (Default fields)

Java (Optional fields)

      `(async () => {   try {     const getSpaceBuyers = await twitterClient.spaces.spaceBuyers(       //The space id from which buyers of the space will be retrieved       "1DXxyRYNejbKM"     );     console.dir(getSpaceBuyers, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `(async () => {   try {     const getSpaceBuyers = await twitterClient.spaces.spaceBuyers(       //The space id from which buyers of the space will be retrieved       "1DXxyRYNejbKM",       {         //A comma separated list of fields to expand         expansions: ["pinned_tweet_id"],          //A comma separated list of User fields to display         "user.fields": ["created_at"],          //A comma separated list of Tweet fields to display         "tweet.fields": ["created_at"],       }     );     console.dir(getSpaceBuyers, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  // String | The space id from which tweets will be retrieved String id = "1YqKDqWqdPLsV";  try {     MultiUserLookupResponse result = apiInstance.spaces().spaceBuyers(id, null, null, null, null, null);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling SpacesApi#spaceBuyers");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

      `// Set the params values // For full list of params visit - https://github.com/twitterdev/twitter-api-java-sdk/blob/main/docs/SpacesApi.md#spaceBuyers  // String | The space id from which tweets will be retrieved String id = "1YqKDqWqdPLsV";  // Set<String> | A comma separated list of fields to expand. Set<String> expansions = new HashSet<>(Arrays.asList("pinned_tweet_id"));  // Set<String> | A comma separated list of User fields to display. Set<String> userFields = new HashSet<>(Arrays.asList("created_at"));  // Set<String> | A comma separated list of Tweet fields to display. Set<String> tweetFields = new HashSet<>(Arrays.asList("created_at"));  try {     MultiUserLookupResponse result = apiInstance.spaces().spaceBuyers(id, null, null, userFields, expansions, tweetFields);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling SpacesApi#spaceBuyers");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

### Example responses

* [Default fields](#tab0)
* [Optional fields](#tab1)

Default fields

Optional fields

      `{   "data": [     {       "id": "2244994945",       "username": "TwitterDev",       "name": "Twitter Dev"     },     {       "id": "783214",       "username": "Twitter",       "name": "Twitter"     }   ] }`
    

      `{   "data": [     {       "created_at": "2013-12-14T04:35:55.000Z",       "username": "TwitterDev",       "pinned_tweet_id": "1255542774432063488",       "id": "2244994945",       "name": "Twitter Dev"     },     {       "created_at": "2007-02-20T14:35:54.000Z",       "username": "Twitter",       "pinned_tweet_id": "1274087687469715457",       "id": "783214",       "name": "Twitter"     }   ],   "includes": {     "tweets": [       {         "created_at": "2020-04-29T17:01:38.000Z",         "text": "During these unprecedented times, what’s happening on Twitter can help the world better understand &amp; respond to the pandemic. nnWe're launching a free COVID-19 stream endpoint so qualified devs &amp; researchers can study the public conversation in real-time. https://t.co/BPqMcQzhId",         "id": "1255542774432063488"       },       {         "created_at": "2020-06-19T21:12:30.000Z",         "text": "📍 Minneapolisn🗣️ @FredTJoseph https://t.co/lNTOkyguG1",         "id": "1274087687469715457"       }     ]   } }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Default | string | Unique identifier of this user. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. |
| `name`  <br> Default | string | The friendly name of this user, as shown on their profile. |
| `username`  <br> Default | string | The Twitter handle (screen name) of this user. |
| `created_at` | date (ISO 8601) | Creation time of this account.  <br>  <br>To return this field, add `user.fields=created_at` in the request's query parameter. |
| `most_recent_tweet_id` | string | The ID of the User's most recent Tweet  <br>  <br>To return this field, add `user.fields=most_recent_tweet_id` in the request's query parameter. |
| `protected` | boolean | Indicates if this user has chosen to protect their Tweets (in other words, if this user's Tweets are private).  <br>  <br>To return this field, add `user.fields=protected` in the request's query parameter. |
| `withheld` | object | Contains withholding details for [withheld content](https://help.twitter.com/en/rules-and-policies/tweet-withheld-by-country).  <br>  <br>To return this field, add `user.fields=withheld` in the request's query parameter. |
| `withheld.country_codes` | array | Provides a list of countries where this user is not available.  <br>  <br>To return this field, add `user.fields=withheld.country_codes` in the request's query parameter. |
| `withheld.scope` | enum (`tweet`, `user`) | Indicates whether the content being withheld is a Tweet or a user (this API will return `user`).  <br>  <br>To return this field, add `user.fields=withheld.scope` in the request's query parameter. |
| `location` | string | The location specified in the user's profile, if the user provided one. As this is a freeform value, it may not indicate a valid location, but it may be fuzzily evaluated when performing searches with location queries.  <br>  <br>To return this field, add `user.fields=location` in the request's query parameter. |
| `url` | string | The URL specified in the user's profile, if present.  <br>  <br>To return this field, add `user.fields=url` in the request's query parameter. |
| `description` | string | The text of this user's profile description (also known as bio), if the user provided one.  <br>  <br>To return this field, add `user.fields=description` in the request's query parameter. |
| `verified` | boolean | Indicate if this user is a verified Twitter user.  <br>  <br>To return this field, add `user.fields=verified` in the request's query parameter. |
| `entities` | object | This object and its children fields contain details about text that has a special meaning in the user's description.  <br>  <br>To return this field, add `user.fields=entities` in the request's query parameter. |
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
| `pinned_tweet_id` | string | Unique identifier of this user's pinned Tweet.  <br>  <br>You can obtain the expanded object in `includes.tweets` by adding `expansions=pinned_tweet_id` in the request's query parameter. |
| `includes.tweets` | array | When including the `expansions=pinned_tweet_id` parameter, this includes the pinned Tweets attached to the returned users' profiles in the form of [Tweet objects](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) with their default fields and any additional fields requested using the `tweet.fields` parameter, assuming there is a referenced Tweet present in the returned Tweet(s). |
| `errors` | object | Contains details about errors that affected any of the requested users. See [Status codes and error messages](https://developer.twitter.com/en/support/twitter-api/error-troubleshooting) for more details. |

GET /2/spaces/:id/tweets

GET /2/spaces/:id/tweets
========================

Returns Tweets shared in the requested Spaces.

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Try a live request ❯](https://oauth-playground.glitch.me/?id=spaceTweets&params=%28%27query%21%28%29%7Ebody%21%27%27%7Epath%21%28%27id%21%271nAKEYqvyoAKL%27%29%29_) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Fspaces%2F%7Bid%7D%2Ftweets&method=get) 

### Endpoint URL

`https://api.twitter.com/2/spaces/:id/tweets`  
  

### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code "This method allows an authorized app to act on behalf of the user, as the user. It is typically used to access or post public information for a specific user, and it us useful when your app needs to be aware of the relationship between a user and what this endpoint returns. Click to learn how to authenticate with OAuth 2.0 Authorization Code with PKCE.") |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | User rate limit (User context): 300 requests per 15-minute window per each authenticated user |

### OAuth 2.0 scopes required by this endpoint

|     |
| --- |
| `tweet.read`<br><br>`users.read`<br><br>`space.read` |
| [Learn more about OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/twitter-api/oauth2) |

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Required | string | Unique identifier of the Space containing the Tweets you'd like to access. |

  
  

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| `expansions`  <br> Optional | enum (`attachments.poll_ids`, `attachments.media_keys`, `author_id`, `edit_history_tweet_ids`, `entities.mentions.username`, `geo.place_id`, `in_reply_to_user_id`, `referenced_tweets.id`, `referenced_tweets.id.author_id`) | [Expansions](https://developer.twitter.com/en/docs/twitter-api/expansions) enable you to request additional data objects that relate to the originally returned Tweets. Submit a list of desired expansions in a comma-separated list without spaces. The ID that represents the expanded data object will be included directly in the Tweet data object, but the expanded object metadata will be returned within the `includes` response object, and will also include the ID so that you can match this data object to the original Tweet object.  <br>  <br>The following data objects can be expanded using this parameter:  <br><br>* The Tweet author's user object<br>* The user object of the Tweet’s author that the original Tweet is responding to<br>* Any mentioned users’ object<br>* Any referenced Tweets’ author’s user object<br>* Attached media’s object<br>* Attached poll’s object<br>* Attached place’s object<br>* Any referenced Tweets’ object |
| `media.fields`  <br> Optional | enum (`duration_ms`, `height`, `media_key`, `preview_image_url`, `type`, `url`, `width`, `public_metrics`, `non_public_metrics`, `organic_metrics`, `promoted_metrics`, `alt_text`, `variants`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [media fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/media) will deliver in each returned Tweet. Specify the desired fields in a comma-separated list without spaces between commas and fields. The Tweet will only return media fields if the Tweet contains media and if you've also included the `expansions=attachments.media_keys` query parameter in your request. While the media ID will be located in the Tweet object, you will find this ID and all additional media fields in the `includes` data object. |
| `place.fields`  <br> Optional | enum (`contained_within`, `country`, `country_code`, `full_name`, `geo`, `id`, `name`, `place_type`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [place fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/place) will deliver in each returned Tweet. Specify the desired fields in a comma-separated list without spaces between commas and fields. The Tweet will only return place fields if the Tweet contains a place and if you've also included the `expansions=geo.place_id` query parameter in your request. While the place ID will be located in the Tweet object, you will find this ID and all additional place fields in the `includes` data object. |
| `poll.fields`  <br> Optional | enum (`duration_minutes`, `end_datetime`, `id`, `options`, `voting_status`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [poll fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/poll) will deliver in each returned Tweet. Specify the desired fields in a comma-separated list without spaces between commas and fields. The Tweet will only return poll fields if the Tweet contains a poll and if you've also included the `expansions=attachments.poll_ids` query parameter in your request. While the poll ID will be located in the Tweet object, you will find this ID and all additional poll fields in the `includes` data object. |
| `tweet.fields`  <br> Optional | enum (`attachments`, `author_id`, `context_annotations`, `conversation_id`, `created_at`, `edit_controls`, `entities`, `geo`, `id`, `in_reply_to_user_id`, `lang`, `non_public_metrics`, `public_metrics`, `organic_metrics`, `promoted_metrics`, `possibly_sensitive`, `referenced_tweets`, `reply_settings`, `source`, `text`, `withheld`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [Tweet fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) will deliver in each returned Tweet object. Specify the desired fields in a comma-separated list without spaces between commas and fields. You can also pass the `expansions=referenced_tweets.id` expansion to return the specified fields for both the original Tweet and any included referenced Tweets. The requested Tweet fields will display in both the original Tweet data object, as well as in the referenced Tweet expanded data object that will be located in the `includes` data object. |
| `user.fields`  <br> Optional | enum (`created_at`, `description`, `entities`, `id`, `location`, `most_recent_tweet_id`, `name`, `pinned_tweet_id`, `profile_image_url`, `protected`, `public_metrics`, `url`, `username`, `verified`, `verified_type`, `withheld`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [user fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) will deliver in each returned Tweet. Specify the desired fields in a comma-separated list without spaces between commas and fields. While the user ID will be located in the original Tweet object, you will find this ID and all additional user fields in the `includes` data object.  <br>  <br>You must also pass one of the user expansions to return the desired user fields:  <br><br>* `expansions=author_id`<br>* `expansions=entities.mentions.username`<br>* `expansions=in_reply_to_user_id`<br>* `expansions=referenced_tweets.id.author_id` |

  
  

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript (Default fields)](#tab0)
* [TypeScript (Optional fields)](#tab1)
* [Java (Default fields)](#tab2)
* [Java (Optional fields)](#tab3)

TypeScript (Default fields)

TypeScript (Optional fields)

Java (Default fields)

Java (Optional fields)

      `(async () => {   try {     const getSpacesTweets = await twitterClient.spaces.spaceTweets(       //The space id to be retrieved       "1DXxyRYNejbKM"     );     console.dir(getSpacesTweets, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `(async () => {   try {     const getSpacesTweets = await twitterClient.spaces.spaceTweets(       //The space id to be retrieved       "1DXxyRYNejbKM",       {         //A comma separated list of fields to expand.         expansions: ["author_id"],          //A comma separated list of Space fields to display.         "user.fields": ["created_at", "description"],       }     );     console.dir(getSpacesTweets, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  // String | The space id to be retrieved String id = "1DXxyRYNejbKM";  try {     MultiTweetLookupResponse result = apiInstance.spaces().spaceTweets(id, null, null, null, null, null, null, null);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling SpacesApi#spaceTweets");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

      `// Set the params values // For full list of params visit - https://github.com/twitterdev/twitter-api-java-sdk/blob/main/docs/SpacesApi.md#spaceTweets  // String | The space id to be retrieved String id = "1DXxyRYNejbKM";  // Set<String> | A comma separated list of fields to expand. Set<String> expansions = new HashSet<>(Arrays.asList("author_id"));  // Set<String> | A comma separated list of User fields to display. Set<String> userFields = new HashSet<>(Arrays.asList("created_at", "description")););  try {     MultiTweetLookupResponse result = apiInstance.spaces().spaceTweets(id, null, null, expansions, null, null, userFields, null);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling SpacesApi#spaceTweets");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

### Example responses

* [Default fields](#tab0)
* [Optional fields](#tab1)

Default fields

Optional fields

      `{   "data": [     {       "id": "1389270063807598594",       "text": "now, everyone with 600 or more followers can host a Space.nnbased on what we've learned, these accounts are likely to have a good experience hosting because of their existing audience. before bringing the ability to create a Space to everyone, we're focused on a few things. :thread:"     },     {       "id": "1354143047324299264",       "text": "Academics are one of the biggest groups using the #TwitterAPI to research what's happening. Their work helps make the world (&amp; Twitter) a better place, and now more than ever, we must enable more of it. nIntroducing :drum_with_drumsticks: the Academic Research product track!nhttps://t.co/nOFiGewAV2"     },     {       "id": "1293595870563381249",       "text": "Twitter API v2: Early Access releasednnToday we announced Early Access to the first endpoints of the new Twitter API!nn#TwitterAPI #EarlyAccess #VersionBump https://t.co/g7v3aeIbtQ"     }   ],   "meta": {     "result_count": 3   } }`
    

      `{   "data": [     {       "id": "1389270063807598594",       "author_id": "1065249714214457345",       "text": "now, everyone with 600 or more followers can host a Space.nnbased on what we've learned, these accounts are likely to have a good experience hosting because of their existing audience. before bringing the ability to create a Space to everyone, we're focused on a few things. :thread:"     },     {       "id": "1354143047324299264",       "author_id": "783214",       "text": "Academics are one of the biggest groups using the #TwitterAPI to research what's happening. Their work helps make the world (&amp; Twitter) a better place, and now more than ever, we must enable more of it. nIntroducing :drum_with_drumsticks: the Academic Research product track!nhttps://t.co/nOFiGewAV2"     },     {       "id": "1293595870563381249",       "author_id": "783214",       "text": "Twitter API v2: Early Access releasednnToday we announced Early Access to the first endpoints of the new Twitter API!nn#TwitterAPI #EarlyAccess #VersionBump https://t.co/g7v3aeIbtQ"     }   ],   "includes": {     "users": [       {         "id": "1065249714214457345",         "created_at": "2018-11-21T14:24:58.000Z",         "name": "Spaces",         "pinned_tweet_id": "1389270063807598594",         "description": "Twitter Spaces is where live audio conversations happen.",         "username": "TwitterSpaces"       },       {         "id": "783214",         "created_at": "2007-02-20T14:35:54.000Z",         "name": "Twitter",         "description": "What's happening?!",         "username": "Twitter"       },       {         "id": "1526228120",         "created_at": "2013-06-17T23:57:45.000Z",         "name": "Twitter Data",         "description": "Data-driven insights about notable moments and conversations from Twitter, Inc., plus tips and tricks to help you get the most out of Twitter data.",         "username": "TwitterData"       }     ],     "meta": {       "result_count": 3     }   } }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Default | string | Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. |
| `text`  <br> Default | string | The content of the Tweet.  <br>  <br>To return this field, add `tweet.fields=text` in the request's query parameter. |
| `created_at` | date (ISO 8601) | Creation time of the Tweet.  <br>  <br>To return this field, add `tweet.fields=created_at` in the request's query parameter. |
| `author_id` | string | Unique identifier of this user. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers.  <br>  <br>You can obtain the expanded object in `includes.users` by adding `expansions=author_id` in the request's query parameter. |
| `edit_controls` | object | Indicates if a Tweet is eligible for edit, how long it is editable for, and the number of remaining edits.  <br>  <br>The `is_edit_eligible` field indicates if a Tweet was eligible for edit when published. This field is not dynamic and won't toggle from True to False when a Tweet reaches its editable time limit, or maximum number of edits. The following Tweet features will cause this field to be false:<br><br>* Tweet is promoted<br>* Tweet has a poll<br>* Tweet is a non-self-thread reply<br>* Tweet is a Retweet (note that Quote Tweets are eligible for edit)<br>* Tweet is nullcast<br>* Community Tweet<br>* Superfollow Tweet<br>* Collaborative Tweet<br><br>`{     "edit_controls": {      "is_edit_eligible": true,      "editable_until": "2022-08-21 09:35:20.311",      "edits_remaining": 4    }   }   `Editable Tweets can be edited for the first 30 minutes after creation and can be edited up to five times.  <br>  <br>To return this field, add `tweet.fields=edit_controls` in the request's query parameter. |
| `conversation_id` | string | The Tweet ID of the original Tweet of the conversation (which includes direct replies, replies of replies).  <br>  <br>To return this field, add `tweet.fields=conversation_id` in the request's query parameter. |
| `note_tweet` | object | Information about Tweets with more than 280 characters.  <br>  <br>To return this field, add `tweet.fields=note_tweet` in the request's query parameter. |
| `in_reply_to_user_id` | string | If this Tweet is a Reply, indicates the user ID of the parent Tweet's author. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers.  <br>  <br>You can obtain the expanded object in `includes.users` by adding `expansions=in_reply_to_user_id` in the request's query parameter. |
| `referenced_tweets` | array | A list of Tweets this Tweet refers to. For example, if the parent Tweet is a Retweet, a Retweet with comment (also known as Quoted Tweet) or a Reply, it will include the related Tweet referenced to by its parent.  <br>  <br>To return this field, add `tweet.fields=referenced_tweets` in the request's query parameter. |
| `referenced_tweets.type` | enum (`retweeted`, `quoted`, `replied_to`) | Indicates the type of relationship between this Tweet and the Tweet returned in the response: `retweeted` (this Tweet is a Retweet), `quoted` (a Retweet with comment, also known as Quoted Tweet), or `replied_to` (this Tweet is a reply). |
| `referenced_tweets.id` | string | The unique identifier of the referenced Tweet.  <br>  <br>You can obtain the expanded object in `includes.tweets` by adding `expansions=referenced_tweets.id` in the request's query parameter. |
| `attachments` | object | Specifies the type of attachments (if any) present in this Tweet.  <br>  <br>To return this field, add `tweet.fields=attachments` in the request's query parameter. |
| `attachments.media_keys` | array | List of unique identifiers of media attached to this Tweet. These identifiers use the same media key format as those returned by the [Media Library](https://developer.twitter.com/en/docs/ads/creatives/guides/media-library).  <br>  <br>You can obtain the expanded object in `includes.media` by adding `expansions=attachments.media_keys` in the request's query parameter. |
| `attachments.poll_ids` | array | List of unique identifiers of polls present in the Tweets returned. These are returned as a string in order to avoid complications with languages and tools that cannot handle large integers.  <br>  <br>You can obtain the expanded object in `includes.polls` by adding `expansions=attachments.polls_ids` in the request's query parameter. |
| `geo` | object | Contains details about the location tagged by the user in this Tweet, if they specified one.  <br>  <br>To return this field, add `tweet.fields=geo` in the request's query parameter. |
| `geo.coordinates` | object | Contains details about the coordinates of the location tagged by the user in this Tweet, if they specified one.  <br>  <br>To return this field, add `tweet.fields=geo.coordinates` in the request's query parameter. |
| `geo.coordinates.type` | string | Describes the type of coordinate. The only value supported at present is `Point`. |
| `geo.coordinates.coordinates` | array | A pair of decimal values representing the precise location of the user (latitude, longitude). This value be `null` unless the user explicitly shared their precise location. |
| `geo.place_id` | string | The unique identifier of the place, if this is a point of interest tagged in the Tweet.  <br>  <br>You can obtain the expanded object in `includes.places` by adding `expansions=geo.place_id` in the request's query parameter. |
| `context_annotations` | array | Contains context annotations for the Tweet.  <br>  <br>To return this field, add `tweet.fields=context_annotations` in the request's query parameter. |
| `context_annotations.domain` | object | Contains elements which identify detailed information regarding the domain classification based on Tweet text. |
| `context_annotations.domain.id` | string | Contains the numeric value of the domain. |
| `context_annotations.domain.name` | string | Domain name based on the Tweet text. |
| `context_annotations.domain.description` | string | Long form description of domain classification. |
| `context_annotations.entity` | object | Contains elements which identify detailed information regarding the domain classification bases on Tweet text. |
| `context_annotations.entity.id` | string | Unique value which correlates to an explicitly mentioned Person, Place, Product or Organization |
| `context_annotations.entity.name` | string | Name or reference of entity referenced in the Tweet. |
| `context_annotations.entity.description` | string | Additional information regarding referenced entity. |
| `entities` | object | Contains details about text that has a special meaning in a Tweet.  <br>  <br>To return this field, add `tweet.fields=entities` in the request's query parameter. |
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
| `entities.mentions.username` | string | The part of text recognized as a user mention.  <br>  <br>You can obtain the expanded object in `includes.users` by adding `expansions=entities.mentions.username` in the request's query parameter. |
| `entities.cashtags` | array | Contains details about text recognized as a Cashtag. |
| `entities.cashtags.start` | integer | The start position (zero-based) of the recognized Cashtag within the Tweet. All start indices are inclusive. |
| `entities.cashtags.end` | integer | The end position (zero-based) of the recognized Cashtag within the Tweet. |
| `entities.cashtags.tag` | string | The text of the Cashtag. |
| `withheld` | object | Contains withholding details for [withheld content](https://help.twitter.com/en/rules-and-policies/tweet-withheld-by-country).  <br>  <br>To return this field, add `tweet.fields=withheld` in the request's query parameter. |
| `withheld.copyright` | boolean | Indicates if the content is being withheld for on the basis of copyright infringement. |
| `withheld.country_codes` | array | Provides a list of countries where this content is not available. |
| `withheld.scope` | enum (`tweet`, `user`) | Indicates whether the content being withheld is a Tweet or a user. |
| `note_tweet` | object | Information for Tweets longer than 280 characters.  <br>  <br>To return this field, add `tweet.fields=note_tweet` in the request's query parameter. |
| `note_tweet.text` | string | The text for Tweets longer than 280 characters. |
| `note_tweet.entities` | object | Contains details about text that has a special meaning in a Tweet. |
| `note_tweet.entities.urls` | array | Contains details about text recognized as a URL. |
| `note_tweet.entities.mentions` | array | Contains details about text recognized as a user mention. |
| `note_tweet.entities.hashtags` | array | Contains details about text recognized as a Hashtag. |
| `note_tweet.entities.cashtags` | array | Contains details about text recognized as a Cashtag. |
| `public_metrics` | object | Engagement metrics for the Tweet at the time of the request.  <br>  <br>To return this field, add `tweet.fields=public_metrics` in the request's query parameter. |
| `public_metrics.retweet_count` | integer | Number of times this Tweet has been Retweeted. |
| `public_metrics.reply_count` | integer | Number of Replies of this Tweet. |
| `public_metrics.like_count` | integer | Number of Likes of this Tweet. |
| `public_metrics.quote_count` | integer | Number of times this Tweet has been Retweeted with a comment (also known as Quote). |
| `public_metrics.impression_count` | integer | Number of times this Tweet has been viewed. |
| `public_metrics.bookmark_count` | integer | Number of times this Tweet has been bookmarked. |
| `non_public_metrics` | object | Non-public engagement metrics for the Tweet at the time of the request. This is a private metric, and requires the use of OAuth 2.0 User Context authentication.  <br>  <br>To return this field, add `tweet.fields=non_public_metrics` in the request's query parameter. |
| `non_public_metrics.impression_count` | integer | Number of times the Tweet has been viewed. This is a private metric, and requires the use of OAuth 2.0 User Context authentication. |
| `non_public_metrics.url_link_clicks` | integer | Number of times a user clicks on a URL link or URL preview card in a Tweet. This is a private metric, and requires the use of OAuth 2.0 User Context authentication. |
| `non_public_metrics.user_profile_clicks` | integer | Number of times a user clicks the following portions of a Tweet - display name, user name, profile picture. This is a private metric, and requires the use of OAuth 2.0 User Context authentication. |
| `organic_metrics` | object | Organic engagement metrics for the Tweet at the time of the request. Requires user context authentication. |
| `organic_metrics.impression_count` | integer | Number of times the Tweet has been viewed organically. This is a private metric, and requires the use of OAuth 2.0 User Context authentication. |
| `organic_metrics.url_link_clicks` | integer | Number of times a user clicks on a URL link or URL preview card in a Tweet organically. This is a private metric, and requires the use of OAuth 2.0 User Context authentication. |
| `organic_metrics.user_profile_clicks` | integer | Number of times a user clicks the following portions of a Tweet organically - display name, user name, profile picture. This is a private metric, and requires the use of OAuth 2.0 User Context authentication. |
| `organic_metrics.retweet_count` | integer | Number of times the Tweet has been Retweeted organically. |
| `organic_metrics.reply_count` | integer | Number of replies the Tweet has received organically. |
| `organic_metrics.like_count` | integer | Number of likes the Tweet has received organically. |
| `promoted_metrics` | object | Engagement metrics for the Tweet at the time of the request in a promoted context. Requires user context authentication. |
| `promoted_metrics.impression_count` | integer | Number of times the Tweet has been viewed when that Tweet is being promoted. This is a private metric, and requires the use of OAuth 2.0 User Context authentication. |
| `promoted_metrics.url_link_clicks` | integer | Number of times a user clicks on a URL link or URL preview card in a Tweet when it is being promoted. This is a private metric, and requires the use of OAuth 2.0 User Context authentication. |
| `promoted_metrics.user_profile_clicks` | integer | Number of times a user clicks the following portions of a Tweet when it is being promoted - display name, user name, profile picture. This is a private metric, and requires the use of OAuth 2.0 User Context authentication. |
| `promoted_metrics.retweet_count` | integer | Number of times this Tweet has been Retweeted when that Tweet is being promoted. |
| `promoted_metrics.reply_count` | integer | Number of Replies to this Tweet when that Tweet is being promoted. |
| `promoted_metrics.like_count` | integer | Number of Likes of this Tweet when that Tweet is being promoted. |
| `possibly_sensitive` | boolean | Indicates if this Tweet contains URLs marked as sensitive, for example content suitable for mature audiences.  <br>  <br>To return this field, add `tweet.fields=possibly_sensitive` in the request's query parameter. |
| `lang` | string | Language of the Tweet, if detected by Twitter. Returned as a BCP47 language tag.  <br>  <br>To return this field, add `tweet.fields=lang` in the request's query parameter. |
| `reply_settings` | string | Shows who can reply to this Tweet. Fields returned are `everyone`, `mentionedUsers`, and `following`.  <br>  <br>To return this field, add `tweet.fields=reply_settings` in the request's query parameter. |
| `source` | string | The name of the app the user Tweeted from.  <br>  <br>To return this field, add `tweet.fields=source` in the request's query parameter. |
| `includes` | object | If you include an `[expansion](https://developer.twitter.com/en/docs/twitter-api/expansions)` parameter, the referenced objects will be returned if available. |
| `includes.tweets` | array | When including the `expansions=referenced_tweets.id` parameter, this includes a list of referenced Retweets, Quoted Tweets, or replies in the form of [Tweet objects](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) with their default fields and any additional fields requested using the `tweet.fields` parameter, assuming there is a referenced Tweet present in the returned Tweet(s). |
| `includes.users` | array | When including the `expansions=author_id` parameter, this includes a list of referenced Tweet authors in the form of [user objects](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) with their default fields and any additional fields requested using the `user.fields` parameter. |
| `includes.places` | array | When including the `expansions=geo.place_id` parameter, this includes a list of referenced places in Tweets in the form of [place objects](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/place) with their default fields and any additional fields requested using the `place.fields` parameter, assuming there is a place present in the returned Tweet(s). |
| `includes.media` | array | When including the `expansions=attachments.media_keys` parameter, this includes a list of images, videos, and GIFs included in Tweets in the form of [media objects](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/media) with their default fields and any additional fields requested using the `media.fields` parameter, assuming there is a media attachment present in the returned Tweet(s). |
| `includes.polls` | string | When including the `expansions=attachments.poll_ids` parameter, this includes a list of polls that are attached to Tweets in the form of [poll objects](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/poll) with their default fields and any additional fields requested using the `poll.fields` parameter, assuming there is a poll present in the returned Tweet(s). |
| `errors` | object | Contains details about errors that affected any of the requested Tweets. See [Status codes and error messages](https://developer.twitter.com/en/support/twitter-api/error-troubleshooting) for more details. |

Introduction

Introduction
------------

This endpoint allows you to search Spaces by their title, and to filter results by status. This endpoint is useful to discover live or upcoming Spaces based on keywords, mentioned users or hashtags in their title.

The endpoint accepts one or more keywords as a query. Its results can be filtered by the status of a Space (live or scheduled). By default, a request will return both live and scheduled Spaces that match the specified query.

**Account setup**

To access these endpoints, you will need:

* An approved [developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info).
* To authenticate using the keys and tokens from a [developer App](https://developer.twitter.com/en/docs/apps) that is located within a [Project](https://developer.twitter.com/en/docs/projects). 

Learn more about getting access to the Twitter API v2 endpoints in our [getting started guide](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api).

[Quick start](https://developer.twitter.com/en/docs/twitter-api/spaces/search/quick-start)

[Sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code)

[Run in Postman](https://t.co/twitter-api-postman)

[Try with API Explorer](https://developer.twitter.com/apitools/api?endpoint=/2/spaces/search&method=get)

Supporting resources
--------------------

[Learn how to use Postman to make requests](https://developer.twitter.com/en/docs/tutorials/postman-getting-started "Learn how to use Postman to make requests")

[Troubleshoot an error](https://developer.twitter.com/en/support/twitter-api "Troubleshoot an error")

[Visit the API reference page for this endpoint](https://developer.twitter.com/en/docs/twitter-api/spaces/search/api-reference "Visit the API reference page for this endpoint")

Quick start

Getting started with the search Spaces endpoint
-----------------------------------------------

This quick start guide will help you make your first request to the search Spaces endpoint with a set of specified fields using Postman.

If you would like to see sample code in different programming languages, please visit our [Twitter API v2 sample code GitHub repository](https://github.com/twitterdev/Twitter-API-v2-sample-code).  

### Prerequisites

To complete this guide, you will need to have a set of [keys and tokens](https://developer.twitter.com/en/docs/authentication) to authenticate your request. You can generate these keys and tokens by following these steps:

* [Sign up for a developer account](https://developer.twitter.com/en/apply-for-access) and receive approval.
* Create a [Project](https://developer.twitter.com/en/docs/projects) and an associated [developer App](https://developer.twitter.com/en/docs/apps) in the developer portal.
* Navigate to your App's “Keys and tokens” page to generate the required credentials. Make sure to save all credentials in a secure location.

### Steps to build a search Spaces request

**Step one: Start with a tool or library**  

There are several different tools, code examples, and libraries that you can use to make a request to this endpoint, but we are going to use the Postman tool here to simplify the process.

To load Twitter API v2 Postman collection into your environment, please click on the following button:

[Add Twitter API v2 to Postman](https://t.co/twitter-api-postman)

Once you have the Twitter API v2 collection loaded in Postman, navigate to the Spaces folder and find the "Search Spaces" request.  
 

**Step two: Authenticate your request**

To properly make a request to the Twitter API, you need to verify that you have permission. To do so, this endpoint requires you to authenticate your request with either [OAuth 2.0 App-Only](https://aem.twitter.biz/content/developer-twitter/en/docs/authentication/oauth-2-0/application-only.html) or [OAuth 2.0 Authorization Code with PKCE](https://aem.twitter.biz/content/developer-twitter/en/docs/authentication/oauth-2-0/authorization-code.html) authentication methods.

For simplicity's sake, we will utilize OAuth 2.0 App-Only with this request, but you will need to use one of the other authentication methods if you'd like to request private [metrics](https://aem.twitter.biz/content/developer-twitter/en/docs/twitter-api/metrics.html) or Spaces from a private user. 

To utilize OAuth 2.0 App-Only, you must add your keys and tokens, specifically the [App Access Token](https://aem.twitter.biz/content/developer-twitter/en/docs/authentication/oauth-2-0/bearer-tokens.html) (also known as the App-only Bearer Token) to Postman. You can do this by selecting the environment named “Twitter API v2” in the top-right corner of Postman and adding your keys and tokens to the "initial value" and "current value" fields (by clicking the eye icon next to the environment dropdown).

These variables will automatically be pulled into the request's authorization tab if you've done this correctly.  
 

**Step three: create a search query**

This endpoint accepts text as a search query. Unlike other search endpoints, it does not accept operators, grouping, and logical operators. For this exercise, we will use “hello” as a simple query.

In Postman, navigate to the "Params" tab and enter this user ID into the "Value" column of the id parameter.

|     |     |
| --- | --- |
| **Key** | **Value** |
| query | hello |

#### Step four: Identify and specify which fields you would like to retrieve

If you click the "Send" button after step three, you will receive the ID of the Spaces and its state, which are the only Space object fields returned by default in your response.

If you would like to receive additional fields, you will have to specify them in your request with the space.fields or expansions parameters.

For this exercise, we will requested three additional sets of fields from different objects:

* The additional title field in the primary Spaces object.
* The full user object of the specified creator ID
* The additional user.created\_at field in the associated user object.

In Postman, navigate to the “Params” tab and add the following key:value pair to the “Query Params” table:

|     |     |     |
| --- | --- | --- |
| **Key** | **Value** | **Returned fields** |
| space.fields | title | creator\_id |
| expansions | creator\_id | includes.users.id, includes.users.name, includes.users.username |
| user.fields | created\_at | includes.users.created\_at |

You should now see the following URL next to the “Send” button:

https://api.twitter.com/2/spaces/search?query=hello&space.fields=creator\_id&expansions=creator\_id&user.fields=created\_at

**Step five: Make your request and review your response**

Once you have everything set up, hit the “Send” button and you will receive the following response:

      `{    "data": [     {         "creator_id": "2244994945",         "id": "1zqKVXPQhvZJB",         "title": "Hello world 👋",         "state": "Running"    },    "includes": {        "users": [            {                "created_at": "2013-12-14T04:35:55.000Z",                "name": "Twitter Dev",                "id": "2244994945",                "username": "TwitterDev"            }        ]    } ] }`
    

Next steps
----------

[Customize your request using the API Reference](https://developer.twitter.com/en/docs/twitter-api/spaces/search/api-reference "Customize your request using the API Reference")

GET /2/spaces/search

GET /2/spaces/search
====================

Return live or scheduled Spaces matching your specified search terms. This endpoint performs a keyword search, meaning that it will return Spaces that are an exact case-insensitive match of the specified search term. The search term will match the original title of the Space.

[Run in Postman ❯](https://t.co/twitter-api-postman) 

[Try a live request ❯](https://oauth-playground.glitch.me/?id=searchSpaces&params=%28%27query%21%27Twitter%27%7Ebody%21%28%29%7Epath%21%28%29%29_) 

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Fspaces%2Fsearch&method=get) 

### Endpoint URL

`https://api.twitter.com/2/spaces/search`  
  

### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code "This method allows an authorized app to act on behalf of the user, as the user. It is typically used to access or post public information for a specific user, and it us useful when your app needs to be aware of the relationship between a user and what this endpoint returns. Click to learn how to authenticate with OAuth 2.0 Authorization Code with PKCE.")<br><br>[OAuth 2.0 App-only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only "Use this method to obtain information in the context of an unauthenticated public user. This method is for developers that just need read-only access to public information. Click to learn how to obtain an OAuth 2.0 App Access Token.") |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | User rate limit (User context): 300 requests per 15-minute window per each authenticated user<br><br>App rate limit (Application-only): 300 requests per 15-minute window shared among all users of your app |

### OAuth 2.0 scopes required by this endpoint

|     |
| --- |
| `tweet.read`<br><br>`users.read`<br><br>`space.read` |
| [Learn more about OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/twitter-api/oauth2) |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| `query`  <br> Required | string | Your search term. This can be any text (including mentions and Hashtags) present in the title of the Space. |
| `expansions`  <br> Optional | enum (`invited_user_ids`, `speaker_ids`, `creator_id`, `host_ids`, `topics_ids`) | [Expansions](https://developer.twitter.com/en/docs/twitter-api/expansions) enable you to request additional data objects that relate to the originally returned Space. Submit a list of desired expansions in a comma-separated list. The ID that represents the expanded data object will be included directly in the Space data object, but the expanded object metadata will be returned within the `includes` response object, and will also include the ID so that you can match this data object to the original Space object.  <br>  <br>The following data objects can be expanded using this parameter:  <br><br>* The Spaces creator's user object<br>* The user objects of any Space co-host<br>* Any mentioned users’ object<br>* Any speaker's user object |
| `space.fields`  <br> Optional | enum (`host_ids`, `created_at`, `creator_id`, `id`, `lang`, `invited_user_ids`, `participant_count`, `speaker_ids`, `started_at`, `ended_at`, `subscriber_count`, `topic_ids`, `state`, `title`, `updated_at`, `scheduled_start`, `is_ticketed`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [Space fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/space) will deliver in each returned Space. Specify the desired fields in a comma-separated list. |
| `state`  <br> Optional | enum (`all`, `live`, `scheduled`) | Determines the type of results to return. This endpoint returns all Spaces by default. Use `live` to only return live Spaces or `scheduled` to only return upcoming Spaces. |
| `topic.fields`  <br> Optional | enum (`id`, `name`, `description`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific topic metadata in each returned Space topic object, if the creator of the Space set one or more topics. Specify the desired fields in a comma-separated list. |
| `user.fields`  <br> Optional | enum (`created_at`, `description`, `entities`, `id`, `location`, `most_recent_tweet_id`, `name`, `pinned_tweet_id`, `profile_image_url`, `protected`, `public_metrics`, `url`, `username`, `verified`, `verified_type`, `withheld`) | This [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter enables you to select which specific [user fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) will deliver in each returned Space. Specify the desired fields in a comma-separated list without spaces between commas and fields. While the user ID will be located in the original Space object, you will find this ID and all additional user fields in the `includes` data object. |

  
  

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript](#tab0)
* [Java](#tab1)

TypeScript

Java

      `(async () => {   try {     const spacesSearch = await twitterClient.spaces.searchSpaces({       //The search query       query: "hello",        // A comma separated list of Space fields to display.       "space.fields": ["title", "host_ids"],     });     console.dir(spacesSearch, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values // For full list of params visit - https://github.com/twitterdev/twitter-api-java-sdk/blob/main/docs/SpacesApi.md#searchSpaces  // String | The search query String query = "hello";  // Set<String> | A comma separated list of Space fields to display. Set<String> spaceFields = new HashSet<>(Arrays.asList("title", "host_ids"));  try {     MultiSpaceLookupResponse result = apiInstance.spaces().searchSpaces(query, null, null, spaceFields, null, null, null);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling SpacesApi#searchSpaces");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

### Example responses

* [Response](#tab0)

Response

      `{   "data": [     {       "host_ids": [         "2244994945"       ],       "id": "1DXxyRYNejbKM",       "state": "live",       "title": "hello world 👋"     },     {       "host_ids": [         "6253282"       ],       "id": "1nAJELYEEPvGL",       "state": "scheduled",       "title": "Say hello to the Spaces endpoints"     }   ],   "meta": {     "result_count": 2   } }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Default | string | Unique identifier of this Space. |
| `host_ids` | array | An array containing the user ID of each Space co-host. These IDs are returned as strings in order to avoid complications with languages and tools that cannot handle large integers.  <br>  <br>To return this field, add `space.fields=host_ids` in the request's query parameter.  <br>  <br>You can obtain the expanded object in `includes.users` by adding `expansions=host_ids` in the request's query parameter. |
| `created_at` | date (ISO 8601) | Creation date and time of this Space. For scheduled Spaces, this indicates the time the Space was created, not the time when the Space will start.  <br>  <br>To return this field, add `space.fields=created_at` in the request's query parameter. |
| `creator_id` | string | The user ID of the account that created this Space. This ID is returned as a string in order to avoid complications with languages and tools that cannot handle large integers.  <br>  <br>To return this field, add `space.fields=creator_id` in the request's query parameter.  <br>  <br>You can obtain the expanded object in `includes.users` by adding `expansions=creator_id` in the request's query parameter. |
| `ended_at` | date (ISO 8601) | End date and time of this Space. This field will be only present for Spaces in the `ended` state.  <br>  <br>To return this field, add `space.fields=ended_at` in the request's query parameter. |
| `lang` | string | Main language of the Space’s creator, as inferred by Twitter (this may differ from the language spoken in the Space). Returned as a BCP 47 language tag.  <br>  <br>Supported values:  <br><br>* Arabic `(ar)`<br>* Armenian `(hy)`<br>* Chinese `(zh)`<br>* Danish `(da)`<br>* English `(en)`<br>* Finnish `(fi)`<br>* French `(fr)`<br>* German `(de)`<br>* Hindi `(hi)`<br>* Hebrew `(iw)`<br>* Indonesian `(in)`<br>* Italian `(it)`<br>* Japanese `(ja)`<br>* Kazakh `(kk)`<br>* Korean `(ko)`<br>* Norwegian `(no)`<br>* Polish `(pl)`<br>* Portuguese `(pt)`<br>* Romanian `(ro)`<br>* Russian `(ru)`<br>* Spanish `(es)`<br>* Swedish `(sv)`<br>* Turkish `(tr)`<br>* Ukranian `(uk)`<br><br>  <br>  <br>To return this field, add `space.fields=lang` in the request's query parameter. |
| `is_ticketed` | boolean | Indicates if this is a ticketed Space.  <br>  <br>To return this field, add `space.fields=is_ticketed` in the request's query parameter. |
| `invited_user_ids` | array | The list of user IDs that can automatically join as Speakers. Usually, users in this list are invited to speak via the Invite user option and have a Speaker role when the Space starts.  <br>  <br>These IDs are returned as strings in order to avoid complications with languages and tools that cannot handle large integers.  <br>  <br>To return this field, add `space.fields=invited_user_ids` in the request's query parameter.  <br>  <br>You can obtain the expanded object in `includes.users` by adding `expansions=invited_user_ids` in the request's query parameter. |
| `participant_count` | integer | The current number of users in the Space, including Hosts and Speakers.  <br>  <br>To return this field, add `space.fields=participant_count` in the request's query parameter. |
| `scheduled_start` | date (ISO 8601) | Indicates the scheduled start time of a Space. This field is returned only if the Space has been scheduled; in other words, if the field is returned, it means the Space is a scheduled Space.  <br>  <br>To return this field, add `space.fields=scheduled_start` in the request's query parameter. |
| `speaker_ids` | array | The list of users who were speaking at any point during the Space. This list contains all the users in `invited_user_ids` in addition to any user who requested to speak and was allowed via the Add speaker option.  <br>  <br>These IDs are returned as strings in order to avoid complications with languages and tools that cannot handle large integers.These IDs are returned as strings in order to avoid complications with languages and tools that cannot handle large integers.  <br>  <br>To return this field, add `space.fields=speaker_ids` in the request's query parameter.  <br>  <br>You can obtain the expanded object in `includes.users` by adding `expansions=speaker_ids` in the request's query parameter. |
| `started_at` | date (ISO 8601) | The start date and time of the Space. Only available if the space has started.  <br>  <br>To return this field, add `space.fields=started_at` in the request's query parameter. |
| `state`  <br> Default | enum (`live`, `scheduled`) | Indicates whether the Space is scheduled and hasn’t started yet (`scheduled`) or if it’s in progress (`live`).  <br>  <br>To return this field, add `space.fields=state` in the request's query parameter. |
| `subscriber_count` | integer | Indicates the number of people who set a remainder to this Space. This field can only be requested if your app is authentic the request using the Access Token of the creator of the Space.  <br>  <br>To return this field, add `space.fields=subscriber_count` in the request's query parameter. |
| `topic_ids` | string | A list of the Space topic IDs, if set by the creator of the Space.  <br>  <br>To return this field, add `space.fields=topic_ids` in the request's query parameter. |
| `topics.id` | string | The ID of the Space topic.  <br>  <br>To return this field, add `topic.fields=topics.id` in the request's query parameter.  <br>  <br>You can obtain the expanded object in `includes.topics` by adding `expansions=topics` in the request's query parameter. |
| `topics.id` | string | The ID of the Space topic.  <br>  <br>To return this field, add `topic.fields=topics.id` in the request's query parameter.  <br>  <br>You can obtain the expanded object in `includes.topics` by adding `expansions=topics` in the request's query parameter. |
| `topics.name` | string | The name of the Space topic.  <br>  <br>To return this field, add `topic.fields=topics.name` in the request's query parameter.  <br>  <br>You can obtain the expanded object in `includes.topics` by adding `expansions=topics` in the request's query parameter. |
| `topics.name` | string | A full text description of the Space topic.  <br>  <br>To return this field, add `topic.fields=topics.name` in the request's query parameter.  <br>  <br>You can obtain the expanded object in `includes.topics` by adding `expansions=topics` in the request's query parameter. |
| `title` | string | The title of this Space as specified by the creator.  <br>  <br>To return this field, add `space.fields=title` in the request's query parameter. |
| `updated_at` | date (ISO 8601) | The timestamp of the last update to any of this Space's metadata, such as the title or scheduled time.  <br>  <br>To return this field, add `space.fields=updated_at` in the request's query parameter. |
| `includes` | object | If you include an `[expansion](https://developer.twitter.com/en/docs/twitter-api/expansions)` parameter, the referenced objects will be returned if available. |
| `includes.users` | array | When including the `expansions=author_id` parameter, this includes a list of referenced Tweet authors in the form of [user objects](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) with their default fields and any additional fields requested using the `user.fields` parameter. |
| `errors` | object | Contains details about errors that affected any of the requested Tweets. See [Status codes and error messages](https://developer.twitter.com/en/support/twitter-api/error-troubleshooting) for more details. |