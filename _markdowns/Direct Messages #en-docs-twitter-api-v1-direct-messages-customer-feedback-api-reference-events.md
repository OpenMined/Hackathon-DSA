::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
Returns Feedback creation and response events that occur in a specified
time period. Please note that the max to_time is 24 hours prior to the
current time.

  -------------------------------------- -------------------------
  Response formats                       JSON
  Requires authentication?               Yes (user context only)
  Rate limited?                          Yes
  Requests / 15 min window (user auth)   1,000
  -------------------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

+-----------------------------------+-----------------------------------+
| **from_time** (required)          | Required on the 1st page. Epoch   |
|                                   | timestamp in milliseconds.        |
|                                   | Example: 1451936737470            |
|                                   |                                   |
|                                   | The range is inclusive.           |
+-----------------------------------+-----------------------------------+
| **to_time** (required)            | Required on the 1st page. Epoch   |
|                                   | timestamp in milliseconds.        |
|                                   | Example: 1451936737470            |
|                                   |                                   |
|                                   | The range is inclusive. The max   |
|                                   | to_time is 24 hours before        |
|                                   | current time. Requests for more   |
|                                   | recent data via this endpoint     |
|                                   | will receive an error.            |
+-----------------------------------+-----------------------------------+
| **count** (required)              | Max number of results returned.   |
|                                   | Default and max is 100.           |
+-----------------------------------+-----------------------------------+
| **cursor** (optiona)              | For paging through res            |
|                                   | ults. Required for paging through |
|                                   |  result sets greater than 1 page. |
|                                   |                                   |
|                                   | :                                 |
|                                   |                                   |
|                                   | An empty value indicates you have |
|                                   | reached the end of the result     |
|                                   | set.                              |
+-----------------------------------+-----------------------------------+

## Response Values [¶](#response-values){.headerlink}

  ----------------- -------------------------------------------------------
  **events**        An array of events.
  **event_type**    Possible values: feedback.created, feedback.updated
  **next_cursor**   Values are unique to a given from_time/to_time range.
  ----------------- -------------------------------------------------------

## Example Result [¶](#example-result){.headerlink}

    {
      "events":[
        {
          "event_type": "feedback.updated",
          "created_at": "SatDec1517:58:22+00002015",
          "feedback": {
            "created_at": "SatDec1517:58:20+00002015",
            "updated_at": "SatDec1517:59:22+00002015",
            "id": "123456789",
            ...
          }
        },
        {
          "event_type": "feedback.created",
          "created_at": "SatDec1517:59:22+00002015",
          "feedback":{
            "created_at": "SatDec1517:59:22+00002015",
            "updated_at": "SatDec1517:59:22+00002015",
            "id": "123456799",
            ...
          }
        }
      ],
      "next_cursor": "10011"
    }
:::
:::
:::
:::
:::
:::
:::
