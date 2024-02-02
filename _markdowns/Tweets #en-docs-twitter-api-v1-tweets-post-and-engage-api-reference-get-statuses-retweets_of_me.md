<div>

::: c01-rich-text-editor
Returns the most recent Tweets authored by the authenticating user that
have been retweeted by others. This timeline is a subset of the user\'s
[GET statuses /
user_timeline](/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline)
.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/statuses/retweets_of_me.json `

  -------------------------------------- -------------------------
  Response formats                       JSON
  Requires authentication?               Yes (user context only)
  Rate limited?                          Yes
  Requests / 15-min window (user auth)   75
  -------------------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

+-------------+-------------+-------------+-------------+-------------+
| Name        | Required    | Description | Default     | Example     |
|             |             |             | Value       |             |
+-------------+-------------+-------------+-------------+-------------+
| count       | optional    | Specifies   |             | *5*         |
|             |             | the number  |             |             |
|             |             | of records  |             |             |
|             |             | to          |             |             |
|             |             | retrieve.   |             |             |
|             |             | Must be     |             |             |
|             |             | less than   |             |             |
|             |             | or equal to |             |             |
|             |             | 100. If     |             |             |
|             |             | omitted, 20 |             |             |
|             |             | will be     |             |             |
|             |             | assumed.    |             |             |
+-------------+-------------+-------------+-------------+-------------+
| since_id    | optional    | Returns     |             | *12345*     |
|             |             | results     |             |             |
|             |             | with an ID  |             |             |
|             |             | greater     |             |             |
|             |             | than (that  |             |             |
|             |             | is, more    |             |             |
|             |             | recent      |             |             |
|             |             | than) the   |             |             |
|             |             | specified   |             |             |
|             |             | ID. There   |             |             |
|             |             | are limits  |             |             |
|             |             | to the      |             |             |
|             |             | number of   |             |             |
|             |             | Tweets      |             |             |
|             |             | which can   |             |             |
|             |             | be accessed |             |             |
|             |             | through the |             |             |
|             |             | API. If the |             |             |
|             |             | limit of    |             |             |
|             |             | Tweets has  |             |             |
|             |             | occured     |             |             |
|             |             | since the   |             |             |
|             |             | since_id,   |             |             |
|             |             | the         |             |             |
|             |             | since_id    |             |             |
|             |             | will be     |             |             |
|             |             | forced to   |             |             |
|             |             | the oldest  |             |             |
|             |             | ID          |             |             |
|             |             | available.  |             |             |
+-------------+-------------+-------------+-------------+-------------+
| max_id      | optional    | Returns     |             | *54321*     |
|             |             | results     |             |             |
|             |             | with an ID  |             |             |
|             |             | less than   |             |             |
|             |             | (that is,   |             |             |
|             |             | older than) |             |             |
|             |             | or equal to |             |             |
|             |             | the         |             |             |
|             |             | specified   |             |             |
|             |             | ID.         |             |             |
+-------------+-------------+-------------+-------------+-------------+
| trim_user   | optional    | When set to |             | *true*      |
|             |             | either      |             |             |
|             |             | *true* ,    |             |             |
|             |             | *t* or *1*  |             |             |
|             |             | , each      |             |             |
|             |             | tweet       |             |             |
|             |             | returned in |             |             |
|             |             | a timeline  |             |             |
|             |             | will        |             |             |
|             |             | include a   |             |             |
|             |             | user object |             |             |
|             |             | including   |             |             |
|             |             | only the    |             |             |
|             |             | status      |             |             |
|             |             | authors     |             |             |
|             |             | numerical   |             |             |
|             |             | ID. Omit    |             |             |
|             |             | this        |             |             |
|             |             | parameter   |             |             |
|             |             | to receive  |             |             |
|             |             | the         |             |             |
|             |             | complete    |             |             |
|             |             | user        |             |             |
|             |             | object.     |             |             |
+-------------+-------------+-------------+-------------+-------------+
| inclu       | optional    | The tweet   |             | *false*     |
| de_entities |             | *entities*  |             |             |
|             |             | node will   |             |             |
|             |             | not be      |             |             |
|             |             | included    |             |             |
|             |             | when set to |             |             |
|             |             | *false* .   |             |             |
+-------------+-------------+-------------+-------------+-------------+
| include_us  | optional    | The user    |             | *false*     |
| er_entities |             | *entities*  |             |             |
|             |             | node will   |             |             |
|             |             | not be      |             |             |
|             |             | included    |             |             |
|             |             | when set to |             |             |
|             |             | *false* .   |             |             |
+-------------+-------------+-------------+-------------+-------------+
| in          | optional    | Must be set |             | *true*      |
| clude_ext_e |             | to true in  |             |             |
| dit_control |             | order to    |             |             |
|             |             | return      |             |             |
|             |             | edited      |             |             |
|             |             | Tweet       |             |             |
|             |             | metadata as |             |             |
|             |             | part of the |             |             |
|             |             | Tweet       |             |             |
|             |             | object.     |             |             |
|             |             |             |             |             |
|             |             | ` include_e |             |             |
|             |             | xt_edit_con |             |             |
|             |             | trol=true ` |             |             |
|             |             |             |             |             |
|             |             | Note that   |             |             |
|             |             | historical  |             |             |
|             |             | Tweets may  |             |             |
|             |             | not contain |             |             |
|             |             | edited      |             |             |
|             |             | Tweet       |             |             |
|             |             | metadata.   |             |             |
+-------------+-------------+-------------+-------------+-------------+

## Example Request [¶](#example-request){.headerlink}

` GET https://api.twitter.com/1.1/statuses/retweets_of_me.json?count=50&since_id=259320959964680190&max_id=259320959964680500 `

