
Facebook events - Content Library and API - Documentation - Meta for Developers










Content Library and API* Get access
* Quick links
* Content Library
* Content Library API
* Appendix
* Get help
* Citations
Guide to Facebook events data
=============================


You can perform Facebook event searches by calling the Meta Content Library API client's `search_events()` method. This document describes the `search_events()` method and its syntax and parameters, and shows how to perform basic queries using the method.


All of the examples in this document assume you have already created a Python or R Jupyter notebook and have created a client object. See Getting started to learn more.


See Data dictionary for detailed information about the fields that are available on a Facebook event node.


Recurring events
----------------


Recurring events have a parent event to which all instances of the recurring event are associated by way of the `parent_event_id`. The set of fields returned for an event search differs depending on whether the event returned is a parent or an instance (child) of the recurring event. Start and end times, for example, are specific to instances of the recurring event. The following table summarizes the differences:




 Event type | Fields returned | Fields not returned || Recurring event (the "parent" event)
(event\_type=`recurring`) | `recurring_event_ids` | `attending_count`
`declined_count`
`interested_count`
`event_start_time`
`event_end_time`
`parent_event_id` |
| Instance of recurring (the "child" event)
(event\_type=`instance_of_recurring`) | `attending_count`
`declined_count`
`interested_count`
`event_start_time`
`event_end_time`
`parent_event_id` | `recurring_event_ids` |

search\_events() method
-----------------------


This is the syntax of the `search_events()` method:



```

search_events(
    q=Q,
    event_ids=EVENT_IDS,
    fields=FIELDS,
    since=SINCE,
    until=UNTIL,
    event_since=EVENT_SINCE,
    event_until=EVENT_UNTIL  
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
| `EVENT_IDS`
*Optional* | List | A comma-separated list of encrypted event IDs as strings. Limits the query to events in the list. Maximum of 250 event IDs. |
| `FIELDS`
*Optional* | List | A comma-separated list of event fields you want included in search results. See Data dictionary for descriptions of all available fields. |
| `SINCE`
*Optional* | String or Integer | Date in YYYY-MM-DD (date only) or UNIX timestamp (translates to a date and time to the second) format. Facebook events scheduled on or after this date or timestamp are returned (used with UNTIL to define a time range). SINCE and UNTIL are based on UTC time zone, regardless of the local time zone of the user who scheduled the event.* If both SINCE and UNTIL are included, the search includes the time range defined by those values.
* If SINCE is included and UNTIL is omitted, the search includes the SINCE time through the present time.
* If SINCE is omitted and UNTIL is included, the search goes from the beginning of Facebook time through the UNTIL time.
* If SINCE and UNTIL are both omitted, the search goes from the beginning of Facebook time to the present time.
* If SINCE and UNTIL are the same UNIX timestamp, the search includes the SINCE time through the SINCE time plus one hour.
* If SINCE and UNTIL are the same Date (YYYY-MM-DD), the search includes the SINCE date through the SINCE date plus one day.
 |
| `UNTIL`
*Optional* | String or Integer | Date in YYYY-MM-DD (date only) or UNIX timestamp (translates to a date and time to the second) format. Facebook events scheduled on or before this date or timestamp are returned (used with SINCE to define a time range). SINCE and UNTIL are based on UTC time zone, regardless of the local time zone of the user who scheduled the event.* If both SINCE and UNTIL are included, the search includes the time range defined by those values.
* If SINCE is included and UNTIL is omitted, the search includes the SINCE time through the present time.
* If SINCE is omitted and UNTIL is included, the search goes from the beginning of Facebook time through the UNTIL time.
* If SINCE and UNTIL are both omitted, the search goes from the beginning of Facebook time to the present time.
* If SINCE and UNTIL are the same UNIX timestamp, the search includes the SINCE time through the SINCE time plus one hour.
* If SINCE and UNTIL are the same Date (YYYY-MM-DD), the search includes the SINCE date through the SINCE date plus one day.
 |
| `EVENT_SINCE`
*Optional* | String or Integer | Date in YYYY-MM-DD (date only) or UNIX timestamp (translates to a date and time to the second) format. Facebook events started on or after this date or timestamp are returned (used with EVENT\_UNTIL to define a time range). EVENT\_SINCE and EVENT\_UNTIL are based on UTC time zone, regardless of the local time zone of the user who started the event.* If both EVENT\_SINCE and EVENT\_UNTIL are included, the search includes the time range defined by those values.
* If EVENT\_SINCE is included and EVENT\_UNTIL is omitted, the search includes the EVENT\_SINCE time through the present time.
* If EVENT\_SINCE is omitted and EVENT\_UNTIL is included, the search goes from the beginning of Facebook time through the EVENT\_UNTIL time.
* If EVENT\_SINCE and EVENT\_UNTIL are both omitted, the search goes from the beginning of Facebook time to the present time.
* If EVENT\_SINCE and EVENT\_UNTIL are the same UNIX timestamp, the search includes the EVENT\_SINCE time through the EVENT\_SINCE time plus one hour.
* If EVENT\_SINCE and EVENT\_UNTIL are the same Date (YYYY-MM-DD), the search includes the EVENT\_SINCE date through the EVENT\_SINCE date plus one day.
 |
| `EVENT_UNTIL`
*Optional* | String or Integer | Date in YYYY-MM-DD (date only) or UNIX timestamp (translates to a date and time to the second) format. Facebook events started on or before this date or timestamp are returned (used with EVENT\_SINCE to define a time range). EVENT\_SINCE and EVENT\_UNTIL are based on UTC time zone, regardless of the local time zone of the user who started the event.* If both EVENT\_SINCE and EVENT\_UNTIL are included, the search includes the time range defined by those values.
* If EVENT\_SINCE is included and EVENT\_UNTIL is omitted, the search includes the EVENT\_SINCE time through the present time.
* If EVENT\_SINCE is omitted and EVENT\_UNTIL is included, the search goes from the beginning of Facebook time through the EVENT\_UNTIL time.
* If EVENT\_SINCE and EVENT\_UNTIL are both omitted, the search goes from the beginning of Facebook time to the present time.
* If EVENT\_SINCE and EVENT\_UNTIL are the same EVENT\_UNIX timestamp, the search includes the EVENT\_SINCE time through the EVENT\_SINCE time plus one hour.
* If EVENT\_SINCE and EVENT\_UNTIL are the same Date (YYYY-MM-DD), the search includes the EVENT\_SINCE date through the EVENT\_SINCE date plus one day.
 |

Sample queries
--------------


### Search for events by keyword


To search for public events that contain specific keywords, create a search object using the `search_events()` method with the `q` parameter. See Advanced search for information about how multiple keyword searches are handled.


RPython
```
library(contentlibraryapi)
        
