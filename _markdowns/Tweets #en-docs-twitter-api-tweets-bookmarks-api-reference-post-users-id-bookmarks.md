::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Causes the user ID of an authenticated user identified in the path
parameter to Bookmark the target Tweet provided in the request body.

### Endpoint URL

` https://api.twitter.com/2/users/:id/bookmarks `

  ----------------------- ----------------------- ------------------------------------------------------------------------------------------
  Name                    Type                    Description

  ` id `\                 string                  The user ID of an authenticated user who you are bookmarking a Tweet on behalf of. It must
  [Required]{.small}                              match your own user ID or that of an authenticating user, meaning that you must pass the
                                                  [Access
                                                  Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/user-access-token)
                                                  associated with the user ID when authenticating your request.
  ----------------------- ----------------------- ------------------------------------------------------------------------------------------

  ----------------------- ----------------------- -----------------------
  Name                    Type                    Description

  ` tweet_id `\           string                  The ID of the Tweet
  [Required]{.small}                              that you would like an
                                                  ` id ` to Bookmark.
  ----------------------- ----------------------- -----------------------
:::
:::

::: c01-rich-text-editor
::: is-table-default
  ---------------- --------- ---------------------------------------------------------------------------------------
  Name             Type      Description
  ` bookmarked `   boolean   Indicates whether the user bookmarks the specified Tweet as a result of this request.
  ---------------- --------- ---------------------------------------------------------------------------------------
:::
:::
:::
