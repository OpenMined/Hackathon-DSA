<div>

::: c01-rich-text-editor
Returns an array of [user
objects](/en/docs/tweets/data-dictionary/overview/user-object) the
authenticating user has muted.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/mutes/users/list.json `

  -------------------------------------- -------------------------
  Response formats                       JSON
  Requires authentication?               Yes (user context only)
  Rate limited?                          Yes
  Requests / 15-min window (user auth)   15
  -------------------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

+-------------+-------------+-------------+-------------+-------------+
| cursor      | optional    | Causes the  | ` -1 `      | ` 2 `       |
|             |             | list of IDs |             |             |
|             |             | to be       |             |             |
|             |             | broken into |             |             |
|             |             | pages of no |             |             |
|             |             | more than   |             |             |
|             |             | 5000 IDs at |             |             |
|             |             | a time. The |             |             |
|             |             | number of   |             |             |
|             |             | IDs         |             |             |
|             |             | returned is |             |             |
|             |             | not         |             |             |
|             |             | guaranteed  |             |             |
|             |             | to be 5000  |             |             |
|             |             | as          |             |             |
|             |             | suspended   |             |             |
|             |             | users are   |             |             |
|             |             | filtered    |             |             |
|             |             | out. If no  |             |             |
|             |             | cursor is   |             |             |
|             |             | provided, a |             |             |
|             |             | value of -1 |             |             |
|             |             | will be     |             |             |
|             |             | assumed,    |             |             |
|             |             | which is    |             |             |
|             |             | the first   |             |             |
|             |             | \"page.\"   |             |             |
|             |             |             |             |             |
|             |             | The         |             |             |
|             |             | response    |             |             |
|             |             | from the    |             |             |
|             |             | API will    |             |             |
|             |             | include a   |             |             |
|             |             | ` previo    |             |             |
|             |             | us_cursor ` |             |             |
|             |             | and         |             |             |
|             |             | ` ne        |             |             |
|             |             | xt_cursor ` |             |             |
|             |             | to allow    |             |             |
|             |             | paging back |             |             |
|             |             | and forth.  |             |             |
|             |             | See [Using  |             |             |
|             |             | cursors to  |             |             |
|             |             | navigate    |             |             |
|             |             | collec      |             |             |
|             |             | tions](/en/ |             |             |
|             |             | docs/basics |             |             |
|             |             | /cursoring) |             |             |
|             |             | for more    |             |             |
|             |             | i           |             |             |
|             |             | nformation. |             |             |
+-------------+-------------+-------------+-------------+-------------+
| inclu       | optional    | The         | ` true `    | ` false `   |
| de_entities |             | `           |             |             |
|             |             |  entities ` |             |             |
|             |             | node will   |             |             |
|             |             | not be      |             |             |
|             |             | included    |             |             |
|             |             | when set to |             |             |
|             |             | ` false ` . |             |             |
+-------------+-------------+-------------+-------------+-------------+
| skip_status | optional    | When set to | ` false `   | ` true `    |
|             |             | either      |             |             |
|             |             | ` true ` ,  |             |             |
|             |             | ` t ` or    |             |             |
|             |             | ` 1 `       |             |             |
|             |             | statuses    |             |             |
|             |             | will not be |             |             |
|             |             | included in |             |             |
|             |             | the         |             |             |
|             |             | returned    |             |             |
|             |             | user        |             |             |
|             |             | objects.    |             |             |
+-------------+-------------+-------------+-------------+-------------+

## Example Request [¶](#example-request){.headerlink}

` GET https://api.twitter.com/1.1/mutes/users/list.json?include_entities=false&skip_status=true `

