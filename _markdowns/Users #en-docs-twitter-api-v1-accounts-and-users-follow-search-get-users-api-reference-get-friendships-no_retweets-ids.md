::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
Returns a collection of user_ids that the currently authenticated user
does not want to receive retweets from.

Use [POST friendships /
update](/en/docs/accounts-and-users/follow-search-get-users/api-reference/post-friendships-update)
to set the \"no retweets\" status for a given user account on behalf of
the current user.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/friendships/no_retweets/ids.json `

  -------------------------------------- -------------------------
  Response formats                       JSON
  Requires authentication?               Yes (user context only)
  Rate limited?                          Yes
  Requests / 15-min window (user auth)   15
  -------------------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

  --------------- ---------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --------------- ---------
  Name            Required   Description                                                                                                                                                                                                                                                              Default Value   Example
  stringify_ids   optional   Some programming environments will not consume Twitter IDs due to their size. Provide this option to have IDs returned as strings instead. Read more about [Twitter IDs](/en/docs/basics/twitter-ids) . This parameter is important to use in Javascript environments.   *false*         *true*
  --------------- ---------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --------------- ---------

## Example Request [¶](#example-request){.headerlink}

` GET https://api.twitter.com/1.1/friendships/no_retweets/ids.json?stringify_ids=true `

## Example Response [¶](#example-response){.headerlink}

    ["777925","732321"]
:::
:::
:::
:::
:::
:::
:::
