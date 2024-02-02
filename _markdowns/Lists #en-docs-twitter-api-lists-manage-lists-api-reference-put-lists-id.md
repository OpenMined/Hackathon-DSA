



PUT /2/lists/:id | Docs | Twitter Developer Platform 





































































































PUT /2/lists/:id



 PUT /2/lists/:id
================

Enables the authenticated user to update the meta data of a specified List that they own.

Run in Postman ❯Try a live request ❯Build request with API Explorer ❯### Endpoint URL

`https://api.twitter.com/2/lists/:id`  
  
### Authentication and rate limits



|  |  |
| --- | --- |
| Authentication methodssupported by this endpoint | OAuth 2.0 Authorization Code with PKCEOAuth 1.0a is also available for this endpoint. |
| Rate limit | User rate limit (User context): 300 requests per 15-minute window per each authenticated user |

### OAuth 2.0 scopes required by this endpoint



|  |
| --- |
| `tweet.read``users.read``list.write` |
| Learn more about OAuth 2.0 Authorization Code with PKCE |

### Path parameters



| Name | Type | Description |
| --- | --- | --- |
| `id` Required  | string | The ID of the List to be updated. |

  
  
### JSON body parameters



| Name | Type | Description |
| --- | --- | --- |
| `description` Optional  | string | Updates the description of the List. |
| `name` Optional  | string | Updates the name of the List. |
| `private` Optional  | boolean | Determines whether the List should be private. |

  
  
### Example code with offical SDKs








* TypeScript
* Java


















 TypeScript
 

 Java
 
















```

      (async () => {
  try {
    const updateList = await twitterClient.lists.listIdUpdate(
      //The ID of the List to modify
      1441163524802158595,
      {
        name: "test v2 create list",
        description: "example code",
        private: false,
      }
    );
    console.dir(updateList, {
      depth: null,
    });
  } catch (error) {
    console.log(error);
  }
})();

    
```
















```

      // Set the params values

ListUpdateRequest listUpdateRequest = new ListUpdateRequest();
listUpdateRequest.name("test v2 update list");
listUpdateRequest.description("example update");
listUpdateRequest.private(false);

// String | The ID of the List to modify
String id = "1441163524802158595";

try {
    ListUpdateResponse result = apiInstance.lists().listIdUpdate(listUpdateRequest, id);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ListsApi#listIdUpdate");
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
    "updated": true
  }
}
    
```












### Response fields



| Name | Type | Description |
| --- | --- | --- |
| `updated` | boolean | Indicates whether the List specified in the request has been updated. |



















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















