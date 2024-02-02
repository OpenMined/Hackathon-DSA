::: {._4-u3 ._588p}
In general, searching for common words and requesting to fetch all the
results can exhaust your query budget. Consider narrowing your searches
for more targeted results.

### Get your current usage

` get_query_budget() ` is a method that displays your maximum number of
data records retrieved per rolling 7-day period (query budget) and how
much of that budget you have already used:

::: _4gnb
::: {#u_0_3_n/ ._4gnf ._4fa6}
``` {.prettyprint .lang-r}
library(contentlibraryapi)
client <- ContentLibraryAPIClient$new(version='1')
        
client$get_query_budget()
```
:::
:::

This is a sample of the output:

``` {._5s-8 .prettyprint .lang-python}
 
[{'current_usage': 101000,
  'preallocated_rows_for_running_queries': 0,
  'total_usage': 101000,
  'max_usage_limit': 500000,
  'timestamp': 'Tuesday, July 18, 2023 06:03:05 PM PDT'}]
```

-   *current_usage* is the number of results already returned by
    completed queries in the current 7-day rolling time window as of the
    current timestamp.

-   *preallocated_rows_for_running_queries* is the number of results
    (rows) allocated for asynchronous queries that are in progress.

-   *total_usage* is the sum of *current_usage* and
    *preallocated_rows_for_running_queries* .

-   *max_usage_limit* is the maximum number of queries allowed in a
    7-day rolling window.

-   *timestamp* marks the point in time at which these statistics were
    collected.

### Estimate response size for asynchronous queries

` get_estimate() ` is a method that gives you a rough idea of how much
data would be returned from a search you plan to run asynchronously. See
[Estimating response
size](/docs/content-library-api/guide-search-object#estimate) and
[Asynchrounous
search](/docs/content-library-api/guide-search-object#async-search) in
the *Search Guide* for more information on these topics.

**Points to keep in mind** :

-   The API can only return up to 100,000 results from a single
    asynchronous search, so it can be helpful to know in advance if your
    search is likely to fail because the response size is too large.

-   The query budget of 500,000 results in a rolling seven-day window
    can be used up quickly on just a few searches with high predicted
    results.

If the estimate comes out higher than 100,000, you might consider
modifying the parameters to reduce the response size. You can continue
to modify the search parameters and get new estimates until the search
results are predicted to fall below the maximum allowed or close to the
response size you prefer.

This is typically most useful for post searches because the number of
results tend to be higher, but it can be used to estimate the number of
results that would be returned by any search.

::: _4gnb
::: {#u_0_7_5c ._4gnf ._4fa6}
``` {.prettyprint .lang-r}
# Request an estimate:
post_search <- client$search_posts(q = 'dogs')
estimate <- post_search$get_estimate()        
        
# Display the estimate:        
print(estimate)
```
:::
:::
:::
