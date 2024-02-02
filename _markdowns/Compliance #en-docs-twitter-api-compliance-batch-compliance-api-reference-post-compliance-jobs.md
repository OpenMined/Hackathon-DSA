::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
\"Creates a new compliance job for Tweet IDs or user IDs. A compliance
job will contain an ID and a destination URL. The destination URL
represents the location that contains the list of IDs consumed by your
App.

You can run one batch job at a time.\"

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

  ` type `\               enum ( ` tweets ` ,     Specify whether you
  [Required]{.small}      ` users ` )             will be uploading tweet
                                                  or user IDs. You can
                                                  either specify tweets
                                                  or users.

  ` name `\               string                  A name for this job,
  [Optional]{.small}                              useful to identify
                                                  multiple jobs using a
                                                  label you define.

  ` resumable `\          boolean                 Specifies whether to
  [Optional]{.small}                              enable the upload URL
                                                  with support for
                                                  resumable uploads. If
                                                  true, this endpoint
                                                  will return a
                                                  pre-signed URL with
                                                  resumable uploads
                                                  enabled.
  ----------------------- ----------------------- -----------------------
:::
:::

::: c01-rich-text-editor
::: is-table-default
  ------------------------- --------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Name                      Type                              Description
  ` id `                    string                            The unique identifier for this job.
  ` created_at `            date (ISO 8601)                   The date and time when the job was created.
  ` type `                  enum ( ` tweets ` , ` users ` )   The type of the job, whether tweets or users.
  ` name `                  string                            The user defined job name. Only returned if specified when the job was created.
  ` upload_url `            string                            A URL representing the location where to upload Tweet IDs consumed by your App. This URL is already signed with an authentication key, so you will not need to pass any additional credentials or headers to authenticate the request.
  ` upload_expires_at `     date (ISO 8601)                   The date and time until which the upload URL will be available (usually 15 minutes from the request time).
  ` download_url `          string                            The predefined location where to download the results from the compliance job. This URL is already signed with an authentication key, so you will not need to pass any additional credentials or headers to authenticate the request.
  ` download_expires_at `   date (ISO 8601)                   The date and time until which the download URL will be available (usually seven days from the request time).
  ------------------------- --------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::
:::
:::
