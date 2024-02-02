
Facebook Pages - Content Library and API - Documentation - Meta for Developers










Content Library and API* Get access
* Quick links
* Content Library
* Content Library API
* Appendix
* Get help
* Citations
Guide to Facebook Pages data
============================


You can perform Facebook Page searches by calling the Meta Content Library API client's `search_pages()` method. This document describes the `search_pages()` method and its syntax and parameters, and shows how to perform basic queries using the method.


All of the examples in this document assume you have already created a Python or R Jupyter notebook and have created a client object. See Getting started to learn more.


See Data dictionary for detailed information about the fields that are available on a Facebook page node.


search\_pages() method
----------------------


This is the syntax of the `search_pages()` method:



```

search_pages(
    q=Q,
    fields=FIELDS,    
    categories=CATEGORIES,
    is_verified=IS_VERIFIED,
    website=WEBSITE,
    page_ids=PAGE_IDS,
    admin_countries=ADMIN_COUNTRIES
    since=SINCE,
    until=UNTIL
)
```
The following table describes the parameters:




 
 Parameter
  | 
 Type
  | 
 Description
  || `Q`
*Optional* | String | Keyword(s) to search for. Searches a Page's `name` and `description` fields. See Advanced search for information about how multiple keyword searches with Boolean operators are handled. |
| `FIELDS`
*Optional* | List | Comma-separated list of Page fields you want included in search results. See Data dictionary for descriptions of all available fields. |
| `CATEGORIES`
*Optional* | List | Comma-separated list of categories to include in the search. |
| `IS_VERIFIED`
*Optional* | Boolean | The verification status of the Facebook Page. A Facebook Page with a verified badge indicates that Facebook has confirmed that it is the authentic presence for that person or brand. Learn more.  |
| `WEBSITE`
*Optional* | String | Website to match against the Facebook Page's "About" section. |
| `PAGE_IDS`
*Optional* | List | Comma-separated list of Encrypted Page IDs as strings. Limits the query to the specified Pages. Maximum of 250 Page IDs. |
| `ADMIN_COUNTRIES`
*Optional* | List | Comma-separated list of countries by which to filter the Facebook Page's admin. Takes ISO Alpha-2 Country Code in 2-letter uppercase format. |
| `SINCE`
*Optional* | String or Integer | Date in YYYY-MM-DD (date only) or UNIX timestamp (translates to a date and time to the second) format. Facebook Pages created on or after this date or timestamp are returned (used with UNTIL to define a time range). SINCE and UNTIL are based on UTC time zone, regardless of the local time zone of the user who created the Page.* If both SINCE and UNTIL are included, the search includes the time range defined by those values.
* If SINCE is included and UNTIL is omitted, the search includes the SINCE time through the present time.
* If SINCE is omitted and UNTIL is included, the search goes from the beginning of Facebook time through the UNTIL time.
* If SINCE and UNTIL are both omitted, the search goes from the beginning of Facebook time to the present time.
* If SINCE and UNTIL are the same UNIX timestamp, the search includes the SINCE time through the SINCE time plus one hour.
* If SINCE and UNTIL are the same Date (YYYY-MM-DD), the search includes the SINCE date through the SINCE date plus one day.
 |
| `UNTIL`
*Optional* | String or Integer | Date in YYYY-MM-DD (date only) or UNIX timestamp (translates to a date and time to the second) format. Facebook Pages created on or before this date or timestamp are returned (used with SINCE to define a time range). SINCE and UNTIL are based on UTC time zone, regardless of the local time zone of the user who created the Page.* If both SINCE and UNTIL are included, the search includes the time range defined by those values.
* If SINCE is included and UNTIL is omitted, the search includes the SINCE time through the present time.
* If SINCE is omitted and UNTIL is included, the search goes from the beginning of Facebook time through the UNTIL time.
* If SINCE and UNTIL are both omitted, the search goes from the beginning of Facebook time to the present time.
* If SINCE and UNTIL are the same UNIX timestamp, the search includes the SINCE time through the SINCE time plus one hour.
* If SINCE and UNTIL are the same Date (YYYY-MM-DD), the search includes the SINCE date through the SINCE date plus one day.
 |

Sample queries
--------------


### Search for Pages by keyword


To search for Pages that contain a specific keyword, create a search object using the `search_pages()` method with the `q` parameter. See Advanced search for information about how multiple keyword searches are handled.


RPython
```
# Create a client object if you have not already done so:
library(contentlibraryapi)
client <- ContentLibraryAPIClient$new(version='1')
        
# Create a search object:
page_search <- client$search_pages(q='cybercrime')        

# No results are displayed until you provide display instructions:        
print(page_search$query_next_page())
```

```
# Create a client object if you have not already done so:
from contentlibraryapi import ContentLibraryAPIClient
client = ContentLibraryAPIClient.get_instance(version='1')

# Create a search object:
page_search = client.search_pages(q='cybercrime')
        
# No results are displayed until you provide display instructions:
display(page_search.query_next_page())
```
This example would return only 10 results per page. You can keep calling `query_next_page()` to get the next page of 10 results, until all the search results have been returned. See Search guide for other display and storage options.


### Request specific fields


To have the API return only specific fields on any Pages in the response, create a search object using the `search_pages()` method with the `fields` parameter and a comma-separated list of fields you want included. If omitted, default fields will be returned. To more easily see columns of data, this example specifies a DataFrame response format (the default response format is JSON).


RPython
```
# Create a search object including a list of fields:
page_search <- client$search_pages(q='cybercrime', fields='id,name,about')        

# Specify DataFrame response format:       
print(page_search$query_next_page('dataframe'))
```

```
# Create a search object including a list of fields:
page_search = client.search_pages(q='cybercrime', fields='id,name,about')

# Specify DataFrame response format:        
display(page_search.query_next_page('dataframe'))
```
DataFrame response format has clear columns:


Learn more
----------


* Getting started
* Search guide
* Data dictionary
* Advanced search


































 
