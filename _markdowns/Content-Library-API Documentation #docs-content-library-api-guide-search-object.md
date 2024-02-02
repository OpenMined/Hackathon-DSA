::: {._4-u3 ._588p}
The Content Library API uses search objects to extract a subset of data
from an extremely large online database. Each search object specifies
the search method to be used and sets the values of the parameters that
determine which data will be returned.

::: {._57yz ._57z1 ._3-8p}
::: _57y-
The parameters accepted by each search method are described in the
search method [guides](/docs/content-library-api/guides) .
:::
:::

The following sections describe how to use search objects to achieve
various objectives, providing query examples in both R and Python.

### Basic synchronous search with paginated results {#sync-search}

Unless you specify otherwise, a search object is synchronous in nature,
meaning that you submit the query and wait for the results, and you
cannot submit another until the first one finishes. Synchronous search
results display 10 results at a time (a \"page\") and you request the
next pages one by one. This type of search is most useful when the data
matching the search criteria is expected to be small or when you just
want to sample some results to see if they are appropriate for your
research and don\'t necessarily need to see everything. This can be a
step in the process of fine-tuning your search criteria.

::: {._57yz ._57z1 ._3-8p}
::: _57y-
Synchronous searches can return a maximum of 1000 results. When you need
a larger set of results, use [asynchronous searches](#async-search) .
:::
:::

::: _4gnb
::: {#u_0_3_WX ._4gnf ._4fa6}
``` {.prettyprint .lang-r}
#Import the client library if you have not already done so:        
library(contentlibraryapi)
client <- ContentLibraryAPIClient$new(version='1')

# Create a search object using the search_posts() search method:
post_search <- client$search_posts(
    q='mountains',
    since=1622937600,
    until=1686095999)
        
# Instructions for display:        
posts <- post_search$query_next_page()
print(posts)
```
:::
:::

By default, search responses use JavaScript Object Notation (JSON)
format. This response format uses separators rather than being organized
into columns. If you prefer the display in columns, the API has a
function to specify DataFrame format instead.

::: _4gnb
::: {#u_0_7_XW ._4gnf ._4fa6}
``` {.prettyprint .lang-r}
# Create a search object
post_search <- client$search_posts(
    q='mountains')
        
# Instructions for display:        
print(post_search$query_next_page('dataframe'))
```
:::
:::

While exploring the data to arrive at the most appropriate search
parameters for your purposes, you might find the ` alter_search_params `
method useful. This method returns a new search object with any new
parameters you specify overriding the original ones.

::: _4gnb
::: {#u_0_b_At ._4gnf ._4fa6}
``` {.prettyprint .lang-r}
# Get a new search object with altered parameters:
new_post_search <- post_search$alter_search_params(q = 'mountains', lang='en,es', since=1622937600,
    until=1622938000)

# Instructions for display:
new_post <- new_post_search$query_next_page()
print(new_post)
```
:::
:::

Asynchronous searching capability is available for when you want to work
with all of the data returned from a search, up to the search results
limit that applies to every individual asynchronous search. Asynchronous
searches can take some time (minutes to days) to complete because they
return all of the data requested, not just one page at a time. However,
because the search happens in the background, you don\'t have to wait
for the results before submitting another search or doing other work.
Once the search results are ready, you can fetch them.

The search result limit for each asynchronous search is 100,000 results.
See [Estimating response size](#estimate) .

::: {._57yz ._57z1 ._3-8p}
::: _57y-
Researcher Platform also has an asynchronous search feature, but that is
strictly for static database use and does not work the same way. With
Content Library API, you can only use the ` async_search() ` method
described here.
:::
:::

When you submit an asynchronous search, the API returns \"True\"
indicating the successful submission of the asynchronous query if the
expected results are below the 100,000 search results limit, and an
error message if the expected results are over the limit.

If the search is successfully submitted, you can check on the status and
receive either IN_PROGRESS or COMPLETE.

Use the ` submit_async_query() ` method with ` async_status ` :

::: _4gnb
::: {#u_0_f_f9 ._4gnf ._4fa6}
``` {.prettyprint .lang-r}
# Previous example submitted as an async search:
async_submission <- new_post_search$submit_async_query()
print(async_submission) # Returns True or error

async_status <- new_post_search$get_async_search_status()
print(async_status) # ex: # Returns IN_PROGRESS or COMPLETE
```
:::
:::

When the check for status shows COMPLETE, you can fetch the data in
either JSON or DataFrame format (JSON is the default). You can also
write the data to a file, which will be stored in the
` /previous_searches/ ` folder in your Jupyter environment in JSON
format.

::: _4gnb
::: {#u_0_j_XJ ._4gnf ._4fa6}
``` {.prettyprint .lang-r}
data <- new_post_search$get_data("dataframe") # Specifies DataFrame format
        
new_post_search$write_data_to_file("file_name")  # Writes data to a file
```
:::
:::

Use the ` get_all_async_queries() ` method to get a list of all your
previously executed asynchronous searches.

::: _4gnb
::: {#u_0_n_sJ ._4gnf ._4fa6}
``` {.prettyprint .lang-r}
# Get a list of search objects you've previously executed asynchronously:
previous_searches <- client$get_all_async_queries()
```
:::
:::

Use the ` get_estimate() ` function to get a rough idea of how much data
would be returned from a search you have defined. Since the API can only
return up to 100,000 results from a single asynchronous search, it can
be helpful to know in advance if your search is likely to fail because
the response size is too large. If the estimate comes out higher than
100,000, consider modifying the parameters to reduce the response size.
You can continue to modify the search parameters and get new estimates
until the search results are predicted to fall below the maximum
allowed.

This is typically most useful for post searches because the number of
results tend to be higher, but it can be used to estimate the size of
data that would be returned by any search.

::: _4gnb
::: {#u_0_r_sZ ._4gnf ._4fa6}
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
