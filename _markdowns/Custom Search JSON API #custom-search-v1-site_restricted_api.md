Stay organized with collections

Save and categorize content based on your preferences.

::: {.devsite-article-body .clearfix}
**Note:**

<div>

The Custom Search Site Restricted JSON API endpoints will cease to serve
traffic on December 18, 2024.

All Custom Search Site Restricted JSON API customers must begin their
transition to [Google Cloud\'s Vertex AI
Search](https://cloud.google.com/enterprise-search) . Detailed
transition guidance can be found
[here](https://cloud.google.com/generative-ai-app-builder/docs/migrate-from-prose-site-restricted)
. If you experience issues, you can contact us
[here](https://cloud.google.com/generative-ai-app-builder/docs/support)
.

</div>

This document describes how to use the Custom Search Site Restricted
JSON API.

## About the Custom Search Site Restricted JSON API {#about_the}

If your Programmable Search Engine is restricted to only searching
specific sites (10 or fewer), you can use the Custom Search Site
Restricted JSON API. This API is similar to the Custom Search JSON API
except this version has no daily query limit. To use this version,
confirm that you see 10 or fewer sites to search in the "Sites to
Search" section of your Programmable Search Engine control panel, there
are no global top level domain patterns, and that "Search the entire
web" is set to OFF.

When using the Custom Search Site Restricted JSON API endpoint, be
mindful that if your Programmable Search Engine configuration is changed
so that it does not conform with the site restriction rules above, the
Custom Search Site Restricted JSON API may not return the expected
results.

## Making a request {#making_a_request}

Making a request to Custom Search Site Restricted JSON API is similar to
making a request to Custom Search JSON API; however, the URI is
different. The format for the Custom Search Site Restricted JSON API is

https://www.googleapis.com/customsearch/v1/siterestrict?\[parameters\]

The ` [parameters] ` are the same as the [Custom Search JSON
API](/custom-search/v1/using_rest) parameters

## Pricing

Custom Search Site Restricted JSON API requests cost \$5 per 1000
queries and there is no daily query limit. You may sign up for
[billing](https://cloud.google.com/billing/docs/how-to/manage-billing-account)
in the API Console.
:::

Except as otherwise noted, the content of this page is licensed under
the [Creative Commons Attribution 4.0
License](https://creativecommons.org/licenses/by/4.0/) , and code
samples are licensed under the [Apache 2.0
License](https://www.apache.org/licenses/LICENSE-2.0) . For details, see
the [Google Developers Site
Policies](https://developers.google.com/site-policies) . Java is a
registered trademark of Oracle and/or its affiliates.

Last updated 2023-12-19 UTC.

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
