



POST /2/users/:id/retweets | Docs | Twitter Developer Platform 





































































































POST /2/users/:id/retweets



 POST /2/users/:id/retweets
==========================

Causes the user ID identified in the path parameter to Retweet the target Tweet.

Run in Postman ❯Try a live request ❯Build request with API Explorer ❯### Endpoint URL

`https://api.twitter.com/2/users/:id/retweets`  
  
### Authentication and rate limits



|  |  |
| --- | --- |
| Authentication methodssupported by this endpoint | OAuth 2.0 Authorization Code with PKCEOAuth 1.0a is also available for this endpoint. |
| Rate limit | User rate limit (User context): 50 requests per 15-minute window per each authenticated user |

### OAuth 2.0 scopes required by this endpoint



|  |
| --- |
| `tweet.read``tweet.write``users.read` |
| Learn more about OAuth 2.0 Authorization Code with PKCE |

### Path parameters



| Name | Type | Description |
| --- | --- | --- |
| `id` Required  | string | The user ID who you are Retweeting a Tweet on behalf of. It must match your own user ID or that of an authenticating user, meaning that you must pass the Access Tokens associated with the user ID when authenticating your request. |

  
  
### JSON body parameters



| Name | Type | Description |
| --- | --- | --- |
| `tweet_id` Required  | string | The ID of the Tweet that you would like the user `id` to Retweet. |

  
  
### Example code with offical SDKs








* TypeScript
* Java


















 TypeScript
 

 Java
 
















```

      (async () => {
  try {
    const createRetweet = await twitterClient.tweets.usersIdRetweets(
      //The ID of the user that is requesting to retweet the tweet
      "2244994945",
      {
        //The ID of the tweet the user is requesting to retweet
        tweet_id: "1228393702244134912",
      }
    );
    console.dir(createRetweet, {
      depth: null,
    });
  } catch (error) {
    console.log(error);
  }
})();

    
```
















```

      // String | The ID of the tweet the user is requesting to retweet
String tweetId = "1228393702244134912"
UsersRetweetsCreateRequest usersRetweetsCreateRequest = new UsersRetweetsCreateRequest();
usersRetweetsCreateRequest.tweetId(tweetId);

// String | The ID of the user that is requesting to retweet the tweet
String id = "2244994945";
try {
    UsersRetweetsCreateResponse result = apiInstance.tweets().usersIdRetweets(usersRetweetsCreateRequest, id);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling TweetsApi#usersIdRetweets");
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
    "retweeted": true
  }
}
    
```












### Response fields



| Name | Type | Description |
| --- | --- | --- |
| `retweeted` | boolean | Indicates whether the user Retweets the specified Tweet as a result of this request. |



















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















