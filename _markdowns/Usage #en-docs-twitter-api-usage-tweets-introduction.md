::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
The Usage API in the Twitter API v2 allows developers to
programmatically retrieve their project usage. Using thie endpoint,
developers can keep a track and monitor of the number of Tweets they
have pulled for a given billing cycle.

Developers can use the GET endpoint to get the daily project usage for
upto the last 90 days. The usage can also be aggregated per client app
connected to your peoject.

There is a app rate limit of 50 requests per 15 minutes for this GET
endpoint.

### Getting started

To use this endpoint, you need a [bearer
token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only)
from the [developer
portal](https://developer.twitter.com/en/portal/dashboard) . Once you
have the bearer token,  you can call the usage API as shown below:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 curl 'https://api.twitter.com/2/usage/tweets' --header 'Authorization: Bearer XXXXX'
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
If the request is successful, you should see the JSON response as shown
below:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {
    "data": {
        "cap_reset_day": 10,
        "project_cap": "5000000000",
        "project_id": "1369785403853424",
        "project_usage": "43435"
    }
}
    
```
:::
:::
:::

::: dtc09-callout-text
::: dtc09-callout-text
:::
:::

::: ct01-columns
:::
:::
