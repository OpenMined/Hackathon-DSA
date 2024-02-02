
Search guide - Content Library and API - Documentation - Meta for Developers









Content Library and API* Get access
* Quick links
* Content Library
* Content Library API
* Appendix
* Get help
* Citations
Search guide
============


How search works
----------------


Queries in Meta Content Library and API are powered by a version of Facebook’s search engine infrastructure, which relies on a combination of indexing and ranking to return relevant entities. The retrieval function combines matched and ranked IDs from a query using the same distributed memory caching layer which serves live platform content. This ensures that results represent the most current state of content on the platform and meet privacy-preserving visibility criteria (see Frequently asked questions for details).

As content is created or modified on Meta platforms, associated entities are registered to a search index built from individual words extracted from text fields as *tokens*. Tokenization generally isolates words separated by spaces or punctuation ( ?@$%^\*()+=~[{}];:"<>|. ), with some URL normalization and locale-specific adjustments for non-English languages. Tokenization is exact, in that it does not introduce additional word variants ("cats" will not be tokenized to "cat"). Direct mentions of users or other platform entities (via @) are not tokenized and are scrubbed from returned text fields, and are thus not searchable.


At query time, relevant content is identified by exact matching between tokens and individual search terms. Candidate matches are then subject to additional filtering via Boolean query logic (see Advanced search) and other selected filters. Matching is performed independently by word in a query, meaning that searching by phrase is not supported (queries “All for one” and “One for all” are equivalent).


Search objects in the API
-------------------------


The Content Library API uses search objects to extract a subset of data from an extremely large online database. Each search object specifies the search method to be used and sets the values of the parameters that determine which data will be returned.


The parameters accepted by each search method are described in the search method guides.


The following sections describe how to use search objects to achieve various objectives, providing query examples in both R and Python.


* Basic synchronous search with paginated results
* Response formats
* Altering search parameters
* Asynchronous search
* Estimating response size


### Basic synchronous search with paginated results


Unless you specify otherwise, a search object is synchronous in nature, meaning that you submit the query and wait for the results, and you cannot submit another until the first one finishes. Synchronous search results display 10 results at a time (a "page") and you request the next pages one by one. This type of search is most useful when the data matching the search criteria is expected to be small or when you just want to sample some results to see if they are appropriate for your research and don't necessarily need to see everything. This can be a step in the process of fine-tuning your search criteria.


Synchronous searches can return a maximum of 1000 results. When you need a larger set of results, use asynchronous searches.


RPython
```
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

```
#Import the client library if you have not already done so:
from contentlibraryapi import ContentLibraryAPIClient
client = ContentLibraryAPIClient.get_instance(version='1')

# Create a search object using the search_posts() search method:
post_search = client.search_posts(
    q='mountains',
    since=1622937600,
    until=1686095999)
        
#Instructions for display:        
posts = post_search.query_next_page()
print(posts)
```
### Response formats


By default, search responses use JavaScript Object Notation (JSON) format. This response format uses separators rather than being organized into columns. If you prefer the display in columns, the API has a function to specify DataFrame format instead.


RPython
```
# Create a search object
post_search <- client$search_posts(
    q='mountains')
        
# Instructions for display:        
print(post_search$query_next_page('dataframe'))
```

```
# Create a search object
post_search = client.search_posts(
    q='mountains')

#Instructions for display:

display(post_search.query_next_page('dataframe'))
```
### Altering search parameters


While exploring the data to arrive at the most appropriate search parameters for your purposes, you might find the `alter_search_params` method useful. This method returns a new search object with any new parameters you specify overriding the original ones.


RPython
```
# Get a new search object with altered parameters:
new_post_search <- post_search$alter_search_params(q = 'mountains', lang='en,es', since=1622937600,
    until=1622938000)

# Instructions for display:
new_post <- new_post_search$query_next_page()
print(new_post)
```

```
# Get a new search object with altered parameters:
new_post_search = post_search.alter_search_params(q = 'mountains', lang='en,es', since=1622937600,
    until=1622938000)

# Instructions for display:
new_post = new_post_search.query_next_page()
print(new_post)
```
### Asynchronous search


Asynchronous searching capability is available for when you want to work with all of the data returned from a search, up to the search results limit that applies to every individual asynchronous search. Asynchronous searches can take some time (minutes to days) to complete because they return all of the data requested, not just one page at a time. However, because the search happens in the background, you don't have to wait for the results before submitting another search or doing other work. Once the search results are ready, you can fetch them.


The search result limit for each asynchronous search is 100,000 results. See Estimating response size.


Researcher Platform also has an asynchronous search feature, but that is strictly for static database use and does not work the same way. With Content Library API, you can only use the `async_search()` method described here.


When you submit an asynchronous search, the API returns "True" indicating the successful submission of the asynchronous query if the expected results are below the 100,000 search results limit, and an error message if the expected results are over the limit.


If the search is successfully submitted, you can check on the status and receive either IN\_PROGRESS or COMPLETE.


Use the `submit_async_query()` method with `async_status`:


RPython
```
# Previous example submitted as an async search:
async_submission <- new_post_search$submit_async_query()
print(async_submission) # Returns True or error

async_status <- new_post_search$get_async_search_status()
print(async_status) # ex: # Returns IN_PROGRESS or COMPLETE
```

```
# Previous example submitted as an async search:
async_submission = new_post_search.submit_async_query()
print(async_submission) # Returns "True" or an error

async_status = new_post_search.get_async_search_status()
print(async_status) # Returns IN_PROGRESS or COMPLETE
```
When the check for status shows COMPLETE, you can fetch the data in either JSON or DataFrame format (JSON is the default). You can also write the data to a file, which will be stored in the `/previous_searches/` folder in your Jupyter environment in JSON format.


RPython
```
data <- new_post_search$get_data("dataframe") # Specifies DataFrame format
        
new_post_search$write_data_to_file("file_name")  # Writes data to a file
```

```
data = new_post_search.get_data("dataframe") # Specifies DataFrame format
        
new_post_search.write_data_to_file("file_name") # Writes data to a file
```
Use the `get_all_async_queries()` method to get a list of all your previously executed asynchronous searches.


RPython
```
# Get a list of search objects you've previously executed asynchronously:
previous_searches <- client$get_all_async_queries()
```

```
# Get a list of Search objects you've previously executed asynchronously:
previous_searches = client.get_all_async_queries()
print(previous_searches)
```
### Estimating response size


Use the `get_estimate()` function to get a rough idea of how much data would be returned from a search you have defined. Since the API can only return up to 100,000 results from a single asynchronous search, it can be helpful to know in advance if your search is likely to fail because the response size is too large. If the estimate comes out higher than 100,000, consider modifying the parameters to reduce the response size. You can continue to modify the search parameters and get new estimates until the search results are predicted to fall below the maximum allowed.


This is typically most useful for post searches because the number of results tend to be higher, but it can be used to estimate the size of data that would be returned by any search.


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


* Rate limiting and query budgeting
* Advanced search
* Search quality approach


































 
