::: is-table-default
[ Enterprise ]{.subscription-tag .subscription-tag--enterprise}

*The enterprise APIs are available within our managed access levels
only. To use these APIs, you must first set up an account with our
enterprise sales team. To learn more see
[HERE](/content/developer-twitter/en/enterprise) .*\

*You can view all of the Twitter API search Tweet offerings
[HERE](/en/docs/twitter-api/search-overview) .*

There are two enterprise search APIs:\

1.  30-Day Search API provides data from the previous 30 days.
2.  Full-Archive Search API provides complete and instant access to the
    full corpus of Twitter data dating all the way back to the first
    Tweet in March 2006.

These RESTful APIs supports a single query of up to 2,048 characters per
request. Queries are written with the PowerTrack rule syntax - see
[Rules and
filtering](/en/docs/twitter-api/enterprise/rules-and-filtering/building-a-rule)
for more details. Users can specify any time period, to the granularity
of a minute. However, responses will be limited to the lesser of your
specified maxResults OR 31 days and include a [ next ]{.code-inline}
token to paginate for the next set of results. If time parameters are
not specified, the API will return matching data from the 30 most recent
days.

The enterprise search APIs provide low-latency, full-fidelity,
query-based access to the Tweet archive with minute granularity. Tweet
data is served in reverse chronological order, starting with the most
recent Tweet that matches your query. Tweets are available from the
search API approximately 30 seconds after being published.

These search endpoints provide edited Tweet metadata. All objects for
Tweets created since September 29, 2022, include Tweet edit metadata,
even if the Tweet was never edited. Each time a Tweet is edited, a new
Tweet ID is created. A Tweet\'s edit history is documented by an array
of Tweet IDs, starting with the original ID.

These endpoints will always return the most recent edit, along with any
edit history. Any Tweet collected after its 30-minute edit window will
represent its final version. To learn more about Edit Tweet metadata,
check out the [Edit Tweets
fundamentals](/content/developer-twitter/en/docs/twitter-api/enterprise/edit-tweets)
page.

Requests include a [ maxResults ]{.code-inline} parameter that specifies
the maximum number of Tweets to return per API response. If more Tweets
are associated with the query than this maximum amount of results per
response, a [ next ]{.code-inline} token is included in the response.
These next tokens are used in subsequent requests to page through the
entire set of Tweets associated with the query.

These enterprise search APIs provide a *counts* endpoint that enables
users to request the data volume associated with their query.

### Request types

The enterprise search APIs support two types of requests:\

#### Search requests (data)

Search requests to the enterprise search APIs allow you to retrieve up
to 500 results per response for a given timeframe, with the ability to
paginate for additional data. Using the [ maxResults ]{.code-inline}
parameter, you can specify smaller page sizes for display use cases
(allowing your user to request more results as needed) or larger page
sizes (up to 500) for larger data pulls. The data is delivered in
reverse chronological order and compliant at the time of delivery.

#### Counts requests (Tweet count)

Counts requests provide the ability to retrieve historical activity
counts, which reflect the number of activities that occurred which match
a given query during the requested timeframe. The response will
essentially provide you with a histogram of counts, bucketed by day,
hour, or minute (the default bucket is *hour* ). It\'s important to note
that counts results do not always reflect compliance events (e.g.,
Tweets deletes) that happen well after (7+ days) a Tweet is published;
therefore, it is expected that the counts metric may not always match
that of a data request for the same query.\

**Billing note:** each request -- *including pagination requests* --
made against the data and counts endpoints are counted as a billed
request. Therefore, if there are multiple pages of results for a single
query, paging through the X pages of results would equate to X requests
for billing.

### Available operators []{#AvailableOperators}

Enterprise search APIs support rules with up to 2,048 characters. The
enterprise search APIs support the operators listed below. For detailed
descriptions see
[HERE](/en/docs/twitter-api/enterprise/search-api/guides/search-api/enterprise-operators)
.

+-----------------+-----------------+-----------------+-----------------+
| **Matching on   | **Matching on   | **Tweet         | **Geospatial    |
| Tweet           | accounts of     | attributes:**\  | operators:**\   |
| contents:**\    | interest:**\    |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| -   keyword     |                 | -   is:retweet\ | -   bounding_   |
| -   "quoted     |                 | -               | box:\[west_long |
|     phrase"     |                 |    has:mentions |     south_lat   |
| -   "keyword1   |                 | -               |     east_long   |
|                 |                 |    has:hashtags |     north_lat\] |
|    keyword2"\~N |                 | -   has:media   | -   poi         |
| -   \#          |                 | -   has:videos  | nt_radius:\[lon |
| -   @           |                 | -   has:images  |     lat         |
| -   \$          |                 | -   has:links   |     radius\]    |
| -   url:        |                 | -   has:symbols | -   has:geo     |
| -   lang:       |                 | -               | -   place:      |
|                 |                 |    is:verified\ | -               |
|                 |                 | -   -is:nul     |  place_country: |
|                 |                 | lcast (negation | -               |
|                 |                 |     only        | has:profile_geo |
|                 |                 |     operator)   | -   p           |
|                 |                 |                 | rofile_country: |
|                 |                 |                 | -               |
|                 |                 |                 | profile_region: |
|                 |                 |                 | -   pr          |
|                 |                 |                 | ofile_locality: |
+-----------------+-----------------+-----------------+-----------------+

