<div>

<div>

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
You can perform Facebook event searches by calling the Meta Content
Library API client\'s ` search_events() ` method. This document
describes the ` search_events() ` method and its syntax and parameters,
and shows how to perform basic queries using the method.

All of the examples in this document assume you have already created a
Python or R Jupyter notebook and have created a client object. See
[Getting started](/docs/content-library-api/quick-start) to learn more.

See [Data dictionary](/docs/content-library-api/data#dd-fb-event) for
detailed information about the fields that are available on a Facebook
event node.
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
Recurring events have a parent event to which all instances of the
recurring event are associated by way of the ` parent_event_id ` . The
set of fields returned for an event search differs depending on whether
the event returned is a parent or an instance (child) of the recurring
event. Start and end times, for example, are specific to instances of
the recurring event. The following table summarizes the differences:

::: _57-c
Event type
:::
:::
:::

</div>

</div>

Fields returned

Fields not returned

Recurring event (the \"parent\" event) (event_type= ` recurring ` )

` recurring_event_ids `

` attending_count `

` declined_count `

` interested_count `

` event_start_time `

` event_end_time `

` parent_event_id `

Instance of recurring (the \"child\" event) (event_type=
` instance_of_recurring ` )

` attending_count `

` declined_count `

` interested_count `

` event_start_time `

` event_end_time `

` parent_event_id `

` recurring_event_ids `

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
This is the syntax of the ` search_events() ` method:

``` {._5s-8 .prettyprint .lang-python}
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

::: _57-c
Parameter
:::
:::
:::

Type

Description

` Q `\
*Optional*

String

Keyword(s) to search for. See [Advanced
search](/docs/content-library-api/adv-search) for information about how
multiple keyword searches with Boolean operators are handled.

` EVENT_IDS `\
*Optional*

List

A comma-separated list of encrypted event IDs as strings. Limits the
query to events in the list. Maximum of 250 event IDs.

` FIELDS `\
*Optional*

List

A comma-separated list of event fields you want included in search
results. See [Data dictionary](/docs/content-library-api/data) for
descriptions of all available fields.

` SINCE `\
*Optional*

String or Integer

Date in YYYY-MM-DD (date only) or UNIX timestamp (translates to a date
and time to the second) format. Facebook events scheduled on or after
this date or timestamp are returned (used with UNTIL to define a time
range). SINCE and UNTIL are based on UTC time zone, regardless of the
local time zone of the user who scheduled the event.

-   If both SINCE and UNTIL are included, the search includes the time
    range defined by those values.
-   If SINCE is included and UNTIL is omitted, the search includes the
    SINCE time through the present time.
-   If SINCE is omitted and UNTIL is included, the search goes from the
    beginning of Facebook time through the UNTIL time.
-   If SINCE and UNTIL are both omitted, the search goes from the
    beginning of Facebook time to the present time.
-   If SINCE and UNTIL are the same UNIX timestamp, the search includes
    the SINCE time through the SINCE time plus one hour.
-   If SINCE and UNTIL are the same Date (YYYY-MM-DD), the search
    includes the SINCE date through the SINCE date plus one day.

` UNTIL `\
*Optional*

String or Integer

Date in YYYY-MM-DD (date only) or UNIX timestamp (translates to a date
and time to the second) format. Facebook events scheduled on or before
this date or timestamp are returned (used with SINCE to define a time
range). SINCE and UNTIL are based on UTC time zone, regardless of the
local time zone of the user who scheduled the event.

-   If both SINCE and UNTIL are included, the search includes the time
    range defined by those values.
-   If SINCE is included and UNTIL is omitted, the search includes the
    SINCE time through the present time.
-   If SINCE is omitted and UNTIL is included, the search goes from the
    beginning of Facebook time through the UNTIL time.
-   If SINCE and UNTIL are both omitted, the search goes from the
    beginning of Facebook time to the present time.
-   If SINCE and UNTIL are the same UNIX timestamp, the search includes
    the SINCE time through the SINCE time plus one hour.
-   If SINCE and UNTIL are the same Date (YYYY-MM-DD), the search
    includes the SINCE date through the SINCE date plus one day.

` EVENT_SINCE `\
*Optional*

String or Integer

Date in YYYY-MM-DD (date only) or UNIX timestamp (translates to a date
and time to the second) format. Facebook events started on or after this
date or timestamp are returned (used with EVENT_UNTIL to define a time
range). EVENT_SINCE and EVENT_UNTIL are based on UTC time zone,
regardless of the local time zone of the user who started the event.

-   If both EVENT_SINCE and EVENT_UNTIL are included, the search
    includes the time range defined by those values.
-   If EVENT_SINCE is included and EVENT_UNTIL is omitted, the search
    includes the EVENT_SINCE time through the present time.
-   If EVENT_SINCE is omitted and EVENT_UNTIL is included, the search
    goes from the beginning of Facebook time through the EVENT_UNTIL
    time.
-   If EVENT_SINCE and EVENT_UNTIL are both omitted, the search goes
    from the beginning of Facebook time to the present time.
-   If EVENT_SINCE and EVENT_UNTIL are the same UNIX timestamp, the
    search includes the EVENT_SINCE time through the EVENT_SINCE time
    plus one hour.
-   If EVENT_SINCE and EVENT_UNTIL are the same Date (YYYY-MM-DD), the
    search includes the EVENT_SINCE date through the EVENT_SINCE date
    plus one day.

` EVENT_UNTIL `\
*Optional*

String or Integer

Date in YYYY-MM-DD (date only) or UNIX timestamp (translates to a date
and time to the second) format. Facebook events started on or before
this date or timestamp are returned (used with EVENT_SINCE to define a
time range). EVENT_SINCE and EVENT_UNTIL are based on UTC time zone,
regardless of the local time zone of the user who started the event.

-   If both EVENT_SINCE and EVENT_UNTIL are included, the search
    includes the time range defined by those values.
-   If EVENT_SINCE is included and EVENT_UNTIL is omitted, the search
    includes the EVENT_SINCE time through the present time.
-   If EVENT_SINCE is omitted and EVENT_UNTIL is included, the search
    goes from the beginning of Facebook time through the EVENT_UNTIL
    time.
-   If EVENT_SINCE and EVENT_UNTIL are both omitted, the search goes
    from the beginning of Facebook time to the present time.
-   If EVENT_SINCE and EVENT_UNTIL are the same EVENT_UNIX timestamp,
    the search includes the EVENT_SINCE time through the EVENT_SINCE
    time plus one hour.
-   If EVENT_SINCE and EVENT_UNTIL are the same Date (YYYY-MM-DD), the
    search includes the EVENT_SINCE date through the EVENT_SINCE date
    plus one day.

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
To search for public events that contain specific keywords, create a
search object using the ` search_events() ` method with the ` q `
parameter. See [Advanced search](/docs/content-library-api/adv-search)
for information about how multiple keyword searches are handled.

::: _4gnb
::: {#u_0_5_e3 ._4gnf ._4fa6}
``` {.prettyprint .lang-r}
library(contentlibraryapi)
        
# Create a client object if you have not already done so:
client <- ContentLibraryAPIClient$new(version='1')
        
# Create a search object:        
event_search <- client$search_events(q='cybercrime')
        
# No results are displayed until you provide display instructions:        
print(event_search$query_next_page())
```
:::
:::

This example would return only 10 results per page. You can keep calling
` query_next_page() ` to get the next page of 10 results, until all the
search results have been returned. See [Search
guide](/docs/content-library-api/guide-search-object) for other display
and storage options.
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
To have the API return only specific fields on any events in the
response, create a search object using the ` search_events() ` method
with the ` fields ` parameter and a comma-separated list of fields you
want included. If omitted, default fields will be returned. To more
easily see columns of data, this example specifies a DataFrame response
format (the default response format is JSON).

::: _4gnb
::: {#u_0_9_I5 ._4gnf ._4fa6}
``` {.prettyprint .lang-r}
# Create a search object including a list of fields:
event_search <- client$search_events(q='cybercrime', fields='id,name,description')        

# Specify DataFrame response format:       
print(event_search$query_next_page('dataframe'))
```
:::
:::

DataFrame response format has clear columns:

![](https://scontent-cdg4-3.xx.fbcdn.net/v/t39.8562-6/361588460_224466613889350_7431544641123459816_n.png?_nc_cat=111&ccb=1-7&_nc_sid=f537c7&_nc_ohc=UqeYaOBAv0QAX-K_AU7&_nc_ht=scontent-cdg4-3.xx&oh=00_AfDCWzxyYUIceZUSedc6yx1t3I-0aYAkcd-3wsDU4MFivw&oe=65AB80BA){.img
srcset="https://scontent-cdg4-3.xx.fbcdn.net/v/t39.8562-6/361588460_224466613889350_7431544641123459816_n.png?_nc_cat=111&ccb=1-7&_nc_sid=f537c7&_nc_ohc=UqeYaOBAv0QAX-K_AU7&_nc_ht=scontent-cdg4-3.xx&oh=00_AfDCWzxyYUIceZUSedc6yx1t3I-0aYAkcd-3wsDU4MFivw&oe=65AB80BA"}
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
## Learn more

-   [Getting started](/docs/content-library-api/quick-start)
-   [Search guide](/docs/content-library-api/guide-search-object)
-   [Data dictionary](/docs/content-library-api/data)
-   [Advanced search](/docs/content-library-api/adv-search)
:::
