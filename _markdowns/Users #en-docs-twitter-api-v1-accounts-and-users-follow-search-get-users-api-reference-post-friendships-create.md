::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
Allows the authenticating user to follow ( *friend* ) the user specified
in the ID parameter.

Returns the followed user when successful. Returns a string describing
the failure condition when unsuccessful. If the user is already friends
with the user a HTTP 403 may be returned, though for performance reasons
this method may also return a HTTP 200 OK message even if the follow
relationship already exists.

Actions taken in this method are asynchronous. Changes will be
eventually consistent.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/friendships/create.json `

  --------------------------- ----------------------------
  Response formats            JSON
  Requires authentication?    Yes (user context only)
  Rate limited?               Yes
  Requests / 24-hour window   400 per user; 1000 per app
  --------------------------- ----------------------------

## Parameters [¶](#parameters){.headerlink}

  ------------- ---------- ------------------------------------------- --------------- --------------
  Name          Required   Description                                 Default Value   Example
  screen_name   optional   The screen name of the user to follow.                      *twitterdev*
  user_id       optional   The ID of the user to follow.                               *2244994945*
  follow        optional   Enable notifications for the target user.                   *true*
  ------------- ---------- ------------------------------------------- --------------- --------------

## Example Request [¶](#example-request){.headerlink}

    curl --request POST 
    --url 'https://api.twitter.com/1.1/friendships/create.json?user_id=2244994945&follow=true' 
    --header 'authorization: OAuth oauth_consumer_key="YOUR_CONSUMER_KEY", oauth_nonce="AUTO_GENERATED_NONCE", oauth_signature="AUTO_GENERATED_SIGNATURE", oauth_signature_method="HMAC-SHA1", oauth_timestamp="AUTO_GENERATED_TIMESTAMP", oauth_token="USERS_ACCESS_TOKEN", oauth_version="1.0"' 
    --header 'content-type: application/json'

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