\
Notes: Do not embed/nest operators (\"#cats\") will resolve to cats with
the search APIs.   The 'lang:' operator and all 'is:' and 'has:'
operators cannot be used as standalone operators and must be combined
with another clause (e.g. \@twitterdev has:links).

Search APIs use a limited set of operators due to tokenization/matching
functionality. enterprise real-time and batched historical APIs provide
additional operators. See
[HERE](/en/docs/twitter-api/enterprise/rules-and-filtering/operators-by-product)
for more details.\

For more details, please see the [Getting started with
operators](/content/developer-twitter/en/docs/twitter-api/enterprise/rules-and-filtering/building-a-rule)
guide.

### Data availability / important date

When using the Full-Archive search API, keep in mind that the Twitter
platform has continued to evolve since 2006. As new features were added,
the underlying JSON objects have had new metadata added to it. For that
reason it is important to understand when Tweet attributes were added
that search operators match on. Below are some of the more fundamental
\'born on\' dates of important groups of metadata. To learn more about
when Tweet attributes were first introduced, see [this
guide](/content/developer-twitter/en/docs/twitter-api/enterprise/search-api/guides/changelog)
.

-   First Tweet: 3/21/2006
-   First Native Retweets: 11/6/2009
-   First Geo-tagged Tweets: 11/19/2009
-   URLs first indexed for filtering: 8/27/2011
-   Enhanced URL expansion metadata (website titles and descriptions):
    12/1/2014
-   Profile Geo enrichment metadata and filtering: 2/17/2015

### []{#DataUpdates} Data Updates and Mutability 

With the enterprise search APIs, some of the data within a Tweet is
mutable, i.e. can be updated or changed after initial archival.

This mutable data falls into two categories:

-   User object metadata:
    -   User's \@handle (numeric ID does not ever change)
    -   Bio description
    -   Counts: statuses, followers, friends, favorites, lists
    -   Profile location
    -   Other details such as time zone and language
-   Tweet statistics - i.e. anything that can be changed on the platform
    by user actions (examples below):
    -   Favorites count
    -   Retweet count

In most of these cases, the search APIs will return data as it exists on
the platform at *query-time* , rather than Tweet generation time.
However, in the case of queries using select operators (e.g. from, to,
@, is:verified), this may not be the case. Data is updated in our index
on a regular basis, with an increased frequency for most recent
timeframes. As a result, in some cases, the data returned may not
exactly match the current data as displayed on Twitter.com, but matches
data at the time it was last indexed.

Note, this issue of inconsistency only applies to queries where the
operator applies to mutable data. One example is filtering for
usernames, and the best workaround would be to use user numeric IDs
rather than \@handles for these queries.

### Single vs. Multi-threaded Requests 

Each customer has a defined rate limit for their search endpoint. The
default per-minute rate limit for Full-Archive search is 120 requests
per minute, for an average of 2 queries per second (QPS). This average
QPS means that, in theory, 2 requests can be made of the API every
second. Given the pagination feature of the product, if a one-year query
has one million Tweets associated with it, spread evenly over the year,
over 2,000 requests would be required (assuming a 'maxResults' of 500)
to receive all the data. Assuming it takes two seconds per response,
that is 4,000 seconds (or just over an hour) to pull all of that data
serially/sequentially through a single thread (1 request per second
using the prior response's "next" token). Not bad!

Now consider the situation where twelve parallel threads are used to
receive data. Assuming an even distribution of the one million Tweets
over the one-year period, you could split the requests into twelve
parallel threads (multi-threaded) and utilize more of the per-second
rate limit for the single "job". In other words, you could run one
thread per-month you are interested in and by doing so, data could be
retrieved 12x as fast (or \~6 minutes).

This multi-threaded example applies equally well to the counts endpoint.
For example, if you wanted to receive Tweet counts for a two-year
period, you could make a single-threaded request and page back through
the counts 31 days at a time. Assuming it takes 2 seconds per response,
it would take approximately 48 seconds to make the 24 API requests and
retrieve the entire set of counts. However, you also have the option to
make multiple one-month requests at a time. When making 12 requests per
second, the entire set of counts could be retrieved in approximately 2
seconds.

### Retry Logic 

If you experience a 503 error with the enterprise search APIs, it is
likely a transient error and can be resolved by re-trying the request a
short time later.

If the request fails 4 times in a row, and you have waited at least 10
minutes between failures, use the following steps to troubleshoot:

-   Retry the request after reducing the amount of time it covers.
    Repeat this down to a 6-hour time window if unsuccessful.
-   If you are ORing a large number of terms together, split them into
    separate rules and retry each individually.
-   If you are using a large number of exclusions in your rule, reduce
    the number of negated terms in the rule and retry.

### Next steps
:::
