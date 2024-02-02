
GET /2/tweets/counts/all | Docs | Twitter Developer Platform 

GET /2/tweets/counts/all

 GET /2/tweets/counts/all
========================
This endpoint is only available to those users who have been approved for Academic Research access.  
The full-archive Tweet counts endpoint returns the count of Tweets that match your query from the complete history of public Tweets; since the first Tweet was created March 26, 2006.
Run in Postman ❯Build request with API Explorer ❯### Endpoint URL
`https://api.twitter.com/2/tweets/counts/all`  
### Authentication and rate limits

|  |  |
| --- | --- |
| Authentication methodssupported by this endpoint | OAuth 2.0 App-only |
| Rate limit | App rate limit (Application-only): 300 requests per 15-minute window shared among all users of your app |
### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| `query` Required  | string | One query for matching Tweets. You can learn how to build this query by reading our build a query guide.You can use all available operators and can make queries up to 1,024 characters long. |
| `end_time` Optional  | date (ISO 8601) | YYYY-MM-DDTHH:mm:ssZ (ISO 8601/RFC 3339). Used with `start_time`. The newest, most recent UTC timestamp to which the Tweets will be provided. Timestamp is in second granularity and is exclusive (for example, 12:00:01 excludes the first second of the minute). If used without `start_time`, Tweets from 30 days before `end_time` will be returned by default. If not specified, `end_time` will default to [now - 30 seconds]. |
| `granularity` Optional  | string | This is the granularity that you want the timeseries count data to be grouped by. You can requeset `minute`, `hour`, or `day` granularity. The default granularity, if not specified is `hour`. |
| `next_token` Optional  | string | This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, assuming that your request contains more than 31 days-worth of results, and should not be modified. You can learn more by visiting our page on pagination. |
| `since_id` Optional  | string | Returns results with a Tweet ID greater than (for example, more recent than) the specified ID. The ID specified is exclusive and responses will not include it. If included with the same request as a `start_time` parameter, only `since_id` will be used. |
| `start_time` Optional  | date (ISO 8601) | YYYY-MM-DDTHH:mm:ssZ (ISO 8601/RFC 3339). The oldest UTC timestamp from which the Tweets will be provided. Timestamp is in second granularity and is inclusive (for example, 12:00:01 includes the first second of the minute). By default, a request will return Tweets from up to 30 days ago if you do not include this parameter. |
| `until_id` Optional  | string | Returns results with a Tweet ID less than (that is, older than) the specified ID. Used with `since_id`. The ID specified is exclusive and responses will not include it. |

### Example code with offical SDKs

* TypeScript (Default fields)
* TypeScript (Optional fields)
* Java (Default fields)
* Java (Optional fields)

 TypeScript (Default fields)

 TypeScript (Optional fields)

 Java (Default fields)

 Java (Optional fields)

```
      (async () => {
  try {
    const getTweetCountsAll =
      await twitterClient.tweets.tweetCountsFullArchiveSearch({
        //One query/rule/filter for matching Tweets. Refer to https://t.co/rulelength to identify the max query length
        query: "lakers",
      });
    console.dir(getTweetCountsAll, {
      depth: null,
    });
  } catch (error) {
    console.log(error);
  }
})();

```

```
      (async () => {
    try {
      const getTweetCountsAll =
        await twitterClient.tweets.tweetCountsFullArchiveSearch({
          //One query/rule/filter for matching Tweets. Refer to https://t.co/rulelength to identify the max query length
          query: "lakers",
          //YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp from which the Tweets will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute).
          start_time: "2021-01-01T00:00:00.000Z",
          //YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Tweets will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute).
          end_time: "2021-01-15T00:00:00.000Z",
          //Granularity | The granularity for the search counts results.
          granularity: "day",
        });
      console.dir(getTweetCountsAll, {
        depth: null,
      });
    } catch (error) {
      console.log(error);
    }
  })();

```

```
      //Set the params values
//String | One query/rule/filter for matching Tweets. Refer to https://t.co/rulelength to identify the max query length
String query = "lakers";
try {
    TweetCountsResponse result = apiInstance.tweets().tweetCountsFullArchiveSearch(query, null, null, null, null, null, null, granularity);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling TweetsApi#tweetCountsFullArchiveSearch");
    System.err.println("Status code: " + e.getCode());
    System.err.println("Reason: " + e.getResponseBody());
    System.err.println("Response headers: " + e.getResponseHeaders());
    e.printStackTrace();
}

```

