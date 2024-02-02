



DELETE /2/users/:id/likes/:tweet\_id | Docs | Twitter Developer Platform 





































































































DELETE /2/users/:id/likes/:tweet\_id



 DELETE /2/users/:id/likes/:tweet\_id
====================================

Allows a user or authenticated user ID to unlike a Tweet.  
  
The request succeeds with no action when the user sends a request to a user they're not liking the Tweet or have already unliked the Tweet.

Run in Postman ❯Try a live request ❯Build request with API Explorer ❯### Endpoint URL

`https://api.twitter.com/2/users/:id/likes/:tweet_id`  
  
### Authentication and rate limits



|  |  |
| --- | --- |
| Authentication methodssupported by this endpoint | OAuth 2.0 Authorization Code with PKCEOAuth 1.0a is also available for this endpoint. |
| Rate limit | User rate limit (User context): 50 requests per 15-minute window per each authenticated user |

### OAuth 2.0 scopes required by this endpoint



|  |
| --- |
| `tweet.read``users.read``like.write` |
| Learn more about OAuth 2.0 Authorization Code with PKCE |

### Path parameters



| Name | Type | Description |
| --- | --- | --- |
| `id` Required  | string | The user ID who you are removing a Like of a Tweet on behalf of. It must match your own user ID or that of an authenticating user, meaning that you must pass the Access Tokens associated with the user ID when authenticating your request. |
| `tweet_id` Required  | string | The ID of the Tweet that you would like the `id` to unlike. |

  
  
### Example code with offical SDKs








* TypeScript
* Java


















 TypeScript
 

 Java
 
















```

      (async () => {
  try {
    const unlikeTweet = await twitterClient.tweets.usersIdUnlike(
      // The ID of the user that is requesting to unlike the tweet
      "2244994945",

      // The ID of the tweet that the user is requesting to unlike
      "1228393702244134912"
    );
    console.dir(unlikeTweet, {
      depth: null,
    });
  } catch (error) {
    console.log(error);
  }
})();

    
```
















```

      // Set the params values

// String | The ID of the user that is requesting to unlike the tweet
String id = "2244994945";

// String | The ID of the tweet that the user is requesting to unlike
String tweetId = "1228393702244134912";

try {
    UsersLikesDeleteResponse result = apiInstance.tweets().usersIdUnlike(id, tweetId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling TweetsApi#usersIdUnlike");
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
    "liked": false
  }
}
    
```












### Response fields



| Name | Type | Description |
| --- | --- | --- |
| `liked` | boolean | Indicates whether the user is unliking the specified Tweet as a result of this request. The returned value is `false` for a successful unlike request. |



















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















