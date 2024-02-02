::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Returns a list of recent compliance jobs.

### Endpoint URL

` https://api.twitter.com/2/compliance/jobs `

+-----------------------------------+-----------------------------------+
| Authentication methods\           | [OAuth 2.0                        |
| supported by this endpoint        | App-only](/en/docs/authentic      |
|                                   | ation/oauth-2-0/application-only) |
+-----------------------------------+-----------------------------------+
| [Rate                             | App rate limit                    |
| limit](/en/docs/rate-limits)      | (Application-only): 150 requests  |
|                                   | per 15-minute window shared among |
|                                   | all users of your app             |
+-----------------------------------+-----------------------------------+

  ----------------------- ----------------------- -----------------------
  Name                    Type                    Description

  ` type `\               enum ( ` tweets ` ,     Allows to filter by job
  [Required]{.small}      ` users ` )             type - either by tweets
                                                  or user ID. Only one
                                                  filter (tweets or
                                                  users) can be specified
                                                  per request.

  ` status `\             enum ( ` created ` ,    Allows to filter by job
  [Optional]{.small}      ` in_progress ` ,       status. Only one filter
                          ` failed ` ,            can be specified per
                          ` complete ` )          request.\
                                                  Default: ` all `
  ----------------------- ----------------------- -----------------------
:::
:::

::: c01-rich-text-editor
::: is-table-default
  ------------------------- ------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Name                      Type                                                   Description
  ` id `                    string                                                 The unique identifier for this job.
  ` created_at `            date (ISO 8601)                                        The date and time when the job was created.
  ` type `                  enum ( ` tweets ` , ` users ` )                        The type of the job, whether tweets or users.
  ` name `                  string                                                 The user defined job name. Only returned if specified when the job was created.
  ` upload_url `            string                                                 A URL representing the location where to upload IDs consumed by your app. This URL is already signed with an authentication key, so you will not need to pass any additional credentials or headers to authenticate the request.
  ` upload_expires_at `     date (ISO 8601)                                        The date and time until which the upload URL will be available (usually 15 minutes from the request time).
  ` download_url `          string                                                 The predefined location where to download the results from the compliance job. This URL is already signed with an authentication key, so you will not need to pass any additional credential or header to authenticate the request.
  ` download_expires_at `   date (ISO 8601)                                        The date and time until which the download URL will be available (usually 7 days from the request time).
  ` status `                enum ( ` in_progress ` , ` failed ` , ` complete ` )   Current status of this job.
  ` error `                 string                                                 Only returned when ` jobs.status ` is ` failed ` . Specifies the reason why the job did not complete successfully.
  ------------------------- ------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::
:::
:::
