
DELETE /2/users/:source\_user\_id/following/:target\_user\_id | Docs | Twitter Developer Platform 

DELETE /2/users/:source\_user\_id/following/:target\_user\_id

 DELETE /2/users/:source\_user\_id/following/:target\_user\_id
=============================================================
Allows a user ID to unfollow another user.  
The request succeeds with no action when the authenticated user sends a request to a user they're not following or have already unfollowed.
Run in Postman ❯Try a live request ❯Build request with API Explorer ❯### Endpoint URL
`https://api.twitter.com/2/users/:source_user_id/following/:target_user_id`  
### Authentication and rate limits

|  |  |
| --- | --- |
| Authentication methodssupported by this endpoint | OAuth 2.0 Authorization Code with PKCEOAuth 1.0a is also available for this endpoint. |
| Rate limit | User rate limit (User context): 50 requests per 15-minute window per each authenticated user |
### OAuth 2.0 scopes required by this endpoint

|  |
| --- |
| `tweet.read``users.read``follows.write` |
| Learn more about OAuth 2.0 Authorization Code with PKCE |
### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `source_user_id` Required  | string | The user ID who you would like to initiate the unfollow on behalf of. You must pass the Access Tokens that relate to this user when authenticating the request. |
| `target_user_id` Required  | string | The user ID of the user that you would like the `source_user_id` to unfollow. |

### Example code with offical SDKs

* TypeScript
* Java

 TypeScript

 Java

```
      (async () => {
  try {
    const unfollowUser = await twitterClient.users.usersIdUnfollow(
      //The ID of the user that is requesting to unfollow the target user
      "2244994945",
      //The ID of the user that the source user is requesting to unfollow
      "6253282"
    );
    console.dir(unfollowUser, {
      depth: null,
    });
  } catch (error) {
    console.log(error);
  }
})();

```

```
      // Set the params values
// String | The ID of the user that is requesting to unfollow the target user
String sourceUserId = "2244994945";
// String | The ID of the user that the source user is requesting to unfollow
String targetUserId = "6253282";
try {
    UsersFollowingDeleteResponse result = apiInstance.users().usersIdUnfollow(sourceUserId, targetUserId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling UsersApi#usersIdUnfollow");
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
    "following": false
  }
}
```

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `following` | boolean | Indicates whether the source\_user\_id is unfollowing the specified user as a result of this request. This value is `false` for a successful the unfollow request. |

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