```
      // Set the params values
// For full list of params visit - https://github.com/twitterdev/twitter-api-java-sdk/blob/main/docs/TweetsApi.md#tweetCountsFullArchiveSearch
//String | One query/rule/filter for matching Tweets. Refer to https://t.co/rulelength to identify the max query length
String query = "lakers";
//OffsetDateTime | YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp from which the Tweets will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute).
OffsetDateTime startTime = OffsetDateTime.parse("2021-01-01T00:00:00.000Z");
//OffsetDateTime | YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Tweets will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute).
OffsetDateTime endTime = OffsetDateTime.parse("2021-01-15T00:00:00.000Z");
//Granularity | The granularity for the search counts results.
Granularity granularity = Granularity.fromValue("day");
try {
    TweetCountsResponse result = apiInstance.tweets().tweetCountsFullArchiveSearch(query, startTime, endTime, null, null, null, null, granularity);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling TweetsApi#tweetCountsFullArchiveSearch");
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
  "data": [
    {
      "end": "2021-05-27T00:00:00.000Z",
      "start": "2021-05-26T23:00:00.000Z",
      "tweet_count": 345
    },
    {
      "end": "2021-05-27T01:00:00.000Z",
      "start": "2021-05-27T00:00:00.000Z",
      "tweet_count": 2183
    },
    {
      "end": "2021-05-27T02:00:00.000Z",
      "start": "2021-05-27T01:00:00.000Z",
      "tweet_count": 2168
    },
    {
      "end": "2021-05-27T03:00:00.000Z",
      "start": "2021-05-27T02:00:00.000Z",
      "tweet_count": 1973
    },
    {
      "end": "2021-05-27T04:00:00.000Z",
      "start": "2021-05-27T03:00:00.000Z",
      "tweet_count": 1575
    },
    {
      "end": "2021-05-27T05:00:00.000Z",
      "start": "2021-05-27T04:00:00.000Z",
      "tweet_count": 1348
    },
    {
      "end": "2021-05-27T06:00:00.000Z",
      "start": "2021-05-27T05:00:00.000Z",
      "tweet_count": 1086
    },
    {
      "end": "2021-05-27T07:00:00.000Z",
      "start": "2021-05-27T06:00:00.000Z",
      "tweet_count": 746
    },
    {
      "end": "2021-05-27T08:00:00.000Z",
      "start": "2021-05-27T07:00:00.000Z",
      "tweet_count": 627
    },
    {
      "end": "2021-05-27T09:00:00.000Z",
      "start": "2021-05-27T08:00:00.000Z",
      "tweet_count": 611
    },
    {
      "end": "2021-05-27T10:00:00.000Z",
      "start": "2021-05-27T09:00:00.000Z",
      "tweet_count": 502
    },
    {
      "end": "2021-05-27T11:00:00.000Z",
      "start": "2021-05-27T10:00:00.000Z",
      "tweet_count": 570
    },
    {
      "end": "2021-05-27T12:00:00.000Z",
      "start": "2021-05-27T11:00:00.000Z",
      "tweet_count": 637
    },
    {
      "end": "2021-05-27T13:00:00.000Z",
      "start": "2021-05-27T12:00:00.000Z",
      "tweet_count": 787
    },
    {
      "end": "2021-05-27T14:00:00.000Z",
      "start": "2021-05-27T13:00:00.000Z",
      "tweet_count": 1278
    },
    {
      "end": "2021-05-27T15:00:00.000Z",
      "start": "2021-05-27T14:00:00.000Z",
      "tweet_count": 1442
    },
    {
      "end": "2021-05-27T16:00:00.000Z",
      "start": "2021-05-27T15:00:00.000Z",
      "tweet_count": 3056
    },
    {
      "end": "2021-05-27T17:00:00.000Z",
      "start": "2021-05-27T16:00:00.000Z",
      "tweet_count": 2393
    },
    {
      "end": "2021-05-27T18:00:00.000Z",
      "start": "2021-05-27T17:00:00.000Z",
      "tweet_count": 3226
    },
    {
      "end": "2021-05-27T19:00:00.000Z",
      "start": "2021-05-27T18:00:00.000Z",
      "tweet_count": 3514
    },
    {
      "end": "2021-05-27T20:00:00.000Z",
      "start": "2021-05-27T19:00:00.000Z",
      "tweet_count": 2750
    },
    {
      "end": "2021-05-27T21:00:00.000Z",
      "start": "2021-05-27T20:00:00.000Z",
      "tweet_count": 2452
    },
    {
      "end": "2021-05-27T22:00:00.000Z",
      "start": "2021-05-27T21:00:00.000Z",
      "tweet_count": 2646
    },
    {
      "end": "2021-05-27T23:00:00.000Z",
      "start": "2021-05-27T22:00:00.000Z",
      "tweet_count": 2475
    },
    {
      "end": "2021-05-28T00:00:00.000Z",
      "start": "2021-05-27T23:00:00.000Z",
      "tweet_count": 3082
    },
    {
      "end": "2021-05-28T01:00:00.000Z",
      "start": "2021-05-28T00:00:00.000Z",
      "tweet_count": 3003
    },
    {
      "end": "2021-05-28T02:00:00.000Z",
      "start": "2021-05-28T01:00:00.000Z",
      "tweet_count": 5866
    },
    {
      "end": "2021-05-28T03:00:00.000Z",
      "start": "2021-05-28T02:00:00.000Z",
      "tweet_count": 15463
    },
    {
      "end": "2021-05-28T04:00:00.000Z",
      "start": "2021-05-28T03:00:00.000Z",
      "tweet_count": 19577
    },
    {
      "end": "2021-05-28T05:00:00.000Z",
      "start": "2021-05-28T04:00:00.000Z",
      "tweet_count": 49621
    },
    {
      "end": "2021-05-28T06:00:00.000Z",
      "start": "2021-05-28T05:00:00.000Z",
      "tweet_count": 20826
    },
    {
      "end": "2021-05-28T07:00:00.000Z",
      "start": "2021-05-28T06:00:00.000Z",
      "tweet_count": 7951
    },
    {
      "end": "2021-05-28T08:00:00.000Z",
      "start": "2021-05-28T07:00:00.000Z",
      "tweet_count": 4791
    },
    {
      "end": "2021-05-28T09:00:00.000Z",
      "start": "2021-05-28T08:00:00.000Z",
      "tweet_count": 2965
    },
    {
      "end": "2021-05-28T10:00:00.000Z",
      "start": "2021-05-28T09:00:00.000Z",
      "tweet_count": 2481
    },
    {
      "end": "2021-05-28T11:00:00.000Z",
      "start": "2021-05-28T10:00:00.000Z",
      "tweet_count": 2721
    },
    {
      "end": "2021-05-28T12:00:00.000Z",
      "start": "2021-05-28T11:00:00.000Z",
      "tweet_count": 3140
    },
    {
      "end": "2021-05-28T13:00:00.000Z",
      "start": "2021-05-28T12:00:00.000Z",
      "tweet_count": 3742
    },
    {
      "end": "2021-05-28T14:00:00.000Z",
      "start": "2021-05-28T13:00:00.000Z",
      "tweet_count": 3978
    },
    {
      "end": "2021-05-28T15:00:00.000Z",
      "start": "2021-05-28T14:00:00.000Z",
      "tweet_count": 4028
    },
    {
      "end": "2021-05-28T16:00:00.000Z",
      "start": "2021-05-28T15:00:00.000Z",
      "tweet_count": 3758
    },
    {
      "end": "2021-05-28T17:00:00.000Z",
      "start": "2021-05-28T16:00:00.000Z",
      "tweet_count": 4207
    },
    {
      "end": "2021-05-28T18:00:00.000Z",
      "start": "2021-05-28T17:00:00.000Z",
      "tweet_count": 3932
    },
    {
      "end": "2021-05-28T19:00:00.000Z",
      "start": "2021-05-28T18:00:00.000Z",
      "tweet_count": 3340
    },
    {
      "end": "2021-05-28T20:00:00.000Z",
      "start": "2021-05-28T19:00:00.000Z",
      "tweet_count": 3306
    },
    {
      "end": "2021-05-28T21:00:00.000Z",
      "start": "2021-05-28T20:00:00.000Z",
      "tweet_count": 3244
    },
    {
      "end": "2021-05-28T22:00:00.000Z",
      "start": "2021-05-28T21:00:00.000Z",
      "tweet_count": 2416
    },
    {
      "end": "2021-05-28T23:00:00.000Z",
      "start": "2021-05-28T22:00:00.000Z",
      "tweet_count": 2184
    },
    {
      "end": "2021-05-29T00:00:00.000Z",
      "start": "2021-05-28T23:00:00.000Z",
      "tweet_count": 2383
    },
    {
      "end": "2021-05-29T01:00:00.000Z",
      "start": "2021-05-29T00:00:00.000Z",
      "tweet_count": 2171
    },
    {
      "end": "2021-05-29T02:00:00.000Z",
      "start": "2021-05-29T01:00:00.000Z",
      "tweet_count": 2431
    },
    {
      "end": "2021-05-29T03:00:00.000Z",
      "start": "2021-05-29T02:00:00.000Z",
      "tweet_count": 3092
    },
    {
      "end": "2021-05-29T04:00:00.000Z",
      "start": "2021-05-29T03:00:00.000Z",
      "tweet_count": 2278
    },
    {
      "end": "2021-05-29T05:00:00.000Z",
      "start": "2021-05-29T04:00:00.000Z",
      "tweet_count": 1760
    },
    {
      "end": "2021-05-29T06:00:00.000Z",
      "start": "2021-05-29T05:00:00.000Z",
      "tweet_count": 1075
    },
    {
      "end": "2021-05-29T07:00:00.000Z",
      "start": "2021-05-29T06:00:00.000Z",
      "tweet_count": 793
    },
    {
      "end": "2021-05-29T08:00:00.000Z",
      "start": "2021-05-29T07:00:00.000Z",
      "tweet_count": 747
    },
    {
      "end": "2021-05-29T09:00:00.000Z",
      "start": "2021-05-29T08:00:00.000Z",
      "tweet_count": 601
    },
    {
      "end": "2021-05-29T10:00:00.000Z",
      "start": "2021-05-29T09:00:00.000Z",
      "tweet_count": 494
    },
    {
      "end": "2021-05-29T11:00:00.000Z",
      "start": "2021-05-29T10:00:00.000Z",
      "tweet_count": 582
    },
    {
      "end": "2021-05-29T12:00:00.000Z",
      "start": "2021-05-29T11:00:00.000Z",
      "tweet_count": 473
    },
    {
      "end": "2021-05-29T13:00:00.000Z",
      "start": "2021-05-29T12:00:00.000Z",
      "tweet_count": 610
    },
    {
      "end": "2021-05-29T14:00:00.000Z",
      "start": "2021-05-29T13:00:00.000Z",
      "tweet_count": 828
    },
    {
      "end": "2021-05-29T15:00:00.000Z",
      "start": "2021-05-29T14:00:00.000Z",
      "tweet_count": 912
    },
    {
      "end": "2021-05-29T16:00:00.000Z",
      "start": "2021-05-29T15:00:00.000Z",
      "tweet_count": 1026
    },
    {
      "end": "2021-05-29T17:00:00.000Z",
      "start": "2021-05-29T16:00:00.000Z",
      "tweet_count": 1466
    },
    {
      "end": "2021-05-29T18:00:00.000Z",
      "start": "2021-05-29T17:00:00.000Z",
      "tweet_count": 1373
    },
    {
      "end": "2021-05-29T19:00:00.000Z",
      "start": "2021-05-29T18:00:00.000Z",
      "tweet_count": 1093
    },
    {
      "end": "2021-05-29T20:00:00.000Z",
      "start": "2021-05-29T19:00:00.000Z",
      "tweet_count": 1525
    },
    {
      "end": "2021-05-29T21:00:00.000Z",
      "start": "2021-05-29T20:00:00.000Z",
      "tweet_count": 2513
    },
    {
      "end": "2021-05-29T22:00:00.000Z",
      "start": "2021-05-29T21:00:00.000Z",
      "tweet_count": 2602
    },
    {
      "end": "2021-05-29T23:00:00.000Z",
      "start": "2021-05-29T22:00:00.000Z",
      "tweet_count": 3211
    },
    {
      "end": "2021-05-30T00:00:00.000Z",
      "start": "2021-05-29T23:00:00.000Z",
      "tweet_count": 2066
    },
    {
      "end": "2021-05-30T01:00:00.000Z",
      "start": "2021-05-30T00:00:00.000Z",
      "tweet_count": 2272
    },
    {
      "end": "2021-05-30T02:00:00.000Z",
      "start": "2021-05-30T01:00:00.000Z",
      "tweet_count": 1851
    },
    {
      "end": "2021-05-30T03:00:00.000Z",
      "start": "2021-05-30T02:00:00.000Z",
      "tweet_count": 1705
    },
    {
      "end": "2021-05-30T04:00:00.000Z",
      "start": "2021-05-30T03:00:00.000Z",
      "tweet_count": 1543
    },
    {
      "end": "2021-05-30T05:00:00.000Z",
      "start": "2021-05-30T04:00:00.000Z",
      "tweet_count": 1446
    },
    {
      "end": "2021-05-30T06:00:00.000Z",
      "start": "2021-05-30T05:00:00.000Z",
      "tweet_count": 1106
    },
    {
      "end": "2021-05-30T07:00:00.000Z",
      "start": "2021-05-30T06:00:00.000Z",
      "tweet_count": 905
    },
    {
      "end": "2021-05-30T08:00:00.000Z",
      "start": "2021-05-30T07:00:00.000Z",
      "tweet_count": 806
    },
    {
      "end": "2021-05-30T09:00:00.000Z",
      "start": "2021-05-30T08:00:00.000Z",
      "tweet_count": 720
    },
    {
      "end": "2021-05-30T10:00:00.000Z",
      "start": "2021-05-30T09:00:00.000Z",
      "tweet_count": 563
    },
    {
      "end": "2021-05-30T11:00:00.000Z",
      "start": "2021-05-30T10:00:00.000Z",
      "tweet_count": 573
    },
    {
      "end": "2021-05-30T12:00:00.000Z",
      "start": "2021-05-30T11:00:00.000Z",
      "tweet_count": 668
    },
    {
      "end": "2021-05-30T13:00:00.000Z",
      "start": "2021-05-30T12:00:00.000Z",
      "tweet_count": 791
    },
    {
      "end": "2021-05-30T14:00:00.000Z",
      "start": "2021-05-30T13:00:00.000Z",
      "tweet_count": 1220
    },
    {
      "end": "2021-05-30T15:00:00.000Z",
      "start": "2021-05-30T14:00:00.000Z",
      "tweet_count": 1606
    },
    {
      "end": "2021-05-30T16:00:00.000Z",
      "start": "2021-05-30T15:00:00.000Z",
      "tweet_count": 1989
    },
    {
      "end": "2021-05-30T17:00:00.000Z",
      "start": "2021-05-30T16:00:00.000Z",
      "tweet_count": 3046
    },
    {
      "end": "2021-05-30T18:00:00.000Z",
      "start": "2021-05-30T17:00:00.000Z",
      "tweet_count": 3598
    },
    {
      "end": "2021-05-30T19:00:00.000Z",
      "start": "2021-05-30T18:00:00.000Z",
      "tweet_count": 4293
    },
    {
      "end": "2021-05-30T20:00:00.000Z",
      "start": "2021-05-30T19:00:00.000Z",
      "tweet_count": 10505
    },
    {
      "end": "2021-05-30T21:00:00.000Z",
      "start": "2021-05-30T20:00:00.000Z",
      "tweet_count": 16604
    },
    {
      "end": "2021-05-30T22:00:00.000Z",
      "start": "2021-05-30T21:00:00.000Z",
      "tweet_count": 32739
    },
    {
      "end": "2021-05-30T23:00:00.000Z",
      "start": "2021-05-30T22:00:00.000Z",
      "tweet_count": 19473
    },
    {
      "end": "2021-05-31T00:00:00.000Z",
      "start": "2021-05-30T23:00:00.000Z",
      "tweet_count": 6223
    },
    {
      "end": "2021-05-31T01:00:00.000Z",
      "start": "2021-05-31T00:00:00.000Z",
      "tweet_count": 6010
    },
    {
      "end": "2021-05-31T02:00:00.000Z",
      "start": "2021-05-31T01:00:00.000Z",
      "tweet_count": 4243
    },
    {
      "end": "2021-05-31T03:00:00.000Z",
      "start": "2021-05-31T02:00:00.000Z",
      "tweet_count": 3389
    },
    {
      "end": "2021-05-31T04:00:00.000Z",
      "start": "2021-05-31T03:00:00.000Z",
      "tweet_count": 2969
    },
    {
      "end": "2021-05-31T05:00:00.000Z",
      "start": "2021-05-31T04:00:00.000Z",
      "tweet_count": 2406
    },
    {
      "end": "2021-05-31T06:00:00.000Z",
      "start": "2021-05-31T05:00:00.000Z",
      "tweet_count": 1796
    },
    {
      "end": "2021-05-31T07:00:00.000Z",
      "start": "2021-05-31T06:00:00.000Z",
      "tweet_count": 1504
    },
    {
      "end": "2021-05-31T08:00:00.000Z",
      "start": "2021-05-31T07:00:00.000Z",
      "tweet_count": 1309
    },
    {
      "end": "2021-05-31T09:00:00.000Z",
      "start": "2021-05-31T08:00:00.000Z",
      "tweet_count": 1018
    },
    {
      "end": "2021-05-31T10:00:00.000Z",
      "start": "2021-05-31T09:00:00.000Z",
      "tweet_count": 842
    },
    {
      "end": "2021-05-31T11:00:00.000Z",
      "start": "2021-05-31T10:00:00.000Z",
      "tweet_count": 1022
    },
    {
      "end": "2021-05-31T12:00:00.000Z",
      "start": "2021-05-31T11:00:00.000Z",
      "tweet_count": 960
    },
    {
      "end": "2021-05-31T13:00:00.000Z",
      "start": "2021-05-31T12:00:00.000Z",
      "tweet_count": 1143
    },
    {
      "end": "2021-05-31T14:00:00.000Z",
      "start": "2021-05-31T13:00:00.000Z",
      "tweet_count": 1471
    },
    {
      "end": "2021-05-31T15:00:00.000Z",
      "start": "2021-05-31T14:00:00.000Z",
      "tweet_count": 1539
    },
    {
      "end": "2021-05-31T16:00:00.000Z",
      "start": "2021-05-31T15:00:00.000Z",
      "tweet_count": 1713
    },
    {
      "end": "2021-05-31T17:00:00.000Z",
      "start": "2021-05-31T16:00:00.000Z",
      "tweet_count": 2215
    },
    {
      "end": "2021-05-31T18:00:00.000Z",
      "start": "2021-05-31T17:00:00.000Z",
      "tweet_count": 3552
    },
    {
      "end": "2021-05-31T19:00:00.000Z",
      "start": "2021-05-31T18:00:00.000Z",
      "tweet_count": 2404
    },
    {
      "end": "2021-05-31T20:00:00.000Z",
      "start": "2021-05-31T19:00:00.000Z",
      "tweet_count": 1939
    },
    {
      "end": "2021-05-31T21:00:00.000Z",
      "start": "2021-05-31T20:00:00.000Z",
      "tweet_count": 1983
    },
    {
      "end": "2021-05-31T22:00:00.000Z",
      "start": "2021-05-31T21:00:00.000Z",
      "tweet_count": 1964
    },
    {
      "end": "2021-05-31T23:00:00.000Z",
      "start": "2021-05-31T22:00:00.000Z",
      "tweet_count": 1650
    },
    {
      "end": "2021-06-01T00:00:00.000Z",
      "start": "2021-05-31T23:00:00.000Z",
      "tweet_count": 1683
    },
    {
      "end": "2021-06-01T01:00:00.000Z",
      "start": "2021-06-01T00:00:00.000Z",
      "tweet_count": 1347
    },
    {
      "end": "2021-06-01T02:00:00.000Z",
      "start": "2021-06-01T01:00:00.000Z",
      "tweet_count": 1179
    },
    {
      "end": "2021-06-01T03:00:00.000Z",
      "start": "2021-06-01T02:00:00.000Z",
      "tweet_count": 1192
    },
    {
      "end": "2021-06-01T04:00:00.000Z",
      "start": "2021-06-01T03:00:00.000Z",
      "tweet_count": 960
    },
    {
      "end": "2021-06-01T05:00:00.000Z",
      "start": "2021-06-01T04:00:00.000Z",
      "tweet_count": 1264
    },
    {
      "end": "2021-06-01T06:00:00.000Z",
      "start": "2021-06-01T05:00:00.000Z",
      "tweet_count": 762
    },
    {
      "end": "2021-06-01T07:00:00.000Z",
      "start": "2021-06-01T06:00:00.000Z",
      "tweet_count": 548
    },
    {
      "end": "2021-06-01T08:00:00.000Z",
      "start": "2021-06-01T07:00:00.000Z",
      "tweet_count": 458
    },
    {
      "end": "2021-06-01T09:00:00.000Z",
      "start": "2021-06-01T08:00:00.000Z",
      "tweet_count": 407
    },
    {
      "end": "2021-06-01T10:00:00.000Z",
      "start": "2021-06-01T09:00:00.000Z",
      "tweet_count": 334
    },
    {
      "end": "2021-06-01T11:00:00.000Z",
      "start": "2021-06-01T10:00:00.000Z",
      "tweet_count": 391
    },
    {
      "end": "2021-06-01T12:00:00.000Z",
      "start": "2021-06-01T11:00:00.000Z",
      "tweet_count": 557
    },
    {
      "end": "2021-06-01T13:00:00.000Z",
      "start": "2021-06-01T12:00:00.000Z",
      "tweet_count": 726
    },
    {
      "end": "2021-06-01T14:00:00.000Z",
      "start": "2021-06-01T13:00:00.000Z",
      "tweet_count": 1230
    },
    {
      "end": "2021-06-01T15:00:00.000Z",
      "start": "2021-06-01T14:00:00.000Z",
      "tweet_count": 1546
    },
    {
      "end": "2021-06-01T16:00:00.000Z",
      "start": "2021-06-01T15:00:00.000Z",
      "tweet_count": 1705
    },
    {
      "end": "2021-06-01T17:00:00.000Z",
      "start": "2021-06-01T16:00:00.000Z",
      "tweet_count": 2163
    },
    {
      "end": "2021-06-01T18:00:00.000Z",
      "start": "2021-06-01T17:00:00.000Z",
      "tweet_count": 2388
    },
    {
      "end": "2021-06-01T19:00:00.000Z",
      "start": "2021-06-01T18:00:00.000Z",
      "tweet_count": 2433
    },
    {
      "end": "2021-06-01T20:00:00.000Z",
      "start": "2021-06-01T19:00:00.000Z",
      "tweet_count": 2832
    },
    {
      "end": "2021-06-01T21:00:00.000Z",
      "start": "2021-06-01T20:00:00.000Z",
      "tweet_count": 3082
    },
    {
      "end": "2021-06-01T22:00:00.000Z",
      "start": "2021-06-01T21:00:00.000Z",
      "tweet_count": 3112
    },
    {
      "end": "2021-06-01T23:00:00.000Z",
      "start": "2021-06-01T22:00:00.000Z",
      "tweet_count": 3509
    },
    {
      "end": "2021-06-02T00:00:00.000Z",
      "start": "2021-06-01T23:00:00.000Z",
      "tweet_count": 3011
    },
    {
      "end": "2021-06-02T01:00:00.000Z",
      "start": "2021-06-02T00:00:00.000Z",
      "tweet_count": 5267
    },
    {
      "end": "2021-06-02T02:00:00.000Z",
      "start": "2021-06-02T01:00:00.000Z",
      "tweet_count": 7784
    },
    {
      "end": "2021-06-02T03:00:00.000Z",
      "start": "2021-06-02T02:00:00.000Z",
      "tweet_count": 29339
    },
    {
      "end": "2021-06-02T04:00:00.000Z",
      "start": "2021-06-02T03:00:00.000Z",
      "tweet_count": 93671
    },
    {
      "end": "2021-06-02T05:00:00.000Z",
      "start": "2021-06-02T04:00:00.000Z",
      "tweet_count": 48240
    },
    {
      "end": "2021-06-02T06:00:00.000Z",
      "start": "2021-06-02T05:00:00.000Z",
      "tweet_count": 14795
    },
    {
      "end": "2021-06-02T07:00:00.000Z",
      "start": "2021-06-02T06:00:00.000Z",
      "tweet_count": 7994
    },
    {
      "end": "2021-06-02T08:00:00.000Z",
      "start": "2021-06-02T07:00:00.000Z",
      "tweet_count": 5430
    },
    {
      "end": "2021-06-02T09:00:00.000Z",
      "start": "2021-06-02T08:00:00.000Z",
      "tweet_count": 3640
    },
    {
      "end": "2021-06-02T10:00:00.000Z",
      "start": "2021-06-02T09:00:00.000Z",
      "tweet_count": 2940
    },
    {
      "end": "2021-06-02T11:00:00.000Z",
      "start": "2021-06-02T10:00:00.000Z",
      "tweet_count": 3377
    },
    {
      "end": "2021-06-02T12:00:00.000Z",
      "start": "2021-06-02T11:00:00.000Z",
      "tweet_count": 4122
    },
    {
      "end": "2021-06-02T13:00:00.000Z",
      "start": "2021-06-02T12:00:00.000Z",
      "tweet_count": 4753
    },
    {
      "end": "2021-06-02T14:00:00.000Z",
      "start": "2021-06-02T13:00:00.000Z",
      "tweet_count": 5258
    },
    {
      "end": "2021-06-02T15:00:00.000Z",
      "start": "2021-06-02T14:00:00.000Z",
      "tweet_count": 6044
    },
    {
      "end": "2021-06-02T16:00:00.000Z",
      "start": "2021-06-02T15:00:00.000Z",
      "tweet_count": 5902
    },
    {
      "end": "2021-06-02T17:00:00.000Z",
      "start": "2021-06-02T16:00:00.000Z",
      "tweet_count": 4986
    },
    {
      "end": "2021-06-02T18:00:00.000Z",
      "start": "2021-06-02T17:00:00.000Z",
      "tweet_count": 5278
    },
    {
      "end": "2021-06-02T19:00:00.000Z",
      "start": "2021-06-02T18:00:00.000Z",
      "tweet_count": 4964
    },
    {
      "end": "2021-06-02T20:00:00.000Z",
      "start": "2021-06-02T19:00:00.000Z",
      "tweet_count": 4641
    },
    {
      "end": "2021-06-02T21:00:00.000Z",
      "start": "2021-06-02T20:00:00.000Z",
      "tweet_count": 4188
    },
    {
      "end": "2021-06-02T22:00:00.000Z",
      "start": "2021-06-02T21:00:00.000Z",
      "tweet_count": 3479
    },
    {
      "end": "2021-06-02T23:00:00.000Z",
      "start": "2021-06-02T22:00:00.000Z",
      "tweet_count": 3506
    },
    {
      "end": "2021-06-03T00:00:00.000Z",
      "start": "2021-06-02T23:00:00.000Z",
      "tweet_count": 2544
    }
  ],
  "meta": {
    "total_tweet_count": 744364
  }
}
```