# Create a client object if you have not already done so:
client <- ContentLibraryAPIClient$new(version='1')
        
# Create a search object:        
event_search <- client$search_events(q='cybercrime')
        
# No results are displayed until you provide display instructions:        
print(event_search$query_next_page())
```

```
from contentlibraryapi import ContentLibraryAPIClient

# Create a client object if you have not already done so:
client = ContentLibraryAPIClient.get_instance(version='1')

# Create a search object:
event_search = client.search_events(q="cybercrime")
        
# No results are displayed until you provide display instructions:
display(event_search.query_next_page())
```
This example would return only 10 results per page. You can keep calling `query_next_page()` to get the next page of 10 results, until all the search results have been returned. See Search guide for other display and storage options.


### Request specific fields


To have the API return only specific fields on any events in the response, create a search object using the `search_events()` method with the `fields` parameter and a comma-separated list of fields you want included. If omitted, default fields will be returned. To more easily see columns of data, this example specifies a DataFrame response format (the default response format is JSON).


RPython
```
# Create a search object including a list of fields:
event_search <- client$search_events(q='cybercrime', fields='id,name,description')        

# Specify DataFrame response format:       
print(event_search$query_next_page('dataframe'))
```

```
# Create a search object including a list of fields:
event_search = client.search_events(q='cybercrime', fields='id,name,description')

# Specify DataFrame response format:        
display(event_search.query_next_page('dataframe'))
```
DataFrame response format has clear columns:


Learn more
----------


* Getting started
* Search guide
* Data dictionary
* Advanced search


































 
