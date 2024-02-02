



GET /2/tweets/search/stream/rules | Docs | Twitter Developer Platform 





































































































GET /2/tweets/search/stream/rules



 GET /2/tweets/search/stream/rules
=================================

Return either a single rule, or a list of rules that have been added to the stream.  
  
If you would like to initiate the stream to receive all Tweets that match these rules in real-time, you will need to use the GET /tweets/search/stream endpoint.

Run in Postman ❯Build request with API Explorer ❯### Endpoint URL

`https://api.twitter.com/2/tweets/search/stream/rules`  
  
### Authentication and rate limits



|  |  |
| --- | --- |
| Authentication methodssupported by this endpoint | OAuth 2.0 App-only |
| Rate limit | App rate limit (Application-only): 450 requests per 15-minute window shared among all users of your app |

### Query parameters



| Name | Type | Description |
| --- | --- | --- |
| `ids` Optional  | string | Comma-separated list of rule IDs. If omitted, all rules are returned. |

  
  
### Example code with offical SDKs








* TypeScript
* Java


















 TypeScript
 

 Java
 
















```

      (async () => {
  try {
    const getStreamRules = await twitterClient.tweets.getRules();
    console.dir(getStreamRules, {
      depth: null,
    });
  } catch (error) {
    console.log(error);
  }
})();

    
```
















```

      //Set the (optional) params values

//List<String> | A comma-separated list of Rule IDs.
List<String> ids = Arrays.asList();

//Integer | The maximum number of results
Integer maxResults = 1000;

//String | This value is populated by passing the 'next_token' returned in a request to paginate through results.
String paginationToken = "paginationToken_example";

try {
    GetRulesResponse result = apiInstance.tweets().getRules(ids, maxResults, paginationToken);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling TweetsApi#getRules");
    System.err.println("Status code: " + e.getCode());
    System.err.println("Reason: " + e.getResponseBody());
    System.err.println("Response headers: " + e.getResponseHeaders());
    e.printStackTrace();
}

    
```












### Example responses








* Response


















 Response
 
















```

      {
  "data": [
    {
      "id": "1165037377523306497",
      "value": "dog has:images",
      "tag": "dog pictures"
    },
    {
      "id": "1165037377523306498",
      "value": "cat has:images -grumpy"
    }
  ],
  "meta": {
    "sent": "2019-08-29T01:12:10.729Z"
  }
}
    
```












### Response fields



| Name | Type | Description |
| --- | --- | --- |
| `id` | string | Unique identifier of this rule. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. |
| `value` | string | The rule text as submitted when creating the rule. |
| `tag` | string | The tag label as defined when creating the rule. |
| `meta.sent` | number | The time when the request body was returned. |
| `errors` | object | Contains details about errors that affected any of the requested Tweets. See Status codes and error messages for more details. |



















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















