::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Allows a user or authenticated user ID to unlike a Tweet.

The request succeeds with no action when the user sends a request to a
user they\'re not liking the Tweet or have already unliked the Tweet.

### Endpoint URL

` https://api.twitter.com/2/users/:id/likes/:tweet_id `

  ----------------------- ----------------------- --------------------------------------------------------------
  Name                    Type                    Description

  ` id `\                 string                  The user ID who you are removing a Like of a Tweet on behalf
  [Required]{.small}                              of. It must match your own user ID or that of an
                                                  authenticating user, meaning that you must pass the [Access
                                                  Tokens](/en/docs/authentication/oauth-2-0/user-access-token)
                                                  associated with the user ID when authenticating your request.

  ` tweet_id `\           string                  The ID of the Tweet that you would like the ` id ` to unlike.
  [Required]{.small}                              
  ----------------------- ----------------------- --------------------------------------------------------------
:::
:::

::: c01-rich-text-editor
::: is-table-default
  ----------- --------- ----------------------------------------------------------------------------------------------------------------------------------------------------------
  Name        Type      Description
  ` liked `   boolean   Indicates whether the user is unliking the specified Tweet as a result of this request. The returned value is ` false ` for a successful unlike request.
  ----------- --------- ----------------------------------------------------------------------------------------------------------------------------------------------------------
:::
:::
:::
