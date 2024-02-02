Rate limiting - Content Library and API - Documentation - Meta for Developers

Content Library and API* Get access
* Quick links
* Content Library
* Content Library API
* Appendix
* Get help
* Citations
Rate limiting and query budgeting
=================================

Meta Content Library and API both have limits at the individual researcher level that:

* Put a cap on the number of queries allowed per user per minute (a separate limit for each tool). This is called a *rate limit*.
* Put a cap on the number of retrieved data records (posts, for example) per user per seven-day rolling window. This limit, called a *query budget*, is shared between the two tools per user. In other words, a single researcher has a total query budget between the two tools, regardless if they are using just Content Library, just Content Library API, or both.

Maintaining a rate-limiting and query-budgeting policy ensures that the tools run efficiently and provide all users with consistent data access, unhindered by reduced performance. It also provides a measure of protection against system flooding.

What are the limits?
--------------------

### Rate limits for Content Library

* 60 queries over any one-minute interval

### Rate limits for Content Library API

* Synchronous search queries: 60 queries over any one-minute interval
* Asynchronous search queries: 1 query per minute

See Search guide for information about the difference between synchronous and asynchronous searches.

### Combined query budget per researcher

For Content Library and API combined, you can retrieve a maximum of 500,000 data records per seven-day rolling window. The rolling window is one week previous to the current timestamp (to the second). If you are blocked by hitting the query budget, you should not need to wait long before you try again.

If you are using the Content Library API in a third-party cleanroom environment, and if that environment supports including multimedia in posts, there is an additional query budget of 1000 queries with multimedia per rolling week.

How to request a limit increase
-------------------------------

If you have questions or concerns about the impact of your limits on your research, contact us through Direct Support.

Limit reached messaging
-----------------------

### Content Library

Content Library warns you when you get close to the maximum number of data records retrieved per seven-day rolling window (query budget) with a banner at the top of the page. This is an example of what the banner looks like:

When you reach your query budget, you will see a different banner at the top of the page that looks like this:

The banner has a "Learn more" link, which will open the following message with additional details about rate limits:

### Content Library API

If you reach the maximum number of queries per minute (rate limit) in Content Library API, you will see a log message indicating that the system will retry your last request after a wait time.

This is an example of what the message looks like:

If you reach the maximum number of data records retrieved per seven-day rolling window (query budget), you will see an error message indicating that you have reached your allotted query budget and recommending that you retry your latest query later. In this case, the system does not handle retrying the request for you.

This is an example of what the message looks like:

Tips for staying below the limits
---------------------------------

In general, searching for common words and requesting to fetch all the results can exhaust your query budget. Consider narrowing your searches for more targeted results.

### Get your current usage

`get_query_budget()` is a method that displays your maximum number of data records retrieved per rolling 7-day period (query budget) and how much of that budget you have already used:

RPython
```
library(contentlibraryapi)
client <- ContentLibraryAPIClient$new(version='1')
client$get_query_budget()
```
```
from contentlibraryapi import ContentLibraryAPIClient
client = ContentLibraryAPIClient.get_instance(version='2')
client.get_query_budget()
```
This is a sample of the output:

```
[{'current_usage': 101000,
  'preallocated_rows_for_running_queries': 0,
  'total_usage': 101000,
  'max_usage_limit': 500000,
  'timestamp': 'Tuesday, July 18, 2023 06:03:05 PM PDT'}]
```
* *current\_usage* is the number of results already returned by completed queries in the current 7-day rolling time window as of the current timestamp.
* *preallocated\_rows\_for\_running\_queries* is the number of results (rows) allocated for asynchronous queries that are in progress.
* *total\_usage* is the sum of *current\_usage* and *preallocated\_rows\_for\_running\_queries*.
* *max\_usage\_limit* is the maximum number of queries allowed in a 7-day rolling window.
* *timestamp* marks the point in time at which these statistics were collected.

#### Current usage for multimedia

If you are using the Meta Content Library API in an approved third-party cleanroom environment (as opposed to Meta's Researcher Platform), *and if that environment supports including multimedia in posts*, multimedia-specific query budget usage is also available as a `multimedia` JSON object with the following fields:

* *total\_usage* is the number of calls with multimedia in the current 7-day rolling time window as of the current timestamp.
* *max\_usage\_limit* is the maximum number of calls with media allowed in a 7-day rolling window.

The query budget specific to queries containing multimedia is 1000 queries per 7-day rolling window.

### Estimate response size for asynchronous queries

`get_estimate()` is a method that gives you a rough idea of how much data would be returned from a search you plan to run asynchronously. See Estimating response size and Asynchrounous search in the *Search Guide* for more information on these topics.

**Points to keep in mind**:

* The API can only return up to 100,000 results from a single asynchronous search, so it can be helpful to know in advance if your search is likely to fail because the response size is too large.
* The query budget of 500,000 results in a rolling seven-day window can be used up quickly on just a few searches with high predicted results.

If the estimate comes out higher than 100,000, you might consider modifying the parameters to reduce the response size. You can continue to modify the search parameters and get new estimates until the search results are predicted to fall below the maximum allowed or close to the response size you prefer.

This is typically most useful for post searches because the number of results tend to be higher, but it can be used to estimate the number of results that would be returned by any search.

RPython
```
# Request an estimate:
post_search <- client$search_posts(q = 'dogs')
estimate <- post_search$get_estimate()        
# Display the estimate:        
print(estimate)
```
```
# Request an estimate:  
post_search = client.search_posts(q='dogs')        
estimate = post_search.get_estimate()
# Display the estimate:        
print(estimate)
```
Learn more
----------

* Search guide