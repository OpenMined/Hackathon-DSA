::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Allows a user or authenticated user ID to remove the Retweet of a Tweet.

The request succeeds with no action when the user sends a request to a
user they\'re not Retweeting the Tweet or have already removed the
Retweet of.

### Endpoint URL

` https://api.twitter.com/2/users/:id/retweets/:source_tweet_id `

  ----------------------- ----------------------- --------------------------------------------------------------
  Name                    Type                    Description

  ` id `\                 string                  The user ID who you are removing a the Retweet of a Tweet on
  [Required]{.small}                              behalf of. It must match your own user ID or that of an
                                                  authenticating user, meaning that you must pass the [Access
                                                  Tokens](/en/docs/authentication/oauth-2-0/user-access-token)
                                                  associated with the user ID when authenticating your request.

  ` source_tweet_id `\    string                  The ID of the Tweet that you would like the ` id ` to remove
  [Required]{.small}                              the Retweet of.
  ----------------------- ----------------------- --------------------------------------------------------------
:::
:::

::: c01-rich-text-editor
::: is-table-default
  --------------- --------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Name            Type      Description
  ` retweeted `   boolean   Indicates whether the user has removed the Retweet of the specified Tweet as a result of this request. The returned value is ` false ` for a successful unretweet request.
  --------------- --------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::
:::
:::
