
GET /2/dm\_conversations/:dm\_conversation\_id/dm\_events | Docs | Twitter Developer Platform 

GET /2/dm\_conversations/:dm\_conversation\_id/dm\_events

 GET /2/dm\_conversations/:dm\_conversation\_id/dm\_events
=========================================================
Returns a list of Direct Messages within a conversation specified in the `dm_conversation_id` path parameter. Messages are returned in reverse chronological order.
Run in Postman ❯Try a live request ❯Build request with API Explorer ❯### Endpoint URL
`https://api.twitter.com/2/dm_conversations/:dm_conversation_id/dm_events`  
### Authentication and rate limits

|  |  |
| --- | --- |
| Authentication methodssupported by this endpoint | OAuth 2.0 Authorization Code with PKCE |
| Rate limit | User rate limit (User context): 300 requests per 15-minute window per each authenticated user |
### OAuth 2.0 scopes required by this endpoint

|  |
| --- |
| `dm.read``tweet.read``user.read` |
| Learn more about OAuth 2.0 Authorization Code with PKCE |
### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `dm_conversation_id` Required  | string | The `id` of the Direct Message conversation for which events are being retrieved.
 |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| `dm_event.fields` Optional  | enum (`id`, `text`, `event_type`, `created_at`, `dm_conversation_id`, `sender_id`, `participant_ids`, `referenced_tweets`, `attachments`) | Extra fields to include in the event payload. `id`, and `event_type` are returned by default. The `text` value isn't included for `ParticipantsJoin` and `PartcipantsLeave` events. |
| `event_types` Optional  | enum (`MessageCreate`, `ParticipantsJoin`, `ParticipantsLeave`) | The type of Direct Message event to returm. If not included, all types are returned. |
| `expansions` Optional  | enum (`attachments.media_keys`, `referenced_tweets.id`, `sender_id`, `participant_ids`) | Expansions enable you to request additional data objects that relate to the returned Direct Message conversation events. Submit a list of desired expansions in a comma-separated list without spaces. The IDs that represents the expanded data objects will be included directly in the event data object, and the expanded object metadata will be returned within the `includes` response object.The following data objects can be expanded using this parameter:* The user object for the message sender.
* Attached media's object.
* Any referenced Tweet's object.
* The user object for who is joining or leaving group conversations.
 |
| `max_results` Optional  | number | The maximum number of results to be returned in a page. Must be between 1 and 100. The default is 100. |
| `media.fields` Optional  | enum (`duration_ms`, `height`, `media_key`, `preview_image_url`, `type`, `url`, `width`, `public_metrics`, `alt_text`, `variants`) | This fields parameter enables you to select which specific media fields will be delivered in Direct Message 'MessageCreate' events.Specify the desired fields in a comma-separated list without spaces between commas and fields. While the media ID will be located in the event object, you will find this ID and all additional media fields in the `includes` data object.The event object will only include media fields if the Direct Message contains media and if you've also included the `expansions=attachments.media_keys` query parameter in your request. |
| `pagination_token` Optional  | string | Contains either the `next_token` or `previous_token` value. |
| `tweet.fields` Optional  | enum (`attachments`, `author_id`, `context_annotations`, `conversation_id`, `created_at`, `edit_controls`, `entities`, `geo`, `id`, `in_reply_to_user_id`, `lang`, `public_metrics`, `possibly_sensitive`, `referenced_tweets`, `reply_settings`, `source`, `text`, `withheld`) | This fields parameter enables you to select which specific Tweet fields will be delivered in each returned Direct Message 'MessageCreate' event object that contains a Tweet reference.Specify the desired fields in a comma-separated list without spaces between commas and fields. While the Tweet ID will be in the event object, you will find this ID and all additional Tweet fields in the `includes data object. The event object will include Tweet fields only if the Direct Message references a Tweet and the `expansions=referenced_tweet.id` query parameter is included in the request.` |
| `user.fields` Optional  | enum (`created_at`, `description`, `entities`, `id`, `location`, `most_recent_tweet_id`, `name`, `pinned_tweet_id`, `profile_image_url`, `protected`, `public_metrics`, `url`, `username`, `verified`, `withheld`) | This fields parameter enables you to select which specific user fields will be delivered for Direct Message conversation events that reference a sender or participant ID.Specify the desired fields in a comma-separated list without spaces between commas and fields.While the user ID will be located in the event object, you will find this ID and all additional user fields in the `includes` data object.You must also pass one of the user-based expansions to return the desired user fields:* `expansions=sender_id`
* `expansions=participants_id`
 |

