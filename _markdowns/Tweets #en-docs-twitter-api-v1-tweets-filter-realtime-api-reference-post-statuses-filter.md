::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
Returns public Tweets that match one or more filter predicates. Multiple
parameters may be specified which allows most clients to use a single
connection to the Streaming API. Both GET and POST requests are
supported, but GET requests with too many parameters may cause the
request to be rejected for excessive URL length. Use a POST request to
avoid long URLs.

The track, follow, and locations fields should be considered to be
combined with an OR operator. ` track=foo&follow=1234 ` returns Tweets
matching \"foo\" OR created by user 1234.

The default access level allows up to 400 track keywords, 5,000 follow
userids and 25 0.1-360 degree location boxes. If you need access to more
rules and filtering tools, please apply for [enterprise
access](/en/enterprise) .

## Resource URL [¶](#resource-url){.headerlink}

` https://stream.twitter.com/1.1/statuses/filter.json `

  ------------------------------- -------------------------
  Response formats                JSON
  Requires authentication?        Yes (user context only)
  Rate limited?                   Yes
  Supports Edit Tweets feature?   No
  ------------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

  -------------------------- ---------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Name                       Required   Description
  follow                     optional   A comma separated list of user IDs, indicating the users to return statuses for in the stream. See [follow](/en/docs/tweets/filter-realtime/guides/basic-stream-parameters) for more information.
  track                      optional   Keywords to track. Phrases of keywords are specified by a comma-separated list. See [track](/en/docs/tweets/filter-realtime/guides/basic-stream-parameters) for more information.
  locations                  optional   Specifies a set of bounding boxes to track. See [locations](/en/docs/tweets/filter-realtime/guides/basic-stream-parameters) for more information.
  delimited                  optional   Specifies whether messages should be length-delimited. See [delimited](/en/docs/tweets/filter-realtime/guides/basic-stream-parameters) for more information.
  stall_warnings             optional   Specifies whether stall warnings should be delivered. See [stall_warnings](/en/docs/tweets/filter-realtime/guides/basic-stream-parameters) for more information.
  include_ext_edit_control   optional   Must be set to true in order to return edited Tweet metadata as part of the Tweet object.
  -------------------------- ---------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Example Request [¶](#example-request){.headerlink}

` GET https://stream.twitter.com/1.1/statuses/filter.json?track=twitter `
:::
:::
:::
:::
:::
:::
:::
