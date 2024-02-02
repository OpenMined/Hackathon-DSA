::: is-table-default
Pagination is a feature in Twitter API v2 endpoints that return more
results than can be returned in a single response. When that happens,
the data is returned in a series of \'pages\'. Pagination refers to
methods for programatically requesting all of the pages, in order to
retrieve the entire result data set. Not all API endpoints support or
require pagination, but it is often used when result sets are large.

### Use cases for pagination

**To retrieve all results for a request:** Pagination should most often
be used to receive all relevant data related to a specific request and
parameters. Pagination is required in cases where there are more
matching results than the [ max_results for a request. Integrating
pagination token data into looping requests will allow you to retrieve
all results. Once a response is returned without a [ next_token
]{.code-inline} value, it can be assumed that all results have been
paged through. Pagination should not be used for polling purposes. To
get the most recent results since a previous request, review polling
with [ since_id ]{.code-inline} . ]{.code-inline}

**To traverse through the results of a request:** Pagination provides
directional options for navigating through results from a request, using
[ next_token ]{.code-inline} and [ previous_token ]{.code-inline} values
from responses. These tokens can be set as the [ pagination_token
]{.code-inline} in the following request, to go to the next or the
previous page of results.

### Pagination token definitions

[ next_token ]{.code-inline} - Opaque string returned within the meta
object response on endpoints which support pagination. Indicates that
more results are available and can be used as the [ pagination_token
]{.code-inline} parameter in the next request to return the next page of
results. The last page of results will not have a [ next_token
]{.code-inline} present.

[ previous_token ]{.code-inline} - Opaque string returned within the
meta object response on endpoints which support pagination. Indicates
that there is a previous page of results available, and can be set as
the [ pagination_token ]{.code-inline} parameter in the next request to
return the previous page of results.

[ pagination_token ]{.code-inline} - Parameter used in pagination
requests. Set to the value of [ next_token ]{.code-inline} for the next
page of results. Set to the value of [ previous_token ]{.code-inline}
for the previous page of results.

### Fundamentals of pagination

-   Endpoints which use pagination, will respond to an initial request
    with the first page of results, and provide a [ next_token
    ]{.code-inline} within the meta object in the JSON response if
    additional pages of results are available. To receive all results,
    this process can be repeated until no [ next_token ]{.code-inline}
    is included in the response.

```{=html}
<!-- -->
```
-   Results are delivered in reverse-chronological order. This is true
    within individual pages, as well as across multiple pages:
    -   The first Tweet in the first response will be the most recent.
    -   The last Tweet in the last response will be the oldest.

```{=html}
<!-- -->
```
-   The [ max_results ]{.code-inline} request parameter enables you to
    configure the number of Tweets returned per response page. There
    will be a default [ max_results ]{.code-inline} and a maximum [
    max_results ]{.code-inline} .

-   Every pagination implementation will involve parsing tokens from the
    response payload, which can be used in subsequent requests. See
    below for more details on how to construct these requests.

```{=html}
<!-- -->
```
-   In some circumstances you may get less than the [ max_results
    ]{.code-inline} page of results. Do not rely on the results per page
    to always equal the [ max_results ]{.code-inline} parameter value.

-   The best ways to successfully use pagination for complete results
    are by using loop logic within integration code, or by using a
    [library](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries)
    that supports Twitter API v2.\

### Pagination example

Here, there are three pages of results because [ max_results
]{.code-inline} is set to [ 100 ]{.code-inline} and there are a total of
\~295 Tweets created by user ID [ 2244994945 ]{.code-inline}
(@TwitterDev) between January 1st, 2019 at 17:00:00 UTC and December
12th at 00:00:00 UTC. The first Tweet on the first page ( [
1337498609819021312 ]{.code-inline} ) is the most recent, and the last
Tweet on the third page of results ( [ 1082718487011885056
]{.code-inline} ) is the oldest.\

#### Initial request
:::
