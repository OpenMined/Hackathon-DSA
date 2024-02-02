
POST /2/users/:id/following | Docs | Twitter Developer Platform 

POST /2/users/:id/following

 POST /2/users/:id/following
===========================
Allows a user ID to follow another user.  
If the target user does not have public Tweets, this endpoint will send a follow request.  
The request succeeds with no action when the authenticated user sends a request to a user they're already following, or if they're sending a follower request to a user that does not have public Tweets.
Run in Postman ❯Try a live request ❯Build request with API Explorer ❯### Endpoint URL
`https://api.twitter.com/2/users/:id/following`  
### Authentication and rate limits

|  |  |
| --- | --- |
| Authentication methodssupported by this endpoint | OAuth 1.0a is also available for this endpoint.OAuth 2.0 Authorization Code with PKCE |
| Rate limit | User rate limit (User context): 50 requests per 15-minute window per each authenticated user |
### OAuth 2.0 scopes required by this endpoint

|  |
| --- |
| `tweet.read``users.read``follows.write` |
| Learn more about OAuth 2.0 Authorization Code with PKCE |
### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `id` Required  | string | The authenticated user ID who you would like to initiate the follow on behalf of. You must pass the Access Tokens that relate to this user when authenticating the request. |

### JSON body parameters

| Name | Type | Description |
| --- | --- | --- |
| `target_user_id` Required  | string | The user ID of the user that you would like the `id` to follow. |

### Example code with offical SDKs

* TypeScript
* Java

 TypeScript

 Java

```
      (async () => {
  try {
    const followUser = await twitterClient.users.usersIdFollow(
      //The ID of the user that is requesting to follow the target user
      "6253282",
      {
        //The ID of the user that the source user is requesting to follow
        target_user_id: "2244994945",
      }
    );
    console.dir(followUser, {
      depth: null,
    });
  } catch (error) {
    console.log(error);
  }
})();

```

```
      // Set the params values
UsersIdFollowRequest usersIdFollowRequest = new UsersIdFollowRequest(); 
//The ID of the user that the source user is requesting to follow
usersIdFollowRequest.targetUserId("2244994945");
// String | The ID of the user that is requesting to follow the target user
String id = "6253282";
try {
    UsersFollowingCreateResponse result = apiInstance.users().usersIdFollow(usersIdFollowRequest, id);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling UsersApi#usersIdFollow");
    System.err.println("Status code: " + e.getCode());
    System.err.println("Reason: " + e.getResponseBody());
    System.err.println("Response headers: " + e.getResponseHeaders());
    e.printStackTrace();
}

```

### Example responses

* Successful response (public user)
* Successful response (protected user)

 Successful response (public user)

 Successful response (protected user)

```
      {
  "data": {
    "following": true,
    "pending_follow": false
  }
}
```

```
      {
  "data": {
    "following": false,
    "pending_follow": true
  }
}
```

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `following` | boolean | Indicates whether the `id` is following the specified user as a result of this request. This value is `false` if the target user does not have public Tweets, as they will have to approve the follower request. |
| `pending_follow` | boolean | Indicates whether the target user will need to approve the follow request. Note that the authenticated user will follow the target user only when they approve the incoming follower request. |

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