::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Get the Tweet usage within the context of a project

### Endpoint URL

` https://api.twitter.com/2/usage/tweets `

+-----------------------------------+-----------------------------------+
| Authentication methods\           | [OAuth 2.0                        |
| supported by this endpoint        | App-only](/en/docs/authentic      |
|                                   | ation/oauth-2-0/application-only) |
+-----------------------------------+-----------------------------------+
| [Rate                             | App rate limit                    |
| limit](/en/docs/rate-limits)      | (Application-only): 50 requests   |
|                                   | per 15-minute window shared among |
|                                   | all users of your app             |
+-----------------------------------+-----------------------------------+

  ----------------------- ---------------------------- -----------------------
  Name                    Type                         Description

  ` days `\               number                       The number of days for
  [Optional]{.small}                                   which you need the
                                                       Tweet usage for. You
                                                       can get usage for upto
                                                       90 days.

  ` usage.fields `\       enum (                       This parameter is used
  [Optional]{.small}      ` daily_client_app_usage ` , to specify if you want
                          ` daily_project_usage ` )    the daily usage
                                                       returned and at a
                                                       client app level.
  ----------------------- ---------------------------- -----------------------
:::
:::

::: c01-rich-text-editor
::: is-table-default
  ---------------------------------------- ----------------- ------------------------------------------------------------------------------------------------
  Name                                     Type              Description
  ` project_id `                           string            The unique identifier for this project.
  ` project_cap `                          string            The total number of Tweets that can be read with this project per month.
  ` project_usage `                        string            The total number of Tweets that have been read with this project in the current billing cycle.
  ` cap_reset_day `                        integer           The day of the month when the Tweet cap is reset.
  ` daily_project_usage `                  object            This object and its fields contain daily usage breakdown for a project.
  ` daily_project_usage.project_id `       string            The unique identifier for this project.
  ` daily_project_usage.usage `            array             This array contains the usage information.
  ` daily_project_usage.usage.date `       date (ISO 8601)   The date for which the usage is returned.
  ` daily_project_usage.usage.usage `      string            The project usage for a day.
  ` daily_client_app_usage `               array             This object and its fields contain daily usage breakdown per client app.
  ` daily_client_app_usage.usage `         array             This array contains the usage information.
  ` daily_client_app_usage.usage.date `    date (ISO 8601)   The date for which the usage is returned.
  ` daily_client_app_usage.usage.usage `   string            The project usage for a day.
  ---------------------------------------- ----------------- ------------------------------------------------------------------------------------------------
:::
:::
:::
