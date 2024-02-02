<div>

::: c01-rich-text-editor
Returns the relationships of the authenticating user to the
comma-separated list of up to 100 screen_names or user_ids provided.
Values for ` connections ` can be: ` following ` ,
` following_requested ` , ` followed_by ` , ` none ` , ` blocking ` ,
` muting ` .

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/friendships/lookup.json `

  -------------------------------------- -------------------------
  Response formats                       JSON
  Requires authentication?               Yes (user context only)
  Rate limited?                          Yes
  Requests / 15-min window (user auth)   15
  -------------------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

  ------------- ---------- ------------------------------------------------------------------------------------ --------------- ----------------------
  Name          Required   Description                                                                          Default Value   Example
  screen_name   optional   A comma separated list of screen names, up to 100 are allowed in a single request.                   *twitterapi twitter*
  user_id       optional   A comma separated list of user IDs, up to 100 are allowed in a single request.                       *783214 6253282*
  ------------- ---------- ------------------------------------------------------------------------------------ --------------- ----------------------

## Example Requests [¶](#example-requests){.headerlink}

    $ curl --request GET 
      --url 'https://api.twitter.com/1.1/friendships/lookup.json?screen_name=andypiper%2Cbinary_aaron%2Ctwitterdev%2Chappycamper%2Charris_0ff' 
      --header 'authorization: OAuth oauth_consumer_key="consumer-key-for-app", 
      oauth_nonce="generated-nonce", oauth_signature="generated-signature", 
      oauth_signature_method="HMAC-SHA1", oauth_timestamp="generated-timestamp", 
      oauth_token="access-token-for-authed-user", oauth_version="1.0"'

    $ twurl /1.1/friendships/lookup.json?screen_name=andypiper,binary_aaron,twitterdev,happycamper,harris_0ff

## Example Response [¶](#example-response){.headerlink}

    [
      {
        "name": "andy piper (pipes)",
        "screen_name": "andypiper",
        "id": 786491,
        "id_str": "786491",
        "connections": [
          "following"
        ]
      },
      {
        "name": "λ🥑. 🍞",
        "screen_name": "binary_aaron",
        "id": 165837734,
        "id_str": "165837734",
        "connections": [
          "following",
          "followed_by"
        ]
      },
      {
        "name": "Twitter Dev",
        "screen_name": "TwitterDev",
        "id": 2244994945,
        "id_str": "2244994945",
        "connections": [
          "following"
        ]
      },
      {
        "name": "Emily Sheehan 🏕",
        "screen_name": "happycamper",
        "id": 63046977,
        "id_str": "63046977",
        "connections": [
          "none"
        ]
      },
      {
        "name": "Harrison Test",
        "screen_name": "Harris_0ff",
        "id": 4337869213,
        "id_str": "4337869213",
        "connections": [
          "following",
          "following_requested",
          "followed_by"
        ]
      }
    ]
:::

</div>
