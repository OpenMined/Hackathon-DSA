::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
This endpoint is only available to those users who have been approved
for [Academic Research
access](/en/docs/twitter-api/getting-started/about-twitter-api#v2-access-level)
.

The full-archive Tweet counts endpoint returns the count of Tweets that
match your query from the complete history of public Tweets; since the
first Tweet was created March 26, 2006.

### Endpoint URL

` https://api.twitter.com/2/tweets/counts/all `

+-----------------------------------+-----------------------------------+
| Authentication methods\           | [OAuth 2.0                        |
| supported by this endpoint        | App-only](/en/docs/authentic      |
|                                   | ation/oauth-2-0/application-only) |
+-----------------------------------+-----------------------------------+
| [Rate                             | App rate limit                    |
| limit](/en/docs/rate-limits)      | (Application-only): 300 requests  |
|                                   | per 15-minute window shared among |
|                                   | all users of your app             |
+-----------------------------------+-----------------------------------+

  ----------------------- ----------------------- --------------------------------------------------------------------
  Name                    Type                    Description

  ` query `\              string                  One query for matching Tweets. You can learn how to build this query
  [Required]{.small}                              by reading our [build a query
                                                  guide](/en/docs/twitter-api/tweets/search/integrate/build-a-query)
                                                  .You can use all available operators and can make queries up to
                                                  1,024 characters long.

  ` end_time `\           date (ISO 8601)         YYYY-MM-DDTHH:mm:ssZ (ISO 8601/RFC 3339). Used with ` start_time ` .
  [Optional]{.small}                              The newest, most recent UTC timestamp to which the Tweets will be
                                                  provided. Timestamp is in second granularity and is exclusive (for
                                                  example, 12:00:01 excludes the first second of the minute). If used
                                                  without ` start_time ` , Tweets from 30 days before ` end_time `
                                                  will be returned by default. If not specified, ` end_time ` will
                                                  default to \[now - 30 seconds\].

  ` granularity `\        string                  This is the granularity that you want the timeseries count data to
  [Optional]{.small}                              be grouped by. You can requeset ` minute ` , ` hour ` , or ` day `
                                                  granularity. The default granularity, if not specified is ` hour ` .

  ` next_token `\         string                  This parameter is used to get the next \'page\' of results. The
  [Optional]{.small}                              value used with the parameter is pulled directly from the response
                                                  provided by the API, assuming that your request contains more than
                                                  31 days-worth of results, and should not be modified. You can learn
                                                  more by visiting our page on
                                                  [pagination](/en/docs/twitter-api/pagination) .

  ` since_id `\           string                  Returns results with a Tweet ID greater than (for example, more
  [Optional]{.small}                              recent than) the specified ID. The ID specified is exclusive and
                                                  responses will not include it. If included with the same request as
                                                  a ` start_time ` parameter, only ` since_id ` will be used.

  ` start_time `\         date (ISO 8601)         YYYY-MM-DDTHH:mm:ssZ (ISO 8601/RFC 3339). The oldest UTC timestamp
  [Optional]{.small}                              from which the Tweets will be provided. Timestamp is in second
                                                  granularity and is inclusive (for example, 12:00:01 includes the
                                                  first second of the minute). By default, a request will return
                                                  Tweets from up to 30 days ago if you do not include this parameter.

  ` until_id `\           string                  Returns results with a Tweet ID less than (that is, older than) the
  [Optional]{.small}                              specified ID. Used with ` since_id ` . The ID specified is exclusive
                                                  and responses will not include it.
  ----------------------- ----------------------- --------------------------------------------------------------------
:::
:::

::: c01-rich-text-editor
::: is-table-default
  ---------------------------- ----------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Name                         Type              Description
  ` start `                    date (ISO 8601)   Start time for the granularity.
  ` end `                      date (ISO 8601)   End time for the granularity.
  ` tweet_count `              integer           Count of the volume of Tweets that match the query.
  ` meta `                     object            Creation time of the Tweet.
  ` meta.total_tweet_count `   integer           Total count of the Tweets that match the query.
  ` meta.next_token `          string            This parameter is used to get the next \'page\' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
  ---------------------------- ----------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::
:::
:::
