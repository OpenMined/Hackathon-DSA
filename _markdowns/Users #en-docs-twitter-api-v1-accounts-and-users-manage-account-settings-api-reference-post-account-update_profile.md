<div>

::: c01-rich-text-editor
Sets some values that users are able to set under the \"Account\" tab of
their settings page. Only the parameters specified will be updated.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/account/update_profile.json `

  -------------------------- -------------------------
  Response formats           JSON
  Requires authentication?   Yes (user context only)
  Rate limited?              Yes
  -------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

  ------------------ ---------- ---------------------------------------------------------------------------------------------------------------------------------- --------------- -----------------------------------------------------------------------------
  Name               Required   Description                                                                                                                        Default Value   Example
  name               optional   Full name associated with the profile.                                                                                                             *Marcel Molina*
  url                optional   URL associated with the profile. Will be prepended with ` http:// ` if not present.                                                                ` http://project.ioni.st `
  location           optional   The city or country describing where the user of the account is located. The contents are not normalized or geocoded in any way.                   *San Francisco CA*
  description        optional   A description of the user owning the account.                                                                                                      *Flipped my wig at age 22 and it never grew back. Also: I work at Twitter.*
  include_entities   optional   The *entities* node will not be included when set to *false* .                                                                                     *false*
  skip_status        optional   When set to either *true* , *t* or *1* statuses will not be included in the returned user object.                                                  
  ------------------ ---------- ---------------------------------------------------------------------------------------------------------------------------------- --------------- -----------------------------------------------------------------------------

## Example Request [¶](#example-request){.headerlink}

` POST https://api.twitter.com/1.1/account/update_profile.json?name=Sean%20Cook&description=Keep%20calm%20and%20rock%20on. `

## Example Response [¶](#example-response){.headerlink}

    {
        "contributors_enabled": false,
        "created_at": "Thu Aug 23 19:45:07 +0000 2012",
        "default_profile": false,
        "default_profile_image": false,
        "description": "Keep calm and rock on.",
        "favourites_count": 0,
        "follow_request_sent": false,
        "followers_count": 0,
        "following": false,
        "friends_count": 10,
        "geo_enabled": true,
        "id": 776627022,
        "id_str": "776627022",
        "is_translator": false,
        "lang": "en",
        "listed_count": 0,
        "location": "San Francisco, CA",
        "name": "Sean Cook",
        "notifications": false,
        "profile_background_color": "9AE4E8",
        "profile_background_image_url": "http://a0.twimg.com/images/themes/theme16/bg.gif",
        "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme16/bg.gif",
        "profile_background_tile": false,
        "profile_image_url": "http://a0.twimg.com/profile_images/2550256790/hv5rtkvistn50nvcuydl_normal.jpeg",
        "profile_image_url_https": "https://si0.twimg.com/profile_images/2550256790/hv5rtkvistn50nvcuydl_normal.jpeg",
        "profile_sidebar_border_color": "BDDCAD",
        "profile_sidebar_fill_color": "DDFFCC",
        "profile_text_color": "333333",
        "profile_use_background_image": true,
        "protected": false,
        "screen_name": "s0c1alm3dia",
        "show_all_inline_media": false,
        "statuses_count": 0,
        "time_zone": "Pacific Time (US & Canada)",
        "url": "http://cnn.com",
        "utc_offset": -28800,
        "verified": false
    }
:::

</div>