### Example code with offical SDKs

* cURL (default fields)
* cURL (optional fields)

 cURL (default fields)

 cURL (optional fields)

```
      curl "https://api.twitter.com/2/dm_conversations/:dm_conversation_id/dm_events" -H "Authorization: Bearer $ACCESS_TOKEN" -H "Authorization: Bearer $ACCESS_TOKEN"
```

```
      curl "https://api.twitter.com/2/dm_conversations/:dm_conversation_id/dm_events?dm_event.fields=id,text,event_type,dm_conversation_id,created_at,sender_id,attachments,participant_ids,referenced_tweets" -H Authorization: Bearer $ACCESS_TOKEN"
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
      "event_type": "MessageCreate",
      "id": "1346889436626259968",
      "text": "Hello just you..."
    }
  ]
}
```

```
      {
  "data": [
    {
      "id": "1585321444547837956",
      "text": "Another photo https://t.co/J5KotyeIyd",
      "event_type": "MessageCreate",
      "dm_conversation_id": "1585094756761149440",
      "created_at": "2022-10-26T17:24:21.000Z",
      "sender_id": "906948460078698496"
    }
  ]
}
```

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | string | The `id` of the Direct Message event. |
| `text` | string | The text included in the Direct Message. |
| `event_type` | string | The type of event. Possible values include MessageCreate, ParticipantsJoin, ParticipantsLeave. |
| `created_at` | date (ISO 8601) | The `timestamp` of the Direct Message event creation. |
| `sender_id` | string | The `id` of the user who sent the Direct Message. |
| `dm_conversation_id` | string | The `id` of the conversation the Direct Message belongs to. |
| `attachments` | object | The attached urls and media information for expansion. E.g. Media, Tweet, Card |
| `attachments.media_keys` | array | List of unique identifiers of media attached to a direct message. These identifiers use the same media key format as those returned by the Media Library.You can obtain the expanded object in `includes.media` by adding `expansions=attachments.media_keys` in the request's query parameter. |
| `referenced_tweets` | array | Expansion of a "shared" Tweet in the Direct Message. If the parent Tweet is a Retweet, a Retweet with comment (also known as Quoted Tweet) or a Reply, it will include the related Tweet referenced to by its parent. |
| `referenced_tweets.id` | string | The `id` of a "shared" Tweet in the Direct Message.You can obtain the expanded object in `includes.tweets` by adding `expansions=referenced_tweets.id` in the request's query parameter. |
| `media.fields` | enum (`duration_ms`, `height`, `media_key`, `preview_image_url`, `type`, `url`, `width`, `public_metrics`, `non_public_metrics`, `organic_metrics`, `promoted_metrics`, `alt_text`, `variants`) | Expansion of included media with its own fields. E.g. url, size, etc. When including the `expansions=attachments.media_keys` parameter, this includes a list of images, videos, and GIFs included in Tweets in the form of media objects with their default fields and any additional fields requested using the `media.fields` parameter, assuming there is a media attachment present in the returned Tweet(s).You can obtain the expanded object in `includes.media` by adding `expansions=media.fields` in the request's query parameter. |
| `user.fields` | string | The Expansion of user object via `sender_id`.You can obtain the expanded object in `includes.users` by adding `expansions=user.fields` in the request's query parameter. |
| `meta` | object | This object contains information about the number of messages returned in the current request and pagination details. |
| `meta.next_token` | string | A value that encodes the next 'page' of results that can be requested, via the `pagination_token` request parameter. |
| `meta.previous_token` | string | A value that encodes the previous 'page' of results that can be requested, via the `pagination_token` request parameter. |
| `meta.result_count` | number | The number of results in the current page. |
| `errors` | object | Contains details about errors in a request for messages in a specified conversation. |

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