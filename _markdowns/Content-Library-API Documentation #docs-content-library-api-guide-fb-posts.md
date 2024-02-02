<div>

<div>

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
You can perform Facebook post searches by calling the Meta Content
Library API client\'s ` search_posts() ` method. This document describes
the ` search_posts() ` method and its syntax and parameters, and shows
how to perform basic queries using the method.

All of the examples in this document assume you have already created a
Jupyter notebook and have created a client object. See [Getting
started](/docs/content-library-api/quick-start) to learn more.

See [Data dictionary](/docs/content-library-api/data#post) for detailed
information about the fields that are available on a Facebook post node.
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
This is the syntax of the ` search_posts() ` method:

``` {._5s-8 .prettyprint .lang-python}
search_posts(
    q=Q,
    lang=LANG,
    since=SINCE,
    until=UNTIL,      
    fields=FIELDS,
    link=LINK,
    is_branded_content=IS_BRANDED_CONTENT,
    page_ids=PAGE_IDS,
    group_ids=GROUP_IDS,
    event_ids=EVENT_IDS,
    owner_types=OWNER_TYPES,
    views_bucket_start=VIEWS_BUCKET_START,
    views_bucket_end=VIEWS_BUCKET_END
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

Keyword(s) to search for. See [Advanced
search](/docs/content-library-api/adv-search) for information about how
multiple keyword searches with Boolean operators are handled.

` LANG `\
*Optional*

String

The content language of the Facebook post, specified as an ISO 639-1
language code in 2-letter lowercase format.

` SINCE `\
*Optional*

String or Integer

Date in YYYY-MM-DD (date only) or UNIX timestamp (translates to a date
and time to the second) format. Facebook posts created on or after this
date or timestamp are returned (used with UNTIL to define a time range).
SINCE and UNTIL are based on UTC time zone, regardless of the local time
zone of the user who made the post.

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
and time to the second) format. Facebook posts created on or before this
date or timestamp are returned (used with SINCE to define a time range).
SINCE and UNTIL are based on UTC time zone, regardless of the local time
zone of the user who made the post.

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

` FIELDS `\
*Optional*

List

Comma-separated list of Facebook post fields you want included in search
results. See [Data dictionary](/docs/content-library-api/data) for
descriptions of all available fields.

` LINK `\
*Optional with the ` q ` parameter*

String

Posts containing the specified URL are included in search results. All
forms of the URL that point to the same piece of content will be
returned.

\

Usage:

-   Can only be used with the ` q ` parameter.
-   Returns posts from exact matches only.
-   Searching for multiple URLs in one query is not supported.

::: {._57yz ._57z1 ._3-8p}
::: _57y-
**If you want to search all posts from a domain, the ` link ` parameter
is not the best option since it returns posts from exact matches only.**

Instead, you can use the ` q ` parameter where q= *url* . Results would
include all posts in which the value of ` q ` is at least a part of the
URL in the post. For example, posts from cnn.com/entertainment would be
included in a search for cnn.com. Once you have the larger set of
results, you can write Python or R code in your Jupyter environment to
narrow them down.
:::
:::

` IS_BRANDED_CONTENT `\
*Optional*

Boolean

Indicates whether the Facebook posts returned can include branded
content or not. [Learn
more](https://www.facebook.com/business/help/788160621327601?id=1912903575666924&content_id=OESWySYCNR5UDZX&ref=sem_smb&utm_term=dsa-1731453251743&gclid=CjwKCAjwtuOlBhBREiwA7agf1uNvtkdQIU-GlDHtOVsq1r2PAFq7Z7QFVqHPf4QsH54oi0soVculuxoCMHMQAvD_BwE)
.

` PAGE_IDS `\
*Optional*

List

Comma-separated list of encrypted page IDs as strings. Limits the query
to pages in the list. Maximum of 250 page IDs.

` Group_IDS `\
*Optional*

List

Comma-separated list of encrypted group IDs as strings. Limits the query
to groups in the list. Maximum of 250 group IDs.

` EVENT_IDS `\
*Optional*

List

Comma-separated list of encrypted event IDs as strings. Limits the query
to events in the list. Maximum of 250 event IDs.

` OWNER_TYPES `\
*Optional*

List

Comma-separated list of owner types to be included in the search
results. Possible values are ` page ` , ` group ` and ` event ` .

` VIEWS_BUCKET_START `\
*Optional*

Integer

Facebook posts with view counts larger than or equal to this number
match the search criteria. Range is from 0 to the maximum of more than
100 million. Used with ` VIEWS_BUCKET_END ` to define a range.

\

Views are the number of times the post or reel was on screen, not
including times it appeared on the post owner's screen. See [Data
Dictionary](/docs/content-library-api/data#facebook-post) for more
details.

` VIEWS_BUCKET_END ` *Optional*

Integer

Facebook posts with view counts smaller than or equal to this number
match the search criteria. Range is from 0 to the maximum of more than
100 million. Used with ` VIEWS_BUCKET_START ` to define a range.

\

Views are the number of times the post or reel was on screen, not
including times it appeared on the post owner's screen. See [Data
dictionary](/docs/content-library-api/data#facebook-post) for more
details.

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
To search for all public posts on Facebook Pages, groups, and events
that contain specific keywords, create a search object using the
` search_posts() ` method with the ` q ` parameter. See [Advanced
search](/docs/content-library-api/adv-search) for information about how
multiple keyword searches are handled.

::: _4gnb
::: {#u_0_4_EN ._4gnf ._4fa6}
``` {.prettyprint .lang-r}
library(contentlibraryapi)
        
# Create a client object if you have not already done so:
client <- ContentLibraryAPIClient$new(version='1')
        
# Create a search object:        
post_search <- client$search_posts(q='cybercrime')
        
# No results are displayed until you provide display instructions:        
print(post_search$query_next_page())
```
:::
:::

This example would return only 10 results per page. You can keep calling
` query_next_page() ` to get the next page of 10 results, until all the
search results have been returned. See [Search
guide](/docs/content-library-api/guide-search-object) for other display
and storage options.

The API only returns posts from Facebook Pages, groups, or events that
can be returned on their respective endpoints ( ` search_pages() ` ,
` search_groups() ` , ` search_events() ` ).
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
To have the API return only specific fields on any Facebook posts in the
response, create a search object using the ` search_posts() ` method
with the ` fields ` parameter and a comma-separated list of fields you
want included. If omitted, default fields will be returned. To more
easily see columns of data, this example specifies a DataFrame response
format (the default response format is JSON).

::: _4gnb
::: {#u_0_8_gK ._4gnf ._4fa6}
``` {.prettyprint .lang-r}
# Create a search object including a list of fields:
post_search <- client$search_posts(q='cybercrime', fields='id,text,lang')        

# Specify DataFrame response format:       
print(post_search$query_next_page('dataframe'))
```
:::
:::

DataFrame response format has clear columns:

![](https://scontent-cdg4-3.xx.fbcdn.net/v/t39.8562-6/361588460_224466613889350_7431544641123459816_n.png?_nc_cat=111&ccb=1-7&_nc_sid=f537c7&_nc_ohc=UqeYaOBAv0QAX-K_AU7&_nc_ht=scontent-cdg4-3.xx&oh=00_AfDCWzxyYUIceZUSedc6yx1t3I-0aYAkcd-3wsDU4MFivw&oe=65AB80BA){.img
srcset="https://scontent-cdg4-3.xx.fbcdn.net/v/t39.8562-6/361588460_224466613889350_7431544641123459816_n.png?_nc_cat=111&ccb=1-7&_nc_sid=f537c7&_nc_ohc=UqeYaOBAv0QAX-K_AU7&_nc_ht=scontent-cdg4-3.xx&oh=00_AfDCWzxyYUIceZUSedc6yx1t3I-0aYAkcd-3wsDU4MFivw&oe=65AB80BA"}

### Search for Facebook posts containing a specific URL

To search for all public posts on Facebook Pages, groups, and events
that contain specific keywords and a specific URL, create a search
object using the ` search_posts() ` method with the ` q ` and ` link `
parameters. The ` link ` parameter cannot be used without the ` q `
parameter. See [Advanced search](/docs/content-library-api/adv-search)
for information about how multiple keyword searches are handled.

All forms of the URL that point to the same piece of content will be
returned. Searching for multiple URLs in one query is not supported.

::: _4gnb
::: {#u_0_c_6/ ._4gnf ._4fa6}
``` {.prettyprint .lang-r}
# Create a search object including both the `q` and `link` parameters:
        
post_search <- client$search_posts(q="nike", link="nike.com")
print(post_search$query_next_page('dataframe'))
```
:::
:::
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
## Learn more

-   [Getting started](/docs/content-library-api/quick-start)
-   [Search guide](/docs/content-library-api/guide-search-object)
-   [Data dictionary](/docs/content-library-api/data)
-   [Advanced search](/docs/content-library-api/adv-search)
:::
