<div>

::: c01-rich-text-editor
Returns the specified list. Private lists will only be shown if the
authenticated user owns the specified list.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/lists/show.json `

  -------------------------------------- ------
  Response formats                       JSON
  Requires authentication?               Yes
  Rate limited?                          Yes
  Requests / 15-min window (user auth)   75
  Requests / 15-min window (app auth)    75
  -------------------------------------- ------

## Parameters [¶](#parameters){.headerlink}

  ------------------- ---------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------- ---------
  Name                Required   Description                                                                                                                                                                                              Default Value   Example
  list_id             required   The numerical *id* of the list.                                                                                                                                                                                          
  slug                required   You can identify a list by its slug instead of its numerical id. If you decide to do so, note that you\'ll also have to specify the list owner using the *owner_id* or *owner_screen_name* parameters.                   
  owner_screen_name   optional   The screen name of the user who owns the list being requested by a *slug* .                                                                                                                                              
  owner_id            optional   The user ID of the user who owns the list being requested by a *slug* .                                                                                                                                                  
  ------------------- ---------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------- ---------

## Example Request [¶](#example-request){.headerlink}

` GET https://api.twitter.com/1.1/lists/show.json?slug=team&owner_screen_name=twitter `

## Example Response [¶](#example-response){.headerlink}

    {
      "created_at": "Wed Sep 23 01:18:01 +0000 2009",
      "slug": "team",
      "name": "Team",
      "full_name": "@twitter/team",
      "description": "",
      "mode": "public",
      "following": false,
      "user": {
        "geo_enabled": true,
        "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme18/bg.gif",
        "profile_background_color": "ACDED6",
        "protected": false,
        "listed_count": 66019,
        "profile_background_tile": false,
        "created_at": "Tue Feb 20 14:35:54 +0000 2007",
        "friends_count": 695,
        "name": "Twitter",
        "profile_sidebar_fill_color": "F6F6F6",
        "notifications": false,
        "utc_offset": -28800,
        "profile_image_url_https": "https://si0.twimg.com/profile_images/1124040897/at-twitter_normal.png",
        "description": "Always wondering what's happening. ",
        "display_url": null,
        "following": false,
        "verified": true,
        "favourites_count": 16,
        "profile_sidebar_border_color": "EEEEEE",
        "followers_count": 6619092,
        "profile_image_url": "http://a0.twimg.com/profile_images/1124040897/at-twitter_normal.png",
        "default_profile_image": false,
        "contributors_enabled": true,
        "deactivated_bit": false,
        "statuses_count": 1218,
        "profile_use_background_image": true,
        "location": "San Francisco, CA",
        "id_str": "783214",
        "default_profile": false,
        "show_all_inline_media": true,
        "profile_text_color": "333333",
        "screen_name": "twitter",
        "follow_request_sent": false,
        "profile_background_image_url": "http://a1.twimg.com/images/themes/theme18/bg.gif",
        "url": "http://blog.twitter.com/",
        "expanded_url": null,
        "is_translator": false,
        "time_zone": "Pacific Time (US & Canada)",
        "profile_link_color": "038543",
        "id": 783214,
        "entities": {
          "urls": [],
          "user_mentions": [],
          "hashtags": []
        },
        "suspended": false,
        "lang": "en"
      },
      "member_count": 643,
      "id_str": "574",
      "subscriber_count": 76779,
      "id": 574,
      "uri": "/twitter/team"
    }
:::

</div>
