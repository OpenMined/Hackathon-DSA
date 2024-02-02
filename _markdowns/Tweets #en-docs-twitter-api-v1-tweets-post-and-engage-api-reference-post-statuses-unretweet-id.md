<div>

::: c01-rich-text-editor
Untweets a retweeted status. Returns the original Tweet with Retweet
details embedded.

**Usage Notes** :

-   This method is subject to update limits. A HTTP 429 will be returned
    if this limit has been hit.
-   The untweeted retweet status ID must be authored by the user backing
    the authentication token.
-   An application must have write privileges to POST. A HTTP 401 will
    be returned for read-only applications.
-   When passing a source status ID instead of the retweet status ID a
    HTTP 200 response will be returned with the same Tweet object but no
    action.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/statuses/unretweet/:id.json `

  -------------------------- -------------------------
  Response formats           JSON
  Requires authentication?   Yes (user context only)
  Rate limited?              Yes
  -------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

  ----------- ---------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------- ---------
  Name        Required   Description                                                                                                                                                                                                      Default Value   Example
  id          required   The numerical ID of the desired status.                                                                                                                                                                                          *123*
  trim_user   optional   When set to either *true* , *t* or *1* , each Tweet returned in a timeline will include a user object including only the status authors numerical ID. Omit this parameter to receive the complete user object.                   *true*
  ----------- ---------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------- ---------

## Example Request [¶](#example-request){.headerlink}

` POST https://api.twitter.com/1.1/statuses/unretweet/1050118621198921728.json `

## Example Response [¶](#example-response){.headerlink}

    {
      "created_at": "Wed Oct 10 20:19:24 +0000 2018",
      "id": 1050118621198921728,
      "id_str": "1050118621198921728",
      "text": "To make room for more expression, we will now count all emojis as equal—including those with gender‍‍‍ and skin t… https://t.co/MkGjXf9aXm",
      "truncated": true,
      "entities": {
        "hashtags": [],
        "symbols": [],
        "user_mentions": [],
        "urls": [
          {
            "url": "https://t.co/MkGjXf9aXm",
            "expanded_url": "https://twitter.com/i/web/status/1050118621198921728",
            "display_url": "twitter.com/i/web/status/1…",
            "indices": [
              117,
              140
            ]
          }
        ]
      },
      "source": "<a href="http://twitter.com" rel="nofollow">Twitter Web Client</a>",
      "in_reply_to_status_id": null,
      "in_reply_to_status_id_str": null,
      "in_reply_to_user_id": null,
      "in_reply_to_user_id_str": null,
      "in_reply_to_screen_name": null,
      "user": {
        "id": 6253282,
        "id_str": "6253282",
        "name": "Twitter API",
        "screen_name": "TwitterAPI",
        "location": "San Francisco, CA",
        "description": "The Real Twitter API. Tweets about API changes, service issues and our Developer Platform. Don't get an answer? It's on my website.",
        "url": "https://t.co/8IkCzCDr19",
        "entities": {
          "url": {
            "urls": [
              {
                "url": "https://t.co/8IkCzCDr19",
                "expanded_url": "https://developer.twitter.com",
                "display_url": "developer.twitter.com",
                "indices": [
                  0,
                  23
                ]
              }
            ]
          },
          "description": {
            "urls": []
          }
        },
        "protected": false,
        "followers_count": 6128663,
        "friends_count": 12,
        "listed_count": 12900,
        "created_at": "Wed May 23 06:01:13 +0000 2007",
        "favourites_count": 32,
        "utc_offset": null,
        "time_zone": null,
        "geo_enabled": null,
        "verified": true,
        "statuses_count": 3659,
        "lang": "null",
        "contributors_enabled": null,
        "is_translator": null,
        "is_translation_enabled": null,
        "profile_background_color": "null",
        "profile_background_image_url": "null",
        "profile_background_image_url_https": "null",
        "profile_background_tile": nulll,
        "profile_image_url": "null",
        "profile_image_url_https": "https://pbs.twimg.com/profile_images/942858479592554497/BbazLO9L_normal.jpg",
        "profile_banner_url": "https://pbs.twimg.com/profile_banners/6253282/1497491515",
        "profile_link_color": "null",
        "profile_sidebar_border_color": "null",
        "profile_sidebar_fill_color": "null",
        "profile_text_color": "null",
        "profile_use_background_image": null,
        "has_extended_profile": null,
        "default_profile": false,
        "default_profile_image": false,
        "following": nul,
        "follow_request_sent": null,
        "notifications": null,
        "translator_type": "null"
      },
      "geo": null,
      "coordinates": null,
      "place": null,
      "contributors": null,
      "is_quote_status": false,
      "retweet_count": 161,
      "favorite_count": 296,
      "favorited": false,
      "retweeted": false,
      "possibly_sensitive": false,
      "possibly_sensitive_appealable": false,
      "lang": "en"
    }
:::

</div>
