::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Allows a user ID to follow another user. If the target user does not
have public Tweets, this endpoint will send a follow request.

The request succeeds with no action when the authenticated user sends a
request to a user they\'re already following, or if they\'re sending a
follower request to a user that does not have public Tweets.

### Endpoint URL

` https://api.twitter.com/2/users/:id/following `

  ----------------------- ----------------------- --------------------------------------------------------------
  Name                    Type                    Description

  ` id `\                 string                  The authenticated user ID who you would like to initiate the
  [Required]{.small}                              follow on behalf of. You must pass the [Access
                                                  Tokens](/en/docs/authentication/oauth-2-0/user-access-token)
                                                  that relate to this user when authenticating the request.
  ----------------------- ----------------------- --------------------------------------------------------------

  ----------------------- ----------------------- -----------------------
  Name                    Type                    Description

  ` target_user_id `\     string                  The user ID of the user
  [Required]{.small}                              that you would like the
                                                  ` id ` to follow.
  ----------------------- ----------------------- -----------------------
:::
:::

::: c01-rich-text-editor
::: is-table-default
  -------------------- --------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Name                 Type      Description
  ` following `        boolean   Indicates whether the ` id ` is following the specified user as a result of this request. This value is ` false ` if the target user does not have public Tweets, as they will have to approve the follower request.
  ` pending_follow `   boolean   Indicates whether the target user will need to approve the follow request. Note that the authenticated user will follow the target user only when they approve the incoming follower request.
  -------------------- --------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::
:::
:::
