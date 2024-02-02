<div>

::: c01-rich-text-editor
Find Collections created by a specific user or containing a specific
curated Tweet.

Results are organized in a cursored collection.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/collections/list.json `

  -------------------------------------- -------------------------
  Response formats                       JSON
  Requires authentication?               Yes (user context only)
  Rate limited?                          Yes
  Requests / 15-min window (user auth)   1000
  -------------------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

  ------------- ---------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------- ----------------------
  Name          Required   Description                                                                                                                                                                                                           Default Value   Example
  user_id       required   The ID of the user for whom to return results.                                                                                                                                                                                        *20*
  screen_name   required   The screen name of the user for whom to return results.                                                                                                                                                                               *twitterdev*
  tweet_id      optional   The identifier of the Tweet for which to return results.                                                                                                                                                                              *514533751213551616*
  count         optional   Specifies the *maximum* number of results to include in the response. Specify a count between 1 and 200. A *next_cursor* value will be provided in the response if additional results are available.                                  *100*
  cursor        optional   A string identifying the segment of the current result set to retrieve. Values for this parameter are yielded in the *cursors* node attached to response objects. Usage of the *count* parameter affects cursoring.                   *BXb2synCEAE*
  ------------- ---------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------- ----------------------

## Example Request [¶](#example-request){.headerlink}

` GET https://api.twitter.com/1.1/collections/list.json?screen_name=twittermusic&count=1 `

## Example Response [¶](#example-response){.headerlink}

    {
      "objects": {
        "users": {
          "373471064": {
            "id": 373471064,
            "id_str": "373471064",
            "name": "Twitter Music",
            "screen_name": "TwitterMusic",
            "location": "Twitter HQ",
            "description": "Music related Tweets from around the world.",
            "url": "http://t.co/7eUtBKV1bf",
            "entities": {
              "url": {
                "urls": [{
                  "url": "http://t.co/7eUtBKV1bf",
                  "expanded_url": "http://music.twitter.com",
                  "display_url": "music.twitter.com",
                  "indices": [0, 22]
                }]
              },
              "description": {
                "urls": []
              }
            },
            "protected": false,
            "followers_count": 7914124,
            "friends_count": 276,
            "listed_count": 9443,
            "created_at": "Wed Sep 14 16:50:47 +0000 2011",
            "favourites_count": 958,
            "utc_offset": -36000,
            "time_zone": "Hawaii",
            "geo_enabled": true,
            "verified": true,
            "statuses_count": 8416,
            "lang": "en",
            "contributors_enabled": false,
            "is_translator": false,
            "is_translation_enabled": false,
            "profile_background_color": "131516",
            "profile_background_image_url": "http://abs.twimg.com/images/themes/theme14/bg.gif",
            "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme14/bg.gif",
            "profile_background_tile": true,
            "profile_image_url": "http://pbs.twimg.com/profile_images/378800000449287089/70dea90873e8a0f92fd582b4d04cfd4b_normal.png",
            "profile_image_url_https": "https://pbs.twimg.com/profile_images/378800000449287089/70dea90873e8a0f92fd582b4d04cfd4b_normal.png",
            "profile_banner_url": "https://pbs.twimg.com/profile_banners/373471064/1433882163",
            "profile_link_color": "009999",
            "profile_sidebar_border_color": "000000",
            "profile_sidebar_fill_color": "EFEFEF",
            "profile_text_color": "333333",
            "profile_use_background_image": true,
            "default_profile": false,
            "default_profile_image": false,
            "following": false,
            "follow_request_sent": false,
            "notifications": false
          }
        },
        "timelines": {
          "custom-588824628950269952": {
            "name": "Josh Groban Tour",
            "user_id": "373471064",
            "collection_url": "https://twitter.com/TwitterMusic/timelines/588824628950269952",
            "description": "Josh announces his tour by replying to fans in different cities",
            "url": "",
            "visibility": "public",
            "timeline_order": "curation_reverse_chron",
            "collection_type": "user"
          }
        }
      },
      "response": {
        "results": [{
          "timeline_id": "custom-588824628950269952"
        }],
        "cursors": {
          "next_cursor": "B9XAeo1CcAA"
        }
      }
    }
:::

</div>
