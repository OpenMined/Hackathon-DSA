::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Upon logging into your account at
[console.gnip.com](http://console.gnip.com) , you will land on the
products tab of the dashboard.  This page includes an overview of the
enterprise products currently available on your account.

For products using streaming delivery like PowerTrack or Decahose, this
page lists the product name, and stream label,  the number of current
active connections, the number of rules currently active for each (where
applicable), and the raw count of activities (for example, Tweets)
delivered in the most recent 24 hours.

For products with REST delivery, like Search API, this page lists the
product name,labels (also shown as \"streams\"), current activities (for
example, Tweets) returned through these endpoints, and a few different
request counts per endpoint.

Note that the [Usage
API](/en/docs/twitter-api/enterprise/usage-api/overview.html) delivers
much of this data programatically.

Specific details per stream are available by clicking the name, or the
settings button.
:::
:::

::: b04-image
::: {.b04 .twtr-component-space--md}
![](https://cdn.cms-twdigitalassets.com/content/dam/developer-twitter/gnip-console/products-tab.png.twimg.1920.png){.b04__img
.b04__img-cover .b04__img--fixed .is-aligned-left .lazyload
width="1886px"}
:::
:::

::: c01-rich-text-editor
::: is-table-default
### Overview

Clicking on one of the streams in the main dashboard will take you to an
overview page for that stream.

For streaming delivery products, this page includes the following:

1.  A volume chart of the number of activities being delivered to you
    through each specific stream connection

2.  Details (connection ID and IP address) on currently active
    connections on the stream

3.  A log of recent connection, disconnection, and rule-update events
    for your stream

Note that the scale of the chart may be adjusted with the links in the
top-right corner. The visibility of individual connections and
disconnections can be toggled by clicking the appropriate key in the
legend directly below the chart.
:::
:::

::: b04-image
::: {.b04 .twtr-component-space--md}
![A screenshot of the stream overview page on
console.gnip.com](https://cdn.cms-twdigitalassets.com/content/dam/developer-twitter/gnip-console/stream-overview.png.twimg.1920.png){.b04__img
.b04__img-cover .b04__img--fixed .is-aligned-left .lazyload
width="2284px"}
:::
:::

::: c01-rich-text-editor
::: is-table-default
### Connections

The Connections page provides details on recent connection events on
your stream. This includes the start and end times for each connection
(in 24 hour UTC), the duration of each connection, the IP of the server
that made the connection, a unique connection ID for reference purposes,
and the current connection status. The status corresponds to the most
recent event for the specified connection -- i.e. Client Connected, or a
disconnect, with the type of disconnect specified.   For more details on
connection debugging, visit the [disconnections explained
guide](/en/docs/twitter-api/enterprise/powertrack-api/guides.html) .
:::
:::

::: b04-image
::: {.b04 .twtr-component-space--md}
![A screenshot of the connections overview page on
console.gnip.com.](https://cdn.cms-twdigitalassets.com/content/dam/developer-twitter/gnip-console/connections.png.twimg.1920.png){.b04__img
.b04__img-cover .b04__img--fixed .is-aligned-left .lazyload
width="1258px"}
:::
:::

::: c01-rich-text-editor
::: is-table-default
### API Help

The API Help page provides the API endpoint URLs for your stream, as
well as the Rules API endpoint for the stream, where applicable. In
addition, it includes sample curl commands and instructions on how to
connect to the stream endpoint, and how to programmatically add, delete,
and list rules from your stream\'s Rules API endpoint.
:::
:::

::: b04-image
::: {.b04 .twtr-component-space--md}
![A screenshot of the API help overview page on
console.gnip.com.](https://cdn.cms-twdigitalassets.com/content/dam/developer-twitter/gnip-console/api-help.png.twimg.1920.png){.b04__img
.b04__img-cover .b04__img--fixed .is-aligned-left .lazyload
width="2326px"}
:::
:::

::: c01-rich-text-editor
::: is-table-default
### Rules

The Rules tab is available for PowerTrack streams, and provides a quick
way to get started by manually entering plain text rules via a user
interface. Note that the interface only supports adding up to 1000 rules
via this manual method, and should be only used for initial testing. We
recommend managing your rules programmatically via the [Rules
API](/en/docs/twitter-api/enterprise/powertrack-api/api-reference.html)
in any production setting.
:::
:::

::: b04-image
::: {.b04 .twtr-component-space--md}
![A screenshot of a PowerTrack API streams rules page on
console.gnip.com.](https://cdn.cms-twdigitalassets.com/content/dam/developer-twitter/gnip-console/rules.png.twimg.1920.png){.b04__img
.b04__img-cover .b04__img--fixed .is-aligned-left .lazyload
width="1274px"}
:::
:::

::: c01-rich-text-editor
::: is-table-default
### Settings

The Settings tab allows you to switch the output format of the data in
your stream, where multiple format options are supported. To switch the
format, just use the radio buttons indicating the different options. The
change will take effect upon reconnecting to the stream.  Note that
updating this setting will take place immediately on the next request or
connection and may break your parser with the new format.

**Please note:** The recommended setting for getting the most data is
\"Leave data in the original format\" which will return data in the
enriched native format
[here](/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects.html)
.  Activity streams format is described
[here](/en/docs/twitter-api/enterprise/data-dictionary/activity-streams-objects.html)
.
:::
:::

::: b04-image
::: {.b04 .twtr-component-space--md}
![A screenshot of the settings page on
console.gnip.com.](https://cdn.cms-twdigitalassets.com/content/dam/developer-twitter/gnip-console/settings-format.png.twimg.1920.png){.b04__img
.b04__img-cover .b04__img--fixed .is-aligned-left .lazyload
width="2660px"}
:::
:::
:::
