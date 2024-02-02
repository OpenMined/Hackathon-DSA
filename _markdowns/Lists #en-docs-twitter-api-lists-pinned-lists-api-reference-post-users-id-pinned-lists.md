



POST /2/users/:id/pinned\_lists | Docs | Twitter Developer Platform 





































































































POST /2/users/:id/pinned\_lists



 POST /2/users/:id/pinned\_lists
===============================

Enables the authenticated user to pin a List.

Run in Postman ❯Try a live request ❯Build request with API Explorer ❯### Endpoint URL

`https://api.twitter.com/2/users/:id/pinned_lists`  
  
### Authentication and rate limits



|  |  |
| --- | --- |
| Authentication methodssupported by this endpoint | OAuth 1.0a is also available for this endpoint.OAuth 2.0 Authorization Code with PKCE |
| Rate limit | User rate limit (User context): 50 requests per 15-minute window per each authenticated user |

### OAuth 2.0 scopes required by this endpoint



|  |
| --- |
| `tweet.read``users.read``list.write` |
| Learn more about OAuth 2.0 Authorization Code with PKCE |

### Path parameters



| Name | Type | Description |
| --- | --- | --- |
| `id` Required  | string | The user ID who you are pinning a List on behalf of. It must match your own user ID or that of an authenticating user, meaning that you must pass the Access Tokens associated with the user ID when authenticating your request. |

  
  
### JSON body parameters



| Name | Type | Description |
| --- | --- | --- |
| `list_id` Required  | string | The ID of the List that you would like the user `id` to pin. |

  
  
### Example code with offical SDKs








* TypeScript
* Java


















 TypeScript
 

 Java
 
















```

      (async () => {
  try {
    const pinList = await twitterClient.lists.listUserPin(
      //The ID of the authenticated source user that will pin the List
      2244994945,
      
      //The ID of the List to be pinned
      1441162269824405510
    );
    console.dir(pinList, {
      depth: null,
    });
  } catch (error) {
    console.log(error);
  }
})();

    
```
















```

      // Set the params values

// String | The ID of the List to be pinned
String listsId = "1441162269824405510";
ListPinRequest listPinRequest = new ListPinRequest();
listPinRequest.listId(listsId);

// String | The ID of the authenticated source user that will pin the List
String id = "2244994945"; 

try {
    ListPinnedResponse result = apiInstance.lists().listUserPin(listPinRequest, id);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ListsApi#listUserPin");
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
    "pinned": true
  }
}
    
```












### Response fields



| Name | Type | Description |
| --- | --- | --- |
| `pinned` | boolean | Indicates whether the user pinned the specified List as a result of the request. |



















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















