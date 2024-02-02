



DELETE /2/lists/:id/members/:user\_id | Docs | Twitter Developer Platform 





































































































DELETE /2/lists/:id/members/:user\_id



 DELETE /2/lists/:id/members/:user\_id
=====================================

Enables the authenticated user to remove a member from a List they own.

Run in Postman ❯Try a live request ❯Build request with API Explorer ❯### Endpoint URL

`https://api.twitter.com/2/lists/:id/members/:user_id`  
  
### Authentication and rate limits



|  |  |
| --- | --- |
| Authentication methodssupported by this endpoint | OAuth 1.0a is also available for this endpoint.OAuth 2.0 Authorization Code with PKCE |
| Rate limit | User rate limit (User context): 300 requests per 15-minute window per each authenticated user |

### OAuth 2.0 scopes required by this endpoint



|  |
| --- |
| `tweet.read``users.read``list.write` |
| Learn more about OAuth 2.0 Authorization Code with PKCE |

### Path parameters



| Name | Type | Description |
| --- | --- | --- |
| `id` Required  | string | The ID of the List you are removing a member from. |
| `user_id` Required  | string | The ID of the user you wish to remove as a member of the List. |

  
  
### Example code with offical SDKs








* TypeScript
* Java


















 TypeScript
 

 Java
 
















```

      (async () => {
  try {
    const removeMember = await twitterClient.lists.listRemoveMember(
      //The ID of the List to remove a member
      1441162269824405510,

      //The ID of user that will be removed from the List
      2244994945
    );
    console.dir(removeMember, {
      depth: null,
    });
  } catch (error) {
    console.log(error);
  }
})();

    
```
















```

      // Set the params values

// String |The ID of the List to remove a member
String id = "1441162269824405510"; 

// String | The ID of user that will be removed from the List
String userId = "2244994945";
try {
    ListMemberResponse result = apiInstance.lists().listRemoveMember(id, userId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ListsApi#listRemoveMember");
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
    "is_member": false
  }
}
    
```












### Response fields



| Name | Type | Description |
| --- | --- | --- |
| `is_member` | boolean | Indicates whether the member specified in the request has been removed from the List. |



















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















