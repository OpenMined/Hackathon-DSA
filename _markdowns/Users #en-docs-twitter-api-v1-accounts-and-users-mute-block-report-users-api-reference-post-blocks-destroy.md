<div>

::: c01-rich-text-editor
Un-blocks the user specified in the ID parameter for the authenticating
user. Returns the un-blocked user when successful. If relationships
existed before the block was instantiated, they will not be restored.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/blocks/destroy.json `

  -------------------------- -------------------------
  Response formats           JSON
  Requires authentication?   Yes (user context only)
  Rate limited?              Yes
  -------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

  ------------------ ---------- ------------------------------------------------------------------------------------------------------------------------- --------------- -----------
  Name               Required   Description                                                                                                               Default Value   Example
  screen_name        optional   The screen name of the potentially blocked user. Helpful for disambiguating when a valid screen name is also a user ID.                   *noradio*
  user_id            optional   The ID of the potentially blocked user. Helpful for disambiguating when a valid user ID is also a valid screen name.                      *12345*
  include_entities   optional   The *entities* node will not be included when set to *false* .                                                                            *false*
  skip_status        optional   When set to either *true* , *t* or *1* statuses will not be included in the returned user objects.                                        
  ------------------ ---------- ------------------------------------------------------------------------------------------------------------------------- --------------- -----------

## Example Request [¶](#example-request){.headerlink}

` POST https://api.twitter.com/1.1/blocks/destroy.json?screen_name=theSeanCook&skip_status=1 `

## Example Response [¶](#example-response){.headerlink}

    {
        "contributors_enabled": true,
        "created_at": "Sat May 09 17:58:22 +0000 2009",
        "default_profile": false,
        "default_profile_image": false,
        "description": "I taught your phone that thing you like.  The Mobile Partner Engineer @Twitter. ",
        "entities": {
            "description": {
                "urls": []
            }
        },
        "favourites_count": 586,
        "follow_request_sent": false,
        "followers_count": 10622,
        "following": false,
        "friends_count": 1181,
        "geo_enabled": true,
        "id": 38895958,
        "id_str": "38895958",
        "is_translator": false,
        "lang": "en",
        "listed_count": 190,
        "location": "San Francisco",
        "name": "Sean Cook",
        "notifications": false,
        "profile_background_color": "1A1B1F",
        "profile_background_image_url": "http://a0.twimg.com/profile_background_images/495742332/purty_wood.png",
        "profile_background_image_url_https": "https://si0.twimg.com/profile_background_images/495742332/purty_wood.png",
        "profile_background_tile": true,
        "profile_image_url": "http://a0.twimg.com/profile_images/1751506047/dead_sexy_normal.JPG",
        "profile_image_url_https": "https://si0.twimg.com/profile_images/1751506047/dead_sexy_normal.JPG",
        "profile_link_color": "2FC2EF",
        "profile_sidebar_border_color": "181A1E",
        "profile_sidebar_fill_color": "252429",
        "profile_text_color": "666666",
        "profile_use_background_image": true,
        "protected": false,
        "screen_name": "theSeanCook",
        "show_all_inline_media": true,
        "statuses_count": 2609,
        "time_zone": "Pacific Time (US & Canada)",
        "url": null,
        "utc_offset": -28800,
        "verified": false
    }
:::

</div>
