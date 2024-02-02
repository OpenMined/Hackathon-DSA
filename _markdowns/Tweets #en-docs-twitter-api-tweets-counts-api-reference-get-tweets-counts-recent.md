::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
The recent Tweet counts endpoint returns count of Tweets from the last
seven days that match a query.

### Endpoint URL

` https://api.twitter.com/2/tweets/counts/recent `

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

+-----------------------+-----------------------+-----------------------+
| Name                  | Type                  | Description           |
+-----------------------+-----------------------+-----------------------+
| ` query `\            | string                | One query for         |
| [Required]{.small}    |                       | matching Tweets. You  |
|                       |                       | can learn how to      |
|                       |                       | build this query by   |
|                       |                       | reading our [build a  |
|                       |                       | query                 |
|                       |                       | gui                   |
|                       |                       | de](/en/docs/twitter- |
|                       |                       | api/tweets/counts/int |
|                       |                       | egrate/build-a-query) |
|                       |                       | . If you have         |
|                       |                       | Essential or Elevated |
|                       |                       | access, you can use   |
|                       |                       | the Basic operators   |
|                       |                       | when building your    |
|                       |                       | query and can make    |
|                       |                       | queries up to 512     |
|                       |                       | characters long. If   |
|                       |                       | you have been         |
|                       |                       | approved for Academic |
|                       |                       | Research access, you  |
|                       |                       | can use all available |
|                       |                       | operators and can     |
|                       |                       | make queries up to    |
|                       |                       | 1,024 characters      |
|                       |                       | long.                 |
|                       |                       |                       |
|                       |                       | Learn more about our  |
|                       |                       | access levels on the  |
|                       |                       | about Twitter API     |
|                       |                       | page .                |
+-----------------------+-----------------------+-----------------------+
| ` end_time `\         | date (ISO 8601)       | YYYY-MM-DDTHH:mm:ssZ  |
| [Optional]{.small}    |                       | (ISO 8601/RFC 3339).  |
|                       |                       | The newest, most      |
|                       |                       | recent UTC timestamp  |
|                       |                       | to which the Tweet    |
|                       |                       | counts will be        |
|                       |                       | provided. Timestamp   |
|                       |                       | is in second          |
|                       |                       | granularity and is    |
|                       |                       | exclusive (for        |
|                       |                       | example, 12:00:01     |
|                       |                       | excludes the first    |
|                       |                       | second of the         |
|                       |                       | minute). By default,  |
|                       |                       | a request will return |
|                       |                       | Tweet counts from as  |
|                       |                       | recent as 30 seconds  |
|                       |                       | ago if you do not     |
|                       |                       | include this          |
|                       |                       | parameter.            |
+-----------------------+-----------------------+-----------------------+
| ` granularity `\      | string                | This is the           |
| [Optional]{.small}    |                       | granularity that you  |
|                       |                       | want the timeseries   |
|                       |                       | count data to be      |
|                       |                       | grouped by. You can   |
|                       |                       | requeset ` minute ` , |
|                       |                       | ` hour ` , or ` day ` |
|                       |                       | granularity. The      |
|                       |                       | default granularity,  |
|                       |                       | if not specified is   |
|                       |                       | ` hour ` .            |
+-----------------------+-----------------------+-----------------------+
| ` since_id `\         | string                | Returns results with  |
| [Optional]{.small}    |                       | a Tweet ID greater    |
|                       |                       | than (that is, more   |
|                       |                       | recent than) the      |
|                       |                       | specified ID. The ID  |
|                       |                       | specified is          |
|                       |                       | exclusive and         |
|                       |                       | responses will not    |
|                       |                       | include it. If        |
|                       |                       | included with the     |
|                       |                       | same request as a     |
|                       |                       | ` start_time `        |
|                       |                       | parameter, only       |
|                       |                       | ` since_id ` will be  |
|                       |                       | used.                 |
+-----------------------+-----------------------+-----------------------+
| ` start_time `\       | date (ISO 8601)       | YYYY-MM-DDTHH:mm:ssZ  |
| [Optional]{.small}    |                       | (ISO 8601/RFC 3339).  |
|                       |                       | The oldest UTC        |
|                       |                       | timestamp (from most  |
|                       |                       | recent seven days)    |
|                       |                       | from which the Tweet  |
|                       |                       | counts will be        |
|                       |                       | provided. Timestamp   |
|                       |                       | is in second          |
|                       |                       | granularity and is    |
|                       |                       | inclusive (for        |
|                       |                       | example, 12:00:01     |
|                       |                       | includes the first    |
|                       |                       | second of the         |
|                       |                       | minute). If included  |
|                       |                       | with the same request |
|                       |                       | as a ` since_id `     |
|                       |                       | parameter, only       |
|                       |                       | ` since_id ` will be  |
|                       |                       | used. By default, a   |
|                       |                       | request will return   |
|                       |                       | Tweet counts from up  |
|                       |                       | to seven days ago if  |
|                       |                       | you do not include    |
|                       |                       | this parameter.       |
+-----------------------+-----------------------+-----------------------+
| ` until_id `\         | string                | Returns results with  |
| [Optional]{.small}    |                       | a Tweet ID less than  |
|                       |                       | (that is, older than) |
|                       |                       | the specified ID. The |
|                       |                       | ID specified is       |
|                       |                       | exclusive and         |
|                       |                       | responses will not    |
|                       |                       | include it.           |
+-----------------------+-----------------------+-----------------------+
:::
:::

::: c01-rich-text-editor
::: is-table-default
  ---------------------------- ----------------- -----------------------------------------------------
  Name                         Type              Description
  ` start `                    date (ISO 8601)   Start time for the granularity.
  ` end `                      date (ISO 8601)   End time for the granularity.
  ` tweet_count `              integer           Count of the volume of Tweets that match the query.
  ` meta `                     object            Creation time of the Tweet.
  ` meta.total_tweet_count `   integer           Total count of the Tweets that match the query.
  ---------------------------- ----------------- -----------------------------------------------------
:::
:::
:::
