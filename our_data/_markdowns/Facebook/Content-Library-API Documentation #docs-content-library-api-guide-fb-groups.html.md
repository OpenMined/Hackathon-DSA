Facebook groups - Content Library and API - Documentation - Meta for Developers

Content Library and API* Get access
* Quick links
* Content Library
* Content Library API
* Appendix
* Get help
* Citations
Guide to Facebook groups data
=============================

You can perform Facebook group searches by calling the Meta Content Library API client's `search_groups()` method. This document describes the `search_groups()` method and its syntax and parameters, and shows how to perform basic queries using the method.

All of the examples in this document assume you have already created a Python or R Jupyter notebook and have created a client object. See Getting started to learn more.

See Data dictionary for detailed information about the fields that are available on a Facebook group node.

search\_groups() method
-----------------------

This is the syntax of the `search_groups()` method:

```
search_groups(
    q=Q
    fields=FIELDS,
    group_ids=GROUP_IDS,
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
*Optional* | String | Keyword(s) to search for. See Advanced search guidelines for information about how multiple keyword searches with Boolean operators are handled. |
| `FIELDS`
*Optional* | List | A comma-separated list of group fields you want included in search results. See Data dictionary for descriptions of all available fields. |
| `GROUP_IDS`
*Optional* | List | A comma-separated list of Meta Content Library group IDs as strings. Limits the query to groups in the list. Maximum of 250 IDs. |
| `SINCE`
*Optional* | String or Integer | Date in YYYY-MM-DD (date only) or UNIX timestamp (translates to a date and time to the second) format. Facebook groups created on or after this date or timestamp are returned (used with UNTIL to define a time range). SINCE and UNTIL are based on UTC time zone, regardless of the local time zone of the user who created the group.* If both SINCE and UNTIL are included, the search includes the time range defined by those values.
* If SINCE is included and UNTIL is omitted, the search includes the SINCE time through the present time.
* If SINCE is omitted and UNTIL is included, the search goes from the beginning of Facebook time through the UNTIL time.
* If SINCE and UNTIL are both omitted, the search goes from the beginning of Facebook time to the present time.
* If SINCE and UNTIL are the same UNIX timestamp, the search includes the SINCE time through the SINCE time plus one hour.
* If SINCE and UNTIL are the same Date (YYYY-MM-DD), the search includes the SINCE date through the SINCE date plus one day.
 |
| `UNTIL`
*Optional* | String or Integer | Date in YYYY-MM-DD (date only) or UNIX timestamp (translates to a date and time to the second) format. Facebook groups created on or before this date or timestamp are returned (used with SINCE to define a time range). SINCE and UNTIL are based on UTC time zone, regardless of the local time zone of the user who created the group.* If both SINCE and UNTIL are included, the search includes the time range defined by those values.
* If SINCE is included and UNTIL is omitted, the search includes the SINCE time through the present time.
* If SINCE is omitted and UNTIL is included, the search goes from the beginning of Facebook time through the UNTIL time.
* If SINCE and UNTIL are both omitted, the search goes from the beginning of Facebook time to the present time.
* If SINCE and UNTIL are the same UNIX timestamp, the search includes the SINCE time through the SINCE time plus one hour.
* If SINCE and UNTIL are the same Date (YYYY-MM-DD), the search includes the SINCE date through the SINCE date plus one day.
 |
Sample queries
--------------

### Search for groups by keyword

To search for public groups that contain specific keywords, create a search object using the `search_groups()` method with the `q` parameter. See Advanced search guidelines for information about how multiple keyword searches are handled.

RPython
```
library(contentlibraryapi)
# Create a client object if you have not already done so:
client <- ContentLibraryAPIClient$new(version='2')
# Create a search object:        
group_search <- client$search_groups(q='cybercrime')
# No results are displayed until you provide display instructions:        
print(group_search$query_next_page())
```
```
from contentlibraryapi import ContentLibraryAPIClient
# Create a client object if you have not already done so:
client = ContentLibraryAPIClient.get_instance(version='2')
# Create a search object:
group_search = client.search_groups(q="cybercrime")
# No results are displayed until you provide display instructions:
display(group_search.query_next_page())
```
This example would return only 10 results per page. You can keep calling `query_next_page()` to get the next page of 10 results, until all the search results have been returned. See Search guide for other display and storage options.

### Request specific fields

To have the API return only specific fields on any groups in the response, create a search object using the `search_groups()` method with the `fields` parameter and a comma-separated list of fields you want included. If omitted, default fields will be returned. To more easily see columns of data, this example specifies a DataFrame response format (the default response format is JSON).

RPython
```
# Create a search object including a list of fields:
group_search <- client$search_groups(q='cybercrime', fields='id,name,description')        
# Specify DataFrame response format:       
print(group_search$query_next_page('dataframe'))
```
```
# Create a search object including a list of fields:
group_search = client.search_groups(q='cybercrime', fields='id,name,description')
# Specify DataFrame response format:        
display(group_search.query_next_page('dataframe'))
```
DataFrame response format has clear columns:

### Search for groups by group ID

You can search for Facebook groups using specific group IDs obtained from previous group searches.

To get data on specific Facebook groups that contain specific keywords or phrases, create a search object using the `search_groups()` method with the `q` parameter (specifying the keywords or phrases) and the `group_ids` parameter (specifying the list of group IDs you want included). If you omit the `q` argument, all groups in the list of IDs are included, not just those with a specific keyword or phrase.

RPython
```
# Create a search object limiting the response to specific group IDs 
        group_search <- client$search_groups(q=`blackpink`, group_ids=[`753110959566351`], fields=`id,name,creation_date`)
```
```
# Create a search object limiting the response to specific group IDs 
        group_search=client.search_groups(q=`blackpink`, group_ids=[`753110959566351`], fields=`id,name,creation_date`)
```
For using group IDs to search for posts from specific Facebook groups, see Guide to Facebook posts data.

Learn more
----------

* Getting started
* Search guide
* Data dictionary
* Advanced search guidelines
* Guide to Facebook posts data