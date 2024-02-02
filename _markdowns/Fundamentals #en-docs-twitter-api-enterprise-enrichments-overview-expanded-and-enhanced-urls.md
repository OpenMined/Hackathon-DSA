::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
The Expanded and Enhanced URL enrichment automatically expands shortened
URLs that are included in the body of a Tweet, and includes the
resulting URL as metadata within the payload. In addition, this
enrichment also provides HTML page metadata from the ` title ` and
` description ` of the destination page.

**Important Details:**

-   To resolve a shortened link, our system sends HTTP HEAD requests to
    the URL provided and follows any redirects until it arrives at the
    final URL. This final URL (NOT the content of the page itself) is
    then included in the response payload.\
-   The URL enrichment does add between 5-10 seconds latency to realtime
    streams
-   For requests made to the Full Archive Search API, expanded URL
    enrichment data is only available for Tweets 13 months old or
    newer.\
-   The URL enrichment is not available for Tweet links (including quote
    Tweets), Moments links, and profile links that are included within a
    Tweet.\

### Tweet payload

The Expanded and Enhanced URL enrichment can be found within the
` entities ` object of the Tweet payload - specifically in the
` entitites.urls.unwound ` object. It provides the following fields of
metadata:

-   Expanded URL - ` unwound.url `
-   Expanded HTTP Status - ` unwound.status `
-   Expanded URL HTML title - 300 character limit - ` unwound.title `
-   Expanded URL HTML description - 1000 character limit -
    ` unwound.description `

\
**This is an example of an [entities
object](/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/entities)
with the URL enrichment:**
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` line-numbers
 "entities": {
    "hashtags": [
      
    ],
    "urls": [
      {
        "url": "https:\/\/t.co\/HkTkwFq8UT",
        "expanded_url": "http:\/\/bit.ly\/2wYTb9y",
        "display_url": "bit.ly\/2wYTb9y",
        "unwound": {
          "url": "https:\/\/www.forbes.com\/sites\/laurencebradford\/2016\/12\/08\/11-websites-to-learn-to-code-for-free-in-2017\/",
          "status": 200,
          "title": "11 Websites To Learn To Code For Free In 2017",
          "description": "It\u2019s totally possible to learn to code for free...but what are the best resources to achieve that? Here are 11 websites where you can get started."
        },
        "indices": [
          10,
          33
        ]
      }
    ],
    "user_mentions": [
      
    ],
    "symbols": [
      
    ]
  },
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
\
**This is an example of an entities object containing a Tweet link that
is not enriched:\
**
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 "entities": {
  "urls": [{ 
    "url": "https://t.co/SywNbZdDmb", 
    "expanded_url": "https://twitter.com/TwitterDev/status/1050118621198921728", 
    "display_url": "twitter.com/TwitterDev/s…",
     "indices": [ 
        142, 
        165
     ]
   }
  ]
}
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
The following operators will filter and provide a tokenized match on the
related fields of URL metadata:

**url:**

-   Example: "url:tennis"
-   Tokenized match on any Expanded URL that includes the word tennis
-   Could also be used as a filter to include or exclude links from
    a specific website using something like "url:npr.org"

**url_title:**

-   Example: "url_title:tennis"
-   Tokenized match on any Expanded URL HTML title that includes the
    word tennis
-   Matches on the HTML title data included in the payload, which is
    limited to 300 characters.

**url_description:**

-   Example: "url_description:tennis"
-   Tokenized match on any Expanded URL HTML description that includes
    the word tennis
-   Matches on the HTML description included in the payload, which is
    limited to 1000 characters.\

### HTTP Status Codes

The expanded URL enrichment also provides the HTTP status code for the
final URL we are attempting to unwind. In normal cases, this will be a
200 value. Other 400-series values indicate problems with resolving the
URL.

Various status codes may be returned when attempting to unwind a URL.
During the process of unwinding a URL, if we get a redirect, we will
follow them indefinitely until we either:

-   Hit a 200 series code (success)
-   Hit a non-redirect series code (failures)
-   Timeout because the final URL could not be resolved in a reasonable
    amount of time (returns a 408 - timeout)
-   Hit an exception of some sort\

If an exception is hit, we use the following mapping between reasons and
status codes returned:

  ------------------------------ ----------------------
  Reason                         Status Code Returned
  SSL Exceptions                 403 (Forbidden)
  Unwinding not allowed by URL   405
  Socket Timeout                 408 (Timeout)
  Unknown Host Exception         404 (Not Found)
  Unsupported Operation          404 (Not Found)
  Connect Exception              404 (Not Found)
  Illegal Argument               400 (Bad Request)
  Everything else                400 (Bad Request)
  ------------------------------ ----------------------
:::
:::
:::
