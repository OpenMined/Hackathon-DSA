<div>

::: c01-rich-text-editor
Creates a new list for the authenticated user. Note that you can create
up to 1000 lists per account.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/lists/create.json `

  -------------------------- ------
  Response formats           JSON
  Requires authentication?   Yes
  Rate limited?              Yes
  -------------------------- ------

## Parameters [¶](#parameters){.headerlink}

  ------------- ---------- --------------------------------------------------------------------------------------------------------------------------------------------------- --------------- ---------
  Name          Required   Description                                                                                                                                         Default Value   Example
  name          required   The name for the list. A list\'s name must start with a letter and can consist only of 25 or fewer letters, numbers, \"-\", or \"\_\" characters.                   
  mode          optional   Whether your list is public or private. Values can be *public* or *private* . If no mode is specified the list will be public.                                      
  description   optional   The description to give the list.                                                                                                                                   
  ------------- ---------- --------------------------------------------------------------------------------------------------------------------------------------------------- --------------- ---------

## Example Request [¶](#example-request){.headerlink}

` POST https://api.twitter.com/1.1/lists/create.json?name=Goonies&mode=public&description=For%20life `

## Example Response [¶](#example-response){.headerlink}

    {
       "created_at":"Fri Nov 04 21:22:36 +0000 2011",
       "slug":"goonies",
       "name":"Goonies",
       "full_name":"@kurrik/goonies",
       "description":"For life",
       "mode":"public",
       "following":false,
       "user":{
          "geo_enabled":true,
          "profile_background_image_url_https":"https://si0.twimg.com/profile_background_images/342542280/background7.png",
          "profile_background_color":"8fc1ff",
          "protected":false,
          "default_profile":false,
          "listed_count":127,
          "profile_background_tile":true,
          "created_at":"Thu Jul 19 15:58:07 +0000 2007",
          "friends_count":291,
          "name":"Arne Roomann-Kurrik",
          "profile_sidebar_fill_color":"c7e0ff",
          "notifications":false,
          "utc_offset":-28800,
          "profile_image_url_https":"https://si0.twimg.com/profile_images/24229162/arne001_normal.jpg",
          "description":"Developer Advocate at Twitter, practitioner of dark sandwich arts. ",
          "display_url":"roomanna.com",
          "following":false,
          "verified":false,
          "favourites_count":190,
          "profile_sidebar_border_color":"6baeff",
          "followers_count":1705,
          "profile_image_url":"http://a2.twimg.com/profile_images/24229162/arne001_normal.jpg",
          "default_profile_image":false,
          "contributors_enabled":false,
          "deactivated_bit":false,
          "statuses_count":1935,
          "profile_use_background_image":true,
          "location":"Scan Francesco",
          "id_str":"7588892",
          "show_all_inline_media":false,
          "profile_text_color":"000000",
          "screen_name":"kurrik",
          "follow_request_sent":false,
          "profile_background_image_url":"http://a2.twimg.com/profile_background_images/342542280/background7.png",
          "url":"http://t.co/SSiVavc4",
          "expanded_url":"http://roomanna.com",
          "is_translator":false,
          "time_zone":"Pacific Time (US & Canada)",
          "profile_link_color":"0084B4",
          "id":7588892,
          "entities":{
             "urls":[

             ],
             "user_mentions":[

             ],
             "hashtags":[

             ]
          },
          "suspended":false,
          "lang":"en"
       },
       "member_count":0,
       "id_str":"58300198",
       "subscriber_count":0,
       "id":58300198,
       "uri":"/kurrik/goonies"
    }
:::

</div>
