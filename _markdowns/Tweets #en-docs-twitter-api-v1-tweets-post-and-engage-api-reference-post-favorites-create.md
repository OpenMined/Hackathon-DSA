::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
Note: favorites are now known as *likes* .

Favorites ( *likes* ) the Tweet specified in the ID parameter as the
authenticating user. Returns the favorite Tweet when successful.

The process invoked by this method is asynchronous. The immediately
returned Tweet object may not indicate the resultant favorited status of
the Tweet. A 200 OK response from this method will indicate whether the
intended action was successful or not.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/favorites/create.json `

  --------------------------- -----------------------------
  Response formats            JSON
  Requires authentication?    Yes (user context only)
  Rate limited?               Yes
  Requests / 24-hour window   1000 per user; 1000 per app
  --------------------------- -----------------------------

## Parameters [¶](#parameters){.headerlink}

  ------------------ ---------- ----------------------------------------------------------- --------------- ---------
  Name               Required   Description                                                 Default Value   Example
  id                 required   The numerical ID of the Tweet to like.                                      *123*
  include_entities   optional   The *entities* node will be omitted when set to *false* .                   *false*
  ------------------ ---------- ----------------------------------------------------------- --------------- ---------

## Example Request [¶](#example-request){.headerlink}

    curl --request POST 
    --url 'https://api.twitter.com/1.1/favorites/create.json?id=TWEET_ID_TO_FAVORITE' 
    --header 'authorization: OAuth oauth_consumer_key="YOUR_CONSUMER_KEY", oauth_nonce="AUTO_GENERATED_NONCE", oauth_signature="AUTO_GENERATED_SIGNATURE", oauth_signature_method="HMAC-SHA1", oauth_timestamp="AUTO_GENERATED_TIMESTAMP", oauth_token="USERS_ACCESS_TOKEN", oauth_version="1.0"' 
    --header 'content-type: application/json'

## Example Response [¶](#example-response){.headerlink}

    {tweet-object,
    "user": {user-object}
    }
:::
:::
:::
:::
:::
:::
:::
