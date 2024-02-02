



POST /2/users/:id/bookmarks | Docs | Twitter Developer Platform 





































































































POST /2/users/:id/bookmarks



 POST /2/users/:id/bookmarks
===========================

Causes the user ID of an authenticated user identified in the path parameter to Bookmark the target Tweet provided in the request body.

Run in Postman ❯Try a live request ❯Build request with API Explorer ❯### Endpoint URL

`https://api.twitter.com/2/users/:id/bookmarks`  
  
### Authentication and rate limits



|  |  |
| --- | --- |
| Authentication methodssupported by this endpoint | OAuth 2.0 Authorization Code with PKCE |
| Rate limit | User rate limit (User context): 50 requests per 15-minute window per each authenticated user |

### OAuth 2.0 scopes required by this endpoint



|  |
| --- |
| `tweet.read``users.read``bookmark.write` |
| Learn more about OAuth 2.0 Authorization Code with PKCE |

### Path parameters



| Name | Type | Description |
| --- | --- | --- |
| `id` Required  | string | The user ID of an authenticated user who you are bookmarking a Tweet on behalf of. It must match your own user ID or that of an authenticating user, meaning that you must pass the Access Token associated with the user ID when authenticating your request. |

  
  
### JSON body parameters



| Name | Type | Description |
| --- | --- | --- |
| `tweet_id` Required  | string | The ID of the Tweet that you would like an `id` to Bookmark. |

  
  
### Example code with offical SDKs








* TypeScript
* Java


















 TypeScript
 

 Java
 
















```

      (async () => {
  try {
    const postBookmark = await twitterClient.bookmarks.postUsersIdBookmarks(
      //User ID
      "2244994945",
      {
        tweet_id: "1228393702244134912",
      }
    );
    console.dir(postBookmark, {
      depth: null,
    });
  } catch (error) {
    console.log(error);
  }
})();

    
```
















```

      // String | The ID of the user for whom to add bookmarks
String id = "2244994945";

// String | The ID of the tweet that the user is adding to bookmarks
String tweetId = "1228393702244134912";

AddBookmarkRequest addBookmarkRequest = new AddBookmarkRequest(); // AddBookmarkRequest | 
addBookmarkRequest.tweetId(tweetId);

try {
    BookmarkMutationResponse result = apiInstance.bookmarks().postUsersIdBookmarks(addBookmarkRequest, id);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling BookmarksApi#postUsersIdBookmarks");
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
    "bookmarked": true
  }
}
    
```












### Response fields



| Name | Type | Description |
| --- | --- | --- |
| `bookmarked` | boolean | Indicates whether the user bookmarks the specified Tweet as a result of this request. |



















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















