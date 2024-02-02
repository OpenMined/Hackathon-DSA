::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
The v2 manage Lists endpoints will eventually replace [POST
lists/create](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-create)
, [POST
lists/destroy](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-destroy)
, and [POST
lists/update](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-update)
. If you have code, apps, or tools that use an older version of these
endpoints and are considering migrating to the newer Twitter API v2,
then this guide is for you.

The following tables compare the standard v1.1 and Twitter API v2 List
endpoints: \

**Create a List**

  Description                                                                     Standard v1.1                               Twitter API v2
  ------------------------------------------------------------------------------- ------------------------------------------- -------------------------------------------
  HTTP methods supported                                                          [ POST ]{.code-inline}                      [ POST ]{.code-inline}
  Host domain                                                                     [ https://api.twitter.com ]{.code-inline}   [ https://api.twitter.com ]{.code-inline}
  Endpoint path                                                                   [ /1.1/lists/create.json ]{.code-inline}    [ /2/lists ]{.code-inline}
  [Authentication](/content/developer-twitter/en/docs/authentication)             OAuth 1.0a User Context                     OAuth 1.0a User Context
  Default request [rate limits](/content/developer-twitter/en/docs/rate-limits)   None                                        300 requests per 15 min (per user)

**Delete a List**

  Description                                                                     Standard v1.1                               Twitter API v2
  ------------------------------------------------------------------------------- ------------------------------------------- -------------------------------------------
  HTTP methods supported                                                          [ POST ]{.code-inline}                      [ DELETE ]{.code-inline}
  Host domain                                                                     [ https://api.twitter.com ]{.code-inline}   [ https://api.twitter.com ]{.code-inline}
  Endpoint path                                                                   [ /1.1/lists/destroy.json ]{.code-inline}   [ /2/lists/:id ]{.code-inline}
  [Authentication](/content/developer-twitter/en/docs/authentication)             OAuth 1.0a User Context                     OAuth 1.0a User Context
  Default request [rate limits](/content/developer-twitter/en/docs/rate-limits)   None                                        300 requests per 15 min (per user)

**Update a List**

  Description                                                                     Standard v1.1                               Twitter API v2
  ------------------------------------------------------------------------------- ------------------------------------------- -------------------------------------------
  HTTP methods supported                                                          [ POST ]{.code-inline}                      [ PUT ]{.code-inline}
  Host domain                                                                     [ https://api.twitter.com ]{.code-inline}   [ https://api.twitter.com ]{.code-inline}
  Endpoint path                                                                   [ /1.1/lists/update.json ]{.code-inline}    [ /2/lists/:id ]{.code-inline}
  [Authentication](/content/developer-twitter/en/docs/authentication)             OAuth 1.0a User Context                     OAuth 1.0a User Context
  Default request [rate limits](/content/developer-twitter/en/docs/rate-limits)   None                                        300 requests per 15 min (per user)

### 
:::
:::

::: c01-rich-text-editor
:::
:::
:::
:::
:::
:::
:::
