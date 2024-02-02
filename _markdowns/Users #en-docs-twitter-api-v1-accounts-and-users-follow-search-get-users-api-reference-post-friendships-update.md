<div>

::: c01-rich-text-editor
Turn on/off Retweets and device notifications from the specified user.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/friendships/update.json `

  -------------------------- -------------------------
  Response formats           JSON
  Requires authentication?   Yes (user context only)
  Rate limited?              Yes
  -------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

  ------------- ---------- -------------------------------------------------------- --------------- --------------
  Name          Required   Description                                              Default Value   Example
  screen_name   optional   The screen name of the user being followed.                              *twitterdev*
  user_id       optional   The ID of the user being followed.                                       *2244994945*
  device        optional   Turn on/off device notifications from the target user.                   *true*
  retweets      optional   Turn on/off Retweets from the target user.                               *false*
  ------------- ---------- -------------------------------------------------------- --------------- --------------

## Example Request [¶](#example-request){.headerlink}

` twurl -X POST /1.1/friendships/update.json?user_id=2244994945 `

## Example Response [¶](#example-response){.headerlink}

    {
      "relationship": {
        "source": {
          "id": 63046977,
          "id_str": "63046977",
          "screen_name": "happycamper",
          "following": true,
          "followed_by": false,
          "live_following": false,
          "following_received": null,
          "following_requested": false,
          "notifications_enabled": false,
          "can_dm": false,
          "blocking": false,
          "blocked_by": false,
          "muting": false,
          "want_retweets": true,
          "all_replies": false,
          "marked_spam": false
        },
        "target": {
          "id": 2244994945,
          "id_str": "2244994945",
          "screen_name": "TwitterDev",
          "following": false,
          "followed_by": true,
          "following_received": false,
          "following_requested": null
        }
      }
    }
:::

</div>
