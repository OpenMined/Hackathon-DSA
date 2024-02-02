::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Allows an authenticated user ID to unmute the target user.

The request succeeds with no action when the user sends a request to a
user they\'re not muting or have already unmuted.

### Endpoint URL

` https://api.twitter.com/2/users/:source_user_id/muting/:target_user_id `

  ----------------------- ----------------------- --------------------------------------------------------------
  Name                    Type                    Description

  ` source_user_id `\     string                  The user ID who you would like to initiate an unmute on behalf
  [Required]{.small}                              of. The user's ID must correspond to the user ID of the
                                                  authenticating user, meaning that you must pass the [Access
                                                  Tokens](/en/docs/authentication/oauth-2-0/user-access-token)
                                                  associated with the user ID when authenticating your request.

  ` target_user_id `\     string                  The user ID of the user that you would like the
  [Required]{.small}                              ` source_user_id ` to unmute.
  ----------------------- ----------------------- --------------------------------------------------------------
:::
:::

::: c01-rich-text-editor
::: is-table-default
  ------------ --------- -------------------------------------------------------------------------------------------------------------------------------------------------------
  Name         Type      Description
  ` muting `   boolean   Indicates whether the user is muting the specified user as a result of this request. The returned value is ` false ` for a successful unmute request.
  ------------ --------- -------------------------------------------------------------------------------------------------------------------------------------------------------
:::
:::
:::
