Overview

With proper authorization your application can read and update a user's account and profile settings. Not all settings are exposed via the API. See the API reference for details.

GET account/settings

get-account-settings

GET account/settings
====================

Returns settings (including current trend, geo and sleep time information) for the authenticating user.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/account/settings.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 15  |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

None

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`GET https://api.twitter.com/1.1/account/settings.json`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
        "always_use_https": true,
        "discoverable_by_email": true,
        "geo_enabled": true,
        "language": "en",
        "protected": false,
        "screen_name": "theSeanCook",
        "show_all_inline_media": false,
        "sleep_time": {
            "enabled": false,
            "end_time": null,
            "start_time": null
        },
        "time_zone": {
            "name": "Pacific Time (US & Canada)",
            "tzinfo_name": "America/Los_Angeles",
            "utc_offset": -28800
        },
        "trend_location": [
            {
                "country": "United States",
                "countryCode": "US",
                "name": "Atlanta",
                "parentid": 23424977,
                "placeType": {
                    "code": 7,
                    "name": "Town"
                },
                "url": "http://where.yahooapis.com/v1/place/2357024",
                "woeid": 2357024
            }
        ],
        "use_cookie_personalization": true,
        "allow_contributor_request": "all"
    }

GET account/verify\_credentials

get-account-verify\_credentials

GET account/verify\_credentials
===============================

Returns an HTTP 200 OK response code and a representation of the requesting user if authentication was successful; returns a 401 status code and an error message if not. Use this method to test if supplied user credentials are valid.

Request a User's Email Address[¶](#request-a-user-s-email-address "Permalink to this headline")
-----------------------------------------------------------------------------------------------

