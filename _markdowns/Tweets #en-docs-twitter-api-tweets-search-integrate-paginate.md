::: is-table-default
Search queries typically match on more Tweets than can be returned in a
single API response. When that happens, the data is returned in a series
of \'pages\'. Pagination refers to methods for requesting all of the
pages in order to retrieve the entire data set.

Here are fundamental recent search pagination details:

-   The recent search endpoints will respond to a query with at least
    one page, and provide a [ next_token ]{.code-inline} in its JSON
    response if additional pages are available. To receive matching
    Tweets, this process can be repeated until no token is included in
    the response.
-   The [ next_token ]{.code-inline} does not expire. Multiple requests
    using the same [ next_token ]{.code-inline} value will receive the
    same results, regardless of when the request is made.

```{=html}
<!-- -->
```
-   Tweets are delivered in reverse-chronological order, in the UTC
    timezone. This is true within individual pages, as well as across
    multiple pages:
    -   The first Tweet in the first response will be the most recent
        one matching your query.
    -   The last Tweet in the last response will be the oldest one
        matching your query.

```{=html}
<!-- -->
```
-   The [ max_results ]{.code-inline} request parameter enables you to
    configure the number of Tweets returned per response. This defaults
    to 10 Tweets and has a maximum of 100.

```{=html}
<!-- -->
```
-   Every pagination implementation will involve parsing [ next_tokens
    ]{.code-inline} from the response payload, and including them in the
    \'next page\' search request. See below for more details on how to
    construct these \'next page\' requests.\

The recent search endpoint was designed to support two fundamental use
patterns:

-   **Get historical** - Requesting matching Tweets from a time period
    of interest. These are typically one-time requests in support of
    historical research. Search requests can be based on [ start_time
    ]{.code-inline} and [ end_time ]{.code-inline} request parameters.
    recent search endpoint respond with Tweets delivered in
    reverse-chronological order, starting with the most recent matching
    Tweet.

```{=html}
<!-- -->
```
-   **Polling** - Requesting matching Tweets that have been posted since
    the last Tweet received. These use cases often have a near-real-time
    focus and are characterized by frequent requests, \"listening\" for
    new Tweets of interest. The recent search endpoint provide the [
    since_id ]{.code-inline} request parameter in support of the
    \'polling\' pattern. To help with navigating by Tweet IDs, the [
    until_id ]{.code-inline} request parameter is also available.\

Next, we\'ll discuss the historical mode. This is the default mode of
the recent search endpoint and illustrates the fundamentals of
pagination. Then we\'ll discuss examples of polling use cases. When
polling triggers pagination, there is an additional step to manage
search requests.\

### Retrieving historical data

This section outlines how you can retrieve Tweets from a period of
interest (currently limited to the last seven days) using the [
start_time ]{.code-inline} and [ end_time ]{.code-inline} request
parameters. Historical requests are typically one-time requests in
support of research and analysis.

Making requests for a period of data is the default mode of the recent
search endpoint. If a search request does not specify a [ start_time
]{.code-inline} , [ end_time ]{.code-inline} , or [ since_id
]{.code-inline} request parameter, the [ end_time ]{.code-inline} will
default to \"now\" (actually 30 seconds before the time of query) and
the [ start_time ]{.code-inline} will default to seven days ago.

The endpoint will respond with the first \'page\' of Tweets in
reverse-chronological order, starting with the most recent Tweet. The
response JSON payload will also include a [ next_token ]{.code-inline}
if there are additional pages of data. To collect the entire set of
matching Tweets, regardless of the number of pages, requests are made
until no [ next_token ]{.code-inline} is provided.\

For example, here is an initial request for Tweets with the keyword [
snow ]{.code-inline} from the last week:

[ https://api.twitter.com/2/tweets/search/recent?query=snow
]{.code-inline}

The response includes the most recent 10 Tweets, along with these
\"meta\" attributes in the JSON response:

    "meta": {
            "newest_id": "1204860593741553664",
            "oldest_id": "1204860580630278147",
            "next_token": "b26v89c19zqg8o3fobd8v73egzbdt3qao235oql",
            "result_count": 10
        }

