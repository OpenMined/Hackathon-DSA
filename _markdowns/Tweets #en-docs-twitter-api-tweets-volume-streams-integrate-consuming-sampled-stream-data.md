::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Consuming data from the sampled stream is very similar to the filtered
stream integration recommendations.  For understanding how to consume
from a streaming endpoint, please follow the recommendations given in
the consuming streaming data integration guide, and note the following
differences with sampled stream.

-   Although only 1% of Tweets, the volume of the sampled stream can be
    very high, and your client should have a high volume capacity.
-   Tweets delivered through the sampled stream endpoint do not count
    towards the monthly total Tweet volume.
-   Tweets delivered with sampled stream will not have a matching rules
    object.\

**Best Practices**

When consuming realtime data, maximizing your connection time is a
fundamental goal to promote both data reliability and data
full-fidelity. When disconnects occur, it is important for your client
to automatically detect the disconnection, [handle the
disconnection](/en/docs/twitter-api/tweets/sampled-stream/integrate/handling-disconnections)
and reconnect quickly.
:::
:::
:::
:::
:::
:::
:::
:::
