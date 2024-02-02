<div>

::: c01-rich-text-editor
Updates the authenticating user\'s profile image. Note that this method
expects raw multipart data, not a URL to an image.

This method asynchronously processes the uploaded file before updating
the user\'s profile image URL. You can either update your local cache
the next time you request the user\'s information, or, at least 5
seconds after uploading the image, ask for the updated URL using [GET
users /
show](/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-show)
.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/account/update_profile_image.json `

  -------------------------- -------------------------
  Response formats           JSON
  Requires authentication?   Yes (user context only)
  Rate limited?              Yes
  -------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

  ------------------ ---------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------- ---------
  Name               Required   Description                                                                                                                                                                                                                                                                              Default Value   Example
  image              required   The avatar image for the profile, base64-encoded. Must be a valid GIF, JPG, or PNG image of less than 700 kilobytes in size. Images with width larger than 400 pixels will be scaled down. Animated GIFs will be converted to a static GIF of the first frame, removing the animation.                   
  include_entities   optional   The *entities* node will not be included when set to *false* .                                                                                                                                                                                                                                           *false*
  skip_status        optional   When set to either *true* , *t* or *1* statuses will not be included in the returned user objects.                                                                                                                                                                                                       
  ------------------ ---------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------- ---------

## Example Request [¶](#example-request){.headerlink}

` POST https://api.twitter.com/1.1/account/update_profile_image.json?image=ABCDEFGH... `

## Example Response [¶](#example-response){.headerlink}

    {
        "contributors_enabled": false, 
        "created_at": "Thu Aug 23 19:45:07 +0000 2012", 
        "default_profile": false, 
        "default_profile_image": false, 
        "description": "Keep calm and test", 
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
        "name": "Sean Test", 
        "notifications": false, 
        "profile_background_color": "000000", 
        "profile_background_image_url": "http://a0.twimg.com/profile_background_images/644522235/cdjlccey99gy36j3em67.jpeg", 
        "profile_background_image_url_https": "https://si0.twimg.com/profile_background_images/644522235/cdjlccey99gy36j3em67.jpeg", 
        "profile_background_tile": true, 
        "profile_image_url": "http://a0.twimg.com/profile_images/2550256790/hv5rtkvistn50nvcuydl_normal.jpeg", 
        "profile_image_url_https": "https://si0.twimg.com/profile_images/2550256790/hv5rtkvistn50nvcuydl_normal.jpeg", 
        "profile_link_color": "000000", 
        "profile_sidebar_border_color": "000000", 
        "profile_sidebar_fill_color": "000000", 
        "profile_text_color": "000000", 
        "profile_use_background_image": false, 
        "protected": false, 
        "screen_name": "s0c1alm3dia", 
        "show_all_inline_media": false, 
        "statuses_count": 0, 
        "time_zone": "Pacific Time (US & Canada)", 
        "url": "http://twitter.com", 
        "utc_offset": -28800, 
        "verified": false
    }
:::

</div>
