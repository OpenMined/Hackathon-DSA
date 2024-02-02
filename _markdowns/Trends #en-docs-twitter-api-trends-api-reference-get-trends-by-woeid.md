::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Get the trends for a location

### Endpoint URL

` https://api.twitter.com/2/trends/by/woeid/:woeid `

### Authentication and rate limits

+-----------------------------------+-----------------------------------+
| Authentication methods\           | [OAuth 2.0                        |
| supported by this endpoint        | App-only](/en/docs/authentic      |
|                                   | ation/oauth-2-0/application-only) |
+-----------------------------------+-----------------------------------+
| [Rate                             | App rate limit                    |
| limit](/en/docs/rate-limits)      | (Application-only): 75 requests   |
|                                   | per 15-minute window shared among |
|                                   | all users of your app             |
+-----------------------------------+-----------------------------------+

### Path parameters

  ----------------------- ----------------------- -----------------------
  Name                    Type                    Description

  ` woeid `\              number                  The where-on-earth ID
  [Required]{.small}                              (woeid) for a location
  ----------------------- ----------------------- -----------------------
:::
:::

::: c01-rich-text-editor
::: is-table-default
  ----------------- --------- ---------------------------------------------------------
  Name              Type      Description
  ` trend_name `    string    The name of the Trend.
  ` tweet_count `   integer   The total number of Tweets that are part of this Trend.
  ----------------- --------- ---------------------------------------------------------
:::
:::
:::
:::
:::
:::
:::
:::
