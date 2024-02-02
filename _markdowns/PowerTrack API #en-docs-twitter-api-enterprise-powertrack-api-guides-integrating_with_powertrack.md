::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
To integrate PowerTrack into your product, you will need to build an
application that can do the following:

1.  Establish a streaming connection to the PowerTrack stream API.
2.  Asynchronously send POST requests to the PowerTrack rules API to add
    and delete rules from the stream.
3.  Handle low data volumes -- Maintain the streaming connection, and
    ensure buffers are flushed regularly.
4.  Handle high data volumes -- de-couple stream ingestion from
    additional processing using asynchronous processes.
5.  Reconnect to the stream automatically when disconnected for any
    reason.

For details on the types of requests needed for tasks 1 and 2, and
important considerations in implementing them, see the [API
reference](/en/docs/twitter-api/enterprise/powertrack-api/api-reference)
.

For information on consuming a realtime data stream, see
[here](/en/docs/tutorials/consuming-streaming-data.html) .
:::
:::
:::
:::
:::
:::
:::
:::
