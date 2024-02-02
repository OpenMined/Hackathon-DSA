<div>

::: c01-rich-text-editor
Returns the members of the specified list. Private list members will
only be shown if the authenticated user owns the specified list.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/lists/members.json `

  -------------------------------------- ------
  Response formats                       JSON
  Requires authentication?               Yes
  Rate limited?                          Yes
  Requests / 15-min window (user auth)   900
  Requests / 15-min window (app auth)    75
  -------------------------------------- ------

## Parameters [¶](#parameters){.headerlink}

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------- -----------
  list_id                                                                                                                                                                            required        The numerical ` id ` of the list.                                                                                                                                                                                                     
  slug                                                                                                                                                                               required        You can identify a list by its slug instead of its numerical id. If you decide to do so, note that you\'ll also have to specify the list owner using the ` owner_id ` or ` owner_screen_name ` parameters.                            
  owner_screen_name                                                                                                                                                                  optional        The screen name of the user who owns the list being requested by a ` slug ` .                                                                                                                                                         
  owner_id                                                                                                                                                                           optional        The user ID of the user who owns the list being requested by a ` slug ` .                                                                                                                                                             
  count                                                                                                                                                                              optional        Specifies the number of results to return per page (see ` cursor ` below). The default is 20, with a maximum of 5,000.                                                                                                                
  cursor                                                                                                                                                                             semi-optional   Causes the collection of list members to be broken into \"pages\" of consistent sizes (specified by the ` count ` parameter). If no cursor is provided, a value of ` -1 ` will be assumed, which is the first \"page.\"               
  The response from the API will include a ` previous_cursor ` and ` next_cursor ` to allow paging back and forth. See Using cursors to navigate collections for more information.   ` -1 `          ` 12893764510938 `                                                                                                                                                                                                                    
  include_entities                                                                                                                                                                   optional        The ` entities ` node will not be included when set to ` false ` .                                                                                                                                                        ` true `    ` false `
  skip_status                                                                                                                                                                        optional        When set to either ` true ` , ` t ` or ` 1 ` statuses will not be included in the returned user objects.                                                                                                                  ` false `   
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------- -----------

## Example Request [¶](#example-request){.headerlink}

` GET https://api.twitter.com/1.1/lists/members.json?slug=team&owner_screen_name=twitterapi&cursor=-1 `

## Example Response [¶](#example-response){.headerlink}

    {
      "previous_cursor": 0,
      "previous_cursor_str": "0",
      "next_cursor": 0,
      "users": [
        {
          "profile_sidebar_fill_color": "bedcfa",
          "expanded_url": null,
          "profile_sidebar_border_color": "85add6",
          "name": "Sharon Ly",
          "profile_background_tile": false,
          "location": "",
          "profile_image_url": "http://a2.twimg.com/profile_images/1359867172/image_normal.jpg",
          "created_at": "Sun May 25 00:29:44 +0000 2008",
          "follow_request_sent": null,
          "is_translator": false,
          "profile_link_color": "955ea6",
          "id_str": "14895163",
          "entities": {
            "urls": [

            ],
            "hashtags": [

            ],
            "user_mentions": [

            ]
          },
          "default_profile": false,
          "favourites_count": 63,
          "contributors_enabled": false,
          "url": null,
          "id": 14895163,
          "utc_offset": -28800,
          "profile_image_url_https": "https://si0.twimg.com/profile_images/1359867172/image_normal.jpg",
          "profile_use_background_image": true,
          "listed_count": 43,
          "lang": "en",
          "profile_text_color": "4c58a3",
          "followers_count": 784,
          "protected": false,
          "profile_background_color": "312040",
          "geo_enabled": true,
          "description": "",
          "time_zone": "Pacific Time (US & Canada)",
          "verified": false,
          "profile_background_image_url_https": "https://si0.twimg.com/profile_background_images/257176598/hydrangeas_94_68830.jpg",
          "notifications": null,
          "friends_count": 188,
          "statuses_count": 325,
          "profile_background_image_url": "http://a1.twimg.com/profile_background_images/257176598/hydrangeas_94_68830.jpg",
          "default_profile_image": false,
          "status": {
            "coordinates": null,
            "truncated": false,
            "created_at": "Tue Jul 05 03:46:03 +0000 2011",
            "favorited": false,
            "id_str": "88091240503058432",
            "in_reply_to_user_id_str": "748353",
            "contributors": null,
            "text": "@kmonkeyjam Oh no... I don't know where that bone is but that sounds terribly painful. How are you still tweeting? Get better!",
            "id": 88091240503058432,
            "retweet_count": 0,
            "in_reply_to_status_id_str": "87979906226597888",
            "geo": null,
            "retweeted": false,
            "in_reply_to_user_id": 748353,
            "source": "Twitter for iPhone",
            "in_reply_to_screen_name": "kmonkeyjam",
            "place": null,
            "in_reply_to_status_id": 87979906226597888
          },
          "display_url": null,
          "screen_name": "onesnowclimber",
          "show_all_inline_media": true,
          "following": null
        }
      ],
      "next_cursor_str": "0"
    }
:::

</div>
