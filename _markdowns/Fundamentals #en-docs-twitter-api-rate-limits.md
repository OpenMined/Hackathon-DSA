::: is-table-default
Use the HTTP headers in order to understand where the application is at
for a given rate limit, on the method that was just utilized.\

Note that the HTTP headers are contextual. When using application-only
authentication, they indicate the rate limit for the application
context. When using user-based authentication, they indicate the rate
limit for that user context.\

-   [ x-rate-limit-limit: ]{.code-inline} the rate limit ceiling for
    that given endpoint
-   [ x-rate-limit-remaining ]{.code-inline} : the number of requests
    left for the 15-minute window
-   [ x-rate-limit-reset ]{.code-inline} : the remaining window before
    the rate limit resets, in UTC [epoch
    seconds](http://en.wikipedia.org/wiki/Unix_time)\

When an application exceeds the rate limit for a given Twitter API
endpoint, the API will return a [HTTP 429 "Too Many
Requests"](http://tools.ietf.org/html/rfc6585) response code, and the
following error will be returned in the response body:

[ { \"errors\": \[ { \"code\": 88, \"message\": \"Rate limit exceeded\"
} \] } ]{.code-inline}

### []{#recovering} Recovering from a rate limit

When these rate limits are exceeded, a 429 \'Too many requests\' error
is returned from the endpoint.  As discussed below, when rate limit
errors occur, a best practice is to examine HTTP headers that indicate
when the limit resets and pause requests until then.\

When a \"too many requests\" or rate-limiting error occurs, the
frequency of making requests needs to be slowed down. When a rate limit
error is hit, the [ x-rate-limit-reset: ]{.code-inline} HTTP header can
be checked to learn when the rate-limiting will reset.\

Another common pattern is based on exponential backoff, where the time
between requests starts off small (for example, a few seconds), then
doubled before each retry. This is continued until a request is
successful, or some reasonable maximum time between requests is reached
(for example, a few minutes).\

Ideally, the client-side is self-aware of existing rate limits and can
pause requests until the currently exceeded window expires. If you
exceed a 15-minute limit, then waiting a minute or two before retrying
makes sense.

Note that beyond these limits on the number of requests, the Standard
Basic level of access provides up to 500,000 Tweets per month from the
recent search and filtered stream endpoints. If you have exceeded the
monthly limit on the number of Tweets, then it makes more sense for your
app to raise a notification and know its enrollment day of the month and
hold off requests until that day.\

### []{#tips} Tips to avoid being rate limited

The tips below are there to help you code defensively and reduce the
possibility of being rate limited. Some application features that you
may want to provide are simply impossible in light of rate-limiting,
especially around the freshness of results. If real-time information is
an aim of your application, look into the filtered and sampled stream
endpoints.\

#### Caching

Store API responses in your application or on your site if you expect a
lot of use. For example, don't try to call the Twitter API on every page
load of your website landing page. Instead, call the API infrequently
and load the response into a local cache. When users hit your website
load the cached version of the results.\

#### Prioritize active users

If your site keeps track of many Twitter users (for example, fetching
their current status or statistics about their Twitter usage), consider
only requesting data for users who have recently signed into your site.\

#### Adapt to the search results

If your application monitors a high volume of search terms, query less
often for searches that have no results than for those that do. By using
a back-off you can keep up to date on queries that are popular but not
waste cycles requesting queries that very rarely change. Alternatively,
consider using the filtered stream endpoint and filter with your search
queries. \

#### Denylist

If an application abuses the rate limits, it will be denied. Denied apps
are unable to get a response from the Twitter API. If you or your
application has been denied and you think there has been a mistake, you
can use our [Platform Support
forms](https://support.twitter.com/forms/platform) to request
assistance. Please include the following information:

1.  Explain why you think your application was denied.
2.  If you are no longer being rate limited, describe in detail how you
    fixed the problem.
:::
