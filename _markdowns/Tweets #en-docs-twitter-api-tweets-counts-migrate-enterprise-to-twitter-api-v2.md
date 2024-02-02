::: is-table-default
**Similarities**

-   Granularity
-   Pagination
-   Timezone

**Differences**

-   Endpoint URLs
-   App and Project requirement
-   Available time periods
-   Response data format
-   HTTP methods
-   Request time formats
-   Request parameters
-   Filtering operators

### Similarities

#### Granularity

While the parameter for selecting granularity of the returned data is
different ( ` bucket ` for the enterprise version, ` granularity ` for
the v2 version), the values that you can pass with that parameter are
the same, as well as the default behavior:

-   ` day `
-   ` hour ` (default)
-   ` minute `

####  Pagination

While v2 has additional pagination features (new pagination parameters
that allow you to navigate using Tweet IDs with ` since_id ` and
` until_id ` ), both enterprise and v2 allow you to paginate using time
( ` fromDate ` and ` toDate ` with enterprise, and ` start_time ` and
` end_time ` for v2).

If you are using the enterprise version, you will use the ` next `
parameter to paginate, the next token field will be called ` next ` ,
and it will be located at the root in the response.

If you are using v2, you can use either the ` next_token ` or
` pagination_token ` parameter to paginate, and your next token will be
located at ` meta.next_token ` in the response.\

#### Timezone

As noted in the pagination section, you can navigate different pages of
data using time for both enterprise and v2. In both cases, you will be
using UTC as the timezone when using these parameters.

### Differences

#### Endpoint URLs

-   Enterprise endpoints:
    -   30 day -
        ` http://gnip-api.twitter.com/search/30day/accounts/:account_name/:label/counts.json `
    -   Full-archive -
        ` http://gnip-api.twitter.com/search/fullarchive/accounts/:account_name/:label/counts.json `
-   Twitter API v2 endpoints
    -   Recent (7 day) -
        ` https://api.twitter.com/2/tweets/counts/recent `
    -   Full-archive - ` https://api.twitter.com/2/tweets/counts/all `

####  App and Project requirement

The Twitter API v2 endpoints require that you use credentials from a
[developer App](/content/developer-twitter/en/docs/apps) that is
associated with a [Project](/content/developer-twitter/en/docs/projects)
when authenticating your requests. All Twitter API v1.1 endpoints can
use credentials from standalone Apps or Apps associated with a Project.\

#### Available time periods

Both the enterprise API and Twitter API v2 offer endpoints that allow
you to retrieve Tweet volume data for the full-archive of Tweets.

However, the Twitter API v2 does not offer a 30 day time period endpoint
like the enterprise API does. Instead it offers the aforementioned
full-archive, or a 7 day time period, which align with the [v2 Search
Tweets
endpoints](/content/developer-twitter/en/docs/twitter-api/tweets/search)
.\

#### Response data format

There are some slight differences in the data format that you will
receive via enterprise and Twitter API v2:

-   Enterprise's counts data is located within a ` results ` object,
    while the v2 counts data is located within a data object.
-   Enterprise's counts fields are called ` timePeriod ` (start time)
    and ` count ` , while v2 breaks out the time period into a ` start `
    and ` end ` field (which use a different date/time format from
    enterprise explained in request time formats), and renamed the count
    field to ` tweet_count ` .
-   The enterprise metadata includes ` totalCount ` , ` next ` , and the
    ` requestParameters ` object at the root level. Instead,v2 doesn't
    include the requestParameters object, and moves/renames the
    following into a ` meta ` object that lives at the root level:
    ` total_tweet_count ` & ` next_token ` .\

#### HTTP methods

The enterprise version of the API allows you to pass the request as
either a POST HTTP method with a JSON body, or a GET HTTP method with a
query string.

V2 only allows you to use the GET HTTP method with a query string.\

#### Request time formats

The enterprise version of this endpoint uses the following date/time
format in both the pagination parameters and the ` timePeriod ` response
field: ` YYYYMMDDHHmm `

The v2 endpoint uses ISO 8601/RFC 3339 date/time format in both the
pagination parameters and the ` start ` and ` end ` response fields:
` YYYY-MM-DDTHH:mm:ssZ `

####  Request parameters

The following is a table of the request parameters for enterprise and
Twitter API v2:

  Enterprise              Search Tweets v2
  ----------------------- -----------------------------------
  query                   query
  bucket                  granularity
  fromDate (YYMMDDHHmm)   start_time (YYYY-MM-DDTHH:mm:ssZ)
  toDate (YYMMDDHHmm)     end_time (YYYY-MM-DDTHH:mm:ssZ)
                          since_id
                          until_id
  next                    next_token and pagination_token

####  Filtering operators

While the operators between enterprise and Twitter API v2 are mostly the
same, there are some differences in operator availability and some new
operators that were introduced to just the Twitter API v2 version.

To see a full table of the operators that are available for Twitter API
v2, enterprise, and even premium, please visit the [Tweet counts
migration landing
page](/content/developer-twitter/en/docs/twitter-api/tweets/counts/migrate)
.
:::
