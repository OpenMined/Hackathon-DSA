
POST /2/dm\_conversations/:dm\_conversation\_id/messages | Docs | Twitter Developer Platform 

POST /2/dm\_conversations/:dm\_conversation\_id/messages

 POST /2/dm\_conversations/:dm\_conversation\_id/messages
========================================================
Creates a Direct Message on behalf of an authenticated user, and adds it to the specified conversation.
Run in Postman ❯Try a live request ❯Build request with API Explorer ❯### Endpoint URL
`https://api.twitter.com/2/dm_conversations/:dm_conversation_id/messages`  
### Authentication and rate limits

|  |  |
| --- | --- |
| Authentication methodssupported by this endpoint | OAuth 2.0 App-onlyOAuth 2.0 Authorization Code with PKCEOAuth 1.0a is also available for this endpoint. |
| Rate limit | User rate limit (User context): 200 requests per 15-minute window per each authenticated userApp rate limit (Application-only): 15000 requests per 24-hour window shared among all users of your app |
### OAuth 2.0 scopes required by this endpoint

|  |
| --- |
| `dm.write``dm.read``tweet.read``users.read` |
| Learn more about OAuth 2.0 Authorization Code with PKCE |
### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `dm_conversation_id` Required  | string | The `dm_conversation_id` of the conversation to add the Direct Message to. Supports both 1-1 and group conversations.
 |

### JSON body parameters

| Name | Type | Description |
| --- | --- | --- |
| `attachments` Optional  | array | A single Media ID being attached to the Direct Message. This field is required if `text` is not present. For this launch, only 1 attachment is supported.Example: `{"text": "Sending a DM with media!", "attachments": [{"media_id": "1455952740635586573"}]` |
| `text` Optional  | string | Text of the Direct Message being created. This field is required if `attachments` is not present. Text messages support up to 10,000 characters.Example: `{"text": "Hello just you conversation participants!""}` |

### Example code with offical SDKs

* cURL

 cURL

```
      curl -X POST "https://api.twitter.com/2/dm_conversations/:dm_conversation_id/messages" -d '{"text": "Adding a Direct Message to a conversation by referencing the conversation ID. This method supports both one-to-one and group conversations."}' -H "Authorization: Bearer $ACCESS_TOKEN"
```

### Example responses

* Successful response

 Successful response

```
      {
  "dm_conversation_id": "1346889436626259968",
  "dm_event_id": "128341038123"
}
```

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `dm_conversation_id` | string | Contains the `id` of the Direct Message conversation the Direct Message was added to. |
| `dm_event_id` | string | Contains the `id` of the event created by this request. |

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