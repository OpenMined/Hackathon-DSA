
POST /2/lists | Docs | Twitter Developer Platform 

POST /2/lists

 POST /2/lists
=============
Enables the authenticated user to create a List.
Run in Postman ❯Try a live request ❯Build request with API Explorer ❯### Endpoint URL
`https://api.twitter.com/2/lists`  
### Authentication and rate limits

|  |  |
| --- | --- |
| Authentication methodssupported by this endpoint | OAuth 2.0 Authorization Code with PKCEOAuth 1.0a is also available for this endpoint. |
| Rate limit | User rate limit (User context): 300 requests per 15-minute window per each authenticated user |
### OAuth 2.0 scopes required by this endpoint

|  |
| --- |
| `tweet.read``users.read``list.read``list.write` |
| Learn more about OAuth 2.0 Authorization Code with PKCE |
### JSON body parameters

| Name | Type | Description |
| --- | --- | --- |
| `name` Required  | string | The name of the List you wish to create. |
| `description` Optional  | string | Description of the List. |
| `private` Optional  | boolean | Determine whether the List should be private. |

### Example code with offical SDKs

* TypeScript
* Java

 TypeScript

 Java

```
      (async () => {
  try {
    const createList = await twitterClient.lists.listIdCreate({
      name: "test v2 create list",
      description: "example create",
      private: false,
    });
    console.dir(createList, {
      depth: null,
    });
  } catch (error) {
    console.log(error);
  }
})();

```

```
      // Set the params values
ListCreateRequest listCreateRequest = new ListCreateRequest();
listCreateRequest.name("test v2 create list");
listCreateRequest.description("example create");
listCreateRequest._private(false);
try {
    ListCreateResponse result = apiInstance.lists().listIdCreate(listCreateRequest);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ListsApi#listIdCreate");
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
    "id": "1441162269824405510",
    "name": "test v2 create list"
  }
}
```

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | number | The id of the newly created List. |
| `name` | string | The name of the newly created List. |

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