The "Request email addresses from users" checkbox is available under the app permissions on [developer.twitter.com](https://developer.twitter.com/en/docs/basics/developer-portal/guides/apps). Privacy Policy URL and Terms of Service URL fields must be completed in the app settings in order for email address access to function. If enabled, users will be informed via the [oauth/authorize](https://developer.twitter.com/oauth/reference/get/oauth/authorize) dialog that your app can access their email address.

**Please note** - Your app will need to regenerate the user access tokens for previously authenticated users to access their email address.

**Please note** - You can view and edit your existing [Twitter apps](https://developer.twitter.com/en/docs/basics/developer-portal/guides/apps) via the [Twitter app dashboard](https://developer.twitter.com/en/apps) if you are logged into your Twitter account on developer.twitter.com.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

[https://api.twitter.com/1.1/account/verify\_credentials.json](https://api.twitter.com/1.1/account/verify_credentials.json)

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 75  |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |
| --- | --- | --- | --- |
| Name | Required | Description | Example |
| include\_entities | optional | The _entities_ node will not be included when set to _false_ . | _false_ |
| skip\_status | optional | When set to either _true_ , _t_ or _1_ statuses will not be included in the returned user object. | _true_ |
| include\_email | optional | When set to _true_ email will be returned in the user objects as a string. If the user does not have an email address on their account, or if the email address is not verified, null will be returned. | _true_ |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

GET [https://api.twitter.com/1.1/account/verify\_credentials.json](https://api.twitter.com/1.1/account/verify_credentials.json)

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
        "contributors_enabled": true,
        "created_at": "Sat May 09 17:58:22 +0000 2009",
        "default_profile": false,
        "default_profile_image": false,
        "description": "I taught your phone that thing you like.  The Mobile Partner Engineer @Twitter. ",
        "favourites_count": 588,
        "follow_request_sent": null,
        "followers_count": 10625,
        "following": null,
        "friends_count": 1181,
        "geo_enabled": true,
        "id": 38895958,
        "id_str": "38895958",
        "is_translator": false,
        "lang": "en",
        "listed_count": 190,
        "location": "San Francisco",
        "name": "Sean Cook",
        "notifications": null,
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
        "status": {
            "contributors": null,
            "coordinates": {
                "coordinates": [
                    -122.45037293,
                    37.76484123
                ],
                "type": "Point"
            },
            "created_at": "Tue Aug 28 05:44:24 +0000 2012",
            "favorited": false,
            "geo": {
                "coordinates": [
                    37.76484123,
                    -122.45037293
                ],
                "type": "Point"
            },
            "id": 240323931419062272,
            "id_str": "240323931419062272",
            "in_reply_to_screen_name": "messl",
            "in_reply_to_status_id": 240316959173009410,
            "in_reply_to_status_id_str": "240316959173009410",
            "in_reply_to_user_id": 18707866,
            "in_reply_to_user_id_str": "18707866",
            "place": {
                "attributes": {},
                "bounding_box": {
                    "coordinates": [
                        [
                            [
                                -122.45778216,
                                37.75932999
                            ],
                            [
                                -122.44248216,
                                37.75932999
                            ],
                            [
                                -122.44248216,
                                37.76752899
                            ],
                            [
                                -122.45778216,
                                37.76752899
                            ]
                        ]
                    ],
                    "type": "Polygon"
                },
                "country": "United States",
                "country_code": "US",
                "full_name": "Ashbury Heights, San Francisco",
                "id": "866269c983527d5a",
                "name": "Ashbury Heights",
                "place_type": "neighborhood",
                "url": "http://api.twitter.com/1/geo/id/866269c983527d5a.json"
            },
            "retweet_count": 0,
            "retweeted": false,
            "source": "Twitter for  iPhone",
            "text": "@messl congrats! So happy for all 3 of you.",
            "truncated": false
        },
        "statuses_count": 2609,
        "time_zone": "Pacific Time (US & Canada)",
        "url": null,
        "utc_offset": -28800,
        "verified": false
    }

GET users/profile\_banner

get-users-profile\_banner

GET users/profile\_banner
=========================

Returns a map of the available size variations of the specified user's profile banner. If the user has not uploaded a profile banner, a HTTP 404 will be served instead. This method can be used instead of string manipulation on the `profile_banner_url` returned in user objects as described in [Profile Images and Banners](https://developer.twitter.com/en/docs/accounts-and-users/user-profile-images-and-banners).

The profile banner data available at each size variant's URL is in PNG format.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/users/profile_banner.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 180 |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| user\_id | optional | The ID of the user for whom to return results. Helpful for disambiguating when a valid user ID is also a valid screen name. |     | _12345_ |
| screen\_name | optional | The screen name of the user for whom to return results. Helpful for disambiguating when a valid screen name is also a user ID. |     | _noradio_ |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`GET https://api.twitter.com/1.1/users/profile_banner.json?screen_name=twitterapi`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
      "sizes": {
        "ipad": {
          "h": 313,
          "w": 626,
          "url": "https://pbs.twimg.com/profile_banners/6253282/1347394302/ipad"
        },
        "ipad_retina": {
          "h": 626,
          "w": 1252,
          "url": "https://pbs.twimg.com/profile_banners/6253282/1347394302/ipad_retina"
        },
        "web": {
          "h": 260,
          "w": 520,
          "url": "https://pbs.twimg.com/profile_banners/6253282/1347394302/web"
        },
        "web_retina": {
          "h": 520,
          "w": 1040,
          "url": "https://pbs.twimg.com/profile_banners/6253282/1347394302/web_retina"
        },
        "mobile": {
          "h": 160,
          "w": 320,
          "url": "https://pbs.twimg.com/profile_banners/6253282/1347394302/mobile"
        },
        "mobile_retina": {
          "h": 320,
          "w": 640,
          "url": "https://pbs.twimg.com/profile_banners/6253282/1347394302/mobile_retina"
        },
        "300x100": {
          "h": 100,
          "w": 300,
          "url": "https://pbs.twimg.com/profile_banners/6253282/1347394302/300x100"
        },
        "600x200": {
          "h": 200,
          "w": 600,
          "url": "https://pbs.twimg.com/profile_banners/6253282/1347394302/600x200"
        },
        "1500x500": {
          "h": 500,
          "w": 1500,
          "url": "https://pbs.twimg.com/profile_banners/6253282/1347394302/1500x500"
        }
      }
    }

POST account/remove\_profile\_banner

post-account-remove\_profile\_banner

POST account/remove\_profile\_banner
====================================

Removes the uploaded profile banner for the authenticating user. Returns HTTP 200 upon success.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/account/remove_profile_banner.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

None

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`POST https://api.twitter.com/1.1/account/remove_profile_banner.json`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

POST account/settings

post-account-settings

POST account/settings
=====================

Updates the authenticating user's settings.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/account/settings.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |
| --- | --- | --- | --- |
| Name | Required | Description | Example |
| sleep\_time\_enabled | optional | When set to _true_ , _t_ or _1_ , will enable sleep time for the user. Sleep time is the time when push or SMS notifications should not be sent to the user. | _true_ |
| start\_sleep\_time | optional | The hour that sleep time should begin if it is enabled. The value for this parameter should be provided in [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) format (i.e. 00-23). The time is considered to be in the same timezone as the user's _time\_zone_ setting. | _13_ |
| end\_sleep\_time | optional | The hour that sleep time should end if it is enabled. The value for this parameter should be provided in [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) format (i.e. 00-23). The time is considered to be in the same timezone as the user's _time\_zone_ setting. | _13_ |
| time\_zone | optional | The timezone dates and times should be displayed in for the user. The timezone must be one of the [Rails TimeZone](http://api.rubyonrails.org/classes/ActiveSupport/TimeZone.html) names. | _Europe/Copenhagen_ _Pacific/Tongatapu_ |
| trend\_location\_woeid | optional | The Yahoo! Where On Earth ID to use as the user's default trend location. Global information is available by using 1 as the WOEID. The WOEID must be one of the locations returned by [GET trends/available](https://developer.twitter.com/en/docs/trends/locations-with-trending-topics/api-reference/get-trends-available) . | _1_ |
| lang | optional | The language which Twitter should render in for this user. The language must be specified by the appropriate two letter ISO 639-1 representation. Currently supported languages are provided by [this endpoint](https://developer.twitter.com/en/docs/developer-utilities/supported-languages/api-reference/get-help-languages) . | _it_ _en_ _es_ |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`POST https://api.twitter.com/1.1/account/settings.json?lang=en`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
      "sleep_time": {
        "end_time": null,
        "enabled": false,
        "start_time": null
      },
      "use_cookie_personalization": true,
      "trend_location": [
        {
          "name": "San Francisco",
          "placeType": {
            "name": "Town",
            "code": 7
          },
          "woeid": 2487956,
          "country": "United States",
          "url": "http://where.yahooapis.com/v1/place/2487956",
          "countryCode": "US",
          "parentid": 23424977
        }
      ],
      "language": "en",
      "discoverable_by_email": true,
      "always_use_https": true,
      "protected": false,
      "geo_enabled": true,
      "show_all_inline_media": false,
      "screen_name": "oauth_dancer"
    }

POST account/update\_profile

post-account-update\_profile

POST account/update\_profile
============================

Sets some values that users are able to set under the "Account" tab of their settings page. Only the parameters specified will be updated.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/account/update_profile.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| name | optional | Full name associated with the profile. |     | _Marcel Molina_ |
| url | optional | URL associated with the profile. Will be prepended with `http://` if not present. |     | `http://project.ioni.st` |
| location | optional | The city or country describing where the user of the account is located. The contents are not normalized or geocoded in any way. |     | _San Francisco CA_ |
| description | optional | A description of the user owning the account. |     | _Flipped my wig at age 22 and it never grew back. Also: I work at Twitter._ |
| include\_entities | optional | The _entities_ node will not be included when set to _false_ . |     | _false_ |
| skip\_status | optional | When set to either _true_ , _t_ or _1_ statuses will not be included in the returned user object. |     |     |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`POST https://api.twitter.com/1.1/account/update_profile.json?name=Sean%20Cook&description=Keep%20calm%20and%20rock%20on.`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

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

POST account/update\_profile\_banner

post-account-update\_profile\_banner

POST account/update\_profile\_banner
====================================

Uploads a profile banner on behalf of the authenticating user. More information about sizing variations can be found in [User Profile Images and Banners](https://developer.twitter.com/en/docs/accounts-and-users/user-profile-images-and-banners) and [GET users / profile\_banner](https://developer.twitter.com/en/docs/accounts-and-users/manage-account-settings/api-reference/get-users-profile_banner).

Profile banner images are processed asynchronously. The profile\_banner\_url and its variant sizes will not necessary be available directly after upload.

HTTP Response Codes[¶](#http-response-codes "Permalink to this headline")
-------------------------------------------------------------------------

|     |     |
| --- | --- |
| Code(s) | Meaning |
| 200, 201, 202 | Profile banner image successfully uploaded |
| 400 | Either an image was not provided, or the image data could not be processed |
| 422 | The image could not be resized, or is too large. |

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/account/update_profile_banner.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| banner | required | The Base64-encoded or raw image data being uploaded as the user's new profile banner. |     |     |
| width | optional | The width of the preferred section of the image being uploaded in pixels. Use with _height_ , _offset\_left_ , and _offset\_top_ to select the desired region of the image to use. |     |     |
| height | optional | The height of the preferred section of the image being uploaded in pixels. Use with _width_ , _offset\_left_ , and _offset\_top_ to select the desired region of the image to use. |     |     |
| offset\_left | optional | The number of pixels by which to offset the uploaded image from the left. Use with _height_ , _width_ , and _offset\_top_ to select the desired region of the image to use. |     |     |
| offset\_top | optional | The number of pixels by which to offset the uploaded image from the top. Use with _height_ , _width_ , and _offset\_left_ to select the desired region of the image to use. |     |     |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`POST https://api.twitter.com/1.1/account/update_profile_banner.json?width=1500&height=500&offset_top=0&offset_left=0&banner=FILE_DATA`

POST account/update\_profile\_image

post-account-update\_profile\_image

POST account/update\_profile\_image
===================================

Updates the authenticating user's profile image. Note that this method expects raw multipart data, not a URL to an image.

This method asynchronously processes the uploaded file before updating the user's profile image URL. You can either update your local cache the next time you request the user's information, or, at least 5 seconds after uploading the image, ask for the updated URL using [GET users / show](https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-show).

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/account/update_profile_image.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| image | required | The avatar image for the profile, base64-encoded. Must be a valid GIF, JPG, or PNG image of less than 700 kilobytes in size. Images with width larger than 400 pixels will be scaled down. Animated GIFs will be converted to a static GIF of the first frame, removing the animation. |     |     |
| include\_entities | optional | The _entities_ node will not be included when set to _false_ . |     | _false_ |
| skip\_status | optional | When set to either _true_ , _t_ or _1_ statuses will not be included in the returned user objects. |     |     |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`POST https://api.twitter.com/1.1/account/update_profile_image.json?image=ABCDEFGH...`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

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

GET saved\_searches/list

get-saved\_searches-list

GET saved\_searches/list
========================

Returns the authenticated user's saved search queries.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/saved_searches/list.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 15  |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

None

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`GET https://api.twitter.com/1.1/saved_searches/list.json`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    [
      {
        "created_at": "Tue Jun 15 09:37:24 +0000 2010",
        "id": 9569704,
        "id_str": "9569704",
        "name": "@twitterapi",
        "position": null,
        "query": "@twitterapi"
      },
      {
        "created_at": "Tue Jun 15 09:38:04 +0000 2010",
        "id": 9569730,
        "id_str": "9569730",
        "name": "@twitter OR twitterapi OR "twitter api" OR "@anywhere"",
        "position": null,
        "query": "@twitter OR twitterapi OR "twitter api" OR "@anywhere""
      }
    ]

GET saved\_searches/show/:id

get-saved\_searches-show-id

GET saved\_searches/show/:id
============================

Retrieve the information for the saved search represented by the given id. The authenticating user must be the owner of saved search ID being requested.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/saved_searches/show/:id.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 15  |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| id  | required | The ID of the saved search. |     | _313006_ |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`GET https://api.twitter.com/1.1/saved_searches/show/9569704.json`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
      "created_at": "Fri Nov 04 18:46:41 +0000 2011", 
      "id": 62353170, 
      "id_str": "62353170", 
      "name": "@anywhere", 
      "position": null, 
      "query": "@anywhere"
    }

POST saved\_searches/create

post-saved\_searches-create

POST saved\_searches/create
===========================

Create a new saved search for the authenticated user. A user may only have 25 saved searches.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/saved_searches/create.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| query | required | The query of the search the user would like to save. |     |     |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`POST https://api.twitter.com/1.1/saved_searches/create.json?query=sandwiches`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
      "created_at": "Fri Aug 24 22:08:58 +0000 2012", 
      "id": 158598597, 
      "id_str": "158598597", 
      "name": "sandwiches", 
      "position": null, 
      "query": "sandwiches"
    }

POST saved\_searches/destroy/:id

post-saved\_searches-destroy-id

POST saved\_searches/destroy/:id
================================

Destroys a saved search for the authenticating user. The authenticating user must be the owner of saved search id being destroyed.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/saved_searches/destroy/:id.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| id  | required | The ID of the saved search. |     | _313006_ |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`POST https://api.twitter.com/1.1/saved_searches/destroy/62353170.json`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
      "created_at": "Fri Nov 04 18:46:41 +0000 2011", 
      "id": 62353170, 
      "id_str": "62353170", 
      "name": "@anywhere", 
      "position": null, 
      "query": "@anywhere"
    }

Overview

**Please note**  

We've released the following endpoints within the [Twitter API v2](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api). 

|     |     |     |
| --- | --- | --- |
| **v1.1 endpoints** | **Corresponding v2 endpoints** |     |
| [GET blocks/id](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/mute-block-report-users/api-reference/get-blocks-ids)   <br>[GET blocks/list](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/mute-block-report-users/api-reference/get-blocks-list)  <br>[POST blocks/create](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/mute-block-report-users/api-reference/post-blocks-create)   <br>[POST blocks/destroy](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/mute-block-report-users/api-reference/post-blocks-destroy) | [Blocks](https://developer.twitter.com/en/docs/twitter-api/users/blocks) | [Migration guide](https://developer.twitter.com/en/docs/twitter-api/users/blocks/migrate) |
| [GET mutes/users/id](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/mute-block-report-users/api-reference/get-mutes-users-ids)   <br>[GET mutes/users/list](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/mute-block-report-users/api-reference/get-mutes-users-list)  <br>[POST mutes/users/create](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/mute-block-report-users/api-reference/post-mutes-users-create)   <br>[POST mutes/users/destroy](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/mute-block-report-users/api-reference/post-mutes-users-destroy) | [Mutes](https://developer.twitter.com/en/docs/twitter-api/users/mutes) | [Migration guide](https://developer.twitter.com/en/docs/twitter-api/users/mutes/migrate) |

Please use the migration guides to see what has changed between the standard v1.1 and v2 versions.

Your app can mute, block and report users for the authenicated user.

For general information on reporting viloations on Twitter see [How to report violations](https://support.twitter.com/articles/15789) in the help center.

GET blocks/ids

get-blocks-ids

GET blocks/ids
==============

Returns an array of numeric user ids the authenticating user is blocking.

**Important** This method is cursored, meaning your app must make multiple requests in order to receive all blocks correctly. See [Using cursors to navigate collections](https://developer.twitter.com/en/docs/basics/cursoring) for more details on how cursoring works.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/blocks/ids.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 15  |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

| Name | Required | Description | Default Value | Example |
| --- | --- | --- | --- | --- |
| stringify\_ids | optional | Many programming environments will not consume Twitter IDs due to their size. Provide this option to have IDs returned as strings instead. Read more about [Twitter IDs](https://developer.twitter.com/en/docs/basics/twitter-ids) . |     | `true` |
| cursor | semi-optional | Causes the list of IDs to be broken into pages of no more than 5000 IDs at a time. The number of IDs returned is not guaranteed to be 5000 as suspended users are filtered out after connections are queried. If no cursor is provided, a value of `-1` will be assumed, which is the first "page."<br><br>The response from the API will include a `previous_cursor` and `next_cursor` to allow paging back and forth. See [Using cursors to navigate collections](https://developer.twitter.com/en/docs/basics/cursoring) for more information. | `-1` | `12893764510938` |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`GET https://api.twitter.com/1.1/blocks/ids.json?stringify_ids=true&cursor=-1`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
      "ids": [
        "123"
      ],
      "next_cursor": 0,
      "next_cursor_str": "0",
      "previous_cursor": 0,
      "previous_cursor_str": "0"
    }

GET blocks/list

get-blocks-list

GET blocks/list
===============

Returns a collection of [user objects](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object) that the authenticating user is blocking.

**Important** This method is cursored, meaning your app must make multiple requests in order to receive all blocks correctly. See [Using cursors to navigate collections](https://developer.twitter.com/en/docs/basics/cursoring) for more details on how cursoring works.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/blocks/list.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 15  |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

| Name | Required | Description | Default Value | Example |
| --- | --- | --- | --- | --- |
| include\_entities | optional | The `entities` node will not be included when set to `false` . |     | `false` |
| skip\_status | optional | When set to either `true` , `t` or `1` statuses will not be included in the returned user objects. |     |     |
| cursor | semi-optional | Causes the list of blocked users to be broken into pages of no more than 5000 IDs at a time. The number of IDs returned is not guaranteed to be 5000 as suspended users are filtered out after connections are queried. If no cursor is provided, a value of `-1` will be assumed, which is the first "page."<br><br>The response from the API will include a `previous_cursor` and `next_cursor` to allow paging back and forth. See [Using cursors to navigate collections](https://developer.twitter.com/en/docs/basics/cursoring) for more information. |     | `12893764510938` |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`GET https://api.twitter.com/1.1/blocks/list.json?skip_status=true&cursor=-1`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
      "previous_cursor": 0,
      "previous_cursor_str": "0",
      "next_cursor": 0,
      "users": [
        {
          "profile_sidebar_fill_color": "DDEEF6",
          "profile_background_tile": false,
          "profile_sidebar_border_color": "C0DEED",
          "name": "Javier Heady r",
          "created_at": "Thu Mar 01 00:16:47 +0000 2012",
          "profile_image_url": "http://a0.twimg.com/sticky/default_profile_images/default_profile_4_normal.png",
          "location": "",
          "is_translator": false,
          "follow_request_sent": false,
          "profile_link_color": "0084B4",
          "id_str": "509466276",
          "entities": {
            "description": {
              "urls": [
    
              ]
            }
          },
          "contributors_enabled": false,
          "favourites_count": 0,
          "url": null,
          "default_profile": true,
          "utc_offset": null,
          "profile_image_url_https": "https://si0.twimg.com/sticky/default_profile_images/default_profile_4_normal.png",
          "id": 509466276,
          "listed_count": 0,
          "profile_use_background_image": true,
          "followers_count": 0,
          "protected": false,
          "lang": "en",
          "profile_text_color": "333333",
          "profile_background_color": "C0DEED",
          "notifications": false,
          "verified": false,
          "description": "",
          "geo_enabled": false,
          "time_zone": null,
          "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme1/bg.png",
          "friends_count": 0,
          "default_profile_image": true,
          "statuses_count": 4,
          "profile_background_image_url": "http://a0.twimg.com/images/themes/theme1/bg.png",
          "following": false,
          "screen_name": "javierg3ong"
        }
      ],
      "next_cursor_str": "0"
    }

GET mutes/users/ids

get-mutes-users-ids

GET mutes/users/ids
===================

Returns an array of numeric user ids the authenticating user has muted.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/mutes/users/ids.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 15  |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

| Name | Required | Description | Default Value | Example |
| --- | --- | --- | --- | --- |
| stringify\_ids | optional | Many programming environments will not consume Twitter IDs due to their size. Provide this option to have IDs returned as strings instead. Read more about [Twitter IDs](https://developer.twitter.com/en/docs/basics/twitter-ids) . |     | `true` |
| cursor | optional | Causes the list of IDs to be broken into pages of no more than 5000 IDs at a time. The number of IDs returned is not guaranteed to be 5000 as suspended users are filtered out. If no cursor is provided, a value of -1 will be assumed, which is the first "page."<br><br>The response from the API will include a `previous_cursor` and `next_cursor` to allow paging back and forth. See [Using cursors to navigate collections](https://developer.twitter.com/en/docs/basics/cursoring) for more information. | `-1` | `2` |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`GET https://api.twitter.com/1.1/mutes/users/ids.json?cursor=-1`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
      "ids": [
        1228026486,
        54931584
      ],
      "next_cursor": 0,
      "next_cursor_str": "0",
      "previous_cursor": 0,
      "previous_cursor_str": "0"
    }

GET mutes/users/list

get-mutes-users-list

GET mutes/users/list
====================

Returns an array of [user objects](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object) the authenticating user has muted.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/mutes/users/list.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 15  |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

| Name | Required | Description | Default Value | Example |
| --- | --- | --- | --- | --- |
| cursor | optional | Causes the list of IDs to be broken into pages of no more than 5000 IDs at a time. The number of IDs returned is not guaranteed to be 5000 as suspended users are filtered out. If no cursor is provided, a value of -1 will be assumed, which is the first "page."<br><br>The response from the API will include a `previous_cursor` and `next_cursor` to allow paging back and forth. See [Using cursors to navigate collections](https://developer.twitter.com/en/docs/basics/cursoring) for more information. | `-1` | `2` |
| include\_entities | optional | The `entities` node will not be included when set to `false` . | `true` | `false` |
| skip\_status | optional | When set to either `true` , `t` or `1` statuses will not be included in the returned user objects. | `false` | `true` |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`GET https://api.twitter.com/1.1/mutes/users/list.json?include_entities=false&skip_status=true`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

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

POST blocks/create

post-blocks-create

POST blocks/create
==================

Blocks the specified user from following the authenticating user. In addition the blocked user will not show in the authenticating users mentions or timeline (unless retweeted by another user). If a follow or friend relationship exists it is destroyed.

The URL pattern `/version/block/create/:screen_name_or_user_id.format` is still accepted but not recommended. As a sequence of numbers is a valid screen name we recommend using the `screen_name` or `user_id` parameter instead.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/blocks/create.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| screen\_name | optional | The screen name of the potentially blocked user. Helpful for disambiguating when a valid screen name is also a user ID. |     | _noradio_ |
| user\_id | optional | The ID of the potentially blocked user. Helpful for disambiguating when a valid user ID is also a valid screen name. |     | _12345_ |
| include\_entities | optional | The _entities_ node will not be included when set to _false_ . |     | _false_ |
| skip\_status | optional | When set to either _true_ , _t_ or _1_ statuses will not be included in the returned user objects. |     | _true_ |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`POST https://api.twitter.com/1.1/blocks/create.json?screen_name=theSeanCook&skip_status=1`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

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

POST blocks/destroy

post-blocks-destroy

POST blocks/destroy
===================

Un-blocks the user specified in the ID parameter for the authenticating user. Returns the un-blocked user when successful. If relationships existed before the block was instantiated, they will not be restored.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/blocks/destroy.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| screen\_name | optional | The screen name of the potentially blocked user. Helpful for disambiguating when a valid screen name is also a user ID. |     | _noradio_ |
| user\_id | optional | The ID of the potentially blocked user. Helpful for disambiguating when a valid user ID is also a valid screen name. |     | _12345_ |
| include\_entities | optional | The _entities_ node will not be included when set to _false_ . |     | _false_ |
| skip\_status | optional | When set to either _true_ , _t_ or _1_ statuses will not be included in the returned user objects. |     |     |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`POST https://api.twitter.com/1.1/blocks/destroy.json?screen_name=theSeanCook&skip_status=1`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

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

POST mutes/users/create

post-mutes-users-create

POST mutes/users/create
=======================

Mutes the user specified in the ID parameter for the authenticating user.

Returns the muted user when successful. Returns a string describing the failure condition when unsuccessful.

Actions taken in this method are asynchronous. Changes will be eventually consistent.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/mutes/users/create.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| screen\_name | optional | The screen name of the potentially muted user. Helpful for disambiguating when a valid screen name is also a user ID. |     | _whiteleaf_ |
| user\_id | optional | The ID of the potentially muted user. Helpful for disambiguating when a valid user ID is also a valid screen name. |     | _12345_ |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`POST https://api.twitter.com/1.1/mutes/users/create.json?screen_name=evilpiper`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

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
      "statuses_count": 71,
      "lang": "en",
      "status": {
        "created_at": "Tue Apr 15 00:10:23 +0000 2014",
        "id": 455860653731753984,
        "id_str": "455860653731753984",
        "text": "Super cool app to install http://t.co/ZiH6VOqLB3",
        "source": "Twitter for  iPhone",
        "truncated": false,
        "in_reply_to_status_id": null,
        "in_reply_to_status_id_str": null,
        "in_reply_to_user_id": null,
        "in_reply_to_user_id_str": null,
        "in_reply_to_screen_name": null,
        "geo": null,
        "coordinates": null,
        "place": null,
        "contributors": null,
        "retweet_count": 0,
        "favorite_count": 0,
        "entities": {
          "hashtags": [
    
          ],
          "symbols": [
    
          ],
          "urls": [
            {
              "url": "http://t.co/ZiH6VOqLB3",
              "expanded_url": "http://cards-demo.cfapps.io/owntracks.html",
              "display_url": "cards-demo.cfapps.io/owntracks.html",
              "indices": [
                26,
                48
              ]
            }
          ],
          "user_mentions": [
    
          ]
        },
        "favorited": false,
        "retweeted": false,
        "possibly_sensitive": false,
        "lang": "en"
      },
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

POST mutes/users/destroy

post-mutes-users-destroy

POST mutes/users/destroy
========================

Un-mutes the user specified in the ID parameter for the authenticating user.

Returns the unmuted user when successful. Returns a string describing the failure condition when unsuccessful.

Actions taken in this method are asynchronous. Changes will be eventually consistent.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/mutes/users/destroy.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| screen\_name | optional | The screen name of the potentially muted user. Helpful for disambiguating when a valid screen name is also a user ID. |     | _whiteleaf_ |
| user\_id | optional | The ID of the potentially muted user. Helpful for disambiguating when a valid user ID is also a valid screen name. |     | _12345_ |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`POST https://api.twitter.com/1.1/mutes/users/destroy.json?screen_name=evilpiper`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

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
      "statuses_count": 71,
      "lang": "en",
      "status": {
        "created_at": "Tue Apr 15 00:10:23 +0000 2014",
        "id": 455860653731753984,
        "id_str": "455860653731753984",
        "text": "Super cool app to install http://t.co/ZiH6VOqLB3",
        "source": "Twitter for  iPhone",
        "truncated": false,
        "in_reply_to_status_id": null,
        "in_reply_to_status_id_str": null,
        "in_reply_to_user_id": null,
        "in_reply_to_user_id_str": null,
        "in_reply_to_screen_name": null,
        "geo": null,
        "coordinates": null,
        "place": null,
        "contributors": null,
        "retweet_count": 0,
        "favorite_count": 0,
        "entities": {
          "hashtags": [
    
          ],
          "symbols": [
    
          ],
          "urls": [
            {
              "url": "http://t.co/ZiH6VOqLB3",
              "expanded_url": "http://cards-demo.cfapps.io/owntracks.html",
              "display_url": "cards-demo.cfapps.io/owntracks.html",
              "indices": [
                26,
                48
              ]
            }
          ],
          "user_mentions": [
    
          ]
        },
        "favorited": false,
        "retweeted": false,
        "possibly_sensitive": false,
        "lang": "en"
      },
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

POST users/report\_spam

post-users-report\_spam

POST users/report\_spam
=======================

Report the specified user as a spam account to Twitter. Additionally, optionally performs the equivalent of [POST blocks / create](https://developer.twitter.com/en/docs/accounts-and-users/mute-block-report-users/api-reference/post-blocks-create) on behalf of the authenticated user.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/users/report_spam.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| screen\_name | optional | The screen\_name of the user to report as a spammer. Helpful for disambiguating when a valid screen name is also a user ID. |     | _noradio_ |
| user\_id | optional | The ID of the user to report as a spammer. Helpful for disambiguating when a valid user ID is also a valid screen name. |     | _12345_ |
| perform\_block | optional | Whether the account should be blocked by the authenticated user, as well as being reported for spam. | true | _false_ |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`POST https://api.twitter.com/1.1/users/report_spam.json?screen_name=themattharris&perform_block=false`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
      "name": "Matt Harris",
      "profile_sidebar_border_color": "C0DEED",
      "profile_sidebar_fill_color": "DDEEF6",
      "profile_background_tile": false,
      "profile_image_url": "http://a0.twimg.com/profile_images/554181350/matt_normal.jpg",
      "created_at": "Sat Feb 17 20:49:54 +0000 2007",
      "location": "SFO/LHR/YVR/JAX/IAD",
      "is_translator": false,
      "follow_request_sent": false,
      "id_str": "777925",
      "profile_link_color": "0084B4",
      "entities": {
        "url": {
          "urls": [
            {
              "expanded_url": null,
              "url": "http://www.themattharris.com",
              "indices": [
                0,
                28
              ],
              "display_url": null
            }
          ]
        },
        "description": {
          "urls": [
    
          ]
        }
      },
      "default_profile": true,
      "contributors_enabled": true,
      "url": "http://www.themattharris.com",
      "favourites_count": 213,
      "utc_offset": -28800,
      "id": 777925,
      "profile_image_url_https": "https://si0.twimg.com/profile_images/554181350/matt_normal.jpg",
      "profile_use_background_image": true,
      "listed_count": 303,
      "profile_text_color": "333333",
      "protected": false,
      "lang": "en",
      "followers_count": 7984,
      "time_zone": "Pacific Time (US & Canada)",
      "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme1/bg.png",
      "verified": false,
      "profile_background_color": "C0DEED",
      "notifications": false,
      "description": "Part of @twitter's Platform Services. Married to @cindyli. Kryptonite hurts me.",
      "geo_enabled": true,
      "statuses_count": 4492,
      "default_profile_image": false,
      "status": {
        "coordinates": null,
        "favorited": false,
        "created_at": "Tue Aug 28 00:11:59 +0000 2012",
        "truncated": false,
        "id_str": "240240276298420224",
        "entities": {
          "urls": [
            {
              "expanded_url": "https://twitter.com/rsarver/status/240224006807117828",
              "url": "https://t.co/DdTXEtcd",
              "indices": [
                71,
                92
              ],
              "display_url": "twitter.com/rsarver/status…"
            },
            {
              "expanded_url": "https://twitter.com/rsarver/status/240223841786404864",
              "url": "https://t.co/Pq8Sj0sl",
              "indices": [
                97,
                118
              ],
              "display_url": "twitter.com/rsarver/status…"
            }
          ],
          "hashtags": [
    
          ],
          "user_mentions": [
            {
              "name": "Heilemann",
              "id_str": "11656",
              "id": 11656,
              "indices": [
                1,
                11
              ],
              "screen_name": "Heilemann"
            },
            {
              "name": "Luke Dorny",
              "id_str": "12587",
              "id": 12587,
              "indices": [
                13,
                24
              ],
              "screen_name": "luxuryluke"
            },
            {
              "name": "Ryan Sarver",
              "id_str": "795649",
              "id": 795649,
              "indices": [
                27,
                35
              ],
              "screen_name": "rsarver"
            },
            {
              "name": "Jeremy Keith",
              "id_str": "11250",
              "id": 11250,
              "indices": [
                61,
                69
              ],
              "screen_name": "adactio"
            }
          ]
        },
        "in_reply_to_user_id_str": "11656",
        "text": ".@Heilemann, @luxuryluke - @rsarver has been clarifying with @adactio: https://t.co/DdTXEtcd and https://t.co/Pq8Sj0sl",
        "contributors": null,
        "retweet_count": 0,
        "id": 240240276298420224,
        "in_reply_to_status_id_str": "240226590703898624",
        "geo": null,
        "retweeted": false,
        "in_reply_to_user_id": 11656,
        "possibly_sensitive": false,
        "place": null,
        "possibly_sensitive_editable": true,
        "source": "Twitter for  iPhone",
        "in_reply_to_screen_name": "Heilemann",
        "in_reply_to_status_id": 240226590703898624
      },
      "friends_count": 430,
      "profile_background_image_url": "http://a0.twimg.com/images/themes/theme1/bg.png",
      "show_all_inline_media": false,
      "screen_name": "themattharris",
      "following": true
    }

Overview

**Please note**  

We've released the following endpoints within the [Twitter API v2](https://developer.twitter.com/en/docs/twitt/content/developer-twitter/en/docs/twitter-api/getting-started/about-twitter-apier-api/early-access) . 

|     |     |     |
| --- | --- | --- |
| **v1.1 endpoints** | **Corresponding v2 endpoints** |     |
| [GET users/lookup](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-users-lookup)  <br>[GET users/show](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-users-show) | [User lookup](https://developer.twitter.com/en/docs/twitter-api/users/lookup/introduction) | [Migration guide](https://developer.twitter.com/en/docs/twitter-api/users/lookup/migrate) |
| [GET followers/ids](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-followers-ids)  <br>[GET followers/list](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-followers-list)  <br>[GET friends/ids](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-friends-ids)  <br>[GET friends/list](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-friends-list)  <br>[POST friendships/create](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/post-friendships-create)[POST friendships/destroy](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/post-friendships-destroy) | [Follows](https://developer.twitter.com/en/docs/twitter-api/users/follows/introduction) | [Migration guide](https://developer.twitter.com/en/docs/twitter-api/users/follows/migrate) |

Please use the migration guides to see what has changed between the standard v1.1 and v2 versions.

Overview
--------

The following API endpoints can be used to programmatically follow users, search for users, and get user information:

|     |     |     |
| --- | --- | --- |
| **Friends and followers** | **POST friendships** | **Get user info** |
| * GET followers/ids<br>* GET followers/list<br>* GET friends/ids<br>* GET friends/list<br>* GET friendships/incoming<br>* GET friendships/lookup<br>* GET friendships/no\_retweets/ids<br>* GET friendships/outgoing<br>* GET friendships/show | * POST friendships/create<br>* POST friendships/destroy<br>* POST friendships/update | * GET users/lookup<br>* GET users/search<br>* GET users/show |

For more details, please see the individual endpoint information within the [API reference](https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference) section.  
 

### Terminology

To avoid confusion around the term "friends" and "followers" with respect to the API endpoints, below is a definition of each:

**Friends** - we refer to "friends" as the Twitter users that a specific user follows (e.g., following). Therefore, the GET friends/ids endpoint returns a collection of user IDs that the specified user follows.

**Followers** - refers to the Twitter users that follow a specific user. Therefore, making a request to the GET followers/ids endpoint returns a collection of user IDs for every user following the specified user.

GET followers/ids

get-followers-ids

GET followers/ids
=================

Returns a cursored collection of user IDs for every user following the specified user.

At this time, results are ordered with the most recent following first — however, this ordering is subject to unannounced change and eventual consistency issues. Results are given in groups of 5,000 user IDs and multiple "pages" of results can be navigated through using the `next_cursor` value in subsequent requests. See [Using cursors to navigate collections](https://developer.twitter.com/en/docs/basics/cursoring) for more information.

This method is especially powerful when used in conjunction with [GET users / lookup](https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-lookup), a method that allows you to convert user IDs into full [user objects](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object) in bulk.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/followers/ids.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 15  |
| Requests / 15-min window (app auth) | 15  |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

| Name | Required | Description | Default Value | Example |
| --- | --- | --- | --- | --- |
| user\_id | optional | The ID of the user for whom to return results. |     | `12345` |
| screen\_name | optional | The screen name of the user for whom to return results. |     | `noradio` |
| cursor | semi-optional | Causes the list of connections to be broken into pages of no more than 5000 IDs at a time. The number of IDs returned is not guaranteed to be 5000 as suspended users are filtered out after connections are queried. If no cursor is provided, a value of `-1` will be assumed, which is the first "page."<br><br>The response from the API will include a `previous_cursor` and `next_cursor` to allow paging back and forth. See [Using cursors to navigate collections](https://developer.twitter.com/en/docs/basics/cursoring) for more information. | `-1` | `12893764510938` |
| stringify\_ids | optional | Some programming environments will not consume Twitter IDs due to their size. Provide this option to have IDs returned as strings instead. More about [Twitter IDs](https://developer.twitter.com/en/docs/basics/twitter-ids). | `false` | `true` |
| count | optional | Specifies the number of IDs attempt retrieval of, up to a maximum of 5,000 per distinct request. The value of `count` is best thought of as a limit to the number of results to return. When using the count parameter with this method, it is wise to use a consistent count value across all requests to the same user's collection. Usage of this parameter is encouraged in environments where all 5,000 IDs constitutes too large of a response. |     | `2048` |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`GET https://api.twitter.com/1.1/followers/ids.json?cursor=-1&screen_name=andypiper&count=5000`

    $ curl --request GET 
    --url 'https://api.twitter.com/1.1/followers/ids.json?screen_name=twitterdev' 
    --header 'authorization: Bearer <bearer>'

    $ curl --request GET 
      --url 'https://api.twitter.com/1.1/followers/ids.json?screen_name=twitterdev' 
      --header 'authorization: OAuth oauth_consumer_key="consumer-key-for-app", 
      oauth_nonce="generated-nonce", oauth_signature="generated-signature", 
      oauth_signature_method="HMAC-SHA1", oauth_timestamp="generated-timestamp", 
      oauth_version="1.0"'

    $ twurl /1.1/followers/ids.json?screen_name=twitterdev

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
        "ids": [
            455974794,
            947576438684872705,
            850839346009780224,
            958850376630910976,
            889483959943536640,
            966094285119606784,
            1020583045,
            948604640811212801,
            967155179614240768,
            554514802,
            14873932,
            963916668731904000,
            970763391181746178,
            966091392631140358,
            .
            .
            .
            5000 ids later,
            .
            .
            .
            813143846,
            958604886735716353,
            402873729,
            958603486551330817,
            913076424897994753,
            820967329068707840,
            958593574932762624,
            958589381102665728,
            958573223737724929,
            889474485694410752
        ],
        "next_cursor": 1591087837626119954,
        "next_cursor_str": "1591087837626119954",
        "previous_cursor": 0,
        "previous_cursor_str": "0"
    }

GET followers/list

get-followers-list

GET followers/list
==================

Returns a cursored collection of user objects for users following the specified user.

At this time, results are ordered with the most recent following first — however, this ordering is subject to unannounced change and eventual consistency issues. Results are given in groups of 20 users and multiple "pages" of results can be navigated through using the `next_cursor` value in subsequent requests. See [Using cursors to navigate collections](https://developer.twitter.com/en/docs/basics/cursoring) for more information.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/followers/list.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 15  |
| Requests / 15-min window (app auth) | 15  |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

| Name | Required | Description | Default Value | Example |
| --- | --- | --- | --- | --- |
| user\_id | optional | The ID of the user for whom to return results. |     | `12345` |
| screen\_name | optional | The screen name of the user for whom to return results. |     | `twitterdev` |
| cursor | semi-optional | Causes the results to be broken into pages. If no cursor is provided, a value of `-1` will be assumed, which is the first "page."<br><br>The response from the API will include a `previous_cursor` and `next_cursor` to allow paging back and forth. See [Using cursors to navigate collections](https://developer.twitter.com/en/docs/basics/cursoring) for more information. | `-1` | `12893764510938` |
| count | optional | The number of users to return per page, up to a maximum of 200. Defaults to 20. |     | `42` |
| skip\_status | optional | When set to either `true`, `t` or `1`, statuses will not be included in the returned user objects. If set to any other value, statuses will be included. | `false` | `false` |
| include\_user\_entities | optional | The user object `entities` node will not be included when set to `false`. | `true` | `false` |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`GET https://api.twitter.com/1.1/followers/list.json?cursor=-1&screen_name=twitterdev&skip_status=true&include_user_entities=false`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
      "users": [
          {user-object},
          {user-object},
          {user-object}
      ],
      "next_cursor": 1489467234237774933,
      "next_cursor_str": "1489467234237774933",
      "previous_cursor": 0,
      "previous_cursor_str": "0"
    }

For more detail, see the [user-object definition](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object).

GET friends/ids

get-friends-ids

GET friends/ids
===============

Returns a cursored collection of user IDs for every user the specified user is following (otherwise known as their "friends").

At this time, results are ordered with the most recent following first — however, this ordering is subject to unannounced change and eventual consistency issues. Results are given in groups of 5,000 user IDs and multiple "pages" of results can be navigated through using the `next_cursor` value in subsequent requests. See [Using cursors to navigate collections](https://developer.twitter.com/en/docs/basics/cursoring) for more information.

This method is especially powerful when used in conjunction with [GET users / lookup](https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-lookup), a method that allows you to convert user IDs into full [user objects](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object) in bulk.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/friends/ids.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 15  |
| Requests / 15-min window (app auth) | 15  |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

| Name | Required | Description | Default Value | Example |
| --- | --- | --- | --- | --- |
| user\_id | optional | The ID of the user for whom to return results. |     | `12345` |
| screen\_name | optional | The screen name of the user for whom to return results. |     | `noradio` |
| cursor | semi-optional | Causes the list of connections to be broken into pages of no more than 5000 IDs at a time. The number of IDs returned is not guaranteed to be 5000 as suspended users are filtered out after connections are queried. If no cursor is provided, a value of `-1` will be assumed, which is the first "page."<br><br>The response from the API will include a `previous_cursor` and `next_cursor` to allow paging back and forth. See [Using cursors to navigate collections](https://developer.twitter.com/en/docs/basics/cursoring) for more information. | `-1` | `12893764510938` |
| stringify\_ids | optional | Some programming environments will not consume Twitter IDs due to their size. Provide this option to have IDs returned as strings instead. More about [Twitter IDs](https://developer.twitter.com/en/docs/basics/twitter-ids). | `false` | `true` |
| count | optional | Specifies the number of IDs attempt retrieval of, up to a maximum of 5,000 per distinct request. The value of `count` is best thought of as a limit to the number of results to return. When using the count parameter with this method, it is wise to use a consistent count value across all requests to the same user's collection. Usage of this parameter is encouraged in environments where all 5,000 IDs constitutes too large of a response. |     | `2048` |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

    $ curl --request GET 
      --url 'https://api.twitter.com/1.1/friends/ids.json?screen_name=twitterdev' 
      --header 'authorization: Bearer <bearer>'

    $ curl --request GET 
      --url 'https://api.twitter.com/1.1/friends/ids.json?screen_name=twitterdev' 
      --header 'authorization: OAuth oauth_consumer_key="consumer-key-for-app", 
      oauth_nonce="generated-nonce", oauth_signature="generated-signature", 
      oauth_signature_method="HMAC-SHA1", oauth_timestamp="generated-timestamp", 
      oauth_version="1.0"'

    $ twurl /1.1/friends/ids.json?screen_name=twitterdev

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
      "previous_cursor": 0,
      "ids": [
        657693,
        183709371,
        7588892,
        38895958,
        22891211,
        9019482,
        14488353,
        11750202,
        12249,
        22915745,
        1249881,
        14927800,
        1523501,
        22548447,
        15062340,
        133031077,
        17874544,
        777925,
        4265731,
        27674040,
        26123649,
        9576402,
        821958,
        7852612,
        819797,
        1401881,
        8285392,
        9160152,
        795649,
        3191321,
        783214
      ],
      "previous_cursor_str": "0",
      "next_cursor": 0,
      "next_cursor_str": "0"
    }

GET friends/list

get-friends-list

GET friends/list
================

Returns a cursored collection of user objects for every user the specified user is following (otherwise known as their "friends").

At this time, results are ordered with the most recent following first — however, this ordering is subject to unannounced change and eventual consistency issues. Results are given in groups of 20 users and multiple "pages" of results can be navigated through using the `next_cursor` value in subsequent requests. See [Using cursors to navigate collections](https://developer.twitter.com/en/docs/basics/cursoring) for more information.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/friends/list.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 15  |
| Requests / 15-min window (app auth) | 15  |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

| Name | Required | Description | Default Value | Example |
| --- | --- | --- | --- | --- |
| user\_id | optional | The ID of the user for whom to return results. |     | `12345` |
| screen\_name | optional | The screen name of the user for whom to return results. |     | `noradio` |
| cursor | semi-optional | Causes the results to be broken into pages. If no cursor is provided, a value of `-1` will be assumed, which is the first "page."<br><br>The response from the API will include a `previous_cursor` and `next_cursor` to allow paging back and forth. See [Using cursors to navigate collections](https://developer.twitter.com/en/docs/basics/cursoring) for more information. | `-1` | `12893764510938` |
| count | optional | The number of users to return per page, up to a maximum of 200. | `20` | `42` |
| skip\_status | optional | When set to either `true`, `t` or `1` statuses will not be included in the returned user objects. | `false` | `false` |
| include\_user\_entities | optional | The user object `entities` node will not be included when set to `false`. | `true` | `false` |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`GET https://api.twitter.com/1.1/friends/list.json?cursor=-1&screen_name=twitterapi&skip_status=true&include_user_entities=false`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
    "users": [
          {user-object},
          {user-object},
          {user-object}
      ],
      "previous_cursor": 0,
      "previous_cursor_str": "0",
      "next_cursor": 1333504313713126852,
      "next_cursor_str": "1333504313713126852"
    }

For more detail, see the [user-object definition](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object).

GET friendships/incoming

get-friendships-incoming

GET friendships/incoming
========================

Returns a collection of numeric IDs for every user who has a pending request to follow the authenticating user.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/friendships/incoming.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 15  |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

| Name | Required | Description | Default Value | Example |
| --- | --- | --- | --- | --- |
| cursor | semi-optional | Causes the list of connections to be broken into pages of no more than 5000 IDs at a time. The number of IDs returned is not guaranteed to be 5000 as suspended users are filtered out after connections are queried. If no cursor is provided, a value of `-1` will be assumed, which is the first "page."<br><br>The response from the API will include a `previous_cursor` and `next_cursor` to allow paging back and forth. |     | `12893764510938` |
| stringify\_ids | optional | Many programming environments will not consume our Tweet ids due to their size. Provide this option to have ids returned as strings instead. |     | `true` |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`GET https://api.twitter.com/1.1/friendships/incoming.json`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
      "previous_cursor": 0,
      "ids": [6253282],
      "previous_cursor_str": "0",
      "next_cursor": 0,
      "next_cursor_str": "0"
    }

GET friendships/lookup

get-friendships-lookup

GET friendships/lookup
======================

Returns the relationships of the authenticating user to the comma-separated list of up to 100 screen\_names or user\_ids provided. Values for `connections` can be: `following`, `following_requested`, `followed_by`, `none`, `blocking`, `muting`.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/friendships/lookup.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 15  |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| screen\_name | optional | A comma separated list of screen names, up to 100 are allowed in a single request. |     | _twitterapi twitter_ |
| user\_id | optional | A comma separated list of user IDs, up to 100 are allowed in a single request. |     | _783214 6253282_ |

Example Requests[¶](#example-requests "Permalink to this headline")
-------------------------------------------------------------------

    $ curl --request GET 
      --url 'https://api.twitter.com/1.1/friendships/lookup.json?screen_name=andypiper%2Cbinary_aaron%2Ctwitterdev%2Chappycamper%2Charris_0ff' 
      --header 'authorization: OAuth oauth_consumer_key="consumer-key-for-app", 
      oauth_nonce="generated-nonce", oauth_signature="generated-signature", 
      oauth_signature_method="HMAC-SHA1", oauth_timestamp="generated-timestamp", 
      oauth_token="access-token-for-authed-user", oauth_version="1.0"'

    $ twurl /1.1/friendships/lookup.json?screen_name=andypiper,binary_aaron,twitterdev,happycamper,harris_0ff

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    [
      {
        "name": "andy piper (pipes)",
        "screen_name": "andypiper",
        "id": 786491,
        "id_str": "786491",
        "connections": [
          "following"
        ]
      },
      {
        "name": "λ🥑. 🍞",
        "screen_name": "binary_aaron",
        "id": 165837734,
        "id_str": "165837734",
        "connections": [
          "following",
          "followed_by"
        ]
      },
      {
        "name": "Twitter Dev",
        "screen_name": "TwitterDev",
        "id": 2244994945,
        "id_str": "2244994945",
        "connections": [
          "following"
        ]
      },
      {
        "name": "Emily Sheehan 🏕",
        "screen_name": "happycamper",
        "id": 63046977,
        "id_str": "63046977",
        "connections": [
          "none"
        ]
      },
      {
        "name": "Harrison Test",
        "screen_name": "Harris_0ff",
        "id": 4337869213,
        "id_str": "4337869213",
        "connections": [
          "following",
          "following_requested",
          "followed_by"
        ]
      }
    ]

GET friendships/no\_retweets/ids

get-friendships-no\_retweets-ids

GET friendships/no\_retweets/ids
================================

Returns a collection of user\_ids that the currently authenticated user does not want to receive retweets from.

Use [POST friendships / update](https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/post-friendships-update) to set the "no retweets" status for a given user account on behalf of the current user.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/friendships/no_retweets/ids.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 15  |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| stringify\_ids | optional | Some programming environments will not consume Twitter IDs due to their size. Provide this option to have IDs returned as strings instead. Read more about [Twitter IDs](https://developer.twitter.com/en/docs/basics/twitter-ids). This parameter is important to use in Javascript environments. | _false_ | _true_ |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`GET https://api.twitter.com/1.1/friendships/no_retweets/ids.json?stringify_ids=true`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    ["777925","732321"]

GET friendships/outgoing

get-friendships-outgoing

GET friendships/outgoing
========================

Returns a collection of numeric IDs for every protected user for whom the authenticating user has a pending follow request.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/friendships/outgoing`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 15  |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

| Name | Required | Description | Default Value | Example |
| --- | --- | --- | --- | --- |
| cursor | semi-optional | Causes the list of connections to be broken into pages of no more than 5000 IDs at a time. The number of IDs returned is not guaranteed to be 5000 as suspended users are filtered out after connections are queried. If no cursor is provided, a value of `-1` will be assumed, which is the first "page."<br><br>The response from the API will include a `previous_cursor` and `next_cursor` to allow paging back and forth. See [Using cursors to navigate collections](https://developer.twitter.com/en/docs/basics/cursoring) for more information. | `-1` | `12893764510938` |
| stringify\_ids | optional | Some programming environments will not consume Twitter IDs due to their size. Provide this option to have IDs returned as strings instead. More about [Twitter IDs](https://developer.twitter.com/en/docs/basics/twitter-ids). | `false` | `true` |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`GET https://api.twitter.com/1.1/friendships/outgoing.json`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
      "previous_cursor": 0,
      "ids": [
        51937528,
        124856868,
        213246307,
        89356977,
        121177351,
        113338333,
        59520091,
        46451699,
        98223312,
        18172433,
        32210115,
        36851055,
        81269257
      ],
      "previous_cursor_str": "0",
      "next_cursor": 0,
      "next_cursor_str": "0"
    }

GET friendships/show

get-friendships-show

GET friendships/show
====================

Returns detailed information about the relationship between two arbitrary users.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/friendships/show.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 180 |
| Requests / 15-min window (app auth) | 15  |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| source\_id | optional | The user\_id of the subject user. |     | _783214_ |
| source\_screen\_name | optional | The screen\_name of the subject user. |     | _Twitter_ |
| target\_id | optional | The user\_id of the target user. |     | _2244994945_ |
| target\_screen\_name | optional | The screen\_name of the target user. |     | _TwitterDev_ |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`GET https://api.twitter.com/1.1/friendships/show.json?source_screen_name=twitterdev&target_screen_name=twitter`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
      "relationship": {
        "source": {
          "id": 783214,
          "id_str": "783214",
          "screen_name": "Twitter",
          "following": true,
          "followed_by": true,
          "live_following": false,
          "following_received": null,
          "following_requested": null,
          "notifications_enabled": null,
          "can_dm": true,
          "blocking": null,
          "blocked_by": null,
          "muting": null,
          "want_retweets": null,
          "all_replies": null,
          "marked_spam": null
        },
        "target": {
          "id": 2244994945,
          "id_str": "2244994945",
          "screen_name": "TwitterDev",
          "following": true,
          "followed_by": true,
          "following_received": null,
          "following_requested": null
        }
      }
    }

GET users/lookup

get-users-lookup

GET users/lookup
================

Returns fully-hydrated [user objects](https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-lookup) for up to 100 users per request, as specified by comma-separated values passed to the `user_id` and/or `screen_name` parameters.

This method is especially useful when used in conjunction with collections of user IDs returned from [GET friends / ids](https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-friends-ids) and [GET followers / ids](https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-followers-ids).

[GET users / show](https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-show) is used to retrieve a single user object.

There are a few things to note when using this method.

* You must be following a protected user to be able to see their most recent status update. If you don't follow a protected user their status will be removed.
* The order of user IDs or screen names may not match the order of users in the returned array.
* If a requested user is unknown, suspended, or deleted, then that user will not be returned in the results list.
* If none of your lookup criteria can be satisfied by returning a user object, a HTTP 404 will be thrown.
* You are strongly encouraged to use a POST for larger requests.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/users/lookup.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 900 |
| Requests / 15-min window (app auth) | 300 |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| screen\_name | optional | A comma separated list of screen names, up to 100 are allowed in a single request. You are strongly encouraged to use a POST for larger (up to 100 screen names) requests. |     | _twitterapi twitter_ |
| user\_id | optional | A comma separated list of user IDs, up to 100 are allowed in a single request. You are strongly encouraged to use a POST for larger requests. |     | _783214 6253282_ |
| include\_entities | optional | The _entities_ node that may appear within embedded statuses will not be included when set to _false_. |     | _false_ |
| tweet\_mode | optional | Valid request values are compat and extended, which give compatibility mode and extended mode, respectively for Tweets that contain over 140 characters |     | _false_ |

Example Requests[¶](#example-requests "Permalink to this headline")
-------------------------------------------------------------------

    $ curl --request GET 
      --url 'https://api.twitter.com/1.1/users/lookup.json?user_id=783214,6253282' 
      --header 'authorization: OAuth oauth_consumer_key="consumer-key-for-app", 
      oauth_nonce="generated-nonce", oauth_signature="generated-signature", 
      oauth_signature_method="HMAC-SHA1", oauth_timestamp="generated-timestamp", 
      oauth_version="1.0"'

    $ twurl /1.1/users/lookup.json?user_id=783214,6253282,2244994945

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    [
      {
        {user-object},
        {user-object},
        {user-object}
      }
    ]

For more detail, see the [user-object definition](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object).

GET users/search

get-users-search

GET users/search
================

Provides a simple, relevance-based search interface to public user accounts on Twitter. Try querying by topical interest, full name, company name, location, or other criteria. Exact match searches are not supported.

Only the first 1,000 matching results are available.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/users/search.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 900 |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| q   | required | The search query to run against people search. |     | _Twitter%20API_ |
| page | optional | Specifies the page of results to retrieve. |     | _3_ |
| count | optional | The number of potential user results to retrieve per page. This value has a maximum of 20. |     | _5_ |
| include\_entities | optional | The _entities_ node will not be included in embedded Tweet objects when set to _false_ . |     | _false_ |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

    $ curl --request GET 
      --url 'https://api.twitter.com/1.1/users/search.json?q=soccer' 
      --header 'authorization: OAuth oauth_consumer_key="consumer-key-for-app", 
      oauth_nonce="generated-nonce", oauth_signature="generated-signature", 
      oauth_signature_method="HMAC-SHA1", oauth_timestamp="generated-timestamp", 
      oauth_token="access-token-for-authed-user", oauth_version="1.0"'

    $ twurl /1.1/users/search.json?q=soccer

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    [
      {user-object},
      {user-object},
      {user-object},
      {user-object},
      {user-object},
      {user-object}
    ]

For more detail, see the [user-object definition](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object).

GET users/show

get-users-show

GET users/show
==============

Returns a [variety of information](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object) about the user specified by the required `user_id` or `screen_name` parameter. The author's most recent Tweet will be returned inline when possible.

[GET users / lookup](https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-lookup) is used to retrieve a bulk collection of user objects.

You must be following a protected user to be able to see their most recent Tweet. If you don't follow a protected user, the user's Tweet will be removed. A Tweet will not always be returned in the current\_status field.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/users/show.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 900 |
| Requests / 15-min window (app auth) | 900 |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| user\_id | required | The ID of the user for whom to return results. Either an id or screen\_name is required for this method. |     | _12345_ |
| screen\_name | required | The screen name of the user for whom to return results. Either a id or screen\_name is required for this method. |     | _noradio_ |
| include\_entities | optional | The _entities_ node will not be included when set to _false_. |     | _false_ |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

    $ curl --request GET 
        --url 'https://api.twitter.com/1.1/users/show.json?screen_name=twitterdev' 
        --header 'authorization: Bearer <bearer>'

    $ curl --request GET 
      --url 'https://api.twitter.com/1.1/users/show.json?screen_name=twitterdev' 
      --header 'authorization: OAuth oauth_consumer_key="consumer-key-for-app", 
      oauth_nonce="generated-nonce", oauth_signature="generated-signature", 
      oauth_signature_method="HMAC-SHA1", oauth_timestamp="generated-timestamp", 
      oauth_version="1.0"'

    $ twurl /1.1/users/show.json?screen_name=twitterdev

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {user-object}

For more detail, see the [user-object definition](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object).

POST friendships/create

post-friendships-create

POST friendships/create
=======================

Allows the authenticating user to follow (_friend_) the user specified in the ID parameter.

Returns the followed user when successful. Returns a string describing the failure condition when unsuccessful. If the user is already friends with the user a HTTP 403 may be returned, though for performance reasons this method may also return a HTTP 200 OK message even if the follow relationship already exists.

Actions taken in this method are asynchronous. Changes will be eventually consistent.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/friendships/create.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 24-hour window | 400 per user; 1000 per app |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| screen\_name | optional | The screen name of the user to follow. |     | _twitterdev_ |
| user\_id | optional | The ID of the user to follow. |     | _2244994945_ |
| follow | optional | Enable notifications for the target user. |     | _true_ |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

    curl --request POST 
    --url 'https://api.twitter.com/1.1/friendships/create.json?user_id=2244994945&follow=true' 
    --header 'authorization: OAuth oauth_consumer_key="YOUR_CONSUMER_KEY", oauth_nonce="AUTO_GENERATED_NONCE", oauth_signature="AUTO_GENERATED_SIGNATURE", oauth_signature_method="HMAC-SHA1", oauth_timestamp="AUTO_GENERATED_TIMESTAMP", oauth_token="USERS_ACCESS_TOKEN", oauth_version="1.0"' 
    --header 'content-type: application/json'

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {user-object,
      "status": {tweet-object}
    }

For more detail, see the [user-object definition](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object) and the [tweet-object definition](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object).

POST friendships/destroy

post-friendships-destroy

POST friendships/destroy
========================

Allows the authenticating user to unfollow the user specified in the ID parameter.

Returns the unfollowed user when successful. Returns a string describing the failure condition when unsuccessful.

Actions taken in this method are asynchronous. Changes will be eventually consistent.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/friendships/destroy.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| screen\_name | optional | The screen name of the user to unfollow. |     | _twitterdev_ |
| user\_id | optional | The ID of the user to unfollow. |     | _2244994945_ |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`POST https://api.twitter.com/1.1/friendships/destroy.json?user_id=2244994945`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {user-object,
      "status": {tweet-object}
    }

For more detail, see the [user-object definition](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object) and the [tweet-object definition](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object).

POST friendships/update

post-friendships-update

POST friendships/update
=======================

Turn on/off Retweets and device notifications from the specified user.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/friendships/update.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| screen\_name | optional | The screen name of the user being followed. |     | _twitterdev_ |
| user\_id | optional | The ID of the user being followed. |     | _2244994945_ |
| device | optional | Turn on/off device notifications from the target user. |     | _true_ |
| retweets | optional | Turn on/off Retweets from the target user. |     | _false_ |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`twurl -X POST /1.1/friendships/update.json?user_id=2244994945`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
      "relationship": {
        "source": {
          "id": 63046977,
          "id_str": "63046977",
          "screen_name": "happycamper",
          "following": true,
          "followed_by": false,
          "live_following": false,
          "following_received": null,
          "following_requested": false,
          "notifications_enabled": false,
          "can_dm": false,
          "blocking": false,
          "blocked_by": false,
          "muting": false,
          "want_retweets": true,
          "all_replies": false,
          "marked_spam": false
        },
        "target": {
          "id": 2244994945,
          "id_str": "2244994945",
          "screen_name": "TwitterDev",
          "following": false,
          "followed_by": true,
          "following_received": false,
          "following_requested": null
        }
      }
    }

Overview

**Please note**  

We've released the following endpoints within the [Twitter API v2](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api). 

|     |     |     |
| --- | --- | --- |
| **v1.1 endpoints** | **Corresponding v2 endpoints** |     |
| [GET lists/show](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-show) | [Lists lookup](https://developer.twitter.com/en/docs/twitter-api/lists/list-lookup) | [Migration guide](https://developer.twitter.com/en/docs/twitter-api/lists/list-lookup/migrate) |
| [POST lists/create](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-create)   <br>[POST lists/destroy](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-destroy)   <br>[POST lists/update](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-update) | [Manage Lists](https://developer.twitter.com/en/docs/twitter-api/lists/manage-lists/introduction) | [Migration guide](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/lists/manage-lists/migrate/manage-lists--standard-v1-1-compared-to-twitter-api-v2) |
| [GET lists/statuses](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-statuses) | [List Tweet lookup](https://developer.twitter.com/en/docs/twitter-api/lists/list-tweets/introduction) | [Migration guide](https://developer.twitter.com/en/docs/twitter-api/lists/list-tweets/migrate) |
| [](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-members-create)[GET lists/members](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-members)  <br>[GET lists/memberships](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-memberships)  <br>[POST lists/members/create](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-members-create)   <br>[POST lists/members/destroy](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-members-destroy) | [List members](https://developer.twitter.com/en/docs/twitter-api/lists/manage-lists/introduction) | [Migration guide](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/lists/manage-lists/migrate/manage-list-members--standard-v1-1-compared-to-twitter-api-v2) |
| [](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-subscribers-create)[GET lists/subscribers](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-subscribers)  <br>[GET lists/subscriptions](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-subscriptions)  <br>[GET lists/lists](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-list)  <br>[POST lists/subscribers/create](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-subscribers-create)   <br>[POST lists/subscribers/destroy](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-subscribers-destroy) | [List follows](https://developer.twitter.com/en/docs/twitter-api/lists/manage-lists/introduction) | [Migration guide](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/lists/manage-lists/migrate/manage-followed-lists--standard-v1-1-compared-to-twitter-api-v2) |

Please use the migration guides to see what has changed between the standard v1.1 and v2 versions.

A list is a curated group of Twitter accounts. You can create your own lists or subscribe to lists created by others for the authenticated user. Viewing a list timeline will show you a stream of Tweets from only the accounts on that list.

For general information on lists, see [Using Twitter lists](https://support.twitter.com/articles/76460) in the help center.

GET lists/list

get-lists-list

GET lists/list
==============

Returns all lists the authenticating or specified user subscribes to, including their own. The user is specified using the `user_id` or `screen_name` parameters. If no user is given, the authenticating user is used.

A maximum of 100 results will be returned by this call. Subscribed lists are returned first, followed by owned lists. This means that if a user subscribes to 90 lists and owns 20 lists, this method returns 90 subscriptions and 10 owned lists. The `reverse` method returns owned lists first, so with `reverse=true`, 20 owned lists and 80 subscriptions would be returned. If your goal is to obtain every list a user owns or subscribes to, use [GET lists / ownerships](https://developer.twitter.com/rest/reference/get/lists/ownerships) and/or [GET lists / subscriptions](https://developer.twitter.com/rest/reference/get/lists/subscriptions) instead.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/lists/list.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 15  |
| Requests / 15-min window (app auth) | 15  |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| user\_id | optional | The ID of the user for whom to return results. Helpful for disambiguating when a valid user ID is also a valid screen name. **Note:** : Specifies the ID of the user to get lists from. Helpful for disambiguating when a valid user ID is also a valid screen name. |     | _12345_ |
| screen\_name | optional | The screen name of the user for whom to return results. Helpful for disambiguating when a valid screen name is also a user ID. |     | _noradio_ |
| reverse | optional | Set this to _true_ if you would like owned lists to be returned first. See description above for information on how this parameter works. |     | _true_ |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`GET https://api.twitter.com/1.1/lists/list.json?screen_name=twitterapi`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    [
      {
        "slug": "meetup-20100301",
        "name": "meetup-20100301",
        "created_at": "Sat Feb 27 21:39:24 +0000 2010",
        "uri": "/twitterapi/meetup-20100301",
        "subscriber_count": 147,
        "id_str": "8044403",
        "member_count": 116,
        "mode": "public",
        "id": 8044403,
        "full_name": "@twitterapi/meetup-20100301",
        "description": "Guests attending the Twitter meetup on 1 March 2010 at the @twoffice",
        "user": {
          "profile_background_tile": true,
          "profile_sidebar_border_color": "C0DEED",
          "name": "Twitter API",
          "profile_sidebar_fill_color": "DDEEF6",
          "location": "San Francisco, CA",
          "created_at": "Wed May 23 06:01:13 +0000 2007",
          "profile_image_url": "http://a0.twimg.com/profile_images/2284174872/7df3h38zabcvjylnyfe3_normal.png",
          "is_translator": false,
          "id_str": "6253282",
          "profile_link_color": "0084B4",
          "follow_request_sent": false,
          "favourites_count": 25,
          "contributors_enabled": true,
          "url": "",
          "default_profile": false,
          "profile_image_url_https": "https://si0.twimg.com/profile_images/2284174872/7df3h38zabcvjylnyfe3_normal.png",
          "utc_offset": -28800,
          "profile_banner_url": "https://si0.twimg.com/profile_banners/6253282/1347394302",
          "id": 6253282,
          "profile_use_background_image": true,
          "listed_count": 11201,
          "profile_text_color": "333333",
          "protected": false,
          "lang": "en",
          "followers_count": 1444739,
          "description": "The Real Twitter API. I tweet about API changes, service issues and happily answer questions about Twitter and our API. Don't get an answer? It's on my website.",
          "notifications": false,
          "geo_enabled": true,
          "verified": true,
          "time_zone": "Pacific Time (US & Canada)",
          "profile_background_color": "C0DEED",
          "profile_background_image_url_https": "https://si0.twimg.com/profile_background_images/656927849/miyt9dpjz77sc0w3d4vj.png",
          "statuses_count": 3367,
          "friends_count": 33,
          "default_profile_image": false,
          "profile_background_image_url": "http://a0.twimg.com/profile_background_images/656927849/miyt9dpjz77sc0w3d4vj.png",
          "following": true,
          "screen_name": "twitterapi"
        },
        "following": false
      },
      {
        "slug": "team",
        "name": "team",
        "created_at": "Wed Nov 04 01:24:28 +0000 2009",
        "uri": "/twitterapi/team",
        "subscriber_count": 277,
        "id_str": "2031945",
        "member_count": 20,
        "mode": "public",
        "id": 2031945,
        "full_name": "@twitterapi/team",
        "description": "",
        "user": {
          "profile_background_tile": true,
          "profile_sidebar_border_color": "C0DEED",
          "name": "Twitter API",
          "profile_sidebar_fill_color": "DDEEF6",
          "location": "San Francisco, CA",
          "created_at": "Wed May 23 06:01:13 +0000 2007",
          "profile_image_url": "http://a0.twimg.com/profile_images/2284174872/7df3h38zabcvjylnyfe3_normal.png",
          "is_translator": false,
          "id_str": "6253282",
          "profile_link_color": "0084B4",
          "follow_request_sent": false,
          "favourites_count": 25,
          "contributors_enabled": true,
          "url": "",
          "default_profile": false,
          "profile_image_url_https": "https://si0.twimg.com/profile_images/2284174872/7df3h38zabcvjylnyfe3_normal.png",
          "utc_offset": -28800,
          "profile_banner_url": "https://si0.twimg.com/profile_banners/6253282/1347394302",
          "id": 6253282,
          "profile_use_background_image": true,
          "listed_count": 11201,
          "profile_text_color": "333333",
          "protected": false,
          "lang": "en",
          "followers_count": 1444739,
          "description": "The Real Twitter API. I tweet about API changes, service issues and happily answer questions about Twitter and our API. Don't get an answer? It's on my website.",
          "notifications": false,
          "geo_enabled": true,
          "verified": true,
          "time_zone": "Pacific Time (US & Canada)",
          "profile_background_color": "C0DEED",
          "profile_background_image_url_https": "https://si0.twimg.com/profile_background_images/656927849/miyt9dpjz77sc0w3d4vj.png",
          "statuses_count": 3367,
          "friends_count": 33,
          "default_profile_image": false,
          "profile_background_image_url": "http://a0.twimg.com/profile_background_images/656927849/miyt9dpjz77sc0w3d4vj.png",
          "following": true,
          "screen_name": "twitterapi"
        },
        "following": true
      }
    ]

GET lists/members

get-lists-members

GET lists/members
=================

Returns the members of the specified list. Private list members will only be shown if the authenticated user owns the specified list.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/lists/members.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 900 |
| Requests / 15-min window (app auth) | 75  |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

| Name | Required | Description | Default Value | Example |
| --- | --- | --- | --- | --- |
| list\_id | required | The numerical `id` of the list. |     |     |
| slug | required | You can identify a list by its slug instead of its numerical id. If you decide to do so, note that you'll also have to specify the list owner using the `owner_id` or `owner_screen_name` parameters. |     |     |
| owner\_screen\_name | optional | The screen name of the user who owns the list being requested by a `slug`. |     |     |
| owner\_id | optional | The user ID of the user who owns the list being requested by a `slug`. |     |     |
| count | optional | Specifies the number of results to return per page (see `cursor` below). The default is 20, with a maximum of 5,000. |     |     |
| cursor | semi-optional | Causes the collection of list members to be broken into "pages" of consistent sizes (specified by the `count` parameter). If no cursor is provided, a value of `-1` will be assumed, which is the first "page." |     |     |
| The response from the API will include a `previous_cursor` and `next_cursor` to allow paging back and forth. See Using cursors to navigate collections for more information. | `-1` | `12893764510938` |     |     |
| include\_entities | optional | The `entities` node will not be included when set to `false`. | `true` | `false` |
| skip\_status | optional | When set to either `true`, `t` or `1` statuses will not be included in the returned user objects. | `false` |     |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`GET https://api.twitter.com/1.1/lists/members.json?slug=team&owner_screen_name=twitterapi&cursor=-1`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

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

GET lists/members/show

get-lists-members-show

GET lists/members/show
======================

Check if the specified user is a member of the specified list.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/lists/members/show.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 15  |
| Requests / 15-min window (app auth) | 15  |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| list\_id | required | The numerical _id_ of the list. |     |     |
| slug | required | You can identify a list by its slug instead of its numerical id. If you decide to do so, note that you'll also have to specify the list owner using the _owner\_id_ or _owner\_screen\_name_ parameters. |     |     |
| user\_id | required | The ID of the user for whom to return results. Helpful for disambiguating when a valid user ID is also a valid screen name. |     |     |
| screen\_name | required | The screen name of the user for whom to return results. Helpful for disambiguating when a valid screen name is also a user ID. |     |     |
| owner\_screen\_name | optional | The screen name of the user who owns the list being requested by a _slug_. |     |     |
| owner\_id | optional | The user ID of the user who owns the list being requested by a _slug_. |     |     |
| include\_entities | optional | When set to either _true_, _t_ or _1_, each tweet will include a node called "entities". This node offers a variety of metadata about the tweet in a discreet structure, including: user\_mentions, urls, and hashtags. While entities are opt-in on timelines at present, they will be made a default component of output in the future. See [Tweet Entities](https://developer.twitter.com/overview/api/tweets) for more details. |     |     |
| skip\_status | optional | When set to either _true_, _t_ or _1_ statuses will not be included in the returned user objects. |     |     |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`GET https://api.twitter.com/1.1/lists/members/show.json?slug=team&owner_screen_name=twitter&screen_name=froginthevalley`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
      "id": "657693",
      "id_str": "657693",
      "is_translator": false,
      "default_profile": false,
      "entities": {
        "url": {
          "urls": [
            {
              "url": "http://t.co/jtb0IaGT",
              "indices": [
                0,
                20
              ],
              "display_url": "afroginthevalley.com",
              "expanded_url": "http://afroginthevalley.com/"
            }
          ]
        },
        "description": {
          "urls": []
        }
      },
      "show_all_inline_media": false,
      "profile_use_background_image": false,
      "profile_text_color": "999999",
      "utc_offset": -18000,
      "listed_count": 302,
      "name": "Sylvain Carle",
      "notifications": false,
      "profile_sidebar_border_color": "87CB00",
      "geo_enabled": true,
      "follow_request_sent": false,
      "url": "http://t.co/jtb0IaGT",
      "lang": "en",
      "profile_image_url_https": "https://si0.twimg.com/profile_images/1532782858/sylvaincarle-2011-profile-480_normal.png",
      "created_at": "Thu Jan 18 00:10:45 +0000 2007",
      "protected": false,
      "followers_count": 4281,
      "profile_background_image_url_https": "https://si0.twimg.com/profile_background_images/228591248/bg-14.png",
      "screen_name": "froginthevalley",
      "profile_background_tile": true,
      "friends_count": 2367,
      "profile_sidebar_fill_color": "333333",
      "description": "Developer Advocate at Twitter. Internet, opensource, media & geo/local geek. See also @sylvaincarle for LANG=FR.",
      "time_zone": "Eastern Time (US & Canada)",
      "default_profile_image": false,
      "location": "San Francisco",
      "profile_image_url": "http://a0.twimg.com/profile_images/1532782858/sylvaincarle-2011-profile-480_normal.png",
      "favourites_count": 1790,
      "following": false,
      "profile_background_color": "000000",
      "verified": false,
      "statuses_count": 8191,
      "status": {
        "entities": {
          "urls": [
            {
              "url": "http://t.co/GtBxX0IW",
              "indices": [
                54,
                74
              ],
              "display_url": "example.com",
              "expanded_url": "http://www.example.com"
            },
            {
              "url": "http://t.co/2E5hDjME",
              "indices": [
                94,
                114
              ],
              "display_url": "example.com",
              "expanded_url": "http://example.com"
            }
          ],
          "hashtags": [],
          "user_mentions": [
            {
              "name": "VO5",
              "indices": [
                0,
                6
              ],
              "screen_name": "MyVO5",
              "id": "485879570",
              "id_str": "485879570"
            }
          ]
        },
        "geo": null,
        "place": null,
        "in_reply_to_screen_name": "MyVO5",
        "in_reply_to_user_id": 485879570,
        "retweeted": false,
        "in_reply_to_status_id": 243404113679888400,
        "created_at": "Wed Sep 05 17:45:14 +0000 2012",
        "possibly_sensitive": false,
        "in_reply_to_status_id_str": "243404113679888385",
        "contributors": null,
        "favorited": false,
        "source": "YoruFukurou",
        "in_reply_to_user_id_str": "485879570",
        "retweet_count": 0,
        "id": "< Unable to parse in Javascript >",
        "id_str": "243404435752099841",
        "coordinates": null,
        "truncated": false,
        "text": "@MyVO5 make sure you configure your domain correctly, http://t.co/GtBxX0IW is not the same as http://t.co/2E5hDjME (also, refresh cache)."
      },
      "contributors_enabled": false,
      "profile_background_image_url": "http://a0.twimg.com/profile_background_images/228591248/bg-14.png",
      "profile_link_color": "009DFF"
    }

GET lists/memberships

get-lists-memberships

GET lists/memberships
=====================

Returns the lists the specified user has been added to. If `user_id` or `screen_name` are not provided, the memberships for the authenticating user are returned.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/lists/memberships.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 75  |
| Requests / 15-min window (app auth) | 75  |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| user\_id | optional | The ID of the user for whom to return results. Helpful for disambiguating when a valid user ID is also a valid screen name. |     |     |
| screen\_name | optional | The screen name of the user for whom to return results. Helpful for disambiguating when a valid screen name is also a user ID. |     |     |
| count | optional | The amount of results to return per page. Defaults to 20. No more than 1000 results will ever be returned in a single page. |     |     |
| cursor | optional | Breaks the results into pages. Provide a value of _\-1_ to begin paging. Provide values as returned in the response body's _next\_cursor_ and _previous\_cursor_ attributes to page back and forth in the list. It is recommended to always use cursors when the method supports them. See [Cursoring](https://developer.twitter.com/en/docs/basics/cursoring) for more information. |     |     |
| filter\_to\_owned\_lists | optional | When set to _true_ , _t_ or _1_ , will return just lists the authenticating user owns, and the user represented by _user\_id_ or _screen\_name_ is a member of. |     |     |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`GET https://api.twitter.com/1.1/lists/memberships.json?screen_name=twitter&cursor=-1`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

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

GET lists/ownerships

get-lists-ownerships

GET lists/ownerships
====================

Returns the lists owned by the specified Twitter user. Private lists will only be shown if the authenticated user is also the owner of the lists.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/lists/ownerships.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 15  |
| Requests / 15-min window (app auth) | 15  |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| user\_id | optional | The ID of the user for whom to return results. Helpful for disambiguating when a valid user ID is also a valid screen name. |     |     |
| screen\_name | optional | The screen name of the user for whom to return results. Helpful for disambiguating when a valid screen name is also a user ID. |     |     |
| count | optional | The amount of results to return per page. Defaults to 20. No more than 1000 results will ever be returned in a single page. |     |     |
| cursor | optional | Breaks the results into pages. Provide a value of _\-1_ to begin paging. Provide values as returned in the response body's _next\_cursor_ and _previous\_cursor_ attributes to page back and forth in the list. It is recommended to always use cursors when the method supports them. See [Cursoring](https://developer.twitter.com/en/docs/basics/cursoring) for more information. |     |     |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`GET https://api.twitter.com/1.1/lists/ownerships.json?screen_name=twitter&count=2`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

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

GET lists/show

get-lists-show

GET lists/show
==============

Returns the specified list. Private lists will only be shown if the authenticated user owns the specified list.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/lists/show.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 75  |
| Requests / 15-min window (app auth) | 75  |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| list\_id | required | The numerical _id_ of the list. |     |     |
| slug | required | You can identify a list by its slug instead of its numerical id. If you decide to do so, note that you'll also have to specify the list owner using the _owner\_id_ or _owner\_screen\_name_ parameters. |     |     |
| owner\_screen\_name | optional | The screen name of the user who owns the list being requested by a _slug_ . |     |     |
| owner\_id | optional | The user ID of the user who owns the list being requested by a _slug_ . |     |     |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`GET https://api.twitter.com/1.1/lists/show.json?slug=team&owner_screen_name=twitter`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

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

GET lists/statuses

get-lists-statuses

GET lists/statuses
==================

Returns a timeline of tweets authored by members of the specified list. Retweets are included by default. Use the `include_rts=false` parameter to omit retweets.

[Embedded Timelines](https://developer.twitter.com/web/embedded-timelines) is a great way to embed list timelines on your website.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/lists/statuses.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 900 |
| Requests / 15-min window (app auth) | 900 |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| list\_id | required | The numerical _id_ of the list. |     |     |
| slug | required | You can identify a list by its slug instead of its numerical id. If you decide to do so, note that you'll also have to specify the list owner using the _owner\_id_ or _owner\_screen\_name_ parameters. |     |     |
| owner\_screen\_name | optional | The screen name of the user who owns the list being requested by a _slug_ . |     |     |
| owner\_id | optional | The user ID of the user who owns the list being requested by a _slug_ . |     |     |
| since\_id | optional | Returns results with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets which can be accessed through the API. If the limit of Tweets has occured since the since\_id, the since\_id will be forced to the oldest ID available. |     |     |
| max\_id | optional | Returns results with an ID less than (that is, older than) or equal to the specified ID. |     |     |
| count | optional | Specifies the number of results to retrieve per "page." |     |     |
| include\_entities | optional | Entities are ON by default in API 1.1, each tweet includes a node called "entities". This node offers a variety of metadata about the tweet in a discreet structure, including: user\_mentions, urls, and hashtags. You can omit entities from the result by using _include\_entities=false_ |     |     |
| include\_rts | optional | When set to either _true_ , _t_ or _1_ , the list timeline will contain native retweets (if they exist) in addition to the standard stream of tweets. The output format of retweeted tweets is identical to the representation you see in home\_timeline. |     |     |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`GET https://api.twitter.com/1.1/lists/statuses.json?slug=teams&owner_screen_name=MLS&count=1`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    [
      {
        "coordinates": null,
        "created_at": "Mon Sep 10 14:04:58 +0000 2012",
        "truncated": false,
        "favorited": false,
        "id_str": "245160944223793152",
        "in_reply_to_user_id_str": null,
        "entities": {
          "urls": [
            {
              "expanded_url": "http://bit.ly/MuCCDo",
              "url": "http://t.co/W2tON3OK",
              "indices": [
                41,
                61
              ],
              "display_url": "bit.ly/MuCCDo"
            }
          ],
          "hashtags": [
            {
              "text": "TorontoFC",
              "indices": [
                87,
                97
              ]
            },
            {
              "text": "MLS",
              "indices": [
                98,
                102
              ]
            }
          ],
          "user_mentions": [
            {
              "name": "Team Up Foundation",
              "id_str": "210844741",
              "id": 210844741,
              "indices": [
                76,
                86
              ],
              "screen_name": "TeamUpFdn"
            }
          ]
        },
        "text": "Create your own TFC ESQ by Movado Watch: http://t.co/W2tON3OK in support of @TeamUpFdn #TorontoFC #MLS",
        "contributors": null,
        "id": 245160944223793152,
        "retweet_count": 0,
        "in_reply_to_status_id_str": null,
        "geo": null,
        "retweeted": false,
        "possibly_sensitive": false,
        "in_reply_to_user_id": null,
        "in_reply_to_screen_name": null,
        "source": "TweetDeck",
        "user": {
          "profile_sidebar_fill_color": "EB1D31",
          "profile_background_tile": false,
          "profile_sidebar_border_color": "FFFFFF",
          "name": "Toronto FC",
          "profile_image_url": "http://a0.twimg.com/profile_images/1827235104/TorontoFC1_normal.jpg",
          "created_at": "Fri Sep 11 15:42:26 +0000 2009",
          "location": "Toronto, ON",
          "follow_request_sent": false,
          "is_translator": false,
          "id_str": "73412535",
          "profile_link_color": "000000",
          "entities": {
            "url": {
              "urls": [
                {
                  "expanded_url": null,
                  "url": "http://www.torontofc.ca",
                  "indices": [
                    0,
                    23
                  ],
                  "display_url": null
                }
              ]
            },
            "description": {
              "urls": [
    
              ]
            }
          },
          "favourites_count": 2,
          "url": "http://www.torontofc.ca",
          "default_profile": false,
          "contributors_enabled": false,
          "profile_image_url_https": "https://si0.twimg.com/profile_images/1827235104/TorontoFC1_normal.jpg",
          "utc_offset": -18000,
          "id": 73412535,
          "listed_count": 1078,
          "profile_use_background_image": true,
          "followers_count": 28281,
          "protected": false,
          "profile_text_color": "000000",
          "lang": "en",
          "profile_background_color": "BC1228",
          "verified": true,
          "time_zone": "Eastern Time (US & Canada)",
          "profile_background_image_url_https": "https://si0.twimg.com/profile_background_images/603424485/k9py0fm18qrjr8l22qlp.jpeg",
          "notifications": false,
          "description": "Official Toronto FC Twitter by @AsifinToronto & @JonSinden. Follow us for the latest club news, links, pics & videos. Join us during matches for #TFClive",
          "geo_enabled": false,
          "default_profile_image": false,
          "friends_count": 13947,
          "profile_background_image_url": "http://a0.twimg.com/profile_background_images/603424485/k9py0fm18qrjr8l22qlp.jpeg",
          "statuses_count": 10774,
          "screen_name": "torontofc",
          "following": true,
          "show_all_inline_media": false
        },
        "place": null,
        "in_reply_to_status_id": null
      }
    ]

GET lists/subscribers

get-lists-subscribers

GET lists/subscribers
=====================

subscribers/\*

Returns the subscribers of the specified list. Private list subscribers will only be shown if the authenticated user owns the specified list.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/lists/subscribers.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 180 |
| Requests / 15-min window (app auth) | 15  |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| list\_id | required | The numerical _id_ of the list. |     |     |
| slug | required | You can identify a list by its slug instead of its numerical id. If you decide to do so, note that you'll also have to specify the list owner using the _owner\_id_ or _owner\_screen\_name_ parameters. |     |     |
| owner\_screen\_name | optional | The screen name of the user who owns the list being requested by a _slug_ . |     |     |
| owner\_id | optional | The user ID of the user who owns the list being requested by a _slug_ . |     |     |
| count | optional | Specifies the number of results to return per page (see _cursor_ below). The default is 20, with a maximum of 5,000. |     |     |
| cursor | optional | Breaks the results into pages. A single page contains 20 lists. Provide a value of _\-1_ to begin paging. Provide values as returned in the response body's _next\_cursor_ and _previous\_cursor_ attributes to page back and forth in the list. See [Using cursors to navigate collections](https://developer.twitter.com/en/docs/basics/cursoring) for more information. |     |     |
| include\_entities | optional | When set to either _true_ , _t_ or _1_ , each tweet will include a node called "entities". This node offers a variety of metadata about the tweet in a discreet structure, including: user\_mentions, urls, and hashtags. While entities are opt-in on timelines at present, they will be made a default component of output in the future. See [Tweet Entities](https://developer.twitter.com/overview/api/tweets) for more details. |     |     |
| skip\_status | optional | When set to either _true_ , _t_ or _1_ statuses will not be included in the returned user objects. |     |     |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`GET https://api.twitter.com/1.1/lists/subscribers.json?include_entities=true&cursor=-1&skip_status=true&slug=team&owner_screen_name=twitter`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
      "previous_cursor": 0,
      "previous_cursor_str": "0",
      "next_cursor": 1357643166637635702,
      "users": [
        {
          "profile_background_tile": false,
          "profile_sidebar_fill_color": "DDEEF6",
          "name": "Almissen665",
          "profile_sidebar_border_color": "C0DEED",
          "location": null,
          "profile_image_url": "http://a0.twimg.com/sticky/default_profile_images/default_profile_1_normal.png",
          "created_at": "Mon Jun 27 09:17:15 +0000 2011",
          "follow_request_sent": false,
          "is_translator": false,
          "profile_link_color": "0084B4",
          "id_str": "324841714",
          "url": null,
          "default_profile": true,
          "contributors_enabled": false,
          "favourites_count": 0,
          "id": 324841714,
          "utc_offset": null,
          "profile_image_url_https": "https://si0.twimg.com/sticky/default_profile_images/default_profile_1_normal.png",
          "profile_use_background_image": true,
          "listed_count": 0,
          "lang": "en",
          "profile_text_color": "333333",
          "followers_count": 6,
          "protected": false,
          "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme1/bg.png",
          "notifications": false,
          "geo_enabled": false,
          "description": null,
          "profile_background_color": "C0DEED",
          "time_zone": null,
          "verified": false,
          "statuses_count": 1,
          "friends_count": 27,
          "profile_background_image_url": "http://a0.twimg.com/images/themes/theme1/bg.png",
          "default_profile_image": true,
          "screen_name": "bonasser789",
          "following": false,
          "show_all_inline_media": false
        },
        {
          "profile_sidebar_fill_color": "E6F6F9",
          "profile_sidebar_border_color": "DBE9ED",
          "name": "GR Syber-Space",
          "profile_background_tile": true,
          "location": "Grand Rapids, MI",
          "profile_image_url": "http://a2.twimg.com/profile_images/1322547748/images__97__normal.jpg",
          "created_at": "Thu Sep 30 23:05:38 +0000 2010",
          "profile_link_color": "CC3366",
          "id_str": "197218370",
          "follow_request_sent": false,
          "is_translator": false,
          "url": "http://www.wix.com/castlesportsgr/myj",
          "default_profile": false,
          "favourites_count": 2,
          "contributors_enabled": false,
          "id": 197218370,
          "utc_offset": -18000,
          "profile_image_url_https": "https://si0.twimg.com/profile_images/1322547748/images__97__normal.jpg",
          "profile_use_background_image": true,
          "listed_count": 268,
          "lang": "en",
          "profile_text_color": "333333",
          "followers_count": 2628,
          "protected": true,
          "notifications": false,
          "geo_enabled": true,
          "profile_background_color": "DBE9ED",
          "description": "Welcome to Teen Gossip 411. Celebrity Gossip, Teens fashion trends for the summer 2011, Hollywood Gossip, Hotest music, Teen Websites, and more.",
          "time_zone": "Quito",
          "verified": false,
          "profile_background_image_url_https": "https://si0.twimg.com/profile_background_images/237705957/images__97_.jpg",
          "default_profile_image": false,
          "friends_count": 2846,
          "profile_background_image_url": "http://a2.twimg.com/profile_background_images/237705957/images__97_.jpg",
          "statuses_count": 7463,
          "show_all_inline_media": true,
          "screen_name": "GRSYBERSPACE",
          "following": false
        }
      ],
      "next_cursor_str": "1357643166637635702"
    }

GET lists/subscribers/show

get-lists-subscribers-show

GET lists/subscribers/show
==========================

Check if the specified user is a subscriber of the specified list. Returns the user if they are a subscriber.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/lists/subscribers/show.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 15  |
| Requests / 15-min window (app auth) | 15  |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| owner\_screen\_name | optional | The screen name of the user who owns the list being requested by a _slug_. |     |     |
| owner\_id | optional | The user ID of the user who owns the list being requested by a _slug_. |     |     |
| list\_id | required | The numerical _id_ of the list. |     |     |
| slug | required | You can identify a list by its slug instead of its numerical id. If you decide to do so, note that you'll also have to specify the list owner using the _owner\_id_ or _owner\_screen\_name_ parameters. |     |     |
| user\_id | required | The ID of the user for whom to return results. Helpful for disambiguating when a valid user ID is also a valid screen name. |     |     |
| screen\_name | required | The screen name of the user for whom to return results. Helpful for disambiguating when a valid screen name is also a user ID. |     |     |
| include\_entities | optional | When set to either _true_, _t_ or _1_, each Tweet will include a node called "entities". This node offers a variety of metadata about the tweet in a discreet structure, including: user\_mentions, urls, and hashtags. While entities are opt-in on timelines at present, they will be made a default component of output in the future. See [Tweet Entities](https://developer.twitter.com/overview/api/tweets) for more details. |     |     |
| skip\_status | optional | When set to either _true_ , _t_ or _1_ statuses will not be included in the returned user objects. |     |     |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`GET https://api.twitter.com/1.1/lists/subscribers/show.json?slug=team&owner_screen_name=twitter&screen_name=episod`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
      "id": "819797",
      "id_str": "819797",
      "is_translator": false,
      "default_profile": false,
      "entities": {
        "url": {
          "urls": [
            {
              "url": "http://t.co/Lxw7upbN",
              "indices": [
                0,
                20
              ],
              "display_url": "rebelmouse.com/episod/",
              "expanded_url": "http://www.rebelmouse.com/episod/"
            }
          ]
        },
        "description": {
          "urls": []
        }
      },
      "show_all_inline_media": true,
      "profile_use_background_image": true,
      "profile_text_color": "D20909",
      "utc_offset": -28800,
      "listed_count": 341,
      "name": "Taylor Singletary",
      "notifications": false,
      "profile_sidebar_border_color": "000000",
      "geo_enabled": true,
      "follow_request_sent": false,
      "url": "http://t.co/Lxw7upbN",
      "lang": "en",
      "profile_image_url_https": "https://si0.twimg.com/profile_images/2574556418/dk93ji5e3w4rwscaabt3_normal.png",
      "created_at": "Wed Mar 07 22:23:19 +0000 2007",
      "protected": false,
      "followers_count": 7180,
      "profile_background_image_url_https": "https://si0.twimg.com/profile_background_images/643655842/hzfv12wini4q60zzrthg.png",
      "screen_name": "episod",
      "profile_background_tile": true,
      "friends_count": 5452,
      "profile_sidebar_fill_color": "FBFBFB",
      "description": "Reality Technician, Twitter API team, synthesizer enthusiast; a most excellent adventure in timelines. Missive commander.",
      "time_zone": "Pacific Time (US & Canada)",
      "default_profile_image": false,
      "location": "San Francisco, CA",
      "profile_image_url": "http://a0.twimg.com/profile_images/2574556418/dk93ji5e3w4rwscaabt3_normal.png",
      "profile_banner_url": "https://si0.twimg.com/profile_banners/819797/1346803502",
      "favourites_count": 16076,
      "following": true,
      "profile_background_color": "000000",
      "verified": false,
      "statuses_count": 18132,
      "status": {
        "entities": {
          "urls": [
            {
              "url": "http://t.co/4mdAn0tF",
              "indices": [
                16,
                36
              ],
              "display_url": "youtube.com/watch?v=pPkNtg…",
              "expanded_url": "http://www.youtube.com/watch?v=pPkNtg3Fvwk&feature=youtube_gdata_player"
            }
          ],
          "hashtags": [],
          "user_mentions": []
        },
        "geo": null,
        "place": null,
        "in_reply_to_screen_name": null,
        "in_reply_to_user_id": null,
        "retweeted": false,
        "in_reply_to_status_id": null,
        "created_at": "Wed Sep 05 15:57:09 +0000 2012",
        "possibly_sensitive": false,
        "in_reply_to_status_id_str": null,
        "contributors": null,
        "favorited": false,
        "source": "YouTube on iOS",
        "in_reply_to_user_id_str": null,
        "retweet_count": 0,
        "id": "< Unable to parse in Javascript >",
        "id_str": "243377236902821888",
        "coordinates": null,
        "truncated": false,
        "text": "Current status  http://t.co/4mdAn0tF"
      },
      "contributors_enabled": false,
      "profile_background_image_url": "http://a0.twimg.com/profile_background_images/643655842/hzfv12wini4q60zzrthg.png",
      "profile_link_color": "C71818"
    }

GET lists/subscriptions

get-lists-subscriptions

GET lists/subscriptions
=======================

Obtain a collection of the lists the specified user is subscribed to, 20 lists per page by default. Does not include the user's own lists.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/lists/subscriptions.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 15  |
| Requests / 15-min window (app auth) | 15  |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| user\_id | optional | The ID of the user for whom to return results. Helpful for disambiguating when a valid user ID is also a valid screen name. |     |     |
| screen\_name | optional | The screen name of the user for whom to return results. Helpful for disambiguating when a valid screen name is also a user ID. |     |     |
| count | optional | The amount of results to return per page. Defaults to 20. No more than 1000 results will ever be returned in a single page. |     |     |
| cursor | optional | Breaks the results into pages. Provide a value of _\-1_ to begin paging. Provide values as returned in the response body's _next\_cursor_ and _previous\_cursor_ attributes to page back and forth in the list. It is recommended to always use cursors when the method supports them. See [Cursoring](https://developer.twitter.com/en/docs/basics/cursoring) for more information. |     |     |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`GET https://api.twitter.com/1.1/lists/subscriptions.json?cursor=-1&screen_name=episod&count=5`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
      "previous_cursor": 0,
      "lists": [
        {
          "slug": "team",
          "name": "team",
          "uri": "/TwitterEng/team",
          "created_at": "Mon Oct 03 02:48:07 +0000 2011",
          "subscriber_count": 131,
          "id_str": "55932616",
          "member_count": 324,
          "mode": "public",
          "id": 55932616,
          "full_name": "@TwitterEng/team",
          "description": "",
          "user": {
            "profile_sidebar_border_color": "C6E2EE",
            "profile_sidebar_fill_color": "DAECF4",
            "profile_background_tile": false,
            "expanded_url": null,
            "name": "Twitter Engineering",
            "location": "San Francisco, CA",
            "created_at": "Sat Jun 16 00:14:36 +0000 2007",
            "profile_image_url": "http://a2.twimg.com/profile_images/1262149685/twitter_newbird_boxed_blueonwhite_normal.png",
            "is_translator": false,
            "profile_link_color": "1F98C7",
            "follow_request_sent": null,
            "id_str": "6844292",
            "entities": {
              "urls": [
    
              ],
              "hashtags": [
    
              ],
              "user_mentions": [
    
              ]
            },
            "url": "http://engineering.twitter.com",
            "default_profile": false,
            "favourites_count": 0,
            "contributors_enabled": true,
            "id": 6844292,
            "utc_offset": -14400,
            "profile_image_url_https": "https://si0.twimg.com/profile_images/1262149685/twitter_newbird_boxed_blueonwhite_normal.png",
            "profile_use_background_image": true,
            "listed_count": 1493,
            "profile_text_color": "663B12",
            "lang": "en",
            "followers_count": 132674,
            "protected": false,
            "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme2/bg.gif",
            "verified": true,
            "geo_enabled": true,
            "notifications": null,
            "time_zone": "Atlantic Time (Canada)",
            "description": "The official account for Twitter Engineering.",
            "profile_background_color": "C6E2EE",
            "profile_background_image_url": "http://a1.twimg.com/images/themes/theme2/bg.gif",
            "default_profile_image": false,
            "statuses_count": 61,
            "friends_count": 0,
            "display_url": null,
            "screen_name": "TwitterEng",
            "following": null,
            "show_all_inline_media": true
          },
          "following": false
        },
        {
          "slug": "the-brain-trust",
          "name": "The Brain Trust",
          "uri": "/LTRK140/the-brain-trust",
          "created_at": "Sun Mar 06 20:01:50 +0000 2011",
          "subscriber_count": 24,
          "id_str": "37396827",
          "member_count": 148,
          "mode": "public",
          "id": 37396827,
          "full_name": "@LTRK140/the-brain-trust",
          "description": "Twitter Artists, Ascii, Unicode Art.",
          "user": {
            "profile_sidebar_border_color": "080000",
            "profile_sidebar_fill_color": "",
            "profile_background_tile": true,
            "name": "﹅█▄▀█▀ █▀▐━▀▄ ▌◢▌██﹅",
            "location": "Toronto",
            "created_at": "Fri Jun 04 16:48:39 +0000 2010",
            "profile_image_url": "http://a1.twimg.com/profile_images/1315622089/Cool_Daddy_normal.png",
            "is_translator": false,
            "profile_link_color": "080000",
            "follow_request_sent": false,
            "id_str": "151938348",
            "url": "http://twitter.com/KREWZO",
            "favourites_count": 10,
            "contributors_enabled": false,
            "default_profile": false,
            "id": 151938348,
            "utc_offset": -28800,
            "profile_image_url_https": "https://si0.twimg.com/profile_images/1315622089/Cool_Daddy_normal.png",
            "profile_use_background_image": true,
            "listed_count": 131,
            "profile_text_color": "000000",
            "lang": "en",
            "followers_count": 838,
            "protected": false,
            "profile_background_image_url_https": "https://si0.twimg.com/profile_background_images/285103295/ltrk140.JPG",
            "verified": false,
            "geo_enabled": true,
            "notifications": false,
            "time_zone": "Pacific Time (US & Canada)",
            "description": "▓⁄─⁄⁄﹅█▄▀█▀ █▀▐━▀▄ ▌◢▌██﹅⁄─⁄⁄▓  rn  •140•ASCII•UNICODE•ART• BY OZ MELO   •  I LIVE & WORK IN #YYZ.     ★★ MOST TWEETS ARE BEST VIEWED AS A STATUS PAGE ★★   █♥█",
            "profile_background_color": "030003",
            "profile_background_image_url": "http://a1.twimg.com/profile_background_images/285103295/ltrk140.JPG",
            "default_profile_image": false,
            "statuses_count": 1006,
            "friends_count": 139,
            "screen_name": "LTRK140",
            "following": false,
            "show_all_inline_media": true
          },
          "following": false
        },
        {
          "slug": "twoutside-lands",
          "name": "Twoutside Lands",
          "uri": "/dannyhertz/twoutside-lands",
          "created_at": "Fri Aug 12 07:21:25 +0000 2011",
          "subscriber_count": 12,
          "id_str": "52270561",
          "member_count": 25,
          "mode": "public",
          "id": 52270561,
          "full_name": "@dannyhertz/twoutside-lands",
          "description": "Tweeps @ Outside Lands 2011",
          "user": {
            "profile_sidebar_border_color": "4685e3",
            "profile_sidebar_fill_color": "c7dced",
            "profile_background_tile": false,
            "expanded_url": "http://www.dannyhertz.com",
            "name": "Danny Hertz",
            "location": "San Francisco",
            "created_at": "Sat Nov 15 02:26:09 +0000 2008",
            "profile_image_url": "http://a0.twimg.com/profile_images/1546221308/6153868543_d7ab87737a_b_normal.jpeg",
            "is_translator": true,
            "profile_link_color": "005082",
            "follow_request_sent": false,
            "id_str": "17400516",
            "entities": {
              "urls": [
    
              ],
              "hashtags": [
    
              ],
              "user_mentions": [
    
              ]
            },
            "url": "http://t.co/90RtgWI",
            "favourites_count": 243,
            "contributors_enabled": false,
            "default_profile": false,
            "id": 17400516,
            "utc_offset": -28800,
            "profile_image_url_https": "https://si0.twimg.com/profile_images/1546221308/6153868543_d7ab87737a_b_normal.jpeg",
            "profile_use_background_image": true,
            "listed_count": 52,
            "profile_text_color": "000000",
            "lang": "en",
            "followers_count": 2684,
            "protected": false,
            "profile_background_image_url_https": "https://si0.twimg.com/profile_background_images/331345358/pamperedpuppy20091103.jpeg",
            "verified": false,
            "geo_enabled": true,
            "notifications": false,
            "time_zone": "Pacific Time (US & Canada)",
            "description": "Software Engineer on the User Services team at Twitter and lead singer for the rock band Journey.",
            "profile_background_color": "ffffff",
            "profile_background_image_url": "http://a0.twimg.com/profile_background_images/331345358/pamperedpuppy20091103.jpeg",
            "default_profile_image": false,
            "statuses_count": 2318,
            "friends_count": 261,
            "display_url": "dannyhertz.com",
            "screen_name": "dannyhertz",
            "following": false,
            "show_all_inline_media": true
          },
          "following": false
        },
        {
          "slug": "july-6-curators",
          "name": "July 6 curators",
          "uri": "/townhall/july-6-curators",
          "created_at": "Mon Jul 04 20:37:28 +0000 2011",
          "subscriber_count": 58,
          "id_str": "49286494",
          "member_count": 8,
          "mode": "public",
          "id": 49286494,
          "full_name": "@townhall/july-6-curators",
          "description": "Curators helping for the Town Hall at the White House on July 6th at 2pm ET",
          "user": {
            "profile_sidebar_border_color": "C0DEED",
            "profile_sidebar_fill_color": "DDEEF6",
            "profile_background_tile": true,
            "name": "Town Hall",
            "location": "",
            "created_at": "Tue May 31 01:50:52 +0000 2011",
            "profile_image_url": "http://a2.twimg.com/profile_images/1419432899/avatar_normal.png",
            "is_translator": false,
            "profile_link_color": "0084B4",
            "follow_request_sent": null,
            "id_str": "308230587",
            "url": "http://askobama.twitter.com",
            "default_profile": false,
            "favourites_count": 0,
            "contributors_enabled": true,
            "id": 308230587,
            "utc_offset": -28800,
            "profile_image_url_https": "https://si0.twimg.com/profile_images/1419432899/avatar_normal.png",
            "profile_use_background_image": true,
            "listed_count": 517,
            "profile_text_color": "333333",
            "lang": "en",
            "followers_count": 24456,
            "protected": false,
            "profile_background_image_url_https": "https://si0.twimg.com/profile_background_images/280500767/bg.jpg",
            "verified": true,
            "geo_enabled": false,
            "notifications": null,
            "time_zone": "Pacific Time (US & Canada)",
            "description": "Official account for Twitter hosted town halls. Our first on July 6th, 2PM ET. ",
            "profile_background_color": "C0DEED",
            "profile_background_image_url": "http://a0.twimg.com/profile_background_images/280500767/bg.jpg",
            "default_profile_image": false,
            "statuses_count": 100,
            "friends_count": 2,
            "screen_name": "townhall",
            "following": null,
            "show_all_inline_media": true
          },
          "following": false
        },
        {
          "slug": "streaming-music-industry",
          "name": "Streaming Music Industry ",
          "uri": "/meetmarshall/streaming-music-industry",
          "created_at": "Thu Mar 31 04:04:10 +0000 2011",
          "subscriber_count": 193,
          "id_str": "41857276",
          "member_count": 1,
          "mode": "public",
          "id": 41857276,
          "full_name": "@meetmarshall/streaming-music-industry",
          "description": "A custom list created by adding, subtracting or filtering existing lists (made using @formulists)",
          "user": {
            "profile_sidebar_border_color": "C0DEED",
            "profile_sidebar_fill_color": "DDEEF6",
            "profile_background_tile": false,
            "name": "Marshall Kirkpatrick",
            "location": "",
            "created_at": "Mon Mar 28 20:18:47 +0000 2011",
            "profile_image_url": "http://a3.twimg.com/sticky/default_profile_images/default_profile_0_normal.png",
            "is_translator": false,
            "profile_link_color": "0084B4",
            "follow_request_sent": false,
            "id_str": "273602749",
            "url": "http://twitter.com/marshallk",
            "default_profile": true,
            "favourites_count": 0,
            "contributors_enabled": false,
            "id": 273602749,
            "utc_offset": -28800,
            "profile_image_url_https": "https://si0.twimg.com/sticky/default_profile_images/default_profile_0_normal.png",
            "profile_use_background_image": true,
            "listed_count": 3,
            "profile_text_color": "333333",
            "lang": "en",
            "followers_count": 29,
            "protected": false,
            "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme1/bg.png",
            "verified": false,
            "geo_enabled": false,
            "notifications": false,
            "time_zone": "Pacific Time (US & Canada)",
            "description": "I just came for the lists.",
            "profile_background_color": "C0DEED",
            "profile_background_image_url": "http://a0.twimg.com/images/themes/theme1/bg.png",
            "default_profile_image": true,
            "statuses_count": 3,
            "friends_count": 146,
            "screen_name": "meetmarshall",
            "following": false,
            "show_all_inline_media": false
          },
          "following": false
        }
      ],
      "previous_cursor_str": "0",
      "next_cursor": 1364811190668631091,
      "next_cursor_str": "1364811190668631091"
    }

POST lists/create

post-lists-create

POST lists/create
=================

Creates a new list for the authenticated user. Note that you can create up to 1000 lists per account.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/lists/create.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| name | required | The name for the list. A list's name must start with a letter and can consist only of 25 or fewer letters, numbers, "-", or "\_" characters. |     |     |
| mode | optional | Whether your list is public or private. Values can be _public_ or _private_ . If no mode is specified the list will be public. |     |     |
| description | optional | The description to give the list. |     |     |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`POST https://api.twitter.com/1.1/lists/create.json?name=Goonies&mode=public&description=For%20life`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

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

POST lists/destroy

post-lists-destroy

POST lists/destroy
==================

Deletes the specified list. The authenticated user must own the list to be able to destroy it.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/lists/destroy.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| owner\_screen\_name | optional | The screen name of the user who owns the list being requested by a _slug_ . |     |     |
| owner\_id | optional | The user ID of the user who owns the list being requested by a _slug_ . |     |     |
| list\_id | required | The numerical _id_ of the list. |     |     |
| slug | required | You can identify a list by its slug instead of its numerical id. If you decide to do so, note that you'll also have to specify the list owner using the _owner\_id_ or _owner\_screen\_name_ parameters. |     |     |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`POST https://api.twitter.com/1.1/lists/destroy.json?owner_screen_name=kurrik&slug=goonies`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

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

POST lists/members/create

post-lists-members-create

POST lists/members/create
=========================

Add a member to a list. The authenticated user must own the list to be able to add members to it. Note that lists cannot have more than 5,000 members.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/lists/members/create.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| list\_id | required | The numerical _id_ of the list. |     |     |
| slug | required | You can identify a list by its slug instead of its numerical id. If you decide to do so, note that you'll also have to specify the list owner using the _owner\_id_ or _owner\_screen\_name_ parameters. |     |     |
| user\_id | required | The ID of the user for whom to return results. Helpful for disambiguating when a valid user ID is also a valid screen name. |     |     |
| screen\_name | required | The screen name of the user for whom to return results. Helpful for disambiguating when a valid screen name is also a user ID. |     |     |
| owner\_screen\_name | optional | The screen name of the user who owns the list being requested by a _slug_. |     |     |
| owner\_id | optional | The user ID of the user who owns the list being requested by a _slug_. |     |     |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`POST https://api.twitter.com/1.1/lists/members/create.json?slug=team&owner_screen_name=twitter&screen_name=kurrik`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

POST lists/members/create\_all

post-lists-members-create\_all

POST lists/members/create\_all
==============================

Adds multiple members to a list, by specifying a comma-separated list of member ids or screen names. The authenticated user must own the list to be able to add members to it. Note that lists can't have more than 5,000 members, and you are limited to adding up to 100 members to a list at a time with this method.

Please note that there can be issues with lists that rapidly remove and add memberships. Take care when using these methods such that you are not too rapidly switching between removals and adds on the same list.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/lists/members/create_all.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| list\_id | required | The numerical _id_ of the list. |     |     |
| slug | required | You can identify a list by its slug instead of its numerical id. If you decide to do so, note that you'll also have to specify the list owner using the _owner\_id_ or _owner\_screen\_name_ parameters. |     |     |
| user\_id | optional | A comma separated list of user IDs, up to 100 are allowed in a single request. |     |     |
| screen\_name | optional | A comma separated list of screen names, up to 100 are allowed in a single request. |     |     |
| owner\_screen\_name | optional | The screen name of the user who owns the list being requested by a _slug_ . |     |     |
| owner\_id | optional | The user ID of the user who owns the list being requested by a _slug_ . |     |     |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`POST https://api.twitter.com/1.1/lists/members/create_all.json?screen_name=rsarver,episod,jasoncosta,theseancook,kurrik,froginthevalley&list_id=23`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

POST lists/members/destroy

post-lists-members-destroy

POST lists/members/destroy
==========================

Removes the specified member from the list. The authenticated user must be the list's owner to remove members from the list.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/lists/members/destroy.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| list\_id | optional | The numerical _id_ of the list. |     |     |
| slug | optional | You can identify a list by its slug instead of its numerical id. If you decide to do so, note that you'll also have to specify the list owner using the _owner\_id_ or _owner\_screen\_name_ parameters. |     |     |
| user\_id | optional | The ID of the user to remove from the list. Helpful for disambiguating when a valid user ID is also a valid screen name. |     |     |
| screen\_name | optional | The screen name of the user for whom to remove from the list. Helpful for disambiguating when a valid screen name is also a user ID. |     |     |
| owner\_screen\_name | optional | The screen name of the user who owns the list being requested by a _slug_ . |     |     |
| owner\_id | optional | The user ID of the user who owns the list being requested by a _slug_ . |     |     |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`POST https://api.twitter.com/1.1/lists/members/destroy?screen_name=episod&slug=cool_people&owner_screen_name=twitter`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

POST lists/members/destroy\_all

post-lists-members-destroy\_all

POST lists/members/destroy\_all
===============================

Removes multiple members from a list, by specifying a comma-separated list of member ids or screen names. The authenticated user must own the list to be able to remove members from it. Note that lists can't have more than 500 members, and you are limited to removing up to 100 members to a list at a time with this method.

Please note that there can be issues with lists that rapidly remove and add memberships. Take care when using these methods such that you are not too rapidly switching between removals and adds on the same list.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/lists/members/destroy_all.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| list\_id | required | The numerical _id_ of the list. |     |     |
| slug | required | You can identify a list by its slug instead of its numerical id. If you decide to do so, note that you'll also have to specify the list owner using the _owner\_id_ or _owner\_screen\_name_ parameters. |     |     |
| user\_id | optional | A comma separated list of user IDs, up to 100 are allowed in a single request. |     |     |
| screen\_name | optional | A comma separated list of screen names, up to 100 are allowed in a single request. |     |     |
| owner\_screen\_name | optional | The screen name of the user who owns the list being requested by a _slug_ . |     |     |
| owner\_id | optional | The user ID of the user who owns the list being requested by a _slug_ . |     |     |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`POST https://api.twitter.com/1.1/lists/members/destroy_all.json?screen_name=rsarver,episod,jasoncosta,theseancook,kurrik,froginthevalley&list_id=23`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

POST lists/subscribers/create

post-lists-subscribers-create

POST lists/subscribers/create
=============================

Subscribes the authenticated user to the specified list.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/lists/subscribers/create.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| owner\_screen\_name | optional | The screen name of the user who owns the list being requested by a _slug_ . |     |     |
| owner\_id | optional | The user ID of the user who owns the list being requested by a _slug_ . |     |     |
| list\_id | required | The numerical _id_ of the list. |     |     |
| slug | required | You can identify a list by its slug instead of its numerical id. If you decide to do so, note that you'll also have to specify the list owner using the _owner\_id_ or _owner\_screen\_name_ parameters. |     |     |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`POST https://api.twitter.com/1.1/lists/subscribers/create.json?slug=team&owner_screen_name=twitter`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    {
       "created_at":"Wed Sep 23 01:18:01 +0000 2009",
       "slug":"team",
       "name":"Team",
       "full_name":"@twitter/team",
       "description":"",
       "mode":"public",
       "following":false,
       "user":{
          "geo_enabled":true,
          "profile_background_color":"ACDED6",
          "protected":false,
          "profile_background_tile":false,
          "created_at":"Tue Feb 20 14:35:54 +0000 2007",
          "profile_image_url_https":"https://si0.twimg.com/profile_images/1124040897/at-twitter_normal.png",
          "name":"Twitter",
          "favourites_count":16,
          "profile_sidebar_fill_color":"F6F6F6",
          "default_profile_image":false,
          "notifications":false,
          "utc_offset":-28800,
          "description":"Always wondering what's happening. ",
          "display_url":null,
          "deactivated_bit":false,
          "statuses_count":1218,
          "following":false,
          "verified":true,
          "profile_sidebar_border_color":"EEEEEE",
          "followers_count":6619949,
          "profile_image_url":"http://a0.twimg.com/profile_images/1124040897/at-twitter_normal.png",
          "contributors_enabled":true,
          "follow_request_sent":false,
          "profile_use_background_image":true,
          "location":"San Francisco, CA",
          "id_str":"783214",
          "is_translator":false,
          "show_all_inline_media":true,
          "profile_text_color":"333333",
          "screen_name":"twitter",
          "profile_background_image_url":"http://a1.twimg.com/images/themes/theme18/bg.gif",
          "url":"http://blog.twitter.com/",
          "expanded_url":null,
          "default_profile":false,
          "profile_background_image_url_https":"https://si0.twimg.com/images/themes/theme18/bg.gif",
          "time_zone":"Pacific Time (US & Canada)",
          "profile_link_color":"038543",
          "id":783214,
          "entities":{
             "urls":[
    
             ],
             "user_mentions":[
    
             ],
             "hashtags":[
    
             ]
          },
          "suspended":false,
          "listed_count":66018,
          "lang":"en",
          "friends_count":695
       },
       "member_count":643,
       "id_str":"574",
       "subscriber_count":76779,
       "id":574,
       "uri":"/twitter/team"
    }

POST lists/subscribers/destroy

post-lists-subscribers-destroy

POST lists/subscribers/destroy
==============================

Unsubscribes the authenticated user from the specified list.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/lists/subscribers/destroy.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| list\_id | required | The numerical _id_ of the list. |     |     |
| slug | required | You can identify a list by its slug instead of its numerical id. If you decide to do so, note that you'll also have to specify the list owner using the _owner\_id_ or _owner\_screen\_name_ parameters. |     |     |
| owner\_screen\_name | optional | The screen name of the user who owns the list being requested by a _slug_ . |     |     |
| owner\_id | optional | The user ID of the user who owns the list being requested by a _slug_ . |     |     |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`POST https://api.twitter.com/1.1/lists/subscribers/destroy.json?slug=team&owner_screen_name=twitterapi`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

POST lists/update

post-lists-update

POST lists/update
=================

Updates the specified list. The authenticated user must own the list to be able to update it.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/lists/update.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| list\_id | required | The numerical _id_ of the list. |     |     |
| slug | required | You can identify a list by its slug instead of its numerical id. If you decide to do so, note that you'll also have to specify the list owner using the _owner\_id_ or _owner\_screen\_name_ parameters. |     |     |
| name | optional | The name for the list. |     |     |
| mode | optional | Whether your list is public or private. Values can be _public_ or _private_ . If no mode is specified the list will be public. |     |     |
| description | optional | The description to give the list. |     |     |
| owner\_screen\_name | optional | The screen name of the user who owns the list being requested by a _slug_ . |     |     |
| owner\_id | optional | The user ID of the user who owns the list being requested by a _slug_ . |     |     |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`POST https://api.twitter.com/1.1/lists/update.json?list_id=1234&mode=public&name=Party%20Time`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

User profile images and banners

Profile images[](#profile-images "Permalink to this headline")  

-----------------------------------------------------------------

Profile images (also known as avatars) are an important component of a Twitter account’s expression of identity. Use [POST account/update\_profile\_image](https://developer.twitter.com/content/developer-twitter/en/docs/accounts-and-users/manage-account-settings/api-reference/post-account-update_profile_image) to upload a profile image on behalf of a user.  
 

### Alternative image sizes for user profile images[¶](#alternative-image-sizes-for-user-profile-images "Permalink to this headline")

Obtain a user’s most recent profile image, along with the other components comprising their identity on Twitter, from [GET users/show](https://developer.twitter.com/content/developer-twitter/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-show). The [user object](https://developer.twitter.com/content/developer-twitter/en/docs/tweets/data-dictionary/overview/user-object) contains the `profile_image_url` and `profile_image_url_https` fields. These fields will contain the resized “normal” variant of the user’s uploaded image. This “normal” variant is typically 48px by 48px.

By modifying the URL, it is possible to retrieve other variant sizings such as “bigger”, “mini”, and “original”. Consult the table below for more examples:

|     |     |     |
| --- | --- | --- |
| Variant | Dimensions | Example URL |
| normal | 48x48 | http://pbs.twimg.com/profile\_images/2284174872/7df3h38zabcvjylnyfe3\_normal.png https://pbs.twimg.com/profile\_images/2284174872/7df3h38zabcvjylnyfe3\_normal.png |
| bigger | 73x73 | http://pbs.twimg.com/profile\_images/2284174872/7df3h38zabcvjylnyfe3\_bigger.png https://pbs.twimg.com/profile\_images/2284174872/7df3h38zabcvjylnyfe3\_bigger.png |
| mini | 24x24 | http://pbs.twimg.com/profile\_images/2284174872/7df3h38zabcvjylnyfe3\_mini.png https://pbs.twimg.com/profile\_images/2284174872/7df3h38zabcvjylnyfe3\_mini.png |
| original | original | http://pbs.twimg.com/profile\_images/2284174872/7df3h38zabcvjylnyfe3.png https://pbs.twimg.com/profile\_images/2284174872/7df3h38zabcvjylnyfe3.png  <br>_Omit the underscore and variant to retrieve the original image. The images can be very large._ |

### Default profile images[¶](#default-profile-images "Permalink to this headline")

Some users may not have uploaded a profile image. Users who have not uploaded a profile image can be identified by the `default_profile_image` field of their user object having a `true` value.

The `profile_image_url` and `profile_image_url_https` URLs provided for users in this case will indicate Twitter’s default profile photo, which is [https://abs.twimg.com/sticky/default\_profile\_images/default\_profile\_normal.png](https://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png).

The table above can be used to determine how to retrieve different size variants of the default image.  
 

### Outdated profile images[¶](#outdated-profile-images "Permalink to this headline")

If a 403 or 404 error is returned when trying to access a profile image, refresh the [user object](https://developer.twitter.com/content/developer-twitter/en/docs/tweets/data-dictionary/overview/user-object) using [GET users/show](https://developer.twitter.com/content/developer-twitter/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-show) to retrieve the most recent `profile_image_url` or `profile_image_url_https`. The URL may have changed, which happens for instance when the user updates their profile image.  
 

Profile banners[¶](#profile-banners "Permalink to this headline")
-----------------------------------------------------------------

Profile banners allow users to further customize the expressiveness of their profiles. Use [POST account/update\_profile\_banner](https://developer.twitter.com/content/developer-twitter/en/docs/accounts-and-users/manage-account-settings/api-reference/post-account-update_profile_banner) to upload a profile banner on behalf of a user.

Profile banners come in a variety of display-enhanced sizes. The variant sizes are available through a request to [GET users/profile\_banner](https://developer.twitter.com/content/developer-twitter/en/docs/accounts-and-users/manage-account-settings/api-reference/get-users-profile_banner) or by modifying the final path component of the `profile_banner_url` found in a user object according to the table below.

The profile banner data available at each size variant’s URL is in PNG format.

The following sizes are available:

|     |     |
| --- | --- |
| Dimensions | Example URL |
| 1500x500 | https://pbs.twimg.com/profile\_banners/6253282/1431474710/1500x500 |
| 600x200 | https://pbs.twimg.com/profile\_banners/6253282/1431474710/600x200 |
| 300x100 | https://pbs.twimg.com/profile\_banners/6253282/1431474710/300x100 |

The following sizes are available for the certain screen types:

|     |     |     |
| --- | --- | --- |
| Screen Type | Dimensions | Example URL |
| web | 520x260 | https://pbs.twimg.com/profile\_banners/6253282/1431474710/web |
| web\_retina | 1040x520 | https://pbs.twimg.com/profile\_banners/6253282/1431474710/web\_retina |
| ipad | 626x313 | https://pbs.twimg.com/profile\_banners/6253282/1431474710/ipad |
| ipad\_retina | 1252x626 | https://pbs.twimg.com/profile\_banners/6253282/1431474710/ipad\_retina |
| mobile | 320x160 | https://pbs.twimg.com/profile\_banners/6253282/1431474710/mobile |
| mobile\_retina | 640x320 | https://pbs.twimg.com/profile\_banners/6253282/1431474710/mobile\_retina |