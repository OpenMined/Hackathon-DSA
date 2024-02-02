::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
Retweets a tweet. Returns the original Tweet with Retweet details
embedded.

*Usage Notes* :

-   This method is subject to update limits. A HTTP 403 will be returned
    if this limit as been hit.
-   Twitter will ignore attempts to perform duplicate retweets.
-   The retweet_count will be current as of when the payload is
    generated and may not reflect the exact count. It is intended as an
    approximation.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/statuses/retweet/:id.json `

  -------------------------- -------------------------------
  Response formats           JSON
  Requires authentication?   Yes (user context only)
  Rate limited?              Yes
  Requests / 3-hour window   300\* per user; 300\* per app
  -------------------------- -------------------------------

*Please note* - The 300 per 3 hours is a combined limit with the [POST
statuses/update](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-statuses-update)
endpoint. You can only post 300 Tweets or Retweets during a 3 hour
period.

## Parameters [¶](#parameters){.headerlink}

  ----------- ---------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------- ---------
  Name        Required   Description                                                                                                                                                                                                      Default Value   Example
  id          required   The numerical ID of the desired status.                                                                                                                                                                                          *123*
  trim_user   optional   When set to either *true* , *t* or *1* , each tweet returned in a timeline will include a user object including only the status authors numerical ID. Omit this parameter to receive the complete user object.                   *true*
  ----------- ---------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------- ---------

## Example Request [¶](#example-request){.headerlink}

    $ curl --request POST 
    --url 'https://api.twitter.com/1.1/statuses/retweet/TWEET_ID.json' 
    --header 'authorization: OAuth oauth_consumer_key="YOUR_CONSUMER_KEY", oauth_nonce="AUTO_GENERATED_NONCE", oauth_signature="AUTO_GENERATED_SIGNATURE", oauth_signature_method="HMAC-SHA1", oauth_timestamp="AUTO_GENERATED_TIMESTAMP", oauth_token="USERS_ACCESS_TOKEN", oauth_version="1.0"' 
    --header 'content-type: application/json'

## Example Response [¶](#example-response){.headerlink}

    {retweet-status-object,
    "user": {retweeting-user-object},
    "retweeted_status": {retweeted-status-object,
      "user": {retweeted-user-object}
    }
    }
:::
:::
:::
:::
:::
:::
:::
