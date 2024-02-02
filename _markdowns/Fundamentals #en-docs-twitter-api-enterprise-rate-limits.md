::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Every day many thousands of developers make requests to the Twitter API.
To help manage the sheer volume of these requests, limits are placed on
the number of requests that can be made. These limits help us provide
the reliable and scalable API that our developer community relies on.

The maximum number of requests that are allowed is based on a time
interval, some specified period or window of time. If an endpoint has a
rate limit of 900 requests/15-minutes, then up to 900 requests over any
15-minute interval is allowed.
:::
:::

::: c01-rich-text-editor
<div>

  Product                                                                         Endpoint                                                                                                                                     Rate limit
  ------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------
  PowerTrack API                                                                  Streaming endpoint                                                                                                                           60 requests per minute
  Rules endpoint                                                                  60 requests per minute aggregated across all /rules endpoints                                                                                
  Replay endpoint                                                                 5 requests per 5 minutes                                                                                                                     
  Historical PowerTrack API                                                                                                                                                                                                    60 Jobs can be created per (UTC) day.
                                                                                  30 Jobs can be created per hour.                                                                                                             
                                                                                  2 Jobs can be estimating concurrently.                                                                                                       
                                                                                  2 Jobs can be running concurrently.                                                                                                          
  Decahose API                                                                                                                                                                                                                 10 requests per minute
  Streaming likes API                                                                                                                                                                                                          10 requests per minute
  Firehose API                                                                                                                                                                                                                 10 requests per minute
  Account Activity API                                                            POST account_activity/webhooks                                                                                                               15 requests per 15 minutes
  GET account_activity/webhooks                                                   15 requests per 15 minutes                                                                                                                   
  PUT account_activity/webhooks/:webhook_id                                       15 requests per 15 minutes                                                                                                                   
  POST account_activity/webhooks/:webhook_id/subscriptions/all                    500 requests per 15 minutes                                                                                                                  
  GET account_activity/subscriptions/count                                        15 requests per 15 minutes                                                                                                                   
  GET account_activity/webhooks/:webhook_id/subscriptions/all                     500 requests per 15 minutes                                                                                                                  
  GET account_activity/webhooks/:webhook_id/subscriptions/all/list                50 requests per 15 minutes                                                                                                                   
  DELETE account_activity/webhooks/:webhook_id                                    15 requests per 15 minutes                                                                                                                   
  DELETE /account_activity/webhooks/:webhook_id/subscriptions/:user_id/all.json   500 requests per 15 minutes                                                                                                                  
  Replay                                                                          5 requests per 15 minutes                                                                                                                    
  Search API                                                                                                                                                                                                                   Per minute rate limit will vary by contract
                                                                                  20 requests per second aggregated across either the 30 day data and counts endpoints, or across the full-archive data and counts endpoints   
  Engagement API                                                                                                                                                                                                               Per minute rate limit will vary by contract
  Compliance Firehose API                                                                                                                                                                                                      10 requests per minute
  Usage API                                                                                                                                                                                                                    2 requests per minute

</div>
:::
:::
:::
:::
:::
:::
:::
