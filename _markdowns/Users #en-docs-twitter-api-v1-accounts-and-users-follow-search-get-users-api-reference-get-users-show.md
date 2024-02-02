::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
Returns a [variety of
information](/en/docs/tweets/data-dictionary/overview/user-object) about
the user specified by the required ` user_id ` or ` screen_name `
parameter. The author\'s most recent Tweet will be returned inline when
possible.

[GET users /
lookup](/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-lookup)
is used to retrieve a bulk collection of user objects.

You must be following a protected user to be able to see their most
recent Tweet. If you don\'t follow a protected user, the user\'s Tweet
will be removed. A Tweet will not always be returned in the
current_status field.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/users/show.json `

  -------------------------------------- ------
  Response formats                       JSON
  Requires authentication?               Yes
  Rate limited?                          Yes
  Requests / 15-min window (user auth)   900
  Requests / 15-min window (app auth)    900
  -------------------------------------- ------

## Parameters [¶](#parameters){.headerlink}

  ------------------ ---------- ----------------------------------------------------------------------------------------------------------------- --------------- -----------
  Name               Required   Description                                                                                                       Default Value   Example
  user_id            required   The ID of the user for whom to return results. Either an id or screen_name is required for this method.                           *12345*
  screen_name        required   The screen name of the user for whom to return results. Either a id or screen_name is required for this method.                   *noradio*
  include_entities   optional   The *entities* node will not be included when set to *false* .                                                                    *false*
  ------------------ ---------- ----------------------------------------------------------------------------------------------------------------- --------------- -----------

## Example Request [¶](#example-request){.headerlink}

    $ curl --request GET 
        --url 'https://api.twitter.com/1.1/users/show.json?screen_name=twitterdev' 
        --header 'authorization: Bearer <bearer>'

    $ curl --request GET 
      --url 'https://api.twitter.com/1.1/users/show.json?screen_name=twitterdev' 
      --header 'authorization: OAuth oauth_consumer_key="consumer-key-for-app", 
      oauth_nonce="generated-nonce", oauth_signature="generated-signature", 
      oauth_signature_method="HMAC-SHA1", oauth_timestamp="generated-timestamp", 
      oauth_version="1.0"'

    $ twurl /1.1/users/show.json?screen_name=twitterdev

## Example Response [¶](#example-response){.headerlink}

    {user-object}

For more detail, see the [user-object
definition](/en/docs/tweets/data-dictionary/overview/user-object) .
:::
:::
:::
:::
:::
:::
:::
