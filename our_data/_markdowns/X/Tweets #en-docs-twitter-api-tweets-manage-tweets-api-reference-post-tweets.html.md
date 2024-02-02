
POST /2/tweets | Docs | Twitter Developer Platform 

POST /2/tweets

 POST /2/tweets
==============
Creates a Tweet on behalf of an authenticated user.
Run in Postman ❯Try a live request ❯Build request with API Explorer ❯### Endpoint URL
`https://api.twitter.com/2/tweets`  
### Authentication and rate limits

|  |  |
| --- | --- |
| Authentication methodssupported by this endpoint | OAuth 2.0 Authorization Code with PKCEOAuth 1.0a is also available for this endpoint. |
| Rate limit | User rate limit (User context): 200 requests per 15-minute window per each authenticated user |
### OAuth 2.0 scopes required by this endpoint

|  |
| --- |
| `tweet.read``tweet.write``users.read` |
| Learn more about OAuth 2.0 Authorization Code with PKCE |
### JSON body parameters

| Name | Type | Description |
| --- | --- | --- |
| `direct_message_deep_link` Optional  | string | Tweets a link directly to a Direct Message conversation with an account.Example: `{"text": "Tweeting a DM deep link!", "direct_message_deep_link": "https://twitter.com/messages/compose?recipient_id=2244994945"}` |
| `for_super_followers_only` Optional  | boolean | Allows you to Tweet exclusively for Super Followers.Example: `{"text": "Hello World!", "for_super_followers_only": true}` |
| `geo` Optional  | object | A JSON object that contains location information for a Tweet. You can only add a location to Tweets if you have geo enabled in your profile settings. If you don't have geo enabled, you can still add a location parameter in your request body, but it won't get attached to your Tweet |
| `geo.place_id` Optional  | string | Place ID being attached to the Tweet for geo location.Example: `{"text": "Tweeting with geo!","geo": {"place_id": "5a110d312052166f"}}` |
| `media` Optional  | object | A JSON object that contains media information being attached to created Tweet. This is mutually exclusive from Quote Tweet ID and Poll. |
| `media.media_ids` Optional  | array | A list of Media IDs being attached to the Tweet. This is only required if the request includes the `tagged_user_ids`.Example: `{"text": "Tweeting with media!", "media": {"media_ids": ["1455952740635586573"]}}` |
| `media.tagged_user_ids` Optional  | array | A list of User IDs being tagged in the Tweet with Media. If the user you're tagging doesn't have photo-tagging enabled, their names won't show up in the list of tagged users even though the Tweet is successfully created.Example: `{"text": "Tagging users in images!", "media": {"media_ids": ["1455952740635586573"], "tagged_user_ids": ["2244994945","6253282"]}}` |
| `poll` Optional  | object | A JSON object that contains options for a Tweet with a poll. This is mutually exclusive from Media and Quote Tweet ID. |
| `poll.duration_minutes` Optional  | number | Duration of the poll in minutes for a Tweet with a poll. This is only required if the request includes `poll.options`.Example: `{"text": "Tweeting with polls!", "poll": {"options": ["yes", "maybe", "no"], "duration_minutes": 120}}` |
| `poll.options` Optional  | array | A list of poll options for a Tweet with a poll. For the request to be successful it must also include `duration_minutes` too.Example: `{"text": "Tweeting with polls!", "poll": {"options": ["yes", "maybe", "no"], "duration_minutes": 120}}"` |
| `quote_tweet_id` Optional  | string | Link to the Tweet being quoted. Example: `{"text": "Yay!", "quote_tweet_id": "1455953449422516226"}` |
| `reply` Optional  | object | A JSON object that contains information of the Tweet being replied to. |
| `reply.exclude_reply_user_ids` Optional  | array | A list of User IDs to be excluded from the reply Tweet thus removing a user from a thread.Example: `{"text": "Yay!", "reply": {"in_reply_to_tweet_id": "1455953449422516226", "exclude_reply_user_ids": ["6253282"]}}` |
| `reply.in_reply_to_tweet_id` Optional  | string | Tweet ID of the Tweet being replied to. Please note that `in_reply_to_tweet_id` needs to be in the request if `exclude_reply_user_ids` is present.Example: `{"text": "Excited!", "reply": {"in_reply_to_tweet_id": "1455953449422516226"}}` |
| `reply_settings` Optional  | string | Settings to indicate who can reply to the Tweet. Options include "mentionedUsers" and "following". If the field isn’t specified, it will default to everyone.Example:`{"text": "Tweeting with reply settings!", "reply_settings": "mentionedUsers"}` |
| `text` Optional  | string | Text of the Tweet being created. This field is required if `media.media_ids` is not present.Example: `{"text": "Hello World!"}` |

### Example code with offical SDKs

* TypeScript (text with poll option)
* Java (text with poll option)

 TypeScript (text with poll option)

 Java (text with poll option)

```
      (async () => {
  try {
    const postTweet = await twitterClient.tweets.createTweet({
      // The text of the Tweet
      text: "Are you excited for the weekend?",
      // Options for a Tweet with a poll
      poll: {
        options: ["Yes", "Maybe", "No"],
        duration_minutes: 120,
      },
    });
    console.dir(postTweet, {
      depth: null,
    });
  } catch (error) {
    console.log(error);
  }
})();

```

```
      // Set the params values
CreateTweetRequest createTweetRequest = new CreateTweetRequest();
CreateTweetRequestPoll createTweetRequestPoll = new CreateTweetRequestPoll();
// The text of the Tweet
createTweetRequest.text("Are you excited for the weekend?");
// Options for a Tweet with a poll
List<String> pollOptions = Arrays.asList("Yes", "Maybe", "No");
createTweetRequestPoll.options(pollOptions);
// Duration of the poll in minutes
createTweetRequestPoll.durationMinutes(120);
createTweetRequest.poll(createTweetRequestPoll);
try {
    TweetCreateResponse result = apiInstance.tweets().createTweet(createTweetRequest);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling TweetsApi#createTweet");
    System.err.println("Status code: " + e.getCode());
    System.err.println("Reason: " + e.getResponseBody());
    System.err.println("Response headers: " + e.getResponseHeaders());
    e.printStackTrace();
}

```

### Example responses

* Successful response

 Successful response

```
      {
  "data": {
    "id": "1445880548472328192",
    "text": "Are you excited for the weekend?"
  }
}
```

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | string | The ID of the newly created Tweet. |
| `text` | string | The text of the newly created Tweet. |

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