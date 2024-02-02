Stay organized with collections

Save and categorize content based on your preferences.

::: {.devsite-article-body .clearfix}
This document will help you to get familiar with Custom Search JSON API
and its usage.

## Before you start {#before_you_start}

### Create Programmable Search Engine {#create_programmable_search_engine}

By calling the API user issues requests against an existing instance of
Programmable Search Engine. Therefore, before using the API, you need to
create one in the [Control
Panel](https://programmablesearchengine.google.com/controlpanel/create)
. Follow the [tutorial](/custom-search/docs/tutorial/creatingcse) to
learn more about different configuration options. Once it is created,
you can find the **Search Engine ID** in the **Overview** page\'s
**Basic** section. This is the ` cx ` parameter used by the API.

### Identify your application to Google with API key {#identify_your_application_to_google_with_api_key}

Custom Search JSON API requires the use of an API key. An API key is a
way to identify your client to Google.

-   [Programmable Search Engine](https://cse.google.com/) (free edition)
    users: [Get a Key]{.devsite-api-getstarted-widget
    .gc-analytics-event .button .button-primary}

After you have an API key, your application can append the query
parameter ` key=yourAPIKey ` to all request URLs. The API key is safe
for embedding in URLs, it doesn\'t need any encoding.

## API overview {#api_overview}

### API operations {#background-operations}

There is only one method to invoke in the Custom Search JSON API:

  Operation                                              Description                                                               REST HTTP mapping
  ------------------------------------------------------ ------------------------------------------------------------------------- -------------------
  [list](/custom-search/v1/reference/rest/v1/cse/list)   Returns the requested search results from a Programmable Search Engine.   ` GET `

### API data model {#background-data-model}

The result of a search query to the Custom Search JSON API is a JSON
object that includes three types of data:

-   Metadata describing the requested search (and, possibly, related
    search requests)
-   Metadata describing the Programmable Search Engine
-   Search results

See the Response data section of [Using
REST](/custom-search/v1/using_rest#response_data) for more details.

The data model is based on the OpenSearch 1.1 Specification. In addition
to the standard OpenSearch properties, the Custom Search JSON API
defines two custom properties and two custom query roles:

-   Custom properties
    -   ` cx ` : The identifier of the Programmable Search Engine.
    -   ` safe ` : A description of the safe search level for filtering
        the returned results.
-   Custom query roles
    -   ` nextPage ` : A role that indicates the query can be used to
        access the next logical page of results, if any.
    -   ` previousPage ` : A role that indicates the query can be used
        to access the previous logical page of results, if any.

## Try it {#try_it}

To play around and see what the API can do, without writing any code,
visit the [\"Try this API\"
tool](/custom-search/v1/reference/rest/v1/cse/list?apix=true) .

For a full description of parameters visit the [cse.list
reference](/custom-search/v1/reference/rest/v1/cse/list) .

To learn how to use the API via HTTP requests, continue to [Using
REST](/custom-search/v1/using_rest) .
:::

Except as otherwise noted, the content of this page is licensed under
the [Creative Commons Attribution 4.0
License](https://creativecommons.org/licenses/by/4.0/) , and code
samples are licensed under the [Apache 2.0
License](https://www.apache.org/licenses/LICENSE-2.0) . For details, see
the [Google Developers Site
Policies](https://developers.google.com/site-policies) . Java is a
registered trademark of Oracle and/or its affiliates.

Last updated 2023-06-22 UTC.

\[{ \"type\": \"thumb-down\", \"id\": \"missingTheInformationINeed\",
\"label\":\"Missing the information I need\" },{ \"type\":
\"thumb-down\", \"id\": \"tooComplicatedTooManySteps\", \"label\":\"Too
complicated / too many steps\" },{ \"type\": \"thumb-down\", \"id\":
\"outOfDate\", \"label\":\"Out of date\" },{ \"type\": \"thumb-down\",
\"id\": \"samplesCodeIssue\", \"label\":\"Samples / code issue\" },{
\"type\": \"thumb-down\", \"id\": \"otherDown\", \"label\":\"Other\" }\]
\[{ \"type\": \"thumb-up\", \"id\": \"easyToUnderstand\",
\"label\":\"Easy to understand\" },{ \"type\": \"thumb-up\", \"id\":
\"solvedMyProblem\", \"label\":\"Solved my problem\" },{ \"type\":
\"thumb-up\", \"id\": \"otherUp\", \"label\":\"Other\" }\]
