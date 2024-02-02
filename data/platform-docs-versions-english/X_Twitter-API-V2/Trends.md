Introduction

Introduction
------------

The Trends lookup endpoint allow developers to get the Trends for a location, specified using the where-on-earth id (WOEID).

**Note**: WOEID is a legacy identifier created by Yahoo and has been deprecated. X API uses the numeric value to identify town and country trend locations. Reference our legacy [blog post](https://blog.twitter.com/engineering/en_us/a/2010/woeids-in-twitters-trends.html), or [archived data](https://archive.org/details/geoplanet_data_7.10.0.zip0.)

The `tweet_count` for the last 24 hours is also returned for many trends if this is available.

This endpoint supports app-auth authentication and has a rate limit of 75 requests per 15-minute window.

### Getting started

To use this endpoint, you need a [bearer token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only) from the [developer portal](https://developer.twitter.com/en/portal/dashboard). Once you have the bearer token,  you can call the usage API as shown below:

      `curl 'https://api.twitter.com/2/trends/by/woeid/26062' --header 'Authorization: Bearer XXXXX'` 
    

If the request is successful, you should see the JSON response as shown below:

      `{     "data": [         {             "trend_name": "Europe",             "tweet_count": 232408         },         {             "trend_name": "Isak",             "tweet_count": 2956         },         {             "trend_name": "RNLI",             "tweet_count": 2484         },         {             "trend_name": "Toon",             "tweet_count": 11447         },         {             "trend_name": "St James",             "tweet_count": 5565         },         {             "trend_name": "Manning",             "tweet_count": 10077         },         {             "trend_name": "Copenhagen",             "tweet_count": 35272         },         {             "trend_name": "Coventry",             "tweet_count": 3662     ] }`
    

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

### Trends

|     |     |
| --- | --- |
| Trends lookup | [GET /2/trends/by/woeid](https://developer.twitter.com/en/docs/twitter-api/trends/api-reference/get-trends-by-woeid) |

GET /2/trends/by/woeid/:woeid

GET /2/trends/by/woeid/:woeid
=============================

Get the trends for a location

### Endpoint URL

`https://api.twitter.com/2/trends/by/woeid/:woeid`  
  

### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 2.0 App-only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only "Use this method to obtain information in the context of an unauthenticated public user. This method is for developers that just need read-only access to public information. Click to learn how to obtain an OAuth 2.0 App Access Token.") |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | App rate limit (Application-only): 75 requests per 15-minute window shared among all users of your app |

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `woeid`  <br> Required | number | The where-on-earth ID (woeid) for a location |

### Example responses

* [Default Fields](#tab0)

Default Fields

      `{   "data": [     {       "trend_name": "#TEZOSTUESDAY",       "tweet_count": 14869     },     {       "trend_name": "Copenhagen",       "tweet_count": 13005     },     {       "trend_name": "Roses",       "tweet_count": 32193     },     {       "trend_name": "Heroes",       "tweet_count": 69798     },     {       "trend_name": "Cedric",       "tweet_count": 14259     },     {       "trend_name": "#AskSonic",       "tweet_count": 8908     },     {       "trend_name": "Nelson",       "tweet_count": 29841     },     {       "trend_name": "#PSVARS",       "tweet_count": 4915     },     {       "trend_name": "Eddie",       "tweet_count": 34139     },     {       "trend_name": "Saliba",       "tweet_count": 7191     },     {       "trend_name": "Walters",       "tweet_count": 8095     },     {       "trend_name": "Bakayoko",       "tweet_count": 1809     },     {       "trend_name": "Bibby Stockholm",       "tweet_count": 21021     },     {       "trend_name": "Nwaneri",       "tweet_count": 5783     },     {       "trend_name": "Doncaster",       "tweet_count": 3551     },     {       "trend_name": "Kiwior",       "tweet_count": 1535     }   ] }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `trend_name` | string | The name of the Trend. |
| `tweet_count` | integer | The total number of Tweets that are part of this Trend. |