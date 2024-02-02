<div>

::: c01-rich-text-editor
Returns the lists the specified user has been added to. If ` user_id `
or ` screen_name ` are not provided, the memberships for the
authenticating user are returned.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/lists/memberships.json `

  -------------------------------------- ------
  Response formats                       JSON
  Requires authentication?               Yes
  Rate limited?                          Yes
  Requests / 15-min window (user auth)   75
  Requests / 15-min window (app auth)    75
  -------------------------------------- ------

## Parameters [¶](#parameters){.headerlink}

  ----------------------- ---------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------- ---------
  Name                    Required   Description                                                                                                                                                                                                                                                                                                                                             Default Value   Example
  user_id                 optional   The ID of the user for whom to return results. Helpful for disambiguating when a valid user ID is also a valid screen name.                                                                                                                                                                                                                                             
  screen_name             optional   The screen name of the user for whom to return results. Helpful for disambiguating when a valid screen name is also a user ID.                                                                                                                                                                                                                                          
  count                   optional   The amount of results to return per page. Defaults to 20. No more than 1000 results will ever be returned in a single page.                                                                                                                                                                                                                                             
  cursor                  optional   Breaks the results into pages. Provide a value of *-1* to begin paging. Provide values as returned in the response body\'s *next_cursor* and *previous_cursor* attributes to page back and forth in the list. It is recommended to always use cursors when the method supports them. See [Cursoring](/en/docs/basics/cursoring) for more information.                   
  filter_to_owned_lists   optional   When set to *true* , *t* or *1* , will return just lists the authenticating user owns, and the user represented by *user_id* or *screen_name* is a member of.                                                                                                                                                                                                           
  ----------------------- ---------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------- ---------

## Example Request [¶](#example-request){.headerlink}

` GET https://api.twitter.com/1.1/lists/memberships.json?screen_name=twitter&cursor=-1 `

## Example Response [¶](#example-response){.headerlink}

    {
      "previous_cursor": 0,
      "lists": [
        {
          "name": "Digital Marketing",
          "slug": "digital-marketing",
          "uri": "/pointcg/digital-marketing",
          "id_str": "49260625",
          "subscriber_count": 1,
          "member_count": 46,
          "mode": "public",
          "id": 49260625,
          "full_name": "@pointcg/digital-marketing",
          "description": "",
          "user": {
            "profile_sidebar_border_color": "447DBC",
            "profile_background_tile": false,
            "profile_sidebar_fill_color": "447DBC",
            "name": "Chris Greco",
            "created_at": "Wed Feb 28 01:05:01 +0000 2007",
            "location": "",
            "profile_image_url": "http://a1.twimg.com/profile_images/1331628329/chris_2_normal.jpg",
            "follow_request_sent": false,
            "profile_link_color": "0000FF",
            "is_translator": false,
            "id_str": "799757",
            "default_profile": false,
            "favourites_count": 2,
            "contributors_enabled": false,
            "url": null,
            "id": 799757,
            "profile_image_url_https": "https://si0.twimg.com/profile_images/1331628329/chris_2_normal.jpg",
            "utc_offset": -18000,
            "profile_use_background_image": true,
            "listed_count": 4,
            "lang": "en",
            "followers_count": 66,
            "profile_text_color": "000000",
            "protected": false,
            "profile_background_color": "0F5B5F",
            "verified": false,
            "time_zone": "Eastern Time (US & Canada)",
            "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme1/bg.png",
            "description": "",
            "notifications": false,
            "geo_enabled": false,
            "statuses_count": 122,
            "default_profile_image": false,
            "friends_count": 80,
            "profile_background_image_url": "http://a0.twimg.com/images/themes/theme1/bg.png",
            "following": false,
            "screen_name": "pointcg",
            "show_all_inline_media": false
          },
          "following": false
        },
        {
          "name": "vanessa williams",
          "slug": "vanessa-williams",
          "uri": "/Barbis_doll/vanessa-williams",
          "id_str": "49270287",
          "subscriber_count": 0,
          "member_count": 1,
          "mode": "public",
          "id": 49270287,
          "full_name": "@Barbis_doll/vanessa-williams",
          "description": "former ms. america, talented dancer, singer and actress",
          "user": {
            "profile_sidebar_border_color": "C0DEED",
            "name": "Debbie M.",
            "profile_background_tile": false,
            "profile_sidebar_fill_color": "DDEEF6",
            "location": null,
            "profile_image_url": "http://a3.twimg.com/sticky/default_profile_images/default_profile_4_normal.png",
            "created_at": "Tue Jun 28 00:50:43 +0000 2011",
            "is_translator": false,
            "profile_link_color": "0084B4",
            "id_str": "325263705",
            "follow_request_sent": null,
            "url": null,
            "favourites_count": 0,
            "contributors_enabled": false,
            "default_profile": true,
            "utc_offset": null,
            "id": 325263705,
            "profile_image_url_https": "https://si0.twimg.com/sticky/default_profile_images/default_profile_4_normal.png",
            "listed_count": 0,
            "profile_use_background_image": true,
            "protected": false,
            "followers_count": 2,
            "lang": "en",
            "profile_text_color": "333333",
            "time_zone": null,
            "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme1/bg.png",
            "notifications": null,
            "geo_enabled": false,
            "description": null,
            "profile_background_color": "C0DEED",
            "verified": false,
            "default_profile_image": true,
            "friends_count": 11,
            "statuses_count": 6,
            "profile_background_image_url": "http://a0.twimg.com/images/themes/theme1/bg.png",
            "following": null,
            "screen_name": "Barbis_doll",
            "show_all_inline_media": false
          },
          "following": false
        },
      ],
      "previous_cursor_str": "0",
      "next_cursor": 1373407125131783107,
      "next_cursor_str": "1373407125131783107"
    }
:::

</div>
