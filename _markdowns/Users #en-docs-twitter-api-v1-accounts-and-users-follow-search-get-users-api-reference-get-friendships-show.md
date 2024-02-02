<div>

::: c01-rich-text-editor
Returns detailed information about the relationship between two
arbitrary users.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/friendships/show.json `

  -------------------------------------- ------
  Response formats                       JSON
  Requires authentication?               Yes
  Rate limited?                          Yes
  Requests / 15-min window (user auth)   180
  Requests / 15-min window (app auth)    15
  -------------------------------------- ------

## Parameters [¶](#parameters){.headerlink}

  -------------------- ---------- -------------------------------------- --------------- --------------
  Name                 Required   Description                            Default Value   Example
  source_id            optional   The user_id of the subject user.                       *783214*
  source_screen_name   optional   The screen_name of the subject user.                   *Twitter*
  target_id            optional   The user_id of the target user.                        *2244994945*
  target_screen_name   optional   The screen_name of the target user.                    *TwitterDev*
  -------------------- ---------- -------------------------------------- --------------- --------------

## Example Request [¶](#example-request){.headerlink}

` GET https://api.twitter.com/1.1/friendships/show.json?source_screen_name=twitterdev&target_screen_name=twitter `

## Example Response [¶](#example-response){.headerlink}

    {
      "relationship": {
        "source": {
          "id": 783214,
          "id_str": "783214",
          "screen_name": "Twitter",
          "following": true,
          "followed_by": true,
          "live_following": false,
          "following_received": null,
          "following_requested": null,
          "notifications_enabled": null,
          "can_dm": true,
          "blocking": null,
          "blocked_by": null,
          "muting": null,
          "want_retweets": null,
          "all_replies": null,
          "marked_spam": null
        },
        "target": {
          "id": 2244994945,
          "id_str": "2244994945",
          "screen_name": "TwitterDev",
          "following": true,
          "followed_by": true,
          "following_received": null,
          "following_requested": null
        }
      }
    }
:::

</div>
