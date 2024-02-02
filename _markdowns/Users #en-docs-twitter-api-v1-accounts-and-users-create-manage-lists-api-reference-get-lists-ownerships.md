<div>

::: c01-rich-text-editor
Returns the lists owned by the specified Twitter user. Private lists
will only be shown if the authenticated user is also the owner of the
lists.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/lists/ownerships.json `

  -------------------------------------- ------
  Response formats                       JSON
  Requires authentication?               Yes
  Rate limited?                          Yes
  Requests / 15-min window (user auth)   15
  Requests / 15-min window (app auth)    15
  -------------------------------------- ------

## Parameters [¶](#parameters){.headerlink}

  ------------- ---------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------- ---------
  Name          Required   Description                                                                                                                                                                                                                                                                                                                                             Default Value   Example
  user_id       optional   The ID of the user for whom to return results. Helpful for disambiguating when a valid user ID is also a valid screen name.                                                                                                                                                                                                                                             
  screen_name   optional   The screen name of the user for whom to return results. Helpful for disambiguating when a valid screen name is also a user ID.                                                                                                                                                                                                                                          
  count         optional   The amount of results to return per page. Defaults to 20. No more than 1000 results will ever be returned in a single page.                                                                                                                                                                                                                                             
  cursor        optional   Breaks the results into pages. Provide a value of *-1* to begin paging. Provide values as returned in the response body\'s *next_cursor* and *previous_cursor* attributes to page back and forth in the list. It is recommended to always use cursors when the method supports them. See [Cursoring](/en/docs/basics/cursoring) for more information.                   
  ------------- ---------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------- ---------

## Example Request [¶](#example-request){.headerlink}

` GET https://api.twitter.com/1.1/lists/ownerships.json?screen_name=twitter&count=2 `

## Example Response [¶](#example-response){.headerlink}

    {
      "next_cursor":46541288,
      "next_cursor_str":"46541288",
      "previous_cursor":0,
      "previous_cursor_str":"0",
      "lists":[
        {
          "id":84839422,
          "id_str":"84839422",
          "name":"Official Twitter accts",
          "uri":"/twitter/official-twitter-accts",
          "subscriber_count":20,
          "member_count":0,
          "mode":"public",
          "description":"Accounts managed by Twitter, Inc. ",
          "slug":"official-twitter-accts",
          "full_name":"@twitter/official-twitter-accts",
          "created_at":"Tue Feb 05 18:14:21 +0000 2013",
          "following":false,
          "user":{
            "id":783214,
            "id_str":"783214",
            "name":"Twitter",
            "screen_name":"twitter",
            "location":"San Francisco, CA",
            "description":"Your official source for news, updates and tips from Twitter, Inc.",
            "url":"http://blog.twitter.com/",
            "entities":{
              "url":{
                "urls":[
                  {
                    "url":"http://blog.twitter.com/",
                    "expanded_url":null,
                    "indices":[
                      0,
                      24
                    ]
                  }
                ]
              },
              "description":{
                "urls":[

                ]
              }
            },
            "protected":false,
            "followers_count":17214319,
            "friends_count":120,
            "listed_count":76232,
            "created_at":"Tue Feb 20 14:35:54 +0000 2007",
            "favourites_count":22,
            "utc_offset":-28800,
            "time_zone":"Pacific Time (US & Canada)",
            "geo_enabled":true,
            "verified":true,
            "statuses_count":1563,
            "lang":"en",
            "contributors_enabled":false,
            "is_translator":false,
            "profile_background_color":"ACDED6",
            "profile_background_image_url":"...",
            "profile_background_image_url_https":"...",
            "profile_background_tile":true,
            "profile_image_url":"...",
            "profile_image_url_https":"...",
            "profile_banner_url":"https://si0.twimg.com/profile_banners/783214/1347405327",
            "profile_link_color":"038543",
            "profile_sidebar_border_color":"EEEEEE",
            "profile_sidebar_fill_color":"F6F6F6",
            "profile_text_color":"333333",
            "profile_use_background_image":true,
            "default_profile":false,
            "default_profile_image":false,
            "following":true,
            "follow_request_sent":false,
            "notifications":false
          }
        },
        {
          "id":46541288,
          "id_str":"46541288",
          "name":"D9",
          "uri":"/twitter/d9",
          "subscriber_count":340,
          "member_count":327,
          "mode":"public",
          "description":"D9 attendees with a Twitter account",
          "slug":"d9",
          "full_name":"@twitter/d9",
          "created_at":"Tue May 31 16:29:35 +0000 2011",
          "following":false,
          "user":{
            "id":783214,
            "id_str":"783214",
            "name":"Twitter",
            "screen_name":"twitter",
            "location":"San Francisco, CA",
            "description":"Your official source for news, updates and tips from Twitter, Inc.",
            "url":"http://blog.twitter.com/",
            "entities":{
              "url":{
                "urls":[
                  {
                    "url":"http://blog.twitter.com/",
                    "expanded_url":null,
                    "indices":[
                      0,
                      24
                    ]
                  }
                ]
              },
              "description":{
                "urls":[

                ]
              }
            },
            "protected":false,
            "followers_count":17214319,
            "friends_count":120,
            "listed_count":76232,
            "created_at":"Tue Feb 20 14:35:54 +0000 2007",
            "favourites_count":22,
            "utc_offset":-28800,
            "time_zone":"Pacific Time (US & Canada)",
            "geo_enabled":true,
            "verified":true,
            "statuses_count":1563,
            "lang":"en",
            "contributors_enabled":false,
            "is_translator":false,
            "profile_background_color":"ACDED6",
            "profile_background_image_url":"...",
            "profile_background_image_url_https":"...",
            "profile_background_tile":true,
            "profile_image_url":"...",
            "profile_image_url_https":"...",
            "profile_banner_url":"https://si0.twimg.com/profile_banners/783214/1347405327",
            "profile_link_color":"038543",
            "profile_sidebar_border_color":"EEEEEE",
            "profile_sidebar_fill_color":"F6F6F6",
            "profile_text_color":"333333",
            "profile_use_background_image":true,
            "default_profile":false,
            "default_profile_image":false,
            "following":true,
            "follow_request_sent":false,
            "notifications":false
          }
        }
      ]
    }
:::

</div>
