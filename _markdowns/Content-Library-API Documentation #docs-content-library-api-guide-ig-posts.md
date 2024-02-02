
Instagram posts - Content Library and API - Documentation - Meta for Developers










Content Library and API* Get access
* Quick links
* Content Library
* Content Library API
* Appendix
* Get help
* Citations
Guide to Instagram posts data
=============================


You can perform searches for Instagram posts from Instagram creator and business accounts by calling the Meta Content Library API client's `search_ig_posts()` method. This document describes the `search_ig_posts()` method and its syntax and parameters, and shows how to perform basic queries using the method.


All of the examples in this document assume you have already created a Jupyter notebook and have created a client object. See Getting started to learn more.


See Data dictionary for detailed information about the fields that are available on an Instagram post node.


search\_ig\_posts() method
--------------------------


This is the syntax of the `search_ig_posts()` method:



```

search_posts(
    q=Q,
    lang=LANG,
    since=SINCE,
    until=UNTIL,      
    account_ids=ACCOUNT_IDS,
    account_types=ACCOUNT_TYPES,
    is_branded_content=IS_BRANDED_CONTENT,
    media_types=MEDIA_TYPES,
    fields=FIELDS,   
    views_bucket_start=VIEWS_BUCKET_START,
    views_bucket_end=VIEWS_BUCKET_END
)
```
The following table describes the parameters:




 
 Parameter
  | 
 Type
  | 
 Description
  || `Q`
*Optional* | String | Keyword(s) to search for. See Advanced search for information about how multiple keyword searches with Boolean operators are handled. |
| `LANG`
*Optional* | String | The content language of the Instagram post, specified as an ISO 639-1 language code in 2-letter lowercase format. |
| `SINCE`
*Optional* | String or Integer | Date in YYYY-MM-DD (date only) or UNIX timestamp (translates to a date and time to the second) format. Instagram posts created on or after this date or timestamp are returned (used with UNTIL to define a time range). SINCE and UNTIL are based on UTC time zone, regardless of the local time zone of the user who made the post.* If both SINCE and UNTIL are included, the search includes the time range defined by those values.
* If SINCE is included and UNTIL is omitted, the search includes the SINCE time through the present time.
* If SINCE is omitted and UNTIL is included, the search goes from the beginning of Instagram time through the UNTIL time.
* If SINCE and UNTIL are both omitted, the search goes from the beginning of Instagram time to the present time.
* If SINCE and UNTIL are the same UNIX timestamp, the search includes the SINCE time through the SINCE time plus one hour.
* If SINCE and UNTIL are the same Date (YYYY-MM-DD), the search includes the SINCE date through the SINCE date plus one day.
 |
| `UNTIL`
*Optional* | String or Integer | Date in YYYY-MM-DD (date only) or UNIX timestamp (translates to a date and time to the second) format. Instagram posts created on or before this date or timestamp are returned (used with SINCE to define a time range). SINCE and UNTIL are based on UTC time zone, regardless of the local time zone of the user who made the post.* If both SINCE and UNTIL are included, the search includes the time range defined by those values.
* If SINCE is included and UNTIL is omitted, the search includes the SINCE time through the present time.
* If SINCE is omitted and UNTIL is included, the search goes from the beginning of Instagram time through the UNTIL time.
* If SINCE and UNTIL are both omitted, the search goes from the beginning of Instagram time to the present time.
* If SINCE and UNTIL are the same UNIX timestamp, the search includes the SINCE time through the SINCE time plus one hour.
* If SINCE and UNTIL are the same Date (YYYY-MM-DD), the search includes the SINCE date through the SINCE date plus one day.
 |
| `ACCOUNT_IDS`
*Optional* | List | Comma-separated list of Instagram account encrypted IDs from which to return posts. Limits the query to posts from accounts in the list. |
| `ACCOUNT_TYPES`
*Optional* | List | Comma-separated list of Instagram account types. Possible values are `creator` and `business`. |
| `IS_BRANDED_CONTENT`
*Optional* | Boolean |  Indicates whether the Instagram posts returned can include branded content or not. Learn more. |
| `MEDIA_TYPES`
*Optional* | List | Comma-separated list of media types to be included in the search results. Media types include `albums`, `photos`, and `videos` (including reels). |
| `FIELDS`
*Optional* | List | Comma-separated list of Instagram post fields to be included in search results. See Data dictionary for descriptions of all available fields. |
| `VIEWS_BUCKET_START`
*Optional* | Integer | Instagram posts with view counts larger than or equal to this number match the search criteria. Range is from 0 to the maximum of more than 100 million.
Views are the number of times the post or reel was on screen, not including times it appeared on the post owner’s screen. See Data dictionary for more details. |
| `VIEWS_BUCKET_END`
*Optional* | Integer | Instagram posts with view counts smaller than or equal to this number match the search criteria. Range is from 0 to the maximum of more than 100 million.
Views are the number of times the post or reel was on screen, not including times it appeared on the post owner’s screen. See Data dictionary for more details. |

Sample Queries
--------------


### Search for Instagram posts by keyword


To search for all public posts from Instagram creator and business accounts that contain a specific keyword, create a search object using the `search_ig_posts()` method with the `q` parameter. See Advanced search for information about how multiple keyword searches are handled.


RPython
```
library(contentlibraryapi)
        
# Create a client object if you have not already done so:
client <- ContentLibraryAPIClient$new(version='1')
        
# Create a search object:        
ig_post_search <- client$search_ig_posts(q='cybercrime')
        
# No results are displayed until you provide display instructions:        
print(ig_post_search$query_next_page())
```

```
from contentlibraryapi import ContentLibraryAPIClient

# Create a client object if you have not already done so:
client = ContentLibraryAPIClient.get_instance(version='1')

# Create a search object:
if_post_search = client.search_ig_posts(q="cybercrime")
        
# No results are displayed until you provide display instructions:
display(ig_post_search.query_next_page())
```
This example would return only 10 results per page. You can keep calling `query_next_page()` to get the next page of 10 results, until all the search results have been returned. See Search guide for other display and storage options.


The API only returns posts from Instagram creator and business accounts that can be returned from the `search_ig_accounts` endpoint.


### Request specific fields


To have the API return only specific fields on any Instagram posts in the response, create a search object using the `search_ig_posts()` method with the `fields` parameter and a comma-separated list of fields you want included. If omitted, default fields will be returned. To more easily see columns of data, this example specifies a DataFrame response format (the default response format is JSON).


RPython
```
# Create a search object including a list of fields:
ig_post_search <- client$search_ig_posts(q='cybercrime', fields='id,text,creation_time')        

# Specify DataFrame response format:       
print(ig_post_search$query_next_page('dataframe'))
```

```
# Create a search object including a list of fields:
ig_post_search = client.search_ig_posts(q='cybercrime', fields='id,text,creation_time')

# Specify DataFrame response format:        
display(ig_post_search.query_next_page('dataframe'))
```
DataFrame response format has clear columns:


Learn more
----------


* Getting started
* Search guide
* Data dictionary
* Advanced search


































 
