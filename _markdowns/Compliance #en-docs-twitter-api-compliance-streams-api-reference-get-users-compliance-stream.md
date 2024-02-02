::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Connect to one of four partitions of the User compliance stream.

### Endpoint URL

` https://api.twitter.com/2/users/compliance/stream `

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
  [Required]{.small}                              or 4. User compliance
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
  ------------------------------- ----------------- ---------------------------------------------------
  Name                            Type              Description
  ` user_delete `                 string            A delete user event.
  ` user_undelete `               string            A undelete user event.
  ` user_withheld `               string            A withheld user event.
  ` user_protect `                string            A protect user event.
  ` user_unprotect `              string            A unprotect user event.
  ` user_suspend `                string            A suspend user event.
  ` user_unsuspend `              string            A unsuspend user event.
  ` scrub_geo `                   string            A geo scrub user event.
  ` user_profile_modification `   string            A modified user profile event.
  ` id `                          string            The ID of the user triggering a compliance event.
  ` event_at `                    date (ISO 8601)   Time of when event happended.
  ` withheld_in_countries `       string            Country where user is withheld.
  ` up_to_tweet_id `              string            Provided when a user removes their geo metadata.
  ` profile_field `               string            Indicates what Profile attribute was updated.
  ------------------------------- ----------------- ---------------------------------------------------
:::
:::
:::
