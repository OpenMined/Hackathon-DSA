::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
The Trends lookup endpoint allow developers to get the Trends for a
location, specified using the where-on-earth id (WOEID).

**Note** : WOEID is a legacy identifier created by Yahoo and has been
deprecated. X API uses the numeric value to identify town and country
trend locations. Reference our legacy [blog
post](https://blog.twitter.com/engineering/en_us/a/2010/woeids-in-twitters-trends.html)
, or [archived
data](https://archive.org/details/geoplanet_data_7.10.0.zip0.)

The ` tweet_count ` for the last 24 hours is also returned for many
trends if this is available.

This endpoint supports app-auth authentication and has a rate limit of
75 requests per 15-minute window.

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
 curl 'https://api.twitter.com/2/trends/by/woeid/26062' --header 'Authorization: Bearer XXXXX' 
    
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
    "data": [
        {
            "trend_name": "Europe",
            "tweet_count": 232408
        },
        {
            "trend_name": "Isak",
            "tweet_count": 2956
        },
        {
            "trend_name": "RNLI",
            "tweet_count": 2484
        },
        {
            "trend_name": "Toon",
            "tweet_count": 11447
        },
        {
            "trend_name": "St James",
            "tweet_count": 5565
        },
        {
            "trend_name": "Manning",
            "tweet_count": 10077
        },
        {
            "trend_name": "Copenhagen",
            "tweet_count": 35272
        },
        {
            "trend_name": "Coventry",
            "tweet_count": 3662
    ]
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