## Example Response [¶](#example-response){.headerlink}

    [
      {
        "created_at": "Thu Nov 29 17:13:16 +0000 2018",
        "id": 1068191175616720896,
        "id_str": "1068191175616720896",
        "text": "@TwitterDev is the source of Twitter Developer news",
        "truncated": false,
        "entities": {
          "hashtags": [],
          "symbols": [],
          "user_mentions": [
            {
              "screen_name": "twitterdev",
              "name": "twitterdev",
              "id": 2244994945,
              "id_str": "2244994945",
              "indices": [
                0,
                10
              ]
            }
          ],
          "urls": []
        },
      "source": "<a href="http://twitter.com" rel="nofollow">Twitter Web Client</a>",
        "in_reply_to_status_id": null,
        "in_reply_to_status_id_str": null,
        "in_reply_to_user_id": 2244994945,
        "in_reply_to_user_id_str": "2244994945",
        "in_reply_to_screen_name": "twitterdev",
        "user": {
          "id": 10183220897015316771,
          "id_str": "10183220897015316771",
          "name": "test account",
          "screen_name": "testuser",
          "location": "USA",
          "description": "",
          "url": null,
          "entities": {
            "description": {
              "urls": []
            }
          },
          "protected": false,
          "followers_count": 3,
          "friends_count": 11,
          "listed_count": 0,
          "created_at": "Sun May 15 02:31:20 +0000 2019",
          "favourites_count": 33,
          "utc_offset": null,
          "time_zone": null,
          "geo_enabled": null,
          "verified": false,
          "statuses_count": 164,
          "lang": "null",
          "contributors_enabled": null,
          "is_translator": null,
          "is_translation_enabled": null,
          "profile_background_color": "null",
          "profile_background_image_url": null,
          "profile_background_image_url_https": null,
          "profile_background_tile": null,
          "profile_image_url": "null",
          "profile_image_url_https": "https://pbs.twimg.com/profile_images/1099410185435734016/G0hE-4u9_normal.jpg",
          "profile_banner_url": "https://pbs.twimg.com/profile_banners/1018322089701531651/1539492123",
          "profile_link_color": "null",
          "profile_sidebar_border_color": "null",
          "profile_sidebar_fill_color": "null",
          "profile_text_color": "null",
          "profile_use_background_image": null,
          "has_extended_profile": null,
          "default_profile": true,
          "default_profile_image": false,
          "following": null,
          "follow_request_sent": null,
          "notifications": null,
          "translator_type": "null"
        },
        "geo": null,
        "coordinates": null,
        "place": null,
        "contributors": null,
        "is_quote_status": false,
        "retweet_count": 1,
        "favorite_count": 1,
        "favorited": true,
        "retweeted": true,
        "lang": "en"
      }
    ]
:::

</div>