```
      {
  "data": [
    {
      "end": "2021-01-02T00:00:00.000Z",
      "start": "2021-01-01T00:00:00.000Z",
      "tweet_count": 18392
    },
    {
      "end": "2021-01-03T00:00:00.000Z",
      "start": "2021-01-02T00:00:00.000Z",
      "tweet_count": 46914
    },
    {
      "end": "2021-01-04T00:00:00.000Z",
      "start": "2021-01-03T00:00:00.000Z",
      "tweet_count": 20441
    },
    {
      "end": "2021-01-05T00:00:00.000Z",
      "start": "2021-01-04T00:00:00.000Z",
      "tweet_count": 33500
    },
    {
      "end": "2021-01-06T00:00:00.000Z",
      "start": "2021-01-05T00:00:00.000Z",
      "tweet_count": 21046
    },
    {
      "end": "2021-01-07T00:00:00.000Z",
      "start": "2021-01-06T00:00:00.000Z",
      "tweet_count": 48095
    },
    {
      "end": "2021-01-08T00:00:00.000Z",
      "start": "2021-01-07T00:00:00.000Z",
      "tweet_count": 26190
    },
    {
      "end": "2021-01-09T00:00:00.000Z",
      "start": "2021-01-08T00:00:00.000Z",
      "tweet_count": 48977
    },
    {
      "end": "2021-01-10T00:00:00.000Z",
      "start": "2021-01-09T00:00:00.000Z",
      "tweet_count": 49339
    },
    {
      "end": "2021-01-11T00:00:00.000Z",
      "start": "2021-01-10T00:00:00.000Z",
      "tweet_count": 13753
    },
    {
      "end": "2021-01-12T00:00:00.000Z",
      "start": "2021-01-11T00:00:00.000Z",
      "tweet_count": 44699
    },
    {
      "end": "2021-01-13T00:00:00.000Z",
      "start": "2021-01-12T00:00:00.000Z",
      "tweet_count": 19848
    },
    {
      "end": "2021-01-14T00:00:00.000Z",
      "start": "2021-01-13T00:00:00.000Z",
      "tweet_count": 161169
    },
    {
      "end": "2021-01-15T00:00:00.000Z",
      "start": "2021-01-14T00:00:00.000Z",
      "tweet_count": 85194
    }
  ],
  "meta": {
    "total_tweet_count": 637557
  }
}
```

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `start` | date (ISO 8601) | Start time for the granularity. |
| `end` | date (ISO 8601) | End time for the granularity. |
| `tweet_count` | integer | Count of the volume of Tweets that match the query. |
| `meta` | object | Creation time of the Tweet. |
| `meta.total_tweet_count` | integer | Total count of the Tweets that match the query. |
| `meta.next_token` | string | This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified. |

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