\
To retrieve the next 10 Tweets, this [ next_token ]{.code-inline} is
added to the original request. The request would be:

[
https://api.twitter.com/2/tweets/search/recent?query=snow&next_token=b26v89c19zqg8o3fobd8v73egzbdt3qao235oql
]{.code-inline}

The process of looking for a [ next_token ]{.code-inline} and including
it in a subsequent request can be repeated until all (or some number of)
Tweets are collected, or until a specified number of requests have been
made. If data fidelity (collecting all matches of your query) is key to
your use case, a simple \"repeat until [ request.next_token
]{.code-inline} is null\" design will suffice.\

### Polling and listening use cases

This section outlines how you can retrieve recent Tweets by polling the
recent search endpoint with the [ since_id ]{.code-inline} request
parameter.

With polling use cases, \"any new Tweets of interest?\" queries are made
on an on-going, frequent basis. Unlike historical use cases, that base
requests on time, polling use cases typically base requests on Tweet
IDs.

Central to the polling use pattern is that every new Tweet has a [unique
ID](/en/docs/twitter-ids) that is \'emitted\' from the Twitter platform
generally in ascending order. If one Tweet has an ID smaller than
another, it means it was posted earlier.

The recent search endpoint support navigating the Tweet archive by Tweet
ID. Responses from the endpoint include [ oldest_id ]{.code-inline} and
[ newest_id ]{.code-inline} Tweet IDs. In the polling mode, requests are
made with the [ since_id ]{.code-inline} set to the largest/newest ID
received so far.

For example, say a query for new Tweets about snow is made every five
minutes, and the last Tweet we received had a Tweet ID of 10000. When it
is time to poll, the request looks like:

[
https://api.twitter.com/2/tweets/search/recent?query=snow&since_id=10000
]{.code-inline}

Next, let\'s say seven Tweets were posted since our last request. Since
all of these fit on a single data \'page\', there is no [ next_token
]{.code-inline} . The response provides the Tweet ID of the most recent
(newest) Tweet:

    "meta": {
            "newest_id": "12000",
            "oldest_id": "10005",
            "result_count": 7
        }

\
To make the next polling query, this [ newest_id ]{.code-inline} value
is used to set the next [ since_id ]{.code-inline} parameter:

` https://api.twitter.com/2/tweets/search/recent?query=snow&since_id=12000 `

When there is more data available, and next tokens are provided, only th
[ newest_id ]{.code-inline} value from the first page of results is
needed. Each page of data will include [ newest_id ]{.code-inline} and [
oldest_id ]{.code-inline} values, but the value provided in the first
page is the only one needed for the next, regularly scheduled, polling
request. So, If you are implementing a polling design, or searching for
Tweets by ID range, pagination logic is slightly more complicated.

Now say that there are now 18 more matching Tweets. The endpoint would
respond with this initial response with a full data page and a [
next_token ]{.code-inline} for requesting the next page of data from
this five minute period. It would also include the newest Tweet ID need
for the next polling interval in five minutes.

    "meta": {
            "newest_id": "13800",
            "oldest_id": "12500",
            "next_token": "fnsih9chihsnkjbvkjbsc",
            "result_count": 10
        }

\
To collect all the matching data for this five minute period, pass the [
next_token ]{.code-inline} in your next request, along with the same [
since_id ]{.code-inline} value as the previous request.

[
https://api.twitter.com/2/tweets/search/recent?query=snow&since_id=12000&next_token=fnsih9chihsnkjbvkjbsc
]{.code-inline}

    "meta": {
            "newest_id": "12300",
            "oldest_id": "12010",
            "result_count": 8
        }

\
This second response provides the remaining eight Tweets, and no [
next_token ]{.code-inline} . Note that we do not update our [ newest_id
]{.code-inline} value (12300), and instead base our next [ since_id
]{.code-inline} request on the first response\'s [ newest_id
]{.code-inline} value:

[
https://api.twitter.com/2/tweets/search/recent?query=snow&since_id=13800
]{.code-inline}
:::
