::: is-table-default
To work with any Twitter API v2 endpoints, you must have a [developer
account](/en/docs/developer-portal/overview) , set up a
[Project](/en/docs/projects/overview) within that account, and created a
[developer App](/en/docs/apps/overview) within that Project. Your keys
and tokens within that developer App will work for the recent Tweet
counts endpoints. If you would like to use the full-archive Tweet counts
endpoint, or utilize the advanced operators and longer query length, you
will need to have been approved for enterprise access.

Please visit our section on enterprise access to learn more. \

#### Rate limits []{#rate-limits}

Every day, many thousands of developers make requests to the Twitter
API. To help manage the volume, [rate
limits](/en/docs/twitter-api/rate-limits) are placed on each endpoint
that limits the number of requests that every developer can make on
behalf of an app or on behalf of an authenticated user.

This endpoint is rate limited at the App-level, meaning that you, the
developer, can only make a certain number of requests to this endpoint
over a given period of time from any given App (assumed by the
credentials that you are using).

####  Building queries  []{#queries} 

The central feature of these endpoints is their use of a single query to
filter the Tweets into the counts that deliver to you. These queries are
made up of operators that match on Tweet and user attributes, such as
message keywords, hashtags, and URLs. Operators can be combined into
queries with boolean logic and parentheses to help refine the query\'s
matching behavior.

You can use our guide on [how to build a
query](/en/docs/twitter-api/tweets/counts/integrate/build-a-query) to
learn more.

We have also written a more in-depth tutorial on how to [build
high-quality filters for getting Twitter
data](/en/docs/tutorials/building-high-quality-filters) .\

#### Pagination []{#pagination}

For recent Tweet counts, there is no [ next_token ]{.code-inline}
returned, which means that regardless of the granularity, you will get 
the Tweet volume for the last 7 days in one API call.

For full-archive Tweet counts, you will get data for the last 30 days.
For data more than 30 days, you will get a [ next_token ]{.code-inline}
which you can then use to paginate to get the additional data.
:::
