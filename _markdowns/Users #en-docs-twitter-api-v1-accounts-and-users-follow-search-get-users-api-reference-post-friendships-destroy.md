::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
Allows the authenticating user to unfollow the user specified in the ID
parameter.

Returns the unfollowed user when successful. Returns a string describing
the failure condition when unsuccessful.

Actions taken in this method are asynchronous. Changes will be
eventually consistent.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/friendships/destroy.json `

  -------------------------- -------------------------
  Response formats           JSON
  Requires authentication?   Yes (user context only)
  Rate limited?              Yes
  -------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

  ------------- ---------- ------------------------------------------ --------------- --------------
  Name          Required   Description                                Default Value   Example
  screen_name   optional   The screen name of the user to unfollow.                   *twitterdev*
  user_id       optional   The ID of the user to unfollow.                            *2244994945*
  ------------- ---------- ------------------------------------------ --------------- --------------

## Example Request [¶](#example-request){.headerlink}

` POST https://api.twitter.com/1.1/friendships/destroy.json?user_id=2244994945 `

## Example Response [¶](#example-response){.headerlink}

    {user-object,
      "status": {tweet-object}
    }

For more detail, see the [user-object
definition](/en/docs/tweets/data-dictionary/overview/user-object) and
the [tweet-object
definition](/en/docs/tweets/data-dictionary/overview/user-object) .
:::
:::
:::
:::
:::
:::
:::
