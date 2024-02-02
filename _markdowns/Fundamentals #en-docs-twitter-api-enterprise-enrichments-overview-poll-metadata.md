::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: bl19-no-edit-wrap
::: {.c15-column-container .js-column-container}
::: {.container--mini .container--mobile}
::: {.column .column-6}
::: c01-rich-text-editor
::: is-table-default
::: gnip-body-container
::: container
::: row
::: col-md-12
Poll metadata is a free enrichment available across all products
(Realtime & Historical APIs) in enriched native format payloads. The
metadata notes the presence of the poll in a Tweet, includes the list of
poll choices, and includes both the poll duration and expiration time.
This enrichment makes it easy to acknowledge the presence of a poll and
enables proper rendering of a poll Tweet for display.

##### Important Details:

-   Available across all enterprise APIs (PowerTrack, Replay, Search,
    Historical PowerTrack)
    -   *Note:* For Replay and Historical PowerTrack, this metadata was
        first made available on 02/22/17 - see documented [enrichment
        availability](/content/developer-twitter/en/docs/tweets/batch-historical/guides/hpt-timeline)
        .
-   Does not include vote information or poll results
-   Does not currently have filter/operator support
-   Available in **enriched native format** only
    -   Enriched native format is a user-controlled setting that can be
        changed at any time through the Console: *Select a Product
        (PowerTrack, Replay, Search) \> Settings tab \> Output Format
        (Leave data in its original format)*

### Tweet Payload

Poll Tweets will contain the following metadata in the "entities.polls"
object in the payload:

-   An "options" array with up to four options that include the position
    (1-4) and option text
-   Poll expiration date
-   Poll duration

See the sample payload below for further reference.

### Sample Payload

Below is a snippet of the enriched native format payload highlighting
the added poll metadata:

    "entities":{  
          "hashtags":[],
          "urls":[],
          "user_mentions":[],
          "symbols":[],
          "polls":[  
             {  
                "options":[  
                   {  
                      "position":1,
                      "text":"The better answer"
                   },
                   {  
                      "position":2,
                      "text":"The best answer"
                   }
                ],
                "end_datetime":"Sat Feb 04 15:33:11 +0000 2017",
                "duration_minutes":1440
             }
          ]
       },
:::
:::
:::
:::
:::
:::
:::
:::
:::
:::
:::
:::
:::
:::
:::
:::
