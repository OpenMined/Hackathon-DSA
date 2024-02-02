Stay organized with collections

Save and categorize content based on your preferences.

::: {.devsite-article-body .clearfix}
The Custom Search JSON API lets you develop websites and applications to
retrieve and display search results from Programmable Search Engine
programmatically. With this API, you can use RESTful requests to get
either **web search** or **image search** results in JSON format.

## Data format {#data_format}

Custom Search JSON API can return results in
[JSON](/custom-search/docs/glossary#json) data format.

The Custom Search JSON API uses the [OpenSearch 1.1
Specification](https://github.com/dewitt/opensearch/blob/master/opensearch-1-1-draft-6.md)
.

## Prerequisites

### Search engine ID {#search_engine_id}

Before using the Custom Search JSON API you will first need to create
and configure your Programmable Search Engine. If you have not already
created a Programmable Search Engine, you can start by visiting the
[Programmable Search Engine control
panel](https://programmablesearchengine.google.com/controlpanel/all) .

Follow the [tutorial](/custom-search/docs/tutorial/creatingcse) to learn
more about different configuration options.

After you have created a Programmable Search Engine, visit the [help
center](https://support.google.com/programmable-search/answer/2649143)
to learn how to locate your Search engine ID.

### API key {#api_key}

Custom Search JSON API requires the use of an API key. [Get a
Key]{.devsite-api-getstarted-widget .gc-analytics-event .button
.button-primary}

## Pricing

Custom Search JSON API provides 100 search queries per day for free. If
you need more, you may sign up for
[billing](https://cloud.google.com/billing/docs/how-to/manage-billing-account)
in the API Console. Additional requests cost \$5 per 1000 queries, up to
10k queries per day.

## Monitoring

Basic monitoring for the Custom Search JSON API is available through
[Cloud Platform Console\'s API
Dashboard](https://console.cloud.google.com/apis/dashboard) . For more
advanced monitoring [Google Cloud\'s Operations
suite](https://cloud.google.com/products/operations) (formerly
Stackdriver) is available.

With Google Cloud Operations you can create [custom
dashboards](https://cloud.google.com/monitoring/charts) , [set up
alerts](https://cloud.google.com/monitoring/alerts) , and [access
metrics data
programmatically](https://cloud.google.com/monitoring/api/v3) . To
access Custom Search JSON API usage data in Google Cloud Operations,
select \"Resource type: Consumed API\" and filter on \"service =
\'customsearch.googleapis.com\'\" in the Query Builder.

See [Monitoring Your API
Usage](https://cloud.google.com/apis/docs/monitoring) for a discussion
of the different monitoring and alerting capabilities provided by the
API Dashboard and the Google Cloud Operations suite.
:::

Except as otherwise noted, the content of this page is licensed under
the [Creative Commons Attribution 4.0
License](https://creativecommons.org/licenses/by/4.0/) , and code
samples are licensed under the [Apache 2.0
License](https://www.apache.org/licenses/LICENSE-2.0) . For details, see
the [Google Developers Site
Policies](https://developers.google.com/site-policies) . Java is a
registered trademark of Oracle and/or its affiliates.

Last updated 2023-12-18 UTC.

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
