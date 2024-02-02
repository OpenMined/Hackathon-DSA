::: is-table-default
To work with any Twitter API v2 endpoints, you must have [signed up for
a developer
account](https://developer.twitter.com/en/portal/petition/essential/basic-info)
, set up a Project within that account, and created a developer App
within that Project. Your keys and tokens within that developer App will
work for these search endpoints.

You can use keys and tokens from a Project with any [access
level](/en/docs/twitter-api/getting-started/about-twitter-api#v2-access-level)
to make requests to the recent search endpoint. However, you will need
to use Project with the Pro or Enterprise access level to make requests
to the full archive search endpoint. If you have [Enterprise
access](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api#v2-access-level)
, you will have access to additional functionality, including the
availability of additional operators and longer query lengths.\

#### Rate limits []{#rate-limits}

Every day, many thousands of developers make requests to the Twitter
API. To help manage the volume, [rate
limits](/en/docs/twitter-api/rate-limits) are placed on each endpoint
that limits the number of requests that every developer can make on
behalf of an app or on behalf of an authenticated user.

There are different rate limits applied for these endpoints depending on
which authentication method is being used. The app-level rate limits
apply to an App making requests using OAuth 2.0 App-Only, whereas the
user-level rate limit applies to requests being made on behalf of the
specific authorizing user using OAuth 1.0a User Context or OAuth 2.0
Authorization Code with PKCE. These two rate limits are based on the
frequency of requests within a 15-minute window.

For example, an app using OAuth 2.0 App-Only auth to make requests to
the recent search endpoint can make 450 requests (including pagination
requests) within a 15-minute timeframe. That same app, within the same
15-minute timeframe and with two different authenticated users (using
OAuth 1.0a User Context or OAuth 2.0 Authorization Code with PKCE) can
make up to 180 requests (including pagination requests) to the recent
search endpoint for each authenticated user.\

#### Fields and expansions []{#fields-expansions}

The Twitter API v2 allows you to select exactly which data you want
returned from the API using [fields](/en/docs/twitter-api/fields) and
[expansions](/en/docs/twitter-api/expansions) . The [ expansion
]{.code-inline} parameter allows you to expand objects referenced in the
payload. For example, this endpoint allows you to request poll, place,
media, and other objects using the [ expansions ]{.code-inline}
parameter.

The [ fields ]{.code-inline} parameters allows you to select exactly
which fields within the different data objects you would like to
receive. By default, the primary Tweet object returned by these
endpoints include the [ id ]{.code-inline} and [ text ]{.code-inline}
fields (in addition to [ edit_history_tweet_ids ]{.code-inline} for
Tweets created after that feature was launched). To receive additional
fields such as [ author_id ]{.code-inline} or [ public_metrics
]{.code-inline} , you will have to specifically request those using the
[ fields ]{.code-inline} parameters. Some important fields that you may
want to consider using in your integration are our poll data,
[metrics](/en/docs/twitter-api/metrics) , [Tweet
annotations](/en/docs/twitter-api/annotations) , and [conversation
ID](/en/docs/twitter-api/conversation-id) fields.

We've added a guide on how to [use fields and expansions
together](/en/docs/twitter-api/data-dictionary/using-fields-and-expansions)
to our [Twitter API v2 data
dictionary](/en/docs/twitter-api/data-dictionary) .\

#### Metrics []{#metrics}

The Twitter API v2 endpoints allow you to request metrics directly from
the returned objects, assuming you pass the proper
[fields](/en/docs/twitter-api/fields) with your request.

There are some limitations with Tweet metrics that you should be aware
of, specifically related to user privacy and the following response
fields:

-   [ tweet.fields.non_public_metrics ]{.code-inline}
-   [ tweet.fields.promoted_metrics ]{.code-inline}
-   [ tweet.fields.organic_metrics ]{.code-inline}
-   [ media.fields.non_public_metrics ]{.code-inline}
-   [ media.fields.promoted_metrics ]{.code-inline}
-   [ media.fields.organic_metrics ]{.code-inline}

\
The noted fields include private metrics data, meaning you must be
authorized by the Tweet's publisher to retrieve this data on their
behalf when using the recent search endpoint, meaning you must use
[OAuth 1.0a User Context](/en/docs/authentication/oauth-1-0a) . Since
you can only use this authentication method using recent search, you
will not be able to retrieve these metrics via the full archive search
endpoint.

For example, in order to receive [ non_public_metrics ]{.code-inline}
for user ID 1234\'s Tweets, you will need to include access tokens
associated with that user in your request. You can have users authorize
your app and receive a set of access tokens associated with them by
using the [3-legged OAuth
flow](/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens) .

All [ non_public_metrics ]{.code-inline} , [ organic_metrics,
]{.code-inline} and [ promoted_metrics ]{.code-inline} are only
available for Tweets created in the last 30 days. This means that when
you are requesting the noted fields, the results will automatically
adjust to only include Tweets from the last 30 days.

If these noted fields are requested, only Tweets that are authored by
the authenticated user will be returned, all other Tweets will receive
an error message.\

#### Building search queries []{#queries}

The central feature of these endpoints is their use of a single search
query to filter the Tweets that deliver to you. These queries are made
up of operators that match on Tweet and user attributes, such as message
keywords, hashtags, and URLs. Operators can be combined into queries
with boolean logic and parentheses to help refine the query\'s matching
behavior.

You can use our guide on [how to build a
query](/en/docs/twitter-api/tweets/search/integrate/build-a-query) to
learn more.

We have also written a more in-depth tutorial on how to [build
high-quality filters for getting Twitter
data](/en/docs/tutorials/building-high-quality-filters) .\

#### Pagination []{#pagination}

These endpoints utilize pagination so that responses are returned
quickly. In cases where there are more results than what can be sent in
a single response (up to 100 Tweets for recent search and 500 for
full-archive search) you will need to paginate. Use the [ max_results
]{.code-inline} parameter to identify how many results will return per
page, and the [ pagination_token ]{.code-inline} parameter to return the
next page of results. You can learn more by reviewing our [pagination
guide](/en/docs/twitter-api/pagination) .\

#### Tweet caps []{#tweet-caps}

The Search Tweets endpoints are limited in the number of Tweets that
they can return in a given month, regardless of pagination.

Regardless of which search endpoint you use, the Tweets returned will
count towards the Project-level [Tweet
caps](/en/docs/twitter-api/tweet-caps) . Usage is shown in the developer
portal, and the \'month\' starts on your subscription renewal day shown
on the [developer portal dashboard](/en/portal/dashboard) .

**Tweet edits **

Tweets that are eligible for edits can be edited up to five times in the
30 minutes after the original Tweet was published. The search endpoints
will always provide the latest version of the Tweet. If you only request
Tweets that were published 30 or more minutes ago, you will always
receive the final version of the Tweet. However, if you have a
near-real-time use case, and are querying Tweets published within the
last thirty minutes, those Tweets could have been edited after you
received them. These Tweets can be rehydrated with search, or the Tweet
Lookup endpoint to confirm their final state. To learn more about how
Tweet edits work, see the [Tweet edits
fundamentals](/en/docs/twitter-api/tweet-edits) page.
:::
