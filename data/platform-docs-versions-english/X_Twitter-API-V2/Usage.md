Introduction

Introduction
------------

The Usage API in the Twitter API v2 allows developers to programmatically retrieve their project usage. Using thie endpoint, developers can keep a track and monitor of the number of Tweets they have pulled for a given billing cycle.

Developers can use the GET endpoint to get the daily project usage for upto the last 90 days. The usage can also be aggregated per client app connected to your peoject.

There is a app rate limit of 50 requests per 15 minutes for this GET endpoint.

### Getting started

To use this endpoint, you need a [bearer token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only) from the [developer portal](https://developer.twitter.com/en/portal/dashboard). Once you have the bearer token,  you can call the usage API as shown below:

      `curl 'https://api.twitter.com/2/usage/tweets' --header 'Authorization: Bearer XXXXX'`
    

If the request is successful, you should see the JSON response as shown below:

      `{     "data": {         "cap_reset_day": 10,         "project_cap": "5000000000",         "project_id": "1369785403853424",         "project_usage": "43435"     } }`
    

**Account setup**

To access these endpoints, you will need:

* An approved [developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info).
* To authenticate using the keys and tokens from a [developer App](https://developer.twitter.com/en/docs/apps) that is located within a [Project](https://developer.twitter.com/en/docs/projects). 

Learn more about getting access to the Twitter API v2 endpoints in our [getting started guide](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api).

[Sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code)

[Run in Postman](https://t.co/twitter-api-postman)

Supporting resources
--------------------

[Learn how to use Postman](https://developer.twitter.com/en/docs/tutorials/postman-getting-started "Learn how to use Postman")

[Troubleshoot an error](https://developer.twitter.com/en/support/twitter-api "Troubleshoot an error")

[API Reference](https://developer.twitter.com/en/docs/twitter-api/tweets/manage-tweets/api-reference "API Reference")

API reference

API reference index
-------------------

### Tweets

|     |     |
| --- | --- |
| Get Tweets Usage | [GET /2/usage/tweets](https://developer.twitter.com/en/docs/twitter-api/usage/tweets/api-reference/get-usage-tweets) |

GET /2/usage/tweets

GET /2/usage/tweets
===================

Get the Tweet usage within the context of a project

### Endpoint URL

`https://api.twitter.com/2/usage/tweets`  
  

### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 2.0 App-only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only "Use this method to obtain information in the context of an unauthenticated public user. This method is for developers that just need read-only access to public information. Click to learn how to obtain an OAuth 2.0 App Access Token.") |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | App rate limit (Application-only): 50 requests per 15-minute window shared among all users of your app |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| `days`  <br> Optional | number | The number of days for which you need the Tweet usage for. You can get usage for upto 90 days. |
| `usage.fields`  <br> Optional | enum (`daily_client_app_usage`, `daily_project_usage`) | This parameter is used to specify if you want the daily usage returned and at a client app level. |

  
  

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript](#tab0)
* [Java](#tab1)

TypeScript

Java

      `(async () => {   try {     const getUsage =       await twitterClient.usage.getUsage();     console.dir(getUsage, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `try {     UsageResponse result = apiInstance.usage().getUsage();     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling UsageApi#getUsage");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

### Example responses

* [Default Fields](#tab0)
* [Optional Fields](#tab1)

Default Fields

Optional Fields

      `{   "data": {     "cap_reset_day": 10,     "project_cap": "2000000",     "project_id": "1281043626347900822499",     "project_usage": "2007"   } }`
    

      `{   "data": {     "daily_client_app_usage": [       {         "usage": [           {             "date": "2023-11-01T00:00:00.000Z",             "usage": "200"           }         ],         "client_app_id": "101111140",         "usage_result_count": 1       }     ],     "project_cap": "2000000",     "daily_project_usage": {       "project_id": "1281043626347900822499",       "usage": [         {           "date": "2023-11-01T00:00:00.000Z",           "usage": "200"         }       ]     },     "project_usage": "200",     "cap_reset_day": 5,     "project_id": "1281043626347900822499"   } }`
    

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