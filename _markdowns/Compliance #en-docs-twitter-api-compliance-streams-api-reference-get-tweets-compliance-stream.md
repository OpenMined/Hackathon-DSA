::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Connect to one of four partitiona of the Tweet compliance stream.

### Endpoint URL

` https://api.twitter.com/2/tweets/compliance/stream `

+-----------------------------------+-----------------------------------+
| Authentication methods\           | [OAuth 2.0                        |
| supported by this endpoint        | App-only](/en/docs/authentic      |
|                                   | ation/oauth-2-0/application-only) |
+-----------------------------------+-----------------------------------+
| [Rate                             | App rate limit                    |
| limit](/en/docs/rate-limits)      | (Application-only): 100 requests  |
|                                   | per 15-minute window shared among |
|                                   | all users of your app             |
+-----------------------------------+-----------------------------------+

  ----------------------- ----------------------- -----------------------
  Name                    Type                    Description

  ` partition `\          number                  Must be set to 1, 2, 3
  [Required]{.small}                              or 4. Tweet compliance
                                                  events are split across
                                                  4 partitions, so 4
                                                  separate streams are
                                                  needed to receive all
                                                  events.

  ` backfill_minutes `\   number                  By passing this
  [Optional]{.small}                              parameter, you can
                                                  recover up to five
                                                  minutes worth of data
                                                  that you might have
                                                  missed during a
                                                  disconnection. The
                                                  backfilled events will
                                                  automatically flow
                                                  through a reconnected
                                                  stream, with older
                                                  events generally being
                                                  delivered before any
                                                  newer events. You must
                                                  include a whole number
                                                  between 1 and 5 as the
                                                  value to this
                                                  parameter. nThis
                                                  feature will deliver
                                                  all events that
                                                  published during the
                                                  timeframe selected,
                                                  meaning that if you
                                                  were disconnected for
                                                  90 seconds, and you
                                                  requested two minutes
                                                  of backfill, you will
                                                  receive 30 seconds
                                                  worth of duplicate
                                                  events. Due to this,
                                                  you should make sure
                                                  your system is tolerant
                                                  of duplicate data.
  ----------------------- ----------------------- -----------------------
:::
:::

::: c01-rich-text-editor
::: is-table-default
  --------------- ----------------- ----------------------------------------------------------------
  Name            Type              Description
  ` delete `      string            A delete Tweet event.
  ` withheld `    string            A withheld Tweet event.
  ` drop `        string            A drop Tweet event.
  ` undrop `      string            A undrop Tweet event.
  ` id `          string            The ID of the Tweet triggering a compliance event.
  ` author_id `   string            The ID of the author of a Tweet triggering a compliance event.
  ` event_at `    date (ISO 8601)   Time of when event happended.
  --------------- ----------------- ----------------------------------------------------------------
:::
:::
:::
