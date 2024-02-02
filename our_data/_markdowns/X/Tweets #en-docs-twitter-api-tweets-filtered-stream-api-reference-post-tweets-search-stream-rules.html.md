
POST /2/tweets/search/stream/rules | Docs | Twitter Developer Platform 

POST /2/tweets/search/stream/rules

 POST /2/tweets/search/stream/rules
==================================
Add or delete rules to your stream.  
Once you've added a rule or rules to your stream, you can retrieve all of the Tweets that match these rules by using the GET /tweets/search/stream endpoint.  
To learn how to build a rule, please read our guide on building a rule.  
To create one or more rules, submit an `add` JSON body with an array of rules and operators. Similarly, to delete one or more rules, submit a `delete` JSON body with an array of list of existing rule IDs.
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
| `delete_all` Optional  | boolean | Set to true to delete all existing rules. |
| `dry_run` Optional  | boolean | Set to true to test the syntax of your rule without submitting it. This is useful if you want to check the syntax of a rule before removing one or more of your existing rules. |

### JSON body parameters

| Name | Type | Description |
| --- | --- | --- |
| `add` Required  | array | Specifies the operation you want to perform on the rules. |
| `add.value` Required  | string | The rule text. You can learn how to build a rule by following our guide on how to build a rule.If you have Essential access, you can use basic operators to build your rule, can add up to 5 rules to your stream concurrently, and each rule can be 512 characters long.If you have Elevated access, you can use basic operators, can add up to 25 rules to your stream, and each rule can be 512 characters longIf you have Academic Research access, you can use all operators, can add up to 1000 rules to your stream, and each rule can be 1024 characters long.To learn more about Twitter API access levels, please visit our about Twitter API page. |
| `delete` Required  | object | Specifies the operation you want to perform on the rules. |
| `delete.ids` Required  | array | Array of rule IDs, each one representing a rule already active in your stream. IDs must be submitted as strings. You can find a rule ID by using the GET /tweets/search/stream/rules endpoint. |
| `add.tag` Optional  | string | The tag label. This is a free-form text you can use to identify the rules that matched a specific Tweet in the streaming response. Tags can be the same across rules.Learn more about tags from our matching returned Tweets guide. |

### Example code with offical SDKs

* TypeScript
* Java

 TypeScript

 Java

```
      (async () => {
  try {
    const addOrDelete = await twitterClient.tweets.addOrDeleteRules(
      {
        add: [
          {
            //The value of the rule text
            value: "cat has:media",
            //A tag meant for the labeling of user provided rules.
            tag: "cats with media",
          },
          {
            value: "cat has:media -grumpy",
            tag: "happy cats with media",
          },
        ],
        //To delete rules comment out the add section and uncomment out the delete code
        /*
        delete: {
          //IDs of all deleted user-specified stream filtering rules.
          ids: ["1165037377523306498", "1165037377523306499"],
        },
        */
      },
      //Optional - Dry Run can be used with both the add and delete action, with the expected result given, but without actually taking any action in the system (meaning the end state will always be as it was when the request was submitted). This is particularly useful to validate rule changes.
      { dry_run: true }
    );
    console.dir(addOrDelete, {
      depth: null,
    });
  } catch (error) {
    console.log(error);
  }
})();

```

```
      // Set the params values
AddOrDeleteRulesRequest addOrDeleteRulesRequest = new AddOrDeleteRulesRequest();

//To delete rule, uncomment out the block of code below
/*
List<String> ids = Arrays.asList("1165037377523306498","1165037377523306499"); // List<String> | IDs of all deleted user-specified stream filtering rules.
DeleteRulesRequest deleteRulesRequest = new DeleteRulesRequest();
DeleteRulesRequestDelete deleteRules = new DeleteRulesRequestDelete();
deleteRules.ids(ids);
deleteRulesRequest.delete(deleteRules);
addOrDeleteRulesRequest.setActualInstance(deleteRulesRequest);
*/
//
AddRulesRequest addRuleRequest = new AddRulesRequest();
RuleNoId newRule = new RuleNoId();
newRule.value("cat has:media");
newRule.tag("cats with media");
addRuleRequest.addAddItem(newRule);
addOrDeleteRulesRequest.setActualInstance(addRuleRequest);
// Boolean | Dry Run can be used with both the add and delete action, with the expected result given, but without actually taking any action in the system (meaning the end state will always be as it was when the request was submitted). This is particularly useful to validate rule changes.
Boolean dryRun = true;
try {
    AddOrDeleteRulesResponse result = apiInstance.tweets().addOrDeleteRules(addOrDeleteRulesRequest, dryRun);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling TweetsApi#addOrDeleteRules");
    System.err.println("Status code: " + e.getCode());
    System.err.println("Reason: " + e.getResponseBody());
    System.err.println("Response headers: " + e.getResponseHeaders());
    e.printStackTrace();
}

```

### Example responses

* Create rules
* Success

 Create rules

 Success

```
      {
  "data": [
    {
      "value": "meme",
      "tag": "funny things",
      "id": "1166895166390583299"
    },
    {
      "value": "cats has:media -grumpy",
      "tag": "happy cats with media",
      "id": "1166895166390583296"
    },
    {
      "value": "cat has:media",
      "tag": "cats with media",
      "id": "1166895166390583297"
    },
    {
      "value": "meme has:images",
      "id": "1166895166390583298"
    }
  ],
  "meta": {
    "sent": "2019-08-29T02:07:42.205Z",
    "summary": {
      "created": 4,
      "not_created": 0
    }
  }
}
```

```
      {
  "meta": {
    "sent": "2019-08-29T01:48:54.633Z",
    "summary": {
      "deleted": 1,
      "not_deleted": 0
    }
  }
}
```

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | string | Unique identifier of this rule. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. |
| `value` | string | The rule text as submitted when creating the rule. |
| `tag` | string | The tag label as defined when creating the rule. |
| `meta` Default  | object | Contains information about when the rule was created, and whether the rule was either created or not created, or deleted or not deleted. |
| `meta.sent` Default  | number | The time when the request body was returned. |
| `meta.summary` Default  | object | Contains fields that describe whether you were successful or unsuccessful in creating or deleting the different rules that you passed in your request. |
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