## Example Response [¶](#example-response){.headerlink}

    {
      "users": [
        {
          "id": 22479443,
          "id_str": "22479443",
          "name": "White Leaf",
          "screen_name": "whiteleaf",
          "location": "hampshire, england",
          "description": "a house, some weather",
          "url": "http://t.co/oMxPc28AJg",
          "entities": {
            "url": {
              "urls": [
                {
                  "url": "http://t.co/oMxPc28AJg",
                  "expanded_url": "http://andypiper.co.uk/",
                  "display_url": "andypiper.co.uk",
                  "indices": [
                    0,
                    22
                  ]
                }
              ]
            },
            "description": {
              "urls": [

              ]
            }
          },
          "protected": false,
          "followers_count": 24,
          "friends_count": 4,
          "listed_count": 4,
          "created_at": "Mon Mar 02 12:30:40 +0000 2009",
          "favourites_count": 0,
          "utc_offset": -36000,
          "time_zone": "Hawaii",
          "geo_enabled": false,
          "verified": false,
          "statuses_count": 1785,
          "lang": "en",
          "contributors_enabled": false,
          "is_translator": false,
          "is_translation_enabled": false,
          "profile_background_color": "0099B9",
          "profile_background_image_url": "http://abs.twimg.com/images/themes/theme4/bg.gif",
          "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme4/bg.gif",
          "profile_background_tile": false,
          "profile_image_url": "http://pbs.twimg.com/profile_images/85874252/whiteleaf_normal.png",
          "profile_image_url_https": "https://pbs.twimg.com/profile_images/85874252/whiteleaf_normal.png",
          "profile_link_color": "D02201",
          "profile_sidebar_border_color": "A6E2DC",
          "profile_sidebar_fill_color": "D9FBFC",
          "profile_text_color": "182277",
          "profile_use_background_image": true,
          "default_profile": false,
          "default_profile_image": false,
          "following": false,
          "follow_request_sent": false,
          "notifications": false,
          "muting": true
        },
        {
          "id": 1228026486,
          "id_str": "1228026486",
          "name": "Andy Piper",
          "screen_name": "OmnipresentAndy",
          "location": "everywhere",
          "description": "ceiling cat, keeping watch on the interwebz",
          "url": null,
          "entities": {
            "description": {
              "urls": [

              ]
            }
          },
          "protected": false,
          "followers_count": 5,
          "friends_count": 13,
          "listed_count": 0,
          "created_at": "Thu Feb 28 17:44:13 +0000 2013",
          "favourites_count": 0,
          "utc_offset": 3600,
          "time_zone": "Casablanca",
          "geo_enabled": false,
          "verified": false,
          "statuses_count": 27,
          "lang": "en",
          "contributors_enabled": false,
          "is_translator": false,
          "is_translation_enabled": false,
          "profile_background_color": "C0DEED",
          "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
          "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
          "profile_background_tile": false,
          "profile_image_url": "http://pbs.twimg.com/profile_images/3320335368/e5316acccf4f5d3b7239193250d7a9bb_normal.png",
          "profile_image_url_https": "https://pbs.twimg.com/profile_images/3320335368/e5316acccf4f5d3b7239193250d7a9bb_normal.png",
          "profile_link_color": "0084B4",
          "profile_sidebar_border_color": "C0DEED",
          "profile_sidebar_fill_color": "DDEEF6",
          "profile_text_color": "333333",
          "profile_use_background_image": true,
          "default_profile": true,
          "default_profile_image": false,
          "following": false,
          "follow_request_sent": false,
          "notifications": false,
          "muting": true
        },
        {
          "id": 54931584,
          "id_str": "54931584",
          "name": "Evil Piper",
          "screen_name": "evilpiper",
          "location": "",
          "description": "mwah-ha-haaaaa",
          "url": null,
          "entities": {
            "description": {
              "urls": [

              ]
            }
          },
          "protected": false,
          "followers_count": 16,
          "friends_count": 10,
          "listed_count": 0,
          "created_at": "Wed Jul 08 15:40:42 +0000 2009",
          "favourites_count": 1,
          "utc_offset": 3600,
          "time_zone": "London",
          "geo_enabled": false,
          "verified": false,
          "statuses_count": 73,
          "lang": "en",
          "contributors_enabled": false,
          "is_translator": false,
          "is_translation_enabled": false,
          "profile_background_color": "1A1B1F",
          "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
          "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
          "profile_background_tile": false,
          "profile_image_url": "http://pbs.twimg.com/profile_images/307611594/evil_normal.png",
          "profile_image_url_https": "https://pbs.twimg.com/profile_images/307611594/evil_normal.png",
          "profile_link_color": "A6001E",
          "profile_sidebar_border_color": "181A1E",
          "profile_sidebar_fill_color": "949399",
          "profile_text_color": "120312",
          "profile_use_background_image": false,
          "default_profile": false,
          "default_profile_image": false,
          "following": true,
          "follow_request_sent": false,
          "notifications": false,
          "muting": true
        }
      ],
      "next_cursor": 0,
      "next_cursor_str": "0",
      "previous_cursor": 0,
      "previous_cursor_str": "0"
    }
:::

</div>
