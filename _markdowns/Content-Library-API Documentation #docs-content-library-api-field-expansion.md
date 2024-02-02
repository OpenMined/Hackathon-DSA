
Field expansion - Content Library and API - Documentation - Meta for Developers









Content Library and API* Get access
* Quick links
* Content Library
* Content Library API
* Appendix
* Get help
* Citations
Field expansion
===============


There are a number of fields in the data available through the Meta Content Library API that are nested. For example, the `statistics` field contains the `like_count`, `haha_count`, and several other fields. When you create search objects, you might want to include some or all of the nested fields in your search. *Field expansion* allows you to perform queries for multiple fields and their nested fields in a single call. We refer to the nested fields as *expanded fields*.


In the Data dictionary, expanded fields are indicated by a dot notation. For example, `statistics.like_count` indicates that `like_count` is available within `statistics`. To specify expanded fields in your search objects, you can either use this dot notation or you can append the names of the expanded fields in curly braces after the parent field. See the examples in this section.


Specifying multiple fields
--------------------------


You can specify which multiple fields you want returned on any associated data by using the `fields` parameter, with the field names separated by commas.


RPython
```
library(contentlibraryapi)
client <- ContentLibraryAPIClient$new(version='1')
        
post_search <- client$search_posts(q='cybercrime', fields="id,text")
post_search$query_next_page()
```

```
from contentlibraryapi import ContentLibraryAPIClient
client = ContentLibraryAPIClient.get_instance(version='1')


post_search = client.search_posts(q="cybercrime", fields="id,text")
display(post_search.query_next_page())
```
Specifying expanded fields
--------------------------


You can specify which expanded fields you want returned on any associated data by using the dot notation in your query to specify first the parent field, then the expanded field (such as `statistics.haha_count`).


RPython
```
post_search <- client$search_posts(q='cybercrime', fields="id,statistics.like_count,statistics.haha_count")
post_search$query_next_page()
```

```
post_search = client.search_posts(q="cybercrime", fields="id,statistics.like_count,statistics.haha_count")
display(post_search.query_next_page())
```
Alternatively, you can append a comma-separated list of expanded field names wrapped in curly braces to the end of any parent field name.


RPython
```
post_search <- client$search_posts(q='cybercrime', fields="id,statistics{like_count,haha_count}")
post_search$query_next_page()
```

```
post_search = client.search_posts(q="cybercrime", fields="id,statistics{like_count,haha_count}")
display(post_search.query_next_page())
```
If you specify a field but do not specify any of its expanded fields, default expanded fields on the associated node are included in the response. If you omit the `fields` parameter altogether, default expanded fields on default parent fields on the associated data are included in the response.


Learn more
----------


* Data dictionary


































 
