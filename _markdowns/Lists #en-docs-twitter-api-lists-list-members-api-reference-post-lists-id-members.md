



POST /2/lists/:id/members | Docs | Twitter Developer Platform 





































































































POST /2/lists/:id/members



 POST /2/lists/:id/members
=========================

Enables the authenticated user to add a member to a List they own.

Run in Postman ❯Try a live request ❯Build request with API Explorer ❯### Endpoint URL

`https://api.twitter.com/2/lists/:id/members`  
  
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
| `id` Required  | string | The ID of the List you are adding a member to. |

  
  
### JSON body parameters



| Name | Type | Description |
| --- | --- | --- |
| `user_id` Required  | string | The ID of the user you wish to add as a member of the List. |

  
  
### Example code with offical SDKs








* TypeScript
* Java


















 TypeScript
 

 Java
 
















```

      (async () => {
  try {
    const addMember = await twitterClient.lists.listAddMember(
      //The ID of the user to be added as a member of the List
      2244994945,

      //The ID of the List to add a member
      1441162269824405510
    );
    console.dir(addMember, {
      depth: null,
    });
  } catch (error) {
    console.log(error);
  }
})();

    
```
















```

      // Set the params values

// String | The ID of the user to be added as a member of the List
String usersId = "2244994945"
ListAddMemberRequest listAddMemberRequest = new ListAddMemberRequest();
listAddMemberRequest.userId(usersId);

// String | The ID of the List to add a member
String id = "1441162269824405510";

try {
    ListMemberResponse result = apiInstance.lists().listAddMember(listAddMemberRequest, id);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ListsApi#listAddMember");
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
    "is_member": true
  }
}
    
```












### Response fields



| Name | Type | Description |
| --- | --- | --- |
| `is_member` | boolean | Indicates whether the member specified in the request has been added to the List. |



















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















