<div>

<div>

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
You can perform Facebook Page searches by calling the Meta Content
Library API client\'s ` search_pages() ` method. This document describes
the ` search_pages() ` method and its syntax and parameters, and shows
how to perform basic queries using the method.

All of the examples in this document assume you have already created a
Python or R Jupyter notebook and have created a client object. See
[Getting started](/docs/content-library-api/quick-start) to learn more.

See [Data dictionary](/docs/content-library-api/data#dd-fb-page) for
detailed information about the fields that are available on a Facebook
page node.
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
This is the syntax of the ` search_pages() ` method:

``` {._5s-8 .prettyprint .lang-python}
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

::: _57-c
Parameter
:::
:::
:::

</div>

</div>

Type

Description

` Q `\
*Optional*

String

Keyword(s) to search for. Searches a Page\'s ` name ` and
` description ` fields. See [Advanced
search](/docs/content-library-api/adv-search) for information about how
multiple keyword searches with Boolean operators are handled.

` FIELDS `\
*Optional*

List

Comma-separated list of Page fields you want included in search results.
See [Data dictionary](/docs/content-library-api/data) for descriptions
of all available fields.

` CATEGORIES `\
*Optional*

List

Comma-separated list of categories to include in the search.

` IS_VERIFIED `\
*Optional*

Boolean

The verification status of the Facebook Page. A Facebook Page with a
verified badge indicates that Facebook has confirmed that it is the
authentic presence for that person or brand. [Learn
more](https://www.facebook.com/help/196050490547892) .

` WEBSITE `\
*Optional*

String

Website to match against the Facebook Page\'s \"About\" section.

` PAGE_IDS `\
*Optional*

List

Comma-separated list of Encrypted Page IDs as strings. Limits the query
to the specified Pages. Maximum of 250 Page IDs.

` ADMIN_COUNTRIES `\
*Optional*

List

Comma-separated list of countries by which to filter the Facebook
Page\'s admin. Takes ISO Alpha-2 Country Code in 2-letter uppercase
format.

` SINCE `\
*Optional*

String or Integer

Date in YYYY-MM-DD (date only) or UNIX timestamp (translates to a date
and time to the second) format. Facebook Pages created on or after this
date or timestamp are returned (used with UNTIL to define a time range).
SINCE and UNTIL are based on UTC time zone, regardless of the local time
zone of the user who created the Page.

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
and time to the second) format. Facebook Pages created on or before this
date or timestamp are returned (used with SINCE to define a time range).
SINCE and UNTIL are based on UTC time zone, regardless of the local time
zone of the user who created the Page.

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

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
To search for Pages that contain a specific keyword, create a search
object using the ` search_pages() ` method with the ` q ` parameter. See
[Advanced search](/docs/content-library-api/adv-search) for information
about how multiple keyword searches are handled.

::: _4gnb
::: {#u_0_4_ml ._4gnf ._4fa6}
``` {.prettyprint .lang-r}
# Create a client object if you have not already done so:
library(contentlibraryapi)
client <- ContentLibraryAPIClient$new(version='1')
        
# Create a search object:
page_search <- client$search_pages(q='cybercrime')        

# No results are displayed until you provide display instructions:        
print(page_search$query_next_page())
```
:::

::: {#u_0_5_DA ._4gnf ._4fa6 .hidden_elem}
``` {.prettyprint .lang-py}
# Create a client object if you have not already done so:
from contentlibraryapi import ContentLibraryAPIClient
client = ContentLibraryAPIClient.get_instance(version='1')

# Create a search object:
page_search = client.search_pages(q='cybercrime')
        
# No results are displayed until you provide display instructions:
display(page_search.query_next_page())
```
:::
:::

This example would return only 10 results per page. You can keep calling
` query_next_page() ` to get the next page of 10 results, until all the
search results have been returned. See [Search
guide](https://developers.facebook.com/docs/content-library-api/guide-search-object)
for other display and storage options.

### Request specific fields

To have the API return only specific fields on any Pages in the
response, create a search object using the ` search_pages() ` method
with the ` fields ` parameter and a comma-separated list of fields you
want included. If omitted, default fields will be returned. To more
easily see columns of data, this example specifies a DataFrame response
format (the default response format is JSON).

::: _4gnb
::: {#u_0_8_Kx ._4gnf ._4fa6}
``` {.prettyprint .lang-r}
# Create a search object including a list of fields:
page_search <- client$search_pages(q='cybercrime', fields='id,name,about')        

# Specify DataFrame response format:       
print(page_search$query_next_page('dataframe'))
```
:::

::: {#u_0_9_K6 ._4gnf ._4fa6 .hidden_elem}
``` {.prettyprint .lang-py}
# Create a search object including a list of fields:
page_search = client.search_pages(q='cybercrime', fields='id,name,about')

# Specify DataFrame response format:        
display(page_search.query_next_page('dataframe'))
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
