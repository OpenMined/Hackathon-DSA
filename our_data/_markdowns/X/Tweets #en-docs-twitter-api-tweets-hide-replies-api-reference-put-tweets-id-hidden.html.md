
PUT /2/tweets/:id/hidden | Docs | Twitter Developer Platform 

PUT /2/tweets/:id/hidden

 PUT /2/tweets/:id/hidden
========================
Hides or unhides a reply to a Tweet.
Run in Postman ❯Try a live request ❯Build request with API Explorer ❯### Endpoint URL
`https://api.twitter.com/2/tweets/:id/hidden`  
### Authentication and rate limits

|  |  |
| --- | --- |
| Authentication methodssupported by this endpoint | OAuth 2.0 Authorization Code with PKCEOAuth 1.0a is also available for this endpoint. |
| Rate limit | User rate limit (User context): 50 requests per 15-minute window per each authenticated user |
### OAuth 2.0 scopes required by this endpoint

|  |
| --- |
| `tweet.read``users.read``tweet.moderate.write` |
| Learn more about OAuth 2.0 Authorization Code with PKCE |
### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `id` Required  | string | Unique identifier of the Tweet to hide or unhide. The Tweet must belong to a conversation initiated by the authenticating user. |

### JSON body parameters

| Name | Type | Description |
| --- | --- | --- |
| `hidden` Required  | boolean | Indicates the action to perform. Specify `true` to hide the Tweet, `false` to unhide. Trying to hide a Tweet that's already hidden (or unhide a Tweet that is not hidden) will result in a successful call. |

### Example code with offical SDKs

* TypeScript - hide reply
* TypeScript - unhide reply
* Java - hide reply
* Java - unhide reply

 TypeScript - hide reply

 TypeScript - unhide reply

 Java - hide reply

 Java - unhide reply

```
      (async () => {
  try {
    const hideReply = await twitterClient.tweets.hideReplyById(
      // The ID of the reply that you want to hide or unhide.
      "1228393702244134912",
      {
        hidden: true,
      }
    );
    console.dir(hideReply, {
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
    const unhideReply = await twitterClient.tweets.hideReplyById(
      // The ID of the reply that you want to hide or unhide.
      "1228393702244134912",
      {
        hidden: false,
      }
    );
    console.dir(unhideReply, {
      depth: null,
    });
  } catch (error) {
    console.log(error);
  }
})();

```

```
      HideReplyByIdRequest hideReplyByIdRequest = new HideReplyByIdRequest(); // HideReplyByIdRequest | 
hideReplyByIdRequest.hidden(true)
// String | The ID of the reply that you want to hide or unhide.
String id = "1228393702244134912";
try {
    HideReplyByIdResponse result = apiInstance.tweets().hideReplyById(hideReplyByIdRequest, id);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling TweetsApi#hideReplyById");
    System.err.println("Status code: " + e.getCode());
    System.err.println("Reason: " + e.getResponseBody());
    System.err.println("Response headers: " + e.getResponseHeaders());
    e.printStackTrace();
}

```

```
      HideReplyByIdRequest hideReplyByIdRequest = new HideReplyByIdRequest(); 
hideReplyByIdRequest.hidden(false)
// String | The ID of the reply that you want to hide or unhide.
String id = "1228393702244134912";
try {
    HideReplyByIdResponse result = apiInstance.tweets().hideReplyById(hideReplyByIdRequest, id);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling TweetsApi#hideReplyById");
    System.err.println("Status code: " + e.getCode());
    System.err.println("Reason: " + e.getResponseBody());
    System.err.println("Response headers: " + e.getResponseHeaders());
    e.printStackTrace();
}

```

### Example responses

* Success (reply hidden)
* Success (reply unhidden)

 Success (reply hidden)

 Success (reply unhidden)

```
      {
  "data": {
    "hidden": true
  }
}
```

```
      {
  "data": {
    "hidden": false
  }
}
```

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `hidden` | boolean | Indicates if the Tweet was successfully hidden or unhidden. |

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