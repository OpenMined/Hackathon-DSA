<div>

::: c01-rich-text-editor
Provides a simple, relevance-based search interface to public user
accounts on Twitter. Try querying by topical interest, full name,
company name, location, or other criteria. Exact match searches are not
supported.

Only the first 1,000 matching results are available.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/users/search.json `

  -------------------------------------- -------------------------
  Response formats                       JSON
  Requires authentication?               Yes (user context only)
  Rate limited?                          Yes
  Requests / 15-min window (user auth)   900
  -------------------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

  ------------------ ---------- -------------------------------------------------------------------------------------------- --------------- -----------------
  Name               Required   Description                                                                                  Default Value   Example
  q                  required   The search query to run against people search.                                                               *Twitter%20API*
  page               optional   Specifies the page of results to retrieve.                                                                   *3*
  count              optional   The number of potential user results to retrieve per page. This value has a maximum of 20.                   *5*
  include_entities   optional   The *entities* node will not be included in embedded Tweet objects when set to *false* .                     *false*
  ------------------ ---------- -------------------------------------------------------------------------------------------- --------------- -----------------

## Example Request [¶](#example-request){.headerlink}

    $ curl --request GET 
      --url 'https://api.twitter.com/1.1/users/search.json?q=soccer' 
      --header 'authorization: OAuth oauth_consumer_key="consumer-key-for-app", 
      oauth_nonce="generated-nonce", oauth_signature="generated-signature", 
      oauth_signature_method="HMAC-SHA1", oauth_timestamp="generated-timestamp", 
      oauth_token="access-token-for-authed-user", oauth_version="1.0"'

    $ twurl /1.1/users/search.json?q=soccer

## Example Response [¶](#example-response){.headerlink}

    [
      {user-object},
      {user-object},
      {user-object},
      {user-object},
      {user-object},
      {user-object}
    ]

For more detail, see the [user-object
definition](/en/docs/tweets/data-dictionary/overview/user-object) .
:::

</div>
