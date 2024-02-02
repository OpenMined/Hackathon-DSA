<div>

::: c01-rich-text-editor
Returns an HTTP 200 OK response code and a representation of the
requesting user if authentication was successful; returns a 401 status
code and an error message if not. Use this method to test if supplied
user credentials are valid.

## Request a User\'s Email Address [¶](#request-a-user-s-email-address){.headerlink} {#request-a-user-s-email-address}

The \"Request email addresses from users\" checkbox is available under
the app permissions on
[developer.twitter.com](https://developer.twitter.com/en/docs/basics/developer-portal/guides/apps)
. Privacy Policy URL and Terms of Service URL fields must be completed
in the app settings in order for email address access to function. If
enabled, users will be informed via the
[oauth/authorize](/oauth/reference/get/oauth/authorize) dialog that your
app can access their email address.

**Please note** - Your app will need to regenerate the user access
tokens for previously authenticated users to access their email address.

**Please note** - You can view and edit your existing [Twitter
apps](https://developer.twitter.com/en/docs/basics/developer-portal/guides/apps)
via the [Twitter app dashboard](https://developer.twitter.com/en/apps)
if you are logged into your Twitter account on developer.twitter.com.

## Resource URL [¶](#resource-url){.headerlink}

<https://api.twitter.com/1.1/account/verify_credentials.json>

  -------------------------------------- -------------------------
  Response formats                       JSON
  Requires authentication?               Yes (user context only)
  Rate limited?                          Yes
  Requests / 15-min window (user auth)   75
  -------------------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

  ------------------ ---------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------
  Name               Required   Description                                                                                                                                                                                               Example
  include_entities   optional   The *entities* node will not be included when set to *false* .                                                                                                                                            *false*
  skip_status        optional   When set to either *true* , *t* or *1* statuses will not be included in the returned user object.                                                                                                         *true*
  include_email      optional   When set to *true* email will be returned in the user objects as a string. If the user does not have an email address on their account, or if the email address is not verified, null will be returned.   *true*
  ------------------ ---------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------

## Example Request [¶](#example-request){.headerlink}

[ GET <https://api.twitter.com/1.1/account/verify_credentials.json>
]{.title-ref}

## Example Response [¶](#example-response){.headerlink}

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
:::

</div>
