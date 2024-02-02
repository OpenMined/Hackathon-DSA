<div>

<div>

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
You can perform searches for Instagram posts from Instagram creator and
business accounts by calling the Meta Content Library API client\'s
` search_ig_posts() ` method. This document describes the
` search_ig_posts() ` method and its syntax and parameters, and shows
how to perform basic queries using the method.

All of the examples in this document assume you have already created a
Jupyter notebook and have created a client object. See [Getting
started](/docs/content-library-api/quick-start) to learn more.

See [Data dictionary](/docs/content-library-api/data#dd-ig-post) for
detailed information about the fields that are available on an Instagram
post node.
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
This is the syntax of the ` search_ig_posts() ` method:

``` {._5s-8 .prettyprint .lang-python}
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

The content language of the Instagram post, specified as an ISO 639-1
language code in 2-letter lowercase format.

` SINCE `\
*Optional*

String or Integer

Date in YYYY-MM-DD (date only) or UNIX timestamp (translates to a date
and time to the second) format. Instagram posts created on or after this
date or timestamp are returned (used with UNTIL to define a time range).
SINCE and UNTIL are based on UTC time zone, regardless of the local time
zone of the user who made the post.

-   If both SINCE and UNTIL are included, the search includes the time
    range defined by those values.
-   If SINCE is included and UNTIL is omitted, the search includes the
    SINCE time through the present time.
-   If SINCE is omitted and UNTIL is included, the search goes from the
    beginning of Instagram time through the UNTIL time.
-   If SINCE and UNTIL are both omitted, the search goes from the
    beginning of Instagram time to the present time.
-   If SINCE and UNTIL are the same UNIX timestamp, the search includes
    the SINCE time through the SINCE time plus one hour.
-   If SINCE and UNTIL are the same Date (YYYY-MM-DD), the search
    includes the SINCE date through the SINCE date plus one day.

` UNTIL `\
*Optional*

String or Integer

Date in YYYY-MM-DD (date only) or UNIX timestamp (translates to a date
and time to the second) format. Instagram posts created on or before
this date or timestamp are returned (used with SINCE to define a time
range). SINCE and UNTIL are based on UTC time zone, regardless of the
local time zone of the user who made the post.

-   If both SINCE and UNTIL are included, the search includes the time
    range defined by those values.
-   If SINCE is included and UNTIL is omitted, the search includes the
    SINCE time through the present time.
-   If SINCE is omitted and UNTIL is included, the search goes from the
    beginning of Instagram time through the UNTIL time.
-   If SINCE and UNTIL are both omitted, the search goes from the
    beginning of Instagram time to the present time.
-   If SINCE and UNTIL are the same UNIX timestamp, the search includes
    the SINCE time through the SINCE time plus one hour.
-   If SINCE and UNTIL are the same Date (YYYY-MM-DD), the search
    includes the SINCE date through the SINCE date plus one day.

` ACCOUNT_IDS `\
*Optional*

List

Comma-separated list of Instagram account encrypted IDs from which to
return posts. Limits the query to posts from accounts in the list.

` ACCOUNT_TYPES `\
*Optional*

List

Comma-separated list of Instagram account types. Possible values are
` creator ` and ` business ` .

` IS_BRANDED_CONTENT `\
*Optional*

Boolean

Indicates whether the Instagram posts returned can include branded
content or not. [Learn
more](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1123581461537025%2F%3Fhelpref%3Dsearch%26query%3Dbrand%2520content%26search_session_id%3Df7d00d14670ab93e032d827b36e54ff3%26sr%3D1&h=AT3uIp2y-K_Biv75RLdLUVbh63N1zodGYjYBFHdCJfMoDJ6j6ZDrcoWnIVOw5bJ5jt208gWKpJDXTHLHCqy_Cj-nypDA7StxRAufIMa6HpBQoYOBVl-gLQDqv0CZ2Lb78ManIpGznE0b4U9l)
.

` MEDIA_TYPES `\
*Optional*

List

Comma-separated list of media types to be included in the search
results. Media types include ` albums ` , ` photos ` , and ` videos `
(including reels).

` FIELDS `\
*Optional*

List

Comma-separated list of Instagram post fields to be included in search
results. See [Data dictionary](/docs/content-library-api/data) for
descriptions of all available fields.

` VIEWS_BUCKET_START `\
*Optional*

Integer

Instagram posts with view counts larger than or equal to this number
match the search criteria. Range is from 0 to the maximum of more than
100 million.

\

Views are the number of times the post or reel was on screen, not
including times it appeared on the post owner's screen. See [Data
dictionary](/docs/content-library-api/data#dd-ig-post) for more details.

` VIEWS_BUCKET_END `\
*Optional*

Integer

Instagram posts with view counts smaller than or equal to this number
match the search criteria. Range is from 0 to the maximum of more than
100 million.

\

Views are the number of times the post or reel was on screen, not
including times it appeared on the post owner's screen. See [Data
dictionary](/docs/content-library-api/data#dd-ig-post) for more details.

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
To search for all public posts from Instagram creator and business
accounts that contain a specific keyword, create a search object using
the ` search_ig_posts() ` method with the ` q ` parameter. See [Advanced
search](/docs/content-library-api/adv-search) for information about how
multiple keyword searches are handled.

::: _4gnb
::: {#u_0_4_lE ._4gnf ._4fa6}
``` {.prettyprint .lang-r}
library(contentlibraryapi)
        
# Create a client object if you have not already done so:
client <- ContentLibraryAPIClient$new(version='1')
        
# Create a search object:        
ig_post_search <- client$search_ig_posts(q='cybercrime')
        
# No results are displayed until you provide display instructions:        
print(ig_post_search$query_next_page())
```
:::
:::

This example would return only 10 results per page. You can keep calling
` query_next_page() ` to get the next page of 10 results, until all the
search results have been returned. See [Search
guide](/docs/content-library-api/guide-search-object) for other display
and storage options.

The API only returns posts from Instagram creator and business accounts
that can be returned from the ` search_ig_accounts ` endpoint.
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
To have the API return only specific fields on any Instagram posts in
the response, create a search object using the ` search_ig_posts() `
method with the ` fields ` parameter and a comma-separated list of
fields you want included. If omitted, default fields will be returned.
To more easily see columns of data, this example specifies a DataFrame
response format (the default response format is JSON).

::: _4gnb
::: {#u_0_8_Fg ._4gnf ._4fa6}
``` {.prettyprint .lang-r}
# Create a search object including a list of fields:
ig_post_search <- client$search_ig_posts(q='cybercrime', fields='id,text,creation_time')        

# Specify DataFrame response format:       
print(ig_post_search$query_next_page('dataframe'))
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
