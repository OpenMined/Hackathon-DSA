
GET /2/usage/tweets | Docs | Twitter Developer Platform 

GET /2/usage/tweets

 GET /2/usage/tweets
===================
Get the Tweet usage within the context of a project
### Endpoint URL
`https://api.twitter.com/2/usage/tweets`  
### Authentication and rate limits

|  |  |
| --- | --- |
| Authentication methodssupported by this endpoint | OAuth 2.0 App-only |
| Rate limit | App rate limit (Application-only): 50 requests per 15-minute window shared among all users of your app |
### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| `days` Optional  | number | The number of days for which you need the Tweet usage for. You can get usage for upto 90 days. |
| `usage.fields` Optional  | enum (`daily_client_app_usage`, `daily_project_usage`) | This parameter is used to specify if you want the daily usage returned and at a client app level. |

### Example code with offical SDKs

* TypeScript
* Java

 TypeScript

 Java

```
      (async () => {
  try {
    const getUsage =
      await twitterClient.usage.getUsage();
    console.dir(getUsage, {
      depth: null,
    });
  } catch (error) {
    console.log(error);
  }
})();

```

```
      try {
    UsageResponse result = apiInstance.usage().getUsage();
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling UsageApi#getUsage");
    System.err.println("Status code: " + e.getCode());
    System.err.println("Reason: " + e.getResponseBody());
    System.err.println("Response headers: " + e.getResponseHeaders());
    e.printStackTrace();
}

```

### Example responses

* Default Fields
* Optional Fields

 Default Fields

 Optional Fields

```
      {
  "data": {
    "cap_reset_day": 10,
    "project_cap": "2000000",
    "project_id": "1281043626347900822499",
    "project_usage": "2007"
  }
}
```

```
      {
  "data": {
    "daily_client_app_usage": [
      {
        "usage": [
          {
            "date": "2023-11-01T00:00:00.000Z",
            "usage": "200"
          }
        ],
        "client_app_id": "101111140",
        "usage_result_count": 1
      }
    ],
    "project_cap": "2000000",
    "daily_project_usage": {
      "project_id": "1281043626347900822499",
      "usage": [
        {
          "date": "2023-11-01T00:00:00.000Z",
          "usage": "200"
        }
      ]
    },
    "project_usage": "200",
    "cap_reset_day": 5,
    "project_id": "1281043626347900822499"
  }
}
```

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `project_id` | string | The unique identifier for this project. |
| `project_cap` | string | The total number of Tweets that can be read with this project per month. |
| `project_usage` | string | The total number of Tweets that have been read with this project in the current billing cycle. |
| `cap_reset_day` | integer | The day of the month when the Tweet cap is reset. |
| `daily_project_usage` | object | This object and its fields contain daily usage breakdown for a project. |
| `daily_project_usage.project_id` | string | The unique identifier for this project. |
| `daily_project_usage.usage` | array | This array contains the usage information. |
| `daily_project_usage.usage.date` | date (ISO 8601) | The date for which the usage is returned. |
| `daily_project_usage.usage.usage` | string | The project usage for a day. |
| `daily_client_app_usage` | array | This object and its fields contain daily usage breakdown per client app. |
| `daily_client_app_usage.usage` | array | This array contains the usage information. |
| `daily_client_app_usage.usage.date` | date (ISO 8601) | The date for which the usage is returned. |
| `daily_client_app_usage.usage.usage` | string | The project usage for a day. |

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